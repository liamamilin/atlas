# Research Notes — Financial News & Research Platform

Research date: 2026-09-07
Slug: financial-news-research-platform
Directory leaf: §08 Finance, Banking, Insurance & Investment — "Financial News & Research Platform"

## Research Goal

Understand what a Financial News & Research Platform actually is as an Application Type: what content it produces, how content is organized around financial instruments, what data and tools accompany the content, who consumes it, how it is monetized, and where its boundaries lie against the Financial Market Data Terminal (processed), the Investment Research Platform (§08 sibling, unprocessed), and the general News Application / News Aggregator leaves (§02.04, unprocessed).

## Initial Boundary (hypothesis before research)

- Hypothesis: the Type is a content platform (news + analysis/research) for investors, organized around identified instruments (symbol pages), with instrument data attached, monetized by subscription/advertising, and distinct from (a) market data terminals (data workspace center), (b) institutional research platforms (document/workflow center), (c) general news apps (no instrument anchoring, no investment-decision data layer).
- Nearest neighbors: Financial Market Data Terminal (processed — recorded seam: "the news stream/editorial content is the center; the terminal integrates news as one function among many"), Investment Research Platform (unprocessed sibling), News Application / News Aggregator (§02.04, unprocessed), Newsletter Marketing Platform (§06 — different: marketing tool), Financial Advisor Platform (processed — advisor practice system), Brokerage Platform (processed — account custody).

## Research Questions

1. What content types exist (news, analysis, research reports, transcripts, lists, education)? Who produces them (staff journalists, staff analysts, paid contributors, licensed wires)?
2. How is content organized and anchored (instruments/symbols, sectors, markets, topics)? What is the atomic surface (symbol page)?
3. What instrument data accompanies content (quotes live/delayed, fundamentals, estimates)? How is it sourced and licensed?
4. What investor tools wrap the content (watchlists, portfolios, screeners, alerts, calendars, charts)?
5. What ratings/opinion layers exist (proprietary quant ratings, analyst research opinions, none)?
6. How does the reading loop work (stream → instrument page → article → tools)?
7. How is the platform monetized (free+ads, freemium paywalls, subscriptions, marketplace)?
8. Who is the audience (retail investors, traders, advisors, professionals)?
9. What compliance/editorial posture is visible (informational-only disclaimers, editorial independence, corrections)?
10. Where are the boundaries vs terminal / investment-research-platform / news-app / newsletter / social-investing?

## Representative Products (sample rationale)

Selected for market representativeness + different product philosophies + different customer tiers:

1. **Seeking Alpha** — crowdsourced-research philosophy: paid contributor analysts + professional editors + community discussion + proprietary quant ratings; freemium (Basic/Premium/PRO/Alpha Picks/Investing Groups marketplace). US equities/ETFs focus. [Documented: root page, about site, help center ×2 — Tier-1/Tier-2]
2. **Morningstar** — research-house philosophy: staff analyst research (Fair Value, Economic Moat, Uncertainty), fund/stock/ETF coverage, licensed third-party news (MarketWatch, Dow Jones), investor tools; subscription (Morningstar Investor; Premium and Portfolio Manager). Advisor-facing section. [Documented: root page, help center — Tier-1/Tier-2]
3. **MarketWatch** — news-first journalism philosophy (Dow Jones): financial news + opinion + personal finance/retirement editorial, light tools (watchlist, search, game), licensed market data (FactSet), subscription + advertising + commerce guides. [Documented: root page — Tier-2]
4. **Investor's Business Daily (IBD)** — methodology-driven research philosophy: proprietary ratings (Composite, RS), curated stock lists (IBD 50, Sector Leaders, Big Cap 20, New Highs, IPO Leaders…), screener/charts (MarketSurge), model portfolio (Leaderboard), newsletter (MarketDiem); subscription (IBD Digital). Growth-stock/trader audience. [Documented: root page — Tier-2]

Boundary-context products (not deep-researched, zero claims): Yahoo Finance (portal pole — unreachable), Investing.com (unreachable), Benzinga (news-wire pole — unreachable), TipRanks (analyst-data aggregation — unreachable), TheStreet, Zacks (unreachable), Bloomberg/LSEG/FactSet (terminal side, covered by the terminal leaf's research), AlphaSense/Tegus class (institutional investment research platform sibling, unprocessed).

## Sources

Fetched successfully (2026-09-07):

- Seeking Alpha — https://seekingalpha.com/ (root: navigation, homepage sections, paywall markers, About block)
- Seeking Alpha — https://about.seekingalpha.com/ (About Us: platform description, crowdsourcing model, quant ratings, product list, comprehensiveness list, Investing Groups, disclaimers)
- Seeking Alpha — https://help.seekingalpha.com/ (Support Center: KB categories Basic/Premium/PRO/Alpha Picks/QG&I/Bundles/Investing Groups/Mobile App/SA Analysts Corner)
- Seeking Alpha — https://help.seekingalpha.com/basic/where-do-you-source-your-market-data-from (Tier-1: market data sourcing — Quodd/Xignite, Cboe BZX real-time, Nasdaq UTP delayed, S&P Global Market Intelligence fundamentals/estimates/ratings, GICS, ClariFI; redistribution prohibition; informational-only disclaimer; KB subcategories incl. Symbol Page, Ask Seeking Alpha, Earnings Calls Insights)
- Morningstar — https://www.morningstar.com/ (root: navigation Tools/Sections/Investing Ideas/For Advisors, market barometer, movers, featured staff analysis, Market News incl. licensed MarketWatch/Dow Jones items, Market Calendar, Company Reports with locked rating fields, podcasts/videos/newsletters)
- Morningstar — https://www.morningstar.com/help-center (Tier-1: help sections — Approach to Investing, Getting Started, Manage Account, Payment, Tools: Portfolio/Watchlists/Screener/Compare, Notifications, Research: Funds/Stocks/Reports, Premium and Portfolio Manager, Markets, Webinars; "How we make money"; editorial-content policy; real-time index quote disclosure)
- MarketWatch — https://www.marketwatch.com/ (root: sections, latest news, opinion columns, Watchlist, search incl. symbols, trending tickers, Guides commerce block, newsletters, Virtual Stock Exchange, FactSet data + 15-minute delay disclosure, subscription)
- Investor's Business Daily — https://www.investors.com/ (root: Stock Market Today, The Big Picture, research articles, IBD Stock Lists with descriptions, Stocks On The Move, premium tools MarketSurge/Leaderboard/SwingTrader/MarketDiem/IBD Digital, screener screenshot, proprietary-ratings video title, data sourcing footer — Nasdaq Last Sale real-time, LSEG ownership, FactSet estimates; informational-only disclaimer)

Unreachable (1–2 attempts each, then abandoned per network rules; zero claims made for these):

- Yahoo Finance — help.yahoo.com/kb/finance 403; finance.yahoo.com 403
- Investing.com — www.investing.com 403; /about/ 403
- Benzinga — www.benzinga.com 403; /about/ 403
- TipRanks — www.tipranks.com 403; /about 403; support.tipranks.com transport error
- TheStreet — www.thestreet.com 403
- Zacks — www.zacks.com Incapsula block
- Seeking Alpha /subscriptions — JS-gated (noscript wall)
- Morningstar /business — empty response

## Product A — Seeking Alpha (crowdsourced research pole)

### Key observations (Evidence layer A unless noted)

- Self-description (about): "the leading platform for investors to research and discuss US-traded stocks and ETFs… provides investment ideas, analysis, news, ratings, investing tools and community discussion."
- Content production model (about): crowdsourcing + editorial quality control + community feedback. Investors submit articles → professional editors check quality criteria and compliance standards → published; contributors are paid. Community comments + a formal "dispute an article" process. Analysts include professionals and individuals; pseudonymous analysts allowed under a policy.
- Coverage claims (about, vendor figures — treated as claims): 5,000+ analysis articles/month; 8,000–10,000 tickers with analysis per quarter; 10,000+ tickers with ratings per quarter.
- Ratings layer (about): (a) SA Analyst ratings — contributors are required to rate every stock/ETF they write about; performance tracked publicly; (b) Quant ratings + factor grades computed from quantitative data (balance sheet/income statement metrics, price history): overall rating + Valuation/Growth/Profitability/Momentum/EPS Revisions grades; dividend grades (Safety/Growth/Yield/Consistency); ETF grades (Momentum/Expenses/Dividends/Risk/Liquidity). Performance pages for Quant Strong Buy / Sell portfolios.
- Products (about + help): Basic (free), Premium, PRO ("for professional and individual investors managing significant portfolios"), Alpha Picks (two quant-team picks/month), Quant Growth & Income portfolio, Bundles, Investing Groups (marketplace of subscription research services run by contributing analysts, with community chat — Rocket.Chat desktop app documented in help), Transcripts.
- Platform comprehensiveness list (about): analysis articles with community discussion; proprietary news coverage; earnings call and event transcripts; SA Analyst ratings per stock/ETF; quant ratings and factor grades per US stock; top stocks/ETFs lists and homepage cards; stock and ETF screeners using proprietary ratings + standard metrics; Portfolio Warnings and Stock Alerts using proprietary ratings; customizable homepage.
- Homepage structure (root): futures/indices strip; Latest News; Trending Analysis (named authors); Trending News; "In Case You Missed It" (symbol + analyst rating + article + analyst, paywalled ratings "Locked. Go Premium to see this"); On The Move news items each tagged with a ticker; Trending & Most Active stocks with Quant Ratings; Upcoming Earnings (EPS estimates table); U.S. Equity Markets table; sections for Stock Ideas / Market Outlook / Investing Strategy / IPO Analysis / Editor's Picks; Market News subsections (Notable Calls, On The Move, sector news, M&A, IPO); Sectors (11 GICS-style sectors); Dividends; ETFs; Earnings (calendar, call transcripts, insights); Education; Podcasts; Videos; Portfolios; Find & Compare (screeners, comparisons).
- Search (root): "Search for Symbols, analysts, keywords."
- Market data sourcing (help, Tier-1): real-time and delayed quotes provided by Quodd (formerly Xignite); real-time from Cboe BZX; delayed from Nasdaq UTP delayed feed; fundamentals, estimates, and Wall Street analyst ratings from S&P Global Market Intelligence; sector/industry data via GICS (licensed from MSCI/S&P); backtest data via ClariFI (S&P). "All data provided on Seeking Alpha is provided for informational purposes only… You may not copy or redistribute information provided by Seeking Alpha." Ratings are opinions, not recommendations.
- Help KB structure (help center): Basic (General / Portfolio / Symbol Page / Account Settings), Premium (…/ Summary Reports / Earnings Calls Insights / Ask Seeking Alpha), PRO, Alpha Picks, QG&I, Bundles, Investing Groups, Mobile App (Android/iPhone), SA Analysts Corner (Contributor Support / Articles; "Do I Get Paid for Writing Articles").
- Compliance posture (about): "not a licensed securities dealer, broker, US investment adviser, or investment bank"; content "offered for information purposes only"; analysts are third-party authors who may not be licensed.
- Paywall mechanics observed (root): premium-gated ratings and articles ("Locked. Go Premium to see this").

## Product B — Morningstar (research-house pole)

### Key observations

- Navigation (root): Tools (Portfolio, Watchlists, Screener, Compare, Chart, Rating Changes); Sections (Markets, Funds, ETFs, Stocks, Bonds); Investing Ideas; For Advisors; Media; Help; What's New; Notifications; "Products for Investors — All Products and Services."
- Homepage (root): US Market Barometer (with Style Box — Morningstar's own 3×3 style map); Market Movers (gainers/losers/actives with tickers, linked to quote pages); Featured staff analysis (named authors with CFA credentials); Market Insights; Editor's Picks; Market News — includes items sourced from MarketWatch and Dow Jones "Global News Select" (licensed third-party news displayed with source attribution); Market Calendar (earnings dates, linked to quote pages); Company Reports — Morningstar analyst research per company with fields Rating / Price / Fair Value / Uncertainty / Economic Moat / Capital Allocation, most fields paywall-locked ("LOCK"); Videos; Podcasts (The Long View, Investing Insights, The Morning Filter); Newsletters ("latest market news curated by Morningstar's editors").
- Proprietary research system (root): per-company analyst reports with Morningstar's own methodology fields (Fair Value, Economic Moat, Uncertainty, Capital Allocation) — a research-house rating layer distinct from news.
- Help center (Tier-1): sections — Morningstar's Approach to Investing; Getting Started (new-subscriber checklist); Manage Account; Payment Information; Tools: Portfolio / Watchlists / Screener / Compare; Notifications; Research: Funds / Stocks / Reports; Premium and Portfolio Manager; Markets; Webinars. Featured how-tos: Intro to Portfolio, Intro to Watchlists, Create a screen (pre-defined screens or custom views), Intro to notifications ("how it can help you make informed investing decisions").
- Business model disclosure (help center, "How we make money"): products/services sold to investment professionals and individual investors via license agreements or subscriptions; investment management business with asset-based fees; conference admissions/sponsorships; website/newsletter advertising.
- Editorial policy (help center): editorial independence; "strict separation between our sales teams and authors"; authors "show their work, distinguish facts from opinions"; corrections page exists.
- Data disclosure (footer): "Dow Jones Industrial Average, S&P 500, Nasdaq, and Morningstar Index (Market Barometer) quotes are real-time."
- Audience posture: individual investors (Morningstar Investor subscription) + advisors (For Advisors section) + professionals (products/services business).

## Product C — MarketWatch (news-first pole)

### Key observations

- Positioning (root): "Stock Market News - Financial News" — a Dow Jones company.
- Sections (root): Markets, Latest News (timestamped stream), Investing, Personal Finance, Retirement, Economy; Opinion columns (e.g., a named personal-finance Q&A column); MarketWatch Picks; MarketWatch Guides ("research and commerce newsroom… distinct from our news team. We earn a commission from some links"); Videos (branded series); Live Coverage; Newsletters; Newsroom Roster.
- Tools (root): Watchlist (top-nav), site search with symbol results ("Symbols" result type, Advanced Search), Trending Tickers module (above-average-volume tickers with prices, linked to /investing/stock/ pages), Virtual Stock Exchange (stock-market game).
- Ticker anchoring (root): story cards carry inline ticker chips (e.g., percentage changes next to stories); ticker pages under /investing/stock/<symbol>.
- Market data (footer, Tier-2 disclosure): "Intraday Data provided by FACTSET… Real-time last sale data for U.S. stock quotes reflect trades reported through Nasdaq only. Intraday data delayed at least 15 minutes or per exchange requirements."
- Monetization (root): Subscribe Now (subscription), advertising, commerce guides with commissions, corporate subscriptions.
- Research depth: journalism + opinion + guides; no proprietary instrument ratings observed on the fetched surface; tools are light (watchlist, game). This product sits at the news-first edge of the Type.

## Product D — Investor's Business Daily (methodology pole)

### Key observations

- Positioning (root): "Stock News and Stock Market Analysis"; founded by William J. O'Neil; "provides exclusive stock lists, market data and research, helping investors take advantage of the IBD Methodology."
- Content (root): Stock Market Today (market-action coverage with buy signals); The Big Picture (market-trend column); News (company/market news, e.g., index-inclusion, trial-failure stories); Research (Investing Action Plan week-ahead, Stock of the Day, IBD Stock Analysis); Stock Lists (IBD 50, Sector Leaders, Big Cap 20, New Highs, Relative Strength at New High, IPO Leaders, Stocks that Funds are Buying — each with a screening description); Stocks On The Move (price moves on unusual volume — "a signal institutions are buying or selling"); Videos (Stock Market Today show, how-to videos incl. "How To Use IBD's Proprietary Ratings"); Options; Swing Trading.
- Ratings layer (root): proprietary ratings ("exclusive stock ratings"; Composite Rating, RS — referenced in list descriptions and how-to video titles); "Stock Checkup" tool.
- Tools (root): Stock Screener (screenshot shown), IBD Stock Charts, Stock Quotes, My Stock Lists (portfolio), MarketSurge (charting platform, "100+ new technical indicators, endlessly customizable charts"), Leaderboard ("model portfolio of the best 10-15 stocks… plus full trading plans"), SwingTrader, MarketDiem (daily trade-ideas newsletter), IBD Live (Q&A).
- Monetization (root): IBD Digital subscription; per-product premium tools; newsletter subscriptions; heavy promotional offers.
- Market data (footer): "Real-time prices by Nasdaq Last Sale… Ownership data provided by LSEG and Estimate data provided by FactSet."
- Compliance posture (footer): "informational and educational purposes only… not an offer, recommendation, solicitation, or rating to buy or sell securities. Authors may own the stocks they discuss."
- Audience: growth-stock investors and traders; methodology-first (buy points, breakouts, relative strength).

## Cross-product Comparison

| Dimension | Seeking Alpha | Morningstar | MarketWatch | IBD |
|---|---|---|---|---|
| Center of gravity | crowdsourced analysis + news + quant ratings | staff research house + licensed news | financial journalism | methodology-driven lists + ratings |
| Content producers | paid contributor analysts + editors | staff analysts (CFA) + editors | staff journalists + columnists | staff analysts + methodology team |
| News stream | proprietary stock news, ticker-tagged | own + licensed (MarketWatch/Dow Jones) | own journalism (primary product) | own news + market-action coverage |
| Research/analysis layer | analysis articles, transcripts, quant grades | company reports (Fair Value/Moat), fund research | opinion columns, guides (light) | stock lists, stock-of-the-day, action plans |
| Instrument anchoring | symbol pages (/symbol/), ticker-tagged items | quote pages, company reports per company | ticker pages, ticker chips on stories | stock lists, charts, checkup per stock |
| Instrument data | licensed quotes (real-time/delayed by source), fundamentals, estimates | real-time index quotes; quote pages | FactSet intraday (delayed ≥15 min/exchange rules) | Nasdaq Last Sale real-time; LSEG ownership; FactSet estimates |
| Ratings layer | SA Analyst ratings + Quant ratings/factor grades | Fair Value/Economic Moat/Uncertainty (+ fund ratings) | none observed | proprietary Composite/RS ratings |
| Investor tools | portfolios, screeners, alerts/warnings, comparisons, customizable homepage | portfolio, watchlists, screener, compare, chart, rating changes, notifications | watchlist, search, game (light) | screener, charts, checkup, my stock lists, MarketSurge/Leaderboard/SwingTrader |
| Calendars | earnings calendar + transcripts | market calendar (earnings) | — (not observed on fetched surface) | earnings previews in research |
| Community | comments, disputes, Investing Groups chat | — (not observed) | — | — (IBD Live Q&A is editorial) |
| Newsletters | yes | yes (editor-curated) | yes | yes (MarketDiem etc.) |
| Video/podcast | yes | yes | yes | yes |
| Monetization | freemium + Premium/PRO/Alpha Picks/Groups marketplace | subscription + licenses + asset fees + ads + conferences | subscription + ads + commerce guides | subscription (IBD Digital) + premium tools |
| Audience | retail investors + pros (PRO) | individual investors + advisors | broad consumers/retail | growth-stock investors/traders |
| Compliance posture | informational-only; not a broker/adviser; editorial + anti-manipulation policies; dispute process | editorial independence; sales/author separation; corrections; transparency page | Dow Jones terms; corrections; newsroom roster | informational/educational only; author-ownership disclosure |
| Data licensing disclosure | explicit help article (vendors named) | footer real-time disclosure; licensed news attribution | footer FactSet + delay disclosure | footer Nasdaq/LSEG/FactSet disclosure |

### Cross-product commonalities (Layer B — across all four)

1. Instrument-anchored content: every product organizes content around identified instruments (symbol/quote/ticker pages; ticker chips; per-company reports/lists).
2. Continuously updated, dated news/analysis stream as the homepage's center.
3. First-party editorial function: all four produce/edit/commission content; none is a pure aggregator. (Morningstar even licenses third-party news and attributes the source — aggregation exists as a supplement, not the center.)
4. Investment-decision framing: ratings, fair values, buy points, stock picks, ideas — content is explicitly decision-oriented.
5. Instrument data attached to content under license, with visible sourcing/delay disclosures and redistribution prohibitions.
6. Investor tools wrapping content: watchlists and/or portfolios, screeners, alerts/notifications, charts — present in at least three of four (MarketWatch light: watchlist only).
7. Paywalls/subscription tiers gating premium content (locked ratings fields, "Go Premium" markers, subscribe prompts).
8. Multi-format content: articles + video + podcasts + email newsletters in all four.
9. Compliance posture: informational-only disclaimers; editorial policies; corrections (explicit in three; Dow Jones-level for MarketWatch).
10. Search spanning symbols and content.

### Common but not universal (Layer B, weaker)

- Proprietary ratings layer (3 of 4; MarketWatch none observed).
- Community discussion layer (1 of 4 strongly — Seeking Alpha).
- Earnings-call transcripts (Seeking Alpha explicit; Morningstar research covers earnings; not observed as a product for MW/IBD on fetched surfaces).
- Advisor-facing sections (Morningstar explicit; others not observed).
- Commerce/affiliate content (MarketWatch Guides; not observed elsewhere).
- AI assistance ("Ask Seeking Alpha", "Earnings Call Insights" — one product; emerging).

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately small)

A Financial News & Research Platform is recognizable when all three hold:

1. **Instrument-anchored content spine.** Identified financial instruments (and the issuers behind them) are organizing records; each instrument accumulates a persistent, growing body of news, analysis, and opinion on a stable instrument page, together with basic market data (price context). Without the spine → a general news/publication site.
2. **Platform-edited financial content stream.** A continuously updated stream of financial-market news and analysis/research that the platform itself produces, commissions, or edits (first-party editorial function — staff journalists, staff analysts, paid contributors, or proprietary methodologies). Without it → a data terminal or a raw aggregator.
3. **Investment-decision purpose.** The content exists to inform investment decisions (buy/sell/hold, allocation, timing), and the platform operates under an informational-only posture (content is opinion/information, not personalized advice or execution). Without it → general media.

Notes on the L0 boundary:
- The instrument data layer is included in property 1 at "basic market data" strength: every sampled product attaches price context to instrument records, but the depth (real-time vs delayed, fundamentals depth) varies by entitlement and is NOT definitional.
- "Research" in the leaf name is satisfied by the analytical layer (analysis/research content beyond wire news) — property 2 covers news AND analysis; a product with only breaking-news wires and no analytical layer would fail property 2's "analysis/research" half and drift toward News Application.

### L1 — Common Mature Structure (cross-product, Layer B)

- Instrument data layer: quotes (live/delayed by entitlement and source), charts, key statistics, fundamentals, estimates — licensed from upstream providers with sourcing/delay disclosures.
- Watchlists and/or portfolios (tracking and analysis only — no custody, no orders).
- Screeners over the instrument universe (frequently powered by the platform's proprietary ratings).
- Alerts/notifications (price, news, ratings conditions).
- Earnings calendars and event coverage; transcripts in research-oriented products.
- Ratings/opinion layer on instruments (proprietary quant models, staff analyst research opinions, or contributor ratings) — common but not universal (news-first products may lack it).
- Email newsletters (editor-curated).
- Multi-format content: articles, video, podcasts.
- Search across symbols, authors/analysts, and keywords.
- Mobile apps.
- Freemium/subscription monetization with paywalled premium content.
- Licensed-data compliance: redistribution prohibitions, "informational purposes only" disclaimers, ratings-are-opinions language.
- Editorial governance: editorial policies, corrections, (in some) separation of commercial and editorial staff.

### L2 — Variant / Optional Structure

- Content production model: staff journalism (news-first) / staff research house / crowdsourced contributors + editors / methodology-driven quant lists.
- Audience posture: retail-first / advisor-facing sections / professional tiers / trader-oriented.
- Asset-class scope: US equities+ETFs / funds+stocks+bonds+multi-asset / broad markets incl. personal finance & retirement editorial / growth-stock focus.
- Regional scope: US-centric vs global/multi-market.
- Community layer: comments, contributor economy, marketplace of subscription services, chat rooms.
- Ratings philosophy: quant-model ratings vs analyst-research opinions vs none.
- Commerce extensions: affiliate/commerce guides; marketplace revenue share.
- Business model: advertising+subscription mix vs pure subscription vs freemium.
- Legacy heritage: newspaper-derived (print lineage) vs research-firm-derived vs digital-native.
- AI assistance (Q&A over content, earnings-call insights) — emerging, single-product-observed in sample.
- Advisor workflow extensions (client-facing use of platform research) — drift toward Financial Advisor Platform.

### L3 — Vendor-specific (research notes only; must NOT enter the final document as Type facts)

- Seeking Alpha: Quant factor-grade taxonomy (Valuation/Growth/Profitability/Momentum/EPS Revisions; dividend grades; ETF grades), Alpha Picks, Quant Growth & Income portfolio, Investing Groups marketplace + Rocket.Chat rooms, "Ask Seeking Alpha" AI Q&A, "Earnings Call Insights", contributor payment system, pseudonymous-analyst policy, article-dispute process, Quodd/Cboe BZX/Nasdaq UTP/S&P Global/GICS/ClariFI sourcing chain, "Symbol Page" help category, customizable homepage.
- Morningstar: Fair Value / Economic Moat / Uncertainty / Capital Allocation methodology fields, Style Box, Rating Changes tool, Morningstar Investor / "Premium and Portfolio Manager" packaging, joe@morningstar.com support address, conferences business, asset-based-fee investment management, licensed MarketWatch/Dow Jones news display with attribution, real-time index-quote footer disclosure.
- MarketWatch: Moneyist Q&A column, MarketWatch Picks, MarketWatch Guides commerce newsroom (commission disclosure), Virtual Stock Exchange game, FactSet sourcing + "delayed at least 15 minutes or per exchange requirements" disclosure, Live Coverage, corporate subscriptions.
- IBD: IBD 50 / Sector Leaders / Big Cap 20 / New Highs / Relative Strength at New High / IPO Leaders / Stocks that Funds are Buying list family, Composite Rating & RS Rating, MarketSurge (100+ technical indicators claim), Leaderboard model portfolio, SwingTrader, MarketDiem, IBD Live Q&A, IBD Methodology / buy points / "Stocks On The Move" institutional-volume signal, Nasdaq Last Sale real-time + LSEG ownership + FactSet estimates sourcing, O'Neil heritage.

## Vendor-specific Findings

See L3 above. Additionally: paywall mechanics differ (per-field locking at Morningstar, per-article/rating locking at Seeking Alpha, subscription prompts at MarketWatch/IBD) — implementation detail, not Type structure.

## Boundary Findings

1. **vs Financial Market Data Terminal (processed).** Recorded seam from the terminal leaf: "the news stream/editorial content is the center; the terminal integrates news as one function among many." Confirmed from this side: all four sampled products center on a content stream with instrument anchoring, not on a function-navigated data workspace; none exposes terminal-style function codes/command navigation as the primary interaction. Removal tests: remove the editorial content stream → data terminal/screener product; remove the function workspace from a terminal → still a terminal. Boundary held. Straddle risk: research-flavored terminals (TIKR-class) — already flagged in the terminal leaf.
2. **vs Investment Research Platform (§08 sibling, UNPROCESSED).** Provisional seam: this Type serves a broad investor audience with a published editorial/analysis stream (news + analysis + ratings) organized for individual consumption; the investment-research-platform leaf is expected to center on institutional research workflow over documents (filings, transcripts, expert calls, research management). Overlap zone: transcripts, earnings coverage, research reports. Removal test (provisional): remove the news stream + broad-audience publishing posture → institutional research platform; remove the institutional document-workflow → this Type. **Joint-review flag recorded** — sibling unprocessed, seam provisional.
3. **vs News Application / News Aggregator (§02.04, unprocessed).** Seam: instrument anchoring + investment-decision purpose + first-party editorial/analytical layer + attached instrument data. A general news app aggregates/presents general news without symbol-anchored accumulation or market-data context. Removal test: remove instrument anchoring and the data layer → news app/aggregator. News-first products of this Type (MarketWatch-class) remain here because of ticker anchoring + market data + subscription research tools. Mild flag recorded in case §02.04 processing claims finance-vertical news products.
4. **vs Newsletter / subscription research services.** Individual newsletters and pick services (Alpha Picks, MarketDiem, Investing Groups services) are products INSIDE this Type (or adjacent consumer surfaces), not the Type itself; the Type is the platform that produces/aggregates content at scale with instrument anchoring. Newsletter Marketing Platform (§06) is a marketing tool — different Type entirely.
5. **vs Brokerage Platform / Retail Trading Platform (processed).** This Type holds no accounts, no custody, no order routing; monetization is content subscription/advertising, not trading. Brokerages attach news/research to accounts — content there is a feature of the account relationship.
6. **vs Financial Advisor Platform (processed).** Advisor platform = advisor-side practice system around client households. This Type = investor-facing content platform. Morningstar's "For Advisors" section is a variant posture (drift flag), not a change of center.
7. **vs Social investing surfaces (StockTwits-class, not a directory leaf).** Center is user-generated trade talk + social graph, not platform-edited content. Not researched in depth; noted as adjacent.
8. **vs Personal Finance Management Application.** Personal-finance TOPICS (retirement, mortgages) appear as editorial sections (MarketWatch, Morningstar) — editorial coverage of personal finance is not money management. Boundary held.

### "去掉什么就变成另一个 Type" 判据 (removal tests)

- Remove the platform-edited content stream → Financial Market Data Terminal / screener tool.
- Remove instrument anchoring + attached market data → News Application / general media site.
- Remove the analytical/research layer (keep only wire news) → News Application (finance-vertical).
- Remove the broad-investor publishing posture (keep institutional document workflow) → Investment Research Platform (provisional, joint review).
- Remove informational-only posture (add execution/accounts) → Brokerage/Trading Platform.

## §24 Historical / Market-Sample Check

- 1990s web finance portals (Yahoo Finance from 1997, AOL Personal Finance, MSN Money Investor, Quicken.com): quotes + news + symbol pages + portfolios, free, ad-supported — fit L0 without quant ratings, paywalls, apps, or AI. ✓
- Newspaper-derived digital products (MarketWatch 1997; IBD's digital presence of a print newspaper; WSJ/Barron's digital): fit — editorial stream + ticker anchoring + data. ✓
- Research-firm-derived products (Morningstar.com in the 1990s–2000s; Value Line–class research publishers moving online): fit. ✓
- Digital-native contributor platforms (Seeking Alpha 2005-era "alpha" blogs → platform): fit. ✓
- Printed financial newspapers (print WSJ/IBD editions): NOT this Type — no instrument-anchored platform, no data layer; they are publishing, and only their digital platform forms are in scope. ✓ (consistent with the "platform" element of the leaf name)
- Terminal-resident news wires (news inside Bloomberg/Reuters terminals): different Type (terminal); news there is a function, not the center. ✓
- Conclusion: the L0 does not overfit to the modern free+premium web-portal pattern; older/regional/heritage products fit without modern L1 features.

## Uncertainties

1. Yahoo Finance, Investing.com, Benzinga, TipRanks, TheStreet, Zacks unreachable (403/bot-blocked). The portal pole (Yahoo Finance-class) and the news-wire pole (Benzinga-class) and analyst-aggregation pole (TipRanks-class) are therefore characterized only indirectly (e.g., Morningstar displaying licensed MarketWatch/Dow Jones news; IBD's Dow Jones network membership). No operational claims are made for these products anywhere.
2. Investment Research Platform sibling unprocessed — boundary provisional; joint-review flag recorded.
3. Community layer prevalence unknown beyond the sample (only 1 of 4 observed) — kept out of the defining core; described as a variant.
4. Whether §02.04 News Application processing will claim finance-vertical news products — mild flag; this pass holds the boundary on instrument anchoring + data layer + investment-decision purpose.
5. AI-assistance prevalence unknown (single-product observation) — treated as emerging variant.
6. Mobile app prevalence assumed common (3 of 4 observed app links; Morningstar app not directly observed) — described as common, not universal.

## Final Synthesis

The Financial News & Research Platform is the investor-facing content platform of the financial domain: it produces or edits a continuous stream of financial news and analysis, anchors that content to identified instruments (symbol pages that accumulate news, analysis, ratings, and price context over time), wraps the content in investor tools (watchlists, portfolios, screeners, alerts, calendars), gates depth behind subscriptions, and operates under an informational-only, licensed-data compliance posture. Its center is content; the market data terminal's center is the data workspace; the (unprocessed) investment research platform's expected center is institutional research workflow. The defining core is three properties — instrument-anchored content spine, platform-edited content stream, investment-decision purpose — and everything else (data depth, ratings systems, community, commerce, AI, advisor extensions) is common mature structure or variant posture.
