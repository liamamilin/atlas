# Research Notes — Crypto Wallet

Research date: 2026-09-08

## Research Goal

Understand what a Crypto Wallet application actually is — not the marketing image of "a place where crypto is stored," but the real structure of the software: what it holds, what it shows, what the user does with it, and where its boundary lies against exchanges, custody platforms, portfolio trackers, and fiat "digital wallets."

## Initial Boundary (working hypothesis before research)

- A crypto wallet does **not** store coins. The blockchain holds asset state; the wallet holds/guards the **keys** that control that state, and is the user's instrument for acting on it.
- Expected core: key material → derived addresses → receive → construct/sign/broadcast transactions → balance/history view sourced from the network.
- Nearest neighbors: Cryptocurrency Exchange (custodial venue), Digital Asset Custody Platform (institutional key custody), DeFi Portfolio Application (tracking without control), Digital Wallet / Mobile Wallet (fiat payment-credential containers — a naming collision, not a relative).
- Key unknowns: how products present seed/backup; how much of the fee/confirmation mechanics is user-facing; how dApp connection is realized; whether "custodial wallet" is inside or outside the Type.

## Research Questions

1. What does the app actually store vs. merely display? What is the account/keys/address relationship?
2. What is the backup and recovery model (seed phrase, wallet file, hardware, MPC)?
3. What is the end-to-end send flow (construct → fee → sign → broadcast → confirm)?
4. What is the receive flow (address presentation, QR)?
5. Which network/chain concepts surface to the user, and where do balances/history come from?
6. How is self-custody vs. custodial arrangement expressed in the market?
7. Which add-ons (buy/sell, swap, staking, NFT, dApp connection) are market-common vs. variant?
8. Which rules matter (irreversibility, fee market, address handling, key loss)?
9. What interface forms exist (mobile, extension, desktop, web, hardware companion)?
10. What are the exact boundary criteria against Exchange / Custody Platform / Portfolio app / fiat Wallet?

## Representative Products

Selected for market representation, philosophical spread, and customer-tier spread:

| Product | Philosophy / position | Direct docs reachable? |
|---|---|---|
| MetaMask | dominant browser-extension/mobile EVM wallet; dApp gateway | No (support.metamask.io ×2, metamask.io, docs.metamask.io all timed out) |
| Trust Wallet | mobile-first multi-chain self-custody wallet | No (trustwallet.com / support timed out) |
| Ledger (Ledger Live) | hardware-secured cold storage + companion management app | No (support.ledger.com transport error, ledger.com timed out) |
| Coinbase Wallet | self-custody wallet from a major exchange (deliberate contrast with the exchange app) | No (coinbase.com timed out) |
| Electrum | lean expert desktop Bitcoin wallet (2011-era lineage); minimal, Bitcoin-only | **Yes** (electrum.readthedocs.io — index, FAQ, coldstorage, seedphrase) |

Supplementary official source (reached): **ethereum.org** — the Ethereum Foundation's public ecosystem site, including the wallets concept page, the curated "find wallet" directory (48 listed products, each listing's data submitted by the wallet project itself), and the step-by-step wallet usage guide. This functioned as a cross-product evidence base over the modern EVM market, including the four unreachable products above (all appear in the directory with project-submitted data).

## Sources

Reached (all fetched 2026-09-08):

- Electrum documentation (official): https://electrum.readthedocs.io/en/latest/ — index, FAQ, Cold Storage, Electrum Seed Version System
- ethereum.org (Ethereum Foundation): https://ethereum.org/en/wallets/ — concept page
- ethereum.org: https://ethereum.org/en/wallets/find-wallet/ — curated directory of 48 wallets + listing criteria
- ethereum.org: https://ethereum.org/en/guides/how-to-use-a-wallet/ — receive / send / connect flows + FAQ

Not reached (source-access limitation, multiple timeouts/transport errors on 2026-09-08):

- support.metamask.io, metamask.io, docs.metamask.io
- trustwallet.com (and /support)
- support.ledger.com, ledger.com
- coinbase.com (/wallet)
- developer.bitcoin.org

**Consequence per evidence rules:** precise product-specific claims about MetaMask / Trust Wallet / Ledger / Coinbase Wallet are NOT made from memory. Product facts for those four are used only as reported by the ethereum.org directory (data submitted by the projects themselves) and are labeled accordingly. No precise numeric limits, defaults, or time windows are asserted for them anywhere.

## Product Observations

### Electrum (official docs; evidence layer A)

- "Electrum is a lightweight Bitcoin wallet"; SPV client; "does not trust servers" in the strong sense; **the client never sends private keys to servers**; server-reported data verified via SPV.
- **Seed**: "a random phrase that is used to generate your private keys"; "Your wallet can be entirely recovered from its seed" (restore wizard: "I already have a seed"). Users told to save the seed on paper.
- **Password ≠ seed**: wallet file and keys encrypted; password required at signing time; forgotten password → restore from seed with a new password; **lose both seed and password → no recovery of funds** ("there is no way to recover your money").
- **Fee market is first-class**: confirmation speed depends on fee; miners prioritize highest fees; dynamic fees by default; **RBF** (replace-by-fee) transactions by default; CPFP; pre-confirmation cancellation via double-spend; an unconfirmed transaction "will either be confirmed or cancelled. This might take several days."
- **UTXO coin selection**: "Unspent coins can have different values, much like physical coins and bills"; send failure when funds are in frozen addresses; consolidation advice for many-input transactions.
- **Addresses**: deterministic sequence from the seed; gap limit (default 20) governs address scan/recovery; addresses can be frozen (excluded from spending); private keys can be imported or **swept** (sweep = move the foreign key's coins into a seed-derived address; imported keys are NOT recoverable from seed — a special no-seed wallet type exists for them).
- **Cold storage workflow** (fully documented): offline wallet holds keys → watching-only wallet on the online machine (created from the master public key) can view history and build an **unsigned transaction file** → file transferred to the offline machine → **signed** there → signed file transferred back → **broadcast** on the online machine. Construct / sign / broadcast are explicitly separable steps.
- **Wallet types as product modes**: standard, multisig (e.g. 2-of-2 with spending requiring both), 2FA (co-signing service), hardware-wallet-backed, watching-only.
- **Network services**: connects to Electrum servers for history/fee estimates/broadcast (not to the P2P network directly); Lightning Network supported; merchant payment-request mode; pay-to-many (batching); raw transaction create+sign in the UI; console for advanced use.
- **Bitcoin-only**: "The project has never supported any altcoins."
- **Security posture surface**: screenshot protection; dedicated malware/attack-scenario documentation; GPG-signed binaries; "Help! My coins have been stolen!" page — theft is treated as an expected user-facing failure mode.
- **Seed format is its own standard**: Electrum explicitly does **not** generate BIP39 seeds; it has its own Seed Version System (version-number prefix hashed from the phrase; BIP39 introduced "two years after Electrum" and criticized for fixed wordlist and lack of versioning). Same 2048-word list and typical 12-word shape as BIP39 are used in practice, but derivation is Electrum-specific.

### ethereum.org — wallets concept page (Ethereum Foundation; evidence layer A)

- "Ethereum wallets are applications that give you control over your account… read your balance, send transactions and verify your identity."
- "Wallet providers don't have custody of your funds. They just provide you a window to see your assets on Ethereum and tools to easily manage them."
- "You can swap wallet providers at any time. Many wallets also let you manage several Ethereum accounts from one application." — provider replaceability is presented as a structural property.
- Terminology model: **account = a pair of keys** (public key → address, shareable; private key → kept secret, signs); "An Ethereum account has an address, like an inbox has an email address"; "A wallet is a tool that lets you interact with your account, using your keys." Most wallet products generate the account for you.
- Form factors enumerated by the Foundation itself: hardware devices, mobile apps, browser (web) wallets, browser extensions, desktop apps.
- Seed phrase: "Wallets will often give you a seed phrase… This is the only way you'll be able to recover your wallet. Don't store it on a computer. Write it down and keep it safe."
- Responsibility framing: "there's no customer support in crypto. You are responsible for keeping your keys safe"; "transactions can't be reversed and wallets can't be easily recovered."
- Exchange contrast: centralized exchanges link the user to a username/password "that you can recover in a traditional way… you're trusting that exchange with custody over your funds."
- dApp connection: "Your wallet lets you connect to applications using your Ethereum account. It's like a login you can use across many apps."

### ethereum.org — how-to-use-a-wallet guide (evidence layer A)

- Opening the wallet shows "a dashboard that will likely show your balance and contain buttons to send and receive tokens."
- **Receive flow**: open app → "Receive" → copy address / show QR → share with sender. Address framed like a bank account number; safe to share. "Avoid typing any Ethereum address manually" (clerical error → lost funds).
- **Send flow**: get recipient address; **verify you are on the same network as the recipient** ("Many assets… exist on multiple networks… not interchangeable"); enter address or scan QR; send; wallet "will automatically add the suggested fee… which varies depending on network conditions"; confirmation "might take anywhere from a few seconds to a few minutes depending on how much the network is currently being used."
- **Connect flow**: visit project → "Connect" → pick wallet from list (or WalletConnect-style option) → confirm signature request to establish the connection — "Signing this message should not require spending any ETH" (signature ≠ payment).
- FAQ: "Wallets are technically only an interface to show you your balance and to make transactions, your account isn't stored inside the wallet, but on the blockchain." — the single most definitional sentence found in any source.
- Same address works across EVM chains "if you have the type of wallet with a recovery phrase"; Bitcoin "implements a completely separate set of network rules" and needs a different address format. Smart-contract wallets differ again.
- Transaction status is checked via block explorers (the chain, not the vendor, is the record).
- "Can I cancel or return transactions? No, once a transaction is confirmed, you cannot cancel the transaction."

### ethereum.org — find-wallet directory (evidence layer A for the listing; product data submitted by projects)

- 48 wallets listed (July 2026 listing update). Device surfaces across the set: Desktop 16, Mobile 37, Browser 28, Hardware 9. Mobile + browser-extension dominate.
- Capabilities across the set: Buy crypto 35, Sell for cash 22 — fiat on/off-ramps are common but clearly **not** universal.
- Network support: Ethereum Mainnet 45; L2s heavily represented (Arbitrum One 37, OP Mainnet 35, Base 32…). Multi-network is the norm in this ecosystem segment.
- In-app swap fees are listed for most products (e.g. MetaMask 0.875% swap / 1% buy-sell; Coinbase Wallet 1%; Rainbow 0.85%; Exodus from 0.5%; several at 0%). A few list staking fees (e.g. Safe "20% of rewards"). These are project-submitted commercial terms — recorded here, not promoted to the canonical document.
- Named products spanning the space: MetaMask, Trust Wallet, Coinbase Wallet ("New to crypto"), Ledger (device $79–$399), Trezor ($59–$129), OneKey, Keystone, GridPlus, Cypherock X1, Burner (card form), Exodus, Rainbow, Phantom, Uniswap Wallet, Rabby, Frame (developer-oriented), Safe (smart-contract wallet), io.finnet MPC wallet for Business (paid plans from $399.99/month — the business tier edge of the sample), imToken, Bitget, Coin98, Zerion, Edge, Cake Wallet, Railway (privacy-oriented), etc.
- Listing criteria (the Foundation's own gate): security-tested (audit / internal team / open-source review); live ≥ 6 months; actively maintained with support; **supports EIP-1559 (type 2) transactions on mainnet**; Ethereum or an L2 as default network; reviewable UX. "Self-custody" is one of the tracked per-wallet attributes.

## Cross-product Comparison

| Dimension | Electrum (Bitcoin-era desktop) | EVM market (48-wallet ethereum.org sample incl. MetaMask/Trust/Coinbase Wallet/Ledger) | Evidence |
|---|---|---|---|
| Holds user's keys | yes — seed-derived, encrypted wallet file; hardware mode moves signing to device | yes — self-custody is a tracked listing attribute; provider "doesn't have custody" | A + A |
| Receive via derived address | yes (deterministic address sequence, QR-less era UX, payment requests) | yes (address + copy + QR; "like a bank account number") | A + A |
| Construct → sign → broadcast | yes, and explicitly decoupled in cold-storage mode | yes (single flow with fee step; hardware variants re-split it) | A + A |
| Balance/history from the network | yes — via Electrum servers + SPV verification; server "can lie by omission" | yes — "window onto your account"; "account isn't stored inside the wallet, but on the blockchain"; explorers as alternative window | A + A |
| Backup/restore as user duty | yes — seed on paper; lose both seed+password → unrecoverable | yes — seed phrase "the only way" to recover; write on paper | A + A |
| Irreversibility | post-confirmation irreversible; pre-confirmation replaceable (RBF/CPFP/cancel) | "once a transaction is confirmed, you cannot cancel" | A + A |
| Fee mechanics user-facing | yes — dynamic fees, fee bumping | yes — suggested fee, varies with network conditions | A + A |
| Seed phrase as recovery | yes — but **own seed format, explicitly not BIP39** | yes — "recovery phrase"; format not standardized across all wallet types | A + A(-) |
| Multi-chain | no — Bitcoin only, by policy | dominant (EVM multi-network; Bitcoin explicitly different address rules) | A + A |
| dApp connection | no | yes — connect + signature requests; wallet-as-login | A + A |
| Buy/sell fiat on/off-ramp | no | 35/48 buy, 22/48 sell | A(via listing) |
| In-app swap | Lightning-adjacent swaps only | most of the 48 list swap fees | A + A(via listing) |
| Hardware-device integration | yes (plugin mode) | yes (9 hardware products; Ledger/Trezor devices with companion apps) | A + A |
| Multisig / shared control | yes (native mode) | yes (Safe-class smart-contract wallets; MPC for business) | A + A |
| Form factor | desktop (+ CLI/daemon) | mobile-dominant, extension, desktop, web, hardware companion, card | A + A |

**Reading:** the two evidence poles (2011-era Bitcoin expert wallet vs. 2026 EVM consumer market) agree on the same four-part skeleton — keys, address, sign-and-broadcast, network-sourced view — while disagreeing on nearly everything else (chain scope, seed standard, ecosystem features, business model). That agreement-under-disagreement is what promotes the four-part skeleton to the defining core, and demotes everything else.

## Canonical Model

### L0 — Defining Invariant

Four jointly-held structures:

1. **Key custody and recovery under the user's own control** — the application holds (or directly orchestrates the holding of) the secret key material that controls the user's on-chain assets, and gives the user a way to back it up and restore it independently of the app or vendor. Remove → block explorer / portfolio tracker (a window with no control), or an exchange account (control delegated to a venue).
2. **Address as the public receiving identity** — public identifiers derived from the keys, safe to share, used to receive assets. Remove → a bare key store; the Type's receive half collapses.
3. **Sign-and-broadcast transaction execution** — construct a transfer (recipient, amount, fee), authorize it with the key, submit it to the network. Remove → watch-only wallet (Electrum's watching-only mode is exactly legs 2+4 without 3).
4. **Network-sourced asset view** — balances and history are read from the blockchain/network; the app is a window onto chain state, never the record itself. Remove → a pure signing device; replace the source with a vendor ledger → the product becomes an exchange/exchange-account app, a different Type.

Jointly-held is load-bearing:

- legs 2+3+4 without 1 = watching-only wallet (real, documented mode — not the Type)
- legs 1+2+3 without 4 = bare signing device (hardware key fob without companion app — not the application Type)
- leg 4 without 1–3 = block explorer / portfolio tracker
- leg 1 alone = key storage (e.g. a paper wallet or password-manager entry — a practice, not an application)

### L1 — Common Mature Structure

- Multi-account management (several accounts from one app — stated by ethereum.org as common)
- Transaction history with per-transaction status (pending/confirmed), explorer links
- Fee estimation with user-visible control (suggested fees; Electrum adds bump/cancel)
- QR presentation/scanning of addresses; copy-with-validation handling
- Fiat price display of holdings (Electrum fetches third-party price; market-wide)
- Security surfaces: app lock (password/PIN), seed backup ceremony, warnings about scams/phishing (Electrum ships a whole malware doc; ethereum.org ships a security page)
- Address book / labels / notes on transactions (Electrum labels; market-common)

### L2 — Variant / Optional Structure

- Chain scope: single-chain (Electrum, by policy) vs multi-chain/multi-network (EVM norm); L2-network support
- Backup/keys substrate: seed phrase (BIP39-style vs Electrum-style versioned seeds — formats differ), keystore file, hardware secure element, MPC key sharing, smart-contract accounts
- Account/control model: single-key vs multisig vs smart-contract wallet vs MPC (business tier)
- Ecosystem attach: dApp connect + signature requests (EVM), Lightning channels (Bitcoin), NFT gallery, staking interfaces
- Fiat on/off-ramp and in-app swap economics (35/48 and majority-with-swap-fees — segment-dependent, business-model-driven)
- Custodial/hosted arrangements and exchange-linked wallet apps (toward the exchange boundary)
- Form factor: mobile / extension / desktop / web / hardware companion / physical card
- Privacy posture: Tor support, own-server operation (Electrum), default-RPC choice (EVM)
- Cold-storage workflows: watching-only + unsigned-tx-file signing (Electrum), device pairing (hardware wallets)

### L3 — Vendor-specific (research notes only)

- Electrum: gap limit default 20; AES-256-CBC key encryption + ECIES wallet-file encryption; ~10 connected servers by default; seed version numbers 0x01/0x100/0x101; 132-bit seed entropy; screenshot-protection toggle; TOFU cert pinning; AppImage distribution.
- ethereum.org listing commercial terms: MetaMask swap 0.875%/buy-sell 1%; Coinbase Wallet swap 1%; Rainbow 0.85%; Exodus from 0.5%; Safe staking fee 20% of rewards; device prices Ledger $79–$399, Trezor $59–$129, GridPlus $397, Keystone $149, Burner $19/card.
- ethereum.org listing gate: EIP-1559 type-2 transaction support required for listing.

## Vendor-specific Findings (kept out of the canonical document)

- All L3 items above.
- Electrum's server architecture (Electrum protocol over SSL, SPV) is a product architecture, not a property of the Type; the Type-level fact is only "the app reads network state and never reveals keys to the services it uses."
- ethereum.org's listing criteria are one curator's gate, not a market standard.

## Rejected Findings (considered and rejected from L0)

- **"Wallet = stores coins"** — rejected by both evidence poles (Electrum: client never holds coins beyond keys+metadata; ethereum.org FAQ: "your account isn't stored inside the wallet, but on the blockchain").
- **Seed phrase (BIP39 12/24 words) as defining** — rejected: Electrum deliberately does not use BIP39; seed formats vary; the invariant is restorable key material, not a specific phrase standard.
- **Multi-chain as defining** — rejected: Bitcoin-only wallets are first-class members of the Type.
- **dApp connection as defining** — rejected: no dApp ecosystem on the Bitcoin pole.
- **Browser extension as defining surface** — rejected: desktop (Electrum), mobile-dominant market, hardware companions, web and card forms all exist.
- **Self-custody as the only posture** — partially rejected as stated: hosted/custodial wallet products exist and some sit inside the market's "wallet" category; however the market's own definitional discourse (ethereum.org concept page + tracked self-custody attribute) treats user-held keys as the normative center. Resolution: user-controlled custody is the canonical posture; custodial-hosted wallets are recorded as a boundary-leaning variant, with the tension recorded in Uncertainties.
- **Exchange-app "wallet" balances as the Type** — rejected: that is a venue ledger, not network-sourced state; naming conflation recorded as a boundary issue.

## Boundary Findings

- **vs Cryptocurrency Exchange**: the exchange is a custodial venue whose own ledger mirrors balances behind username/password with traditional recovery; trading/matching is its primary job. The wallet's record is the chain itself; its primary job is key-based control. **Seam test: remove direct key control and network-anchored state → venue account → exchange.** Conflation risk: exchanges colloquially call account balances "wallets"; several exchange-affiliated self-custody wallets exist (Coinbase Wallet vs the Coinbase exchange app is the deliberate market example) — same company, two Types.
- **vs Digital Asset Custody Platform**: shared concept (key custody) but different users/objects/rules — institutional governance, multi-party approval, compliance machinery, APIs for organizations vs. a personal control surface. The io.finnet MPC-for-business listing shows the gradient; the directory treats them as separate leaves and research supports keeping them separate.
- **vs DeFi Portfolio Application**: portfolio apps aggregate/analytics over addresses (often watch-only); no signing as defining core. Wallets add portfolio views; the seam is control. Watching-only mode is the wallet's own acknowledgment of the seam.
- **vs Digital Wallet / Mobile Wallet (fiat)**: pure naming collision — those are containers for fiat payment credentials (cards, passes); no blockchain keys, no on-chain state, different regulators. Not relatives.
- **vs Block Explorer**: read-only window onto chain state without keys — legs 4 only.
- **Paper wallet / raw key practice**: key storage without the application loop — outside the Type (leg 1 alone).
- **Hardware device alone**: a key-securing device, not the application; the Type includes its companion app (Ledger Live / Trezor Suite class).
- **"Remove-what" criteria** (for the directory): remove key control → explorer/tracker; remove network-sourced view → signing device; remove chain state as record → exchange; remove personal scale and add governance → custody platform.

## Historical / Market-Sample Check

- **Electrum (2011-lineage, desktop, Bitcoin-only, own seed format, no dApps/swaps/on-ramp)** satisfies all four L0 legs → the definition is not over-fitted to the modern EVM mobile pattern.
- **Early Bitcoin Core wallet (wallet.dat era, 2009+)** — key file + derived addresses + send/receive + balance from own full node: fits the conceptual core (reasoning-based; no live fetch — flagged in Uncertainties).
- **Paper wallets** fail legs 3–4 → correctly outside the application Type (a storage practice).
- **Early hosted web wallets (custodial)** — partial fit; recorded as the boundary-leaning variant; they fail the "user holds keys" posture but were marketed as wallets; the market's own definitional center has since moved to self-custody.
- Platform-native/fiat "wallets" (Apple/Google Pay) fail legs 1–4 entirely — the name overlap is nominal only.

## Uncertainties

1. **Custodial-hosted wallets**: the research could not reach a dedicated custodial-wallet product's official docs; the variant is inferred from the market's own discourse (ethereum.org exchange contrast; tracked self-custody attribute). Where the exchange/wallet seam sits for a specific hosted product is unresolved — recorded as a boundary issue.
2. **Four sampled products' official docs unreachable** (MetaMask, Trust Wallet, Ledger, Coinbase Wallet): all claims about them derive from the ethereum.org directory (project-submitted data). No precise operational details asserted for them.
3. **Non-EVM/non-Bitcoin ecosystems** (Solana/Phantom, privacy chains/Railway, etc.): present in the directory listing but not independently documented; assumed to fit the L0 skeleton (all sample evidence is Bitcoin/EVM).
4. **Whether smart-contract wallets change the definition long-term** (account abstraction, passkey-based recovery): listed in the sample (Safe, Clave) but under-documented here; currently treated as an L2 account-model variant.
5. **Exact confirmation-time behavior on other chains**: fee/confirmation mechanics documented for Bitcoin (Electrum) and Ethereum (ethereum.org guide); other chains not verified.

## Final Synthesis

A Crypto Wallet is the personal control surface over blockchain assets. Its defining core is a jointly-held four-part structure: user-held key material with independent backup/restore; public addresses derived from those keys for receiving; transaction execution by key signature broadcast to the network; and an asset/activity view read from the blockchain itself. The wallet is deliberately NOT the record of the user's assets — the chain is — and this is what makes wallet providers replaceable and separates the Type from exchanges (venue ledger), custody platforms (institutional governance), portfolio apps (windows without control), and fiat "digital wallets" (a name collision). Everything the modern market loads onto wallets — multi-chain support, dApp connection, swaps, on-ramps, NFTs, staking, seed-phrase standards, hardware pairing — is mature structure or variant, not definition.
