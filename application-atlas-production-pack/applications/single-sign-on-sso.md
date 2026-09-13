# Single Sign-on / SSO

## Overview

A **Single Sign-on (SSO) application** is an organization's authentication broker between its people and its applications: users sign in once at a central point, and that one authentication carries them into every connected application without signing in again.

The problem it solves is credential sprawl. Without a broker, every application holds its own usernames and passwords, users accumulate credentials, help desks absorb the resets, and the organization has no single point at which sign-in is verified, protected, or revoked.

Its defining core is small:

```text
Central authentication broker (one sign-in point, verifies the user once)
└── Application connections (each app delegates authentication to the broker
    via standard federation protocols)
    └── Brokering session (one authentication grants access to all
        connected applications without re-authentication)
```

Everything else commonly associated with modern SSO — the app-launch dashboard, the pre-built integration catalog, directory sync, MFA at the sign-in page, session policies — is widespread market machinery, not the definition. Older and open-source web SSO systems, and even Kerberos-era network sign-in, satisfy the same core without any of it.

When the product's center shifts to issuing and administering the identities themselves, it has drifted toward Identity & Access Management; when it centers on verifying a second factor at sign-in, it has drifted toward Multi-factor Authentication. The SSO broker attaches to either without becoming them.

## Users & Context

**Primary users:**

- **End users (workforce, and often contractors and partners)** — sign in once and launch their assigned applications from the broker's portal or by opening the applications directly. They experience SSO daily; they rarely configure anything.
- **IT / identity administrators** — create and maintain the per-application connections, decide who may access which application, set session policy, and integrate the organization's directory as the source of users and passwords.

**Secondary users:**

- **Application owners / developers** — register their applications with the broker, configure protocol endpoints and identity attributes, and consume the broker's assertions or tokens.
- **Help-desk staff** — handle sign-in exceptions: lockouts, session problems, access requests.

Typical context: an organization connecting its workforce to a portfolio of SaaS applications, internal web applications, and legacy systems through one identity front door — replacing per-application credentials with centrally verified, centrally revocable access.

## Core Model

### The Defining Core

Three structures, jointly. Remove any one and the product stops being an SSO application.

**1. The central authentication broker.** One sign-in point verifies the user once, on behalf of many applications. The broker — not each application — checks the credential. *Without this, every application verifies credentials itself, and the product is a password system or a credential store.*

**2. Application delegation via standard federation.** Applications do not send credentials to the broker; they redirect the user to it and consume its signed assertion or token. The broker authenticates, then tells the application who the user is. Standard federation protocols (SAML, OpenID Connect) are the common carriers of this delegation. *Without delegation, the product is a password vault that replays credentials — the applications still authenticate independently.*

**3. The application connection as the unit of record.** Each protected application exists in the system as an admin-configured connection: protocol endpoints, the identity attributes the broker passes, which users are assigned, and how sign-in behaves for that app. The connection registry is what turns "many applications" into a managed portfolio rather than an accident. *Without it, the product is a bare login page serving a single application.*

The observable outcome of the three together: **one authentication produces a session that grants access to multiple connected applications** — the user signs in at the broker and then opens application after application without re-entering credentials.

### Standard Capabilities of Mature Products

These appear across the market and make the broker practical, but they do not define it:

- **End-user application portal** — a dashboard listing the user's assigned applications; clicking one launches it through the broker. Commonly brandable and organized by the organization.
- **Application catalog and generic connectors** — pre-built connection templates for popular applications, plus generic SAML/OIDC connectors for anything standards-compliant.
- **External authentication sources** — the broker can verify users against an existing directory (on-premises or cloud) or even another identity provider, rather than requiring its own user store. The SSO function demonstrably works without owning identities.
- **MFA at the brokered sign-in** — the second-factor layer commonly attaches at the broker's sign-in, protecting all connected applications at once.
- **Session policy and central revocation** — how long the brokered session lasts, remembered-device behavior, and the defining administrative consequence: deactivating a user at the broker cuts off every connected application simultaneously.
- **Assignment and access control** — which users or groups may launch which applications.
- **Authentication logging and reporting** — who signed in, to what, when, and how.
- **Branding** — organization-branded sign-in pages and portals.

### One Structure, Many Implementations

The core is conceptual; products realize each piece differently:

```text
Concept:   Central authentication broker
Implementations:  cloud-hosted IdP, on-premises identity service,
                  open-source web SSO server, network-authentication service

Concept:   Delegation protocol
Implementations:  SAML 2.0 assertions, OpenID Connect / OAuth 2.0 tokens,
                  Kerberos tickets (older and platform-native forms)

Concept:   Where identities live
Implementations:  the broker's own directory, a synced external directory
                  (Active Directory, LDAP, HR source), or another
                  identity provider delegated to in turn
```

A reader who has only seen a cloud SaaS SSO dashboard should still recognize an open-source campus SSO or a Kerberos-based network sign-in from the defining core.

## How It Works

### Connect an application

```text
Admin creates an application connection
→ choose the federation protocol (SAML or OIDC)
→ exchange configuration (endpoints, certificates, identity attributes)
→ assign users or groups to the application
→ application is live behind the broker
```

Mature products shortcut this with catalog templates: pick the application from a catalog, fill in a few values, done. Generic connectors cover everything else that speaks the standard protocols.

### Sign in once, reach many applications

```text
User opens an application (or the portal)
→ application redirects the user to the broker's sign-in page
→ broker verifies the user's primary credential
  (against its own directory or a connected external directory)
→ commonly: second-factor verification at the same sign-in
→ broker issues the assertion/token and returns the user to the application
→ application grants access
→ user opens the next application
→ broker already holds a valid session → no re-authentication
```

The broker's session and each application's own session are distinct layers: the broker's session expiring does not necessarily end an application's session, and logging out of one application does not always end the brokered session. Products differ in how they handle single-logout; the brokered session is the layer that makes "sign in once" true.

### Revoke access

```text
Administrator deactivates the user at the broker
→ the brokered session ends
→ access to every connected application is cut off
→ no per-application cleanup needed
```

This "one switch" property is a direct consequence of the brokering position and one of the main reasons organizations adopt the Type.

### Handle applications that cannot federate

Not every application speaks a federation protocol. Mature products offer variant paths:

- **Credential replay** — the broker securely stores the app's username/password and fills it in at sign-in; the app still authenticates independently, so this is a convenience bridge, not true federation.
- **Access gateways / proxies** — an intermediary sits in front of on-premises or legacy applications and enforces brokered sign-in without changing the application's code.
- **Linked sign-in** — the portal simply links to the application's own login; a migration aid, not real SSO.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### End-user application portal

The user's primary entry surface.

- lists assigned applications, commonly searchable and organized
- primary actions: launch an application, manage profile/devices, report problems

### Broker sign-in page

The central authentication surface.

- credential entry against the configured authentication source, second-factor prompt when attached, organization branding
- primary actions: sign in, recover/reset credentials where enabled

### Admin console — application connections

The administrator's center of gravity.

- the connection registry: each application with its protocol settings, attribute mappings, and assigned users
- primary actions: add/configure an application connection, assign or remove access, test the sign-in flow

### Admin console — authentication sources and policy

- connect external directories or upstream identity providers; set session duration, remembered-device behavior, sign-in policies
- primary actions: add an authentication source, set session policy, review authentication logs

### Self-service portal

Where end users manage their own side of the brokered relationship: enrolled devices and authenticators, sometimes password changes.

## Important Rules / Behaviors

### Delegation, not credential sharing

Applications never see the user's primary credential. The broker verifies it and issues its own assertion/token. This is the structural difference between SSO and password reuse or vaulting.

### Two session layers

The brokered session (one sign-in → many apps) and each application's own session are independent. Ending one application's session does not end the brokered session; the brokered session expiring does not necessarily log the user out of applications they already opened. Single-logout behavior varies by product and application support.

### The broker is the access chokepoint

Because every connected application's sign-in flows through the broker, policy applied at the broker — stronger authentication, blocked users, revoked access — applies to the whole portfolio at once. This concentration is the product's main security value and also its main risk: the broker is a high-value target, which is why domain verification of the sign-in surface and phishing-resistant authentication are common concerns at this layer.

### Assignment gates launching

A user can only reach applications they are assigned to; the portal and the delegation flow both enforce this. Access changes take effect at the broker without touching the applications.

## Variants

- **Workforce SaaS SSO** — the dominant modern form: cloud broker, app portal, integration catalog, directory integration (the researched sample's center of gravity)
- **Platform-native SSO** — the brokering function embedded in a platform's wider identity service; the SSO concepts remain separately documented inside the platform
- **Security-first standalone SSO** — an access-security vendor's SSO product, typically with MFA and device checks attached tightly at the sign-in
- **Open-source / institutional web SSO** — self-hosted brokers serving campuses or public institutions; satisfies the core without commercial catalogs or portals
- **Network / Kerberos-era SSO** — sign-in once to the network, reach many services; the historical ancestor of the web-federation form
- **Customer-facing SSO** — the same brokering mechanics pointed at a business's end customers rather than its workforce
- **Legacy-app bridging** — credential replay and gateway/proxy machinery extending the broker to applications that cannot federate

## Related Application Types

| Application Type | Distinction |
|---|---|
| Identity & Access Management / IAM | IAM's center is the identity itself — accounts, lifecycle, groups, central administration. SSO's center is the application connection and authentication brokering; it works with identities held elsewhere. Mature IAM suites bundle SSO as a capability, and SSO products consume directories rather than governing identities — the functions ship separately in the market |
| Multi-factor Authentication / MFA | MFA holds and verifies second factors at sign-in; it has no application-connection registry and attaches to any sign-in flow, including the SSO broker's own. SSO without the factor layer is still SSO; the two ship as separately documented products |
| Password Manager | stores and replays credentials, but applications still authenticate independently — no central broker, no delegation, no connection registry. Credential replay inside SSO products is a bridge for non-federable apps, not the Type's core |
| Customer Identity / CIAM | same brokering mechanics, different population (customers) and different surrounding machinery (registration, consent, self-service) |
| Zero Trust Network Access / ZTNA | brokers access at the network/path layer for private applications; appears inside SSO products as optional gateway machinery, not the defining structure |
| Privileged Access Management / PAM | brokers and vaults access to administrative targets (servers, accounts) with session recording and just-in-time elevation — a different population and object model |

## Representative Products

- Microsoft Entra ID (SSO for enterprise applications)
- Okta Single Sign-On (Workforce Identity)
- Duo Single Sign-On (Cisco)
- OneLogin

The defining core was checked against open-source/institutional web SSO and Kerberos-era network sign-in to avoid over-fitting to the modern cloud-SaaS dashboard pattern.

## Sources

Research date: **2026-09-10**

- Microsoft Learn — "What is single sign-on in Microsoft Entra ID?" — https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on
- Cisco Duo — "Duo Single Sign-On" documentation — https://duo.com/docs/sso
- Okta — Single Sign-On product page — https://www.okta.com/products/single-sign-on/
- OneLogin — product/learn pages (unreachable at research time; product listed as a market anchor without fetched evidence)

> Sourcing limitation: OneLogin's site returned empty responses and Okta's help center was not reachable from the research environment on 2026-09-10. OneLogin is listed as a representative product without claims drawn from it; Okta's evidence is product-page level, so no operational specifics (session defaults, protocol configuration detail) are asserted from it. Precise operational details observed for other products (session ranges, verification mechanics) are recorded in the Research Notes rather than stated here as general rules.

Detailed evidence, product-by-product observations, cross-product comparison, and the boundary discharges with IAM and MFA are recorded in the paired Research Notes.
