# Research Notes — Payment Processing Platform

## Research Goal

Determine what a **Payment Processing Platform** is as an Application Type: what structure defines it, what work it carries out that neighboring payment Types (Gateway, Orchestration, Billing, POS, issuer-side Card Processing) do not, and how the modern "everything bundled" market affects the definition. The directory already contains a processed sibling — Payment Gateway — whose research explicitly flagged this leaf as "the acquiring/settlement backend of the same stack; modern vendors bundle gateway + processing in one product, so the boundary is stack position, not structure — flagged for joint review." This research pass must therefore establish the processing-side structure on its own evidence, not merely mirror the gateway document.

## Initial Boundary

Hypothesis before research:

- A payment processing platform is the **acquiring/processing back end**: merchant processing accounts (underwriting + provisioning), transaction routing into card/bank networks for authorization, and clearing/settlement/funding of the merchant's bank account, with fee handling and risk accountability (holds, reserves, chargebacks).
- Nearest neighbors: Payment Gateway (front-end acceptance; bundled in modern products), Merchant Payment Platform (terminology sibling), Payment Orchestration Platform (layer above multiple providers), Card Processing Platform (issuer-side, same word "processing"), Billing/Subscription Billing (decides what/when to charge), Retail POS (composes the sale), Fraud Detection Platform (standalone decisioning), Peer-to-peer Payment (no merchant).
- Unknowns: (1) whether the classic decoupled processor model is still evidenced by reachable documentation; (2) how deeply merchant underwriting/provisioning is a first-class structure; (3) whether settlement/funding mechanics are uniform enough across products to be canonical; (4) whether this leaf is a distinct Type or a synonym bucket.

## Research Questions

1. What does the processing back end do *beyond* what the gateway document already describes: underwriting, account provisioning, clearing, settlement, funding?
2. What is the merchant processing account as an object — who provisions it, what states does it have, what identifiers attach to it?
3. How do platforms/marketplaces reshape merchant enrollment (sub-merchants, seller onboarding, split payments)?
4. How are fees handled (net vs gross payouts, fee profiles, statements)?
5. What is the dispute/chargeback model from the processing side, and where does financial liability sit?
6. What settlement/funding machinery is common (schedules, timing tiers, negative balances, payout holds)?
7. How do modern products bundle gateway + processing, and how do they describe themselves?
8. Where does the boundary with Gateway / Orchestration / issuer-side Card Processing / Merchant Payment Platform actually hold or collapse?

## Representative Products

Selection principles: market representation across processor eras and customer tiers, documentation completeness, different product philosophies, different distribution models.

| Product | Role in sample | Tier / philosophy |
|---|---|---|
| **Finix** | modern API-first processor infrastructure; explicit seller-underwriting + settlement machinery; platform/marketplace posture | platforms & enterprise; API-first |
| **Stax** (ex-Fattmerchant) | ISV/partner-distributed processing; self-describes via its docs as platform for managing merchants, with a full underwriting program | ISVs & SMB sub-merchants; partner-distributed |
| **Worldpay** (now part of Global Payments) | global merchant acquirer/processor; ISO and financial-institution distribution channels; full product stack | SMB through enterprise; classic acquiring distribution |
| **Stripe** (cross-check only) | already sampled for Payment Gateway; re-sampled here only for settlement/funding/payout mechanics | self-serve all-in-one; modern bundling check |

Classic processors (Fiserv/First Data, CardConnect, TSYS/Global Payments, Adyen, Helcim) were attempted and abandoned — see Sources. The historical-model check is therefore reasoned from Worldpay's acquiring positioning + cross-product structure, not from a directly fetched classic-era product.

## Sources

Fetched successfully (research date 2026-09-06):

- Finix — Docs home: https://docs.finix.com/
- Finix — Getting started: https://docs.finix.com/guides/getting-started
- Finix — After the payment (section index): https://docs.finix.com/guides/after-the-payment
- Finix — Your payout schedule: https://docs.finix.com/guides/after-the-payment/payouts
- Finix — Platform quickstart (seller onboarding): https://docs.finix.com/guides/platform-payments/platform-quickstart
- Finix — Disputes (section index): https://docs.finix.com/guides/after-the-payment/disputes
- Stax — Docs home: https://docs.staxpayments.com/
- Stax — Getting started with Stax Connect: https://docs.staxpayments.com/docs/getting-started-implementation
- Stax — Underwriting overview: https://docs.staxpayments.com/docs/underwriting-overview
- Stax — Merchant enrollment: https://docs.staxpayments.com/docs/enrollment
- Worldpay — Corporate/product site root: https://www.worldpay.com/en
- Stripe — Receive payouts: https://docs.stripe.com/payouts

Attempted and abandoned (network limitation, 1–2 attempts each per the workflow rule):

- Fiserv developer hub (developer.fiserv.com root and /product/CardPointe) — empty JS-rendered shell, twice.
- CardConnect developer portal (developer.cardconnect.com) — transport error.
- Global Payments developer portal (developer.globalpayments.com) — empty JS-rendered shell.
- Adyen docs settlement pages (two URL guesses) — 404; deeper Adyen settlement evidence not gathered.
- Helcim docs (docs.helcim.com) — 403.
- Stax marketing root (staxpayments.com) — 403 (docs subdomain worked).
- Worldpay developer docs root (docs.worldpay.com) — JS-rendered title only; deeper pages not reachable.
- Chase Paymentech, Elavon, TSYS — not attempted after repeated JS-shell failures on同类 corporate developer portals (evidence budget exhausted elsewhere).

Consequence for assertion strength: settlement/funding/dispute/underwriting mechanics rest on Finix + Stax + Stripe (direct) and Worldpay at product-page level only. Claims about the classic decoupled processor era are kept conceptual and marked as inferred.

## Product Observations

### Finix (evidence layer A — official docs, multiple pages)

**Positioning (docs home).** "End-to-end payment solution… build a payments experience using our intuitive APIs, and provide you with tools to manage fees, operations, compliance and more." Docs sections: Online Payments, In-Person Payments, After the Payment, Managing Operations, Platform Payments, Payouts, low-code surfaces (invoices, payment links, subscriptions, virtual terminal).

**Getting started.** Three steps: (1) sign up for account (sandbox), (2) build integration (online / in-person / platform), (3) "receive payouts — collect the payouts for the payments you've processed." Payouts as the third definitional step of "processing payments."

**Merchant onboarding & underwriting (platform quickstart).** To process a seller's payments: create an **Identity** for the seller (plus one per beneficial owner >25% ownership) carrying **additional_underwriting_data**: merchant-agreement acceptance (with IP/UA/timestamp), refund policy, credit-check consent, annual card/ACH volume, volume distribution by channel and business type, average ticket. Then a **Payment Instrument** (bank account for settlement payouts, or card/bank for charging; tokenized; fingerprinted; raw sensitive data only for PCI Level 1 organizations, otherwise tokenization forms). Then create the **Merchant** resource — "the resource you will use to process your seller's payments" — which is ready only when `onboarding_state` is `APPROVED` (states: PROVISIONING / APPROVED / REJECTED / UPDATE_REQUESTED; webhooks recommended for state changes). Merchant fields include processor-side identifiers (`mid`, per-brand MIDs), `processor` and `gateway` engine references, MCC, currencies, `processing_enabled`, `settlement_enabled`, disbursement options (incl. same-day ACH toggles), surcharge/convenience-charge flags, and settlement-window settings.

**Sale.** A **Transfer** moves value from a buyer's Payment Instrument to a seller's Merchant (amount in minor units; state machine with SUCCEEDED etc.; `fees` and `fee_profile`; `split_transfers` for marketplace splits; statement descriptor; network details; surcharge/convenience amounts). Authorization-and-capture available as a separate flow (Authorization captured later).

**Settlement & funding (payout schedule page).** "As you process payments, Finix buckets the funds from transactions into **Settlements**. After Finix reviews and approves your settlement, you will receive a **Funding Transfer** with your payout." Daily business-day payouts; configurable availability tiers (T+1/T+2); ACH debits held for a return window before funding; payout destination = bank account from the onboarding form (changing it requires risk-team review). **Payout types:** **Net** (fees deducted from the payout; deposits and fees combined) vs **Gross** (separate payout and fee debit). Settlement lifecycle: Accruing → Awaiting Approval → Approved; accrual window; funding speed shown; breakdown (payments, fees, net). Merchant deposit states: Succeeded/Failed. **Risk behavior:** first payout may be withheld for standard risk review; subsequent holds on unusual activity (volume spikes, dispute rates, ACH returns); **negative payouts** — if refunds exceed sales, the settlement is negative and the platform debits the merchant's bank account; **failed payouts** — settlements disabled, automatic retries, then human risk review.

**Disputes.** "A dispute (also known as a chargeback) occurs when a cardholder protests a charge on their statement with their issuing bank. When a dispute is filed, Finix notifies you, **holds the disputed funds**, and gives you a window to respond." Respond with evidence via dashboard/API, or concede (accept). Dispute states, response states, reason codes documented; prevention guidance. Refunds, receipts, instant payouts, account updater, network tokens documented as adjacent capabilities.

### Stax (evidence layer A — official docs)

**Positioning (docs home).** "Empower your platform with fast, secure, and flexible payment solutions" — APIs for online payments (payment links, PCI-compliant storage of payment methods, webhooks), in-person (terminals/POS, tokenization), and **Payments for Platforms** ("manage your merchants"; merchant enrollment; partner webhooks).

**Stax Connect (getting-started-implementation).** Partner/ISV console: "Effortlessly manage your merchants, onboard new clients, and access key performance metrics—all from one powerful platform designed to help ISVs grow." Core sections: Merchant Enrollment, Underwriting, Reports.

**Underwriting overview — the clearest direct statement of the acquiring-side model found in the sample.**
- Definition: "underwriting is the process by which a business's (sub-merchant) processing application is reviewed and assessed **prior to an account being provisioned and activated**."
- Underwriters validate: legitimacy of the business, applicant identity, risk the sub-merchant poses, absence of fraud/illegal activity, creditworthiness, financial integrity, validity of the bank account.
- Rationale — liability mechanics: chargebacks can be initiated well after the transaction; "Before the funds being debited from the sub-merchant, they are debited from Stax. If the sub-merchant doesn't have enough funds to cover the debit… it becomes exceedingly difficult for Stax to recoup those funds." Consequences: account terminations, **account reserves**, increased costs for the ecosystem.
- Regulatory anchor: US federal requirements (FinCEN rules, USA PATRIOT Act) oblige financial-like institutions to collect specified information when opening a merchant processing account.
- **Underwriting statuses:** Awaiting Signature → Awaiting Review → Pended → Approved (→ provisioning) / Rejected (may reapply). Pended reasons catalog: Signer Verification, Business Location, Volume Clarity, TIN Mismatch, Previous Processing History/Credit, Marketing Materials, Deposit Policy, Financials/Banking, Banking Verification — each with resolution steps. Partner (ISV) responsible for working with the sub-merchant to resolve pends.
- Portfolio surfaces: Enrollment page funnel (In progress / In review / Pended / Approved; declined list), ownership filter ("Your move" vs "With Stax"), application timeline, outstanding documents, underwriting notes.

**Enrollment methods.** Four: White-Glove (partner fills in via console), white-labeled Landing Page, Hybrid (SSO redirect into Stax's signup application), Custom (API enrollment embedded in the partner's own software). Progress tracking across the funnel.

### Worldpay (evidence layer A at product-page level; operational flow not fetched)

Corporate/product site root. Serves SMB, Enterprise, Software platforms, Marketplaces. Partner channels: **Financial institutions** ("empower your bank customers") and **ISOs** (independent sales organizations) — the classic acquiring distribution model. Product families: **Accept** (online, in-store, omnichannel, payment methods), **Protect** (fraud prevention, authentication, dispute management "safeguard against chargebacks", vault), **Optimize** (authorization/revenue tools, dynamic routing, credential management, insights & reporting, loyalty/gift), **Embed** (marketplaces "onboard, accept and make payments, all-in-one"; software platforms — embedded payments), **Move Money** (payouts, multicurrency). Enterprise-scale processing-volume figure is displayed as marketing (not recorded as an operational fact). Interpretation: a full-stack merchant acquirer/processor whose positioning spans the same structural territory as the other samples, distributed through classic acquiring channels. Deeper settlement/dispute operational detail was not reachable (developer docs JS shell) — structure-level evidence only.

### Stripe (evidence layer A — payouts page only; cross-check for funding mechanics)

- Funds accumulate in an available balance and are paid out to the merchant's bank as **payouts**; first payout is scheduled after the first live payment with a risk-dependent delay (delay described as variable — not recorded as a canonical fact).
- **Payout schedule** (manual / daily / weekly / monthly) is conceptually distinct from **settlement timing** (how long after capture funds become available, expressed as T+X business/calendar days, varying by country and method); bank-debit methods settle slower due to return risk.
- **Multi-currency settlement:** one bank account per settlement currency; presentment vs settlement currency; acquiring fees tied to the settlement currency; automatic conversion to the default currency for unset currencies.
- **Negative balance:** if refunds/disputes/fees exceed sales, a payout *debits* the merchant's bank account.
- **Risk:** payout timing subject to risk criteria; minimum payout amounts; instant-payout tiers with eligibility.
- **Connect** (platforms/marketplaces): payouts to connected accounts — the platform/sub-merchant structure in self-serve form.

## Cross-product Comparison

| Structural element | Finix | Stax | Worldpay | Stripe (cross-check) |
|---|---|---|---|---|
| Merchant processing account as first-class object | Merchant resource; onboarding states; MIDs; processing/settlement flags | "processing account" provisioned only after underwriting approval | merchant relationships via direct/ISO/bank channels (page level) | account / connected accounts (Connect) |
| Underwriting before processing | underwriting data + verifications; APPROVED required to process | full underwriting program (statuses, pend reasons, documents) | acquiring-side onboarding implied by ISO/bank channels | risk review before first payout; account reviews |
| Transaction processing & outcomes | Transfer/Authorization with states, network details | payments + capture + tokenization surfaces | Accept + Protect families | PaymentIntents (from gateway research) |
| Clearing/settlement/funding | Settlement resource: accruing → approval → funding transfer; net/gross; risk holds; negative debits; failed-funding retries | implied (bank-account validation, deposit policy in underwriting; reserves) | Move Money: payouts, automated settlements | balance → payouts; schedules; T+X; negative debits; multi-currency |
| Fee machinery | fee profiles; per-transfer fees; net vs gross payout | pricing managed for partners (not fetched) | — (insights & reporting family) | acquiring fees per settlement currency; fees deducted from balance |
| Disputes/chargebacks | lifecycle: notify → hold funds → evidence window → challenge/accept | clawback liability ("debited from Stax first"); reserves; terminations | Dispute Management product | disputes product (from gateway research) |
| Platform / sub-merchant enablement | seller onboarding via API/forms; beneficial-owner identities; split transfers | Stax Connect: ISVs enroll & manage sub-merchants; four enrollment methods | Embed: marketplaces, software platforms | Connect |
| Intake surfaces | API, tokenization forms, links, virtual terminal, terminals | API, payment links, terminals | Accept (online/in-store/omnichannel) | full gateway stack |
| Risk levers on money movement | payout holds; negative debits; settlements disabled on failure | reserves; terminations; underwriting rejection | fraud prevention family | risk-based delays; eligibility tiers |

Reading of the matrix:

- All four expose the same three-part spine: **administered merchant processing account → transaction processing with authorization outcomes → settlement/funding back end with fee handling and risk levers**. (Layers A/A/page-level/A)
- Underwriting-before-processing is explicit and elaborate in Finix and Stax; Worldpay's acquiring distribution (ISO/banks) is the same function carried by partners; Stripe enforces risk review before first payout and on connected accounts. (Layer B)
- Settlement/funding machinery (scheduled payouts, net/gross fee handling, negative-balance debits, holds, multi-currency) is directly evidenced in Finix and Stripe and structurally implied in Stax/Worldpay. (Layer B)
- Dispute/chargeback handling with platform-held funds appears in all four. (Layer B)
- The "platform" word is used two ways in the market: the processing back end itself, and products aimed at software platforms/marketplaces (sub-merchant aggregation). All four support the second posture as a mode. (Layer B)

## Canonical Abstraction

### L0 — Defining Invariant

Three properties. Remove any one and the product stops being recognizable as a payment processing platform:

1. **Administered merchant processing account.** The platform establishes and administers, for each selling business, a payment-processing account — underwritten (business identity, legitimacy, creditworthiness, risk reviewed before activation) and provisioned by the platform itself or by its acquiring partners — identified by processor-side merchant identifiers, and governable (enable, suspend, hold funds, terminate). Without it there is no payee to fund and no underwriting to perform: the product is a front end, an orchestration layer, or a wallet.
2. **Transaction processing through authorization.** The platform receives payment transactions (directly from merchant channels, via front-end acceptance surfaces — its own or third parties' — or from platforms acting for sub-merchants), applies risk screening and authentication as required, and routes each transaction into the relevant card/bank network for an authorization decision, recording the outcome per attempt. Without it there is no processing: the product is a payouts service or accounting tool.
3. **Money completion: clearing, settlement, funding.** Approved transactions are cleared and batched into settlements; processing fees are computed and either netted from the payout or billed separately; funds are paid out to the merchant's designated bank account on a defined schedule; balances, accrual, failed payouts, and negative-balance debits are managed by the platform. Without it the product is an authorization-only front end whose merchant still needs a separate acquiring/settlement relationship.

### L1 — Common Mature Structure

Present in essentially all mature current products; makes the Type practical but does not define it:

- dispute/chargeback lifecycle: notification, funds hold, evidence submission within a response window, challenge or concede, reason codes, prevention tooling
- refunds (full/partial) and reversals against processed transactions
- in-flow risk screening and cardholder/bank authentication
- vault/tokenization of payment instruments; account updater; network tokens
- fee machinery: fee profiles/pricing, statements, net-vs-gross payout configuration
- webhooks/events; operational dashboards (transactions, settlements, deposits, disputes); reporting and deposit reconciliation
- platform/sub-merchant enablement: enrollment workflows and forms, per-seller identities and accounts, split payments, per-seller settlement
- multi-currency settlement (per-currency bank accounts, presentment vs settlement currency)
- accelerated payout tiers (same-day/instant) with eligibility
- omnichannel intake surfaces (hosted pages, payment links, virtual terminal, terminals) — where intake is bundled
- reserves and risk-based payout holds as standing risk levers

### L2 — Variant / Optional Structure

- **Distribution model:** direct merchant relationships; classic acquiring distribution via ISOs and banks; ISV/platform-embedded (sub-merchant aggregation, "PayFac-style"); white-label by institutions
- **Intake depth:** full acceptance stack bundled vs decoupled (front-end provided by other products; processor receives transactions behind it)
- **Pricing presentation:** interchange-plus, flat-rate, subscription/SaaS-style billing of fees
- **Settlement speed tiers and schedules** (product- and country-specific; configurable)
- **Regional method coverage and compliance packs** (local schemes, bank-debit systems, mandates)
- **Bundled adjacent products** by the same vendor (billing, issuing, capital, treasury accounts)

### L3 — Vendor-specific Structure (stays in Research Notes)

- Finix: Identity/Merchant/Transfer/Settlement resource model; `gateway`/`processor` engine fields; beneficial-owner identities >25%; split_transfers; net/gross payout types; specific settlement states.
- Stax: "Stax Connect" partner console; four named enrollment methods; pend-reason catalog; stated review-time benchmark (~36–48h) and stated card/ACH dispute windows (product statements, US-specific).
- Stripe: Payout/Connect/Treasury/Capital product names; country T+X tables; first-payout delay ranges; minimum-payout and same-day-limit figures.
- Worldpay: Accept/Protect/Optimize/Embed/Move Money suite naming; "now part of Global Payments"; displayed enterprise-volume marketing figure.

## Vendor-specific Findings

- Finix treats the payout destination change as a risk event requiring review; failed funding transfers disable settlements with an automatic retry ladder before human review (Layer A).
- Stax documents the liability chain explicitly — the platform is debited before the sub-merchant, and recoupment failure drives reserves/terminations (Layer A). This is the clearest articulation of the processing platform's financial intermediation role found in the sample.
- Stax's enrollment funnel gives partners ("Your move" vs "With Stax") a shared operational pipeline for underwriting resolution — a partner-workflow detail beyond the merchant-facing flow (Layer A).
- Stripe separates payout cadence from settlement timing as two configurable concepts and ties acquiring fees to the settlement currency (Layer A; cross-check).
- Worldpay markets "dynamic routing"/"revenue boost" authorization-optimization products — routing *inside* its own processing stack, distinct from cross-provider orchestration (page-level).

## Rejected Findings

- **"A processing platform is a gateway with more features."** Rejected as a definition: it collapses the stack-position distinction the directory makes; the account/engine/funding spine is the distinct center.
- **"Chargeback windows are 120 days (cards) / 60 days (ACH)."** Rejected as canonical: single-product (Stax, US) statement reflecting scheme/regulator rules that vary by network and market; the final document keeps only the concept of network-defined windows.
- **"Underwriting review takes ~36–48 hours."** Stax operational benchmark, not structure; excluded from the final document.
- **"Payouts are daily at T+1/T+2."** Rejected as canonical: configurable tiers differ per product, country, and method; only the concept of scheduled, tiered funding is canonical.
- **"A processing platform must own payer-facing checkout."** Rejected: the classic decoupled model has front ends owned by others; Finix itself restricts raw-data intake to PCI Level 1 organizations. Intake depth is L2.
- **"Sub-merchant aggregation (PayFac) defines the Type."** Rejected: it is a distribution/market variant; direct-merchant and bank/ISO-distributed models satisfy the same L0.
- **"Processing volume statistics (e.g., trillions annually) as evidence of structure."** Marketing figures; excluded.

## Boundary Findings

1. **vs Payment Gateway (sibling, §08) — the central boundary.** The classic stack separates the front end (gateway: acceptance surfaces, secure transmission of payment data, outcome records) from the back end (processor: processing account, network routing, clearing/settlement/funding). Every modern product sampled bundles both (Finix, Worldpay, Stripe; the gateway research found the same for Adyen/Braintree/Checkout.com), so the two directory leaves overlap on the same products and differ in emphasis. Structural test: remove the administered processing account + settlement/funding → a gateway front-end remains; remove the payer-facing acceptance surfaces → a processing engine remains, served by any front end. Consistent with the flag recorded in research/payment-gateway.md; joint review required.
2. **vs Merchant Payment Platform (sibling, §08).** Terminology sibling: the market uses "payments platform for merchants" loosely for the same bundled product. No distinct structure observed at research depth — probable Alias. Flag for joint review when that leaf is processed (the gateway research flagged it identically).
3. **vs Payment Orchestration Platform (sibling, §08).** Orchestration is a merchant-side control layer *above* multiple independently contracted providers; it does not hold the processing account, does not authorize, does not settle. The processing platform *is* the processing path (one of the routable targets). Boundary holds.
4. **vs Card Processing Platform (sibling, §08).** Same word, opposite sides of the network: issuer-side card processing runs cardholder accounts and issuer authorizations for card issuers; this leaf is acquiring/merchant-side. Expected to hold; no issuer-side product was sampled — confirm when Card Processing Platform is processed.
5. **vs Billing Platform / Subscription Billing (§08).** Billing decides what and when to charge (plans, invoices, dunning); the processing platform executes charges and completes money movement. Bundled billing products are adjacent Types. Holds.
6. **vs Retail POS (05.10) / Restaurant POS (05.10).** POS composes the sale (catalog, cart, staff, checks) and uses a payment stack; the processing platform never composes the sale. "Payments included" POS is bundling. Holds.
7. **vs Fraud Detection Platform (§15).** Standalone cross-industry risk decisioning vs screening embedded inside the payment flow. Holds.
8. **vs Peer-to-peer Payment Application (§08).** No merchant processing account, no underwriting, no acquiring relationship — consumer-to-consumer money movement. Holds.
9. **vs Invoicing Application / Accounts Receivable Management (§08).** AR/invoicing manages the receivables book and may *use* a processing platform to collect; it does not run the processing account or settlement. Holds.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Classic decoupled processors** (bank-sponsored acquiring, ISO distribution, batch settlement era): merchant application/underwriting → MID provisioning → network routing → scheduled settlement into the merchant's bank account → chargeback handling. All three L0 properties present. Fits. (No classic-era product was directly fetched — Fiserv/CardConnect unreachable — so this check is structural reasoning + Worldpay's ISO/bank channel evidence, not direct Layer A. Recorded in Uncertainties.)
- **Modern API-first platforms:** the same spine with self-serve underwriting and API-configurable settlement. Fits.
- **Regional acquirers** (SEPA/local-scheme acquirers, UPI-stack processors): the L0 is method-agnostic ("card/bank network or equivalent"); fits structurally, though no regional acquirer was directly sampled.
- **PayFac/platform aggregators:** sub-merchants are underwritten and provisioned inside the platform; the spine is unchanged, only the account-holder relationship is nested. Fits as variant.

The definition does not over-fit the current API-first generation; the strongest over-fitting risk (requiring payer-facing intake surfaces) was deliberately excluded to L2.

## Uncertainties

- **Worldpay depth:** evidence is product-page level only (developer docs unreachable). Suite structure and distribution model confirmed; settlement/dispute operational flow not directly observed for Worldpay.
- **Stax settlement detail:** funding mechanics implied via underwriting/deposit-policy/bank-validation evidence; the settlement page itself was not fetched.
- **Classic-processor reach:** Fiserv/CardConnect/TSYS/Global Payments/Adyen/Helcim all unreachable; the "classic decoupled processor" model rests on Worldpay's positioning + structural reasoning rather than a fetched operational document.
- **Taxonomy intent:** whether the directory intends Payment Processing Platform as the distinct classic-processor Type or as a synonym bucket for bundled payment products is not decidable from product research; both readings produce the same L0, but the alias question (esp. vs Merchant Payment Platform) needs joint review.
- **Issuer-side contrast:** Card Processing Platform was not sampled; the acquiring-vs-issuing boundary is stated from stack reasoning, pending that leaf's research.
- **Precise operational facts** (settlement timing tables, dispute windows, review SLAs, volume figures, retry counts) deliberately excluded from the final document per the evidence rules; some are recorded here as product-specific L3.

## Final Synthesis

A **Payment Processing Platform** is best understood as the **money-completion back end of electronic payments for selling businesses**: it establishes and administers each merchant's payment-processing account (underwritten and provisioned by the platform or its acquiring partners), runs transactions through risk screening into the card/bank networks for authorization, and then completes the financial cycle — clearing, settlement, and funding the merchant's designated bank account, with processing fees netted or billed — while holding the risk levers over that money movement (payout holds, reserves, negative-balance debits, terminations) and operating the dispute/chargeback lifecycle in which it stands financially between the networks and the merchant.

Everything else commonly associated with the category — payer-facing acceptance surfaces, tokenization, terminals, multi-currency settlement, accelerated payouts, platform/sub-merchant enablement, reporting — is mature-market structure layered on that spine, or a distribution/intake variant. In the current market most such products also bundle the gateway front end, so the Payment Gateway and Payment Processing Platform directory leaves largely overlap on the same products and differ in stack emphasis; that overlap is recorded as a boundary issue for joint review, together with the probable Merchant Payment Platform alias.
