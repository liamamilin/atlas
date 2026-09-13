# Store Credit / Stored Value Platform

## Overview

A **Store Credit / Stored Value Platform** is the merchant-side system of record for closed-loop customer credit: currency balances that a merchant holds against identified customers — issued as refunds converted to credit, goodwill, rewards, or purchased top-ups — and redeemed as a payment method at the merchant's own selling channels.

The defining structure is small:

```text
Merchant-operated closed-loop customer credit program
└── Customer credit balance of record
    └── Merchant-governed issuance of value into the balance
        └── Redemption as tender at the merchant's own channels
            └── Balance-activity record over the balance's life
```

Store credit is not a discount (it carries prepaid value rather than changing a price), not loyalty points (it is issued, owed, or deposited — not earned through purchase behavior — and it is spent as tender rather than traded against a rewards catalog), and not a consumer wallet (the program, the ledger, and the liability belong to the merchant, and the value spends only at that merchant's channels). What the platform manages is the population of customer balances: how value enters them, how it is spent, how it is governed, and what the merchant ultimately owes.

The two halves of the name describe the same machinery from two angles. **Store credit** is the value the merchant owes a customer — most visibly the refund issued as credit instead of cash. **Stored value** is the broader family of prepaid, closed-loop balances a merchant operates for its customers, including customer-funded top-up accounts. Realizations range from dedicated credit-wallet platforms to prepaid card instruments to coupon-code implementations; the balance semantics, not the plumbing, make the Type.

## Users & Context

**Primary users (merchant side):**

- **Customer-service / refund operator** — converts a refund into store credit (directly or through a returns platform's flow), issues goodwill credit for service failures, answers balance questions.
- **Retention / marketing administrator** — configures the credit program: what issuance events grant credit, whether taking credit over cash earns a bonus, whether and when credit expires, and which channels can redeem it.
- **Store staff / cashier** — looks up a customer's balance, applies credit as tender in person, adjusts balances for operational reasons.
- **Finance / accounting** — owns the outstanding-liability view: issued-but-unredeemed credit is money the merchant owes back as goods and services, and it must be reported and reconciled.

**Secondary users (customer side):** the customer holds the balance — in a store-account wallet, as an emailed credit code, or on a linked card — sees the remaining amount, and spends it at checkout over one or many visits.

The work context is dominated by e-commerce (where refund-to-credit is a core retention lever), extends to omnichannel retail where credit redeemed in person must match the online balance, and reaches corporate audiences (employee recognition, B2B incentives) where the same balance machinery serves non-refund issuance.

## Core Model

### The Defining Core

Four jointly-held properties; remove any one and the product stops being a store credit / stored value platform:

- **Customer credit balance of record.** The central object is a currency-denominated balance held against an identified customer relationship — realized as a wallet in the customer's store account, a credit code the program attributes to that customer, or a prepaid instrument linked to the customer's profile. The balance is closed-loop: it spends only at the issuing merchant's channels. Without a standing customer-attached balance, there is nothing to manage — only one-off vouchers or refund memos.
- **Merchant-governed issuance.** Value does not appear in the balance by itself. It enters through controlled issuance events defined by the merchant's program, each carrying a distinguishable provenance: a refund converted to credit, goodwill or compensation, a manual send, a customer's own purchase or top-up, or a campaign/employee issue. This governance — the merchant decides what value enters, when, and on what terms, and the records show which kind of value it was — is what separates a credit program from a plain prepaid payment account.
- **Redemption as tender.** The balance is spent as a payment method for purchases at the merchant's channels. Partial redemption — apply part of the balance now, keep the rest — is the standard semantic, and a purchase larger than the balance is paid by combining the credit with another payment method. Without spendable-as-tender semantics the value is not store credit but accounting or rewards.
- **Balance-activity record.** Every value movement — issuance, redemption, adjustment, refund-to-credit, expiry where present — is recorded as a typed event against the balance, forming an inspectable history. This is what makes balances auditable, disputes resolvable, provenance traceable, and the merchant's outstanding liability computable.

### How Credit Attaches to the Customer

The conceptual object — a customer-attached, closed-loop balance — is substrate-independent. Common implementations:

```text
Concept:      Customer credit balance of record
Realizations: wallet inside the customer's store account
              emailed credit code attributed to the customer
              prepaid card/instrument linked to the customer profile
              coupon-code object carrying a monetary balance
```

A reader who meets only one realization should still recognize the others: the wallet, the code, the card, and the coupon are the same balance wearing different plumbing.

### Capabilities Mature Products Commonly Add

Widespread in current products, but not what makes the product a store credit platform:

- **Refund-to-credit as a first-class flow**, often automated from returns systems, with opt-in incentives — a bonus amount if the customer takes credit instead of a cash refund.
- **Customer wallet surface** — balance display in the store account or via the emailed code, redemption history, one-click application at checkout.
- **Expiry/validity policy machinery** — credit may never expire, expire after a window, or carry a deliberately short expiry used as a re-purchase motivator, constrained by the law of each market.
- **Multi-provenance wallet unification** — refunds, cashback, compensation, referral rewards, membership credits, employee recognition, and B2B incentives landing in one balance.
- **Manual issuance and adjustments** as distinct typed events, so a goodwill credit does not look like a sale and an operational correction does not look like a redemption.
- **Bulk issuance** of credit codes for campaigns, segments, and employee programs.
- **Outstanding-liability reporting** — the total unredeemed balance across the program, sometimes with per-merchant liability caps as a risk control.
- **Integration surfaces** — APIs and webhooks so returns platforms, checkouts, POS, and finance systems can issue, redeem, and reconcile against the same ledger.
- **Multi-location / multi-store redemption** — one program spanning all of the merchant's locations and online store.

## How It Works

### Configure the credit program

The administrator defines the rules before any value moves: which issuance events grant credit and how much, whether customers receive an incentive for choosing credit over cash, whether credit expires and from when, which provenances share one balance, and which channels (online checkout, in-store POS, multi-store family) can redeem it.

### Issue value

Four issuance loops recur across implementations:

```text
Refund conversion   return processed → customer offered credit (often with a bonus)
                    → merchant or returns flow issues credit to the customer's
                      balance — the flagship loop
Goodwill/manual     service failure or compensation → merchant sends credit
                    directly from an admin console
Customer-funded     customer buys a credit top-up (or a "gift card" that is
                    functionally store credit) → value lands in their balance
Program/automated   campaign bulk issue, employee recognition, referral or
                    cashback rewards, or an automated trigger on a user event
```

Each issuance is recorded with its provenance. The refund-credit event is deliberately distinct from an ordinary sale in the records, and an operational adjustment is distinct from both.

### Customer holds and sees the balance

The balance lives where the customer can reach it: a wallet in their store account, an emailed credit code, or a linked card. Customer-facing surfaces show the remaining amount and, commonly, the redemption history.

### Redeem as tender

```text
Customer reaches checkout (online) or the register (in person)
→ applies the balance — one-click from the wallet, by entering the code,
  or by staff lookup
→ purchase amount is drawn down — partially if the balance is smaller
→ the excess, if any, is paid with another payment method
→ remaining balance stays for future purchases
→ repeat until the balance is exhausted or expires
```

### Govern and report

- **Adjustments and corrections** — mistaken redemptions reversed, balances corrected, credit disabled for fraud or closure; all recorded.
- **Expiry** — a policy decision and a compliance surface; enforcement strength can differ between an in-store clerk who sees a warning and an online checkout that hard-blocks.
- **Reporting** — issuance and redemption activity by provenance and channel, and the outstanding liability: money the merchant has taken in (or owed out) that still must be delivered as future goods and services.

### Core, standard, and optional capabilities

**Defining core** — without these, not this Type:

- customer credit balance of record (closed-loop)
- merchant-governed, provenance-typed issuance
- redemption as tender with partial drawdown and combined payment
- balance-activity record

**Standard capabilities** — present in most mature products:

- refund-to-credit flow with opt-in incentives
- customer wallet/balance surface
- expiry/validity policy machinery
- manual issuance and typed adjustments
- outstanding-liability reporting
- admin operations (search, adjust, disable, resend)
- APIs/webhooks and returns-platform integration
- multi-location redemption

**Optional / variant** — depends on segment and posture:

- multi-provenance wallet unification (cashback, referrals, memberships, employee, B2B)
- bulk/campaign issuance
- instant credit before returned goods arrive
- per-merchant liability caps and regional compliance-limit tables
- in-store (POS) redemption where the program started online-only
- service-unit backing instead of currency (found in the wider stored-value family)

## Interfaces

Exact layouts vary by product; conceptually the surfaces are:

### Program settings

Purpose: configure the credit program. Typical contents: issuance rules and amounts, incentive/bonus terms, expiry policy, provenance types sharing the balance, redemption channels. Primary actions: create/edit program rules.

### Issuance console

Purpose: put value into balances. Typical information: target customer, amount, provenance (refund/goodwill/campaign), optional expiry date, message. Primary actions: send credit, convert a refund to credit, bulk-generate credit codes, schedule delivery.

### Balance list and balance detail

Purpose: operate the population of customer balances. Typical information: customer, current balance, provenance of each issuance, state, activity history. Primary actions: inspect history, adjust, disable/void, resend credit.

### Customer wallet (customer-facing)

Purpose: let the customer hold and spend their value. Typical information: current balance, redemption history, the credit code where code-based. Primary actions: view balance, apply at checkout, redeem in store.

### Checkout / POS application surface

Purpose: spend the balance as tender. Typical information: available balance, amount to apply, remaining due. Primary actions: apply credit, partial application, combined payment with another method.

### Reporting

Purpose: monitor the program and its obligation. Typical information: issuance and redemption by provenance/channel/time, outstanding liability, exportable data. Primary actions: filter, export, reconcile with accounting.

### APIs / webhooks

Not a page but a working surface for mature deployments: returns platforms trigger issuance, checkouts redeem, finance systems pull liability data.

## Important Rules / Behaviors

**Spend-only, partial by default.** Redemption reduces the balance; a balance cannot go negative; amounts beyond the balance are paid by other means. Remaining value stays spendable until exhausted or expired.

**Issuance is governed and typed.** Value enters only through program-controlled events, and the records distinguish refund-credit from goodwill, from top-up, from adjustment. This typing is what keeps the liability computable and disputes resolvable.

**Credit is normally not cash.** The balance pays for the merchant's goods and services; cashing out is not the standard semantic, and refunding a purchase that was paid with credit typically re-credits the balance rather than paying cash.

**Expiry is a policy — and a legal one.** Whether credit expires, from when, and whether staff may still honor expired credit are program decisions constrained by jurisdiction; several markets regulate stored-value expiry. Short expiries are also used deliberately as a re-purchase motivator where lawful.

**The outstanding balance is a liability.** Issued-but-unredeemed credit is an obligation the merchant owes back as future purchases. Mature products surface it as a report; some platforms cap it per merchant as a risk control.

**Closed loop.** The balance spends only at the issuing merchant's program — its locations and online store. Multi-store and multi-location redemption work within the program, never outside it.

**Instant credit is a risk posture.** When credit is issued before returned goods arrive (a pattern in returns-integrated programs), the merchant has opted into a faster experience with higher exposure; programs that wait for the return to process issue credit later.

## Variants

- **Dedicated credit-wallet platform** — an independent product whose entire frame is the customer credit wallet, slotting into a commerce platform as an app layer and unifying refunds, cashback, and rewards in one balance.
- **Commerce/POS instrument implementation** — credit realized through the merchant's prepaid card instrument, linked to customer profiles; refund-to-card is the store-credit flow.
- **Coupon-code implementation** — credit realized as a monetary-balance coupon applied at checkout; the balance semantics (reusable until exhausted, remainder by other methods) distinguish it from an ordinary discount coupon.
- **Commerce-platform native primitive** — store credit built directly into the selling platform's customer accounts.
- **Enterprise closed-loop network** — stored-value machinery sold as a network service at multi-brand, multi-location scale, including cashless venue/campus forms.
- **Provenance-mix variants** — refunds-only programs vs full retention wallets with many issuance intents.
- **Channel variants** — online-only programs vs omnichannel (online balance redeemable in store).
- **Regional compliance shapes** — expiry legality, per-card and per-merchant caps, and fee regimes vary by market and shape the program's rules.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Gift Card Management | the same balance-drawdown machinery, aimed at a different job: a purchased instrument meant to be given to (and spent by) someone else, instrument-centric and typically transferable; store credit is value the merchant owes or holds for a specific customer, customer-attached by default. The two meet and blur in products that implement credit through gift-card instruments or unify both in one wallet |
| Loyalty Program Management | value is earned through purchase behavior under accrual rules and typically redeemed against a rewards catalog; store credit is issued/owed/deposited currency value spent as tender. They meet where loyalty pays out as credit |
| Returns Management Platform | decides return entitlement and orchestrates the return; its credit outcome is executed by creating credit in the commerce platform or a credit platform. The returns system owns the workflow; the credit platform owns the balance |
| Promotion Management | a promo code changes the price of a transaction; store credit carries prepaid value consumed across transactions. Coupon-based credit implementations live exactly on this seam — the balance, not the coupon mechanics, makes it credit |
| Retail POS / E-commerce Platform / Checkout | the surfaces where credit is redeemed; the credit platform owns the balance, program, ledger, and liability, and is usually packaged as a module or app of these platforms |
| Credit Management Platform | B2B trade credit: invoiced, post-sale receivable exposure governed by limits — a different world from prepaid closed-loop customer value, despite the shared word "credit" |
| Digital Wallet / Stored Value Wallet | consumer-side storage of value, often general-purpose and open-loop; the merchant-side program, ledger, and liability remain with this Type |
| Card Issuing / Payment Processing | a credit balance may act as a payment method at the merchant, but settlement stays inside the merchant's program; network-branded prepaid cards are issuing products, outside this Type |
| Cashless Venue Platform / Campus Card Management | prepaid balances bound to a venue or campus context (access, hardware, on-site consumption); store credit is general merchant credit, spendable across the merchant's catalog |

## Representative Products

- **Rise.ai** — dedicated "Gift Card & Store Credit Platform" for e-commerce brands; one customer wallet holding store credit, gift cards, and cashback; refund-to-credit automations with opt-in boosts; liability reporting; bulk issuance.
- **Square Gift Cards** — store credit realized through a POS-ecosystem prepaid instrument; Square's own documentation frames refund-to-gift-card as "issuing store credit"; typed activity ledger; liability caps.
- **Smart Coupons for WooCommerce** — coupon-code implementation: store credit as a monetary-balance coupon reusable until exhausted; refund-to-credit via a send-credit console; open-source/self-host pole.
- **Loop Returns** — studied as a boundary anchor: a returns platform whose credit outcome (gift-card creation, instant credit) executes in the commerce platform, demonstrating the seam between returns orchestration and credit balance management.
- **Givex (Shift4)** — enterprise closed-loop network pole (gift cards, loyalty, cashless venue ticketing), studied as structural context for the enterprise/stored-value family.

The definition was checked against older and lower-technology forms: a paper merchandise credit slip — issued on a return under store policy, recorded in a ledger, presented at the register as payment, non-cashable — satisfies the same core without cards, wallets, emails, or APIs, which is why none of those appear in the defining structure.

## Sources

Research date: **2026-09-08**

- Rise.ai — https://rise.ai/ and https://rise.ai/solutions/refunds/ (fetched 2026-09-08); gift-card solution page fetched 2026-09-07
- Square — Gift Cards API and Gift Card Activities API guide: https://developer.squareup.com/docs/gift-cards/using-gift-cards-api (fetched 2026-09-08); product page https://squareup.com/us/en/gift-cards and API reference (fetched 2026-09-07)
- Loop Returns — documentation index https://docs.loopreturns.com/llms.txt, Set Credit Type and Process Return API references (fetched 2026-09-08)
- Smart Coupons for WooCommerce — https://woocommerce.com/document/smart-coupons/, including "How to provide store credit for a refund" and "How to create gift cards in WooCommerce (advanced)" (fetched 2026-09-08)
- Givex / Shift4 — https://web.givex.com/ (fetched 2026-09-08)

> Sourcing limitations: the Rise.ai help center (403 ×2) and the Shopify help center (403 ×2, across 2026-09-07 and 2026-09-08) were not reachable from the research environment, so Rise-specific mechanics rest on product-page evidence and platform-native store-credit implementations were not directly observed; the enterprise closed-loop pole (Givex-class) is described structurally from landing-page evidence only. Numeric limits, fee schedules, code formats, and vendor benchmark claims are intentionally omitted from this document and retained, where observed, in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
