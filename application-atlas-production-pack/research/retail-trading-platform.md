# Research Notes — Retail Trading Platform

Research date: 2026-09-07 · Methodology: v1.1 (WORKFLOW_v1.1.md / WRITING_GUIDE_v1.1.md)

## Research Goal

Understand the directory leaf "Retail Trading Platform" (§08 Finance, Banking, Insurance & Investment) as an Application Type: what the system's world consists of, what the individual investor/trader actually does in it end to end, how it relates to the brokerage relationship it presupposes, and where its boundaries sit. **This pass must answer the pending joint-review flag** for the three-way seam retail-trading-platform / professional-trading-terminal / brokerage-platform (raised by algorithmic-trading-platform, answered by brokerage-platform and professional-trading-terminal with this sibling unprocessed), and the secondary flag crypto-inside-brokerage convergence (joint review with cryptocurrency-exchange recommended).

## Initial Boundary

- Working hypothesis: the consumer-facing **trading experience surface** — instrument discovery, quotes/charts, order entry, position tracking — for individuals trading their **own** money, executing through broker/exchange infrastructure. The account relationship itself belongs to Brokerage Platform; the pro-grade market-density workspace belongs to Professional Trading Terminal; encoded decision loops belong to Algorithmic Trading Platform.
- Prior sibling notes to honor:
  - brokerage-platform (processed): center-of-gravity test recorded — remove account administration → trading surface (this leaf); remove the trading loop → statement portal. Straddles expected (Robinhood merges account+trading; Schwab attaches thinkorswim; Zerodha splits Kite/Console).
  - professional-trading-terminal (processed): retail is "account-centric consumer surface (funding, statements, simple order flows)" vs terminal "market-centric professional workspace (depth, ladder, hotkeys, entitlements, risk administration)".
  - algorithmic-trading-platform (processed): conditional order types (stop/bracket/OCO) are order-management primitives, not strategies; the structural test is who decides at trade time.
- Nearest confusion risks: brokerage platforms (same family, different center), pro terminals (straddle via broker-attached pro surfaces), robo-advisors (decision delegated), market-data/news products (no execution), crypto exchanges (venue+custody model), paper-trading simulators (no real execution), personal-finance trackers (no orders).

## Research Questions

1. What objects does the surface manage (instruments, quotes, watchlists, orders, positions, holdings) and which is the center?
2. What is the full retail trading loop from finding an instrument to seeing the outcome?
3. How is market data presented (quotes, depth, charts) and where does it come from (entitlements, disclaimers)?
4. What order vocabulary exists (types, validity, product codes, conditional/group orders) and what order states does the user see?
5. How do retail platforms govern trading — eligibility gating, risk documents, intraday rules, surveillance flags?
6. How is the account relationship handled — inside the same product, split into a backoffice, or presupposed?
7. What asset classes and regional market microstructures shape the surface?
8. Which capabilities are definitional vs common vs variant (paper trading, fractional shares, recurring investing, IPOs, extended hours, social/community, APIs)?
9. Where exactly do the seams run vs Brokerage Platform / Professional Trading Terminal / Algorithmic Trading Platform / data-and-news Types / crypto exchange / robo-advisor?
10. Does the definition survive older/regional/platform-native samples (1990s web trading, phone-order era, India vs US microstructure)?

## Representative Products

| Product | Geography | Philosophy | Evidence tier |
|---|---|---|---|
| **Zerodha Kite** | India | discount broker; deliberately split trading platform (Kite) from account backoffice (Console); minimal, no-tips posture | Tier-1 (support portal: categories + articles, deep) |
| **Webull** | US | charting-centric retail platform for active retail traders; tiered subscription | Tier-1 (landing + help center + order-types FAQ, deep) |
| **Charles Schwab trading surfaces** | US | full-service broker; ladder of surfaces from simplified web/mobile to pro-grade thinkorswim | Tier-2 (product/marketing page + FAQ, moderate) |
| **Robinhood** | US | app-first consumer pioneer; single merged app over a constellation of licensed entities | Tier-2 (support page navigation + legal/entity disclosures only — help articles JS-rendered, same limitation as brokerage pass) |

Selection covers two geographies (US/India), four philosophies (bare discount / charting-first / full-service ladder / app-first merger), and different tiers (first-time investor to active retail trader). eToro (global social-trading; would have anchored the copy-trading pole) and Trading 212 (UK/EU fractional-first) were **unreachable** (transport errors / timeout) — see Source-access Limitation.

## Sources

- Zerodha — Support Portal root (product taxonomy): https://support.zerodha.com/
- Zerodha — Kite "Charts and orders" category (chart engines, order types, GTT, baskets, stock SIP): https://support.zerodha.com/category/trading-and-markets/charts-and-orders
- Zerodha — "What are limit and market orders?": https://support.zerodha.com/category/trading-and-markets/charts-and-orders/order/articles/what-are-limit-and-market-orders
- Zerodha — "Trading FAQs" category (holdings vs positions, sessions, circuit limits, surveillance, settlement): https://support.zerodha.com/category/trading-and-markets/trading-faqs
- Webull — corporate site landing (product/navigation structure): https://www.webull.com/
- Webull — Help Center root: https://www.webull.com/help
- Webull — "Supported Investments & Order Types": https://www.webull.com/help/faq/298-Supported-Investments-Order-Types
- Charles Schwab — "Schwab Trading Powered by Ameritrade" (platforms ladder, FAQ, disclosures): https://www.schwab.com/trading
- Robinhood — Support page (site navigation + legal/entity disclosure block): https://robinhood.com/us/en/support/
- Unreachable: eToro (https://www.etoro.com/en/help/ , https://www.etoro.com/customer-service/ — transport error ×2), Trading 212 (https://help.trading212.com/ — timeout). No claims rest on either.

## Product Observations

### Zerodha Kite (evidence layer A — direct)

- **Product family split**: support portal lists "Kite Trading platform" and "Console Backoffice" as separate products, plus Kite Connect (trading APIs), Coin (mutual funds), Varsity (education), Trading Q&A. Kite support categories: IPO, Trading FAQs, Margin Trading Facility (MTF) and Margins, **Charts and orders**, **Alerts and Nudges**, General. Console categories: Portfolio, Corporate actions, Funds statement (ledger), Reports, Profile, Segments. → trading surface vs account administration split is explicit.
- **Charts**: two embedded chart engines (ChartIQ and TradingView) with switchable charts; Trade-From-Chart (TFC) order placement on both; drawings, indicators, saved layouts/views, multiple charts, backtest feature on charts, relative-performance comparison, corporate actions on charts; candle/axis/theme configuration. Historical-data quirks vs exchange records documented.
- **Order types**: limit and market (with definitions: limit = specified price or better; market = best available immediately; partial fills; ₹0 limit rejected; limit orders valid 1 day), stoploss (SL/SLM, trigger price concept), cover orders, **market protection** on the order window, Iceberg orders, After Market Orders (AMO), Alert Trigger Orders (ATO). Validity: Day / Immediate (IOC) / Minutes.
- **Product codes as a second axis**: CNC (Longterm/delivery), MIS (Intraday), NRML (Overnight); conversion between them; auto square-off policy for intraday positions with published timings; MIS blocked for some instruments; market orders blocked for trade-to-trade/debt instruments.
- **GTT (Good Till Triggered)**: long-lived conditional orders — OCO (one-cancels-other, e.g. target+stoploss), trailing stoploss, one-year validity horizon; states: active → triggered → (executed | not executed); triggered-but-pending GTT not visible in order book; notifications on trigger; GTT disabled/cancelled/expired/rejected states. GTC orders *not* offered on Kite (GTT is their substitute).
- **Basket orders**: multi-order baskets with margin analysis ("required" vs "final margin"), shareable baskets, quick baskets, CSV import to execute trades; partial basket execution.
- **Stock SIP**: recurring buy orders at weekly/fortnightly/monthly/daily frequencies, created/modified from the trading platform.
- **Holdings vs positions distinction** (dedicated FAQ): holdings = delivery-based long-term positions in demat; positions = intraday/derivatives book. This vocabulary is the retail platform's state model.
- **Market microstructure surfaced to the user**: market sessions (timings, pre-market/post-market sessions, periodic call auction), circuit limits/price bands, market-wide circuit breakers, F&O ban periods, ASM/GSM surveillance measures restricting trading, trade-to-trade segment, SSE listing-day sessions.
- **Derivatives breadth**: option chain viewer on Kite, open interest, lot sizes, physical settlement policy, rollover, currency/commodity/electricity derivatives.
- **Depository interplay**: CDSL TPIN authorization required to sell holdings (demat debit authorization), pledge mechanism for margin collateral (regulatory), consolidated account statement from depository.
- **Order lifecycle**: order pending / rejected / executed-not-filled states all have dedicated FAQ entries; "charges" shown on the order window; quick order window; placing orders without adding to marketwatch; quick order cancellation.
- **Regulatory/entity structure**: SEBI-registered broker, NSE/BSE member; commodity trading through a separate entity (Zerodha Commodities Pvt Ltd, MCX member); exchange-level trade confirmations by SMS/email; daily margin statement; peak-margin penalty; SCORES/ODR complaint channels.
- **Self-directed posture, explicit**: footer states "we don't give stock tips, and have not authorized anyone to trade on behalf of others"; FAQ: no assigned relationship manager providing advisory tips; phone ordering exists as a fallback channel ("Can orders be placed by calling Zerodha?"); no demo/paper-trading account (FAQ title: "Does Zerodha offer demo accounts for paper trading?"); legacy desktop platform (Pi) still referenced; "Kite terminal mode" exists as a denser mode; Stockreports+ third-party research subscription referenced.

### Webull (evidence layer A — direct)

- **Product/navigation structure**: Trading (Stocks, ETFs, Options, Index Options, Futures, Overnight Trading, Crypto, OTC, Margin, Prediction Markets) vs Investing (Cash Management, Recurring Investing, Retirement Accounts/IRAs, Fixed Income, Money Market Funds, Webull Advisors, Mutual Funds) — the platform explicitly serves both trading and investing modes. Tools: paperTrade, Charts & Tools, Vega, Open API, Third-Party Platforms (TradingView connectivity), Orderflow Chart. Platform: Desktop, Mobile. Plus Learn/Community/Premium (subscription)/Agentic AI.
- **Order-type taxonomy (FAQ, verbatim structure)**: equities simple types = Limit, Market, Sell Stop, Stop Limit, Trailing Stop, Conditional; group types = Take-Profit/Stop-Loss (bracket: parent order + activated sub-orders), OCO, OTO (one-triggers-the-other), OTOCO. Options: Limit/Market/Stop Limit/TP-SL/Trailing. Futures: Limit/Market/Stop Limit/Sell Stop/Trailing/TP-SL. Bonds: Limit. Event contracts: Limit + Quick Order. Conditional orders (index/stock triggers) **mobile-app-only, regular hours only**.
- **Time in force**: Day order (expires at close; extended-hours inclusion extends to 8 PM ET), GTC (~90-day expiry; pauses outside regular hours unless extended hours selected; corporate actions cancel GTC).
- **Order mechanics**: partial fills; stop→market conversion semantics; trailing-stop mechanics; bracket minimum TP/SL separation (0.1% of price); OCO simultaneous-execution edge case (can produce a short position).
- **Asset-class/entity separation**: Webull Financial LLC (SEC/FINRA broker-dealer; "self-directed customers"), Webull Futures LLC (CFTC-registered FCM), Webull Advisors LLC (SEC RIA; "Trades in your Webull Advisors account are executed by Webull Financial LLC"), Webull Pay (crypto account linking). SIPC + excess-SIPC disclosures.
- **Eligibility gating**: "You need to complete an options trading application and get approval on eligible accounts"; margin "subject to Webull Financial, LLC review and approval"; futures/forex approval; margin includes "possibility of a forced sale if account equity drops below required levels."
- **Market data layer**: "Level 2 Quotes and NBBO", Nasdaq/Cboe/TradingView/WSJ/CME partnerships; help categories "Market Data and Analysis" with **Non-Professional market-data disclaimer** (exchange-agreement regime), NASDAQ Advanced Quotes. Extended hours: pre-market 4 AM–9:30 AM ET, after hours 4 PM–8 PM ET; overnight trading product; "Day Trade Without the $25K Minimum. No more day trade limits" banner (US pattern-day-trading regime referenced as marketing).
- **Account machinery inside the same product**: Bank Transfer (Linking Your Bank, Debit Card Deposits, ACH Deposits), Account Transfer (Transfer Basics, Internal Cash/Asset Transfers), Documents and Taxes (tax documents, **Tax Lot Preferences**), Retirement (contributions/distributions).
- **Paper trading**: "Test trading strategies with real-time quotes without risking a penny" — a first-class tool; script editor exists (custom indicator scripting); order-flow chart; AI assistant ("Agentic", Trading Assistant, Voice Quote).

### Charles Schwab trading surfaces (evidence layer A for positioning; B for mechanics)

- **Surface ladder inside one firm**: Schwab.com (web trading) + Schwab Mobile (beginner-oriented: "simplified interface, educational content in context") + thinkorswim desktop/web/mobile ("professional-grade trading workstation"; "powerful charting tools, advanced technical analysis, high customization") + paperMoney (paper trading) — all free with any Schwab account, trades priced identically across surfaces. **Vendor-acknowledged straddle**: "The market typically forces a choice between a simplified mobile experience and a professional-grade trading workstation, but Schwab delivers both."
- **Trading offer scoped to self-directed accounts**: "Schwab Trading Powered by Ameritrade™ is available for most Schwab self-directed brokerage accounts. Accounts not eligible include managed and specialty accounts"; account must be opened and approved first, then platforms "enabled".
- **Asset classes with separate entities**: futures/forex through Charles Schwab Futures and Forex LLC (CFTC-registered FCM; "Trading privileges subject to review and approval. Not all clients will qualify"); options require reading the OCC "Characteristics and Risks of Standardized Options"; crypto "coming soon" through Charles Schwab Premier Bank (separate bank entity); broker-assisted trades cost extra ($25) and automated phone trades ($5) — electronic self-directed entry is the default mode, human channels are paid exceptions.
- **24/5 trading** on 1,300+ tickers (extended-hours variant); dedicated Trade Desk team of trading specialists; education library; research tools; fractional shares ("Stock Slices"); margin rates.

### Robinhood (evidence layer B — navigation and legal surfaces only; help articles did not render)

- **Single merged app** spanning: Invest, IPO Access, Predict (prediction markets), Strategies (managed), Agentic Trading (AI), Retirement, Gold (subscription membership), Crypto (Earn/Staking/Wallet/Connect/API), **Legend** (advanced desktop platform — "no additional cost to use Robinhood Legend"), Options, Futures, Trading, Custodial, Ventures, Social, Banking, credit cards.
- **Entity constellation** (legal footer): RHF (broker-dealer), RHS (clearing), RAM (SEC RIA for Strategies), RHD (CFTC FCM for futures), RHC (crypto; NYDFSBitLicense-framed; "not FDIC insured or SIPC protected"), RHY (money transmitter for spending account), RCT (credit), RHG (Gold) — all subsidiaries of Robinhood Markets. Options require the OCC disclosure document. This matches the crypto-inside-brokerage convergence pattern flagged by the brokerage pass.

## Cross-product Comparison

| Dimension | Zerodha Kite | Webull | Schwab trading | Robinhood |
|---|---|---|---|---|
| Instrument universe | equities, ETFs, bonds, F&O, currency & commodity derivatives | US stocks/ETFs/OTC, options, futures, bonds, event contracts, crypto (separate entity) | stocks/ETFs, options, futures, forex, fixed income, fractional; crypto coming | stocks/ETFs, options, futures, crypto, prediction markets (entity-per-class) |
| Quotes/charts | ChartIQ + TradingView embedded engines, TFC, backtest | Level II/NBBO, TradingView partnership, order-flow chart, script editor | thinkorswim "professional-grade" charting; simplified web/mobile | Legend desktop platform (advanced), app |
| Order types | limit/market/SL(SLM)/cover/iceberg/AMO/ATO + GTT OCO/trailing; validity Day/IOC/Minutes | limit/market/stop/stop-limit/trailing/conditional + bracket/OCO/OTO/OTOCO; Day/GTC | full ladder incl. via thinkorswim; approval-gated classes | not directly observed (help JS-rendered) |
| Positions model | holdings (demat) vs positions (intraday/derivatives) explicit | positions + tax-lot preferences | holdings/performance via account; trading via surfaces | not directly observed |
| Intraday/regime rules | auto square-off timings, circuit limits, ASM/GSM, F&O ban | day-trade regime marketing ("no $25K minimum"), overnight sessions | 24/5 trading, extended hours | not directly observed |
| Account machinery | split out to Console (portfolio/ledger/reports) | inside same product (bank transfer, transfers, tax docs) | inside same account platform | inside same app |
| Paper trading | none (FAQ indicates no demo accounts) | paperTrade first-class | paperMoney (thinkorswim) | not observed |
| Recurring investing | Stock SIP (daily→monthly) | Recurring Investing | not observed on this page | Strategies adjacent |
| IPO access | IPO category (ASBA framing) | IPOs in supported investments | not on this page | IPO Access product |
| Eligibility gating | segment activation (F&O/commodity) | options/margin/futures applications + approval | futures/forex approval; options OCC doc | options OCC doc; entity separation |
| Advisory/managed | none (explicit no-tips posture) | Webull Advisors (RIA, same execution) | Intelligent Portfolios / Wealth Advisory | Strategies (RAM) |
| Social/community | none (explicit) | Community feature | Trade Desk human support | Social product surface |
| Personal API | Kite Connect | Open API | not observed | Crypto API (docs.robinhood.com) |
| Entity separation | Broking vs Commodities entities | Financial vs Futures vs Advisors vs Pay | &Co. vs Futures-Forex vs Banks | RHF/RHS/RAM/RHD/RHC/RHY/RCT/RHG |
| Monetization | flat per-order fee (₹20/₹40 seen in FAQ titles) | zero-commission + Premium subscription + promo T&Cs | $0 equities + per-contract fees + satisfaction guarantee | free core + Gold subscription |

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product is not a retail trading platform:

1. **Individual, self-directed participant trading their own money** — the user is the principal making every trade decision; the product's posture is explicitly self-directed (advisory/managed modes, where present, are add-ons over the same surface, not the center).
2. **A tradeable instrument universe with market pricing** — searchable/browsable instruments with prices (live or delayed; depth optional).
3. **Order construction and submission by the human** — the person composes an order (side, quantity, price terms) and submits it; conditional/group orders are still human-authored contingencies, not running decision loops.
4. **Real execution through broker/exchange infrastructure** — orders route to actual markets via the brokerage relationship the platform presupposes (paper trading exists only as a mode; a simulation-only product is a different Type).
5. **The person's own positions/holdings as tracked state** — fills update what the person holds and at what cost, with P&L visible, closing the loop for the next decision.

Historical check: 1990s consumer web-trading platforms (instrument list, quote, order ticket, positions) satisfy this; the pre-electronic phone-order brokerage relationship does not instantiate this Type at all (no self-directed electronic surface) — which *sharpens* rather than breaks the definition; India (Kite) and US (Webull/Schwab/Robinhood) both fit despite opposite market microstructure. No modern convenience (mobile-first, zero commission, fractional shares, crypto, social) is required.

### L1 — Common Mature Structure

- Watchlists (marketwatch) as the personal instrument shortlist; search/discovery over the universe
- Interactive charts with indicators/drawings, increasingly embedded third-party engines; trade-from-chart
- Extended order vocabulary: stop/stop-limit, trailing, validity (day/GTC/IOC), after-hours/after-market orders, conditional and bracket/group orders (OCO/OTO)
- Order lifecycle visibility: pending/working/filled/rejected/cancelled, partial fills, modify/cancel; charges visible on the order
- Positions/holdings views with cost basis, unrealized/realized P&L; day P&L for active use
- Basic market depth on quotes; Level II gated in the US sample
- Price alerts and order notifications
- Funding/withdrawal linkage to bank sources (light version of the brokerage machinery)
- Eligibility gating for advanced classes (options, margin, futures, commodity segments) via application + approval + risk-document acceptance
- Margin borrowing as a gated capability with forced-liquidation terms
- Multi-surface delivery: mobile app primary for consumers, web standard, desktop-class surface for active users
- One brand spanning multiple regulated entities per asset class
- Zero-commission/flat-fee discount economics as the dominant business posture
- Risk disclosures as an in-product step (options/futures documents)

### L2 — Variant / Optional

- Delivery shape: merged single app (Robinhood) vs split trading/backoffice products (Kite/Console) vs tiered surface ladder inside one login (Schwab.com → thinkorswim)
- Trading-vs-investing framing inside one product (Webull's nav split; Schwab "self-directed investing" vs "active trading")
- Asset-class center of gravity (equities default; options/futures/FX-CFD/crypto/prediction-market emphases)
- Regional microstructure surfaced to users: circuit limits/surveillance segments/ban periods/TPIN debit authorization (India) vs day-trading regime/overnight & 24-5 sessions/tax-lot methods (US)
- Paper-trading/simulation modes (common in US sample; explicitly absent at Zerodha)
- Fractional shares (US-centric; not evidenced in India sample)
- Recurring investing/SIP (both geographies, different names)
- IPO participation surfaces
- Extended/overnight sessions (US)
- News/research/education depth (from deliberately minimal to full research suites)
- Social/community surfaces (Robinhood Social nav, Webull Community; copy-trading pole — eToro — unreachable, unverified)
- Personal trading APIs for one's own automation (Kite Connect, Webull Open API) — seam toward Algorithmic Trading Platform
- Advisory/managed add-ons over the same account (robo seam)
- Subscription tiers over free trading (Gold, Premium)
- AI assistance (agentic trading, trading assistant, AI answers)

### L3 — Vendor-specific (research notes only)

Kite: GTT/CO/AMO/ATO/iceberg/basket/stock-SIP feature names, ChartIQ+TradingView dual engines, Console split, CDSL TPIN flow, terminal mode, Pi legacy desktop, ₹20/₹40 brokerage figures, quick order window/cancellation, "nudges". Webull: Vega, AgenticAI, Script Editor, Orderflow Chart, OTOCO naming, conditional-orders-mobile-only rule, 0.1% bracket separation rule, GTC ~90-day expiry, Apex clearing disclosures, Webull Pay linking. Schwab: thinkorswim/paperMoney branding, Trade Desk, 24/5 ticker count, satisfaction guarantee, $25 broker-assisted/$5 automated-phone fees, Stock Slices. Robinhood: Legend, Gold, RHF/RHS/RAM/RHD/RHC/RHY/RCT/RHG entity stack, Agentic Trading, Predict, Custodial, Ventures, Snacks/Sherwood.

## Vendor-specific Findings

See L3 above. Additionally: Schwab's own comparison table lists competitor feature rows (paper trading, 24/5, desktop platform) — treated as vendor claims about competitors, not evidence. Webull's "no day-trade limits" banner is a marketing claim about a regulatory change; the underlying US day-trading regime is referenced only qualitatively.

## Boundary Findings

1. **vs Brokerage Platform** (ANSWERS the pending joint-review flag from this side): the three-way seam **holds by center of gravity, confirmed from the retail side**. Retail Trading Platform centers the **trading loop for the individual's own money** (instrument discovery → market view → order construction → execution → positions → next decision); Brokerage Platform centers the **account relationship** (gated account creation, funding sources, custody records, statements, capability approvals). Structural tests both ways: remove the trading loop → statement portal (brokerage remains, this Type does not); remove account administration → this Type remains (it presupposes the account). Objects are shared (the family shares instrument/quote/order/position) — the seam is the center, not disjoint objects. Straddles are real and structural: Robinhood merges both in one app; Schwab ships a surface ladder over one account family; Zerodha splits them into separate products (Kite/Console) while one firm owns both. **Recommendation: keep both Types.** This entry discharges the joint-review flag for retail-trading-platform (brokerage and terminal sides already answered).
2. **vs Professional Trading Terminal**: retail = consumer-grade, account-anchored, simple order flows, decisions for one's own portfolio at human speed; terminal = market-centric workspace density (ladders/depth/hotkeys/entitlements/risk administration) for frequent professional use. Straddles: broker-attached pro surfaces (thinkorswim, Robinhood Legend, Kite terminal mode) — the same firm shipping both is the pattern, and the Schwab page itself names the "simplified mobile experience vs professional-grade trading workstation" split. Consistent with the terminal pass's account-centric vs market-centric test.
3. **vs Algorithmic Trading Platform**: at trade time the human decides; conditional/bracket/OCO orders are order-management primitives (consistent with both sibling passes). Seam: personal APIs (Kite Connect, Webull Open API) let users run their own code — a hand-off surface into that Type; broker-embedded strategy platforms (TradeStation pattern) straddle as previously recorded.
4. **vs Financial Market Data Terminal**: the data/analysis layer is separable — remove order entry and the product becomes a quotes/charts/news tool. Market-data non-professional disclaimers (Webull) show the data layer has its own licensing regime.
5. **vs Financial News / Investment Research Platform**: content products hold no accounts and take no orders; research inside retail platforms is decision support, varying from deliberately none (Zerodha's no-tips posture) to full suites (Schwab).
6. **vs Robo-advisor / managed investing**: when the vendor's algorithm decides and rebalances, the mode crosses toward robo-advisor; sampled products host managed modes over the same account (Strategies/RAM, Webull Advisors, Intelligent Portfolios) as add-ons — the self-directed loop remains this Type's center.
7. **vs Cryptocurrency Exchange**: retail platforms increasingly sell crypto, but through **separately licensed entities with distinct (usually weaker) protection** (RHC, Webull Pay, Schwab Premier Bank) — the exchange operates its own venue and custody, while the retail trading platform routes orders through broker/regulatory infrastructure. Answers the brokerage pass's secondary crypto-convergence flag from this side: **joint review with cryptocurrency-exchange recommended** when that leaf is processed.
8. **vs paper-trading simulators**: simulation-only products are a different Type; simulation as a mode inside real platforms is common (paperTrade, paperMoney) but not universal (Zerodha offers none).
9. **vs Personal Finance / Portfolio tracking apps**: trackers hold no orders and no execution; the retail platform's defining loop starts at order entry.
10. **Historical note**: the phone-order brokerage relationship contains no self-directed electronic surface and therefore does not instantiate this Type — useful for the historical check, not a boundary against an existing leaf.

## Uncertainties

- eToro (social/copy-trading pole) and Trading 212 unreachable — the copy-trading variant is recorded only structurally, not from product evidence; Robinhood's surface details beyond navigation are unverified (help center JS-rendered, same limitation as the brokerage pass).
- Robinhood "Social" and "Agentic Trading" are nav items only; their mechanics are unverified and deliberately not described.
- US day-trading regime details (exact thresholds/windows) not asserted — marketing banner only.
- Fee/limit figures observed (Zerodha ₹20/₹40, Webull 0.1% bracket rule, GTC ~90 days) are product-specific facts kept in research notes; no numeric claims carried into the final document except where needed as clearly-marked single-product examples — none carried.
- Whether social/copy trading is becoming a standard layer cannot be determined from this sample (2 of 4 products show community surfaces; 1 unreachable product is the known copy-trading exemplar).

## Final Synthesis

The Retail Trading Platform is the individual's self-directed trading loop made software: a personal surface over a tradeable instrument universe with prices, where the person finds an instrument, reads its market, constructs and submits an order as a human decision, the order executes for real through broker/exchange infrastructure, and the resulting positions/holdings with P&L return as the state the next decision starts from. Around that loop, mature products add watchlists, charts, order vocabulary (conditional/group orders, validity), order-lifecycle visibility, alerts, funding linkage, eligibility-gated asset classes, margin, multi-surface delivery, and — variably — paper trading, recurring investing, fractional shares, extended hours, IPO access, research depth, community, APIs, and managed modes. The account relationship is presupposed, not administered (Brokerage Platform); the workspace density of professional trading is not the center (Professional Trading Terminal); the decision at trade time is human, not encoded (Algorithmic Trading Platform); execution is real, not simulated (simulators) or absent (data/news/research products); and crypto asset classes ride on separate licensed entities rather than converting the product into an exchange. The market persistently ships this Type merged with, laddered over, or split from the brokerage platform — the center-of-gravity test separates the Types while expecting straddling products.
