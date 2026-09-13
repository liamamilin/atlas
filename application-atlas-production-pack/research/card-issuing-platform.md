# Research Notes — Card Issuing Platform

## Research Goal

Understand what a "card issuing platform" is as practiced by real vendors, and derive a vendor-neutral Application Type definition for the directory leaf **Card Issuing Platform** (§08 Finance, Banking, Insurance & Investment; directory siblings: Card Management System, Card Processing Platform, Core Banking System, Corporate Card & Spend Platform, Digital Wallet, plus processed neighbors Payment Processing Platform, Gift Card Management, Fraud Detection Platform, Banking Back-office Platform).

## Initial Boundary

Working hypothesis before research:

- A card issuing platform is issuer-side software: it creates and manages payment cards (virtual and physical) issued to cardholders, binds them to funding sources, governs card usage through configurable controls, and participates in the authorization/clearing lifecycle of card transactions.
- Most easily confused with: **Card Processing Platform** (expected: the transaction-switch rails), **Card Management System** (expected: issuer-side card records), **Payment Processing Platform** (merchant-side acquiring — opposite network side), **Corporate Card & Spend Platform** (spend-side software used by card-issuing customers), **Digital Wallet** (cardholder-side credential storage), **Gift Card Management** (closed-loop merchant value vs open-loop network cards).
- The directory has three adjacent card leaves (Issuing / Management / Processing); the market may not separate them cleanly. Joint-review flags likely.

## Research Questions

1. What objects does an issuing platform manage (card, cardholder, account, program, product)?
2. How does a card get issued — what is the creation flow for virtual vs physical cards?
3. What funding models exist (prepaid balance, credit line, pooled program funds, wallet-backed)?
4. How does authorization work — who decides approve/decline, what controls are evaluated, what happens after authorization (clearing, reversal, expiry, advice, refund)?
5. What card lifecycle states and operations exist (activate, suspend, terminate, reissue, replace)?
6. What spend-control taxonomies do products expose (categories, geography, velocity, limits)?
7. What compliance machinery is built in (KYC/KYB, 3DS, PCI scope offloading)?
8. What interfaces exist (dashboard, API, webhooks, cardholder-facing components, sandbox)?
9. Where is the line to Card Processing Platform / Card Management System / Payment Processing Platform?
10. Would older/traditional issuer systems (bank-owned issuing, issuer processors) satisfy the same minimal definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, different customer tiers:

1. **Stripe Issuing** — API-first issuing embedded in a payments platform; startups → large platforms; commercial + consumer.
2. **Adyen Issuing** — issuing as a module of an enterprise payments platform; enterprise and platform customers; enterprise vs embedded issuing poles.
3. **Marqeta** — independent modern issuing platform; large fintechs/marketplaces/retailers; debit/credit/prepaid program management heritage.
4. **Lithic** — embedded-finance issuing for startups/mid-market; explicit "issuing + money movement + program management" positioning.

Rejected/abandoned: **Galileo** (issuer-processor heritage pole) — galileo.io is an unrelated healthcare company; galileo-ft.com returned 403; abandoned after two attempts per source rules. The processor-heritage pole is therefore argued structurally, not from direct product evidence (see Uncertainties).

## Sources

All fetched 2026-09-07. Evidence layer A (direct observation) unless noted.

- Stripe — https://docs.stripe.com/issuing (Tier 1); https://docs.stripe.com/issuing/how-issuing-works (Tier 1); https://docs.stripe.com/issuing/controls/spending-controls (Tier 1)
- Adyen — https://docs.adyen.com/issuing/ (Tier 1, full doc-map landing with concept definitions)
- Marqeta — https://docs.marqeta.com/ (Tier 1); https://www.marqeta.com/docs/developer-guides/platform-overview/ (Tier 1)
- Lithic — https://docs.lithic.com/ (Tier 1); https://docs.lithic.com/docs/transaction-flow (Tier 1, deep lifecycle detail)
- Context (no product claims): gift-card-management research (open-loop network prepaid = issuing territory); payment-processing-platform STATUS boundary note (issuer-side leaves expected opposite network side)

Source-access limitation: Galileo unreachable (wrong domain / 403). Traditional issuer-processor and bank card-management systems were not directly sampled. No numeric limits or defaults from unreachable sources are asserted anywhere.

## Product Observations

### Stripe Issuing

Key observations (Layer A):

- Positioning: "create, manage, and distribute payment cards for your business"; commercial and consumer card programs; partner banks provide the licensed issuance ("embedded finance infrastructure"); cards on Mastercard and Visa.
- Program setup flow: eligibility → choose virtual/physical → customize program (network, card product type) → fund an Issuing balance → fraud steps → optional spending controls → simulate purchases in sandbox.
- Architecture: platform → connected account → cardholder → card, with funding sources: **Issuing balance** (top-up from external bank or Stripe balance) or **Treasury financial accounts** (banking-partner accounts with routing numbers); also wallet-funded (stablecoin/custodial wallet) programs in preview.
- Cards: virtual (issue immediately) and physical (card bundles, custom designs, shipping options, bulk shipments); replacement cards (expired/damaged/lost/stolen); PIN management.
- Spending controls: allowed/blocked merchant categories (MCC), merchant countries, merchant IDs, card presence (card-present/card-not-present); spending limits (amount + interval, e.g. per-authorization / monthly); controls attach to cards and cardholders; cardholder limits span all their cards; replacement cards inherit limits; most-restrictive control wins on overlap; controls run **before** real-time authorizations.
- Real-time authorizations: approve/decline authorization requests as they happen via webhooks; handle partial, incremental, and reversal authorizations; transactions include refunds and captures (including later-posted tips/fees).
- Disputes: submitting and tracking disputes.
- Digital wallets: add physical/virtual cards to Apple Pay / Google Pay / Samsung Pay via manual, in-app push, or web push provisioning.
- Fraud management guidance + controls; automatic reconciliation / transaction categorization; multi-currency issuance.
- Sandbox testing: simulate test purchases.
- Use cases table: commercial card program; consumer card program (bank-sponsored credit).
- Vendor-specific (L3): default spending limit of 500 USD/day on new cards when none configured; unconfigurable default per-authorization limit of 10000 USD; spend aggregation best-effort with up-to-30-seconds delay; "Issuing balance"/"Treasury for platforms"/"Connect connected accounts" naming; Bridge stablecoin integration.

### Adyen Issuing

Key observations (Layer A):

- Positioning: "Create virtual and physical cards for your users"; customizable card issuing; cards from Mastercard and Visa; EEA/UK/US availability.
- Core resource model (documented explicitly): **balance platform** → **accountHolder** (user entity: your company or your customers) → **balanceAccount** (where funds are held; one or more per account holder) → **paymentInstrument** ("The card itself… Creating a payment instrument issues a card"); plus **transactionRules** ("Rules that are applied to automatically approve or deny authorization when a user attempts to pay with a payment instrument").
- Funding: single pool of funds for all cards or balances per card; liable balance account holds the operator's own funds for loading cards and balance transfers; top-ups (recurring supported), external bank transfers, settle funds, balance updates webhooks, reconcile balances.
- Authorization: **transaction rules** auto approve/deny; **relayed authorisation** — receive authorization requests on your own servers to approve/decline any authorization; payment stages: authorisation holds, authorisation, scheme advice.
- Onboarding: onboard and verify users (KYC) — verification requirements per country, required information, document uploads, verification codes/error codes, hosted onboarding, ToS acceptance; account holder status management.
- Card data: reveal card details via iOS SDK or standard encryption; reveal/change PIN; PCI compliance scope depends on use case.
- Network tokens: digital-wallet tokens (Apple Pay in-app provisioning), card-on-file tokens; manage token lifecycle.
- 3D Secure: enroll cards, OTP, out-of-band SDK authentication.
- Disputes: raise duplicate/fraud/non-delivery disputes, attachments, manage disputes.
- Reporting: Accounting Report (payment lifecycle, cash management, authorization rates), Balance Report, Payment Instrument Report, Received Payments Report; generate/download reports.
- Webhooks are mandatory ("An Issuing integration is incomplete without accepting and handling webhooks").
- UI component libraries for building user (cardholder-facing) dashboards.
- Two documented structures: **Enterprise issuing** (own company's cards) and **Embedded issuing** (platform issuing for its customers).
- Vendor-specific (L3): balance platform resource naming; "relayed authorisation", "scheme advice" terminology; brand-specific industry code lists.

### Marqeta

Key observations (Layer A):

- Positioning: "Companies use the Marqeta platform to launch and manage their payment card programs. Marqeta works on their behalf with card networks and issuing banks to issue cards, authorize transactions, and communicate with settlement entities."
- Interfaces: **Core API** (RESTful, program management, webhooks), **DiVA API** (programmatic production-data reporting), public sandbox (evaluation), private sandbox (integration validation), production; **Marqeta Dashboard** (web interface: create users/businesses, permissions, create cards, fraud monitoring, suspend/terminate cards).
- Funding models: **Standard Funding** — account holders' general purpose accounts (GPA) carry loaded balances; **Just-in-Time (JIT) Funding** — card accounts carry no balance, funds held in program funding account until purchase: **Managed JIT** (platform's configured spend controls decide) vs **Gateway JIT** (platform applies spend controls, then forwards funding request to client system for approval; client maintains a ledger of record and must respond accurately).
- Account holders: individuals or businesses; both have GPAs; only individuals can be cardholders; a user is created with the business as parent to spend business funds; account holder groups apply common spend-control sets.
- Card model: **card product** configures how cards behave; **cards** inherit product settings; card lifecycle: issued, activated, funded, used, tokenized, suspended, terminated, expired, reissued; physical cards require activation, virtual often immediate one-time use; bulk card orders to card providers; lost/stolen/damaged handling (suspend/terminate/reissue) incl. wallet tokens sourced from the card.
- Spend controls: **authorization controls** (limits on merchants and merchant categories) + **velocity controls** (maximum amounts, transaction frequency, vendor categories); merchant category (MCC) groups.
- Transactions: electronic message from merchant/ATM → card network → Marqeta for authorization; dual-message vs single-message models; monitor transaction impact on balances; retrieve historical transactions.
- Webhooks: transaction events, card activations; for Gateway JIT, ingest funding requests and return funding decisions.
- Failure handling: **STIP** (network stand-in processing when platform unreachable; network notifies platform later; requires approval, not generally used for prepaid) and **Commando Mode** (platform decides on client's behalf per business rules when client can't respond; stores unsent webhooks for later transmission so client state converges).
- Digital wallets/tokenization: Apple Pay and Google Wallet; network tokens; token lifecycle controls.
- PCI compliance: UX Toolkit components (activate card, set/reveal PIN, view card details incl. PAN/expiry/CVV2 via hosted iframes so client servers don't touch card data).
- IVR services: cardholders activate cards, set/change PIN, check balance, report lost/stolen by phone.
- Risk: RiskControl — KYC (identity verification before cards/loading/payments where required), 3D Secure, Real-Time Decisioning (dashboard + dedicated rule language for fraud rules; offline unit tests), Dispute Management (dashboard + /cases endpoint, supporting documents), AVS (address verification with configurable decline on mismatch).
- Reporting: standard and customized reports in dashboard; DiVA API.
- Credit platform (Layer A, module): system of record for credit programs — policies (credit product/APR/fee) bundled into programs; applications (bank approves application); account origination; account management with **account transitions** (activate → suspend → terminate → charge-off); account cards; journal entries; reward accounts/redemptions; statements (billing cycle activity, interest, rewards); payment sources/schedules/payments; adjustments; credit disputes; balance refunds.
- Vendor-specific (L3): GPA, Managed/Gateway JIT Funding, Commando Mode, DiVA, RiskControl, UX Toolkit, IVR service, MCC groups naming.

### Lithic

Key observations (Layer A):

- Positioning: "Card issuing, money movement, and program management — everything you need to launch a payments product, in one modern API." Solutions: digital banking, revolving credit, disbursements, expense management.
- Doc-map structure: Card Issuance & Processing (transaction object/flow; card overview; physical card setup; card accounts); Fraud & Risk Controls (Authorization Intelligence, Fraud Command, Authorization Stream Access, Authorization Rules, Transaction Monitoring); Reconciliation & Reporting (Settlement API, bank reporting, quarterly network reporting); Ledger & Account Infrastructure (ledger, financial accounts); Identity Verification (KYC/KYB account holders, status checks); Money Movement (ACH, wires, external bank accounts); Developer Tools (sandbox simulation of account holders/transactions/tokenizations/webhooks; Events API; transaction webhooks).
- Transaction flow (detailed, Layer A): network sends ISO-8583 authorization request (MTI 0100) → platform converts to JSON and sends to client's endpoint (**ASA — Authorization Stream Access**; HTTP 200 response required) → client responds APPROVED/decline/partial-approval → platform returns ISO-8583 response → later clearing message (MTI 0220, "typically arrives between 0-7 days after" — network-timing wording) → transaction status SETTLED with clearing webhook.
- Transaction states observed: PENDING, SETTLED, VOIDED, EXPIRED, DECLINED. Event types: AUTHORIZATION, CLEARING, AUTHORIZATION_REVERSAL, AUTHORIZATION_EXPIRY, AUTHORIZATION_ADVICE, RETURN (and return reversal).
- Lifecycle nuances (Layer A): partial approval; clearing greater/equal/less than authorization (tips; multiple completion — multiple clearings on one authorization); authorization reversal (full → VOIDED; partial → stays PENDING); authorization expiry — network-set validity window; platform releases holds ("expiring" the authorization); late clearing after expiry still accepted; authorization advice updates authorized amount (gas-pump example); network **stand-in**: networks decline by default on platform timeout; enterprise clients can configure stand-in to approve.
- Single-message (SMS) "financial authorization": authorization and clearing combined; immediate financial impact; merchant can still reverse.
- Ledger integration guidance: client systems must track available balances (balance minus pending and settled), place holds on authorized funds, and post settled amounts; three implementation routes (third-party wallet provider, pooled funds + third-party core, pooled funds + own ledger).
- Amounts model: merchant/cardholder/settlement currencies with conversion rates; acquirer fee surfaced separately; FX drift between clearing and return amounts.
- Vendor-specific (L3): ASA naming, Authorization Intelligence/Fraud Command module names, Events API type taxonomy, enterprise stand-in customization, quarterly network reporting.

## Cross-product Comparison

| Dimension | Stripe Issuing | Adyen Issuing | Marqeta | Lithic |
|---|---|---|---|---|
| Card creation | virtual + physical, bundles/designs, shipping, bulk | virtual + physical (paymentInstrument) | card products + cards inherit; bulk orders to provider | virtual + physical (setup guide) |
| Cardholder model | cardholder (person) under connected account | accountHolder + balanceAccount + paymentInstrument | account holder (individual/business), user under business; only individuals are cardholders | account holder (KYC/KYB), card accounts |
| Funding | issuing balance / treasury financial account / wallet | balanceAccount pool or per-card; liable account; top-ups | GPA standard funding vs JIT (managed/gateway) | ledger/financial accounts; client keeps available-balance logic |
| Authorization decisioning | real-time authorizations via webhooks; controls run first | transactionRules auto; relayed authorisation to own servers | spend controls decide; Gateway JIT forwards to client | ASA request/response; network stand-in default-decline |
| Spend-control taxonomy | categories, countries, merchant IDs, card presence, amount×interval limits | transaction rules (+ limits) | authorization controls (merchant/MCC) + velocity controls (amount/frequency) | authorization rules + transaction monitoring |
| Transaction lifecycle | authorization (partial/incremental/reversal) → transactions (refunds/captures) | payment stages: holds, authorisation, scheme advice; track transactions | dual/single-message; balances impact | AUTHORIZATION → CLEARING/REVERSAL/EXPIRY/ADVICE/RETURN; PENDING/SETTLED/VOIDED/EXPIRED/DECLINED |
| Card lifecycle ops | replace (expired/damaged/lost/stolen); PIN management | manage cards; PIN reveal/change; suspend via status | issued/activated/suspended/terminated/expired/reissued; lost/stolen flows | manage cards; physical setup |
| Digital wallets | Apple/Google/Samsung Pay; manual/push provisioning | network tokens; Apple Pay provisioning | Apple Pay/Google Wallet; token lifecycle | tokenization + simulate tokenizations |
| KYC/KYB | (referenced; compliance guides) | deep onboarding/verification docs | KYC before cards/funds where required; 3DS; AVS | KYC/KYB account holders + status |
| Disputes | submit/track disputes | raise/manage disputes (reason-coded) | dispute management + credit disputes | (fraud command/monitoring; disputes less central in sampled pages) |
| Credit programs | consumer issuing (bank-sponsored credit, preview) | enterprise/embedded | full credit module (origination→servicing→statements→charge-off) | revolving credit solution |
| Cardholder-facing surfaces | (dashboard for user is platform-side) | UI components for user dashboards | UX Toolkit components; IVR | (client-built; reveal via client) |
| Ops surfaces | Dashboard + API + sandbox | Dashboard/API/webhooks/reports | Dashboard + Core API + DiVA + sandboxes | Dashboard + API + sandbox |
| Failure handling | — | webhooks mandatory; scheme advice | STIP + Commando Mode | network stand-in; late clearing accepted after expiry |

Cross-product commonalities (Layer B — observed across all four):

1. Cards as managed, lifecycle-bearing objects (issue → activate → govern → suspend/terminate → reissue/replace), virtual and physical forms.
2. Identified cardholder/account-holder entity, with identity verification machinery (KYC/KYB) gating card creation or usage.
3. A funding source or balance the card draws from (balance account, program funds, credit line, wallet), with funds-loading machinery (top-ups, transfers).
4. Real-time participation in authorization decisions, under configurable spend controls/limits (merchant categories, geography, amounts, frequency), with the operator's own decisioning hook (webhooks/relayed auth/ASA/gateway funding).
5. A recorded transaction lifecycle beyond the authorization moment: clearing/settlement, reversals, expiries, advice/updates, returns/refunds — with statuses and amount projections (authorized/held/settled).
6. Program configuration layer (card products/bundles; account-holder groups; program defaults) above individual cards.
7. Digital-wallet tokenization to Apple/Google-class wallets.
8. Operator surfaces: dashboard/console + REST API + webhooks + sandbox/simulation; reporting/reconciliation.
9. PIN management and PCI-burden offloading (hosted card-data/PIN components or SDKs).
10. Fraud/risk machinery attached to the program (rules engines, 3DS, AVS, monitoring, disputes).

Layer C (canonical inference): the defining structure is the **card program operated on the issuing side of network rails**: the platform turns a funding relationship into governed, spendable network cards and answers for their usage — issuance and lifecycle of cards, real-time authorization decisioning under program rules against available funds, and the recorded money lifecycle of what was spent.

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **Issuable card as managed payment credential** — the platform creates and maintains identified cards (network payment instruments) in virtual and/or physical form, with a governed lifecycle (issue → activate → manage → suspend/terminate → replace/reissue). Without card creation/lifecycle it is not an issuing platform.
2. **Identified cardholder** — an identified person or business to whom cards belong and who is onboarded/verifiable. Without it, cards are anonymous credentials and no program exists.
3. **Funding binding** — each card draws on an identifiable funding source (balance account, credit line, pooled program funds, wallet) that constrains what can be spent. Without it, it is a credential factory, not a card program.
4. **Authorization decisioning + recorded transaction lifecycle** — card usage arrives as real-time authorization requests; the platform decides (or configures who decides) approve/decline/partial under available funds and program controls, and records what happens next (clearing/settlement, reversal, expiry, updates, refunds) as inspectable transaction records. Without this, it is card design/print or an inert registry.

Deliberately NOT in L0: virtual-first shape, digital wallets, API/webhooks, sandboxes, KYC depth, disputes, rewards, statements/billing cycles, JIT funding, interchange monetization — all are L1/L2 (see below).

### L1 — Common Mature Structure (observed in all/most sampled products)

- Virtual cards as a first-class card type alongside physical plastic; card designs/bundles; physical fulfillment (shipping, bulk orders).
- Digital-wallet tokenization (Apple Pay/Google Pay-class) with provisioning flows.
- PIN management and card-data reveal with PCI offloading (hosted components/SDKs).
- KYC/KYB onboarding machinery gating issuance/usage.
- Spend-control layer: merchant-category/merchant-identity restrictions, geographic restrictions, amount/frequency (velocity) limits, card-present/not-present rules; per-program/cardholder/card scoping.
- Operator's own decisioning hook on authorizations (webhooks / relayed authorization / gateway funding / authorization-stream access).
- Full transaction lifecycle: dual-message and single-message shapes; partial approval; clearing; reversals; authorization expiry; advice updates; returns/refunds; statuses and amount projections (authorized/held/settled).
- Program operations: dashboard/console, REST API, webhooks, sandbox/simulation, reporting/reconciliation/settlement reporting.
- Dispute machinery; fraud/risk tools (rules engines, 3DS, AVS-class verification, monitoring); replacement/reissue handling for lost/stolen/damaged.
- Multi-currency with currency-conversion visibility on transactions.

### L2 — Variant / Optional Structure

- Funding model: prepaid/debit balances vs credit lines/revolving credit vs charge cards vs wallet/stablecoin-backed; pooled program funds vs per-card balances; balance-carrying (standard) vs JIT funding.
- Program type/audience: consumer, commercial/corporate (expense, T&E, procurement), marketplace/platform payouts, disbursements, digital banking.
- Issuing posture: enterprise (own company's cards) vs embedded (platform issuing to its customers); single-company program vs multi-tenant platform.
- Credit-program depth: origination (applications, approvals), account transitions (activate→suspend→terminate→charge-off), statements/billing cycles, payment schedules, interest/rewards — as an optional module (present as full module in one sampled product, lighter elsewhere).
- Regulatory/geo regimes: availability regions, region-specific verification and authentication machinery (e.g., 3DS), scheme/product availability.
- Delivery: API-first vs dashboard-first; suite module (payments platform) vs independent platform vs embedded-finance stack.
- Monetization features: interchange-sharing framing (vendor guide material, Layer B-light).
- Legacy surface: IVR cardholder services (one product).

### L3 — Vendor-specific (research notes only)

- Stripe: Issuing balance; Treasury for platforms financial accounts; Connect connected-account model; default 500 USD/day new-card limit and unconfigurable 10000 USD per-authorization limit; ≤30s spend-aggregation delay; Bridge/Privy stablecoin funding; merchant-ID controls in private preview.
- Adyen: balance platform resource taxonomy (accountHolder/balanceAccount/paymentInstrument/liable balance account); "relayed authorisation"; "scheme advice"; brand-specific industry codes; hosted onboarding components; enterprise-vs-embedded issuing split naming.
- Marqeta: GPA; Managed vs Gateway JIT Funding; Commando Mode; STIP posture (not generally for prepaid); DiVA API; RiskControl; Real-Time Decisioning rule language; UX Toolkit components; IVR services; MCC groups; account transitions taxonomy (incl. charge-off).
- Lithic: ASA (Authorization Stream Access); Events API type taxonomy (AUTHORIZATION_EXPIRY etc.); enterprise stand-in-approve customization; Fraud Command/Authorization Intelligence naming; quarterly network reporting.

## Vendor-specific Findings

See L3 above. None of these enter the canonical core. Note: several are operationally significant (stand-in behavior, funding-mode choice) and are surfaced in the final document only as generic behaviors ("the network may stand in when the platform cannot respond"; "funding may be balance-carrying or just-in-time").

## Boundary Findings

- **vs Card Processing Platform** (directory sibling, unprocessed): expected seam — the issuing platform owns the *program and card side* (cards, cardholders, funding config, spend controls, card lifecycle); a card processing platform is the *transaction-rail side* (authorization switching/routing to networks, interchange/clearing/settlement mechanics as infrastructure). In the sampled modern products both are fused (Lithic names a section "Card Issuance & Processing"; Stripe/Marqeta process the authorization stream themselves), so the same vendor family can satisfy both leaves — same overlap pattern the processed Payment Processing Platform leaf flagged for its sibling. Structural tests: strip card issuance/lifecycle → authorization-only processor (Card Processing); strip rail participation and keep only card records/design → Card Management/registry. **Flag for joint review when Card Processing Platform is processed.**
- **vs Card Management System** (directory sibling, unprocessed): at research depth the market does not clearly separate "card management" from "issuing platform" — sampled products all "manage cards" (status, PIN, limits, lifecycle) as the heart of issuing. Plausible readings: (a) Card Management System = traditional bank-internal issuer-side system of record (statuses, limits, plastic, PIN) → near-alias of issuing from a different era; (b) a sub-capability of issuing. **Flag for joint review; do not resolve unilaterally.**
- **vs Payment Processing Platform** (processed): confirmed opposite network sides — merchant-side acquiring (underwrites sellers, routes payments into networks, funds merchants) vs issuer-side (creates cards, answers authorization requests, moves cardholder/program funds). Removal test: strip card issuance and serve businesses *accepting* payments → Payment Processing Platform.
- **vs Core Banking System**: the ledger of deposit/credit accounts. Issuing platforms bind cards to funding accounts but do not own the deposit ledger; deep issuing products add ledgers/balance accounts as program infrastructure, not as the bank's books.
- **vs Corporate Card & Spend Platform** (unprocessed at time of writing): spend-side software used by the card-using company's finance team and employees (budgets, receipts, approvals). Issuing platforms are program-side software operated by the program owner. Corporate spend platforms are issuing *customers* (several embed issuing); the seam is who operates the software and for whom. Removal test: remove card issuance and manage only budgets/receipts/policies → spend platform.
- **vs Digital Wallet**: cardholder-side credential storage and payment initiation; issuing creates and governs the credentials wallets hold. Wallet-facing tokenization is an issuing output.
- **vs Gift Card Management** (processed): consistent with that leaf's own finding — merchant closed-loop stored value vs open-loop network-branded cards; once value is held in a bank-issued network instrument, it is issuing territory.
- **vs Fraud Detection Platform** (processed): issuing platforms embed program-governance decisioning (spend rules, real-time rules engines) — these are *program configuration and authorization controls*, not the standalone operational fraud system (signal enrichment, case management, model feedback loops). Overlap is real but the centers differ.
- **vs Banking Back-office Platform** (processed): that leaf explicitly recorded that card rails have their own leaves; the issuing platform is the card-rail leaf for program-side operation, not a bank-wide work-processing pipeline.
- **去掉什么就变成另一个 Type** 判据: remove authorization participation/transaction lifecycle → card design & fulfillment tooling; remove card issuance and lifecycle → transaction-rail processing (Card Processing); remove funding binding and spend governance → digital credential manager; remove open-loop network rails → closed-loop gift/stored-value program; remove program-operator side and serve the card-using company → Corporate Card & Spend Platform; remove card semantics entirely and hold balances → digital wallet / banking app.

## Uncertainties

1. **Processor-heritage pole unsampled** (Galileo unreachable; classic issuer processors/bank card-management systems gated). The L0 was abstracted precisely so that such systems (cardholder records, card statuses/limits, authorization processing, funding via deposit/credit accounts) satisfy it without virtual cards/APIs/webhooks. Assertions about that pole are structural inference, marked as such; no product claims made.
2. **Card Management System vs Card Issuing Platform vs Card Processing Platform** — three directory leaves over what may be one or two real market structures; joint-review flags recorded (Boundary Findings above and STATUS).
3. Region-specific regulatory machinery (US consumer error-resolution regimes, EU strong-customer-authentication) was observed only as menu structure (verification/3DS doc sections), not researched at content level; final document keeps regulatory claims generic.
4. Disputes/chargeback mechanics verified directly at three of four products (Stripe, Adyen, Marqeta); kept as common-mature rather than defining.
5. Interchange/revenue-share monetization observed only as guide-level framing (Stripe guide); kept as variant with moderate wording.

## Final Synthesis

A **Card Issuing Platform** is issuer-side infrastructure through which a company operates a payment card program on card-network rails: it turns a funding relationship (balance account, credit line, pooled program funds, or wallet) into identified, spendable cards — virtual and/or physical — issued to verified cardholders; it governs every card's usage through configurable spend controls and takes part in the real-time authorization decision for each attempted purchase; and it records the resulting money lifecycle (authorization → clearing/settlement, with reversals, expiries, updates, and refunds) as inspectable transaction records, operated through an operator console and APIs with webhooks, sandboxes, reporting, and attached risk machinery (KYC/KYB onboarding, 3DS, fraud rules, disputes).

The defining core is small (issuable lifecycle-managed cards + identified cardholder + funding binding + authorization decisioning under program controls with a recorded transaction lifecycle). Everything else — virtual-first shapes, wallet tokenization, funding-mode philosophy, credit modules, program types, delivery posture — is variant space. The Type sits on the issuing side of the card rails, opposite the merchant-side payment processing Types; its deepest unresolved boundary is with the two directory siblings Card Management System and Card Processing Platform, where the market itself does not maintain crisp lines.
