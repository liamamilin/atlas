# Research Notes — DeFi Portfolio Application

## Research Goal

Understand what a DeFi Portfolio Application actually is as an Application Type: what its unit of aggregation is, what position structures it models, how it learns and values those positions, what surfaces and rules it exposes, and where its boundaries sit against the crypto wallet, the cryptocurrency exchange, the institutional portfolio management system, and the personal net worth tracker.

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Core use: aggregate and monitor an individual's on-chain (DeFi) positions across protocols and chains, valued in a reference currency.
- Primary users: individuals holding crypto in self-custody who interact with DeFi protocols.
- Nearest neighbors: Crypto Wallet (control surface), Cryptocurrency Exchange (custodial venue), Portfolio Management System (institutional book), Net Worth Tracker (personal fiat+everything aggregation), Financial Market Data Terminal (market-centric).
- Likely boundary: read-side aggregation over self-custodied positions vs custody/signing (wallet), venue (exchange), organizational book (PMS).
- Unknowns: whether NFT display, alerts, tax/accounting, social features, or transaction execution are definitional; whether "watch other people's addresses" is primary or secondary; how multi-chain coverage factors into the definition.

Sibling leaves already processed (cryptocurrency-exchange, crypto-wallet, digital-asset-custody-platform, portfolio-management-system, net-worth-tracker) each recorded a boundary expectation for this leaf: read-only aggregation and tracking over self-custodied on-chain positions; no key control, no movement execution, no custodial balances, no operator venue, no organizational book. This research must confirm or refine those expectations.

## Research Questions

1. What is the unit of aggregation — a wallet address, a connected wallet, a named identity (ENS / Web3 ID), a set of addresses?
2. What position types are modeled: raw token balances, protocol positions (deposited / staked / borrowed / LP / locked / rewards), NFTs, liabilities?
3. How does the application learn positions — direct chain reads, indexers/APIs, wallet connection, exchange API keys, manual entry?
4. How is valuation performed — price sources, reference currency, historical tracking, PnL?
5. What DeFi-specific semantics exist beyond token balances (debt, rewards, claimables, protocol placement)?
6. What surfaces exist (dashboard, position detail, history, alerts, settings)?
7. What rules/behaviors matter (privacy posture, data accuracy, unsupported protocols, multi-chain handling)?
8. Where do transaction execution, tax/accounting, and social features sit — definitional, common, or variant?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies / customer tiers:

| Product | Philosophy | Tier / posture |
|---|---|---|
| Zerion | mobile-first consumer wallet with an embedded DeFi portfolio tracker (wallet-bundled pole) | consumer, self-custodial, multichain |
| DeBank | web dashboard centered on the address as a public profile (aggregation/profile pole) | consumer/power user, Ethereum+EVM focus |
| Zapper | DeFi/NFT portfolio dashboard with a developer data API (dashboard/API pole) | consumer + developer |
| rotki | open-source, local-first, privacy-focused portfolio manager and accounting tool (local-first/accounting pole) | privacy-conscious power users, tax/accounting emphasis |

## Sources

Directly fetched (2026-09-10):

- rotki — https://rotki.com/ (product page; features, premium feature list, testimonials)
- rotki — https://docs.rotki.com/ (documentation root: "What is rotki?", disclaimer)
- rotki — https://docs.rotki.com/usage-guides/portfolio/dashboard (Dashboard guide)
- rotki — https://docs.rotki.com/usage-guides/portfolio/accounts (Tracking Accounts guide)

Reached via search excerpts of official pages (direct fetch timed out / region-blocked / 403):

- Zerion — https://zerion.io/ , https://zerion.io/defi-portfolio-tracker , https://www.zerion.io/crypto-wallet-tracker , https://help.zerion.io/en/collections/14184109-portfolio-tracking , https://help.zerion.io/en/articles/13831023-understanding-portfolio-tracking-in-zerion , https://zerion.io/api/endpoints/defi-positions , https://app.zerion.io/settings (excerpts)
- DeBank — https://debank.com/ (homepage excerpts), https://debank.com/official (excerpts), DeBank Cloud OpenAPI description via third-party index (web3.new)
- Zapper — https://build.zapper.xyz/ (Portfolio Data API docs), https://build.zapper.xyz/docs/api/endpoints/portfolio , https://zapper.xyz (app excerpts), https://help.zapper.xyz/hc/en-us (help center index)

Source-access limitations:

- Zerion: zerion.io and help.zerion.io direct fetches timed out repeatedly; evidence limited to search-engine excerpts of the official pages. No precise operational details asserted from these.
- DeBank: debank.com region-blocked ("service is not available in your region"), docs.debank.com transport error, open.debank.com requires JavaScript. Evidence limited to homepage excerpts and the vendor's own API description as indexed by a third party. Precision downgraded accordingly.
- Zapper: zapper.xyz and docs.zapper.xyz returned 403; evidence from build.zapper.xyz (official developer docs, reached via search excerpts) and the app's own pages.
- rotki: fully documented from official sources (Layer A throughout).

## Product Observations

### rotki (Layer A — direct observation of official docs)

Positioning: "an open-source asset management and accounting application specializing in crypto assets"; "open source, self-hosted portfolio manager, accounting and analytics tool that protects your privacy." Runs on the local machine; no email needed to create an account. Disclaimer: the service "is intended only to import, display, store, and generate reports and statistics from cryptocurrency transaction data" — explicitly read-side.

Key observations:

- **Address as the aggregation anchor.** "Tracking Accounts": rotki "allows to track balances of blockchain accounts" by entering addresses (single, comma-separated multiple, or "All Supported Chains" for EVM). Supported chains: EVM (Ethereum, Optimism, Polygon PoS, Arbitrum One, Base, Gnosis, Scroll, BSC, Avalanche, zkSync Lite), Bitcoin/BCH (plain address or xpub with automatic address discovery), Substrate (Polkadot, Kusama), Solana. Ethereum validators (with ownership percentage) also trackable. Accounts carry labels and tags; CSV import/export.
- **Identity resolution.** ENS names and avatars are resolved automatically and shown instead of raw addresses across the app.
- **Sources beyond addresses.** Exchange API keys (centralized exchanges), manual balances (for assets rotki can't query automatically — "real estate, stocks, or assets on unsupported chains"). So the address is the on-chain anchor, but the portfolio can span sources.
- **Wallet vs protocol placement.** Aggregated blockchain balances show "whether they are in the wallet, or being put into some protocol" — the wallet/protocol distinction is a first-class display dimension.
- **Dashboard.** Total Balance in a configured profit currency with change indicator vs earliest snapshot in the timeframe; Net Value Graph over saved balance snapshots; Balance Summary in three source columns (Exchange / Blockchain / Manual); Assets Table (asset, location, price, amount, value, % of net value; search by name, symbol, or contract address; row expansion per chain/exchange/protocol); Liquidity Pools table (DeFi positions with per-pool composition); Liabilities table (outstanding debts); NFT Balances table (module-gated); Refresh Prices from configured price oracles.
- **Position semantics.** Liquidity pools (LP join/exit events, profit/loss per pool — premium), staking (staked amount per account, expected APR, earned rewards, staking events), DeFi historical accounting and per-protocol PnL (premium), protocol "modules" configurable in settings.
- **History & events.** Historical events (transactions, trades, deposits, withdrawals), filtering, issue resolution, on-chain transactions, data import.
- **Tax & accounting.** Tax accounting guide, Profit/Loss report, event types & subtypes, accounting rules. Explicitly not tax advice; not for continuous monitoring or automatic transmission to tax authorities.
- **Tracking.** Statistics, snapshots (balance snapshots browsable/editable/exportable), watchers (premium: email alerts when conditions met).
- **Data management.** Assets database, missing prices, address book, tags. Settings: chains, price oracles, RPC nodes, modules.
- **Execution.** On-chain transaction sending exists (screenshot "on-chain send") — a recent addition, not the product's center.
- **Privacy posture.** Local-first, self-hosted (Docker), own your data; premium limits on free tier (timeframes, event counts).

### Zerion (Layer A via official-page excerpts; precision downgraded)

Positioning: "Crypto Wallet for Solana, Ethereum, DeFi"; "Track crypto portfolio with our DeFi tracker and wallet tracker across 50+ chains. Pulls together assets, NFTs and DeFi across chains"; "Non custodial. Nobody can suspend your wallet, freeze your money, or stop your transactions." The wallet and the portfolio tracker are one product; the portfolio tracker is also offered standalone via web app.

Key observations:

- **Wallets as the anchor.** Settings: "Manage Wallets — Connect, organize and rename your wallets"; Address Book; Backup (export wallets + address book to file); Hide balances (blur amounts); privacy setting states wallet addresses are never sent to analytics.
- **DeFi position semantics.** DeFi Positions API (the same data that drives the app): "simple token balances plus decoded DeFi protocol positions (deposited, staked, borrowed, locked, and reward assets) with prices, labels, and protocol metadata." Help center Portfolio Tracking collection: Understanding Portfolio Tracking, View your tokens, Understanding Your Asset PnL, Unsupported Wallets, View your NFTs, Protocol positions ("Manage Positions in Zerion explained").
- **Valuation & PnL.** "Calculate your DeFi portfolio value in ETH, BTC, or any fiat currency"; Premium: "Real PnL: realized and unrealized"; P&L for any token position.
- **Asset page.** Tapping a token opens an Asset Page with price chart; personal buy/sell markers correlate the user's own transaction history with market price.
- **Watching others.** "Follow any wallet, find alpha" — third-party address watching is a marketed feature.
- **Execution bundled.** Swap & bridge in one transaction, send, perps, tokenized assets, copy trading — the wallet side. The portfolio core remains read-side aggregation.
- **NFTs.** "View your NFTs"; "Play videos and music NFTs"; NFT data EVM-only per developer changelog.
- **Chain coverage.** Marketing pages state 40+ / 50+ / 58+ chains including Solana (numbers vary by page and date — do not treat as precise).

### DeBank (Layer A via homepage excerpts; precision downgraded — region-blocked)

Positioning: "Your go-to portfolio tracker for Ethereum and EVM"; "Concise View of Portfolio Tracking"; search by "address / Web3 ID" or connect wallet.

Key observations:

- **Address as public profile.** Any address searchable; "Tracking any Whale's Portfolio" — watching third-party addresses is a headline feature. Web3 ID as a named identity layer over addresses.
- **Portfolio views.** VIP features: "Time Machine — Compare asset changes between any two dates"; "Change View of Portfolio — View 24-hour asset changes of any address"; "Summary View of Portfolio — Compare asset changes between any two dates"; "Transaction History Analysis Mode — user-friendly transaction data summaries and record filter."
- **Protocol layer.** Protocols pages with follower counts and TVF (total value followed); DeBank Cloud OpenAPI (vendor's own description, third-party indexed): "total balances, token lists, protocol-level DeFi positions, transaction history, and contract/transaction explanations across 90+ EVM chains."
- **Social layer.** Stream, Quest, community, Web3 Badges ("Reflects the unique achievements accomplished by each 0x address"), Credit system, follow users, profile avatars/covers — a substantial social product wrapped around the portfolio core.
- **Execution.** Swap present in nav; the portfolio core is read-side.

### Zapper (Layer A via official developer docs; consumer app docs limited)

Positioning: "Zapper: DeFi and NFT tracker"; "Your Home to Web3"; "View Search accounts, combined accounts view across Ethereum, Solana and Bitcoin, all in one place."

Key observations (from build.zapper.xyz — the official API docs, same data layer as the app):

- **Addresses as subjects.** Portfolio queries take an array of addresses; "combined accounts view" aggregates multiple addresses. Identity resolution beyond addresses exists (Farcaster FID/username → connected + custody addresses → portfolio).
- **Position model.** The portfolio query returns: token balances, app balances (DeFi protocol positions — AppTokenPositionBalance and ContractPositionBalance types), NFT balances, portfolio totals and breakdowns (by network, by asset type), and claimables (claimable rewards surfaced as a position type).
- **Valuation.** USD-denominated totals; net worth = sum of token + app + NFT balances; per-network breakdowns; real-time updates.
- **Chains.** 60+ chains per the API docs (EVM + Solana + Bitcoin per app excerpts).
- **Social drift.** iOS app marketing: "Bring your social graph, discover with the best onchain signals" — social discovery layered on the portfolio core.

## Cross-product Comparison

| Dimension | Zerion | DeBank | Zapper | rotki | Reading |
|---|---|---|---|---|---|
| Unit of aggregation | connected/managed wallets (addresses) | address / Web3 ID (any address searchable) | address set (combined view); Farcaster identity resolution | blockchain accounts (addresses, xpubs, validators) + exchange accounts + manual balances | address-anchored in all; source breadth varies |
| Position types | tokens + decoded DeFi positions (deposited/staked/borrowed/locked/rewards) + NFTs | tokens + protocol-level DeFi positions + NFTs | tokenBalances + appBalances (DeFi) + nftBalances + claimables | assets + liabilities + liquidity pools + staking + NFTs (module) | protocol-position decoding is universal |
| Wallet vs protocol placement | positions grouped by platform/protocol | protocol-level positions | app balances | "in the wallet, or being put into some protocol" | shared structural distinction |
| Chains | multichain incl. Solana (40–58+ per marketing) | Ethereum + EVM focus (90+ EVM per API) | 60+ incl. Solana, Bitcoin | EVM + BTC/BCH + Substrate + Solana | multichain common, not definitional (early products were single-chain) |
| Valuation | fiat / ETH / BTC; real-time + historical | net worth; date-comparison views | USD totals + network breakdowns | profit currency; net worth over time via snapshots | unified valuation universal |
| PnL / history | realized/unrealized PnL (premium); buy/sell markers on chart | asset-change comparison views | transaction history API | PnL report, event types, accounting rules | change-over-time universal; accounting depth varies |
| Watch third-party addresses | "Follow any wallet" | whale tracking headline | any address queryable | any address trackable | common, not definitional |
| Execution | swap/bridge/send/perps (wallet) | swap (nav) | none observed | on-chain send (recent) | variant/bundling, not core |
| Tax/accounting | none surfaced | none surfaced | none surfaced | full accounting + PnL reports | segment variant |
| Social | copy trading, follow | Web3 ID, badges, credit, stream, follows | Farcaster resolution, social graph | none | variant drift, not core |
| Privacy posture | addresses never sent to analytics; hide balances | public profiles by default | public by default | local-first, self-hosted, no email | posture variant |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures plus one structural negative property:

1. **The address as the aggregation anchor.** The application's portfolio is built around blockchain addresses — the user's own (connected or entered) and commonly any watchable address — identified by raw address or a resolved name (ENS / Web3-style ID). Remove → a market data site or an exchange account dashboard with no on-chain anchor.
2. **Cross-protocol on-chain position aggregation.** The application decodes raw on-chain state into protocol positions — deposited, staked, borrowed, lent, liquidity-pool, locked, and reward/claimable positions — across multiple protocols (and commonly multiple chains), distinguishing holdings "in the wallet" from holdings "in a protocol." Remove → a token balance checker or block explorer.
3. **Unified valuation and monitoring.** All aggregated positions are valued in a reference currency (or crypto unit) and tracked as a total with change over time. Remove → a raw position list with no economic view, or a price site with no positions.

Structural negative property: **read-side posture over self-custody.** The application holds none of the user's assets and its defining job is not execution; positions remain on-chain under the user's own keys. Remove this and the product becomes wallet / exchange / custody territory.

Jointly-held load-bearing analysis:

- 1 alone = block explorer / address lookup
- 2 without 1 = protocol analytics (TVL dashboards)
- 3 without 1+2 = price/market site
- 1+2 without 3 = raw position list with no valuation
- 1+3 without 2 = token balance checker
- 2+3 without 1 = market/protocol analytics with no user anchor

### L1 — Common Mature Structure

- Multi-chain coverage (EVM L2s, Solana, Bitcoin; chain lists vary widely)
- NFT display alongside tokens
- Transaction/activity history with the portfolio
- PnL / asset-change views (realized/unrealized, date comparison)
- Watching third-party addresses (whale tracking)
- Address naming: labels, tags, address books, ENS/name resolution
- Manual balances for unqueryable assets
- Alerts/watchers on conditions
- Price-source configuration (oracles)

### L2 — Variant / Optional Structure

- Execution bundling: in-app swap/bridge/send/trade (wallet-bundled pole) vs pure read-side
- Tax/accounting depth: full accounting engines with rules and reports (segment variant)
- Exchange-account aggregation alongside on-chain addresses (CEX API keys)
- Social layer: public address profiles, Web3 IDs, badges, follows, social-graph discovery
- Deployment/privacy posture: hosted SaaS vs local-first self-hosted; analytics minimalism
- Identity substrate: raw address, ENS, Web3 ID, Farcaster identity
- Monetization: freemium limits (timeframes, event counts, per-position PnL)

### L3 — Vendor-specific Structure

- rotki: profit-currency setting, balance snapshots with force-save/ignore-errors/import, event types & subtypes taxonomy, accounting rules engine, MCP integration, Gnosis Pay integration, premium timeframe gating (1W/2W free)
- Zerion: Zerion DNA NFT, Rewards program, perps/tokenized assets, x402/MPP pay-per-call API, specific audit firms
- DeBank: Web3 badges, Credit system, XP, Quest, Stream, VIP feature names (Time Machine, Change View, Summary View)
- Zapper: GraphQL portfolioV2 schema, Farcaster portfolio endpoint, API credit model

## Historical / Market-Sample Check

- The sampled products all date from the 2019–2020 DeFi-summer wave; the Type is young. The earliest forms (2020-era Zerion/Zapper/DeBank) already satisfy the L0: address input → decoded protocol positions → unified valuation. The definition does not depend on current-era features (perps, copy trading, AI agents, social graphs).
- Single-chain check: an Ethereum-only DeFi portfolio tracker (the 2020 form) satisfies L0 — multi-chain is L1, not definitional.
- Predecessor check: exchange-account portfolio trackers (track custodial exchange balances) fail leg 1/2 — they aggregate venue accounts, not on-chain addresses/protocol positions; they belong to a different (unlisted) tracker family. Pure token-balance checkers fail leg 2. Block explorers fail legs 2–3 (transaction-centric, no portfolio valuation).
- Wallet check: a wallet shows balances but does not decode cross-protocol positions into a portfolio view; bundling both in one product (Zerion) is packaging, not identity.
- Regional check: the sampled set is globally distributed consumer products; no region-specific pattern entered the core.

## Vendor-specific Findings

See L3 above. Notable: rotki is the only sampled product with full tax/accounting machinery; Zerion is the only one whose primary surface is a wallet; DeBank is the only one with a full social product wrapped around addresses; Zapper is the only one whose primary documented surface is a developer API.

## Boundary Findings

- **vs Crypto Wallet:** the wallet's defining core is key custody + sign/broadcast; the DeFi portfolio's defining core is read-side aggregation. Zerion ships both in one product (packaging seam — keep-both). A watch-only wallet is the overlap zone; it remains a wallet if it can sign, a portfolio app if it cannot.
- **vs Cryptocurrency Exchange:** exchange = custodial venue with its own ledger; DeFi portfolio = read-side over self-custodied on-chain positions. Confirms the exchange pass's recorded seam ("self-custody positions across on-chain protocols; no custodial balances, no operator venue").
- **vs Digital Asset Custody Platform:** institutional custody with governed movement vs personal read-side tracking. Confirms the custody pass's seam.
- **vs Portfolio Management System:** PMS = organizational book of record (mandates, positions the firm owns, execution loop); DeFi portfolio = personal read-only aggregation over chain state the app does not own. Confirms the PMS pass's "different universe" seam.
- **vs Net Worth Tracker:** net worth tracker aggregates fiat/bank/brokerage accounts via credentials/feeds into a life net worth; DeFi portfolio aggregates on-chain addresses. rotki blurs the line (manual balances for real estate/stocks; net-worth-over-time framing) — the on-chain-address anchor remains the distinguishing leg.
- **vs Financial Market Data Terminal:** market-centric data vs position-centric aggregation.
- **vs Block Explorer:** explorer = transaction/chain lookup; portfolio = position-centric aggregation with valuation and protocol semantics.
- **"Remove what to become another Type" tests:** remove the address anchor → market data site; remove protocol-position decoding → token balance checker; remove valuation → raw chain viewer; add custody/signing as the defining job → crypto wallet; add custodial balances + venue → exchange; add organizational book/mandates → PMS.

## Uncertainties

- DeBank's consumer-app structure is evidenced only by homepage excerpts (region-blocked); its internal position model is inferred from the vendor's own API description as indexed by a third party. Precision downgraded; no precise claims made.
- Zerion help-center articles were not directly fetched (timeouts); article titles and one article's excerpts are used. No precise operational details asserted.
- Zapper's consumer app surface is thinly documented in reachable sources; its position model is evidenced via the official API docs (same data layer).
- Chain-count figures (40+/50+/58+/60+/90+) vary by page and date; treated as "multichain, dozens of chains" not as precise numbers.
- Whether watching third-party addresses is a primary or secondary use case varies by product positioning (headline at DeBank, marketed feature at Zerion, incidental at rotki); treated as common structure, not definitional.
- The exact set of "protocol position types" (deposited/staked/borrowed/locked/rewards/claimables/LP) varies in vocabulary across products; the canonical abstraction is "decoded protocol positions," not any specific type list.

## Final Synthesis

A DeFi Portfolio Application is the individual's read-side aggregation and monitoring application over self-custodied on-chain positions. Its defining core is three jointly-held structures — the blockchain address as the aggregation anchor, cross-protocol decoding of on-chain state into positions (deposited/staked/borrowed/LP/rewards/claimables, distinct from wallet-held tokens), and unified valuation with change over time — plus the structural property that the application holds no assets and executes nothing as its defining job. Everything else — multichain breadth, NFTs, PnL depth, whale watching, alerts, tax accounting, social layers, execution bundling — is common mature structure or variant, not definition. The Type sits between the crypto wallet (control side of the same asset universe) and the institutional portfolio management system (organizational book of record), with the read-side/no-custody posture as the load-bearing boundary.
