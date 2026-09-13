# Research Notes — Secrets Management

## Research Goal

Understand what a Secrets Management application really is by studying real products: what the managed object is, who consumes it, how access is controlled, what lifecycle machinery exists, and where the Type's boundaries sit against Password Manager, PAM, Encryption & Key Management, Certificate Lifecycle Management, Machine Identity Management, and Secrets Security.

## Initial Boundary

Working hypothesis before research:

- Core: centralized custody of sensitive credential material (passwords, API keys, tokens, connection strings) with controlled programmatic distribution to machines/pipelines and lifecycle machinery (rotation, revocation, audit).
- Likely users: DevOps/platform engineers, security teams, application developers; consumers are applications, CI/CD pipelines, operators via tooling.
- Nearest neighbors: Password Manager (human at login), PAM (privileged account mediation), Encryption & Key Management (cryptographic keys), Certificate Lifecycle Management (certificates), Machine Identity Management (actor records), Secrets Security (leak detection), Configuration Management (desired-state enforcement), CI/CD platforms (pipeline variables).
- Unknowns: Is dynamic/short-lived credential generation definitional or variant? Is rotation definitional? Is encryption-at-rest by the product itself definitional? Is the human-facing UI definitional?

## Research Questions

1. What exactly counts as a "secret" in these products? What material is stored?
2. What is the unit of record — secret, name/path, version? How is versioning handled?
3. How do consumers authenticate and get authorized (identity kinds, policy models)?
4. How is delivery done (API, SDK, CLI, agent/sidecar/injector, sync to platforms)?
5. What lifecycle operations exist (create, version, rotate, revoke, expire, delete/destroy, recover)?
6. What governance exists (audit, RBAC, segmentation/namespaces)?
7. What interfaces exist (CLI, API, UI, agents)?
8. Dynamic secrets vs static secrets — definitional or variant?
9. Encryption at rest — definitional or common?
10. Boundaries: vs password manager, PAM, KMS, CLM, machine identity, CI/CD variables, config management.

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| HashiCorp Vault | self-hosted/OSS archetype; richest engine model | canonical DevOps vault; dynamic secrets origin |
| AWS Secrets Manager | hyperscaler managed service | simplest managed model; vendor-documented boundary statements |
| CyberArk Conjur OSS (+ Palo Alto Idira Secrets Manager page) | enterprise policy/machine-identity pole | policy-as-code access; enterprise lineage |
| Doppler | developer-first SaaS | env-var-shaped secrets; sync/integration model; smaller-team tier |
| Azure Key Vault | cloud suite pole (secrets beside keys & certificates) | boundary vs KMS/CLM inside one product; minimal-lifecycle pole |

## Sources

Research date: 2026-09-09. All Tier 1 (official operational documentation) unless noted.

- HashiCorp Vault — developer.hashicorp.com/vault/docs (product docs home), /vault/docs/secrets (secrets engines), /vault/docs/secrets/kv (KV engine), /vault/docs/auth (auth methods), /vault/docs/audit (audit devices)
- AWS Secrets Manager — docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html, /retrieving-secrets.html, /rotating-secrets.html, /auth-and-access.html
- CyberArk Conjur OSS — github.com/cyberark/conjur (README: architecture, authenticators, rotators, cryptography)
- Palo Alto Networks Idira Secrets Manager — conjur.org (redirects to PAN Idira "Secrets Manager" product page; Tier 2 positioning + FAQ)
- Doppler — docs.doppler.com (welcome, llms.txt index, /docs/secrets)
- Azure Key Vault — learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets, /azure/key-vault/general/about-keys-secrets-certificates

Sourcing limitations: CyberArk's own Conjur docs portal (docs.conjur.org / docs.cyberark.com) was not directly reachable in this pass (404 on the attempted overview URL); Conjur evidence is from the official GitHub README (Tier 1 for the OSS product) plus the PAN Idira product page (Tier 2). No precise numeric limits (secret sizes, TTL defaults, version counts) are asserted in the final document beyond what fetched pages state.

## Product A — HashiCorp Vault (evidence layer A)

From official docs (fetched 2026-09-09):

- Positioning: "Centralize secret management, rotate old credentials, generate credentials on demand, audit client interactions, and support regulatory compliance."
- "Why use Vault" pages: manage static secrets ("Store, rotate, and encrypt arbitrary strings as key-value pairs"); manage certificates (PKI integration); manage identities and authentication (managed entities, identity tokens, OIDC, workload identity federation); manage 3rd-party secrets ("Generate and revoke on-demand credentials and control access to external encryption keys and cloud credentials"); manage sensitive data (encrypt/tokenize); regulatory compliance (HSM/FIPS/PKCS11).
- **Secrets engines**: "components which store, generate, or encrypt data… Some secrets engines simply store and read data… Other secrets engines connect to other services and generate dynamic credentials on demand. Other secrets engines provide encryption as a service, totp generation, certificates, and much more." Engines are enabled at a **path**; behave "similar to a virtual filesystem, supporting operations like read, write, and delete." Engine lifecycle: enable / disable (revokes secrets, deletes data) / move / tune. Engines are isolated ("barrier view" — chroot-like).
- Engine catalog: KV, AWS, Azure, GCP, databases, Kubernetes, Nomad, MongoDB Atlas, LDAP, OS local accounts, PKI, SSH, TOTP, Transit (encryption as a service), Transform, KMIP, SPIFFE, HCP Terraform, Cubbyhole, Identity, Google Cloud KMS, Key Management (ENT).
- **KV engine**: "a generic key-value store used to store arbitrary secrets"; v1 non-versioned (overwrite), v2 versioned ("a key can retain a configurable number of versions"; check-and-set; delete marks deleted, undelete possible; `destroy` permanently removes; metadata delete removes all versions).
- **Auth methods**: "components in Vault that perform authentication and are responsible for assigning identity and a set of policies to a user." Catalog: AppRole, AWS, Azure, GCP, GitHub, Kubernetes, JWT/OIDC, Kerberos, LDAP, Login MFA, OCI, Okta, RADIUS, SAML, SCEP, SPIFFE, TLS certificates, tokens, userpass. Mounted under `auth/`; disabling logs out users.
- **Audit devices**: "record all API requests and responses in detail" (file/syslog/socket); disabled by default at init; sensitive values HMAC-hashed; if all audit devices unavailable Vault refuses to service requests.
- Tools: Vault Agent and Proxy (delivery machinery); CLI, GUI, APIs as peer surfaces.

## Product B — AWS Secrets Manager (evidence layer A)

From official user guide (fetched 2026-09-09):

- "helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles."
- Value framing: "you no longer need hard-coded credentials in application source code… You replace hard-coded credentials with a runtime call to the Secrets Manager service to retrieve credentials dynamically when you need them."
- Rotation: "the process of periodically updating a secret. When you rotate a secret, you update the credentials in both the secret and the database or service." Two forms: managed rotation (for managed secrets, no Lambda) and rotation by Lambda function (for other types). "This enables you to replace long-term secrets with short-term ones."
- **Vendor-documented boundary routing**: "AWS credentials – We recommend AWS Identity and Access Management. Encryption keys – We recommend AWS Key Management Service. SSH keys – We recommend Amazon EC2 Instance Connect. Private keys and certificates – We recommend AWS Certificate Manager."
- Access control: IAM provides authentication and access control; identity-based and resource-based policies; ABAC; cross-account access; on-prem access documented.
- Encryption: KMS keys encrypt secrets; AWS managed key `aws/secretsmanager` default.
- Retrieval: SDKs (Java/Python/.NET/Go/Rust/C++/JavaScript/Kotlin/PHP/Ruby), AWS CLI, console, EKS, Lambda, Batch, IoT Greengrass, GitHub jobs, GitLab, CloudFormation, Parameter Store integration. "Secrets Manager generates a CloudTrail log entry when you retrieve a secret."
- Pricing: pay per use; no charge for secrets marked for deletion (implies deletion workflow).

## Product C — CyberArk Conjur OSS / Palo Alto Idira Secrets Manager (evidence layer A for OSS README; layer A/B for PAN page)

From the official GitHub README (fetched 2026-09-09):

- "Conjur provides secrets management and application identity for modern infrastructure."
- **MAML** ("Machine Authorization Markup Language"): "a role-based access policy language to define system components & their roles, privileges and metadata."
- REST web service to: "manage identity life cycles for humans and machines; organize and search roles and data in your secrets infrastructure; authorize access to resources using a sophisticated permission model; store secrets and make them available securely."
- Integrations "throughout the cloud toolchain": IaaS, configuration management, CI/CD, container management.
- Architecture: Docker + PostgreSQL backing store; **Authenticators** (enable/disable built-in, secure via policy files, create custom); **Rotators** ("Rotate variables regularly using built-in rotators"); secrets/keys encrypted in the database (AES-256-GCM via Slosilo; roles have API keys stored encrypted; token signing key stored encrypted); master data key required at startup ("Do NOT lose the data key, or all the encrypted data will be unrecoverable"); multi-account (multi-tenant) with per-account token-signing keys.
- Migration path documented to "CyberArk Secrets Manager, Self-Hosted."

From the PAN Idira Secrets Manager product page (conjur.org redirect; Tier 2):

- "Enterprise vault and lifecycle automation for secrets and credentials, with unique and universal identity for every workload across any environment."
- "Store and manage API keys, tokens, passwords, certificates and database credentials from a single platform."
- "Automated rotation and lifecycle controls… every secret has an owner, an expiration and an audit trail."
- "One identity to access any resource… universal cryptographic identity that retrieves secrets or authenticates directly to resources… Use identity-based access where environments support it and secrets where they don't."
- **Vendor-documented PAM boundary (FAQ)**: "While PAM secures privileged human access and sessions, Secure Secrets and Workloads governs nonhuman identities, secrets and workload access — giving security teams unified visibility, policy consistency and auditability across both human and machine identities."
- SaaS or self-hosted deployment; SPIFFE-based short-lived workload identities ("expire in hours, not years"); discovery/visibility across existing vaults.

## Product D — Doppler (evidence layer A)

From official docs (fetched 2026-09-09):

- Positioning: "Secrets management is hard and becomes more complex over time. Doppler scales as you do and comes with fine grained access controls, logs, versioning, and a seamless CLI right out-of-the-box."
- Structure: Workplace → Projects → Environments → Configs (branch configs, config inheritance, cloning, lock/unlock).
- **Secrets**: env-var-shaped names (uppercase/underscore only); import from ENV/JSON/YAML files or other configs; update across environments (cascade); missing-secret detection; visibility levels; value types (JSON/URL/UUID/etc. validation); secret age; reminders (rotation nudges); generation; **version history**; **redaction** (permanent removal of historical values; current version handled via Restricted visibility); notes; multi-line secrets (PEM/SSH keys); **referencing** (`${SECRET_NAME}`, across configs/projects); reserved secrets (DOPPLER_PROJECT etc.); cascading changes.
- **Access**: service tokens ("Provide restricted secrets access to applications in live environments" — read-only to a specific config); service accounts + API tokens; **OIDC identities** (EC2, GitHub, Kubernetes operator federation — "Returns a short lived API token"); SAML SSO + SCIM; user groups, custom roles, advanced permissions; MFA; trusted IPs.
- **Delivery**: CLI (`doppler run` injects secrets into applications as environment variables); TUI; VS Code/JetBrains extensions; SDKs (JS/Python/Go/.NET/Ruby/Elixir); Docker (CLI in image, container env vars, encrypted fallback snapshots); Kubernetes (Operator with deployment auto-reload, External Secrets Operator provider); **syncs/integrations** pushing secrets to AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, Parameter Store, CI/CD platforms (GitHub/GitLab/Bitbucket/CircleCI/Jenkins…), PaaS (Vercel/Netlify/Render/Heroku…), Terraform Cloud.
- **Rotation**: "proxied and API secrets rotation models… two secret strategy" for zero-downtime; per-service rotation guides (AWS IAM, Azure service principal, GCP service account, databases, OpenAI/SendGrid/Twilio tokens).
- **Dynamic secrets**: leases (issue/revoke) for AWS IAM / Azure service principals.
- **Audit**: activity logs (with rollback of changes), access logs, audit API, log forwarding (SQS/Datadog/Splunk/Slack/webhook).
- Governance extras: change requests with approval policies; project templates; webhooks; analytics dashboards (secret health, stale secrets); enterprise key management (customer-controlled encryption key / EKM for AWS KMS & GCP KMS).

## Product E — Azure Key Vault (evidence layer A)

From official Microsoft Learn docs (fetched 2026-09-09):

- "Key Vault provides secure storage for generic secrets, such as passwords and database connection strings."
- **Semantics-free storage**: "The Key Vault service doesn't provide semantics for secrets. It merely accepts the data, encrypts it, stores it, and returns a secret identifier (`id`)." contentType field as an interpretation hint ("There are no predefined values").
- Encryption: "Key Vault stores all secrets in your key vault as encrypted data… a hierarchy of encryption keys, with all keys in the hierarchy protected by FIPS-validated modules… transparent and requires no action from you."
- **Attributes**: exp (expiration, default forever), nbf (not before, default now), enabled (default true) — operations outside the window "automatically disallowed"; created/updated read-only per version. Get works for not-yet-valid and expired secrets (test/recovery use).
- **Access control**: at the vault level; secrets policy distinct from keys policy; permissions: get, list, set, delete, recover, backup, restore + privileged purge; RBAC recommended over legacy access policies.
- Tags (application metadata); object identifiers `https://<vault>.vault.azure.net/secrets/<name>/<version>`; versioning: "Key Vault versions objects whenever you create a new instance of an object… omitting the version gets the latest."
- Object siblings: keys (cryptographic), secrets, certificates ("built on top of keys and secrets and add an automated renewal feature"), storage account keys (deprecated).
- Usage scenario: "Securely store, manage lifecycle, and monitor credentials for service-to-service communication like passwords, access keys, service principal client secrets."
- Notably ABSENT: automatic rotation of secret values (no rotation engine; near-expiry eventing exists elsewhere in the service), dynamic credential generation.

## Cross-product Comparison

| Dimension | Vault | AWS Secrets Manager | Conjur OSS / Idira | Doppler | Azure Key Vault |
|---|---|---|---|---|---|
| Unit of record | secret at a path (KV versions; engine-specific objects) | secret (name + versions) | variable (policy-addressed resource) | secret (name in a config) | secret (name + version, identifier URL) |
| Material | arbitrary strings/KV; dynamic creds; certs; keys | DB creds, API keys, OAuth tokens, arbitrary | variables (opaque values) | env-var-shaped values incl. multi-line PEM | opaque octets (≤ size cap), contentType hint |
| Versioning | KV v2 versions + CAS + undelete/destroy | versions per secret | (not emphasized in OSS README) | version history + rollback + redaction | versions; latest-by-default get |
| Access model | auth methods → identity + policies (path-scoped ACLs) | IAM identity/resource policies + ABAC | MAML role policy + authenticators | service tokens / service accounts / OIDC + project permissions | vault-level policies or RBAC (Entra ID) |
| Primary consumption | API/CLI/SDK; Agent/Proxy injection | SDK/CLI/console; EKS/Lambda/GitHub/GitLab | REST API + integrations | CLI injection (`doppler run`), SDKs, K8s operator, syncs | API/SDK/portal; RBAC-gated |
| Rotation | dynamic engines generate+revoke on demand; KV manual | managed rotation or Lambda function | built-in/custom rotators | proxied/API rotation, two-secret strategy | none built-in (manual; expiry attributes only) |
| Dynamic/short-lived creds | yes (core engine family) | rotation toward short-term; managed rotation | workload identity emphasis (PAN page) | dynamic secrets with leases | no |
| Encryption at rest | barrier + storage encryption | KMS (managed or CMK) | AES-256-GCM in PostgreSQL | platform encryption + optional customer-managed EKM | FIPS-validated key hierarchy, transparent |
| Audit | audit devices (all requests, HMAC-hashed; opt-in) | CloudTrail entries (incl. retrieval) | (audit machinery in suite) | activity logs + access logs + audit API | diagnostics/monitoring (configurable) |
| Deletion semantics | delete→undelete; destroy; metadata delete | delete → scheduled window → recovery | — | delete; redaction for history | soft delete → recover → purge |
| Human UI | GUI | console | (suite consoles) | dashboard (primary authoring surface) | portal |
| Deployment | self-hosted OSS/ENT + HCP managed | managed service only | self-hosted OSS; SaaS/self-hosted (Idira) | SaaS | managed service (+ Managed HSM for keys) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The secret as managed object of record** — a persistent, individually addressable named record holding sensitive credential material (passwords, API keys, tokens, connection strings, key/certificate material), held under the system's own protection (encryption at rest the universal realization), with versions/history retained. Remove → scattered credentials in config files / an encrypted flat file; no store of record.
2. **Identity-gated programmatic access** — consumers (applications, pipelines, operators through tooling) authenticate as identities (human or machine) and are authorized by policy to retrieve and manage specific secrets through programmatic interfaces; every read is mediated and attributable. Remove → a shared encrypted file or config store anyone with the file can read; the control is gone.
3. **The managed lifecycle of the stored population** — the system maintains the population over time: versioning with current-version semantics, enable/expire state, deletion with recovery/destroy semantics, and (as the common mature realization) rotation/replacement of values. Remove → a static encrypted snapshot; the "management" is gone.

Jointly-held load-bearing:

- 1 alone = encrypted config store / encrypted .env file
- 2 without 1 = an authorization proxy over nothing
- 3 without 1+2 = a credentials spreadsheet with reminders
- 1+2 without 3 = a static vault (recognizable but degenerate; every sampled product carries the lifecycle leg)
- 1+3 without 2 = a personal encrypted archive (drifts toward password-manager territory)
- 2+3 without 1 = access machinery with nothing held

### L1 — Common Mature Structure

- Rotation machinery (scheduled or triggered value replacement; AWS managed/Lambda, Conjur rotators, Doppler rotated secrets, Vault KV+dynamic engines) — near-universal but Azure Key Vault proves non-definitional
- Dynamic / short-lived credential generation with leases (Vault dynamic engines, Doppler dynamic secrets, PAN workload identities) — major capability, not definitional (Azure pole lacks it)
- Audit trail of access and change (Vault audit devices, AWS CloudTrail, Doppler activity/access logs, PAN "audit trail") — near-universal; realization varies (opt-in vs built-in vs external service)
- Delivery machinery beyond direct API: agents/sidecars/injectors (Vault Agent/Proxy, Doppler CLI run, K8s operators/ESO), sync/push to platforms and CI/CD (Doppler syncs, Vault Secrets Sync ENT, AWS EKS/GitHub/GitLab retrieval paths)
- Human-facing admin UI beside the programmatic core (all five)
- Segmentation/organization of the secret population (Vault paths/namespaces, Doppler projects/configs/environments, Azure vaults, Conjur accounts/policies, AWS region/account + tags)
- Human identity federation (SSO/OIDC/LDAP) alongside machine authentication
- Soft-delete/recovery windows (AWS, Azure, Vault KV v2, Doppler redaction as the history analogue)

### L2 — Variant / Optional Structure

- Secret shape: opaque strings (Azure "no semantics"), key-value pairs (Vault KV, AWS), env-var-shaped records with value types and referencing (Doppler), policy-addressed variables (Conjur)
- Dynamic-secret posture: engine-based on-demand generation (Vault) vs lease-based (Doppler) vs identity-first "secrets where identity isn't supported" (PAN) vs none (Azure)
- Encryption substrate: product-managed hierarchy (Azure), cloud KMS/CMK (AWS, Doppler EKM), database-level AES (Conjur), HSM/FIPS backing (Vault ENT, Azure Managed HSM for keys)
- Deployment: self-hosted OSS (Vault, Conjur), managed SaaS (AWS, Azure, Doppler, HCP, Idira SaaS), hybrid
- Sync/push topology: pull-only (Azure) vs sync-to-platforms (Doppler, Vault Secrets Sync)
- Governance depth: change requests/approval workflows (Doppler), policy-as-code (Conjur MAML), ABAC/tags (AWS)
- Adjacent engines inside the vault: PKI/certificate issuance (Vault PKI engine — CLM-adjacent machinery as deployment variant per the pki-management pass), encryption-as-a-service (Transit), TOTP, SSH — the vault as platform vs the pure secret store
- Customer tier: developer-team SaaS (Doppler) ↔ enterprise estate (Idira, Vault ENT)

### L3 — Vendor-specific (research notes only)

- Vault: barrier view isolation; mount-path case sensitivity; audit-device refusal-to-serve behavior; KV v1 vs v2 endpoint differences; Secrets Sync/Import ENT; Vault Radar (secrets detection — different Type); Agentic IAM/MCP server (era-current)
- AWS: Lambda-based rotation functions; managed rotation for service-linked secrets; `aws/secretsmanager` managed key; Parameter Store integration; pay-per-secret pricing; AI Coding Agents retrieval page (era-current)
- Conjur: Slosilo crypto library; CONJUR_DATA_KEY master key; per-account token-signing keys; MAML; migration guide to CyberArk Secrets Manager Self-Hosted; PAN Idira SPIFFE identities
- Doppler: reserved secrets (DOPPLER_PROJECT/ENVIRONMENT/CONFIG); invisible-character warnings; missing-secret detection with dismissal; config lock/unlock; Doppler Share (one-off secret sharing links — adjacent to share utilities); GnuPG CLI install requirement
- Azure: 25 KB per-secret size cap; 15 tags cap; contentType hint field; storage account keys (deprecated); certificates built on keys+secrets; Managed HSM pools don't hold secrets

## Vendor-specific Findings

See L3. Cross-vendor packaging observation: the same vendors split the market themselves — Bitwarden Secrets Manager and Keeper Secrets Manager ship as separate products beside their password managers (password-manager pass evidence); every sampled PAM suite ships a machine-facing secrets sibling (PAM pass evidence); HashiCorp ships Vault Radar (detection) beside Vault (custody). This is strong packaging evidence that custody-for-machines, detection-of-leaks, human-password-custody, and privileged-account-mediation are distinct Types.

## Boundary Findings

1. **vs Privileged Access Management (§15, pre-hung flag — RATIFIED from this side)**: PAM mediates gated access to privileged accounts on target systems (credential disclosure/checkout or brokered sessions, session recording, human accountability); Secrets Management serves programmatic consumption of credential material by machines/pipelines. PAN's own FAQ draws the same line ("While PAM secures privileged human access and sessions, Secure Secrets and Workloads governs nonhuman identities, secrets and workload access"). Overlap zone: PAM suites increasingly cover non-human identities and ship secrets siblings; secrets managers store privileged-account passwords as opaque secrets. Keep-both; seam = primary consumer + mediation style (API retrieval of material vs gated use of an account).
2. **vs Password Manager (§15, pre-hung flag — RATIFIED from this side)**: person-at-a-login consumption of personal/organizational login credentials vs machine-via-API consumption of infrastructure/application credentials. Vendors split the space (Bitwarden Secrets Manager, Keeper Secrets Manager, 1Password secrets automation as separate products). Overlap zone: secrets managers store some human-facing material (Conjur "privileged users and machine identities"; Vault TOTP engine); password managers gain API surfaces. Keep-both; seam = who/what consumes at the point of use.
3. **vs Machine Identity Management (§15, processed — RATIFIED from this side)**: machine identity holds actor-centric records (the machine actor is the record; credential kind is an attribute); secrets management holds credential-material-centric records (the secret is the record; the consumer identity is the access gate, not the record). That pass's own test ("2 without 1 = credential store = secrets management") confirms from this side. Keep-both.
4. **vs Encryption & Key Management (§15, processed — RATIFIED from this side)**: KMS holds cryptographic keys for policy-gated crypto operations (encrypt/decrypt/sign; key material typically never leaves); secrets management holds authentication/configuration material that consumers retrieve and take away. AWS's own routing ("Encryption keys – We recommend AWS Key Management Service") and Azure's distinct keys-vs-secrets object types with distinct permission sets confirm. Overlap zone: secrets managers encrypt their stores using KMS keys; vaults may hold key material as opaque secrets. Keep-both.
5. **vs Certificate Lifecycle Management (§14, processed — RATIFIED from this side)**: certificates carry issuer/validity/trust semantics external to the storing system; secrets are opaque material. That pass's test ("manage opaque secrets/keys instead → Secrets/Key Management") confirms. Overlap zone: certificate material stored as opaque secrets (Azure contentType hint; PAN lists certificates); Vault's PKI engine is CLM-adjacent machinery inside a secrets manager (deployment variant per the pki-management pass). Keep-both.
6. **vs Secrets Security (§15, UNPROCESSED — forward note)**: detection of exposed/hardcoded secrets in code, repositories, and scanned surfaces (scanner posture) vs custody and delivery of secrets (vault posture). HashiCorp ships Vault Radar (detection) as a separate product beside Vault (custody) — packaging evidence. The secrets-security pass should center detection/remediation of leaks, not custody. Keep-both expected.
7. **vs Configuration Management (§14, processed)**: config management enforces desired state on node populations; secrets handling there is integration (encrypted vars, vault integrations — that pass's own evidence). Keep-both.
8. **vs CI/CD platforms (§12)**: pipeline secrets/variables are an embedded capability of the pipeline Type (GitLab CI/CD variables, GitHub Actions secrets — continuous-integration pass evidence); dedicated secrets managers are the organization-wide system of record the pipeline consumes (AWS documents GitHub/GitLab retrieval; Doppler syncs to pipelines). Adjacent, keep-both.
9. **vs PaaS Management Console (§14, processed)**: app-scoped config vars/env vars at application grain vs organization-wide credential custody with identity-gated access and lifecycle. Adjacent.
10. **Internal boundary — encrypted flat file / .env store**: an encrypted credentials file fails legs 2 and 3 (no identity-gated mediated access, no managed lifecycle) — this is the lower boundary of the Type. Kubernetes Secrets (platform-native pole) satisfies all three legs (named secret objects, RBAC-gated API retrieval, create/update/delete lifecycle) even where at-rest encryption is delegated to the storage layer — held as the platform-native realization, with the at-rest-protection nuance recorded under Uncertainties.

## Uncertainties

- Conjur OSS docs portal not directly fetched (404); Conjur observations rest on the official GitHub README + PAN product page. Policy/variable mechanics described at README level only; no precise Conjur operational claims made in the final document.
- At-rest encryption as invariant: Kubernetes Secrets without etcd encryption is a known platform-native counter-shape (base64 by default, encryption optional). Held as: protection under the system's own access control is the invariant; product-managed encryption at rest is the universal market realization. Not asserted as a hard invariant in the final document.
- Versioning as invariant: Conjur OSS README does not emphasize variable versioning; versioning is universal in the other four. Held as common-mature rather than definitional; the lifecycle leg is phrased to survive a non-versioning pole.
- Precise numeric limits (Azure 25 KB cap, tag caps, KV version-count defaults) recorded here only; excluded from the final document per evidence-calibration rules.
- Secrets Security (§15) unprocessed — the custody-vs-detection seam is a forward note, not yet ratified from that side.

## Final Synthesis

A Secrets Management application is the organization's **machine-facing credential store of record**: it holds sensitive credential material as named, addressable, protected records; it mediates every retrieval through authenticated, policy-authorized programmatic access; and it maintains the stored population over time (versions, enable/expire states, deletion/recovery, and commonly rotation). Everything else — dynamic short-lived credentials, agents/sidecars, platform syncs, human UIs, SSO, change approvals, compliance machinery — is the mature market's standard or variant layering on that core. The defining seams: password managers serve the person at a login; PAM mediates gated use of privileged accounts; KMS serves cryptographic operations with keys that stay; CLM manages certificates with trust semantics; machine identity manages actor records; secrets security detects leaked secrets. This Type is where the material itself is the record and the machine is the consumer.
