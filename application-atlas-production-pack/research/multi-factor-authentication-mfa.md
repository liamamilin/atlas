# Research Notes — Multi-factor Authentication / MFA

Research date: **2026-09-08**
Slug: `multi-factor-authentication-mfa` (DIRECTORY §15 Cybersecurity, Identity & Trust)

## Research Goal

Determine what a "Multi-factor Authentication / MFA" application is as an Application Type in its own right: its defining core, standard mature structure, variants, and boundaries — especially against the neighboring §15 leaves (IAM, SSO, CIAM, Identity Verification, Password Manager, PAM) which were all processed in earlier passes and bundle MFA-like capability.

## Initial Boundary

Working hypothesis before research:

- Core purpose: a system that requires users to verify identity with an additional factor at authentication time, manages enrollment of those factors, and controls when/for whom verification is required.
- Nearest types: SSO (authentication brokering), IAM/IdP (identity lifecycle), CIAM (customer identity), Password Manager (personal TOTP capability), Identity Verification (onboarding proofing), Fraud Prevention (risk decisions), PAM (privileged sessions).
- Open question carried in from a prior pass: the IAM pass flagged (STATUS Boundary Issues) that SSO/MFA "likely behave as Capabilities/Variants of IAM rather than independent Types" because every sampled modern IAM bundles factor management. This pass must answer that flag from the MFA side.

## Research Questions

1. What is the unit of record — what does the system hold for each user? (enrolled factor / authenticator / method?)
2. What happens at authentication time? How does the challenge relate to the primary credential and to the application being accessed?
3. How does enrollment work (self-service, admin-issued, bulk, directory-sync)?
4. What factor kinds exist and how do they map to knowledge / possession / inherence?
5. What policy machinery decides when MFA is required, for whom, with which methods?
6. How do bypass, lockout, recovery, and replacement work?
7. What integration surfaces exist (IdP, VPN, RADIUS/LDAP, OS logon, web apps, APIs)?
8. What packaging shapes does the market realize (standalone vs bundled vs API vs on-prem)?
9. Do standalone MFA products exist as a real population, or is MFA only ever a capability inside identity platforms? (the IAM-pass question)
10. Where are the boundaries with SSO, IAM, CIAM, Identity Verification, Password Manager?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Philosophy | Customer tier | Evidence |
|---|---|---|---|---|
| Cisco Duo | dedicated standalone MFA overlay service | MFA as an independent layer attached to any app/IdP, with its own trust engine and admin plane | SMB free → enterprise → government editions | A (Tier-1, deep) |
| Microsoft Entra ID MFA | MFA bundled inside a hyperscale identity platform | MFA as a capability of the IdP control plane, policy via Conditional Access | enterprise / education / government cloud | A (Tier-1, deep) |
| Okta | identity platform with distinct MFA terminology | MFA as assurance machinery: factor / authenticator / enrollment, two policy families | enterprise workforce + CIAM | A (Tier-1, concept-level) |
| Twilio Verify | API-first verification service | MFA as a developer primitive: start-verification / check-verification API, no directory | developer / CIAM builders | A (Tier-1, API docs) |
| RSA SecurID | on-premises heritage / hardware-token pole | authentication management for high-assurance orgs; hardware authenticators; hybrid failover | financial services / government | B (Tier-2 positioning only — see Sources limitation) |

## Sources

- Cisco Duo: https://duo.com/docs (docs index), https://duo.com/docs/administration, https://duo.com/docs/policy, https://duo.com/docs/enrolling-users, https://duo.com/docs/microsoft-mfa, https://guide.duo.com (end-user guide) — fetched 2026-09-08.
- Microsoft: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks, …/concept-authentication-methods (authentication overview), …/how-to-authentication-external-method-manage — fetched 2026-09-08. (First URL attempt `concept-mfa-how-it-works` 404'd; correct path found on retry.)
- Okta: https://developer.okta.com/docs/concepts/mfa/ — fetched 2026-09-08. (help.okta.com not attempted — known JS-SPA; developer docs serve the concept layer.)
- Twilio Verify: https://www.twilio.com/docs/verify — fetched 2026-09-08.
- RSA SecurID: https://www.rsa.com/products/securid/ — fetched 2026-09-08 (product page only).

**Source-access limitation:** RSA's operational documentation lives in a community portal (community.rsa.com) that was not fetched; RSA-specific observations are held at positioning strength (product page claims), and no RSA-specific operational rule is asserted anywhere. Okta help-center operational detail (help.okta.com) was not fetched; Okta evidence is concept-level (official developer concept docs + API reference tables).

## Product Observations

### Cisco Duo (evidence layer A — directly observed)

**Positioning:** dedicated MFA service ("Multi-Factor Authentication (MFA)" is a named product line alongside SSO and Duo IAM). End-user guide: "Verifying your identity using a second factor … prevents anyone but you from logging in, even if they know your password"; flow = enter username/password as usual → verify identity with registered device → logged in. "This second factor of authentication is separate and independent from your username and password — Duo never sees your password."

**Unit of record:** user (username, shared across applications) + attached authentication devices/methods. Official definition: "A 'fully-enrolled' Duo user is an end user who … exists in Duo as a user with an associated authentication method. A partially-enrolled user is one who exists in Duo with a username but has no authentication methods registered." Devices are first-class objects: phones, tablets, hardware tokens, WebAuthn security keys, YubiKeys — managed by admins, attachable to users.

**Enrollment (multiple mechanisms):** inline self-enrollment at first protected login (creates the Duo user); bulk enroll via emailed links (link expiry; pending-enrollments table; resend); directory sync from AD / OpenLDAP / Entra ID / Google / Okta (SCIM) with automatic enrollment emails; CSV import; manual admin enrollment with enrollment emails/codes; Duo Mobile activation via QR link. Enrollment policy is a separate policy family from authentication policy ("You can now define distinct user enrollment and account management policies … such as selecting whether users must set a Duo password, or which authentication methods they can register").

**Challenge at authentication:** after primary credentials are verified by the application/directory/IdP (Duo can also be the IdP via Duo SSO/Duo Directory, but explicitly supports "2FA-only application authentication" where "the application is responsible for primary authentication against whichever identity stores it supports … For these applications Duo solely provides two-factor authentication"), the Duo Prompt appears; the user picks a method: Duo Push (approve request in mobile app), Verified Duo Push (verification code or Bluetooth proximity), platform authenticator (Touch ID/Face ID/Windows Hello/Android biometrics), roaming authenticator (FIDO2 security keys/passkeys), Duo Mobile passcode, SMS passcode, phone callback, hardware token passcode, YubiKey passcode, Duo Desktop approval. Multiple devices per user; fallback method choice is user-visible ("Back to login options").

**Status & policy:** user status: active / bypass / locked-out / disabled; "users with bypass status … bypass Duo authentication entirely." New-user policy (require enrollment / allow access without MFA / deny access). Authentication policy (enforce MFA / bypass 2FA / deny). Policy machinery: built-in Global Policy + custom policies assigned to groups/applications/application-groups with a documented precedence chain (application-group > application > user-group > global) and a Policy Calculator showing effective per-user-per-app policy. Policy settings include: authentication-method allowlist (incl. require user verification on security keys, verified push), remembered devices (time-windowed "Is this your device?" skip, separate settings for web vs Windows logon), user location (per-country require/skip/deny, considering both access-device and auth-device IP), authorized networks, trusted endpoints (managed-device verification), device health (OS, browsers, plugins, screen lock, full-disk encryption, biometrics, tampered devices), risk-based factor selection (step-up/block by risk). New-user and enrollment-policy restrictions apply to the enrollment portal too (a country block can block enrollment from that country).

**Admin & reporting:** Admin Panel: dashboard (total users, bypass/locked-out counts, inactive users, deployment progress, average 2FA devices per user, top authentication methods, authentication successes/failures graph), Authentication Log per attempt (success/failure + reason, username, application, access-device IP/OS/browser, second-factor device type/phone/location), Reports (Authentication Summary, Administrator Actions log), telephony credits (SMS/voice calls consume credits; rate card). Admin logins themselves are second-factor protected with a separately configurable admin authentication-method set.

**Integration surfaces:** huge application catalog (2FA apps, SSO apps), VPNs via RADIUS, LDAP, web SDK (Duo Web), Auth API, OS logon (Windows/RDP, macOS, Unix/SSH), Authentication Proxy component for on-prem services. Duo also ships as the Entra ID "External MFA" method.

**Recovery:** bypass codes (admins issue), self-service portal for device management, help-desk role with permission-gated enrollment actions, temporary Duo passwords, forgotten-password flows, admin lockout rules.

### Microsoft Entra ID MFA (evidence layer A — directly observed)

**Positioning:** "Multifactor authentication is a process in which users are prompted during the sign-in process for an additional form of identification, such as a code on their cellphone or a fingerprint scan." "Microsoft Entra multifactor authentication works by requiring two or more of the following authentication methods: Something you know … Something you have … Something you are." "The verification prompts are part of the Microsoft Entra sign-in."

**Unit of record:** registered authentication methods on the user, managed via the Authentication methods policy. Official method-role matrix distinguishes primary authentication vs secondary (MFA) vs SSPR/recovery: password is primary-only ("No" as secondary); Microsoft Authenticator push, FIDO2/passkeys, TAP, OATH tokens, SMS, voice, Authenticator Lite, CBA, external MFA can serve as MFA factors; Windows Hello can serve as MFA step-up in a defined configuration. Method catalog includes: Microsoft Authenticator, Authenticator Lite (in Outlook), Windows Hello for Business, Passkey (FIDO2), Passkey in Authenticator, QR code, certificate-based authentication, External MFA, Temporary Access Pass (TAP), OATH hardware (preview)/software tokens, SMS, voice call. "Phishing-resistant authentication methods" is an official class (Windows Hello, passkeys/FIDO2 security keys, CBA).

**Registration:** users self-register methods at Security info (mysignins.microsoft.com); combined registration for MFA + SSPR ("When users register themselves for Microsoft Entra multifactor authentication, they can also register for self-service password reset in one step"); registration campaigns nudge users; admins can register or delete methods on a user's behalf ("Admins can register a user for an external MFA… They can delete the registration to help users in recovery scenarios"); users not registered for external MFA are excluded from registration reports.

**Challenge at authentication:** MFA prompt occurs within the Entra sign-in flow; method picker lists the user's registered methods; "system-preferred multifactor authentication" automatically prompts the most secure method; number matching for push; "Other options" reveals alternates (e.g., a TAP or passkey may shadow the external method). MFA requirement is decided by policy: security defaults (all users), per-user MFA (legacy), or Conditional Access policies ("define events or applications that require MFA … allow regular sign-in when the user is on the corporate network or a registered device but prompt for additional verification factors when the user is remote"). Sign-in frequency / MFA freshness policies control re-prompting.

**External MFA (the interlock):** Microsoft's own framework for attaching a third-party MFA product: "External multifactor authentication (MFA) … lets users choose an external provider to meet MFA requirements when they sign in … Microsoft Entra ID continues to handle full policy evaluation and access decisions as the identity control plane." Config requires provider metadata (App ID, Client ID, OIDC discovery URL); the external method is managed inside the Authentication methods policy (include/exclude users); users register the external method through the provider ("Complete the second factor challenge with the external provider"); admin deletion of the registration is a recovery trigger. Duo's own page documents the history (custom controls 2017 → External Authentication Methods preview 2024 → "External MFA" GA 2026) and the semantics (Duo-verified factor returns an MFA claim that satisfies Conditional Access MFA grants; bypassed Duo authentication does not satisfy the MFA requirement).

**Recovery-adjacent structures:** TAP (time-limited sign-in credential for onboarding/recovery); MFA also secures SSPR; "high-assurance account recovery" via government-ID verification + biometric matching is explicitly classified as identity-verification capability, "not a traditional authentication method. It can't be used to satisfy authentication requirements like sign-in, MFA, or SSPR."

### Okta (evidence layer A — concept-level)

**Terminology (official concept docs):** MFA = "an assurance method that requires users to provide two or more verification factors"; factor = category (knowledge / possession / biometric); authenticator = "a method or device that a user possesses and controls"; authenticator method = the protocol (totp, push, sms, webauthn, …); authenticator enrollment = "the specific instance of an authenticator that a user has enrolled and that's linked to them and their account." One authenticator can satisfy more than one factor (Okta Verify = possession + biometric).

**Authenticator catalog (API table):** okta_verify (totp/push/signed_nonce incl. FastPass), google_otp, yubikey_token, rsa_token, duo, symantec_vip, onprem_mfa, webauthn, smart_card_idp, external_idp (federated), phone_number (sms/voice), okta_email, security_question, custom_otp/custom_app, tac, nfc_pin. Notable: other MFA vendors' products appear as authenticators inside Okta — the IdP absorbs MFA products as authenticator types.

**Two policy families:** authenticator enrollment policies ("control which authenticators are available for a user and when a user can enroll"); app sign-in policies ("determine the extra levels of authentication that are performed before a user can access an app" — required authenticators per app/group/scenario, assurance levels, conditions such as network location and device platform). Adaptive MFA = context-based (location/device). MFA positioned as one use of authenticators among several (passwordless is another).

### Twilio Verify (evidence layer A — directly observed, API surface)

**Positioning:** "Fight fraud and protect user accounts. Quickly verify users via SMS, Passkeys, Silent Network Auth, Voice, WhatsApp, TOTP, Push, Silent Device Approval, and Email." A verification API service, not an identity platform: "Twilio handles storing verification tokens and making sure messages are delivered globally. Your app provides the phone number or email address and verification method."

**Loop:** create a Verification (send token to user's device via a channel) → user receives token → Verification Check (the app submits the user-entered token; API returns valid/invalid). Channels: SMS, voice, WhatsApp, email, plus TOTP ("Authenticator Apps"), Push and Silent Device Approval (SDK/device-app based), Passkeys, Silent Network Auth (carrier-based). Configuration objects are "Verification Services" (per-use-case settings). Retry/rate-limiting/localization handled by the service; "Bring Your Own One-Time code" customization exists.

**No identity lifecycle:** no user directory, no sessions, no app federation — the calling application owns users and decides when to invoke verification. Twilio markets Verify integrations into identity platforms (Auth0, PingOne) and even RSA SecurID ("RSA SecurID + Verify" blog). This pole demonstrates MFA machinery sold as an API primitive where policy and identity live entirely with the caller.

### RSA SecurID (evidence layer B — positioning only; operational docs unreachable)

Product page claims: on-premises "access, authentication, and identity management" for "financial services, government agencies, and other high-assurance organizations"; "SecurID products like the SecurID 700 hardware authenticator have secured on-premises identity, data, and services … for decades"; RSA Authenticator App and DS100 hardware authenticator offered through RSA ID Plus with "hybrid failover" supporting on-prem authentication during cloud outages; RSA Authentication Manager "delivers the authentication, access, and management capabilities"; hardware appliance form factor; part of the RSA Unified Identity Platform (alongside Governance & Lifecycle). Supports "a range of hardware and software authentication factors and protocols including OTP, MFA, passwordless."

Held at positioning strength only. The heritage pole (hardware OTP token + PIN enforced for VPN/dial-in, tokens issued and assigned by administrators) is used in the historical check below at conceptual strength.

## Cross-product Comparison

| Dimension | Duo | Entra ID | Okta | Twilio Verify | RSA SecurID |
|---|---|---|---|---|---|
| Factor records held for users | devices/authenticators attached to user (phones, tokens, WebAuthn) | registered authentication methods | authenticator enrollments (instances) | TOTP/push/passkey factor registrations; per-request channel for SMS/voice/email; verification-token state | (positioning) issued hardware/software tokens |
| Challenge placement | separate prompt after primary auth (or redirect from IdP) | inside the Entra sign-in flow | inside sign-in flow per app sign-in policy | API start→check invoked by the calling app | (positioning) at access time for protected resources |
| Relationship to primary credential | "separate and independent … never sees your password"; can also be IdP itself | prompt "part of the Microsoft Entra sign-in" | sign-in policies add factors to primary auth | caller owns primary auth entirely | (positioning) authentication manager for protected resources |
| Who decides when MFA is required | Duo policies (per app/group/network/risk) | Conditional Access / security defaults / per-user MFA | app sign-in policies (+ enrollment policies) | the calling application | (positioning) always-on for protected resources |
| Method allowlist | per-policy authentication-method settings | authentication methods policy (enable/target per method) | authenticator configuration + enrollment policies | per-Service channel configuration | (positioning) token assignment |
| Recovery | bypass codes, self-service portal, admin reset, help-desk roles | TAP, admin re-registration/deletion, SSPR interplay, IDV-based high-assurance recovery | (concept docs: enrollment re-issue; not deep-fetched) | caller-implemented (service returns pass/fail) | (positioning) token replacement |
| Bypass / status model | explicit user status (active/bypass/locked-out/disabled) | method targeting; CA exclusions (documented in Duo-EAM page context) | policy targeting include/exclude | none (no user records) | (not observed) |
| Reporting | authentication log per attempt, dashboards, admin action log | sign-in logs / registration reports (referenced) | (not deep-fetched) | delivery/rate metrics via API/console | (not observed) |
| Standalone vs bundled | standalone product (also module of Duo IAM suite) | bundled in IdP (but attachable from outside via External MFA) | bundled in IdP | standalone API service | standalone on-prem product (part of larger platform) |

### What is common to all five (candidate core)

1. **Factor state held per user.** Every product holds something per user that it will verify against: enrolled devices/methods/authenticators (Duo, Entra, Okta), factor registrations or channel state (Verify), issued tokens (SecurID heritage).
2. **Challenge-verify distinct from the primary credential.** Every product presents a verification step at authentication time whose outcome (pass/fail) is consumed by the surrounding authentication flow — as an in-flow prompt (Entra, Okta), a secondary prompt/redirect (Duo), or an API check call (Verify).
3. **The factor set is under the relying organization's control.** Enrollment, allowed methods, replacement, revocation, and coverage are operated by the organization (admin console and/or management APIs), never solely by the end user. Even Verify exposes Service configuration to the developer-organization.

### What varies (candidate L1/L2)

- Whether the product is also the identity store / IdP (Duo optional; Entra/Okta yes; Verify no; SecurID no).
- Policy machinery depth (full policy engines with precedence + risk vs caller-owned policy).
- Factor-catalog breadth and phishing-resistance posture.
- remembered-device / step-up / adaptive behavior.
- Session/bypass/status models.
- Delivery of one-time codes (SMS/voice/WhatsApp/email) vs cryptographic authenticators (push, TOTP, FIDO2) vs federation.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

The MFA application is the **organization's second-factor verification layer**, held together by three jointly-lived structures:

1. **The enrolled factor of record** — for each covered user, the layer holds factor state it can verify against: an enrolled authenticator/device/method instance, an issued token, or a verified addressable channel, bound to the user's identity (which may live in the layer's own store or elsewhere).
   *Remove → a bare factor protocol or personal authenticator app with nothing held at the organizational layer.*
2. **The challenge-verify loop at authentication** — during/after primary credential verification, the layer challenges for a factor distinct from the primary credential and returns a verified/failed outcome that the authentication flow (sign-in UI, IdP policy engine, or calling application) consumes to grant or deny.
   *Remove → a primary-authentication password system / IdP; remove the distinction-from-primary → single-factor authentication.*
3. **The factor lifecycle under the relying organization's control** — enrollment (self-service, admin-assisted, bulk), method allowlist, replacement, revocation, recovery, and coverage/status are administered by the organization (console and/or APIs).
   *Remove → consumer personal 2FA or a stateless one-shot verification utility.*

### L1 — Common Mature Structure (market-expected, not defining)

- Broad factor catalog: mobile-app push, TOTP/software tokens, hardware OTP tokens, FIDO2 security keys & platform passkeys/biometrics, SMS/voice (and sometimes WhatsApp/email) one-time codes, security questions.
- Method allowlist + factor-role policy (some methods valid as primary vs secondary; phishing-resistant classes).
- Policy engine deciding when/for whom MFA is required (per app, group, network, location, risk), including degenerate always-on mode; risk-based/adaptive factor selection or step-up.
- Remembered devices / session trust (time-windowed skip).
- Bypass and status models (bypass users, lockout), backup/bypass codes, temporary credentials (TAP-like).
- Reporting: authentication logs (attempt, outcome, reason, device info), enrollment reports, admin-action logs.
- Dual surfaces: admin console + end-user self-service (enrollment portal, device management, security info).
- Integration surfaces: IdP federation (SAML/OIDC), RADIUS/LDAP for VPN/network gear, OS logon plugins, web SDKs/Auth APIs.
- Telephony/cost accounting for SMS/voice channels (where offered).

### L2 — Variant / Optional Structure

- Packaging: dedicated overlay service / module inside an identity platform / API-only service / on-premises authentication manager with hardware tokens and hybrid failover.
- Identity-store role: own directory with passwords (passwordless-ready) vs pure sync/attach to external directories vs no identity store at all.
- Enforcement scope: workforce/enterprise vs customer-facing (CIAM-integrated) vs both.
- Posture: phishing-resistant-only mandates; FIDO2-first; passwordless as a co-equal mode built on the same factor machinery.
- Guest/cross-tenant semantics, federal/regulatory editions, on-prem/cloud/hybrid deployment.
- Device-trust integration as a policy condition (managed-device checks, device health).

### L3 — Vendor-specific (kept out of the final document; examples for flavor)

- Duo: Verified Duo Push (code/Bluetooth proximity), Duo Desktop as an authentication factor, Policy Calculator, telephony-credit rate card, Authentication Proxy component.
- Entra: system-preferred MFA, number matching, Authenticator Lite in Outlook, Temporary Access Pass specifics, External MFA discovery-endpoint wiring, registration campaigns.
- Okta: FastPass/signed_nonce, third-party authenticator absorption (duo, rsa_token, symantec_vip keys), assurance-level policy language.
- Twilio: Silent Network Auth (carrier-level), Silent Device Approval, Bring Your Own One-Time code, per-Service configuration objects.
- RSA: SecurID 700/DS100 hardware authenticators, iShield Key FIDO series, hardware appliance form, hybrid failover during cloud outages.

### Anti-overfitting checks

- **Do not define by the smartphone/push era.** The SecurID heritage pole (hardware token + PIN, always-on) and printed one-time-code lists satisfy the L0 legs with no cloud, no app, no policy engine. Policy machinery therefore stays L1; the degenerate case "MFA always required for covered authentications" is valid.
- **Do not define by cloud SaaS.** On-prem Authentication Manager (positioning-level) and hardware appliances are in-type.
- **Do not define by the IdP-bundled form.** Verify has no directory and no sessions; Duo explicitly runs as 2FA-only with primary auth elsewhere; Microsoft built an External MFA framework precisely to attach outside MFA products to its control plane.
- **Do not define by factor kind.** SMS, TOTP, push, FIDO2, hardware tokens, biometrics are all realizations; the invariant is that the factor is distinct from the primary credential and held/enrolled at the layer.

## Historical / Market-Sample Check

- 1980s–2000s hardware-token MFA (RSA SecurID heritage, per vendor's own "for decades" claim): tokens issued by administrators, PIN + code at login for VPN/dial-in — all three L0 legs hold. ✓
- Bank paper one-time-code (TAN) lists: bank issues and replaces the list (factor of record + org-controlled lifecycle); code entry at transaction/login (challenge-verify). Conceptual strength only — fits. ✓
- Early smartphone-era TOTP: the authenticator app is not the Type; the server side that enrolled the shared secret and verifies codes is. This sharpens L0 leg 1/3 (the layer holds the factor state and the org controls it). ✓
- Modern FIDO2/passkey deployments: same three legs with a cryptographic factor; "phishing-resistant" is a posture (L2), not the Type. ✓

Conclusion: the definition survives older, regional, platform-native, and differently positioned products; no era-specific machinery (push notifications, cloud, smartphones, FIDO2, policy engines) appears in L0.

## Vendor-specific Findings

(See L3 above; none promoted to the canonical document except as clearly attributed examples.)

Additional packaging evidence worth retaining:
- Duo editions (Free/Essentials/Advantage/Premier) gate policy depth — pricing-tier packaging, not structure.
- Entra External MFA requires Entra ID P1/P2 with Conditional Access — licensing interlock, not structure.
- Okta's Classic-vs-Identity Engine terminology shift ("factor" once meant the concrete method) — terminology churn inside one vendor.

## Boundary Findings

**vs Single Sign-on / SSO (sibling §15, unprocessed):** SSO brokers one primary authentication into many applications (sessions/tokens); MFA adds a verification step at authentication. Clean remove-tests both ways: remove the factor layer → SSO/IdP; remove app brokering/session issuing → MFA. Market evidence the seam is real: Duo ships MFA and SSO as separately documented products; Entra's External MFA framework attaches an MFA provider under an IdP whose own policy engine still decides access ("Microsoft Entra ID continues to handle full policy evaluation and access decisions as the identity control plane"). The two Types interlock (an MFA layer commonly protects the SSO portal itself; Duo documents exactly this for its Admin Panel).

**vs Identity & Access Management / IAM (sibling §15, processed) — answers the IAM pass's pre-hung flag:** The IAM pass suspected MFA/SSO are "Capabilities/Variants of IAM rather than independent Types." This pass holds **keep-both** from the MFA side: (1) the unit of record differs — IAM's defining structure is administered identity lifecycle + access grants + central administrative control over identities; the MFA layer's unit of record is the enrolled factor, and it can operate with no identity lifecycle of its own (Duo 2FA-only mode with primary auth elsewhere; Twilio Verify with no directory at all); (2) hyperscale IdPs acknowledge the split architecturally (Entra External MFA; Okta listing duo/rsa_token/symantec_vip as external authenticator types — IdPs absorb MFA products as authenticators rather than replacing them); (3) conversely, every sampled identity platform bundles factor management as standard capability — so IAM-bundled MFA is capability packaging of this Type's machinery, the same pattern other passes recorded (monitoring inside observability platforms, proctoring inside examination platforms). Joint review note stands for the SSO leaf; for MFA this pass records the seam as settled unless the SSO pass disagrees.

**vs Customer Identity / CIAM (sibling §15, processed):** CIAM's defining core is the customer identity population + self-service lifecycle + delegated authentication for the organization's apps. MFA/step-up is standard capability inside CIAM platforms; standalone MFA machinery serves CIAM as a factor layer via API (Twilio Verify's own docs and its Auth0/PingOne integration posts). Seam = account-of-record + authentication brokering vs factor enrollment/challenge. No merger.

**vs Identity Verification (sibling §15, processed):** Identity verification establishes real-world identity at onboarding/recovery (subject of record + evidence capture + evaluation + decision). MFA verifies recurring access with enrolled factors. Vendor-acknowledged seam: Microsoft's own docs classify Verified ID as "an identity verification capability … not a traditional authentication method. It can't be used to satisfy authentication requirements like sign-in, MFA, or SSPR." Interlock, not overlap: high-assurance account recovery (IDV + biometric) bridges lost-factor recovery into identity verification.

**vs Password Manager (sibling §15, unprocessed):** password managers commonly store TOTP seeds for personal convenience — an authenticator capability without organizational enrollment, allowlist, policy, or lifecycle control. Fails L0 leg 3; not this Type. Recorded to preempt confusion since Duo lists 1Password/LastPass as *protected applications*.

**vs Fraud Prevention / Account Abuse Protection (siblings §15, processed):** risk scoring appears inside MFA products as a policy input (risk-based factor selection/step-up); the fraud Types center journey/transaction risk decisions. MFA risk machinery is an L1/L2 policy input, not the defining core.

**vs PAM (sibling §15, unprocessed):** PAM centers privileged sessions/credential vaulting; MFA is commonly consumed there as a step-up capability. No structural confusion observed in this sample.

**Packaging observation (taxonomy-safe):** the Type realizes in four market shapes — dedicated overlay (Duo), identity-platform module (Entra, Okta), API service (Verify), on-prem authentication manager (SecurID). The leaf is kept as one Type because all four realize the same three L0 legs and are independently sold/deployable; bundling inside IAM/CIAM suites is capability packaging, consistent with precedent passes.

## Uncertainties

1. RSA SecurID operational mechanics (Authentication Manager admin surface, token provisioning, policies) are NOT verified — community.rsa.com not fetched. All RSA statements are positioning-level.
2. Okta operational detail (admin console flows, exact enrollment UX) not fetched (help.okta.com SPA); concept-level evidence only.
3. Twilio Verify's account-level policy surface (beyond per-Service configuration) was not deep-fetched; the claim "the caller owns policy" rests on the API design and product docs read.
4. Historical samples (TAN lists, early TOTP server side) are used at conceptual strength for the §24 check, not asserted as product facts.
5. The relative market weight of the four packaging shapes is unknown (no market-size evidence gathered); the document deliberately makes no market-share claim.
6. Exact numeric limits everywhere (code lengths, session windows, retry counts) were observed only for a few Duo/Entra specifics and are deliberately excluded from the final document per evidence rules.

## Final Synthesis

MFA is best modeled as the **organization's second-factor verification layer**: it holds enrolled factor state per user (or verifies addressable channels), challenges at authentication time with a factor distinct from the primary credential, returns a verified/failed outcome the surrounding authentication flow consumes, and keeps the factor set under organizational control (enroll, allow, replace, revoke, recover). Everything else — factor catalog breadth, policy engines, risk-based step-up, remembered devices, bypass/recovery programs, reporting, integration surfaces — is mature market structure layered on that core, varying by packaging (overlay / IdP-module / API / on-prem) and by audience (workforce vs customer-facing). The Type survives the historical check (hardware-token era, paper code lists) and coexists with IAM/SSO/CIAM products that bundle its machinery as a capability.
