# Brokerage Platform

## Overview

A **Brokerage Platform** is the client-facing platform a brokerage firm operates for its customers: through it, a client opens a brokerage account, moves money and securities into and out of that account, places orders to buy and sell financial instruments that the broker executes or routes to markets, and reads the records the broker maintains — holdings, cash balance, transactions, statements, and tax documents.

The defining core is the **brokerage account relationship**. The account is the central record of the system: everything else — trading, funding, income, documents, account features — happens to it. The platform differs from a trading application in that trading is a capability of the account, not the account's reason to exist: the same account can sit unused while its owner collects dividends, or be traded actively through an attached trading surface.

Outside the core sit the market's many extensions: margin and pledging, options and futures permissions, retirement and custodial wrappers, cash-management and banking overlays, managed-investing modes, and separately licensed crypto accounts. These are common and consequential, but a brokerage without any particular one of them is still a brokerage; an investment product without the broker-gated account and its executed, recorded transactions is not a brokerage platform.

## Users & Context

**Primary user: the account owner** — an individual (or, in some products, a family group or an entity) who invests their own money. They open the account, fund it, decide what to buy or sell, and monitor what they own. Their relationship with the platform is long-lived: an account typically persists for years across market conditions and life events.

**Secondary users and roles:**

- **Co-owners and authorized parties** — joint account holders, and in some products limited-access or view-only users.
- **Guardians and custodians** — adults operating custodial or minor accounts on behalf of a child's assets.
- **Managed-investing clients** — owners who delegate decisions to a robo or human advisor service operated by or alongside the broker; the account remains theirs, the decision loop differs.
- **The broker's own service staff** — behind the client platform stands the firm's operations: approving applications, processing transfers, handling support. The client platform surfaces the results (approval states, transfer progress, service channels) but the staff-side systems are a separate world.

**Typical context of use:** onboarding at a kitchen table or on a phone; funding from a bank account; buying a first fund or a first stock; periodic check-ins on holdings and performance; responding to corporate actions and tax season; eventually transferring the account elsewhere or closing it. Sessions are usually short and outcome-driven rather than continuous — with the exception of clients who use the attached trading surfaces, for whom the platform becomes a frequent-use tool.

## Core Model

### The Defining Core

```text
Identified client (person / joint owners / entity)
  → Broker-gated account creation (application → approval)
    → Brokerage account  ← central record
        ├── Cash balance            (funding in / withdrawals out)
        ├── Positions               (securities held, with cost basis)
        ├── Orders & transactions   (placed → executed → confirmed)
        └── Account records         (statements, documents, reports)
```

Four properties. Remove any one and the product stops being a brokerage platform:

- **The account is a broker-held record owned by an identified client.** The broker maintains the authoritative record of what the client owns and what cash sits in the account. If nothing is held or recorded, it is a market-information or portfolio-tracking tool instead.
- **The account is created through a gate the broker controls.** An application is submitted, the owner's identity is verified, and the broker approves the account before it can be used. The verification machinery varies by jurisdiction; the gate does not. If anyone can self-register an account instantly, it is not operating as a brokerage.
- **Value crosses the account boundary by client-initiated movement.** Cash comes in from designated funding sources and goes back out to them; securities can also arrive or leave as in-kind transfers of whole accounts or holdings. If value cannot enter or leave, it is a simulation.
- **Orders lead to real, recorded execution by the broker.** A buy or sell order placed through the platform is executed or routed by the broker to real markets; the resulting fills change the account's positions and cash and become attributable transaction records. Remove this and only an account-document portal remains.

### Standard Capabilities Around the Core

Mature products almost universally add these. They make the account practical without defining what it is:

- **Funding-source management** — the client designates external funding sources (typically bank accounts), which the platform verifies before use; multiple transfer methods may be supported.
- **Order lifecycle visibility** — an order moves through states (placed, working, filled, cancelled, rejected) and each fill yields a confirmation the client can look up later.
- **Holdings and performance views** — positions with cost basis, account value over time, and portfolio-level metrics such as overall return.
- **Income and corporate-action recording** — dividends, interest, and events like splits or redemptions post to the account automatically.
- **Statements and documents** — periodic statements, transaction confirmations, downloadable reports, and tax-relevant documents; in some regimes a monthly consolidated statement is issued by a depository or regulator-mandated party.
- **Capability gating** — advanced capabilities (margin, options, futures, certain market segments) are not on by default; they must be applied for and approved for the account.
- **Market data, watchlists, screeners, research** — the information layer that supports the buy/sell decision; depth varies enormously between a minimal listing and a professional research suite.
- **Alerts and notifications** — price alerts, order and transaction notifications, account-security messages.
- **Profile, security, and estate features** — login security, contact details, and beneficiary/nomination designations.

### One Structure, Many Implementations

The core model is written conceptually. Products realize it differently, and the differences are regional and philosophical rather than structural:

```text
Concept:  Securities custody
          Where the held securities legally live
Examples: street-name custody at the broker or its clearing arm (US pattern)
          securities held in the client's account at a central depository,
          with the broker acting as depository participant (India pattern)

Concept:  Funding source
Examples: linked bank account transfers, wires, checks, instant
          payment systems — rails differ by country

Concept:  Ownership wrapper
Examples: individual, joint (several legal sub-forms), custodial/minor,
          company/trust entities, tax-advantaged retirement wrappers

Concept:  Capability gate
Examples: margin account add-on, options approval, futures enrollment,
          market-segment activation
```

A reader who has only seen one national model should still recognize the others: the account, the gate, the value movement, and the executed order are always there.

## How It Works

### Open an account

```text
Choose ownership type (individual / joint / custodial / entity / retirement wrapper)
→ provide personal, employment, and financial information
→ identity verification
→ select optional account features (e.g., margin, options)
→ broker approves the account
→ choose how to fund it
```

Approval timing varies by product and jurisdiction. Some brokers can approve quickly; the sequence — gated application, verification, approval, then funding — is the pattern. The account exists once approved; a capability added later follows the same gated path.

### Move value in and out

```text
Designate and verify a funding source
→ deposit cash (or transfer securities in kind from another broker)
→ cash balance / positions update on the account
→ later: withdraw cash to a designated source,
   or transfer the whole account (positions as they are) to another broker
```

Two rules recur across products. First, **movements are tied to designated sources**: transfers originating from an unverified external account are typically rejected or refunded rather than credited. Second, **accounts move as records, not as liquidations**: an in-kind transfer carries holdings across brokers without selling them, which is also why such transfers carry no tax event in many regimes.

### Trade

```text
Find an instrument (search / watchlist / research)
→ place an order (buy or sell, quantity, order terms)
→ order works on the market through the broker
→ filled, cancelled, or rejected
→ position and cash update; confirmation recorded
→ income and corporate actions post to the account over time
```

The trading loop can be simple (one-click market order from a phone) or deep (attached professional surfaces with advanced order handling). What stays constant is that the order ends in a real execution recorded on the account.

### Administer the account over time

```text
Read statements and documents
→ track holdings, performance, dividends, corporate actions
→ update profile, beneficiaries, security settings
→ apply for new capabilities (margin, options, segments)
→ eventually: transfer out or close
```

This is the quiet majority of the platform's life. For most account owners, administration and monitoring — not trading — is the dominant interaction, which is why the account, not the order ticket, is the model's center.

### Core vs standard vs variant

- **Defining core** — broker-gated identified-owner account; broker-maintained record of cash and positions; value movement across the account boundary; securities orders with real recorded execution.
- **Standard capabilities** — funding-source management, order lifecycle and confirmations, holdings/performance views, statements and documents, income and corporate-action recording, capability gating, market data and research, alerts, profile and beneficiary management.
- **Common variants** — see Variants below.

## Interfaces

Most products present some combination of these surfaces. Some brokers split them into separate products (a trading app beside an account backoffice); others merge everything into one app. The split-vs-merged choice is philosophy, not structure.

### Account dashboard / portfolio

The account's home.

- total account value, cash balance, holdings with current values and cost basis, performance over time
- primary actions: review holdings, drill into a position, view recent activity, move money, go trade

### Order ticket / trading surface

Where orders are placed.

- instrument, quote, quantity, order terms; sometimes charts, watchlists, screeners, research
- primary actions: preview and submit an order, manage working orders, view recent fills

### Money movement / transfers

- funding sources on file, deposit and withdrawal forms, transfer status, account-transfer (in-kind) initiation
- primary actions: add or verify a funding source, deposit, withdraw, track a pending transfer

### Documents and statements

- statements, trade confirmations, tax documents, reports, regulatory relationship disclosures
- primary actions: view, download, search by period

### Account settings and capabilities

- profile and contact details, login security, beneficiaries/nomination, account features and their approval states, linked services (banking overlay, managed investing)
- primary actions: update information, apply for a capability, configure alerts

### Mobile app

For most modern products the mobile app is the primary client surface, covering dashboard, funding, trading, and documents; web portals tend to carry the deeper administrative and research tools, and some brokers add desktop-class trading applications on top.

## Important Rules / Behaviors

### The gate comes before everything

An account cannot trade before it is approved, and most products also require it to be funded. Capabilities are gated separately: margin, options, futures, and certain market segments each require their own approval, and some carry eligibility conditions on the owner.

### Cash accounts and margin accounts behave differently

In a cash account, the client invests only their own funds, and unsettled proceeds typically cannot be reused immediately. In a margin account, the client can borrow against holdings — which introduces broker rights that are unusual among consumer applications: margin terms typically include the broker's right to sell securities in the account without prior contact with the client in order to meet a margin call, and to raise maintenance requirements without notice. Margin terms are regulatory and contractual; details vary by product and jurisdiction and are disclosed by each broker.

### Funding is anchored to designated sources

Money moves between the account and funding sources the client has designated and the platform has verified. Transfers from unverified sources are typically rejected or refunded to the source rather than credited. Withdrawals flow back to designated sources for the same reason — this is simultaneously an operational rule and a fraud-control surface.

### The broker keeps the record

Statements, confirmations, and transaction history are the broker's records of what happened. Many regimes require periodic account statements, and some go further, with exchange-level confirmations sent to the client directly. Discrepancies are corrected through explicit repair paths (for example, holdings acquired outside the platform may need to be reconciled manually), reflecting that the record is authoritative, not cosmetic.

### Ownership structure determines rights

Joint ownership has legal sub-forms with different survivorship outcomes; custodial accounts legally belong to the minor; retirement wrappers carry contribution and withdrawal restrictions enforced by the platform. The account type chosen at opening is not a label — it changes what the platform permits.

### Protections attach to the custody regime

Client-asset protections differ by jurisdiction and by entity: investor protection schemes for broker-dealer custody in some markets, central-depository registration in others, and distinct (usually weaker) protection for non-securities assets such as crypto held through sister entities. The platform's disclosures are part of the product: which entity holds which asset under which regime is materially important and is surfaced in account documents.

## Variants

- **Ownership and wrapper variants** — individual, joint (multiple legal sub-forms), custodial/minor, entity accounts (companies, trusts, family-vehicle entities), and tax-advantaged retirement or education wrappers; the wrapper changes rules and tax treatment, not the core.
- **Custody-regime variants** — broker-side street-name custody versus central-depository (demat) custody with the broker as participant; contract-note and exchange-confirmation cultures differ accordingly.
- **Self-directed vs managed modes** — the same account family may host pure self-directed investing, a robo-advised mode, or human advisory services, often run by a separate registered-adviser entity; some brokers are deliberately self-directed only.
- **Margin and borrowing variants** — margin accounts with broker liquidation rights, pledge-based collateral (securities pledged through a depository to unlock trading margin), and loans against securities.
- **Cash-management overlay** — linked checking accounts, debit cards, check writing, and spending accounts with deposit insurance; the brokerage account becomes partially bank-like while securities custody remains a separate regulated relationship.
- **Asset-class expansion** — options, futures, fixed income, foreign exchange, and crypto; crypto in particular is often operated by a separately licensed entity with separate protection terms, even inside a single app.
- **Advanced trading surfaces** — professional-grade platforms attached to the account for active traders; the point where this Type blends into the trading-application Types.
- **Delivery-shape variants** — merged single app versus split products (trading app + account backoffice); app-first versus web-first; subscription tiers layered over the free account.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Retail Trading Platform | the consumer **trading experience** is the product's center (order entry, charting, watchlists); it presupposes a brokerage account but does not administer one. Most brokers ship both as one family; the center-of-gravity test separates them |
| Professional Trading Terminal | the professional trader's live market workspace; routes orders and displays real-time state but does not open, fund, or record the account |
| Algorithmic Trading Platform | trading decisions made by encoded strategies; broker-embedded algo tools are modules over the account, not the account platform |
| Robo-advisor | a managed-portfolio service (algorithm decides and rebalances, typically no self-directed order entry); appears inside brokerage platforms as a mode over the same account |
| Digital Banking Application | deposit/payment relationships and FDIC-framed balances; no securities positions or executed trades; cash-management overlays are the overlap zone |
| Cryptocurrency Exchange | trades crypto assets under exchange custody and wallet mechanics; brokerages add crypto via separately licensed entities with separate protections |
| Portfolio Management System | institutional portfolio records and attribution for portfolio managers; different user and time horizon from the client account |
| Wealth Management / Financial Advisor Platform | the advisor's book of business; the advisor-side system that may act *on* brokerage accounts, not the client-side account platform |
| Investment Research Platform | research content and market data without account custody or execution |
| Insurance Broker Management Platform / Freight Brokerage Platform | shares only the word "broker" — insurance intermediary book-of-business and logistics load brokerage respectively; unrelated models |

The most important seam is the first one. Brokerage Platform and Retail Trading Platform are two Types that the market constantly packages together: the account platform without a trading surface is a statement portal, and the trading surface without an account relationship settles nothing. The structural test is the center of gravity — account administration versus trading experience — and it should be expected that single products will often span both.

## Representative Products

- **Zerodha** — India's largest discount brokerage; explicitly splits its trading surface (Kite) from its account backoffice (Console); operates under the Indian depository-participant regime.
- **Charles Schwab** — US bank-plus-brokerage combination; one account family hosting self-directed, robo, and advisory modes, with advanced trading platforms attached.
- **Robinhood** — US mobile-first consumer brokerage; one app over a constellation of separately licensed entities (broker-dealer, clearing, advisory, futures, crypto, money transmitter).

The model was checked against the regional custody regime (India), the bank-brokerage combination (US), and the app-first entrant, and against the historical full-service brokerage relationship (phone orders, paper statements) to avoid defining the Type by any single era, market, or interface.

## Sources

Research date: **2026-09-06**

- Zerodha — Support Portal (Account Opening, Your Account, Funds, Console: Portfolio/Corporate actions/Statements) — https://support.zerodha.com/
- Charles Schwab — Brokerage account product page and "What is a brokerage account" explainer (including FAQ and disclosures) — https://www.schwab.com/brokerage , https://www.schwab.com/brokerage/what-is-a-brokerage-account
- Robinhood — Support home, site navigation, and legal/entity disclosures — https://robinhood.com/us/en/support/

> Sourcing limitation: Interactive Brokers documentation and Fidelity customer-service pages could not be retrieved from the research environment (repeated timeouts and access denial); Robinhood's help-center articles did not render. Statements about those products are limited to what their reachable pages show, and no precise operational details (fee schedules, transfer timelines, limits, approval criteria) are asserted for any product beyond what its own fetched pages state. Cross-product rules in this document are stated at the level the evidence supports; regime- and product-specific specifics are left to the vendors' disclosures.
