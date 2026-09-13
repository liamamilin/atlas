# Private Market Investment Platform

## Overview

A **Private Market Investment Platform** is an investor-facing platform for investing in private-market assets — private company shares, private fund interests, and similar non-publicly-traded investments. It lists investable private-market opportunities, determines which investors are eligible to invest, takes investors through a commitment and funding process, and maintains a lasting record of each investor's positions.

The defining core is small:

```text
Listed private-market investment opportunities
+ Investor eligibility gate
+ Commitment-to-execution flow
+ Persistent investor-side investment record
```

Everything else commonly associated with the category — pooling vehicles, capital calls, secondary markets, relationship managers, tax-document delivery — is a standard capability of mature products or a variant of a particular market segment, not part of what makes the platform this Type.

The platform serves the **investor side** of the private markets. The manager side — running the fund's books, distributing reports to a fund's own investors, tracking a deal pipeline, keeping a company's equity records — belongs to neighboring Application Types (Fund Administration, Investor Portal, Deal Management for PE/VC, Cap Table Management).

## Users & Context

**Primary user: the individual investor** — an accredited, high-net-worth, professional, or (on some platforms) ordinary retail investor who wants exposure to private-market assets. Typical reasons to open the platform:

- browse what private-market investments are currently open
- check whether they qualify and what their investment limits are
- commit capital to an offering and complete the paperwork
- track the value, documents, and cash events of positions they already hold

**Secondary users:**

- **wealth advisors / relationship managers** — on some platforms, intermediaries who bring clients to private-market offerings and manage the relationship on the client's behalf
- **fund managers / issuers** — the sell side: they supply the underlying investment (a fund raising capital, a company whose shares are being sold) and may interact with the platform for listing, share sourcing, or closing
- **platform operations staff** — run eligibility review, share sourcing, transaction closing, and investor servicing

The work context is episodic and long-horizon: an investor may act a few times a year (committing to an offering, reviewing a statement, responding to a notice) rather than trading daily. Positions are typically held for years.

## Core Model

### The Defining Core

```text
Investment Opportunity (offering)
  └── listed with terms, documents, availability state
Investor (qualified identity)
  └── eligibility determined by the platform
Commitment → executed Investment
  └── funded through a pooling vehicle or direct acquisition
Portfolio (persistent investor-side record)
  └── holdings, value, documents, cash events
```

Four properties. If any one is removed, the product is no longer recognizable as a private market investment platform:

- **Listed private-market investment opportunities** — the platform maintains a catalog of investable offerings. Each offering names the underlying asset (a specific private company, a fund, a portfolio of companies), its commercial terms, its legal documents, and its availability state (open, upcoming, waitlisted, closed). Without the catalog, the product is a portfolio tracker or a document portal, not an investment platform.
- **Investor eligibility gate** — private-market investing is legally restricted, and the platform itself determines who may invest in what: identity verification, financial criteria (income, net worth, portfolio size), regulatory investor categories, jurisdiction rules, and per-investor limits. The strictness of the gate varies enormously between platforms; its existence does not. Without a gate, the product is a public brokerage.
- **Commitment-to-execution flow** — an investor's interest becomes a binding commitment, is funded, and is executed into an actual investment: a vehicle acquires the asset, or shares are transferred, and the subscription is finalized. Without this flow, the product is a listings or research site.
- **Persistent investor-side investment record** — every commitment and holding lives in the investor's portfolio with its state, its value, and its documents, and survives across sessions and years. Without this, the product is one-shot deal matching with no investment relationship.

### Standard Capabilities of Mature Products

These are widespread across the category but do not define it:

- **Pooling investment vehicles** — the most common execution structure. Instead of each investor holding shares directly, investors become parties in a vehicle (a feeder fund, a special-purpose vehicle, a multi-company fund) that holds the underlying asset. This lets many investors act as one holder toward the company or fund, and lets the platform administer economics and reporting in one place. Direct share acquisition exists as an alternative on some platforms, usually with higher minimums and more investor responsibility.
- **Identity verification and onboarding** — blocking prerequisites (identity documents, tax identification, financial disclosures) that must be completed before an investment can proceed.
- **Eligibility tiers and limits** — accreditation status, income/net-worth-based limits, jurisdiction-based investor categories; some offerings are restricted to a higher tier.
- **Portfolio value tracking** — positions carry a value that is *not* a live market quote: a net asset value reported by a fund manager, or a platform estimate updated on events. Updates are periodic or event-driven.
- **Document library** — offering documents, subscription agreements, statements, and tax documents, delivered and retained per investor.
- **Fee machinery** — platform or transaction fees, sometimes management fees or carried interest, disclosed per offering.
- **Investor communications** — updates, closing notices, capital-call notices, distribution notices.
- **Liquidity machinery** (in a subset of products) — secondary-sale matching, periodic auctions, or semi-liquid fund structures that offer exit routes before the underlying asset resolves.
- **Human intermediary layer** (in a subset) — relationship managers or specialists who guide investors or source supply.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:  Investment Opportunity
Realized as:  a feeder fund allocation, a single-company vehicle,
              a multi-company fund, a direct share purchase,
              a startup round (equity, SAFE, note, revenue share)

Concept:  Eligibility gate
Realized as:  accredited-investor verification, professional/HNW investor
              categories, income/net-worth limits, jurisdiction rules

Concept:  Execution
Realized as:  feeder vehicle, SPV, custodian arrangement, direct shares

Concept:  Value
Realized as:  manager-reported NAV, platform estimate, deal-based marks
```

A reader who has only seen one implementation — say, a pre-IPO share marketplace — should still be able to recognize a feeder-fund platform or a retail startup-investing platform from the core model.

## How It Works

### Qualify

```text
Register
→ verify identity (documents, tax ID)
→ disclose financial situation (income / net worth / portfolio)
→ platform determines eligibility category and limits
```

Qualification is a prerequisite, not a per-offering formality: it gates the whole platform, and some offerings apply additional restrictions on top.

### Discover and indicate interest

```text
Browse the offering catalog
→ open an offering (asset, terms, fees, documents, availability)
→ indicate interest / reserve an allocation
```

Offerings are discrete and capacity-bound. Unlike a stock market, supply is not continuous: shares or fund allocations must be sourced, demand may be aggregated before an offering goes live, and offerings close when complete. Platforms commonly surface availability states (open / upcoming / waitlist) and let investors register interest that is honored when supply appears.

### Commit and fund

```text
Commit to the offering
→ complete subscription documents (electronically, in the platform)
→ fund the commitment (payment or first capital call)
→ platform executes: vehicle acquires the asset / shares transfer
→ investment finalizes; position appears in the portfolio
```

The commitment is the pivot of the whole model: before it, the investor is browsing; after it, the investor is bound. Funding timing varies by structure — one-shot payment at commitment for direct and SPV-style deals, staged capital calls over an investment period for closed-end fund structures. Between commitment and finalization there is often a legal closing phase (documents executed, counterparty or company processes exercised) that can take weeks.

### Hold and service

```text
Position sits in the portfolio
→ value updated (NAV or estimate, periodically or on events)
→ documents accumulate (statements, tax documents, notices)
→ cash events occur (capital calls draw the commitment;
   distributions return proceeds)
```

This is the long middle of the investment: years, not days. The platform is the investor's system of record for what they hold, what it is worth, what it has paid them, and what they still owe.

### Exit

```text
Underlying asset resolves (company exit, fund wind-down)
→ distributions paid through the platform
```

or, where the platform offers liquidity machinery:

```text
Investor offers the position for sale
→ platform matches buyers (auction, matching, resale)
→ transfer executes; buyer assumes the position
```

Liquidity is the exception, not the rule. Where it exists, it runs through defined processes and windows, not a continuous market.

### Capability tiers

**Defining core** — without these, not this Type:

- listed private-market investment opportunities
- investor eligibility gate
- commitment-to-execution flow
- persistent investor-side investment record

**Standard capabilities** — present in most modern products:

- pooling vehicles
- identity verification / onboarding
- eligibility tiers and limits
- portfolio value tracking
- document library
- fees
- investor communications

**Variant / optional** — depends on segment and product:

- capital calls (closed-end fund structures)
- secondary liquidity (auctions, resale matching)
- relationship managers / advisor channel
- issuer-side participation (shareholder sell-side intake, issuer listing)
- multi-jurisdiction eligibility matrices
- tax-document machinery per jurisdiction

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Offering catalog / explore

The primary entry surface for discovery.

- lists currently investable offerings with availability state
- typical information: company or fund identity, sector or asset class, stage, headline terms
- primary actions: browse, filter, open an offering, register interest

### Offering detail

The decision surface for one opportunity.

- typical information: underlying asset description, terms (minimum, fees, structure), risk disclosures, legal documents, availability and timeline
- primary actions: indicate interest, reserve, commit, download documents

### Investor onboarding / eligibility

The qualification surface.

- typical information: outstanding prerequisites (identity, tax ID, financial disclosures), current eligibility status, investment limits
- primary actions: complete verification steps, update financial information

### Portfolio

The investor's home surface after investing.

- typical information: positions with state (in progress / held), value estimates, unfunded commitments, recent activity
- primary actions: open a position, review value history, track pending investments, act on blocking tasks

### Transaction / subscription workspace

The execution surface for one commitment.

- typical information: document status, required signatures, payment status, timeline
- primary actions: fill and sign subscription documents, fund, track to finalization

### Documents

The record surface.

- typical information: offering documents, executed agreements, statements, tax documents
- primary actions: view, download

### Secondary market surface (where offered)

The liquidity surface.

- typical information: positions eligible for sale, auction or matching status, pricing references
- primary actions: offer to sell, bid, track a transaction to transfer

## Important Rules / Behaviors

### Access is gated, per offering and per jurisdiction

Eligibility is enforced by the platform before money moves. The same investor may be eligible for one offering and not another; rules differ by the investor's jurisdiction. This is the structural difference from public-market brokerage, where anyone with an account can buy anything listed.

### Offerings are discrete and capacity-bound

An offering opens, collects commitments, and closes. Supply is sourced, not continuous. Waitlists, interest registration, and demand aggregation exist precisely because supply cannot be taken for granted.

### Commitments become binding

Once the commitment and documents are executed, the investor is bound: cancellation windows are narrow and defined, and failing to complete paperwork after reserving can forfeit the allocation. Before disbursement, cancellation and refunds are typically possible; after finalization, the position is illiquid except through defined liquidity processes.

### Value is not market-quoted

Positions are valued by NAV or estimate, updated periodically or on events — never as a live market price. Investors see estimates with explicit uncertainty, not quotes.

### Liquidity is constrained by design

Positions are long-dated. Where exit routes exist (auctions, resale matching, semi-liquid structures), they run on the platform's process and schedule, often with eligibility conditions and fees, and a buyer may assume not just the position but its remaining obligations (such as unfunded commitments).

### No investment advice

Platforms commonly state that they do not provide investment advice; the investor (or their advisor) makes the decision. Curation depth varies — some platforms diligence offerings heavily, others explicitly do not curate — but the decision responsibility stays with the investor.

### Fees are disclosed per offering

Platform fees, and where applicable management fees or carried interest, are attached to the offering and its documents rather than to a general account. Structures differ widely between platforms and offerings.

## Variants

Common forms of the Type:

- **Retail startup-investing platform** — open eligibility with regulatory limits, small minimums, direct or SPV execution into early-stage companies; offerings may be uncurated beyond fraud screening
- **Accredited pre-IPO marketplace** — accredited investors only; the platform sources shares of late-stage private companies (or interests in them) and matches demand from buyers with supply from existing holders
- **Professional / HNW fund-access platform** — jurisdiction-gated professional or high-net-worth investors; curated top-tier private funds accessed through feeder vehicles; capital-call economics; sometimes a periodic secondary auction
- **Wealth-channel distribution platform** — offerings distributed through banks, private banks, and advisory firms; the advisor, not the end investor, is often the operating user
- **Asset-class specialists** — the same core model applied to one asset class (real estate, credit, art, collectibles)
- **Tokenized private markets** — the same core model with blockchain-based registration and transfer of the positions (observed in the market; not directly researched here)

A variant remains a variant while the core model holds. If a product drops the offering catalog and only services existing positions, it has become an Investor Portal; if it drops the eligibility gate, it has become a public brokerage.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Fund Administration Platform | adjacent (manager side) | GP-side back office: fund accounting, NAV computation, capital-call and distribution processing, report production; this platform may consume fund administration as a service |
| Investor Portal | adjacent (capability slice) | LP-facing documents/statements for a fund the investor already holds, operated by the manager; no discovery, no eligibility gate, no subscription execution |
| Deal Management for Private Equity / VC | adjacent (manager side) | GP-side deal pipeline and LP relationship management; opposite side of the same market |
| Cap Table Management | adjacent (company side) | company-side equity records; platform vehicles appear on cap tables as single aggregated holders — complementary, not overlapping |
| Retail Trading Platform / Brokerage Platform | adjacent (public markets) | continuous markets, no eligibility gate, market-quoted prices, instant settlement; this Type has gated access, discrete offerings, estimated values, long-dated positions |
| Wealth Management Platform | adjacent | advisory-relationship-centric across asset classes; may distribute this Type's offerings; object model centers on the client relationship, not the offering |
| Portfolio Management System | adjacent (institutional) | book of record + forward management loop for portfolios; the LP-side institutional reading of "private market investment" belongs there, not here |
| Virtual Data Room | adjacent (manager side) | fundraising document sharing during a raise; one input surface to this Type's offering documents |
| Investment Research Platform | adjacent | research and data about private companies/funds without an execution or holding layer |

The most important boundary is the **side of the market**: this Type's primary user is the investor committing capital; the sibling Types' primary users are the manager, the company, or the advisor.

## Representative Products

- **Moonfare** — professional/HNW fund-access platform; feeder vehicles into top-tier private equity funds; secondary auction
- **EquityZen** — accredited-investor pre-IPO marketplace; single- and multi-company vehicles, direct share acquisitions; broker-dealer operated
- **Wefunder** — retail startup-investing platform; open eligibility with limits; SPV/custodian/direct execution

Other products commonly cited in this category (iCapital, Yieldstreet, Forge Global, Republic, Securitize) could not be directly researched for this document; see Sources.

## Sources

Research date: **2026-09-06**

- Moonfare — FAQ — https://www.moonfare.com/faq
- EquityZen — Help Center (types of deals; how to invest; how to sell) — https://help.equityzen.com/
- Wefunder — Help Center (who can invest; investment timeline; portfolio) — https://help.wefunder.com/
- Carta — Support Center (category taxonomy, used for boundary analysis) — https://support.carta.com/
- AngelList — Investor Management Help Center (product structure, used for boundary analysis) — https://support.angellist.com/

> Sourcing limitation: several prominent category products (iCapital, Yieldstreet, Forge Global, Republic, Securitize, CAIS, Fundrise) were not reachable from the research environment on 2026-09-06 (access blocked or transport errors). No operational claims about those products are made in this document. Cross-product findings rest on the three researched products; the wealth-channel distribution variant is described structurally only. Precise figures (minimums, fee percentages, timelines, cadences) observed in individual products are recorded in the paired Research Notes and are deliberately not stated here.
