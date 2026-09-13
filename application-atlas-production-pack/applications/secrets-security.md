# Secrets Security

## Overview

A **Secrets Security** application detects authentication credential material — API keys, tokens, passwords, private keys, connection strings — that has been exposed where it should never be: in source code, in commit history, in wikis and collaboration tools, in artifacts and storage, sometimes in public. It then drives remediation through the credential's own lifecycle: **revoke or rotate the exposed credential first**, and clean the code second.

The problem it solves is exposure, not code defect. A credential committed to a repository is compromised from the moment it becomes reachable — deleting the code later does not un-compromise it, because copies of the repository, its history, and its forks persist. So the remediation that matters is the credential's: invalidate it at the issuing service, issue a replacement, and only then (optionally, per code policy) scrub the history.

The defining core is small:

```text
Detection knowledge for credential material
└── Scanning of surfaces where credentials should not live
    └── Findings binding the credential to its location
        └── Credential-centric remediation
            (revoke/rotate first; code and history cleanup second)
```

Everything else commonly associated with the category — validity checking, blocking secrets at push time, incident dashboards, public-leak monitoring, provider notification programs — is standard or optional layering that mature products add, not what makes the product a secrets-security tool.

## Users & Context

The primary users are **security teams** (application security, security operations): they connect the organization's sources, tune detection, triage findings, and push remediation to closure.

**Developers** are the second constant presence: findings land in their code, push-time blocks interrupt their work, and remediation usually requires their cooperation (updating the code to fetch the credential from a vault instead of a literal).

**Platform / DevOps engineers** wire the scanners into the delivery path — repositories, CI pipelines, pre-commit and pre-receive hooks — and manage the integrations.

Typical context: any organization that writes software and therefore holds credentials. The application watches the development estate (repositories and their histories being the canonical surface, with collaboration tools, wikis, artifact stores, and CI systems as common extensions) and, in some products, public surfaces where the organization's material may have leaked.

## Core Model

### The Defining Core

**Detection knowledge for credential material.** The product carries packaged knowledge of what credentials look like. Two shapes recur across the market: **typed detectors** that recognize provider-specific credential formats (a cloud key, a payment-provider token, a database password format), and **generic heuristics** that flag high-entropy strings and credential-adjacent keywords where no signature exists. Most products also let the organization define **custom rules** for credential shapes unique to their environment. The object of detection is always the credential — not the general vulnerability.

**Scanning of surfaces where credentials should not live.** The product inspects content it does not own. The canonical surface is the code repository **including its full commit history** — a secret removed from the current code still lives in past commits, so history scanning is the dominant realization. Common extensions cover wikis, issue and pull-request text, chat tools, object storage, container registries, and CI logs; some products also monitor public repositories for the organization's leaked material. The scan is read-only: the product observes content, it does not custody it.

**Findings binding credential + location.** Each detection produces an identified finding: what kind of credential was recognized, where it sits (file, line, commit, surface), and a stable identity so the same finding can be tracked across scans. In minimal products the finding is the scan report entry; in platform products it becomes a persistent incident or alert with status, assignee, and history.

**Credential-centric remediation.** The finding's resolution path runs through the credential's lifecycle, not the code's. The exposed credential is revoked or rotated at the issuing service; the code is updated to retrieve the credential from proper storage; history rewriting is optional and policy-dependent. This orientation is the Type's signature: vendors' own remediation guidance instructs rotating the credential immediately and treats history removal as often unnecessary once the credential is revoked.

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- **Validity checking** — testing whether a detected credential is still live ("can it still log in?") so live exposures are prioritized over stale ones; some products verify revocation after remediation
- **Prevention at write time** — the same detection knowledge applied at the point of entry: pre-commit hooks, CI gates that fail the build, push protection that blocks a secret from ever reaching the repository (typically with a documented bypass-and-reason flow)
- **Incident platform** — persistent findings with statuses (open/investigating/resolved/ignored), assignment, timelines, notifications, and regression behavior (a new occurrence of a resolved finding re-opens it)
- **False-positive control** — allowlists, per-finding ignore files, inline allow comments, and bypass reasons (false positive / test credential / low risk), because detection heuristics over free text are inherently noisy
- **Custom detection rules** — organization-specific patterns beyond the packaged detector set
- **Alerting and integration plumbing** — email/chat/ticket notifications, APIs, standard report formats (JSON/SARIF-class), CI exit-code gating

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   detection knowledge
Realized as:  provider-typed detectors, entropy + keyword heuristics,
              custom regex rules, AI-assisted detection of unstructured secrets

Concept:   the scanned surface
Realized as:  full git history, working tree / directories, stdin streams,
              wikis / chats / object stores / registries, public repositories

Concept:   the finding
Realized as:  scan-report entry (file/line/commit/fingerprint),
              repository alert, platform incident with status lifecycle

Concept:   remediation
Realized as:  out-of-band (a human takes the report and revokes),
              guided step-by-step revocation, automated revocation via
              provider integrations, push-to-vault handoff
```

A reader who has only seen one implementation — say, a platform's built-in secret scanning — should still be able to recognize a standalone CLI scanner or a dedicated SaaS platform as the same Type from the core model.

## How It Works

### Aim the scanners

```text
Connect the sources to monitor (repositories, org, wikis, storage, registries)
→ choose the enforcement points (scheduled scans, CI checks,
  pre-commit/pre-receive hooks, push-time blocking, public monitoring)
→ tune detection (enable/disable detector families, add custom rules,
  set allowlists for known-benign content)
```

### Detect

```text
A scan trigger fires (new commit, pull request, push attempt, schedule, on demand)
→ the engine inspects the content — including commit history for repository scans
→ each match of the detection knowledge becomes a finding:
   credential type + exact location + stable finding identity
→ findings surface as alerts/incidents (platforms) or report entries (engines)
```

### Triage and investigate

```text
Review the finding: what kind of credential, where, how exposed
→ where supported, check validity: is the credential still live?
→ dispose of false positives explicitly (ignore with a reason,
  allowlist the pattern, bypass with a recorded reason)
→ assign ownership for real exposures
```

### Remediate through the credential's lifecycle

```text
Revoke or rotate the exposed credential at the issuing service
  (manually, or guided/automated where the product integrates with the provider)
→ move the replacement into proper storage (a secrets manager) and
  update the code to retrieve it from there
→ optionally rewrite history to scrub the material, per code policy
→ verify: revocation confirmed, dependent systems still working
```

### Close and watch for regression

```text
Resolve the finding (resolution presumes the credential is dead)
→ if a new occurrence of the same credential appears later,
  the finding re-opens and re-alerts (regression behavior)
→ analytics accumulate: exposure trends, time-to-remediate, repeat offenders
```

### Capability tiers

**Defining core** — without these, not this Type:

- detection knowledge for credential material
- scanning of surfaces where credentials should not live
- findings binding credential + location
- credential-centric remediation orientation

**Standard in mature products**:

- history scanning; validity checking; prevention at write time; incident platform with statuses and regression; false-positive control; custom rules; alerting/integrations

**Variant / optional**:

- public/external monitoring; provider notification programs (forwarding detected provider-patterned secrets to the issuing service for revocation); beyond-secrets content categories (PII, language policy); honeytokens (decoy credentials); vault interlocks (pushing found secrets into a secrets manager); AI-assisted detection; deployment shape (SaaS / self-hosted / platform-embedded / OSS CLI)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Scanner CLI

The engine in developers' hands.

- primary actions: scan a repository (with history), a directory, or a stream; configure rules; produce a report; exit with a failure code when leaks are found (the CI gate)

### CI / pull-request checks and hooks

The enforcement points in the delivery path.

- scan results appear as pipeline failures, merge checks, or blocked pushes
- push-time blocking presents the detected secret, requires removal (or a recorded bypass with a reason), and commonly generates an alert for the bypass

### Findings dashboard (platform products)

The security team's work surface.

- lists findings with status, severity/priority signals, source, and age
- finding detail: occurrences (every location the credential appears), credential type, validity state where supported, timeline of activity and notes
- primary actions: assign, investigate, mark false positive/ignored with reason, resolve, configure regression behavior

### Reports and notifications

- scan reports in standard formats for downstream tooling
- notifications (email/chat/ticket) on new and regressed findings; historical scans typically report in summary rather than per-finding alerts

### Administrative settings

- source connections, detector/rule configuration, allowlists, bypass policies, integration and notification setup

## Important Rules / Behaviors

### Exposure equals compromise

The operating premise of the whole Type: once a credential is detectable outside custody, it must be treated as compromised. Remediation therefore starts at the issuing service (revoke/rotate), and code cleanup is secondary. Products' own guidance states this ordering explicitly.

### History is in scope

A secret committed years ago is a live finding today. Repository scanning reaches into commit history; removing a secret from the current code does not close the finding.

### Findings persist and regress

Findings are tracked records, not ephemeral scan output: they survive across scans, and a new occurrence of a resolved finding re-opens it and re-alerts. Ignored findings (false positive, test credential) stay closed by design.

### False-positive control is structural

Detection over free text is heuristic; every mature product ships explicit mechanisms to disposition noise — allowlists, ignore files keyed to finding identity, inline allow comments, bypass-with-reason flows — and ignored findings carry their reasons.

### Read-only over scanned content

The product's system of record is the finding, not the credential. It detects, reports, and tracks; it does not hold secrets for later use, mediate their retrieval, or manage their rotation as stored objects — that is the secrets manager's job, and remediation typically ends by handing the replacement credential to one.

### Detection is probabilistic and extensible

Packaged detectors cover known credential formats; generic heuristics catch the rest with more noise; custom rules extend coverage to organization-specific shapes. Coverage breadth differs substantially across products.

## Variants

- **Dedicated secrets-security platform** — internal + public monitoring, incident platform, remediation machinery (guided/automated revocation, push-to-vault), analytics; SaaS or self-hosted
- **OSS-first scanner with an enterprise line** — open-source engine (discovery, classification, verification) with a commercial tier adding continuous monitoring, dashboards, and integrations
- **Minimal open-source engine** — detection rules + scan modes + findings report; no platform, no validity checks; consumed via CLI, CI, and hooks
- **Platform-native** — secret detection embedded in the code-hosting platform itself: history scans, repository alerts, push protection, provider partner programs, public monitoring
- **Custody vendor's detection sibling** — a secrets-management vendor shipping a scanner as a separate product beside its vault; commonly extends to adjacent content-risk categories (PII, language policy)
- **Suite module** — secret-detection rules inside a broader SAST or application-security suite; the overlap zone with the SAST Type

## Related Application Types

| Application Type | Distinction |
|---|---|
| Secrets Management | the custody-and-delivery posture: holds secrets as protected, access-gated, lifecycle-managed records and mediates their retrieval. This Type finds credentials that escaped custody and drives their revocation. Vendors ship the two as separate products — a vault does not find leaks; a scanner does not mediate credential use |
| SAST | scans the application's own code for vulnerability classes (hardcoded credentials being one among many) and remediates by fixing code. This Type is dedicated to credential material, reaches into full history and non-source surfaces, and remediates through the credential's lifecycle — revocation first, code fix second |
| Vulnerability Management | aggregates findings from many scanners into remediation workflow; this Type is the dedicated scanner whose findings may feed it |
| Data Loss Prevention / DLP | polices sensitive data (PII, documents) in transit and at rest broadly; this Type targets authentication credential material specifically, with credential-lifecycle remediation |
| Password Manager | holds a person's login credentials for use at logins and forms; no scanning posture |
| Privileged Access Management / PAM | mediates gated use of privileged accounts on target systems; no scanning posture |
| Digital Risk Protection | discovers external threats across public surfaces broadly (brand, domains, personas); the overlap is public credential-leak monitoring, held here as an optional variant |
| Code Review / CI Platforms | may embed secrets checks as integrations; the dedicated engine and finding record remain this Type |

The most important boundary is the custody test: **does the product hold and mediate the credential, or find it?** Holding and mediating → Secrets Management (or Password Manager / PAM for their postures). Finding exposed material and driving its revocation → this Type.

## Representative Products

- GitGuardian
- TruffleHog (Truffle Security)
- Gitleaks
- GitHub Secret Protection (secret scanning / push protection)
- HashiCorp Vault Radar

The core model was checked against a minimal-engine pole (a CLI scanner with report-only output and no platform), a platform-native realization, and a custody vendor's detection sibling, to avoid defining the Type by any one implementation pattern.

## Sources

Research date: **2026-09-09**

- GitGuardian — Product docs: Secrets Detection, What is a secret?, Internal Monitoring, Secrets incidents, Incident statuses, Secret Remediation Overview — https://docs.gitguardian.com/
- Truffle Security — TruffleHog documentation (what is TruffleHog; OSS vs Enterprise) — https://docs.trufflesecurity.com/
- Gitleaks — official repository README (usage, finding structure, configuration, reports) — https://github.com/gitleaks/gitleaks
- GitHub — Secret scanning overview; Push protection — https://docs.github.com/en/code-security/secret-scanning
- HashiCorp — HCP Vault Radar documentation ("What is Vault Radar?") — https://developer.hashicorp.com/hcp/docs/vault-radar

> Sourcing note: all five sampled products were researched from their official operational documentation fetched on the research date. Vendor-specific numeric details (detector counts, scan frequencies, retention windows) observed in fetched pages are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
