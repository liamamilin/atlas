# Research Notes — Password Manager

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Password Manager actually is as an Application Type: its core objects, its defining workflows, what mature products commonly add, where the Type's boundaries sit (vs MFA, vs Secrets Management, vs IAM/SSO, vs browser built-in password stores, vs digital wallets), and what a reader who has never used one needs to know.

## Initial Boundary

Initial hypothesis before research:

- Core purpose: store account credentials (and other secrets) in an encrypted vault, retrieve them at the point of login, generate strong passwords, and keep the credential population healthy.
- Primary users: individuals; secondarily families and organizations.
- Nearest neighbors: Multi-factor Authentication (TOTP overlap), Secrets Management (developer/infrastructure secrets), IAM/SSO (identity machinery), browser built-in password saving (capability overlap), Digital Wallet (card storage overlap), encrypted notes apps.
- Unknowns going in: how the unlock model is structured across products; how sharing differs between family and enterprise tiers; how passkeys are positioned; whether TOTP storage is definitional or optional; how the local-only pole (KeePass-class) fits the same definition as hosted products.

## Research Questions

1. What is the unit of record? What item types exist beyond username/password?
2. How is the vault protected? What is the unlock model (login vs unlock, master password, key file, biometrics, hardware keys)?
3. How do credentials get into the vault (capture) and out of it (retrieval at point of use)?
4. How does sync / multi-device work, and what does the local-only pole look like?
5. What sharing models exist (family, team, enterprise, ad-hoc links, emergency access)?
6. What does the enterprise admin surface look like (provisioning, collections/shared vaults, policies, SSO, event logs, recovery)?
7. What health/generation machinery is common (generator, breach watch, reports)?
8. How is TOTP/2FA storage positioned — definitional or optional? (MFA pass left a seam here.)
9. How are passkeys positioned?
10. Where are the boundaries vs MFA, Secrets Management, IAM/SSO, browser password stores, wallets?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence tier reached |
|---|---|---|
| Bitwarden | Open-source, free tier, self-hostable, consumer→enterprise; richest help center | Tier 1 (help center articles fetched) |
| KeePassXC | Local-first, offline, open-source desktop pole; no cloud service | Tier 1/2 (official Getting Started guide + site) |
| 1Password | Polished consumer+family+business, hosted cloud | Tier 2 (official product page; support site 403) |
| Keeper | Enterprise-heavy hosted pole (with consumer plans) | Tier 1 (official docs index + end-user guide) |

Dashlane (consumer web-first pole) was attempted twice (support.dashlane.com, dashlane.com/features) — both timed out; abandoned per the network-restriction rule and recorded as a sourcing limitation.

## Sources

- Bitwarden Help Center — https://bitwarden.com/help/ (index), /help/managing-items/, /help/about-organizations/, /help/integrated-authenticator/, /help/understand-log-in-vs-unlock/ — fetched 2026-09-09
- KeePassXC — https://keepassxc.org/ (site), https://keepassxc.org/docs/KeePassXC_GettingStarted.html — fetched 2026-09-09 (User Guide HTML exceeded fetch size limit; Getting Started guide used instead)
- 1Password — https://1password.com/password-manager (product page) — fetched 2026-09-09; https://support.1password.com/explore/ returned 403 (not fetched)
- Keeper — https://docs.keeper.io/ (documentation index), https://docs.keeper.io/user-guides/ — fetched 2026-09-09
- Dashlane — https://support.dashlane.com/hc/en-us and https://www.dashlane.com/features/password-manager — both timed out 2026-09-09 (abandoned)

## Product Observations

### Bitwarden (evidence layer A — directly observed, Tier 1)

- **Item types (5)**: Login (username+password, can also store passkeys and TOTP verification codes), Card, Identity, Secure note, SSH key. Custom fields and file attachments attach to items. (managing-items)
- **Item lifecycle**: edit, archive (excluded from search/autofill, kept in exports), delete → trash (30-day retention, restore or permanent delete), clone (passkey field not copied). (managing-items)
- **Organization structure**: Organizations relate users and vault items for secure sharing; Admin Console for admins (manage items and members, run reporting, configure settings). Collections = shared item containers (items may belong to multiple); Groups = bulk permission assignment. Plan ladder: Free (2 users/2 collections), Families (6 users), Teams, Enterprise (adds SSO + policies). Premium individual unlocks TOTP generation, encrypted attachments, advanced 2FA — but no sharing. Providers = MSP vault-administration entities over multiple organizations. (about-organizations)
- **Enterprise machinery**: member invite/roles/revoke, account recovery administration, SCIM + Directory Connector (LDAP/Entra/Google Workspace/Okta/OneLogin), event logs + SIEM integrations, enterprise policies, SSO (SAML/OIDC, trusted devices, JIT provisioning), client deployment via GPO/Intune, "Deactivate Browser Password Managers Using Device Management". (help index)
- **Login vs unlock (documented distinction)**: Logging in retrieves encrypted vault data and decrypts locally (requires master password / approved device / passkey + any enabled two-step login; requires network). Unlocking works only when already logged in: encrypted data is on disk; unlock can use PIN/biometrics instead of master password; locking deletes decrypted vault data and keys from memory. (understand-log-in-vs-unlock)
- **Integrated authenticator**: TOTP generation inside the vault, attached to login items via an "Authenticator key" field; six-digit codes, SHA-1, 30-second rotation by default with otpauth:// parameter customization; storing keys available to all accounts, generating codes gated to Premium/paid orgs; TOTP autofill and auto-copy; codes available offline while logged in. A separate Bitwarden Authenticator app exists as a distinct product. (integrated-authenticator)
- **Security tools**: username & password generator (+ generator history), vault health reports, change at-risk passwords, master password re-prompt, manage devices. (help index)
- **Autofill**: browser extension (multiple methods incl. on-page-load, copy credentials), iOS/Android autofill, passkey autofill, cards & identities autofill, custom fields, basic-auth prompts, per-site block lists, URI match detection, "Deactivate My Browser's Built-in Password Manager". (help index)
- **Other**: Bitwarden Send (encrypted one-off sharing with lifespan), SSH agent, CLI, API, offline use, self-hosting (Docker/Helm, Key Connector), encrypted exports, import guides from LastPass/1Password/Keeper/Dashlane/browsers/KeePass/Password Safe. (help index)

### KeePassXC (evidence layer A — directly observed, Tier 1/2)

- **Positioning**: "stores and manages your most sensitive information… in an offline, encrypted file that can be stored in any location, including private and public cloud solutions." "No data is stored on remote servers." Cloud-free, ad-free, tracker-free. (site + Getting Started)
- **Unit of record**: the database (KDBX format, KeePass-compatible). "Every piece of information you store in your database is encrypted at all times within the kdbx file. When you are accessing your database from within KeePassXC, your information is decrypted and stored in your computer's memory." (Getting Started)
- **Structure**: entries with user-defined titles/icons, organized in customizable (nestable) groups; parent group settings apply to children; searches and tags as dynamic groups incl. saved searches for expired/weak passwords. (Getting Started)
- **Database creation**: password + optional key file as an additional authentication factor; hardware keys (YubiKey challenge-response) supported; Quick Unlock via biometrics. (Getting Started)
- **Retrieval**: search, copy/paste, Auto-Type into applications ({TOTP}, {TIMEOTP} placeholders), browser integration (KeePassXC-Browser extension for Chrome/Firefox/Edge/Chromium/Vivaldi/Brave/Tor) requiring the database to be unlocked; passkeys via browser integration. (Getting Started + release notes)
- **Generator**: passwords with any character combination or passphrases. (Getting Started)
- **TOTP**: "KeePassXC can calculate TOTP codes like any authenticator app" — with an explicit vendor warning: "Storing TOTP codes in the same database as the password will eliminate the advantages of two-factor authentication. If you desire maximum security, we recommend keeping TOTP codes in a separate database." (Getting Started)
- **Advanced**: database reports (password health, HIBP, statistics), export CSV/XML/HTML, entry history and data restoration, recycle bin (disable-able), field references, attachments + custom attributes, CLI (keepassxc-cli), SSH Agent, FreeDesktop.org Secret Service, KeeShare shared databases (import/export/synchronize), auto-open databases, extra ciphers (Twofish, ChaCha20), import from CSV/1Password/Bitwarden/Proton Pass/KeePass1. (Getting Started)
- **Certification**: ANSSI CSPN security visa (2.7.9). (site)

### 1Password (evidence layer A at positioning level — Tier 2 product page; support site unreachable)

- **Positioning**: "Save and manage login credentials, financial information, and more"; generate passwords, autosave and autofill credentials, share items securely, use on all devices, alerts for weak or compromised credentials. (product page)
- **Item breadth**: "logins, payment cards, bank accounts, identities, documents, and much more" (item-categories link on support site, not fetched). (product page FAQ)
- **Vaults & sharing**: vaults as sharing containers for family members; expiring links for short-term sharing with anyone, including non-users. (product page)
- **Watchtower**: flags compromised passwords and other security issues related to saved items; overall password strength score, passkey availability, 2FA availability. (product page)
- **Security model**: account password + Secret Key dual-layer encryption; "We can't see passwords or sensitive data stored in 1Password"; third-party audits + bug bounty. (product page)
- **Recovery**: Emergency Kit per account; family administrators can recover members' accounts. (product page FAQ)
- **Passkeys**: save and sign in with passkeys. (product page)
- **Enterprise surface** (footer/navigation): Unified Access Platform, Enterprise Password Manager, Credential Broker, Privileged Access, SaaS Manager, Device Trust, Secrets Management, travel mode. (product page navigation)
- **Sourcing limitation**: support.1password.com returned 403 twice (explore page). All 1Password observations are positioning-level from the official product page; operational details (item type list, autofill mechanics, recovery flow specifics) not directly verified.

### Keeper (evidence layer A — directly observed, Tier 1 docs index + end-user guide)

- **Zero-knowledge posture**: "The data stored in a Keeper vault is encrypted and decrypted locally on the user's device"; "Keeper Security employees have no ability to decrypt customer data, because the encryption keys are managed by the customer." (user-guides)
- **Vault account 2FA**: FIDO2 WebAuthn devices, Google/Microsoft Authenticator, SMS. (user-guides)
- **Client surfaces**: Web Vault & Desktop App; KeeperFill browser extensions (Chrome, Firefox, Safari, Edge, Opera) and KeeperFill for Apps; iOS/Android with autofill & passkey setup; Commander CLI. (user-guides)
- **Enterprise end-user setup**: two documented login modes — Master Password Login and SSO Login. (user-guides)
- **Enterprise machinery**: Enterprise Admin guide, KeeperMSP, SSO Connect Cloud (SAML 2.0 IdP) / SSO Connect On-Prem, AD Bridge (AD/LDAP provisioning for users, roles, teams), Forcefield (infostealer protection). (docs index)
- **Product family separation**: Password Manager is one product line; Privileged Access Manager (KeeperPAM: Secrets Manager, Commander, Endpoint Privilege Manager, KeeperDB, Connection Manager) is a separate line — i.e., the vendor itself separates human credential management from infrastructure secrets and privileged access. (docs index)
- **Compliance**: SOC 2, ISO 27001/27017/27018, FedRAMP, StateRAMP. (user-guides)

## Cross-product Comparison

| Structure | Bitwarden | KeePassXC | 1Password | Keeper | Layer |
|---|---|---|---|---|---|
| Encrypted vault as store of record | account vault, encrypted server-side, decrypted locally | KDBX database file, encrypted at all times, decrypted in memory | encrypted vault, dual-layer (password + Secret Key) | vault, zero-knowledge, keys customer-managed | **L0** |
| Credential item as unit of record | Login/Card/Identity/Secure note/SSH key + custom fields + attachments | entries (username/password/URL/notes/attachments) in groups | logins, cards, bank accounts, identities, documents… | records in vault (record types per end-user guides) | **L0** |
| User-held unlock gate; locked by default | login vs unlock; master password / device / passkey; PIN/biometric unlock; lock deletes keys from memory | database password + optional key file + hardware key; Quick Unlock biometrics | account password + Secret Key; Emergency Kit | master password or SSO login; 2FA on the account | **L0** |
| Retrieval at point of use | browser extension autofill, iOS/Android autofill, copy, CLI | Auto-Type, browser extension, copy/paste, CLI | autosave + autofill in browsers and apps, Apple Watch quick access | KeeperFill browser extensions + for Apps, autofill | **L0** |
| Password generator | yes (username + password, history) | yes (passwords + passphrases) | yes | yes (documented in product family; generator standard) | L1 |
| Organization of items | folders, favorites, search, filter | groups (nested), tags, saved searches | vaults, search | folders/subfolders (per end-user guides) | L1 |
| Multi-device sync | cloud sync (or self-hosted server) | none built-in (file stored anywhere; KeeShare sync) | cloud sync across devices | cloud sync | L1 (sync) / L2 (mechanism) |
| Security/health reporting | vault health reports, at-risk password change | database reports (health, HIBP, statistics) | Watchtower | (enterprise reporting; not directly verified) | L1 |
| TOTP storage/generation | integrated authenticator (premium-gated generation) | TOTP storage + generation (with separate-database warning) | MFA codes in items (Apple Watch access) | (2FA codes supported per product family; not directly verified) | L1 |
| Passkeys | storing + autofill | via browser integration (BE/BS flags) | save + sign in | autofill & passkey setup guides | L1 |
| Import/export | extensive import guides + encrypted export | CSV/1Password/Bitwarden/Proton Pass/KeePass1 import; CSV/XML/HTML export | (switch tooling exists; not verified) | (not directly verified) | L1 |
| Trash/restore + item history | 30-day trash, archive | recycle bin, entry history | (not verified) | (not verified) | L1 |
| Sharing containers | organizations → collections; families | KeeShare (import/export/synchronize) | shared vaults (family), expiring links | shared folders (enterprise), teams | L2 |
| Ad-hoc sharing to non-users | Bitwarden Send | — | expiring links | — | L2 |
| Emergency access / recovery | emergency access contacts; admin account recovery | — (file backup is user's own practice) | Emergency Kit; family admin recovery | enterprise account recovery (admin) | L2 |
| Enterprise administration | admin console, SCIM/directory, policies, event logs, SIEM, SSO, deployment | — (no org model) | enterprise line (Unified Access Platform) | admin guide, SSO Connect, AD Bridge, MSP | L2 |
| Self-hosting | Docker/Helm self-host | inherently local (no server) | — | — | L2 |
| Developer surfaces | CLI, API, SSH agent | CLI, SSH agent, Secret Service | CLI | Commander CLI/SDK | L2 |
| Vault-account 2FA | two-step login (multiple methods) | — (no account; database key file/hardware key instead) | (documented on security page; not verified) | FIDO2/authenticator apps/SMS | L2 |
| Vendor-specific | Send, Provider Portal, Key Connector, separate Authenticator app | KDBX compatibility, KeeShare, Secret Service, ANSSI cert | Secret Key, Emergency Kit, travel mode, Watchtower brand | KeeperPAM, Keeper Secrets Manager, KeeperFill brand, Forcefield | L3 |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Four jointly-held structures:

1. **The encrypted vault as the store of record** — a persistent container of secret records, encrypted at rest, decrypted only in use (in device memory while unlocked). Remove → an encrypted archive / backup file, nothing managed.
2. **The credential item as the unit of record** — an individually addressable record binding a service/account to its secret material (password; commonly username, URL, TOTP seed, passkey, notes, attachments). Remove → an encrypted blob with no addressable records.
3. **The user-held unlock gate** — the vault is locked by default; contents are unreadable while locked; opening requires a user-held primary secret (master password, optionally strengthened by key file / hardware key / account key), with convenience unlock methods (PIN/biometrics) layered on an already-authenticated device. Remove → a plaintext credential list.
4. **Retrieval at the point of use** — mechanisms that deliver stored credentials into login/form contexts (autofill, copy, auto-type, CLI get). Remove → a safe-deposit box: storage without the "manager" function.

Jointly-held load-bearing tests:

- 1 alone = encrypted archive
- 2 without 1 = plaintext credential list
- 3 without 1+2 = generic locked container
- 4 without 1–3 = form filler with no store
- 1+2 without 3 = unencrypted credential list
- 1+2+3 without 4 = backup vault, not a manager

### L1 — Common Mature Structure

Present across the sampled products (and the market) but not definitional:

- password/passphrase generator (+ generator history)
- organization of the item population (folders/groups/collections, tags, favorites, search/filter)
- item types beyond logins (cards, identities, secure notes, SSH keys, attachments, custom fields)
- multi-device availability (cloud sync in hosted products; user-managed file placement in local products)
- browser extension + mobile autofill as the dominant retrieval surfaces
- password health / security reporting (weak, reused, compromised; HIBP-class checks)
- TOTP storage and generation attached to login items
- passkey storage and autofill
- import/export (including from competing managers and browsers)
- trash/restore and item history
- sharing containers (family/team shared vaults or collections)
- emergency access / recovery machinery
- vault-account second factors (two-step login on the manager's own account)

### L2 — Variant / Optional Structure

- deployment posture: hosted cloud vs self-hosted server vs local-only file
- sharing depth: family plans, team/enterprise shared containers, ad-hoc expiring links to non-users, emergency/inheritance access
- enterprise administration: admin console, member provisioning (SCIM/directory sync), SSO login for the vault account, enterprise policies, event logs/SIEM export, administered account recovery, managed client deployment
- unlock-method mix: biometrics, PIN, hardware keys (challenge-response), approved devices, passkeys
- developer surfaces: CLI, API, SSH agent, OS secret-service integration
- breach-intelligence integrations (HIBP-class) and at-risk password workflows
- vault-account 2FA method breadth

### L3 — Vendor-specific Structure

- 1Password: Secret Key (additional account key), Emergency Kit, travel mode, Watchtower branding, Unified Access Platform / Credential Broker / SaaS Manager enterprise line
- Bitwarden: Send, Provider Portal (MSP), Key Connector, self-hosting stack, separate Bitwarden Authenticator app, premium gating of TOTP generation
- Keeper: KeeperPAM / Keeper Secrets Manager / Commander / Endpoint Privilege Manager / KeeperDB / Connection Manager product family, KeeperFill branding, Forcefield, KeeperMSP
- KeePassXC: KDBX format compatibility, KeeShare, FreeDesktop Secret Service, ANSSI CSPN certification, extra cipher choices

## Rejected Findings (anti-overfit)

- **Cloud sync is NOT definitional** — KeePassXC is cloud-free by design and stores the vault as a local file; hosted sync is the dominant modern realization, not the invariant.
- **Zero-knowledge *hosting* is NOT definitional as stated** — the invariant is the user-held key over an encrypted vault; in hosted products this is realized as zero-knowledge architecture (documented by Bitwarden, Keeper, 1Password), in local products there is no operator at all. What is invariant: the operator (if any) cannot read the vault without the user's secret.
- **TOTP generation is NOT definitional** — it is an L1 capability attached to items; KeePassXC's own documentation recommends *against* combining TOTP with the password in the same database for maximum security, proving it is a convenience capability, not the Type's center.
- **Browser extension is NOT definitional** — KeePassXC's primary non-browser retrieval is Auto-Type + copy/paste; the extension is the dominant modern surface, not the invariant.
- **Family/team sharing is NOT definitional** — the local pole has no org model at all; sharing is a variant layer.
- **Passkeys are NOT definitional** — a current-market capability layer (all four sampled products now document it, but the historical pole predates it).
- **Specific item-type catalogs are NOT definitional** — the five-type Bitwarden list, KeePassXC's entry model, and 1Password's category list differ; the invariant is the credential item binding a service to secret material, not any specific type taxonomy.
- **Enterprise administration is NOT definitional** — it is the organizational variant layer; the Type stands complete for a single individual.

## Historical / Market-Sample Check

- **Password Safe (1997, Schneier)** and **KeePass (2003)**: local encrypted file of username/password entries, user-held master credential, copy/auto-type retrieval — satisfies all four L0 legs with no cloud, no browser extension, no generator, no TOTP, no passkeys, no sharing.
- **Paper-era analog**: a guarded personal notebook of account credentials (locked drawer) — the conceptual ancestor; satisfies item + gate + retrieval but not durable encryption; the definition should not require software machinery beyond the encrypted-vault realization.
- **Platform-native keychains** (OS/browser password stores): satisfy the same four legs as embedded capabilities — they are the platform-embedded variant of the same structure, not a different structure.
- Conclusion: the L0 holds across eras and poles; the definition names no cloud, no extension, no generator, no TOTP, no passkeys, no org model.

## Boundary Findings

1. **vs Multi-factor Authentication / MFA** (discharges the MFA pass's pre-hung flag): MFA's unit of record is the enrolled factor under a relying organization's control, verified during authentication. A password manager's TOTP capability is a per-item personal convenience: the seed is item data, generated for the user's own use, with no factor lifecycle under a relying organization. KeePassXC's own warning (storing TOTP beside the password reduces 2FA's value) is vendor-acknowledged evidence that the capability is vault convenience, not factor machinery. The interlock runs the other way: MFA products list password managers as protected applications, and password managers document two-step login on their own vault accounts — the password manager is a *consumer* of MFA at its gate and a *holder* of TOTP seeds as item data. Keep-both ratified; seam = org-controlled factor lifecycle + verification step (MFA) vs personal/organizational secret store + retrieval (password manager).
2. **vs Secrets Management / Secrets Security (§14/§15)**: the vendors themselves split the space — Bitwarden ships Secrets Manager as a separate product (projects, machine accounts, access tokens, CI/CD integrations), Keeper ships Keeper Secrets Manager inside KeeperPAM. Seam = who/what consumes the secret: a person at a login/form (password manager) vs machines/pipelines via API/SDK/CLI (secrets manager). Human-facing credential items vs infrastructure secrets.
3. **vs IAM / SSO**: the password manager holds credentials for accounts whose identity lives elsewhere; it has no identity lifecycle, issues no sessions, makes no access decisions. Enterprise SSO integration (Bitwarden SSO login, Keeper SSO Connect) authenticates the *vault account* — integration surface, not identity machinery.
4. **vs browser/OS built-in password stores**: browsers and OSes embed the same four-leg structure as a capability of their own Type (Web Browser / platform). The standalone Password Manager is defined by the vault as a cross-browser, cross-app, cross-device system of record, plus the health/generation/sharing machinery around it. The market treats them as substitutes: Bitwarden documents deactivating browser password managers (individual setting + enterprise device-management deployment). Capability-vs-Type boundary.
5. **vs Digital Wallet**: overlap on card items (Bitwarden Card, 1Password payment cards) — but card items exist for form autofill; the wallet's center is payment transactions and money movement, the password manager's center is authentication credentials.
6. **vs encrypted notes apps**: secure notes are an item type inside the vault; a notes app lacks the credential-item model, point-of-use retrieval, generator, and health machinery.
7. **vs Privileged Access Management**: Keeper's own product family separates Password Manager from KeeperPAM (privileged access, connection management, endpoint privilege). Enterprise password managers may *feed* PAM-adjacent use cases (shared service credentials), but session brokering/vaulting of privileged sessions is another Type.

## Uncertainties

- **1Password operational detail unverified**: support.1password.com 403'd; all 1Password observations are positioning-level from the official product page. Item-type catalog, autofill mechanics, and recovery flow specifics not directly confirmed (mitigated: Bitwarden and Keeper document the same structures, and 1Password's own FAQ names the categories).
- **Dashlane absent**: two timeouts; the consumer web-first pole is unrepresented first-hand. Market-structure claims about consumer products rest on 1Password + Bitwarden + Keeper consumer documentation.
- **Keeper end-user record-type detail**: the docs index and end-user guide confirm vault/records/autofill/2FA/SSO but the fetched pages did not enumerate Keeper's item types; treated as L1-level commonality rather than A-evidence for specific type lists.
- **Exact numeric limits** (attachment sizes, item counts, trash retention beyond Bitwarden's documented 30 days, TOTP parameter defaults beyond Bitwarden's documented defaults) deliberately not asserted in the final document.
- **Market-share claims**: none made; no third-party market data was fetched.

## Final Synthesis

A Password Manager is the personal or organizational **secret store of record**: an encrypted vault whose addressable records bind services/accounts to their secret material, gated by a user-held secret and locked by default, with retrieval machinery that delivers the right secret at the point of use. Everything else — generator, health reports, TOTP, passkeys, sync, sharing, enterprise administration — is the mature market's standard or variant layering on that core. The Type is complete at the individual pole (local file, one person) and extends, without structural change, to families (shared containers) and enterprises (administered containers + provisioning + policy + audit). The defining seams: MFA owns factor verification under org control; Secrets Management owns machine-consumed secrets; IAM/SSO owns identity and sessions; browsers/OSes embed the same structure as a capability rather than a standalone system of record.
