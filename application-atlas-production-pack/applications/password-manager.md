# Password Manager

## Overview

A **Password Manager** is a secret store of record: an encrypted vault whose individually addressable records bind services and accounts to their secret material — above all passwords, and commonly usernames, web addresses, one-time-code seeds, passkeys, secure notes, and file attachments. The vault is locked by default and can only be opened with a secret the user holds, and the application's defining job is to deliver the right secret at the point of use — filling a login form, copying a credential, typing it into an application — so that a person can use a different, strong secret for every account without having to remember any of them.

The defining core is small:

```text
Encrypted vault (store of record)
└── Credential item (service/account ↔ secret material)
    └── User-held unlock gate (locked by default)
        └── Retrieval at the point of use (autofill / copy / auto-type)
```

Everything else commonly associated with the category — password generators, breach alerts, cloud sync, browser extensions, two-factor code generation, family and team sharing, enterprise administration — is standard or optional layering that mature products add. The core stands complete for a single person with a single encrypted file on a single device; it extends, without structural change, to families and enterprises.

## Users & Context

**Individuals** are the primary users. The recurring problem is account proliferation: dozens of services, each wanting its own password, with weak or reused passwords as the practical failure mode. The password manager becomes the one place where credentials are created, stored, and used.

**Families** use shared containers for joint accounts — streaming services, utilities, household administration — and rely on recovery and emergency-access arrangements for the case where one member is locked out or unavailable.

**Teams and organizations** use shared containers for service accounts and shared logins, and add an administrative layer: provisioning and deprovisioning members, enforcing policies, auditing access, and recovering member accounts. In this tier the application is deployed by IT and security teams, often as part of a security program, and competes for the role previously played by spreadsheets and shared documents of credentials.

The dominant point of use is the login form — in a web browser, in a mobile app, occasionally in a desktop application or a terminal. The password manager lives one keystroke away from that moment.

## Core Model

### The Defining Core

**The vault.** A persistent container holding all of the user's secret records. The vault is encrypted at rest — in a hosted product, on the operator's servers in encrypted form; in a local product, as an encrypted file on disk. Decryption happens only in use: while the vault is open, its contents exist decrypted in the device's memory, and locking the vault discards that decrypted state. In hosted products the operator is positioned so that it cannot read vault contents — the encryption keys are derived from or protected by the user's own secret, a posture the industry calls zero knowledge. In local products there is no operator at all.

**The credential item.** The unit of record: an individually addressable record that binds a service or account to its secret material. A login item typically carries the site or app it belongs to, a username, the password, and commonly a one-time-code seed, passkey, notes, custom fields, and file attachments. Beyond logins, mature products define item types for payment cards, identities (addresses and form data), secure notes, and machine credentials such as SSH keys. The item is what the user searches for, opens, edits, shares, and deletes; exact type catalogs vary by product, but the login item is the center of gravity.

**The unlock gate.** The vault is locked by default. Opening it requires a user-held primary secret — conventionally the master password, which is also the root of the vault's key hierarchy. Local products may strengthen the gate with a key file or a hardware security key; hosted products layer account-level factors (a second factor, an approved device, a passkey) on top. Once a device is authenticated, convenience unlock methods — PIN, biometrics — can reopen the vault without re-entering the master password, until the vault locks again. While locked, the contents are unreadable by anyone, including the product's operator.

**Retrieval at the point of use.** The function that makes a store a *manager*: mechanisms that deliver the stored secret into the login moment. The dominant form is autofill — a browser extension or mobile autofill provider that recognizes a login form and offers the matching item. Copy-to-clipboard, global auto-typing into desktop applications, and command-line retrieval serve the same function elsewhere. Matching is typically driven by the site address recorded on the item, and products provide controls to block autofill on specific sites.

Remove any one of the four and the Type collapses into a neighbor: an encrypted archive (no retrieval), a plaintext credential list (no vault or gate), a form filler with no store (no vault), or a backup safe (no retrieval).

### Standard Capabilities Mature Products Add

These are widespread across the market and expected by users, but they are not what makes the product a password manager:

- **Password and passphrase generator** — creates strong random secrets at the moment an account is created or changed; generation history is commonly kept.
- **Organization of the item population** — folders or nested groups, tags, favorites, and search/filter across the vault.
- **Security health reporting** — scans of the item population for weak, reused, old, or breached-appearing passwords (some products integrate breach-data services), with workflows to change at-risk credentials.
- **One-time-code (TOTP) storage and generation** — a seed stored as a field on a login item, with rotating codes generated, autofilled, or copied like any other field. Vendors themselves treat this as a convenience capability; at least one product's documentation explicitly recommends keeping codes in a separate vault when maximum security matters.
- **Passkey storage and autofill** — storing passkey credentials alongside or instead of passwords and filling them at sign-in.
- **Multi-device availability** — hosted products sync the encrypted vault through their service; local products leave the encrypted file for the user to place or synchronize.
- **Import and export** — migration tooling from browsers and competing managers is a standard onboarding path; export (including encrypted export) preserves user ownership of the data.
- **Item lifecycle machinery** — trash/restore with a retention window, item history, archiving, cloning.
- **Sharing containers** — shared vaults, folders, or collections for families and teams; some products add ad-hoc encrypted links for sharing a single item with someone who does not use the product at all.
- **Emergency access and recovery** — designated trusted contacts who can request access, printable recovery kits, and (in organizations) administered account recovery.

### One Structure, Many Implementations

```text
Concept:            Encrypted vault under a user-held secret
Implementations:    hosted zero-knowledge vault, self-hosted server, local encrypted file

Concept:            Primary gate secret
Implementations:    master password; master password + key file; master password + hardware key;
                    account password + additional account key (hosted)

Concept:            Retrieval surface
Implementations:    browser extension autofill, mobile autofill provider, auto-typing into
                    desktop apps, copy-to-clipboard, command-line retrieval

Concept:            Sharing container
Implementations:    shared vault (family), organization collections (team/enterprise),
                    shared folders, ad-hoc expiring links
```

A reader who has only seen one hosted cloud product should still be able to recognize a local-file product — or a platform's built-in keychain — as the same structure.

## How It Works

### Establish the vault and its gate

```text
Create the account or database
→ set the master password (optionally add a key file / hardware key / account key)
→ the vault exists, empty and locked
```

The master password is deliberately the only secret that opens the vault. Products are explicit that losing it can mean losing the vault's contents; recovery arrangements (emergency contacts, recovery kits, administered recovery) exist precisely because the gate is not bypassable by design.

### Capture credentials

```text
Add items manually (new item → type → fields)
or save automatically at login time (the extension or app offers to save
   the credentials just used)
or import in bulk from a browser or a previous password manager
```

Bulk import from browsers and competing products is the standard first-run path; autosave at login is the standard ongoing path.

### Retrieve at the point of use

```text
Arrive at a login form (browser, app, or desktop application)
→ the retrieval surface offers the matching item
→ unlock the vault if locked (master password, or PIN/biometric on an
   already-authenticated device)
→ autofill / copy / auto-type the credentials
→ the vault re-locks after its timeout or on demand
```

This loop — locked vault, unlock, fill, re-lock — is the daily rhythm of the Type. While unlocked, contents exist decrypted only in device memory; locking discards them.

### Maintain the population

```text
Generate a strong secret whenever an account is created or its password changed
→ health reports periodically flag weak / reused / old / breached-appearing items
→ the user updates the affected account and records the new secret
```

The generator and the health reports are two halves of one job: getting the population of secrets into, and keeping it in, a state where each account has its own strong secret.

### Share (families and organizations)

```text
Move or assign items into a shared container (shared vault / collection / folder)
→ grant members or groups access to the container
→ members see shared items alongside personal items in their own vault view
```

Organizations add an administration loop on top: invite and provision members (manually or via directory synchronization), group members, set container permissions, enforce policies (for example, minimum password strength or lock behavior), audit event logs, and recover member accounts. Single items can also be shared ad hoc with non-users through expiring encrypted links in some products.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Vault list

The primary surface: a searchable, filterable list of items, showing titles, usernames, and identifying icons, with quick-copy actions for username/password/code. Primary actions: search, open an item, add an item, organize (folders/groups/favorites).

### Item detail / editor

One credential item's full record: all fields (with reveal/copy controls), custom fields, attachments, one-time-code seed and its rotating code, item history, and sharing state. Primary actions: edit, copy a field, share/move to a container, archive, delete.

### Generator

A surface for creating passwords or passphrases with chosen length and character rules, usually reachable both standalone and inline while editing an item or filling a signup form.

### Security / health dashboard

A report surface over the item population: weak, reused, old, or compromised credentials, missing two-factor codes, and similar findings, each linking to the affected item for remediation.

### Browser extension and in-page autofill

The dominant retrieval surface: an extension icon next to login forms, offering matching items, autosaving new credentials, generating passwords during signup, and holding settings such as per-site autofill blocks.

### Mobile autofill surface

The mobile operating system's autofill provider integration: the vault offers matching credentials (and one-time codes and passkeys) to any app's login screen.

### Settings

Unlock methods (biometrics, PIN), vault timeout behavior, autofill behavior, import/export, and account security (master password change, second factors, device management).

### Admin console (organizational variant)

Administrators' surface: members and groups, shared containers and their permissions, policies, event logs and reporting, account recovery administration, and provisioning integrations.

## Important Rules / Behaviors

- **Locked by default; decrypted only in use.** The vault's contents are unreadable while locked — including, by design, to the product's operator in hosted products. Locking discards decrypted keys and data from memory. A configurable timeout re-locks the vault automatically.
- **Login and unlock are distinct acts** (documented explicitly by at least one product, and structurally present in others): *logging in* authenticates the account and retrieves/decrypts the vault (requires the primary secret and network, plus any account-level second factor); *unlocking* reopens an already-retrieved vault on the device (works offline, and may use PIN/biometrics instead of the master password).
- **The master password is the root of trust and is not recoverable by the operator.** Losing it can mean permanent loss of vault contents; this is why recovery machinery (emergency contacts, recovery kits, administered recovery) is a first-class surface rather than an afterthought.
- **Autofill matching is address-driven and controllable.** Items carry the site/app they belong to; matching rules determine what is offered where, and users can block autofill on specific sites. Mismatched or overly loose matching is a known risk area products document and tune.
- **Sharing moves items into containers with their own access rules.** In organizational products, assigning an item to a shared container transfers its ownership to the organization; per-container permissions decide who can use, edit, or manage it.
- **Deletion is recoverable for a bounded period.** Deleted items go to a trash/recycle area with a retention window before permanent deletion; item history preserves prior versions in some products.
- **One-time codes stored beside passwords are a documented trade-off.** Products support TOTP seeds as item fields for convenience; vendor documentation itself notes that combining the code with the password in one vault reduces the protection two-factor authentication provides, and recommends separate storage where maximum security matters.
- **The vault account itself is commonly second-factor protected.** Hosted products offer two-step login on the manager's own account — the password manager is a consumer of multi-factor authentication at its own gate.

## Variants

- **Hosted consumer/family vaults** — the dominant market form: cloud-synced encrypted vaults, individual and family plans, sharing containers for households.
- **Local-first offline vaults** — an encrypted file the user stores and backs up themselves; no operator, no hosted sync; retrieval via auto-typing, clipboard, and an optional browser extension that talks to the local application.
- **Self-hosted** — the hosted model operated on the customer's own infrastructure; the vault service runs where the customer controls it.
- **Enterprise deployments** — the organizational variant: SSO-based login for the vault account, directory-driven provisioning, policy enforcement, event logging and security-tool integrations, administered recovery, and managed rollout of client apps (including centrally deactivating browsers' built-in password saving).
- **Platform-embedded stores** — operating-system keychains and browser built-in password saving realize the same structure as a capability of another product; they are the platform-embedded variant rather than standalone systems of record (see Related Application Types).
- **Developer-oriented extensions** — command-line interfaces, SSH-agent service, and APIs that let scripts and developer tools retrieve credentials from the same vault.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Multi-factor Authentication / MFA | owns the enrolled factor and the verification step during sign-in, under a relying organization's control; a password manager's one-time-code capability is per-item personal convenience with no factor lifecycle — and the password manager itself consumes MFA to protect its own gate |
| Secrets Management / Secrets Security | serves machine-consumed secrets (API keys, tokens, infrastructure credentials) retrieved by pipelines and services via API/SDK; the password manager serves person-at-a-login retrieval — vendors ship them as separate products |
| Identity & Access Management / IAM; Single Sign-on / SSO | own identity lifecycle, sessions, and access decisions; a password manager holds credentials for accounts whose identity lives elsewhere and makes no access decisions — enterprise SSO integration merely authenticates the vault account |
| Web Browser (built-in password saving) | embeds the same store-fill structure as one capability of the browser, scoped to that browser's profile; the standalone Type is a cross-browser, cross-app, cross-device system of record with health/generation/sharing machinery — the market treats them as substitutes, and password managers document deactivating the browser's built-in saving |
| Digital Wallet | centers on payment transactions and money movement; card entries in a password manager exist for form autofill, not payment processing |
| Note-taking Application (encrypted notes) | secure notes are one item type inside the vault; a notes app lacks the credential-item model, point-of-use retrieval, generator, and health machinery |
| Privileged Access Management / PAM | brokers and vaults privileged sessions and just-in-time elevated access for infrastructure; enterprise password managers may hold shared service credentials but do not manage privileged session brokering |

The closest structural neighbor is the browser's built-in password saving — same four-part structure, different scope and standing. The closest *confusable* neighbor is MFA, because of the one-time-code overlap; the org-control test separates them cleanly.

## Representative Products

- **Bitwarden** — open-source hosted manager with a free tier, self-hosting option, and a full organizational tier (collections, policies, SSO, event logs)
- **KeePassXC** — local-first, offline, open-source desktop manager (encrypted database file, no hosted service)
- **1Password** — hosted consumer/family/business manager (dual-key account model, security dashboard, family sharing)
- **Keeper** — enterprise-leaning hosted manager (zero-knowledge vault, SSO and directory integration, MSP administration)

The defining core was checked against the local-only pole (KeePassXC), the self-hostable pole (Bitwarden), and the enterprise pole (Keeper), and against the historical generation of local encrypted-file managers, to avoid defining the Type by today's hosted cloud pattern.

## Sources

Research date: **2026-09-09**

- Bitwarden Help Center — https://bitwarden.com/help/ (incl. Vault Items, Organizations Overview, Integrated Authenticator, Understand Log in vs. Unlock)
- KeePassXC — https://keepassxc.org/ and https://keepassxc.org/docs/KeePassXC_GettingStarted.html
- 1Password — https://1password.com/password-manager (product page)
- Keeper — https://docs.keeper.io/ and https://docs.keeper.io/user-guides/

> Sourcing limitations: 1Password's support site (support.1password.com) was not reachable (403); 1Password observations rest on its official product page at positioning level. Dashlane was not reachable (repeated timeouts) and is absent from the sample. Precise operational figures (numeric limits, retention windows beyond those directly documented, default settings) are intentionally not asserted; where a specific figure appears it is traceable to a fetched official page recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
