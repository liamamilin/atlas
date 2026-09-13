# Research Notes — Merchant Payment Platform

## Research Goal

Determine what "Merchant Payment Platform" names in the real market, and — because two processed sibling leaves (payment-gateway, payment-processing-platform) both flagged this leaf as a probable alias for joint review — decide whether it is:

1. a distinct Application Type with its own defining structure, or
2. an alias/umbrella name for the bundled merchant-side payments product class that the gateway and processing leaves each describe from one stack position, or
3. something else (e.g., an acquirer-side merchant-portfolio system).

This pass DISCHARGES both prior joint-review flags from fresh evidence (research/payment-gateway.md §Boundary Findings item 5; research/payment-processing-platform.md §Boundary Findings item 2).

## Initial Boundary

Working hypothesis at start: "merchant payment platform" reads as "payment platform for merchants" — the market's umbrella label for the bundled product family (Stripe/Adyen/Checkout.com/Braintree/Square-class products) that bundles acceptance + processing + settlement. Alternative readings to test:

- a distinct acquirer/bank-side platform for managing a portfolio of merchants (merchant onboarding/MID management) — would be a genuinely different Type;
- a regional "merchant payments" specialization (QR-acceptance stacks) — would be a variant, not a Type;
- identical to Payment Gateway or Payment Processing Platform (pure alias of one slice).

Nearest processed siblings: payment-gateway, payment-processing-platform, payment-orchestration-platform, card-issuing-platform, card-processing-platform, digital-wallet, peer-to-peer-payment-application, cashless-venue-platform.

## Research Questions

1. What do products marketed under the "merchant payments" name actually contain? Which parts of the payment stack (acceptance / authorization / processing account / settlement / merchant operations) do they hold?
2. Does any sampled product hold a structure NOT covered by gateway L0 ∪ processing L0 (administered account, acceptance surfaces, per-attempt authorization outcomes, durable transaction lifecycle, clearing→settlement→funding)?
3. How does the market use the vocabulary: "merchant payment provider", "merchant services", "payments platform for merchants"?
4. What is the relationship to the two stack-position siblings: does the bundled product = gateway + processing in one product?
5. Would older / regional products fit a "bundled whole" definition, or does it over-fit the current API-first generation?

## Representative Products

Selected for market representation, different product philosophy, different customer layer, and documentation access:

| Product | Pole | Why sampled |
|---|---|---|
| Stripe | developer-first internet-business payments platform | canonical modern pole; also names the market category ("Merchant Payment Providers") |
| Adyen | single-platform enterprise pole | one-platform philosophy; bank-licensed enterprise |
| Square | SMB / hardware-led merchant payments | different customer layer (small business), hardware+software bundle |
| PayPal Braintree / PayPal Enterprise Payments | ecosystem payments platform | PayPal-owned, enterprise repositioning; merchant-account + gateway heritage |
| Rapyd | fintech-as-a-service pole | acquiring + payouts + issuing + accounts bundle; publishes a literal "Merchant Services" product |

Continuity with prior passes: gateway pass sampled Stripe, Adyen, Braintree, Checkout.com, Authorize.Net; processing pass sampled Finix, Worldpay, Stax, Stripe. This pass's sample is disjoint enough (Square, Rapyd fresh; Stripe/Adyen/Braintree re-observed at product-page tier) to give independent confirmation.

## Sources

All fetched 2026-09-08, official vendor surfaces:

- Stripe — https://stripe.com/payments (product page: acceptance surfaces, methods, Radar/disputes, unified platform, compliance, pricing, Forrester "Merchant Payment Providers" naming)
- Adyen — https://www.adyen.com/ (root: one-platform positioning, Unified Payments / accept-payments / payouts / POS / for Platforms; /payments returned 404)
- Square — https://squareup.com/us/en/payments (payments product page incl. FAQ, "Merchant services" sub-nav, payment-platform link)
- PayPal Braintree — https://www.braintreepayments.com/ (root: "end-to-end payment platform", merchant account application, sandbox, control panel, PCI, orchestration/payouts links)
- Rapyd — https://www.rapyd.net/ (root: accept/send/manage funds, product set) + https://www.rapyd.net/products/payments/merchant-services/ (merchant account, acquiring bank, settlement wording)

No Tier-1 help-center articles were fetched this pass; evidence is product-page tier (Layer A for product structure and scope; not for operational flow detail). Operational detail is inherited from the two sibling passes' Tier-1 documentation where the same products overlap (Stripe, Adyen, Braintree).

## Product Observations

### Stripe (Layer A — product page)

- Self-describes as "a payments solution built for any business—from scaling startups to global enterprises"; named a Leader in "The Forrester Wave™: Merchant Payment Providers, Q1 2026" (market-category naming anchor).
- Acceptance surfaces: prebuilt payment page (hosted checkout, embed or redirect), shareable payment links (no-code, QR/embeddable buy button), embedded form (single/multi-step iframe), customizable UI components (Elements), in-person via Terminal pre-certified devices ("countertop to curbside", run-your-own-POS on select readers).
- Payment methods: "125+ payment methods" incl. BNPL, bank debits, stablecoins, real-time payments; AI-driven surfacing of relevant methods; A/B testing of methods.
- Global: local acquiring coverage, multi-currency settlement ("settling and paying out funds with multi-currency settlement"), 195 countries / 135+ currencies presented as marketing figures.
- Intelligence layer: Radar fraud, Authorization Boost (retries, messaging, card lifecycle), authentication/3DS handling with SCA exemptions, Smart Disputes (AI evidence submission), payments analytics.
- Platform: "unified platform"; advanced capabilities incl. local acquiring, regional debit networks, multiprocessor setups, Organizations (multiple accounts); Connect for platforms/marketplaces; Global Payouts; billing/tax/revenue-recognition as separate products (adjacent).
- Compliance/security posture: PCI Level 1, KYC/AML checks, money-transmitter and e-money licenses; uptime claims.
- Developer surfaces: API code samples, SDKs, webhooks, test environment, CLI; account creation "no contracts or banking details required" (self-serve onboarding) vs custom pricing (enterprise).

### Adyen (Layer A — root page)

- "Fintech platform for enterprises — One platform for payments, data, and financial products. Built to scale with the world's leading businesses."
- Value props: US/UK/EU banking licenses; 99.999% uptime claim; "one platform"; built-in optimizations (conversion/fraud/cost); "one API that supports multiple use cases and channels".
- Use cases: Accept payments, Send payouts globally, In person payments; Adyen for Platforms (marketplace/platform enablement).
- "Intelligent Money Movement": "Accept, settle, and move funds on one platform" — acceptance and settlement held as one span.
- Products: Unified Payments (accept-payments), Risk management, Authentication, Issuing; embedded finance (accounts, issuing, capital under one integration).
- Adjacent: payouts, issuing — the bundled financial-products layer.

### Square (Layer A — payments page)

- "Square Payments — Built for however you do business"; sub-nav includes "Merchant services" (terminology anchor: merchant payments = merchant services).
- Acceptance surfaces: in person (own hardware lineup: handheld, terminal, register, stand, kiosk, readers; Tap to Pay on phone), online (free online store, payment links, "connect your existing store or app to one of our trusted payment APIs"), remote (invoices payable by card or ACH; Virtual Terminal keyed-in card; over-the-phone).
- Payment methods: major cards, digital wallets (Apple/Google Pay), BNPL (Afterpay) — "you get paid in full immediately".
- FAQ defines the bundle directly: "payment processing ... is how money moves safely from your customer's card to your bank account. With Square Payments, you get everything you need in one simple package: accept payments..., get your money fast with transfers in 1-2 business days, ... fraud protection, ... built-in PCI".
- Money completion: transfers to external bank next business day free or instant for fee; funds flow into Square Checking (banking layer, affiliate-bank wording); offline payments mode (store-and-forward, 24h reconnect rule footnote) — in-person resilience variant.
- Operations: dispute management, active fraud prevention, E2E encryption, PCI built in; dashboard reporting/analytics ("real-time tracking of payments, refunds, and customer activity in your Square Dashboard").
- Larger businesses: "our payment platform offers a range of in-person and online payments APIs and SDKs"; custom pricing above a volume threshold; franchises/multi-location testimonials.
- Adjacent: banking (checking/savings/loans), payroll, loyalty, marketing — the SMB suite pole.

### PayPal Braintree / PayPal Enterprise Payments (Layer A — root page)

- "Braintree is now PayPal Enterprise Payments"; "Help drive growth with our end-to-end payment platform"; FAQ: "a global payment processing solution that delivers end-to-end checkout experiences for businesses".
- Capabilities surfaced: integrated payments solution; network + PCI compliance (validated Level 1 PCI DSS service provider; SAQ-A readiness via ready-built interfaces); global and local payment methods; PayPal, Pay Later, Venmo as method types; Orchestration (share payment data with other providers — the multi-processor seam); Global Payouts; fraud protection.
- Merchant account: sandbox exists "before applying for a merchant account or going into production" — merchant account application is part of the product's onboarding (Layer A wording).
- Operations: Control Panel login, reporting tools, subscriptions testing, sandbox.
- Scale claims: total volume, transactions, 200+ markets (marketing figures, not asserted in final doc).

### Rapyd (Layer A — root + merchant services page)

- "The Fintech Platform For Every Business — One solution to accept, send and manage funds globally."
- Product set: Accept Payments Online (Global Payments API, Hosted Checkout, Payment Links, Virtual Terminal), Accept Payments In-Store (card machines, short-term hire), Merchant Services, Israel Card Acquiring, Send Payouts (Disburse), Issue Cards, Multi-Currency Business Accounts, Virtual Accounts.
- Merchant Services page (naming + structure anchor): "If you run a small or medium-sized business, then you need a merchant account to accept card payments"; "A merchant account is where your customers' card details are sent for authorization during a transaction. Rapyd provides a merchant account"; "As an acquiring bank, it is also our responsibility to make sure that your customer has sufficient funds... Once authorised, we will then make sure that the money is transferred to your linked account"; "Faster settlement – you can receive your funds as quickly as the next working day"; dedicated in-house merchant services team; managed setup of the merchant account.
- Adjacent: issuing, payouts, multi-currency business accounts, stablecoin solutions, embedded fintech; industries from eCommerce to crypto exchanges.

## Cross-product Comparison

| Structure | Stripe | Adyen | Square | Braintree/PP | Rapyd | Evidence |
|---|---|---|---|---|---|---|
| Serves an enrolled selling business (merchant) | A | A | A | A (merchant account application) | A | A×5 |
| Multiple acceptance surfaces across channels (hosted/embedded/links/terminal/invoices/virtual terminal) | A | A | A | A | A | A×5 |
| Payment-method breadth incl. cards + wallets + local methods | A | A | A | A | A | A×5 |
| Per-attempt authorization into external payment ecosystem | A (implied by processing wording; Tier-1 docs from gateway/processing passes) | A (implied) | A (FAQ: "card to your bank account", authorization) | A (Rapyd-style wording; sandbox/merchant account) | A (explicit: "sent for authorization") | B (explicit at Rapyd/Square; structural at others) |
| Administered processing/merchant account provided by the platform (or its acquiring partners) | A (KYC/AML, self-serve or contract) | A (bank licenses) | A (FAQ "everything in one package") | A (apply for merchant account) | A (explicit acquiring bank wording) | A×5 |
| Money completion: settlement/funding to merchant's bank (payouts, speed options) | A (multi-currency settlement, payouts) | A ("accept, settle, and move funds"; payouts) | A (transfers next-day/instant) | A (implied; payouts page) | A (explicit "money is transferred to your linked account", next working day) | A×5 |
| Fraud/risk tooling in the flow | A (Radar) | A (Risk management) | A (active fraud prevention) | A (fraud protection) | (not surfaced on fetched pages) | A×4 |
| Dispute management | A (Smart Disputes) | (not on fetched page) | A | (not on fetched page) | (not on fetched page) | A×2 + inherited Tier-1 from sibling passes |
| Merchant dashboard / control panel / client portal | A | A (implied; platform) | A (Dashboard) | A (Control Panel) | A (Client Portal in docs nav) | A×5 |
| Platform/marketplace sub-merchant enablement | A (Connect) | A (Adyen for Platforms) | (large business APIs; not platform-specific on page) | (orchestration adjacency) | A (marketplaces industry + PayFac partner program) | A×3–4 (common) |
| Bundled adjacent financial products (issuing, accounts, banking, billing) | A (Billing, Payouts, Atlas...) | A (Issuing, embedded finance) | A (Banking, Payroll...) | A (Pay Later, payouts) | A (Issuing, Accounts, Payouts) | A×5 (adjacent layer, NOT core) |
| Multi-currency / global settlement options | A | A | (not surfaced) | A (implied) | A | A×4 (common) |

Reading: every sampled product holds the FULL span — acceptance + authorization + administered account + settlement/funding + merchant operations — in one product. No product markets only one stack position under this name. No acquirer-side merchant-portfolio-management product surfaced under this name.

## Canonical Abstraction

### L0 — Defining Invariant

A Merchant Payment Platform is the **bundled merchant-side payments product**: one product serving an enrolled selling business that spans the whole acceptance-to-money path. Invariants — remove any one and it is no longer this Type (it becomes one of the siblings):

1. **Enrolled selling business** — the platform serves a merchant (the payee side), underwriting/onboarding the merchant account or processing relationship. Remove → payer-side product (wallet / P2P), not merchant payments.
2. **Acceptance surfaces in the merchant's channels** — hosted/embedded checkout, payment links, virtual terminal, in-person terminal, invoicing: the interfaces through which the merchant's sales channels submit payment requests. Remove → back-end processing engine with no merchant-facing acceptance (the processing leaf's isolated form).
3. **Per-attempt authorization with durable transaction records** — each payment attempt routes into the external payment ecosystem, returns an approved/declined outcome, and is recorded with a tracked lifecycle (authorized → captured → settled; declined/refunded/disputed branches). Remove → settlement-only money mover, not a payments platform.
4. **Money completion under the same product** — the platform (or its acquiring partners under the administered relationship) completes clearing → settlement → funding the merchant's designated bank account, with fees netted or billed. Remove → acceptance-and-authorization front end that requires an externally arranged merchant account — i.e., a gateway in the decoupled form, not the bundled whole.

The load-bearing property that distinguishes this leaf from its two siblings is the **whole-span-in-one-product** posture: gateway = the acceptance/authorization slice (which can exist decoupled from acquiring); processing platform = the account/money-completion slice; merchant payment platform = the market name for the bundled product that holds the entire span. Historically this bundle is not new — the full-service "merchant services" package (merchant account + acceptance + equipment + processing + deposits) sold by acquirers/ISOs since the card-acceptance era satisfies the same span without any API — so the definition does not over-fit the API-first generation.

### L1 — Common Mature Structure

- breadth of payment methods (cards, wallets, BNPL, bank/local methods) with eligibility handling
- fraud screening and card authentication (3DS/SCA-class) in the flow
- dispute/chargeback management surfaces
- merchant dashboard: transaction search, refunds, reporting/analytics, payout visibility
- webhooks/APIs/SDKs + sandbox/test environments
- multi-currency settlement / local acquiring options
- platform & marketplace enablement (sub-merchants, split payments) — common in larger products
- PCI-compliance offloading via hosted/card-data-isolating acceptance surfaces

### L2 — Variant / Optional Structure

- customer layer: self-serve SMB (sign up, get hardware) vs enterprise contract (custom pricing, local acquiring depth)
- channel emphasis: hardware-led in-person pole vs API-led online pole vs both (unified commerce)
- platform/marketplace aggregation posture (the platform itself underwrites sub-merchants)
- adjacent financial products bundled under one brand: billing/recurring, tax, issuing, business bank accounts, payouts to third parties, lending/capital — the "fintech platform" drift zone
- regional method/regulatory packs; regional acquiring subsidiaries
- offline payment resilience (in-person store-and-forward)
- multiprocessor setups / data sharing with other providers (the orchestration seam)

### L3 — Vendor-specific (research notes only)

- Stripe: Link, Authorization Boost, Optimized Checkout Suite, Radar, Smart Disputes, Connect, Atlas, Organizations; Forrester Wave quote; uptime/volume claims; HK price figures.
- Adyen: Intelligent Money Movement, Uplift (Risk/Authenticate product naming), Spotlight campaign, €1.4T processed claim, license list.
- Square: hardware lineup names (Handheld/Terminal/Register/Stand/Kiosk/Readers), Tap to Pay, Square Checking/Savings/Loans, offline 24-hour reconnect rule, instant-transfer limits footnote, Block/Sutton Bank wording.
- Braintree: Control Panel, sandbox signup, SSO login, Venmo/Pay Later method pages, PayPal Enterprise Payments rebrand, volume claims.
- Rapyd: Israel Card Acquiring, Icelandic-localized pages, card-machine rental, "0 screaming" campaign tone.

## Rejected Findings

- **"Merchant payment platform = acquirer-side merchant-portfolio management system"** — rejected for this leaf's name. No sampled product under merchant-payments vocabulary is an acquirer's internal merchant-onboarding/MID-management system; such products exist in the market but are named differently (acquirer platforms, merchant management). If the directory ever wants that Type it needs a different leaf; nothing in this research supports folding it here.
- **"Merchant payment platform = payment orchestration"** — rejected. Orchestration's L0 is routing above multiple independently contracted providers; sampled merchant-payment products route within their own acquiring relationships. Braintree markets "Orchestration" as an adjacent capability (sharing payment data with other providers), which confirms orchestration is a neighboring layer, not the same product.
- **"Adjacent financial products (banking accounts, issuing, billing) are part of the Type"** — rejected; present in all 5 samples as bundled adjacents, but the merchant payments span is complete without them; they are the fintech-platform drift zone (L2).
- **"Instant/fast payout is definitional"** — rejected; payout speed varies (next-day free vs instant-for-fee vs standard schedules) and is a money-completion option, not the invariant.

## Boundary Findings

**Joint review disposition (DISCHARGES both prior flags):** Merchant Payment Platform is CONFIRMED as the umbrella/alias-level name of the bundled merchant-side payments product class. The market uses "merchant payment providers" (Forrester, quoted by Stripe), "merchant services" (Square sub-nav, Rapyd product), "end-to-end payment platform" (Braintree), "payments platform" (Stripe/Adyen/Rapyd) for one and the same product family. No structural difference from gateway ∪ processing was observed — every sampled product holds both stack positions' cores simultaneously. Recommendation recorded for STATUS: treat this leaf as the bundled-whole entry whose defining core is the union span; Payment Gateway and Payment Processing Platform remain meaningful as the two stack-position slices (the gateway slice demonstrably exists decoupled — Authorize.Net heritage — and the processing slice as back-end emphasis), but all three leaves describe one product family in the modern market.

Boundary seams from this side:

- **vs Payment Gateway (processed):** gateway = enrolled merchant + acceptance + authorization + transaction record (can require an external merchant account); merchant payment platform additionally holds the administered processing relationship and money completion in the same product. Test: remove settlement/funding → a decoupled gateway remains; the bundled whole does not.
- **vs Payment Processing Platform (processed):** processing = account + network processing + clearing/settlement/funding (back-end emphasis; payer-facing acceptance excluded from its L0); merchant payment platform additionally holds the merchant-channel acceptance surfaces. Test: remove acceptance surfaces → a processing back end remains.
- **vs Payment Orchestration Platform (processed):** routing control above multiple independently contracted providers vs the provider itself. Holds.
- **vs Retail POS / Restaurant POS (05.10):** POS composes the sale (catalog/cart/staff/checks) and uses a payment stack; the merchant payment platform never composes the sale. Hardware-led merchant-payment products approach the POS seam (Square ships a full POS suite) but the payments span is the leaf's subject. Holds.
- **vs Checkout Platform (05.06):** payer-facing conversion surface vs merchant-side payment execution. Holds.
- **vs Digital Wallet / P2P Payment (§08):** payee-side merchant service vs payer-side consumer products. Holds.
- **vs Billing Platform / Invoicing (§08):** decide what/when to charge vs execute the charge and complete the money. Invoicing acceptance surfaces appear inside merchant-payment products (Square Invoices, Stripe Invoicing) as adjacent products. Holds.
- **vs Card Issuing / Card Processing (§08):** issuer side of the network vs merchant/acquiring side. Adyen/Rapyd/Stripe bundle issuing as adjacent financial products, mirroring the card passes' fused-products observation. Holds.
- **vs International Commerce Management (§05.24):** market-scoped selling layer vs payment execution. Holds (multi-currency settlement is a capability of this leaf, not its center).

## Historical / Market-Sample Check

- **Classic full-service merchant services (bank/ISO acquiring packages, pre-API era):** merchant account underwriting + card acceptance equipment + processing + scheduled deposits + statements. Same span, different implementation. Fits — so the "bundled whole" is NOT an over-fit to the API-first generation; the API-first products are its current form.
- **Classic decoupled gateway (Authorize.Net heritage, 1996):** acceptance + authorization requiring an externally arranged merchant account. Does NOT satisfy L0 property 4 — correctly excluded as the gateway leaf's decoupled form, which is exactly how the market treats it (a gateway, not a merchant payment platform). This exclusion is the definition's sharpest validation.
- **Regional QR-acceptance stacks (UPI-class merchant payments, wallet-acquirer hybrids):** enrolled merchant + acceptance (QR) + settlement to bank — structurally fits the L0; not directly sampled (uncertainty recorded).
- **Platform-native payment components (commerce platforms' built-in payments):** same span exposed inside a commerce platform; reads as a deployment/packaging variant of this span.

## Uncertainties

- Evidence tier: all fresh fetches are product-page tier; no help-center article bodies were fetched this pass. Operational-flow claims (capture/settle timing windows, dispute deadlines, reserve mechanics) are inherited from the sibling passes' Tier-1 docs (same products) or kept general. No precise operational numbers asserted in the final document.
- Adyen evidence is root-page level (its /payments path 404'd); "Unified Payments" product naming observed via footer only.
- Checkout.com, Worldpay, Fiserv, Paysafe not re-fetched this pass (prior passes recorded their access limits); the bundled-class conclusion rests on 5 fresh products + continuity with prior passes' 8 additional products.
- Whether the taxonomy should merge the three leaves (gateway/processing/merchant-payment-platform) into one Type with stack-position variants is a directory-design decision, not decidable from product research; recorded as a recommendation in Boundary Issues, no taxonomy change made unilaterally.
- Regional merchant-payment products (UPI, Pix-for-merchants, SEPA-centric acquirers) not sampled; L0 is method-agnostic and structurally accommodates them, but no Layer A evidence collected.

## Final Synthesis

"Merchant Payment Platform" is the market's umbrella name for the **bundled merchant-side payments product**: one product that serves an enrolled selling business end to end — acceptance surfaces in the merchant's channels (hosted/embedded checkout, links, virtual terminal, in-person terminals, invoices), per-attempt authorization with durable transaction lifecycles, an administered merchant processing relationship, and money completion into the merchant's bank account — plus the merchant-operations layer (dashboard, refunds, disputes, fraud, reporting).

The two processed siblings describe the same product family from single stack positions: the Payment Gateway is the acceptance-and-authorization slice (which can exist decoupled from acquiring), the Payment Processing Platform is the account-and-money-completion slice. The joint review confirms the alias/umbrella reading: every product sampled under merchant-payments vocabulary holds the whole span, and the only structural discriminator of this leaf is the bundled-whole posture itself. The bundle is historically deep (full-service merchant services packages), so the definition does not over-fit the current API-first generation.
