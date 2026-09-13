# Secrets Management

## Overview

A **Secrets Management** application is an organization's machine-facing credential store of record: it holds sensitive credential material — passwords, API keys, tokens, connection strings, key and certificate material — as named, protected records, mediates every retrieval through authenticated and policy-authorized programmatic access, and maintains the stored population over time through versioning, expiration, deletion, and rotation.

The problem it solves is credential sprawl: credentials hardcoded in source code, scattered across config files, or shared in chat and spreadsheets are invisible, unrotatable, and unauditable. A secrets-management system replaces all of that with one governed store that applications and pipelines read from at runtime, so credentials can be rotated, expired, and audited without touching the consuming code.

The defining core is deliberately small:

```text
Secret (named, protected, versioned record of credential material)
└── Identity-gated programmatic access (authenticated consumers, policy-authorized retrieval)
    └── Managed lifecycle of the stored population
        (versions, enable/expire states, delete/recover, rotation)
```

Everything else commonly associated with the category — dynamic short-lived credentials, agents and sidecars that inject secrets into workloads, sync to cloud platforms, human-facing dashboards, SSO, change approvals — is standard or optional layering that mature products add, not what makes the system a secrets manager.

## Users & Context

The primary **consumers are machines**: applications at startup and runtime, CI/CD pipelines, scheduled jobs, containers and orchestrators, and operators working through CLIs and SDKs. They authenticate as identities (machine tokens, workload identities, federated platform identities, or human accounts acting through tooling) and retrieve credential material programmatically.

The primary **administrators are people**:

- platform/DevOps engineers — create and organize secrets, wire up delivery to workloads and pipelines, manage access policies
- security teams — own the governance layer: access review, audit trails, rotation policy, expiration
- application developers — author and update the secret values their services consume, usually through a dashboard or CLI

Typical context: an engineering organization of any size running services across cloud and on-premises environments, where every service, pipeline, and integration needs credentials and no human should handle them by hand. The human-facing surfaces exist for administration and authoring; the defining consumption path is programmatic.

## Core Model

### The Defining Core

**The secret.** The central object is the secret: a persistent, individually addressable record that binds a name (or path) to a piece of sensitive material. The material is usually an opaque value — the system stores and returns it without interpreting it; some products add structure such as key-value pairs inside the record or typed values. The record carries metadata: version identifiers, created/updated timestamps, and commonly enable/expire windows. The system holds the material under its own protection — encryption at rest is the universal realization, whether the product manages its own key hierarchy, delegates to a cloud key service, or encrypts within its database. Versions are retained: writing a new value creates a new version while history remains retrievable, which is what makes rotation and incident response possible.

**Identity-gated programmatic access.** Nothing reads a secret without first authenticating and being authorized. Consumers authenticate as identities — machine identities (app roles, service tokens, workload/platform identities), federated identities from cloud or directory providers, or human accounts. Authorization is expressed as policy: rules that bind identities to the specific secrets they may read or manage. The system mediates every retrieval, which is what makes access revocable and attributable. This gate is the property that separates a secrets manager from an encrypted file: a file decrypts for whoever holds its key, with no per-record identity, no per-record policy, and no record of who read what.

**The managed lifecycle.** The stored population is actively maintained over time:

- versioning — new values become new versions; the latest version is the default read; history stays inspectable
- state — records can be enabled/disabled and carry expiration (and sometimes not-before) windows that gate retrieval
- deletion — deleting is typically staged (soft delete, a recovery window, then permanent destroy/purge), because destructive mistakes with credentials are expensive
- rotation — the common mature realization: replacing a secret's value in step with the credential's owner (a database, a cloud account, an API provider), on a schedule or on demand, so long-lived credentials become short-lived ones

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- **Rotation machinery** — scheduled or triggered value replacement, sometimes executed against the owning system (a database, an IAM service) so the secret and the real credential stay in step
- **Dynamic secrets** — on-demand generation of short-lived credentials (database accounts, cloud credentials) with automatic expiry and revocation, instead of storing static values
- **Audit trail** — a record of every access and change: who authenticated, what was read or written, when; often exportable to the organization's logging estate
- **Delivery machinery** — ways to get secrets into workloads beyond direct API calls: CLI injection into processes, agents/sidecars that render secrets to files or environment variables, Kubernetes operators that sync secrets into the cluster, and sync/push into cloud platforms and CI/CD systems
- **Organization of the population** — segmentation into projects, environments, paths, namespaces, or multiple vaults, with inheritance and per-scope access control
- **Human identity federation** — SSO/SCIM/LDAP for the administrative side, alongside machine authentication
- **Recovery semantics** — soft-delete windows, undelete, version rollback, and redaction of historical values

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   the secret as record
Realized as:  opaque string (semantics-free storage), key-value pair set,
              env-var-shaped record, policy-addressed variable

Concept:   the access gate
Realized as:  built-in policy engine over paths, cloud IAM policies,
              policy-as-code role language, scoped service tokens, vault-level RBAC

Concept:   the lifecycle
Realized as:  versioned key-value history, scheduled rotation functions,
              built-in rotators, expiry attributes with soft delete and purge
```

A reader who has only seen one implementation — say, a cloud-hosted secret store — should still be able to recognize a self-hosted policy-driven vault or a developer-first environment-variable manager as the same Type from the core model.

## How It Works

### Establish the store and its structure

```text
Deploy or subscribe to the system
→ create the top-level containers (vaults / projects / namespaces / accounts)
→ define the segmentation the organization wants (per app, per environment, per team)
→ configure how identities will authenticate (machine tokens, platform federation, directory)
→ author the access policies binding identities to scopes
```

### Put a secret in

```text
Create the record under a name/path
→ write the sensitive value (typed in a dashboard, pushed via CLI/API, imported from files)
→ the system encrypts and versions it
→ optionally set expiry/enable windows and metadata
```

### Grant a consumer access

```text
Identify the consumer (an application, a pipeline, a team)
→ issue or bind an identity (service token, app role, workload identity federation)
→ authorize it against the specific scope (policy: read this path, this project, this secret)
→ the consumer can now authenticate and retrieve — and nothing else
```

### Consume at runtime

```text
The application/pipeline authenticates as its identity
→ requests the secret by name/path
→ the system checks identity → policy → state (enabled? expired?)
→ returns the current version's value
→ the access is recorded in the audit trail
```

This loop replaces hardcoded credentials: the consuming code contains only the address of the secret and the identity to authenticate with; the material itself arrives at runtime.

### Keep the population healthy

```text
Rotate: replace values on schedule or demand — manually, via a rotation function
        that updates the owning system too, or by generating fresh short-lived
        credentials instead of storing static ones
→ consumers pick up the new version on their next read (or via sync/agent refresh)
Expire/revoke: disable or expire a record, or revoke a consumer's identity —
        access stops at the gate without touching consuming code
Delete: soft-delete → recovery window → destroy/purge; history redactable
Review: audit trail answers who accessed what, when
```

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Administrative dashboard / UI

The human authoring and governance surface.

- lists secrets with their scopes, versions, states, and metadata
- primary actions: create/edit secrets, organize scopes, manage identities and policies, inspect version history, review audit/activity logs

### CLI

The operator and developer workhorse; in several products it is also a delivery mechanism.

- primary actions: authenticate, read/write/list secrets, import/export, inject secrets into a process's environment at launch

### API / SDKs

The defining consumption surface for machines.

- authenticate → retrieve (by name/path, latest or specific version) → manage (create, update, delete)
- SDKs for application languages; platform-native retrieval paths for orchestrators and pipeline systems

### Delivery agents / operators (optional surface)

Components that bring secrets to workloads: agents/sidecars rendering secrets to files or environment variables, operators syncing secrets into cluster-native objects, sync connections pushing values into cloud platforms and CI/CD secret stores.

### Audit / activity view

The governance surface: access logs and change logs, often forwardable to the organization's logging and monitoring estate.

## Important Rules / Behaviors

### The gate is per-identity and per-scope

Access is granted to identities over specific scopes, not to "everyone with the URL." A consumer can only read what its policy allows; the same store can serve many teams with strict isolation. Revoking an identity or policy cuts access immediately at the gate — consuming code keeps running but can no longer retrieve.

### Retrieval is mediated and recorded

Every read passes through the system and is commonly logged. This is the auditability that hardcoded credentials can never offer, and it is why retrieval — not bulk export — is the intended consumption path.

### Versioning makes rotation safe

Writing a new value creates a new version rather than overwriting; consumers reading "latest" pick up the new value, while the old version remains for rollback or incident forensics. Deletion is staged (recoverable window, then permanent destruction) because credential mistakes are costly.

### State windows gate use

Records commonly carry enabled/expiration windows; operations outside the window are refused (with limited exceptions for recovery-style reads, depending on the product). Expiration is a first-class lifecycle state, not just a note.

### The system's own protection is load-bearing

The store is encrypted under keys the system controls (its own hierarchy, a cloud key service, or its database layer); losing the master key material can mean losing the entire store. Access to the administrative plane is itself identity-gated, commonly federated to the organization's directory.

### Opaque by design

The system generally does not interpret secret material — it stores, protects, versions, and returns it. Structure (what a value means, how it is used) belongs to the consumer; the vault's job is custody, access control, and lifecycle.

## Variants

- **Self-hosted policy-driven vault** — the platform runs in the organization's own infrastructure; access expressed as policy-as-code; often extends into adjacent engines (certificate issuance, encryption-as-a-service, SSH/TOTP) beside the core secret store
- **Cloud-managed secret service** — a managed service where access control delegates to the cloud's IAM and encryption delegates to the cloud's key service; simplest operational model
- **Developer-first secrets platform** — environment-variable-shaped secrets organized by project/environment, with CLI injection, dashboards, and broad sync integrations as the center of gravity; typical of smaller teams
- **Enterprise estate vault** — governance-first: universal workload identity, discovery across existing vaults, estate-wide audit, SaaS or self-hosted deployment
- **Platform-native secret objects** — orchestrator/platform built-in secret objects (e.g. cluster-native secrets) gated by the platform's own access control; the same three-part core realized inside an infrastructure platform rather than a dedicated product
- **Suite siblings** — the same vendor frequently ships this Type beside a password manager (human-facing) and a PAM line (privileged-account mediation), as separate products

## Related Application Types

| Application Type | Distinction |
|---|---|
| Password Manager | serves the person at a login/form — personal or workforce login credentials with autofill; this Type serves machines and pipelines via API. Vendors ship them as separate products |
| Privileged Access Management / PAM | mediates gated use of privileged accounts on target systems (credential checkout or brokered sessions, session recording, human accountability); this Type serves programmatic retrieval of credential material. PAM suites ship machine-facing secrets siblings as separate products |
| Encryption & Key Management | holds cryptographic keys for policy-gated crypto operations where key material stays put; this Type holds authentication/configuration material that consumers take away and use. Cloud vendors route these to different services themselves |
| Certificate Lifecycle Management | manages certificates as objects with issuer/validity/trust semantics and renewal against CAs; this Type holds opaque material. Certificate material may be stored as a secret, but its trust lifecycle is the other Type |
| Machine Identity Management | holds actor-centric records (the machine actor is the record; credentials are attributes); this Type holds credential-material-centric records (the secret is the record; the consumer identity is only the gate) |
| Secrets Security | detects exposed/hardcoded secrets in code, repositories, and surfaces (scanner posture); this Type is the custody-and-delivery store. Vendors ship detection and custody as separate products |
| Configuration Management | enforces desired state on node populations; secrets handling there is an integration point (encrypted variables, vault lookups), not the system of record |
| CI/CD Platform | pipeline variables/secrets are an embedded capability of the pipeline; the organization-wide credential store of record is this Type, which pipelines consume |
| PaaS Management Console | app-scoped config/environment variables at application grain; this Type is organization-wide credential custody with identity-gated access and lifecycle |

The most important boundary is the consumer test: **who or what uses the credential at the point of use?** A person at a login → password manager; a privileged session on a target system → PAM; a cryptographic operation where the key never leaves → key management; a machine or pipeline retrieving material over an API → this Type.

## Representative Products

- HashiCorp Vault
- AWS Secrets Manager
- CyberArk Conjur (open source; enterprise line now positioned as Palo Alto Networks Secrets Manager)
- Doppler
- Azure Key Vault (secrets)

The core model was checked against a platform-native realization (cluster-native secret objects) and a minimal-lifecycle pole (a cloud store without built-in rotation or dynamic secrets) to avoid defining the Type by one implementation pattern.

## Sources

Research date: **2026-09-09**

- HashiCorp Vault — Vault Documentation, Secrets Engines, KV secrets engine, Auth Methods, Audit Logging — https://developer.hashicorp.com/vault/docs , /vault/docs/secrets , /vault/docs/secrets/kv , /vault/docs/auth , /vault/docs/audit
- AWS Secrets Manager — What is AWS Secrets Manager; Get secrets; Rotate secrets; Authentication and access control — https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html , /retrieving-secrets.html , /rotating-secrets.html , /auth-and-access.html
- CyberArk Conjur Open Source — GitHub README (architecture, authenticators, rotators, cryptography) — https://github.com/cyberark/conjur
- Palo Alto Networks Secrets Manager (Idira) — product page and FAQ — https://www.conjur.org/ (redirects to the vendor's Secrets Manager page)
- Doppler — Documentation: Welcome, Secrets, documentation index — https://docs.doppler.com/ , https://docs.doppler.com/docs/secrets
- Azure Key Vault — About Azure Key Vault secrets; Keys, secrets, and certificates overview — https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets , https://learn.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates

> Sourcing limitation: the CyberArk Conjur documentation portal was not directly reachable during research; Conjur observations rest on the official open-source README and the vendor's product page, so product-specific operational details for that sample are stated at positioning level only. Precise numeric limits (secret size caps, version-count defaults, token lifetimes) observed in fetched pages are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
