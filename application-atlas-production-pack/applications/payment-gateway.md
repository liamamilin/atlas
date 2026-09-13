# Payment Gateway

## Overview

A **Payment Gateway** is a merchant-side service that accepts payment requests from a merchant's sales channels, securely routes them into the external payment ecosystem (card networks, banks, wallets) for authorization, and records each payment as a durable transaction whose lifecycle it tracks — from authorization through capture and settlement, with decline, cancellation, refund and dispute branches.

The defining core is small:

```text
Enrolled Merchant (account + credentials)
└── Acceptance surface (the merchant's channel submits a payment request)
    └── Secure routing toward the authorizing side
        → authorization outcome returned per attempt (approved / declined)
        └── Durable transaction record with a tracked lifecycle
```

Everything else commonly associated with the category — many payment methods, hosted checkout pages, saved-payment vaults, webhooks, dashboards, fraud screening, card authentication, settlement reports, in-person terminals — is standard capability layered on that spine, not what makes the product a gateway. The definition deliberately holds for older, separately-banked gateways that only exposed a server API and processed cards, as well as for modern all-in-one payment platforms.

When the primary job shifts to composing the sale itself (catalog, cart, staff) the product is a Retail POS; when it shifts to deciding what and when to charge (plans, invoices, dunning) it is a Billing Platform; when it shifts to routing traffic *across multiple* gateways it is a Payment Orchestration Platform; when the payer-side credentials or stored value are the point, it is a Digital Wallet.

## Users & Context

The gateway serves **merchants** — businesses that sell goods or services and need to get paid electronically. Three merchant-side roles matter:

- **Integrators / developers** — connect the merchant's sales channels (web shop, mobile app, call-center system, point-of-sale) to the gateway, choose the acceptance surfaces, and handle the server-side logic that creates payment requests and reacts to status changes.
- **Payment operations staff** — work in the gateway's merchant dashboard day to day: inspect transactions, issue refunds, respond to cardholder disputes, reconcile gateway records against the merchant's own orders, and monitor settlement.
- **Business owners / finance** — consume reports, settlement visibility, and fraud/acceptance metrics.

A fourth participant, the **payer**, never holds an account in the gateway. They interact transiently with its acceptance surfaces — entering card details into a hosted page or embedded form, or tapping a terminal — and their relationship is with the merchant, not with the gateway.

Typical contexts: e-commerce checkout, in-app purchases, recurring subscription charges, invoice payment, and in-person card acceptance. One gateway commonly serves all of a merchant's channels.

## Core Model

### The Defining Core

Four properties. Remove any one and the product is no longer recognizable as a payment gateway:

- **Enrolled merchant relationship.** The gateway processes payments on behalf of an enrolled merchant that holds an account with credentials. Without a merchant there is no payee, no settlement destination, and no one to serve — a payer-side product is a wallet, not a gateway.
- **Acceptance surface.** An interface through which the merchant's sales channels submit a payment request — an amount plus payment details. Without it, the product is back-end infrastructure with no merchant-facing acceptance function.
- **Authorization outcome from the external payment ecosystem.** The gateway carries the payment data securely toward the authorizing side (acquirer/processor/card network or equivalent) and returns an approved-or-declined result for each attempt. Without this it is a form builder or data collector.
- **Durable transaction record with a tracked lifecycle.** Every attempt is recorded, and its state evolves — initiated, authorized, captured, settled, declined, canceled — with the gateway acting as the merchant's system of record for payments. Without this, refunds, reconciliation, disputes and settlement reporting are impossible.

### What Mature Products Add

These capabilities are near-universal in current products and make the gateway practical, but they do not define the Type:

- **Multiple acceptance surfaces** — a hosted payment page, embeddable card-entry fields or components, a direct server API, no-code payment links, mobile SDKs, and in-person terminal integrations; most merchants combine several.
- **Payment-method breadth** — cards are the historical core, but mature gateways carry wallets, bank debits and transfers, and country-specific local methods, with per-method enablement.
- **Authorization/capture split** — an approval can be obtained first and funds captured later, with cancel/void, full and partial refunds, and reversals as lifecycle operations.
- **Vault / tokenization** — payment details are replaced by reusable tokens bound to a customer record, enabling one-click checkout, recurring charges, and off-session payments.
- **Server notifications** — payment status changes are pushed to the merchant's server (webhooks in current products) so the merchant can fulfill orders on facts, not assumptions.
- **Merchant dashboard** — transaction search and inspection, manual refunds, dispute response, reports; test-environment access and a go-live process.
- **Risk screening and card authentication** — transaction-time fraud evaluation (rules, scores, reviews) and 3D-Secure-style cardholder authentication handled inside the payment flow.
- **Reconciliation aids** — merchant reference fields / metadata linking each gateway transaction to the merchant's own order, plus statement-descriptor control over what payers see on their statements.
- **Settlement visibility** — balances, settlement reports, and payouts toward the merchant's bank account.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:    Enrolled merchant        Implementations:  self-serve account + API keys, contract onboarded account, sub-merchant under a platform
Concept:    Acceptance surface       Implementations:  hosted page, embedded fields/components, server API, payment link, terminal SDK
Concept:    Transaction lifecycle    Implementations:  state machines with product-specific status labels; exact names vary by product
Concept:    Payment details          Implementations:  raw card entry on hosted/embedded surfaces, wallet redirects, bank-authorised debits, stored tokens
Concept:    Status change delivery   Implementations:  webhooks (current standard), earlier polling/redirect callbacks
```

A reader who has only seen one modern hosted-checkout product should still be able to recognize an older server-API-only gateway from the same core.

## How It Works

### Connect the merchant's channels

```text
Enroll the merchant (account, credentials, business verification)
→ choose acceptance surfaces (hosted page / embedded fields / server API / terminal)
→ enable payment methods and configure descriptor, currency, risk posture
→ integrate in a test/sandbox environment with simulated payments
→ pass the go-live review and switch to live processing
```

### Process a payment

```text
Merchant's channel creates a payment request (amount, currency, reference)
→ acceptance surface collects payment details from the payer
→ gateway transmits the details securely toward the authorizing side
→ additional cardholder authentication if required (e.g. 3D Secure)
→ authorization outcome returned: approved or declined
→ approved: funds are captured (immediately, or later under the auth/capture split)
→ captured transactions are settled and paid out to the merchant
→ every state change is recorded and can be pushed to the merchant's server
```

A declined attempt returns a result the merchant's channel can act on — typically by letting the payer retry with another method. Because attempts are attached to a single payment record, retries and failures remain traceable instead of spawning orphaned charges.

### Operate after the payment

```text
Refund (full or partial) against a captured transaction
→ respond to cardholder disputes with evidence through the dashboard/API
→ reconcile transactions to orders via references/metadata
→ monitor settlement and payouts; export reports
```

## Interfaces

### Hosted payment page / checkout

The gateway's own payer-facing page, reached by redirect or link.

- Purpose: collect payment details and complete the payment without the merchant touching sensitive data.
- Typical information: amount, order description, enabled payment methods, brand styling.
- Primary actions: choose method, enter details, confirm; payer is returned to the merchant with an outcome.

### Embedded fields / components

Card-entry or wallet UI embedded in the merchant's own page or app.

- Purpose: keep the buying experience on the merchant's surface while sensitive data flows directly to the gateway.
- Primary actions: render method-specific inputs, tokenize the entered details, hand a token/confirmation to the merchant's server to authorize.

### Server API

The programmatic surface for the merchant's backend.

- Purpose: create and confirm payment requests, capture, cancel, refund, manage customers/tokens, retrieve transactions.
- Typical information: request/response objects carrying amount, payment details or tokens, status, outcome, references.
- Primary actions: create, confirm, capture, cancel, refund, search.

### Merchant dashboard

The operational console for merchant staff.

- Purpose: run day-to-day payment operations without code.
- Typical information: transaction lists with status/outcome, single-transaction detail (attempts, method, risk evaluation), disputes, balances and settlement, reports.
- Primary actions: search/inspect, refund, respond to a dispute, export, configure methods and settings.

### Notifications (webhooks)

Server-to-server messages about status changes.

- Purpose: let the merchant's systems react to facts (payment succeeded, failed, disputed, funds settled) asynchronously.
- Typical information: event type, affected transaction, status.
- Primary actions: receive, verify, acknowledge; drive fulfillment logic.

### Terminal integration

SDKs and certified readers for in-person acceptance.

- Purpose: extend the same payment processing to physical locations.
- Primary actions: collect a card-present payment, hand over a receipt, record the transaction in the same lifecycle as online ones.

## Important Rules / Behaviors

- **Authorization is not money in the bank.** An approved authorization reserves funds on the payer's instrument; the money moves when the payment is captured and settled. Products support an authorize-first/capture-later model, and an authorization that is never captured is cancelled or expires.
- **The lifecycle is authoritative and durable.** Every attempt — successful or not — is recorded with its outcome. A decline returns the payment to a retryable state rather than destroying the record; cancellations release held funds and invalidate future attempts.
- **Sensitive payment data is kept out of the merchant's systems.** In hosted and embedded surfaces, details flow directly from the payer to the gateway and are returned only as tokens. This division of labor — the gateway carrying the compliance burden for card-data handling — is a structural reason the Type exists; the merchant's server works with tokens and references, not raw numbers.
- **Some payments are asynchronous.** Certain methods (e.g. bank-based debits) can take days rather than seconds to confirm; the payment sits in a processing state and the merchant is expected to fulfill on the confirmed notification, not the initial submission.
- **Refunds are bounded by what was captured.** Refunds (full or partial) apply to captured transactions; reversals/cancellations apply to authorized-but-uncaptured ones. Mixing them up is the classic operational error.
- **Disputes run on their own clock.** A cardholder dispute (chargeback) opens a case against a settled transaction, with a defined window to submit evidence and an eventual win/loss decision that reverses funds if lost. The gateway surfaces and manages the case; the merchant argues it.
- **Risk and authentication gate the attempt.** The gateway may decline, challenge (3D-Secure-style authentication), or flag for review before authorization, based on risk rules and regulatory requirements in the relevant market.
- **What the payer sees matters.** Statement descriptors (controlled by the merchant) and payer-facing messaging are product surfaces, because confusion about a charge is a direct driver of disputes.
- **Exact status labels vary by product.** The lifecycle above is conceptual; each product names its states differently and the mapping between API states and dashboard labels is product-specific.

## Variants

- **API-first self-serve** — one gateway serving startups through enterprises via developer integration; hosted page and embedded components emphasized (e.g. Stripe).
- **Enterprise unified-commerce platform** — contract-based, single platform for online and in-person payments with strong reporting and regional compliance tooling (e.g. Adyen, Checkout.com).
- **Classic decoupled gateway** — card-processing front end that requires the merchant to hold a separate bank merchant account; gateway and acquiring are distinct businesses (e.g. Authorize.Net).
- **Vault-centric mid-market gateway** — emphasis on stored customers/payment methods and wallet methods (e.g. Braintree).
- **In-person / omnichannel** — terminal hardware and SDKs bringing store payments onto the same platform as online ones.
- **Platform / marketplace posture** — the gateway onboards sub-merchants (KYC), splits payments, and pays out to third parties; the "merchant" becomes many merchants under one platform.
- **Bundled-suite posture** — the gateway shipped alongside billing, invoicing, issuing or capital products by the same vendor; the adjacent products remain separate Types.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Payment Processing Platform | the acquiring/settlement backend of the same stack; modern vendors bundle gateway + processing in one product, so the boundary is stack position, not structure — flagged for joint review |
| Merchant Payment Platform | terminology sibling; no structural difference observed at research depth — flagged for joint review |
| Payment Orchestration Platform | sits *above* multiple gateways/PSPs and routes between them; a gateway is itself one of the routable targets |
| Checkout Platform | centers on the payer-facing conversion experience (cart → order UX); the gateway centers on authorization and the transaction lifecycle — hosted payment pages are the overlap zone |
| Digital Wallet / Mobile Wallet / Stored Value Wallet | payer-side: holds the consumer's credentials or stored value; the gateway is payee-side and treats wallets as payment method types |
| Billing Platform / Subscription Billing | decides what and when to charge (plans, invoices, dunning); the gateway executes the charge and records the transaction |
| Retail POS | composes the sale (catalog, cart, staff, checks) and uses a payment stack; the gateway is the card-acceptance component inside it |
| Peer-to-peer Payment Application | moves money between consumers; no enrolled merchant, no sales-channel acceptance surfaces |
| Fraud Detection Platform | standalone risk decisioning across many signals and industries; a gateway's risk layer is transaction-time screening inside the payment flow |
| Transaction Monitoring / AML Platform | compliance-side surveillance of money flows; the gateway's defining job is authorization and lifecycle, not surveillance |

The most important boundary is against the Payment Processing Platform: in the classic model the gateway captured and securely transmitted payment data while a separate processor/acquirer did the authorizing and settling, but every modern product researched bundles both, so the two directory leaves overlap on the same products and differ mainly in emphasis.

## Representative Products

- Stripe — API-first, self-serve, developer-centric payments platform
- Adyen — enterprise unified-commerce payments platform (online + in-person)
- Braintree (a PayPal service) — vault-centric gateway with bundled merchant account
- Checkout.com — enterprise API-first acquiring/payments platform
- Authorize.Net — long-running classic gateway; used as the historical check that the definition does not over-fit the modern API-first generation

## Sources

Research date: **2026-09-06**

- Stripe — Payments overview: https://docs.stripe.com/payments
- Stripe — Payment Intents API guide: https://docs.stripe.com/payments/payment-intents
- Stripe — Payment / Setup Intent lifecycle: https://docs.stripe.com/payments/paymentintents/lifecycle
- Adyen — Online payments documentation: https://docs.adyen.com/online-payments
- Braintree — Developer documentation home: https://developer.paypal.com/braintree/docs
- Checkout.com — Documentation home: https://docs.checkout.com/
- Authorize.Net — Developer center getting-started pages: https://developer.authorize.net/hello_world/

> Sourcing limitation: Checkout.com evidence was gathered at documentation-home level (structure and feature set confirmed; operational flow detail not fetched), and per-product pricing, contract terms, and dispute-flow detail pages were not consulted for any product. Precise operational facts (settlement timing windows, capture expiry windows, retry counts, descriptor length limits, authentication thresholds) are therefore intentionally not stated in this document. Detailed observations and evidence calibration are recorded in the paired Research Notes.
