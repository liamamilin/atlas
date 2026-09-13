# Research Notes — PKI Management

## Research Goal

Understand what a **PKI Management** application is from real products: what objects it manages, what workflows it runs, what rules govern it, and where its boundary lies against Certificate Lifecycle Management, Secrets Management, and Encryption & Key Management.

## Initial Boundary

Directory position: section 14 (IT, Cloud & Infrastructure), between "Certificate Lifecycle Management" and "Message Queue Management".

Working hypothesis at start:

- PKI Management = the operator-facing application for **running certificate authority infrastructure**: CA hierarchy and keys, policy-constrained issuance, revocation and verification services, issuance records.
- Nearest neighbors: Certificate Lifecycle Management (estate of deployed certificates), Secrets Management, Encryption & Key Management, Machine Identity Management.
- Expected complication: commercial suites fuse PKI and CLM; the seam must be found, not assumed.

## Research Questions

1. What are the core objects? (CA, hierarchy, keys, policy objects, end entities, certificates, CRLs/OCSP)
2. How does the enrollment → issuance loop work, and through which protocols/surfaces?
3. How does revocation work, and what verification services does the authority expose?
4. What does the CA's own lifecycle look like (create, activate, renew, revoke, expire)?
5. What does "management" add beyond a key pair + signing script?
6. Where exactly is the seam to Certificate Lifecycle Management?
7. Which capabilities are definitional vs common vs variant vs vendor-specific?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| **EJBCA (Keyfactor)** | open-source-rooted full-featured enterprise CA software; national eID / IoT / enterprise poles | deepest object model; longest-running CA software project |
| **Microsoft Active Directory Certificate Services (AD CS)** | platform-native PKI bundled with Windows Server | platform-native pole; role-service decomposition |
| **DigiCert Private CA (DigiCert ONE)** | vendor-operated managed private CA service | managed/cloud pole; suite-split evidence vs CLM |
| **HashiCorp Vault PKI secrets engine** | API-driven dynamic/short-lived CA embedded in a secrets manager | devops pole; minimal-CA pole; single-root pole |
| **Smallstep step-ca** | modern open-source online CA, ACME-first, passive revocation | minimal-pole stress test; explicit limitations list |

## Sources

All fetched 2026-09-09.

- EJBCA — docs.keyfactor.com/ejbca/: Introduction, EJBCA Concepts, Certificate Authority Overview (Tier 1, direct)
- HashiCorp Vault — developer.hashicorp.com/vault/docs/secrets/pki and /pki/setup (Tier 1, direct)
- Microsoft Learn (archived) — AD CS Overview, Windows Server 2012 R2 (Tier 1, direct; archived official doc)
- DigiCert — docs.digicert.com index and DigiCert Private CA section page (Tier 1, direct)
- Smallstep — smallstep.com/docs/step-ca/ (introduction) and /docs/step-ca/revocation/ (Tier 1, direct)

**Source-access limitations:**

- DigiCert CA Manager / Enterprise PKI Manager detail pages returned 404 on two URL attempts; abandoned per retry rule. DigiCert observations are limited to the docs index and the Private CA positioning page; no CA Manager UI specifics are claimed.
- Microsoft's current-version AD CS certificate-templates pages returned 404 on two URL attempts; abandoned. ADCS observations rely on the archived official overview (role services, purpose). Template machinery specifics for ADCS are NOT claimed.
- No third-party sources were needed; Tier 1 coverage was sufficient.

## Product Observations

### EJBCA (Keyfactor) — evidence layer A

From Introduction, Concepts, and CA Overview (official docs):

- Self-description: "one of the longest running CA software projects"; implements PKI per X.509 / IETF-PKIX; use cases named: national eID, industrial IoT platform, internal PKI.
- Deployment types: SaaS, Cloud, Software Appliance, Hardware Appliance, Container, Software stack.
- Issuance: "powerful profiles that give you fine-grained … control over the identities and properties of your cryptographic certificates"; automated validation of submitted keys and certification requests; enrollment protocols: **ACME, EST, CMP, SCEP, Microsoft Auto-enrollment**.
- Revocation/renewal: administrator tools to "revoke and renew certificates"; validation via **CRL and OCSP**.
- Core concepts (direct definitions):
  - **Root CA** — self-signed, "Trusted Root"; "must somehow be configured as a trusted root for all clients in the PKI".
  - **Sub CA** — certificate signed by another CA; part of a chain ending at the Root CA.
  - **RA (Registration Authority)** — "administrative function that registers entities in the PKI", trusted to identify/authenticate entities per CA policy; one or more RAs per CA.
  - **VA (Validation Authority)** — provides validity information: CRL (generated on a schedule) and OCSP (real-time; good / revoked / unknown); one or more VAs per CA.
  - **CA** — "issues certificates to and vouches for the authenticity of entities"; per-CA trust level tied to CP/CPS documents.
  - **End Entity** — "a user of the PKI, like a device, person, or server"; endpoint of the hierarchy; one EE can hold many certificates with the same identifying values; each EE enrolls against exactly one CA (its issuer).
  - **End Entity Profile** — template constraining enrollment values (Subject DN, SAN; available Certificate Profiles and CAs; values pre-set / default-modifiable / critical / optional).
  - **Certificate Profile** — constraints of issued certificates: extensions (presence/criticality/value), algorithms, key sizes; publishing decision.
  - **Crypto Token** — key storage abstraction: soft (PKCS#12 in DB) or PKCS#11 (HSM); each CA has exactly one.
  - **Publishers** — store issued certificates/CRLs to central locations: VA, LDAP, Active Directory, custom; direct or queued publishing.
  - **Validators** — check submitted keys/requests before/during/after signing (key-size constraints, weak-key block lists, CAA online checks); effects from warning to rejecting issuance.
  - **Peer Connector / External RA** — remote peer automation (e.g., publish revocation info to a VA); outbound-only CA operation.
- CA configuration: key pairs mapped to purposes (certSignKey, crlSignKey, keyEncryptKey for key recovery/escrow, testKey); signing algorithm; CA certificate self-signed / locally signed / externally signed via CSR.
- **Approvals**: approval profiles can require (multi-person) approval for: adding/editing end entities, key recovery, **revoking certificates**, activating CA services.
- **CA lifecycle statuses**: Uninitialized → Waiting for certificate response → Active → (Offline | Revoked | Expired | External CA); renewal with rollover certificates; Expired returns to Active via renewal; Revoked is terminal.
- CA/B Forum Baseline Requirements compliance notes (serial number entropy).
- CA types beyond X.509: CVC (EU ePassport), C-ITS ECA (Vehicle2X), SSH CA.

### HashiCorp Vault PKI secrets engine — evidence layer A

From PKI secrets engine overview and Setup (official docs):

- Self-description: "generates dynamic X.509 certificates"; services get certificates "without going through the usual manual process of generating a private key and CSR, submitting to a CA, and waiting for a verification and signing process"; Vault's built-in auth/authz provides the verification.
- Design philosophy: short TTLs → "revocations are less likely to be needed, keeping CRLs short"; ephemeral certificates possible (in-memory, discarded at shutdown).
- Setup flow (documented): enable engine → tune max TTL → **configure CA** (generate self-signed root internally, or import existing key pair; recommendation: keep root outside Vault, give Vault a signed intermediate) → **configure URLs** (issuing certificates endpoint, CRL distribution points) → **configure a role** ("maps a name in Vault to a procedure for generating a certificate"; allowed_domains, allow_subdomains, max_ttl).
- Usage: write to `/issue/<role>` → returns certificate, private key, issuing CA chain, serial number.
- Issuance protocols: ACME (open source); **EST, CMPv2, SCEP** (enterprise); CIEPS (external policy service, enterprise); PKI external CA mode (enterprise).
- Terraform resources confirm object model: CA config, **issuers**, **keys**, **roles**, CRL config, URLs config, ACME config/EAB, root/intermediate certificate flows, sign/issue endpoints, auto-tidy.
- Multiple issuers per mount supported (issuers config resource); rotation primitives documented.
- Full HTTP API; managed keys (external KMS) supported.

### Microsoft Active Directory Certificate Services — evidence layer A

From archived official AD CS Overview (Windows Server 2012 R2):

- Self-description: "the Server Role that allows you to build a public key infrastructure (PKI)"; "customizable services for issuing and managing digital certificates".
- Purpose: bind identity of person/device/service to a private key; certificates for confidentiality, integrity, authentication; applications: S/MIME, wireless, VPN, IPsec, EFS, smart card logon, SSL/TLS, digital signatures.
- Role services (direct evidence of decomposition):
  - **Certification Authority (CA)** — "Root and subordinate CAs are used to issue certificates to users, computers, and services, and to manage certificate validity."
  - **Web Enrollment** — browser-based certificate requests and CRL retrieval.
  - **Online Responder** — decodes revocation status requests, evaluates status, returns signed responses (OCSP).
  - **Network Device Enrollment Service (NDES)** — routers/network devices without domain accounts obtain certificates.
  - **Certificate Enrollment Policy Web Service** — obtain enrollment policy information.
  - **Certificate Enrollment Web Service** — HTTPS enrollment; together with policy web service enables policy-based enrollment for non-domain and off-domain machines.

### DigiCert Private CA (DigiCert ONE) — evidence layer A (limited depth)

From docs index and Private CA section page (official docs):

- Self-description: "helps you build and operate a privately trusted Public Key Infrastructure (PKI) for securing your organization's users, devices, applications, and digital assets across both on-premises and cloud environments"; "a private PKI issues certificates trusted only within your organization's systems".
- "Supports the full lifecycle of private trust management."
- Capability checklist (from the page's own capability summary): CRL types, OCSP, AIA, HSM support, protocols **ACME, CMP, EST, SCEP**, API, customizable certificate template, guidelines for certificate parameters (extensions, algorithms, validity, policies), post-quantum cryptography, user access permissions and roles, user activity audit log.
- Suite structure (from docs index): DigiCert ONE platform contains **CA Manager**, **Enterprise PKI Manager**, IoT Device Manager, Document Signing Manager, Secure Software Manager, Account Manager — plus **Trust Lifecycle Manager** ("Unify PKI operations and streamline digital trust management with automation, monitoring, and self-service tools") and **DigiCert Private CA** ("Secure private certificate authority (CA) services for managing your roots, intermediates, and X.509 certificate policy and issuance") as separate documented products. CertCentral = public CA side.
- Detail pages for CA Manager / Enterprise PKI Manager were unreachable (404 ×2); no UI-level claims made.

### Smallstep step-ca — evidence layer A

From step-ca introduction and Revocation docs (official docs):

- Self-description: "an online Certificate Authority (CA) for secure, automated X.509 and SSH certificate management"; "sane default algorithms and attributes, so you don't have to be a security engineer to use it securely".
- Uses: TLS certs for private infrastructure via **ACME**; automated renewal; add ACME to a legacy subordinate CA; short-lived SSH certificates via OAuth OIDC; customized X.509/SSH certificates.
- **Provisioners** = "methods of using the CA to get certificates … different modes of authorization": ACME challenge responses, OAuth OIDC ID tokens (Okta/Google/Entra/Auth0/Keycloak/Dex), cloud instance identity documents (AWS/GCP/Azure), single-use JWK tokens from CD tools.
- **Templates**: customize certificate fields (custom SANs/OIDs, restrict by domain/key size, CA path lengths); built-in + Go-template-based.
- Cryptographic protection: PKCS#11 HSMs, Google Cloud KMS, AWS KMS, YubiKey PIV integrations.
- RA mode: local registration authority authorizing requests for an upstream CA.
- **Revocation model (documented)**: "once a certificate is issued, the certificate authority (CA) can't un-issue it. It's valid until it expires." step-ca issues **short-lived certificates**; revoking blocks future renewal — "**passive revocation**"; contrast with **active revocation** (CRL/OCSP) used on the public internet. Revocation by serial number (authenticated) or cert+key; revocation token; offline mode; a certificate can only be revoked once; revoked certs fail renewal with an authorization error.
- **Limitations (explicit, vendor-documented)**: single configured Intermediate CA (multiple issuing CAs not supported); root CA always offline; single-tier PKI not supported; issuance policies authority-wide; "very limited options for active revocation (CRL, OCSP)"; "very limited options for legacy CA protocols"; limited device attestation; no Certificate Transparency integration; **"no support for certificate issuance history or metrics"**; no dynamic SCEP; no ACME EAB.

## Cross-product Comparison

| Structure | EJBCA | Vault PKI | AD CS | DigiCert Private CA | step-ca | Evidence |
|---|---|---|---|---|---|---|
| CA as managed object with protected keys | CA + Crypto Token (soft/PKCS#11) | issuer + key resources, internal/managed keys | CA role service (root/subordinate) | roots + intermediates managed as CA service | root (offline) + intermediate | A×5 |
| Trust hierarchy position (root/sub/external) | Root CA / Sub CA / externally signed via CSR | root or intermediate; external CA mode | root and subordinate CAs | roots + intermediates | root + intermediate (fixed two-tier) | A×5 |
| Policy object governing issuance | End Entity Profile + Certificate Profile | role | enrollment policy web service + customizable services | customizable certificate template + parameter guidelines | provisioners + templates + policies | A×5 |
| End entity (subject) concept | End Entity (device/person/server) | machines/services via roles; humans via auth methods | users, computers, services | users, devices, applications | humans and machines (provisioner-dependent) | A×5 |
| Enrollment surfaces/protocols | ACME, EST, CMP, SCEP, MS autoenrollment, web | ACME, EST, CMPv2, SCEP, /issue API | Web Enrollment, NDES, CEP/CES (HTTPS) | ACME, CMP, EST, SCEP, API | ACME, OIDC, cloud identity, JWK tokens | A×5 |
| Revocation | administrator revoke tools; approvals optional | revocation + CRL; auto-tidy | CA "manage certificate validity"; Online Responder | CRL, OCSP | revoke by serial/cert+key; passive-first | A×5 |
| Verification services published | CRL + OCSP (VA concept) | CRL distribution points + URLs config | CRLs + Online Responder (OCSP) | CRL, OCSP, AIA | CRL/OCSP "very limited"; passive revocation | A×5 |
| Issuance record / audit | logging; publishers | issued-cert storage + tidy; audit logging | (not directly evidenced in fetched page) | user activity audit log | **explicitly absent** ("no issuance history") | A×4, absent ×1 |
| CA lifecycle (create→active→renew/revoke/expire) | named statuses + rollover | rotation primitives; issuers | (implied by "manage certificate validity") | "full lifecycle of private trust management" | renewal; offline root | A×3–4 |
| Approvals / multi-person control | approval profiles (revoke, key recovery, EE edits) | Vault ACLs/policies (authz) | (not evidenced) | user access permissions and roles | provisioner auth | A×2–3 |
| Key recovery / archival | keyEncryptKey, key recovery ops | (not evidenced) | (not evidenced) | (not evidenced) | (not evidenced) | A×1 → Optional |
| HSM/KMS backing | PKCS#11 crypto tokens | managed keys (external KMS) | (not evidenced) | HSM support | PKCS#11, cloud KMS, YubiKey | A×3–4 |
| Publishing to directories | Publishers (LDAP/AD/VA/custom) | URLs config | (not evidenced) | AIA | (not evidenced) | A×2 → Common |
| Deployment spectrum | software/appliance/container/SaaS/cloud | self-hosted or HCP; secrets-engine-embedded | Windows Server role | vendor-operated service | self-hosted OSS + hosted offering | A×5 |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a PKI management application:

1. **The managed certificate authority.** A persistent, operator-managed CA object: an identified trust position (self-signed root, subordinate/intermediate, or externally signed) holding protected signing keys, with its own lifecycle (create → activate → renew/revoke/expire). This is what EJBCA's own docs contrast against "little more than a key pair and a signing script". Remove → crypto library / one-shot signing script / HSM console; there is no PKI to manage.
2. **Policy-governed certificate issuance.** Certificate requests from end entities (persons, devices, services) are evaluated against a defined issuance policy — a persistent operator-authored object (profiles / roles / provisioners / templates) constraining identities, fields, extensions, key constraints, validity, and which CA issues — and resolved into certificates signed by the CA. Remove → raw signing utility with no governance; the operator has no control surface.
3. **Trust status services.** The authority's public face for relying parties: the ability to revoke an issued certificate before expiry (via CRL publication and/or OCSP responses, or passively via short lifetimes with renewal blocking) and published verification data (where to fetch the CA certificate, CRL/OCSP endpoints, AIA). Remove → issued certificates become permanently unwithdrawable trust statements; the authority cannot take trust back; not a functioning PKI.

Jointly-held load-bearing:

- 1 alone = key store / HSM console.
- 2 without 1 = policy document and request form with no authority behind it.
- 3 without 1+2 = revocation machinery with nothing issued to revoke.
- 1+2 without 3 = an issuance machine that can never withdraw trust (step-ca shows leg 3 can be *minimized* to passive revocation, but not absent — revocation still exists).
- 1+3 without 2 = trust services with no governed path to issuance.

Anti-overfit notes:

- **Hierarchy depth is NOT definitional.** Vault's quick start runs a single self-signed root issuing end-entity certificates directly; step-ca fixes a two-tier shape. The invariant is "CA as managed trust position", not "root+intermediate".
- **Issuance record/audit is NOT definitional.** step-ca explicitly ships without issuance history. Common (EJBCA, Vault, DigiCert) but not invariant.
- **Specific protocols are NOT definitional.** ACME/SCEP/EST/CMP are the modern set; ADCS's documented surfaces include web enrollment and NDES; step-ca's are ACME/OIDC/cloud-identity/JWK. The invariant is "enrollment surfaces exist and are policy-gated", not any protocol set.
- **X.509 is the dominant realization but the sample also holds SSH CA (EJBCA, step-ca), CVC/ePassport, C-ITS V2X (EJBCA).** The invariant is certificate issuance by an authority, realized dominantly as X.509.

### L1 — Common Mature Structure

- Named, reusable issuance-policy objects (EJBCA profiles; Vault roles; step-ca provisioners/templates; DigiCert customizable template; ADCS policy/enrollment services).
- Multiple enrollment protocols beside a primary API (ACME, SCEP, EST, CMPv2, Microsoft autoenrollment; web enrollment).
- RA function: registration/validation of requesters, optionally separated from the CA (EJBCA RA concept; step-ca RA mode; ADCS NDES/CEP-CES).
- Issuance record / audit trail (EJBCA logging; Vault issued-cert storage + audit; DigiCert audit log) — absent in step-ca, hence common-not-definitional.
- CA renewal / rollover (EJBCA rollover certificates; Vault rotation primitives; step-ca renewal).
- HSM / external KMS backing of CA keys (EJBCA PKCS#11; Vault managed keys; DigiCert HSM; step-ca integrations).
- Publishing/distribution of certificates and revocation data to directories or VAs (EJBCA publishers; Vault URLs config; DigiCert AIA).
- Administrative roles/permissions and approval workflows for sensitive operations (EJBCA approval profiles; DigiCert roles; Vault ACLs).
- REST APIs / automation clients (Vault full HTTP API + Terraform; DigiCert API; step-ca API/CLI).
- Trust-anchor distribution to relying parties (EJBCA: root "must somehow be configured as a trusted root for all clients"; realized variously).

### L2 — Variant / Optional Structure

- Deployment: self-hosted software (EJBCA software, step-ca, AD CS role), appliance (EJBCA HW/SW appliance), vendor-operated service (DigiCert Private CA, EJBCA SaaS), embedded in a secrets manager (Vault).
- Trust scope: private/internal trust vs publicly trusted CA operations (DigiCert contrasts Private CA vs CertCentral public CA).
- Certificate families: TLS/mTLS, SSH certificates, device/IoT identity, code signing, document signing, eID/ePassport (CVC), V2X (C-ITS).
- Revocation posture: active (CRL/OCSP) vs passive (short-lived + renewal blocking) — step-ca's documented philosophy; Vault's short-TTL design leans the same way.
- Certificate lifetime philosophy: short-lived dynamic (Vault, step-ca) vs long-lived enterprise certificates (AD CS, EJBCA enterprise deployments).
- Root custody: offline root + online intermediate (Vault recommendation; step-ca fixed design) vs online root.
- Scale/regulatory poles: national eID, IoT device fleets, ePassport, CA/B-compliant public trust.

### L3 — Vendor-specific (Research Notes only)

- EJBCA: End Entity Profile vs Certificate Profile split; Crypto Tokens; Peer Connectors; Validators; partitioned CRLs; Chimera CA (hybrid post-quantum); named CA statuses; CVC/C-ITS/SSH CA types.
- Vault: secrets-engine mount model; roles as policy objects; CIEPS external policy service; PKI external CA mode; auto-tidy; issuers abstraction.
- AD CS: role-service packaging (Web Enrollment, Online Responder, NDES, CEP/CES); Active Directory integration (implied by domain-account language).
- DigiCert: ONE suite manager decomposition (CA Manager, Enterprise PKI Manager, IoT/Document/Software Trust managers); pooled managed roots.
- step-ca: provisioner taxonomy; passive-revocation design; always-offline root; authority-wide policies.

## Vendor-specific Findings

See L3. Additionally: step-ca's limitations list is itself valuable market evidence — it shows which structures the fuller products carry that a minimal in-type product may omit (issuance history, active revocation depth, legacy protocols, multiple issuing CAs).

## Boundary Findings

**vs Certificate Lifecycle Management (CLM)** — the most important seam:

- CLM manages the **estate of certificates already deployed** across the fleet: discovery/inventory, expiry monitoring, renewal orchestration, policy compliance — often CA-agnostic.
- PKI Management operates the **issuing authority itself**: CA objects, keys, issuance policy, revocation services.
- Evidence for the split being real: DigiCert documents Private CA (CA services: "managing your roots, intermediates, and X.509 certificate policy and issuance") and Trust Lifecycle Manager ("automation, monitoring, and self-service tools") as separate products; Keyfactor pairs EJBCA (CA) with Command (CLM); Vault PKI and step-ca have no estate management at all (step-ca explicitly lacks even issuance history).
- Test: remove the authority/issuance side and keep inventory/monitoring/renewal → CLM. Remove the estate side and keep CA/issuance/revocation → PKI Management. Suites fuse both; fusion is packaging, not identity.

**vs Secrets Management** — Vault is in-sample as a secrets manager carrying a PKI engine. The PKI engine itself (CA, issuers, roles, issue, CRL) is this Type; the surrounding secret-storage/dynamic-credential machinery is Secrets Management territory. A PKI engine embedded in a secrets manager is a deployment variant, not a different Type.

**vs Encryption & Key Management** — KMS treats keys as protected material (create, store, rotate, grant access). PKI management treats keys as the *signing identity of an authority* and manages trust relationships (identity↔key bindings via certificates) plus the services that let others verify them. A CA key in a KMS is a key; in PKI management it is the anchor of a trust hierarchy.

**vs Machine Identity Management** — machine identity is the broader umbrella (certificates as one credential class for machines, plus inventory/lifecycle of the identities). PKI management is the authority-side machinery any such program may sit on.

**vs Endpoint Management / UEM** — UEM/MDM products distribute trust anchors and profiles to endpoints; they do not run the CA. Distribution is an integration point, not the same Type.

**"去掉什么就变成另一个 Type" judgments:**

- Remove the CA/issuance authority, keep estate inventory/monitoring/renewal → Certificate Lifecycle Management.
- Remove certificates/trust services, keep protected key material → Encryption & Key Management / Secrets Management.
- Remove the operator/authority side entirely, keep only end-user certificate request self-service → a self-service enrollment portal (variant surface, not a separate Type).

## Historical / Market-Sample Check

- AD CS is platform-native and its documented generation (Windows Server 2012 R2 overview, archived) fits all three L0 legs with no cloud, ACME, or short-lived-cert machinery: CA role service, enrollment surfaces, Online Responder/CRLs.
- EJBCA self-identifies as "one of the longest running CA software projects" and its concept vocabulary (Root CA/Sub CA/RA/VA/End Entity) is the classic 1990s/2000s PKI vocabulary; the same structure describes the Windows Certificate Server / Netscape CMS / Entrust generation.
- National eID, ePassport (CVC), and V2X (C-ITS) regional poles are named EJBCA use cases and fit the same core.
- Conclusion: the L0 holds across eras and regions; nothing in it depends on cloud, ACME, short-lived certs, or automation fashion.

## Uncertainties

- ADCS: certificate-template machinery and autoenrollment specifics were not directly evidenced (current-version doc URLs unreachable); ADCS claims here are limited to the archived overview's role services and purpose statements.
- DigiCert: CA Manager / Enterprise PKI Manager UI-level structure unverified (404s); DigiCert claims limited to positioning and capability checklist.
- Vault: whether issued-certificate storage is on by default was not verified; only that storage + tidy exist.
- Whether any product exists that is in-type with **no** revocation capability whatsoever (pure passive, no renewal-blocking) — not observed; all five sampled products have revocation. If such a product exists, leg 3 would need re-examination.
- Public-trust CA operations (CertCentral-class) were sampled only at the suite-index level; this document treats public-trust operation as a variant pole without deep evidence.

## Final Synthesis

A PKI Management application is the operator-facing system for standing up and running certificate authority infrastructure. Its world consists of: managed CAs (trust positions with protected keys, arranged in hierarchies, each with its own lifecycle); issuance policy objects that gate what may be issued to whom; end entities (people, devices, services) that enroll through defined surfaces; the certificates themselves; and the authority's trust services — revocation and the published verification data (CRL/OCSP/distribution points) that relying parties consume. The daily loop is: establish and protect the authority → define policy → enroll/validate/issue → publish and serve trust status → renew, revoke, and eventually retire both certificates and CAs. What distinguishes it from a signing script is precisely the management layer: persistent CA objects, policy gates, records, services, and lifecycle. What distinguishes it from CLM is side of the seam: it runs the authority; CLM manages the deployed estate.
