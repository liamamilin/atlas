# Research Notes — Secrets Security

## Research Goal

Understand the Application Type behind the directory leaf **Secrets Security** (§15 Cybersecurity, line 1139): what products in this category actually do, what their core structure is, and how they differ from the neighboring custody Types (Secrets Management §14, Password Manager, PAM) and from SAST, which already claims "hardcoded credentials" as one of its detection classes.

This pass also carries three pre-hung seams to ratify:

1. **secrets-management (§14) forward note**: "custody-and-delivery vs leak-detection posture — HashiCorp ships Vault Radar (detection) beside Vault (custody) as separate products; keep-both expected, ratify at that pass."
2. **sast (§15)**: hardcoded credentials documented as one SAST rule class; the seam (dedicated secrets detection vs SAST rule class) must be held.
3. **privileged-access-management-pam / password-manager (§15)**: both recorded seams toward secrets Types; this pass should confirm the scanner posture is distinct from both custody postures.

## Initial Boundary

Working hypothesis before research:

- Secrets Security is **not** a vault. It does not hold secrets as its system of record, mediate their retrieval, or manage their lifecycle as stored objects. That is Secrets Management (§14, processed).
- Secrets Security is the **detection-and-remediation** posture: finding credential material that ended up where it should not be (source code, commit history, wikis, collaboration tools), and driving its revocation/rotation.
- Nearest confusion risks: Secrets Management (custody), SAST (shares the "scan code, emit findings" shape), Vulnerability Management (aggregates findings), DLP (shares "sensitive content" framing).

## Research Questions

1. What exactly do these products scan, and what do they look for?
2. What is the unit of output — a finding, an incident, an alert? What does it carry?
3. What does "remediation" mean here — code fix or credential lifecycle action? (This is the suspected differentiator vs SAST.)
4. Is prevention (blocking at write time) definitional or a deployment mode of detection?
5. Is validity checking (is the secret still live?) definitional or common?
6. What surfaces do products cover beyond git repositories?
7. How do custody vendors position their own detection siblings (Vault vs Vault Radar)?
8. Where does the Type end and SAST / DLP / Vulnerability Management begin?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| GitGuardian | Dedicated commercial secrets-security platform (SaaS + self-hosted); internal + public monitoring; enterprise + dev-first | The category-defining dedicated vendor; richest incident/remediation documentation |
| Truffle Security (TruffleHog) | OSS-first scanner with enterprise line; verification-centric philosophy ("only valid secrets") | The discovery/classification/validation/analysis articulation; strong OSS pole |
| Gitleaks | Minimal open-source engine; rules + scan + report, no platform | The minimal-engine pole; proves what the Type can lack and still be itself |
| GitHub Secret Protection (secret scanning + push protection) | Platform-native, embedded in the code-hosting platform; partner program | The platform-native realization; authoritative remediation wording |
| HashiCorp Vault Radar | Custody vendor's detection sibling beside Vault | The seam product named by the secrets-management pass; ratifies keep-both |

## Sources

All fetched 2026-09-09 (Tier 1 — official operational documentation):

- GitGuardian — docs portal https://docs.gitguardian.com/ ; Secrets Detection home (/secrets-detection/home); Core concepts: What is a secret? (/secrets-detection/core-concepts/what-is-a-secret); Internal Monitoring home (/internal-monitoring/home); Secrets incidents (/internal-monitoring/detect/secrets-incidents); Incident statuses (/internal-monitoring/detect/incident-statuses); Secret Remediation Overview (/internal-monitoring/remediate/remediation-overview)
- Truffle Security — TruffleHog docs https://docs.trufflesecurity.com/ (home: what is TruffleHog; OSS vs Enterprise comparison)
- Gitleaks — official GitHub README https://github.com/gitleaks/gitleaks (usage, commands, finding structure, configuration, reports)
- GitHub — Secret scanning overview https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning ; Push protection https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- HashiCorp — HCP Vault Radar https://developer.hashicorp.com/hcp/docs/vault-radar ("What is Vault Radar?")

Sourcing limitations: none material. All five products yielded direct official documentation. (Two guessed Vault Radar URLs 404'd before the correct docs path was found; no evidence was taken from memory.)

## Product Observations

### GitGuardian (dedicated platform)

Evidence layer: A (direct, official docs).

- Definition of object: "secrets generally refer to digital authentication credentials that grant access to systems or data. These are most commonly API keys, usernames and passwords, or security certificates." Two shapes: **specific** secrets (provider-prefixed, e.g. `ghp_…` tokens) and **generic** secrets (high-entropy strings, e.g. Base64 basic-auth).
- Product framing: "Detect and remediate compromised secrets in your internal assets, including your Code Repositories, CI/CD pipelines and Storage Systems." Internal Monitoring: "Find and fix hardcoded secrets across your internal development environment — from code repositories to container registries and collaboration tools."
- **Incident as unit of record**: "Secret incidents are open issues that need your attention to be resolved. They are created thanks to our secrets detection engine that scans your internal sources for hardcoded secrets to display them in your dashboard."
- **Incident lifecycle**: Open (Triggered → Assigned) / Closed (Resolved / Ignored). "Resolved: … you must revoke the secret (and optionally erase all evidence from the git history) before considering it resolved." Ignore reasons: false positive / test credential / low-risk secret. **Regression behavior**: a new occurrence of a resolved incident reopens it (configurable); ignored incidents never reopen.
- **Remediation is credential-centric**: 6-step methodology — assess → secure storage (push-to-vault) → update code → test & deploy → **rotate & revoke** → monitor & verify. "Revocation Features: automated revocation (direct integration with service providers), guided revocation, revocation verification." Internal vs external incidents: public leaks "require faster response… may require emergency revocation procedures."
- Surfaces: internal sources (repos, CI/CD, container registries, collaboration tools, storage) + **Public Monitoring** (public repos) + CLI (ggshield: "Detect and prevent 450+ types of hardcoded secrets before pushing code") + IDE plugins + API.
- Adjacent modules (packaging, not identity): NHI Governance, Honeytoken, GitGuardian Scout ("Collect and monitor vaulted secrets in your production environment… bootstrap incident remediation" — vault-side observation feeding detection), Endpoint Protection, self-hosting.

### Truffle Security / TruffleHog (OSS-first + enterprise)

Evidence layer: A.

- Self-definition: "TruffleHog is the most powerful secrets discovery, classification, validation, and analysis tool… in this context **secret refers to a credential a machine uses to authenticate itself to another machine**. This includes API keys, database passwords, private encryption keys, and more."
- Four-stage articulation: **Discovery** ("look for secrets in many places including git, chats, wikis, logs, API testing platforms, object stores, filesystems and more") → **Classification** ("classifies over 800 secret types, mapping them back to the specific identity they belong to — is it an AWS secret? Stripe secret? Postgres password? SSL private key?") → **Validation** ("for every secret TruffleHog can classify, it can also log in to confirm if that secret is live or not. This step is critical to know if there's an active present danger or not") → **Analysis** (for 50+ types: "who created it? what resources can it access? what permissions does it have?").
- OSS tier: scanning of GitHub/S3/directory/GCS/Docker, 800+ detectors, GitHub Actions / pre-commit / pre-receive hooks, custom regex + verification. Enterprise tier adds: 19+ integrations (GitHub, Confluence, Jira, Slack…), continuous monitoring, dashboard, alerting, public-dataset monitoring, SSO, RBAC, analytics.
- Doc sections confirm the capability set: "Reverify secrets", "Analyze secrets", "Notify results", "Block secrets from leaking", "Connect sources", "Monitor scans".

### Gitleaks (minimal OSS engine)

Evidence layer: A.

- Self-definition: "Gitleaks is a tool for **detecting** secrets like passwords, API keys, and tokens in git repos, files, and whatever else you wanna throw at it via stdin."
- **Finding structure** (the product's entire output model): Finding / Secret / RuleID / Entropy / File / Line / Commit / Author / Email / Date / **Fingerprint** (unique finding identity: commit:file:rule:line).
- Three scan modes: `git` (uses `git log -p` — **scans commit history**, "code, past or present"), `dir` (directories/files), `stdin`.
- Detection knowledge is packaged and extensible: default rule config + user rules (regex, secretGroup, entropy threshold, path regex, keywords, allowlists with commit/path/stopword criteria, composite proximity rules); `gitleaks:allow` inline comments; `.gitleaksignore` fingerprint-based ignore file; baseline reports to suppress old findings.
- Decoding (base64/hex/percent) and archive traversal (nested archives) as scan-depth options.
- Reports: json / csv / junit / sarif / custom template. Exit code 1 on leaks (CI gate). Pre-commit hook mode ("Detect hardcoded secrets…Failed").
- **What it lacks**: no validity checking, no incident store, no dashboard, no revocation, no public monitoring. Still unambiguously the same Type — the minimal pole.

### GitHub Secret Protection / secret scanning (platform-native)

Evidence layer: A.

- Framing: "Prevent fraudulent use of your secrets by automatically detecting exposed credentials before they can be exploited… Secret scanning automatically detects credential leaks so you can secure them before they're exploited."
- Scan scope: "scans your **entire Git history on all branches** … for hardcoded credentials, including API keys, passwords, tokens, and other known secret types. This helps you identify **secret sprawl**, the uncontrolled proliferation of credentials across repositories." Also scans issues, PR titles/descriptions/comments, Discussions, **wikis**, secret gists; periodic rescans when new secret types are added.
- **Alert as unit of record**: "When secret scanning detects a credential leak, GitHub generates an alert on your repository's Security tab with details about the exposed credential."
- **Remediation wording (key evidence)**: "When you receive an alert, **rotate the affected credential immediately** to prevent unauthorized access. While you can also remove secrets from your Git history, this is time-intensive and **often unnecessary if you've already revoked the credential**."
- **Partner program**: "GitHub partners with a large variety of service providers to validate detected secrets. When a partner secret is detected, we notify the provider so they can take action, such as revoking the credential."
- Customizability: generic patterns (private keys, connection strings, generic API keys), custom regex patterns, **validity checks** ("verifying whether a detected secret is still active… may contact the secret's issuing service"), AI-detected unstructured secrets, AI-generated regexes.
- **Push protection** (prevention mode): "blocks pushes that contain secrets *before* they reach your repository" (CLI pushes, UI commits, file uploads, REST API); bypass with reason — bypass reasons map to alert outcomes ("It's used in tests" → closed alert; "It's a false positive" → closed alert; "I'll fix it later" → open alert); delegated bypass; audit log.
- **Public monitoring**: "detect secrets leaked by your enterprise members in public repositories across GitHub."
- Packaging: free on public repos; paid add-on (Secret Protection) for private/internal repos.

### HashiCorp Vault Radar (custody vendor's detection sibling)

Evidence layer: A.

- Positioning (vendor's own navigation): under "Security Lifecycle Management", **Vault — "Centrally manage secrets"** sits beside **Vault Radar — "Scan for embedded secrets"**. Two products, one family.
- Self-definition: "Vault Radar is a product that automates the **detection and identification of unmanaged secrets in your code** so that security teams can take appropriate actions to remediate issues."
- Multi-category content risk: scans for **Secrets**, **PII**, and **Non-inclusive language** — secrets is the headline use case ("Passwords, keys, and other secrets in code are no longer secret when someone shares the code across teams, repositories are public, or when employees leave with copies of the code").
- Mechanics: "scans connected data sources when initially added, when there is a new commit, and for new pull requests"; "deep scans identify secrets in git history, and can even **identify active secrets** so you know which ones are most important"; "scans pull requests, alerts on commits to monitored repositories, and helps **triage and mitigate** secrets already committed"; PR blocking documented for PII (same machinery).
- Docs structure: set up the agent, manage configuration, **remediate secrets**, commands (CLI), scan for inline secrets, MCP server, API, FAQ.
- Deployment: HCP-hosted with a scanning agent; one project per HCP organization (documented constraint).

## Cross-product Comparison

| Dimension | GitGuardian | TruffleHog | Gitleaks | GitHub secret scanning | Vault Radar |
|---|---|---|---|---|---|
| Detection knowledge for credential material | yes (specific + generic detectors, customizable) | yes (800+ typed detectors + custom regex) | yes (default rule set + user rules: regex/entropy/keywords) | yes (partner patterns + generic + custom patterns + AI) | yes (secrets category among content-risk categories) |
| Scanned surfaces | repos, CI/CD, registries, collaboration tools, storage; public repos (separate module) | git, chats, wikis, logs, API-testing platforms, object stores, filesystems | git repos (incl. history), dirs/files, stdin | entire git history all branches + issues/PRs/discussions/wikis/gists | connected sources incl. git history, PRs, inline scans |
| Findings bound to location | incidents + occurrences | findings w/ source + classification | findings w/ file/line/commit/fingerprint | alerts w/ location details | risks by category/rank |
| Credential-centric remediation orientation | explicit (resolved = revoked; automated/guided revocation + verification) | explicit (validation = live-or-not; "active present danger") | implicit (finding is the revocation input; no machinery) | explicit ("rotate immediately"; history removal "often unnecessary" after revocation; partner revocation) | explicit (remediate secrets; active-secret identification) |
| Validity checking | revocation verification (product-specific realization) | core philosophy (log in to confirm live) | none | optional validity checks | active-secret identification |
| Prevention at write time | CLI pre-push + IDE real-time | pre-commit/pre-receive hooks, GitHub Actions | pre-commit hook; exit-code CI gate | push protection (block + bypass-with-reason) | PR scanning/blocking |
| Persistent incident platform | yes (statuses, assignment, timeline, regression) | enterprise tier (dashboard, alerting) | no (report only) | yes (alerts open/closed, bypass alerts) | yes (risk views, triage) |
| Public/external monitoring | Public Monitoring module | enterprise "public datasets" | no | public monitoring + partner program | public-repo risk named in use case |
| Beyond-secrets content categories | NHI governance (adjacent module) | PII-adjacent analysis of credentials | no | no | PII + non-inclusive language (same scanner) |
| Custody of found secrets | no (push-to-vault integration instead) | no | no | no (notifies provider instead) | no (sits beside Vault) |

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **Detection knowledge for credential material** — packaged detectors that recognize authentication credential material (API keys, tokens, passwords, private keys, connection strings) in content: provider-specific typed detectors, generic high-entropy/keyword heuristics, and commonly user-defined rules. The object of detection is the credential, not the general vulnerability.
2. **Scanning of surfaces where credentials should not live** — read-only inspection of content surfaces (canonically code repositories including commit history; commonly also collaboration tools, wikis, artifacts, storage, public surfaces). The product watches content it does not custody.
3. **Findings binding credential + location, oriented to credential remediation** — each detection produces an identified finding (what kind of credential, where it sits, uniquely identifiable) whose resolution path runs through the credential's own lifecycle — revoke/rotate at the issuing service first, code/history cleanup second.

Jointly-held load-bearing tests:

- 1 alone = a regex/pattern library, not a product
- 2 without 1 = code search / grep
- 3 without 1+2 = an incident tracker with nothing to track
- 1+2 without 3 = a linter emitting match counts — no per-finding record to act on
- 2+3 without 1 = generic issue tracking over scanned content

The remediation orientation (leg 3) is what separates this Type from SAST-with-secrets-rules: for an exposed credential the code fix is secondary because the credential is already compromised — GitHub's own remediation guidance ("rotate the affected credential immediately… removing secrets from Git history is… often unnecessary if you've already revoked the credential") and GitGuardian's resolution rule ("you must revoke the secret… before considering it resolved") state this directly.

### Level 1 — Common Mature Structure

Present across most of the sample, not required for the definition:

- **History scanning** — every sampled product reaches into commit history, not just the working tree ("code, past or present"); the canonical realization of surface scanning for git-hosted code
- **Prevention at write time** — the same detection knowledge applied at the point of entry: pre-commit hooks, pre-receive/CI gates, push protection with bypass-with-reason, PR blocking
- **Validity / verification checking** — testing whether a detected credential is still live to prioritize remediation (TruffleHog's core philosophy; GitHub optional checks; Vault Radar active-secret identification; GitGuardian revocation verification)
- **Persistent incident/alert platform** — statuses (open/closed, triggered/assigned/resolved/ignored), assignment, timelines, regression/reopening behavior, notifications
- **False-positive control as a first-class surface** — allowlists, ignore files keyed by finding fingerprint, inline allow comments, bypass reasons, ignore statuses with reasons (false positive / test credential / low risk)
- **Custom detection rules** — user-defined regex/patterns for organization-specific credential shapes
- **Alerting/integration plumbing** — email/Slack/ticket notifications, APIs, SARIF-class report formats, CI exit-code gating

### Level 2 — Variant / Optional Structure

Depends on segment, deployment, or vendor posture:

- **Public/external surface monitoring** — watching public repositories/datasets for the organization's leaked credentials (GitGuardian Public Monitoring, GitHub public monitoring + partner program, TruffleHog enterprise public datasets); internal-only scanning satisfies the Type
- **Partner/provider notification programs** — forwarding detected provider-patterned secrets to the issuing service for revocation (GitHub partner program; GitGuardian automated revocation integrations)
- **Beyond-secrets content categories** — PII, non-inclusive language (Vault Radar); NHI governance modules (GitGuardian)
- **Honeytokens / canary credentials** — decoy detection (GitGuardian)
- **Vault interlock** — pushing found secrets into a secrets manager, observing vault contents to bootstrap remediation (GitGuardian Scout push-to-vault)
- **Deployment shape** — SaaS, self-hosted, agent-based, platform-embedded, OSS CLI
- **Surface breadth** — which non-repository surfaces are scanned (wikis, chats, object stores, logs, CI systems) varies substantially
- **AI-assisted detection** — AI-detected unstructured secrets, AI-generated patterns (GitHub; era-current)

### Level 3 — Vendor-specific (Research Notes only)

- GitGuardian: incident statuses Triggered/Assigned/Resolved/Ignored; configurable regression behavior (real-time-only reopening); Honeytoken module; NHI Governance; Scout; ggshield CLI; self-hosting option
- TruffleHog: 800+ detector count; 50+ types with deep permission analysis; OSS/Enterprise tier split; hosted vs self-hosted scanner deployment
- Gitleaks: `.gitleaksignore` fingerprint file; `gitleaks:allow` comment; composite proximity rules (experimental); feature-complete notice with successor project
- GitHub: partner program mechanics; bypass-reason→alert-outcome mapping ("used in tests"/"false positive" → closed, "I'll fix it later" → open); delegated bypass; free public-repo scanning vs paid Secret Protection packaging; organization-level free secret-risk assessment report
- Vault Radar: one-project-per-HCP-org constraint; agent-based scanning; PII/NIL categories; MCP server

### Rejected Findings (considered and not promoted)

- **"Secrets scanning = SAST rule class"** — rejected as the Type's identity: every sampled product is dedicated to credential material, and the remediation orientation (revoke/rotate first) is categorically different from SAST's code-fix orientation. SAST's hardcoded-credential rules are an overlap zone, not the Type.
- **"Validity checking is definitional"** — rejected: Gitleaks (a full member of the Type) has none; GitHub ships it as an optional toggle. Common mature at best.
- **"Prevention/blocking is definitional"** — rejected: detection-only realizations (Gitleaks CLI scan, GitGuardian public monitoring, TruffleHog OSS scan) are fully in-type; prevention is a deployment point of the same detection knowledge.
- **"Persistent incident store is definitional"** — rejected: Gitleaks satisfies the Type with report-only output; the incident platform is the platform-tier realization of the finding record.
- **"Git history scanning is definitional"** — rejected as strict invariant: universal in-sample but `dir`/`stdin`/inline scan modes satisfy the Type without a git repository; held as the canonical dominant realization of surface scanning.
- **"Detector counts / pattern counts"** — vendor marketing numbers (450+, 800+); never promoted to the canonical document.

## Historical / Market-Sample Check

The Type is young (its products date from the mid-2010s OSS scanner generation onward), so the check runs on conceptual lineage rather than paper-era equivalents:

- **Early OSS scanner generation** (TruffleHog v1, detect-secrets-class tools, early Gitleaks): detectors + repo/history scan + findings report — satisfies all three legs with no platform, no validity checks, no cloud. ✔
- **Hand-rolled lineage** (grep scripts with entropy filters, pre-commit password checks): the conceptual ancestor — fails the packaged-detection-knowledge and finding-record legs; held as lineage, not the Type.
- **Platform-native and regional products**: GitHub's embedded realization and non-US regional scanners fit without any US- or SaaS-specific machinery in the definition. ✔
- The definition names no cloud, no SaaS, no AI, no validity checks, no push protection, no incident platform — none of these are needed to recognize the earliest or the most minimal products. ✔

## Boundary Findings

1. **vs Secrets Management (§14) — RATIFIED keep-both** (discharges the forward note). Seam: **custody-and-delivery vs leak-detection-and-remediation**. The vault's unit of record is the secret as a managed, access-gated, lifecycle-managed object; the scanner's unit of record is the finding about credential material outside custody. Vendor-documented split: HashiCorp's own navigation separates Vault ("Centrally manage secrets") from Vault Radar ("Scan for embedded secrets") as two products in one family; GitGuardian ships vault observation (Scout) and push-to-vault as integrations beside detection, not as the detection product itself. The two interlock (remediation often ends with "move the credential into the vault and rotate it") but neither subsumes the other. A vault does not find leaks; a scanner does not mediate credential use.
2. **vs SAST — held, keep-both.** SAST scans the application's own code for vulnerability classes (hardcoded credentials being one class among many) and remediates by fixing code. Secrets Security is dedicated to credential material, reaches beyond build-time source into full history and non-source surfaces, and remediates through the credential's lifecycle (revoke/rotate first). Overlap zone: SAST engines' secret-detection rules catch the same content at build time; dedicated products exist because exposure (not code defect) is the failure mode. GitHub itself ships CodeQL code scanning and secret scanning as separate product lines.
3. **vs Vulnerability Management — adjacent.** Secrets findings commonly flow into vulnerability-management workflows as inputs; VM aggregates and tracks remediation across scanner types. The dedicated scanner + credential-lifecycle remediation remains this Type.
4. **vs DLP — adjacent, different object.** DLP polices sensitive data (PII, documents) in transit/at rest broadly; this Type targets authentication credential material specifically, with credential-lifecycle remediation. Vault Radar's PII category is an adjacent capability of one sampled product, not the Type's center.
5. **vs Password Manager / PAM — distinct custody postures.** Password managers hold a person's login credentials for form-fill; PAM mediates gated use of privileged accounts. Neither scans for leaked material. This pass confirms the scanner posture is a third, distinct posture in the credential-security space (consistent with both passes' recorded seams).
6. **vs Code Review Platform / CI Platform — embedded capability.** Secrets checks appear inside code review and pipelines as integrations; the dedicated detection engine and finding record remain this Type.
7. **vs Digital Risk Protection / Attack Surface Management — partial overlap on external monitoring.** Public-leak monitoring of credentials overlaps DRP's external discovery; the seam is object-centric: credential material detection + credential remediation vs broader brand/threat-surface monitoring.

"Remove what to become the other Type" tests:

- Remove the remediation orientation (findings become code defects to fix, credential lifecycle ignored) → SAST rule class
- Remove detection (hold secrets, gate access, manage lifecycle) → Secrets Management
- Remove the credential-material focus (any sensitive data in motion/at rest) → DLP
- Remove scanning (aggregate others' findings into remediation workflow) → Vulnerability Management

## Uncertainties

- **Category vocabulary**: the market uses "secrets detection", "secret scanning", "secrets security", and increasingly folds this capability into NHI (non-human identity) platforms. The directory name "Secrets Security" is retained; the document explains the market vocabulary. Whether NHI-governance platforms (inventory-and-ownership posture over machine identities) constitute a separate future Type is not settled here — GitGuardian ships NHI Governance as a separate module, which supports treating it as adjacent packaging.
- **Vault Radar's PII/NIL categories**: one product only; held as optional/variant, not promoted. Whether multi-category content risk scanning is an emerging convergence (secrets scanner → code content risk scanner) is uncertain.
- **Gitleaks maintenance status**: the README declares the project feature-complete with a successor project; this does not affect the Type analysis (the minimal pole remains valid) but the product's future is uncertain.
- **Prevention-first products**: no sampled product is prevention-only (all detect post-hoc as well); a hypothetical prevention-only product's classification is untested — held as unlikely given push-protection products all ship detection.
- **Exact detector counts, scan frequencies, retention windows**: deliberately not stated in the final document; vendor-specific and change-prone.

## Final Synthesis

**Secrets Security** is the leak-detection-and-remediation posture of credential security: products whose defining core is (1) packaged detection knowledge for authentication credential material, (2) read-only scanning of the surfaces where credentials should never live — canonically code repositories including their full commit history, and (3) findings that bind the detected credential to its location and drive remediation through the credential's own lifecycle — revoke/rotate first, code and history cleanup second.

Everything else the market associates with the category — validity checking, push-time blocking, incident platforms, public monitoring, partner revocation programs, honeytokens, vault interlocks, AI detection — is common mature or variant structure, not the definition. The Type is deliberately distinct from Secrets Management (custody), SAST (code-defect orientation), DLP (data-in-motion object), and Vulnerability Management (aggregation posture), with the custody-vendor split (Vault vs Vault Radar) as the market's own ratification of the custody/detection seam.
