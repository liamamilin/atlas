# Stored Value Wallet

## Overview

A **Stored Value Wallet** is a consumer payment application whose payment instrument is the user's own prepaid monetary balance. The user keeps money inside a wallet account, loads it through standing entry paths (bank transfer, card, cash at an agent or outlet, payroll), spends it down at the wallet's acceptance points, and relies on the balance and transaction history as the standing record of what they hold and what moved.

The defining structure is small:

```text
Wallet Account (persistent, attributed to a holder)
└── Prepaid Balance of record
    ├── Loading (in) — bank transfer, card, cash at agent/outlet, payroll, refunds
    ├── Spending (out) — merchants, bills, online checkout, transfers,
    │                    each authorized by drawing down the balance
    └── Balance & history — the user's standing view of value and movement
```

The single question that separates this Type from its sibling wallet Types is **where a payment draws from**. A credential-style wallet stores cards and passes and pays from linked external accounts; a stored value wallet pays from the user's own money held inside the wallet. Many real products carry both structures in one app — the boundary is structural, not per-product.

## Users & Context

The primary user is an individual consumer who pays, receives, and holds money in everyday life. Typical reasons to open the application:

- load money in and pay a merchant, a bill, or another person without reaching for cash or a card
- check what is left before or after spending
- receive money from another person, an employer, or a refund into a place it can be spent immediately
- keep spending inside a fixed amount loaded in advance — the balance is a natural budget

Counterparties form the context around the user: merchants who accept the wallet (in-store and online), billers, and — in cash-heavy markets — human agents and outlets where cash is converted into wallet value and back. The dominant surface is a phone app, but the Type does not require a smartphone: some of the most widely used shapes run on basic phones through operator menu codes and agent counters, and others extend the balance onto a physical card.

## Core Model

### The Defining Core

Four properties together make a stored value wallet. Removing any one turns the remainder into a different kind of product:

- **Wallet account of record** — a persistent container for value, attributed to a holder and maintained by the wallet operator, outliving any individual transaction. The holder may be identified in different ways across products (full identity, phone number, account credential). Without this, the product is a disposable instrument — a voucher or one-shot code, not an account a person returns to.
- **Prepaid balance of record** — the user's own monetary value, held in the account **in advance of spending**. The balance is the reservoir every payment draws from. Without this, the product is a credential container that pays from linked bank accounts or cards — a different wallet Type.
- **Loading path** — standing ways value enters the balance from outside: bank transfer, card top-up, cash handed to an agent or outlet, payroll or direct deposit, refunds and rewards credited by the operator. Without ongoing loading, the product is a single-endowment account — a gift-card shape.
- **Spending against the balance** — the wallet's own payment motion. A payment to a merchant, a biller, an online checkout, or another person is authorized by drawing down the stored balance at the wallet's acceptance points. Without this, the account is a place where value sits — a savings jar or top-up register, not a payment wallet.

### Standard Capabilities of Mature Products

These capabilities are widespread in mature products and make the wallet practical, but they do not define the Type:

- **Balance and history visibility** — a current balance on the home surface and a searchable record of every load, spend, and transfer. The wallet is its own statement.
- **Linked funding sources** — bank accounts and cards attached to the account to feed the loading path.
- **Cash-out / withdrawal** — moving value back out: withdrawal to a bank, or cash at an agent or outlet. Common, but not universal — some closed-loop shapes forbid it.
- **Person-to-person send and request** — transferring between wallet users as an alternative to cash.
- **Merchant acceptance surfaces** — the era's instruments: QR codes to scan or present, tap-to-pay, online checkout buttons, business payment codes.
- **Bill payment** — utilities, airtime, and recurring services as a spend category.
- **Security surfaces** — PIN or app lock, payment confirmation, in some products recipient-name confirmation before sending.
- **Published limits and fees** — tariffs, caps, and charges published per product and jurisdiction; what an account may do often depends on how far it has been registered and verified.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently, and no single implementation is the definition:

```text
Concept:      Wallet account of record
Realizations: e-money account, wallet balance account, mobile-money account,
              prepaid account behind a card

Concept:      Loading path
Realizations: cash at agents/outlets, bank transfer, card top-up,
              payroll/direct deposit, refunds and cashback credit

Concept:      Spending against the balance
Realizations: merchant QR / tap / payment code, online checkout,
              bill payment, in-app purchases, transfers to other users

Concept:      User surfaces
Realizations: smartphone app, USSD / operator menu codes on basic phones,
              web dashboard, agent counters, companion physical card
```

A reader who has only seen one shape — for example a phone-app wallet in a card-heavy market — should still be able to recognize an agent-and-USSD mobile-money wallet, or a balance behind a prepaid card, as the same Type.

## How It Works

### Open and verify the account

```text
Register
→ provide the identity the product requires (phone number, ID, credential)
→ account becomes active
→ what the account may do can widen as verification deepens
```

Registration is an explicit getting-started step across the researched products. The details of tiers and limits vary by product and jurisdiction; what is structural is that usage is gated by an account the operator controls.

### Load the balance

```text
Choose a loading path
→ cash at an agent/outlet, bank transfer, card top-up, direct deposit
→ value appears in the wallet balance
→ balance and history update
```

Loading is the prepaid motion: money moves from the outside world into the wallet's own reservoir. In cash-heavy markets the agent network is the dominant loading path; in card-heavy markets bank and card links dominate.

### Spend against the balance

```text
Choose a payee
→ merchant (scan / tap / payment code / checkout), bill, or another person
→ authorize with PIN or confirmation
→ the payment is drawn from the wallet balance
→ the balance falls; the transaction appears in history
```

This is the defining motion. The payment is authorized against stored value — if the balance is empty, the pure-form wallet cannot pay — rather than against a linked bank account or card.

### Check balance and history

```text
Open the home surface
→ see current balance and recent activity
→ open the statement for a full record of loads, spends, and transfers
```

The user returns to this loop constantly; the balance is the wallet's center of gravity, and the history is how the user reconciles what happened.

### Cash out (where supported)

```text
Choose a withdrawal path
→ transfer to a bank, or collect cash at an agent/outlet
→ balance falls by the withdrawn amount
```

Cash-out closes the loop with the physical economy. It is standard in mobile-money shapes; closed-loop variants may not offer it at all.

### Capability tiers

**Defining core** — without these, not a stored value wallet:

- persistent wallet account attributed to a holder
- prepaid balance held in the account in advance of spending
- standing loading paths into the balance
- spending that draws down the balance at the wallet's acceptance points

**Standard capabilities** — present in most mature products:

- balance and transaction history surfaces
- linked funding sources (banks, cards)
- cash-out / withdrawal (where the shape permits)
- person-to-person send and request
- merchant acceptance surfaces, bill payment
- PIN/confirmation security, published limits and fees

**Variant or optional** — depends on market, operator, and era:

- agent cash networks and basic-phone channels
- companion physical or virtual card drawn against the balance
- withdrawable vs spend-only value classes
- cross-border send/receive
- savings, credit, and investment modules riding on the wallet

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Home / balance dashboard

The entry surface and the wallet's center of gravity.

- current balance, quick actions (pay, send, add money)
- recent activity at a glance
- primary actions: start a payment, add money, open history

### Add money surface

The loading motion made explicit.

- loading paths available to the account (bank, card, agent/outlet instructions, direct deposit)
- amount entry and confirmation
- primary actions: load the balance, review pending loads

### Pay surface

The spending motion.

- acceptance instruments of the product: QR scan/present, tap, business payment code, online checkout handoff, bill selection
- amount entry, authorization (PIN/confirmation), success or failure state
- primary actions: pay a merchant, pay a bill, pay a person

### Send & request

The person-to-person surface.

- recipient selection from the wallet's user base, amount, confirmation — in some products with recipient-name verification before sending
- primary actions: send, request, split

### Activity / statement

The record surface.

- chronological loads, spends, transfers, withdrawals with amounts and counterparties
- primary actions: search/filter, inspect a transaction, in some products report or reverse

### Operator-channel and agent surfaces (variant)

Surfaces for shapes that run beyond the smartphone app.

- menu codes on basic phones exposing balance, send, and pay as numbered menus
- agent counters where cash is converted to and from wallet value on the user's behalf
- card management for balance-backed companion cards

### Settings & security

- PIN and lock configuration, linked funding sources, verification status, limits and fees

## Important Rules / Behaviors

### Spending stops at the balance

In its pure form the wallet cannot go negative: a payment exceeding the available balance fails rather than drawing on credit or a linked account. Where overdrafts or credit products exist, they are separate add-on structures riding on the wallet, not the wallet's own motion.

### The payment draws down stored value, not a linked instrument

This is the rule that distinguishes the Type. However the payment is presented (QR, code, checkout, card), the authorization consumes the wallet's own balance. Credential-style wallets follow the opposite rule; hybrid products carry both motions side by side.

### Verification gates capability

What an account may do — how much it can load, hold, spend, or withdraw — depends on registration and verification depth, with limits and fees published by the operator per jurisdiction. The specifics vary widely; the gating itself is structural.

### Value classes can differ

Some products distinguish kinds of balance value — for example promotional or cashback value that can be spent but not withdrawn, versus fully withdrawable loaded value. Where value came from can therefore matter to what it can do.

### Where the money sits

The balance is the user's money held by the wallet operator under whatever regime applies — in researched products the operator is typically a fintech, a telecom, or a licensed issuer rather than a deposit-taking bank; one product keeps even its savings product explicitly outside the balance as a separate bank-held account. The consumer-facing consequence is the same: the balance is spendable value, not a bank deposit.

### Closing the loop with cash

In cash-heavy shapes the agent/outlet network is a structural counterparty: cash in and cash out are standing services, not exceptional events. Reversal and error-recovery paths exist in mature products — payment mistakes are an expected part of the workflow, and some products surface recipient confirmation before money leaves.

## Variants

- **Open-loop general-purpose wallets** — spend anywhere the operator's acceptance network runs: in-store, online, bills, transfers (e.g. PayPal, GCash).
- **Telco/agent mobile money** — phone-number identity, agent cash network, USSD/basic-phone channels alongside an app; designed for markets where cash and agents dominate (e.g. M-PESA).
- **Hybrid credential + balance wallets** — a credential container that also carries a distinct balance account; both motions in one app (e.g. PayPal's Balance account beside stored cards and banks).
- **Super-app embedded wallets** — the wallet as the payments module of a wider platform carrying shopping, credit, savings, and investments (e.g. GCash, Paytm).
- **Card-companion wallets** — the balance extended onto a physical or virtual prepaid card spendable on ordinary card rails.
- **P2P-first wallets** — transfer-led products where the balance is the funding reservoir behind social payments (e.g. Venmo).
- **Closed-loop operator-scoped value** — retailer store credit, campus cards, venue cashless systems, transit purses: same prepaid mechanics, but scoped to an operating institution with its own privileges and rules. These are separate Types in this atlas, related by the shared balance mechanic rather than absorbed into this one.
- **Market-drift note** — in some markets, spending has migrated toward bank-account rails (e.g. India's UPI), and formerly wallet-first products now lead with bank transfers; the wallet persists as a reservoir and residual rails. This is market context, not a change to the Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Digital Wallet | sibling (§08) | credential container: stores cards/passes and pays from linked external accounts; a user-held prepaid balance is optional. Strip the balance → Digital Wallet; add it as the spend source → this Type. Hybrid products carry both |
| Mobile Wallet | sibling (§08) | names a form factor, not a value structure; most wallets are mobile. Expected to resolve as a form-factor variant in its own pass |
| Peer-to-peer Payment Application | embedded capability | P2P core is transfer between individuals; the wallet core is the prepaid spending account. Remove merchant/bill spending → P2P remains; remove P2P → wallet remains |
| Digital Banking Application / Mobile Banking Application | adjacent | a deposit relationship (interest, overdraft, bank statements) vs prepaid spendable value held by a non-bank operator; a wallet balance is not a bank deposit |
| Store Credit / Stored Value Platform | merchant-side counterpart | the merchant's system of record for a closed-loop value program vs the consumer's own spending wallet; value spendable only at the issuing merchant's channels belongs to that Type |
| Gift Card Management | adjacent | single-merchant, single-endowment instrument programs vs an ongoing-load, multi-use user account |
| Campus Card Management | scoped sibling | institution-scoped closed loop bundled with identity and access privileges; strip the institution layer → a wallet |
| Cashless Venue Platform | scoped sibling | venue-administered guest spending account for venue operations; strip the venue context → a (closed-loop) wallet |
| Card Issuing Platform | B-side counterpart | issuing/processing infrastructure behind prepaid cards and wallet rails vs the consumer-facing wallet application |
| Payment Gateway / Payment Processing Platform | payee-side rails | acceptance infrastructure that treats wallets as payment method types; wallets are payer-side instruments |
| Crypto Wallet | same word, different asset | user-held blockchain keys over chain assets vs operator-held fiat prepaid balance over a ledger |

## Representative Products

- PayPal — hybrid consumer wallet carrying an explicit balance account beside stored cards and banks
- GCash — mobile-first wallet with cash-in/cash-out outlet services, merchant QR, and bill pay
- M-PESA — telco-anchored mobile money: agent deposit/withdrawal, merchant payment codes, USSD and basic-phone channels
- Paytm — India market anchor; formerly wallet-first, now bank-rail-led (market-drift reference)
- Venmo — P2P-first wallet shape (market anchor; official documentation not reachable during research)

The definition was checked against older and non-app shapes: prepaid calling-card accounts (persistent PIN account, top-up, usage draw-down) and prepaid airtime credit satisfy the defining core with no smartphone, QR code, or agent app; paper vouchers and single-shot codes fail the account leg and are instruments, not wallets.

## Sources

Research date: **2026-09-08**

Official product surfaces reached:

- Safaricom (M-PESA) — M-PESA services hub — https://www.safaricom.co.ke/personal/m-pesa
- PayPal — PayPal US consumer home (incl. Balance-account footnotes) — https://www.paypal.com/us/home
- GCash (G-Xchange / Mynt) — consumer home — https://www.gcash.com/
- Paytm — consumer home — https://paytm.com/

> Sourcing limitation: vendor help centers, legal/user-agreement pages, and Venmo were not reachable from the research environment (403/404/406 responses) on 2026-09-08. Product facts rest on the reachable official product/home pages listed above. Operational precision — verification-tier limits, fee schedules, balance-expiry and closure rules, withdrawability classes per product — is intentionally not stated in this document; such details remain in the Research Notes with their evidence status.

Detailed product-by-product observations, the cross-product comparison matrix, rejected findings, and boundary remove-tests are recorded in the paired Research Notes.
