# Investment Research Platform

## Overview

An **Investment Research Platform** is an investor's research workspace: it maintains a continuously updated body of research material about investable subjects — companies, securities, funds — and provides the machinery an investor uses to interrogate that material: finding information across the corpus, monitoring subjects for new developments, and capturing the work into their own research output.

The defining structure is small:

```text
Identified investable subjects (issuers / securities / funds)
└── Maintained research corpus bound to those subjects
    ├── primary issuer documents (filings, earnings-call transcripts, IR material)
    ├── structured financial data (fundamentals, estimates)
    └── professional analysis (broker research, expert calls, contributor analysis)
└── Research interrogation loop
    ├── find (search and screening across the corpus)
    ├── monitor (subjects and saved queries for new material)
    └── capture / synthesize (watchlists, saved queries, models, exports, deliverables)
└── Informational-only posture (no order execution, no custody)
```

Everything else commonly associated with these products — AI question-answering, valuation model builders, expert-call networks, licensed broker research, brokerage-account connections, office add-ins, APIs — is widespread in current products but is not what makes the product an investment research platform. Older, pre-AI research databases and differently positioned products fit the same definition without any of those specifics.

When the center of gravity shifts to a live-data workspace organized around instruments and functions, the product is a Financial Market Data Terminal; when it shifts to a platform-edited content stream for a broad audience, it is a Financial News & Research Platform; when it adds accounts and order routing, it becomes a Brokerage or Trading Platform.

## Users & Context

The primary user is a person who makes or supports investment decisions and needs to do original research work, not just consume commentary:

- **buy-side analysts and portfolio managers** — build and maintain coverage of companies; test an investment thesis against filings, transcripts, estimates, and expert perspectives
- **investment bankers and corporate development teams** — research companies and industries for pitches, diligence, and comparables
- **serious individual investors** — screen for ideas, analyze companies in depth, track their holdings and watchlists
- **adjacent professionals** — consultants, corporate strategy, and legal teams use the same corpus for market and competitive questions (an extension posture, not the center)

Typical reasons to open the application:

- screen the universe of stocks for candidates matching financial or valuation criteria
- deep-dive one company: read its filings and earnings-call transcripts, inspect its financials and estimates
- check what changed on covered companies since last time (new filings, transcripts, analysis)
- compare a set of peer companies side by side
- build or update a valuation model, then export or present the result

The work environment is a web workspace (often called a "terminal" by its products); enterprise deployments add team access, office add-ins, and APIs. The platform sits upstream of execution: conclusions formed here are acted on in a brokerage, trading, or portfolio-management system elsewhere.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as an investment research platform:

- **Identified investable subjects as the anchor** — issuers, securities, and funds exist as identified records, and every piece of research material binds to them: search targets them, screens filter them, pages accumulate them, watchlists track them. Without subject anchoring, the product is a generic document search or an unanchored content site.
- **A maintained research corpus** — the platform curates, ingests, licenses, or extracts a continuously updated, accumulating body of subject-bound material. The material comes in three families, and products mix them in different proportions:
  - *primary issuer documents* — regulatory filings, earnings-call transcripts, investor-relations presentations
  - *structured financial data* — historical fundamentals, segment/KPI detail, analyst estimates
  - *professional analysis* — licensed broker research, expert-call transcripts, contributor or in-house analysis
  Without the corpus there is no product; with only live quotes and charts it is a market-data terminal.
- **The research interrogation loop** — machinery for the user's own research work, in three movements: *find* (search and screening across the whole corpus), *monitor* (subjects and saved queries watched for new material, with alerts or feeds), and *capture/synthesize* (user-owned research state: watchlists, saved searches, valuation models, notes, exports, deliverables). Remove find and the product is a static report library; remove monitor and capture and it is a read-only publisher's archive.
- **Informational-only posture** — the platform's output feeds decisions made elsewhere. There is no order routing, no custody, no account relationship. Add execution and the research becomes a feature of a brokerage or trading platform.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They are not what makes the product a research platform, but they make the research loop practical:

- **Screener** — filter the instrument universe by country, industry, financial metrics, ratios, valuation multiples, growth, and analyst forecasts; save screens for reuse.
- **Subject page** — a per-company (or per-fund) surface accumulating that subject's material: financial statements, estimates, transcripts, filings, analysis, ownership. This is the corpus made navigable.
- **Saved searches and alerts** — persist a query and be notified when new material matches; the monitoring half of the loop.
- **Watchlists and portfolio monitoring** — the user's list of subjects with a feed of new events, filings, transcripts, and news; some consumer products connect brokerage accounts to display holdings (read-only).
- **Comparison machinery** — side-by-side comparison of peer companies across financials, multiples, and estimates.
- **Event machinery** — earnings calendars and the transcript/presentation record of earnings events.
- **Export and deliverable paths** — data exports to spreadsheets; at the enterprise pole, office add-ins and generated decks/reports that carry the research into the user's documents.
- **Entitlement gating** — the corpus and tooling are gated by subscription tier; enterprise products meter usage and manage seats.
- **AI assistance over the corpus** — question-answering, summarization, and drafted deliverables grounded in the corpus with citations. Dominant in current enterprise and AI-native products; an era-typical layer rather than a defining one.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Products realize each concept differently:

```text
Concept:          Maintained research corpus
Implementations:  licensed third-party data + aggregated filings/transcripts,
                  proprietary extraction pipelines audited to source documents,
                  licensed broker research, expert-network transcripts,
                  contributor-written analysis

Concept:          Find machinery
Implementations:  keyword/document search, natural-language generative search,
                  criteria screeners, saved screen libraries

Concept:          Monitor machinery
Implementations:  email alerts on saved queries, watchlist event feeds,
                  dashboards of information streams, brokerage-connected holdings display

Concept:          Capture / synthesis
Implementations:  saved valuation models, in-platform dashboards,
                  spreadsheet exports, office add-ins, AI-drafted reports and decks
```

A reader who encounters only one implementation (say, an AI-search enterprise platform) should still be able to recognize a data-first prosumer terminal or a consumer research community as the same Type from the Core Model.

## How It Works

### Establish coverage: find candidates

```text
Open the screener (or search)
→ filter the universe by criteria (industry, financials, valuation, estimates)
→ inspect results on their subject pages
→ add interesting subjects to a watchlist
```

Screening is the corpus's front door: it turns the maintained universe into a candidate set the user will track.

### Deep-dive a subject

```text
Open the subject page
→ read financials and estimates (linked to source documents where the product emphasizes auditability)
→ read the latest filings and earnings-call transcripts
→ read analysis (broker research, expert calls, contributor articles — depending on the product)
→ compare against peers
→ record the conclusion: save to the watchlist, build a model, export, or draft a deliverable
```

This is the loop the product exists for: the user's own analysis, produced from the corpus, captured into durable research state.

### Monitor coverage over time

```text
Maintain watchlists and saved searches
→ the platform surfaces new material (filings, transcripts, analysis, events)
→ alerts or feeds bring the new material to the user
→ the user returns to the subject page and updates their work
```

Monitoring is what makes the platform a standing workspace rather than a one-shot lookup: the corpus keeps moving, and the user's coverage moves with it.

### Produce the output

```text
Synthesize findings
→ export data to a spreadsheet, or build the model in-platform
→ generate or assemble the deliverable (report, deck) — enterprise products increasingly draft this with AI, grounded in cited corpus material
→ hand the conclusion to the decision process (which happens outside this platform)
```

### Core vs Common vs Optional

**Defining core** — without these, not an investment research platform:

- identified investable subjects as the anchor
- maintained, accumulating research corpus (documents / structured data / analysis)
- find → monitor → capture/synthesize interrogation loop
- informational-only posture

**Common mature structure** — present in most modern products:

- screener, subject pages, saved searches + alerts, watchlists, comparison views, event machinery, exports, subscription gating, AI assistance

**Variant / optional** — depends on tier, philosophy, and era:

- expert-call networks and their compliance regime
- licensed broker/sell-side research
- internal-content integration (searching the firm's own documents alongside the corpus)
- office add-ins, mobile apps, API/data-feed products
- brokerage-account connections for display
- contributor/community research economies
- corporate/competitive-intelligence extension audiences

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Search surface

The corpus's primary entry point.

- keyword/document search over filings, transcripts, research, and data; increasingly a natural-language question box returning cited answers
- primary actions: run a query, filter by content type or subject, save the query, set an alert

### Screener

The universe-filtering surface.

- filterable table of instruments with financial, valuation, and estimate criteria
- primary actions: build/save a screen, open a subject from results

### Subject page

The per-company (or per-fund) accumulation surface.

- financial statements, estimates, segment/KPI detail, filings, transcripts, analysis, ownership — organized in tabs
- primary actions: read material, add to watchlist, compare with peers, export

### Document / transcript viewer

The reading surface for primary documents and analysis.

- full text with search-within-document and highlighting; source attribution visible
- primary actions: search, highlight, extract, move to the next document

### Watchlist / dashboard

The monitoring surface.

- the user's subjects with new events, filings, transcripts, and news; enterprise products aggregate multiple information streams
- primary actions: review what's new, jump to the subject page, manage the list

### Synthesis surfaces

Where research work becomes output.

- valuation model builders (in-platform or via spreadsheet export/add-ins), notes, AI-drafted summaries and deliverables
- primary actions: build/edit a model, export, generate a deliverable

## Important Rules / Behaviors

### The corpus keeps moving

New issuer material (filings, transcripts, presentations) enters the corpus as it is published, and analysis accumulates continuously. Update speed is a competitive dimension — some products emphasize near-real-time ingestion of new filings — but the structural rule is simpler: the corpus is current, and monitoring exists precisely because it changes.

### Provenance is visible and load-bearing

Research material is either licensed from third-party data providers, aggregated from issuers, or extracted from source documents by the platform. Mature products make provenance a feature: data linked or auditable to source documents, AI answers with citations, licensed content attributed. The user is expected to be able to trace a number or a claim back to its origin.

### Access is gated by entitlement

The corpus and tooling are subscription-gated; different tiers expose different depth (history length, exports, events, seats). Enterprise products add usage metering and organization-level access. What is gated is depth and breadth of the same corpus, not a different product.

### Informational-only by design

The platform takes no orders and holds no custody. Where it connects to brokerage accounts, the connection is for display and monitoring. This is a structural boundary, not a missing feature.

### AI outputs are positioned as grounded

Where AI answers or drafts deliverables, products emphasize grounding in the corpus with citations — because in this domain an untraceable claim is worthless. The AI layer changes the delivery of research, not the ownership of the corpus or the loop.

## Variants

Common realizations of the Type:

- **enterprise market-intelligence platform** — document/search-first corpus (filings, broker research, expert transcripts, the firm's own content), AI research agents, office add-ins, team deployment; also serves corporate strategy and consulting audiences
- **prosumer research terminal** — data/valuation-first: long-history fundamentals, screeners, transcripts, in-platform valuation model builders, investor-tracking content; individual subscription pricing
- **AI-native data infrastructure + terminal** — proprietary extraction pipelines auditable to source, delivered through a web terminal and wholesale data products (APIs, AI-tool connectors) to both investors and other platforms
- **consumer research community platform** — contributor-written analysis and ratings at the center of the corpus, with screeners, portfolios, and earnings transcripts as the tooling layer; freemium monetization
- **institutional research database** — coverage-database realizations serving fund and security research at institutions (adjacent form; not deep-observed in this research pass)

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies — as when execution is added (brokerage) or the live-data workspace becomes the center (terminal).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Financial Market Data Terminal | centers the instrument-centered live-data workspace (quotes/charts/functions over licensed market data); research platform centers the corpus and interrogation loop. Research-flavored terminals straddle; boundary held on center of gravity |
| Financial News & Research Platform | centers a platform-edited, continuously-updated content stream for a broad investor audience; research platform centers the user's own research machinery. Consumer research products straddle the seam |
| Professional Trading Terminal | order construction and routing for the trader's own trading; research platform takes no orders |
| Brokerage Platform / Retail Trading Platform | account relationship, custody, and execution; research there is a feature of the account, not the product's center |
| Portfolio Management System | the institution's book of record for portfolios (positions, intent, checked change loop); research platform holds no portfolio book — watchlists are monitoring conveniences |
| AI Research Assistant | general-purpose assistant over user-supplied or web corpora; research platform's base is a maintained, licensed/extracted, subject-anchored corpus with domain objects |
| Due Diligence Platform / Virtual Data Room | deal-specific confidential document sets for controlled sharing; research platform aggregates public-domain issuer material at continuous scale |
| Market Research Platform / Competitive Intelligence Platform | consumer/commercial markets and brand competition as the object world; investable subjects are a different universe (some enterprise research platforms extend toward competitive intelligence as a variant posture) |
| Financial Modeling Application | standalone modeling tools; modeling embedded in a research platform is a capability, not the center |

## Representative Products

- AlphaSense — enterprise market-intelligence and search platform (with the absorbed Tegus expert-transcript business)
- TIKR — prosumer research terminal with a valuation-workflow center
- Fiscal.ai — AI-native research terminal and financial-data infrastructure
- Seeking Alpha — consumer research platform built on a contributor analysis community with quant ratings and screeners

The Core Model was checked against pre-AI research-platform patterns and terminal-era research delivery to avoid over-fitting to the current AI-era implementation.

## Sources

Research date: **2026-09-07**

- AlphaSense — https://www.alpha-sense.com/ (product and solutions pages)
- AlphaSense Help Center — Getting Started in AlphaSense: https://help.alpha-sense.com/hc/en-us/articles/41098563605395-Getting-Started-in-AlphaSense
- AlphaSense Help Center — When to use Document vs Generative Search: https://help.alpha-sense.com/hc/en-us/articles/41702241422995-When-to-use-Document-vs-Generative-Search
- Tegus (now part of AlphaSense) — https://www.tegus.com/
- TIKR — https://tikr.com/ (root and linked feature pages)
- Fiscal.ai — https://fiscal.ai/ , https://fiscal.ai/products/terminal/ , https://fiscal.ai/help/ (FAQ)
- Seeking Alpha — https://seekingalpha.com/ (root page incl. About section and navigation)

> Sourcing limitation: the institutional research-database pole (Morningstar Direct) could not be fetched (empty responses on two attempts) and is characterized only as an adjacent form; TIKR's help desk was unreachable, so TIKR is asserted at product-page level only; Seeking Alpha is evidenced at product-page level. Precise operational figures (coverage counts, update-speed claims, pricing) observed in vendor materials are recorded in the Research Notes and deliberately not stated as Type facts here.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary discharges against the Financial Market Data Terminal and Financial News & Research Platform passes are recorded in the paired Research Notes.
