# Research Notes — Professional Trading Terminal

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Professional Trading Terminal actually is as an Application Type: the objects it manages, the loop a professional trader runs through it, the surfaces it exposes, the rules that govern order and risk behavior, and where it separates from neighboring trading-related Types (Retail Trading Platform, Brokerage Platform, Algorithmic Trading Platform, Financial Market Data Terminal, Portfolio Management System).

## Initial Boundary

Initial hypothesis (to be verified, not asserted):

- A professional trading terminal is a trader-facing workstation: live multi-instrument market state + direct order routing + real-time position/P&L, arranged in a user-configured workspace.
- The human makes the trading decision at trade time (vs Algorithmic Trading Platform, where an encoded decision loop decides).
- It does not administer accounts/custody (vs Brokerage Platform) and does not stop at data/analytics (vs Financial Market Data Terminal).
- Nearest confusion risks: broker-attached "pro" surfaces (straddle with Retail Trading Platform), data terminals with execution add-ons (Bloomberg Terminal pattern), terminals with hosted algos (straddle with Algorithmic Trading Platform).

Prior sibling note to honor (from research/algorithmic-trading-platform.md §Boundary Findings): conditional order types (stop/bracket/OCO) are order-management primitives, not strategies; the structural test is who makes the trading decision at trade time; brokerage-embedded algo platforms straddle Brokerage Platform and this leaf — joint review flagged for Retail Trading Platform / Professional Trading Terminal / Brokerage Platform.

## Research Questions

1. What objects exist in the system (instrument, quote/depth/trades, order, fill, position, account/P&L, workspace)?
2. What order-entry surfaces exist (ladder/DOM, ticket, chart trading, hotkeys, grid)?
3. What is the order lifecycle, and how do amend/cancel/flatten work?
4. How do positions and P&L update (marking, realized/unrealized)?
5. How is market data gated (entitlements/enablements)?
6. What risk controls exist (pre-trade checks, kill switch, cancel-all, confirmations)?
7. What is the connectivity model (broker-attached, independent vendor, FIX/service bureau, multi-broker)?
8. Is simulated/mock trading a standard part?
9. What is vendor-specific (spread engines, algo hosting, OMS modules, order-flow analytics)?
10. Where are the boundaries vs the five neighboring Types?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence level |
|---|---|---|
| Trading Technologies (TT) | independent institutional vendor; futures-first; ladder-centric; platform suite (OMS, clearing, surveillance) | Tier-1 help library (fetched) |
| CQG | futures data + execution specialist; web-based; broker/FCM-attached | Tier-1 online help (fetched) |
| Quantower | modern broker-neutral desktop; multi-asset; community-driven; per-seat licensing | Tier-1 help center + product page (fetched) |
| DAS Trader Pro | equities direct-access terminal; Level II / hotkey philosophy; broker & prop-firm service bureau | Tier-1 product site (fetched) |

Attempted but unreachable (source-access limitation — no operational claims made from them):

- Interactive Brokers TWS — interactivebrokers.com timed out ×2 (broker-native multi-asset workstation; positioning-level only)
- Sterling Trader Pro — sterlingtrader.com returned 525 ×2 (equities Level II prop/broker platform)
- MetaTrader 5 — metatrader5.com timed out ×2 (multi-asset terminal, retail-leaning)

Historical / market-sample check (§24): TT's predecessor X_TRADER (ladder-centric, no native charts in early eras), MetaTrader 4/5 ("terminal" is the vendor's own word), CQG Integrated Client (desktop lineage), RealTick-era direct-access terminals, broker-native platforms (TWS, thinkorswim), and regional futures terminals (e.g., China connectivity is an explicit CQG/TT solution area). All fit the same core loop; none require charting, order-flow analytics, or any single identity/connectivity model to qualify.

## Sources

Fetched 2026-09-06:

- TT Help Library — https://library.tradingtechnologies.com/ (full index; sections: Trade overview, Workspace Windows, Widgets, Preferences, Viewing Market Data, Basic Order Entry, Order Management, TT OMS, Options, Spread Trading, Analytics/Charts, Algo Trading, APIs)
- TT corporate site — https://www.tradingtechnologies.com/ (product scope: trading, post-trade, compliance, TCA, data, infrastructure)
- CQG Desktop product page — https://www.cqg.com/products/cqg-desktop
- CQG One / CQG Desktop online help — https://mhelp.cqg.com/cqg-desktop/overview and https://mhelp.cqg.com/cqg-desktop/trading
- Quantower product page — https://www.quantower.com/
- Quantower help center — https://help.quantower.com/quantower/trading-panels/dom-trader.md and https://help.quantower.com/quantower/sitemap.md
- DAS Inc product site — https://dastrader.com/ (DAS Trader Pro, MTS, RMAc, FIX/API, market data, connectivity)

Not reachable (limitation recorded; assertions kept generic):

- interactivebrokers.com (TWS) — timeout ×2
- sterlingtrader.com — 525 ×2
- metatrader5.com — timeout ×2

## Product A — Trading Technologies (TT)

### Key observations (evidence layer A unless noted)

- **Platform framing**: "multi-asset platform for capital markets" spanning futures/options, fixed income, FX, crypto; modules for trading, post-trade (TT Clearing, close-out & position reporting, allocation blotter), compliance (trade surveillance, risk management, MiFID II), TCA, data, infrastructure (global network, hosting).
- **Access**: browser access and TT Desktop; login with TT account, two-factor authentication; company membership ("Joining a company"); session status surface; "changing trading environments" (production vs mock/UAT).
- **Workspace**: user-created workspaces; multi-window and multi-monitor management; import/export workspaces; templates; workspace locking; widget groups; drag-and-drop instruments between widgets; tabs; widget settings/columns; zoom.
- **Instrument discovery**: search for an instrument; Market Explorer; Product Grid; tradable products reference.
- **Market data widgets**: Market Grid (multi-instrument quote grid with trading from the grid), Depth widget, Time & Sales (with order entry from T&S), Watchlist, PIQ (Position in Queue — queue position display).
- **Order entry surfaces**: MD Trader (price ladder/DOM with keyboard trading, laser lines, recentering, price-ladder adjustment), Order Ticket (floating/linked/unlinked; broker mode; custom action buttons; cross trades; block trades; RFQ), chart trading (enter/modify/cancel orders on a chart), trading from Market Grid/Product Grid/Spread Matrix.
- **Order types**: TT Order Types (bracket, iceberg, if-touched, OCO, retry, stop, time duration, TWAP, time sliced, timed, trailing limit, volume duration, volume sliced, with-a-tick, autohedger, order-by-volatility, sniper, multi-level bracket, conditional OMA, theo-based MMA types) + TT Premium Order Types (POV, TWAP+, VWAP+, Prowler, Splicer, Scale POV, Brisk, Close) — synthetic order types hosted by TT; templates; per-exchange support lists.
- **Order management**: Order Book (monitor working orders, modify, delete, place orders on hold, monitor rejected orders, confirm fills, review/approve orders, upload orders via CSV), Floating Order Book, Fills widget (filter, confirm, historical fills, export/download/print, manual fills), Orders and Fills (allocate fills to different accounts), Audit Trail (filter, historical data; Fill and Audit Trail Service), Audit Query.
- **Positions & accounts**: Positions widget (how P/L is calculated; positions matrix view; display by group/product group), Position Manager (manual fills, SOD — start-of-day positions, preview/upload), Account List, Balances, Account & User Restrictions (exportable).
- **Risk / control**: Order Profiles with Soft Limits (pre-trade limit profiles uploaded to TT); Routing Rules (route order portions to destinations); Account & User Restrictions; Options Risk and Risk Matrix (scenarios); review-and-approve order flow in Order Book.
- **Institutional modules**: TT OMS — care orders (submit, claim/unclaim, approve/reject, stitch/split, bulking, order passing, night desk support, FIX care-order rejections), Lock and Release; Blocktrader (wholesale/block trades per exchange: CME R-Cross, Eurex/EEX, Euronext, HKEx OTC, ICE, JPX J-Net, LME cross, SGX, NZX…); RFQ flows.
- **Spread trading**: Autospreader (synthetic spreads, spread configuration, rules engine, reload/sniper/queue-holder orders, custom spread formulas, decimal ratios); Spread Matrix (inter-product spreads, exchange-listed spreads).
- **Analytics**: Charts (chart types, chart trading, export chart data, settings); options chain, vol curve manager, options trade monitor, Electronic Eye, options risk.
- **Automation/APIs**: ADL (visual algo definition language; Time And Sales block etc.), TT REST / TT .NET SDK / TT Core SDK, Excel linking (RTD), FIX services; algo trading section.
- **Sim**: Mock Trading Support; UAT environment; trading environments switch.
- **Alerts**: Alert Manager and Alert Viewer; alerts creatable from Market Grid and Order Book.

## Product B — CQG

### Key observations

- **Framing**: "trading, market data, charting, and analytics all in one"; web-based (HTML5/Protobuf/WebSockets); product family (Integrated Client, QTrader, One, Desktop, Mobile, APIs, Spreader); "robust cloud infrastructure … standard for data quality in the futures industry since 1984" (vendor claim).
- **Workspace**: pages (tabs) with widgets; add/reorder/rename pages; templates; drag-and-drop widget arrangement; full-screen widget; "window out of page" floating browser windows; per-widget task menus; preferences (language, theme, notifications).
- **Account**: "In live mode, your trading account number from your broker/FCM is displayed here" — the terminal is attached to a broker/FCM account.
- **Entitlements**: "Symbols, markets, and order types available depend on a trader's own enablements and trading application" (help disclaimers); multiple features require explicit enablement (trailing orders, CQG Algos "contact your broker/FCM for access", XL Toolkit "contact their FCM and request the XL Toolkit enablement").
- **Trading surfaces**: HOT (Hybrid Order Ticket) — price-scale interactions: drag & drop to place stop/limit, buy/sell buttons, buy/sell columns, order modification/cancel from the scale, scale compression for illiquid markets, order size presets, best bid/ask highlight, recent-trade dots; Spreadsheet Trader (multi-instrument quotes + expandable DOM rows + trading toolbar); Slide Trader (quantity by lots / $ cost / % of available cash); chart trading; DOMTrader (trademark).
- **Order types**: server-side bracket orders & OCOs (enablement-gated, ticks-based target/stop), trailing limits/stops (cannot change price after placement), iceberg orders (display quantity vs total; venue support listed: Globex, ICE, Montreal, BrokerTec), post-only orders (certain markets), Go Market (convert working limit/stop to market), sweep mode (high-impact; must be explicitly enabled per symbol; forced confirmation window with cumulative size warning).
- **Position management**: Go Flat per symbol (cancel working orders / liquidate position); Accounts widget Go Flat / Liquidate all / Cancel all (must be enabled in preferences); allocation account configuration (allocation orders must be a multiple of configured lots, else rejected).
- **Views**: Orders, Positions, Accounts widgets; account filter (multiple/all accounts); account linking (Account Summary pushes account to Orders/HOT); color highlighting; quick filters; historical order search (30-day presets); manage columns.
- **Fills**: download today's fill report as CSV; fill-report popup actions (duplicate order, add stop loss, add OCO bracket).
- **Strategy/spread**: Strategy Builder and User-Defined Strategies (UDS); Spreader (same core as CQG Spreader in IC); synthetic spread parameters; CQG Algos (named algos: TWAP, VWAP, Iceberg, Peg, Snipe, Arrival Price, Roll, Vola…; parameters via CSV; broker/FCM enablement).
- **Excel**: XL Toolkit batch orders (parked or sent; algo orders with CSV parameters; login with trading credentials).
- **Other widgets**: quotes (QSS quote board), charting, options, symbols, formulas, alerts, news; mobile companions (iOS/Android); Hedge Management System (commercials/producers — separate product).

## Product C — Quantower

### Key observations

- **Framing**: "multi-asset & multi-connect trading platform for any trader and free to start"; broker-neutral; "60+ connections" (brokers, crypto exchanges, data feeds, technology providers, prop-trading); simultaneous connections in one environment; per-seat licensing (free version / trial / All-in-One); Windows desktop.
- **Workspace**: panels as separate windows; panels organized in groups, binds, workspaces; templates; set-as-default; link panels by color (symbol linking); custom hotkeys (terminal-wide and panel-specific); setup actions & advanced filters (behavior on data change); notifications center; themes editor; backup & restore manager.
- **Connections**: Connections manager (select integrations, connect with accounts); documented connection guides (CQG/AMP, Rithmic, ProjectX prop firms, Topstep, Binance, Bybit, Interactive Brokers, cTrader brokers, OANDA, FXCM, OKX, Hyperliquid, IQFeed, MetaStock); symbol mapping manager (receive data from one broker, trade with another).
- **Analytics panels**: Chart (many chart types incl. tick/renko/Heikin Ashi/Kagi/P&F/range/volume bars; indicators; drawing tools; volume analysis: cluster/footprint charts, volume profiles, time statistics, historical T&S; VWAP/anchored VWAP; power trades), Watchlist, Time & Sales, Price Statistic, DOM Surface, TPO Profile, Option Analytics, Market Heat map, Stat matrix, Exchange times, Quote board, News (RSS), Browser.
- **Trading panels**: DOM Trader (depth ladder; three order-entry modes: mouse trading on the ladder, order entry sidebar with bracket SL/TP, hotkeys; positions bar with contracts/average price/live P&L/liquidation price; configurable columns incl. imbalance, liquidity changes, cumulative size; scalping setup guide), Market depth (single-click order entry), Order Entry panel, Multiple Order Entry (predefined order lists sent individually or as a list), Chart Trading (visual trading on chart), FX Cell, Copy Trading (parent/child accounts within one exchange/broker), Trading Simulator (emulate execution under any connection, including non-trading ones), Market Replay (history player for practice/backtest).
- **Order types**: order types documentation ("how an order behaves when it enters the market"); order placing strategies incl. Local SL/TP (platform-side stop loss/take profit for connections that don't natively support them).
- **Portfolio panels**: Positions (open positions, P/L, prices), Working Orders, Trades (trading history), Orders History, Synthetic Symbols (create non-standard instruments/spreads, tradeable), Historical Symbols (import third-party history).
- **Account panels**: Account info (balances, margin, key metrics; option to lock trading per account), Account performance (statistics), Crypto balances, Currencies exposure, Event log, Reports (from broker, filtered by account/date).
- **Risk**: Risk Management panel — "Create risk plan templates with daily profit and loss limits, max order and position sizes, then assign them to any account or connection."
- **Automation**: Quantower Algo (C# indicators/strategies/plugins/connectors; strategies manager; backtest & optimize; access to Level2 data, volume analysis, trading operations via API); Excel RTD export; Telegram bot notifications; open GitHub repo.
- **Misc**: Futures Rollover (roll contracts before expiration, keep drawings valid), History Exporter (CSV), Sessions manager, Live support chat.

## Product D — DAS Trader (Pro)

### Key observations

- **Framing**: "Direct Access Software"; end-to-end electronic trading for brokerage and trading community; clients: broker/dealers, clearing firms, online brokers, institutional trading desks, traders; certified service bureau & market data vendor (Nasdaq, NYSE, CBOE, IEX, OTC, OPRA).
- **Market data**: Level 1 for US equities/options/select futures; Level 2 in DAS Trader Pro and mobile (Nasdaq Totalview, ArcaBook, IEX DEEP, OTC Markets, OPRA); regional feed; custom feeds.
- **Connectivity**: low-latency order validation to US exchanges; direct market access and service-bureau FIX connectivity; order routing to 100+ destinations; access to NYSE floor brokers, routing strategies, algos, dark pools, liquidity providers; collocation at Nasdaq (DAS HUB); DMAr smart router.
- **DAS Trader Pro** (the terminal): "advanced order types, charting, and multi-account management in a real-time environment"; collocated order executions; multiple stop types; real-time account management; multiple monitors; advanced charting; equities and options. Community/testimonial-visible surfaces: hotkey scripting ("robust hotkey scripting"; buy-hotkey with %-based limit and trailing stop), Level 2 boxes, ECN book, multiple time & sales windows, top-20 list, short locate monitor window, replay-mode practice.
- **Simulator**: "Real-Time Simulator" subscription; test-trade widget ("send orders, view real-time market data, set up alerts and hot keys"); 14-day trial.
- **Institutional layer**: DAS Trader MTS — omnibus master/sub-account order & risk management platform for institutions (all sub-accounts transmitted under one master; master controller monitors all sub-account transactions; pre-trade risk management applied); Trade Reporting Tools (Report Center; IBOSS multi-account back office; OATS/CAT, TRACE, ACT reporting; SEC 605/606; EOD and real-time drop copies; pre-trade alert reporting for SEC 15c3-5).
- **Risk administration (RMAc)**: single GUI administering permissions/access/trading rights for Rule 15c3-5 market-access clients: MPID-level control, risk-check violation handling, hierarchical risk profiles, event logging/notification, EOD log file, **kill switch**, Reg NMS (ISO/minimum pricing increments), exchange/venue and asset-type trading allowances, entry-type allowance, Reg SHO rules, symbol restrictions, user/account restrictions, **mass order cancellation**, order-by-order checks (maximum price discrepancy, SOQ/SOV, order throttle, duplicate orders).
- **API**: DAS FIX/API (DMA to market destinations; advanced order types, execution reports, order status, positions, liquidity flags, account balances); DAS API for front-ends.
- **Delivery**: Windows desktop (hardware requirements page), ActiveWeb (HTML5 browser platform), iPhone/Android/Mobile Web companions.

## Cross-product Comparison

| Dimension | TT | CQG | Quantower | DAS Trader Pro | Layer |
|---|---|---|---|---|---|
| Live multi-instrument market state | Market Grid, Watchlist, Depth, T&S, PIQ | QSS quote board, Spreadsheet Trader, HOT depth | Watchlist, Quote board, Market depth, T&S, DOM Surface | Level 1/Level 2 quotes, T&S windows, top-20 list | B |
| User-arranged workspace | Workspaces, widgets, multi-monitor, templates, import/export | Pages, widgets, templates, floating windows | Workspaces, panels, binds, groups, templates | Layouts, multiple monitors | B |
| Depth-of-market ladder as order-entry surface | MD Trader (keyboard trading) | HOT (drag & drop, buy/sell columns) | DOM Trader (mouse trading, hotkeys) | Level 2 box + hotkey-driven entry | B |
| Order ticket | Order Ticket (floating/linked/broker mode) | HOT (Hybrid Order Ticket) | Order Entry panel; Multiple Order Entry | order entry + hotkey scripting | B |
| Chart trading | Charts with enter/modify/cancel on chart | chart trading | Chart Trading + visual trading settings | advanced charting (order entry from charts per testimonials) | B |
| Working-order management | Order Book (modify/delete/hold/rejects/approve) | Orders widget, Order Info (modify/cancel), Go Market | Working Orders panel | order management in real-time environment | B |
| Fills / trade history | Fills widget (confirm/export/manual fills), Audit Trail | Fill report CSV download; fill-popup actions | Trades, Orders History, History Exporter | Report Center (orders/trades historical) | B |
| Positions & P&L | Positions widget (P/L calc documented), Position Manager (SOD/manual fills) | Positions widget; Go Flat/Liquidate | Positions panel; positions bar in DOM (avg price, live P&L) | real-time account management | B |
| Account/balances | Account List, Balances, Account & User Restrictions | Accounts widget; account number from broker/FCM | Account info (balances, margin; lock trading per account) | multi-account management; MTS master/sub | B |
| Hotkeys / keyboard trading | Hotkeys preferences; keyboard trading in MD Trader | keyboard-driven HOT interactions | Custom hotkeys (terminal-wide + panel) | hotkey scripting (signature feature) | B |
| Symbol linking across windows | drag-and-drop instruments between widgets; chart↔options-chain linking | link groups (colors) push symbols/accounts | Link panels by color | (not confirmed from fetched docs) | B |
| Alerts | Alert Manager/Viewer; alerts from grid/order book | Alerts section in help | Alerts log; setup actions | alerts + hot keys (test-trade widget) | B |
| Sim / mock trading | Mock Trading; UAT; trading environments | demo environment (mdemo); (sim naming not confirmed) | Trading Simulator; Market Replay | Real-Time Simulator; replay mode | B |
| Market-data entitlements | (implied by exchange data model; not explicitly fetched) | explicit: "enablements" gate symbols/markets/order types/features | connection-level: broker/feed accounts determine data | exchange-specific data subscriptions (Totalview/ArcaBook/IEX DEEP/OPRA) | B |
| Pre-trade risk controls | Order Profiles w/ Soft Limits; Account & User Restrictions; order review/approve | enablement-gated features; allocation rules; sweep confirmations | Risk Management panel (daily P&L limits, max order/position sizes per account/connection) | RMAc (15c3-5 risk checks, kill switch, mass cancel, throttles, price-discrepancy checks) | B |
| Conditional order types | TT Order Types (bracket/OCO/iceberg/trailing/sliced/TWAP…) | server-side brackets/OCO/trailing/iceberg/post-only | order types + Local SL/TP (platform-side) | multiple stop types; advanced order types | B |
| Multi-account / institutional | TT OMS care orders; allocation blotter; Blocktrader | allocation accounts; account linking | Copy Trading (parent/child) | MTS omnibus master/sub; IBOSS | B |
| Spread/synthetic instruments | Autospreader; Spread Matrix; synthetic spreads | Spreader; UDS; Strategy Builder | Synthetic Symbols | (not confirmed) | B |
| Algo hosting / scripting | ADL; TT SDKs; Excel autotrader | CQG Algos (enablement); XL Toolkit | Quantower Algo (C#); backtest | FIX/API; DAS API (dev environment) | B |
| News inside terminal | (not prominent in fetched pages) | news solutions; RSS in Desktop | RSS news panel | streaming news (Newsware) | B |
| Delivery form | browser + desktop | web (HTML5) + mobile apps | Windows desktop | Windows desktop + web + mobile | B |
| Connectivity posture | independent vendor platform (own network/gateway) | independent vendor attached to broker/FCM accounts | broker-neutral client (bring your connection) | service bureau behind brokers/prop firms | B |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately small)

A Professional Trading Terminal is recognizable by four properties together:

1. **Live market state for multiple instruments, arranged by the user** — real-time quotes (and, in practice, depth) presented in a user-configured workspace of simultaneous instrument views that persists across sessions.
2. **Direct order construction and routing** — the user composes orders (place, amend, cancel) and sends them to execution venues or broker backends from within the same surface that displays the market.
3. **Real-time position and P&L/account state for the user's own trading** — fills update positions and profit/loss continuously against live marks.
4. **The human makes the trading decision at trade time** — the terminal is the instrument of a human trader's decision loop, not a strategy runtime.

Remove (1) → it is a blind order gateway, not a terminal. Remove (2) → it is a market-data terminal. Remove (3) → it is a charting/analysis tool. Remove (4) → it is an algorithmic trading platform. Remove the multi-instrument workspace character → it degrades into a single-instrument trading widget, not a terminal.

### L1 — Common Mature Structure (very common, not defining)

- Depth-of-market ladder (DOM) as an order-entry surface (click/drag on price levels)
- Charting with chart trading (orders placed/managed on the chart)
- Order ticket as a form-based entry surface
- Working-order management (order book/blotter: modify, cancel, cancel-all, reject visibility)
- Fills view and trade/order history with export
- Positions view (per-instrument aggregation, average price, realized/unrealized P&L) and account/balances view
- Hotkeys / keyboard trading
- Symbol linking across windows (color/link groups)
- Price/condition alerts
- Simulated/mock trading environment or demo mode
- Market-data entitlements gating what a user sees (per exchange/feed/feature)
- Pre-trade risk controls in some layer (platform-side limits, firm-side risk administration, or broker-side checks)
- Conditional order types beyond market/limit/stop (bracket, OCO, trailing, iceberg) — implemented venue-side, broker-side, or platform-side
- Multi-account support (allocation, master/sub, copy)
- Audit trail / order-and-fill records

### L2 — Variant / Optional Structure

- Asset-class center of gravity: futures-first, equities Level II-first, multi-asset, FX/CFD, crypto
- Connectivity posture: independent vendor platform with own gateway/network; broker-attached (account numbers from broker/FCM); broker-neutral multi-connection client; service bureau behind brokers/prop firms
- Delivery form: native desktop, browser, mobile companion
- User tier: institutional desk (OMS integration, approvals, allocation) vs independent professional
- Interface philosophy: ladder-first, chart-first, Level II-first, grid-first
- Order-flow analytics (footprint/cluster charts, volume profile, TPO, delta) — futures/equities-active niche
- Spread/synthetic instrument engines
- Strategy scripting/backtesting inside the terminal (boundary pressure toward Algorithmic Trading Platform)
- Options analytics (chains, Greeks, risk matrix)
- News inside the terminal
- Market replay / backtesting
- Regional/venue specifics (China connectivity, wholesale/block trades, RFQ workflows)
- Business model (per-seat license, broker-bundled, exchange/data pass-through fees)

### L3 — Vendor-specific (research notes only)

- TT: MD Trader ladder, Autospreader/ADL, care orders, PIQ, Order Profiles, TT OMS, Blocktrader, Premium Order Types
- CQG: HOT (Hybrid Order Ticket), DOMTrader/TFlow trademarks, Slide Trader, CQG Algos catalog, XL Toolkit, Hedge Management System
- Quantower: Binds, DOM Surface, Symbol Mapping, Telegram bot, themes editor, panel naming
- DAS: RMAc, MTS, hotkey scripting language, short locate monitor, top-20 list, Report Center/CAT reporting
- Marketing figures (Quantower "60+ connections", DAS "100+ destinations", CQG "since 1984") are vendor claims — not generalized.

## Vendor-specific Findings

See L3. Additionally: TT's ladder design is patented (CQG's help page licenses TT ladder patents — evidence the ladder is a distinctive, long-standing structure, not a generic UI). CQG's "enablement" model (features unlocked by broker/FCM request) is a distribution detail, though the underlying pattern (entitlements gate data/features) is cross-product.

## Boundary Findings

**vs Retail Trading Platform** (sibling, unprocessed — joint-review flag): both share instrument/quote/order/position objects. The retail platform is account-centric (funding, statements, simple order flows, consumer onboarding); the professional terminal is market-centric (workspace of live instrument views, depth/ladder/hotkeys, direct routing, entitlements, risk administration). Straddles are real: broker-native platforms ship pro-grade surfaces (TWS, thinkorswim pattern), and prop-firm retail traders use pro terminals. Structural test: where does the surface's center of gravity sit — the account relationship or the live trading workspace? Held as separate Types; straddling products noted.

**vs Brokerage Platform**: the brokerage platform owns the account relationship (onboarding, custody, money movement, statements, corporate actions). The terminal routes orders and displays state; it does not administer the account. Evidence: CQG displays "your trading account number from your broker/FCM"; DAS is a service bureau behind brokers; Quantower connects to brokers. A terminal without a brokerage behind it cannot settle anything. Held.

**vs Algorithmic Trading Platform** (honors prior sibling note): the structural test is who makes the trading decision at trade time. Conditional order types (stop/bracket/OCO/trailing/iceberg) are order-management primitives present in terminals and do not make them algo platforms. Some terminals host user scripts/strategies (Quantower Algo, TT ADL, CQG Algos) — a straddle; the terminal remains the manual surface, the algo runtime is a module. Boundary held on the human decision loop as the Type center.

**vs Financial Market Data Terminal**: a data terminal's center is market state/news/analytics/communication without order routing (Bloomberg Terminal pattern). The professional terminal adds order construction/routing and position/P&L closure. Terminals adding news (Quantower RSS, DAS Newsware) and data terminals adding execution add-ons are drifts, not identity changes. Test: remove order routing → data terminal. Held.

**vs Portfolio Management System**: PMS treats holdings as longer-lived investment records for portfolio-level management/attribution (PM user); the terminal treats positions as live intraday/exchange-traded state driven by the trader's own fills (trader user). Different object horizon, different user, different loop. Held.

**vs Order/Execution Management System (concept; no dedicated directory leaf)**: institutional order workflow (care orders, allocation, approvals) appears inside terminal suites (TT OMS) as a module; the terminal seat remains the trader's live surface. Noted as module-vs-Type, not a directory conflict.

**"去掉什么就变成另一个 Type" 判据**:
- 去掉 order routing → Financial Market Data Terminal
- 去掉 human decision loop（决策由编码策略做出）→ Algorithmic Trading Platform
- 去掉 live trading loop、只留账户关系 → Brokerage Platform
- 去掉 pro 数据面/工作台密度、只留账户中心的简单下单 → Retail Trading Platform
- 去掉 multi-instrument workspace → 单品种交易小部件，不再是 terminal

## Uncertainties

- IBKR TWS / Sterling Trader Pro / MetaTrader 5 unreachable — the broker-native and retail-leaning straddle postures are reasoned from the sampled products and prior sibling research, not from those vendors' docs. No operational claims made for them.
- Symbol linking in DAS not confirmed from fetched docs (marked in comparison table).
- Precise entitlement mechanics per product (which exchanges/fees/features) not researched — deliberately not asserted.
- Regional terminals (e.g., Chinese futures terminals) not fetched; the historical/regional fit of the L0 is an inference from the sampled products' breadth (CQG/TT China connectivity pages) and the Type's long lineage, kept qualitative.
- Whether "pre-trade risk controls" should be L1 or L2: all four sampled products expose some risk-control layer, but its location (platform vs firm vs broker) and depth vary widely; kept in L1 with explicit qualification, depth details left to variants.

## Final Synthesis

The Professional Trading Terminal is the professional trader's live workstation: a user-arranged, multi-instrument workspace of real-time market state (quotes, depth, trades), coupled in the same surface to direct order construction/routing and to real-time position/P&L/account state, with the human making the trading decision at trade time. Everything else — ladders, chart trading, hotkeys, alerts, sim modes, entitlements, risk administration, spread engines, algo hosting, OMS modules — is mature structure or variant structure layered on that loop. The Type is separable from Retail Trading Platform (account-centric), Brokerage Platform (account administration), Algorithmic Trading Platform (encoded decision loop), Financial Market Data Terminal (no order routing), and Portfolio Management System (investment-record horizon), with acknowledged straddling products at each seam.
