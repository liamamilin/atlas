# Identity & Access Management / IAM

## Overview

An **Identity & Access Management (IAM) application** is the central system through which an organization administers identities, verifies them at sign-in, and grants or revokes their access to protected applications and resources.

The defining structure is small:

```text
Organization-administered Identity
└── Authentication (the system verifies the identity before access)
    └── Access Grant (identity → protected application / resource)
        └── Central administrative control (create / change / revoke identities and access)
```

Everything commonly associated with modern IAM — SSO federation, MFA, app catalogs, self-service portals, HR-driven lifecycle automation, conditional access policy — is widespread in current products but is not part of the defining core. The oldest dominant implementation of this job (the on-prem directory service with sign-in authentication and object access control) satisfies the definition with none of those additions, and open-source, self-hosted, and cloud-broker products all satisfy it with all of them.

When the primary identity population shifts from organization-administered members to self-enrolling customers, or from people to machines and AI agents, the product is drifting toward a different Application Type (Customer Identity / CIAM, Machine Identity Management).

## Users & Context

The primary users are **administrators** — IT, security, or identity teams who operate the system on behalf of the organization:

- create, modify, disable, and remove identity records
- attach and remove access (via groups, roles, or direct app assignment)
- configure how sign-in works (credentials, factors, policies)
- investigate sign-in problems and audit what happened

The secondary user is the **end user** (employee, contractor, partner) who experiences IAM mostly at two moments: signing in, and regaining access (password reset, factor re-enrollment). In mature products the end user also has a small self-service surface: a launcher of the applications they may open, their profile, their sign-in methods, and their active sessions.

The work context is organizational: identities exist because the organization says so, and their access exists because the organization granted it. This is the structural difference from consumer account systems, where the user enrolls and administers themselves.

## Core Model

### The Defining Core

```text
Organization-administered Identity
└── Authentication (verify the identity before access)
└── Access Grant (identity → protected application / resource)
└── Central administrative control (create / change / revoke identities and access)
```

Four properties. If any one is removed, the product is no longer recognizable as IAM:

- **Organization-administered identity records** — the application maintains accounts for the people (and commonly non-human actors) the organization administers, each with attributes and at least one credential or authenticator. Without this, there is nothing to administer.
- **Authentication** — the system verifies (or governs the verification of) an identity's credentials before access is granted. Without this, the product is an identity data store, not access management.
- **Access grants** — access to protected applications and resources is assigned to identities, is visible to them, and can be changed or revoked. Without this, the product is a credential store.
- **Central administrative control** — administrators, not end users alone, create, change, and remove identities and their access from a central control surface. Without this, the product drifts to self-enrolled consumer identity or user-held secrets.

### Capabilities Shared by Mature Products

A typical modern IAM product carries most of these capabilities. They are not what makes the product an IAM, but they make IAM practical at organizational scale.

- **Groups as grantable containers** — access is attached to a group or role, and identities receive it by membership. This is the pivot that makes access manageable at scale; direct identity-to-resource grants are the exception path.
- **Roles / role-based assignment** — named bundles of access ("type or category of user") that applications and admins assign to, rather than configuring each resource per person.
- **SSO federation to applications** — applications delegate sign-in to the IAM system (commonly via standard federation protocols such as SAML or OpenID Connect); the application receives a signed assertion or token and never handles the user's credentials. Prebuilt app integrations / catalogs are the common commercial expression of this.
- **Credential & factor management** — password policies, administrator- or self-initiated password reset, and enrollment of additional factors (one-time passwords, passkeys/security keys) as sign-in requirements.
- **Lifecycle automation** — identities enter (created manually, imported from an HR system, or synced from an existing directory), move (role change → group change → access change), and leave (disable, revoke sessions, remove access) through repeatable processes rather than ad-hoc edits.
- **Audit / event logging** — sign-in events and administrative changes are recorded as a queryable stream.
- **Session management** — active sign-in sessions can be viewed and revoked, by admins and often by the users themselves.
- **Two primary surfaces** — an Admin Console for the organization's operators, and an end-user portal (app launcher + account self-service). These are structurally distinct surfaces of the same system.
- **Delegated administration** — administrative authority can be scoped (per domain, realm, org, or subset of users), so large organizations distribute admin work without granting blanket control.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. The Variants section below enumerates how specific implementations realize each concept.

```text
Concept:          Administered Identity
Implementations:  cloud directory user, self-hosted realm user, synced directory object, HR-imported account

Concept:          Authentication decision point
Implementations:  hosted login page with browser redirect (SAML/OIDC), domain/Kerberos sign-in,
                  LDAP bind, RADIUS, brokered social or partner identity provider

Concept:          Access Grant
Implementations:  group membership, role mapping, application assignment, entitlement, object ACL

Concept:          Central administrative control
Implementations:  web admin console, management API, CLI, policy engine, scoped/delegated admin roles
```

A reader who only encounters one implementation (e.g. only a cloud SSO broker) should still be able to recognize an on-prem directory service or a self-hosted open-source product as the same Application Type from the Core Model.

## How It Works

IAM is not one flow but a small set of recurring loops. The four below are the defining ones.

### Provisioning — how an identity enters

```text
A person joins (or a workload is created)
→ an identity record is created (manually, by HR-driven automation, or by directory sync)
→ the identity is placed into groups / assigned roles
→ access to applications follows from those memberships
→ credentials or authenticators are issued (set password, enroll factor)
→ the person signs in for the first time and completes any required setup
```

The essential mechanic: **access follows membership, not personhood**. The admin rarely grants an application to a person directly; they put the person in a container that already carries the access.

### Authentication — how access is exercised

```text
User opens an application (or the app launcher)
→ the application redirects to the IAM system's sign-in surface (or the resource challenges locally)
→ the user presents credentials / factors
→ the system evaluates sign-in policy (who, from where, on what device, what risk)
→ on success, a session or signed token/assertion is issued
→ the application admits the user based on the identity and access data it received
```

The essential mechanic: **the application never handles the raw credentials**. Authentication is brokered; the application trusts a signed statement of who the user is and what roles/groups apply.

### Authorization administration — how access changes

```text
Admin creates or edits a group / role / app assignment
→ identities gain or lose the attached access
→ the change takes effect at the next sign-in or token refresh (product-dependent)
→ the change is recorded in the audit stream
```

### Deprovisioning — how an identity leaves

```text
A person leaves (or a workload is retired)
→ the identity is disabled or deleted (manually or by HR-driven automation)
→ active sessions are revoked
→ access grants disappear with the identity or its memberships
→ the audit stream records the offboarding
```

The essential mechanic: **offboarding is a first-class lifecycle event**, not a cleanup task. The system is designed so that one administrative action removes a person's ability to sign in everywhere.

### Core vs Common vs Optional

Capabilities fall into three tiers:

**Defining core** — without these, not IAM.

- organization-administered identity records
- authentication before access
- access grants to protected applications/resources
- central administrative control

**Common mature structure** — present in most modern products.

- groups as grantable containers
- roles / role-based assignment
- SSO federation + app integrations
- credential & factor management (policies, reset, MFA)
- lifecycle automation (joiner-mover-leaver)
- audit / event logging
- session management
- Admin Console + end-user portal
- delegated administration

**Variant / optional** — depends on segment, deployment, security posture, customer scale.

- deployment: cloud SaaS / self-hosted / hybrid
- identity substrate: native store / directory or HR federation / external IdPs
- conditional & risk-based access policy
- governance layer (access reviews, requests, separation of duties)
- population extensions: guests, customers, machines, AI agents
- bundled adjacent capabilities (device management, privileged access, password vault)
- legacy protocol bridges (LDAP / RADIUS / Kerberos)
- developer platform (APIs, token customization)
- commercial shape (standalone / suite component / tenant-bundled / open source)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Admin Console

The operator's primary surface.

- directory views: users, groups, roles (searchable lists with detail views)
- application/integration views: which apps are connected and who can use them
- policy views: sign-in requirements, factor requirements, access rules
- lifecycle views: pending provisioning, sync status, required user actions
- audit views: sign-in and admin-change event streams
- primary actions: create/edit/disable/delete identities, manage memberships, connect applications, configure policies, review events

### End-user portal / app launcher

The member's primary surface.

- the set of applications the person may open (their access grants, made visible)
- profile and contact attributes
- sign-in method management: change password, enroll or replace factors
- active sessions and (in some products) linked devices
- primary actions: open an app, reset a credential, manage factors, sign out sessions

### Sign-in surface

The moment the whole system exists for.

- identity input (username/email), credential or factor challenge
- policy-driven steps: additional factor, required actions (e.g. set a new password), risk-based interstitials
- on success: redirect back to the application with a signed identity statement

### Directory / sync configuration

The surface where the identity substrate is wired up.

- connections to HR systems, existing directories, or external identity providers
- mapping rules: which fields flow where, how often, in which direction
- primary actions: add/edit connections, test sync, resolve conflicts

### Management API / CLI

The automation surface for the same administrative operations the console exposes — used for lifecycle automation, bulk operations, and infrastructure-as-code styles of administration.

## Important Rules / Behaviors

### Access follows membership

The dominant pattern is that access is attached to containers (groups, roles, app assignments) and identities inherit it. Changing a person's job means changing their memberships, not their per-app permissions. This is the structural reason IAM scales.

### Authentication is brokered, not delegated blindly

Applications receive a signed statement of identity (and often role/group data), not the user's credentials. The IAM system is the single point where credentials live and sign-in policy is enforced. This is a defining behavior of the modern Type, and the reason an IAM can change sign-in requirements (add a factor, block a credential) without touching any application.

### Disabling an identity ends access

A disabled or deleted identity cannot authenticate, and its access grants become inert. Mature products also propagate session revocation, so offboarding takes effect on live sessions, not just future sign-ins.

### The identity substrate question is structural

Every product must answer: which store is the source of truth? A native cloud directory, a synced on-prem directory, or an HR system. The answer determines how provisioning works and what happens when sources disagree — it is an architectural decision, not a feature toggle.

### Administrative power is itself permissioned

The system that enforces access for everyone must also control its own operators: admin roles are scoped, administrative actions are logged as events, and (in mature products) administrators can be delegated limited authority. The IAM is thus both the access-control system for the organization and a protected application in its own right.

### Auditability is a structural expectation

Sign-ins and administrative changes are recorded as events. This is not an add-on analytics feature; it is what makes central control accountable and is typically required by the organization's compliance posture.

## Variants

The IAM Type is implemented in many ways. Common variants:

- **cloud multi-tenant IAM / SSO broker** — cloud-hosted directory plus federation broker to SaaS applications; the dominant modern shape for workforce identity
- **platform-native IAM** — identity administration bundled with a productivity/cloud platform tenant; every subscriber of the platform automatically has the identity service
- **self-hosted / open-source IAM** — deployed as a separate server the organization operates; isolated administrative partitions keep populations (and often environments) separate; customization via themes and extensions
- **cloud directory platform** — directory-first product that also absorbs device management, legacy protocol bridges (LDAP/RADIUS), and privileged access; common in SMB/mid-market and MSP contexts
- **hybrid IAM** — cloud broker federating an existing on-prem directory; the on-prem store remains the source of truth
- **governance-heavy IAM** — the same core plus access reviews, access requests, and certification, often delivered as a governance layer product
- **customer-facing identity (CIAM)** — the same machinery pointed at self-enrolling customers with consent and social login; a separate Type in this directory
- **workload / agent identity** — the same machinery pointed at services, workloads, and AI agents; increasingly split into its own Type

A variant should remain a **Variant**, not become a separate Type, unless the variant changes users, core objects, workflow or rules in a way that the Core Model no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Single Sign-on / SSO | the federation capability inside IAM; a standalone SSO product lacks identity lifecycle and administration as primary structure — likely a Capability/Variant of this Type (flagged for joint review) |
| Multi-factor Authentication / MFA | the authentication-factor capability inside IAM; a standalone MFA product enforces factors without owning identities or access grants — likely a Capability/Variant (flagged for joint review) |
| Identity Governance / IGA | a governance layer (access reviews, requests, separation of duties) on top of the IAM core; its objects are the IAM objects; vendors ship it as a separate layer |
| Customer Identity / CIAM | same machinery, different population and administration model: customers self-enroll instead of being organization-provisioned |
| Privileged Access Management / PAM | primary object is privileged accounts, credential vaulting, and session brokering, not the ordinary workforce identity lifecycle |
| Machine Identity Management | primary subject is non-human actors (services, workloads, agents); appears inside IAM only as an optional extension |
| Password Manager | user-held secret store; no central authority over identities and no authorization of resources |
| Secrets Management | machine credential vaulting for infrastructure; no human sign-in or workforce lifecycle |
| Endpoint Management / UEM | devices are the primary object; device posture may feed IAM policy as an input, but device administration is a different Type |
| Government Digital Identity | national-scale identity for citizens; different population, governance, and legal semantics |

The boundary with the SSO and MFA sibling leaves is the most important one, because modern IAM products bundle both. The structural test: strip federation and factors from an IAM and it is still IAM (the on-prem directory era proves it); strip identity administration from an SSO or MFA product and nothing recognizable remains.

## Representative Products

- Microsoft Entra ID
- Okta (Workforce Identity)
- Keycloak
- JumpCloud

The Core Model was checked against a platform-native historical sample (Active Directory Domain Services) to avoid over-fitting the definition to the modern cloud-broker pattern.

## Sources

Research date: **2026-09-06**

Primary official sources:

- Microsoft — What is Microsoft Entra?: https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra
- Keycloak — Server Administration Guide: https://www.keycloak.org/docs/latest/server_admin/
- Okta — Okta organizations (developer docs): https://developer.okta.com/docs/concepts/okta-organizations/
- JumpCloud — platform and Open Cloud Directory product pages: https://jumpcloud.com/platform , https://jumpcloud.com/platform/cloud-directory
- Microsoft — Active Directory Domain Services overview (historical sample): https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview

> Sourcing limitation: the Okta product help center (`help.okta.com`) and the JumpCloud support KB (`support.jumpcloud.com`) could not be fetched from the research environment on 2026-09-06; two Okta developer concept-page URLs returned 404. Okta evidence is therefore limited to its organizations concept page, and JumpCloud evidence to official product/platform pages (Tier 2). Precise operational details (numeric limits, session durations, default policy values, pricing) are intentionally not stated in this document. Such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison matrix, and historical / market-sample breadth check are recorded in the paired Research Notes.
