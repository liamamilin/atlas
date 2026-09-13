# Loyalty Program Management

## Overview

A **Loyalty Program Management** application is the brand-side system of record for operating a customer loyalty program. It holds a configured program — rules for how customers earn value and what that value can be exchanged for — over an enrolled member population; records qualifying customer behavior (purchases above all, and in many products non-purchase actions such as birthdays or reviews) as earned value in member balances; and redeems that value through the program's configured reward options.

The defining core is small:

```text
Loyalty program (brand-configured earn + redemption rules)
└── Enrolled member (identified customer holding an earned-value balance)
    └── Behavior-triggered accrual (qualifying behavior under earn rules)
        └── Redemption (earned value exchanged for configured benefits)
```

Everything commonly associated with loyalty products — member tiers, birthday bonuses, gamification, referral modules, fraud tooling, marketing-automation integrations, mobile apps and wallet passes — is widespread in current products but layered on that core rather than defining it. The paper stamp book and the café punch card satisfy the same core: a program's earn rule, a customer holding earned value, and a counter where the value redeems. What the software adds is scale: configuration instead of printed rules, automatic accrual instead of hand stamping, and a ledger that survives across every channel.

## Users & Context

**Primary operators** work inside the brand or merchant that runs the program:

- **Program / loyalty manager** — configures the program: how value is earned, what it redeems for, expiry policy, and (where present) tier ladders; launches temporary earn campaigns; watches program health.
- **Store or checkout staff** — identify the member at the point of sale, apply earned rewards to a transaction, and enroll new members.
- **Member operations / customer service** — look up individual member accounts, correct balances, apply goodwill adjustments, and resolve redemption problems.

**External participant**: the customer, who joins the program (directly or via checkout enrollment), earns value through purchases and actions, tracks their balance in a member-facing surface, and redeems rewards at the brand's channels.

The work environment spans the brand's selling surfaces — physical stores, online checkout, mobile apps — and the operator back office. Loyalty is an always-on program rather than a campaign: it runs continuously against every qualifying transaction, with campaigns layered on top for limited periods.

## Core Model

### The defining core

**Loyalty program.** The container the brand configures. A program defines:

- **Earn rules** — which qualifying behavior produces value, and how much. Purchase-based earn rules are the backbone: points per visit (optionally with a minimum spend), points per amount spent, or points for specific items or categories. Action-based earn rules extend earning beyond purchases — signing up, a birthday, writing a review, sharing on social media, or custom actions the brand defines.
- **Redemption options** — what earned value can be exchanged for, at what threshold. A redemption option pairs a points requirement with a benefit: a discount (amount or percentage, scoped to the whole sale, specific categories, or specific items), a free item, a voucher, or another configured perk. Multiple options at escalating thresholds form the reward catalog.
- **Program policy** — expiry of earned value, earning limits, and terms of participation.

**Member.** An identified customer enrolled in the program, holding a member account. The account carries the earned-value balance (what is currently spendable) alongside lifetime-earned totals and the enrollment record. A mapping ties the account to the person in the real world — a phone number, an email, a member code, or a linked customer profile in the brand's CRM. One customer holds one account per program; identification is what makes earning possible at all.

**Accrual.** The movement of value into a member's balance when recorded behavior matches an earn rule. Accrual is event-driven: a purchase is identified as belonging to a member, the earn rules are evaluated, and a credit is posted. In mature products every balance change is recorded as a typed transaction on the member account — earn, redemption, adjustment, expiry — forming an auditable ledger.

**Redemption.** The exchange of accumulated value for a configured benefit. The member chooses a redemption option they can afford; the system checks the threshold, debits the balance, and issues the reward — commonly as a discount coupon, an instant discount at checkout, or a voucher presented to staff. The reward attaches to the member's *own* accumulated value, which is what separates loyalty from acquisition programs that reward bringing in other people.

```text
Customer behavior (purchase / action)
  → identified as belonging to a member
  → evaluated against earn rules
  → balance credited (ledger entry)
  → member selects a redemption option
  → threshold checked, balance debited
  → reward issued (coupon / discount / voucher / free item)
```

### Earned value takes different forms

The core model speaks of *earned value* deliberately, because products implement it differently:

```text
Concept:      Earned program value
Forms:        points (most common), stamps/punches, visit counts, status credit

Concept:      Member identification
Forms:        phone number lookup, member code / app scan, NFC tap,
              email match on an order, card in the brand's CRM

Concept:      Accrual trigger
Forms:        POS transaction, e-commerce order sync, imported transaction
              batch, explicit customer action, manual staff validation

Concept:      Reward issuance
Forms:        discount coupon code, instant checkout discount,
              voucher to show in-store, free item, physical/perk reward
```

A reader who has only seen points-based e-commerce loyalty should still recognize a punch-card program as the same Type from this table.

### Standard capabilities layered on the core

Mature products commonly add:

- **Member tiers** — a status ladder (qualification by spend, points, or other criteria) with per-tier benefits such as better earn rates, exclusive rewards, or privileges. Very common, but several real programs run without tiers, so tiers do not define the Type.
- **Bonus campaigns** — temporary multiplier events ("double points weekends") layered on the base earn rules.
- **Expiry machinery** — schedules under which earned value expires if unused.
- **Return/refund handling** — see Rules below.
- **Manual adjustments** — staff-posted balance corrections and goodwill credits, fully recorded in the ledger.
- **Reporting and analytics** — enrollment, earning, redemption, and breakage-style program health views.
- **Integration spine** — event ingestion from POS/e-commerce systems, webhooks, and connectors into marketing-automation and CRM platforms, so loyalty balances and statuses flow into the brand's wider customer view.

Optional capabilities, depending on product and segment: gamification (challenges, quizzes, prize wheels), referral modules riding the same platform, fraud-prevention tooling over action-based earning, in-store wallet/card credentials, multi-brand or coalition operation, white-label and headless delivery.

## How It Works

### Configure the program

The operator defines the earn rules, the redemption options, expiry policy, and (optionally) tiers and their benefits. In most products this configuration lives in an admin console; the program is created once and then runs continuously. Many products deliberately separate configuration from runtime APIs — integrations can earn and redeem on behalf of members, but the program's rules are changed only by operators.

### Enroll members

A customer becomes a member by joining the program — through a signup page, an embedded loyalty panel, a mobile app, or staff enrollment at the register, typically with an acceptance of terms. Enrollment creates the member account and establishes the identification mapping (phone number, email, member code) that will bind future behavior to the balance.

### Earn

```text
Customer makes a purchase (or performs a qualifying action)
→ the behavior is identified as belonging to a member
  (phone lookup at POS, email match at checkout, transaction import,
   member-code scan, app check-in)
→ earn rules are evaluated against the recorded behavior
→ the balance is credited, with a ledger entry
```

Unidentified purchases do not earn — the identification step is what makes loyalty an account-based program rather than anonymous promotion. Action-based earning follows the same loop with a different event: the platform receives the action (often through an integration or webhook), matches it against earn rules, and credits the balance.

### Redeem

```text
Member views their balance (panel / app / staff lookup)
→ selects a redemption option they qualify for
→ system checks the threshold and debits the balance
→ reward is issued: coupon code, instant discount, voucher, free item
→ the reward is consumed at the brand's selling surface
```

Redemption usually executes inside the brand's own checkout or point of sale; the loyalty system owns the rules, the balance, and the issuance, while the selling surface applies the result to the transaction.

### Maintain and operate

Ongoing operation includes: staff looking up members and adjusting balances (corrections, goodwill), handling returns (see below), expiry running on schedule, tier requalification, campaign setup and teardown, and program reporting. Integration with marketing systems keeps the member's tier and balance visible in the brand's wider customer view, and lets loyalty events trigger messages.

### Capability tiers

- **Defining core** — program configuration (earn rules, redemption options, policy), enrolled member accounts with earned-value balances, behavior-triggered accrual, redemption with reward issuance, ledgered balance changes.
- **Standard capabilities** — identification surfaces, manual adjustments, bonus campaigns, expiry machinery, return handling, member-facing balance surfaces, checkout/POS redemption, tiers, reporting, integrations.
- **Optional / variant** — gamification, referral modules, fraud tooling, multi-brand coalitions, white-label/headless delivery, paid-membership hybrids.

## Interfaces

### Program configuration (operator)

- Purpose: define and evolve the program.
- Typical information: earn rules and their parameters, redemption options with thresholds and scopes, expiry settings, tier ladders and benefits, campaign setup.
- Primary actions: create/edit rules, launch or stop campaigns, set policy.

### Member directory and member detail (operator)

- Purpose: operate on individual member accounts.
- Typical information: identification mapping, current balance, lifetime earned, transaction and ledger history, tier status.
- Primary actions: search member, adjust balance (with reason), fix mappings, view earning/redemption history.

### Reporting (operator)

- Purpose: monitor program health.
- Typical information: enrollment counts, earning and redemption volumes, campaign performance, reward issuance statistics.
- Primary actions: filter by period/location, export.

### Member-facing surface

- Purpose: let the customer see and use their program standing.
- Typical information: current balance, earning history, available rewards, tier progress, referral status where present.
- Primary actions: browse rewards, redeem, view how to earn. Realized as an embedded storefront panel, a standalone portal, a mobile app, or a wallet pass.

### Checkout / point-of-sale surfaces

- Purpose: bind the transaction to the member and apply rewards.
- Typical information: member lookup by phone/email/code, available rewards eligible for the current basket.
- Primary actions: identify member, apply redemption, enroll new member.

### Integration surfaces

- Purpose: move program events in and out.
- Typical information: order/transaction events, member events, balance changes.
- Primary actions: post transactions or actions via API/webhook, sync member data to CRM/marketing platforms.

## Important Rules / Behaviors

- **Opt-in enrollment.** Membership is created deliberately — the customer joins, or is enrolled with their knowledge, typically accepting program terms. This is a structural gate, not a courtesy: earning and redemption presuppose an enrolled, identified member.
- **Identification gates earning.** A purchase that cannot be attributed to a member does not accrue value. The identification mapping is simultaneously a UX surface and an access-control surface for the whole economy.
- **Returns claw value back — through one of two documented approaches.** Some programs hold earned points *pending* until the transaction's return window closes before making them spendable; others post the earn immediately and apply retroactive adjustments when goods come back — an approach under which a member balance can legitimately go negative. Both postures exist in products with real documentation.
- **Expiry is a program policy.** Earned value can carry scheduled expiration; member accounts expose the pending deadlines. Programs differ in whether expiry applies to the spendable balance, to older tranches of points, or not at all.
- **Redemption is threshold-checked and scoped.** The system validates that the member can afford the option and that the benefit's scope matches the transaction; discounts may be capped, and the reward is issued as a consumable artifact (coupon, voucher, applied discount) rather than as raw spendable money.
- **Program value is not currency.** Earned value spends only through the program's configured redemption options — it is not a general tender at the register. Where brands want cashback-like behavior, they typically pay it out as store credit, which is a different (adjacent) system with its own ledger.
- **Action-based earning is fraud-prone.** Because actions other than purchases can be fabricated, products that support them commonly add rule criteria and fraud-prevention machinery around action credits.

## Variants

- **Self-serve e-commerce loyalty** — app-style products embedded in storefront platforms; the brand configures points, VIP tiers, and rewards without developers; redemption happens through checkout integrations.
- **POS-embedded loyalty** — loyalty as a subscription module of a point-of-sale ecosystem for brick-and-mortar merchants; identification at the register (often by phone number) and redemption applied directly to the sale.
- **Enterprise standalone platform** — full-scale programs for large retailers, travel, and fashion brands: transaction ingestion from multiple channels, tiers, workflows, gamification, fraud tooling, governance (roles, SSO), and deep marketing-stack connectors.
- **Headless / white-label engine** — the loyalty machinery exposed purely as APIs and configuration for integrators to build bespoke member experiences on top.
- **Digital punch card** — the minimal pole: a stamp counter per member, a fixed stamp threshold, a voucher at the end. No points economy, no tiers — and still unmistakably loyalty.
- **Large-scale vertical programs** — travel and hospitality programs (frequent-flyer and hotel-point schemes are the classic large instances) run the same core at industry scale, usually as part of the brand's own platform estate.
- **Adjacent shapes** — paid-membership programs (benefits from dues, not behavior) sit on the boundary toward Membership Management; multi-brand coalition programs pool earning across banners on shared infrastructure.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Gift Card Management | sibling value program | gift card value is purchased by a giver and held as a prepaid instrument; loyalty value is earned through behavior under accrual rules. They meet where loyalty rewards are paid out as gift cards |
| Store Credit / Stored Value Platform | sibling value program | store credit is issued, owed, or deposited currency value spent as tender; loyalty value is behavior-earned and redeemed through configured benefit options. Cashback paid as credit is the documented meeting point |
| Referral Marketing Platform | adjacent growth program | referral rewards the arrival or conversion of *other people*; loyalty rewards the customer's own repeat behavior. Shared currencies and even shared platforms, but the reward attachment differs |
| Customer Advocacy Platform | adjacent | advocacy runs asks and participation (reviews, references, UGC) with recognition rewards; loyalty runs the earned-value economy over repeat behavior |
| Promotion Management | adjacent | promotions change transaction prices for eligible populations; loyalty runs an always-on member program whose redemption *produces* discounts. Member-targeted offers can exist without owning the program |
| CRM | data neighbor | CRM holds customer relationships and interaction history; loyalty adds the program rules engine and the earned-value ledger, usually linked to CRM customer records |
| Membership Management / Member Benefits | boundary seam | membership value derives from dues and standing; loyalty value derives from behavior. Paid-membership loyalty hybrids sit exactly on this seam |
| Retail POS / E-commerce Platform | execution surface | redemption and identification happen inside those surfaces; loyalty owns program, rules, balances, and ledger |
| Affiliate / Partner Programs | different participant population | affiliates are external partners earning commissions; loyalty members are the brand's own customers earning program value |
| Rewards & Incentive Distribution | different object | distribution platforms hand out third-party reward catalogs and own no member balances or accrual rules |

## Representative Products

- **Square Loyalty** — loyalty as a module of a POS/commerce ecosystem for small merchants; phone-number-identified accounts, purchase-based accrual rules, reward-tier redemption.
- **Smile.io** — self-serve e-commerce loyalty (points, VIP tiers, referrals) embedded in storefront platforms; action-driven earning with prebuilt member panels and checkout redemption.
- **Antavo** — enterprise standalone loyalty platform; full points economy (earning, pending, burn, expiry), tiers, gamification, workflow automation, fraud tooling, and marketing-stack integrations.
- **Open Loyalty** — headless/white-label loyalty engine; transaction ingestion, earning rules, levels, and reward campaigns exposed as an API-first platform for bespoke programs.
- **Stamp Me** — mobile digital punch-card platform for small physical businesses; stamps validated at the counter (app scan, NFC tap, QR), voucher redemption at stamp thresholds.

## Sources

Research date: **2026-09-08**

- Square — Loyalty Program overview and Create and Retrieve Loyalty Accounts (developer documentation): https://developer.squareup.com/docs/loyalty/overview , https://developer.squareup.com/docs/loyalty-api/loyalty-accounts
- Smile.io — Developer documentation home, index, and Concepts & fundamentals: https://docs.smile.io/ , https://dev.smile.io/llms.txt , https://dev.smile.io/guides/fundamentals.md
- Open Loyalty — Documentation home and User Guide: https://docs.openloyalty.io/ , https://docs.openloyalty.io/en/latest/userguide/index.html
- Antavo — Documentation portal, index, and Points economy: https://docs.antavo.com/ , https://docs.antavo.com/llms.txt , https://docs.antavo.com/docs/points-economy.md
- Stamp Me — How It Works: https://www.stampme.com/how-it-works

> Sourcing limitation: a sixth major e-commerce loyalty suite (Yotpo) could not be reached this pass (repeated transport errors / 404), so the e-commerce-suite pole rests on the self-serve and enterprise samples above. Enterprise loyalty suites that bundle gift-card programs (Paytronix/Givex-class) were likewise unreachable across this and prior sibling passes; loyalty–gift-card bundling is therefore treated as a packaging posture, not asserted as market structure. Claims about expiry windows, point valuations, and other numeric specifics are intentionally omitted — the sampled documentation supports the structures, not precise figures.
