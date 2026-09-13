# Research Notes — Digital Asset Custody Platform

Research date: 2026-09-08
Directory leaf: Digital Asset Custody Platform (§08 Finance, Banking, Insurance & Investment)
Slug: digital-asset-custody-platform

---

## Research Goal

Understand, from real products, what an institutional digital asset custody platform actually is: its core objects, its security model as seen by users, how assets enter and leave, what governance machinery surrounds movement, and where its boundary sits against consumer crypto wallets, exchanges, and generic key management.

---

## Initial Boundary (hypothesis before research)

- Hypothesized core use: institutions (exchanges, funds, corporate treasuries, custodian businesses) safeguarding digital assets under organizational control, with governed movement rather than single-person control.
- Hypothesized users: custody/treasury operations staff, approvers, compliance, auditors; plus end clients in B2B2X arrangements.
- Nearest neighbor types: Crypto Wallet (consumer, personal), Cryptocurrency Exchange (trading), Encryption & Key Management / Secrets Management (generic KMS), AML Platform (screening), DeFi Portfolio Application (read-only tracking), Fund Administration (accounting without control).
- Suspected confusion: "custody" is used both for custodian-held (third-party) arrangements and for self-custody infrastructure; products in this leaf span both postures.

---

## Research Questions

1. What objects compose the custody world (account / vault / wallet / address / asset / transaction / key / policy)?
2. How do assets enter (deposits) and exit (withdrawals / transfers)? What controls each direction?
3. Who holds the key material and who can move assets — custodian, customer, or a split?
4. What governance machinery exists (roles, quorums, policies, destination allowlists, audit)?
5. What records and reports does the platform maintain (balances, statements, transaction history)?
6. Where do adjacent services (trading, staking, settlement, fiat, tokenization) attach, and what stays custody-core?
7. What distinguishes this Type from Crypto Wallet / Cryptocurrency Exchange / generic KMS?
8. How do regulatory postures (qualified custodian vs self-custody infrastructure) shape the product?

---

## Representative Products

| Product | Posture (as documented) | Customer level | Evidence tier reached |
|---|---|---|---|
| Fireblocks | self-custody infrastructure ("direct custody is a type of self-custody"), MPC | institutions building on the platform; treasuries | Tier 1 (developer docs, multiple pages fetched) |
| Anchorage Digital | custodian-operated platform; quorum + custodian co-approval; HSM; USD banking | institutions; B2B2X servicers | Tier 1 (knowledge base, multiple pages fetched) |
| BitGo | full spectrum: regulated custodian cold custody → self-custody hot wallets; multisig + MPC | enterprises, exchanges, retail-facing businesses | Tier 1 (developer portal, multiple pages fetched) |
| Copper | qualified custody + off-exchange settlement network (ClearLoop) + collateral management | institutions | Tier 2 (marketing site only) |

Intended fifth sample Coinbase Custody was dropped: two fetch attempts (coinbase.com/custody, docs.cdp.coinbase.com/prime) timed out. Per source-access rules the vendor was abandoned rather than reconstructed from memory.

---

## Sources

Fetched 2026-09-08 (all Layer A unless noted):

Fireblocks (developers.fireblocks.com):
- Docs index + quickstart: https://docs.fireblocks.com/docs/quickstart ; https://developers.fireblocks.com/llms.txt ; https://developers.fireblocks.com/_llms/guides.md
- What Is Fireblocks: https://developers.fireblocks.com/docs/what-is-fireblocks.md
- Object Model: https://developers.fireblocks.com/docs/object-model.md

Anchorage Digital (docs.anchorage.com):
- Index: https://docs.anchorage.com/llms.txt ; https://docs.anchorage.com/_llms/anchorage-digital.md
- What is Anchorage Digital: https://docs.anchorage.com/knowledge-base/platform/users/overview.md
- Security architecture: https://docs.anchorage.com/knowledge-base/platform/users/security.md
- Account hierarchy: https://docs.anchorage.com/knowledge-base/platform/users/account-hierarchy.md
- Policies overview: https://docs.anchorage.com/knowledge-base/platform/users/policies.md

BitGo (developers.bitgo.com):
- Guide index: https://developers.bitgo.com/llms.txt
- Introduction: https://developers.bitgo.com/docs/get-started-intro
- Wallet Types: https://developers.bitgo.com/docs/wallet-types
- Policies Overview: https://developers.bitgo.com/docs/policies-overview
- Custody Starter Architecture: https://developers.bitgo.com/docs/custody-starter-architecture-overview

Copper (Layer B / positioning only):
- https://www.copper.co/ (root marketing site)

Anchorage index page summaries (guide titles/descriptions inside _llms index) were used as Layer A evidence for capability existence (e.g., trusted destinations, travel rule, reporting, staking), with operational detail kept at correspondingly reduced strength.

---

## Product A — Fireblocks

### Key observations (Layer A unless noted)

Positioning (docs/what-is-fireblocks):
- "a user-friendly platform that uses direct custody to build new blockchain-based products and manage your digital asset operations. Direct custody is a type of self-custody… you're always the owner and controller of your assets."
- Explicitly NOT custodian-held: zero counterparty risk framing; customer owns and controls assets; the platform is key-control and operations infrastructure.
- Three declared components: Digital Asset Wallets (MPC-CMP; "never gathering a private key as one whole"), Platform Governance (Policy Engine), Treasury Management (vault accounts + Fireblocks Network).

Object model (docs/object-model):
- Workspace = unique platform instance (deployment unit).
- Vault account = security boundary; holds asset wallets; structure can be Segregated (per-user vault accounts) or Omnibus (centralized vaults, funds swept for single withdrawal).
- Asset wallet = per-asset container managing deposit addresses (≥1; multiple on UTXO chains).
- Connected accounts = customer's own exchange API credentials wired into the workspace; Fiat accounts = fiat provider credentials.
- Whitelisted addresses ("unmanaged wallets" in API) = external destinations, typed internal / external / contract wallet.

Security model:
- MPC key shares distributed across multiple cloud environments (or on-prem / hybrid).
- Intel SGX secure enclaves protect key shares and API keys.
- Policy Engine rules decide block / approve / require additional signers using filters: source, destination, asset, amount; destinations include internal wallets, network connections, exchanges, fiat providers, whitelisted addresses, contract wallets.
- Policy Engine itself runs inside SGX; rules signed by a quorum of admins.
- Admin Quorum required for whitelisting, network connections, exchange accounts, new users, workspace configuration changes.
- 2FA minimum for all users; all workspace activity (admin changes + transactions) logged, viewable in console, exportable to SIEM.

Movement:
- Deposits: per-asset confirmation policies; deposit validation; sweep funds to omnibus; associating end clients with transactions.
- Withdrawals: whitelisted addresses as the flow; fee estimation endpoints; Gas Station (auto-fueled gas wallets).
- Transaction status monitoring; webhooks for deposit/withdrawal/status events.
- Raw signing + typed message signing (offchain signing surface).
- API co-signers: customer-hosted signing agents (SGX / AWS Nitro / GCP Confidential Space) as an additional approver layer.

Adjacent services:
- Fireblocks Network: peer-to-peer institutional transfer network; authenticated deposit addresses (removes address copy/paste + test transfers); connections to 30+ exchanges and fiat providers (marketing figure — count not load-bearing).
- Smart Transfers (workflow-based multi-account transfers); Off Exchange (assets remain in custody while trading on connected venues).
- Staking; AML screening integrations (Chainalysis, Elliptic); Travel Rule (TRUST, Notabene); tokenization (ERC20F etc.); workspace users via console or API; no client PII stored (customers map anonymized tokens).

### Level classification
- A-evidence for: workspace/vault/asset-wallet/address model, MPC split, Policy Engine semantics, admin quorum, whitelisting, omnibus vs segregated, deposits/withdrawals machinery, audit logs, exchange/fiat connectivity, staking, AML/travel-rule hooks.
- Marketing-layer only (Tier 2): "$3T transferred", network participant counts.

---

## Product B — Anchorage Digital

### Key observations (Layer A unless noted)

Positioning (users/overview):
- "institutional digital asset platform"; declared pillars: Custody, Trading (RFQ), Staking and governance, Settlement (Atlas — settle directly from custody, "no pre-funding an exchange, no moving assets out to settle").

Account hierarchy (users/account-hierarchy):
- Organization → Accounts (own legal entity, division, or end customer under B2B2B/B2B2C; FBO and omnibus structures documented in developers section) → Vaults (organize wallets; carry policy; hold single or multiple assets) → Wallets (per asset; provide deposit addresses; default wallet used for external withdrawals / trade settlement / API holds; one USD wallet per vault) → Addresses.
- Account-based chains: one address shared by all tokens on the network; UTXO chains: multiple addresses pooled to the wallet, change addresses auto-generated.
- Balances: Available (withdrawable now, excludes holds/pending/locked) vs Total (includes pending, locked-for-voting, in-transition).

Security model (users/security):
- No usernames/passwords, no email/SMS recovery; only pre-approved devices.
- 3-step transaction flow: (1) multi-user approval — every transaction needs approval from at least two organization members via authorized devices; each user's identity is a cryptographic key in the iOS Secure Enclave; biometrics bind approval to a specific human on a specific device. (2) Transaction review — Anchorage itself reviews every transaction: automated outlier detection + behavioral analytics + human oversight; "no transaction moves forward without human confirmation". (3) Hardware-enforced logic — air-gapped HSMs sign only when the operation carries a valid quorum of client approvals plus Anchorage approval; key material never exported in plaintext.
- "Why HSMs": tamper-resistant hardware; signing returns only the signature; physical tamper destroys keys.

Permissions:
- Three permission levels: Administrator (org-level: edit policies, add/remove users, create vault, add/remove trusted destinations, provision API keys), Operator (vault-level: deposit & withdraw, staking), Viewer (view balances, download statements). Same user can be Operator in one vault, Viewer in another.
- Vault constraints: minimum 3 vault members; minimum quorum 2 approvers; sub-quorums per operation type (withdrawal / staking / governance). (Product-specific numbers — do not generalize.)

Policies (users/policies):
- Admin policy (org-wide operations, e.g., inviting users) + vault policies (asset operations, e.g., withdrawals).
- Rule = trigger → who must approve + how many approvals; after quorum met, Anchorage performs final review.
- Conditional rules (fewer approvals for trusted destinations; amount thresholds) documented as in development, not GA.

Movement:
- Deposits: deposit attribution, trusted sources, address-poisoning protection (from index summaries + developers move-money docs).
- Withdrawals: require quorum approval per request; trusted destinations = pre-approved withdrawal addresses (crypto addresses and USD bank recipients); AML questionnaire payload required on every external transfer/withdrawal; Travel Rule compliance; compliance RFIs.
- Transfers vs withdrawals: two approval models — transfers (between wallets / to external address without per-transaction quorum) vs withdrawals (quorum every request).
- Gas station per wallet; stuck-transaction handling; operation status tracking (polling or webhooks).

Records & reports:
- Statements; balance and transaction report downloads; tax documents; cost basis / tax lots; invoices; operations tab with tags and tag-filtered reports.

Adjacent services:
- USD banking (wire instructions, deposits/withdrawals, interest program, B2B2X account structures) — bank-side capability directly documented.
- Staking across a long asset list (index); stablecoin mint/redeem/bridge; on-chain interactions (bridge; Web3 via Chrome extension / WalletConnect); trading RFQ; Atlas settlement API (propose/accept/authorize/monitor; collateral management).
- Developers: API keys with permission groups; Ed25519 request signing for sensitive operations; sandbox; webhooks.

### Level classification
- A-evidence for: hierarchy, permission matrix, quorum/sub-quorum model, dual approval (client quorum + custodian review), HSM posture, trusted destinations, transfer/withdrawal distinction, reporting/tax, USD banking, Atlas.
- Not verified in fetched docs: specific regulatory charter (e.g., OCC federal charter) — kept out of canonical claims; USD banking documented without charter attribution.
- Product-specific numbers (min 3 members, quorum 2, iOS-only flows) stay in these notes.

---

## Product C — BitGo

### Key observations (Layer A unless noted)

Positioning (get-started-intro):
- "a robust and highly configurable platform of REST APIs"; securely Transact / Hold (multisig and MPC wallets, incl. NFTs) / Protect (customizable policies) / Trade / Stake.

Account & wallet structure:
- Enterprise = customer container; unlimited number of segregated wallets per asset; unlimited receive addresses where supported.
- Wallet types table: Custody (Multisig Cold, MPC Cold — no custody hot) vs Self-Custody (Multisig Hot/Cold, MPC Hot/Cold); support varies by asset.
- All on-chain wallets use 2-of-3 keys: user key, backup key, BitGo key. Key custody table: custody wallets → all three keys created by BitGo; self-custody/offline-vault wallets → user and backup keys created by the customer, BitGo key by BitGo.
- Signature schemes: multisignature (on-chain; pioneered by BitGo in 2013 — heritage claim from docs) vs MPC/TSS (off-chain key shares; full private key never assembled; shares shardable up to 99 — product-specific figure).
- Special types: Go Account (omnibus custody cold wallet with off-chain ledger, single key, fiat included, one per enterprise; powers Go Network trades/settlements); Lightning custody wallets; Advanced Wallets (self-custody hot wallets with HSM-managed keys in a secure subnet).

Custody signing flow (wallet-types, custody section):
- Custody wallets are cold; users initiate transactions via API or web app; users never sign.
- Flow: BitGo signs with the user key after video ID verification with a BitGo Bank & Trust operator → a different BitGo Bank & Trust operator downloads and signs in the Offline Vault Console (OVC) with the BitGo key → upload and broadcast.
- 24-hour SLA for on-chain withdrawals from custody wallets (product-specific); policies can remove video-verification requirements under defined conditions.
- Testnet custody transactions remain unsigned (protocol enforcement).

Custody starter architecture (custody-starter-architecture-overview):
- Recommended three-wallet pattern per coin: Custody wallet (cold, majority of assets, strictest policies) → Standby wallet (self-custody buffer) → Deposit/Withdraw wallet (daily operations, smallest balance, fewest policies).
- Whitelists govern movement between the three; fund flow: deposits land on hot wallet → accumulate → sweep to standby → sweep to custody; withdrawals paid from hot wallet; replenishment chains upward.
- Stated security benefits: limited exposure, layered approvals, whitelist restrictions, audit trail.

Policies (policies-overview):
- Rule types: Destination, Initiator, Percentage of Wallet Balance, Threshold, Velocity Limit (time window), Webhook.
- Policy rules apply to transactions involving BitGo; recovery via user key + backup key bypasses policies (documented escape hatch).

Other machinery:
- Whitelists/blacklists; wallet freeze; add/remove wallet users with permissions (removal may need multiple admin approvals); webhooks (wallet / enterprise / block); staking for custody / self-custody / Go Accounts; proof of reserves; Off-Exchange Settlement (client allocates assets to partner venues, deallocate, settle, disputes); Travel Rule with address whitelisting + originator PII; KYC/KYB flows; gas tanks; transaction acceleration (RBF / CPFP); nonce-hole resolution; token enablement; bulk ERC-20 withdrawals; mint/burn stablecoins; real-world-asset tokenization.

### Level classification
- A-evidence for: enterprise→wallet hierarchy, 2-of-3 key scheme (multisig + MPC as alternative implementations), custody vs self-custody postures, operator signing flow, tiered wallet architecture, policy rule types, whitelists, Go Account omnibus off-chain ledger, OES.
- Product-specific: video-verification step, OVC, 24h SLA, 99x sharding, named wallet types.

---

## Product D — Copper (positioning only; Layer B)

### Key observations (Tier 2 marketing site; reduced strength)

- Positions custody together with trading, settlement, and collateral management: "bringing custody, trading, settlement and collateral management together".
- Named capabilities: Qualified Custody; Vaults; Staking; Collateral Management; Financing; Trading & Settlement; ClearLoop Network (off-exchange settlement / "protected collateral" — assets stay at Copper while trading on connected venues); Copper Network (counterparty connectivity).
- Institutional framing throughout; US custody offered through Copper Markets (US), Inc., an SEC-registered broker-dealer / FINRA member (from site legal footer); SOC2 / ISO badges displayed.
- Internal operating model (policies, quorums, key architecture) NOT verifiable from reachable sources; treated as variant breadth only: qualified-custodian posture + off-exchange settlement as a first-class pattern.

---

## Cross-product Comparison

| Dimension | Fireblocks | Anchorage Digital | BitGo | Copper |
|---|---|---|---|---|
| Deployment container | Workspace | Organization → Accounts | Enterprise | (not verified) |
| Holding structure | Vault account (segregated or omnibus) → asset wallet → addresses | Account → Vault → Wallet → addresses | Enterprise → wallets (segregated) + Go Account (omnibus, off-chain ledger) | Vaults (named capability) |
| Who controls keys | customer + platform hold MPC shares; "direct custody is a type of self-custody" | custodian holds key material in air-gapped HSMs; movement needs client quorum + custodian approval | spectrum: custodian-held (custody wallets) or customer-held user+backup keys (self-custody) | custodian (qualified custody; internals not verified) |
| No unilateral movement enforced by | Policy Engine (block/approve/add signers) + Admin Quorum | quorum ≥2 org members + custodian review + HSM-enforced quorum check | 2-of-3 signatures + policy rules (approval, velocity, threshold, destination) | (not verified) |
| Destination controls | whitelisted addresses (internal/external/contract) | trusted destinations (crypto + USD bank recipients) | whitelists/blacklists per wallet & enterprise | (not verified) |
| Deposit machinery | confirmation policies, sweeps, end-client association, balance validation | deposit attribution, trusted sources, address-poisoning protection | receive addresses, deposit assets flow | (not verified) |
| Approval surface | web console + API (+ co-signers) | iOS app (biometric, Secure Enclave) + web + API | web app + API (+ OVC offline console for cold) | (not verified) |
| Records | audit logs → SIEM export; transaction history | statements, balance/transaction reports, tax docs, cost basis | transaction records, webhooks, proof of reserves | (not verified) |
| Fiat rail | fiat provider accounts (customer's own credentials) | USD wallets, wire, interest program | Go Account fiat, fiat withdrawals (CaaS) | (not verified) |
| Trading/settlement adjacency | connected exchange accounts; Fireblocks Network; Off Exchange; Smart Transfers | RFQ trading; Atlas settlement from custody | funded/margin trading; Go Network; OES | ClearLoop off-exchange settlement |
| Staking | yes | yes (long asset list; governance) | yes (all wallet types) | yes |
| Compliance hooks | AML integrations, Travel Rule | AML questionnaire per transfer, Travel Rule, RFIs | Travel Rule, KYC/KYB | (not verified) |

### What is present in ALL sampled products (A or strong B)
1. A hierarchical custody holding structure ending in per-asset wallets with deposit addresses and balances.
2. Cryptographic key control organized so that no single actor moves assets unilaterally — implemented as MPC key shares + policy engine (Fireblocks), client quorum + custodian HSM approval (Anchorage), 2-of-3 keys + policy rules (BitGo). The shared abstraction: platform-mediated multi-party key control.
3. Governed movement: initiation → policy/quorum evaluation → (custodian/platform participation in signing) → broadcast → durable transaction record.
4. Destination controls on outbound movement (whitelists / trusted destinations) in all products where the operating model is documented.
5. Organizational operation: roles, admin quorums for configuration changes, segregation of duties, audit/logging.
6. API + web console as standard surfaces; webhooks; staking; exchange connectivity or trading adjacency; deposit machinery with confirmation semantics.

### Where sampled products differ (implementation or variant, not definition)
- Custody posture: custodian-held vs customer-held key splits; "custody" as a legal posture (qualified custodian) vs a technological one (self-custody infrastructure).
- Cold/hot tiering: explicit cold wallets (BitGo custody, Anchorage air-gapped HSMs) vs warm/hot MPC-centric operation (Fireblocks); BitGo documents a three-tier wallet architecture as a recommended pattern.
- Omnibus vs segregated client structures; off-chain omnibus ledgers (BitGo Go Account, Anchorage FBO/omnibus docs) vs fully on-chain segregated wallets.
- Regulatory anchoring: regulated custodian entities (BitGo Bank & Trust operator signing; Anchorage USD banking; Copper US broker-dealer) vs non-custodial infrastructure vendor (Fireblocks explicitly "self-custody, zero counterparty risk").
- Approval surfaces: mobile biometric approvals (Anchorage) vs web/API (Fireblocks, BitGo).

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Three jointly-held structures; removing any one collapses the Type:

1. **Custodial holdings of record** — the platform maintains the authoritative, persistent record of digital assets held under its safekeeping: an organized holding structure (accounts/vaults/wallets per asset) with deposit-address machinery and per-asset balances that credit deposits.
   - remove → portfolio/valuation or accounting tool; nothing is "held".

2. **Platform-mediated key control over those assets** — movement of the assets is controlled by cryptographic key material that the platform's security model manages (custodian-held, customer-held, or split across parties) such that asset movement always runs through the platform's key machinery and no single person can move assets unilaterally.
   - remove → generic key management / secrets store, or a plain consumer wallet; the platform no longer controls anything of value.

3. **Governed asset movement** — deposits and outbound transfers/withdrawals are executed as platform-mediated transactions subject to the operating organization's authorization model (roles, approval quorums, policy rules, destination controls), with the platform or custodian participating in signing and every movement durably recorded.
   - remove → cold storage locker with no operations, or a payments workflow with no assets.

Jointly-held is load-bearing:
- 1 alone = balance reporting / fund accounting.
- 2 alone = KMS / MPC toolkit.
- 3 alone = approval-workflow engine.
- 1+2 without 3 = vault with no operational loop.
- 1+3 without 2 = accounting with no actual asset control.
- 2+3 without 1 = signing middleware with nothing of record.

Domain anchor: digital (on-chain bearer) assets — control equals key control; transfer irreversibility shapes every rule. The Type is the institutional safekeeping-and-movement system for this asset class.

### §24 historical / market-sample check

- Early-generation model (segregated client accounts in deep cold storage under a trust company, withdrawal approvals + address whitelists, periodic statements) satisfies all three legs — no MPC, no HSM enforcement, no mobile app required.
- Platform-native exchange custody (exchange operating client custody with omnibus on-chain wallets + off-chain client ledgers) satisfies — matches the Go Account / omnibus pattern.
- Regional regulated custodians (EU / Japan regimes) satisfy at the abstract level — regime specifics are variant, not definition.
- Pre-digital conceptual ancestor: a trust company's vault for bearer instruments — holdings ledger + dual-control withdrawals — satisfies the abstract shape; this Type is its digital-asset instantiation where "possession" is key material.
- Conclusion: L0 must not include MPC, HSM, mobile approvals, blockchain-specific signature schemes, or any specific quorum numbers — all are era/current-market implementations.

### L1 — Common Mature Structure (very common, not definitional)

- Cold/hot (or tiered) storage posture and rebalancing sweeps between tiers.
- Role model: administrator / operator / viewer-class separation; admin quorum for configuration changes.
- Whitelist / trusted-destination management as a named surface.
- Transaction lifecycle tracking with user-visible states; webhooks/notifications.
- Deposit machinery depth: confirmation policies, deposit attribution, address-poisoning protections.
- Audit logging / export; statements and balance/transaction reports; tax/cost-basis reporting (depth varies).
- Gas/fee management; transaction acceleration.
- Staking; exchange account connectivity; AML screening / Travel Rule hooks; recovery and key-shard escrow machinery.
- B2B2X structures for serving end clients (segregated / omnibus / FBO), sometimes with off-chain ledgers.

### L2 — Variant / Optional

- Custody posture: custodian-held keys (qualified custody) ↔ self-custody infrastructure ↔ hybrid MPC splits.
- Regulatory anchoring: trust/bank/broker-dealer entities vs non-custodial vendor posture; regional regimes.
- Client structure: segregated vs omnibus; on-chain vs off-chain client ledgers.
- Off-exchange settlement networks as a first-class pattern.
- Fiat rails attached to custody (USD wallets, wire, interest).
- Trading depth: none / RFQ / full trading stack.
- Approval surfaces: web/API only vs mobile biometric approvals.
- Scope additions: tokenization, stablecoin mint/burn, collateral management, NFTs.

### L3 — Vendor-specific (research notes only)

- Fireblocks: MPC-CMP branding; SGX-hosted Policy Engine; Admin Quorum terminology; Fireblocks Network; Smart Transfers; Gas Station; API co-signers (SGX/Nitro/Confidential Space); workspace PII-anonymization policy.
- BitGo: OVC (Offline Vault Console); video-ID-verified operator signing; 24h custody withdrawal SLA; Go Account / Go Network; custody starter architecture as a named pattern; 99x key-share sharding; RBF/CPFP acceleration; proof of reserves; custodial Lightning wallets.
- Anchorage: iOS Secure Enclave identity + biometric approvals; behavioral-analytics transaction review; three-step transaction process framing; Atlas settlement; Porto; minimum 3 vault members / quorum 2; sub-quorum per operation type; tax center / cost-basis workflows.
- Copper: ClearLoop; collateral mobility framing; specific volume figures (marketing).

---

## Vendor-specific Findings (explicit list)

See L3 above. None of these enter the canonical document except as neutral, de-branded variants (e.g., "mobile approval app", "off-exchange settlement network", "omnibus off-chain ledger").

---

## Boundary Findings

**vs Crypto Wallet** — the closest boundary. A consumer wallet: individual's own keys, single-user control, no organizational governance, no client structures, no policy engine, no statements. Two distinguishing tests:
1. Remove the organizational governance machinery (roles, quorums, policies, audit) and what remains is a wallet.
2. An on-chain multisig wallet (N-of-M) provides on-chain quorum but is a wallet *primitive*: it lacks the platform's holdings-of-record layer, policy engine, deposit machinery, destination book, and reporting. Custody platforms wrap or replace such primitives with an operational system around them.

**vs Cryptocurrency Exchange** — exchange centers on trading/marketplace; custody centers on safekeeping + governed movement. The boundary blurs by design: exchanges embed custody services; custody platforms embed trading/settlement (RFQ, OES, ClearLoop). The distinguishing question is what the record of value is anchored to: order books and trading accounts (exchange) vs custody holdings with controlled movement (this Type). Off-exchange settlement exists precisely to keep the custody anchor while trading elsewhere.

**vs Encryption & Key Management / Secrets Management** — generic KMS treats keys as opaque secrets for IT systems; no asset-bearing structure, no financial governance (quorums, destination allowlists, client segregation), no statements. Custody's key machinery is inseparable from the assets it controls and the governance that surrounds movement. Remove asset-bearing + governance → KMS.

**vs AML Platform / Transaction Monitoring** — screening appears inside custody platforms as policy hooks (send/receive checks, travel-rule payloads) but the monitoring platforms are separate Types; custody embeds, monitoring specializes.

**vs DeFi Portfolio Application / Portfolio Management System** — read-only aggregation/tracking vs actual key control and movement execution.

**vs Fund Administration / Investment Fund Accounting** — accounting of holdings without controlling keys; custody platforms feed such systems but do not perform fund-level NAV accounting as their core.

**"Remove what → another Type" tests**
- Remove key control → accounting / reporting tool (Fund Administration territory).
- Remove governance → consumer Crypto Wallet.
- Remove holdings record → signing/key-management middleware.
- Remove digital-asset domain anchor → classic securities safekeeping (a different, non-digital Type outside this leaf).

**Taxonomy note**: the leaf name "Digital Asset Custody Platform" is defensible as a single Type, but the market word "custody" spans two regulatory postures (custodian-held vs self-custody infrastructure) that share one operational core. Kept as one Type with posture as variant; recorded for awareness rather than as a directory problem.

---

## Uncertainties

1. Coinbase Custody (a leading qualified custodian) could not be fetched (2 timeouts). Its exclusion weakens breadth for the "exchange-affiliated qualified custodian" variant; no claims about it are made.
2. Copper evidence is marketing-tier only: internal policy/quorum/key architecture unverified; used solely for posture/variant breadth (qualified custody, off-exchange settlement, collateral management).
3. Anchorage's specific charter/regulatory status not verified in fetched docs; USD banking documented as capability without charter attribution; kept out of canonical claims.
4. Insurance coverage, SOC/attestation claims appear in marketing materials across the market but were not verified as operational documentation; omitted.
5. Precise operational numbers (Anchorage min-3-members/quorum-2, BitGo 24h SLA, 99x sharding) are product-specific observations; generalizing them into the canonical document would violate evidence calibration.
6. Fireblocks' "custody" vocabulary ("direct custody" = self-custody) shows the term itself is contested; canonical writing avoids the adjective battle and defines by structure (who holds keys, how movement is governed) rather than by vendor terminology.

---

## Final Synthesis

A Digital Asset Custody Platform is the institutional system of record for holding digital assets and for moving them. Its world has three inseparable parts:

1. **A holding structure** (accounts/vaults/wallets per asset, deposit addresses, balances) that is the authoritative record of what is held, for whom, and in what shape (segregated or omnibus).
2. **Key control** — the security model ensures asset movement requires controlled cryptographic key material managed through the platform (held by the custodian, split MPC-style with the customer, or 2-of-3 across parties) so that no single actor moves assets unilaterally.
3. **Governed movement** — deposits credited under confirmation rules; withdrawals/transfers executed only through policy evaluation and approval quorums toward controlled destinations; every movement signed (often with custodian/platform participation) and durably recorded, feeding reporting, audit, and compliance hooks.

Mature products add tiered storage, role/quorum administration, destination books, transaction lifecycle surfaces, staking, exchange connectivity, fiat rails, B2B2X client structures, and off-exchange settlement — all standard capabilities, none definitional. The Type's boundary is sharpest against the consumer wallet (no organizational governance) and the exchange (not the anchor of the holdings record).
