# Card Processing Platform

## Overview

A **Card Processing Platform** is the **issuer-side transaction-rail infrastructure of card payments**. It is operated for card issuers — banks, fintech issuers, and BIN-sponsored card programmes — and runs the issuer's side of every card transaction: it connects directly to the card networks, receives the transaction stream those networks route to the issuer, takes part in the real-time approve/decline decision for every attempted purchase, posts the transaction against a cardholder account, and carries it through the full financial lifecycle of clearing, settlement, fees, reversals, and disputes.

The defining core is small:

```text
Issuer-side scheme connectivity
└── Real-time authorization processing
    └── Cardholder account / balance record
        └── Transaction lifecycle through clearing and settlement
```

Everything else commonly associated with the category — stand-in processing, rules engines, fraud screening, chargeback handling, card management, tokenization, portals, reporting — is standard mature structure layered on that spine, not what makes the product a card processing platform.

The Type sits on the **issuing side** of the card rails. It is the mirror image of merchant-side payment processing: an acquiring-side processor helps businesses *accept* payments; a card processing platform helps issuers make their cards *work* on the networks. In the current market many products combine this rail with card-program governance (issuing), so the boundary with issuing platforms is one of emphasis rather than of separate products — see Related Application Types.

## Users & Context

The platform is B2B infrastructure: cardholders never see it directly.

**Primary users:**

- **Issuer payments/card teams** — bank or fintech staff responsible for keeping the card programme running: monitoring authorizations and declines, managing card statuses and limits, resolving clearing mismatches, reconciling settlement.
- **Programme managers at fintechs and embedded-finance platforms** — operate card programmes (often under a BIN sponsor's licence) through the platform's APIs and portal; configure transaction rules, launch card products, watch real-time activity.
- **Integration/engineering teams** — build and maintain the real-time interface between the platform and the issuer's own systems (core banking, ledgers, decisioning services).

**Secondary users:**

- **Finance/reconciliation teams** — work with settlement advisories, interchange and scheme-fee reports, and reconciliation data.
- **Risk and dispute teams** — manage fraud rules, 3-D Secure, and chargeback handling.
- **The platform vendor's own operations staff** — scheme connectivity, programme implementation, and back-office processing sit behind the product.

The working context is the four-party card scheme (cardholder, merchant, acquirer, issuer, with the network in the middle): the platform occupies the issuer's corner of that model, opposite the acquirer's processing stack.

## Core Model

### The Defining Core

Four properties. Remove any one and the product stops being a card processing platform:

- **Issuer-side scheme connectivity.** The platform is directly connected to card networks and is the issuer's processing point on the rails: authorization requests, presentments, fee collections, and chargeback messages for its clients' cards arrive at the platform, in scheme message formats. Without this, the product is card record administration, not processing.
- **Real-time authorization processing.** For every attempted transaction the platform takes part in the approve/decline decision within the network's real-time window: it performs card-data checks (card validity, expiry, CVV, PIN, token data) and rule checks, and either decides directly — against balances and rules it holds — or relays the request in real time to the issuer's own system and returns that system's response to the network. Without this, the product is not on the transaction rail.
- **Cardholder account/balance record.** Transactions post against cardholder accounts that carry balances. The platform either holds that ledger itself or works in real time against a ledger the issuer holds; the record itself is part of the defining core, while who holds it is a deployment choice (see the division-of-labor dial below).
- **Transaction lifecycle through clearing and settlement.** The platform processes the scheme's clearing files — presentments matched back to their authorizations, plus fees and interchange — supports the settlement cycle with advisories and reconciliation data, and records the resulting account movements: authorization hold → cleared → settled, with reversals, refunds, and chargebacks along the way. Without this, the product is an authorization-only gateway, not a processing platform.

### The Division-of-Labor Dial

The most distinctive structural feature of this Type is that the *same* platform can be operated at different depths of responsibility. Two independently developed products expose this as an explicit, named configuration:

```text
Concept:            who holds the balance and who decides
One end:            issuer holds balances, issuer decides
                    (platform = connectivity + checks + message relay)
Middle:             balances managed jointly, decision shared
                    (platform decides, issuer can override)
Other end:          platform holds the ledger and decides
                    (issuer consumes data and configures rules)
```

Common implementations:

- Named processing modes: gateway / cooperative / full-service (with a gateway-plus-stand-in variant)
- Named authorization types: external / internal / passive, tied to "remote" vs "local" store of value

The dial is a configuration of one product family, not a choice between different Types: every position on it still satisfies the defining core. What varies is operational responsibility, not the structure of the rail.

### Standard Capabilities

Mature products commonly add the following around the core. They make the platform practical; they do not define the Type.

- **Stand-in processing (STIP)** — when the issuer's decisioning system is unreachable, the platform (or the scheme) answers the network on the issuer's behalf: basic stand-in declines on timeout; enhanced stand-in can approve transactions meeting issuer-defined criteria (spend limits, risk thresholds), optionally using balance data supplied by the issuer; advice messages record what was decided and are delivered to the issuer's system when it recovers.
- **Transaction rules engine** — spending limits, merchant-category restrictions, and authorization rules configured at programme, product, account, or cardholder level, evaluated in real time during authorization.
- **Fraud screening and 3-D Secure** — risk checks inside the authorization flow, fraud monitoring services, and authentication for card-not-present transactions.
- **Dispute/chargeback machinery** — the issuer-side dispute lifecycle: chargeback receipt and creation, funds processing, evidence exchange, API or manual handling.
- **Fees machinery** — configuration of programme fees charged to cardholders or the programme, plus processing of interchange amounts and network/scheme fees arriving in scheme files, with reporting that supports reconciliation.
- **Card management toolset** — card status lifecycle (active, blocked, temporary blocks), PIN management, physical and virtual card configuration.
- **Tokenization and digital wallets** — token lifecycle management and push provisioning so issued cards work in mobile wallets.
- **Operator portal** — view and manage cards, transactions, limits, and disputes; configure rules without reissuing cards.
- **Automated back office** — transaction reconciliation, scheme reporting, and network fee management as processed outputs rather than manual work.
- **Reporting and data exchanges** — transaction and balance reports, daily presentment/interchange/fee reports, raw scheme settlement reports for reconciliation.
- **APIs, webhooks, and test tooling** — programmatic integration for card and account management, real-time event delivery, and sandbox/test-transaction simulators.
- **Multi-currency and account structures** — balances and processing in multiple currencies; account structures that support aggregator, BIN-sponsor, and multi-programme operation (depth varies by product).

## How It Works

### Authorization (the real-time loop)

```text
Cardholder pays a merchant
→ merchant's acquirer sends an authorization request into the network
→ network routes the request to the issuer's processing platform
→ platform performs initial checks (card data, expiry, CVV, PIN, token)
→ platform applies rules-engine analytics (limits, restrictions, fraud, fees)
→ decision:
     · platform-held balance → platform decides and responds
     · issuer-held balance   → platform relays the request to the issuer's
                               system in real time and returns its response
→ platform returns the final response to the network
→ approved: an authorization hold is recorded against the cardholder account
→ both sides keep a record: the platform stores the financial decision and
  streams the transaction data to the issuer in real time
```

The response carries standardized result codes; authorization codes are generated for approvals and, in some products, for declines as well, so every attempt is traceable. Partial approvals, incremental authorizations (e.g., fuel pumps, hotel stays), and authorization reversals are handled as first-class variants of the loop.

### Clearing and settlement (the financial completion)

```text
Merchant's acquirer batches completed transactions
→ scheme assembles clearing files (presentments, fees, interchange)
→ platform receives the clearing files from the scheme
→ platform matches each presentment back to its original authorization
  (authorization code, card number, merchant, amount)
→ platform posts the cleared amount to the cardholder account,
  replacing the authorization hold
→ scheme computes net positions and runs settlement:
  advisories are delivered; funds move between issuer and acquirer
  through the scheme's settlement process
→ platform delivers settlement data and raw scheme reports
  to the issuer for reconciliation
```

Two structural rules govern this flow: clearing messages carry data but do not move funds — settlement does; and settlement happens only after clearing. Matching is the load-bearing step: schemes do not provide a single field linking a presentment to its authorization, so the platform reconstructs the link from several fields; a small residue of forced or manually keyed presentments can never be matched and surfaces as reconciliation exceptions.

### Stand-in processing (keeping the rail alive)

```text
Issuer's decisioning system unreachable (maintenance, outage)
→ platform (or scheme) answers the network on the issuer's behalf
→ basic stand-in: decline after the response window expires
→ enhanced stand-in: approve transactions meeting the issuer's
  pre-set criteria (limits, risk thresholds, optionally balances)
→ every stand-in decision is stored as an advice message
→ advices are queued and delivered to the issuer's system
  automatically once it is back online
```

### Disputes and exceptions

The platform runs the issuer side of the dispute lifecycle: chargebacks arrive as scheme messages, are matched to original transactions, and move through creation, representment, and funds processing — via API or manual handling. Refunds and financial reversals post against the account like any other lifecycle event. Card-status controls (temporary blocks, fraud-triggered holds) and account-status inquiries operate through the same message machinery.

### Programme onboarding

Bringing a card programme onto the platform is a structured project: programme and product configuration (BIN, card products, fees, limits, rules), the choice of processing mode (who holds balances, who decides), integration of the real-time interface and APIs, card art and physical/virtual configuration, scheme certification testing, and launch. The processing-mode choice is the pivotal decision, because it determines how much of the issuer's own stack (core ledger, decisioning) participates in the real-time loop.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Operator portal

The issuer/programme team's primary working surface.

- real-time views of cards, accounts, transactions, and authorizations
- card management (status changes, blocks, PIN), limit and rule configuration
- dispute/chargeback queues and case handling
- primary actions: search and inspect transactions, manage cards, adjust rules, work disputes

### Real-time authorization interface

The machine-to-machine surface between the platform and the issuer's own systems — the defining integration of the Type.

- the platform delivers each incoming authorization (and financial advice) to the issuer's system and expects a decision response within a strict time window
- message formats follow scheme message structures with product-specific extensions; XML and JSON variants are common
- configuration options cover endpoints, timeouts, and which checks the platform performs before relaying

### APIs and webhooks

Programmatic surfaces for everything around the rail.

- card and account management (create, status, limits, tokens)
- real-time event subscriptions (transactions, authorizations, stand-in advices)
- balance updates and account queries where the platform holds the ledger

### Reporting and data exchanges

The financial-control surface.

- transaction and balance reports (real-time and scheduled)
- daily presentment, interchange, and fee reports
- raw scheme settlement and reconciliation reports forwarded for the issuer's finance team
- delivery via secure file transfer, portals, or webhooks

### Test tooling

- sandbox environments and test-transaction simulators that emulate scheme messages (point-of-sale, e-commerce, ATM, fuel-pump scenarios) so integrations can be certified before going live

### Cardholder self-service channels (optional)

Some products extend the rail to cardholder-facing automation — interactive voice response and SMS services for card activation, status, and PIN actions — operated on the platform's card data.

## Important Rules / Behaviors

- **The processing mode determines who decides.** In gateway/external modes the issuer's system holds the balance and makes the authorization decision; the platform performs checks and relays. In full-service/internal modes the platform holds the ledger and decides. Cooperative modes share the decision — for example, letting the issuer replace a platform decline with a more specific decline reason. The same platform can serve different clients at different positions on this dial.
- **Real-time windows are hard constraints.** Authorization responses must return within the scheme's time window; this is why stand-in processing exists and why the platform's checks are engineered to complete before the relay deadline.
- **Clearing precedes settlement; both follow authorization.** A transaction's money movement happens in stages: authorization creates a hold, clearing confirms the final amount (which may differ from the authorized amount), settlement moves the funds. The account balance reflects each stage — holds reduce available balance, clearing and settlement finalize it.
- **Presentment matching is reconstructed, not given.** Schemes do not supply a universal link between a presentment and its authorization; the platform derives it from authorization code, card number, merchant identity, and amount. Unmatchable presentments (forced transactions, manual key-ins, altered amounts) are a normal exception class that surfaces for review.
- **Every decision is recorded and advised.** Approvals, declines, stand-in decisions, and financial notifications generate records and advice messages; issuers depend on this stream for their own ledgers, and in some products certain advices require explicit acknowledgement.
- **Card status is a live control surface.** Status changes (blocks, temporary fraud holds, PIN changes) take effect in the authorization path immediately, without reissuing the card.
- **Scheme rules permeate the product.** Message formats, response codes, clearing cycles, dispute windows, and reporting obligations are dictated by the card networks; the platform's job is to keep the issuer compliant with them as they change.

## Variants

Common shapes of the same Type:

- **By division of labor** — gateway (issuer-run), cooperative (shared), full-service (platform-run); the same product family typically offers all of them.
- **By product scope** — debit and prepaid programmes vs credit programmes; credit adds origination and servicing depth, which some platforms deliver through partners.
- **By client base** — banks (classic outsourcing of card processing) vs fintechs/embedded finance (API-first programme operation) vs aggregators and BIN sponsors running many sub-programmes on one platform.
- **By scheme coverage** — the international schemes as baseline, with regional schemes added per market.
- **By delivery posture** — cloud-native, API-first platforms vs bank-heritage processing suites; the classic pole bundles the same rail with cardholder digital experiences, portfolio analytics, and consulting services.
- **By programme sourcing** — platforms that also arrange BIN sponsorship connect issuers-of-record with programme owners; a service variant around the same rail.
- **Emerging** — stablecoin-backed settlement and agentic-commerce readiness are appearing as platform capabilities without changing the core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Card Issuing Platform | closest sibling; same products, different emphasis | issuing centers the programme side (create/govern cards, cardholders, funding, spend controls); processing centers the rail (scheme connectivity, authorization switching, ledger, clearing/settlement). Modern products fuse both; the leaves differ in emphasis, not in product families |
| Card Management System | adjacent; the record-administration residue | card record administration (statuses, limits, plastic, PIN) without rail participation is card management; add scheme connectivity and authorization and it becomes processing. Classic processors include card management as a component |
| Payment Processing Platform | opposite side of the network | merchant-side acquiring: underwrites sellers, administers processing accounts, routes payments inward, settles/funds merchants. Card processing runs the issuer's side: cardholder accounts, issuer authorizations, settlement as the scheme's issuer-side counterparty |
| Payment Gateway | opposite side, front end | merchant-facing acceptance surfaces and secure payment-data transmission; no issuer-side rail participation |
| Core Banking System | upstream ledger | the bank's deposit/credit books. The processing platform either holds a programme-scoped balance ledger or interfaces with the core in real time; in gateway modes the core remains the balance holder and decision maker |
| Fraud Detection Platform | embedded vs standalone | the processing platform embeds programme-scoped fraud screening in the authorization flow; the standalone fraud platform is cross-industry fraud operations (signal enrichment, cases, model loops) |
| Digital Wallet | downstream credential holder | wallets store and present card credentials; tokenization for wallets is an output of the processing platform, which runs the rail behind the credential |
| Corporate Card & Spend Platform | different operator | spend-side software used by the card-using company (budgets, receipts, approvals); the processing platform is programme-side infrastructure operated by the issuer/programme owner |

The boundary with **Card Issuing Platform** is the most important one: the market largely sells one fused product family, and the taxonomy separates the programme side from the rail side. The working seam: strip the rail machinery (scheme connectivity, authorization, clearing/settlement) and what remains is programme governance — issuing territory; strip programme/card governance and what remains is pure rail processing — this Type.

## Representative Products

- **Thredd** — global issuer processor (debit, credit, prepaid) with a fully public documentation portal; exposes named processing modes (gateway / cooperative / full-service) and a real-time system of record.
- **Paymentology** — global cloud-native issuer processor ("issuing & processing platform"); exposes external/internal/passive authorization tied to remote vs local store of value, with detailed transaction-lifecycle documentation.
- **Fiserv (Card Services)** — classic bank-heritage card processing for financial institutions: end-to-end debit/credit processing "from authorization to clearing and settlement" with network access, risk, and dispute services.

The modern API-first issuing platforms studied in the sibling Card Issuing Platform research (Stripe Issuing, Adyen Issuing, Marqeta, Lithic) all run issuer-side authorization processing themselves — evidence that the issuing and processing leaves overlap on the same product families.

## Sources

Research date: **2026-09-07**

- Thredd — product site and platform pages: https://www.thredd.com/ , https://www.thredd.com/platform , https://www.thredd.com/platform/core-processing , https://www.thredd.com/platform/system-of-record
- Thredd — Documentation Portal (Tier-1): https://docs.thredd.com/ ; External Host Interface (EHI) Guide (JSON): https://docs.thredd.com/EHI_Guide_JSON.htm
- Paymentology — product site: https://www.paymentology.com/ , https://www.paymentology.com/en/processing-overview
- Paymentology — Banking.Live Developer Portal (Tier-1): https://developer.paymentology.com/docs/start-get-started ; Transaction lifecycle overview: https://developer.paymentology.com/v3.0/docs/txn-lifecycle-overview ; Authorization: https://developer.paymentology.com/v3.0/docs/txn-authorization ; Clearing, settlement and reconciliation: https://developer.paymentology.com/v3.0/docs/txn-clearing-settlement-reconciliation ; Stand-in Processing: https://developer.paymentology.com/v3.0/docs/txn-stip
- Fiserv — Card Services (product pages): https://www.fiserv.com/en/solutions/card-services.html , https://www.fiserv.com/en/who-we-serve/bank.html
- Sibling research cross-checks: research/card-issuing-platform.md , research/payment-processing-platform.md

> Sourcing limitations: several issuer processors could not be reached from the research environment (Pismo, i2c, TSYS, FIS, Galileo — repeated transport errors, wrong-site responses, or gated documentation). The classic bank-processor pole is therefore evidenced at product-page level only, and its internal operational workflow is structurally inferred rather than directly observed; claims about that pole are kept general. Precise operational figures (scheme timing tables, matching-rate claims, scale statistics) observed in vendor materials are intentionally not stated as general facts in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
