# Research Notes — Encryption & Key Management

Research date: 2026-09-08
Slug: encryption-key-management
Directory leaf: "Encryption & Key Management" (§15 Cybersecurity, Identity & Trust)

---

## Research Goal

Understand what an Encryption & Key Management application actually is as a Type: what objects exist inside it, what its users do with them, how key lifecycle and key use actually flow, which structures are definitional vs. merely common in today's market, and where its boundaries lie against Secrets Management, PKI/Certificate Lifecycle Management, Password Manager, and data-protection neighbors.

## Initial Boundary (hypothesis before research)

- Hypothesis: enterprise security software that (a) holds custody of an organization's cryptographic keys, (b) administers their lifecycle (create/rotate/retire/destroy), and (c) mediates their cryptographic use by applications, databases, storage, and cloud services under access policy.
- Likely confusions: Secrets Management (credentials vs. keys), PKI/Certificate Lifecycle Management (identity bindings vs. raw keys), Password Manager (end-user credentials), DSPM (discovery, no custody), Crypto Wallet (blockchain assets), and the encryption features embedded in databases/storage products (consumers of this Type, not instances of it).
- Unknowns going in: whether "encryption" (as opposed to "key") management adds a definitional leg; whether audit is definitional or common; whether the KMIP key-delivery model (consumer performs the crypto) breaks an API-centric definition.

## Research Questions

1. What are the core objects? (key, key version, key ring/group/domain, HSM backing key, data key, policy, grant, audit record)
2. What is the key lifecycle, and which transitions are system-enforced?
3. How is key material protected and can it ever leave custody? (non-exportable vs. delivered vs. external key store)
4. How do consumers use keys? (API crypto, envelope encryption/data keys, KMIP/PKCS#11 delivery, TDE, agents)
5. How does rotation work? (new version vs. new key; re-encryption vs. rewrap; retention of old versions)
6. What access control exists over keys, and how are administrators separated from users?
7. What role do audit, FIPS validation, dual control/quorum play — definitional or market expectation?
8. How does the Type reach cloud services? (BYOK, HYOK, XKS/EKM external key stores)
9. Where is the boundary against Secrets Management and Certificate Lifecycle Management?
10. Would older / non-cloud products (tape-era key managers, KMIP servers, HSM+ceremony practice) still fit the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Documentation reached |
|---|---|---|
| AWS KMS | hyperscaler cloud-native KMS; API-first; integrated with cloud services | Full developer guide (Tier 1) |
| Thales CipherTrust Manager (CipherTrust Data Security Platform) | enterprise on-prem/hybrid leader; HSM lineage (Luna); platform with data protection | Docs hub root only (Tier 2); deep docs unreachable |
| Fortanix Data Security Manager (DSM) | modern unified KMS+HSM; SaaS/on-prem; confidential-computing architecture | Product page + support docs (Tier 1+2) |
| HashiCorp Vault (transit + KMIP engines) | developer/DevOps "encryption as a service"; straddles Secrets vs. Keys | Full docs (Tier 1) |

Plus: OASIS KMIP standard (for the key-delivery model and the historical/storage-device variant); historical check against tape-era key management practice (no dedicated product fetch — see Uncertainties).

## Sources

- AWS KMS Developer Guide — overview, concepts, key states, data keys:
  - https://docs.aws.amazon.com/kms/latest/developerguide/overview.html
  - https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html
  - https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html
  - https://docs.aws.amazon.com/kms/latest/developerguide/data-keys.html
- Thales Documentation Hub (root): https://thalesdocs.com/ (deep CipherTrust Manager docs redirect to a JS-rendered portal; content not retrievable)
- Fortanix:
  - https://www.fortanix.com/platform/data-security-manager (product page)
  - https://support.fortanix.com/llms.txt (docs index)
  - https://support.fortanix.com/docs/fortanix-data-security-manager-key-lifecycle-management.md
  - https://support.fortanix.com/docs/dsm-concepts.md (resolved to the Cluster Attestation Guide; used for SGX/attestation and product-scope quote)
- HashiCorp Vault: https://developer.hashicorp.com/vault/docs/secrets/transit (plus docs nav for KMIP / Key Management engines)
- OASIS KMIP TC: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=kmip
- IBM Guardium Key Lifecycle Manager docs: 403 — not used; no IBM-specific claims made.

---

## Product A — AWS KMS (evidence layer A: directly observed)

Key observations:

- Positioning: "create and control the keys used to encrypt and sign your data"; KMS keys are protected by FIPS 140-3 Security Level 3 validated HSMs and "never leave AWS KMS unencrypted".
- Key hierarchy: a KMS key is a logical container (ARN/key ID) over HSM backing keys (HBKs) that are generated in HSMs and never exported in plaintext; domain keys wrap HBKs; derived encryption keys are per-operation; customer data keys (CDKs) can be returned encrypted (and optionally plaintext) to callers.
- Key classes: customer managed keys (full customer control: policies, rotation, deletion scheduling, tags, aliases), AWS managed keys (in customer account, service-scoped, annual rotation, not directly usable by customers), AWS owned keys (in AWS accounts, invisible to customer, no audit view).
- Key states: Enabled, Disabled, PendingDeletion (with cancellation), PendingImport (imported key material), Unavailable (custom key stores disconnected), plus transient Creating/Updating for multi-Region keys. A state table governs which API operations succeed per state.
- Operations vocabulary: Encrypt, Decrypt, GenerateDataKey(WithoutPlaintext), GenerateDataKeyPair(WithoutPlaintext), ReEncrypt, Sign, Verify, GenerateMac, DeriveSharedSecret, GetPublicKey.
- Envelope encryption: data keys are generated, returned plaintext + encrypted under the KMS key; KMS "does not store, manage, or track your data keys"; callers encrypt data locally with the data key and store the wrapped copy alongside.
- Rotation: optional for customer managed keys (new HBK version; old versions retained for decrypt/verify; only active version protects new data); annual automatic for AWS managed keys; on-demand rotation exists.
- Deletion: scheduled with a waiting window; cancellable (PendingDeletion state).
- Access control: key policies (per-key resource policy), IAM policies, and grants (temporary, delegable use authorizations with retire/revoke).
- Custody variants: custom key stores backed by AWS CloudHSM, and external key stores (XKS) where key material stays in an external key manager outside AWS — the "hold your own key" posture.
- Audit: CloudTrail logging of key API usage (customer-managed keys; not visible for AWS owned keys).
- Imported key material (BYOK): keys created in PendingImport, material imported wrapped; can be deleted/expired, returning the key to PendingImport.

## Product B — Thales CipherTrust Data Security Platform (evidence layer A- for structure only; deep docs unreachable)

Observations from the official documentation hub (product structure level only):

- The CipherTrust Data Security Platform is described as integrating "data discovery, classification, data protection and granular access controls with centralized key management – on a single platform", with a unified management console and APIs.
- Components named on the hub: CipherTrust Manager (the key management core), CipherTrust Cloud Key Manager (cloud key management), CipherTrust Transparent Encryption (CTE), Data Protection Gateway, CipherTrust Connectors/Integrations, Data Discovery and Classification.
- General Purpose HSM family: Luna Network/PCIe/USB/Cloud HSMs described as "FIPS validated ... root of trust"; Crypto Command Center for HSM administration.
- Data Protection on Demand: cloud marketplace delivering "Cloud HSM and Key Management services".
- Limitation: CipherTrust Manager operational detail (key states, quorum, domains, KMIP profiles) could not be verified — the deep docs are behind a 403/JS portal. No operational claims about CipherTrust Manager internals are made in this research; the enterprise pole's operational picture is carried by Fortanix + AWS + Vault evidence.

## Product C — Fortanix DSM (evidence layer A: directly observed)

Key observations:

- Positioning: "Data Encryption and Key Management" — "Encrypt sensitive data across hybrid multicloud and centralize enterprise key management"; modules: KMS, HSM, File System Encryption, Transparent Database Encryption, Data Tokenization, BYOK, AWS XKS, Google EKM, Secrets Management, Code Signing, Secure Business Logic, DSM Accelerator (local key caching / in-memory crypto), multicloud key management. FIPS 140-2 L3 validated hardware; on-prem and SaaS deployment.
- Core object: the security object — generated or imported; types include AES, DES, DES3, HMAC, RSA, EC, DSA, Opaque, Secret, Certificate, BIP32, SLIP10, ARIA, KCDSA/EC-KCDSA, SEED, BLS, LMS, ML-KEM, ML-DSA, XMSS, Tokenization (FPE) and Irreversible Tokenization.
- Lifecycle states: PreActive (future activation date; no crypto possible) → Active (with reversible Enabled/Disabled sub-states) → Deactivated (deactivation date reached or Revoke called; irreversible back-transition) → Compromised (final; set via Revoke with reason COMPROMISED). Destroy removes key material but retains metadata (irreversible disable); Delete removes metadata permanently; a Key Undo Policy can make deletion reversible for a defined period.
- Operations split: "Process Operations" (Verify, Decrypt, UnwrapKey, MacVerify) vs. "Protect Operations" (Sign, Encrypt, WrapKey, DeriveKey, MacGenerate, AgreeKey); per-key permitted operations chosen at creation; state gates which operations run (deactivated keys can still process/decrypt when enabled).
- Rotation: "Generate new key" (new UUID; old key renamed with rotation timestamp; key links recorded; optional "deactivate original after rotation" so the old key only decrypts/verifies/unwraps) or "Rotate to an existing key" (same type/size/permissions/group required); scheduled rotation policies (start date + frequency); quorum approval required if the key's group has a quorum policy.
- Governance: accounts and groups as containers; account- and group-level cryptographic policies, key metadata policies, quorum approval policies (M-of-N approvals gate destructive/sensitive operations); per-key permissions for apps; per-object detailed audit logs; KCV/CMAC verification on import; wrapped import (key encrypted under a Key Encryption Key so material never crosses TLS in plaintext).
- Consumers: apps authenticate with API keys or client certificates; client interfaces PKCS#11, Microsoft CNG, JCE, REST API, CLI, SDKs, Terraform provider.
- Encryption surfaces: TDE integrations documented for Oracle, SQL Server (incl. Always Encrypted), Cassandra, MongoDB (incl. client-side field-level), MySQL/Percona/MariaDB, IBM Db2, Informix, InterSystems (via KMIP), EDB Postgres; filesystem encryption for Linux/Windows/VMs; VMware encryption/KMS integrations.
- Cloud key management: BYOK export to AWS KMS, Azure Key Vault/Managed HSM, GCP Cloud KMS, OCI, Salesforce, Alibaba; external key stores (AWS XKS, Google EKM, Azure Managed HSM external key management); "cloud native key management" groups that operate cloud KMS keys from DSM.
- Secrets management on the same platform (Secret objects viewable in UI; quorum-gated reveal); tokenization as key types; certificate management integrations (AppViewX, Keyfactor, CyberArk/Venafi, Microsoft PKI, EJBCA).
- Architecture: software runs inside Intel SGX enclaves; cluster attestation (DCAP) at node-join/upgrade events; strict FIPS mode algorithm restrictions.

## Product D — HashiCorp Vault, transit + KMIP engines (evidence layer A: directly observed)

Key observations:

- Transit engine self-described as "cryptography as a service" / "encryption as a service"; Vault does not store the data sent to it — the caller stores ciphertext.
- Named keys with versioning: rotation adds a version to a keyring; `min_decryption_version` archives old versions (security + performance lever); rewrap re-encrypts ciphertext to the newest version without revealing plaintext (safe for nearly-untrusted processes); datakey generation returns a high-entropy key encrypted under the named key (plaintext return optional "to accommodate auditing requirements").
- Operations: encrypt/decrypt, sign/verify, HMAC, generate hashes, source of random bytes; key derivation with context; convergent encryption (deterministic nonce; same plaintext+context → same ciphertext, enabling encrypted equality lookups).
- Key types: AES-GCM (128/256), ChaCha20-Poly1305, Ed25519, ECDSA P-256/384/521, RSA 2048/3072/4096, HMAC, CMAC (ENT), managed_key (ENT — key material held by an external KMS/HSM), PQC ML-DSA/SLH-DSA/hybrid (ENT); FIPS 140-3 mode exists with algorithm restrictions.
- BYOK import: wrapping-key flow (RSA-4096 public wrapping key; PKCS#11 HSM import paths documented); docs note it is "more secure to have Transit generate and manage a key within Vault".
- Access control: Vault ACL paths — "trusted operators can manage the named keys, and applications can only encrypt or decrypt using the named keys they need access to".
- Sibling engines confirm the boundary map: KV (secrets), PKI (certificates), KMIP (ENT — serves the KMIP protocol so KMIP clients like databases/storage can use Vault as their key store), Key Management (ENT — distributes keys to cloud KMSs), Transform (ENT — FPE/tokenization).
- NIST rotation guidance quoted for AES-GCM usage limits; operators estimate rates to set rotation frequency.

## Standard reference — OASIS KMIP (evidence layer A: standard text)

- KMIP is the OASIS standard protocol "for communication between encryption systems and a broad range of new and legacy enterprise applications, including email, databases, and storage devices"; TC mission: "advancing interoperability standards for enterprise encryption key management".
- Confirms the key-delivery model as a first-class industry pattern: a key management server holds and lifecycles keys; storage devices/tape drives/databases consume them via protocol. Interop demos (2011–2018) list key managers, HSM vendors, database and storage vendors as KMIP implementers.
- Supports the historical check: pre-cloud enterprise key management (KMIP servers fronting tape/storage encryption, HSM-backed key ceremonies) has the same core structure as modern cloud KMS.

## Historical / Market-Sample Check

Question: would older, regional, platform-native products still fit the definition?

- Tape-era / storage-device key management (KMIP servers managing keys for tape drives and storage arrays; IBM-style key lifecycle managers for device encryption): fits — keys of record, lifecycle (generate/rotate/retire), policy-gated delivery to devices, audit. No cloud, no REST API needed.
- HSM + key ceremony practice (dual-control key generation ceremonies, M-of-N custodians, paper logs): fits the custody + lifecycle + controlled-use core; the ceremony is the manual realization of quorum/dual control that modern products implement as quorum policies.
- Early database TDE with locally held keys (no external manager): does NOT fit as an instance of this Type — it is the consumer-side encryption feature; the Type appears when key custody and lifecycle move to a governed external custodian. This is the same relationship as "database has an encryption feature" vs. "key management system".
- Conclusion: the definition holds across eras if it is anchored on custody + lifecycle + policy-gated use, not on cloud APIs, HSM-as-mandatory, or any specific protocol.

---

## Cross-product Comparison

| Dimension | AWS KMS | Fortanix DSM | Vault (transit/KMIP) | Thales CDSP (structure only) |
|---|---|---|---|---|
| Keys of record | KMS key = logical container over HSM backing keys | security objects (many types incl. secrets/certs) | named transit keys (versioned keyring); KMIP objects | CipherTrust Manager key management core |
| Custody | FIPS 140-3 L3 HSMs; material never leaves unencrypted; XKS = external custody | FIPS 140-2 L3 HSM/appliance or SaaS; SGX enclaves; wrapped import | Vault server storage (FIPS mode exists); managed keys delegate to external KMS/HSM | Luna HSM "root of trust" |
| Lifecycle states | Enabled/Disabled/PendingDeletion/PendingImport/Unavailable | PreActive/Active(Enabled/Disabled)/Deactivated/Compromised; Destroy vs Delete; undo window | versioning + min_decryption_version; rotate/rewrap | not verified |
| Rotation | new HBK version; old retained for decrypt; optional/annual/on-demand | new key + links, or rotate-to-existing; scheduled policies; deactivate-original option | rotate adds version; rewrap without plaintext | not verified |
| Use model | API crypto + data keys (envelope) | API crypto + wrap/unwrap + PKCS#11/CNG/JCE + KMIP + TDE + agents | API crypto (transit) + KMIP server + managed keys | CTE agents + connectors (structure) |
| Access control | key policies + IAM + grants | app permissions + account/group policies + quorum approval | ACL paths (operators manage, apps use) | "granular access controls" (claim) |
| Audit | CloudTrail | per-object detailed logs + transient audit logging | audit logging (devices) | centralized management (claim) |
| Cloud reach | is the cloud KMS; XKS receives external keys | BYOK export to clouds; XKS/EKM hosting; cloud-native key management | Key Management engine distributes to cloud KMSs | CCKM (cloud key manager) |
| Secrets on same platform | no (separate AWS services) | yes (Secret objects) | yes (KV engine) | platform includes data protection |
| Certificates | no | certificate objects + integrations | PKI engine (separate) | platform includes data protection |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **Managed keys of record under protected custody** — persistent, individually identified cryptographic key objects (symmetric and/or asymmetric) carrying lifecycle metadata, held by the system under its technical protection (HSM or hardened key service) as the organization's authoritative key inventory. Remove → key material scattered in application configs with no custodian, or a bare HSM appliance with no managed inventory.
2. **Governed key lifecycle** — the system administers each key through its life: creation/generation or import → activation → rotation/versioning → suspension (enable/disable) → retirement/revocation → destruction, with transitions enforced by the system (dates, policies, waiting periods, approvals). Remove → a static keystore; keys exist but never age; "management" gone.
3. **Policy-gated cryptographic use for authorized consumers** — applications, databases, storage systems, and cloud services invoke the keys' cryptographic power (encrypt/decrypt/wrap/unwrap/sign/verify/MAC, or receive key material) through defined interfaces (API, KMIP, PKCS#11, CNG/JCE), under per-key access policy; every use is mediated by the system. Remove → an offline key archive / ceremony record; keys never serve data protection.

Jointly-held test:
- 1 alone = key inventory/keystore; 2 without 1 = lifecycle paperwork; 3 without 1 = stateless crypto oracle with ephemeral keys (not key management).
- 1+2 without 3 = key archive with a calendar; 1+3 without 2 = keystore with a crypto API whose keys never age; 2+3 without 1 = lifecycle + crypto with no custody of record.

Note: "protected custody" is the invariant; *non-exportability* is a posture (L2), not the invariant — the KMIP delivery model and BYOK export both move material to authorized consumers under policy while the KMS remains the record.

### L1 — Common Mature Structure (near-universal in sample; not definitional)

- Audit trail of key operations (who/what/when) — all sampled products; compliance-driven market expectation. Judgment call: held at L1 because a KMS without audit is still recognizable as a KMS, though it would be unsellable in the regulated market.
- FIPS-validated modules / HSM backing — near-universal (AWS FIPS 140-3 L3; Fortanix FIPS 140-2 L3; Thales Luna FIPS-validated; Vault FIPS 140-3 mode). Held at L1: Vault transit without HSM is still recognized as key management; protected custody is the invariant, HSM is the dominant implementation.
- Per-key access control with administrator/user separation (key policies/grants; app permissions; ACL paths).
- Envelope encryption / data-key pattern (GenerateDataKey; datakey; wrap/unwrap).
- Rotation with old-version retention for decryption (HBK versions; keyring; key links).
- Key state model with enable/disable and controlled deletion (waiting periods, undo windows).
- Import of external key material (BYOK) with wrapping and verification (KCV).
- Multi-interface support: REST API + KMIP and/or PKCS#11 (+ CNG/JCE in the enterprise pole).
- HA/clustering and backup/restore of the key store.
- Dual control / quorum approval for sensitive operations — common in the enterprise pole (Fortanix quorum policies; ceremony heritage); not universal (AWS uses scheduled-deletion windows instead). Held at L1, marked posture-dependent.

### L2 — Variant / Optional Structure

- Custody posture: never-exposed (AWS default, Vault transit) vs. delivered-to-endpoint (KMIP storage profiles) vs. external key store / HYOK (XKS, EKM).
- Encryption surface packaging: application-level API crypto; database TDE custody; file/volume encryption agents; tokenization/FPE; code signing — bundled differently per vendor.
- Secrets management on the same platform (Fortanix Secret objects; Vault KV) — packaging, not definitional.
- Deployment: hyperscaler-managed service; self-hosted cluster/appliance; SaaS; cloud marketplace.
- PQC algorithm support (ML-KEM/ML-DSA/XMSS/LMS/SLH-DSA) — era-current, unevenly distributed.
- Convergent encryption / key derivation (Vault); local key caching/accelerators (Fortanix); confidential-computing attestation (Fortanix SGX).
- Multi-region/multi-cloud key replication (AWS multi-region keys; Fortanix account replication).
- Key discovery/inventory of keys held elsewhere (Fortanix Key Insight as a separate product) — adjacent capability.

### L3 — Vendor-specific (research notes only)

- AWS: HBK/domain-key/derived-key hierarchy; grants; aliases; customer/AWS-managed/AWS-owned key classes; RotateKeyOnDemand; XKS proxy architecture; CloudTrail integration.
- Fortanix: SGX enclave + DCAP attestation; DSM Accelerator (local key cache, in-memory crypto); Secure Business Logic (Lua plugins inside HSM); BIP32/SLIP10 wallet-key support; Key Undo Policy; group-level cryptographic/metadata policies; KCV/CMAC display; tokenization as key types.
- Vault: engine mount model; `vault:v1:` ciphertext prefix; min_decryption_version archiving; convergent-encryption version history; managed keys; Transform engine (FPE); KMIP/Key Management engines as ENT features.
- Thales: CTE agent architecture; CCKM; DPoD marketplace; Luna HSM family; Crypto Command Center (structure-level only; internals unverified).

## Vendor-specific Findings → Rejected as Core

- "Key management includes secrets management" — rejected. Secrets (passwords, API keys, tokens) are a different Type; coexistence on one platform (Fortanix, Vault) is packaging. The keys-vs-secrets object difference and governance depth define the boundary.
- "Key management includes certificate lifecycle" — rejected. Certificates bind identities to keys with issuance/renewal workflows (PKI); KMS holds raw keys and may back a CA's keys. Fortanix certificate objects and Vault PKI engine confirm adjacency, not identity.
- "Tokenization is part of key management" — rejected as core; optional bundled capability (Fortanix tokenization keys; Vault Transform).
- "The KMS itself must perform the encryption" — rejected. The KMIP delivery model (device/database encrypts locally with delivered keys) satisfies the Type; the invariant is policy-gated use, not who executes the cipher.
- "HSM required" — rejected as strict requirement; dominant market expectation (L1) but Vault transit without HSM remains recognizable key management.
- "Cloud-only / API-only" — rejected; on-prem/self-hosted pole (Fortanix on-prem, Vault self-hosted, Thales appliances) and KMIP-era products fit the core.

## Boundary Findings

- **vs Secrets Management** (adjacent leaf): secrets are credentials (passwords, API keys, tokens, connection strings) whose value is consumed by applications; keys are cryptographic material whose lifecycle and use the system governs for data protection. Test: strip lifecycle/audit/compliance machinery → you have a secret store; strip secret-value storage → you have a KMS. Vault and Fortanix straddle by packaging; the Type boundary is by object and governance, not by vendor. Note: the directory also carries "Secrets Management" (§14) and "Secrets Security" (§15) as separate leaves — overlap risk flagged in STATUS.
- **vs PKI Management / Certificate Lifecycle Management** (adjacent leaves): certificates = CA-issued identity bindings with validity, issuance, renewal, revocation publication; keys = raw cryptographic material. A KMS may generate/store the CA's keys; a cert manager consumes them. Test: remove issuance/identity-binding → KMS territory; remove raw-key custody → cert manager territory.
- **vs Password Manager**: end-user credential vault; no cryptographic service offered to other systems; no key lifecycle governance.
- **vs Crypto Wallet / Digital Asset Custody**: blockchain key custody for asset control; different users, objects, and workflows (signing transactions, addresses), even though "key custody" rhymes.
- **vs DSPM / Data Access Governance**: discovery/classification/policy over data stores; no key custody or crypto service.
- **vs database/storage encryption features (TDE, LUN/disk encryption)**: those are consumers of this Type. The Type appears when custody + lifecycle + policy move to a governed external custodian.
- **"Encryption" half of the leaf name**: realized through the use leg — the same system that holds keys commonly drives encryption at application level (API), database level (TDE via KMIP/PKCS#11), file/volume level (agents), and cloud level (BYOK/XKS/EKM). No separate definitional leg is needed; "encryption management" without key custody is not this Type.

## Uncertainties

- Thales CipherTrust Manager operational internals (key states, quorum, domains, KMIP profile coverage) unverified — deep docs unreachable (403; JS-rendered portal). Enterprise-pole operational claims are carried by Fortanix/AWS/Vault evidence; Thales is used only for product-structure evidence. Assertion strength reduced accordingly.
- Whether audit belongs in L0 or L1 is a judgment call; held at L1 (recognizability test) with the note that market expectation is near-universal.
- Exact KMIP profile coverage per product not verified (only that KMIP interfaces exist in Fortanix and Vault ENT).
- Historical tape-era products were checked against the KMIP standard and general practice, not against a fetched product manual (IBM docs 403). The historical-fit conclusion is therefore inference from the standard + modern docs, marked as such.
- Market-share/leadership claims deliberately avoided (no evidence gathered).

## Final Synthesis

An Encryption & Key Management application is the organization's custodian and governor of cryptographic keys: it holds keys of record under protected custody, administers their lifecycle from creation to destruction, and mediates their cryptographic use by authorized consumers under per-key policy, with an auditable record of every operation. The "encryption" half is the employment side: the same system typically drives encryption across application, database, file/volume, and cloud surfaces — via API crypto and envelope data keys, via key-delivery protocols (KMIP/PKCS#11) for TDE and storage devices, via agents, and via BYOK/external-key-store bridges to cloud services. Custody posture (never-exposed vs. delivered vs. external), surface packaging, deployment model, and algorithm era (incl. PQC) are variants. The Type is distinct from Secrets Management (credentials vs. keys), Certificate/PKI Management (identity bindings vs. raw keys), Password Manager (end-user credentials), and DSPM (no custody). Historical check passes: KMIP-era and ceremony-era key management satisfy the same three-part core without cloud, REST APIs, or mandatory HSMs.
