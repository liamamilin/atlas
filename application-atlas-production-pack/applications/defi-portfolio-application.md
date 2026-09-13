# DeFi Portfolio Application

## Overview

A **DeFi Portfolio Application** is an individual's read-side aggregation and monitoring application over assets held on blockchains: it takes blockchain addresses as its anchor, decodes the raw on-chain state behind those addresses into positions across DeFi protocols, and presents the whole as one valued, changing portfolio.

The problem it solves is fragmentation. A self-custody user's holdings are not in one place: tokens sit in wallets, liquidity sits in pools, deposits sit in lending protocols, staked assets sit in staking contracts, rewards sit unclaimed — often across many networks. No single protocol shows the whole picture. This application reads the chain, reconstructs the user's positions from it, and values them together.

The defining structure is small:

```text
Blockchain address (the aggregation anchor)
└── On-chain state behind the address, decoded into positions
    ├── tokens held in the wallet
    └── protocol positions: deposited / staked / borrowed / liquidity-pool / locked / rewards
        └── unified valuation in a reference currency, tracked over time
```

One structural property separates this Type from its neighbors: **the application holds none of the user's assets and its defining job is not execution.** The positions it displays remain on-chain under the user's own keys; the application is a window, not a venue or a custodian. If a product's defining job becomes holding keys and signing transactions, it is a crypto wallet; if it holds the assets itself, it is an exchange or custody platform.

## Users & Context

The primary user is an individual who holds crypto in self-custody and interacts with DeFi protocols — lending, liquidity provision, staking, yield farming — and wants one place to see everything they own and owe.

Typical reasons to open the application:

- check the total value of the portfolio and how it has moved
- see which protocols hold what — deposits, borrowed amounts, LP positions, staked assets, unclaimed rewards
- inspect a specific position or asset in detail
- review transaction history to understand what happened and when
- watch other addresses (a common secondary use: following known investors' portfolios)

The usage context is crypto-native: the user already has a wallet, and the portfolio application typically connects to it or takes its address as input. Because the application holds no assets, the stakes of using it are informational — a wrong display is an annoyance, not a loss — but the data it presents drives real decisions, so accuracy of position decoding and pricing is the product's main quality axis.

Surfaces are typically web dashboards and mobile apps; some products are desktop applications or self-hosted tools.

## Core Model

### The Defining Core

```text
Blockchain address (the aggregation anchor)
└── On-chain state behind the address, decoded into positions
    ├── tokens held in the wallet
    └── protocol positions: deposited / staked / borrowed / liquidity-pool / locked / rewards
        └── unified valuation in a reference currency, tracked over time
```

Four properties. If any one is removed, the product is no longer recognizable as a DeFi portfolio application:

- **The address as the aggregation anchor.** The portfolio is built around blockchain addresses — the user's own (connected or entered) and commonly any watchable address — identified by raw address or a resolved name (for example an ENS name or a Web3-style ID). Without this anchor, the product is a market data site or an exchange account dashboard with nothing on-chain behind it.
- **Cross-protocol position decoding.** The application does not stop at raw token balances: it recognizes which protocols the address interacts with and reconstructs the positions — what is deposited, staked, borrowed, provided as liquidity, locked, or sitting as unclaimed rewards. The distinction between tokens "in the wallet" and tokens "in a protocol" is a first-class display dimension in every researched product. Without this, the product is a token balance checker or a block explorer.
- **Unified valuation.** All positions — across protocols and chains — are valued in a reference currency (or a crypto unit such as ETH) and summed into a portfolio total. Without this, the product is a raw position list with no economic view.
- **Read-side posture over self-custody.** The application holds no assets; positions live on-chain under the user's own keys. This is what keeps the Type distinct from wallets (which control assets), exchanges (which hold them), and custody platforms (which govern them).

### Standard Capabilities

A typical modern product carries most of these. They make the portfolio view practical; they do not define the Type.

- **Multi-chain coverage** — positions across many networks (EVM chains and layer-2s, commonly Solana and Bitcoin in current products). Chain breadth varies widely between products.
- **NFT display** — NFTs owned by the tracked addresses shown alongside tokens, often with estimated values.
- **Transaction / activity history** — the address's past activity listed and linked to the portfolio; some products correlate the user's own trades onto asset price charts.
- **Change and PnL views** — portfolio value over time, asset-level gains and losses, comparisons between dates; depth ranges from simple change indicators to full realized/unrealized PnL.
- **Watching third-party addresses** — entering any address to see its portfolio, commonly used for following large holders.
- **Address naming** — labels, tags, address books, and automatic name resolution (ENS and similar) so raw addresses become readable identities.
- **Manual balances** — entries for assets the application cannot query automatically (unsupported chains, off-chain holdings), so the total stays complete.
- **Alerts / watchers** — notifications when portfolio or protocol conditions are met.
- **Price-source configuration** — which price oracles or data sources feed the valuation (more prominent in self-hosted products).

### One Structure, Many Implementations

The core model is written conceptually. Realizations vary:

```text
Concept:          Aggregation anchor
Implementations:  connected wallet, manually entered address, address set
                  ("combined accounts"), named identity (ENS, Web3 ID)

Concept:          Position decoding
Implementations:  vendor-operated indexers and APIs, user-configured RPC nodes
                  and indexers, protocol-specific modules

Concept:          Valuation
Implementations:  fiat reference currency, crypto unit (ETH/BTC),
                  configurable price oracles, USD-denominated API totals

Concept:          Data custody
Implementations:  hosted service (vendor sees the addresses),
                  local-first self-hosted application (data stays with the user)
```

A reader who has only seen one implementation — say, a hosted mobile tracker connected to one wallet — should still be able to recognize a self-hosted desktop accounting tool or an address-search dashboard as the same Application Type from the core model.

## How It Works

### Anchor the portfolio to addresses

```text
Open the application
→ connect a wallet or enter one or more addresses
  (optionally a named identity that resolves to addresses)
→ the application reads the on-chain state behind them
→ tokens, protocol positions, and NFTs appear
→ optionally add more addresses, exchange accounts, or manual balances
```

There is no account creation in the pure form of the Type in several products: the address is the identity. Where accounts exist, they exist to sync settings and history across devices, not to hold assets.

### Read and decode positions

```text
For each tracked address and chain
→ query balances and protocol interactions
→ decode raw state into positions: wallet tokens vs deposited / staked /
  borrowed / LP / locked / reward positions per protocol
→ aggregate across addresses, protocols, and chains
```

Decoding is the hard part and the product's main value-add. Protocol coverage is never complete: newly launched or obscure protocols may not be decoded, in which case their tokens may appear as unrecognized assets or be missed entirely. Mature products let users trigger re-detection and report gaps.

### Value and monitor

```text
Price each position from the configured price sources
→ sum into a portfolio total in the reference currency
→ record snapshots over time
→ present value, change since a past point, and per-asset/per-protocol breakdowns
```

The monitoring loop is open-the-app-and-look: refresh, compare against earlier snapshots, drill into what changed. Some products add automated alerts on conditions.

### Inspect and act on the detail

```text
Open an asset or protocol position
→ see composition, value, and history of that position
→ follow links to the underlying protocol or transaction
→ (in products that bundle execution) trade, bridge, or send from the same surface
```

Execution — swap, bridge, send — appears in some products as a bundled wallet capability. It is a variant, not the portfolio core: the read-side products remain complete portfolio applications without it.

### Capability tiers

**Defining core** — without these, not a DeFi portfolio application:

- address as the aggregation anchor
- cross-protocol position decoding (wallet tokens vs protocol positions)
- unified valuation with change over time
- read-side posture (no custody, no execution as the defining job)

**Standard capabilities** — present in most mature products:

- multi-chain coverage, NFT display, activity history
- change/PnL views, third-party address watching
- address naming (labels, tags, name resolution), manual balances
- alerts/watchers, price-source configuration

**Variant / optional** — depends on product philosophy and segment:

- bundled execution (swap/bridge/send/trade) in wallet-first products
- full tax/accounting machinery (accounting rules, PnL reports, event taxonomies)
- centralized-exchange account aggregation alongside on-chain addresses
- social layers (public address profiles, badges, follows, social-graph discovery)
- deployment posture: hosted SaaS vs local-first self-hosted
- monetization: freemium limits on history depth, timeframes, or per-position PnL

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Dashboard / portfolio overview

The entry surface.

- total portfolio value in the reference currency, with change indicator
- value-over-time graph based on saved snapshots
- breakdown by source (blockchain accounts, exchange accounts, manual entries) and by asset
- primary actions: refresh, add address/account, open asset or position detail

### Assets table

The aggregated holdings view.

- one row per asset: name/symbol, chain, location, amount, price, value, share of total
- search by name, symbol, or contract address (the contract address disambiguates tokens sharing a symbol)
- row expansion showing where the asset is held (per chain, per exchange, per protocol)

### Protocol positions view

The DeFi-specific view.

- positions grouped by protocol: deposits, staked assets, borrowed amounts, liquidity pools, unclaimed rewards
- liabilities shown alongside assets where the user has debt positions
- primary actions: inspect position detail, open the protocol

### Asset / position detail

- price chart with the user's own transaction markers where supported
- position composition and history
- links to the underlying protocol or on-chain records

### Activity / history

- past transactions and events for the tracked addresses, filterable
- primary actions: inspect, filter, export (where supported)

### Accounts / addresses management

- add, label, tag, and remove tracked addresses; connect wallets
- chain selection and per-chain inclusion/exclusion
- manual balance entry; exchange-account connection where supported

### Settings

- reference currency, price sources, privacy controls (hide balances, analytics opt-out), data import/export

## Important Rules / Behaviors

### The application holds nothing

The portfolio is a view over on-chain state. Connecting a wallet or entering an address grants read access, not control; nothing in the portfolio core can move assets. Products that add execution do so as a separate, explicitly confirmed act.

### Decoding coverage is incomplete by nature

New protocols and chains appear faster than any product decodes them. An asset may show as an unrecognized token; a position may be missing until the product adds support. Users of self-hosted products can configure data sources; users of hosted products depend on the vendor's coverage.

### Valuation is only as good as its price sources

Illiquid tokens, NFTs, and positions in obscure protocols may have missing or unreliable prices. Mature products surface missing-price states rather than silently zeroing them.

### The address is public by default

On-chain holdings are publicly readable by anyone who knows the address. Products differ sharply in posture: some treat any address as publicly searchable (address watching as a headline feature), while privacy-postured products minimize what leaves the user's machine and warn that connecting a wallet exposes addresses to the service.

### History depends on snapshots or indexing

Value-over-time views are built from recorded snapshots or indexed history. They start when tracking begins; they cannot reconstruct the past before the address was added (some products backfill from chain data where possible).

### Freemium limits shape the view

Several products gate depth — longer timeframes, more history events, per-position PnL — behind subscriptions. The core aggregation view is commonly free; depth is the monetization axis.

## Variants

Common shapes the Type takes; a variant stays a variant unless it changes users, core objects, workflow, or rules so much that the core model no longer applies.

- **Wallet-bundled portfolio** — the portfolio tracker embedded in a self-custody wallet; execution (swap/bridge/send) sits one tap away from the portfolio view
- **Address-profile dashboards** — web products centered on searching and watching any address, often with a public profile page per address and social/community layers built around it
- **Dashboard-plus-API products** — consumer dashboards whose same data layer is offered as a developer API
- **Local-first accounting tools** — self-hosted, open-source applications emphasizing privacy and full tax/accounting machinery (profit/loss reports, accounting rules, event taxonomies), often combining on-chain addresses with exchange accounts and manual balances
- **Tax-first trackers** — products whose center of gravity is tax reporting, with the portfolio view in support

## Related Application Types

| Application Type | Distinction |
|---|---|
| Crypto Wallet | the control side of the same asset universe: holds keys, signs and broadcasts transactions, presents balances as a by-product. The portfolio application reads and aggregates but holds no keys and executes nothing as its defining job. One product can bundle both (packaging, not identity). |
| Cryptocurrency Exchange | custodial venue whose own ledger mirrors balances behind recoverable credentials; trading is the primary job. The portfolio application tracks self-custodied on-chain positions with no custodial balances and no operator venue. |
| Digital Asset Custody Platform | institutional custody with governed movement, approvals, and compliance machinery; the portfolio application is a personal read-side view. |
| Portfolio Management System | the organizational book of record for managed investments: mandates, positions the firm owns, execution and compliance loops. The DeFi portfolio application is personal, read-only, and owns no positions. |
| Net Worth Tracker | aggregates bank, brokerage, and other fiat-world accounts via credentials or feeds into a life net worth. The DeFi portfolio application aggregates on-chain addresses. Products that add manual balances for real-world assets blur the edge, but the on-chain anchor remains the distinguishing leg. |
| Financial Market Data Terminal | market-centric (prices, instruments, news) rather than position-centric (what a specific set of addresses holds). |
| Block Explorer | transaction- and chain-centric lookup of raw state; no cross-protocol position decoding, no unified portfolio valuation. |
| Personal Finance Management Application | fiat-world budgeting and account aggregation; a different asset universe and data model. |

The most important boundary is the one against the **Crypto Wallet**, because the two Types share the asset universe and are frequently bundled in one product. The structural test: does the product's defining job include holding keys and authorizing transactions (wallet), or reading and aggregating positions (portfolio)?

## Representative Products

- **Zerion** — self-custodial multichain wallet with an embedded DeFi portfolio tracker; the wallet-bundled pole
- **DeBank** — web dashboard centered on the address as a searchable public profile; the aggregation/profile pole
- **Zapper** — DeFi and NFT portfolio dashboard whose data layer is also a developer API; the dashboard/API pole
- **rotki** — open-source, local-first portfolio manager and accounting tool; the privacy/accounting pole

The definition was checked against the Type's earliest forms (2020-era single-chain trackers) and against adjacent products (pure token-balance checkers, block explorers, exchange-account trackers) to avoid defining the category by the current multichain, feature-rich pattern.

## Sources

Research date: **2026-09-10**

Primary sources:

- rotki — product page: https://rotki.com/
- rotki — documentation: https://docs.rotki.com/ (What is rotki?, Dashboard, Tracking Accounts)
- Zerion — product pages: https://zerion.io/ , https://zerion.io/defi-portfolio-tracker , https://www.zerion.io/crypto-wallet-tracker
- Zerion — Help Center, Portfolio Tracking collection: https://help.zerion.io/en/collections/14184109-portfolio-tracking
- Zerion — DeFi Positions API: https://zerion.io/api/endpoints/defi-positions
- DeBank — product site: https://debank.com/
- Zapper — developer documentation: https://build.zapper.xyz/ (Portfolio Data)

> Sourcing limitation: direct fetches of zerion.io, help.zerion.io, and debank.com failed from the research environment on 2026-09-10 (timeouts and regional restriction). Claims about those products rest on search-engine excerpts of their official pages and are stated at correspondingly reduced precision. No precise operational details (chain counts, limits, defaults, timings) are asserted for any product in this document; chain-coverage figures quoted in vendor marketing vary by page and date and are reported only as "multichain, dozens of chains."

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
