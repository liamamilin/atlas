# Research Notes — Financial Market Data Terminal

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Financial Market Data Terminal actually is as an Application Type: the objects it organizes, the loop a professional user runs through it, the surfaces it exposes, how data licensing and entitlements shape it, and where it separates from neighboring Types (Professional Trading Terminal, Investment Research Platform, Financial News & Research Platform, Portfolio Management System, consumer finance portals, charting platforms).

## Initial Boundary

Initial hypothesis (to be verified, not asserted):

- A financial market data terminal is a professional workstation for observing and analyzing markets: an instrument-centered data spine (securities, indices, currencies, commodities, rates, funds, companies) carrying live market data, fundamentals, estimates, news and analytics, navigated function-by-function around a persistent instrument context.
- It does not route orders (vs Professional Trading Terminal). Execution modules in some terminals (Bloomberg-style EMS add-ons) are add-ons, not the center.
- Its data is licensed from upstream sources (exchanges, fundamentals vendors, news agencies) and distributed under per-user entitlements — this shapes what the product can and cannot do.
- Nearest confusion risks: research-flavored terminals straddling Investment Research Platform; news-heavy products straddling Financial News & Research Platform; advisor-tier products straddling Financial Advisor Platform; low-end products shading into consumer finance portals.

Prior sibling notes honored:

- research/professional-trading-terminal.md: "a data terminal's center is market state/news/analytics/communication without order routing (Bloomberg Terminal pattern)… Test: remove order routing → data terminal."
- research/algorithmic-trading-platform.md: "data terminals serve observation/analysis; algo platforms consume data as strategy input."
- applications/portfolio-management-system.md and applications/performance-attribution-platform.md both list Financial Market Data Terminal as a *data supplier* to their Types.

## Research Questions

1. What is the organizing spine — instruments, companies, indices? How are they identified and "loaded"?
2. What functions does the terminal expose, and how does the user navigate between them (command bar, menus, function codes)?
3. Does instrument context persist across functions (linking)?
4. What data domains are included (quotes, fundamentals, estimates, transcripts, economics, fixed income, news)?
5. How is news integrated with instruments and markets?
6. What analytics exist (charting, screening, portfolio tracking, macro dashboards)?
7. How does data leave the terminal (download, export, API) — and what limits do data licenses impose?
8. How is access governed (subscription tiers, real-time vs delayed entitlements, per-user licensing)?
9. Where does execution appear (add-on modules) and how is it bounded?
10. Where are the boundaries vs Professional Trading Terminal, Investment Research Platform, Financial News & Research Platform, Portfolio Management System, Financial Advisor Platform, consumer finance portals?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence level |
|---|---|---|
| Koyfin | modern web-based terminal; advisor + independent-investor tier; command-bar navigation; licensed data aggregation | Tier-1 help center + FAQ + product pages (fetched) |
| Finviz | screener-first market data site; free delayed vs paid Elite real-time; equities-centric with futures/forex/crypto | Tier-2 product site (fetched) |
| TIKR ("TIKR Terminal") | fundamental-research-first terminal for investors; screener + financials + transcripts + valuation builder | Tier-2 product site (fetched; help desk unreachable) |
| Bloomberg Terminal | the archetype institutional terminal; function-code navigation, news, analytics, communication, execution add-ons | NOT directly fetched — see source-access limitation below |

Attempted but unreachable (source-access limitation — no operational claims made from them):

- Bloomberg Terminal — bloomberg.com/professional/ timeout ×2; bd.help.bloomberg.com timeout ×2; web.archive.org fallback timeout ×2. The archetype is characterized only qualitatively, from (a) Koyfin's own help docs explicitly citing "Professional terminals such as Bloomberg and Reuters" and their shortcut-navigation convention, and (b) the sibling professional-trading-terminal research. No function-code lists, pricing figures, or operational specifics asserted.
- LSEG Workspace (Refinitiv Eikon lineage) — lseg.com workspace paths 404 ×2; support.lseg.com JS-gated (Salesforce CSS error).
- FactSet — factset.com JS-rendered (title-only) ×2; help.factset.com transport error; deep product path 404.
- TradingView — tradingview.com timeout ×2 (would have served as charting-first boundary anchor).
- YCharts — 403. Morningstar — empty responses ×2. S&P Global Market Intelligence — 403. Barchart — empty response.

## Sources

Fetched 2026-09-06:

- Koyfin product site — https://www.koyfin.com/ (positioning, data coverage list, features)
- Koyfin features page — https://www.koyfin.com/features/ (model portfolios, client portfolios, proposals, reports, alerts, advanced graphing, financial analysis, equity screener, market dashboards, watchlists, custom dashboards, company snapshots)
- Koyfin Help Center — https://www.koyfin.com/help/ (index: Getting Started, Functionality ×49, Release notes ×93, How do I, Mobile, Integrations ×8, FAQ)
- Koyfin help: Command Bar & Search — https://www.koyfin.com/help/command-bar-search/
- Koyfin help: Right Sidebar — https://www.koyfin.com/help/right-sidebar/
- Koyfin FAQ: Where do you get your data? — https://www.koyfin.com/help/faq/where-do-you-get-your-data/
- Koyfin FAQ: Is your data live or delayed? — https://www.koyfin.com/help/faq/is-your-data-live-or-delayed/
- Koyfin FAQ: Can I get the data via API? — https://www.koyfin.com/help/faq/can-i-get-the-data-via-api/
- Finviz product site — https://finviz.com/ (navigation structure, screener/maps/charts/news/groups/insider/futures/forex/crypto/portfolio/calendar, Elite tier, delayed-data footer)
- TIKR product site — https://www.tikr.com/ (terminal positioning, screener, financials, transcripts, valuation builder, portfolio tracking, superinvestor portfolios, CapitalIQ sourcing, competitor-comparison set)

Not reachable (limitation recorded; assertions kept generic):

- bloomberg.com, bd.help.bloomberg.com, web.archive.org (for Bloomberg) — timeouts
- lseg.com workspace paths, support.lseg.com — 404 / JS-gated
- factset.com, help.factset.com — JS-rendered / transport error / 404
- tradingview.com — timeouts; ycharts.com — 403; morningstar.com — empty; spglobal.com — 403; barchart.com — empty; tikr.zendesk.com — timeout + transport error

## Product A — Koyfin

### Key observations (evidence layer A unless noted)

- **Positioning**: "A modern investment platform for advisors and investors. Research markets, analyze portfolios, and create client-ready reports in one place." "Get instant access to live market data." Testimonials explicitly compare it to Bloomberg and Eikon ("I've used Bloomberg terminals that my university provides…", "I subscribe to and use a number of tools ranging from Eikon to Zephyr, I open Koyfin every day").
- **Data coverage** (product page): Stocks, ETFs, Mutual Funds, Government Yields, Indices, Currencies, Commodities, Global Economics, Transcripts, Cryptocurrencies, News.
- **Licensed data aggregation** (FAQ, Tier-1): "We buy our data and have license agreements with over a dozen data vendors to provide professional-grade data via Koyfin. We don't scrape the web for any data." Global equity fundamentals, consensus estimates and valuation sourced from S&P Capital IQ; fund data from Morningstar; other vendors include FRED and Trading Economics (economic data), True FX (FX), Polygon (crypto).
- **Data real-time-ness is entitlement/region-dependent** (FAQ, Tier-1): US stocks a combination of live and 15-minute delayed; Canadian prices 15-minute delayed; all other countries end-of-day; last-trade timestamp surfaced in the UI.
- **Data redistribution is license-limited** (FAQ, Tier-1): "We don't allow users to get data via API because of restrictions from our data providers. They are in the API business. We are in the analytics business." (Data download FAQ also exists; chart-reuse FAQ addresses licensing of charts in blogs/reports.)
- **Command-bar function navigation** (help, Tier-1): "The command bar on top is a quick way to use shortcuts to find securities and charts… Professional terminals such as Bloomberg and Reuters also have shortcut navigation to allow users to move quickly through the system." Format: **ticker** <enter> **function** <enter> — e.g., AAPL <enter> G <enter> pulls the AAPL graph; AAPL <enter> EST <enter> pulls estimates; SPY <enter> HDS <enter> pulls holdings. Slash-commands (/MOV movers page). Relative tickers with a colon (AAPL:FB for relative performance). Search sorted by match + trading volume (AUM for funds); filters by asset type and country.
- **Persistent instrument context** (help, Tier-1): the right sidebar holds watchlists, movers and news; "You can click on the securities in the right sidebar to load them into Koyfin functions like Snapshot (S), Estimates (EST) or Graph (G)." — the instrument is *loaded into functions*; functions render views of the loaded instrument.
- **Function inventory** (help index + features page): watchlists (with views, sharing, news), my portfolios, screens (screener), historical graph (G), model portfolios, corporate transcripts, my dashboards (MYD), markets news, relative performance (A/B), ETF exposure (EXP), portfolio analysis tools, financial analysis templates (FA), dividend snapshot (DVD), earnings calendar, custom news screens, custom formulas, actuals vs consensus, global bonds/yield curves/FX, global equities/fundamentals/valuation, insider ownership & transactions, hotkeys and custom shortcuts, data overview, mutual fund data, ETF holdings/constituents/contribution, percentile ranks, custom data series, teams.
- **Equity screener**: "scan through over 100K global securities using 5,900+ filter criteria" (vendor figures — claims).
- **Alerts**: price, valuation, technicals, and news alerts across watchlists and portfolios; desktop/email/mobile delivery.
- **Advisor-tier drift** (features + release notes): client portfolios (accounts grouped into portfolios and households), proposals (client-facing, branded), reports (customizable, benchmarks, templates), rebalance table, SMA screener, custodian/custodian-software integrations (Schwab Advisor Center, Altruist, TradePMR, Black Diamond, Interactive Brokers, Orion, Fidelity Wealthscape, Addepar), PDF brokerage statement upload. Packaging: "Koyfin Advisor Core" / "Koyfin Advisor Pro" tiers.
- **Collaboration**: watchlist sharing, model portfolio sharing, report sharing, teams, My Graphs sharing.
- **AI**: transcript summaries (release note v3.69).
- **News**: markets news, watchlist news, company news, press releases, custom news screens; MT Newswires as a news source (release note v3.14).
- **Delivery**: web app (app.koyfin.com), mobile app (iOS home-screen widgets release note), themes/customizable left navigation.

## Product B — Finviz

### Key observations

- **Framing**: "Finviz - Stock Screener"; top-level navigation is a function menu: Screener, Maps, Charts, News, Groups, Insider, Futures, Forex, Crypto, Portfolio, Calendar (economic). Help/knowledge base linked.
- **Instrument universe**: US equities (screener over stocks with ticker pages), plus futures, forex, crypto quote surfaces; indices (S&P 500 map by sector).
- **Market overview surfaces**: advancing/declining breadth, new highs/lows, SMA50/SMA200 breadth, top gainers/losers/unusual volume/most active lists, headline news stream (attributed to Bloomberg, MarketWatch, Reuters, Yahoo, WSJ, CNBC), major-news movers, insider trading tables (latest + top by value), futures table, forex & bonds table (treasury yields), economic calendar (release date/time/impact/actual/expected/prior), earnings calendar.
- **Entitlement structure**: free tier — "Stock quotes delayed by 1 minute. Futures and options delayed by 15 minutes." Elite paid tier — "real-time data, technical charting, alerts, and no ads"; "Unlock real-time market data, fullscreen multi-layout charts, custom alerts, advanced screening filters, ETF insights, seamless exports/API, and an ad-free experience." Pricing figure "$24.96/mo" is a vendor claim (research notes only).
- **Screener**: filter-based stock screening with signal presets (top gainers, new high, overbought, unusual volume, upgrades, insider buying…); export all screener data as CSV (public link); API and exports as an Elite-adjacent offering (footer: "API and Exports").
- **News integration**: dedicated News page; headlines embedded on the home dashboard; news items linked to external publishers (aggregation posture, not original editorial).
- **Portfolio**: a Portfolio surface (user-tracked holdings) — analysis/monitoring posture.
- **Insider**: insider trading records as a first-class data domain (latest transactions, top transactions by value, per-insider relationship detail).
- **Groups**: group-level (sector/industry/country) performance views; Maps: market-cap-weighted heat maps.
- **Delivery**: web; guided tour; light/dark mode. No order routing anywhere in the observed surface.

## Product C — TIKR

### Key observations

- **Framing**: "Invest like Wall Street with TIKR Terminal… Find the best stocks, follow top investors, quickly analyze businesses, and monitor your portfolio with TIKR." "Go From Idea to Conviction Without Leaving TIKR."
- **Instrument universe**: "100,000+ global stocks… across 92 countries and 136 exchanges" (vendor figures — claims).
- **Licensed data aggregation**: "accurate financial data powered by S&P Global CapitalIQ" — same upstream-vendor pattern as Koyfin (independently evidenced).
- **Function inventory** (product page tabs): detailed financials (up to 30 years), valuations (metrics, multiples, analyst forecasts), transcripts, screener (thousands of filters incl. country, industry, financials, ratios, Wall Street analyst forecasts, valuation multiples, capital structure, growth rates, margins), dashboard, investing gurus (superinvestor portfolios — "portfolios of 10,000+ investors… including company insiders, hedge funds… globally, beyond US 13F"), custom valuation builder (forecast models without a spreadsheet, saveable to dashboard).
- **Portfolio tracking**: "Monitor your Portfolio Easily… stock market news that can be customized across hundreds of topics… watchlist news feed that highlights upcoming events, company news, earnings & conference transcripts, and company filings."
- **News integration**: watchlist-bound news feed with topic customization; transcripts and filings attached to companies.
- **Competitor set** (footer): Bloomberg, Morningstar, Yahoo Finance, Sentieo, Google Finance, TradingView, FactSet, Finviz, YCharts, MarketBeat, Benzinga, Gurufocus, FAST Graphs, TipRanks, Seeking Alpha, TheStreet, Investing.com, Zacks, AlphaSense — evidence that the market frames this product family against both terminals (Bloomberg/FactSet) and research/content platforms (Sentieo/AlphaSense/Seeking Alpha).
- **Delivery**: web app (app.tikr.com); free tier + paid plans; help desk on Zendesk (unreachable during research).
- **No order routing, no real-time trading surfaces** observed in the product page; emphasis is fundamentals/valuation/research.

## Product D — Bloomberg Terminal (archetype; NOT directly fetched)

### Key observations (provenance-limited — qualitative only)

- Koyfin's own Tier-1 help documentation cites "Professional terminals such as Bloomberg and Reuters" as the origin of the shortcut/command navigation convention (evidence layer B via a fetched source).
- Sibling research (professional-trading-terminal.md, fetched 2026-09-06) characterizes the "Bloomberg Terminal pattern" as "market state/news/analytics/communication without order routing", and notes data terminals adding execution add-ons are drifts, not identity changes.
- Market-common knowledge (NOT asserted as researched fact in the final document): function-code navigation, participant chat/messaging, execution modules (EMS), dedicated keyboard hardware heritage, per-user subscription with exchange-fee pass-through. These remain qualitative context in Research Notes only; no precise operational claims are made.

## Cross-product Comparison

| Dimension | Koyfin | Finviz | TIKR | Bloomberg (archetype, qualitative) | Layer |
|---|---|---|---|---|---|
| Instrument-centered spine | tickers loaded into functions (S/EST/G…) | ticker pages + screener rows | company pages + screener rows | instrument-centric functions | B |
| Function navigation | command bar (ticker→function), hotkeys, left nav | top function menu | product tabs/pages | function-code navigation (convention cited by Koyfin) | B |
| Persistent instrument context | explicit: sidebar click loads instrument into functions | stock page aggregates quote/chart/news/financials | company page aggregates financials/transcripts/news | function chaining on loaded security | B |
| Market data (price) | live+delayed mix (US), delayed (CA), EOD (other) — entitlement/region-dependent | free delayed 1-min equities / 15-min futures; Elite real-time | price charts present; fundamentals-first emphasis | real-time professional feeds | B |
| Fundamentals & estimates | financial analysis, estimates, actuals vs consensus, valuation | screener fundamental filters | 30y financials, valuation multiples, analyst forecasts (CapitalIQ-powered) | fundamentals/estimates functions | B |
| Screener | 100K+ securities, 5,900+ filters (claim) | signature screener with signal presets | 100K+ global stocks, thousands of filters (claim) | screening functions | B |
| News | markets news, watchlist news, company news, press releases, custom news screens, MT Newswires | news page + dashboard headlines (external publishers) | watchlist news feed, topic-customized | integrated news functions | B |
| Transcripts | corporate transcripts + summaries | — | transcripts tab | transcripts (market-common) | B |
| Economics / macro | macro dashboards, economic + earnings calendars, FRED/Trading Economics data | economic calendar, futures/forex/bonds tables | — | economics functions | B |
| Multi-asset breadth | stocks/ETFs/funds/yields/indices/FX/commodities/crypto/economics | equities + futures/forex/crypto | equities-focused | multi-asset | B (breadth varies) |
| Portfolio tracking | my portfolios, model portfolios, client portfolios | portfolio surface | portfolio tracking + watchlists | portfolio functions | B |
| Alerts | price/valuation/technicals/news alerts | Elite alerts | (not confirmed from fetched pages) | alerts | B |
| Export / API | download data; API refused (data-provider restrictions) | CSV screener export; Elite exports/API | (not confirmed) | export/API (market-common) | B |
| Sharing / collaboration | watchlist/model-portfolio/report sharing, teams | — | — | (archetype: communication layer) | B |
| Licensed data aggregation | explicit: 12+ vendors, Capital IQ/Morningstar/FRED/TrueFX/Polygon | (not stated on fetched pages) | explicit: S&P Capital IQ | licensed feeds | B |
| Entitlement tiers | free + paid plans; live vs delayed by region/plan | free delayed vs Elite real-time | free + paid | per-user subscription | B |
| Order routing | none | none | none | execution add-ons (drift, per sibling research) | B |
| Advisor workflow extensions | client portfolios/households, proposals, reports, custodian integrations, Advisor Core/Pro tiers | — | — | — | A (Koyfin only) |
| Insider data domain | insider ownership & transactions | insider trading tables | superinvestor/guru portfolios (13F+) | — | B |
| Delivery | web + mobile | web | web | desktop/keyboard heritage (qualitative) | B |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately small)

A Financial Market Data Terminal is recognizable by four properties together:

1. **Instrument-centered data spine** — identified securities/instruments (and their issuers) are the organizing records of the system; the user selects ("loads") an instrument and the system renders it.
2. **Market data bound to instruments** — prices/quotes (real-time, delayed, or end-of-day depending on entitlement) plus fundamentals/estimates attached to the same instrument records are the primary content.
3. **Function-navigated workspace with persistent instrument context** — the product is organized as a set of distinct functions (quote/snapshot, chart, financials, estimates, news, screener, calendars) that each render a view of the loaded instrument; moving between functions while keeping the instrument context is a first-class interaction.
4. **Observation-and-analysis purpose** — the terminal's loop is monitoring, researching and analyzing markets; it does not construct or route orders. Where execution exists in some products, it is an add-on module, not the center.

Remove (1) → a news service or analytics tool without an instrument spine. Remove (2) → a pure research/fundamentals database (drifts toward Investment Research Platform). Remove (3) → disconnected data tools, a raw data feed, or a consumer portal's separate pages. Remove (4) → a Professional Trading Terminal.

### L1 — Common Mature Structure (very common, not defining)

- Watchlists / monitors — user-defined instrument sets with configurable columns and views
- Screening over the instrument universe (filterable, saveable screens)
- Charting — price history, technicals, fundamental time series, relative performance
- Company fundamentals and analyst estimates (financials, consensus vs actuals)
- News integrated with instruments and markets (tagged, filterable, watchlist-bound)
- Economic/macro data and calendars (earnings calendar, economic calendar, macro dashboards)
- Portfolio tracking (user portfolios monitored against market data — analytical, not custody)
- Alerts on price/valuation/technicals/news conditions
- Data export (download/CSV; API in some products, refused in others due to data licenses)
- Sharing/collaboration (shared watchlists, teams, shared reports)
- Licensed data aggregation from upstream vendors (exchanges, fundamentals vendors, news agencies) — the commercial backbone of the Type
- Subscription tiers / entitlements (free delayed vs paid real-time; feature gating; per-user licensing)
- Mobile companion surface
- Command/shortcut navigation (in command-bar products)

### L2 — Variant / Optional Structure

- Asset-class center of gravity (multi-asset vs equities-focused vs fixed-income-heavy)
- Customer tier (institutional vs advisor vs independent professional vs retail)
- Data real-time-ness posture (real-time vs delayed vs EOD, by entitlement and region)
- Delivery form (browser, desktop app, mobile; historically dedicated hardware/keyboard terminals)
- Advisor-workflow extensions (client portfolios/households, proposals, client reports, custodian integrations — boundary pressure toward Financial Advisor Platform)
- Research-content depth (transcripts, filings, superinvestor/13F portfolios, broker research — boundary pressure toward Investment Research Platform)
- Communication layer (participant chat/messaging — present in the archetype, absent in sampled lower tiers)
- Execution add-ons (EMS-style modules — straddle toward Professional Trading Terminal)
- AI assistance (transcript summaries, AI Q&A)
- Regional specialization (regional terminals for specific markets)
- Pricing model (freemium, per-user flat, modular add-ons)
- Insider/ownership data domains (insider transactions, institutional holdings)

### L3 — Vendor-specific (research notes only)

- Koyfin: command-bar syntax (ticker <enter> function <enter>), function codes (G, GM, EST, HDS, S, MOV, EXP, DVD, FA, MYD, A/B), right-sidebar loading, relative tickers (AAPL:FB), themes, customizable left navigation, Advisor Core/Pro packaging, named custodian integrations (Schwab, Altruist, TradePMR, Black Diamond, IBKR, Orion, Fidelity Wealthscape, Addepar), MT Newswires, custom formulas, data dictionary, transcript summaries
- Finviz: heat maps, groups, insider-trading tables, signal-preset screener, Elite tier specifics, "$24.96/mo" pricing claim, 1-min equities / 15-min futures delay figures (free tier), public CSV screener export
- TIKR: "TIKR Terminal" branding, superinvestor portfolios ("10,000+ investors" claim), 30-year financials, 92 countries/136 exchanges claims, valuation model builder, CapitalIQ powering
- Bloomberg: <GO> function codes, IB chat, terminal keyboard, EMSX execution module — NOT verified from primary sources; qualitative context only
- All vendor figures (security counts, filter counts, prices, delay windows) are vendor claims — kept out of the final document except where directly quoted with attribution.

## Vendor-specific Findings

See L3. Notable: Koyfin's API refusal is explicitly attributed to data-provider restrictions ("They are in the API business. We are in the analytics business.") — direct evidence that upstream data licenses, not product choice alone, shape terminal capabilities. Koyfin's advisor packaging (client portfolios, proposals, custodian integrations) is a single-product drift toward Financial Advisor Platform territory.

## Boundary Findings

**vs Professional Trading Terminal** (sibling, processed): the sharpest seam. The trading terminal's loop closes with order construction/routing and live position/P&L; the data terminal's loop ends in observation/analysis. Evidence: none of the three fetched data-terminal products exposes order routing anywhere in its observed surface; the sibling research documents the "remove order routing → data terminal" test from the other side. Execution add-ons in data terminals (Bloomberg-style EMS modules, per sibling research) are drifts, not identity changes. Held.

**vs Investment Research Platform** (sibling, unprocessed — joint-review flag): research-flavored terminals (TIKR most clearly; FactSet-style products by market reputation) straddle. Distinction attempted: the data terminal's center is the instrument-centered live-data workspace (market state + functions over instruments); the research platform's center is research content and workflow (reports, estimates databases, filings, expert calls, notes, collaboration). TIKR's own positioning ("Go From Idea to Conviction", valuation builder, guru portfolios) is research-first while retaining the terminal's instrument/function spine — a genuine straddle. Flagged for joint review when that leaf is processed.

**vs Financial News & Research Platform** (sibling, unprocessed): news-centric products have the news stream/editorial content as the center; the data terminal integrates news as one function bound to instruments among many. Finviz aggregates external publishers' headlines (aggregation posture) but its center is the screener/market-data surface. Held, pending sibling processing.

**vs Portfolio Management System** (sibling, processed): PMS manages institutional portfolios as long-lived records (positions, attribution, compliance) for portfolio managers; the data terminal's portfolio tracking is personal/analytical monitoring against market data. The two Types meet: PMS consumes terminal data (documented in the PMS application doc as "data supplier"). Koyfin's client-portfolio layer drifts toward advisor practice management — noted below. Held.

**vs Financial Advisor Platform** (sibling, processed): Koyfin's advisor tier (client portfolios/households, proposals, client reports, custodian integrations) overlaps FA-platform territory; the FMDT center remains market data/analysis, and the advisor extensions are a variant posture. Straddle noted; boundary held on the center of gravity.

**vs consumer finance portals** (Yahoo Finance, Google Finance — no dedicated directory leaf): the low end shades into free portals (Finviz's free tier is publicly accessible with delayed data). Discriminators: the professional function-workspace model with persistent instrument context, licensed professional-grade data, subscription entitlement structure, and screening/analytics depth. A portal's quote page and a terminal's snapshot function can look similar; the difference is the integrated function workspace and the professional data/entitlement posture. Recorded as a boundary note, not a directory conflict.

**vs charting platforms** (TradingView — unreachable during research): charting-first products make the chart the center with social/community layers; the terminal makes the instrument spine with charting as one function. Boundary anchor only; no claims made.

**vs Data Explorer / Public Data Portal (§02.12)**: generic data exploration over arbitrary datasets vs instrument-centered licensed market data with a professional function workspace. Held.

**"去掉什么就变成另一个 Type" 判据**:
- 加上 order routing + position/P&L closure → Professional Trading Terminal
- 去掉 live market data、只留研究内容 → Investment Research Platform
- 把 news 变成中心 → Financial News & Research Platform
- 把 portfolio 从分析性跟踪变成机构组合记录 → Portfolio Management System
- 去掉 function workspace + licensed professional data → consumer finance portal

## Uncertainties

- The institutional archetype (Bloomberg Terminal) and the other institutional terminals (LSEG Workspace, FactSet) could not be fetched. The institutional end of the Type (communication layers, execution add-ons, entitlement administration, fixed-income/derivatives analytics depth) is reasoned from the sibling professional-trading-terminal research and Koyfin's explicit references, not from those vendors' docs. All institutional-specific claims in the final document are kept qualitative.
- Whether "communication layer (participant chat)" belongs in L1: it is market-famous in the archetype but absent from all three fetched products. Kept in L2 (variant) with a note — evidence does not support "common" across the sample.
- Whether "alerts" is universal: confirmed in Koyfin and Finviz (Elite); not confirmed for TIKR from fetched pages. Kept in L1 with "common" wording.
- TIKR's export/API posture not confirmed from fetched pages.
- Precise entitlement mechanics per product (which exchanges, which fees, which features per tier) not researched — deliberately not asserted.
- The boundary vs Investment Research Platform is genuinely fuzzy at the research-flavored end; joint review flagged.

## Final Synthesis

The Financial Market Data Terminal is the professional's instrument-centered market workstation: identified instruments form the data spine; market data (prices, fundamentals, estimates) is bound to those instruments under licensed, entitlement-gated distribution; the product is organized as a set of functions (snapshot, chart, financials, estimates, news, screener, calendars, portfolio tracking) that render views of the loaded instrument, with the instrument context persisting across functions; and the whole loop serves observation and analysis — monitoring, researching, screening, communicating — rather than order execution. Everything else — multi-asset breadth, real-time posture, advisor extensions, research depth, chat networks, execution add-ons, AI — is mature or variant structure layered on that spine. The Type is separable from the Professional Trading Terminal (order routing), the Investment Research Platform (research content as center), the Financial News & Research Platform (news as center), the Portfolio Management System (institutional portfolio records), and consumer finance portals (no professional function workspace or licensed data posture), with acknowledged straddling products at the research-flavored and advisor-flavored seams.
