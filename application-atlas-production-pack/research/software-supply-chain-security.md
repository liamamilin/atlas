# Research Notes — Software Supply Chain Security

Research date: 2026-09-09
Slug: software-supply-chain-security
Directory leaf: Software Supply Chain Security (§15 Cybersecurity, Identity & Trust)

## Research Goal

Understand what "Software Supply Chain Security" (SSCS) products actually are and do, from official product documentation — not from marketing category language. The market uses "software supply chain security" loosely (often as a rebrand of SCA); this pass must determine whether the leaf is a real, distinct Application Type, and if so what its minimal defining structure is, how it differs from the many adjacent security/engineering Types, and where its boundary with Software Composition Analysis (SCA, a pending sibling leaf) sits.

## Initial Boundary (working hypothesis before research)

- Hypothesis: SSCS products protect the organization from threats that arrive *through the software it consumes* (open-source packages, images, models, vendor software) and secure *the path its own software takes* from source to distribution. The threat model is an adversarial supplier (malicious package, tampered artifact, hijacked maintainer, build injection), not merely a buggy component.
- Nearest neighbors: SCA (pending sibling), SBOM Management (processed), Secrets Security (processed), Application Security Platform (processed), Container & Kubernetes Security (processed), Artifact Repository (processed), Package Registry (processed), Dependency Management Application (processed), Continuous Integration Platform (processed), Vulnerability Management (pending), Software Delivery Governance Platform (pending).
- Known risk: the leaf could be an umbrella/alias of SCA rather than its own Type. This pass must resolve or explicitly flag that.

## Research Questions

1. What is the managed object domain — packages? artifacts? vendor software? SBOMs? applications?
2. What threat model do the products encode (malicious code, typosquatting, hijacked maintainers, build tampering, dependency confusion, new-package risk)?
3. Where do trust decisions happen and how are they enforced (registry proxy/repository, install-time wrapper, CI gate, PR check, release verification)?
4. What verdict/evidence structure do products produce (classifications, behaviors, attack vectors, identity verification)?
5. What is the record structure (quarantine records, event logs, audit, dashboards)?
6. How does SCA-class capability (CVE matching, license compliance) sit inside these products — central or bundled?
7. Is there a distinct output-integrity leg (release verification, provenance), and how is it realized?
8. What rules matter (fail-open vs fail-closed, waiver/allow-list mechanics, transitive-dependency coverage)?
9. Who uses it and through which surfaces?
10. What would make a product NOT this Type (boundary tests)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Sonatype (Repository Firewall + Lifecycle/IQ Server) | repository/proxy-anchored admission control + policy engine; the incumbent | enterprise |
| Socket | developer-first behavioral malicious-package detection + install-time firewall | dev teams → enterprise |
| ReversingLabs Spectra Assure | deep binary/malware analysis; publisher-side release verification + third-party adoption verification | enterprise / PSIRT / publishers |
| Endor Labs | unified platform (SCA+SAST+secrets+containers) with reachability + Package Firewall module | enterprise dev |

Rejected/considered: JFrog Curation (registry-anchored curation; overlaps Sonatype pole), Chainguard (curated-supply substitution pole), Scribe Security (provenance-attestation pole — unreachable, see Sources), GitHub platform-native features (dependency review, artifact attestations — docs URLs 404'd in this environment).

## Sources

All fetched 2026-09-09 from official vendor documentation.

- Socket: https://docs.socket.dev/ (hub), https://docs.socket.dev/docs/socket-firewall-overview, https://docs.socket.dev/llms.txt (full docs index: alert categories, policies, cool-down policy, threat feed, SBOM export, CLI/GitHub/VS Code surfaces)
- Sonatype: https://help.sonatype.com/en/ (hub), https://help.sonatype.com/en/firewall-quarantine.html, https://help.sonatype.com/en/firewall-malware.html, https://help.sonatype.com/en/policy-concepts.html, https://help.sonatype.com/en/firewall-product-information.html
- ReversingLabs: https://docs.reversinglabs.com/ (hub), https://docs.secure.software/ (Spectra Assure hub), https://docs.secure.software/concepts/basic-concepts (glossary)
- Endor Labs: https://docs.endorlabs.com/ (hub), https://docs.endorlabs.com/package-firewall/

Source-access limitations:

- **Scribe Security unreachable** (docs.scribesecurity.com, docs.scribesecurity.com/docs/intro/, scribesecurity.com all failed with transport errors/404). The provenance-attestation-generation pole is therefore under-evidenced in this sample; claims about it are kept weak (see Uncertainties).
- **GitHub artifact-attestations docs 404** (two URL attempts). Platform-native attestation features are treated as market context only, no precise claims.
- Sonatype help pages embed very large navigation; page bodies were extracted from saved fetch output. Content used is limited to what was actually retrieved.

## Product A — Sonatype (Repository Firewall + Lifecycle / IQ Server)

Evidence layer: A (directly observed, official help center).

### Key observations

- **Product composition**: "Sonatype Repository Firewall requires both IQ Server and Nexus Repository" — the firewall is a layer that rides on the organization's repository manager (proxy repositories). (firewall-product-information.html)
- **Quarantine mechanics** (firewall-quarantine.html):
  - "When a requested component violates your open-source policy, the component is put into quarantine while returning an error message and linking the component details to the requester. While the component remains quarantined in the proxy repository, it may not be downloaded through that proxy repository."
  - "The Repository Firewall is used to quarantine components that are found too risky to allow in your development pipeline without going through a security review."
  - Security team reviews violations of quarantined components from the **Firewall Dashboard**; waivers release components; components are "automatically released from quarantine when the failing violations are no longer open."
  - Policy action `FAIL` at the `PROXY` stage triggers quarantine; changing policy actions requires Policy Administrator/Owner roles.
  - "Repository Firewall only quarantines newly requested components. Components already found in the proxy repository are audited but not quarantined" — to avoid disrupting the build pipeline.
  - **Fail-closed**: "When the Repository Firewall service is unavailable and quarantine enabled, requests for new components are immediately placed in quarantine until they are evaluated and released."
  - Time-based waivers: once expired, the component "will again trigger the violation. However, since it is already in the repository, it will not be quarantined."
  - Client quirks: NuGet quarantine returns 409 (clients hardcode 403 as auth failure); Pub returns 451. (L3 detail)
- **Malware Insights dashboard** (firewall-malware.html): "visibility into malware that Sonatype Firewall detects and blocks... malware frequency, severity, classification, and where threats are entering your environment." Threat types include "Data corruption, Backdoor, Potentially unwanted application, or Other"; charts by severity, attack vector, threat type, component format; metrics include Hugging Face models and container images evaluated for malware; Malware Events table with per-detection detail.
- **Policy engine** (policy-concepts.html):
  - Lifecycle described as a "Policy Engine": "a policy is a rule for how to act when certain constraints are met" (component age, CVSS score, license obligations).
  - Four risk categories: **Security, License, Quality, Other**.
  - Actions on violation: "warn the user, block/fail the build, or just record this information in a report"; each policy has a **threat score**.
  - Policies scoped by company/organization/application/category; **SDLC stages** for enforcement: **Proxy** ("enforces policy when components enter your repository manager" — the Firewall stage), Develop, Source, Build, Stage release, Release, Operate, Compliance.
  - Reference policies as base templates; **waivers** as the exception path ("If a team needs a component that violates the set policies, they can request a waiver").
- Related surface: "Sonatype Malware Data" and "Threats in AI/ML Models" doc sections exist (malware/AI-model intelligence); "Repository Firewall Hashing" and "Firewall Audit and Quarantine Capability" pages exist in the nav.

## Product B — Socket

Evidence layer: A (directly observed, official docs).

### Key observations

- **Positioning**: "Socket is a developer-first security platform that protects your most critical apps from software supply chain attacks." Hub: "Socket fights vulnerabilities and provides visibility, defense-in-depth, and proactive supply chain protection for your open source dependencies."
- **Socket Firewall** (socket-firewall-overview.html):
  - "acts as an intelligent proxy between your package managers and package registries"; intercepts install requests, "checks packages against Socket's security intelligence", "blocks malicious packages at any dependency depth, including transitive dependencies."
  - Architecture: HTTP/HTTPS proxy; extracts package metadata (name, version, registry); queries Socket security API against org policy; allows or blocks with informative error.
  - Enterprise variant: org-wide policy enforcement, visibility into what is installed across the org, configurable handling of "AI-detected malware, unscanned packages, packages with CVEs, and other threats", private registry support, **allow-list capabilities** to override blocking, dashboard integration, telemetry controls, chained proxy support. Deployment modes: **registry mode** (persistent service as registry interface) and **wrapper mode** (command prefix, e.g. `sfw npm install`).
  - Free variant: zero-config, blocks confirmed malicious packages, "warns on AI-detected threats", public registries only.
- **Alert taxonomy** (docs index): package issues categorized as **Supply Chain Risk, Vulnerability, Quality, Maintenance, License**; alert actions error|warn|monitor|ignore; alert triage/resolution machinery; package scores.
- **Supply-chain-specific controls**: **Cool-down policy (recently published packages)** — risk control on newly published packages; **Threat Feed / threat campaigns** (Enterprise add-on): "paginated list of supply chain attack campaigns" with per-campaign package lists.
- **Reachability analysis** (SCA with reachability; dependency/precomputed/full-application/static reachability pages) — prioritization capability.
- **Surfaces**: Socket for GitHub (PR checks, branch protection as required check), CLI (`socket scan`, `socket package`, `socket threat-feed`, `socket optimize` with @socketregistry overrides — curated dependency replacement), VS Code extension, Chrome extension, MCP, CI integrations (GitLab/Bitbucket/Jenkins/Azure), Slack/Jira/Linear/ClickUp/Asana integrations, SSO/SCIM, audit log.
- **SBOM**: full scans produce SBOM artifacts; export as SPDX / CycloneDX / OpenVEX (Beta endpoints).

## Product C — ReversingLabs Spectra Assure

Evidence layer: A (directly observed, official docs).

### Key observations

- **Positioning** (docs.reversinglabs.com hub): "Protects software supply chains by analyzing compiled software packages, components and third-party dependencies to detect exposures and eliminate threats before reaching production." Glossary: "a software supply chain security platform that can protect your development lifecycle from software supply chain threats"; "inspects software packages before their release, deployment, or adoption by an organization."
- **Product set**: CLI (scan packages on-prem and in CI/CD; "Protect your software releases by continuously verifying build artifacts"; policy controls; export reports), Portal (SaaS: "managing software projects and verifying third-party software used in your organization... visibility into deployment risks"), Community (free public risk-assessment catalogue of popular OSS packages; "monitors open source package repositories to identify malware, code tampering and indicators of software supply chain attacks"), Integrations (CI/CD).
- **Threat model — six risk categories ordered by priority** (glossary): **1. Malware, 2. Tampering, 3. Vulnerabilities, 4. Secrets, 5. Hardening, 6. Licenses.** Malware and tampering outrank vulnerabilities — the supply-chain threat model is explicit.
- **Policy → issue → verdict machinery**: "a policy is a set of built-in rules that prescribe how software should behave in order to be considered secure"; policies trigger on files, violations become **issues**; "Every policy automatically sets the priority for its violation (issue) and impacts the final build status (**CI PASS or FAIL**)" — configurable/overridable. Policy IDs: SQ* (software quality), TH* (threat hunting).
- **SAFE report**: unpacks software binaries, extracts metadata, detects supply-chain compromise; contains classification, complete BOM (xBOM = SBOM + SaaSBOM + CBOM + ML-BOM + BOV + VEX), deployment risks by severity/priority, **digital signatures** info, **file behaviors**, URIs; RL-SAFE portable archive + SAFE Viewer.
- **Identity verification** ("verified" glossary entry): multiple methods ordered by significance — SHA-256 mapping, Authentihash, Certificate, Cloud source (reputation zone), Byte pattern (original-hash comparison), Similarity (match against ReversingLabs cloud package inventory), Manifest. I.e., establishing *what this binary is and where it came from* is a first-class capability.
- **Tampering detection**: digital-signature, package-integrity, threat-hunting policy checks; **reproducible build** checks ("a reliable method of detecting build environment tampering, as well as a way of proving that binaries have been compiled from a trusted source code") with a Reproducibility page diffing version artifact vs reproducible-build artifact.
- **"Silent vulnerability"** concept: vulnerabilities hidden by statically linked dependencies, findable only by binary analysis — a capability SCA-by-manifest cannot reach.
- **Explicit self-distinction from SAST and SCA** (glossary): its static analysis "is not the same as SAST because it does not require access to source code"; SCA defined as component identification + license/vulnerability database comparison.

## Product D — Endor Labs

Evidence layer: A (directly observed, official docs).

### Key observations

- **Positioning**: "a unified application security platform... A single platform for SAST, secrets detection, SCA, malicious package detection, Package Firewall, Coding Agent Governance, and container scanning." Workflow: Scan → Triage (reachability + risk scoring) → Remediate.
- **Package Firewall** (package-firewall/):
  - "real-time protection against malicious packages during software installations... Positioned between package manager clients and public registries, it blocks the installation of known malicious packages by default while allowing safe packages to install normally."
  - "checks every package in the dependency tree individually, including transitive dependencies."
  - Deployment models: direct integration, JFrog Artifactory, Google Artifact Registry, Sonatype Nexus Repository, MDM deployment; also blocks malicious **VS Code extension** installations from the Microsoft Marketplace via MDM.
  - Policy actions per condition (malware, vulnerabilities, restricted licenses, minimum package age): **Warn** (record + allow), **Block** (prevent + error), **Allow safe versions only (curate)** — "Removes the unsafe versions from the response so the package manager client installs a safe version instead" (npm/PyPI). Exceptions let specific packages bypass checks. Events recorded in logs with package, version, time, reason.
  - Evaluation: parses ecosystem/name/version, checks against Endor Labs malware database; API-key auth per request.
- **Other capabilities**: reachability analysis ("analyzes your first-party code, software packages, and containers"), Endor scores (metadata-based risk scores for packages and AI models), policies combined with GitHub/GitLab integrations ("choose which risks to block and which to flag as warnings"), AI-model discovery/governance, remediation guidance/automated patching.

## Cross-product Comparison

| Dimension | Sonatype | Socket | ReversingLabs | Endor Labs |
|---|---|---|---|---|
| Managed object | components entering proxy repositories (+ apps in Lifecycle) | packages/dependencies in repos & installs | compiled packages/binaries — third-party AND own releases | packages in dependency trees (+ code/containers/AI models platform-wide) |
| Supply-chain threat evaluation | malware detection + classification (backdoor, data corruption, PUA), attack vectors, quality/age risk | behavioral malicious-package detection (AI + human review), supply-chain risk alerts, cool-down on new packages, threat campaigns | malware + tampering (top-2 risk categories), identity verification (hash/cert/similarity), reproducible-build checks, silent vulnerabilities | malicious package detection vs malware database, minimum package age, Endor scores |
| Known-vuln / license (SCA-class) | yes — one of four risk categories; separate Lifecycle product | yes — Vulnerability + License alert categories; reachability | yes — risk categories 3 and 6 of six | yes — SCA in unified platform |
| Enforcement point | proxy repository (quarantine at entry); policy stages Proxy→Operate | registry-mode proxy, install-time wrapper, PR checks (GitHub app), CI | CI PASS/FAIL gate; release verification before publish; adoption verification (Portal) | registry integrations (Artifactory/Nexus/GAR), direct integration, MDM, CI/PR policy |
| Actions | quarantine / audit / warn / fail build / report; waivers release | block / error / warn / monitor / ignore; allow-lists | CI PASS/FAIL; policy-driven issues; suppression/override | block / warn / curate (serve safe version); exceptions |
| Records | quarantined-component records, Firewall Dashboard, Malware Insights, audit/policy-violation logs | org alerts, scans (full/diff), historical data endpoints, audit log | package store / Portal projects, SAFE reports, Community catalogue | firewall event logs (package/version/reason), scan results |
| Developer surface | error message + link at request time; IDE tools (Develop stage) | PR comments, VS Code, Chrome ext, CLI, MCP | CLI in CI; Portal reports; shareable reports | install-time block/warn messages; PR/CI policy outcomes |
| Threat intel | Sonatype Malware Data; AI/ML model threats | Threat Feed / attack campaigns (Enterprise) | ReversingLabs cloud (goodware/malware corpus, similarity) | Endor Labs malware database; package metadata scores |
| SBOM | SBOM Manager sibling product; Compliance stage | SPDX/CycloneDX/OpenVEX export | xBOM (SBOM/SaaSBOM/CBOM/ML-BOM/BOV/VEX) export | (platform scan results; not emphasized on fetched pages) |
| Distinctive | quarantine + waiver lifecycle on the repository; stage model | developer-first surfaces; cool-down; campaign feed | binary-level analysis without source; publisher-side release verification; identity verification ladder | unified-platform framing; curate action (serve safe version); MDM/VS Code extension scope |

### Cross-product commonalities (Layer B)

1. **The managed object is software crossing the organization's software-intake/release boundaries, identified by ecosystem + name + version** (purl-class identity; Socket and ReversingLabs both document purl). Held as records with evaluation state — not one-off scan output.
2. **Evaluation against the supply-chain threat model beyond CVE matching**: malicious-package detection (all four), tampering/identity/provenance verification (Sonatype hashing, ReversingLabs identity ladder + reproducible builds), new/unknown-package risk (Socket cool-down, Endor minimum package age, Sonatype quality/age risk).
3. **Policy-driven trust decisions with tiered actions and an exception path**: block/quarantine/warn/monitor/allow(/curate) + waivers/allow-lists/exceptions (all four).
4. **Enforcement located at chain boundaries** — where software enters (registry proxy, install time, PR, CI) and, for publishers, where software leaves (release verification). The Sonatype stage model (Proxy→Develop→Source→Build→Stage→Release→Operate) makes the chain-boundary framing explicit.
5. **Recorded, reviewable decisions**: dashboards/logs of quarantines/blocks/events with package/version/reason; security-team review loop with waiver/release.
6. **Vendor threat intelligence as the evaluation substrate**: malware databases/corpora, campaign feeds, similarity/reputation data.
7. **SCA-class capability (CVE + license) commonly bundled but not the distinguishing leg** — it appears as one risk category among several (Sonatype: 1 of 4; ReversingLabs: 2 of 6; Socket: 2 of 5 alert categories; Endor: one module of a unified platform).
8. **Developer-facing surfaces at the moment of decision** (install-time error with details link, PR check, IDE) — common.
9. **SBOM generation/export common** — a byproduct/capability, not the core (SBOM record-keeping is the SBOM Management sibling's core).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

The Type is recognizable only when all three structures are jointly held:

1. **The supply-chain software population as the unit of record** — the third-party software the organization consumes (open-source packages/libraries, container images, AI models, vendor software) and/or the software artifacts it releases, held as persistent identified records (ecosystem/name/version identity) carrying their trust/evaluation state.
   - Remove → point-in-time scan output (SCA run) or a bare policy engine with nothing to govern.
2. **Supply-chain threat evaluation** — the platform renders trust verdicts on that software against the adversarial-supplier threat model: malicious code, tampering, untrusted or unknown origin/provenance — beyond known-vulnerability matching — with evidence attached to the verdict.
   - Remove → vulnerability/license matching over a dependency list = SCA territory.
3. **Trust decisions acted on in the software flow** — verdicts drive enforced decisions where software crosses the organization's chain boundaries: inputs admitted/blocked/quarantined/curated at intake points (registry/repository proxy, install time, CI, PR), and/or outputs verified before release/deployment; decisions are recorded and reviewable.
   - Remove → passive analysis/reporting platform (no enforcement, no gate).

Jointly-held load-bearing tests:
- 1 alone = package/component inventory
- 2 without 1 = one-off analysis service
- 3 without 1+2 = policy gate with no supply-chain knowledge
- 1+2 without 3 = analysis/reporting platform (SCA + malware intel, nothing enforced)
- 1+3 without 2 = gate with no threat model (generic blocklist)
- 2+3 without 1 = ephemeral verdicts with no record

### L1 — Common Mature Structure (standard, not definitional)

- SCA-class capability: CVE/vulnerability matching, license compliance over the dependency composition
- SBOM generation/export (SPDX/CycloneDX-class; VEX increasingly)
- Reachability analysis / risk scoring for prioritization
- Vendor threat-intelligence substrate (malware DB, campaign/reputation feeds)
- Developer surfaces: PR checks/comments, IDE extensions, CLI, install-time messages
- Dashboards & event/audit logs; org-level visibility
- Waiver/allow-list/exception management with scoping (repo-, time-based)
- CI/CD integrations and policy gates (PASS/FAIL)
- Enterprise hygiene: SSO/SCIM, RBAC, audit logs

### L2 — Variant / Optional Structure

- Enforcement-point choice: repository/proxy-anchored vs install-time wrapper/proxy vs CI/PR-anchored vs publisher-side release verification (variant axis; products combine several)
- Ecosystem scope: npm/PyPI/Maven/Go/… ; extension to container images, AI/ML models (Hugging Face), VS Code extensions, vendor/commercial software
- Posture: screening/evaluation (dominant) vs curated substitution (serve/rebuild safe versions — @socketregistry overrides observed; Chainguard-class hardened supply as market context)
- Fail-open vs fail-closed when the evaluation service is unavailable (observed both ways — see Rules)
- Customer tier: free individual-developer tooling → team → enterprise policy/telemetry
- Platform-native realization: supply-chain security features embedded in SCM/CI platforms (market context; under-evidenced in this sample)
- Attestation/provenance generation machinery (Sigstore/in-toto/SLSA-class) as an enabler for output verification (market context; under-evidenced in this sample — see Uncertainties)

### L3 — Vendor-specific (research notes only)

- Sonatype: quarantine returns 409 for NuGet / 451 for Pub clients; "Legacy Violations" not enforced by Firewall; Firewall requires IQ Server + Nexus Repository; stage names (Proxy/Develop/Source/Build/Stage release/Release/Operate/Compliance); threat scores; Advanced Legal Pack.
- Socket: `sfw` wrapper syntax; registry-mode config for Artifactory/CodeArtifact/Nexus; Vigil selectors; @socketregistry overrides; quota model (units per API call); batch purl endpoint limits.
- ReversingLabs: SAFE report / RL-SAFE archive / SAFE Viewer; SQ*/TH* policy ID scheme; package store; P0–P4 priority scale; effort estimate formula; Authentihash; Spectra Assure Community catalogue.
- Endor Labs: LicenseBadge SKU gating (EL-OSS-FWAL); Google Artifact Registry Go limitation; curate action limited to npm/PyPI; MDM deployment for VS Code extensions.

## Vendor-specific Findings

- Sonatype's **stage model** is the clearest articulation of chain-boundary enforcement, but the specific stage list is vendor-specific; the canonical concept is "policy enforced at defined points of the software flow."
- ReversingLabs is the only sampled product with a **publisher-side release-verification** posture as a first-class workflow ("continuously verifying build artifacts", reproducible-build diffing) — treat publisher-side verification as a variant pole, not the center.
- Endor's **curate** action (serve a safe version instead of the requested one) is the most aggressive admission action observed; Socket's @socketregistry overrides are a similar substitution idea realized differently. Substitution is a variant, not the definitional action set.
- Socket's **cool-down policy** and Endor's **minimum package age** converge on the same control (distrust freshly published packages) via different mechanisms — cross-product commonality at the concept level, product-specific at the mechanism level.

## Boundary Findings

- **vs Software Composition Analysis / SCA (pending sibling leaf)** — the critical seam. SCA is the *analysis capability* over the composition of the organization's own applications (identify components; match vulnerabilities/licenses). SSCS is the *chain-protection posture*: supply-chain threat evaluation (malware/tampering/provenance) + trust decisions enforced at chain boundaries + records of those decisions. Evidence that these are separable: Socket Firewall Free blocks known-malicious packages with no application composition analysis; ReversingLabs analyzes binaries with no manifest/dependency list at all ("silent vulnerabilities"); Sonatype Firewall quarantines at the proxy independent of any application scan. Conversely, pure SCA (manifest → CVE/license report, no malicious-package evaluation, no enforcement) lacks legs 2–3. SSCS products commonly *bundle* SCA capability (all four sampled) — bundling does not merge the Types. **Seam test: remove malicious/tampering/provenance evaluation and boundary enforcement → what remains is SCA.** Flag for the SCA pass to ratify.
- **vs SBOM Management (processed)** — SBOM Management's record is the SBOM document (composition inventory) with product/release binding and a serve-onward lifecycle. SSCS's record is the trust verdict/decision on software crossing the chain. SSCS products generate/export SBOMs (Socket, ReversingLabs); SBOM Management products consume/enrich/deliver them. Seam: inventory-of-composition vs trust-decision-and-enforcement.
- **vs Application Security Platform (processed)** — ASP's unit of record is the organization-owned *application* with its finding population and triage lifecycle (engine-agnostic). SSCS's unit is the *software crossing the chain* (mostly third-party inputs) with trust verdicts and boundary decisions. SSCS findings can feed an ASP; the ASP does not enforce chain admission.
- **vs Container & Kubernetes Security (processed)** — CKS secures the container estate (images + runtime + cluster config) in container-native terms; SSCS treats images as one input/output class in the software chain (Sonatype evaluates container images for malware; ReversingLabs unpacks containers). Image-scanning overlap exists; the domain framing and object set differ.
- **vs Artifact Repository (processed)** — custody vs trust. SSCS enforcement frequently rides *on* the artifact repository (Sonatype Firewall on Nexus proxy; Endor via Artifactory/Nexus). The repository holds and serves; the SSCS layer decides what may pass.
- **vs Package Registry (processed)** — the public ecosystem venue vs the organization's protection of its consumption from that venue.
- **vs Secrets Security (processed)** — credential-leak detection vs software trust. Overlap: ReversingLabs reports exposed secrets found inside scanned packages (a risk category), but its object is the package, not the credential surface.
- **vs Dependency Management Application (processed)** — project-side declaration/resolution tooling (developer intent) vs trust evaluation of what flows through the chain.
- **vs Continuous Integration Platform (processed)** — CI runs change-bound validation; SSCS gates ride on CI but the SSCS record/verdict/enforcement is not a CI run.
- **vs Vulnerability Management (pending)** — org-wide vulnerability lifecycle vs supply-chain-scoped trust decisions; SSCS verdicts may become VM records.
- **vs Software Delivery Governance Platform (pending)** — governance of the delivery process (approvals/policies across pipelines) vs trust of software crossing chain boundaries; real adjacency, flag for that pass's joint review.
- **"Remove what → becomes another Type" summary**: remove the adversarial threat model + enforcement → SCA; remove the chain framing (keep records) → SBOM Management/component inventory; remove software objects (keep app records) → Application Security Platform; remove trust decisions (keep custody) → Artifact Repository.

## Historical / Market-Sample Check (per §24)

- The Type as a named market category is young — it crystallized after the 2020s supply-chain attack wave (the sampled vendors' own materials reference npm malware campaigns and worm attacks; Sonatype's help center carries advisories for named npm malware campaigns). The definition must therefore be checked against pre-wave ancestors:
  - **2010s license-compliance / SCA scanners**: hold leg 1 (component inventory) but lack the adversarial threat model and boundary enforcement → they sit *below* this Type (they are the SCA ancestor). This confirms the threat model, not any specific machinery, is the invariant.
  - **AV-style scanning of downloaded files**: malware evaluation without the chain framing, records, or boundary decisions → below the Type.
  - **Early policy-engine-over-components products** (pre-malware-detection Lifecycle-era): legs 1+3 with a vulnerability/license/quality-only threat model → historically SCA+governance; the sampled vendors themselves added malware/tampering evaluation, which is what moved the category across the boundary. The definition stays honest: a product with only CVE+license evaluation and a build gate is *not* this Type today.
- Older/regional/platform-native realizations: platform-native dependency admission and attestation features inside SCM/CI platforms satisfy the same three legs with no standalone product — the definition (records + threat evaluation + boundary decisions) holds without naming any vendor machinery.

## Uncertainties

1. **Provenance-attestation-generation pole under-evidenced**: Scribe unreachable (3 attempts), GitHub attestations docs 404 (2 attempts). The output-integrity leg is evidenced only through *verification* (ReversingLabs release verification, reproducible-build checks, identity ladder; Sonatype hash-based evaluation). Claims about attestation *generation* (Sigstore/in-toto/SLSA-class machinery) are kept as market context without precise claims.
2. **Whether the market converges on "SSCS ⊃ SCA" or "SSCS ∥ SCA"**: all four sampled vendors bundle SCA capability inside SSCS-branded offerings, and two of them (Sonatype, Endor) ship SCA as a separately positioned capability/product line. The seam proposed here (threat model + enforcement vs composition analysis) is this pass's inference (Layer C); the SCA pass should ratify.
3. **Fail-open vs fail-closed**: observed fail-closed for Sonatype quarantine and a documented fail-open *option* (`poll=false`) in Socket's API — but Socket's firewall default behavior when the intelligence service is unavailable was not directly documented on fetched pages. The final document states only that products differ on this axis, without claiming a market default.
4. **Curated-supply pole (Chainguard-class)**: not sampled (docs not fetched). Treated as market context; the substitution variant is evidenced only via Socket's @socketregistry overrides and Endor's curate action.
5. **JFrog Curation**: not fetched (time budget). Registry-anchored curation is already doubly evidenced (Sonatype quarantine, Endor via Artifactory); absence does not weaken the core.

## Final Synthesis

Software Supply Chain Security is a real, distinct Application Type — not an alias of SCA. Its defining core is three jointly-held structures: (1) a persistent, identified record population of the software crossing the organization's supply chain — the third-party inputs it consumes and/or the artifacts it releases; (2) trust evaluation of that software against the adversarial-supplier threat model — malicious code, tampering, untrusted or unknown origin — beyond known-vulnerability matching, with evidence attached; (3) trust decisions enforced where the software crosses chain boundaries — admit/block/quarantine/curate at intake, verify at release — recorded and reviewable, with waivers/allow-lists as the exception path. SCA-class vulnerability/license analysis is a common bundled capability, not the defining leg. The Type's realization varies along enforcement point (repository proxy / install time / CI / PR / release), object scope (packages → images → AI models → vendor software), and posture (screening vs curated substitution). The boundary with SCA (threat model + enforcement vs composition analysis) is the single most important seam and is flagged for ratification by the SCA pass.
