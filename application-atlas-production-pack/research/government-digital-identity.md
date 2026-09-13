# Research Notes — Government Digital Identity

## Research Goal

Understand the Application Type "Government Digital Identity" (Directory leaf, section 24 Government, Public Sector & Civic) from real products: what the system is, who operates it, what its core structures are, how residents and relying services use it, and where its boundaries lie against adjacent Types (Government Service Portal, IAM, CIAM, Identity Verification, Digital Wallet, SSO).

## Initial Boundary

Hypothesis before research:

- Core use: a government-operated (or government-mandated) digital identity system that lets residents prove who they are online and use that identity to access public digital services, sometimes private services.
- Likely confusions:
  - Government Service Portal (the front door that aggregates services — different object)
  - IAM / SSO (organizational workforce identity — different population and legal basis)
  - Identity Verification / KYC (commercial one-shot proofing — no ongoing holder identity)
  - Digital Wallet / Digital Credential Platform (holds and presents documents; does not establish identity)

## Research Questions

1. What is the core object: an account, a credential, a verified attribute set, or all three?
2. How does identity verification (proofing) work, and is it structurally separate from authentication?
3. What does the resident do day-to-day (authenticate, share data, sign, manage credentials)?
4. How do relying services (government departments, sometimes private companies) consume the identity?
5. Is there a strength/assurance concept that gates which services a resident can access?
6. What exception flows exist (lost phone, lost card, blocked PIN, duplicates, name changes, fraud)?
7. Who operates the system, and does the operating model vary (government-run vs delegated)?
8. What is the historical check result — do older / card-based / non-app systems fit the same definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different eras/geographies:

| Product | Jurisdiction / Operator | Philosophy | Evidence |
|---|---|---|---|
| Login.gov | United States / GSA | central web sign-in service for agencies; proofing optional by service level | A — direct (developer guide + help center + verify-identity overview) |
| Singpass | Singapore / GovTech (National Digital Identity) | app-first super-credential: login + data sharing + in-person proving + signing | A — direct (main site + individuals pages; developer docs unreachable) |
| ID.ee (Estonian e-ID) | Estonia / Information System Authority (RIA), with private operator SK ID Solutions for Smart-ID | smartcard PKI ecosystem: ID-card + Mobile-ID + Smart-ID; signing-centric | A — direct (id.ee home + authentication section) |
| myID | Australia / Commonwealth (ATO-operated) | mobile app proving "who you are" with identity-strength tiers gating services | A — direct (myid.gov.au home + setup page) |

Samples attempted and abandoned (source unreachable after retries; no claims drawn from them):

- GOV.UK One Login (docs.signin.service.gov.uk transport error; gov.uk publication page 404; one-login.service.gov.uk transport error)
- MitID (mitid.dk 403; docs.mitid.dk transport error)
- Aadhaar / UIDAI (uidai.gov.in transport errors ×2)
- Singpass developer docs (docs.singpass.gov.sg transport errors ×2)

## Sources

Fetched 2026-09-07:

- Login.gov Developer Guide — https://developers.login.gov/
- Login.gov Help Center — https://www.login.gov/help/
- Login.gov "Verify my identity" — https://www.login.gov/help/verify-your-identity/overview/
- Singpass main site — https://www.singpass.gov.sg/main
- Singpass For Individuals — https://www.singpass.gov.sg/main/individuals/
- ID.ee home — https://www.id.ee/en/
- ID.ee Authentication section — https://www.id.ee/en/rubriik/authentication/
- myID home — https://www.myid.gov.au/
- myID "How to set up myID" — https://www.myid.gov.au/how-to-set-up-myid

## Product Observations

### Login.gov (United States) — Evidence Layer A

Developer guide (agency-facing):

- Login.gov is a central sign-in service that US government agency applications integrate with. Agencies register applications in a Partner Portal, configure and test in a sandbox, then request production; an Inter-Agency Agreement is required for go-live.
- Integration checklist: application name, protocol (SAML or OpenID Connect), **service level "either Authentication only or Identity Verification"**, data/attributes needed, **authentication assurance levels**, agency logo, key pair/certificate.
- Attributes page exists (data agencies can request about the user).

Help center (resident-facing) — top-level sections:

- Create my account (email + password; authentication methods: face or touch unlock, authentication application, security key, text/SMS or phone call, backup codes, **government employee ID (PIV/CAC)**)
- Trouble signing in (lost phone or personal key, account locked, security check failed)
- Manage my account (change/add email addresses, change phone, change password, change email shared with a partner agency, add/change authentication method, delete account, account deactivated, **relink account with a partner agency**, **fix duplicate accounts**)
- Verify my identity (see below)
- Help with agencies (IRS, Medicare.gov, SSA, Trusted Traveler Programs, SAM.gov)
- Fraud concerns (unrequested one-time codes, verifying messages, protecting account, common scams, reporting suspicious activity)

"Verify my identity" overview:

- Identity verification defined as "the process where you prove you are you — and not someone pretending to be you." Needed **to access services at some agencies** — i.e., proofing is per-agency-requirement, not universal.
- Requirements: US driver's license / state ID / passport book or card; Social Security number; US phone number or mailing address.
- Flow: (1) take photos of ID online, sometimes a selfie to confirm ID ownership; alternative in-person at a US Post Office; (2) enter SSN, verified against public and proprietary records; (3) verify phone via one-time code, or address by mail; (4) re-enter password to store verified information in the account and **connect it to the partner agency**.
- "We ask for your consent before we share your verified information with the partner agency."

Interpretation:

- Two distinct service levels (authentication vs identity verification) confirm that **account/authentication and identity proofing are structurally separate layers**; a resident can hold a usable account without any proofing, and proofing is triggered by agency requirements.
- The identity is presented to many distinct agencies (IRS, SSA, Medicare, TTP, SAM.gov…) — multi-relying-party by design.
- Account lifecycle is resident-managed (emails, phone, factors, deletion, relink, duplicates).

### Singpass (Singapore) — Evidence Layer A (user-facing surfaces only; developer docs unreachable)

- Positioning: "Singpass is your trusted digital identity for all the secure transaction needs in your everyday life"; "Access over 2,700 services by over 800 government agencies and businesses" — relying parties explicitly include both government and private sector.
- Operator: Government of Singapore (GovTech; National Digital Identity programme). Registration via portal with step-by-step guide (PDF).
- Login without passwords: passkeys created in the Singpass app; **Face Verification kiosks** at selected public service centres ("scan your NRIC and verify with your face"); **Login shortcuts** (one-tap from app to services like CPF e-services, HealthHub); **QR Login** — scan the QR code shown by a government or private service; the app shows a **consent screen** ("Are you logging into CPF E-Services?").
- Prove identity in person: **Digital IC** — show a watermarked digital identity card or tap a barcode in the app; **Verify details** — share your details from government sources with an organisation, with a consent screen ("Are you sending your details to Tan Tock Seng Hospital?").
- Digital signing: **document signing** (sign documents/contracts remotely, validated signature) and **transaction signing** (authorise transactions remotely, with app confirmation).
- Myinfo: **Myinfo profile** — view personal information from different public agencies in one place; **Autofill with Myinfo** — fill forms with one click ("Use Myinfo" button). Myinfo described from the business side as "Receive information from individual and corporate users quickly and easily with data from government sources" (note: corporate users too).
- Notifications: reminders and updates (e.g., passport appointment), renewal notifications before documents expire (inbox in app).
- SGFinDex: a financial-planning data platform reached via Singpass login; connect accounts across financial institutions and government agencies; disconnect anytime.
- Digital documents: visual of passport/NRIC/education certificate/driver's licence as digital items "easily accessed with your trusted digital identity."
- Anti-fraud surface: never share Singpass ID/password/2FA; check the singpass.gov.sg domain; "Singpass never sends web links or QR codes via SMS or WhatsApp."
- Scale figures published on the page (4.2M+ app users, 2,700+ services, 41M+ transactions/month) — vendor-published marketing numbers, recorded as such.

Interpretation:

- The most feature-complete sample: authentication (app/QR/kiosk/passkey), in-person identity proving, consent-based data sharing from government sources, digital signing, notifications, and digital documents all attach to one identity.
- The consent screen naming the receiving party appears both at login (which service am I logging into?) and at data sharing (which organisation am I sending my details to?) — consent is user-visible at the moment of presentation.
- Login is the daily core; data sharing (Myinfo) and signing are major attached capabilities.

### ID.ee / Estonian e-ID (Estonia) — Evidence Layer A

- The site (maintained by the Information System Authority, RIA) covers the electronic use of government-issued identity: **ID-card** (electronic use, certificates, PIN/PUK codes, security, testing), **Mobile-ID** (SIM-based digital identity document), **Smart-ID** (a free app by private operator SK ID Solutions enabling login to e-services, transaction confirmation, and document signing).
- ID-help sections: Signing, Authentication, Encryption, PIN codes, Browsers, Software and installation, Card reader, For administrator, Security software, Security.
- Authentication section: "If you want to enter an e-service using your ID-card or a digital identification method, you must first authenticate yourself, i.e. prove that you are who you claim to be… Authentication must be reliable and secure." e-services explicitly include online banks (private sector reliance) as well as national e-services.
- Digital signing is a first-class pillar: DigiDoc applications, signing on phone via NFC (RIA DigiDoc + ID card), developer libraries, validation service (SiVa), trust services (timestamping), Web eID.
- Credential lifecycle and exceptions are heavily documented: blocked PIN unlocked with PUK via DigiDoc4; new PIN code envelopes ordered from the Police and Border Guard Board; lost/stolen card guidance; **certificate suspension** (SK ID Solutions 24/7) and **revocation** (Police and Border Guard Board self-service portal).
- One identity, multiple credential media: card, Mobile-ID, Smart-ID — the person's e-identity persists across media; counters show ~1.16M ID-cards, ~217K Mobile-ID, ~794K Smart-ID users (site-published).
- Applying for the ID card itself is done at politsei.ee (Police and Border Guard Board) — issuance of the underlying identity document is separated from the electronic-use support site.

Interpretation:

- The oldest sample (smartcard PKI era, app-optional). Fits the Type without any of the modern app-centric features: the defining structure cannot include mobile apps, QR login, or central data platforms.
- Confirms: authentication to many e-services (government + private) with government-issued credentials is the recurring act; signing is a major variant capability; credential lifecycle (PIN/PUK, suspension, revocation) is central to operations.
- Confirms a hybrid operating model: government issues the identity document and certificates; a private company (SK ID Solutions) operates one of the credential channels (Smart-ID).

### myID (Australia) — Evidence Layer A

- Positioning: "The Australian Government's Digital ID app. myID is a secure way to prove who you are online." Download from official app stores only; use "again and again to access participating online services."
- Setup: smart device + personal email address ("your ID documents will be linked to the email you choose") + age 15+; enter email, password, full name, date of birth → **Basic** identity strength.
- **Identity strength tiers** (named): Basic (personal details only; access to limited services), Standard (verify ID with any 2 of a list of Australian documents — passport, driver's licence/learner's permit, birth certificate, visa, ImmiCard, citizenship certificate, Medicare card; names must generally match; change-of-name certificates supported in some states), Strong (documents + photo verification: a one-off face verification — selfie compared to the photo on the passport or driver's licence, with step-by-step "real person, right person, verifying in real time" confirmation; access to all services).
- "Each online service has a minimum identity strength for access" — the strength concept is explicitly the access-gating mechanism across participating services.
- Business use: to act for a business, myID is linked to the business's ABN in **Relationship Authorisation Manager** (a separate online service); the principal authority links first at Standard strength; other users are authorised by the principal authority or authorisation administrator.
- Other sections: verifying your ID in myID (documents + photos), increasing identity strength, protecting your Digital ID, help, system maintenance.

Interpretation:

- The cleanest expression of the **assurance-level gating** pattern: strength tiers are named, documents-defined, and map to per-service minimums.
- Verification is document-evidence-based (2-document rule, name matching, face check at Strong) — same family as Login.gov's proofing but tiered differently.
- Multi-RP from birth ("participating online services", with a service directory); business representation is a variant surface (relationship authorisation is delegated to a separate system).

## Cross-product Comparison

| Dimension | Login.gov | Singpass | ID.ee (Estonia) | myID |
|---|---|---|---|---|
| Core positioning | central sign-in for US agencies | trusted digital ID for everyday transactions | electronic use of national e-identity (card/SIM/app credentials) | government app to prove who you are online |
| Identity account for a natural person | yes (email+password account) | yes (Singpass account, registration flow) | yes (person holds e-identity credentials) | yes (app account tied to email+personal details) |
| Verification against authoritative evidence | ID document + SSN vs records; optional per agency | registration per national process (guide; details not fetched) | government issues ID card with certificates via Police | document set rules + face check; tiered Basic/Standard/Strong |
| Assurance/strength gating access | service levels (auth-only vs ID verification); authentication assurance levels | not directly observed in fetched pages (likely; unconfirmed) | certificates underpin trust (levels not fetched) | explicit named tiers; per-service minimum strength |
| Multiple authentication factors/methods | face/touch, authenticator app, security key, SMS/call, backup codes, PIV/CAC | app login, passkeys, QR, face kiosks | card PIN, Mobile-ID, Smart-ID | app password + device; face verification at Strong |
| Multi-relying-party presentation | IRS, SSA, Medicare, TTP, SAM.gov… | 2,700+ gov & business services (vendor figure) | national e-services + online banks | participating government services directory |
| Consent-gated data sharing | consent before sharing verified info with partner agency | Myinfo autofill + verify-details consent screens; SGFinDex connections | not observed as a central data platform | not observed (business authorisation via RAM instead) |
| In-person / assisted channel | US Post Office verification | face verification kiosks; counters | police-issued card, PIN envelopes | not observed in fetched pages |
| Digital signing | not part of the service | document + transaction signing | first-class (DigiDoc, NFC signing, validation) | not part of the service |
| Notifications/reminders | not prominent | reminders, renewal notices | not observed | not observed in fetched pages |
| Holder credential management | emails/phone/factors, delete, relink, duplicates | registration, 2FA care, anti-phishing rules | PIN/PUK, suspension, revocation, card loss | set up again on new devices, protect Digital ID |
| Business/on-behalf use | not observed | Myinfo covers corporate users (business side) | not observed | ABN linking via Relationship Authorisation Manager |
| RP integration machinery | Partner Portal, sandbox→production, IAA, OIDC/SAML | developer portal exists (unreachable) | developer sections (identification, signing, testing) | participating-services model (mechanism not fetched) |
| Private-sector relying parties | not observed (agencies listed) | yes (businesses) | yes (banks) | government only (observed) |
| Era / medium | modern web-first | modern app-first | 2002-era smartcard + SIM + app | modern app-first |

## Canonical Abstraction

### Level 0 — Defining Invariant

Three structures, held jointly:

1. **The resident identity account** — a persistent identity held by a natural person (resident/citizen), established by registering with the service and anchored to that person (in all samples tied to personal details and, ultimately, government-issued evidence). Remove → ordinary multi-user website accounts or enterprise workforce IAM.
2. **Identity verification against authoritative evidence** — the service verifies the person against government-issued documents, government records, biometrics, or in-person attestation, producing a verification state (with strength/assurance) attached to the identity. Remove → plain self-registered account system (any CIAM).
3. **Repeated presentation of the verified identity to multiple relying services** — the holder authenticates (and/or shares verified attributes with consent) across many independent services, government and sometimes private. Remove → a single department's account system, or a one-shot commercial identity check (Identity Verification Type).

### Level 1 — Common Mature Structure

- Multiple authentication methods/factors per holder (app biometrics, passkeys, OTP, security keys, PINs; device or card bound)
- Assurance/strength levels gating which services can be accessed (Login.gov service levels + assurance levels; myID named tiers with per-service minimums)
- Holder account management: change contact details, add/remove factors, delete/deactivate, relink with services, resolve duplicate accounts
- Recovery and exception machinery: lost phone/card, blocked PIN/PUK, locked accounts, suspension and revocation channels
- Consent-gated attribute sharing with relying services (verified data released per-service, user visible consent)
- In-person / assisted verification alternatives to remote proofing (Post Office, kiosks, police counters)
- Anti-fraud and anti-phishing guidance as a standing surface
- Relying-party integration machinery (partner portal, sandbox/testing, protocols, go-live review)
- Notifications/reminders tied to the identity holder

### Level 2 — Variant / Optional Structure

- Relying-party scope: government-only vs including private sector (Singpass, Estonia include businesses/banks; Login.gov's observed list is agencies)
- Central data-sharing platforms over the identity (Myinfo/SGFinDex-class) — strong in Singapore, absent elsewhere in the sample
- Digital documents / digital identity card presented in-app (Singpass Digital IC)
- Digital/transaction signing as part of the identity service (Singpass, Estonia — a signature-capable identity; absent in Login.gov/myID observations)
- Medium philosophy: web sign-in service (Login.gov), mobile app (Singpass, myID), smartcard/SIM ecosystem (Estonia)
- Operating model: direct government operation vs delegated components to private operators (Smart-ID by SK ID Solutions; police-issued certificates)
- Business/on-behalf-of representation with relationship authorization (myID/RAM; Singpass corporate Myinfo)
- Population-coverage model (universal issuance vs opt-in registration; not directly researched in the sample)

### Level 3 — Vendor-specific Structure

- Login.gov: Inter-Agency Agreement requirement, Partner Portal + sandbox, PIV/CAC as a factor, reCAPTCHA security checks, relink/duplicate-account flows
- Singpass: SGFinDex, National Digital Identity programme branding, passkey creation flow, watermarked Digital IC, SafeEntry reference, vendor-published scale figures
- myID: ABN linking via Relationship Authorisation Manager, the specific document lists and name-change certificate state scope (ACT/NT/SA/Tas), age-15 floor, "setting up again" device migration flow
- Estonia: DigiDoc/CDOC2 formats, SiVa validation service, Web eID, trust-list versioning, SK ID Solutions as TSP, politsei.ee PIN envelopes, revocation-portal split by certificate issue date

## Historical / Market-Sample Check

- Estonia's e-ID (smartcard era, 2000s) satisfies the three Level 0 structures with **no mobile app, no QR, no central data platform, no biometric proofing**. So none of those can be definitional.
- Login.gov serves agencies whose services require **authentication only** (no identity verification) — a resident's account is still a government digital identity. So mandatory document-based proofing for every holder is not definitional (verification capability and the verification *layer* are; universal proofing is not).
- myID's Basic tier (personal details only) likewise shows an identity can exist below document verification — verification strength is graduated, not binary.
- Conclusion: the definition holds across eras and media; modern app/QR/biometric features are implementations, not invariants.

## Boundary Findings

| Adjacent Type | Distinguishing test |
|---|---|
| **Government Service Portal** | Portal aggregates services and transactions for the resident (content, forms, payments, messaging). The digital identity is the identity *layer* those services call. Remove multi-service presentation and verification → a service catalogue/portal; a portal without an identity layer just has per-service accounts. Singpass login vs the services behind it illustrates the seam. |
| **Identity & Access Management / IAM** | IAM governs workforce access to an organization's systems. Remove the government mandate, resident population, and authoritative-evidence verification → enterprise IAM. |
| **Customer Identity / CIAM** | CIAM manages customers of one commercial organization. Remove government anchoring/issuance → CIAM. |
| **Identity Verification (commercial)** | One-shot proofing delivered to a relying business; no ongoing holder identity, credentials, or repeated presentation. Remove the persistent resident account + recurring authentication → Identity Verification. |
| **KYC / KYB Platform** | Regulated onboarding proofing for financial institutions, tied to compliance case files. Same removal test as Identity Verification. |
| **Single Sign-on / SSO** | SSO is a capability/mechanism. A citizen-facing SSO with government anchoring and proofing *is* an instance of this Type (Login.gov is close to this pole), not a separate one; generic enterprise SSO lacks the resident-verification layer. |
| **Digital Wallet** | Wallets hold and present documents/credentials the user already has. The digital identity establishes and authenticates the identity itself. Singpass includes wallet-like surfaces (Digital IC) — wallet features are variants, not the Type. A pure document wallet without identity verification/authentication is not this Type. |
| **Digital Credential Platform (education)** | Issues/verifies domain credentials (diplomas etc.); no government identity anchoring, no population-scale resident identity. |

"Remove what to become another Type" summary:
- Remove government anchoring + authoritative-evidence verification → CIAM / enterprise IAM
- Remove the persistent holder identity + recurring presentation → Identity Verification / KYC
- Remove multi-service reliance (single service only) → that service's account system
- Remove verification and presentation, keep service aggregation → Government Service Portal
- Keep only document holding/presentation → Digital Wallet

## Uncertainties

- Relying-party integration protocols for Singpass and myID were not directly observed (developer docs unreachable); protocol-level claims avoided.
- Singpass registration/proofing steps (what evidence is accepted) were not fetched; kept out of all claims.
- Whether identity-strength tiers exist under other names in Singpass (likely, unconfirmed) — recorded as likely-but-unverified.
- Whether newer wallet-first models (e.g., EU EUDI Wallet) shift the Type's center of gravity was not researched; no fetch succeeded for EU sources.
- Evidence that Login.gov serves private-sector relying parties: none found; assertion kept to agencies.
- Vendor-published scale figures (Singpass user/transaction counts, Estonia credential counters) recorded as vendor-published, not independently verified.

## Final Synthesis

A Government Digital Identity is government-anchored identity infrastructure for a resident population. Its defining core is three structures held jointly: (1) a persistent resident identity account; (2) verification of that identity against authoritative (government-issued) evidence, producing a graduated verification strength; (3) repeated presentation of the verified identity to many relying services through authentication and, where supported, consent-gated sharing of verified attributes. Around this core, mature systems add multi-factor authentication, holder-managed credential lifecycle with recovery/revocation, in-person channels, anti-fraud surfaces, relying-party integration machinery, and — variably — data-sharing platforms, digital documents, digital signing, and business representation. Realizations range from smartcard PKI ecosystems (Estonia) through web sign-in services (Login.gov) to app-first super-credentials (Singpass, myID). The Type is distinct from portals (service aggregation), IAM/CIAM (organizational/commercial identity), identity verification (one-shot proofing), and wallets (document holding).
