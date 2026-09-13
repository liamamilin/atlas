# Research Notes — Gift Card Management

## Research Goal

Understand how real products implement merchant-side gift card programs: what the managed object is, how cards are issued/sold, how redemption draws down balances, what lifecycle and rules exist, what reporting (especially liability) looks like, and how this Type separates from loyalty points, store credit, promo codes, card issuing, consumer wallets, and rewards distribution platforms.

## Initial Boundary

Working hypothesis at start: Gift Card Management is the merchant-operated program layer for prepaid stored-value instruments (physical cards, digital codes/eGifts): configure the program → issue/sell cards → track balances → redeem by drawdown across channels → manage lifecycle (reload, refund-to-card, void, expiry) → report on sales/redemptions and outstanding liability.

Neighboring Types anticipated:
- Loyalty Program Management (earned points vs purchased value)
- Store Credit / Stored Value Platform (merchant-owed credit vs purchased gift)
- Retail POS / Checkout / E-commerce Platform (sale and redemption surfaces)
- Payment Processing / Card Issuing (gift card as payment method; open-loop network prepaid)
- Digital Wallet (consumer-side holding)
- Promotion Management (price reduction vs stored value)
- Rewards & incentive distribution platforms (third-party catalog distribution)

## Research Questions

1. What is the managed object (card/code/balance) and what states does it move through?
2. How is a program configured (forms, denominations/custom value, designs, code format, validity, terms)?
3. Through which channels are cards sold/issued (online order site, POS, API, bulk/corporate)?
4. How does redemption work (partial redemption, balance check, cross-channel, top-up, combine, undo)?
5. Which rules matter (expiry/valid-from, jurisdiction limits, fees, fraud controls, compliance caps)?
6. What reporting exists (sales, redemption, liability/breakage, exports)?
7. How do sampled products relate gift cards to store credit, refunds, and loyalty in the same product?

## Representative Products

| Product | Pole | Evidence level |
|---|---|---|
| Square Gift Cards | POS-ecosystem embedded program; SMB → multi-location; physical + digital | Tier-1 (product page + developer guide + API reference) |
| Gift Up! | Standalone self-serve "gift card checkout for any website"; per-transaction business model | Tier-1 (product page + help center: settings, redemption, reporting, undo articles) |
| Rise.ai | E-commerce brand platform; gift cards inside a store-credit wallet family; enterprise features | Tier-2 (root + gift-cards solution page) |
| Tango (Blackhawk Network) | Boundary context: third-party gift card catalog distribution + corporate rewards, not own-program management | Tier-2 (root page) |

Unreachable after 1–2 attempts (recorded as source-access limitations): Shopify (help.shopify.com and shopify.dev transport errors ×2), Givex (403 ×2), Toast (404 + 403), Clover (JS-only shell), Paytronix (404). No claims are made for these products.

## Sources

- Square — https://squareup.com/us/en/gift-cards (product page) — fetched 2026-09-07
- Square — https://developer.squareup.com/docs/gift-cards/using-gift-cards-api (Gift Cards API & Gift Card Activities API guide) — fetched 2026-09-07
- Square — https://developer.squareup.com/reference/square/giftcards-api (API reference) — fetched 2026-09-07
- Gift Up! — https://giftup.com/ (product page) — fetched 2026-09-07
- Gift Up! — https://help.giftup.com/ (help index), /category/104-settings-you-can-apply, /category/13-how-to-redeem-gift-cards, /category/183-reporting, /article/181-currency-vs-unit-backed-gift-cards, /article/105-specifying-expiry-dates-on-gift-cards, /article/224-how-to-undo-a-redemption — fetched 2026-09-07
- Rise.ai — https://www.rise.ai/ and https://rise.ai/solutions/gift-cards/ — fetched 2026-09-07
- Tango — https://www.tangocard.com/ — fetched 2026-09-07

## Product Observations

### Square Gift Cards (evidence layer A — directly observed)

**Object & states.** A gift card is `DIGITAL` or `PHYSICAL`. Newly created cards are in a `PENDING` state with zero balance; an `ACTIVATE` activity with an initial balance moves the card to `ACTIVE`; only `ACTIVE` cards support other activities. `DEACTIVATE` "permanently blocks a gift card from any future balance-changing activities" (lost/stolen/disposal). `CLEAR_BALANCE` zeroes a card (used before reusing a physical card). Buyer-side: buyers view and manage gift cards from their Square profile; sellers work in Square Point of Sale and the Square Dashboard.

**Identity.** Cards carry a GAN (gift card account number), Square-assigned or custom (unique per seller, 8–20 alphanumeric, must not collide with major card BINs; numeric-only + Luhn for QR/barcode scanning; `sqgc://` URI scheme). Custom GANs enable "gift card redemptions across multiple Square sellers and channels", attaching value to tickets, and accepting cards from external sites. Physical cards are imprinted with a 16-digit GAN + barcode and QR.

**Balance-activity ledger.** Gift Card Activities API defines typed activities: ACTIVATE, LOAD, REDEEM, CLEAR_BALANCE, DEACTIVATE, ADJUST_INCREMENT, ADJUST_DECREMENT, REFUND, UNLINKED_ACTIVITY_REFUND, plus system-managed BLOCK/UNBLOCK (chargeback processing), IMPORT/IMPORT_REVERSAL (third-party import via Square Support), TRANSFER_BALANCE_TO/FROM (buyer transfers between cards linked to their profile). Every activity carries gift_card_balance_money; ListGiftCardActivities exposes history; webhooks notify on activity/updated. ADJUST types exist precisely for balance changes not tied to a gift card order/payment.

**Sale & issuance channels.** Digital: seller publishes an eGift Card Order Site; developer must deliver digital-card information when issuing via API. Physical: seller orders card packs (third-party printer link) beforehand; cards must be unused to sell. Orders integration: selling = CreateOrder → CreatePayment → CreateGiftCard → ACTIVATE with order_id + GIFT_CARD line item. Third-party gift cards (bought from another provider previously) can be imported once via Support and then redeemed like Square cards, but cannot be reloaded.

**Redemption.** Redeemable at all seller locations (multi-location), in person at Square POS and online at Square Online; scannable QR/barcodes; cards can be saved to a customer profile ("card on file", link/unlink customers; product-specific link limits 50 cards/customer, 10 customers/card). Gift card is a payment method: card_brand SQUARE_GIFT_CARD; partial payment flows supported. Refunds: same-method refund to the same card (REFUND), cross-method refund to a card (REFUND/UNLINKED_ACTIVITY_REFUND), refund to a *new* gift card (activates it, PENDING→ACTIVE) — the merchant-facing product page frames refunds to gift cards as "an easy way to offer store credit".

**Rules & controls.** Country compliance limits: max balance per card, max load per card/day, max load per payment card/day, max outstanding balance per seller (error message: "The merchant cannot accrue any more liability"). Load fees of 2.5% in US/CA/AU on ACTIVATE/LOAD/ADJUST_INCREMENT (no fee on redemption or refund). No expiration (US FAQ). Auto-unlink of linked customers when a physical card hits zero balance. Security guidance for custom GANs (avoid guessable patterns).

**Reporting.** Square Dashboard gift-cards section lists all activated cards regardless of processing system, activity history per card, receipt links for integrated sales; sales appear in POS reporting.

### Gift Up! (evidence layer A — directly observed)

**Positioning.** "The simplest way to sell your business' gift cards online with no monthly fee" — embeddable checkout for any website/Facebook/Instagram, any currency; per-transaction fee model (no monthly/setup fees). Handles "everything from payment to delivery".

**Sale configuration.** Items for sale: fixed-value cards, custom-value cards (buyer chooses the amount), or selling products/services as gift cards. Backing types: **currency-backed** (any amount off, $0.01 minimum increments, custom amounts purchasable, redeemable via integrations/app/API) vs **unit-backed** (whole units only — e.g., 5 hotel nights, 5 massages; cannot take partial units; redeemable only via the redeem app and API, not integrations). Designs: 100s of pre-made designs, custom artwork upload, custom layout designer, buyer can choose design. Code format configurable; merchant can upload own codes to be issued; barcode display configurable. Terms & conditions attachable. Naming guidance covers cards/certificates/vouchers.

**Validity.** Valid-from policy (immediate default / set days after purchase / specific date per item) and expiry policy (never default / months after purchase / specific date per item); expiry computed from the valid-from date; per-item override of account defaults; per-card validity editing after issuance (e.g., extend). Enforcement differs by channel: in-store soft enforcement (staff see a warning; per-user permission can hard-enforce), online integrations hard-enforce, API returns the dates and the caller decides. Help article links jurisdiction-specific rules: US Credit CARD Act, Canadian prepaid card legislation, EU/Irish Consumer Protection (Gift Vouchers) Act 2019, UK, Australian Treasury Laws Amendment (Gift Cards) Act 2018, NZ.

**Delivery.** Email delivery instant or scheduled for a special occasion; recipient gets a branded card to print, download, or save to the phone's wallet; postal orders for the merchant's own printed cards.

**Redemption.** Staff companion app (mobile/iPad/PC/Mac) and POS terminal integrations for in-store validation/redemption; online redemption in shopping carts (WooCommerce/Shopify-class integrations), booking systems, or custom platforms via REST API; redemption through a payment provider is a separate topic (partial-redemption supported out of the box; scanning; topping up; balance checking). Merchant operations: how to top up a card, how to void a card, how to combine 2+ gift cards, how to undo a redemption (app undo button, or dashboard: locate card → expand history → undo). Customer-facing balance check exists ("How do my customers check their gift card balance?").

**Reporting.** Program performance overview; **outstanding gift card liability** report; who/where cards were redeemed; export all gift cards; export all financial transactions; multi-location support ("Working with locations").

### Rise.ai (evidence layer A for product-page claims; no help-center depth fetched)

**Positioning.** "Gift Card & Store Credit Platform": one customer wallet holding Gift Cards, Cashback, Refunds-as-credit, Compensation, Referrals, Memberships, Loyalty ("skip the points — real currency"), Employee Recognition, B2B incentives. The same balance machinery serves value from different provenance.

**Gift card specifics.** Send/schedule gift cards; tailored reminder flows to drive redemption; immediate balance checks; one-click apply or tap at checkout; redemption across storefront, POS, and multi-store family; unified wallet across sales channels. Back-end: full visibility, 16-digit codes (product-specific detail), resend gift cards, change balance, disable cards, **full liability reporting**. Bulk: generate up to 10,000 gift card codes in one click for campaigns/segments (product-specific number, kept as claim); corporate gift cards (35K claim). Enterprise: liability reporting & ERPs, APIs, headless customization, multi-store & omnichannel, custom triggers issuing store credit from user events.

**Claims.** Vendor benchmarks (70% upsell on gift card purchases, 89% redemption rate, 72% spend more than card value, 13.4× ROI) — marketing claims, recorded as claims only.

### Tango (Blackhawk Network) (boundary context, evidence layer A)

Not a merchant's own-card program manager. Tango is a rewards/distribution platform: catalog of "3,100+ physical and digital gift cards" of third-party brands plus Visa/Mastercard prepaid cards and charity donations; send via self-serve portal, bulk ordering, SaaS integrations, or RaaS API; choice products (Reward Link, Global Choice Link, Payouts Link) let recipients pick rewards; use cases are HR recognition, research incentives, marketing, sales, corporate disbursements, government payouts. Regulatory layer: money-transmitter licensing; open-loop prepaid cards issued by partner banks (Pathward, Sunrise Banks, Peoples Trust, GVS Prepaid). This pole shows where Gift Card Management *ends*: Tango owns no merchant card program or card balance ledger of the giver's own brand; it distributes other parties' instruments.

## Cross-product Comparison

| Dimension | Square | Gift Up! | Rise.ai | Tango (context) |
|---|---|---|---|---|
| Managed object | Gift card record (GAN + balance + state) | Gift card/code + balance (currency or unit backed) | Gift card code + balance in unified credit wallet | Not own-program cards; third-party catalog items |
| Card states | PENDING → ACTIVE; CLEAR_BALANCE; DEACTIVATE | active/voided; validity window (valid-from/expiry) | active; disable; resend | N/A |
| Balance ledger | Typed activity ledger (9+ types + system types), full history, webhooks | Per-card history with undo; top-up; void; combine | Change balance, disable; liability reporting | N/A |
| Sale channels | eGift Order Site; POS; API with Orders/Payments integration; physical packs ordered from printer | Embedded checkout on any website; postal orders; API | Storefront + API + bulk codes; corporate orders | Portal/bulk/API for third-party cards |
| Redemption | POS + Square Online; all locations; QR/barcode; card-on-file; partial payments | Redeem app; POS terminals; cart/booking integrations; API; partial until zero | Storefront + POS + multi-store; one-click apply/tap | Recipient redeems at the brand |
| Refund-to-card | REFUND / cross-method REFUND / refund-to-new-card activates | Store-credit style flows via redemption ops | Refunds-as-credit in same wallet | N/A |
| Expiry | None (US FAQ) | Configurable; jurisdiction-dependent legality; channel-dependent enforcement | Expiry used as a motivation lever (case study claim) | N/A |
| Liability | Per-seller outstanding-balance compliance cap; Dashboard | Dedicated outstanding-liability report | Full liability reporting + ERP integration | N/A |
| Fraud/security | Compliance caps per country; GAN security guidance; chargeback BLOCK | Terms; merchant-controlled void; per-user expiry enforcement | Fraud monitoring not evidenced on page | Money-transmitter licensing; prepaid issuance partners |
| Business model | Load fees + processing fees inside platform | Per-transaction fee, no monthly | Subscription tiers (Shopify app) | Per-order/margin on catalog |

**Convergent findings (B — cross-product commonality):**
1. The card is an identified instrument (code/GAN) bound to a value balance.
2. Value enters via issuance tied to a sale/gift event and can later grow (reload/top-up) or be corrected (adjust/refund).
3. Redemption is a drawdown — partial redemption until zero is standard.
4. Every value movement is recorded as a typed event on the card, inspectable and (within policy) reversible.
5. Merchants get a control surface over the whole population of cards (search, inspect, adjust, disable).
6. Outstanding liability is a first-class reportable number.
7. Digital and physical forms; multi-channel redemption (online + in person).

**Divergent findings:** value backing (currency vs units); expiry posture (never vs configurable vs leveraged); states vocabulary; fee models; whether refunds create credit; degree of wallet unification with store credit/cashback.

## Abstraction Levels

### L0 — Defining Invariant

```text
Merchant-operated prepaid value program
└── Gift card = identified stored-value instrument (unique code/card number bound to a value balance)
    └── Issuance under the merchant's program (created/activated with value, program-configured)
        └── Redemption by balance drawdown at the merchant's selling channels
            └── Balance-activity record tracking every value movement over the card's life
```

Removal tests:
- No identified instrument with balance → discount/promo codes, not gift cards.
- No merchant program/issuance control → consumer wallet or open-loop prepaid card issuing, not gift card management.
- No drawdown redemption → a plain accounting ledger, not a gift card system.
- No per-card value-activity record → balances without audit/history; sales reports without card-level truth; the "management" is gone.

**Historical/market-sample check:** paper gift certificates (numbered certificates, issued for value, verified and marked used on redemption, logged in a register) satisfy this core without plastic, PINs, e-gift email, phone wallets, or APIs. Standalone POS-terminal-era gift card processors satisfy it without e-commerce. Digital-first and wallet-era products are the same core with more delivery surfaces. The definition does not over-fit the modern digital pattern.

### L1 — Common Mature Structure

- Digital (eGift/code) and physical (printed/plastic) forms with scanning (QR/barcode)
- Online sale surface (order site / embeddable checkout) + POS in-person sale and redemption
- Custom designs, fixed denominations and/or buyer-chosen custom value
- Partial redemption until zero; holder-facing balance check
- Reload/top-up; refund-to-gift-card (store-credit posture)
- Card-on-file linking to customer profiles
- Lifecycle operations: void/disable/deactivate (lost/stolen), validity edits, resend
- Per-card transaction/activity history; merchant search over issued cards
- Reporting: sales, redemptions (who/where), outstanding liability; exports
- Program terms & conditions; multi-location redemption
- API/webhooks for integration (nearly universal in current market)

### L2 — Variant / Optional Structure

- Value backing: currency vs units (whole-unit semantics; narrower redemption support)
- Expiry posture: none / configurable windows / expiration as motivation; legality varies by jurisdiction (US CARD Act, AU 2018 Act, EU/IE 2019, CA, NZ) and enforcement strength varies by channel
- Bulk/corporate programs: mass code generation, B2B gifting, employee incentives, campaign codes
- Third-party card import/migration from a previous provider (redemption only, no reload)
- Cross-merchant or ticket-value reuse via custom identifiers
- Unification with store credit/cashback/rewards in one wallet (provenance-agnostic balance)
- Open-loop network-branded prepaid cards (adjacent to Card Issuing)
- Loyalty interplay: rewards redeemed into gift cards; cards as loyalty currency
- Fraud/compliance machinery depth: per-country load/balance caps, per-buyer daily caps, chargeback blocking
- Fee models: load fees, per-transaction fees, subscription tiers
- Physical fulfillment logistics (print packs, postal orders); phone-wallet delivery
- Card combination (merge balances) and buyer-side transfer between cards
- Regional/per-seller liability caps; breakage-oriented finance integrations

### L3 — Vendor-specific (research notes only)

- Square: GAN structure and BIN prefixes (778273/778332), `sqgc://` scheme, Luhn requirement for custom GANs, 2.5% load fee countries, per-country compliance-limit tables (e.g., $2,000 max balance US/AU/CA; ¥10,000,000 per-seller cap JP), 50-card/10-customer link limits, activity-type vocabulary (UNLINKED_ACTIVITY_REFUND, TRANSFER_BALANCE_TO/FROM), auto-unlink at zero balance, sandbox limitations, March 2016 activity-history cutoff.
- Gift Up!: 5-minute install positioning, per-transaction fee model, Help Scout desk, item-level validity override, per-user soft/hard expiry enforcement permission, $0.01 redemption minimum increments, unit-backed integrations exclusion, upload-own-codes flow, postal orders toggle.
- Rise.ai: 16-digit codes, 10,000-code bulk generation, one-wallet multi-product framing (cashback/refunds/compensation/referrals/memberships/loyalty), custom triggers, in-store beta, benchmark claims (70% upsell, 89% redemption, 13.4× ROI), brand customers (Skims, Kroger, Miami Heat).
- Tango: 3,100+ brand catalog claim, Reward Link / Global Choice Link / Payouts Link products, RaaS API, money-transmitter license #, Pathward/Sunrise Banks/Peoples Trust/GVS issuance footnotes.

## Vendor-specific Findings

See L3. Additionally: Square's refunds-to-gift-card-as-store-credit framing is a merchant-facing product decision, not universal; Gift Up!'s unit-backed cards being unredeemable in cart integrations is an implementation constraint of one product; Rise.ai's wallet unification is a philosophy, not the family's definition (Gift Up! and Square keep gift cards distinct from other money).

## Rejected Findings

- "Gift cards never expire" — rejected as definitional; it is one posture among several (Gift Up! default is never-expiring but configurable; Rise.ai case study uses short expiries deliberately; jurisdiction rules constrain).
- "Gift card management includes selling third-party brand cards" — rejected; that is the distribution/incentives pole (Tango) where the operator owns no card program. Importing previously-sold third-party cards (Square) is migration, not distribution.
- "Open-loop Visa/Mastercard gift cards are part of the Type" — rejected from the core; they are prepaid card issuance (Tango's prepaid products issued by licensed banks). Closed-loop merchant programs are the Type.
- "Balance must be currency" — rejected; unit-backed cards are a real product structure.
- "Bulk corporate gifting is definitional" — rejected to L2; it is common in mature products (Rise.ai, Tango-side demand) but not required to recognize the Type.

## Boundary Findings

| Nearby Type | Seam | Removal test |
|---|---|---|
| Loyalty Program Management (§05.15 sibling) | Provenance of value: loyalty points are earned through behavior under accrual rules; gift card value is purchased/gifted. Loyalty manages accrual/redemption rules over points; gift card management manages prepaid instruments. They meet where rewards are paid out as gift cards. | Remove earning/accrual and the reward-catalog loop from a loyalty product and what remains may be a gift card program; remove purchased-instrument issuance and redemption drawdown from gift card management and no loyalty program remains. |
| Store Credit / Stored Value Platform (§05.15 sibling) | Same balance-drawdown machinery; different provenance: store credit is value the merchant owes the customer (refunds, goodwill), gift cards are purchased by a giver and typically transferable. Rise.ai merges both into one wallet — evidence the machinery is shared while issuance intent differs. | If value only ever enters via refunds/goodwill, it is store credit; the purchased-giver-recipient flow is the gift card marker. |
| Promotion Management / coupon codes | Promo codes change the price of a transaction; gift cards carry prepaid value consumed across transactions. | No balance → promotion. |
| Retail POS / Checkout / E-commerce Platform | Redemption and sale happen inside those surfaces; gift card management owns instrument, program, ledger, liability. Packaging is usually embedded (Square inside Square POS; Rise.ai inside Shopify). | Remove card program/ledger and the platform still sells; remove checkout/POS and the gift card system still manages value. |
| Payment Processing / Card Issuing | The gift card acts as a payment method at POS (Square: SQUARE_GIFT_CARD brand, partial payments) but settlement stays inside the program; open-loop network prepaid cards are issuing territory (Tango's bank-issued prepaid). | If value is held in a bank-issued network instrument, it is issuing, not merchant program management. |
| Digital Wallet (consumer) | Consumers hold cards in Square profiles or phone wallets; the system of record for issuance/redemption/liability stays merchant-side. | Consumer-side storage alone is a wallet. |
| Rewards & Incentive Distribution (Tango-class) | Distributes third-party catalog cards as rewards; no own-program instrument/ledger. | Owns no merchant card balance → distribution platform. |

Taxonomy note: all three §05.15 siblings (Loyalty Program Management, Gift Card Management, Store Credit / Stored Value Platform) were unprocessed at the time of this pass; the seams above are recorded for joint review. The leaf stands as a Type: standalone pure-plays exist (Gift Up!), platform-embedded programs exist (Square, Rise.ai), and the loyalty-suite bundling pattern known for Paytronix/Givex-class vendors could not be directly verified (source-access limitation) — bundling posture is treated as a packaging variant, mirroring the module-delivery pattern recorded for product-catalog-management and quota-management.

## Uncertainties

- Loyalty-suite enterprise vendors (Givex, Paytronix) and restaurant-vertical products (Toast, Clover) could not be fetched; the enterprise closed-loop network pole (card production, third-party distribution networks, certification) is inferred structurally, not observed. Claims kept generic.
- Shopify's native gift card mechanics were not observed (transport failures); Rise.ai operates as a Shopify-app-layer alternative, which weakly implies platform-native capability exists, but no specifics are asserted.
- Escheatment/breakage accounting depth beyond liability reporting was not directly observed in any sampled product; kept as an L2 uncertainty rather than asserted.
- Rise.ai evidence is product-page level; help-center depth (states, exact operations) was not fetched, so Rise.ai-specific mechanics are lower-confidence.
- Degree to which merchants can transfer liability between systems (migration formats) was only observed as Square's one-time Support-driven third-party import.

## Final Synthesis

Gift Card Management is the merchant-side system of record for a prepaid value program. Its defining core is small: an identified stored-value instrument (code/card bound to a balance), issued and configured under the merchant's program, redeemed by balance drawdown across the merchant's channels, with every value movement recorded as a typed activity on the card. Mature products add the two-form (digital/physical) sales-and-redemption loop, partial redemption and balance checks, reload and refund-to-card, lifecycle ops (void, disable, validity edits, resend), holder-facing balance surfaces, and liability reporting. The Type is usually packaged as a module of commerce/POS platforms; standalone pure-plays compete on embedding and simplicity. Its boundaries are held by provenance of value (purchased vs earned vs owed), ownership of the program ledger (merchant vs distributor vs consumer), and whether the instrument is closed-loop merchant value or network-issued prepaid money.
