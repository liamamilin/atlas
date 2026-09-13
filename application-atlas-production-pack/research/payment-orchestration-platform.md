# Research Notes — Payment Orchestration Platform

Research date: 2026-09-06

## Research Goal

Understand what a Payment Orchestration Platform actually is as an Application Type: what objects exist inside it, what its per-transaction workflow is, how it differs from the adjacent Payment Gateway / Payment Processing Platform Types, and which capabilities are definitional vs. common market structure vs. vendor-specific.

## Initial Boundary (working hypothesis before research)

- Hypothesis: an orchestration platform sits **above** multiple payment service providers (PSPs/gateways/acquirers), gives the merchant one integration, routes each transaction to one of the connected providers, and normalizes results/lifecycle across them.
- Nearest neighbors: Payment Gateway (a routable target, already documented in this Atlas), Payment Processing Platform, Fraud Detection Platform, Checkout Platform, Billing Platform.
- Key uncertainty going in: is "routing" required for the Type, or is multi-provider aggregation alone enough? Is the vault definitional or common?

## Research Questions

1. What are the core objects? (connections, transactions, routing rules, vault/tokens, workflows)
2. What is the per-transaction flow, including retries/failover?
3. Whose merchant accounts are used — the orchestrator's or the merchant's own PSP accounts?
4. What routing models exist (static, conditional, split/percentage, failover/cascading)?
5. How is normalization achieved (statuses, decline codes, settlement data)?
6. What role do vault/tokenization, 3DS, and fraud services play — core or common?
7. What interfaces exist (dashboard, API, no-code workflow editor, embedded checkout)?
8. Where is the boundary with Payment Gateway, and with fraud/checkout/billing Types?
9. Historical check: do older/simpler products (vault + gateway abstraction, no smart routing) still fit the Type?

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| Spreedly | The original "vault + gateway abstraction" orchestrator; extensive Tier-1 docs | API-first, vault-centric, mid-market/enterprise |
| Primer | Workflow/no-code orchestration; merchant-side payments teams | Developer + no-code, digital businesses |
| Gr4vy | Embedded-checkout-first orchestration; very detailed docs | Embedded/API, platforms & merchants |
| IXOPAY | European white-label orchestrator for PSPs/enterprises; multi-tenant | White-label infrastructure, PSP-side + enterprise |

Sample covers: different product philosophies (vault-centric / workflow-first / embedded-first / white-label), different customer tiers, and two geographies (US, UK/EU). All four have Tier-1 operational documentation that was directly fetched.

## Sources

All fetched 2026-09-06 (Tier 1 — official operational documentation):

- Spreedly — docs home, overview, workflow user guide, routing rules guide, recover user guide: https://developer.spreedly.com/docs/overview.md , /docs/workflow-user-guide.md , /docs/routing-rules-user-guide.md , /docs/recover-user-guide.md (plus llms.txt index)
- Primer — docs home, concepts overview, payment lifecycle, fallbacks, workflows overview, reconciliation overview: https://primer.io/docs , /docs/concepts/payment-lifecycle.md , /docs/payment-services/fallbacks.md , /docs/workflows/overview.md , /docs/reconciliation/overview.md
- Gr4vy — docs home, llms.txt index, Flow overview, card transactions flow, merchant accounts, transaction statuses, vaulting: https://docs.gr4vy.com/ , /guides/dashboard/flow/overview.md , /guides/dashboard/flow/card-transactions.md , /guides/features/merchant-accounts/overview.md , /guides/api/statuses/transactions.md , /guides/features/vault-forwarding/overview.md
- IXOPAY — user manual getting started, connector section, Meta-Connector routing page, transactions section, tokenization section, developer hub reference overview: https://documentation.ixopay.com/manual/docs/getting-started , /manual/docs/connector , /manual/docs/connector/routing-cascading-balancing-fallback , /manual/docs/transactions , /manual/docs/tokenization , /docs/reference

Source-access limitations:

- `docs.primer.io` was unreachable (2 transport errors); Primer documentation was fetched successfully from the same content at `primer.io/docs` — evidence quality unaffected.
- Pricing pages, contract terms, and per-connection credential specifics were not consulted for any product; no pricing or numeric commercial claims are made.
- IXOPAY's decline-code list and Spreedly's Recover modes are product-specific normalizations; they are recorded here and not generalized.

## Product Observations

### Spreedly (evidence layer A unless noted)

- Self-description: "securely store credit cards and use them to transact against any number of payment gateways and third party APIs"; "universal tokenization" — a Spreedly token usable against multiple gateways; card data never touches the merchant's servers.
- Core objects: **environments** (org → environments), **gateways** (provisioned instances of supported gateway types, created with the merchant's own gateway credentials), **payment methods** (vault tokens with states: retained/cached/redacted/used), **transactions** (every interaction with a gateway/receiver creates a transaction record), **receivers** (payment-method distribution endpoints), **merchant profiles** (hold SCA/fraud providers).
- **Workflows (Composer)**: low-code UI designer; routing options = single (static) gateway, split volume between two gateways by %, conditional routing rules; a `workflow_key` is passed in the API (or a Default Workflow is used); changes apply immediately to live traffic.
- **Routing rules**: conditional steps with dimensions — currency, amount, transaction metadata (key/value), BIN range, payment method type, payment method gateway type (for third-party tokens), and (with Advanced Vault) BIN metadata: card brand, category, type, issuing country, issuing bank, BIN type. Conditions evaluated top-down; final "Else" step routes if no condition matches.
- **Recover** (optional paid service): automatic retry of declined transactions on backup gateways; modes (Outage / Standard + Outage); up to two Recover gateways; configurable via normalized `failure_reason` values mapped across gateways; network-token attempt + PAN-retry options on workflow steps.
- **Normalization**: "normalized response values" and "normalized request and response fields" across gateways; gateway error code mapping; transaction transcript (human-readable exchange with the gateway, retained for a defined period).
- **Vault**: Advanced Vault (lifecycle management, data enrichment, network tokenization), third-party vaulting (store at gateway's vault as ThirdPartyToken, locked to that gateway), import/export of payment methods, card fingerprints, stored credentials.
- **App**: web application for environments, connections, workflows, analytics ("review data & analytics of your orchestration strategy"), RBAC roles (Administrator / Environment Manager / Workflow Manager), activity log.
- Fraud/identity services integrated via "Dodgeball" (checkpoints, external services: Sift, Forter, Socure, Veriff, 3DS Global) — vendor-specific packaging.

### Primer (evidence layer A)

- Self-description: "unified intelligence for payments"; product suites: **Accept** (Checkout, Centralized vault, Workflows), **Optimize** (Network Tokenization, Fallbacks, 3D Secure, AI Companion), **Manage** (Observability, Monitors, Reconciliation, Costs Overview, Global Accounts).
- Core objects: **Payment** (unified object), **payment attempt** (per-processor attempt; approve/abort endpoints), **payment method token** (centralized vault), **Connection** (connected processor/service), **Workflow** (no-code automation), **client session** (checkout session token).
- **Unified lifecycle**: "All Primer payments conform to a unified payment lifecycle, which makes them work the same way regardless of the payment services you need." Statuses: PENDING, AUTHORIZED, SETTLING, SETTLED, PARTIALLY_SETTLED, DECLINED, FAILED, CANCELLED. The API enforces the state machine (validation error on illegal action per status; per-status action table documented).
- **Workflows**: no-code; native apps provide triggers/actions (Payment created / Payment status updated / Web request received / Monitor event / Dispute status update triggers; Authorize / Capture / Refund / Cancel / Decline / Perform 3DS / Continue payment flow / Send web request / Send card details / Send email actions); conditions, split utility (A/B analysis), templates, export/import, monitoring with failed-run webhooks.
- **Fallbacks**: payment recovery service routing to a backup processor when the primary fails; triggered on standardized decline conditions (gateway-rejected, soft issuer declines incl. "Do Not Honor"/"Issuer Temporarily Unavailable", application errors); 3DS data carried into the fallback authorization so the customer doesn't re-authenticate; incompatible with processor-side 3DS.
- **Standardization**: unified decline codes ("Primer's Unified Mapping Standard"), standardized fields across processors (status, error decision type, error decline type, error decline reason).
- **Reconciliation**: unified settlement report across processors; track settlements, match transactions, surface payout discrepancies; costs overview for provider cost comparison.
- **Observability**: dashboards (payments, sales, refunds, declines, 3DS, sales recovery, network tokenization), custom dashboards, monitors (e.g., processor outages, fallback usage), payment timeline showing each event's request/response ("full transparency into everything that's happened to your payment").
- Checkout: Universal Checkout / Drop-in / Headless SDKs; manual payment approval from the merchant's backend; idempotency keys.

### Gr4vy (evidence layer A)

- Self-description: "payment orchestration platform that lets you connect multiple payment processors, route transactions intelligently, and manage your entire payments stack from one place."
- Core objects: **connection** (payment processors, anti-fraud services, digital wallets — large catalog: Adyen, Stripe, Braintree, PayPal, Worldpay, Nuvei, dLocal, Cybersource, Chase, Fiserv, etc., plus per-method configurations via each processor), **transaction** (with statuses), **payment method** (vault), **buyer**, **merchant account** (container for connections/rules/transactions; multi-merchant is a premium feature), **Flow rules**, **webhooks**, **reports**.
- **Flow**: dashboard/API-configurable rules over "flows" (checkout experience, card transactions, other transactions); actions = decline (with custom error code), route to connection, 3-D Secure control; rules = conditions + outcome, evaluated top-down, first match wins.
- **Routing mechanics**: sequential routing — connections tried in order until success; automatic retries on technical failures and "retriable declines" (soft issuer declines, technical acquirer codes); retry decision logic prioritizes ISO 8583 response codes (documented retriable-code list) over generic error codes; merchant advice code blocks retry.
- **Split routing**: distribute traffic across up to 4 variants by percentage (A/B testing, load balancing, gradual rollout); failover stays within a variant; variant performance compared in Insights.
- **Instruments & message transformations**: route with PAN or Network Token; transformations include MIT flagging and co-badged scheme routing (e.g., force Cartes Bancaires); account-updater-driven payment method replacement and retry.
- **Conditions**: amount, currency, anti-fraud decision, browser language, BIN range, card country/issuer/product/scheme/source/type, customer country, gift-card BIN, subsequent-payment/merchant-initiated flags, metadata (string/numeric), payment source, product categories/types, SKUs, split-routing probability.
- **Transaction statuses**: processing, buyer_approval_pending, authorization_succeeded/failed/declined, capture_pending/succeeded, authorization_void_pending/voided; state diagrams for authorize-then-capture and direct capture; timeout handling with background retries (documented 24h resolution bound) and webhook outcomes.
- **Vaulting**: tokenize (Secure Fields/mobile keep PAN off merchant servers), PSP tokenization (provision provider-specific tokens), Vault Forwarding (proxy stored card data to third-party PCI-compliant endpoints: booking, loyalty, OMS), network token lifecycle, token import.
- **3DS**: Embed/Hosted/Native/External approaches; issuer-mandated 3DS overrides rules.
- **Anti-fraud**: connect providers (Cybersource Decision Manager, Forter, Riskified, Sardine, Sift); primary + silent-mode services for comparison/migration; decision used in Flow conditions; manual review queues.
- **Operations**: settlement report ingestion with per-processor mappings (Adyen, Braintree, Stripe, Nuvei, dLocal, PayPal, Cybersource, BlueSnap, Chase Orbital, Trustly...), reconciliation against system records, monitoring & alerting on authorization rates, SSO, roles & permissions.

### IXOPAY (evidence layer A)

- Self-description: platform to "scale your payments globally"; user manual organized around tenants, merchants, connectors, transactions, risk management, tokenization, post-processing.
- Core objects: **tenant / sub-tenant** (white-label multi-level structure: "used by our White Label customers to create a multi-level sub-structure"), **merchant profile** (one per brand/entity/market or per PSP credential set), **API user** (per merchant, for the Transaction API), **connector** (a configured integration to one PSP/acquirer using an **adapter**; always bound to a merchant profile; one connector per credential set/payment method/endpoint), **Meta-Connector** (routing container), **transaction** (list/details across connectors), **customer profiles** (tokenization), **risk checks**.
- **Smart Routing Engine (Meta-Connector)**: rule editor with drag-and-drop **conditions** and **actions**; conditions include credit-card brand, BIN country/level/type, BIN/IBAN regular-expression checks, IBAN position value, customer billing country, customer IP country, random load balancer (percentage), transaction extra data, is-recurring, transaction type, connector of initial transaction, transaction currency/amount, risk score, chargeback count/volume, debit/preauth count/volume; action = "Route to Connector"; then/else branching; default connector when no action matches.
- **Fallback routing**: backup connector added directly after the primary; triggered on soft/recoverable decline codes; hard (non-recoverable) declines listed and never re-routed (e.g., insufficient funds, fraudulent card, expired card, 3DS failure); fallback does not apply to void/capture/refund; "Customers will not notice any issues with the first provider, as the transaction is routed to another PSP by the IXOPAY platform in the background."
- **Recurring routing**: option to re-route recurring transactions or pin them to the initial transaction's connector.
- **Tokenization**: customer profiles for tokenized repeat purchases; Account Updater (Mastercard/Visa/Discover); Network Token Services (scheme tokens to keep data current, reduce PCI scope, lower fees).
- **Post-processing**: reconciliation and provider settlement retrieval via connector-level data fetchers; statistics; data export tool.
- **Integration options**: full-page redirect, hosted payment pages, hosted fields (payment.js), server-to-server; callbacks; 3DS; scheduler; risk checks; DCC; pay-by-link; virtual terminal (MOTO); PCI data migration.
- **Adapters**: catalog of technical PSP/acquirer integrations (adapters.ixopay.com); ISO 8583 adapter family and terminal IDs for card-present.

## Cross-product Comparison

| Dimension | Spreedly | Primer | Gr4vy | IXOPAY | Layer |
|---|---|---|---|---|---|
| Multiple provider connections under merchant's own accounts | gateways provisioned with merchant credentials | Connections (processors) | connections (processors/fraud/wallets) | connectors (per PSP credential set) | **L0** |
| Single normalized entry point | single API + workflow_key | single API + client session | single API + Embed/SDKs | single Transaction API | **L0** |
| Per-transaction provider-selection decision | workflow steps + routing rules + split volume | workflow authorize action + fallbacks | Flow rules + sequential/split routing | Meta-Connector rules + load balancer | **L0** |
| Provider-independent transaction record, normalized lifecycle | transaction records + normalized values | unified lifecycle + state machine | transaction statuses + state diagrams | transaction list/details across connectors | **L0** |
| Failover/retry on backup provider | Recover (modes, 2 backup gateways) | Fallbacks (standardized triggers) | automatic retries/cascading (ISO-code logic) | fallback routing (soft vs hard declines) | L1 |
| Rule condition dimensions | currency/amount/metadata/BIN/BIN-metadata/method type | workflow conditions | amount/BIN/card/customer/metadata/fraud-decision/SKU... | card/IBAN/customer/transaction/risk-score/chargeback-stats | L1 |
| Percentage split / load balancing | split volume (2 gateways) | split utility (analysis) | split routing (up to 4 variants) | random load balancer | L1 |
| Platform vault across providers | universal tokenization, Advanced Vault | centralized vault, payment method token | vaulting + PSP tokens + vault forwarding | customer profiles + tokenization | L1 |
| Network tokens / account updater | network tokenization, PAN retry | network tokenization | network tokens, account updater | Network Token Services, Account Updater | L1 |
| 3DS orchestration | 3DS2 Global / gateway-specific | Primer 3DS / Adaptive 3DS | Embed/Hosted/Native/External 3DS | 3DS configuration per connector | L1 |
| Fraud service integration as flow participant | Dodgeball checkpoints (Sift, Forter...) | Fraud Checks | anti-fraud connections + silent mode | risk checks + risk-score routing | L1 |
| Unified ops (refund/capture/cancel/disputes) | API + app | manage-payments + unified dispute webhooks | API + dashboard | post-processing | L1 |
| Unified settlement/reconciliation | reporting | unified settlement report | settlement reports w/ per-processor mappings | connector-level data fetchers | L1 |
| Observability / per-attempt transparency | app analytics, transaction transcript | payment timeline (request/response per event), monitors | Insights, monitoring & alerting | statistics, transaction details | L1 |
| Webhooks | events API | PAYMENT.STATUS etc. | transaction/capture/refund events | callbacks | L1 |
| Payer-facing acceptance surfaces | iFrame/express (vault-centric) | Universal Checkout/Drop-in/Headless | Embed/Secure Fields/mobile SDKs | hosted pages/payment.js/redirect/server-to-server | L2 |
| Checkout as product centerpiece | no | yes (Universal Checkout) | yes (Embed) | optional | L2 |
| Multi-tenant / white-label posture | environments, merchant profiles (aggregators) | — | merchant accounts (premium) | tenants/sub-tenants (white-label core) | L2 |
| Recurring/schedules | stored credentials | recurring payments | recurring payments | scheduler, recurring routing | L2 |
| Named routing container | Workflow (Composer) | Workflow | Flow rule | Meta-Connector | L3 (naming) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A Payment Orchestration Platform is a merchant-side control layer **above multiple independently contracted payment providers**, consisting of four properties. Remove any one and it stops being this Type:

1. **Multiple connected provider paths.** The merchant registers its own accounts/credentials with several external PSPs/gateways/acquirers as routable connections inside the platform. Without plurality, the product is itself a gateway/PSP.
2. **A single normalized payment entry point.** The merchant integrates once; payment requests enter through one API/surface regardless of which provider will process them. Without it, the merchant holds N separate integrations and there is no orchestration layer.
3. **A per-transaction provider-selection decision.** For each payment, the platform selects the provider path — by rule, split, failover, or explicit selection. The decision point is structural even when the policy is trivial (a single static connection is the degenerate case). Without it, the product is aggregation/reporting, not orchestration.
4. **A provider-independent transaction record with a normalized lifecycle.** Each payment is recorded once in the platform with a unified status model and per-attempt detail, independent of which provider processed it; lifecycle operations (capture, refund, cancel, dispute) are issued through the platform. Without it, retries, unified operations, and reconciliation are impossible — the product is a thin proxy.

The orchestrator itself does **not** authorize or settle: it forwards to the selected provider, which returns the outcome. This is the structural difference from a gateway.

### L1 — Common Mature Structure

Present in all four researched products; makes the Type practical but does not define it:

- **Failover / retry machinery** — automatic re-attempt on a backup provider for soft declines and technical failures, with a normalized classification of "retriable" vs "final" outcomes.
- **Rule condition dimensions** — amount, currency, card brand/BIN data (range, country, issuer, type), customer geography, transaction metadata, recurring/merchant-initiated flags, risk score.
- **Percentage split / load balancing** — distribute volume across providers for A/B testing, load balancing, and gradual rollout.
- **Platform vault** — provider-independent payment-method tokens usable across connections; PSP-token provisioning; token import/export.
- **Network tokens & account updater** — scheme tokens and automatic credential refresh to raise authorization rates.
- **3DS orchestration** — choose the 3DS approach/provider; carry authentication data across fallback attempts.
- **Fraud/risk services as flow participants** — external fraud providers connected into the flow; their decisions usable as routing conditions.
- **Unified operations** — capture/refund/cancel/void and dispute handling issued from one surface against whichever provider holds the transaction.
- **Unified settlement & reconciliation** — per-provider settlement data ingested and normalized into one report/view.
- **Observability** — per-transaction timelines showing every attempt (request/response), dashboards, monitors/alerts.
- **Webhooks** — unified event notifications for asynchronous outcomes.

### L2 — Variant / Optional Structure

- **Product philosophy**: vault-centric API layer (Spreedly-style) vs no-code workflow platform (Primer-style) vs embedded-checkout-first (Gr4vy-style) vs white-label multi-tenant infrastructure (IXOPAY-style).
- **Operator side**: merchant-operated (most) vs PSP-side white-label operation for downstream merchants (IXOPAY sub-tenants).
- **Acceptance surfaces**: API-only operation vs platform-provided hosted checkout/embedded fields/mobile SDKs; commerce-platform plugins.
- **Multi-tenancy**: single-merchant default vs multi-merchant accounts vs white-label sub-tenant trees.
- **Recurring/scheduling**, **payouts/global accounts/FX**, **DCC**, **virtual terminal (MOTO)**, **pay-by-link**, **gift cards/wallet method breadth**, **PCI data migration** — present in some products.
- **Deployment/tiering**: SaaS tiers, sandbox environments, premium features gated by plan.

### L3 — Vendor-specific (research notes only)

- Spreedly: Composer, Dodgeball, Recover as a paid service, receivers/payment-method distribution, environments, merchant profiles, S1 certification, transaction transcripts with defined retention.
- Primer: AI Companion, Costs Overview, Global Accounts, client sessions, Universal Checkout component model, Unified Mapping Standard (decline codes).
- Gr4vy: merchant accounts as premium multi-tenancy, ADK (agentic development kit), payment links, gift-card connections, Paze/Click to Pay, CAM/TAS modules, documented 24-hour timeout resolution bound, 4-variant split-routing limit.
- IXOPAY: Meta-Connector terminology, adapters catalog, FAST Editor, ISO 8583 terminals, fee management, DCC, virtual terminal, TokenEx module, Payments Intelligence module, specific hard-decline code list.

## Rejected Findings

- "Orchestration = the platform holds the merchant accounts" — **rejected**. In all four products the merchant (or the white-label operator's merchants) holds its own PSP/acquirer accounts; the platform stores credentials and routes. (Some PSPs bundle acquiring, but that is the gateway/processing side, not the orchestration invariant.)
- "Orchestration = smart/AI routing" — **rejected as definitional**. Smart routing is the flagship use case, but the structural invariant is the per-transaction selection decision; static and failover-only configurations are still the same Type.
- "Vault is definitional" — **rejected**. All four sampled products have one, but an API-only orchestrator without vaulting is conceivable and the vault is a separable subsystem (Spreedly sells Advanced Vault as an add-on; Gr4vy treats vaulting as a feature group). Classified L1.
- "Checkout UI is definitional" — **rejected**. Spreedly and IXOPAY operate API-first/server-to-server without being the checkout center; checkout is an acceptance-surface variant (L2).
- "Unified settlement reporting is definitional" — **rejected**; it is a consequence of the normalized record (L0 #4) and a mature capability (L1), not the defining structure.

## Boundary Findings

**vs Payment Gateway** (the most important boundary; the gateway doc in this Atlas already flags this Type):
- A gateway is one authorizing path: it carries payment data toward the authorizing side and owns the transaction lifecycle for its own processing. An orchestrator is the decisioning layer **above** authorizing paths; gateways/PSPs are its routable targets, and the merchant keeps its own accounts with each.
- Test: remove multi-provider connectivity + provider selection → the orchestrator collapses into a gateway; remove the authorizing backend (keep only routing/normalization over external providers) → the gateway collapses into an orchestrator.
- Gradient risk: modern PSPs market "orchestration" for routing across their own acquiring configurations/multiple MIDs. The structural test is whether the routed targets are **independent external providers under the merchant's own contracts**. Flagged for joint review when Payment Processing Platform is processed.

**vs Payment Processing Platform**: processing is the acquiring/settlement backend (authorization, capture, settlement, payouts); orchestration sits above it and consumes it. Modern vendors bundle both; boundary is stack position.

**vs Fraud Detection Platform**: fraud vendors appear *inside* the orchestration flow as connected services; the orchestrator uses their decisions as routing conditions but does not own the risk model or the fraud decision. Remove fraud → orchestrator intact; remove routing → fraud platform intact.

**vs Checkout Platform**: overlap zone — Primer and Gr4vy ship full checkout UIs. The orchestrator's defining job is provider connectivity + routing + normalization; checkout is an optional acceptance surface. A checkout platform centers the payer-facing conversion experience.

**vs Billing Platform / Subscription Billing**: billing decides what and when to charge (plans, invoices, dunning); orchestration executes and routes the charge. Clean split.

**vs AI Gateway / Model Routing Platform (§13 sibling pattern)**: same abstract pattern (single API over multiple upstream providers, routing, failover, normalization) in a different domain; recorded as a structural analogy only, no taxonomy conflict.

**Historical / market-sample check**: Spreedly's original model (vault + gateway abstraction with static/explicit gateway selection, before smart-routing features) satisfies L0 — the selection decision point exists even when the policy is trivial. IXOPAY's ISO 8583 terminal support shows the same pattern extends to card-present/store routing ("payment switch" lineage). The definition therefore does not over-fit the current no-code/smart-routing generation.

## Uncertainties

- Exact market share / vendor landscape beyond the sample (e.g., PayU Hub, APEXX, Solidgate, CellPoint) was not researched; the four-product sample was chosen for philosophy/tier/geography spread, not exhaustive coverage.
- Whether every "orchestration"-branded product satisfies L0 #3 (some PSP marketing uses the word for single-provider optimization) — could not be verified without sampling those products; the definition keeps the structural test.
- Pricing/contract models (per-transaction vs platform fees) not researched; no commercial claims made.
- IXOPAY's post-acquisition positioning (white-label vs merchant-direct) may have shifted; research reflects current documentation structure (tenants/sub-tenants, white-label guidance).

## Final Synthesis

The Payment Orchestration Platform is the **merchant-side control layer of a multi-provider payments stack**: many independently contracted provider connections, one normalized entry point, a per-transaction provider-selection decision, and one provider-independent transaction record with a normalized lifecycle. Around that spine, mature products add failover/retry, rule dimensions, split routing, a cross-provider vault, network tokens/account updater, 3DS and fraud-service orchestration, unified operations, unified settlement/reconciliation, observability, and webhooks. Products differentiate by philosophy (vault-centric, workflow/no-code, embedded-checkout, white-label) and by how much of the acceptance surface they take over. The Type is distinct from the Payment Gateway (which is one of its routable targets) and from fraud/checkout/billing Types by the structural tests above.
