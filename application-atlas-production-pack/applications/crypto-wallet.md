# Crypto Wallet

## Overview

A **Crypto Wallet** is the user's personal control surface over assets held on blockchains: it guards the cryptographic keys that control those assets, presents addresses for receiving, constructs and authorizes transactions that it submits to the network, and displays balances and activity read from the blockchain itself.

The paradox that defines the Type: **a wallet does not store the user's coins.** The blockchain holds the asset state; the wallet holds the keys that control that state and provides a window onto it. This is why the assets survive the loss or replacement of any particular wallet application, why wallet providers can be swapped without moving the assets, and why the Type separates cleanly from exchanges, custody platforms, and portfolio trackers.

The defining structure is small:

```text
User-held key material (with independent backup & restore)
└── Addresses derived from the keys — the public receiving identity
    └── On-chain asset state (balances, history) — read from the network, not owned by the vendor
        └── Transaction construction → key signature → broadcast to the network
```

Everything commonly associated with modern wallets — multi-chain support, dApp connection, in-app swaps, fiat on-ramps, NFT galleries, staking, seed-phrase standards, hardware devices — is widespread in current products but is not what makes a product a wallet. Single-chain desktop wallets from the early era of the category satisfy the same core without any of those specifics.

## Users & Context

The primary user is an individual who owns — or is about to acquire — crypto assets and wants direct control over them rather than holding them through an intermediary.

Typical reasons to open the application:

- check current holdings and their value
- receive assets from someone else
- send assets to a recipient address
- connect to on-chain applications (in ecosystems that have an application layer)
- back up or restore the key material that controls everything above

The usage context carries a responsibility posture that is unusual among application types: there is traditionally no password reset and no customer support that can reverse an outcome. Losing the key backup means losing the assets; confirming a transaction means it is final. Wallet products treat educating the user about this posture as part of their core job, not as fine print.

Secondary users include developers testing on-chain applications, merchants receiving payments, and small organizations using shared-key schemes — the last of these shades toward the separate institutional-custody Type (see Related Application Types).

Surfaces span mobile apps, browser extensions, desktop applications, web wallets, hardware devices with companion apps, and combinations of these. Mobile and browser-extension forms dominate the current market; desktop and hardware forms carry the long-lived and security-focused segments.

## Core Model

### The Defining Core

```text
User-held key material (with independent backup & restore)
└── Addresses derived from the keys — the public receiving identity
    └── On-chain asset state (balances, history) — read from the network, not owned by the vendor
        └── Transaction construction → key signature → broadcast to the network
```

Four properties. If any one is removed, the product is no longer recognizable as a crypto wallet:

- **User-held key custody and recovery** — the application holds, or directly orchestrates the holding of, the secret key material that controls the user's on-chain assets, and gives the user a way to back it up and restore it independently of the app or its vendor. Without this, the product is a window with no control (a block explorer or portfolio tracker), or an account whose control is delegated to a venue (an exchange).
- **Address as the receiving identity** — public identifiers derived from the keys, safe to share with anyone, used to receive assets. Without this, the product collapses into a bare key store.
- **Sign-and-broadcast execution** — the user constructs a transfer (recipient, amount, fee), the application authorizes it with the user's key, and the signed transaction is submitted to the network. Without this, the product is a watch-only view of someone else's holdings.
- **Network-sourced asset view** — balances and history are read from the blockchain. The application is an interface; the chain is the record. If this leg's source is replaced by the vendor's own ledger, the product becomes an exchange account — a different Application Type.

Two structural consequences follow from this core and are worth stating explicitly:

- **The wallet is replaceable; the account is not stored inside it.** The same keys can be restored into a different wallet product, which then shows the same balances and history. Mature products present provider portability as a normal property, not an emergency procedure.
- **The vendor is not the record-keeper.** Transaction status can be checked against the chain itself (for example through block explorers), not only through the wallet's own display.

### Standard Capabilities

A typical modern wallet carries most of these. They make a wallet practical; they do not define it.

- **Multiple accounts** — several independent accounts managed from one application, each with its own addresses.
- **Transaction history with status** — past activity with pending/confirmed state, usually with the ability to inspect a transaction on the network beyond the app.
- **Fee estimation and control** — a suggested fee that varies with network conditions, typically adjustable; in some ecosystems, tools for speeding up or replacing a pending transaction.
- **Address handling** — copy-to-clipboard and QR display for receiving; scanning or pasting for sending, with products actively discouraging manual address typing because a mistyped address sends funds to an unreachable place.
- **Fiat value display** — holdings shown with a market price reference in the user's currency.
- **Backup ceremony and app security** — a guided process for writing down the recovery phrase, plus app locks (password/PIN/biometric) and prominent warnings about scams and key handling.
- **Labels / address book** — naming addresses and transactions for the user's own bookkeeping.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Realizations vary widely across products and ecosystems:

```text
Concept:          Key custody & recovery
Implementations:  recovery/seed phrase written down by the user, encrypted wallet file,
                  hardware device secure element, distributed key schemes (MPC),
                  smart-contract accounts with programmable recovery

Concept:          Address
Implementations:  chain-specific address formats; one key set reused across
                  compatible networks; completely separate address systems on
                  incompatible chains

Concept:          Network state source
Implementations:  the user's own full node, third-party API services,
                  lightweight verification against servers, block explorers

Concept:          Transaction authorization
Implementations:  on-device signature, hardware-device confirmation,
                  multi-party co-signing, smart-contract approval flows
```

A reader who has only seen one implementation — say, a mobile multi-chain wallet with a 12-word recovery phrase — should still be able to recognize a desktop single-chain wallet, a hardware-secured setup, or a multisig arrangement as the same Application Type from the Core Model.

## How It Works

### Set up and secure the wallet

```text
Install / open the application
→ create a new wallet (keys are generated on the spot) or restore/import existing key material
→ perform the backup ceremony (write the recovery phrase down — it is the only path back)
→ set an app lock
```

There is no registration form in the pure form of the Type: no email, no identity verification between the user and the network. The backup step is the single most consequential moment in the product's lifecycle — every serious product interrupts the user for it, because the backup, not the app, is what survives device loss.

### Receive assets

```text
Open the receive surface
→ copy the address or show a QR code
→ share it with the sender
→ the asset becomes visible once the network records the incoming transaction
```

Sharing the address is safe by design — it is the public half of the key pair. The wallet then watches the network for transactions touching the user's addresses and updates balances and history accordingly.

### Send assets

```text
Choose the asset and the network
→ enter or scan the recipient address
→ enter the amount
→ review the fee (suggested by the app; varies with network conditions; usually adjustable)
→ confirm → the app signs the transaction with the key → it is broadcast to the network
→ watch status: pending → confirmed
```

Confirmation time depends on the fee paid and current network congestion; it ranges from seconds to minutes on many networks and can stretch much longer under congestion or with a deliberately low fee. In some ecosystems a pending transaction can be sped up or replaced before confirmation; once confirmed, it is final and cannot be cancelled or recalled.

### Connect to applications (in ecosystems that support it)

```text
Choose "connect" in an on-chain application
→ the wallet surfaces the connection request → the user approves it with a signature
→ subsequent requests from that application arrive as transaction proposals
  that the user reviews and confirms (and pays fees for) in the wallet
```

The wallet functions as a portable login across applications, and a connection signature is not itself a payment. Distinguishing "signing a message" from "authorizing a transfer of value" is one of the security skills wallet products must teach.

### Capability tiers

**Defining core** — without these, not a crypto wallet:

- user-held key material with independent backup/restore
- addresses derived from the keys for receiving
- construct → sign → broadcast transaction execution
- balances and history read from the blockchain

**Standard capabilities** — present in most mature products:

- multiple accounts, transaction history with status, fee estimation/control
- QR and clipboard address handling, fiat value display
- backup ceremony, app lock, scam/key-safety warnings, labels

**Variant / optional** — depends on ecosystem, segment, and security posture:

- buy/sell on-ramps and off-ramps, in-app swaps, staking interfaces
- dApp connection and in-app browsers, NFT galleries
- multi-network/multi-chain support, scaling-network integration (layer-2 networks, payment channels)
- multisig / smart-contract / distributed-key (MPC) account models
- watch-only mode and cold-storage workflows, hardware-device pairing
- privacy posture (routing through anonymity networks, connecting to user-run infrastructure)
- custodial or hosted arrangements (a boundary-leaning variant — see below)

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and naming vary by product.

### Dashboard / home

The entry surface.

- shows total and per-asset balances with fiat value
- primary actions: send, receive, open asset details

### Receive surface

- displays one of the user's addresses, with QR code and copy action
- primary actions: choose account/network, copy, share

### Send surface

- recipient address field (paste/scan preferred), amount entry
- fee presentation with adjustment
- primary actions: review, confirm, observe status

### Activity / history

- list of past transactions with status (pending/confirmed), counterparties, amounts, fees
- primary actions: inspect details, view on the network, retry/bump where the ecosystem allows

### Accounts & networks

- account list with create/import actions; network or chain switcher where multi-network is supported
- primary actions: create account, import/restore, switch network

### Backup & security

- recovery-phrase reveal and verification, app lock settings, connected-device or connected-application management
- primary actions: back up, verify backup, lock, revoke connections

### Connection approvals (extension and mobile forms)

- prompts raised when an external application requests a connection or proposes a transaction
- primary actions: approve, reject, inspect what is being requested

### Advanced surfaces (product-dependent)

- expert single-chain products additionally expose address lists, individual unspent amounts, raw transaction tools, and scripting consoles; consumer products hide most of these

## Important Rules / Behaviors

### Confirmed transactions are final

There is no cancel, recall, or refund once a transaction is confirmed. Payment-reversal workflows that exist in other financial software do not exist here; support for a mistaken transfer is education, not recovery.

### The backup is the only recovery path

If the user loses both the device and the backup of the key material, the assets are unreachable — no vendor can restore them. Conversely, possession of the backup is possession of control, which is why wallet products warn so heavily about where backups are stored and who sees them.

### Fees are a market, not a price list

Transaction fees fluctuate with network demand and are chosen (explicitly or via the app's suggestion) per transaction. A too-low fee can leave a transaction pending for a long time; mechanisms to replace or prioritize pending transactions exist in some ecosystems.

### Network correctness matters

Assets exist on specific networks. Sending to the right address on the wrong network, or receiving on a network the sender is not using, can strand funds. Wallets therefore surface the current network prominently in send/receive flows.

### Signing is not one thing

The same key-signature act can mean establishing a connection, approving an application's proposal, or moving assets. Wallets present these as distinct request types with distinct warnings, because distinguishing them is the user's main defense in connected ecosystems.

### The user is the custodian

In the canonical posture of the Type, the vendor neither holds the user's keys nor maintains the record of the user's assets. Products position themselves as interfaces and tools; the control — and the responsibility — remains with the user. Products that take custody themselves are drifting toward the exchange boundary (see Variants).

## Variants

Common shapes the Type takes; a variant stays a variant unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies.

- **Single-chain expert wallets** — desktop, minimal, deep tooling for one chain; no ecosystem extras by policy (historically the earliest form of the Type)
- **Mobile-first multi-chain consumer wallets** — the current market center of gravity; many assets and networks, simplified flows
- **Browser-extension wallets** — the connect-to-application gateway in ecosystems with an application layer
- **Hardware-secured wallets** — a dedicated device holds the keys and confirms actions; a companion app provides the balances/history/connectivity surface
- **Shared-control wallets** — multisig or distributed-key schemes requiring several parties (or devices) to authorize a transaction; used by individuals for security and by small organizations
- **Smart-contract wallets** — accounts implemented as on-chain programs with programmable rules (recovery, spending limits, session keys)
- **Custodial / hosted wallets** — the provider holds the keys on the user's behalf; sits on the boundary toward the exchange Type, and the market's own definitional discourse treats user-held keys as the normative center of the Type
- **Privacy-postured wallets** — network routing and infrastructure choices aimed at reducing linkability

## Related Application Types

| Application Type | Distinction |
|---|---|
| Cryptocurrency Exchange | custodial venue whose own ledger mirrors balances behind recoverable username/password credentials; trading is the primary job; the chain is not the record. Exchanges colloquially call account balances "wallets" — a naming conflation, not the same Type. Some exchange companies ship a separate self-custody wallet product alongside their exchange app: same company, two different Types. |
| Digital Asset Custody Platform | shares the key-custody concept but for organizations: governance, multi-party approval, compliance machinery, and APIs replace a personal control surface |
| DeFi Portfolio Application | aggregation and analytics over addresses, often watch-only; no signing or custody as the defining core — a window without control |
| Digital Wallet / Mobile Wallet | containers for fiat payment instruments (cards, passes) on traditional payment rails; a pure naming collision with this Type — no blockchain keys, no on-chain state |
| Peer-to-peer Payment Application | fiat money transfer between people through a payment service's own ledger and identity system; the transfer is the product, key custody does not exist |
| Block Explorer / chain data viewer | a read-only window onto network state — one leg of a wallet without the other three |

The most important boundary is the one against the **Cryptocurrency Exchange**: remove direct key control and network-anchored state, and a wallet becomes a venue account; restore them, and an exchange-adjacent product becomes a wallet. **Digital Asset Custody Platform** is the institutional counterpart: same custody concept, different users, objects, and rules.

## Representative Products

- **Electrum** — long-lived Bitcoin-only desktop wallet; the minimal/expert pole (directly documented)
- **MetaMask** — browser-extension and mobile wallet in the Ethereum-ecosystem segment
- **Trust Wallet** — mobile-first multi-chain wallet
- **Ledger (Ledger Live)** — hardware-device-secured storage with a companion management app
- **Coinbase Wallet** — a self-custody wallet shipped by an exchange company, deliberately distinct from the company's exchange app

The definition was checked against older and simpler forms of the Type (early-era desktop single-chain wallets, offline key-storage practices) to avoid defining the category by the current mobile multi-chain pattern.

## Sources

Research date: **2026-09-08**

Primary sources:

- Electrum documentation (official) — https://electrum.readthedocs.io/en/latest/ (FAQ, Cold Storage, Seed Version System)
- ethereum.org (Ethereum Foundation) — https://ethereum.org/en/wallets/
- ethereum.org — https://ethereum.org/en/wallets/find-wallet/
- ethereum.org — https://ethereum.org/en/guides/how-to-use-a-wallet/

Representative products referenced from the ethereum.org curated wallet directory (listing data submitted by the projects themselves): MetaMask, Trust Wallet, Coinbase Wallet, Ledger, Trezor, Exodus, Rainbow, Phantom, Safe, Uniswap Wallet, and others.

> Sourcing limitation: the official help centers and product sites of MetaMask, Trust Wallet, Ledger, and Coinbase Wallet could not be reached from the research environment on 2026-09-08 (repeated timeouts). Claims about those products are therefore limited to what the reachable official sources report about them; no precise operational details (limits, defaults, fees, timings) are asserted for any product in this document. Confirmation-time ranges and fee behavior are stated at the level of the underlying networks as described by the official sources above.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
