# Research Notes — Privileged Access Management / PAM

## Research Goal

Understand what a Privileged Access Management application really is from real products: what objects exist inside it, how privileged access is controlled and recorded, how the two access realizations (credential disclosure vs brokered session) relate, and where the Type's boundaries run against IAM, Password Managers, Secrets Management, IGA, and ZTNA.

## Initial Boundary

Temporary hypothesis before research:

- PAM manages an organization's **privileged accounts** (administrator, root, domain admin, service accounts) on target systems — not the end user's own identity.
- Core mechanics expected: credential vaulting, policy-gated disclosure (checkout/show), session brokering (proxy without revealing credentials), session recording, rotation, discovery, approval/JIT.
- Nearest neighbors: IAM (identity lifecycle), SSO/MFA (authentication), Password Manager (credential storage for people), Secrets Management (machine-consumed secrets), IGA (governance/certification), ZTNA (network access), Endpoint Management (endpoint privilege management overlap).
- Unknowns: is the vault definitional or is mediation the invariant? How far has non-human/machine identity coverage pulled PAM into Secrets Management territory? Is session recording definitional?

## Research Questions

1. What is the central object — how do products represent a privileged account?
2. How does a privileged account enter the system (manual onboarding vs discovery)?
3. How does a person actually get access: credential disclosure (show/copy/checkout) vs brokered session? Are both present?
4. What policy machinery gates access (permissions containers, master/access policies, reason-for-access, ticketing, approval/dual control, time windows)?
5. What happens to credentials over time (rotation, check-in/change-on-check-in, exclusive locks)?
6. How are sessions controlled and recorded (proxy, isolation, recording, live monitoring, command filtering)?
7. What are the two user surfaces (PAM administrator vs privileged user/requester)?
8. Where do non-human identities (service accounts, cloud keys) sit?
9. Where are the boundaries vs Password Manager, Secrets Management, IAM, IGA, ZTNA?
10. What would an older / platform-native product look like — does the definition over-fit the current market?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy, and differing customer tiers:

| Product | Position | Philosophy | Evidence quality |
|---|---|---|---|
| CyberArk Privilege Cloud (Idira) | Enterprise market leader | Vault-centric: accounts in Safes, rotation engine, session manager | Tier-1, extensive |
| Delinea Secret Server | Mid-market/enterprise, vault heritage | Vault + checkout + discovery as "Phase 1" of a PAM program | Tier-1, extensive |
| BeyondTrust Password Safe | Enterprise suite | Managed accounts + access policies + request/approval + session proxy | Tier-1, extensive |
| HashiCorp Boundary | Modern/DevOps, open-source root | Identity-aware proxy; session brokering without owning a vault | Tier-1, extensive |
| Keeper KeeperPAM | SMB/mid-market, password-manager heritage | Zero-knowledge vault as launch surface + gateway brokering + JIT | Tier-1 via docs query interface |

## Sources

All fetched 2026-09-09.

- CyberArk (Idira) docs portal — https://docs.cyberark.com/ (portal root)
- CyberArk Privilege Cloud Standard — introduction: https://docs.cyberark.com/privilege-cloud-standard/latest/en/content/privilege%20cloud/privcloud-introduction.htm
- CyberArk — Retrieve (display) the account password: .../privcloud-show-copy-psswd.htm
- CyberArk — Connect to a target device: .../privcloud-connect-to-device.htm
- CyberArk — Find Privilege Cloud documentation in spaces (concept map incl. Master Policy, dual control, session monitoring): https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/resources/_topnav/cc_home.htm
- Delinea docs portal — https://docs.delinea.com/
- Delinea Secret Server home: https://docs.delinea.com/online-help/secret-server/start.htm
- Delinea Secret Server Business User Guide: .../guides-tutorials/end-user-guide/index.htm
- Delinea Checkout Overview: .../secret-operations/secret-access-workflow/secret-checkout/index.htm
- BeyondInsight & Password Safe 26.2 release notes: https://docs.beyondtrust.com/bips/docs/password-safe
- BeyondTrust Managed Accounts Overview: https://docs.beyondtrust.com/bips/docs/managed-accounts
- BeyondTrust PS Cloud Accounts tab (request/release/retrieve/sessions/Direct Connect): https://docs.beyondtrust.com/bips/docs/ps-cloud-accounts
- HashiCorp Boundary docs: https://developer.hashicorp.com/boundary/docs
- Boundary — What is Boundary?: https://developer.hashicorp.com/boundary/docs/what-is-boundary
- Boundary — Domain model overview: https://developer.hashicorp.com/boundary/docs/domain-model
- Keeper docs root: https://docs.keeper.io/
- KeeperPAM overview (via official docs query interface, sourced from listed doc pages incl. architecture, JIT, session recording): https://docs.keeper.io/keeper-documentation.md?ask=...

Failed/abandoned: docs.cyberark.com/privilege-cloud/latest/ (404), docs.delinea.com Secret Server "current" path (404), Delinea dual-control page (404 — dual control not directly evidenced for Delinea; approval workflows evidenced at CyberArk/BeyondTrust/Keeper instead).

## Product Observations

### CyberArk Privilege Cloud (Idira)

Evidence layer: A (directly observed, official docs).

- Positioning: "a SaaS solution that enables organizations to securely store, rotate and isolate credentials (for both human and non-human users), monitor sessions"; "protects, controls, and monitors privileged access across on-premises, cloud, and hybrid infrastructures."
- **Accounts**: "Access to sensitive systems or applications in your environment is managed through access credentials that are defined in accounts. Accounts determine the target resource, the user credentials for access, linked accounts for logon or reconcile, and dependents that use the account's credentials."
- **Platforms**: shared characteristics for groups of accounts — machine/app properties, credential management policies, password rules, session management.
- **Safes**: "controls access to target machines by storing privileged identities in Safes, and giving access only to authorized users" — permission container.
- **Password rotation** by Central Policy Manager (CPM): "changes secrets automatically on remote machines and stores the new secrets in the Privilege Cloud... verify secrets on remote machines, and reconcile them when necessary."
- **Session isolation & recording** by Privileged Session Manager (PSM): "establish privileged sessions with Windows target machines and records sessions"; "strict isolation between endpoints and targets... never exposing endpoints... to privileged credentials"; searchable audit trail, real-time monitoring, "search and play video recordings" (session monitoring space).
- **Discovery**: "automated tools to identify and secure privileged credentials across your organization."
- **Least privilege for *NIX/Windows**: "run authorized administrative commands from their native sessions while eliminating unneeded superuser privileges" (PSM / PSM for SSH).
- **Non-human credentials**: hardcoded application credentials "removed and managed by Privilege Cloud."
- End-user disclosure path: Show → enter **reason** ("Require users to specify reason for access rule in the Master Policy... set to Active" by default) → password displayed "for a limited amount of time"; **exclusive access**: "the account is locked from the time that the user displays the password until the user releases the account" or rotation changes it.
- Brokered path: "connect to Windows servers, databases, SSH devices... without knowing or specifying the required password or key"; Safe permissions required: "Use account", "List account"; Ad Hoc Connections to unmanaged machines "while retaining privileged session management benefits."
- **Dual control**: "Manage privileged access requests to accounts in a dual control environment" (account requests space).
- Master Policy: "Set the default security policy for privileged access in your organization."
- Personal privileged accounts: end users (IT admins) can "independently create their own personal privileged accounts."
- Suite siblings (same vendor, separate services): Endpoint Privilege Manager (endpoint least privilege), Secrets Manager (DevOps secrets), Workforce Password Management, IGA, Secure Infrastructure Access ("zero standing privileges or vaulted credentials"), Remote Access (zero trust + JIT provisioning).

### Delinea Secret Server

Evidence layer: A.

- Positioning: "comprehensive Privileged Access Management (PAM) solution designed to protect, control, and manage privileged accounts and credentials"; "enterprise-grade password management solution... to securely store, manage, and control access to privileged credentials."
- Program framing (vendor's own maturity model): "Secret Server is where most organizations begin a privileged access management (PAM) program. It delivers the Phase 1 capabilities every mature program is built on: a hardened vault for privileged credentials, automated discovery of the accounts already loose in your environment, multi-factor authentication on every credential retrieval, and privileged remote access that lets administrators connect to target systems without ever seeing the password. Once those foundations are in place, organizations typically expand into session recording, just-in-time access, endpoint privilege management, and identity threat detection."
- **Secrets**: "individually named packets of sensitive information, such as passwords... each type represented and created by a secret template that defines the parameters of all secrets based on it." Controls: complexity/change intervals, who has access, MFA, "Recording who actually accessed a secret", "detailed audit trail for access and history."
- **Secret folders**: nested containers; permissions set at folder level, inherited by secrets.
- **Checkout**: "forces accountability on secrets by granting exclusive access to a single user... No other user can access a secret while it is checked out... guarantees that if the remote machine is accessed using the secret, the user who had it checked out was the only one with proper credentials at that time." "Change Password on Check In" forces a password change on the remote machine after check-in. Auto check-in after a configured interval (30 minutes default per docs — product-specific). Exception: "Unlimited Vault Access" role (break-glass analog).
- Login with AD or local account; MFA (Duo, text/email codes).
- Web Password Filler / Credential Manager browser extension for website logons.
- Event notifications (expired secrets, subscriptions).
- Suite siblings: Connection Manager (RDP/SSH session launcher), Server PAM/Server Suite (JIT privileges for Linux/Unix/Windows servers; "check out account passwords that are stored in the Privileged Access Service"), Privilege Manager (endpoint least privilege), Account Lifecycle Manager (service account lifecycle), DevOps Secrets Vault, Privileged Behavior Analytics.

### BeyondTrust Password Safe (BeyondInsight)

Evidence layer: A.

- **Managed accounts**: "user accounts which are local or Active Directory accounts on the managed system"; "centralized control, security, and automation for user accounts on managed systems." Accounts tab "lists the managed accounts for which you have permissions to request access to retrieve passwords and start sessions."
- **Request a password release**: Access panel → reason → ticket system + ticket number (required or optional per **access policy**) → start date/time + length of time the password is available → Submit Request → email to approver → status in Requests tab.
- **Retrieve a password**: reason → Retrieve Password → "password displays in a separate window... with a timer showing remaining time" → copy → "Use the password to log in to the system within the password release time period."
- **Quick Launch**: auto-approval path bypassing the request queue (policy-configured).
- **Brokered sessions**: "Password Safe acts as a proxy, providing session management to target systems. No passwords are transmitted, allowing inherently secure session management." RDP connection file with one-time-use token; SSH proxy via custom connection strings embedding requester + account + system.
- **Direct Connect**: "access the system without ever viewing the managed account's credentials"; approval window then auto-disconnect (5 minutes per docs — product-specific).
- Access policies govern whether Reason / Ticket System / Ticket Number are required; location restrictions (CIDR/IP ranges) gate password retrieval and RDP sessions (from release-notes issue list).
- Discovery: AWS/Azure connectors for asset discovery; cloud service principal credentials (AWS access tokens, Azure client secrets) onboarded/rotated/retrieved "through the standard Password Safe workflow, extending PAM coverage to Cloud API access."
- Smart Rules, Managed Systems, Functional Accounts (automation accounts used for rotation), Personal Access Tokens for Direct Connect/API.
- Suite siblings: Secrets Safe (secrets management), Endpoint Privilege Management (Web Policy Editor), Workforce Passwords (personal folders), BeyondInsight (management/analytics console).

### HashiCorp Boundary

Evidence layer: A.

- Positioning: "an identity-aware proxy aimed at simplifying and securing least-privileged access to cloud infrastructure"; "grant access to critical systems using the principle of least privilege"; "secure access to hosts and critical systems without distributing and managing credentials, configuring firewalls, or exposing the organization's private network" (replaces SSH bastions/VPNs).
- Capabilities: SSO via external OIDC IdPs; just-in-time network access; "passwordless access with dynamic credentials via HashiCorp Vault"; "Automate discovery of new target systems"; "Record and manage privileged sessions"; credential brokering; credential injection; transparent sessions; multi-hop sessions; session recording + recording lifecycle management (paid editions); audit logs/streaming.
- Core workflow: User Authentication (trusted IdP) → Granular Authorization (roles/grants) → user selects target from dynamic host catalogs → Access.
- Domain model: **Scopes** (global → org → project) as permission containers/blast-radius boundaries; principals = users/groups; auth methods (OIDC, password) with **accounts** = the user's own login credentials for those methods (distinct from target credentials); **Target** = "a resource that represents a networked service with an associated set of permissions a user can connect to and interact with through Boundary by way of a session"; **Host/Host set/Host catalog**; **Credential** = "a data structure containing one or more secrets that binds an identity to a set of permissions or capabilities on a host for a session"; **Credential store/library** = "can retrieve, store, and potentially generate credentials" (external, e.g., Vault); **Session** = "a set of related connections between a user and a host. A session may include a set of credentials which define the permissions granted to the user on the host for the duration of the session"; **Session recordings** stored in external object-store **storage buckets** under **storage policies** (retention); **Worker** = data-plane service that "proxies sessions between users and targets... without exposing the networks they run on."
- RBAC: composable, allow-only grants/actions/roles.
- Notably: Boundary does not hold a proprietary credential vault — credentials come from credential stores (Vault or others). The PAM-ness lives in the brokering/authorization/session layer.

### Keeper KeeperPAM

Evidence layer: A (official docs, retrieved through the docs' own query interface which returns sourced excerpts).

- Positioning: "secures and manages access to critical resources like servers, web apps, databases, and workloads. It provides zero-trust privileged sessions and Just-in-Time (JIT) access without exposing credentials."
- Components: **Vault** (users manage access and launch privileged sessions from the UI); **Secrets Manager** (zero-knowledge infrastructure secrets, integrated so vault secrets establish sessions); **Keeper Gateway** (in-customer service that "performs secret retrieval and brokers privileged sessions"); self-hosted **Connection Manager** (agentless gateway container); **Session recording** (graphical and text/typescript, encrypted with customer-controlled keys); **JIT** ("grants elevated access only for the required time window with approvals, expiry, and automatic cleanup").
- Flow: admin shares a PAM resource (PAM Machine/Database/Cloud) → optional **Workflow** requiring approvals, MFA, access windows, check-in/check-out → JIT realization varies (IdP elevation, temporary/ephemeral accounts, time-limited access with rotation, endpoint elevation) → user launches from the Vault record → session established through the gateway and streamed into the Vault → recording + expiry cleanup (elevated access removed, ephemeral accounts deleted).
- Suite siblings: password manager product line (consumer/business), Endpoint Privilege Manager ("Eliminate standing admin rights and enable Just-in-Time (JIT) across all endpoints"), Commander CLI, KeeperDB.

## Cross-product Comparison

| Dimension | CyberArk | Delinea | BeyondTrust | Boundary | Keeper |
|---|---|---|---|---|---|
| Central privileged object | Account (target resource + credentials + linked accounts) | Secret (template-typed credential packet) | Managed Account (on a Managed System) | Target (+ host sources + credential sources) | PAM resource (Machine/Database/Cloud) |
| Credential custody | Own vault (Safes) | Own vault | Own vault | External credential stores (e.g., Vault) | Own zero-knowledge vault |
| Permission containers | Safes (+ platforms for policy) | Folders (+ secret templates) | Smart Groups / access policies | Scopes (global/org/project) | Shared folders / roles |
| Disclosure path | Show/copy with reason; limited display time; exclusive lock | View/checkout; exclusive checkout; auto check-in; change-on-check-in | Retrieve password; timed release window; timer display | Credential injection (user never sees) | Launch without exposing credentials |
| Brokered session path | PSM / PSM for SSH; connect "without knowing or specifying the required password" | Privileged remote access "without ever seeing the password"; Connection Manager | RDP/SSH proxy; "No passwords are transmitted"; Direct Connect | Workers proxy sessions; credential injection | Keeper Gateway brokers; streamed into Vault |
| Request/approval | Dual control account requests | (JIT named as later phase; not directly evidenced in fetched pages) | Request/approval with reason + ticket + time window; Quick Launch bypass | (JIT network access; grants) | JIT workflow: approvals, MFA, access windows |
| Reason/ticket capture | Reason rule in Master Policy | Audit trail of access | Reason + ticket system + ticket number | Audit logs | Workflow approvals |
| Rotation | CPM automatic rotation + verify/reconcile | Automated password management; change on check-in | Rotation incl. cloud service principal keys | Dynamic credentials via Vault | Rotation in time-limited JIT modes |
| Discovery | "Discovers accounts" | "automated discovery of the accounts already loose in your environment" | AWS/Azure connectors for asset discovery | "Automate discovery of new target systems" (host catalogs) | (not directly evidenced) |
| Session recording | PSM records; searchable; video playback | Later-phase capability (vendor's own framing) | Session manager; recording in suite | Session recordings + storage buckets + retention policies | Graphical + text recordings, customer-held keys |
| MFA at access | PSM for SSH MFA caching | "multi-factor authentication on every credential retrieval" | RADIUS/Okta MFA; push-only Direct Connect | Delegated to IdP (OIDC) | MFA in JIT workflow |
| Non-human identities | Explicit: "human and non-human users"; hardcoded app credentials | Account Lifecycle Manager (service accounts); DevOps Secrets Vault | Cloud service principals (AWS/Azure) | Machine targets; Vault-issued dynamic credentials | Workloads; Secrets Manager |
| Endpoint privilege sibling | Endpoint Privilege Manager | Privilege Manager | Endpoint Privilege Management | — | Endpoint Privilege Manager |
| Secrets-management sibling | Secrets Manager / Secrets Hub | DevOps Secrets Vault | Secrets Safe | Vault (separate product, integrated) | Keeper Secrets Manager |
| Deployment | SaaS + self-hosted lines | Cloud + on-premises | Cloud + on-premises + appliance | Self-managed + HCP (cloud) | Cloud + self-hosted gateway |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as PAM:

```text
Privileged account as managed unit
  (an account on a target system whose elevated access the organization
   controls, held as a persistent managed record)
└── Policy-gated mediation of its use
    (the system stands between the person and the account: it either
     discloses the credential under rules — show/copy, checkout, timed
     release — or brokers the session so the credential is never revealed;
     access happens only through this gate)
    └── Attributable record of privileged use
        (who used which account, when, why — retained for audit)
```

Three properties, jointly held:

1. **Privileged account as managed unit.** The objects of record are the *target systems'* privileged accounts, not the user's own credentials. Remove → password manager / workforce credential store.
2. **Policy-gated mediation.** The system is the mandatory intermediary: disclosure is rule-gated (reason, exclusivity, time window) or the session is brokered (credential never revealed). Remove → a shared-password spreadsheet or a plain secret store; the "control" is gone.
3. **Attributable record.** Every use leaves an attributable, retained record. Remove → storage without accountability; "management" collapses.

Jointly load-bearing: (1) alone = password manager; (2) without (1) = network access broker / generic proxy; (3) without (1)+(2) = an audit log over nothing; (1)+(3) without (2) = credential archive with no control gate.

Anti-overfit notes:
- **The vault is NOT the invariant.** Boundary holds no proprietary vault (credentials from external credential stores) yet is squarely in-type. The invariant is the mediation gate, not custody. (C-layer inference from A-layer observations.)
- **Session brokering is NOT the invariant.** The earliest PAM generation (privileged password vaults with checkout) mediates by disclosure only. Brokered sessions are the mature common structure.
- **Rotation, discovery, recording, approval are NOT invariants** — all are absent from the earliest generation and/or optional modules.

### L1 — Common Mature Structure

Present across the sampled products (B-layer: cross-product commonality):

- Encrypted credential vault with permission containers (Safes / folders / smart groups / scopes / shared folders)
- Brokered privileged sessions (RDP/SSH/DB/web) where credentials are never exposed to the client
- Automated credential rotation with verify/reconcile semantics
- Discovery of privileged accounts / target systems
- Exclusive checkout or timed password release (account locked while disclosed)
- Reason-for-access capture and ITSM ticket linkage
- Request/approval workflows (dual control) and/or JIT access windows
- Session recording, playback, live monitoring
- MFA at the point of access
- RBAC over the whole estate; audit trail + reports
- Break-glass / override path (Unlimited Vault Access; bypass permissions; admin override)

### L2 — Variant / Optional Structure

- Endpoint privilege management (remove standing admin rights, application control) — packaged as sibling modules in 3/5 sampled suites
- Non-human identities: service accounts, cloud API keys — increasingly first-class (CyberArk explicit "human and non-human"; BeyondTrust cloud service principals)
- Secrets management for machines/DevOps — sibling product in every suite; boundary seam documented below
- Zero standing privileges / ephemeral accounts (Boundary, Keeper JIT, CyberArk Secure Infrastructure Access)
- Third-party/vendor remote access; OT/industrial contexts
- Behavior analytics / AI overlays (Delinea PBA, CyberArk CORA)
- Deployment shape: SaaS vs self-hosted vs hybrid; appliance
- Personal privileged accounts (CyberArk)

### L3 — Vendor-specific (Research Notes only)

- CyberArk: Safes, Platforms, CPM/PSM/PVWA component names, Master Policy, "Idira" platform rebrand, CORA AI, Ad Hoc Connections
- Delinea: secret templates, QuantumLock, Unlimited Vault Access, Distributed Engines, 30-minute default auto check-in, Delinea Platform
- BeyondTrust: Managed Systems, Functional Accounts, Smart Rules, Direct Connect SSH connection-string grammar, PAT defaults (90-day lifetime, 5 per user), BeyondInsight console, U-Series appliance
- Boundary: scopes/orgs/projects hierarchy, workers/worker tags, host catalogs, HCL configuration, transparent sessions, multi-hop, HCP editions
- Keeper: zero-knowledge encryption model, Keeper Gateway, PAM Machine/Database/Cloud record types, Commander CLI, KeeperDB

## Historical / Market-Sample Check

- **Earliest PAM generation (2000s privileged password vaults)**: vault + checkout + audit trail, no session brokering, no recording, no JIT → satisfies L0 (mediation by disclosure). ✔
- **Platform-native lineage**: Unix sudo / mainframe security (privileged command execution under policy with logging) — no held account records, no credential custody; conceptual ancestry, not the Type (OS capability, not an application of this Type). Recorded as lineage, not counterexample.
- **Modern session-brokering pole (Boundary)**: no proprietary vault → still in-type because mediation + accountability hold. ✔ (This is what forced "vault" out of L0.)
- **Password-manager-heritage pole (Keeper)**: consumer-grade vault origin, SMB tier → in-type once the privileged-account object + mediation + audit exist. ✔
- Conclusion: the definition does not over-fit the current vault-centric enterprise pattern; it survives the disclosure-only historical pole and the proxy-only modern pole.

## Vendor-specific Findings

See L3 above. Also: vendor suites consistently bundle sibling Types (endpoint privilege management, secrets management, workforce password management, IGA) — presence of a sibling in a suite is packaging evidence, not evidence that the sibling belongs to the PAM Type.

## Boundary Findings

| Neighbor | Relationship | Distinction (the "remove what" test) |
|---|---|---|
| Password Manager | adjacent, often same suite | Password manager holds the *individual's own* credentials for convenience; PAM holds the *organization's target-system privileged accounts* and mediates their use (checkout/brokering/recording). Remove the privileged-account object + mediation gate → password manager. Enterprise password managers inside PAM suites (WPM, Credential Manager, Workforce Passwords) are siblings, not the Type. |
| Secrets Management | adjacent sibling, converging | Secrets management serves *machine/programmatic* consumers pulling secrets via API; PAM centers on *people at consoles* reaching privileged accounts through gated disclosure or brokered sessions. Modern PAM covers non-human identities too (CyberArk explicit), so the seam is the primary consumer + session-level control, not "human vs machine" absolutely. Suites ship both as separate products — packaging evidence that vendors themselves treat them as distinct. |
| IAM | upstream, complementary | IAM manages the *user's own* identity, authentication, and entitlements lifecycle; PAM manages access *through* the system to target-system privileged accounts. The PAM user authenticates with their own identity (often from the IAM/IdP) and then assumes a privileged account. Remove the target-account object → IAM. |
| IGA | governance sibling | IGA certifies/reviews who should have what (access reviews, lifecycle); PAM operationally controls and records the use of privileged credentials. Certification without mediation = IGA. |
| SSO / MFA | consumed mechanisms | Authentication methods PAM consumes (IdP login, MFA at retrieval). They define no privileged-account object. |
| ZTNA | adjacent network layer | ZTNA brokers *network-level* access to private apps; PAM brokers *account/credential-level* access to privileged targets with session recording. Boundary straddles (identity-aware proxy) but its in-type surface is the privileged-session/credential layer. |
| Endpoint Management / UEM | overlapping variant | Endpoint privilege management (removing local admin, elevation on demand) overlaps device management; it is a PAM suite sibling, not the core Type. |
| SIEM | downstream consumer | PAM produces audit/session records; SIEM consumes them for correlation. Recording ≠ detection. |

## Uncertainties

- Delinea's approval/dual-control machinery was not directly evidenced in fetched pages (404 on the dual-control page); approval workflows are evidenced at CyberArk, BeyondTrust, and Keeper. Treated as common-but-not-universally-evidenced.
- Keeper evidence came through the official docs' query interface (sourced excerpts from official pages) rather than direct page fetches; treated as Tier-1 with a mediation note.
- Session recording for Delinea/BeyondTrust was evidenced indirectly (vendor maturity framing; release notes) rather than via a dedicated concept page — held as common, not universal.
- Exact numeric parameters (auto check-in interval, display timers, approval windows, PAT lifetimes) are product-specific and kept out of the canonical document.
- Market-share/market-position claims were not researched; products were chosen for representation and documentation quality.

## Final Synthesis

A Privileged Access Management application is the organization's system of control and record for its privileged accounts. Its world is built from: the **privileged account** on a target system (held as a managed record with its credential), **permission containers and policies** that decide who may do what, an **access gate** that mediates every use — either rule-gated disclosure of the credential (show/copy, exclusive checkout, timed release) or a **brokered session** in which the credential is never revealed — and the **attributable record** of who used which account, when, why, and (in mature products) what happened in the session. Around this core, mature products add rotation, discovery, approval/JIT workflows, MFA at the point of access, session recording and monitoring, and reporting. The vault is the most common implementation of custody but not the defining structure (proxy-only products are in-type); session brokering is the most common modern mediation but not the defining structure (disclosure-only historical products are in-type). The Type is distinct from password managers (own credentials vs the organization's privileged accounts), from secrets management (programmatic consumption vs gated human/machine access to privileged accounts), from IAM (own identity vs target-system privileged accounts), and from ZTNA (network access vs account-level brokering).
