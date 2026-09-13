# Research Notes — Customer Identity / CIAM

## Research Goal

Understand "Customer Identity / CIAM" (Directory §15, Cybersecurity, Identity & Trust) as an Application Type: what object it maintains, who operates and who self-serves it, what its defining structure is, how enrollment / authentication / self-service / administration actually work in real products, and where its boundaries lie against neighboring identity Types (IAM, SSO, MFA, Identity Verification, Account Abuse Protection) and against consuming surfaces (Customer Portal, apps).

## Initial Boundary

Hypothesis before research:

- CIAM is the customer-facing counterpart to workforce IAM: an identity platform operated by an organization for **its own external end-customers** (consumers or business customers of the organization's digital products), where customers **enroll and self-manage their own accounts** and the organization's applications **delegate sign-in** to the platform.
- Nearest confusions recorded by already-processed sibling leaves:
  - IAM research: "customer-facing identity (CIAM) — the same machinery pointed at self-enrolling customers with consent and social login; a separate Type in this directory"; boundary test = flip the primary administration model from org-provisioned to self-enrolled.
  - Account Abuse Protection research: "CIAM **administers** customer identity (registration, profile, consent, sessions). Account abuse protection is the **risk/enforcement layer over account events**. Remove risk evaluation/decision → CIAM remains."
- Also adjacent: SSO and MFA (candidate capabilities rather than Types — flagged by the IAM pass), Identity Verification / KYC (proofing of real-world identity), Fraud Detection Platform (activity risk decisioning), Customer Portal (a consuming surface), Government Digital Identity (state-operated identity), Password Manager (user-held secrets).

## Research Questions

1. How do the products themselves distinguish customer identity from workforce identity?
2. How does a customer account enter the system? What enrollment paths, verification and confirmation states exist?
3. What authentication methods exist (local credentials, social/enterprise federation, one-time codes, MFA, passwordless) and how are they combined?
4. How does sign-in reach the organization's applications (hosted vs embedded login, SSO across the org's apps, token issuance)?
5. What can customers self-manage (profile, credentials, MFA enrollment, consent, deletion)?
6. What does the organization administer (app registrations, sign-in methods, flows, branding, keys, admin operations on accounts)?
7. Where do privacy/regulatory features appear (terms/consent capture, account deletion, data protection)?
8. What account-protection machinery is bundled (breached-password detection, bot/attack protection, risk-based authentication, WAF integration)?
9. What developer-facing surfaces exist (SDKs, management APIs, extensibility hooks, user migration tooling)?
10. What deployment/business-model poles exist (developer-first IDaaS, hyperscaler service, enterprise self-managed suite)?
11. Boundary tests vs IAM / SSO / MFA / Identity Verification / Account Abuse Protection / Customer Portal.
12. Historical check: does the definition overfit the modern cloud-IDaaS era?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

1. **Auth0 (Okta Customer Identity Cloud)** — developer-first identity-as-a-service; the reference "add authentication as a service" product; extremely deep docs.
2. **Microsoft Entra External ID** (external-tenant configuration; successor to Azure AD B2C) — workforce-IAM vendor extending to consumer/business-customer apps; hyperscaler platform pole.
3. **Amazon Cognito** — hyperscaler primitive pole (directory + auth server + AWS credential broker); infrastructure-primitive philosophy with unusually detailed operational docs.
4. **Ping Advanced Identity Software** (ex-ForgeRock; PingAM/PingIDM/PingDS/PingGateway) — enterprise self-managed suite pole (ForgeRock heritage, now under the same Thales-owned umbrella as Ping; backstage.forgerock.com redirects to docs.pingidentity.com). SaaS consumption documented as PingOne / Advanced Identity Cloud.
5. **Azure AD B2C** — treated as the documented legacy/historical pole (Microsoft's earlier CIAM product; end-of-sale for new customers May 1, 2025 per official docs).

## Sources

### Successfully fetched official sources (research date 2026-09-07)

- Auth0 — Docs: Get Started (https://auth0.com/docs/get-started), Auth0 Overview (https://auth0.com/docs/get-started/auth0-overview), User Accounts (https://auth0.com/docs/manage-users/user-accounts), llms.txt docs index (https://auth0.com/llms.txt) — Layer A
- Auth0 — Platform pages: User Management (https://auth0.com/platform/user-management.md), Customer Identity / B2C (https://auth0.com/b2c-customer-identity-management.md) — Tier-2 official product pages
- Microsoft Entra External ID — External identities overview (https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview), External tenant overview / CIAM (https://learn.microsoft.com/en-us/entra/external-id/customers/overview-customers-ciam) — Layer A
- Amazon Cognito — What is Amazon Cognito (https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html), Signing up and confirming user accounts (https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.md), Managing users in your user pool (https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html) — Layer A
- Ping Identity — Platform guide overview (https://docs.pingidentity.com/platform/8.1/platform-guide/about.html; reached via redirect from backstage.forgerock.com/docs/platform) — Layer A (module-level, not workflow-level)

### Source-access Limitations

- SAP Help Portal (SAP Customer Data Cloud, ex-Gigya — early-CIAM pole): page returns an empty JS shell → abandoned after 1 attempt; no claims about Gigya-era features are made in this pass.
- Wikipedia (Janrain, Gigya historical context): timeouts ×2 → abandoned; historical social-login-era claims are NOT asserted from memory.
- ForgeRock backstage platform "about" page: 404 at `/docs/platform/latest/about-platform.html`; reached the resolved Ping platform guide instead.
- Ping evidence is module-level (what the suite contains), not end-to-end workflow evidence; claims about Ping workflows are kept at reduced strength.
- No pricing/limit numbers were asserted beyond what fetched pages state (e.g., Cognito's documented 24-hour confirmation-code validity is kept product-specific).

## Product Observations

### Auth0 (Okta) — Layer A (docs) + Tier-2 platform pages

- Positioning (docs): "an identity platform to manage access to your applications"; "flexible, drop-in solution to add authentication and authorization services to your applications" so teams "avoid the cost, time, and risk that come with building your own solution."
- Building blocks (Get Started / Overview): **tenant**, **applications** (registered client types: native/mobile, SPA, regular web app, backend/API, AI agents), **APIs** (resource registrations), **connections** (identity sources: database, social, enterprise), **users**; plus dashboard, tenant settings, dashboard-access management, flows/architecture docs.
- Use cases enumerated in the official overview include: login with identifier (username/email/phone) + password or social accounts (Facebook, X); secure APIs with OAuth 2.0; **SSO across more than one app**; SAML federation; **passwordless** one-time codes via email/SMS; **breached-password detection** (notify users and/or block sign-in until password reset); **block suspicious IPs after consecutive failed logins**; federate an enterprise directory (workforce case); "You don't want (or you don't know how) to implement your own user management solution. Password resets, creating, provisioning, blocking, and deleting users, and the UI to manage all these"; enforce MFA for sensitive data; compliance posture (SOC 2, GDPR, PCI DSS, HIPAA); **monitor users** to "create funnels, measure user retention, and improve your sign-up flow"; RBAC and relationship-based (fine-grained) authorization.
- User accounts: hosted cloud user store grouped by tenant; profiles sourced from identity providers, the customer's own databases, or enterprise connections.
- User management (docs + platform page): centralized dashboard + management API to "create, search, and update user profiles, manage roles and permissions, and handle password resets"; **user_metadata** (user-editable) vs **app_metadata** (admin-only); user search API for helpdesk/security-audit use; **bulk user imports** and **trickle (lazy) migration** — users migrate from a legacy database as they log in, avoiding forced password resets; **account linking** — multiple identities (e.g., email account and Google account) linked to one user profile sharing one user_id and metadata; **normalized user profile** — consistent structure regardless of source IdP; dashboard access roles for administrative staff.
- Customer-identity framing (B2C page): reduce sign-up/login drop-off (passwordless, **Embedded Login**, social connections, **progressive profiling**, configurable forms); fraud defense (adaptive MFA, **risk-based authentication**, Actions, **bot and attack protection**); carry customer context across experiences (**consent**, progressive profiling, account linking); customization via APIs/SDKs or customized **Universal Login**; AI-assisted commerce (delegated authority, consent, fine-grained authorization, token vault).

### Microsoft Entra External ID — Layer A (learn.microsoft.com)

- Positioning: "Microsoft's customer identity and access management (CIAM) solution" for "organizations and businesses that want to make their apps available to consumers and business customers"; features named as "**self-service registration, personalized sign-in experiences, and customer account management**."
- **External tenant** (separate from the workforce tenant): contains a **directory** ("stores your customers' credentials and profile data"; a local account is created at sign-up), **application registrations** (OIDC or SAML; establishes trust; enables SSO), **user flows** ("the self-service sign-up, sign-in, and password reset experiences you want to enable"), **extensions** (custom authentication extensions adding claims/data from external systems at defined points in the flow), **sign-in methods** (username+password, one-time passcode, Google/Facebook/Apple/Entra-ID/custom-OIDC federation), and **encryption keys** (token-signing keys, secrets, certificates).
- Two account types: **customer accounts** (the app users) vs **admin accounts** (work accounts; "create new consumer accounts, reset passwords, block/unblock accounts, and set permissions or assign an account to a security group").
- Branding: external-tenant default is neutral (no Microsoft branding); org-level or per-app customization; per-language experiences.
- Sign-up customization: choose attributes collected at sign-up from built-in user attributes or custom attributes.
- **Self-service account management** (explicit): "Customers can register for your online services by themselves, manage their profile, delete their account, enroll in a multifactor authentication (MFA) method, or reset their password with no admin or help desk assistance."
- **Consent capture** (explicit): prompt users to accept terms of use and privacy policies during sign-up; checkbox attributes can carry links to terms/privacy.
- Conditional Access: if-then policies evaluated after first factor (e.g., high sign-in risk → require MFA or block); per-app MFA targeting (e.g., one app in the tenant requires phone verification, another doesn't).
- MFA second factors in external tenants: email one-time passcode, SMS.
- SSO: "SSO to apps registered in the external tenant is supported" (not to Microsoft 365).
- User activity/engagement analytics: Application user activity dashboards (usage & insights) — being retired in favor of Azure Monitor/Graph sign-in logs (migration note in docs).
- M2M authentication (client credentials) available as premium add-on.
- Licensing/billing based on **monthly active users (MAU)** (stated on the External ID overview page).
- **Azure AD B2C** (legacy): "a legacy solution for customer identity and access management" with "a separate consumer-based directory," custom user journeys via Identity Experience Framework; end-of-sale for new customers effective May 1, 2025; External ID is "the next-generation CIAM solution."
- Sibling scenario inside External ID: **B2B collaboration** (guests using home-org credentials in the workforce tenant) — a different scenario family from the consumer/business-customer external tenant.

### Amazon Cognito — Layer A (docs.aws.amazon.com)

- Positioning: "an identity platform for web and mobile apps. It's a **user directory**, an **authentication server**, and an **authorization service** for OAuth 2.0 access tokens and AWS credentials"; explicitly references CIAM ("For more information about customer identity and access management (CIAM), see What is CIAM?").
- Two components: **user pools** (user directory with "both self-service and administrator-driven user creation, management, and authentication"; independent OIDC IdP issuing JWTs; service provider to social IdPs [Amazon, Google, Apple, Facebook] and workforce IdPs [Okta, ADFS]; "SSO in your app"; managed login front end **or** "API support for your own UI") and **identity pools** (brokering temporary AWS credentials via STS for authenticated **or guest** users — an AWS-ecosystem authorization specialization).
- User pool features: MFA (TOTP, SMS, "your user's device"); "security monitoring & response" ("secure against malicious activity and insecure passwords"); **custom multi-step authentication flows**; **migrate users from another directory** (Lambda trigger at first sign-in); token claim customization (add/modify/suppress); custom user attributes; groups carrying IAM role claims; **AWS WAF web ACLs** attachable to the authentication front end.
- **Enrollment paths** (three, documented): self sign-up in the client app; CSV import; admin-created + invitation. "Users who sign themselves up must be confirmed before they can sign in."
- **Account states** (documented): Registered (Unconfirmed) → Confirmed → (Password Reset Required / Force Change Password) → Disabled; confirmation code/link valid 24 hours; confirming via code auto-verifies the email/phone attribute.
- Verification rules: password reset requires a **verified contact method** (email or phone); auto-confirmation without verification risks lockout (documented warning); updates to sign-in attributes can require re-verification before taking effect.
- Sign-in identity configs: username vs "username attributes" (email/phone as sign-in names) vs "alias attributes" (multiple alternative sign-in names).
- Admin operations: search users by standard attributes, reset passwords, disable accounts, view user event history, admin-confirm sign-ups ("leaves room for human review of new sign-up requests").
- Scale statement: "User pools can scale to millions of users."
- Federation constraint: several features (MFA, custom flows) are "unavailable to federated users" — the external IdP owns the factors for federated identities.
- Passwordless: OTP-based sign-in possible in SDK-built apps; "Managed login and the hosted UI always require passwords" (documented constraint at this product).

### Ping Advanced Identity Software (ex-ForgeRock) — Layer A (module-level)

- Platform composition (official docs): **PingAM** (access management: intelligent access/authentication, authorization, federation, user-managed access, strong authentication), **PingIDM** (identity management: identity synchronization, **self-service**, workflow, **social sign-on**, identity lifecycle and relationship), **PingDS** (directory server/proxy), **PingGateway** (edge security), plus a platform UI; containerized/Kubernetes self-managed deployment (ForgeOps reference tooling); "To consume Ping Advanced Identity Software as a service, use PingOne or Advanced Identity Cloud instead."
- Demonstrates the **enterprise self-managed pole**: the CIAM capability set can be assembled from an access manager + identity manager + directory + gateway rather than consumed as a hosted service; social sign-on and self-service exist as named modules inside the identity-management component.
- Market-consolidation evidence: backstage.forgerock.com/docs redirects to docs.pingidentity.com — ForgeRock and Ping now share one documentation platform (Thales umbrella).

### Azure AD B2C (legacy pole) — Layer A (via Entra docs)

- Documented as Microsoft's earlier CIAM product: separate consumer-based directory, customizable user journeys (Identity Experience Framework), end-of-sale May 1, 2025. Provides the historical-sample anchor: CIAM as practiced in the B2C era already had self-service registration, sign-in method choices, branded experiences — and the current L0 must also fit it.

## Cross-product Comparison

| Dimension | Auth0 | Entra External ID | Amazon Cognito | Ping Advanced Identity Software |
|---|---|---|---|---|
| Core framing | identity platform / "drop-in authentication & authorization" for apps | CIAM: "self-service registration, personalized sign-in, customer account management" in a dedicated external tenant | "user directory, authentication server, authorization service" for web/mobile apps | access management + identity management + directory + gateway suite |
| Identity population | tenant user store, multiple sources (db, social, enterprise) | customer accounts in external tenant directory | user pool directory, "millions of users" | PingDS directory, IDM-managed identities |
| Enrollment | self sign-up; bulk import; trickle migration from legacy DB | self-service sign-up user flows; local account created on sign-up | self sign-up / CSV import / admin-created; confirmation states documented | IDM self-service + lifecycle/synchronization modules |
| Verification | (docs surface: passwordless codes email/SMS; breached-password detection) | OTP + social; per-language flows | confirmation code/link; verified contact gates recovery; verification-before-update for sign-in attributes | module-level only |
| Authentication methods | identifier+password, social, passwordless (email/SMS codes), MFA, SAML/OIDC federation | username+password, OTP, Google/Facebook/Apple/Entra-ID/custom OIDC | password, TOTP/SMS/device MFA, social + workforce IdP federation, custom multi-step flows, passwordless in SDK apps | strong auth, federation, social sign-on modules |
| Sign-in surface | Universal Login (hosted, customizable) vs Embedded Login (custom UI via SDKs) | branded sign-up/sign-in experiences (neutral default; per-app/per-language) | managed login (hosted) vs your own UI via APIs | gateway/access-manager-hosted flows (module-level) |
| SSO | SSO across the customer's multiple apps (documented use case) | SSO to apps registered in the external tenant | "SSO in your app" via user pool federation | federation module (cross-app SSO) |
| MFA / step-up | adaptive MFA, risk-based authentication | Conditional Access (risk → MFA/block), email OTP / SMS second factors | MFA TOTP/SMS/device; unavailable for federated users | PingID mobile app, MFA push, transactional authorization |
| Account protection | breached-password detection; block suspicious IPs; bot & attack protection | platform security posture; Conditional Access risk signals | security monitoring & response; WAF on auth front end | strong-auth module (module-level) |
| Consent / privacy | consent in customer-context set (platform page) | terms-of-use + privacy-policy acceptance at sign-up; checkbox pattern; account deletion self-service | (not surfaced on fetched pages) | (not surfaced on fetched pages) |
| Self-service account mgmt | password resets, profile via user management | explicit: profile, delete account, MFA enrollment, password reset — "no admin or help desk assistance" | forgot-password; attribute verification; (profile via API) | IDM self-service module |
| Admin ops | dashboard + management API: create/search/update, reset, block/delete; dashboard roles | admin accounts: create consumer accounts, reset, block/unblock, permissions, groups | console/API: search, reset, disable, event history, admin-confirm | PingIDM lifecycle/workflow modules |
| Developer surface | SDK quickstarts per app type, management API, Actions extensibility, CLI, AI-agent support | user flows, custom authentication extensions, MSAL native auth, Graph APIs | SDK APIs, Lambda triggers, token customization, IAM role mapping | ForgeOps/Kubernetes reference, container images |
| Consumption model | multi-tenant IDaaS | platform service (MAU-based billing stated) | hyperscaler service (region-based) | self-managed containers; SaaS alternative (PingOne / Advanced Identity Cloud) |
| Authorization depth | RBAC + fine-grained (relationship-based) authorization | groups/permissions for admin-managed accounts | groups → IAM roles; ABAC via principal tags | authorization + UMA modules |

**Stable across the sample (Layer B / C):**

- The system is an **organization-operated identity platform for external end-customers**, distinct from the workforce directory (Entra makes the separation physical via a separate tenant; Auth0/Cognito via a separate tenant/user pool; Ping via IDM-managed populations).
- **Self-service enrollment** is a first-class flow (self sign-up + confirmation/verification), and **self-service account management** (profile, credentials, recovery) is explicit in every product where the fetched pages reach that depth.
- **Brokered sign-in**: the organization's applications register with the platform (app registrations/clients/connections) and delegate authentication; the platform issues tokens/sessions. Credentials are never handled by the apps.
- **Multiple credential sources**: local credentials and federated external identities (social providers; enterprise IdPs) coexist; federation is standard.
- **Verification of a contact channel** (email or phone) is the universal trust anchor for self-service (confirmation at sign-up; recovery prerequisite).
- **Hosted/customizable sign-in surface vs custom-built UI** exists as a choice in every product.
- **SSO across the organization's own customer apps** from one identity.
- **MFA** available as second factor / step-up in all sampled products.
- **Admin control plane** for the organization (console + management APIs): search accounts, reset, block, delete; plus configuration of apps, methods, flows, branding, keys.
- **Migration/import tooling** from legacy user stores (Auth0 trickle migration; Cognito CSV import + sign-in-time Lambda migration; PingIDM synchronization).
- **Account-protection machinery** bundled to some degree (breached passwords, suspicious-IP/attack protection, WAF attach, risk-based authentication).

**Where products diverge:** consent/privacy tooling depth (only surfaced in 2 of 4 at fetch depth); engagement/conversion analytics (2 of 4 surfaced); passwordless breadth (Cognito hosted UI password constraint vs Auth0 passwordless emphasis); authorization depth attached to the identity layer (Auth0 FGA / Cognito-IAM mapping vs thin authorization in others); deployment model (IDaaS vs self-managed suite vs hyperscaler primitive).

## L0 — Defining Invariant

Smallest structure without which the product stops being recognizable as Customer Identity / CIAM:

```text
External Customer Identity Population
└── Self-service identity lifecycle (the customer enrolls, confirms, recovers,
    and manages their own account without per-account administrator action)
└── Delegated authentication for the organization's customer-facing
    applications (apps register with the platform; sign-in is brokered;
    sessions/tokens are issued)
└── Organization-side administration of the identity system itself
    (register apps, choose sign-in methods/flows, operate on accounts)
```

- **External customer identity population** — persistent identity records for the organization's end-customers (consumers / business customers of its digital products), kept separate from the workforce identity population. Remove this → workforce IAM.
- **Self-service identity lifecycle** — enrollment (self sign-up with confirmation/verification) plus self-management of one's own credentials, profile, and recovery. Remove self-enrollment/self-management → the population becomes org-provisioned (workforce IAM drift). This is the administration-model flip test recorded in the IAM sibling pass.
- **Delegated authentication** — the organization's customer-facing applications delegate sign-in to the platform and admit customers based on issued sessions/tokens. Remove this → a bare profile database (not access management).
- **Organization-side administration** — the organization configures and operates the system (apps, sign-in methods, flows, branding, admin operations on accounts). Remove this → there is no product to deploy; note that administration here governs configuration and exceptional account operations, **not** routine per-customer provisioning.

L0 is deliberately minimal: no social login, no MFA, no consent tooling, no hosted customization, no SDKs, no analytics, no MAU pricing — all of these are absent in some qualifying realization (legacy B2C-era products, SDK-only integrations, local-credentials-only deployments).

## L1 — Common Mature Structure

Present in most mature modern products; not required for the Type to be recognizable:

- **Federated external identity** — sign-in via social providers (Google/Facebook/Apple-class) and enterprise/custom OIDC-SAML IdPs ("bring your own identity"); coexists with local credentials. 4/4 sampled.
- **Verified contact channel as trust anchor** — email/phone verification codes at enrollment; verification gates recovery (Cognito documents the recovery dependency explicitly). 4/4.
- **MFA / step-up authentication** — second factors (OTP, TOTP, SMS, device); adaptive/risk-gated variants in modern products. 4/4.
- **SSO across the organization's customer apps** — one identity, many apps. 4/4.
- **Hosted, brandable sign-in surface** with the alternative of building custom UI on APIs/SDKs (Universal Login vs Embedded Login; managed login vs own UI; branded user flows). 4/4.
- **Admin console + management APIs** over accounts (search, reset, block, delete, event history) and configuration (apps, methods, flows, branding, keys). 4/4.
- **Developer integration layer** — SDKs per app type, quickstarts, standards (OIDC/OAuth 2.0/SAML), extensibility hooks in the authentication flow. 4/4.
- **User migration/import machinery** — bulk import and lazy/trickle migration from legacy stores. 3/4 directly observed (Auth0, Cognito, PingIDM sync).
- **Progressive profiling / custom attributes** — collect and extend customer attributes over time. Observed directly at Entra and Auth0; attribute extensibility present in all. Moderate strength.
- **Consent & terms capture** — acceptance of terms/privacy at sign-up, consent records in customer context. Directly surfaced at Entra and Auth0. Moderate strength (privacy-era differentiator vs workforce IAM, but not definitional — the legacy pole fits without it).
- **Sign-in/abuse protection** — breached-password detection, suspicious-IP/attack blocking, WAF attachment, risk-based authentication. Observed at Auth0, Cognito, Entra (risk signals). Category-level common; specific mechanisms vary.
- **Engagement/conversion analytics** over sign-up/sign-in activity. Observed at Entra (user activity dashboards) and Auth0 (funnels/retention framing). Moderate strength.

## L2 — Variant / Optional Structure

Depends on segment, regulation, deployment, or era:

- **Passwordless-first postures** (magic codes, passkeys) vs password-centric; product-level constraints exist (Cognito's managed login requires passwords while SDK apps can go passwordless).
- **Authorization depth attached to the identity layer** — from thin group/role mapping to fine-grained relationship-based authorization (Auth0 FGA; Cognito groups → IAM roles/ABAC). Some deployments keep authorization in the apps.
- **B2B / business-customer variants** — organizations as customers, delegated administration, partner-portal identity (Entra splits B2B collaboration into a sibling scenario; Auth0 markets a B2B SaaS posture).
- **Non-personal authentication** — M2M (client credentials) and AI-agent client types emerging at the frontier (Entra M2M add-on; Auth0 AI-agent app type / token vault; Cognito identity pools brokering backend credentials).
- **Consent-management depth** — from a terms checkbox to preference/consent records; regulation-dependent (GDPR-era).
- **Deployment/consumption model** — multi-tenant IDaaS vs hyperscaler service vs self-managed containerized suite vs managed SaaS.
- **Identity-verification integration** (proofing of real-world identity at enrollment) — treated in this pass as an integration seam to a separate Type (Identity Verification / KYC); no product-specific claims made here.
- **Regional data residency and compliance packaging** (certification postures, regional hosting).
- **Identity-proofing-adjacent flows such as admin review of sign-ups** (Cognito admin-confirm pattern) — mechanism varies.

## L3 — Vendor-specific Structure (research notes only)

- **Auth0**: tenant model, Universal Login vs Embedded Login, Actions extensibility, trickle migration, Guardian-class MFA app, user_metadata/app_metadata split, normalized user profile, AI-agent application type, Agent Experience positioning, llms.txt docs strategy.
- **Microsoft Entra External ID**: external vs workforce tenant configurations, user flows, custom authentication extensions, Conditional Access if-then model, MSAL native authentication, per-app MFA targeting, MAU billing, User Insights retirement (Aug 31, 2026), Azure AD B2C end-of-sale (May 1, 2025) and Identity Experience Framework.
- **Amazon Cognito**: user pool vs identity pool split, JWT issuance and claim customization, Lambda-trigger extensibility (pre-sign-up, migrate-user, custom message), secret-hash mechanics, alias vs username-attribute configurations, documented state machine (Registered/Unconfirmed → Confirmed → Password Reset Required / Force Change Password → Disabled), 24-hour code validity, WAF attach, mailbox-simulator test addresses.
- **Ping / ForgeRock**: PingAM/PingIDM/PingDS/PingGateway module split, ForgeOps Kubernetes reference, Advanced Identity Cloud SaaS packaging, PingID mobile app, transactional authorization, UMA module.

## Boundary Findings

### vs Identity & Access Management / IAM (sibling leaf)

Sharpest boundary; already fixed by the IAM pass and confirmed here. Same machinery family, different population and administration model: workforce identities are organization-provisioned and admin-controlled; customer identities are self-enrolled and self-managed. Entra makes the split literal (workforce tenant vs external tenant; customer accounts vs admin accounts). Boundary test: flip the primary administration model from org-provisioned to self-enrolled and the product has drifted between the Types. Both leaves stand.

### vs Single Sign-on / SSO and Multi-factor Authentication / MFA (sibling leaves)

SSO (across the org's customer apps) and MFA are **capabilities inside** CIAM, present in all sampled products, but neither defines the Type: remove SSO → a CIAM serving one app remains; remove MFA → CIAM remains (legacy pole). Consistent with the IAM pass's flag that SSO/MFA look like capabilities rather than independent Types.

### vs Identity Verification / KYC-KYB

CIAM authenticates **returning** customers against stored credentials/federated identities; proofing of real-world identity (documents, liveness, registries) is a separate Type. CIAM deployments can integrate proofing at enrollment, but remove the stored-credential authentication machinery and only proofing remains (not CIAM). No product-specific claims made in this pass.

### vs Account Abuse Protection / Fraud Prevention Platform

Confirmed boundary from that leaf's own pass: CIAM **administers** customer identity; abuse protection is the **risk/enforcement layer over account events** (evaluate → decide → enforce on suspicious sign-ins/sign-ups). The CIAM products studied increasingly bundle protection primitives (breached-password detection, bot protection, WAF attach, risk-based auth) — a real overlap zone, but remove the identity administration (enrollment, profile, consent, sessions) and what remains is risk tooling, not CIAM.

### vs Customer Portal / Self-service Support Portal

Portals are **consuming surfaces** standing on CIAM. The portal's sign-in is delegated to the identity platform; the portal itself holds content/orders/support cases. Remove the identity machinery → the portal remains a content/service surface. Remove the portal → CIAM remains.

### vs Customer Relationship Management / CRM (and CDP)

Both hold person-level records about customers, but the spine differs: CRM records exist for commercial relationship management (pipeline, activity, value); CIAM records exist to authenticate and admit (credentials, verified channels, sessions, consent for access). A CIAM record can carry profile attributes and consent, but it is not a deal/account structure.

### vs Government Digital Identity

A state-operated digital identity scheme is structurally similar (self-enrollment, authentication for services) but the operator is a sovereign authority and the audience is citizens; kept as an adjacent Type in this directory rather than collapsed into CIAM.

### vs Password Manager

A password manager holds the **user's own** secrets for third-party services; CIAM holds the **organization's** records and verification machinery for its customers. No overlap in the locus of control.

### "Remove what to become another Type" summary

- Remove self-enrollment/self-management (population becomes org-provisioned) → workforce IAM.
- Remove delegated authentication + tokens → a profile database / CRM-like contact store.
- Remove the identity population administration entirely and keep only risk decisions → Account Abuse Protection / fraud tooling.
- Remove credentials/sessions and keep only real-world proofing → Identity Verification.
- Remove the platform and keep the consuming surface → Customer Portal.

## Historical / Market-Sample Check

- Legacy pole fits: Azure AD B2C (documented, end-of-sale 2025) — separate consumer directory, self-service registration, sign-in methods, branded journeys — satisfies the L0 without any modern addition (no passkeys, no AI-agent clients, no FGA).
- Pre-IDaaS era: organizations historically built customer account systems in-house (registration + sign-in + profile on a website). The L0 deliberately matches that shape (self-enrollment + delegated/self-hosted authentication + ownable administration) so the Type is not defined by the cloud-IDaaS implementation. The claim that early social-login platforms (mid-2000s) formed the first CIAM product wave could **not** be evidenced in this pass (SAP/Wikipedia sources unreachable) and is recorded as market context only, not asserted in the final document.
- Therefore L0 avoids: social login (a common but not invariant mechanism), MAU pricing, hosted-page customization, SDK-first integration, and consent tooling.

## Taxonomy Notes

- The directory leaf "Customer Identity / CIAM" stands as an independent Type; the IAM pass already resolved the family relationship (same machinery, different population/administration model). No merge recommended.
- Consistent with the IAM pass, the sibling leaves SSO and MFA look like capabilities; if a joint review is ever held, the CIAM pass would support treating them as embedded capabilities rather than fully independent Types. (Already flagged; no new escalation needed.)
- Product naming drift observed: ForgeRock documentation now resolves under Ping Identity (Thales consolidation) — matters for representative-product attribution, not for the Type definition.

## Uncertainties

- **Consent/privacy tooling depth**: only 2 of 4 sampled products surfaced consent/terms features at reachable doc depth; asserted at moderate strength ("commonly", not "universally"). GDPR-era marketing materials (not fetched) would likely strengthen this.
- **Engagement analytics**: same situation (2 of 4 surfaced); kept at moderate strength.
- **Identity-verification integration prevalence**: not evidenced in fetched pages; treated as a boundary/integration note only.
- **Ping workflow-level behavior**: evidence is module-level; no workflow claims made.
- **Pricing/limits**: only statements made on fetched pages (e.g., MAU billing statement; Cognito's 24-hour code validity) are carried; all other numbers deliberately absent.
- **Early-CIAM history** (Janrain/Gigya era): sources unreachable; not asserted.

## Final Synthesis

Customer Identity / CIAM is the Application Type of **organization-operated identity platforms for external end-customers**. Its defining structure is small: a persistent population of customer identities kept separate from the workforce; a self-service identity lifecycle in which customers enroll, confirm, recover, and manage their own accounts; delegated authentication through which the organization's customer-facing applications admit customers on issued sessions/tokens; and an organization-side control plane that configures the system and operates on accounts — without routinely provisioning each customer.

Around that core, mature products add a stable layer: federated social/enterprise identity, verified contact channels anchoring recovery, MFA and step-up, SSO across the organization's apps, a brandable hosted sign-in surface with a custom-UI alternative, admin consoles with management APIs, developer SDKs and extensibility hooks, user migration machinery, consent/terms capture, sign-in protection, and engagement analytics. Deployment spans developer-first IDaaS, hyperscaler services, and self-managed enterprise suites.

The Type's identity is the **administration-model flip**: the workforce IAM family pointed at a self-enrolling population. Everything else — federation, MFA, consent, analytics, protection — is where the market currently concentrates, not what the Type is.
