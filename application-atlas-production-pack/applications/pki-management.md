# PKI Management

## Overview

A **PKI Management** application is the operator-facing system for standing up and running certificate authority infrastructure — a Public Key Infrastructure. It manages the certificate authorities themselves (their identities, their protected signing keys, their position in a chain of trust), governs which certificates may be issued to whom and under what rules, and operates the services through which relying parties verify that trust: revocation status and certificate/chain publication.

The problem it solves: in a certificate-based system, trust is delegated to authorities. Someone must hold the authority's keys, decide what it is allowed to vouch for, issue certificates under those rules, and — critically — be able to take that trust back when a key is compromised or a certificate is no longer valid. A PKI Management application is the system of record and control surface for exactly that job.

Its defining core is small:

```text
Managed certificate authority (trust position + protected signing keys)
└── Policy-governed certificate issuance
    └── (enrollment → validation → signed certificate)
└── Trust status services
    └── (revocation + published verification data)
```

Everything else commonly associated with modern PKI products — specific enrollment protocols, HSM integration, approval workflows, audit trails, automation APIs — is standard equipment in mature products but not what makes the product a PKI management application. A product that only stores keys, or only inventories certificates that some other authority issued, is a different kind of application.

## Users & Context

Primary users are the people responsible for an organization's trust infrastructure:

- **PKI / security administrators** — create and configure CAs, define issuance policy, manage keys, revoke certificates, rotate and renew authority certificates.
- **Infrastructure / DevOps engineers** — consume the authority through APIs and enrollment protocols to obtain certificates for servers, services, and workloads, often programmatically and at scale.
- **Registration / helpdesk operators** (in larger deployments) — register and validate end entities (people, devices) on behalf of the authority, sometimes with approval duties.

Secondary consumers are the *subjects* of the system — end entities: servers, network devices, IoT devices, applications, and occasionally human users — which request certificates through enrollment surfaces without ever seeing the administrative console.

Typical contexts:

- internal TLS / mutual-TLS for services and infrastructure
- device and IoT identity at fleet scale
- Wi-Fi / VPN access based on certificates
- code signing and document signing
- workforce smart-card / login certificates
- regional and regulated programs: national eID, ePassport, vehicle-to-vehicle communication

The work environment is administrative and long-lived: CAs live for years, root keys may be kept offline, and changes are deliberate and audited rather than continuous.

## Core Model

### The certificate authority as a managed object

The central object is the **certificate authority (CA)**: an identified issuer that holds signing keys and vouches for the authenticity of entities by signing certificates. A CA in a PKI management application is a persistent, configured object — not a one-off key pair. It carries:

- its **subject identity** (the name certificates will chain to),
- its **signing keys**, held in a protected key store — software-protected, an HSM, or an external key-management service,
- its **issuing certificate**: self-signed (a **root CA**), signed by another CA in the system (a **subordinate or intermediate CA**), or signed by an external authority (obtained by submitting a CSR),
- its **configuration**: signing algorithms, CRL schedule and distribution points, certificate and revocation behavior,
- its **lifecycle state**: created → active → renewed / revoked / expired.

CAs form a **trust hierarchy**: a self-signed root anchors trust; subordinate CAs issue beneath it. The hierarchy is the common shape, not a requirement — some products happily run a single self-signed root that issues end-entity certificates directly, and some designs mandate an offline root with a single online intermediate. What is definitional is that the CA exists as a managed trust position with protected keys; how many tiers it has is a design choice.

### The issuance policy object

Between the authority and its subjects stands a **policy object** — the operator's control surface over issuance. Products name it differently (certificate profiles, enrollment profiles, roles, provisioners, templates), but it answers the same questions:

- *which subjects* may request (which end entities, which domains, which device classes),
- *what* may be issued to them (subject fields, alternative names, extensions, key types and sizes),
- *how long* certificates are valid,
- *which CA* issues them,
- *how the requester proves eligibility* (authentication method, challenge, approval).

Requests that do not satisfy the policy are rejected or escalated for human approval. Without this object, the product is a signing utility; with it, issuance becomes governed.

### End entities and certificates

An **end entity** is the subject of issuance: a person, device, server, or service. It enrolls against an authority, and one end entity may hold several certificates over time. The **certificate** is the issued artifact — a signed binding between the subject's identity and a public key, valid for a bounded period. Certificates are the system's output and the reason everything else exists.

### Trust status services

Issuing a certificate is only half of an authority's job. The other half is telling relying parties whether a certificate can still be trusted:

- **Revocation** — invalidating an issued certificate before its natural expiry (compromised key, decommissioned server, departed employee). The authority records the revocation against the certificate.
- **Published verification data** — the authority publishes where its certificate can be fetched and where revocation status can be checked: certificate-revocation lists (CRLs) generated on a schedule, online status responses (OCSP), and issuer-information pointers. These endpoints are the authority's public face; relying parties consume them independently of the admin console.

Some products minimize active revocation in favor of **passive revocation**: certificates are issued with short lifetimes, and revoking means blocking renewal, so a revoked certificate simply dies of old age quickly. This is a documented design posture, not an absence of revocation — the authority still revokes; it just changes how the revocation takes effect.

### The record layer

Mature products keep records: issued certificates (searchable by subject, serial, status), administrative audit logs, and often the ability to publish issued certificates and revocation data outward (to directories, to dedicated validation services). This layer is what makes the system operable and auditable over years — but it is standard equipment rather than part of the definition; at least one deliberately minimal product in this category operates without an issuance-history feature.

### How the pieces relate

```text
Trust hierarchy
  Root CA (self-signed, often offline)
  └── Subordinate / issuing CA(s) — protected keys, lifecycle state
        │ governed by
        ▼
  Issuance policy objects (profiles / roles / provisioners)
        │ constrain requests from
        ▼
  End entities (persons, devices, servers, services)
        │ enroll via
        ▼
  Enrollment surfaces (protocols, APIs, web forms)
        │ produce
        ▼
  Certificates (identity ↔ key bindings, bounded validity)
        │ status served through
        ▼
  Trust status services (revocation, CRL / OCSP, publication points)
```

## How It Works

### 1. Establish the authority

The operator creates a CA: generate or import signing keys into a protected store, define the CA's identity and configuration, and obtain its issuing certificate — either self-signed (root), signed by another CA in the system, or signed externally by submitting a CSR. Distribution points (where the CA certificate and CRL will be published) are configured at this stage. A common pattern keeps the root offline and operates only an online intermediate; another common pattern runs everything online behind access controls. The CA then enters an active state in which it can issue.

### 2. Define issuance policy

The operator authors the policy objects that will gate issuance: which subjects may enroll, what fields and key constraints their certificates carry, what validity they get, which CA signs, and how requesters authenticate. In enterprise deployments these objects encode organizational rules (e.g., separate policies for servers, network devices, and people); in automation-first deployments they encode machine-oriented rules (allowed domains, maximum lifetimes).

### 3. Enroll → validate → issue

This is the system's central loop:

```text
End entity requests a certificate
→ request arrives through an enrollment surface
  (standard protocol, product API, or web form)
→ the authority validates the requester
  (authentication per policy; sometimes human approval)
→ the request is checked against the policy object
→ the CA signs the certificate
→ certificate (and often the key pair, if generated server-side)
  is returned to the requester
→ issuance is recorded
```

Enrollment surfaces vary widely by product and audience: standardized protocols for automated clients (ACME, SCEP, EST, CMP), platform-native mechanisms, plain APIs for programmatic issuance, and browser-based forms for one-off or human requests. The invariant is not the protocol set but the gate: every issuance path passes through the policy object.

### 4. Publish and serve trust status

The authority publishes its verification data: the CA certificate at its distribution point, CRLs on their schedule, OCSP responses on demand. Relying parties — browsers, servers, devices — consume these endpoints directly, without involving the administrator. When a certificate must be withdrawn, the operator (or an authorized automation) revokes it; the revocation propagates through the same published channels. In passive-revocation designs, revocation instead blocks the certificate's renewal, letting it expire quickly.

### 5. Operate over time

The authority itself has a lifecycle the operator manages:

- **Renewal / rollover** — CA certificates expire too; products support renewing them and rolling to new keys without breaking the chain.
- **Key events** — CA keys may be rotated; some products support key archival and recovery for end-entity keys.
- **Retirement** — a CA can be taken offline temporarily or revoked permanently; revocation of a CA is terminal and invalidates what it issued.
- **Housekeeping** — expired/revoked certificate records are retained or cleaned according to policy.

The daily rhythm is therefore asymmetric: issuance may be constant and automated, while authority-level changes are rare, deliberate, and heavily audited.

## Interfaces

### Administrative console

The operator's primary surface. Typical areas:

- **CA management** — list of CAs with their hierarchy position, status, and key store; create/edit/renew/revoke actions.
- **Policy / profile editor** — the issuance policy objects: subject rules, extensions, key constraints, validity, allowed CAs, authentication requirements.
- **End entity management** — registered subjects, their enrollment data, their certificates.
- **Certificate search** — issued certificates by subject, serial, status (active / expired / revoked); revoke and renew actions.
- **Approvals** — a queue of pending sensitive operations awaiting one or more authorizers (common in enterprise products).
- **Audit / logs** — administrative and issuance activity.

### Enrollment surfaces

The subjects' side: protocol endpoints for automated clients, REST APIs and CLIs for programmatic issuance, and web forms for manual requests. These are the interfaces most end entities ever touch.

### Verification endpoints

Public, unauthenticated-by-design surfaces: CRL distribution points and OCSP responders, plus the CA certificate publication location. Consumed by relying parties, not by operators.

### Automation layer

APIs, CLIs, and configuration-as-code integrations that let infrastructure teams treat CAs, policy objects, and issuance as programmable resources.

## Important Rules / Behaviors

- **The CA's own lifecycle is explicit.** A CA moves through states (created, active, offline, revoked, expired). Revoking a CA is terminal — it can no longer issue, and trust in what it issued collapses. Expired CAs can often be revived by renewal; revoked ones cannot.
- **Revocation is effectively irreversible.** A certificate can generally be revoked once; repeated revocation attempts fail. This asymmetry (easy to revoke, impossible to un-revoke) shapes operational caution.
- **Policy gates everything.** A request that violates the policy object — wrong subject shape, disallowed key, excessive validity, unauthenticated requester — is rejected or held for approval. The policy object, not the operator's discretion at request time, is the control point.
- **Root custody is a structural decision.** The root's key is the ultimate anchor; keeping it offline (or with an external provider) while operating only intermediates online is a common posture, and some products are designed around it.
- **Trust must be established on the client side.** Issuing a certificate does not make anyone trust it: the root must be configured as a trust anchor on every relying party, through whatever distribution channel the organization uses. The authority publishes; the clients must be taught to trust.
- **Revocation posture is a design choice with consequences.** Active revocation (CRL/OCSP) gives real-time withdrawal but adds infrastructure clients must consult; passive revocation (short lifetimes, renewal blocking) is simpler and scales well but accepts a window in which a revoked certificate remains technically valid.
- **Sensitive operations can require multi-person approval** — revocation, key recovery, end-entity changes — in enterprise-grade products.

## Variants

- **By deployment**: self-hosted software; software or hardware appliances; vendor-operated managed CA service; embedded as an engine inside a broader secrets-management platform.
- **By trust scope**: private/internal PKI (certificates trusted only within the organization's systems) versus publicly trusted operations (subject to public baseline requirements).
- **By certificate family**: TLS/mTLS server and client certificates; SSH certificates; device/IoT identity; code signing; document signing; regional formats such as ePassport or vehicle-to-vehicle certificates.
- **By revocation posture**: active revocation (CRL/OCSP infrastructure) versus passive revocation (short-lived certificates, renewal blocking).
- **By lifetime philosophy**: dynamic short-lived certificates issued per-deployment versus long-lived certificates issued per-person/per-device.
- **By scale and regulation**: small internal PKIs; enterprise-wide deployments; IoT fleets; national eID and other regulated programs with formal certificate policies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Certificate Lifecycle Management | closest neighbor; frequently fused in suites | CLM manages the *estate of certificates already deployed* — discovery, inventory, expiry monitoring, renewal orchestration, often across multiple CAs. PKI Management operates the *issuing authority itself* — CA objects, keys, issuance policy, revocation services. Remove the authority/issuance side and keep inventory/monitoring → CLM; remove the estate side → PKI Management. |
| Secrets Management | adjacent; sometimes hosts a PKI engine | Secrets management stores and doles out protected material (credentials, keys, dynamic secrets) generally. A PKI engine embedded in one is still this Type; the surrounding secret-storage machinery is not. |
| Encryption & Key Management | adjacent | KMS treats keys as protected material to create, store, rotate, and gate access to. PKI management treats keys as the signing identity of an authority and manages trust relationships expressed as certificates. |
| Machine Identity Management | umbrella over this Type | Machine identity programs manage identities of machines across credential types, with inventory and lifecycle of the identities themselves. PKI management is the authority-side machinery beneath such programs. |
| Endpoint Management / UEM | integration partner | Endpoint tools distribute trust anchors and certificate profiles to managed devices; they do not run the CA. Distribution is an integration point, not the same Type. |
| IT Change / Configuration Management | governance neighbor | May record PKI changes as changes, but holds no authority, issues nothing, and serves no trust status. |

The boundary with Certificate Lifecycle Management is the one to watch: commercial suites routinely sell both, and marketing language ("unify PKI operations") blurs them. The structural test is consistent across the sample: does the product run the authority (create CAs, hold their keys, gate issuance, revoke), or does it manage certificates that some authority — possibly external — already issued?

## Representative Products

- **EJBCA (Keyfactor)** — long-running, full-featured CA software; open-source roots with enterprise/appliance/SaaS packaging; enterprise, national-eID, and IoT poles.
- **Microsoft Active Directory Certificate Services (AD CS)** — platform-native PKI role bundled with Windows Server; the default enterprise CA for Windows-centric organizations.
- **DigiCert Private CA (DigiCert ONE)** — vendor-operated managed private CA service; roots, intermediates, and certificate policy operated as a service.
- **HashiCorp Vault PKI secrets engine** — API-driven, dynamic/short-lived certificate issuance embedded in a secrets-management platform.
- **Smallstep step-ca** — modern open-source online CA; ACME-first, short-lived certificates, passive revocation; a deliberately minimal pole.

These five were chosen to span deployment models (self-hosted, platform-native, managed service, embedded engine), trust philosophies (long-lived enterprise vs short-lived dynamic), and customer tiers (from single-team infrastructure to national-scale programs).

## Sources

Research date: **2026-09-09**

- EJBCA (Keyfactor) — Introduction, EJBCA Concepts, Certificate Authority Overview: https://docs.keyfactor.com/ejbca/latest/ejbca-introduction , https://docs.keyfactor.com/ejbca/latest/ejbca-concepts , https://docs.keyfactor.com/ejbca/latest/certificate-authority-overview
- HashiCorp Vault — PKI secrets engine (overview, setup and usage): https://developer.hashicorp.com/vault/docs/secrets/pki , https://developer.hashicorp.com/vault/docs/secrets/pki/setup
- Microsoft Learn (archived official documentation) — Active Directory Certificate Services Overview: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831740(v=ws.11)
- DigiCert — product documentation index and DigiCert Private CA: https://docs.digicert.com/ , https://docs.digicert.com/en/digicert-private-ca.html
- Smallstep — step-ca introduction and certificate revocation: https://smallstep.com/docs/step-ca/ , https://smallstep.com/docs/step-ca/revocation/

> Sourcing limitations: detail pages for DigiCert's CA Manager and for current-version AD CS certificate templates were not reachable during research; claims about those specific surfaces are correspondingly omitted or kept general. All product observations above come from official vendor documentation fetched on the research date; precise numeric limits, default settings, and protocol-version specifics are intentionally not stated.
