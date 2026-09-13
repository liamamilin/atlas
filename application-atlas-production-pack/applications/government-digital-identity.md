# Government Digital Identity

## Overview

A **Government Digital Identity** is a government-operated or government-mandated identity service that lets residents prove who they are online and use that verified identity to access public digital services — and, in many countries, private-sector services as well.

It is the identity layer of the state's digital front: individual agencies build their own services, but instead of every service maintaining its own accounts and its own proof of who you are, one authoritative system establishes the resident's identity once, verifies it against government-issued evidence, and then stands behind every login and every exchange of personal data that the resident makes with participating services.

The defining structure is small:

```text
Resident identity account
  └── verified against authoritative (government-issued) evidence
        └── presented repeatedly to many relying services
              (authentication, and consent-gated sharing of verified data)
```

Everything commonly associated with modern systems — mobile apps, QR-code login, face verification, central data-sharing platforms, digital signatures, digital identity cards — is widespread in current products but is not part of the defining core. Older and differently-shaped systems, such as smartcard-based national e-ID ecosystems from the early 2000s, satisfy the same definition without any of those specifics.

When the aggregation of services themselves becomes the focus — service catalogues, forms, payments, case messages — the product is a Government Service Portal, which *consumes* a digital identity rather than being one.

## Users & Context

**Primary users — residents and citizens (identity holders).** Each person registers once, verifies their identity, and then uses the same identity again and again: signing in to tax, health, benefits, licensing, and municipal services; proving who they are in person at counters or kiosks; authorizing transactions; sharing verified personal data instead of re-submitting documents. The identity holder is a layperson, so usage must work at population scale, including people who lose their phone, forget their PIN, or cannot complete remote verification.

**Relying services.** Government agencies and departments integrate against the identity service instead of building their own login and proofing. In several systems, private organizations — banks, hospitals, businesses — are relying parties too. Each service declares what it requires (for example, a minimum verification strength) and what data it may receive.

**Business representatives.** Some systems support acting on behalf of a business: a person's individual identity is linked to the business, and their authorization rights within it are managed separately.

**Operators and support staff.** The identity service is run by a government agency or a mandated operator. Its staff manage the registration and verification machinery, credential lifecycle (issuance, suspension, revocation), help channels, and the integration program through which relying services join.

## Core Model

### The Defining Core

Three structures, held jointly. If any one is removed, the product is no longer recognizable as a government digital identity:

- **Resident identity account** — a persistent identity held by one natural person, established by registering with the service. The account is the anchor: it is personal, lifelong in intent, and independent of any single relying service. Without it, there is no ongoing identity — only disconnected service accounts.
- **Verification against authoritative evidence** — the service verifies the person against government-issued documents, government records, biometrics, or in-person attestation, and records a verification state attached to the identity. Verification is typically graduated: a person who has registered but not yet verified documents holds a weaker identity than one who has verified documents and a face match. Without this, the system is just a self-registered account service, indistinguishable from any commercial login.
- **Repeated presentation to many relying services** — the holder uses the identity across many independent services: signing in to each one, and where supported, sharing verified personal data with a service after explicit consent. The identity service is shared infrastructure for a whole service landscape, not the account system of one website. Without this, it is a single department's login page or a one-shot identity check.

### How the Structures Relate

```text
Resident
  └── registers → identity account
        └── verifies → verification strength (graduated)
              └── presents to relying services
                    ├── authenticate (sign in)
                    └── share verified data (with consent)
```

The verification strength is what makes the system authoritative: it records *how well* the person's identity has been established, and relying services depend on it when deciding what a given person may do online.

### Standard Capabilities of Mature Systems

These are common across mature implementations; they make the identity practical but do not define the Type:

- **Multiple authentication methods** per holder — app-based biometrics, passkeys, one-time codes, security keys, PINs tied to a card or SIM, and physical employee/official credentials in some systems. Methods can be added, removed, and replaced.
- **Verification strength tiers** — named levels (such as basic / standard / strong) or assurance levels, each defined by the evidence verified, with each relying service declaring the minimum it accepts.
- **Holder account management** — changing contact details, adding or replacing authentication methods, deleting or deactivating the account, relinking with a relying service, and resolving duplicate accounts.
- **Recovery and exception machinery** — lost phone or card flows, blocked PINs with unlock procedures, locked accounts, certificate suspension and revocation channels, and assisted re-registration on new devices.
- **Consent-gated data sharing** — verified personal data held by the identity system (or reachable through it from government sources) is released to a relying service only with the holder's explicit, per-service consent.
- **In-person and assisted channels** — verification at post offices, government counters, or kiosks for people who cannot complete remote verification, and in-person identity proving as an alternative to carrying physical documents.
- **Anti-fraud and anti-phishing surfaces** — standing guidance (never share codes or passwords; check the official domain; the service never sends links through messaging apps) and reporting channels for suspicious activity.
- **Relying-party integration machinery** — a partner or developer program with registration, testing environments, and a go-live review before a service may accept the identity.
- **Notifications** — reminders and updates tied to the holder, such as document expiry notices.

### One Structure, Many Implementations

The core is written conceptually. Realizations differ:

```text
Concept:                      Resident identity account
Implementations:              app account, web account, smartcard/SIM credential ecosystem

Concept:                      Verification against authoritative evidence
Implementations:              document photo + records check + selfie; two-document rules;
                              face-verification kiosks; government-issued card with certificates

Concept:                      Presentation to relying services
Implementations:              web redirect sign-in, app login shortcuts, QR-code login,
                              kiosk login, consent-screen attribute sharing
```

A reader who has only seen app-based systems should still recognize a smartcard-era national e-ID, and vice versa, from the defining core alone.

## How It Works

### Register and verify (the establishment loop)

```text
Download app / visit sign-up
→ create the identity account (email or personal identifier, password, name, date of birth)
→ basic identity: limited access to participating services
→ verify identity documents (photo capture, records check, possibly a face check)
   or attend in person at a counter / post office / kiosk
→ verification strength rises; more services become accessible
```

Registration and verification are deliberately separate: a person can hold a working, weaker identity before completing document verification, and verification depth grows as more evidence is verified. Each relying service declares the minimum strength it accepts, so the same person can use a low-strength identity for simple services and a fully verified one for sensitive ones.

### Sign in to a relying service (the authentication loop)

```text
Open the government or private service
→ choose the national digital identity as the sign-in method
→ authenticate with the chosen method (app biometric, passkey, one-time code, card PIN…)
→ confirm on the trusted surface which service is being entered
→ return to the service, signed in
```

The confirmation step matters: the holder sees, on the identity app or a trusted page, *which* service they are entering. Some systems add app-based login shortcuts (one tap from the identity app straight into a frequently used service) or QR-code login, where the service shows a code and the identity app scans it.

### Share verified data (the attribute loop)

```text
In a relying service's form or counter interaction
→ choose to use the digital identity's verified data
→ the identity app shows a consent screen naming the receiving organization
→ holder approves
→ the service receives the verified details; no documents re-submitted
```

Where a system supports this, the identity service (or platforms built on it) pulls personal data from authoritative government sources and releases it per-service, per-consent. The same consent pattern appears at the counter: the holder proves or sends their details to an organization from the app instead of presenting physical documents.

### Manage credentials and recover (the lifecycle loop)

```text
Holder manages the identity over years:
→ add / replace authentication methods and devices
→ change contact details; set up the identity again on a new phone
→ handle exceptions: lost phone or card, blocked PIN (unlock with recovery code),
   locked account, suspected fraud
→ operators may suspend or revoke credentials / certificates when compromised
```

Because the identity is long-lived and gates access to sensitive services, credential lifecycle is a first-class operational concern: recovery paths, suspension and revocation channels, and in-person re-establishment are documented parts of the system, not afterthoughts.

## Interfaces

### Mobile identity app

The holder's primary surface in app-first systems.

- shows the verified identity (and, in some systems, a digital identity card that can be shown or scanned in person)
- performs logins (direct shortcuts, QR scanning) with a confirmation screen naming the target service
- presents consent screens for data sharing and transaction authorizations
- carries notifications and reminders
- primary actions: sign in, approve, share details, show identity

### Web sign-in and account management

The web surface of the identity service.

- sign-in page used as the redirect target when a resident chooses the national identity on a relying service's site
- account management area: change email/phone/password, manage authentication methods, delete or deactivate, relink with a service, resolve duplicate accounts
- verification area: start or continue identity verification, upload document photos, book or find in-person verification
- help and fraud-reporting sections

### Consent / confirmation screens (in-app and web)

Small, safety-critical surfaces.

- state exactly which organization or service is receiving the login or the data
- carry the approve / deny decision
- are the holder's main defense against phishing — the trusted surface that impostor sites cannot reproduce

### In-person channels

- verification kiosks (scan an identity document, verify with a face check)
- post-office and government-counter verification and credential collection
- app-based proving of identity or details at a counter as an alternative to physical documents

### Partner / developer portal

The relying-party side.

- register an integrating service, configure protocols and required data, test in a sandbox
- declare the service's required verification strength and requested attributes
- request go-live approval under the operating agency's program

## Important Rules / Behaviors

### Verification strength gates access

A resident's verification state is not binary. Services declare the minimum strength they require; the identity service enforces it. A basic identity may reach only simple services; document-verified and face-verified identities reach increasingly sensitive ones. Increasing strength is the holder's deliberate act of verifying more evidence.

### Consent precedes data release

Verified personal data flows to a relying service only after an explicit, user-visible consent that names the recipient. The same discipline applies to logins (confirm which service you are entering) and transaction authorizations (approve the specific action). Data sharing is scoped per service, and holders can disconnect previously authorized connections in systems that maintain them.

### Credentials are holder-managed but institutionally revocable

The holder controls their factors day-to-day (add a device, change a password). The operator retains authoritative control over the credential's validity: certificates can be suspended and revoked, accounts locked, and compromised credentials invalidated — because a government digital identity is an identity of record, not merely a preference setting.

### The identity persists across media and services

One person, one identity: credential media may change (card to SIM to app), services may come and go, but the resident identity account remains the stable anchor. Duplicate accounts are treated as problems to resolve, and linking to a relying service can be re-established when broken.

### Phishing resistance is designed in

Because the identity's brand is abused by fraudsters, mature systems publish standing rules — the service will never send login links or QR codes through messaging apps, never ask for codes, and login confirmation always names the destination — and route suspicious-activity reports through official channels.

### Name and evidence consistency matters

Verification rules require that names match across documents (with defined paths for changed names, such as marriage or name-change certificates), and that documents are current within defined limits. These rules exist because the verified identity must match the person's legal records.

## Variants

Common forms of the Type:

- **Web sign-in service** — a central login (and optional verification) service that agencies integrate; identity lives in a web account; verification optional per service requirement.
- **App-first super-credential** — a national identity app combining login (biometrics, passkeys, QR), in-person proving, data sharing, digital signing, notifications, and digital documents; typically serves both government and business relying parties.
- **Smartcard / PKI credential ecosystem** — a government-issued card (and SIM- or app-based companion credentials) with certificates; signing and encryption are as central as authentication; e-services in both public and private sectors consume the credentials.
- **Identity-strength-tiered app** — a mobile app centered on "prove who you are," with named strength tiers and per-service minimums; business representation handled through a linked authorization system.
- **Operation model variants** — fully government-operated, or with delegated components (private operators running one of the credential channels or certificate services under mandate).
- **Scope variants** — government-only relying parties versus including banks and businesses; standalone identity versus bundled with central data-sharing platforms built on top of it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Government Service Portal | adjacent consumer | the portal aggregates services and transactions (catalogues, forms, payments, messages); the digital identity is the identity layer the portal and its services call. Remove service aggregation from a portal and add verification + multi-service presentation → digital identity; the portal without one falls back to per-service accounts. |
| Identity & Access Management / IAM | same mechanism family, different population | IAM governs an organization's workforce access to internal systems. Remove the government mandate, the resident population, and authoritative-evidence verification → enterprise IAM. |
| Customer Identity / CIAM | same mechanism family, different anchoring | CIAM manages customers for one commercial organization. Remove government issuance/mandate and legal anchoring → CIAM. |
| Identity Verification | adjacent capability | a one-shot proofing delivered to a relying business; no persistent holder identity, no credentials, no recurring presentation. Remove the persistent account and the recurring authentication loop → Identity Verification. |
| KYC / KYB Platform | adjacent capability | regulated onboarding proofing bound to compliance case files for financial institutions; same removal test as Identity Verification. |
| Single Sign-on / SSO | mechanism inside the Type | a citizen-facing sign-on service with government anchoring and verification *is* an instance of this Type; generic enterprise SSO lacks the resident-identity verification layer and legal anchoring. |
| Digital Wallet | overlapping features | wallets hold and present documents the user already has; the digital identity establishes and authenticates the identity itself. Digital-document surfaces inside some systems are variants, not the defining core; a pure document wallet is not this Type. |
| Digital Credential Platform | different domain | issues and verifies domain credentials (diplomas, certificates); no population-scale resident identity anchoring. |

The most easily confused pair is **Government Service Portal vs Government Digital Identity**: both face residents across the whole service landscape. The structural difference is that the portal's object is the service catalogue and its transactions, while the identity's objects are the resident's verified identity and its presentation. Real deployments pair them: the portal typically authenticates people *through* the digital identity.

## Representative Products

- **Singpass** (Singapore) — app-first national digital identity: QR and kiosk login, Myinfo data sharing, digital IC, document and transaction signing, serving government and business relying parties.
- **Login.gov** (United States) — central web sign-in service for federal agencies, with authentication-only and identity-verification service levels and a partner integration program.
- **ID.ee / Estonian e-ID** (Estonia) — smartcard-era national e-identity ecosystem (ID-card, Mobile-ID, Smart-ID) with certificates, digital signing, and public-private relying parties.
- **myID** (Australia) — government Digital ID app with Basic/Standard/Strong identity-strength tiers gating participating services.

These four were chosen to span different philosophies (central sign-in service vs app super-credential vs card ecosystem), different eras (2000s smartcard to current apps), and different relying-party scopes. The defining core was checked against the smartcard-era and authentication-only samples to avoid over-fitting the definition to today's app-based pattern.

## Sources

Research date: **2026-09-07**

- Login.gov — Developer Guide: https://developers.login.gov/
- Login.gov — Help Center: https://www.login.gov/help/
- Login.gov — Verify my identity: https://www.login.gov/help/verify-your-identity/overview/
- Singpass — main site: https://www.singpass.gov.sg/main
- Singpass — For Individuals: https://www.singpass.gov.sg/main/individuals/
- ID.ee (Information System Authority, Estonia) — home: https://www.id.ee/en/
- ID.ee — Authentication: https://www.id.ee/en/rubriik/authentication/
- myID (Australian Government) — home: https://www.myid.gov.au/
- myID — How to set up myID: https://www.myid.gov.au/how-to-set-up-myid

> Sourcing limitation: several planned samples could not be reached from the research environment on 2026-09-07 — Singpass developer documentation, GOV.UK One Login, MitID (Denmark), and Aadhaar/UIDAI (India). No claims in this document rely on those systems. Relying-party integration is described from the systems whose integration documentation was reachable. Published scale figures (user, service, and transaction counts) are vendor-published and are not treated as verified facts; no precise numeric limits, time windows, or default settings are asserted beyond what the cited pages directly document.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
