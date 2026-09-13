# Gift Card Management

## Overview

A **Gift Card Management** application is the merchant-side system of record for a prepaid stored-value program: it issues and tracks gift cards — physical cards and digital codes — that a buyer purchases (often as a gift for someone else) and a holder later spends at the merchant's own selling channels.

The defining structure is small:

```text
Merchant-operated prepaid value program
└── Gift card = identified instrument (unique code or card number bound to a value balance)
    └── Issuance under the merchant's program (created/activated with value, program-configured)
        └── Redemption by balance drawdown at the merchant's channels
            └── Balance-activity record of every value movement over the card's life
```

A gift card is not a discount (it carries prepaid value rather than reducing a price), not loyalty points (its value is purchased, not earned), and not a bank product (the value is the merchant's own closed-loop obligation, not network-issued money). What the application manages is the *population of cards*: their balances, their validity, their transaction history, and the merchant's outstanding liability to cardholders.

## Users & Context

**Primary users (merchant side):**

- **Program administrator / marketer** — configures the program (card designs, denominations or custom-value rules, validity policy, terms), launches the online sale surface, and monitors performance.
- **Store staff / cashier** — sells cards in person, activates them, scans codes at redemption, handles top-ups and balance inquiries.
- **E-commerce operator** — embeds gift card sales in the online store and accepts them at checkout.
- **Finance / accounting** — owns the outstanding-liability view: sold-but-unredeemed value is deferred revenue the merchant owes back as goods and services, and it must be reported and reconciled.

**Secondary users (buyer/holder side):** the giver purchases and often schedules delivery of the card; the holder checks the balance and spends it, partially or fully, over one or many visits.

The work context spans the merchant's whole selling estate: online store, physical locations, and increasingly multi-location chains where a card bought in one place must spend anywhere in the program.

## Core Model

### The Defining Core

Four properties; remove any one and the product stops being gift card management:

- **Identified stored-value instrument.** Every card is a uniquely identified object — a card number, code, or account number — bound to a value balance. The identifier is what gets sold, delivered, scanned, and looked up. Without a balance on an identifier, you have coupon codes, not gift cards.
- **Program-governed issuance.** Cards do not float freely: they are created, activated, and loaded under the merchant's program, with the program defining what cards look like, what values they can carry, and under what terms they are valid. A card typically exists in the system before it carries spendable value — it is issued, then activated with its initial balance when sold.
- **Redemption by balance drawdown.** Spending a card reduces its balance. Partial redemption — spend part now, keep the remainder for later — is the standard semantic, and a card's life commonly consists of many small drawdowns rather than one.
- **Balance-activity record.** Every value movement — activation, load, redemption, adjustment, refund-to-card, clearing, deactivation — is recorded as a typed event against the card, forming an inspectable history. This is what makes balances auditable, disputes resolvable, and liability computable.

### Value Representation

The balance is overwhelmingly denominated in currency, but the concept generalizes: some products back a card in **units** of a service (nights, sessions, visits) instead of money, with whole-unit redemption semantics and correspondingly narrower redemption support. Concept and implementation separate cleanly:

```text
Concept:          Identified instrument + balance
Implementations:  plastic card with embossed/printed number, digital code in an email,
                  QR/barcode on a phone wallet pass, account number in a buyer profile

Concept:          Value
Implementations:  currency amount (any-amount drawdown), fixed denominations,
                  service units (whole-unit drawdown)
```

### Capabilities Mature Products Commonly Add

These are widespread in current products but not what makes the product a gift card system:

- **Two forms, one program** — physical cards (printed or plastic, with scannable barcode/QR) and digital cards (eGift delivered by email, printable or wallet-stored), sold through the same program and redeemable interchangeably.
- **Online sale surface** — a hosted order page or embeddable checkout widget where buyers choose a value (fixed denominations or a custom amount), a design, and a delivery date.
- **Holder-facing balance access** — a balance-check page or app where the holder can see the remaining value; optional card-on-file linking to the holder's customer profile at the merchant.
- **Reload / top-up** — adding value to an existing card, sometimes by the holder directly.
- **Refund-to-card** — refunds issued as gift card value, effectively a store-credit flow riding the same instrument.
- **Lifecycle operations** — voiding or disabling lost/stolen cards, undoing a mistaken redemption, resending digital deliveries, and (in some products) editing validity dates or combining several cards' balances.
- **Reporting** — sales, redemption activity (who and where), exports, and — treated as first-class in mature products — **outstanding liability**: the total unredeemed balance across all issued cards.
- **Integration surfaces** — APIs (and in some products webhooks) so checkout, POS, booking, and accounting systems can sell, redeem, and reconcile against the same card ledger.
- **Multi-location redemption** — one program spanning all of a merchant's locations.

## How It Works

### Configure the program

The administrator defines what the cards are before any card exists: designs (pre-made or custom artwork), the values buyers may choose (fixed denominations, buyer-chosen custom amounts, or service units), validity policy (whether cards expire, from when they are valid), terms and conditions, and the delivery options for digital cards. The program, not the individual card, carries most of this configuration.

### Sell and activate

```text
Buyer picks a card (value / design / delivery)
→ pays through the online checkout or at the POS
→ card is issued with a unique code
→ digital: delivered to the recipient (instant or scheduled); physical: handed over or shipped
→ card is activated with its initial balance — now live in the program
```

The sale and the activation are distinct events: many systems create the card record at purchase and give it spendable value at activation, which is what makes unsold physical card stock possible — cards exist in inventory, valueless until sold.

### Redeem

```text
Holder presents the code / card / phone pass
→ staff (or the checkout) validates it and reads the balance
→ purchase amount is drawn down — partially if the balance is smaller than the purchase
→ remaining balance stays on the card for future visits
→ holder can repeat until the balance reaches zero
```

Redemption may happen in person through a staff redemption app or POS terminal, or online by entering the code at checkout. Combined payment — card balance plus another payment method for the excess — is a supported flow in mature products.

### Keep value moving

- **Reload / top-up** adds value to a live card.
- **Refund-to-card** converts a returned purchase into card value (same card or a new one), keeping the money inside the merchant's program.
- **Adjustments** correct balances that are wrong for operational reasons — every adjustment is itself a recorded activity, and mistaken redemptions can be reversed.

### Handle lifecycle exceptions

- **Lost or stolen cards** are voided or deactivated so no further value movement can occur; digital deliveries can be resent.
- **Expiry** is a program decision, not a technical constant: many programs never expire their cards, others expire them after a set window or on a set date — and in several jurisdictions the law constrains, or forbids, expiry, so validity policy is a compliance surface, not just a marketing one.
- **Zero balance** is not the end of the record: the card's history remains, which is what allows refunds, disputes, and audit to reference it.

### Report and reconcile

Finance-facing views aggregate the card population: sold vs redeemed value, redemption locations, and outstanding liability. The liability number — total unredeemed balance — is the accounting heart of a gift card program: it is money the merchant has collected but not yet delivered value for.

## Interfaces

Exact layouts vary by product; conceptually the surfaces are:

### Program settings

Purpose: configure the program. Typical contents: card designs and artwork, value rules (denominations, custom value, units), validity and expiry policy, terms, delivery options, fee/plan settings. Primary actions: create/edit program rules, launch the online sale surface.

### Card list and card detail

Purpose: operate the population of issued cards. Typical information: card identifier, current balance, state (active/disabled/void), validity dates, linked customer if any. Primary actions: search and inspect a card, view its full activity history (activation, loads, redemptions, refunds, adjustments), adjust or undo, void/disable, edit validity, resend.

### Online sale surface (order site / checkout widget)

Purpose: the buyer- and giver-facing storefront for gift cards. Typical information: card designs, value choices, recipient email and delivery date, message. Primary actions: buy, schedule delivery, (where supported) check balance afterward.

### Staff / POS redemption surface

Purpose: validate and redeem cards in person. Typical information: scanned or keyed code, current balance, validity warnings. Primary actions: redeem an amount, partial redeem, top up, balance inquiry, undo recent redemption.

### Holder-facing surfaces

Purpose: let the recipient see and use their value. Typical information: delivered eGift (branded card image with code), balance, transaction history where offered. Primary actions: check balance, save to phone wallet, print.

### Reporting

Purpose: monitor the program and its liability. Typical information: sales, redemptions by location and time, outstanding liability, exportable data. Primary actions: filter, export, reconcile against accounting.

### API / webhooks

Not a page but a working surface for mature deployments: checkout, POS, booking, and finance systems sell, redeem, adjust, and listen for card events programmatically.

## Important Rules / Behaviors

**Drawdown-only, partial by default.** Redemption reduces the balance; a card cannot go negative, and partial redemption until zero is the standard behavior. Amounts below the balance leave residue on the card by design.

**Issue before value.** Cards commonly exist as records before they carry value (unsold physical stock, prepared digital codes). Activation with the initial balance is the gate that makes a card spendable; disabled or voided cards reverse that gate.

**Every movement is typed and reversible-in-principle.** Activations, loads, redemptions, refunds, and adjustments are distinct recorded events — the distinction matters because a refund-to-card must not look like a sale, and an operational adjustment must not look like a redemption. This event history is the basis for dispute resolution and audit.

**Validity is a policy, and a legal one.** Whether cards expire, from when, and whether staff may still honor an expired card are program decisions constrained by jurisdiction; several markets regulate gift card expiry. Enforcement strength can differ by channel (a staff member may see a warning where the online checkout hard-blocks).

**Refunds and credit share the instrument.** Refund-to-card turns the gift card into the merchant's store-credit vehicle; the same balance machinery serves purchased and refunded value, but the provenance of each amount is traceable in the activity record.

**The outstanding balance is a liability.** Sold-but-unredeemed value is money owed back as future purchases; mature products surface it as a report, and some platforms cap it per merchant as a risk control.

**Closed-loop by default.** The card's value spends only at the issuing merchant's program (its locations and online store) — that closure is what keeps the liability, the ledger, and the program configuration inside one system.

## Variants

- **POS-ecosystem embedded** — the gift card program is a module of a broader point-of-sale/commerce platform, sharing customer profiles, payments, and reporting with it.
- **Standalone embeddable** — an independent service whose entire product is the gift card checkout, delivery, and redemption machinery, slotted into any website or POS.
- **E-commerce wallet family** — gift cards offered alongside store credit, cashback, and rewards in one unified customer wallet, with gift cards as one provenance of a shared balance.
- **Service-unit cards** — value denominated in service units (stays, sessions, visits) rather than currency, with whole-unit redemption.
- **Bulk / corporate programs** — mass-generated codes for campaigns, employee incentives, and B2B gifting.
- **Expiry postures** — never-expiring (common as both default and legal posture), window-based, date-based, or deliberately short expiries used as a purchase motivator where law permits.
- **Physical-heavy vs digital-heavy** — programs built around ordered plastic card stock and in-store sales versus programs that never touch plastic.
- **Regional compliance shapes** — expiry legality, per-card and per-buyer load caps, and liability rules vary by market and shape the program's rule set.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Loyalty Program Management | value is earned through purchase behavior under accrual rules; gift card value is purchased and gifted. They meet where loyalty rewards are paid out as gift cards |
| Store Credit / Stored Value Platform | the same balance-drawdown machinery, but the value is what the merchant owes the customer (refunds, goodwill) rather than what a giver purchased; many products offer both from one ledger |
| Promotion Management | a promo code changes the price of a transaction; a gift card carries prepaid value consumed across transactions |
| Retail POS / E-commerce Platform | the surfaces where gift cards are sold and redeemed; the gift card system owns the instrument, the ledger, and the liability, and is usually packaged as a module of these platforms |
| Payment Processing / Card Issuing | a gift card acts as a payment method at the merchant, but the value stays inside the merchant's program; network-branded prepaid cards (Visa/Mastercard gift cards) are card-issuing products, outside this Type |
| Digital Wallet | consumer-side storage of value and passes; the merchant-side issuance, redemption, and liability record remains with this Type |
| Rewards & Incentive Distribution Platforms | distribute third-party brands' gift cards as corporate rewards through catalogs; they own no merchant card program or balance ledger |

## Representative Products

- **Square Gift Cards** — gift card program embedded in a POS/commerce ecosystem; physical and digital; card-as-payment, refunds-to-card, liability caps.
- **Gift Up!** — standalone embeddable gift card checkout for any website; currency- and unit-backed cards; configurable validity with channel-dependent enforcement.
- **Rise.ai** — gift cards and store credit unified in one customer wallet for e-commerce brands; bulk code generation; liability reporting.
- **Tango (Blackhawk Network)** — studied as a boundary anchor: third-party gift card catalog distribution and corporate rewards, owning no merchant card program.

The definition was checked against older and lower-technology forms: a paper gift certificate program — numbered certificates issued for value, verified and marked used at redemption, recorded in a register — satisfies the same core without plastic, emails, or APIs, which is why none of those appear in the defining structure.

## Sources

Research date: **2026-09-07**

- Square — Gift Cards product page: https://squareup.com/us/en/gift-cards
- Square — Gift Cards API and Gift Card Activities API guide: https://developer.squareup.com/docs/gift-cards/using-gift-cards-api
- Square — Gift Cards API reference: https://developer.squareup.com/reference/square/giftcards-api
- Gift Up! — product page: https://giftup.com/
- Gift Up! — Help Desk: https://help.giftup.com/ (gift card settings, redeeming gift cards, and reporting categories; currency vs unit-backed cards; expiry/validity rules; undo redemption)
- Rise.ai — https://www.rise.ai/ and https://rise.ai/solutions/gift-cards/
- Tango — https://www.tangocard.com/

> Sourcing limitation: Shopify, Givex, Toast, Clover, and Paytronix surfaces were unreachable from the research environment on 2026-09-07 (transport errors, access denials, or script-only pages), so no claims are made about those products; the enterprise closed-loop network pole and restaurant-vertical packaging are described structurally rather than from direct observation. Vendor performance claims are recorded as claims only. Numeric limits, fee schedules, and state-name specifics are intentionally omitted from this document and retained, where observed, in the Research Notes.
