# Cryptocurrency Exchange

## Overview

A **Cryptocurrency Exchange** is an operator-run venue where users exchange cryptocurrency assets — against fiat money or other crypto assets — through orders that execute into custodial exchange accounts, with funds entering and leaving through blockchain deposits and withdrawals.

The defining structure has four parts:

```text
Operator-run trading venue (order book / quoted conversion over trading pairs)
└── Custodial exchange account (the venue holds the user's crypto and often fiat balances)
    └── Order-based exchange (buy/sell a pair; execution settles into the account balances)
        └── On-chain funding linkage (deposits from, withdrawals to external blockchain addresses)
```

Everything commonly associated with modern exchanges — identity-verification levels, fiat bank rails, advanced order types, derivatives, staking, P2P markets, trading APIs — is widespread in current products but is not what makes the product an exchange. Early-generation exchanges satisfy the defining core without most of it; conversely, decentralized exchanges fail the core (no custodial account, no operator-run market) and are a different kind of product.

## Users & Context

The primary user is an individual trading their own crypto assets — buying crypto with fiat, selling back to fiat, or exchanging one crypto asset for another. Usage spans from occasional buyers using a simple purchase surface to active traders working in order-book interfaces.

Secondary users:

- **active traders** — use advanced order types, charts, and often the trading API
- **high-volume / institutional clients** — use higher verification tiers, OTC desks, and institutional exchange surfaces
- **compliance and security functions** — verification, limits, and withdrawal controls are operated by the platform on the user's behalf

The work environment is dominated by mobile apps for simple buying and web/desktop interfaces for trading. Because funds are bearer-like and transfers are irreversible, security behavior (2FA, address checking, network selection) is part of ordinary use, not an edge case.

## Core Model

### The Defining Core

**1. Operator-run trading venue.** The operator runs the market itself: it defines the trading pairs (crypto/fiat and crypto/crypto), maintains the order book or quoted conversion rates, matches or fills orders, sets trading rules, and charges fees. The venue is the reason the product exists — without it, the operator is a wallet maker or a data provider.

**2. Custodial exchange account.** The venue holds the user's assets as account balances — crypto balances, and commonly fiat balances used for trading. Trades move balances inside the account; the user does not hold keys for assets held on the exchange. This custodial account is the unit around which everything else is organized.

**3. Order-based exchange.** The user commits an order — a side (buy/sell), a trading pair, a size, and price terms — which executes against the venue's market and settles into the account balances. At minimum this means market and limit orders; mature products add a much larger conditional vocabulary. Execution is the moment the exchange actually exchanges.

**4. On-chain funding linkage.** Crypto enters by deposit to a venue-generated address (with memo/destination-tag where the asset requires it) and leaves by withdrawal to an external blockchain address. Selecting the correct network is a first-class user responsibility: funds sent on a wrong or unsupported network are typically unrecoverable — all researched products state this prominently. Fiat funding (bank transfer, card, wire) is the complementary leg for fiat balances.

Jointly-held test: a venue without custodial accounts is a matching engine, not a product; balances without the venue are a custodial wallet; orders without custodial balances are decentralized trading; funding without venue and orders is a bridge.

### Capabilities Shared by Mature Products

- **Trading pairs with live prices and order books** — depth (bids/asks with sizes) is visible in trading interfaces; market orders may partially fill at several prices.
- **Order-type vocabulary** — market and limit orders everywhere; commonly stop-loss/take-profit families, OCO (one-cancels-the-other), trailing stops, post-only / fill-or-kill / immediate-or-cancel execution instructions, and in some products iceberg or TWAP orders. Breadth varies substantially by product and surface.
- **Maker/taker fees** — fee schedules that distinguish orders that rest on the book from orders that take liquidity; fees and spread are shown at order preview in simple-buy flows.
- **Order and trade history** — open orders (cancelable while resting), executed trades, and funding history.
- **Simple and advanced surfaces** — a simple buy/sell/convert surface for one-step purchases alongside an advanced trade surface with order books; most products ship both.
- **Verification gating** — identity verification (government ID, selfie/liveness, sometimes proof of address and questionnaires) gates what an account can do; verification levels correspond to funding limits and feature access. Unverified or under-verified accounts are typically restricted (in one researched product, reduced to withdrawal-only).
- **Funding limits** — deposit/withdrawal limits tied to verification level, residency, payment method, account age, and activity; limits are dynamic and shown in account settings.
- **Withdrawal security** — two-factor authentication or passkeys at withdrawal, confirmation steps, and address management (address books / whitelists in some products).
- **Fiat on-ramps and off-ramps** — bank transfer, card, wire; availability is region-dependent.
- **Charts, watchlists, portfolio views** — price charts with indicators, balance and portfolio overviews.
- **Trading API** — programmatic order placement and account management is a standard surface for active traders and integrations.

### One Structure, Many Implementations

```text
Concept:      Operator-run venue
Realizations: central limit order book matching; quoted conversion at a displayed rate

Concept:      Custodial balances
Realizations: single unified balance; multiple internal wallets (e.g. trading vs funding vs earn sub-accounts)

Concept:      Order-based exchange
Realizations: simple one-step buy; convert; full order-form trading; API trading

Concept:      On-chain funding
Realizations: per-asset deposit addresses with network selection; memo/tag requirements; address whitelists
```

## How It Works

### Open and verify an account

```text
Register (email/phone)
→ complete identity verification (ID document, selfie/liveness, sometimes proof of address)
→ account unlocks functions progressively with verification level
→ funding limits and available features shown in account settings
```

Verification is the gate to trading and funding; accounts have limited functionality until it completes.

### Fund the account

```text
Crypto leg:   select asset → select network → copy deposit address (and memo/tag if required)
              → send from external wallet/exchange → funds credited after confirmations
Fiat leg:     link a bank/card → deposit by the available regional method → fiat balance credited
```

The network check is the critical user action on the crypto leg: the deposit network must match the sending platform's network, or funds may be permanently lost.

### Trade

```text
Select a trading pair
→ choose order type (market / limit / conditional)
→ enter size and price terms
→ preview (fees/spread shown) → place order
→ order executes immediately (market) or rests on the book until filled or canceled (limit)
→ fills settle into the account balances
```

Simple surfaces compress this to: pick asset → enter amount → preview → confirm. Advanced surfaces expose the full order vocabulary, depth, and charts.

### Withdraw

```text
Select asset → enter external address → select network → enter amount
→ review fee and final amount → confirm with 2FA/passkey (and email confirmation in some products)
→ transfer processed on-chain
```

Withdrawals are irreversible; address and network mistakes are the characteristic user error, which is why products repeat the network warning at every step.

### Core vs Common vs Optional

**Defining core** — venue, custodial account, order-based exchange, on-chain funding.

**Common mature structure** — pairs/order books, extended order types, maker/taker fees, verification gating, funding limits, withdrawal security, fiat rails, simple+advanced surfaces, API, charts/history.

**Optional / variant** — margin trading, derivatives (futures/options/perpetuals), staking/earn, P2P fiat markets, OTC desks, trading bots/grid strategies, institutional tiers, internal user-to-user transfers, payment cards, launchpads, NFT markets.

## Interfaces

### Simple buy/sell/convert surface

One-step purchase: asset picker, amount in local currency or crypto, order preview with fees and spread, confirmation. Purpose: acquire or exit an asset with minimal trading knowledge.

### Advanced trade surface

Order-book trading interface: pair selector, price chart, order book (bids/asks), order form (order type, price, size, execution instructions), open orders and trade history. Purpose: precise control over execution.

### Balances / portfolio

Account balances per asset, often split by internal purpose (trading vs funding vs earn in some products), with transaction history. Primary actions: deposit, withdraw, transfer internally.

### Deposit / withdrawal flows

Guided flows for moving funds: asset → network → address (with memo/tag handling), fee display, security confirmation, and status tracking ("deposit wasn't credited" and "withdrawal hasn't arrived" are standard help topics).

### Verification and limits settings

Verification status, requirements for higher levels, and current funding limits per payment type/asset.

### API / programmatic access

Key management and documented endpoints for order placement, cancellation, and account data.

## Important Rules / Behaviors

### Wrong-network transfers are unrecoverable

Every researched product warns that crypto sent on an incorrect or unsupported network — or to a wrong address — may be permanently lost and cannot be retrieved by the platform. This is the defining operational risk of the on-chain funding leg and shapes the entire deposit/withdrawal UX.

### Verification gates everything

Trading, depositing, and withdrawing are functions of a verified account. Verification levels map to funding limits and feature access; limits are dynamic (based on residency, verification, account age, activity) and can change over time.

### Orders rest and hold funds

Limit orders remain open until filled or canceled (good-til-canceled is the common default); the committed funds are on hold while the order is open, and cancellation returns them to the balance. Market orders execute immediately and cannot be canceled; they may partially fill at several prices.

### Withdrawals are security-gated

Two-factor authentication or passkeys, confirmation emails, and (in some products) address whitelists control the movement of funds out of the account. Withdrawal is the highest-friction, highest-protection action in the product.

### Fees are maker/taker and preview-disclosed

Trading fees distinguish resting (maker) from taking (taker) orders; simple purchases disclose fees and spread at the preview step. Exact schedules vary by product, tier, and region.

## Variants

- **regulated retail-first exchanges** — strong verification gating, simple-buy emphasis, fiat rails central (e.g. Coinbase)
- **trader-oriented exchanges** — advanced order forms, margin, API-first documentation (e.g. Kraken)
- **global high-volume suites** — broad product families (spot, margin, futures, earn, P2P, bots) around the exchange core (e.g. Binance, OKX)
- **regional-entity exchanges** — one brand operating separately licensed entities per jurisdiction, with different feature sets and protections per entity
- **institutional exchange tiers** — portfolios, higher API limits, OTC desks for high-volume clients

A variant remains a variant as long as the four-part defining core holds; when custody of holdings with governed movement becomes the center rather than the venue, the product is drifting toward a different Type (Digital Asset Custody Platform).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Crypto Wallet | user holds their own keys; asset records live on-chain, not as custodial exchange balances; no venue or order book |
| Digital Asset Custody Platform | organization's holdings of record with multi-party key control and governed movement; trading incidental — the exchange's records of record are order books and trading accounts |
| Retail Trading Platform | self-directed trading loop routed through broker/regulatory infrastructure for any asset class; crypto sold there runs through separately licensed entities, not the exchange's own venue |
| Brokerage Platform | centers the gated account relationship (funding, custody records, statements); the exchange centers the venue and the trade |
| DeFi Portfolio Application | self-custody positions across on-chain protocols; no custodial balances, no operator venue |
| Payment Gateway / Peer-to-peer Payment | moves fiat money between parties; the exchange exchanges assets (internal user-to-user transfers inside an exchange are a movement feature, not the core) |
| Financial Market Data Terminal | market data and analytics without custodial accounts or order execution |

The most important boundary is with the Crypto Wallet: the exchange holds the assets under its control so they can be traded; the wallet holds them under the user's control. Many brands ship both as separate products.

## Representative Products

- Coinbase
- Kraken
- Binance
- OKX

The defining core was checked against early-generation exchanges (order book + custodial balances + on-chain funding + simple orders, minimal KYC) to avoid over-fitting to the modern regulated implementation, and against decentralized exchanges to confirm the custodial-venue boundary.

## Sources

Research date: **2026-09-10**

- Coinbase Help Center — identity verification, account limits, order types, send/receive/deposit/withdraw: https://help.coinbase.com/ , https://www.coinbase.com/how-to-buy , https://www.coinbase.com/learn/advanced-trading/order-types
- Kraken Support — verification levels, funding limits, order types, trading API: https://support.kraken.com/ , https://docs.kraken.com/api-reference/trading/add-order
- Binance Support / Academy — identity verification, spot trading, order types, deposit/withdrawal: https://www.binance.com/en/support/faq , https://www.binance.com/en/academy
- OKX Help Center — order types, spot & margin documentation, deposit/withdrawal: https://www.okx.com/help , https://www.okx.com/en-us/help

> Sourcing limitation: direct fetches of vendor help centers timed out from the research environment; official vendor documentation was obtained via search results returning the vendors' own help pages. Precise fee schedules, numeric limits, and processing times are intentionally not stated — vendor documentation itself marks limits as dynamic. OKX verification specifics were not directly retrieved; related claims are kept at cross-product-commonality strength.
