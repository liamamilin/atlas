# Research Notes — Algorithmic Trading Platform

## Research Goal

Understand what software sits under the directory leaf "Algorithmic Trading Platform" (§08 Finance, Banking, Insurance & Investment, listed between "Professional Trading Terminal" and "Financial Market Data Terminal"): what its core objects are, how a trading strategy is expressed and executed, how the strategy lifecycle (author → test → deploy) works, what risk/monitoring structures exist, and where the boundary lies against Retail Trading Platform, Professional Trading Terminal, Brokerage Platform, Financial Market Data Terminal, and the institutional execution-algo world.

## Initial Boundary (hypothesis before research)

- Hypothesis: an Algorithmic Trading Platform is software where trading decision logic is expressed as an executable artifact (code, formula, or visual program) and the platform runs that logic against market data, generating and managing orders automatically — the human decides the *rules*, the machine decides each *trade*.
- Likely neighbors: Retail Trading Platform (manual order entry), Professional Trading Terminal (manual, professional-grade), Brokerage Platform (account + market access), Financial Market Data Terminal (data/observation), charting platforms with strategy scripting (signals without managed execution), institutional EMS/OMS with execution algos (TWAP/VWAP order slicing — a different sense of the word "algo"), Robo-advisor (automated but vendor-authored strategy).
- Known ambiguity going in: "algorithmic trading" has two market senses — (1) strategy algos: user-authored decision logic that decides what/when to trade; (2) execution algos: broker/EMS-side order-slicing logic (TWAP/VWAP/POV) that decides *how* to work a given order. The leaf is expected to be sense (1), with sense (2) appearing as an institutional capability inside some platforms.
- Key unknowns: how backtest→live continuity is handled; whether venue connectivity is definitional or common; how risk controls are exposed; how much the Type depends on any one authoring surface (code vs visual vs parameters).

## Research Questions

1. How is a trading strategy expressed in each product (code language, formula language, visual builder, parameterized template)?
2. What is the runtime loop: data in → signal → order out → position management?
3. How does the platform reach the market (embedded broker, broker-agnostic gateways, FIX/network, API)?
4. What role does backtesting play, and how does a strategy move from backtest to live?
5. What simulation/paper-trading forms exist?
6. What risk controls, monitoring, and intervention surfaces exist for running strategies?
7. Who uses it (individual vs institutional) and how does that shape the product?
8. Where is the boundary vs manual trading platforms (order types vs strategies), vs charting platforms with alerts, vs broker APIs?
9. Historical check: do older/regional products (1990s system-trading software, MetaTrader-era terminals) fit the same definition?

## Representative Products

| Product | Philosophy | Tier | Why sampled |
|---|---|---|---|
| QuantConnect | cloud-native, code-first (Python/C#), open-source LEAN engine, research→backtest→live | individual quants → institutions | clearest full-lifecycle cloud platform; rich official docs |
| MultiCharts | desktop, chart-centric, trading-specific language (EasyLanguage-compatible), broker-agnostic | retail/prosumer | classic design→backtest→optimize→automate desktop pipeline |
| Trading Technologies | institutional execution network, preconfigured execution algos + visual (ADL) and SDK authoring | institutional | institutional tier; shows the execution-algo sense of "algo" |
| AmiBroker | desktop, array-processing formula language (AFL), analysis/backtesting-first | retail/prosumer, long-lived (since 1995) | historical-depth check; formula-language philosophy |
| Alpaca (boundary probe) | API-first brokerage "built for retail, algorithmic and proprietary traders" | retail/developer | boundary probe: market pipe without strategy runtime |

Rejected/considered: MetaTrader 4/5 (retail-dominant, MQL Expert Advisors) — official docs unreachable (see Sources); NinjaTrader, TradeStation, cTrader, TradingView, Interactive Brokers — unreachable in this environment; used only as structural references where noted.

## Sources

Fetched 2026-09-06 (all Layer A unless noted):

- QuantConnect — Documentation root: https://www.quantconnect.com/docs/v2/
- QuantConnect — Writing Algorithms: https://www.quantconnect.com/docs/v2/writing-algorithms
- QuantConnect — Cloud Platform / Live Trading: https://www.quantconnect.com/docs/v2/cloud-platform/live-trading
- MultiCharts — home: https://www.multicharts.com/
- MultiCharts — Algorithmic trading: https://www.multicharts.com/features/algorithmic-trading/
- MultiCharts — Automated trading: https://www.multicharts.com/features/automated-trading/
- Trading Technologies — home: https://tradingtechnologies.com/
- Trading Technologies — Algo Trading: https://tradingtechnologies.com/trading/algo-trading/
- AmiBroker — User's Guide contents: https://www.amibroker.com/guide/
- AmiBroker — AFL specification: https://www.amibroker.com/guide/AFL.html
- AmiBroker — Understanding how AFL works: https://www.amibroker.com/guide/h_understandafl.html
- Alpaca — Docs home (boundary probe): https://docs.alpaca.markets/

Source-access limitations (2026-09-06):

- metatrader5.com timed out ×2; mql5.com timed out ×1 — MetaTrader family abandoned as a direct sample; no official-doc claims made for it.
- ninjatrader.com help (404 ×2, 500 ×1), tradestation.com help (404 ×2), help.ctrader.com (transport error), tradingview.com Pine docs (transport error), interactivebrokers.com TWS API docs (timeout) — all abandoned after repeated failures.
- Consequence: the retail-terminal family (MetaTrader/NinjaTrader/TradeStation/cTrader) is characterized structurally from the sampled products' shared pattern and from MultiCharts' explicit EasyLanguage compatibility; no product-specific operational claims are made for the unreachable products.

## Product Observations

### QuantConnect (Layer A — official docs)

- Self-description: "open-source, community-driven algorithmic trading platform"; trading engine powered by LEAN, "cross-platform, multi-asset"; supports Python and C#.
- Documentation structure (Writing Algorithms): Key Concepts (Algorithm Engine, Event Handlers, Time Modeling, Security Identifiers), Initialization, Securities (requesting/handling data; asset classes: US Equity, Equity Options, Crypto, Crypto Futures, Forex, Futures, Future Options, Index, Index Options, CFD, India Equity), Portfolio (Holdings, Cashbook), Universes (dynamic security selection: liquidity/fundamental/ETF-constituents/alternative-data/custom), Datasets (large vendor catalog), Consolidating Data (time/calendar/count/Renko/range consolidators feeding indicators), Historical Data (history requests, warm-up periods, rolling windows), Trading and Orders (order tickets, transaction manager; order types: market/limit/stop/OCO-family/combo/option-exercise; pre-trade risk control; position sizing; liquidating; order events/errors; trade statistics), Reality Modeling (trade fills, slippage, transaction fees, brokerage models, buying power, settlement, margin calls, short availability), Scheduled Events, Indicators (large library incl. candlestick patterns).
- Cloud Platform structure: Organizations (teams, tiers, resources, billing), Projects (IDE, collaboration, package environments, LEAN engine versions), Research (Jupyter environment), Backtesting (deployment, results, report, debugging, engine performance), Optimization (parameters, objectives, strategies), Live Trading (brokerages, deployment, notifications, results, algorithm control, reconciliation, risks), Object Store, Community, full REST API (compile, backtest, live management incl. stop/liquidate, live commands).
- Live trading: "A live algorithm is an algorithm that trades in real-time with real market data… run on co-located servers"; supported brokerages include Interactive Brokers, TradeStation, Tastytrade, Alpaca, Charles Schwab, Webull, Binance, Bybit, Kraken, Coinbase, Bitfinex, dYdX, Bloomberg EMSX/FIX, SSC Eze, Trading Technologies, Wolverine, FIX connections, CFD/FOREX brokerages; QuantConnect Paper Trading is a first-class brokerage option.
- The same strategy code runs across backtest and live; docs explicitly cover "Differences between backtesting and live trading" (Algorithm Control) and "Reconciliation".

### MultiCharts (Layer A — official product pages)

- Positioning: "Trading software for backtesting and algo trading"; "MultiCharts enables traders to design and execute high performance trading strategies."
- Algorithmic trading page: "Strategy trading has a number of significant advantages when compared to intuition-based trading. Institutional traders have been using trading strategies for a long time, and now these tools are also available for individual traders." Pipeline: **Design → Backtest → Optimize → Automate**.
- Strategy development: "you need to check [the idea's] validity, which requires programming the idea as a set of rules… It uses a coding language designed for trading rather than relying on a conventional programming language." EasyLanguage-friendly; also .NET (C#/VB) and Python (beta) interfaces.
- Strategy backtesting: "simulates your strategy on historical data and provides a backtesting report." Trading system analysis: "various performance ratios and descriptive ways of viewing the results." Optimization incl. genetic optimization and walk-forward testing.
- Automated trading: "Orders generated by a trading strategy in MultiCharts are sent directly to the broker's server. Then the broker responds with a message about the order status, and you can see on your chart if the trade was successful." Paper Trading broker profile for testing "before sending orders to your live account… no need to request a demo account."
- Strategy runtime access: strategies can read Level-2 depth (ten price levels each direction) and real-time account attributes (positions, average price, open PnL, equity).
- Execution model: "orders are sent at the close of the previous bar—instead of being sent at the moment when they appear on the chart," so fill prices correspond to chart prices. Order types: market, limit, stop, bracket, OCO/OCA. Unfilled-order replacement (e.g., convert unexecuted limit/stop to market after a set period) keeps strategy synchronized with the broker position.
- Auto-trading switch on the chart: green = live, grey = backtest mode; synchronous vs asynchronous auto-trading modes (synchronous plots entries/exits only after broker execution, keeping chart position = broker position; asynchronous plots on signal and may diverge unless order conversion is enabled).
- Order and Position Tracker: accounts, strategy orders, open positions, positions history, trade summary; fields include Filled/Cancelled status, Strategy Position vs Broker Position, Positions Match, Strategy P/L vs Open P/L; Log tab with broker/platform messages. Alerts: visual, audio, email.
- Trading Performance Report: "over 100 performance indices… including about 30 charts."
- Broker-agnostic: connects to many brokers/exchanges/data feeds (Interactive Brokers, TradeStation, Binance, Coinbase, Kraken, OKX, Bybit, Saxo, TT, Rithmic, dxFeed, IQFeed, etc.); symbol mapping window aligns data-feed symbols with broker symbols.
- Also: DOM with one-click trading, chart trading, drag-and-drop entry/exit strategies attachable to orders/positions, Portfolio Trader ("simulate and auto trade entire portfolios, which can contain 100's of stocks, futures, and other instruments"), market scanner, trading simulator with replayable historical data.

### Trading Technologies (Layer A — official product pages)

- Positioning: "The multi-asset platform for capital markets" (futures/options, fixed income, FX, crypto); Algo Trading page: "Easily build algorithms and get better execution of your automated trading strategies."
- Three-part structure: **Preconfigured** (TT Order Types; TT Premium Order Types — "intelligently driven premium order types"; Broker Algos made available through the platform; Third-party algos), **Build Your Own** (ADL® — "drag-and-drop building blocks to develop and test automated trading strategies"; TT Core SDK — "high-performance Linux C++ API"; TT Strategy Studio — "create, test and deploy complex multi-asset strategies through an ultra-low latency architecture"), **Backtesting** (P&L Testing — "replay up to a year of historical book data and simultaneously test multiple versions of your algos using different parameter settings"; Compliance Testing — "test your algos using market data from historically volatile market conditions to avoid deploying potentially disruptive algos into live markets"), **Execute** (colocation — "deploy algos to bare metal servers in colocated data centers"; TT Premium Services; Algo Dashboard — "monitor and manage your algos from virtually anywhere").
- Stated benefits mix both senses of "algo": "Automate the entry and exit of positions" (strategy sense) and "Reduce the market impact of large orders" (execution sense); also "Reduce the risk of manual errors", "Remove the emotional aspect of trading", "Reduce the transaction costs of trading".
- Related resources name Autospreader® (custom algos can "drive" it) and an Excel plug-in.

### AmiBroker (Layer A — official user's guide)

- User's Guide: "AmiBroker is equipped with a powerful formula language allowing you to write trading system rules, define your own indicators and custom commentaries" — AFL chapter covers language reference, built-in analysis functions, "automatic analyzer and formula editor", advanced portfolio backtester interface, custom backtester metrics, Equity function "analyzing your trading system performance".
- AFL execution model: "an array processing language. It operates on arrays (or rows/vectors) of data… quite similar to the way popular spreadsheets work." Each symbol has stored arrays for open/high/low/close/volume/open interest; all other arrays are calculated from formulas. Operators work on whole arrays "at full compiled-code speed".
- Signals as arrays: tutorial example defines `Buy = Cond1 AND Cond2` and `Sell = High > 1.30` as per-bar boolean arrays; "Buy and Sell are special arrays whose results can be displayed in the Analyzer window or on screen". Bar indexing from oldest (0) to newest (BarCount-1); `Ref()` for lookback; `IIF()` as array-valued conditional; `AMA()` recursive array function; loops (`for`/`while`, `if-else`) added in later versions for bar-by-bar logic.
- Product family marks: AmiQuote/AmiFeed (data companions); copyright 1995–2025 — a long-lived desktop product.

### Alpaca (boundary probe — Layer A, positioning only)

- Docs home: "Trading API — Stock trading for individuals and business accounts. Built for retail, algorithmic and proprietary traders." Also Broker API (build brokerage services) and Market Data API. No strategy authoring/runtime surface in the product; the algorithm lives in the customer's own code, which calls the API. This is the "market pipe without strategy runtime" pole.

## Cross-product Comparison

| Dimension | QuantConnect | MultiCharts | Trading Technologies | AmiBroker |
|---|---|---|---|---|
| Strategy expression | Python/C# code against a strategy API (event handlers) | trading-specific language (EasyLanguage-compatible) + .NET/Python | visual dataflow (ADL), C++ SDK, Strategy Studio | array-processing formula language (AFL) |
| Strategy artifact | project/algorithm (code files) | strategy applied to a chart | algo (deployed to runtime) | formula/analysis file |
| Data input | curated multi-asset datasets + live feeds | data feeds (broker-agnostic) + replay simulator | live book data; historical replay for testing | local/vendor databases of OHLCV arrays |
| Backtesting | first-class (results, report, debugging, engine performance) | first-class (report, 100+ indices claim) | P&L Testing (replay, parameter variants) + Compliance Testing | core purpose (portfolio backtester, custom metrics) |
| Optimization | parameter optimization (objectives, strategies) | optimization + genetic + walk-forward | parameter variants in P&L testing | custom backtester metrics (optimization not evidenced in fetched pages) |
| Paper/simulation | QuantConnect Paper Trading brokerage | Paper Trading broker profile + simulator with replay | "robust simulated matching engine" with live market data | (not evidenced in fetched pages) |
| Live execution | live algorithms on co-located servers; many brokerage integrations; stop/liquidate controls | auto-trading switch per chart; orders sent to broker server; sync/async modes | colocation, premium services; Algo Dashboard | (live auto-trading not evidenced in fetched pages) |
| Order/position monitoring | live results, algorithm control, reconciliation, notifications | Order and Position Tracker (strategy vs broker position, positions match) | Algo Dashboard | Analyzer window (analysis side) |
| Risk controls | pre-trade risk control (docs section) | unfilled-order replacement; position sync | compliance testing against volatile data | (not evidenced) |
| Broker relationship | platform-hosted integrations (brokers, FIX, EMS) | broker-agnostic gateways + symbol mapping | execution network; broker algos distributed through platform | data-vendor companions; (broker side not evidenced) |
| Audience | individual quants → institutions | retail/prosumer | institutional | retail/prosumer |
| Substrate | cloud (+ local LEAN CLI) | Windows desktop | vendor cloud/colo network | Windows desktop |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an Algorithmic Trading Platform:

1. **Executable strategy artifact** — trading decision logic (what/when/how much to trade, and how to manage the resulting position) encoded as a persistent, machine-runnable, user-authored or user-configured object: code, formula, or visual program.
2. **Market-data-driven evaluation** — the platform runs the strategy against market data (historical datasets for testing; live feeds for trading).
3. **Automated order generation and tracking** — strategy evaluation produces orders that the platform creates, submits, and tracks (with the resulting positions), without a human deciding each trade.

Remove #1 → a manual trading platform (human decides each trade). Remove #3 → a charting/analytics tool that merely signals. Remove #2 → nothing trade-related remains. The venue connection is deliberately NOT in L0: the same strategy artifact runs against a simulated fill model (backtest/paper) or a live venue, and the author→test→deploy pipeline over that one artifact is the Type's signature. Historical-data-only operation is the minimum viable form of the loop; live venue connectivity is the common mature completion (L1).

### L1 — Common Mature Structure

- **Backtesting** on historical data with performance reports/statistics (all four sampled products).
- **Strategy parameter optimization** (QuantConnect optimization; MultiCharts optimization incl. genetic and walk-forward; TT parameter variants).
- **Paper/simulated trading** (QuantConnect paper brokerage; MultiCharts paper profile + replay simulator; TT simulated matching engine).
- **Live deployment with venue/broker connectivity** (QuantConnect brokerage integrations; MultiCharts broker gateways; TT colocation network).
- **Order/position/account monitoring surfaces** (QuantConnect live results/algorithm control; MultiCharts Order and Position Tracker; TT Algo Dashboard).
- **Risk controls** (QuantConnect pre-trade risk control; MultiCharts unfilled-order replacement and position synchronization; TT compliance testing).
- **Technical indicator library** (QuantConnect indicator library; AmiBroker built-in analysis functions; MultiCharts indicator ecosystem).
- **Alerts/notifications** (MultiCharts visual/audio/email; QuantConnect notifications).
- **Charting as authoring/visualization surface** (MultiCharts, AmiBroker; QuantConnect provides charts in results).

### L2 — Variant / Optional Structure

- **Authoring surface**: trading-specific language (EasyLanguage/PowerLanguage family, AFL, MQL family), general-purpose code (Python/C#), visual dataflow builder (ADL), parameterized preconfigured algos.
- **Runtime locus**: user's desktop vs vendor cloud vs colocated low-latency servers.
- **Broker relationship**: embedded brokerage, broker-agnostic gateways, FIX/EMS connections, API-only access.
- **Asset-class focus**: futures-first, forex/CFD, equities/options, crypto, multi-asset.
- **Execution granularity**: bar-close evaluation vs tick-level vs low-latency colo deployment.
- **Execution algos** (order-slicing to reduce market impact of large orders) as an institutional capability — present in TT's preconfigured/premium order types; a distinct sense of "algo" whose primary home is EMS/OMS suites.
- **Portfolio-level strategy trading** (MultiCharts Portfolio Trader; QuantConnect multi-asset portfolio modeling).
- **Compliance testing** of algos against historically volatile data (TT).
- **Strategy marketplaces / pre-built strategies** (common in the retail-terminal family; not directly evidenced in the fetched sample).
- **Team/organization structures** for strategy development (QuantConnect organizations).

### L3 — Vendor-specific (research notes only)

- QuantConnect: LEAN engine, Organizations/Object Store/Research Pipeline, co-located cloud servers, REST API for compile/backtest/live management, AI assistance.
- MultiCharts: synchronous vs asynchronous auto-trading modes, symbol mapping, Order and Position Tracker field vocabulary, Portfolio Trader, genetic/walk-forward optimization branding.
- Trading Technologies: ADL®, TT Strategy Studio, Autospreader®, TT Premium Order Types, Algo Dashboard, Excel plug-in.
- AmiBroker: AFL array-processing semantics (Buy/Sell as special arrays), Automatic Analyzer, custom backtester interface, AmiQuote/AmiFeed companions.
- Alpaca: Trading API / Broker API / Market Data API split.

## Vendor-specific Findings

- MultiCharts' bar-close order dispatch ("orders are sent at the close of the previous bar") is a product-specific execution-model choice made for chart-price fidelity; other products evaluate on different triggers. Not generalizable.
- TT's compliance testing (volatile-market replay to avoid "disruptive algos") reflects institutional/exchange concerns; not observed elsewhere in the sample.
- QuantConnect's organizations/object-store/team structures reflect its cloud-SaaS model; desktop products handle collaboration differently (file-based).
- AmiBroker's array-processing language (spreadsheet-like whole-array evaluation) is a distinctive philosophy; other sampled products use event/bar-loop or visual models.

## Boundary Findings

1. **vs Retail Trading Platform / Professional Trading Terminal**: manual platforms execute human decisions and offer conditional order types (stop, bracket, OCO) — these are order-management primitives, not strategies. The boundary test: at trade time, does an encoded decision loop generate the order (algo platform) or does a human (manual platform)? Blur exists: manual platforms add scripting; algo platforms (MultiCharts) retain full manual trading surfaces. The Type center is the strategy runtime, not the absence of manual trading.
2. **vs Brokerage Platform**: brokerage = account + market access + order routing; algo platform = strategy authoring + runtime. Alpaca probe shows the pure pipe pole ("built for… algorithmic… traders" with no strategy runtime). Brokerage-embedded algo platforms (the TradeStation pattern, referenced by MultiCharts' EasyLanguage compatibility and QuantConnect's TradeStation integration) straddle the two; the leaf remains valid because strategy-authoring products exist that are not brokerages (MultiCharts, AmiBroker, QuantConnect, TT).
3. **vs Financial Market Data Terminal**: data terminals serve observation/analysis; algo platforms consume data as strategy input. Overlap in charting is superficial.
4. **vs charting platforms with strategy scripting (TradingView pattern)**: such products let users write strategies and fire alerts/webhooks, but execution and position management happen in external systems. Structural distinction: managed order lifecycle vs emitted signals. (TradingView docs unreachable — this boundary is argued structurally, weaker evidence.)
5. **Two senses of "algorithmic trading"**: strategy algos (decision logic — this Type) vs execution algos (order-slicing TWAP/VWAP-style logic — institutional EMS/OMS territory). TT evidence shows one platform carrying both ("Automate the entry and exit of positions" + "Reduce the market impact of large orders"). The leaf is interpreted as the strategy-algo platform; execution algos are recorded as an L2 institutional capability, with EMS/OMS as a different Type.
6. **vs Robo-advisor**: both automate trading, but the robo-advisor's strategy is the vendor's product; the user is an investor, not a strategy author. Different Type.
7. **vs quant research tools / Event Stream Processing**: research environments (Jupyter-style) and stream-processing engines are components or adjacent infrastructure; the Type is defined by integrating strategy authoring, testing, and order-generating execution in one product.
8. **Historical/market-sample check**: the definition holds for 1990s-era system-trading software (formula language + backtest + automate — the TradeStation/EasyLanguage lineage that MultiCharts explicitly stays compatible with), for the MetaTrader-era terminal family (structurally the same pattern; official docs unreachable, so no product-specific claims), and for modern cloud platforms. The definition does not depend on cloud, Python, charting, colocation, or any asset class.

## Uncertainties

- MetaTrader/NinjaTrader/TradeStation/cTrader/TradingView/IBKR official docs were unreachable; the retail-terminal family's inclusion in the Type rests on the sampled products' shared structure plus MultiCharts' documented EasyLanguage compatibility — no operational claims made for those products.
- AmiBroker's live auto-trading capability was not evidenced in fetched pages; AmiBroker is treated as the analysis/backtesting-first pole of the Type.
- Exact risk-control defaults, latency figures, order-type vocabularies per product, and marketplace mechanics were not researched to assertion strength and are not claimed.
- Whether optimization is definitional or common: treated as L1 (common) because AmiBroker's optimization was not directly evidenced in fetched pages, though the portfolio backtester and custom metrics were.

## Final Synthesis

An Algorithmic Trading Platform is defined by a small loop: **an executable strategy artifact (code, formula, or visual program) that the platform evaluates against market data and from which it generates and tracks orders automatically**. Around that loop, mature products add the strategy lifecycle — backtest on history, optimize parameters, rehearse in simulation, deploy live through broker/venue connectivity — plus monitoring, risk controls, and indicator libraries. Products differ along authoring surface (trading language / general code / visual / parameters), runtime locus (desktop / cloud / colo), broker relationship (embedded / agnostic / network / API), and audience (retail → institutional). The word "algo" also covers execution algos (order slicing), an institutional capability that some platforms carry alongside strategy algos but whose primary home is EMS/OMS software. The Type is distinct from manual trading platforms (human decides each trade), brokerages (pipe without runtime), data terminals (observation without orders), and robo-advisors (vendor-authored strategy).
