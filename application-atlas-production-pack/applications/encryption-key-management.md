# Encryption & Key Management

## Overview

An **Encryption & Key Management** application is an organization's custodian and governor of cryptographic keys. It holds the organization's encryption keys as managed records under protected custody, administers each key through a governed lifecycle from creation to destruction, and mediates the keys' cryptographic use by authorized consumers — applications, databases, storage systems, and cloud services — under per-key access policy, with an auditable record of every operation.

The problem it solves is structural: encryption is only as strong as the protection of its keys. Without a dedicated system, key material ends up scattered in application configurations, databases, and scripts, where it cannot be rotated, revoked, audited, or demonstrably controlled. Regulated industries additionally need to *prove* key control to auditors, not merely practice it. This Type concentrates custody, lifecycle, use, and evidence in one governed place.

The defining structure is small:

```text
Managed Keys of Record (held under protected custody)
└── Governed Key Lifecycle (create/import → activate → rotate → suspend → retire → destroy)
    └── Policy-gated Cryptographic Use (authorized consumers, defined interfaces, per-key policy)
```

Everything else commonly associated with the category — HSM hardware backing, FIPS validation, envelope encryption, KMIP/PKCS#11 protocol endpoints, cloud BYOK bridges, quorum approvals, tokenization — is widespread in current products but is either a standard capability layered on this core or a variant of how the core is realized.

The "encryption" half of the name is the employment side of the same system: the keys it holds are typically put to work encrypting data across application, database, file/volume, and cloud surfaces. A system that manages keys but never lets authorized consumers use them is a key archive, not key management; a system that performs encryption with ephemeral keys but holds no keys of record is a crypto service, not key management. The three structures above are held jointly.

## Users & Context

Primary users:

- **Key administrators / security team** — create, import, rotate, and retire keys; define policies; approve sensitive operations; act as custodians of the organization's cryptographic material.
- **Security architects** — design which systems use which keys, in which custody posture, to satisfy regulatory and sovereignty requirements.

Secondary users:

- **Application developers** — consume keys through APIs and SDKs to encrypt application data, without handling key material themselves.
- **Database and storage administrators** — connect database transparent encryption and storage/device encryption to externally managed keys through key-delivery interfaces.
- **Platform / DevOps engineers** — provision keys and consumer access as code, integrate CI/CD and infrastructure automation.
- **Compliance officers and auditors** — read the audit trail and key inventory as evidence that encryption controls are operating.

Typical context: organizations with regulatory obligations that require demonstrable control over encryption keys (payment, healthcare, financial, government, and data-protection regimes), organizations consolidating keys that were previously scattered across teams and clouds, and organizations adopting cloud services while retaining independent control of the keys that protect their data.

## Core Model

### The Defining Core

**Managed keys of record under protected custody.** The system's central object is the key: a persistent, individually identified cryptographic key — symmetric (e.g., AES-class) or asymmetric (e.g., RSA/EC-class) — carrying metadata such as its state, version, algorithm, owner, creation and expiration dates, and permitted operations. Keys are held *by the system* under its technical protection, in an HSM or a hardened key service, as the organization's authoritative key inventory. Key material does not live in application configuration files; the system is the custodian. Custody is the invariant — whether key material may ever leave custody is a policy posture (see Variants), not the definition.

**Governed key lifecycle.** Every key has a state, and the system enforces the transitions:

```text
create / generate ──or── import (wrapped, verified)
        ↓
   Pre-activation (exists, cannot be used yet — optional)
        ↓
     Active / Enabled  ⇄  Suspended / Disabled (reversible)
        ↓
rotate (new version or successor key; old retained for decryption)
        ↓
Retired / Revoked (no longer protects new data)
        ↓
Destroyed (material eliminated) → metadata deleted (record closed)
```

Activation and deactivation can be scheduled by date; destruction is deliberate, usually gated by a waiting period, an undo window, or multi-person approval, because destroying a key irreversibly destroys the data it protected. Rotation produces a new key version or successor key while old versions are retained so that previously encrypted data remains readable. Exact state names vary by product; the create → use → rotate → retire → destroy arc does not.

**Policy-gated cryptographic use for authorized consumers.** Keys exist to be used, and the system mediates every use. Consumers — an application, a database engine, a storage device, a cloud service — are registered identities with per-key permissions (encrypt, decrypt, wrap, unwrap, sign, verify, generate MAC, and so on). A use request is allowed only if the consumer's identity is authorized for that operation on that key, and the key's state permits it. Two use models exist across the market, and both satisfy the model:

- *Service-performed crypto*: the consumer sends data (or a data-encryption key) to the system, which performs the operation inside custody and returns the result; key material never leaves.
- *Key delivery*: the system delivers key material (typically wrapped) to an authorized consumer over a key-management protocol, and the consumer performs the encryption locally — the pattern used by storage devices, tape drives, and database transparent encryption.

### Standard Capabilities

Mature products across the researched sample carry most of the following. They are not what makes the product key management, but they make it operable and sellable:

- **Audit trail** — a record of who did what to which key, when: every administrative change and every cryptographic use. This is the compliance evidence the Type exists to produce, and it is a near-universal market expectation.
- **HSM / FIPS-validated backing** — key material generated and used inside hardware security modules or validated cryptographic modules. The dominant market expectation; some products also operate without dedicated HSMs while still providing protected custody.
- **Per-key access control with separation of duties** — key administrators manage keys; consumer identities use them; the two roles are separated, and per-key policies (sometimes plus temporary, delegable grants) express who may do what.
- **Envelope encryption / data keys** — the system generates data-encryption keys, returns them encrypted under a managed key (optionally with a plaintext copy for immediate use), and later decrypts the wrapped copy; the bulk data is encrypted locally by the consumer with the data key, and the system never stores or tracks the data keys.
- **Rotation with retention** — rotation adds a new version; old versions remain available for decryption (sometimes with a floor version below which decryption is refused); ciphertext can be re-wrapped to the newest version without exposing plaintext.
- **Key import (BYOK)** — externally generated key material can be imported, wrapped under a system key so plaintext never crosses the wire, and verified with a key check value.
- **Multiple consumer interfaces** — a REST/SDK API plus industry key-management interfaces (KMIP, PKCS#11, and in enterprise products CNG/JCE providers), so databases, storage devices, and legacy software can consume the same keys.
- **High availability and backup** — clustered deployment, replication, and backup/restore of the key store, because loss of keys means loss of all data they protect.
- **Dual control / quorum approval** — sensitive operations (destruction, export, policy changes) can require approval from multiple named individuals; a modern realization of the older key-ceremony discipline. Common in enterprise deployments; cloud services often realize the same caution through scheduled deletion windows instead.

### One Structure, Many Implementations

The core model is written conceptually. Common implementation realizations:

```text
Concept:            Protected custody
Implementations:    dedicated HSM appliances · hardened key-service clusters ·
                    confidential-computing enclaves · cloud-provider managed HSMs ·
                    external key stores the system fronts

Concept:            Cryptographic use
Implementations:    request/response crypto API · envelope data keys ·
                    KMIP key delivery · PKCS#11 / CNG / JCE providers ·
                    encryption agents on hosts

Concept:            Rotation
Implementations:    new version inside one key object · successor key linked to the old ·
                    scheduled automatic rotation · on-demand rotation
```

A reader who has only seen one implementation — say, a cloud API where keys are never exposed — should still be able to recognize a KMIP server that delivers keys to tape drives, or an appliance cluster fronting database encryption, as the same Application Type.

## How It Works

### Establish custody and administration

The organization deploys the system (self-managed cluster or appliance) or subscribes to it (managed cloud service). Cryptographic modules are initialized, administrator identities and roles are defined, and the audit pipeline is connected. From this point, the system is the custodian of record for the keys entrusted to it.

### Create or import keys

```text
Create:  request generation (algorithm, size, permitted operations, group/owner)
         → material generated inside custody, never exposed
         → key enters service (immediately, or at a scheduled activation date)

Import:  obtain public wrapping key from the system
         → wrap external key material under it
         → upload; system unwraps inside custody and verifies a key check value
         → key enters service
```

Keys are organized in containers (groups, domains, or namespaces) that carry policies and scope access.

### Authorize consumers

Each consuming system is registered as an identity (application credential, certificate, or cloud principal) and granted specific operations on specific keys. The separation is structural: administrators change keys and policies; consumers only exercise the operations granted to them.

### Use keys for encryption

Three recurring patterns:

```text
1. Direct crypto call
   application → encrypt(data) under key K → ciphertext returned → application stores it

2. Envelope encryption
   application → request data key under key K
   → receives plaintext data key (for immediate use) + wrapped copy (to store with the data)
   → encrypts bulk data locally; discards plaintext data key
   → later: sends wrapped copy back for decryption when needed

3. Key delivery (databases, storage devices, tape)
   consumer connects over a key-management protocol (e.g., KMIP)
   → system delivers/wraps keys per policy
   → consumer encrypts its data locally; system keeps the lifecycle and the record
```

A fourth pattern bridges to cloud services: the organization's key manager either exports a wrapped key into a cloud provider's key service (bring-your-own-key) or acts as an external key store that the cloud provider calls at encryption time (hold-your-own-key). The organization's system remains the record and the control point.

### Rotate

```text
trigger (schedule, policy, or manual)
→ new key version or successor key created in custody
→ new encryptions use the new material
→ old material retained for decryption of existing data
→ optional: re-wrap existing ciphertext to the new version (without exposing plaintext)
→ optional: old version deactivated so it can only decrypt/verify
```

### Retire and destroy

```text
suspend (disable) → retire/revoke (no new protection) → destroy material
→ waiting period / undo window / multi-person approval as configured
→ delete metadata; audit trail retains the record
```

Destruction is treated as the most dangerous operation in the system, because it converts encrypted data into unrecoverable loss. Products therefore surround it with friction: confirmation states, delay windows, reversible-delete policies, and quorum approval.

### Audit throughout

Every step above — creation, policy change, each use, rotation, destruction — is written to the audit trail, from which compliance evidence and forensic answers are drawn. Many products export these records to security-analytics platforms.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Administrative console

The custodian's primary surface.

- key inventory (list and search by state, type, owner, group) and key detail (metadata, versions, links, permitted operations, audit log)
- policy surfaces: per-key and container-level access, cryptographic and metadata policies, rotation schedules, quorum approval rules
- consumer registration and credential management
- approval queues for quorum-gated operations
- audit log browsing and export

### Cryptographic API (REST/SDK)

The developer surface: request/response operations (encrypt, decrypt, generate data key, wrap/unwrap, sign, verify, MAC, random generation) authenticated by consumer credentials, with per-key authorization enforced server-side.

### Key-delivery interfaces

Protocol endpoints and libraries through which external systems consume keys: key-management protocols (KMIP) for databases, storage arrays, and tape/device encryption; cryptographic provider interfaces (PKCS#11, CNG, JCE) for applications and legacy software that expect a local cryptographic provider backed by remote custody.

### Cloud bridge surfaces

Surfaces for exercising key control over cloud services: exporting wrapped keys into cloud key services (BYOK), and operating as an external key store that a cloud provider calls at encryption time (hold-your-own-key).

### Automation interfaces

CLI and infrastructure-as-code providers so key creation, policy, and consumer grants are provisioned and changed as reviewed code rather than console clicks.

## Important Rules / Behaviors

### Keys are used, not handed around

The default posture is that key material never leaves custody in plaintext; consumers get results (ciphertext, signatures) or wrapped material. Delivery of usable key material to consumers is a policy-gated variant used where the consumer must encrypt locally (storage devices, database engines) — and even then the system remains the source of record and the lifecycle owner.

### State gates operations

A key's state determines what is possible: a pre-activation key performs no operations; a suspended key performs none; a retired key typically retains only the "process" side (decrypt, verify, unwrap) so old data stays readable while new data is protected by the successor. Suspend/unsuspend is reversible; deactivation and destruction are not.

### Rotation preserves decryptability

Rotation never orphans existing ciphertext: old versions remain decryptable (sometimes with a configurable floor below which decryption is refused as a security lever), and re-wrapping moves ciphertext to the new version without ever exposing plaintext. Rotation cadence is a policy choice; some products also advise usage-based rotation for certain algorithm modes.

### Destruction is deliberate, delayed, and often plural

Scheduled deletion with a waiting period, reversible-delete windows, and multi-person approval are the standard friction around destruction. The rule exists because key destruction is data destruction.

### Separation of duties is structural

The identity that manages keys and the identities that use them are different, with different credentials and permissions. In enterprise deployments, sensitive administrative operations can require quorum approval — the software realization of dual-control key ceremonies.

### Every operation is evidenced

The audit trail is not an accessory; it is the product's compliance deliverable. Administrative actions and cryptographic uses are both recorded, and the records are commonly exported to the organization's security-analytics stack.

### Import and export are wrapped and verified

Key material entering or leaving custody crosses the wire wrapped under a wrapping key and is verified with a key check value, so plaintext material does not travel and mistakes are detected.

## Variants

- **Custody posture** — keys never exposed (API-crypto-centric cloud services and encryption-as-a-service) vs. keys delivered to authorized consumers under protocol (storage/device and database key management) vs. external key stores where the organization's system holds material while a cloud platform fronts it (hold-your-own-key).
- **Encryption surface packaging** — the same core is sold with different employment surfaces attached: application-level API crypto; database transparent-encryption custody; file/volume encryption agents on hosts; tokenization/format-preserving encryption; code signing.
- **Deployment model** — hyperscaler-managed service; self-hosted cluster or appliance; vendor-operated SaaS; cloud marketplace services pairing key management with cloud HSMs.
- **Platform bundling** — standalone key management vs. a platform that also carries secrets management, certificate integrations, data discovery, or key-inventory discovery across external systems.
- **Consumer ecosystem emphasis** — cloud-service integration (BYOK/external key stores) vs. database/storage integration (KMIP/PKCS#11) vs. developer application integration (SDKs/CLI).
- **Algorithm era** — classical algorithm sets vs. post-quantum algorithm support (signature and key-encapsulation families) appearing in current-generation products.

A variant remains a variant unless it changes the core: if a product holds no keys of record, or imposes no lifecycle, or mediates no use, it has drifted into a neighboring Type (see below).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Secrets Management | adjacent, frequently co-sold | secrets are credentials (passwords, API keys, tokens) whose *values* applications consume; keys are cryptographic material whose lifecycle and use the system governs for data protection. Strip lifecycle/audit/compliance machinery → secret store; strip secret-value storage → key management |
| Secrets Security | adjacent | detection/hygiene over exposed secrets in code and collaboration systems; no key custody or crypto service |
| PKI Management | adjacent | certificate authorities and identity bindings; a PKI issues certificates that bind identities to keys, while this Type holds the raw keys (including a CA's keys) without issuing anything |
| Certificate Lifecycle Management | adjacent | issuance, renewal, and deployment of certificates; consumes keys held here; no key lifecycle governance of its own |
| Password Manager | distinct audience | end-user credential vault; offers no cryptographic service to other systems and no key lifecycle |
| Data Security Posture Management / Data Access Governance | adjacent | discovers and classifies data and configures access; holds no keys and performs no crypto |
| Crypto Wallet / Digital Asset Custody | different domain | custody of blockchain keys for asset control; different users, objects, and workflows despite the "key custody" resemblance |
| Database / storage encryption features (TDE, device encryption) | consumer, not instance | these features encrypt data; this Type is the external custodian they draw keys and lifecycle from |
| Backup Management | consumer | backup products may encrypt backups with keys managed here |

The most consequential boundary is with Secrets Management, because several vendors ship both capabilities in one platform and the vocabulary overlaps ("vault", "key", "secret"). The structural test is the object and the governance: credentials consumed as values vs. cryptographic material governed through a lifecycle and mediated in use.

## Representative Products

- AWS Key Management Service (AWS KMS)
- Thales CipherTrust Data Security Platform (CipherTrust Manager)
- Fortanix Data Security Manager
- HashiCorp Vault (transit and KMIP engines)

These span the main market shapes: a hyperscaler's cloud-native service, the enterprise on-premises/hybrid platform with HSM lineage, a modern unified KMS+HSM offered as SaaS or appliance, and a developer-centric encryption-as-a-service engine inside a secrets platform.

The core model was checked against older, non-cloud key management practice — KMIP-era key managers serving storage-device and tape encryption, and dual-control key-ceremony discipline — to avoid over-fitting the definition to the modern cloud API pattern.

## Sources

Research date: **2026-09-08**

- AWS KMS Developer Guide (overview, key concepts, key states, data keys) — https://docs.aws.amazon.com/kms/latest/developerguide/overview.html
- Thales Documentation Hub (CipherTrust Data Security Platform structure) — https://thalesdocs.com/
- Fortanix Data Security Manager (product page; key lifecycle management documentation) — https://www.fortanix.com/platform/data-security-manager , https://support.fortanix.com/docs/fortanix-data-security-manager-key-lifecycle-management.md
- HashiCorp Vault documentation (transit secrets engine) — https://developer.hashicorp.com/vault/docs/secrets/transit
- OASIS Key Management Interoperability Protocol (KMIP) Technical Committee — https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=kmip

> Sourcing limitation: deep operational documentation for Thales CipherTrust Manager was not retrievable from the research environment (access denied; documentation portal rendered only via scripts). Thales is therefore used as product-structure evidence only, and operational claims in this document rest on the other sampled products. Precise numeric limits, default settings, and per-product state names are intentionally not stated; conceptual state and operation descriptions reflect cross-product commonality rather than any single vendor's exact labels.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
