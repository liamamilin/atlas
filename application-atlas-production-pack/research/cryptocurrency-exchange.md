# Research Notes — Cryptocurrency Exchange

## Research Goal

Understand the directory leaf "Cryptocurrency Exchange" (§08 Finance, Banking, Insurance & Investment) as an Application Type: what the system's world consists of, what a user actually does in it end to end, how it differs from adjacent crypto and trading Types, and where its boundaries sit.

This pass must answer pending joint-review flags from sibling passes:
- **digital-asset-custody-platform** (processed 2026-09-08): forward note — exchange-embedded custody services and custody platforms' embedded trading/settlement are packaging seams; this pass should hold the **anchor-record test** (order books and trading accounts vs custody holdings with governed movement) rather than module presence.
- **retail-trading-platform** (processed 2026-09-07): crypto-inside-brokerage convergence — sampled US retail platforms operate crypto through separately licensed entities while the exchange leaf owns venue+custody; joint review recommended.
- **brokerage-platform** (processed): same secondary flag.

## Initial Boundary

Hypothesis before research:
- Core use: trade cryptocurrencies (and stablecoins) against fiat or other crypto on an operator-run venue.
- Users: retail individuals primarily; institutions secondarily.
- Nearest neighbors: Crypto Wallet, Digital Asset Custody Platform, Retail Trading Platform, Brokerage Platform, DeFi Portfolio Application, Payment Gateway.
- Key unknowns: is custody of balances definitional or incidental? Is the order book definitional (vs simple convert)? How do fiat on/off ramps fit? Where exactly is the DEX boundary?

## Research Questions

1. What must a user do to open and use an account (identity verification, limits)?
2. How do funds enter and leave — crypto deposits/withdrawals, fiat rails?
3. What is the trading model — order book, pairs, order types, execution, fees?
4. What balances/records does the system hold for the user?
5. What security rules govern movement of funds (2FA, whitelists, network selection)?
6. What is common but optional (derivatives, staking, P2P, OTC, cards, bots)?
7. Where does this Type end and Crypto Wallet / DEX / custody platform begin?
8. Would older/regional exchanges (pre-2017 era) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, and different product philosophies / customer tiers:

- **Coinbase** — US-regulated, retail-first, simple-buy + advanced-trade split
- **Kraken** — long-running, trader-oriented, strong Pro interface documentation
- **Binance** — global volume leader, broad product suite, multi-network funding
- **OKX** — global, derivatives-heavy heritage, US entity documented separately

## Sources

Research date: 2026-09-10. Direct WebFetch of vendor help centers timed out repeatedly (1–2 attempts each, then abandoned per network-restricted rule); content was obtained via web search returning the vendors' own help-center articles (help.coinbase.com, support.kraken.com, binance.com/binance.info support/academy, okx.com/help). Evidence layer A for all product observations below (official vendor documentation, retrieved via search snippets).

## Product Observations

### Coinbase (Layer A)

- **Onboarding/KYC**: identity verification required at account creation; "Accounts have limited functionality until verification is complete"; ID document + selfie capture, sometimes via QR handoff to phone; periodic re-verification for recordkeeping. (help.coinbase.com id-doc-verification)
- **Account limits**: purchase/deposit limits vary by location, payment method, account age, transaction history, verification steps; limits can change over time; shown per payment type in settings. (Account limits; Why did my limits change)
- **Simple buy/sell**: Buy & Sell panel — select asset, enter amount in local currency, preview order (fees/spread shown), confirm. Minimum buy amount exists ($5 stated for limit orders). (how-to-buy; Place a limit order)
- **Convert**: convert one crypto directly to another (FAQ present).
- **Advanced trade**: market / limit / stop-limit / bracket / TP-SL / TWAP orders on market pairs (crypto/crypto and crypto/fiat); limit orders rest until filled or canceled (GTC); funds on hold while order open; cancel returns funds. (Understanding the order types)
- **Order book concept documented**: bids/asks with sizes; market orders may partially fill at several prices. (learn/advanced-trading/order-types)
- **Custodial balances**: USD balance, crypto balances; funds held on hold when orders placed.
- **Send/receive**: on-chain sends to external blockchain addresses (irreversible, network fees, network selection mandatory — wrong network = lost funds, unrecoverable); off-chain sends to other Coinbase users by email/phone/username (instant, no fee, not on blockchain); receive via per-asset deposit address + QR; destination tags/memos for some assets; multichain support (same asset on multiple networks). (Steps to send/receive crypto)
- **Fiat funding**: bank account, debit card, wire. (how-to-buy)
- **Recurring buys** exist. **DEX integration** ("Trade on DEX") exists as an adjacent surface inside the app — explicitly separated from the centralized exchange ("assets not available through Coinbase centralized exchange").
- **Exchange (institutional product)**: separate "Coinbase Exchange" with portfolios, wallet balances, deposit/withdraw with 2-step verification, deposit addresses regenerate per generation while old ones remain valid. (help.coinbase.com/en/exchange)

### Kraken (Layer A)

- **Verification levels**: Verified / Verified with higher limits / Business; verification "similar to opening a bank account"; requirements include email, full name, DOB, phone, address, occupation, SSN/Tax ID (US), valid ID, proof of address, face photo, KYC questionnaire at higher level; verification status determines features, products, and funding limits. (Verification explained; Verification level requirements)
- **Funding limits**: cash deposit/withdrawal limits per rolling 24h/30d windows, dynamic, depend on residency/verification/asset; crypto deposits unlimited, crypto withdrawal limits dynamic; bank name must match account name. (Deposit and withdrawal limits)
- **Trading**: Kraken Pro trade page; Simple form (market/limit) vs full Order form; order types: market, limit, stop loss, take profit, stop-loss-limit, take-profit-limit, iceberg, trailing stop (+ limit variants); conditional close; bracket (TP/SL) orders. (Summary of order options; How to trade on Kraken Pro)
- **Order book**: market orders "match with limit orders that are already available on our order books"; maker/taker fee distinction documented. 
- **Margin**: spot vs margin selector; leverage parameter; settle-position order; derivatives available to verified accounts.
- **OTC desk** access at higher verification levels.
- **API**: full trading API (AddOrder with ordertype, volume, pair, price, time-in-force GTC/IOC/GTD/FOK, self-trade-prevention, post-only flags) — programmatic trading is a first-class surface.
- **Staking & rewards** available to verified accounts.

### Binance (Layer A)

- **KYC**: all new users required to complete [Verified] to access products including deposits, trades, withdrawals; unverified existing users reduced to "Withdraw Only" (withdraw, cancel orders, close positions, redeem); levels Verified / Verified Plus / Enterprise with different limits; ID + liveness check; limits vary by country. (How to Complete Identity Verification)
- **Spot trading**: Trade → Spot interface with sell/buy order books, trading-type selector (Spot/Cross Margin/Isolated Margin/Grid), order types Limit/Market/Stop-limit/OCO/Trailing Stop/OTO/OTOCO; default order type limit; percentage-of-balance amount slider; source-of-funds account selector. (How to Spot Trade)
- **Order-type taxonomy documented**: market (immediate, best price), limit (specified price or better), conditional orders (stop, trailing stop, OCO, OTOCO, BBO, TWAP), scaled limit, POV. (Different Order Types in Spot Trading)
- **Funding**: deposit crypto (choose asset → choose network → address/QR → credited to Spot or Funding wallet); network selection critical — wrong network = funds lost, unrecoverable; memo required on some networks; fiat deposits (bank transfer, region-dependent), card purchase, P2P trading. Withdraw crypto: address + network + amount, network fee shown, 2FA/passkey + email confirmation; address book / withdrawal whitelist (whitelist-only withdrawal mode). (Deposit/Withdraw FAQ; Academy guide)
- **Internal account structure**: multiple internal wallets (Spot, Funding, Earn, Margin) with internal transfers — a vendor structure.
- **Broad suite**: margin, futures, grid bots, Earn, P2P, card — suite breadth beyond the core.

### OKX (Layer A)

- **Help center structure**: deposit/withdrawal troubleshooting ("Deposit wasn't credited", "Withdrawal hasn't arrived"), buy/sell incl. P2P, product documentation for spot & margin, futures, options, pre-market futures, trading bots, event contracts.
- **Order types**: market, limit (GTC default), advanced limit (post-only / FOK / IOC), TP/SL (conditional/OCO), trailing stop, trigger orders (trigger on last/mark/index price), reduce-only orders, scaled orders (futures). (How do I trade with different order types; Basic Order Types)
- **Price/size limits**: documented price-limit bands for market/limit orders; market orders may be cancelled if not filled within price limit; retry mechanics for conditional orders. (Basic Order Types)
- **Margin**: isolated and cross margin modes documented as product documentation.
- **US entity**: okx.com/en-us is a separate regulated surface (OKX United States) — regional entity separation pattern.

## Cross-product Comparison

| Structure | Coinbase | Kraken | Binance | OKX | Strength |
|---|---|---|---|---|---|
| Identity verification gates account functions | ✓ (limited until verified) | ✓ (levels determine features/limits) | ✓ (unverified → Withdraw-Only) | ✓ (implied by help structure; regional entities) | B — universal |
| Custodial account balances (crypto + often fiat) | ✓ | ✓ | ✓ (multi-wallet) | ✓ | B — universal |
| Trading pairs (crypto/fiat, crypto/crypto) | ✓ | ✓ | ✓ | ✓ | B — universal |
| Order placement → execution into balances | ✓ | ✓ | ✓ | ✓ | B — universal |
| Order book / matching run by the operator | ✓ (documented) | ✓ (documented) | ✓ (documented) | ✓ (documented) | B — universal |
| Market + limit orders at minimum | ✓ | ✓ | ✓ | ✓ | B — universal |
| Conditional orders (stop/TP/trailing/OCO family) | ✓ | ✓ | ✓ | ✓ | B — universal |
| Maker/taker fee model | ✓ (spread+fees; markets rules) | ✓ (documented) | ✓ | ✓ | B — universal |
| On-chain deposit via per-asset address (+memo/tag where required) | ✓ | ✓ | ✓ | ✓ | B — universal |
| On-chain withdrawal to external address | ✓ | ✓ | ✓ | ✓ | B — universal |
| Network selection warning (wrong network = permanent loss) | ✓ | ✓ (implied by funding docs) | ✓ (repeated emphatically) | ✓ | B — universal |
| Withdrawal security (2FA/passkey, confirmation) | ✓ | ✓ | ✓ (2FA + email) | ✓ | B — universal |
| Fiat on-ramp (bank/card/wire, region-dependent) | ✓ | ✓ | ✓ | ✓ | B — universal |
| Funding limits tied to verification | ✓ | ✓ | ✓ | ✓ | B — universal |
| Address whitelist / address book for withdrawals | — (not confirmed in sample) | — | ✓ | — | single-product → optional |
| Off-chain internal transfers between users of same platform | ✓ (email/phone/username) | — | — | — | product-specific |
| Simple/convert surface vs advanced trade surface split | ✓ | ✓ (Simple form vs Order form) | ✓ (Convert + Spot) | ✓ | B — common |
| Margin trading | ✓ (advanced) | ✓ | ✓ | ✓ | B — common |
| Derivatives (futures/options) | separate product | ✓ | ✓ | ✓ (heritage core) | B — common |
| Staking/earn | ✓ | ✓ | ✓ (Earn) | ✓ | B — common |
| P2P fiat markets | — | — | ✓ | ✓ | B — common (regional) |
| OTC desk | ✓ (institutional) | ✓ | ✓ | ✓ | B — common |
| Trading API | ✓ | ✓ (extensive) | ✓ | ✓ | B — common |
| Recurring buys | ✓ | — | — | — | product-specific |
| Trading bots / grid | — | — | ✓ | ✓ | B — common |
| Internal multi-wallet split (Spot/Funding/Earn) | — | — | ✓ | — | product-specific |
| DEX aggregation inside the app | ✓ | — | — | — | product-specific |

## Canonical Model (four abstraction levels)

### L0 — Defining Invariant

The smallest structure without which the product stops being a cryptocurrency exchange:

1. **Operator-run trading venue for crypto assets** — the operator runs the market (order book matching or quoted conversion), defines pairs, rules, and fees. Remove → the operator is not an exchange.
2. **Custodial exchange account with balances** — the venue holds the user's crypto (and commonly fiat) balances as account records; trades move balances inside the account. Remove → self-custody trading (DEX/wallet territory).
3. **Order-based exchange of assets** — the user commits an order (buy/sell a pair, size, price terms) that executes against the venue's market and settles into the account balances. Remove → price tracker or portfolio viewer.
4. **On-chain funding linkage** — deposits arrive from and withdrawals leave to external blockchain addresses under the user's control, with network/address semantics as a first-class user responsibility. Remove → a closed-loop token swap service or a pure fiat brokerage.

Jointly-held test: (1) alone = market data site; (2) alone = custodial wallet; (3) without (2) = DEX; (4) without (1)–(3) = a bridge; (1)+(3) without (2)+(4) = simulated/paper venue; (2)+(4) without (1)+(3) = custody/wallet product.

### L1 — Common Mature Structure

- trading pairs with live prices and order books (depth)
- order-type vocabulary: market, limit, stop/TP family, OCO, trailing, post-only/FOK/IOC, iceberg, TWAP (breadth varies)
- maker/taker fees; order/trade history; open-order management (cancel, GTC default)
- simple/convert surface alongside advanced trade surface
- KYC/verification levels gating functions and funding limits
- fiat on-ramps/off-ramps (bank, card, wire; region-dependent)
- withdrawal security: 2FA/passkey, confirmations, address management
- price charts, watchlists, portfolio/balance views
- trading API

### L2 — Variant / Optional Structure

- margin trading; derivatives (futures, options, perpetuals)
- staking/earn products
- P2P fiat markets (regional)
- OTC desks for high-volume clients
- institutional/exchange-tier products (portfolios, higher API limits)
- trading bots/grid strategies
- internal off-chain transfers between same-platform users
- regional entity separation (one brand, multiple licensed entities)
- payment cards, launchpads, NFT markets (suite extensions)

### L3 — Vendor-specific (Research Notes only)

- Coinbase: off-chain sends by email/phone/username; deposit-address regeneration on Coinbase Exchange; "Experimental asset" labels; DEX-in-app integration; $5 minimum on limit orders.
- Kraken: named verification levels with documented requirement tables; AA-prefixed account reference for bank deposits; STP modes; conditional-close order syntax.
- Binance: Spot/Funding/Earn internal wallet split; BEP20/ERC20/TRC20 network taxonomy; whitelist-only withdrawal mode; OTOCO/OTOCO/BBO/POV order names.
- OKX: reduce-only defaults on position-page orders; documented retry mechanics for conditional market orders; price-limit bands per business line.

## Historical / Market-Sample Check

Early-generation exchanges (2010–2013 era, e.g. the first bitcoin exchanges): order-book matching, custodial account balances, on-chain deposits/withdrawals, simple market/limit orders, minimal or no KYC. All four L0 structures hold; KYC and fiat rails are L1/L2, not definitional — the definition does not over-fit to the modern regulated implementation. Conversely, modern DEXs fail L0 (no custodial account, no operator-run matching in the same sense), confirming the custodial-venue boundary rather than breaking it.

## Vendor-specific Findings

See L3 above. None promoted to the canonical document.

## Boundary Findings

- **vs Crypto Wallet**: wallet = user's own keys under personal control, asset records on-chain; exchange = custodial balances on an operator venue with order-based exchange. Removal test: remove the venue/order book → wallet; remove self-held keys → exchange. Exchange-embedded wallet features (Coinbase Wallet) are packaging seams.
- **vs Digital Asset Custody Platform** (answers that pass's forward note): anchor-record test applied — the exchange's records of record are **order books and trading accounts** (balances exist to be traded); the custody platform's records of record are **holdings of record with governed movement** (policy engine, deposit machinery, destination book, reporting; trading incidental via RFQ/off-exchange settlement). Exchange-embedded custody services are packaging seams; keep-both.
- **vs Retail Trading Platform**: retail platform centers the self-directed trading loop routed through broker/regulatory infrastructure for any asset class; the crypto exchange centers the operator-run crypto venue with on-chain funding. The crypto-inside-brokerage pattern (separately licensed entities) confirms the seam: same brand, different regulated venue. Keep-both.
- **vs Brokerage Platform**: brokerage centers the account relationship (gated creation, funding, custody records, statements); the exchange centers the venue and the trade. Overlap expected; keep-both.
- **vs DeFi Portfolio Application**: DeFi portfolio = self-custody positions across on-chain protocols, no custodial balances, no operator venue. The exchange's DEX-aggregation features are adjacent surfaces, not the Type.
- **vs Payment Gateway / Peer-to-peer Payment**: payment products move fiat money between parties; the exchange exchanges assets. Off-chain internal transfers (Coinbase) resemble payments but are a movement feature inside the exchange account, not the defining core.
- **"去掉什么就变成另一个 Type" 判据**: remove custodial balances → DEX/wallet; remove the venue/matching → custody platform; remove on-chain funding → closed-loop points exchange; remove crypto assets → generic trading platform.

## Uncertainties

- OKX identity-verification specifics were not directly retrieved (help structure implies gating consistent with peers); assertion kept at "verification gates functions" strength.
- Kraken network-selection warning was not captured verbatim in the sample; treated as implied by funding documentation, not asserted as a documented warning page.
- Address whitelisting confirmed only for Binance in this sample → kept optional.
- Fee schedules, exact limit numbers, and processing times deliberately not asserted in the final document (precision rule; limits are dynamic per vendor docs).

## Final Synthesis

A Cryptocurrency Exchange is an operator-run venue for exchanging crypto assets, defined by four jointly-held structures: the operator-run market (order book or quoted conversion over trading pairs), custodial exchange accounts holding the user's crypto/fiat balances, order-based exchange that executes into those balances, and on-chain funding linkage to external blockchain addresses. Everything else — order-type breadth, KYC levels, fiat rails, derivatives, staking, P2P, OTC, bots, APIs — is common mature or optional structure. The joint-review flags from digital-asset-custody-platform, retail-trading-platform, and brokerage-platform are answered: keep-both in all cases, with the anchor-record test (order books + trading accounts vs custody holdings) and the separately-licensed-entity pattern confirming the seams.
