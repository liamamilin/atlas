# Privileged Access Management / PAM

## Overview

A **Privileged Access Management (PAM)** application is an organization's system of control and record for its **privileged accounts** — the administrative, root, service, and other elevated accounts on its servers, databases, network devices, cloud platforms, and applications.

Its purpose is to solve a specific structural problem: privileged credentials are shared, powerful, and few, so organizations cannot treat them like personal passwords. PAM takes custody of those credentials, stands between the people who need them and the systems those credentials unlock, allows their use only under explicit policy — either by disclosing the credential under rules or by brokering a session in which the credential is never revealed — and keeps an attributable record of who used which account, when, and why.

The defining core is deliberately small:

```text
Privileged account (on a target system) held as a managed record
└── Policy-gated mediation of its use
    ├── disclosure path: credential released under rules (reason, exclusivity, time window)
    └── brokering path: session established without the credential ever being revealed
    └── Attributable record of privileged use (who, what, when, why)
```

Everything else commonly associated with PAM — credential rotation, account discovery, session recording, approval workflows, just-in-time access, MFA at the point of access — is standard capability that mature products carry, not what makes the product PAM. The earliest generation of these products was a hardened vault with checkout and an audit trail; the newest generation brokers sessions without holding a credential vault of its own. Both are recognizably PAM.

## Users & Context

PAM is an organizational security infrastructure, not a personal tool. Its users sit on both sides of the gate:

**Primary users — the people who use privileged access:**

- system, database, and network administrators who need to reach privileged accounts on the systems they operate
- IT operations and support staff performing maintenance, break-fix, or emergency work
- third-party vendors and contractors given tightly scoped, time-boxed access to specific systems

**Administrative users — the people who run the system:**

- security or identity teams who define which accounts are managed, who may use them, under what conditions, and what must be recorded
- PAM platform administrators who onboard accounts, configure rotation and session machinery, and manage permission containers

**Downstream consumers:**

- auditors and compliance functions who consume the access records, session recordings, and reports as evidence of control
- security operations, which monitors live privileged sessions and feeds access records into broader threat detection

The work context is almost always an organization with regulatory or security obligations: the value of the system is that privileged use is *controlled* (no free access to shared admin credentials) and *accountable* (every use is attributable to a person and a reason).

## Core Model

### The defining core

**Privileged account.** The central object is an account *on a target system* whose elevated access the organization controls — a domain administrator, a root account, a database admin login, a network device enable account, a service account. The record binds the account to its target system and to its credential. This is the object every workflow advances, and it is what separates PAM from tools that store a person's own credentials: the accounts of record belong to the infrastructure, not to the individual.

**Credential in custody.** The system holds the account's credential (password, key, token) as a protected asset. Users do not own these credentials; at most they borrow them through the gate. In most products the credentials live in an encrypted vault organized into permission containers — safes, folders, or scoped collections that decide who can see and use what. Custody by the system is the normal implementation, though not the only one: a product may instead pull credentials from an external secret store at the moment of use, so long as the gate and the record remain.

**Access policy.** A layer of rules decides who may use which account, how, and when: which permission container a person belongs to, whether use requires a reason or a ticket, whether it requires another person's approval, how long a disclosed credential stays valid, whether the account is locked while in use. Policy is typically expressed both as container-level permissions and as organization-wide defaults.

**The access gate.** Every use of a managed account passes through the system, in one of two forms:

- *Disclosure* — the user is shown or handed the credential under rules: a reason is recorded, the display may be time-limited, and the account is commonly locked to that one user while the credential is out (exclusive checkout). When the user is done, the credential is checked back in and typically rotated, so what was disclosed is no longer valid.
- *Brokering* — the user launches a session to the target through the system, which injects the credential on the user's behalf. The user authenticates with their *own* identity and never sees the privileged credential at all. The system acts as a proxy between the user's client and the target.

Both paths are first-class. Disclosure is the older and simpler realization; brokering is the stronger control and the direction modern products have moved. A product may offer either or both.

**Attributable record.** Every gate passage leaves a record: who requested, which account, when, for what stated reason, against which ticket, and — in mature products — a recording of what happened in the session. This record is the "management" in privileged access management: without it the system is merely a password store.

### Standard capabilities around the core

Mature products commonly add:

- **Automated credential rotation** — the system changes the target system's password on a schedule or on check-in, verifies the change took effect, and can reconcile when a change fails. Rotation is what makes disclosure survivable: a leaked checkout credential dies quickly.
- **Discovery** — scans of the environment that find privileged and local accounts "loose" on target systems and bring them under management, so coverage does not depend on someone hand-registering every admin account.
- **Request and approval (dual control)** — for sensitive accounts, use requires a second person's approval; the request carries reason, ticket, and a time window.
- **Just-in-time access** — instead of standing privilege, access is granted for a bounded window and removed afterward, sometimes by creating a temporary account that is deleted when the window closes.
- **Session recording and monitoring** — brokered sessions are recorded (video, keystroke/text, or both) for playback, and live sessions can be watched or terminated; administrators may also filter or block specific commands inside sessions.
- **MFA at the point of access** — retrieving a credential or opening a brokered session commonly requires a second factor, separate from logging into the product.
- **Break-glass override** — a tightly controlled path for emergencies that bypasses the normal gate; the override is itself recorded and alerted on.
- **Reporting and audit export** — the access record is packaged for auditors: who used what, when, and why.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:      Privileged account as managed record
Realizations: vault account entry, template-typed secret, managed account
              bound to a managed system, target with credential sources

Concept:      Permission container
Realizations: safes, secret folders, smart groups + access policies,
              scopes (organization/project), shared folders

Concept:      The access gate
Realizations: show/copy with reason + exclusive lock; checkout with
              auto check-in; timed password release; RDP/SSH proxy
              session; identity-aware proxy with credential injection;
              gateway-brokered session streamed to the user

Concept:      Attributable record
Realizations: checkout log, access-request history, session recordings
              in object storage, audit event stream, scheduled reports
```

A reader who has only seen one style — say, an enterprise vault with checkout — should still be able to recognize a proxy-style product as the same Type from the core model.

## How It Works

PAM is not a single linear flow but a small set of recurring loops.

### 1. Bring privileged accounts under management

```text
Discover (scan target systems for privileged/local accounts)
→ or register accounts manually
→ bind each account to its target system and credential
→ place it in a permission container
→ attach platform/type defaults (rotation rules, session behavior)
```

Discovery matters because the accounts that matter are exactly the ones nobody documented. The system's coverage of the organization's privileged estate is a first-class concern.

### 2. Define who may use what

Administrators populate permission containers with users and accounts, and set policy: whether use needs a reason or a ticket, whether it needs approval, how long disclosed credentials remain valid, whether the account locks while in use, whether sessions are recorded. Organization-wide defaults sit underneath per-container rules.

### 3. Request and gain access

```text
User finds the account (search / favorites / assigned list)
→ submits a request (reason, ticket, time window) — or is pre-authorized by policy
→ approval, if required (dual control / workflow)
→ access granted for the granted scope and window
```

Pre-authorized users skip the queue; sensitive accounts always pass through approval. The request itself — reason, ticket, window — becomes part of the record.

### 4. Use the access — through one of the two gates

**Disclosure path:**

```text
Request the credential (reason recorded)
→ credential displayed or copied (time-limited display)
→ account locked to this user while the credential is out
→ user connects to the target themselves
→ check in → credential rotated → lock released
```

**Brokering path:**

```text
Launch a session to the target from the portal or client
→ system authenticates the user's own identity (often with MFA)
→ system injects the privileged credential server-side
→ session established through the proxy/gateway; credential never shown
→ session recorded; window enforced; session ends
```

The brokering path is the stronger control: the endpoint that the user works from is never exposed to the privileged credential, which shrinks the surface for credential theft.

### 5. Close the loop

After use: the credential is checked in and rotated (disclosure path), the temporary elevation is removed and any ephemeral account deleted (JIT path), the recording lands in the audit store, and the access record is complete — request, reason, ticket, user, account, window, session recording.

### 6. Audit and review

Auditors and security teams consume the accumulated record: who used which privileged account, when, why, and what happened in the session. Reports and exports feed compliance evidence; live monitoring feeds security operations.

## Interfaces

### Administration console

The administrator's surface for onboarding accounts, running discovery, configuring permission containers and policies, setting rotation and session machinery, and managing users and roles. Typically a web console with grids of accounts/systems, policy editors, and health views of the machinery (rotation jobs, gateways, connectors).

### End-user portal

The privileged user's surface: a searchable list of the accounts they are allowed to request, with actions to request access, retrieve a password, or launch a session. Requests show status and approval state; favorites and filters organize large account populations. This is where reason and ticket fields appear.

### Session surfaces

The client-side experience of a brokered session: an RDP/SSH client launched through a connection file or proxy string, a browser-based session streamed from a gateway, or a launcher inside the portal. The user works in the target system while the system handles authentication invisibly.

### Session monitoring and audit console

The oversight surface: live session views (watch, terminate), the recording library with search and playback, the access-request history, and the report/export tooling. This is the auditor-facing face of the product.

### Machine and API interfaces

Programmatic access for automation: APIs and CLIs for retrieving secrets for service accounts and CI/CD pipelines, triggering rotation, and extracting audit data. In several products this surface has grown into a sibling secrets-management capability for machine consumers.

## Important Rules / Behaviors

- **The credential belongs to the system, not the user.** Disclosure is an exception granted under rules, not a handout. The strongest products make disclosure unnecessary (brokering) or self-destructing (rotation on check-in).
- **Exclusive use while disclosed.** When a credential is checked out or released, the account is commonly locked to that one user so that accountability is unambiguous: if the target was touched, the holder of the checkout is the person who touched it. Overrides exist (break-glass roles) but are themselves recorded and alerted.
- **Reason and ticket are policy-enforceable.** Products can require a stated reason and a linked change/incident ticket for every access; the requirement is a policy setting, and the captured reason becomes part of the audit record.
- **Time-boundedness.** Disclosed credentials, approved requests, and JIT elevations all carry windows; when the window ends, the credential is rotated, the elevation removed, or the ephemeral account deleted. Standing access to privileged accounts is treated as the condition to eliminate, not the default.
- **The user's own identity is always distinct from the privileged account.** Users authenticate as themselves (commonly federated to the organization's identity provider, commonly with MFA) and then *assume* the privileged account through the gate. The record preserves both: the person and the account they used.
- **Brokered sessions isolate endpoint from target.** In the brokering path the user's device never receives the credential, which both prevents theft and gives the system a control point where recording, command filtering, and termination happen.
- **Rotation can fail.** Changing a password on a remote system is a distributed operation; mature products verify the change and reconcile when a target did not accept it, because a rotation failure silently leaves the old credential valid.
- **Coverage is a goal, not a given.** Discovery exists because privileged accounts accumulate outside the system; an unmanaged admin account is the hole in the control, so products push toward finding and onboarding them.

## Variants

- **Vault-centric enterprise PAM** — the classic shape: a hardened credential vault with safes/folders, checkout, rotation, and an added session-management layer for brokering and recording. The dominant enterprise pattern.
- **Session-brokering / zero-standing-privilege PAM** — proxy-first products that broker identity-aware sessions and inject credentials from external stores, minimizing or eliminating standing privileged credentials. Common in cloud/DevOps-centric organizations.
- **Password-manager-heritage PAM** — products that grew from password management into privileged access for small and mid-sized organizations: vault plus checkout plus brokered access, lighter-weight and faster to adopt.
- **Endpoint privilege management** — a sibling capability (often bundled in PAM suites) that removes standing administrator rights from workstations/servers and elevates specific processes on demand; it manages *endpoint* privilege rather than accounts on remote targets.
- **Secrets management (sibling capability)** — machine-facing secret storage and delivery for applications and pipelines; sold alongside PAM in most suites and increasingly intertwined with it as service accounts and cloud keys come under PAM management.
- **Deployment variants** — SaaS, self-hosted, hybrid (cloud control plane with in-customer gateways/session appliances), and appliance form factors; regulated and air-gapped environments drive the self-hosted pole.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Identity & Access Management / IAM | upstream, complementary | IAM manages the user's *own* identity, authentication, and entitlements across the organization. PAM manages access *through* the system to the *target systems'* privileged accounts. A PAM user logs in with their IAM identity and then assumes a privileged account. |
| Single Sign-on / SSO | consumed mechanism | SSO federates the user's login. PAM consumes it as the front door but adds the privileged-account object, the gate, and the record — none of which SSO defines. |
| Multi-factor Authentication / MFA | consumed mechanism | MFA is a factor check at login or at the moment of credential retrieval. It defines no account custody or mediation. |
| Password Manager | adjacent, often same suite | A password manager stores the *individual's own* credentials for convenience. PAM holds the *organization's* privileged accounts and mediates their use with checkout, brokering, and audit. Remove the privileged-account object and the gate → password manager. Enterprise password managers bundled in PAM suites are siblings, not the Type. |
| Secrets Management | adjacent sibling, converging | Secrets management serves *programmatic* consumers (applications, pipelines) pulling secrets via API. PAM centers on gated access to privileged accounts with session-level control and human accountability. Modern PAM also covers service accounts and cloud keys, so the seam is the primary consumer and the session/record machinery, not strictly "human vs machine". Suites ship the two as separate products. |
| Identity Governance / IGA | governance sibling | IGA decides and certifies who *should* have access (reviews, lifecycle, approvals as governance). PAM operationally controls and records the *use* of privileged credentials. Certification without a mediation gate is IGA territory. |
| Zero Trust Network Access / ZTNA | adjacent network layer | ZTNA brokers network-level reachability to private applications. PAM brokers account/credential-level access to privileged targets with session recording. Proxy-style PAM products sit close to this line but their object is the privileged account/session, not the network path. |
| Endpoint Management / UEM | overlapping variant | Endpoint privilege management overlaps device management (both touch endpoints), but its object is privilege elevation rather than device configuration or software distribution. |
| SIEM | downstream consumer | PAM produces the privileged-access record; SIEM consumes it for correlation and detection. Recording privileged sessions is not itself threat detection. |

The most consequential boundary is with **Password Manager** and **Secrets Management**, because products increasingly span all three. The test is the object of record and the gate: the organization's privileged accounts mediated under policy with attributable records is PAM; the individual's own credentials is a password manager; machine-consumed secrets delivered programmatically is secrets management.

## Representative Products

- **CyberArk Privilege Cloud** — vault-centric enterprise leader: accounts in safes, automated rotation, session isolation/recording, discovery, dual-control requests
- **Delinea Secret Server** — vault + checkout + discovery as the entry point of a phased PAM program, with brokered remote access
- **BeyondTrust Password Safe** — managed accounts with access policies, request/approval with ticket linkage, RDP/SSH session proxying
- **HashiCorp Boundary** — identity-aware proxy pole: session brokering and credential injection without a proprietary vault
- **Keeper KeeperPAM** — password-manager-heritage pole: zero-knowledge vault as launch surface, gateway-brokered sessions, JIT with ephemeral accounts

The defining core was checked against the disclosure-only historical generation (vault + checkout + audit, no session brokering) and the proxy-only modern pole (no proprietary vault) to avoid over-fitting the definition to the current vault-centric enterprise pattern.

## Sources

Research date: **2026-09-09**

- CyberArk (Idira) — Privilege Cloud documentation: introduction & capabilities, retrieve/display password, connect to a target device, documentation-space concept map (Master Policy, dual control, session monitoring) — https://docs.cyberark.com/privilege-cloud-standard/latest/en/content/privilege%20cloud/privcloud-introduction.htm and linked pages
- Delinea — Secret Server documentation: product home, Business User Guide, Checkout Overview — https://docs.delinea.com/online-help/secret-server/start.htm and linked pages
- BeyondTrust — Password Safe / BeyondInsight documentation: Managed Accounts Overview, Accounts tab (request/release/retrieve/sessions/Direct Connect), 26.2 release notes — https://docs.beyondtrust.com/bips/docs/ps-cloud-accounts and linked pages
- HashiCorp — Boundary documentation: What is Boundary?, Domain model overview — https://developer.hashicorp.com/boundary/docs/what-is-boundary
- Keeper — KeeperPAM documentation (retrieved via the official documentation query interface, sourced from the product's architecture, JIT, and session-recording pages) — https://docs.keeper.io/

> Sourcing limitations: Delinea's approval/dual-control documentation could not be reached (page 404); approval workflows are therefore evidenced at CyberArk, BeyondTrust, and Keeper and stated as common rather than universal. Keeper evidence was retrieved through the vendor's official docs query interface rather than direct page fetches. Product-specific numeric parameters (checkout intervals, display timers, approval windows, token lifetimes) observed in vendor docs were deliberately kept out of this document; they are recorded in the paired Research Notes.
