# Research Notes — Single Sign-on / SSO

## Research Goal

Understand what a Single Sign-on application actually is as an Application Type: its core objects, defining workflows, what mature products commonly add, where its boundaries sit (vs IAM, vs MFA, vs password managers, vs access proxies), and what a reader who has never used one needs to know. Special duty this pass: discharge the joint-review flag left by the identity-access-management-iam pass (SSO suspected as an IAM capability) and the pending joint review with multi-factor-authentication-mfa (session/token-brokering seam).

## Initial Boundary

- Nearest neighbors: Identity & Access Management / IAM (identity lifecycle + central administration), Multi-factor Authentication / MFA (factor layer), Password Manager (credential storage/replay), ZTNA / Access Gateway (network-path access enforcement), CIAM (customer-facing identity), Web SSO protocols (SAML/OIDC — machinery, not the Type).
- Prior flags on record:
  - IAM pass: "standalone SSO/MFA lacks identity lifecycle and central administration as primary structure, so the leaves likely behave as Capabilities/Variants of IAM rather than independent Types — flagged for joint review."
  - MFA pass: keep-both ratified from the MFA side; "JOINT REVIEW still required with single-sign-on-sso when that leaf is processed (session/token-brokering seam expected clean: remove the factor layer → SSO, remove app brokering → MFA; Duo ships MFA and SSO as separately documented products; interlock = the MFA layer commonly protects the SSO portal itself)."

## Research Questions

1. What is the unit of record in an SSO product — the user, the application connection, the session?
2. What does "single sign-on" concretely consist of: what is signed in once, and how does that carry to other applications?
3. How are applications connected (protocols, catalogs, generic connectors)?
4. Where do identities and primary credentials live — must the SSO product own a directory?
5. What does the admin configure vs what does the end user see?
6. How do sessions work (duration, per-IdP vs per-app sessions, logout)?
7. What happens for apps that cannot federate (password replay, gateways, linked sign-in)?
8. Where is the seam vs IAM (identity lifecycle) and vs MFA (factor layer)?

## Representative Products

| Product | Why chosen | Evidence tier reached |
|---|---|---|
| Microsoft Entra ID (SSO for enterprise apps) | platform-native suite IdP; richest Tier-1 conceptual doc | A (official Learn doc) |
| Duo Single Sign-On (Cisco) | access-security vendor's standalone SSO product; separately documented from its MFA — decisive for the MFA joint review | A (official docs, deep) |
| Okta Single Sign-On (Workforce Identity) | neutral independent IdP, market flagship | B (official product page + FAQ; help center not reachable) |
| OneLogin | mid-market pure-play SSO | — unreachable (2 fetch failures; abandoned) |

## Sources

- Microsoft Learn — "What is single sign-on in Microsoft Entra ID?" — https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on (fetched 2026-09-10)
- Cisco Duo — "Duo Single Sign-On" docs — https://duo.com/docs/sso (fetched 2026-09-10)
- Okta — Single Sign-On product page — https://www.okta.com/products/single-sign-on/ (fetched 2026-09-10)
- OneLogin — https://www.onelogin.com/product/single-sign-on , https://www.onelogin.com/learn/what-is-sso (both failed/empty, 2026-09-10 — abandoned)

## Product Observations

### Microsoft Entra ID — SSO for enterprise applications (Layer A)

- Definition: "Single sign-on (SSO) lets users sign in once and reach many applications… With SSO, users sign in with one set of credentials. They can then open every assigned application without signing in again."
- Three-party structure named explicitly: the user, the app, and the identity provider. "Apps no longer manage separate usernames and passwords."
- Flow: user opens app → app redirects to the IdP → IdP verifies work credentials → IdP confirms identity to the app → app grants access. "This four-step process happens automatically."
- SSO methods per application: federation-based (SAML 2.0, OIDC), password-based SSO (IdP "securely stores the credentials and replays them to the app" — for apps without federation, esp. via Application Proxy), linked SSO ("adds app links in user portals, but it doesn't provide true single sign-on" — migration aid), disabled SSO.
- Access is per-application assignment: "every assigned application" — assignment precedes launch.
- End-user surface: the My Apps portal — "a centralized location for all assigned applications. Users can find and launch applications without remembering multiple credentials."
- Deployment planning axis: app hosting (cloud / on-premises / hybrid) shapes the SSO method.

### Duo Single Sign-On (Layer A — deepest operational evidence)

- Self-definition: "a cloud-hosted SAML 2.0 identity provider (IdP) and OIDC provider (OP) that adds two-factor authentication and access policy enforcement to popular cloud services… using SSO protocols."
- Delegation named as the mechanism: "SAML and OIDC delegate authentication from the application to an identity provider."
- Primary-authentication-source model: Duo SSO can verify users from its own Duo Directory OR external sources (on-prem Active Directory via an on-prem Authentication Proxy, or an external SAML IdP such as Entra ID, Google Workspace, Okta). I.e., the SSO product demonstrably operates **without owning the identity store**.
- Routing rules direct users to the correct authentication source (multiple co-existing sources; internal users vs third-party users).
- Per-application protection: "Protected cloud applications redirect your users to Duo Single Sign-On, authenticate your users… then prompt for two-factor authentication and perform access and device checks before permitting access." Connectors for named enterprise apps plus generic SAML/OIDC connectors ("connect to just about any app that supports the SAML 2.0 or OIDC standard").
- Session machinery: admin-configured SSO session duration (documented range 0–30 days; default 8h for the AD source); "Duo SSO session expiration does not affect the session established independent of Duo between the end-user's client and the application" — the IdP session and per-app sessions are distinct layers. Remembered-device sessions inherit the original authentication's method-strength values (AMR).
- Domain verification: permitted email domains verified via DNS TXT before users may log in — anti-phishing guard on the login surface.
- Admin surface: Applications → SSO Settings; authentication sources; per-application configuration; policies. End-user surface: the SSO login page (subdomain-branded), self-service device management portal.
- Duo ships SSO and MFA as separately documented products (separate /product pages; SSO docs describe MFA as an added layer on top of the SSO flow).

### Okta Single Sign-On (Layer B — product page + FAQ; help center unreachable)

- Positioning: "Single Sign-On gives employees, contractors, and business partners secure access to everything they need."
- End-user dashboard: "By logging in once to the Okta dashboard, users gain instant access to their entire tech stack"; customizable, brandable, organized into tabs/sections.
- Integration catalog: "8,000+ pre-built integrations to instantly connect your cloud and on-prem apps. No custom code or maintenance required."
- Identity-store posture: "Integrate with any and all Identity stores including AD, LDAP, HR systems and more… manage all your Identities from a single control plane" — directory integration as an input, not a requirement of the SSO function itself.
- Offboarding framing: deactivating the user in Okta revokes access to all integrated SSO applications ("single kill switch") — central session/access revocation as a consequence of the brokering position.
- Legacy apps: reached via a separate product (Access Gateway) — on-prem apps "without changing source code."
- MFA sold as a separate complementary product (Adaptive MFA).

## Cross-product Comparison

| Dimension | Entra ID | Duo SSO | Okta | Level |
|---|---|---|---|---|
| Central sign-in point verifying the user once | ✔ (IdP verifies work credentials) | ✔ (primary auth at Duo SSO) | ✔ (login once to dashboard) | **Core (A/B)** |
| Applications delegate authentication to it via standard protocols | ✔ SAML/OIDC | ✔ SAML 2.0 IdP + OIDC OP | ✔ (pre-built integrations) | **Core (A)** |
| Per-application connections configured by admins | ✔ (per-app SSO method settings) | ✔ (connectors + generic SAML/OIDC) | ✔ (integration catalog) | **Core (A)** |
| One authentication carries to multiple apps without re-auth | ✔ | ✔ (SSO session duration machinery) | ✔ | **Core (A)** |
| End-user app portal / dashboard | ✔ My Apps portal | ◐ (Duo Central access URL; portal less emphasized) | ✔ (End-User Dashboard) | Common (A/B) |
| Pre-built application catalog / integration network | ✔ (gallery implied by per-app templates) | ✔ (named connectors + generic) | ✔ (8,000+ claim) | Common (A/B) |
| External directory as primary auth source (no own directory needed) | ✔ (Entra IS the directory; but SSO function consumes it) | ✔ explicit (AD / external SAML IdP) | ✔ (AD/LDAP/HR integration) | Common (A/B) |
| Non-federated app support | ✔ password-based SSO (credential replay), linked SSO | — (not observed in fetched scope) | ✔ via Access Gateway (separate product) | Variant (A/B) |
| MFA attached at the SSO sign-in | ✔ (Entra MFA capability) | ✔ explicit ("adds two-factor authentication") | ✔ (Adaptive MFA complementary) | Common interlock (A/B) |
| Session policy (duration, remembered device) | not detailed in fetched doc | ✔ (0–30 days, default 8h; remembered devices) | not observed | Common (A — one product detailed) |
| Login-surface domain verification | not observed in fetched doc | ✔ (DNS TXT domain verification) | not observed | Product-specific (A) |
| Routing rules across multiple auth sources | not observed | ✔ | not observed | Product-specific (A) |
| On-prem app gateway | ✔ Application Proxy | — | ✔ Access Gateway (separate product) | Variant (A/B) |
| Identity lifecycle / provisioning as primary structure | ✖ (lives in the wider platform) | ✖ (directory sync separate) | ✖ (Lifecycle Mgmt separate product) | — confirms seam vs IAM |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The central authentication broker** — one sign-in point that verifies the user once, on behalf of many applications. Remove → per-app logins (password manager territory).
2. **Application delegation via standard federation** — applications redirect authentication to the broker and consume its assertion/token; the broker, not the app, verifies the credential. Remove → credential vault/replay tool.
3. **The application connection as the unit of record** — each protected application is an admin-configured connection (protocol endpoints, identity attributes, assignment) through which the broker serves that app; the connection registry is what makes "many applications" a managed set rather than an accident. Remove → a bare login page / single-app IdP.

Plus the brokering consequence: one authentication produces a session/token state that grants access to multiple connected applications without re-authentication. (This is the observable outcome of 1+2+3; stated as the defining behavior rather than a fourth object.)

### L1 — Common Mature Structure

- End-user application portal/dashboard (launch surface for assigned apps)
- Pre-built application catalog / integration network + generic SAML/OIDC connectors
- External directory/IdP as primary authentication source (SSO without owning identities)
- MFA attached at the brokered sign-in (the standard interlock)
- Session policy machinery (duration, remembered device) and central revocation (deactivate → all apps cut off)
- Authentication logging/reporting; branding/customization of the sign-in and portal surfaces
- Assignment/access control over which users may launch which apps

### L2 — Variant / Optional

- Password-based SSO (credential replay) and linked sign-in for non-federable apps
- On-premises application gateways/proxies (separate products in two of three samples)
- B2B/partner federation, external-identity scenarios
- Customer-facing (CIAM-flavored) SSO deployments
- Routing rules across multiple authentication sources; login-domain verification
- Protocol-era variants: Kerberos-era network SSO and open-source web SSO (CAS/Shibboleth-class) satisfy L0 without any portal, catalog, or commercial integration network — historical check passed

### L3 — Vendor-specific (Research Notes only)

- Duo: routing rules, AMR values, permitted-email-domain TXT verification, 0–30-day session range with 8h default, Authentication Proxy topology, Duo Central
- Entra: My Apps portal naming, Application Proxy, four SSO-method taxonomy (federation/password/linked/disabled)
- Okta: Okta Integration Network (8,000+), Access Gateway, End-User Dashboard branding, "75% fewer help-desk calls" marketing claims

## Vendor-specific Findings

- Okta's numeric marketing claims (8,000+ integrations, 75%/3X/50% figures) are vendor-reported estimates — not asserted in the final document.
- Duo's specific session defaults and domain-verification mechanics are product-specific operational detail.
- Entra's four-method SSO taxonomy is a vendor framing; other products express the same spread (federated vs replayed vs gatewayed) without the same labels.

## Boundary Findings

**vs IAM (discharges the IAM pass's joint-review flag): keep-both RATIFIED.** The IAM suspicion ("standalone SSO lacks identity lifecycle and central administration as primary structure") is confirmed as the seam, not a merger ground. Evidence: Duo SSO runs with an external AD or external SAML IdP as its primary authentication source and no directory of its own — the SSO function demonstrably survives without identity lifecycle; Okta ships SSO and Lifecycle Management as separately documented products; Entra documents SSO as a distinct concept inside the wider platform. The SSO Type's unit of record is the **application connection** and its job is **authentication brokering**; IAM's unit of record is the **identity/account** and its job is **lifecycle + central administration**. If maintainers ever prefer an IAM-capability framing, this leaf is the app-brokering function whose machinery IAM suites bundle.

**vs MFA (discharges the MFA pass's pending joint review): keep-both RATIFIED, seam clean as predicted.** Remove the factor layer → SSO (Duo SSO works with policy settings that skip MFA for bypass-status users; the brokering machinery is independent); remove app brokering → MFA (the MFA layer attaches to single sign-in flows with no connection registry). Duo ships MFA and SSO as separately documented products — vendor-confirmed separability. Interlock confirmed: the MFA layer commonly protects the SSO portal itself (Duo SSO "adds two-factor authentication… before permitting access to the application").

**vs Password Manager:** a password manager stores and replays credentials but the applications still verify them independently — no central broker, no delegation, no application-connection registry. Password-based SSO (credential replay at the broker) is the SSO product absorbing the non-federable app, not the two Types merging.

**vs ZTNA / Access Gateway / Application Proxy:** those broker access at the network/path layer for on-prem or private apps; they appear in SSO products as optional variant machinery (Entra Application Proxy, Okta Access Gateway — both separate products), not as the defining structure.

**vs CIAM:** same brokering mechanics, different population (customers vs workforce) and different surrounding machinery; treated here as a deployment variant.

## Uncertainties

- OneLogin unreachable — mid-market pure-play pole characterized only by market knowledge, no fetched evidence; no claims made from it.
- Okta help center not reachable — Okta evidence is product-page level (Tier 2); operational details (session defaults, protocol specifics) not asserted.
- Entra session-policy detail not in the fetched doc; not asserted.
- Historical open-source/Kerberos SSO characterized at canonical level only (no fetched docs this pass) — used only for the historical check, not for precise claims.

## Final Synthesis

A Single Sign-on application is the organization's authentication broker between its people and its applications. Its defining core is three jointly-held structures: a central sign-in point that verifies each user once; per-application connections through which applications delegate authentication to that point via standard federation protocols; and the brokering session that lets one authentication carry across all connected applications. Around this core, mature products add the end-user app portal, the pre-built integration catalog, external-directory authentication sources, MFA attachment at the brokered sign-in, session policy and central revocation, logging, and branding. Non-federable applications are handled by variant machinery (credential replay, gateways, linked sign-in). The Type is distinct from IAM (identity lifecycle vs authentication brokering) and from MFA (factor layer vs app brokering), with both seams vendor-confirmed by products that ship the functions separately.
