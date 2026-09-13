# Research Notes — Investment Research Platform

Research date: 2026-09-07

## Research Goal

Understand what an Investment Research Platform actually is as an Application Type: what research material it holds, how that material is organized and kept current, what research workflow the user runs through it, what surfaces it exposes, how it is monetized and gated, and where it separates from neighboring Types (Financial Market Data Terminal, Financial News & Research Platform, Professional Trading Terminal, Brokerage Platform, Portfolio Management System, AI Research Assistant).

## Initial Boundary

Working hypothesis before research:

1. Core purpose: a workspace where investment professionals and serious investors conduct research on investable subjects (companies, securities, funds) — finding, reading, extracting, monitoring, and synthesizing information into investment decisions.
2. Likely users: buy-side analysts, portfolio managers, investment bankers, corporate development, consultants; at the other end, individual serious investors.
3. Nearest neighbors: Financial Market Data Terminal (live-data workspace), Financial News & Research Platform (edited content stream), Brokerage/Trading platforms (execution), Portfolio Management System (portfolio book of record), AI Research Assistant (generic).
4. Known flags to discharge (recorded by processed siblings):
   - financial-market-data-terminal pass: "research-flavored terminals straddle — TIKR keeps the terminal's instrument/function spine but its center of gravity is research content and workflow … recommend joint review when investment-research-platform is processed."
   - financial-news-research-platform pass: "provisional seam — this Type centers on a platform-edited news+analysis stream for a broad investor audience; investment-research-platform expected to center on institutional research workflow over documents … recommend joint review."
5. Unknowns: the exact material families that make up the "research corpus"; whether capture/synthesis machinery (models, notes, deliverables) is definitional or optional; how deep the AI layer has penetrated; whether consumer-tier products (Seeking Alpha-class) belong in this Type or the news Type.

## Research Questions

1. What material families compose the research corpus (filings, transcripts, estimates, financials, broker research, expert calls, contributor analysis, news)?
2. How is the corpus organized — around identified issuers/symbols? document types? themes?
3. What is the core research loop (find → read → extract → monitor → synthesize → deliver)?
4. What surfaces exist: search, screener, subject/company pages, transcript viewers, watchlists, dashboards, model builders?
5. What monitoring machinery exists (alerts, saved searches, watchlists, dashboards)?
6. What capture/synthesis machinery exists (valuation models, notes, exports, AI answers, deliverables)?
7. How do data licensing and extraction shape the corpus (third-party providers vs proprietary extraction; auditability)?
8. What audience tiers are served and what changes with tier (collaboration, compliance, API, add-ins)?
9. What is the AI layer's role — definitional or era-typical?
10. Where are the boundaries vs terminal / news platform / brokerage / PMS / generic AI assistant, and how are the two sibling flags discharged?

## Representative Products

Selected for market representation, documentation availability, different product philosophies, and different customer tiers:

| Product | Tier / philosophy | Evidence level |
|---|---|---|
| AlphaSense | Enterprise "market intelligence and search platform" — AI search over a massive curated document corpus (filings, broker research, expert transcripts, internal content) | Tier-1 help center (2 articles) + product pages; Tegus (now part of AlphaSense) transition page |
| TIKR | Prosumer "research terminal" — valuation-workflow-first: long-history fundamentals, screener, transcripts, valuation model builder, guru/insider portfolio tracking | Tier-2 product pages (root + linked feature pages); help desk unreachable |
| Fiscal.ai | AI-native data infrastructure + web terminal — auditable fundamentals linked to source, estimates, transcripts, IR content; Terminal + API + MCP products | Tier-1 help center FAQ + product pages |
| Seeking Alpha | Consumer/prosumer "financial research platform" — contributor analysis community + quant ratings + screeners + portfolios + earnings transcripts | Tier-2 root page incl. About section and full navigation |

Rejected/absent from sample: Morningstar Direct (institutional research database; site returned empty content twice — recorded as sampling limitation, not dropped for lack of fit); Tegus standalone (absorbed into AlphaSense — observed directly on tegus.com); Bloomberg/FactSet terminals (assigned to Financial Market Data Terminal by the processed sibling pass; used as boundary anchors only).

## Sources

- AlphaSense — https://www.alpha-sense.com/ (root product page; platform/content/solutions navigation)
- AlphaSense Help Center — https://help.alpha-sense.com/hc/en-us/articles/41098563605395-Getting-Started-in-AlphaSense
- AlphaSense Help Center — https://help.alpha-sense.com/hc/en-us/articles/41702241422995-When-to-use-Document-vs-Generative-Search
- Tegus (now part of AlphaSense) — https://www.tegus.com/ (transition page)
- TIKR — https://tikr.com/ (root; linked feature pages: screener, fundamental analysis, valuation model builder, portfolio tracking, investor-stock-portfolio)
- Fiscal.ai — https://fiscal.ai/ (root), https://fiscal.ai/products/terminal/, https://fiscal.ai/help/ (FAQ)
- Seeking Alpha — https://seekingalpha.com/ (root incl. About section, navigation taxonomy, portfolio/screener surfaces)

Failed sources (per source-access limitation rules): www.alphaspense.com and help.alphaspense.com — transport error ×2 (reachable only via www.alpha-sense.com); tikr.zendesk.com — timeout + transport error ×2 (TIKR asserted at product-page level only); www.morningstar.com/products/direct — empty response ×2 (institutional database pole under-observed); seekingalpha.com/page/our_mission — 404 (root page used instead).

## Product A — AlphaSense (enterprise pole; includes absorbed Tegus)

### Key observations (evidence layer A unless noted)

- Self-labels a "Market Intelligence and Search Platform"; "Accelerate your workflow with AI insights you can trust"; claims 7,000+ enterprise customers across financial services (investment banking, hedge funds, private equity, asset management, VC), corporations (life sciences, TMT, energy, industrials, consumer), consulting, law firms, insurance.
- Content universe: "500+ million premium financial and business documents" — Tegus expert transcripts, broker research, company filings, private and public financial data, "alongside your firm's internal content" (users can bring internal decks, reports, notes into the platform and search them alongside external content).
- Tegus absorption page (tegus.com): "Tegus is now part of AlphaSense"; enumerates 260,000+ expert transcripts, expert call services, 4K+ pre-built Canalyst financial models, 500M+ documents, 1,500 global and regional broker partners.
- Search is described as "the foundation of how AlphaSense delivers value"; two modes: Document Search (keywords + companies; raw results; alerts-able) and Generative Search (natural-language questions; synthesized summary). Official help-center "D.N.A. Framework" (Deliverable / Narrowness / Alerts) teaches when to use each — evidence that search + monitoring (alerts) is the product's spine.
- Help center Getting Started: Dashboard "to organize and monitor all your information streams at-a-glance"; Company and Keyword search bars; filtering content sets; "staying up to date."
- AI layer: Deep Research ("in-depth, multi-step research, autonomously"), SuperAnalyst ("always-on AI agent"), Workflow Agents library (company primers, diligence scans, industry overviews "in one click"), comparison grid across "hundreds of perspectives side-by-side — earnings calls, broker research, expert interviews"; claims sentence-level citations.
- Output machinery: PowerPoint and Excel Add-Ins ("build and iterate on financial models in Excel, populate and refresh presentations in PowerPoint, generate slide decks and reports directly in the platform"); Connectors; mobile app; developer portal (API).
- Solutions include "Financial Research" (self-labeled /solutions/financial-research-platform/), Aftermarket Research, Analyst Reports, Broker Reports, Expert Calls, Channel Checks, Due Diligence, ESG Data, Sentiment Indices.
- Enterprise posture: Credit Usage Dashboard (usage-metered), login at research.alpha-sense.com, training sessions, trust center.

## Product B — TIKR (prosumer terminal-flavored pole)

### Key observations

- Self-labels "TIKR Terminal": "Find the best stocks, follow top investors, quickly analyze businesses, and monitor your portfolio." Positioning: "Go From Idea to Conviction Without Leaving TIKR — Screen 100,000+ global stocks, pull up to 30 years of financials, read the transcript, and build your valuation model in one workflow."
- Subject-anchored workspace: per-company tabs shown in product imagery (Detailed Financials, Valuations, Transcripts, Screener, Dashboard, Investing Gurus).
- Fundamentals sourcing: "accurate financial data powered by S&P Global CapitalIQ on 100,000+ stocks across 92 countries and 136 exchanges" — third-party licensed data is structural.
- Screener: "thousands of filters including by country, industry, financials, ratios, Wall Street analyst forecasts, valuation multiples, capital structure, growth rates, and margins."
- Monitoring: portfolio tracking + "watchlist news feed that highlights upcoming events, company news, earnings & conference transcripts, and company filings"; customizable news topics.
- Synthesis: Custom Valuation Builder — "build dynamic, forward-looking models … without touching a spreadsheet. Start from a prebuilt template or build your own … save models to your dashboard and revisit anytime."
- Tracking investors: "portfolios of 10,000+ investors, including company insiders, hedge funds" beyond US 13F — filings-derived tracking content.
- Business model: free signup, subscription tiers (pricing page exists; precise figures not recorded here).
- Straddle note (from the terminal pass, confirmed): TIKR self-labels "Terminal" and retains an instrument/function spine, but its center of gravity is research content and workflow; its own comparison pages target both terminals (Bloomberg, FactSet) and research platforms (AlphaSense, Sentieo, YCharts, Seeking Alpha).

## Product C — Fiscal.ai (AI-native data-infrastructure + terminal pole)

### Key observations

- Self-labels "The Complete AI Powered Stock Research Platform" and "Modern Financial Data Infrastructure"; the terminal is "The Complete Public Company Research Terminal … Auditable fundamentals updated within minutes and powerful tools for company research."
- Two-sided identity: research terminal for investors (hedge funds, asset managers, individuals) + data-feed supplier to other platforms (Google Finance, KPMG, Perplexity, VanEck logos as customers) via Data Feed API and MCP Connectors.
- Terminal content stack: "global data across financials linked to source, estimates, transcripts, IR content, filings, news, ownership and more."
- Data pipeline: Aggregated Filings & IR → Extraction & Verification ("human analyst verification", "auditable to source") → delivered via Terminal/API/MCP. Proprietary data for US/Canada/ADR/UK/EU fundamentals; S&P Capital IQ for other geographies (help FAQ).
- Help FAQ confirms subject-anchored structure: company pages with Financials tab incl. Segments & KPIs sub-tab; Dashboards (tickers added from company page or dashboard search; metric headers); Events (Calls, Transcripts & Slides); Estimates; screener tutorials ("How to Screen For Stocks"); "Ultimate Guide" describing "the all-in-one research platform for fundamental investors."
- Monitoring variant: "Connect Brokerage" — brokerage account connections for portfolio display in the dashboard (read-only monitoring, not execution).
- Export/deliverable machinery: dashboard table export (all plans), financial-data export on higher plan, no Excel add-in but MCP lets AI tools autofill spreadsheets with Fiscal data.
- Gating: free tier with deep limits (10y financials, 1 event, 1 dashboard), Pro/Max subscriptions, separate annual API/MCP subscription; 7-day trial. Coverage: 100,000+ public companies/ETFs/funds; Segments & KPIs for 2,500+.

## Product D — Seeking Alpha (consumer/community pole)

### Key observations

- Self-label (About section): "an industry-leading financial research platform powered by one of the world's largest investing communities … in-depth analysis on thousands of stocks to timely investment ideas and market-beating Quant ratings … an essential resource for millions of investors globally."
- Content corpus: platform-published + contributor-published analysis ("Trending Analysis" by named analysts), market news, earnings-call transcripts, "Earnings Call Insights", editor picks, sector/dividend/ETF content trees, podcasts/videos, education.
- Contributor economy: "Investors contribute articles … because they receive payment, exposure … and the ability to run their own subscription research business in our Investing Groups"; editors vet analysts ("must be accepted by our editors … quality and compliance standards").
- Research tooling: Stock Screener + ETF Screener with saved preset screens (Top Rated, Top Growth, Top Value, Most Shorted…), Comparisons (peer sets), Portfolios ("Create Portfolio+", "Portfolio Health Check"), Quant Ratings and analyst ratings on symbol pages (paywalled), Earnings Calendar, "My Stocks" watchlists, Save buttons on articles.
- Navigation taxonomy (observed): Stock Ideas / Market News / Market Data / Sectors / Dividends / ETFs / Earnings / Education / Podcasts / Videos + Investing Groups + Portfolios + Find & Compare — content stream and tooling coexist; tooling is research-workflow oriented (screeners/ratings/portfolios), not an edited-news-only posture.
- Paywall mechanics: per-article/per-rating locks ("Locked. Go Premium…"), Premium/Alpha Picks/Quant Growth & Income subscription products.

## Cross-product Comparison

| Dimension | AlphaSense | TIKR | Fiscal.ai | Seeking Alpha |
|---|---|---|---|---|
| Self-label | Market Intelligence and Search Platform | TIKR Terminal | AI Powered Stock Research Platform / research terminal | Financial research platform |
| Audience | Enterprise (funds, banks, corporations, consulting) | Individual serious investors | Individuals → institutions (plus data feeds to platforms) | Mass serious-retail / contributors |
| Corpus: primary documents | filings + broker research + expert transcripts (+ internal uploads) | transcripts, filings (watchlist feed) | filings, transcripts, IR content, slides | transcripts, filings referenced in articles |
| Corpus: structured data | private/public financial data | long-history financials + forecasts (CapitalIQ) | auditable fundamentals linked to source + estimates + KPIs | quant factor data, estimates views, calendars |
| Corpus: analysis | broker research (licensed), expert calls | analyst forecasts; superinvestor tracking | internal team blog/research (secondary) | contributor analysis economy + editor curation |
| Subject anchoring | Company Profiles; Company + Keyword search | per-company tabs (Financials/Valuations/Transcripts) | company pages, Financials + Segments & KPIs tabs | symbol pages with ratings |
| Find machinery | Document Search + Generative Search + Smart Synonyms | Screener (100k+ stocks, thousands of filters) | Screener + dashboard search | Screener/ETF screener + keyword search |
| Monitor machinery | email alerts on saved searches; Dashboard streams | watchlist + news feed of events/filings | dashboards + brokerage connections; update-speed posture | My Stocks, Portfolios, Health Check |
| Capture/synthesis | Deep Research agents, decks/reports generation, Excel/PPT add-ins, Search Library | valuation model builder (templates, saved to dashboard) | exports, dashboards, KPI extraction, MCP-to-AI autofill | saved articles/portfolios (lighter) |
| AI layer | Deep Research, SuperAnalyst, Workflow Agents, Generative Search (centrally marketed) | not prominently marketed on root page | "AI powered" positioning; MCP connectors for AI tools | AI features not directly evidenced this pass |
| Execution | none | none | none (brokerage connection is display-only) | none |
| Delivery surface | web app + mobile + Excel/PPT add-ins + API | web terminal | web terminal + API + MCP | web + apps (implied) |
| Gating | enterprise subscription, usage credits | freemium + subscription | freemium + subscription + separate API/MCP | freemium + premium locks |

Cross-product commonalities (evidence layer B):

1. Identified issuers/symbols anchor everything: search targets, pages, screens, watchlists.
2. A continuously maintained corpus in three material families — primary issuer documents (filings, earnings-call transcripts, IR material), structured financial data (fundamentals, estimates), and professional analysis (broker research, expert calls, contributor analysis) — with each product assembling a different mix.
3. A find → monitor → synthesize research loop: search/screen across the corpus; monitor subjects/saved queries for new material; capture the work into user-owned research state (watchlists, saved searches, models, dashboards, exports, deliverables).
4. Informational-only posture: no order routing, no custody; monetization is subscription/gating of the corpus and tooling.
5. New-material currency: the corpus updates as issuers publish (filings, transcripts), with several products making update speed a marketing claim.
6. Data provenance is a visible structural concern: third-party licensing (TIKR: CapitalIQ; Fiscal: CapitalIQ for some geographies; AlphaSense: broker partners) or proprietary extraction marketed as auditable/linked to source (Fiscal; AlphaSense sentence-level citations claim).
7. AI over the corpus is now prominent in enterprise/AI-native products (AlphaSense, Fiscal) and marketed as grounded/cited; not yet universally definitional across the tier range.

## Canonical Model

### L0 — Defining Invariant (remove any → a different Type)

1. **The identified investable subject as anchor** — issuers/securities/funds exist as identified records to which all research material binds (search, screens, pages, watchlists). Remove → a generic document search or unanchored content site.
2. **The maintained research corpus** — a continuously updated, accumulating body of subject-bound research material drawn from the three families (primary documents, structured financial data, professional analysis), which the platform curates/ingests/licenses/extracts. Remove → a quote/chart live-data workspace (terminal) or a broker's account page.
3. **The research interrogation loop** — machinery for the user's own research work: find (cross-corpus search and screening), monitor (subjects and saved queries with alerts/new-material feeds), capture/synthesize (user-owned research state: watchlists, saved queries, models, notes, exports, deliverables). Remove find → a static report library; remove monitor/capture → a read-only publisher's archive (drifts to Financial News & Research Platform).
4. **Informational-only posture** — the platform's output feeds decisions made elsewhere; no order routing, no custody/accounts. Remove → brokerage/trading platform (research becomes an account feature).

### L1 — Common Mature Structure (evidence layer B)

- Screener across the instrument universe with financial/estimate/valuation criteria.
- Per-subject page accumulating the corpus for that subject (financials, estimates, transcripts, filings, analysis, ownership).
- Saved searches / search library; email or in-app alerts on monitored queries and subjects.
- Watchlist / portfolio monitoring surfaces (incl. consumer-grade brokerage connections for display).
- Comparison machinery across subjects (peer sets, side-by-side grids).
- Export and deliverable paths (Excel/data exports; presentation generation at the enterprise pole).
- Event machinery around earnings (calendars, transcripts, slides).
- Entitlement/gating of the corpus by subscription tier; usage metering at the enterprise pole.
- AI assistance over the corpus (Q&A, summaries, drafted deliverables) — dominant in current enterprise/AI-native products; era-typical rather than definitional.

### L2 — Variant / Optional Structure

- Audience tier: enterprise seats/collaboration vs prosumer solo vs consumer community.
- Corpus pole: document/search-first (AlphaSense), data/valuation-first (TIKR, Fiscal), analysis/community-first (Seeking Alpha).
- Expert-call/expert-network content with its compliance regime (observed at the AlphaSense/Tegus pole only — single-pole posture in this sample).
- Broker/sell-side research licensing (aftermarket research).
- Internal-content integration (upload firm decks/notes to search alongside external corpus) — enterprise-pole capability.
- Delivery extensions: API/data-feed products (Fiscal API/MCP), office add-ins (AlphaSense Excel/PPT), mobile apps.
- Data-supplier posture: some platforms also wholesale their data to other platforms (Fiscal's API/MCP business).
- Adjacent-audience extension: corporate strategy/competitive-intelligence use (AlphaSense solutions for corporations/consulting/law) — drift toward Competitive Intelligence Platform.
- Asset-class scope: equities-dominant with fund/ETF coverage in the sample; multi-asset breadth not directly observed here.
- Historical/adjacent forms: institutional research databases (fund research), sell-side research aggregators — adjacent realizations not deep-observed this pass.

### L3 — Vendor-specific (research notes only)

- AlphaSense: "D.N.A. Framework" (Deliverable/Narrowness/Alerts), Smart Synonyms, SuperAnalyst, Deep Research, Workflow Agents library, Four Perspectives, Canalyst Models, Sentiment Indices, Credit Usage Dashboard, AlphaDemics academic program, "500M+ documents", "7,000+ enterprises", "1,500 broker partners" (via Tegus page), research.alpha-sense.com login, help center by Zendesk.
- TIKR: "30 years of financials", "100,000+ stocks across 92 countries and 136 exchanges", "10,000+ tracked investors", S&P Global CapitalIQ sourcing, "Superinvestors"/guru portfolio tab, valuation-builder templates, competitor-comparison page family (Bloomberg/FactSet/AlphaSense/Sentieo/Seeking Alpha…), free-signup funnel.
- Fiscal.ai: auditable-to-source pipeline with human analyst verification, "updated within minutes" post-earnings claims (3–7 min covered geographies, 24–48h via CapitalIQ; 15-min delayed prices), free-tier limits (10y/6q financials, 1 event, 1 dashboard/30 rows), Pro $49/Month-class pricing, Segments & KPIs (2,500+ companies), brokerage-connection display, MCP Connectors (Claude tutorial), Stratosphere Technology Inc. legal entity.
- Seeking Alpha: Quant factor-grade system and ratings paywall, contributor payment + Investing Groups marketplace (analysts run subscription businesses), Alpha Picks / Quant Growth & Income products, "Earnings Call Insights", editor-acceptance of analysts, per-rating "Locked. Go Premium" mechanics.

## Boundary Findings

1. **vs Financial Market Data Terminal (§08, processed) — joint-review flag DISCHARGED from this side.** The terminal's center is the instrument-centered live-data workspace (market state bound to instruments under licensed entitlements, function-navigated, persistent instrument context; observation/monitoring loop). This Type's center is the research corpus and the interrogation loop over it (documents/estimates/analysis; find → monitor → synthesize). Removal tests confirmed both directions: remove live market data / the function workspace → a research platform; remove the research corpus and capture/synthesis (keep quotes/charts/functions) → a terminal or screener. TIKR is the documented straddler: it self-labels "Terminal" and keeps an instrument/function spine, but its center of gravity is long-history fundamentals + valuation workflow + transcripts + tracking content, and its own comparison pages span both categories. Adopted resolution: TIKR is in-sample for this Type as a research-center product with terminal-adjacent surface; the seam is held on center of gravity, consistent with the terminal pass's recorded test ("remove live market data → research platform"). Naming collision ("terminal" used by research products) documented as market vocabulary drift, not type fusion.
2. **vs Financial News & Research Platform (§08, processed) — joint-review flag DISCHARGED from this side.** The news Type centers on a platform-edited, continuously-updated content stream for a broad investor audience, informational-only, with instrument-anchored pages. This Type centers on the corpus + interrogation machinery for the user's own research work. Overlap zone is real: transcripts, earnings coverage, and research reports appear on both sides, and Seeking Alpha was sampled by BOTH passes (it has a news stream AND research tooling + a contributor research economy + quant ratings + screeners + portfolios). Adopted resolution: Seeking Alpha is assigned to this Type as the consumer-pole straddler because its center of gravity is research content consumption plus research tooling and its own monetized research community, not an edited news stream; the boundary is held on center of gravity + presence of user-side research machinery (find/monitor/capture). Recommendation for human/taxonomy review: the two Types share a graded overlap zone (news-stream-first → tooling-first); cross-reference both documents when the directory is consolidated. Boundary direction from the sibling's removal test confirmed: "remove the news stream + broad-audience publishing posture → institutional research platform."
3. **vs Professional Trading Terminal / Brokerage Platform / Retail Trading Platform (all processed).** Informational-only posture: no order construction/routing, no accounts/custody. Consistent with the brokerage pass ("去掉证券托管与成交记录 → Investment Research Platform") and the retail-trading pass ("content products hold no accounts and take no orders"). Boundary clean in this sample; Fiscal's "Connect Brokerage" is display-only monitoring, not execution.
4. **vs Portfolio Management System (§08, processed).** PMS is the institution's book of record for portfolios (positions/cash/intent/checked change loop). This Type holds no portfolio book; user-side watchlists/portfolios are monitoring conveniences over the corpus, not managed books. The investment-management-platform pass independently recorded research/data surfaces as "inputs consumed by the platform" — consistent.
5. **vs AI Research Assistant (§02.03, unprocessed).** A generic AI research assistant answers questions over user-supplied or web corpora. This Type's defining base is a maintained, licensed/extracted, subject-anchored corpus with domain objects (estimates, filings, transcripts) and monitoring machinery; AI is a delivery layer over it. If AI were removed, sampled products remain recognizably research platforms (historical check below).
6. **vs Due Diligence Platform / Virtual Data Room (§11).** This Type aggregates public-domain issuer material (filings, transcripts, licensed research) at continuous scale; data rooms host deal-specific confidential document sets for controlled sharing. AlphaSense markets a due-diligence *solution* over its corpus — capability framing, not a change of center.
7. **vs Market Research Platform (§06) / Competitive Intelligence Platform (§06).** Different object worlds (consumer/commercial markets and brand competition vs investable subjects). AlphaSense's corporate/consulting solutions document genuine drift toward competitive intelligence; recorded as variant posture (L2), with the competitive-intelligence pass independently noting the different audience/object world.
8. **vs Financial Modeling Application (§08 leaf).** Valuation-model building appears inside sampled products (TIKR valuation builder; AlphaSense Excel add-in; Canalyst models). Modeling embedded in a research corpus/monitoring platform is a capability here; standalone modeling tools remain a separate leaf. No conflict; noted for that leaf's pass.

### "去掉什么就变成另一个 Type" 判据 (removal tests)

- Remove the research corpus (keep live quotes/charts/functions) → Financial Market Data Terminal.
- Remove the interrogation loop (keep a browsable edited stream) → Financial News & Research Platform.
- Remove informational-only posture (add accounts/order routing) → Brokerage/Trading Platform.
- Remove the subject anchoring → generic document search / AI research assistant.
- Remove the corpus entirely → nothing; the Type has no center.

## §24 Historical / Market-Sample Check

- Would older products fit? Pre-AI research platforms (the S&P Capital IQ-era pattern: filings + financials + screening + saved work) satisfy all four invariants without AI, add-ins, or expert networks. ✓
- Would terminal-era research delivery fit? Sell-side/broker research consumed through terminal workstations was distribution over someone else's platform; where the research corpus and interrogation workflow are the product's center (not the live-data workspace), it satisfies this Type — the terminal pass's removal test handles the reverse case. ✓
- Would pre-digital ancestors fit? Print-era investment research services (ranked research sheets, coverage manuals) carried corpus + ratings + monitoring-as-publication, but the *platform* form — interactive interrogation machinery over a maintained digital corpus — is what this directory node names; print-era services are recorded as ancestors, not members. ✓ (definitional choice recorded, not a boundary failure)
- Would free finance portals fit? Free quote/news portals with symbol pages shade into the news/portal side; where they lack a maintained research corpus + interrogation machinery as the center, they belong to the sibling Types. ✓
- Regional check: sampled products are global-coverage but US/EU-centric operations; regional research platforms (e.g., Asia-local data + research services) were not directly sampled — flagged under Uncertainties rather than assumed.

## Uncertainties

1. Morningstar Direct (institutional research-database pole, funds+equities) unreachable ×2 — the "database-first institutional" realization is inferred from category knowledge, not directly evidenced; no claims rest on it.
2. TIKR operational details (help desk unreachable ×2) — TIKR asserted at product-page level only; no watchlist/alert mechanics claimed for it beyond the root page's description.
3. Seeking Alpha's AI features were not directly evidenced this pass (recorded only in the sibling news pass's notes); AI commonality is asserted from AlphaSense + Fiscal only (two of four).
4. Expert-network compliance regimes: observed as product posture (Tegus/AlphaSense compliance surfaces) but the operating rules (MNPI controls, call vetting) were not researched; kept out of the final document beyond a soft posture note.
5. Collaboration machinery inside enterprise products (shared workspaces, permissions) is implied by the enterprise tier and internal-content uploads but not directly documented; kept out of the final document.
6. Multi-asset/fund-heavy institutional realizations (Morningstar-class) may widen the subject universe beyond issuers; unresolved due to the sourcing gap.

## Final Synthesis

The Investment Research Platform is the investor's research-workspace system: identified investable subjects anchor a maintained, accumulating corpus of research material (primary issuer documents, structured financial data, professional analysis), and the platform's defining job is the interrogation loop — find across the corpus, monitor subjects and saved queries for new material, and capture/synthesize the work into user-owned research state — all in an informational-only posture that ends where execution begins. Products differ by corpus pole (document/search-first, data/valuation-first, analysis/community-first) and audience tier (enterprise → prosumer → consumer), with AI as an era-typical delivery layer over the corpus. The Type is bounded from the Financial Market Data Terminal (live-data workspace center), the Financial News & Research Platform (edited-stream center), trading/brokerage Types (execution), and the Portfolio Management System (book of record).
