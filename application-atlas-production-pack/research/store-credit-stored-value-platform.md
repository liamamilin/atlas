# Research Notes — Store Credit / Stored Value Platform

## Research Goal

Understand how real products implement merchant-side store credit / stored value: what the managed balance object is and how it attaches to customers, how value enters the balance (refund conversion, goodwill, top-up, campaigns), how redemption works as a payment method, what rules govern balances (expiry, cash-out, liability), and how this Type separates from Gift Card Management (processed §05.15 sibling), Loyalty Program Management (unprocessed §05.15 sibling), Returns platforms, promotion/coupon tools, consumer wallets, and B2B trade credit.

This pass also performs the joint review requested by the gift-card-management pass (2026-09-07), which recorded: "gift-card-management vs loyalty-program-management + store-credit-stored-value-platform (both unprocessed siblings): shared balance-drawdown machinery over an identified value instrument, different provenance of value — gift card = purchased by a giver under a merchant program, loyalty points = earned through behavior under accrual rules, store credit = owed by the merchant (refunds/goodwill); direct market evidence that the machinery is shared while issuance intent differs: Rise.ai explicitly merges gift cards, store credit, cashback and rewards into one customer wallet, and Square frames refunds-to-gift-card as store credit."

## Initial Boundary

Working hypothesis at start: Store Credit / Stored Value Platform is the merchant-operated program layer for customer-attached, closed-loop credit balances: issue value to a customer (refund-as-credit, goodwill, compensation, prepaid top-up) → hold it as a per-customer balance → redeem it as tender at the merchant's own channels → record every movement → report the outstanding liability. Expected packaging: platform-native (commerce/POS), app-layer wallet, coupon-mechanics implementations, enterprise closed-loop network.

Neighboring Types anticipated:
- Gift Card Management (§05.15 sibling, processed) — purchased transferable instrument vs customer-owed/held credit
- Loyalty Program Management (§05.15 sibling, unprocessed) — behavior-earned points vs issued/owed/deposited value
- Returns Management Platform — decides entitlement/orchestration; credit outcome executed elsewhere
- Promotion Management / coupon codes — price change vs prepaid value (note: coupon-based credit implementations live exactly on this seam)
- Retail POS / E-commerce Platform / Checkout — redemption surface and packaging substrate
- Credit Management Platform (§08) — B2B invoiced trade credit, not prepaid consumer value
- Digital Wallet / Stored Value Wallet (§08) — consumer-side, often open-loop/e-money
- Card Issuing / Payment Processing — network-branded prepaid vs merchant closed-loop
- Cashless Venue Platform (§26) / Campus Card Management (§23) — venue/campus prepaid balances with access/hardware context

## Research Questions

1. What is the managed object — a customer-account balance, an instrument code, a coupon, or a card? How does the balance attach to the customer?
2. How does value enter the balance? Which issuance loops exist (refund conversion, goodwill/compensation, manual send, customer purchase/top-up, campaign/bulk, automated triggers)?
3. How does redemption work — as tender at checkout/POS? Partial drawdown? Combined with other payment methods? Cross-channel?
4. Which rules matter — expiry/validity, cash-out prohibition, refund-of-credit, transferability, compliance caps, liability accounting?
5. What admin and reporting surfaces exist (adjustments, disable, history, outstanding liability)?
6. How do sampled products relate store credit to gift cards and loyalty inside the same product — shared ledger or separate objects?
7. Where is the seam against Gift Card Management and Loyalty Program Management, and does this leaf stand as an independent Type?

## Representative Products

| Product | Pole | Evidence level |
|---|---|---|
| Rise.ai | Dedicated "Gift Card & Store Credit Platform" — unified customer credit wallet for e-commerce brands; refund-automation center of gravity | Tier-2 (root + refunds solution page; help center unreachable) |
| Square Gift Cards | POS/payments-ecosystem instrument implementation; refund-to-gift-card explicitly framed by Square's own docs as "issuing store credit" | Tier-1 (developer docs fetched fresh; product page from sibling pass 2026-09-07) |
| Loop Returns | Boundary anchor: returns platform whose credit outcome is creating gift cards in the commerce platform; instant-credit posture | Tier-1 (docs: set-credit-type, process-return, index) |
| Smart Coupons for WooCommerce | Coupon-mechanics implementation: store credit as a monetary-balance coupon; open-source/self-host pole | Tier-1 (docs index + two targeted articles) |
| Givex (now Shift4) | Enterprise closed-loop network pole (gift cards, loyalty, cashless ticketing); structural context only | Tier-2 (landing page only; deep docs unfetchable) |

Rejected sample: Cashier for WooCommerce — documentation shows it is checkout-flow UX (Buy Now buttons), not credit management. Product mismatch recorded.

Unreachable after 1–2 attempts (source-access limitations recorded):
- Rise.ai Help Center (help.rise.ai and help.rise.ai/en/ — 403 ×2 on 2026-09-08). Rise evidence stays product-page level.
- Shopify Help Center (help.shopify.com — 403 ×2 across 2026-09-07 and 2026-09-08). Platform-native store credit is NOT directly observed; no claims made about Shopify specifics.

## Sources

- Rise.ai — https://rise.ai/ — fetched 2026-09-08
- Rise.ai — https://rise.ai/solutions/refunds/ — fetched 2026-09-08
- Rise.ai — https://rise.ai/solutions/gift-cards/ — fetched 2026-09-07 (gift-card-management pass)
- Square — https://developer.squareup.com/docs/gift-cards/using-gift-cards-api — fetched 2026-09-08
- Square — https://squareup.com/us/en/gift-cards — fetched 2026-09-07 (gift-card-management pass)
- Square — https://developer.squareup.com/reference/square/giftcards-api — fetched 2026-09-07 (gift-card-management pass)
- Loop Returns — https://docs.loopreturns.com/llms.txt (documentation index) — fetched 2026-09-08
- Loop Returns — https://docs.loopreturns.com/api-reference/latest/draft-returns/set-credit-type.md — fetched 2026-09-08
- Loop Returns — https://docs.loopreturns.com/api-reference/latest/return-actions/process-return.md — fetched 2026-09-08
- Smart Coupons for WooCommerce — https://woocommerce.com/document/smart-coupons/ — fetched 2026-09-08
- Smart Coupons for WooCommerce — https://woocommerce.com/document/smart-coupons/how-to-provide-store-credit-for-a-refund/ — fetched 2026-09-08
- Smart Coupons for WooCommerce — https://woocommerce.com/document/smart-coupons/how-to-sell-gift-card-of-any-amount/ — fetched 2026-09-08
- Givex / Shift4 — https://web.givex.com/ — fetched 2026-09-08
- Gift Up! help-center evidence (expiry jurisdiction rules, currency/unit backing) reused from the gift-card-management pass (fetched 2026-09-07, sources recorded there)

## Product Observations

### Rise.ai (evidence layer A for product-page claims; no help-center depth)

**Positioning.** "Gift Card & Store Credit Platform." Store credit is the umbrella frame: "One Wallet, for Everything Store Credit — Store Credit, Gift Cards, and Cashback — ALL in one place."

**Provenance menu (issuance intents).** Nine solution lines, all landing in the same wallet: Gift Cards, Refunds ("Convert Refunds to Sales Opportunities"), Cashback ("Spend & Earn"), Memberships, Loyalty Programs ("Skip the Points – Real Currency, True Loyalty"), Employee Recognition, Compensation ("Instantly Transform Mistakes into Loyalty"), Referrals, B2B. The loyalty line's own positioning — real currency instead of points — is direct market evidence for the loyalty/store-credit seam.

**Refund-to-credit machinery.** "Move from Cash to Store Credit Refunds." "One Wallet for All Store Credit Refunds." Opt-ins: "Offer customers a percentage boost on their refund value in store credit, with merchant-friendly expiry options — easily automate conditions and workflows." "Plug-n-Play with Your Returns Providers — connect Rise.ai seamlessly with any refund or returns system; trigger automated Store Credit compensations." Explicit integration story with Loop Returns (blog: "Integrating Rise.ai & Loop Returns").

**Enterprise features.** Liability Reporting & ERPs ("real-time insights to manage Gift Card and Store Credit liabilities"), APIs, headless customization, multi-store & omnichannel ("unify your brand's sales channels for cohesive issuance and redemption management"), Bulk Create ("generate up to 10,000 gift card codes instantly for targeted campaigns" — product-specific number kept as claim), Custom Triggers ("set automated triggers from any source to issue Store Credit based on any user event"). In-store beta ("retention beyond the storefront").

**Claims (marketing, recorded as claims only).** 2023 benchmarks (32% repeat purchase rate, 18% AOV, 40% redemption rate, 8% CLV); refund-page benchmarks (retain up to 30% more revenue; 10K+ credit refunds issued; 40% of credits redeemed; 300% upsell on redeemed credits); case-study claims (Kosas: short expiration period as second-purchase motivator).

### Square (evidence layer A — developer docs fetched fresh 2026-09-08; product page via sibling pass)

**Store-credit linkage is explicit in Square's own docs.** Gift card `id` serves as `destination_id` "when issuing store credit in a `CreateRefund` request. This is an alternative method for activating a gift card." Refund-to-a-new-gift-card: create the card then refund to it — the card auto-activates (PENDING → ACTIVE) with the refund as initial balance; "refunding to a new gift card activates the card... creates a REFUND activity but doesn't create an ACTIVATE activity."

**Refund activity taxonomy (provenance typing).** `REFUND` = "adds money to a gift card from a refunded transaction" (same-method, carries `redeem_activity_id`; cross-method via Refunds API); `UNLINKED_ACTIVITY_REFUND` = cross-method refund where the original payment wasn't the same card; `ADJUST_INCREMENT` = "increases a gift card balance when the adjustment isn't related to a gift card order or payment" (the goodwill/manual-credit slot); `ADJUST_DECREMENT` with reason `PURCHASE_WAS_REFUNDED` for reversing a credit issuance; `ACTIVATE`/`LOAD`/`REDEEM`/`CLEAR_BALANCE`/`DEACTIVATE` complete the lifecycle. Typed provenance matters: a refund-credit must not look like a sale, an adjustment must not look like a redemption.

**Tender mechanics.** Gift card payment: `card_brand` = `SQUARE_GIFT_CARD`; "Square supports partial payment flows using gift cards." Redeemable at all seller locations, in person (POS) and online (Square Online). Cards link to customer profiles ("gift cards on file", link/unlink; product-specific limits: 50 cards per customer, 10 customers per card). Buyers manage cards from their Square profile; sellers via Square Point of Sale and Dashboard. No expiration (US FAQ, sibling pass).

**Liability controls.** Compliance limits enforced on value-loading: max balance per card, max load per card/day, max load per payment card/day, and **maximum outstanding balance per seller** — the per-merchant liability cap ("The merchant cannot accrue any more liability"). Per-country limit tables exist (numbers kept in L3). Load fees apply to value-loading activities (ACTIVATE/LOAD/ADJUST_INCREMENT), not to redemption or refund.

### Loop Returns (evidence layer A — docs fetched 2026-09-08)

**Credit as a returns outcome, not a balance system.** The returns flow exposes a customer choice "Choose how to receive the refund": `credit_type` enum = `refund` | `gift` | `exchange`. Processing a return "will archive it in Loop and fulfill any remaining outcomes, such as placing exchange orders or creating gift cards." I.e., when the customer picks gift/credit, Loop's fulfillment act is creating a gift card in the commerce provider — the balance machinery and redemption live in the commerce platform (or an app like Rise), not in Loop.

**Instant credit posture.** `processing_type` = `regular` | `instant`; a "Reshop instant-refund credit" can exist while the return is still open — processing is intentionally skipped for such returns ("a successful (true) response is returned without dispatching any processing jobs"). Instant credit = value issued before the returned goods arrive; a distinct risk posture the merchant opts into.

**Boundary anchor use.** Loop owns entitlement (eligibility, reasons, fraud flags, allow/block lists, grading/disposition) and orchestration (exchanges, shop-now carts, labels); the credit balance is downstream. This is the cleanest observed demonstration that Returns Management and Store Credit are different Types that integrate.

### Smart Coupons for WooCommerce (evidence layer A — docs fetched 2026-09-08)

**Definitional quote.** "A store credit or gift certificate is a monetary value assigned as a credit to the customer. So the customer can use that credit all at once or multiple times to make purchases until the credit is exhausted or its validity expires. If the available store credit balance is less than the total amount to be paid, the remaining amount can be paid using other payment methods." Also: "The WooCommerce gift card/store credit functionality... is different from how normal coupon codes work. A gift card is treated as real credit / money — very much like a prepaid credit card."

**Implementation substrate.** Store credit is implemented as a coupon of a special discount type ("Store Credit/Gift Certificate") carrying a monetary balance, with no usage limit so it can be redeemed repeatedly until exhausted or expired. The credit code is emailed to the customer. This shows the same Type can be realized on top of a promotion engine — the balance semantics, not the plumbing, make it store credit.

**Issuance loops.** (1) Refund conversion: after processing a WooCommerce refund, merchant uses Marketing > Coupons > "Send Store Credit" tab → customer email + Worth (amount) + optional Expiry Date + message → credit emailed. (2) Purchasable credit: customer buys store credit/gift card of any amount (coupon value = product price), fixed amounts, or fixed denominations; can "send to me" or "gift to someone else" — the same object serves purchased-gift and merchant-issued credit intent. (3) Scheduled delivery of credit. (4) Physical printed vouchers.

**Redemption & rules.** Applied at cart/checkout as payment; remainder payable by other methods; setting "Deduct store credit before applying tax" (tax-timing policy); balance display anywhere via shortcode; terminology renamable ("How to rename 'Store Credit/Gift Certificate'"); customer-facing "My Account" coupon/credit page. Fraud rule documented by the vendor: if a discount coupon can be applied to the credit-purchase product, customers could repeatedly buy real credit at a discount — a usage-limit interplay specific to the coupon substrate.

### Givex / Shift4 (evidence layer A-lite — landing page only; treated structurally)

Enterprise closed-loop engagement network (founded 1999; acquired by Shift4): product lines Gift Cards ("create your own branded mobile wallet"), Loyalty Programs, Rewards, Uptix Ticketing ("cashless concessions and in-game promotions" — venue stored value), Payments, Kiosk & Self-Service, Analytics; 24/7 client services, 1,000+ APIs, global multi-location scale (clients include 7-Eleven, Marriott, Tesco, M&S). Deep gift/stored-value documentation remains unfetchable (403 in the 2026-09-07 pass; the current site is a rebrand landing). Used only for the enterprise pole's shape: stored-value machinery sold as a network service with physical card production, multi-brand wallets, and venue cashless variants. No operational specifics asserted.

### Reused sibling evidence (recorded in gift-card-management pass, 2026-09-07)

- Gift Up!: currency-backed vs unit-backed cards; validity/expiry policies with jurisdiction rules (US CARD Act, Canadian prepaid legislation, EU/Irish 2019, UK, AU 2018, NZ) and channel-dependent enforcement strength.
- Rise.ai gift-card solution page: unified wallet, liability reporting, bulk codes.
- Square product page frames refunds-to-gift-card as "an easy way to offer store credit."

## Cross-product Comparison

| Dimension | Rise.ai | Square | Loop Returns | Smart Coupons (Woo) | Givex (structural) |
|---|---|---|---|---|---|
| Managed object | Customer credit wallet (unified: gift cards, credit, cashback) | Gift-card instrument (GAN + balance + state) linked to customer profiles | (none — issues gift cards as returns outcome) | Coupon object with monetary balance, attributed to customer email | Closed-loop card/account on enterprise network |
| Balance attachment | Customer wallet | Card on file → customer profile; or unlinked card | Customer receives commerce-platform gift card | Coupon code emailed to / purchasable by customer | Card/account held by consumer |
| Issuance loops | Refund automations, opt-in boosts, custom triggers, bulk campaigns, compensation, referral, B2B | Refund / cross-method refund to new card (= store credit), ADJUST_INCREMENT, LOAD | Credit-type choice at return; instant or on-processing credit | Send Store Credit tab (refund/goodwill), purchasable credit, scheduled delivery | Card issuance/sale (deep docs unavailable) |
| Redemption | Storefront one-click apply/tap; POS + multi-store (in-store beta) | POS + Square Online; partial payments; all locations | (at commerce checkout via the created gift card) | Cart/checkout coupon application; remainder by other methods | Merchant network locations |
| Expiry | "Merchant-friendly expiry options"; short expiry used as motivator (case study) | None (US FAQ) | (inherits commerce-platform card policy) | Optional expiry date per issuance; validity expiry semantics in definition | Unknown (not fetched) |
| Liability view | Liability reporting & ERPs (gift card + store credit) | Per-seller outstanding-balance compliance cap; Dashboard reporting | N/A | Not observed as dedicated report (coupon logs exist) | Not observed |
| Provenance typing | Provenance = solution line (refunds/cashback/compensation/...) | Typed activities (REFUND vs ADJUST vs LOAD vs REDEEM) | credit_type enum refund/gift/exchange | Coupon-generation context (sent/received details) | Unknown |
| Loyalty relationship | "Skip the points — real currency" (explicit seam) | Separate Loyalty API (points, accrual, rewards) distinct from Gift Cards API | N/A | Separate from discount coupons (balance vs price-off) | Loyalty as separate product line |
| Packaging | Standalone wallet platform on commerce platform | POS/payments-suite module | Returns platform (integration partner) | Commerce extension (coupon substrate) | Enterprise network suite |

**Convergent findings (B — cross-product commonality):**
1. The managed value is a currency-denominated, closed-loop balance that attaches to an identified customer relationship — as a wallet, a customer-linked instrument, or a customer-attributed code.
2. Value enters only through governed issuance events whose provenance is distinguishable: refund conversion, goodwill/compensation, merchant manual send, customer purchase/top-up, campaign issue. Every sampled implementation keeps refund-credit distinct from ordinary sales activity in its records.
3. Redemption is a tender drawdown at the merchant's own channels: partial redemption until zero, remainder payable by other methods, reusable across visits/orders.
4. Every value movement is recorded (issuance, redemption, adjustment, refund); mature products expose per-balance histories and an outstanding-liability view or cap.
5. Refund-to-credit is the flagship flow — it is the one issuance loop present in every directly observed implementation, and the one the vendors lead with.
6. Expiry is a policy surface (optional per issuance, programmatic, or absent), with jurisdiction constraints known from the sibling pass; incentive expiry (short windows as a purchase motivator) appears as a deliberate posture.
7. Loyalty and store credit are kept distinct inside the same vendors' products (Square: separate Loyalty API vs Gift Cards API; Rise: "skip the points — real currency"; Smart Coupons: credit coupon vs discount coupon).

**Divergent findings:** attachment substrate (wallet vs card instrument vs coupon code); whether purchased/gifted value shares the same balance object as owed value (Rise and Smart Coupons: yes, one object/wallet; Square: same instrument, provenance typed; Loop: outsourced); transferability (customer-bound vs giftable); instant-credit appetite (Loop/Rise market it; risk posture is merchant choice); liability reporting depth (first-class in Square/Rise, not observed in Smart Coupons); fee models.

## Abstraction Levels

### L0 — Defining Invariant

```text
Merchant-operated closed-loop customer credit program
└── Customer credit balance of record
    (currency balance held against an identified customer relationship
     or a customer-held code/instrument the program attributes to that customer)
    └── Merchant-governed issuance of value into the balance
        (refund conversion, goodwill/compensation, manual send, customer
         purchase/top-up, campaign issue — each a governed, provenance-typed event)
        └── Redemption as tender at the merchant's own channels
            (drawdown of the balance as payment; partial redemption and
             combination with other payment methods)
            └── Balance-activity record
                (typed value movements over the balance's life —
                 the audit and liability basis)
```

Removal tests:
- No customer-attached balance of record → one-off promotional vouchers or refund memos; the "value the customer carries with the merchant" is gone.
- No merchant-governed issuance (policy-controlled, provenance-typed value entry) → a plain prepaid payment account or customer-money ledger; the program layer is gone.
- No redemption-as-tender → refund accounting or a rewards catalog (loyalty territory); the value is not spendable money at the merchant.
- No balance-activity record → balances without audit, dispute, or liability computation; "management" is gone.

**Historical / market-sample check (§24 reasoning):** the paper-era merchandise credit slip satisfies the core — a store issues a credit slip on a return under store policy (governed issuance), the slip/ledger line records the credit (balance of record + record), the customer presents the slip at the register and the store marks its use as payment for goods (tender drawdown), the credit is non-cashable and typically bound to the store. Pre-software customer deposit accounts (e.g., house "milk money" style deposit books) satisfy it from the customer-funded side. Neither plastic cards, wallets, emails, nor APIs are part of the definition — the modern digital wallet is one substrate among several.

### L1 — Common Mature Structure

- Refund-to-credit as a first-class flow, including automated returns-provider integration and opt-in incentives (boost percentages on taking credit over cash)
- Customer-facing balance surface: wallet in the store account, emailed credit code, balance display, redemption history
- Checkout application as a payment method: one-click apply or code entry; partial drawdown; combined payment for the excess
- Expiry/validity policy machinery (per-issuance or programmatic), constrained by jurisdiction
- Manual merchant issuance and adjustments (goodwill/compensation) as distinct typed events
- Multi-provenance wallet unification (refunds + cashback + compensation + referrals + memberships + employee recognition + B2B incentives in one balance)
- Admin operations over the balance population: search/inspect, adjust, disable/void, resend credit
- Bulk issuance for campaigns/segments/employees
- Outstanding-liability reporting (and in some products, liability caps as risk control)
- Returns-platform and checkout integration; APIs/webhooks
- Multi-location / multi-store redemption within the program; in-store (POS) redemption alongside online

### L2 — Variant / Optional Structure

- Attachment substrate: customer-account wallet vs emailed code vs customer-linked card instrument vs coupon-code object (the Type is substrate-independent)
- Provenance mix: refunds-only posture vs full credit wallet with many issuance intents
- Instant credit (issued before returned goods arrive) as a merchant-chosen risk posture
- Transferability posture: customer-bound by default vs giftable/forwardable at issuance
- Expiry posture: never vs window vs fixed date vs deliberately short incentive expiry (lawfulness varies by jurisdiction)
- Value backing: currency dominant; unit/service credit exists in the wider stored-value family (sibling-pass evidence: unit-backed gift cards)
- Channel realization: e-commerce-first vs omnichannel (POS + online) vs enterprise multi-brand network
- Regional compliance shapes: per-card/per-seller caps, load-fee regimes, expiry legality
- Audience extensions: employee recognition, B2B/incentive credit
- Fee/business models: subscription app tiers, load fees, per-transaction fees

### L3 — Vendor-specific (research notes only)

- Square: GAN structure (physical 778273, digital 778332 BIN prefixes), `sqgc://` URI scheme, Luhn + numeric-only custom-GAN rules for scanning, custom GANs enabling cross-seller redemption and ticket-value attachment, 2.5% load fee (US/CA/AU) on ACTIVATE/LOAD/ADJUST_INCREMENT, per-country compliance-limit tables (e.g., $2,000 max balance US/AU/CA; ¥10,000,000 per-seller cap JP; reload-forbidden €250 cards ES), 50-card/10-customer link limits, activity-type vocabulary (UNLINKED_ACTIVITY_REFUND, TRANSFER_BALANCE_TO/FROM, IMPORT via Support), auto-unlink of customers at zero balance, no-expiration US posture, March 2016 activity-history cutoff.
- Rise.ai: one-wallet multi-product framing, 16-digit codes (product-specific), 10,000-code bulk generation, custom triggers from any user event, in-store beta, benchmark claims (32% repeat purchase, 40% redemption, 300% upsell on redeemed credits, 30% revenue retention — vendor claims), brand customers (Skims, Kroger, Miami Heat, Dr. Squatch, Milk Bar, Kosas, Bokksu).
- Loop Returns: `credit_type` enum (refund/gift/exchange), `processing_type` regular/instant, "Reshop instant-refund credit" naming, process-return semantics (queued processing, return.closed / return.processing.failed webhooks, UNPROCESSABLE_FLAGGED_RETURN error class), gift-card creation as the credit fulfillment outcome.
- Smart Coupons: store-credit-as-coupon substrate ("Store Credit/Gift Certificate" discount type, coupon value = product price for purchasable credit, no usage limit for reusable credit), Send Store Credit tab fields (email/worth/expiry/message), "Deduct store credit before applying tax" setting, balance shortcode, renamable terminology, usage-limit fraud interplay, recipient form on product page (version 9.65.0+).
- Givex/Shift4: Uptix venue cashless ticketing; branded mobile wallet framing; 1,000+ APIs; 24/7 support; client logos.

## Vendor-specific Findings

See L3. Cross-cutting vendor observations that must NOT enter the canonical model: Square's refunds-to-gift-card-as-store-credit framing is one vendor's naming of the flow; Rise's wallet unification is a philosophy (Gift Up!/Square-class products keep gift value and other money more separate); Smart Coupons' coupon substrate is one implementation, not the definition; Loop has no balance system at all — it is the integration counterparty.

## Rejected Findings

- "Store credit is only refund-credit" — rejected: sampled products issue credit for goodwill/compensation, referrals, employee recognition, B2B incentives, cashback, and customer purchase; refund conversion is the flagship loop, not the whole Type.
- "Store credit must be non-transferable" — rejected as absolute: Smart Coupons lets purchased credit be gifted at issuance; Square custom GANs enable cross-merchant scenarios. Default posture (customer-bound) is common; transfer-at-issuance exists.
- "Store credit is a Shopify/plus-tier feature" — rejected: not observed (Shopify unfetchable), and the coupon-substrate and POS-instrument implementations show the Type does not depend on any one platform's native primitive.
- "Wallet unification (gift cards + credit + cashback in one balance) is definitional" — rejected to L2: it is Rise's philosophy; other products keep provenances typed within one object or keep objects separate.
- "Instant credit is definitional" — rejected to L2: it is a risk posture offered around returns integration, not present in all implementations.
- "Store credit belongs with B2B trade credit (Credit Management Platform)" — rejected: different object entirely (invoiced receivables vs prepaid closed-loop customer value). Seam recorded in boundaries.
- "Cashier for WooCommerce belongs in the sample" — rejected: documentation shows checkout-UX features (Buy Now), no credit management. Product mismatch.

## Boundary Findings

| Nearby Type | Seam | Removal test |
|---|---|---|
| Gift Card Management (§05.15, processed) | Same balance-drawdown machinery, different object intent: store credit = value the merchant owes or holds for a specific customer (refunds, goodwill, deposits), attached to that customer by default, typically non-transferable; gift card = purchased instrument meant to be given/forwarded, instrument-centric. Market blur is real and systematic: Square implements store credit *through* the gift-card instrument (its docs call refund-to-card "issuing store credit"); Smart Coupons sells "gift cards" that are literally store credit; Rise merges both in one wallet. | If value only ever enters as merchant-owed/deposited customer value and the balance stays with the customer, it is store credit; the purchased-giver-recipient gifting flow is the gift-card marker. |
| Loyalty Program Management (§05.15, unprocessed) | Provenance and spend grammar: loyalty value is earned through purchase behavior under accrual rules and typically redeemed against a rewards catalog; store credit is issued/owed/deposited currency value spent as tender. Meeting point: cashback/rewards paid out as credit (Rise's "skip the points — real currency" positioning is explicit market evidence of the seam; Square ships Loyalty and Gift Cards as separate APIs). | Remove earning/accrual and the reward catalog from loyalty and what remains may be a credit balance; make credit earned-by-behavior and catalog-bound and it becomes points. |
| Returns Management Platform | Loop owns entitlement/orchestration (eligibility, reasons, fraud, grading) and its credit outcome is *creating gift cards* in the commerce platform or triggering an app like Rise; the credit platform owns the balance, tender, and ledger. | Remove the balance/tender machinery from a returns platform and it still returns goods; remove return orchestration from a credit platform and it still holds value. |
| Promotion Management / coupon codes | A discount coupon changes a transaction's price; store credit carries prepaid value consumed across transactions. Smart Coupons demonstrates the seam precisely: credit is implemented *as* a coupon type but defined by balance semantics ("treated as real credit / money... like a prepaid credit card"), with vendors documenting the difference from "normal coupon codes." | No balance → promotion. |
| Retail POS / E-commerce Platform / Checkout | Redemption and application happen inside those surfaces; the credit platform owns the instrument/balance, program, ledger, and liability. Packaging is usually embedded. | Remove the credit program and the store still sells; remove checkout/POS and the credit platform still manages value. |
| Credit Management Platform (§08) | B2B trade credit = invoiced, post-sale receivable exposure governed by limits; store credit = prepaid/owed closed-loop consumer value spent as tender. Shared word "credit," different world. | Trade credit has no prepaid balance and no tender drawdown; it accumulates receivables. |
| Digital Wallet / Stored Value Wallet (§08) | Consumer-side, general-purpose (often open-loop, regulated e-money) vs merchant-side closed-loop program. The consumer-facing wallet surface of a credit program is UX, not the system of record. | Value spends anywhere → wallet; value spends only at the issuing merchant's channels → this Type. |
| Card Issuing / Payment Processing | The credit balance may act as a payment method (Square: SQUARE_GIFT_CARD brand), but settlement stays inside the merchant program; network-branded prepaid is issuing territory. | Bank-issued network instrument → issuing. |
| Cashless Venue Platform (§26) / Campus Card (§23) | Venue/campus prepaid balances bound to a venue/campus context (access, hardware, consumption); store credit is general merchant credit. Givex's Uptix (cashless concessions) sits in that neighborhood. | Venue-bound consumption context with access control → venue/campus Types. |

**Joint review resolution (from this side) for the gift-card-management recommendation:** keep-both RATIFIED. The machinery (balance, drawdown, activity record, liability) is shared and the packaging overlaps heavily, but the market sustainably distinguishes the two: dedicated gift-card-only products exist (Gift Up! class), dedicated credit-wallet positioning exists (Rise), the two §05.15 leaves answer different merchant jobs (gifting programs vs refund/retention policy), and this pass found the same seams from the credit side that the gift-card pass found from its side. Loyalty Program Management remains unprocessed; its joint review (points vs value) is pending on that side — noted for STATUS.md.

## Uncertainties

- Rise.ai mechanics (balance states, exact issuance operations, expiry behavior) rest on product-page evidence only; help center unreachable (403 ×2). Rise-specific claims are lower confidence; none of them were promoted to the canonical model.
- Platform-native commerce implementations (Shopify-class) could not be observed (help center 403 ×2 across two passes). Rise's positioning as a Shopify app and Loop's gift-card-creation outcome weakly imply a native gift-card/store-credit primitive exists there, but no specifics are asserted.
- Enterprise closed-loop network pole (Givex-class) described structurally only; deep documentation unfetchable across both passes.
- Escheatment/breakage accounting depth beyond liability reporting was not directly observed in this pass's sample; kept as an uncertainty rather than asserted.
- Whether any product lets customers cash out remaining credit (legal regimes sometimes require it) was not observed; the sampled posture is spend-only.
- Tax-treatment variance (credit issued vs redeemed timing) observed only as Smart Coupons' deduct-before-tax setting; broader treatment unknown.

## Final Synthesis

Store Credit / Stored Value Platform is the merchant-side system of record for closed-loop customer credit. Its defining core is small and jointly held: a currency balance of record attached to an identified customer relationship (as a wallet, a customer-held code, or a customer-linked instrument); merchant-governed issuance of value into that balance with typed provenance (refund conversion being the flagship loop, alongside goodwill, manual sends, customer top-ups, and campaign issue); redemption of the balance as tender at the merchant's own channels with partial drawdown and combined payment; and a balance-activity record that makes the balance auditable and the merchant's outstanding liability computable. Mature products add refund-to-credit automation with opt-in incentives, customer wallets, expiry policy machinery, multi-provenance wallet unification, bulk issuance, liability reporting, and returns-platform integration. The Type is substrate-independent — realized as dedicated wallet platforms, POS/commerce instruments, coupon-based credit, and enterprise closed-loop networks — and is usually packaged inside commerce/POS platforms or as an app layer on them. Its boundaries are held by provenance and spend grammar: purchased-and-giftable instruments (gift cards), behavior-earned points (loyalty), price changes (promotions), returns orchestration (returns platforms), invoiced receivables (trade credit), and consumer-side general-purpose wallets are all different Types, even where the underlying ledger machinery resembles this one.
