# Research Notes — Identity & Access Management / IAM

## Research Goal

Identify the smallest stable invariant that defines the **Identity & Access Management / IAM** Application Type (directory section 15, Cybersecurity, Identity & Trust), and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

It also separates evidence into layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Identity & Access Management / IAM (directory section 15 Cybersecurity, Identity & Trust)

Nearest confusing Types (all siblings in section 15 unless noted):

- Single Sign-on / SSO — highest confusion risk; modern IAM products all include SSO
- Multi-factor Authentication / MFA — authentication-factor capability bundled in IAM
- Identity Governance / IGA — governance layer on top of IAM
- Customer Identity / CIAM — different identity population (customers, not workforce)
- Privileged Access Management / PAM — different primary object (privileged accounts/sessions)
- Machine Identity Management — non-human identities as primary object
- Password Manager (section 15) — user-held secret store, no central authority
- Secrets Management (section 14) — machine credential vaulting
- Endpoint Management / UEM (section 14) — devices as primary object; JumpCloud bundles it
- Government Digital Identity (section 24) — national-scale identity, different population and governance

Working hypothesis:

> An IAM application is the central system through which an organization administers identities, verifies them at sign-in, and grants or revokes their access to protected applications and resources.

The hypothesis is intentionally broader than "cloud SSO broker" — deployment, protocol, and directory ownership are implementation choices, not the defining invariant.

## Research Questions

Per `WORKFLOW_v1.1.md §5` (IAM example) plus boundary questions:

- What is an Identity in this Application's world, and what does its record contain?
- How do User / Group / Role / Permission relate, and which construct carries access?
- How are Authentication and Authorization distinguished and where does each happen?
- How does an identity enter the system (provisioning) and leave it (deprovisioning)?
- How do policies decide whether a sign-in or an access grant is allowed?
- What surfaces do administrators use, and what surfaces do end users use?
- What is the relationship to existing directories (AD/LDAP/HR) — store of record vs broker?
- Where is the boundary with SSO, MFA, IGA, CIAM, PAM — capability, layer, or separate Type?
- Would older, platform-native, or self-hosted products (AD DS era, open-source) still fit the definition?

## Representative Products

| Product | Why selected |
|---|---|
| Microsoft Entra ID | platform-native cloud IAM; largest install base (bundled with Microsoft 365/Azure); official docs fully reachable |
| Okta (Workforce Identity) | standalone cloud IAM market leader; vendor-neutral broker philosophy; org model documented on developer docs |
| Keycloak | open-source, self-hosted IAM; different deployment and licensing philosophy; server admin guide fully reachable |
| JumpCloud | SMB / mid-market "cloud directory" platform; directory-plus-devices philosophy; marketing/product pages reachable, support KB not |

Additional sample used for **historical / market-sample breadth** (per `WORKFLOW_v1.1.md §24`), not for primary structural evidence:

- Active Directory Domain Services (AD DS) — platform-native on-prem directory service from the pre-cloud era; used to check that the definition does not over-fit the modern cloud-broker pattern

The AD DS sample is the reason SSO federation, MFA, cloud deployment, and app catalogs must not be promoted into the defining invariant: the oldest dominant implementation of this Type had none of them and is still recognizably the same job.

## Sources

Research date: **2026-09-06**

### Source-access Limitation

Per `WORKFLOW_v1.1.md §23`:

- `help.okta.com` (Okta product help center) was not fetched; two concept-page URLs on `developer.okta.com` returned 404 (`/docs/concepts/users/`, `/docs/concepts/sso/`) before the reachable organizations concept page was found. Okta evidence is therefore limited to the organizations concept page plus what that page states about org contents and the Admin Console. Operational Okta workflow details (sign-in policies, lifecycle state machines, specific admin pages) are **not** claimed in the final document.
- `support.jumpcloud.com` (Salesforce-based help center) was not fetched; JumpCloud evidence is limited to official product/platform marketing pages, which are Tier-2 sources. JumpCloud operational details are **not** claimed in the final document beyond what its product pages state.
- No precise numeric limits, session durations, default policy values, or pricing figures are stated anywhere in the final document.

### Successfully fetched official sources

- Microsoft — What is Microsoft Entra?: https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra
- Keycloak — Server Administration Guide (v26.7.3): https://www.keycloak.org/docs/latest/server_admin/
- Okta — Okta organizations (developer docs): https://developer.okta.com/docs/concepts/okta-organizations/
- JumpCloud — platform homepage: https://jumpcloud.com/platform
- JumpCloud — Open Cloud Directory product page: https://jumpcloud.com/platform/cloud-directory
- Microsoft — Active Directory Domain Services overview: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview

## Product Observations

### Microsoft Entra ID (learn.microsoft.com) — Layer A

- Official framing: "a cloud-based identity and access management service that provides authentication, policy enforcement, and protection for users, devices, apps, and resources."
- Tenant model: every Microsoft 365, Azure, or Dynamics CRM Online subscriber is automatically an Entra tenant; each new directory gets an initial domain (`contoso.onmicrosoft.com`) and can add custom domain names. Identity administration is coupled to the organization's Microsoft tenant.
- The Entra family splits adjacent layers into separately named products — strong boundary evidence:
  - **Entra ID Governance**: "automating access requests, assignments, and reviews… identity lifecycle management" (e.g. auto-assign accounts/groups/licenses to new employees, remove on departure)
  - **Entra ID Protection**: identity-risk detection with risk-based Conditional Access policies
  - **Entra External ID**: B2B collaboration and customer identity (CIAM), including self-service registration with one-time passcodes or social accounts
  - **Entra Workload ID**: identities for applications, services, containers
  - **Entra Agent ID**: identity constructs for AI agents
  - **Entra Domain Services**: managed Kerberos/NTLM/LDAP for legacy apps
  - **Private/Internet Access**: network-access products (ZTNA/SSE family, outside this Type)
- Administration surfaces: the web-based **Microsoft Entra admin center** ("configuring and managing Microsoft Entra products from a single interface") and the **Microsoft Graph API** for automating "administrative tasks like license deployments and user lifecycle management."
- Licensing tiers exist (Free/P1/P2/Suite etc.) — feature gating is commercial, not structural.

### Keycloak (Server Administration Guide) — Layer A

- Self-description: "a single sign on solution for web apps and RESTful web services," deployed as "a separate server that you manage on your network." Applications redirect the browser to Keycloak for authentication; "applications never see a user's credentials" and instead receive cryptographically signed identity tokens or assertions carrying identity and permission data.
- Core concepts (verbatim-grounded):
  - **users** — "entities that are able to log into your system," with attributes, group membership, and roles
  - **authentication** — "the process of identifying and validating a user"
  - **authorization** — "the process of granting access to a user"
  - **credentials** — "pieces of data that Keycloak uses to verify the identity of a user" (passwords, one-time-passwords, digital certificates, fingerprints)
  - **roles** — "identify a type or category of user"; applications assign access to roles rather than individual users
  - **user role mapping** — mapping between a role and a user; encapsulated into tokens so applications can decide access
  - **groups** — "manage groups of users"; members inherit the group's attributes and role mappings. "Groups are a collection of users to which you apply roles and attributes. Roles define types of users, and applications assign permissions and access control to roles."
  - **realms** — "a realm manages a set of users, credentials, roles, and groups… Realms are isolated from one another"; a master realm administers other realms
  - **clients** — "entities that can request Keycloak to authenticate a user" (applications and services)
  - **sessions** — created at login; admins and users can view and manage them
  - **user federation** — validate credentials against external LDAP/Active Directory stores
  - **identity provider federation** — delegate authentication to external OIDC/SAML IdPs or social providers
  - **required actions** — actions a user must complete during authentication (e.g. update password, verify email)
  - **authentication flows** — configurable workflows defining what credentials/steps are required (browser login, registration, reset credentials, step-up)
  - **events** — "audit streams that admins can view and hook into" (user events and admin events)
- Feature list observed: SSO/Single Sign-Out, OIDC, OAuth 2.0, SAML, brokering, social login, LDAP/AD federation, Kerberos bridge, **Admin Console** ("central management of users, roles, role mappings, clients and configuration"), **Account Console** ("allows users to centrally manage their account" — sign-in methods, device activity, group memberships, linked IdPs, app access), themes, flexible authentication (passkey/password/X.509, step-up), two-factor (passkey, recovery codes, TOTP/HOTP), login flows (self-registration, forgot password, verify email), session management, token mappers, revocation policies, brute-force detection/lockout, SCIM user/group endpoints, Admin REST API and Admin CLI, delegated realm administration with fine-grained admin permissions.
- Admin operations observed: create users, set/request password resets, create OTP credentials, enable self-registration, impersonate a user ("an administrator with the appropriate permissions can impersonate a user"), delete users, manage sessions (sign out all active sessions), manage roles/groups, configure password and OTP policies.

### Okta (developer.okta.com, organizations concept page) — Layer A (limited)

- The **org** is "a root object and a container for all other Okta objects. It contains resources such as users, groups, and app integrations (apps), as well as policy and configurations."
- "Within every org, there are users and apps. These are the only mandatory items that you must configure for your org to use Okta."
- User sources: "You can create users in Okta, import them through directory integrations, or through app integrations."
- Apps: "connections to public apps (such as Office 365) or connections to proprietary apps (such as your own apps)."
- **Admin Console**: "where you go to manage your Okta org"; landing Dashboard "provides a summary of activity in Okta and in your apps" plus notifications of problems/outstanding work; separate admin URL (`-admin` subdomain).
- Orgs are "hard boundaries" — objects cannot be shared across orgs; federation can allow sign-in across organizations while "users still exist in each org separately." Multiple orgs are used to segregate internal vs external populations.
- Operational details beyond the org model (sign-in policy UI, lifecycle states, workflow specifics) were not reachable — see Source-access Limitation.

### JumpCloud (product/platform pages) — Layer B (marketing tier)

- Positioning: "Unified Platform for Identity, Access, & Devices"; the directory product is "Open Cloud Directory: The Alternative to Legacy AD" — "Consolidate all identities—human, machine, and agent—secure access, and device management into one automated source of truth."
- "One Unified Identity Per User": "Create user accounts or easily import them from another authoritative identity source, such as your HR system or existing directory. Automate your lifecycle management so that one change in your source of truth reflects across all resources in real-time."
- Native directory capabilities claimed: SSO, password management, MFA/2FA, cloud LDAP, cloud RADIUS, SSH key management, cross-OS device management and MDM, identity governance/auditing.
- Platform taxonomy on the product pages: **Identity Management** (Cloud Directory, Identity Lifecycle Management, HRIS integration), **Access Management** (PAM, SSO, Cloud LDAP, Cloud RADIUS, MFA, Password Vault, Conditional Access, Access Request, Directory Insights), **Device Management** (UEM/MDM, patch, remote access), plus API services, SaaS management, workflows.
- MSP orientation: multi-tenant portal for partners.
- Because these are marketing pages (Tier 2), they are used for positioning and module structure only; no operational workflow claims are drawn from them.

### Active Directory Domain Services (historical sample) — Layer A

- "A directory is a hierarchical structure that stores information about objects on a network… AD DS stores information about user accounts, such as names, passwords, phone numbers."
- "Security is integrated with AD DS through sign-in authentication and access control to objects in the directory. With a single network username and password, administrators can manage directory data and organization throughout their network, and authorized network users can access resources anywhere on the network."
- "Policy-based administration eases the management of even the most complex network."
- Structural elements: schema (object/attribute classes), global catalog, query/index, replication across domain controllers.
- Notably absent vs modern products: no SaaS app federation, no MFA, no cloud multi-tenancy, no self-service portals. Yet the job — administered identity records + sign-in authentication + access control + central policy administration — is fully present. This anchors the L0.

## Cross-product Comparison

| Finding | Entra ID | Okta | Keycloak | JumpCloud | AD DS (historical) | Abstraction level |
|---|---|---|---|---|---|---|
| administered identity records (user accounts with attributes) | yes | yes ("users… in every org") | yes (users) | yes ("one unified identity per user") | yes (user accounts) | L0 |
| authentication of the identity before access | yes ("authentication, policy enforcement") | yes (org policy; sign-in implied by product) | yes ("process of identifying and validating a user") | yes (MFA/SSO/password mgmt) | yes (sign-in authentication) | L0 |
| access grants linking identities to protected apps/resources | yes (apps and resources) | yes (app integrations) | yes (roles/role mappings → clients) | yes (SSO/LDAP/RADIUS access) | yes (access control to objects) | L0 |
| central administrative control surface | yes (admin center + Graph API) | yes (Admin Console) | yes (Admin Console + REST API + CLI) | yes (admin console implied; Directory Insights) | yes (policy-based administration) | L0 |
| groups as grantable containers | yes | yes (groups in org) | yes (groups inherit roles/attributes) | yes (user groups) | yes (security groups) | L1 |
| roles / role-based assignment | yes | yes (implied by policy/app model) | yes (roles, role mapping, composite roles) | yes (implied by access mgmt modules) | partial (group-based) | L1 |
| SSO federation to third-party apps (SAML/OIDC/WS-Fed) | yes | yes (app integrations) | yes (OIDC/OAuth2/SAML) | yes (SSO module) | no | L1 |
| app catalog / prebuilt integrations | yes (integrated cloud apps) | yes (public apps e.g. Office 365) | partial (clients registered manually) | yes (application catalog) | no | L1 |
| credential & factor management (password policy, reset, MFA) | yes | yes (implied) | yes (password policies, OTP, WebAuthn/passkeys, required actions) | yes (password mgmt, MFA/2FA) | password only | L1 |
| self-service portal for end users | yes | yes (implied by org model) | yes (Account Console) | yes (implied) | no | L1 |
| lifecycle automation (joiner/mover/leaver, HR/directory sync) | yes (Graph lifecycle; Governance product) | yes (directory/app import) | yes (LDAP/AD federation, SCIM, workflows) | yes (HRIS import, lifecycle automation) | no | L1 |
| audit/event logging | yes | yes (Dashboard activity summary) | yes (user + admin events) | yes (Directory Insights) | limited | L1 |
| session management (view/revoke) | yes | yes (implied) | yes (admin + user session management) | not asserted | no | L1 |
| delegated administration | yes | yes (multi-org, admin roles implied) | yes (master realm, fine-grained admin permissions) | yes (MSP multi-tenant portal) | partial (AD delegation) | L1 |
| deployment: cloud multi-tenant | native | native | self-hosted (or 3rd-party hosted) | cloud | on-prem | L2 |
| identity substrate: native store vs federated (AD/LDAP/HR) | both (tenant-native + sync) | both (create/import) | both (internal + federation) | both (create/import) | native store | L2 |
| conditional / risk-based access policy | yes (Conditional Access, ID Protection) | yes (org policy; specifics not fetched) | partial (conditional flows, brute-force lockout) | yes (Conditional Access module) | no | L2 |
| governance layer (access reviews, requests/approvals) | separate product (ID Governance) | not asserted | partial (workflows, SCIM) | yes (Access Request, governance/auditing claims) | no | L2 / adjacent Type |
| customer-facing identity (self-registration, social login) | separate product (External ID) | not asserted | optional feature (self-registration, social brokering) | not asserted | no | L2 / adjacent Type |
| machine/workload/agent identities | separate product (Workload ID, Agent ID) | not asserted | partial (service accounts, clients) | claimed ("human, machine, and agent") | computer accounts | L2 / adjacent Type |
| device management integration | adjacent (Intune/other) | adjacent | no | bundled (UEM/MDM) | partial (domain join) | L2 / adjacent Type |
| legacy protocol bridges (LDAP/RADIUS/Kerberos) | yes (Domain Services) | yes (AD integrations implied) | yes (LDAP/Kerberos) | yes (Cloud LDAP/RADIUS) | native | L2 |
| developer platform (APIs, token customization) | yes (Graph, identity platform) | yes (management API implied) | yes (Admin REST API, SPIs, protocol mappers) | yes (API services) | no | L2 |
| multi-tenant / MSP management | tenant model | orgs, Aerial, Org Creator | realms | multi-tenant portal | forests/domains | L2 |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as IAM:

```text
Organization-administered Identity
└── Authentication (the system verifies the identity before access)
└── Access Grant (identity → protected application / resource)
└── Central administrative control (create / change / revoke identities and access)
```

Four properties. If any one is removed, the product either stops being recognizable as IAM or becomes a different Application Type:

- remove the **administered identity records** → a policy engine or network gate with nobody to administer (not IAM)
- remove **authentication** → a pure directory/provisioning data tool (identity data sync without access decisions)
- remove **access grants** → a credential store or password manager (identities verified but nothing authorized)
- remove **central administrative control** → self-enrolled consumer accounts (drift toward CIAM) or user-held secrets (password manager)

Deliberately **not** in L0 (checked against §24 historical/market samples): SSO federation protocols, MFA, groups/roles, app catalogs, self-service portals, audit logging, HR-driven lifecycle, cloud deployment, APIs. AD DS — the dominant pre-cloud implementation — satisfies the four properties with none of the modern additions; Keycloak, Entra ID, Okta, and JumpCloud satisfy them with all of them.

## L1 — Common Mature Structure

Common in mature modern IAM products; not required for the Type:

```text
Directory constructs: groups (grantable containers), user attributes/profile
Roles / role-based assignment (access attached to roles or group membership, not individuals)
SSO federation to applications (SAML / OIDC / WS-Federation) + app catalog / prebuilt integrations
Credential & factor management: password policies, self-service reset, MFA enrollment
Lifecycle automation: provisioning / deprovisioning driven by HR or directory sync (joiner-mover-leaver)
Audit / event logging of sign-ins and administrative changes
Session management (view and revoke active sessions)
Two primary surfaces: Admin Console + end-user portal (app launcher / account self-service)
Delegated administration (scoped admin roles, multi-domain/multi-realm/multi-org management)
```

A product can be a fully recognizable IAM without an app catalog, without self-service, even without MFA — but a typical modern product includes most of these.

## L2 — Variant / Optional Structure

```text
Deployment
- cloud multi-tenant SaaS
- self-hosted / open source
- hybrid (cloud broker federating an on-prem directory)

Identity substrate
- native cloud directory as source of truth
- federated/synced from Active Directory, LDAP, or HR system
- delegated to external identity providers (social, partner IdPs)

Access policy sophistication
- static assignment (groups/roles only)
- conditional / risk-based access (device posture, location, risk level)

Governance layer (→ IGA boundary)
- access reviews / certification
- access requests with approvals
- separation of duties

Identity population (→ CIAM / machine-identity boundaries)
- workforce only
- + external partners / guests
- + customers (self-registration, consent, social login)
- + machines / workloads / AI agents

Adjacent bundling
- device management (UEM/MDM) in the same platform
- privileged access (session vaulting) in the same platform
- password vaulting

Legacy protocol bridges
- LDAP, RADIUS, Kerberos for non-federated resources

Developer platform
- management APIs, CLI
- token/claim customization, embedded authentication

Commercial shape
- standalone product
- platform suite component
- bundled with a productivity tenant
- open source with paid support
```

## L3 — Vendor-specific Structure

Belongs in Research Notes only:

- **Keycloak**: realms (isolated user/credential/role/group sets), master realm, clients, client scopes, protocol mappers, composite roles, required actions, authentication flows, themes, SPIs, Account Console specifics, LDAP edit modes (READ_ONLY/WRITABLE/UNSYNCED), impersonation role, brute-force lockout configuration, Admin CLI, SCIM endpoints, organizations feature, workflow engine (onboarding/offboarding/inactivity)
- **Okta**: org as root container, org URLs / admin subdomain, cells, preview vs production orgs, Okta Integration Network, Aerial multi-org management, Org Creator, rate limits, free trial / integrator plans
- **Microsoft Entra ID**: tenant coupling to Microsoft 365/Azure, initial `*.onmicrosoft.com` domain, admin center, Microsoft Graph, product-family split (ID Governance, ID Protection, External ID, Workload ID, Agent ID, Verified ID, Domain Services, Private/Internet Access), licensing tiers (Free/P1/P2/Suite)
- **JumpCloud**: "Open Directory" branding, Directory Insights, HRIS integration, password vault, cloud LDAP/RADIUS as directory capabilities, device-management bundling, MSP multi-tenant portal, "Secure, Frictionless Access" marketing term
- Any numeric limits, session durations, default policy values, pricing

## Canonical Model (v1.1)

```text
L0
Organization-administered Identity
├── Authentication (verify the identity before access)
├── Access Grant (identity → protected application / resource)
└── Central administrative control (create / change / revoke identities and access)
```

This is the entire Core Model. Everything else is L1 or lower.

Concept → implementation separation:

```text
Concept:            Administered Identity
Implementations:    cloud directory user, realm user, synced AD/LDAP object, HR-imported account

Concept:            Authentication decision point
Implementations:    hosted login page with SAML/OIDC redirect, Kerberos domain sign-in,
                    LDAP bind, RADIUS, brokered social/partner IdP login

Concept:            Access Grant
Implementations:    group membership, role mapping, app assignment, entitlement, ACL on directory objects

Concept:            Central administrative control
Implementations:    web admin console, REST/Graph API, CLI, policy engine, delegated scoped admin
```

## Boundary Findings

### vs Single Sign-on / SSO (sibling leaf)

- SSO is the **federation capability** — in every sampled modern product it is an L1 component of IAM, not a competing structure. A standalone SSO product without identity lifecycle and administration is a capability product.
- Boundary test: strip federation from an IAM and it is still IAM (AD DS proves it); strip identity administration from an SSO product and nothing recognizable remains.
- Directory risk: the SSO leaf may be a Capability/Variant of IAM rather than an independent Type. Flagged for joint review.

### vs Multi-factor Authentication / MFA (sibling leaf)

- MFA is an **authentication-factor capability**. Inside IAM it appears as credential/factor management and policy (Keycloak OTP/WebAuthn policies; JumpCloud MFA module; Entra risk-based Conditional Access). A standalone MFA product enforces factors without owning the identity lifecycle.
- Directory risk: same as SSO — likely a Capability of IAM. Flagged for joint review.

### vs Identity Governance / IGA (sibling leaf)

- Governance (access reviews, certification, access requests, separation of duties) is a **layer on top of** the IAM core. Microsoft ships it as a separate product (Entra ID Governance) — market evidence that the layer is distinct — but its objects (identities, access grants) are the IAM objects.
- Boundary test: an IAM without reviews is still IAM; a governance product without an identity store/authN has nothing to govern.

### vs Customer Identity / CIAM (sibling leaf)

- Different identity **population and administration model**: customers self-register and self-manage; the organization does not provision them as employees. Entra ships it as a separate product (External ID); Keycloak exposes self-registration/social brokering as optional features; Okta documents multi-org segregation of internal vs external users.
- Boundary test: flip the primary administration model from org-provisioned to self-enrolled and the product has drifted to CIAM.

### vs Privileged Access Management / PAM (sibling leaf)

- Different primary **object**: privileged accounts, credential vaulting, and session brokering vs the ordinary workforce identity lifecycle. JumpCloud bundles a PAM module inside its platform, which shows the market treats it as a distinct capability even when sold together.

### vs Machine Identity Management (sibling leaf)

- Different primary **subject**: non-human actors (services, workloads, agents). Keycloak's service accounts and AD's computer accounts are L2 presences inside IAM products; Entra ships Workload ID / Agent ID as separate products. The directory split is defensible; the boundary is the subject of the identity, not the mechanism.

### vs Password Manager (sibling leaf)

- A password manager is a **user-held secret store** with no central authority over identities and no authorization of resources. IAM holds credentials as one attribute of an administered identity and couples them to access decisions.

### vs Directory service (AD DS / LDAP — not a separate leaf here)

- A directory is the **store**; IAM is the **administration + decision system**. The historical sample shows the two grew together: AD DS already combines the store with sign-in authentication, object access control, and policy administration, i.e. it satisfies this Type's L0. The modern category adds federation/brokerage and lifecycle automation as L1. The boundary between "directory service" and "IAM" is therefore a deployment-era gradient, not a structural wall — recorded as a boundary observation.

### vs Endpoint Management / UEM (section 14)

- Devices are a different primary object. JumpCloud bundles UEM/MDM with its directory, and Entra's family includes network-access products — evidence that identity platforms absorb adjacent capabilities commercially, without the device becoming an IAM core object. Device posture can serve as a **policy input** to access decisions (L2).

### Cleanest boundary test

> Remove the identity records → nothing left to administer.
> Remove authentication → an identity data sync tool.
> Remove access grants → a password manager.
> Remove central administration → a consumer account system (CIAM drift).
> Remove only SSO/MFA/catalogs/self-service → still IAM (AD DS era proves it).

## Uncertainties

- Okta's product help center was unreachable; Okta observations are limited to the org model, mandatory objects (users + apps), user sources, and the Admin Console's existence/landing page. Okta-specific workflow claims (sign-in policy mechanics, lifecycle state names) are intentionally absent.
- JumpCloud evidence is marketing-tier (Tier 2); its support KB was not fetched. Claims about JumpCloud are limited to positioning and module structure.
- The exact L1 status of "roles" vs "groups": all sampled products carry both constructs, but their semantics differ per product (Keycloak documents the distinction explicitly; AD DS historically used security groups for both purposes). Placed at L1 as "grantable containers" rather than asserting a universal role/group/permission ontology.
- Whether the directory should eventually split "IAM" into workforce-IAM vs CIAM vs machine-identity as fully independent Types is a taxonomy question; this research documents the boundaries and flags the sibling leaves (SSO, MFA) that look most like Capabilities rather than Types.
- Historical samples beyond AD DS (e.g. Novell eDirectory, IBM Tivoli) were not directly fetched; the AD DS page was used as the single platform-native anchor, so claims about "older IAM" are calibrated to that evidence only.

## Final Synthesis

Canonical Identity & Access Management / IAM, v1.1:

```text
L0 (defining invariant)
- Organization-administered identity records
- Authentication of the identity before access is granted
- Access grants linking identities to protected applications/resources
- Central administrative control over identities and access (create / change / revoke)

L1 (common mature structure)
- Groups as grantable containers; user attributes/profile
- Roles / role-based assignment
- SSO federation to applications + app catalog / integrations
- Credential & factor management (password policy, self-service reset, MFA)
- Lifecycle automation (HR/directory-driven provisioning & deprovisioning)
- Audit / event logging
- Session management
- Admin Console + end-user self-service portal
- Delegated administration

L2 (variant / optional)
- Deployment (cloud SaaS / self-hosted / hybrid)
- Identity substrate (native store / AD-LDAP-HR federation / external IdPs)
- Conditional & risk-based access policy
- Governance layer (reviews, requests, SoD → IGA boundary)
- Identity population extensions (guests, customers → CIAM; machines/agents → machine identity)
- Bundled adjacent capabilities (device management, PAM, password vault)
- Legacy protocol bridges (LDAP / RADIUS / Kerberos)
- Developer platform (APIs, token customization)
- Commercial shape (standalone / suite component / tenant-bundled / open source)
```

The Application Document will present only L0 and L1, with a Variants section naming L2 options. L3 stays in these Research Notes.
