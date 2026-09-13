# Research Notes — Machine Identity Management

Directory leaf: "Machine Identity Management" (§15 Cybersecurity, Identity & Trust). Research date: 2026-09-08. Methodology: v1.1.

## Research Goal

Understand what a Machine Identity Management application is from real products: what the managed object is (a machine's identity vs its credentials vs the issuing infrastructure), how identities are created/registered, how credentials are issued and delivered to machines, how rotation/revocation/retirement works, who operates these products, and where the boundary lies against the already-processed siblings — Certificate Lifecycle Management, Secrets Management, Secrets Security, Encryption & Key Management, IAM, IGA, PAM — and against cloud-native managed identities and the era-current non-human-identity (NHI) / AI-agent governance wave.

Pre-pass context from sibling passes (recorded in STATUS.md):

- **certificate-lifecycle-management** (2026-09-07): "machine identity is the broader umbrella (certificates + SSH keys + workload identities + tokens). CLM is the certificate-specific slice. CyberArk's own portfolio demonstrates the split: Certificate Manager vs SSH Manager vs Workload Identity Manager under one 'Machine Identity Security' brand." This pass must verify and formalize that seam.
- **identity-governance-iga** (2026-09-08) forward flag: "machine-identity-management + the era-current agent-governance wave: all three researched IGA families now govern machine/AI-agent identities through the same loop (SailPoint Machine/Agent Identity Security, Entra Agent ID inside entitlement management, Omada Agent Governance) — population extension of IGA, that pass should test whether agent governance stays inside IGA products or drifts to a separate Type."
- **identity-access-management-iam**: boundary row already written: "Machine Identity Management — primary subject is non-human actors (services, workloads, agents); appears inside IAM only as an optional extension."
- **encryption-key-management**: keys as crypto material under custody vs keys as identity proofs of machines.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: organizations run vast populations of non-human actors (servers, services, workloads, devices, scripts, and now AI agents) that must authenticate to each other and to services. A Machine Identity Management application gives these actors managed identities — identifiers plus authenticating credentials — and drives their lifecycle (issue, deliver, rotate, revoke, retire) as a governed population, because machines cannot manage their own credentials and humans cannot track them by memory.
- Suspected confusions:
  - Certificate Lifecycle Management (§14 sibling, processed) — certificates are the largest historical slice of machine identity.
  - Secrets Management (§14) / Secrets Security (§15) — machine-related credentials as stored values.
  - PKI Management (§15 sibling) — the issuing infrastructure.
  - IAM / IGA / PAM (§15 siblings, processed) — identity and access family; IGA pass flagged the machine-population extension.
  - Cloud-native managed identities (AWS/Azure/GCP) — platform-native pole, not a standalone product.
  - NHI security startups (Oasis, Astrix, Entro, Silverfort) — discovery/governance overlays.
  - AI-agent identity governance — era-current wave.

## Research Questions

1. What exactly is the managed object — the machine, the identity, the credential, or the certificate?
2. How does a machine identity come into existence: discovered, registered, attested, issued?
3. What credential forms appear (certificates, SSH keys, tokens, federated identities, service accounts)? Is any single form definitional?
4. How do credentials get to where machines use them (provisioning, injection, workload API)?
5. What drives the lifecycle: validity clocks, deployment/decommission events, rotation schedules, compromise?
6. Who operates the product, and who (or what) is the "end user"?
7. What governance exists over machine identities (ownership, approvals, audit)?
8. How does the IGA-pass question resolve: is agent/machine governance inside IGA, inside machine-identity products, or drifting to a separate Type?
9. Where are the exact seams: CLM (certificate slice), PKI Management (infrastructure), Secrets Management (credentials as values), IAM (human population)?

## Representative Products

Selected for market representativeness, documentation completeness, product-philosophy diversity, and customer-level diversity:

| Product | Pole | Why sampled |
|---|---|---|
| CyberArk Machine Identity Security (Certificate Manager, Workload Identity Manager, Code Sign Manager; Venafi heritage) | Enterprise machine-identity platform, certificate-led, multi-product portfolio | The category's namesake vendor; richest operational docs; the portfolio itself demonstrates the CLM/MIM split |
| SPIFFE / SPIRE (CNCF open source) | Open-source workload identity issuance runtime | The reference standard for workload identity; identity-first (not artifact-first) philosophy; excellent spec-level docs |
| DigiCert Trust Lifecycle Manager | CA-led trust lifecycle suite | CA-vendor pole: certificate management + PKI services under one lifecycle roof; contrasts with CA-agnostic platforms |
| Aembit | Workload identity & access broker (NHI access layer) | Identity/policy/credential-broker philosophy; token/federation-native, no certificate issuance of its own; AI-agent use cases |

Corroborating (not deep-sampled): Keyfactor Command ("Discover and automate every certificate" — docs root confirmed; deep coverage already exists in the CLM pass's research), cloud provider managed identities (platform-native pole, recorded conceptually), SailPoint Machine/Agent Identity Security (directly observed in the IGA pass).

## Sources

Fetched 2026-09-08:

1. CyberArk Machine Identity Security docs root and Certificate Manager – SaaS full TOC: https://docs.cyberark.com/mis-saas/ (evidence: discovery services incl. private networks/K8s/cloud keystores/machines/public TLS endpoints; CA-agnostic CA list incl. built-in CA, AD CS, ACMEv2/Let's Encrypt, major public CAs; request policies; applications; approval workflows (issuance + revocation); machines catalog + per-product provisioning; auto-renewal + provisioning; retirement/revocation + revocation status monitoring; 47-Day Validity Readiness Dashboard; notifications; custom reports; VSatellite edge nodes; service accounts (create/enable/disable/delete/renew validity, workload identity federation); teams; event logging; licensing). Evidence layer A.
2. CyberArk Workload Identity Manager overview: https://docs.cyberark.com/mis-saas/firefly/overview/ ("high performing, lightweight micro-service for issuing machine identities quickly… high-speed/high-volume certificate issuance capacity with enterprise trust and policy enforcement"; formerly Firefly; managed via Certificate Manager SaaS or Self-Hosted control plane). Evidence layer A.
3. CyberArk Workload Identity Manager get-started: https://docs.cyberark.com/mis-saas/firefly/get-started/ (setup chain: CA account → sub-CA provider → policies → team → service account (workload identity federation via OIDC/K8s tokens vs key pair) → configuration (sub CA + policies + IdP trust via JWKS/OIDC discovery) → deploy K8s/Docker → gRPC/REST certificate requests → issuer certificate inventory; opening line: "Machine identity management is about trust."). Evidence layer A.
4. SPIFFE overview: https://spiffe.io/docs/latest/spiffe-about/overview/ (SPIFFE = open-source standards "for securely identifying software systems in dynamic and heterogeneous environments"; SVIDs; Workload API; implementer matrix incl. SPIRE, cert-manager, Consul, Dapr, Istio; commercial implementers; AWS IAM Roles Anywhere / GCP Workload Identity Federation as "works with" row). Evidence layer A.
5. SPIFFE concepts: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/ (Workload; SPIFFE ID = spiffe://trust-domain/workload-id URI; Trust Domain; SVID in X.509 or JWT form; Workload API needs no pre-shared secret — "your application need not co-deploy any authentication secrets"; private keys "short lived, rotated frequently and automatically"; trust bundles). Evidence layer A.
6. DigiCert Trust Lifecycle Manager overview: https://docs.digicert.com/en/trust-lifecycle-manager.html ("CA-agnostic certificate management and PKI services… certificate discovery, management, notification, automation, and integration… intermediate CA creation and private certificate issuance for users, devices, servers, and other IT resources"). Evidence layer A (overview level only).
7. Aembit docs root + conceptual overview: https://docs.aembit.io/ and https://docs.aembit.io/get-started/concepts/ ("Aembit operates conceptually as an identity broker"; Client Workloads / Server Workloads; Trust Providers = workload attestation from runtime environment; Access Policies + Access Conditions; Credential Providers = "generate and manage the credentials needed… OAuth tokens, API keys, temporary cloud credentials… create, rotate, and delete access credentials on your behalf"; JIT credential injection; Aembit Cloud control plane + Aembit Edge data plane; audit logs/workload events/access authorization events; tenant RBAC administration; workload discovery; Terraform provider; AI-agent/MCP use cases incl. blended identities). Evidence layer A.
8. Keyfactor docs root: https://docs.keyfactor.com/ (product framing "Discover and automate every certificate with Keyfactor Command"; Command separate from EJBCA PKI platform). Evidence layer A at root level; deep coverage inherited from CLM pass.

Abandoned/limited sources (network rule):

- Oasis Security docs (docs.oasis.security) — login-gated; abandoned after one attempt. NHI-startup feature claims therefore NOT asserted from primary evidence.
- DigiCert TLM deeper pages (get-started, workflows) — not fetched; product kept at overview level.
- Silverfort, Astrix, Entro — not attempted after the Oasis gate; treated as an unverified market pole.

## Product Observations

### CyberArk Machine Identity Security (Certificate Manager – SaaS + Workload Identity Manager + Code Sign Manager)

Evidence layer: A (docs.cyberark.com, fetched 2026-09-08).

- Portfolio framing: docs site titled "Machine Identity Security Docs"; "our machine identity management docs are available across multiple sites." Portfolio members observed: Certificate Manager – SaaS, Certificate Manager – Self-Hosted, Code Sign Manager – SaaS, Workload Identity Manager, Zero Touch PKI, VSatellite edge nodes, CLI tool (venctl), K8s components (cert-manager, CSI driver, CSI driver for SPIFFE, discovery agent, approver policy).
- **Discovery/inventory**: discovery services across private networks, public networks (domain scan), Kubernetes clusters, cloud keystores (Azure Key Vault / AWS / GCP), machines (server discovery), TLS server endpoints; certificate inventory with filters, tagging, custom reports, standard reports; "47-Day Validity Readiness Dashboard" (shortening-validity era surface); TLS certificate dashboard.
- **Issuance**: CA-agnostic — add a CA (built-in CA, AWS Public/Private CA, DigiCert(+One), Entrust, GlobalSign, GoDaddy, Google CAS, HID, OpenSSL, Sectigo, SSL.com, ACMEv2 incl. Let's Encrypt, Microsoft AD CS via VSatellite, custom CA Connector Framework, import from Zero Touch PKI); request policies constrain what can be issued (key algorithms, regex rules on names); applications as the containers that receive certificates; certificate request + approval workflows (issuance rules, approvers); Automated Secure Keypair.
- **Deployment/provisioning**: "Installations" section — cloud keystores (provision certificates to them) and a large "Machines" catalog (IIS, SQL Server, F5, Citrix ADC, NetScaler-class ADCs, WAFs, load balancers, cloud services, Azure app registrations, secrets managers) with per-product provision steps.
- **Lifecycle**: renewing (manual + auto-renewal with global/per-application settings + provisioning at renewal), reissuing, retiring ("retiring certificates"), revoking (revocation workflows with approval rules, revocation status monitoring), downloading, importing from third-party CAs.
- **Workload Identity Manager** (formerly Firefly): "a high performing, lightweight micro-service for issuing machine identities quickly and with no dependencies… high-speed/high-volume certificate issuance capacity with enterprise trust and policy enforcement"; setup chain: CA account → sub-CA provider → issuance policies → team → service account (two auth methods: workload identity federation via OIDC with Kubernetes service-account tokens — "the public key is never stored there" — or key pair in a Secret with "regular rotation") → configuration (sub CA provider + policies + IdP trust: JWKS or OIDC Discovery) → deploy in K8s (Helm) or Docker → workloads request certificates over gRPC/REST → issuer-certificate inventory page. Docs' opening: "Machine identity management is about trust. You want to ensure that the certificates that Workload Identity Manager will issue will be trustable. For that, you need to chain back to a trusted certificate authority."
- **Governance/administration**: user roles (PKI Administrator, System Administrator), teams with rule-based membership, service accounts with enable/disable/edit/delete/"renewing an account's validity period", event logging (activity logs, filtering, export as API endpoint, webhook forwarding), notifications center (PagerDuty, Zoom, email digests), licensing per certificate/machine, SSO integrations (Okta, Azure AD, PingOne, Auth0, ADFS).
- Interpretation: the portfolio structure (Certificate Manager for the TLS population; Workload Identity Manager for in-cluster issuance; Code Sign Manager for signing keys; SSH Manager on a separate docs site) is itself evidence for the umbrella-vs-slice reading of the Type.

### SPIFFE / SPIRE

Evidence layer: A (spiffe.io, fetched 2026-09-08).

- SPIFFE = "Secure Production Identity Framework for Everyone… a set of open-source specifications for a framework capable of bootstrapping and issuing identity to services across heterogeneous environments and organizational boundaries."
- Core objects: **Workload** ("a single piece of software, deployed with a particular configuration for a single purpose"; may span nodes or be process-granular; must be isolated so a malicious workload cannot steal another's credentials); **SPIFFE ID** (URI: spiffe://trust-domain/workload-identifier; "uniquely and specifically identifies a workload"); **Trust Domain** (the trust root — per org/environment/department; staging vs production separation advised); **SVID** ("the document with which a workload proves its identity"; X.509 certificate or JWT token, signed by the trust domain's authority); **Trust Bundle** (root keys used to verify SVIDs; "frequently rotated").
- **Workload API**: platform-agnostic local API exposing the workload's identity, private key, and trust bundle; modeled after cloud instance-metadata APIs; "does not require that a calling workload have any knowledge of its own identity, or possess any authentication token"; "all private keys (and corresponding certificates) are short lived, rotated frequently and automatically. Workloads can request new keys and trust bundles from the Workload API before the corresponding key(s) expire."
- **SPIRE** (the production implementation): server + agents; registration entries (the record of what identities exist and which selectors/attestation match them); node and workload attestation ("Attestation-based Issuance"); SVID rotation; federation across trust domains; nested SPIRE.
- Ecosystem matrix: SPIRE, cert-manager, Consul, Dapr, Istio implement SPIFFE open source; commercial implementers include GCP, Teleport ("machine and workload identity"), Red Hat; "works with" rows include AWS IAM Roles Anywhere and GCP Workload Identity Federation.
- Interpretation: the identity (SPIFFE ID) is the primary object; the credential (SVID) is a rotation-consuming proof; issuance is attestation-gated; there is no certificate-artifact inventory in the CLM sense — the population is registered workloads, and lifecycle is automatic short-lived rotation.

### DigiCert Trust Lifecycle Manager

Evidence layer: A at overview level (docs.digicert.com landing page only).

- "DigiCert Trust Lifecycle Manager is a unified digital trust solution that integrates CA-agnostic certificate management and PKI services." Two pillars: (1) "Certificate lifecycle management… certificate discovery, management, notification, automation, and integration"; (2) "PKI services, streamlining identity and authentication with intermediate CA creation and private certificate issuance for users, devices, servers, and other IT resources."
- Interpretation: CA-led pole; same vendor family operates both the CA infrastructure (DigiCert One / private CA) and the lifecycle layer. The issuance population is named in identity terms ("users, devices, servers, and other IT resources") — i.e., identities issued to non-human and human principals — but the documentation surface observed is certificate-centric. Treated as a straddling pole (certificate management with identity-issuance services), consistent with the CLM pass's characterization of CA-led CLM suites.
- Deeper workflow claims deliberately not asserted (only overview fetched).

### Aembit

Evidence layer: A (docs.aembit.io, fetched 2026-09-08).

- Positioning: "Aembit operates conceptually as an identity broker… facilitating secure access requests initiated by a Client Workload… attempting to connect to a target Server Workload"; workloads "may operate across security boundaries or reside in different compute environments."
- **Client Workloads** = "any non-human entity that needs to consume services or resources" (web apps calling APIs, microservices, background jobs, CI/CD pipelines, scheduled tasks). **Server Workloads** = targets (APIs, databases, SaaS, cloud services).
- **Trust Providers**: "validate Client Workload identities through workload attestation, verifying identity claims from the workload's runtime environment rather than relying on pre-shared secrets"; integrations across AWS, Azure, Kubernetes, CI/CD platforms; "cryptographically signed evidence, such as platform identity documents or tokens."
- **Access Policies** bind client → server under **Access Conditions** ("dynamic, context-aware constraints… similar to Multi-Factor Authentication for human identities" — time, GeoIP, external posture feeds).
- **Credential Providers**: "generate and manage the credentials needed for a Client Workload to authenticate to a Server Workload" — Basic auth, OAuth 2.0, API keys, certificate-based (mTLS), cloud provider credentials via Workload Identity Federation (AWS/Azure/GCP), SAML, Kubernetes tokens; can retrieve from external secrets managers; "to provide credential lifecycle management capabilities, Aembit offers Credential Provider integrations with services like GitLab to create, rotate, and delete access credentials on your behalf."
- **Credential injection**: Aembit Edge (data plane) intercepts outbound requests, gets a credential from Aembit Cloud, "injects the credential into the original request 'just-in-time'"; "without the Client Workload storing or managing long-lived credentials, eliminating credential sprawl."
- **Observability/administration**: audit logs, workload events, per-request access-authorization events (attestation outcome, condition checks, credential delivered, allow/deny verdict); tenant UI; RBAC with users/roles/permissions; "Discovery — tools for identifying and cataloging workloads across your infrastructure"; resource sets; log streams; admin IdP/SSO; Terraform provider for policies and workload identity configuration.
- AI-agent wave: dedicated AI guide (MCP identity gateway, MCP authorization server, "Agentic AI Blended Identities", LLM API access use case).
- Interpretation: token/federation-native pole — no certificate issuance of its own (certificate-based auth is consumed via credential providers); the identity population is workloads registered in the platform; lifecycle is JIT + delegated create/rotate/delete rather than validity-clock renewal.

## Cross-product Comparison

| Structure | CyberArk MIS | SPIFFE/SPIRE | DigiCert TLM | Aembit | Verdict |
|---|---|---|---|---|---|
| Persistent record of a non-human actor (machine/workload) as an identity-bearing principal | yes (machines, service accounts, applications; Workload Identity Manager client records) | yes (registration entries; SPIFFE IDs) | partial-at-overview (identities issued "for users, devices, servers"; certificate inventory is artifact-centric) | yes (client/server workload records) | defining (actor-centric identity of record) |
| Authenticating credential attached to the identity record; credential kind is a variable of the Type | certificates (Cert Manager), signing keys (Code Sign), workload certs (WIM); SSH keys in portfolio (separate product/docs site) | SVIDs: X.509 or JWT — two kinds under one identity | certificates (observed) | OAuth tokens, API keys, cloud WIF creds, SAML, K8s tokens, mTLS certs via providers — no native issuance | defining (actor-centric binding; kind-agnostic) |
| System-driven lifecycle: issue/assign → keep current (rotate/renew) → revoke/retire | yes (auto-renewal + provisioning, revocation workflows, retirement, service-account enable/disable/delete/renew) | yes (short-lived auto-rotated SVIDs; registration lifecycle) | yes (discovery, management, notification, automation per overview) | yes (JIT injection; delegated create/rotate/delete) | defining |
| Discovery/inventory of pre-existing (unmanaged) credentials | yes (network/K8s/cloud-keystore/machine/TLS-endpoint discovery) | no (greenfield issuance; registration) | yes (certificate discovery) | partial (workload discovery for the platform's own population) | common-mature (not definitional — registration-based poles lack it) |
| Policy-constrained issuance/access | yes (request policies; approval workflows) | yes (registration entries + selectors as issuance policy) | not asserted at overview level | yes (access policies + conditions) | common-mature |
| Attestation / trust verification before issuing or accepting identity | yes (WIF via OIDC/K8s tokens; IdP trust JWKS/OIDC discovery) | yes (node + workload attestation — signature capability) | not asserted | yes (Trust Providers — defining philosophy) | common-mature, era-current (absent in legacy cert issuance) |
| Delivery machinery to where machines use credentials | yes (provisioning catalog, VSatellites, K8s components, CSI drivers) | yes (Workload API local to workload) | integration (overview-level "integration") | yes (Edge interception + JIT injection) | common-mature |
| Rotation/short-lived credentials as posture | yes (auto-renewal; "regular rotation" for key-pair service accounts; shortening-validity dashboard) | yes (short-lived, frequently rotated — built into spec) | yes (automation) | yes (JIT, no long-lived secrets) | common-mature, era-current |
| Revocation/retirement machinery | yes (revocation workflows + status monitoring; retirement) | retirement = registration removal; SVID expiry self-limits (federation bundle rotation exists) | not asserted (overview) | delete/disable credentials via integrations | common-mature (form varies widely) |
| Human ownership/governance over machine identities | yes (teams, roles, approvals, event logs) | no owner concept observed (operators only) | not asserted | yes (RBAC, audit logs; humans own config) | common-mature |
| Dashboards/notifications/reports | yes | telemetry configuration | yes (notification per overview) | yes (dashboard, events, log streams) | common-mature |
| API/CLI/IaC surfaces | yes (REST API, venctl CLI, Terraform-class integrations) | yes (API-first; spec) | integration | yes (Cloud/Edge API, CLI, SDKs, Terraform) | common-mature |
| Control plane + customer-deployed edge/agent components | yes (VSatellites, discovery agents, K8s components) | yes (server + agents) | not asserted | yes (Cloud + Edge) | common-mature |
| AI-agent identity governance | era-current (portfolio direction; K8s/service-account machinery) | not asserted | not asserted | yes (AI guide, MCP gateway, blended identities) | variant/optional, era-current |
| Human principal issuance alongside machines | no | no | yes ("users, devices, servers") | no | variant (CA-led pole blurs toward certificate-issuance-for-all) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product stops being recognizable as Machine Identity Management:

```text
L0.1  Machine identity of record
      a persistent, individually identified record binding a non-human actor
      (service, workload, device, agent) to its identity — the name it is known by
      plus the authenticating material it uses to prove that identity
      remove → asset inventory / CMDB (machines as assets, not principals),
               or a bare CA issuing credentials with no actor records (PKI territory)

L0.2  Actor-centric identity binding
      the record's organizing subject is the machine actor; credentials attach to
      the actor, and the credential kind — certificate, key, token, federated
      identity — is an implementation variable of the Type, not the record's center
      remove (center the credential artifact instead) → Certificate Lifecycle Management

L0.3  Driven identity lifecycle across the machine population
      the system actively moves identities through their lifecycle: issue/assign
      when the actor is created or onboarded, rotate/renew to keep credentials
      current, revoke/retire when the actor is decommissioned or trust fails —
      machinery that would otherwise be per-machine manual work no human can track
      remove → a static registry of machine accounts / a monitoring-only view
```

Jointly-held is load-bearing:

- 1 without 3 = static machine-account inventory (an asset list with credentials noted).
- 3 without 1 = issuance machinery with no actor records — a CA/issuance endpoint, i.e., PKI Management territory.
- 2 without 1 = a credential store (secrets manager) — values without actor identity.
- 1+2 without 3 = an inventory, not management.

Note on L0.2's phrasing: it does NOT require any single product to support multiple credential kinds. It requires the record to be organized around the actor, which is what makes credential breadth a Type-level variable (CyberArk splits kinds across portfolio products; SPIRE uses SVIDs; Aembit uses tokens/federation). Certificate-only products satisfy L0 only when the certificate record is organized as the actor's identity (with the actor as subject), and the CLM pass's own artifact-centric reading shows the seam: in CLM the certificate is the subject and machines/applications are deployment locations.

### L1 — Common Mature Structure

- **Discovery/inventory of existing machine credentials** (network scans, cloud keystores, K8s clusters, public TLS endpoints, cloud/SaaS NHI discovery) — strong in artifact-led products; absent in greenfield registration poles (SPIRE, Aembit core).
- **Policy-constrained issuance/access** — request policies, registration entries, access policies; approval workflows in governance-heavy poles.
- **Attestation / trust verification before issuing** — node/workload attestation (SPIRE), runtime-environment attestation (Aembit Trust Providers), OIDC/workload-identity-federation trust (CyberArk WIM, cloud WIF).
- **Delivery/provisioning machinery** — provisioning catalogs, agents/edge components, CSI drivers, workload API, JIT credential injection.
- **Rotation/renewal automation; short-lived credentials as default posture** — auto-renewal, auto-rotated SVIDs, JIT injection.
- **Revocation/retirement machinery** — revocation workflows with status monitoring, registration removal, credential deletion via integrations.
- **Human governance over the machine population** — teams/ownership, RBAC, approval workflows, audit/event logging.
- **Dashboards/notifications/reports** — expiry readiness, posture, custom reports, notification center.
- **API/CLI/IaC surfaces** — REST/gRPC APIs, CLIs, Terraform providers, SDKs.
- **Control plane + customer-deployed edge/agent components** — VSatellite-class nodes, SPIRE agents, Edge data planes.

### L2 — Variant / Optional Structure

- Credential-kind scope of the product (TLS-certificate-only slice; SSH-only; token/federation-only; multi-kind portfolio).
- Identity naming substrate (URI-form workload IDs and trust domains; certificate subject/SAN; account names; cloud principal IDs).
- Federation across trust domains/organizational boundaries.
- Cloud-native managed identity as the substrate vs product-operated issuance (AWS IAM Roles Anywhere / GCP WIF appear in SPIFFE's "works with" matrix; Azure/AWS consoles as platform-native pole).
- Deployment form (SaaS + connectors; self-hosted; in-cluster OSS runtime).
- Human-decision approval workflows on machine-credential issuance (governance-heavy poles) vs fully automated issuance.
- AI/agent identity governance (blended identities, MCP gateways, agent identity security) — era-current, evidence concentrated in one pole + IGA pass.
- Device identity via MDM/UEM enrollment (SCEP-class device certificates) — device-fleet pole.
- NHI security overlays (discovery of non-human identities across clouds/SaaS, ownership mapping, risk scoring) — market wave asserted only at variant strength (docs gated; see Uncertainties).

### L3 — Vendor-specific (stays in Research Notes)

- CyberArk: VSatellite nodes, venctl CLI, "47-Day Validity Readiness Dashboard", Firefly heritage naming, Scanafi, Automated Secure Keypair, CA Connector Framework, licensing per certificate/machine, Code Sign projects/signing keys.
- SPIFFE/SPIRE: SVID name, SPIFFE ID URI format, trust-bundle mechanics, registration-entry selectors, nested SPIRE, Helm "hardened" charts.
- Aembit: Edge/Agent Proxy interception model, Tenant isolation, Content Security (CrowdStrike AIDR for MCP traffic), Access Conditions' external posture integrations (Wiz/CrowdStrike), blended-identity concept.
- DigiCert: DigiCert One integrations, divisions on CA accounts.

## Rejected Findings

- **"Machine identity = certificates."** Rejected: the sample includes a token/federation-only product with no native certificate issuance (Aembit) and an OSS identity framework whose credential may be a JWT (SPIFFE). Certificates are the largest historical slice, not the definition. (Corroborated by the CLM pass: CyberArk's own portfolio splits Certificate/SSH/Workload managers.)
- **"Machine identity management = cloud workload identity federation."** Rejected as era-specific: SPIFFE-era federation is one posture; SSH key management, service accounts, and device certificates predate it and satisfy the core.
- **"Discovery of unmanaged credentials is definitional."** Rejected: registration-based greenfield poles (SPIRE, Aembit) manage identity populations without discovering pre-existing artifacts.
- **"AI-agent governance defines the Type."** Rejected for now: evidence shows it as an era-current population extension present in some poles (Aembit AI guide) and in IGA products (SailPoint/Omada/Entra per the IGA pass); recorded as a watch item.
- **"Machine identity management is just IGA for machines."** Rejected: IGA's defining core includes structured human decision processes (certifications/attestations) and desired-state reconciliation of access; machine-identity products' core is the identity/credential lifecycle machinery. Overlap exists (ownership, reviews in NHI overlays) but the cores differ.
- **"Every machine-identity product must operate a CA."** Rejected: CyberArk connects to external CAs; SPIRE chains to external PKI ("PKI Integration" column); Aembit issues nothing itself.

## §24 Historical / Market-Sample Check

- Would older / platform-native products still fit? **SSH key management across server fleets** (authorized_keys provisioning, rotation, removal on decommission): actor records (hosts/service principals) + key lifecycle — fits L0 with no cloud, no federation, no certificates. ✔
- **Directory service accounts with Kerberos principals/keytabs** (AD-era): identity of record + credential + lifecycle driven by the directory — fits; platform-native pole. ✔
- **MDM-issued device certificates (SCEP-era)**: device identity of record + certificate + enrollment/rotation lifecycle — fits. ✔
- **Cloud managed identities / workload identity federation (AWS/Azure/GCP)**: principal records + credentials + lifecycle — fits; platform-native modern pole. ✔
- Would a modern cloud-era framing (SPIFFE, zero trust, short-lived everything) over-define the Type? The L0 names no protocol, no credential kind, no attestation, no cloud — SPIRE-era machinery stays in L1. ✔
- Would the certificate-era framing over-define it (the Venafi-heritage view)? The L0's actor-centric leg explicitly prevents collapsing the Type into CLM. ✔

## Boundary Findings

1. **vs Certificate Lifecycle Management (processed sibling, sharpest seam)** — CLM's record is the certificate artifact (issuer, validity clock, renewal); MIM's record is the machine actor whose credentials (of any kind) attach to it. Remove MIM's actor-centric leg (center the artifact) → CLM. Evidence: CyberArk's portfolio splits Certificate Manager vs SSH Manager vs Workload Identity Manager under one machine-identity brand; SPIRE/Aembit manage identities with no certificate-artifact inventory. Honest overlap: the TLS population sits on the seam, and certificate-led platforms (DigiCert TLM, Keyfactor Command) straddle — their certificate management is CLM; their identity-issuance services for devices/servers/users reach toward MIM.
2. **vs PKI Management (sibling leaf)** — PKI Management's object is the issuing infrastructure (roots, hierarchies, CA policies, revocation infrastructure). Remove MIM's machine-actor records, keep issuance machinery → PKI Management. Same seam the CLM pass recorded, one level up.
3. **vs Secrets Management (§14) / Secrets Security (§15)** — secrets managers hold credentials as retrievable values for authorized consumers; MIM manages the actor's own identity and its lifecycle. Remove the actor identity records; hold credentials as values → Secrets Management. Straddling is handled by integration: CyberArk provisions to/from credential managers; Aembit's Credential Providers can read from Vault/Secrets Managers; Vault itself issues PKI/SSH credentials (machine-identity issuance embedded in a secrets platform).
4. **vs IAM (processed sibling)** — identity population. IAM's subjects are organization-administered people (self-service auth UX, joiner/mover/leaver). Change the population to people → IAM. Machine actors never log in to a self-service portal; lifecycle is driven by deployment/decommission events and trust policy, not HR.
5. **vs Identity Governance / IGA (processed sibling)** — IGA adds structured human decision processes (requests/approvals, certifications, SoD) and desired-state reconciliation over access. Add human-decision governance as the core loop → IGA. The IGA pass observed machine/AI-agent governance inside all three researched IGA families (SailPoint Machine/Agent Identity Security, Entra agent identities in entitlement management, Omada Agent Governance) — population extension. Answer to the IGA pass's forward flag: agent governance appears BOTH inside IGA products and natively in machine-identity poles (Aembit's AI guide; CyberArk portfolio direction); it does not yet constitute a separate Type; credential-lifecycle machinery (issuance/rotation/revocation) remains the differentiating core of MIM and is not present in IGA products (they delegate to credential systems).
6. **vs PAM (sibling leaf)** — PAM brokers privileged access and sessions (vaulting, session recording, JIT activation). Add session/credential brokering for interactive privileged use → PAM. Machine identity credentials are consumed by machines programmatically, not checked out by humans.
7. **vs Encryption & Key Management (processed sibling)** — KMS's object is key material under custody with a governed crypto lifecycle; MIM's object is the actor's identity. Remove identity binding (keys as raw crypto material) → KMS.
8. **vs IT Asset Management / CMDB** — assets are records of what exists and where; identities are authenticatable principals. Remove authentication/credential lifecycle → asset registry.
9. **vs Endpoint Management / UEM** — UEM's subject is the device fleet (configuration, apps, patches); device-certificate enrollment is an issuance capability inside it. Remove identity lifecycle, manage the fleet → UEM.
10. **vs API gateway / service mesh runtime** — meshes and gateways issue workload identities as an embedded runtime capability (Istio/Consul appear in SPIFFE's implementer matrix). When identity issuance is a capability of traffic infrastructure, it's not the Type; MIM products make the identity population itself the managed object. Watch: the boundary is porous by design (SPIFFE is the interoperability layer between them).

## Uncertainties

- NHI-governance startup feature sets (Oasis, Astrix, Entro, Silverfort) were not verified — Oasis docs login-gated, others not attempted after the gate. All NHI-overlay claims are carried at variant strength, cross-referenced only from the IGA pass's direct observation of SailPoint Machine/Agent Identity Security.
- DigiCert TLM was observed at overview level only; deeper workflows (approval, discovery configuration) not asserted.
- Keyfactor Command observed at docs-root level this pass; its deep structure is inherited from the CLM pass and used only as corroboration for the certificate-led pole.
- Cloud-provider native machine-identity consoles (AWS/Azure/GCP IAM machine identities) were not directly researched; the platform-native pole is asserted conceptually, corroborated by SPIFFE's "works with" rows (AWS IAM Roles Anywhere, GCP Workload Identity Federation).
- Whether standalone SSH-key-management products persist as a market pole was not independently verified; recorded as a variant informed by CyberArk's portfolio split (SSH Manager on a separate docs site) and by historical practice.
- Exact numeric limits (validity periods, rotation windows, scan scopes, seat counts) deliberately not asserted; the "47-Day" dashboard is quoted as a product surface, not an industry rule.

## Final Synthesis

A Machine Identity Management application is a **system of record and lifecycle engine for the identities of non-human actors**: it keeps a persistent, actor-centric record of each machine identity — the service, workload, device, or agent — together with the authenticating material it uses to prove that identity, and it drives that population through its lifecycle, issuing or assigning identities when machines are created, rotating and renewing credentials so they stay current, and revoking or retiring identities when machines are decommissioned or trust fails. Mature products add discovery of existing machine credentials, policy-constrained issuance, attestation-gated trust, delivery machinery that places credentials where machines use them, rotation automation with short-lived credentials as the modern posture, revocation workflows, human governance (ownership, approvals, audit), and API/CLI/IaC surfaces behind a control-plane-plus-edge architecture. The Type's poles: certificate-led enterprise platforms, CA-led trust suites, open-source workload-identity runtimes, token/federation-native access brokers, platform-native cloud managed identities, and governance overlays. The defining core is deliberately small and credential-kind-agnostic: certificates are its largest historical slice (and the adjacent CLM Type documents that slice), not its definition.
