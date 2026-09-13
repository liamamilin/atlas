# Research Notes — Payment Gateway

Research date: 2026-09-06

## Research Goal

Understand what a Payment Gateway actually is as an Application Type — its core objects, the payment lifecycle it manages, how merchants integrate and operate it, which rules govern its behavior — and where its boundary lies against the neighboring payment-related Types in the directory (Payment Processing Platform, Payment Orchestration Platform, Merchant Payment Platform, Checkout Platform, Digital Wallet, Billing Platform, Retail POS).

## Initial Boundary

Initial hypothesis (before research):

- Core use: a merchant-side service that collects payment details from a merchant's sales channels and turns them into authorized, recorded, settleable transactions.
- Primary users: the merchant (its developers for integration; its operations/support staff for day-to-day payment operations). The payer interacts only transiently with hosted acceptance surfaces and is not an account holder of the gateway.
- Nearest Types: Payment Processing Platform (backend of the same stack), Payment Orchestration Platform (routing layer above gateways), Checkout Platform (customer-facing conversion surface), Digital Wallet (payer-side), Merchant Payment Platform (terminology sibling), Retail POS (in-person sale composition), Billing Platform (what/when to charge).
- Unknowns: (1) whether "gateway" vs "processor" remains structurally separable in modern products that bundle both; (2) whether merchant enrollment/onboarding is definitional or merely common; (3) how much acceptance-surface variety is definitional vs market fashion.

## Research Questions

1. Who are the parties in the system, and what does each do? (merchant, gateway operator, payer, external payment ecosystem)
2. What is the central object, and what states does it move through? (transaction / payment intent lifecycle)
3. Through what surfaces do merchants accept payments? (hosted page, embedded components, API, no-code links, terminals)
4. What happens to payment data? (security scope, tokenization/vault)
5. What operational controls does the merchant get? (dashboard, webhooks, reports, refunds, disputes)
6. Which rules materially shape behavior? (authorization vs capture, authentication/SCA, risk screening, statement descriptors, settlement)
7. What exceptions matter? (declines/retries, chargebacks, asynchronous methods, duplicates, partial capture/refund)
8. Where does the gateway end and the processor / orchestrator / checkout / wallet begin?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Stripe | developer-first, self-serve, API-centric; startups → enterprise | canonical modern gateway/platform; best-documented lifecycle |
| Adyen | enterprise-first, single unified platform (online + in-person); contract sales | enterprise tier; strong lifecycle + compliance docs |
| Braintree (PayPal service) | mid-market; gateway + merchant-account bundling; wallet-heavy | different lineage (classic gateway), vault-centric model |
| Checkout.com | enterprise, API-first acquiring platform | newer-generation enterprise PSP; structure confirmation |
| Authorize.Net (Visa) | historical sample check; classic gateway since 1996 | §24-style check: does the definition hold for pre-modern, separately-banked gateways? |

## Sources

All fetched 2026-09-06 (Layer A — directly observed unless noted):

- Stripe — Payments overview: https://docs.stripe.com/payments
- Stripe — Payment Intents API guide: https://docs.stripe.com/payments/payment-intents
- Stripe — Payment/Setup Intent lifecycle: https://docs.stripe.com/payments/paymentintents/lifecycle
- Adyen — Online payments overview: https://docs.adyen.com/online-payments
- Braintree (PayPal) — Docs home / integration guide index: https://developer.paypal.com/braintree/docs
- Checkout.com — Docs home: https://docs.checkout.com/ (Tier 2: docs-home-level only; operational depth not fetched — see Uncertainties)
- Authorize.Net — Developer "Hello world" / getting started: https://developer.authorize.net/hello_world/

Not fetched (limitation): per-product pricing pages, merchant-agreement terms, dispute-flow detail pages, Checkout.com operational guides, any non-official review sources. No claim in this file relies on model memory for precise operational facts.

## Product Observations

### Stripe (Layer A unless noted)

- Positions as "accept payments online and in person"; also embeds financial services and custom revenue models (product breadth beyond gateway noted as vendor bundling).
- Acceptance surfaces enumerated by official docs: Stripe-hosted payment page (Checkout), embedded payment form (Elements), embedded components, no-code Payment Links, mobile SDKs, and in-person Terminal (SDKs + card readers).
- Payment methods categorized: cards, wallets, bank debits, bank redirects, Link (vendor's own accelerated checkout — vendor-specific).
- Core API objects: **PaymentIntent** (tracks a payment from creation through checkout; status changes over its lifecycle; triggers additional authentication steps when required), **PaymentMethod**, **SetupIntent** (collect/save payment details without charging), **Charge** (each attempt; a PaymentIntent can have multiple Charges from retries), **Refund**, **Customer** (implied by saved payment methods).
- Lifecycle states (official): `requires_payment_method` → `requires_confirmation` → `requires_action` (e.g. 3D Secure) → `processing` / `requires_capture` (if separately authorizing and capturing) → `succeeded` / `canceled`. On decline, status returns to `requires_payment_method` so the payment can be retried. Cancellation releases held funds and invalidates future attempts.
- Two-action model: create (server) + confirm (client); server monitors webhooks to detect completion/failure; client-secret pattern for client access (implementation detail).
- Authorization/capture split explicitly supported ("place a hold", `requires_capture`); refunds after success.
- Setup flows for future payments: on-session vs off-session semantics for saved payment methods; banks may reject off-session charges without authentication.
- Fraud: Radar (rules on metadata attributes; Radar Plus tier) — vendor-named, capability-level common.
- 3D Secure / SCA handled natively by the intent lifecycle.
- Statement descriptors settable per account and per payment (precision on limits deliberately not recorded).
- Metadata (e.g., order id) for reconciling gateway payments with merchant's own orders; visible in Dashboard and reports.
- Idempotency keys to prevent duplicate charges (implementation-level but behavior-relevant).
- Separate products bundled: Billing/subscriptions, Invoicing, Connect (platforms/marketplaces), Terminal, crypto, etc. — recorded as vendor bundling, not gateway definition.

### Adyen (Layer A unless noted)

- Online payments overview: accept cards, wallets, local payment methods on website and mobile app; unify with in-person payments on one platform ("unified commerce").
- Integration architecture (official): **payments server** (calls Checkout API), **client website/app** (Drop-in/Components collect payment details), **webhook server** (receives webhooks about payment statuses and other payments-related activity). — Confirms server-create/client-collect/notify-via-webhook loop as cross-product structure (with Stripe).
- Transaction types: one-off payments, subscriptions, bookings, top-ups.
- Modify payments (official nav): Capture, Cancel, Refund, Reversal, Authorization adjustment (incl. pre-auth adjustment), CAPTURE_FAILED reasons. — Confirms auth/capture split + reversal semantics (Layer B with Stripe's `requires_capture`/cancellation).
- Features: 3D Secure 2 (native/redirect, per-platform), risk management, tokenization (store shopper's payment details; make token payments; manage tokens), network tokenization, Account Updater, Auto Rescue (automatic retries), partial authorizations, partial payments, two-step checkout, surcharge, payment links.
- Compliance section: PCI DSS compliance, PSD2 SCA implementation guides, regional compliance guides (India, Japan, Australia, co-badged cards). — Confirms regulatory-compliance surface as common structure.
- **Customer Area** = merchant dashboard: view unified transaction data and reports across in-person and online channels; account and transaction management. (test URL referenced: ca-test.adyen.com — implies test vs live environments.)
- Online payouts to bank accounts/wallets; payout webhooks (payout = money movement toward merchant/payees).
- Plugins for commerce systems (platform connectivity as optional surface).

### Braintree (Layer A unless noted)

- Docs home organized as: **Accept Payments** (checkout UIs: Drop-in UI, Hosted Fields; payment method types; customer data/vaulting), **Protect** (Premium Fraud Management Tools — real-time transaction evaluation; 3DS2), **Manage** (Disputes via API incl. search/status/evidence submission; Reports; Webhooks; In-Store Payments), **Extend** (OAuth; Grant API — share vaulted payment methods with other Braintree merchants; Forward API — send vaulted data to PCI-compliant third parties).
- Basics: Client Authorization, **Single-use Token (payment method nonce)** — client-side tokenization of raw payment data before it reaches the merchant server; **Customers**, **Payment Methods**, **Transactions** as core objects.
- Payment method types: credit cards, ACH Direct Debit, Apple Pay, Google Pay, PayPal, Venmo, Secure Remote Commerce.
- Recurring Billing as a feature.
- Merchant onboarding language: "Become a Merchant" (contact sales), **Production Control Panel** login (braintreegateway.com), sandbox account creation + sandbox/production environments.
- Vault-centric model: "Store customer and payment information to reduce friction at checkout" — vaulting is a first-class pillar.

### Checkout.com (Layer A at docs-home level; operational detail not fetched)

- Docs sections: **Payments** ("Accept online payments, create a Platform, and process payments on behalf of your sub-entities"; low-code "Flow" acceptance; payment methods), **Funds management** (Checkout Business Account: store/manage funds in multiple currencies, receive settlements), **Business operations**, **Card issuing**, **Platforms**.
- Optimization features: Intelligent Acceptance (AI-driven acceptance-rate optimization), integration-health monitoring, payment-request data-quality guidance.
- Product catalog (Tier 2 pages): payment processing, fraud protection, authentication (3DS), Vault, Real-Time Account Updater, network tokens, payouts, issuing, identity verification.
- Dashboard at dashboard.checkout.com; test-account self-service ("Get test account").

### Authorize.Net (historical sample, Layer A)

- Explicit separation: "To accept real payments, you will need a **merchant account**" — the gateway historically requires the merchant to hold a bank merchant account; gateway and acquiring are decoupled.
- Merchant authentication = apiLoginId + transactionKey (per-merchant credentials; direct evidence of the enrolled-merchant + credential structure).
- Transaction request carries: transaction type (**authCaptureTransaction** vs **authOnlyTransaction** — direct evidence of the authorize/capture split in the oldest sampled product), payment (card number/expiry/CVV), amount, order info (invoice number, line items), billing address, customer data, merchant-defined fields.
- Response: Transaction ID, Response Code, Auth Code (authorization outcome is a first-class return value).
- Duplicate-detection setting (`duplicateWindow`) — duplicate-payment guard as long-standing behavior.
- Sandbox + testing guide + go-live checklist — test/live separation is not a modern invention.
- "How payments work" educational content places the gateway inside the credit-card processing chain (gateway → processor → card networks), consistent with the classic gateway/processor split.
- Note: sample code shown on the page mixes Authorize.Net and CyberSource samples (same owner); only Authorize.Net content used here.

## Cross-product Comparison

| Dimension | Stripe | Adyen | Braintree | Checkout.com | Authorize.Net |
|---|---|---|---|---|---|
| Enrolled merchant account w/ credentials | yes (account + API keys) | yes (account; Customer Area) | yes ("Become a Merchant"; Control Panel) | yes (dashboard login; business account) | yes (merchant account required; apiLoginId/key) |
| Acceptance surfaces | hosted page, embedded form, components, payment links, mobile SDK, terminal | Drop-in/Components, hosted/redirect flows, payment links, terminal (unified commerce) | Drop-in UI, Hosted Fields, in-store | hosted/low-code "Flow", embedded, API | hosted (SIM era), server API, (modern: Accept.js hosted fields) |
| Payment method breadth | cards, wallets, bank debits/redirects | cards, wallets, local methods | cards, ACH, PayPal, Venmo, Apple/Google Pay | cards, wallets, local methods | cards, ACH, (e-check etc.) |
| Authorization outcome returned to merchant | yes (intent status) | yes (result codes) | yes (transaction result) | yes | yes (Response Code + Auth Code) |
| Auth/capture split | yes (`requires_capture`) | yes (capture/cancel/reversal) | yes (auth then submit for settlement) | yes | yes (`authOnly` → capture) |
| Decline → retry modeled | yes (status returns to requires_payment_method; multiple Charges) | yes (result codes; Auto Rescue retries) | yes (transaction result; processor declines) | yes (acceptance-rate optimization) | yes (duplicate window; retries) |
| Refunds / reversals | yes (Refunds API) | yes (refund, reversal) | yes (refund/void) | yes | yes (refund/void transactions) |
| Vault / tokenization | yes (PaymentMethod + Customer; setup flows) | yes (tokenization, network tokens, account updater) | yes (Vault; nonces; Grant/Forward APIs) | yes (Vault; account updater; network tokens) | yes (customer profiles; payment profiles) |
| Server notifications of status | yes (webhooks) | yes (webhooks — dedicated server component) | yes (webhooks) | yes (webhooks; docs-home level) | yes (silent post / webhooks; not fetched in detail — inferred from product docs nav; treat as B) |
| Merchant dashboard | yes (Dashboard) | yes (Customer Area) | yes (Control Panel) | yes (dashboard) | yes (Merchant Interface) |
| Sandbox/test + go-live | yes (test mode, sandbox) | yes (test Customer Area; go-live checklist) | yes (sandbox) | yes (test account) | yes (sandbox + go-live checklist) |
| Fraud / risk screening | yes (Radar rules) | yes (risk management) | yes (fraud tools) | yes (fraud protection) | yes (fraud detection suite; nav-level) |
| 3DS/SCA handling | yes (in intent lifecycle) | yes (3DS2; SCA guides) | yes (3DS2) | yes (3DS authentication) | yes (3DS support) |
| Statement descriptor control | yes | yes (nav-level) | yes (nav-level) | not observed (not fetched) | not observed |
| In-person / terminals | yes (Terminal SDK/readers) | yes (cloud terminals; unified commerce) | yes (in-store) | not observed at docs-home level | (historically POS-facing via processors; not observed here) |
| Platforms/marketplaces (sub-merchants, splits) | yes (Connect) | yes (platforms/marketplaces) | yes (Braintree Marketplace) | yes (Platforms; sub-entities) | no (single-merchant classic) |
| Settlement/payout visibility | yes (balance/payouts; succeeded ⇒ funds in account) | yes (payouts; payout webhooks) | yes (settlement batched; reporting) | yes (Business Account; receive settlements) | yes (settlement via merchant account/processor) |

**Stable commonalities (Layer B, across all or nearly all sampled products):** enrolled merchant relationship with credentials; multi-surface acceptance; authorization outcome as the central return value; authorize-then-capture split with cancel/void/refund/reversal; durable transaction records with lifecycle states; tokenization/vaulting; server notifications (webhooks); merchant dashboard; sandbox→go-live; risk screening; 3DS/SCA handling; settlement visibility.

## Canonical Abstraction

### L0 — Defining Invariant

A Payment Gateway is a **merchant-side payment acceptance and authorization service**. Minimal structure, all four required:

```text
Enrolled Merchant (account + credentials, multi-tenant)
└── Acceptance surface (merchant's sales channel submits a payment request:
    amount + payment details, via hosted page / embedded component / API / terminal)
    └── Secure routing into the external payment ecosystem
        → authorization outcome returned per attempt (approved / declined)
        └── Durable transaction record with tracked lifecycle
            (initiated → authorized → captured → settled; declined; canceled)
```

1. **Enrolled merchant relationship** — the gateway processes on behalf of an enrolled merchant holding an account and credentials; without it there is no payee, no settlement destination, no one to serve (a payer-side product is a wallet, not a gateway).
2. **Acceptance surface for the merchant's channels** — an interface through which payment requests enter (hosted page, embedded fields, server API, terminal). Without it, the product is back-end processing infrastructure with no merchant-facing acceptance function.
3. **Authorization outcome via the external payment ecosystem** — the gateway transmits payment data securely toward the authorizing side (processor/acquirer/networks) and returns an approve/decline result per attempt. Without this, it is a form builder or data collector, not a gateway.
4. **Durable, retrievable transaction record with lifecycle** — each attempt is recorded and its state tracked (authorization, capture, settlement, decline, cancellation) as the system of record for the merchant's payments. Without this, settlement, refunds, reconciliation and disputes are impossible — and the "gateway" degenerates into a pass-through pipe.

Deliberately **not** in L0 (checked against the historical sample): specific integration styles (hosted page vs API — the 1996-era product used server APIs and hosted redirects), payment method breadth (cards-only historical products qualify), tokenization, webhooks, dashboards, 3DS/SCA, fraud tooling, refund/dispute management, in-person support, multi-currency, platforms/marketplaces.

§24 historical check: Authorize.Net (1996-era, decoupled from merchant acquiring, card-centric, no bundled platforms) satisfies all four properties. Regional/acquirer-hosted gateways and terminal-first gateways satisfy them without any modern surface. The definition does not over-fit to the API-first generation.

### L1 — Common Mature Structure

Present across the modern sample; expected in market but not definitional:

- Multiple acceptance surfaces (hosted payment page, embedded fields/components, server API, no-code payment links, mobile SDKs)
- Payment-method breadth beyond cards (wallets, bank debits/transfers, local methods) with per-method enablement
- Tokenization / vault (store payment details under a customer record; reuse for one-click and recurring charges; network tokens, account updaters)
- Authorization/capture split with cancel/void, refund (full/partial), reversal, authorization adjustment
- Webhooks / server-to-server notifications of payment-status changes
- Merchant dashboard: transaction search/inspection, manual refunds, dispute response, reports
- Sandbox/test environment with simulated payments and a go-live process
- Risk/fraud screening at transaction time (rules, scores, review queues)
- Card authentication handling (3DS/SCA) inside the payment flow
- Statement descriptor control; merchant reference/metadata fields for reconciliation
- Settlement visibility: balances, settlement reports, payouts to the merchant's bank account
- Dispute/chargeback lifecycle management (view, evidence submission, status)

### L2 — Variant / Optional Structure

Depends on segment, geography, regulation, business model:

- In-person/terminal hardware and omnichannel unification (online + POS on one platform)
- Platform/marketplace posture: sub-merchant onboarding (KYC), split payments, payouts to third parties, platform fees
- Merchant-of-record vs own-merchant-account posture (Authorize.Net requires a separate merchant account; modern platforms bundle acquiring/underwriting)
- Regional regulatory packs (PSD2/SCA in Europe, country-specific compliance guides)
- Acceptance-rate optimization machinery (retries/auto-rescue, network tokens, account updater, AI-driven acceptance optimization)
- Bundled adjacent products (billing/subscriptions, invoicing, issuing, capital, identity verification, crypto on-ramps) — vendor bundling, not the Type
- Pricing/packaging models (flat-rate self-serve vs interchange++ contract)
- Local-method depth per geography

### L3 — Vendor-specific Structure (stays in Research Notes)

- Stripe: PaymentIntent/SetupIntent/Charge naming, client-secret pattern, Radar/Radar Plus, Link, Checkout Sessions, Connect, Atlas, Financial Connections, 22-char descriptor limit (precision kept out of final doc)
- Adyen: Customer Area, Drop-in/Components, Auto Rescue, Adyen Giving, sessions vs advanced flow, Pay by Link
- Braintree: nonces, Vault, Hosted Fields vs Drop-in UI, Grant API / Forward API, Venmo, Braintree Marketplace
- Checkout.com: Flow, Intelligent Acceptance, Checkout Business Account
- Authorize.Net: apiLoginId/transactionKey, duplicateWindow setting, SIM/AIM classic integration names

## Vendor-specific Findings

- Stripe's client-secret confirmation flow and Radar rule engine are implementation/branding, not structural.
- Adyen's Customer Area branding and Auto Rescue retries are vendor realizations of dashboard and retry-recovery commonalities.
- Braintree's Grant/Forward APIs (sharing vaulted payment methods across merchants / to third parties) are unusual extensions with no counterpart in the other sampled products — product-specific.
- Checkout.com's Intelligent Acceptance is a branded realization of acceptance-rate optimization.
- Authorize.Net's duplicateWindow and merchant-defined user fields are long-standing but not universal mechanisms.

## Rejected Findings

- "A gateway is only card processing" — rejected: all modern sampled products treat cards as one method family among wallets/bank transfers; cards are the historical core method, not the definition.
- "A gateway must bundle a merchant account / acquiring" — rejected: Authorize.Net explicitly requires a separate merchant account; the bundled-acquiring model is a modern packaging variant (L2), not definitional.
- "A gateway is a hosted checkout page" — rejected: hosted page is one acceptance surface; API-only integrations are first-class in every sampled product.
- "Subscriptions/recurring billing is part of the gateway" — rejected: recurring is an L1/L2 capability (vaulting + off-session charges) plus a separate billing Type; sampled products bundle full billing products alongside the gateway.
- "Webhooks are definitional" — rejected: they are the modern notification mechanism; the definitional content is "payment status changes are communicated to the merchant server," which predates webhooks.

## Boundary Findings

1. **vs Payment Processing Platform (sibling, §08):** the classic model separates gateway (merchant-facing acceptance + secure transmission) from processor (connection to acquirers/networks, authorization & settlement machinery). Every modern sampled product bundles both under one platform; Authorize.Net keeps them separable (requires external merchant account). Structural test: gateway centers on the merchant-facing acceptance surface + authorization outcome + transaction records; processing platform centers on the acquiring/settlement backend. Boundary is a stack-position gradient, heavily blurred by modern bundling — flagged for joint review; the two leaves likely overlap on the same products.
2. **vs Payment Orchestration Platform (sibling, §08):** orchestration abstracts *above multiple* gateways/PSPs (routing, normalization, failover); a gateway routes within its own acquiring connections and is itself the routable target. None of the sampled products primarily positions as a multi-PSP abstraction layer. Distinct Type; boundary holds.
3. **vs Checkout Platform (05.06):** checkout centers on the payer-facing conversion experience (cart→order UX); the gateway centers on authorization + transaction lifecycle. Overlap zone: gateways provide hosted payment pages/checkout as acceptance surfaces. Test: remove acceptance/authorization/settlement → checkout platform remains a conversion surface; remove the buying UX → gateway remains.
4. **vs Digital Wallet / Mobile Wallet / Stored Value Wallet (§08):** wallets are payer-side (hold the consumer's credentials or value); gateways are payee-side (serve enrolled merchants). Wallets appear *inside* gateways as payment method types (Apple/Google Pay, PayPal, Venmo). Boundary holds by whose money/credential is managed.
5. **vs Merchant Payment Platform (sibling, §08):** terminology sibling; sampled products self-describe as "payments platforms" serving merchants. No structural difference observed at research depth — probable Alias/overlap; flagged for joint review.
6. **vs Retail POS (05.10):** POS composes the sale (catalog, cart, staff, checks) and *uses* a payment stack; the gateway *is* the card-acceptance component. Overlap: gateway-provided terminals (Stripe Terminal, Adyen terminals, Braintree in-store). Test: remove the payment-routing/lifecycle machinery → gateway collapses into POS's tender step; remove sale composition → gateway remains.
7. **vs Billing Platform / Subscription Billing (§08):** billing decides what/when to charge (plans, invoices, dunning); the gateway executes charges and records transactions. Bundled billing products in the sample (Stripe Billing, Braintree Recurring Billing) are adjacent Types, not the gateway core.
8. **vs Peer-to-peer Payment Application (§08):** P2P transfers money between consumers; no enrolled-merchant payee, no sales-channel acceptance surfaces. Boundary holds via L0 property 1.

## Uncertainties

- **Checkout.com depth:** only docs-home-level evidence gathered (features/structure confirmed; operational flow detail not fetched). Lifecycle claims for Checkout.com rest on docs-home + product-page naming; treated as Layer A for structure, not for flow detail.
- **Notification mechanisms pre-webhook:** the Authorize.Net webhook/silent-post detail was not fetched; "status change notification" as a commonality is supported directly for Stripe/Adyen/Braintree and structurally implied for the others.
- **Gateway-vs-processor line in the directory:** whether the taxonomy intends Payment Gateway = pure front layer and Payment Processing Platform = full-stack is not decidable from product research alone (products bundle both). Recorded as a boundary issue rather than resolved unilaterally.
- **Precise operational facts** (settlement timing windows, capture expiry windows, retry counts, descriptor length limits, SCA exemption thresholds) deliberately not recorded: not systematically researched across the sample; would violate the precision rule.
- **Regional gateways** (e.g., iDEAL-centric acquirers, UPI stacks) were not sampled; the L0 is built to accommodate them (acceptance surface + authorization outcome + lifecycle are method-agnostic), but no direct evidence was collected.

## Final Synthesis

A Payment Gateway is best understood as the **merchant-side acceptance-and-authorization layer of electronic payments**: an enrolled merchant connects its sales channels (web shop, app, call center, terminal) to the gateway through one of several acceptance surfaces; the gateway securely carries each payment request into the external payment ecosystem, obtains an authorization decision, and records the payment as a durable transaction whose lifecycle (authorize → capture → settle, with decline/cancel/refund/dispute branches) it tracks as the system of record.

Everything else commonly associated with the category — breadth of payment methods, hosted checkout pages, tokenization/vaults, webhooks, dashboards, fraud scoring, 3DS/SCA, settlement reporting, terminals, platform/marketplace splits — is mature-market structure layered on that spine, or a variant of packaging (bundled acquiring, platforms, regional compliance). The definition is validated against a 1996-era decoupled gateway (Authorize.Net) as well as four modern API-first platforms, so it does not over-fit the current dominant implementation.

The two structural ambiguities worth joint review: (1) Payment Gateway vs Payment Processing Platform — one bundled product family, two stack positions; (2) Payment Gateway vs Merchant Payment Platform — probable terminology overlap.
