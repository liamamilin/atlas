# Research Notes — Fraud Prevention Platform

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what "Fraud Prevention Platform" (Directory §15, Cybersecurity, Identity & Trust) is as an Application Type: what it protects, what objects exist inside it, how evaluation and enforcement work across a digital business's customer journey, what feedback loops make it a platform, and — critically — where it sits against two flagged counterparties:

1. **Fraud Detection Platform** (§08, processed 2026-09-07) — flagged PROBABLE OVERLAP; that pass proposed the discriminating test "money-loss decision loop on customer activity records (fraud detection) vs attack/abuse prevention posture on identity/session surfaces (fraud prevention §15)" and explicitly left the §15 leaf's scope for joint review.
2. **Account Abuse Protection** (§15, processed 2026-09-06) — flagged adjacent/heavily overlapping; that pass's boundary test holds that account abuse protection centers the **account lifecycle** while fraud prevention centers **transactions/payments**, and flagged Sift as spanning both.

This pass must resolve both flags from the §15 side.

## Initial Boundary

Working hypothesis before research (guided by the two sibling passes):

- The §15 leaf is the merchant/digital-business-facing fraud platform category — the products the market actually calls "fraud prevention platforms" (Sift literally titles itself this; Riskified, Forter, SEON all sell under the prevention label).
- Hypothesis to test: the §15 center of gravity is the **operator's own customer journey** (signup → login → in-session → checkout/payment → post-transaction), not a single decision point and not identity/session surfaces alone.
- Nearest confusions: Fraud Detection Platform (§08; same machinery, different framing?), Account Abuse Protection (§15; account-lifecycle slice), Bot Management/DDoS (traffic-centric edge), Identity Verification/KYC (point-in-time proofing), Payment Orchestration (consumes fraud decisions), AML Platform (regulatory objective).

## Research Questions

1. What do products carrying the market name "fraud prevention platform" actually center on — transaction decisioning, account events, abuse, or the whole journey?
2. What is the unit of evaluation: the business record (order/transaction), the interaction (session/login), or the actor (persona/device)?
3. What decision vocabulary do these platforms return, and who executes it?
4. How are the platforms integrated into the operator's properties — client-side instrumentation, server APIs, both?
5. What fraud classes do the platforms claim: payment fraud only, or payments + ATO + fake accounts + policy abuse?
6. What feedback loops exist (chargebacks, disputes, labels, network intelligence), and what commercial models (tooling, guarantee/liability, score feed)?
7. What does onboarding look like (historical data, listen/monitor modes, validation)?
8. Who operates the platform day-to-day — operator fraud teams, vendor analysts, or both?
9. Boundary questions: vs Fraud Detection Platform §08, vs Account Abuse Protection §15, vs Bot Management, vs IDV/KYC, vs AML, vs Payment Orchestration.
10. Historical check: would older/regional/implementation-poor fraud prevention (manual merchant review desks, AVS/CVV + blocklists, 3-D Secure step-up) still satisfy the candidate core?

## Representative Products

| Product | Why selected | Evidence tier reached (this pass) |
|---|---|---|
| Forter | Archetypal "fraud prevention" merchant platform; full docs public covering fraud management + abuse prevention + account protection + chargeback recovery | Tier 1 (docs.forter.com — overview, checkout integration, abuse prevention, account protection) |
| SEON | Transparent API-first tooling pole; strong public docs; fraud + AML + IDV bundling | Tier 1 (docs.seon.io — product overview, end-to-end, scoring & decisioning, common fraud problems) |
| Riskified | Guarantee/liability pole; journey-wide product family (Chargeback Guarantee, Account Secure, Policy Protect, Dispute Resolve) | Tier 2 (official homepage, platform page, Account Secure page; docs 403) |
| Sift | Self-described "Fraud Prevention Platform for Digital Business"; spans payment fraud + ATO + fake accounts; console/workflow model visible | Tier 2 (homepage fetched fresh 2026-09-08; developers docs unreachable) |
| Arkose Labs | Challenge-enforcement pole on identity + payment touchpoints; bot/fraud convergence; warranty model | Tier 2 (payment-fraud solution page + platform/product structure; docs transport error ×2 across two passes) |

Cross-references reused from sibling passes (cited, not re-fetched): Castle and DataDome Account Protect (Tier 1, research/account-abuse-protection.md) for the account-event decision vocabulary; Signifyd and SAS (research/fraud-detection-platform.md) for the §08 side of the boundary.

Selection covers: full-journey platform vs transaction-centered vs identity-touchpoint-centered; tooling vs guarantee/warranty; operator-tuned vs vendor-managed; transparency-first vs network-intelligence-first; Tier-1 and Tier-2 evidence.

## Sources

Fetched 2026-09-08:

- Forter — docs.forter.com: Overview (Fraud Management); Account Protection Overview; Checkout Integration; Abuse at Checkout — https://docs.forter.com/overview , https://docs.forter.com/sMivTlM7-OuDz3Q6WlZOp , https://docs.forter.com/checkout-integration , https://docs.forter.com/abuse-at-checkout
- SEON — docs.seon.io: Product overview; End-to-end fraud prevention; Scoring and decisioning; Common fraud problems — https://docs.seon.io/getting-started/product-overview , https://docs.seon.io/getting-started/end-to-end-fraud-prevention , https://docs.seon.io/getting-started/scoring-and-decisioning , https://docs.seon.io/getting-started/common-fraud-problems
- Riskified — https://www.riskified.com/ , https://www.riskified.com/platform-riskified/ , https://www.riskified.com/account-secure/
- Sift — https://sift.com/ (homepage incl. console mock and consumer-journey model)
- Arkose Labs — https://www.arkoselabs.com/solutions/payment-fraud/ (plus platform/product/solutions structure from page navigation)

Reused from sibling passes:

- Castle, DataDome Account Protect, Sift homepage (2026-09-06), Arkose homepage/ATO — research/account-abuse-protection.md
- SEON scoring/case management, Signifyd, SAS, Sardine — research/fraud-detection-platform.md

### Source-access Limitations

- docs.riskified.com returned 403 (1 attempt). Riskified evidence is official product/platform pages (Tier 2): structural claims supported, precise operational details not asserted.
- sift.com/platform returned 403 (1 attempt this pass; also unreachable 2026-09-07 per sibling pass); developers.sift.com unreachable both passes. Sift evidence = homepage only (Tier 2). Console contents in the homepage mock are treated as vendor-presented, not independently verified.
- docs.arkoselabs.com transport error (1 attempt this pass; 1 prior attempt in the account-abuse pass) — dropped per the two-failure rule. Arkose evidence = official solution/platform pages (Tier 2).
- Vendor performance figures visible on marketing pages (persona counts, event volumes, signal counts, latency claims, percentage improvements) are treated as marketing claims and are NOT promoted to the final document.

## Product Observations

### Forter (Tier 1 — official docs)

Evidence layer: A.

- **Fraud Management center**: "ensure that only good, legitimate customers are able to checkout on your site while fraudsters are identified and blocked. Forter will send approve or decline decisions for every single transaction." Decisions 100% automated, powered by a persona graph (claimed 1B personas — marketing figure) + machine learning.
- **Integration positions**: pre-authorization (decision before payment gateway call) or post-authorization (after; authorization response incl. AVS/CVV/3DS results must be fed back).
- **Front-end integration**: JavaScript snippet on the website + Mobile SDKs for native apps; collects behavioral data asynchronously and generates a unique per-user token (forterTokenCookie / forterMobileUID) included in Order API requests.
- **Order API**: full checkout context — connectionInformation (customer IP, user agent, token), cartItems, payment[] (split payments, gift cards, loyalty points), delivery/recipient details, accountOwner, customerAccountData.
- **Decision vocabulary**: Approve / Decline / **Not Reviewed**. Approve → capture funds, confirm, invoice; Decline → cancel and communicate with customer. "Not Reviewed" occurs for defined conditions: Listen Mode ramp, newly added payment methods pending validation, missing data (no BIN/email/phone), merchant IP instead of customer IP, no payment data — in which case the merchant "act[s] according to the policies in place prior to the integration."
- **Onboarding discipline**: sandbox integration tests per use-case scenario; production Data Validation (daily automated reports on live data accuracy/completeness); **Listen Mode** (traffic monitored, models calibrated, decisions return "Not Reviewed", documented duration "around 7-14 days"); then Go Live.
- **Post-purchase loop**: Order Status updates on fulfillment/authorization; **Dispute Notifications** (chargebacks/claims/fraud alerts via PSP webhook or Dispute API) — "extremely important because it enables Forter's system to learn and continually improve future decisions"; **Historical Data upload** (past orders + account data incl. actual fraud outcomes; 1 year for returns/INR) so the model is customized to the merchant's risk profile "from Day 1."
- **Abuse Prevention at checkout**: policy types — Item Not Received (INR) Abuse, Limited Item Abuse, Promotion Abuse, Reseller Abuse, Reshipper Abuse, Returns INR Abuse. Policies built in a Policy Builder (merchantPolicyId returned in responses); outcomes are either a decline decision or a recommendation (e.g. MONITOR_POTENTIAL_COUPON_ABUSE); velocity counters over prior returns/INR refunds; compensation/returns data (compensationStatus) flows back.
- **Other product lines**: Chargeback Recovery; Payment Optimization (3DS recommendation/execution, card vaulting, network uplift, Visa Data Only, MIT flows, migrate-to-pre-auth, payment orchestration, predictive payments routing); **Account Protection** (Sign Up Protection, Login Protection, Session Protection) — "Not every user attempting to log in to or create an account on your site is the legitimate account owner… fraudsters and abusers… exploit the account ecosystem to commit various types of fraud and abuse, including account takeover, Incentive & referral abuse, PII and loyalty points theft, card testing, payment fraud and more… ensuring the account ecosystem remains secure at every touchpoint — from registration and login to in-session activities performed while logged in." Also Element for PSPs and Agentic Commerce.

### Riskified (Tier 2 — official product/platform pages)

Evidence layer: A for what the pages literally claim; Tier 2 (docs unreachable).

- **Positioning**: "AI fraud prevention fueling ecommerce success"; "secure every step of the customer journey from login to checkout to refund claims and returns."
- **Platform layer — Data Collection**: device data and behavioral insights collected by the **storefront Beacon**; "knowledge about all chargebacks incurred"; a global **Merchant Network** pooling eCommerce activity and fraud patterns across merchants.
- **Platform layer — Analytics**: real-time decisions; ML features + **Smart Linking** drawing on "over a billion historical transactions" on the network (marketing figure); Decision Optimizer; unsupervised AI monitoring for anomalies and suspected fraud rings; **"Dedicated risk analysts monitor performance 24/7 and adjust thresholds to protect each merchant's unique interests"**; per-industry/type-of-goods/merchant model optimization; false-decline identification.
- **Platform layer — Control Center**: dashboards; decision insight; "fraud analysts and call center agents can better interact with customers, even overriding the models' decisions."
- **Products**: Chargeback Guarantee ("guaranteed performance and instant decisions"; customer quote: "The fraud that does come in is covered by the liability shift"); Adaptive Checkout (dynamically adapts the shopping journey); Policy Protect ("preventing refund, promo, and reseller abuse"); Dispute Resolve (chargeback management/recovery); **Account Secure** — ATO Prevention ("catches malicious login attempts by both bots and humans"; "models compare the current session to past behavior by the account owner… provide an **allow/notify/challenge** decision"), Fake Account Prevention ("detects and blocks anomalous sign-up activity"), Account Recovery (tracks account security status; notifies owners after an attack); "Accuracy driven by our expertise at checkout" — transaction history at the merchant and across the network feeds ATO models; fully automated, no rule-setting or alert-response burden on the merchant.

### SEON (Tier 1 — official docs)

Evidence layer: A.

- **Product overview**: "comprehensive suite of fraud prevention and compliance solutions tailored for financial services, fintechs, iGaming operators, e-commerce platforms, retailers…" Modular APIs usable individually or as a complete risk strategy; targets "transactional fraud, synthetic identities, AML compliance."
- **Fraud API** (primary tool): consolidates digital footprinting, decisioning, risk scoring in one response. Digital Footprint = Email/Phone/IP APIs (linked profiles, data breaches, reputation; disposable emails, suspicious IPs). Device Intelligence = SDKs tracking device attributes, behavioral biometrics, interaction patterns ("bot activity, device spoofing, multi-accounting").
- **End-to-end framing**: "All the data is fed through rules, which calculate the risk for specific user actions (login, signup, etc.) or transactions." "SEON enriches and analyzes data points at signup, checkout, or login." Use-case picker: Register, Login, Deposit, Withdrawal, Payment. Industries: iGaming, Ecommerce, Travel & Ticketing, Banking & Insurance, Online Lending, Payment Gateways, Crypto exchange.
- **Scoring & decisioning**: score → low: approve; moderate: manual review; high: automatic decline. Rules contribute to the score; "all rule evaluations are included in the API response and event details for full transparency." Default rules (fixed) + custom rules (adjust score or directly approve/review/decline). AI Insights Score (explainable fraud probability) + AI Rule Suggestions (human-readable rules from labeled history). **Lists**: blacklist auto-declines, whitelist auto-approves, custom lists monitor without affecting score.
- **Bundled adjacencies**: AML screening (sanctions/PEP, continuous monitoring) integrated with the Fraud API; Case Management ("centralized hub for managing fraud investigations and regulatory reporting… unifying fraud and AML data"); Identity Verification product; Feedback Loops & Label API (labels train the ML models).
- **Common fraud problems** (the loss taxonomy the product markets against): payment fraud/chargebacks ("every $100 fraudulent transaction ends up costing $240" — marketing figure), fake accounts (promo/bonus abuse, multi-accounting rings), manual review cost, friendly fraud (first-party chargebacks), ATO attacks.

### Sift (Tier 2 — homepage, fetched fresh 2026-09-08)

Evidence layer: A for homepage claims; Tier 2 limitation recorded.

- **Positioning**: page title "Fraud Prevention Platform for Digital Business"; "real-time visibility into payment fraud, account takeover, and account abuse."
- **Use cases**: Payment Fraud ("approve more and decline fewer legit orders"), Account Takeover ("block unauthorized access in real time"), Fake Account Creation ("stop fraudulent signups at the door"). Industries: SaaS, e-commerce, marketplaces, iGaming ("cash-out abuse, multi-accounting, deposit fraud"), food & delivery, travel, fintech.
- **Platform components**: Decisioning Engine ("build rules and adapt risk strategy in real time"), Network Intelligence ("1T+ annual events" — marketing figure; "New-to-you users are often not new to Sift"), Automation & Workflows ("automate review, routing, and repetitive fraud ops work").
- **Products**: Payment Protection, Account Defense ("stop account takeover before it turns into revenue loss"), Sift Score API ("bring Sift intelligence into your own risk models"), Expert Services.
- **Console (homepage mock)**: workflows by name — "Create Order - User", "Transaction Workflow", "Queues", "Chargeback", "ATO" — each with runs, block rate, accuracy; dashboard: orders blocked, chargebacks received, block rate for manual vs automated decisions; **manual decisions: Accept / Block / Watch**; per-analyst review stats.
- **Consumer journey model**: Signup (Account creation) → Login (Account access) → Account activity (Behavior monitoring) → Transaction (Payment processing) → Post-transaction (Chargeback prevention).
- "Clearbox" transparency positioning; Expert Services; community/benchmarking (FIBR, Digital Trust Index).

### Arkose Labs (Tier 2 — official pages; docs unreachable)

Evidence layer: A for page claims; Tier 2 (docs transport error ×2 across passes).

- **Platform**: Arkose Titan — "unifies bot detection, account security, and adaptive enforcement… across the entire user journey. Stop bots, AI agents, and human fraud networks." Products: Bot Manager, Agent Trust Manager (AI-agent classification), Arkose Edge (server-side API protection), Device ID, Email Intelligence, Phishing Protection.
- **Solutions**: Account Takeover (credential stuffing, brute force), API Security, Human Fraud Farms, Fake Account Creation ("fake signups and bonus abuse"), SMS Toll Fraud (IRSF/SMS pumping), MFA Compromise (reverse-proxy phishing), **Payment Fraud** — "defends against card testing fraud… backed by a Card Testing Guarantee"; "combines risk-based decisioning and targeted friction"; detection engine (claimed 225+ signals); **Adaptive Challenges** ("AI-resistant challenges deploy incrementally complex puzzles"); Card Testing Warranty ("the only solution backed by a financial warranty"); 24/7 SOC; ACTIR threat-research unit.
- Industries: banking/fintech, gaming/iGaming, travel, e-commerce/retail, technology/telco.

### Cross-check from sibling passes

- **Castle** (Tier 1, account-abuse pass): event-typed API ($login, $registration, $transaction…) with three ML scores (Account Abuse / Account Takeover / Bot), policies returning **allow / challenge / deny**, review lists, fail-open posture. Demonstrates the account-event decision vocabulary inside a prevention product.
- **DataDome Account Protect** (Tier 1, account-abuse pass): login/registration events → recommendation **allow / deny / challenge / review**, feedback API, fail-open on timeout. Same vocabulary.
- **Signifyd / SAS** (§08 pass): guarantee-backed commerce protection and bank-grade model governance — the §08 side of the machinery.

## Cross-product Comparison

| Dimension | Forter | Riskified | SEON | Sift | Arkose Labs |
|---|---|---|---|---|---|
| Protected surface (self-described) | checkout + post-purchase + accounts + abuse + chargebacks (one platform, named product lines) | "every step of the customer journey from login to checkout to refund claims and returns" | "signup, checkout, or login" + deposits/withdrawals/payments | Signup → Login → Account activity → Transaction → Post-transaction | "entire user journey" — account events + payment flows + APIs |
| Client-side instrumentation | JS snippet + mobile SDKs generating per-user token (Tier 1) | storefront Beacon (device + behavioral) (Tier 2) | Device Intelligence SDKs (Tier 1) | not verified from reachable sources (Tier 2) | challenges/SDK embedded in flows (Tier 2) |
| Decision vocabulary | Approve / Decline / Not Reviewed (+ abuse recommendations) | order approve/decline; account events allow / notify / challenge | approve / manual review / auto-decline (+ list overrides) | Accept / Block / Watch + workflow queues | risk decision + enforced adaptive challenges |
| Evaluation machinery | persona graph + ML, 100% automated | ML features + Smart Linking + Decision Optimizer + unsupervised anomaly detection; vendor analysts adjust thresholds | transparent rules + ML (labels via Feedback/Label API); explainability first-class | Decisioning Engine rules + Network Intelligence; workflow automation | risk-based decisioning (claimed 225+ signals) + adaptive challenges |
| Fraud classes claimed | payment fraud, ATO, card testing, incentive/referral abuse, PII/loyalty theft, INR/promotion/limited-item/reseller/reshipper/returns abuse | payment fraud/chargebacks, ATO, fake accounts, refund/promo/reseller abuse | payment fraud/chargebacks, friendly fraud, fake accounts/promo abuse/multi-accounting, ATO | payment fraud, ATO, fake accounts, account abuse | card testing/payment fraud, ATO, fake accounts/bonus abuse, fraud farms, SMS toll fraud, API abuse |
| Ground truth / feedback | dispute notifications (chargebacks/claims/fraud alerts) + post-purchase status + historical data upload | all chargebacks collected; guarantee liability; per-merchant threshold tuning by vendor analysts | Feedback Loops & Label API; chargeback/friendly-fraud loss framing | chargeback workflow; post-transaction stage; network intelligence | warranty on card testing; SOC + threat research tuning |
| Commercial model | tooling (decisions automated; model customized per merchant) | guarantee/liability shift | tooling (score + rules console) | tooling (+ score-feed product, + expert services) | warranty (financial liability on card testing) |
| Operator-facing console | Portal (integration tests, data validation, policies) | Control Center (analysts/call-center can override) | Admin panel (rules, lists, case management) | console with workflows, queues, analyst stats | customer portal + 24/7 SOC |
| Adjacent bundling | 3DS/payment optimization, card vaulting, payment orchestration, PSP edition, agentic commerce | adaptive checkout, dispute recovery | AML screening, identity verification, case management | score API, expert services | bot manager, edge/API protection, phishing, email/device intelligence |
| Segments | digital commerce (travel, retail, marketplaces) | ecommerce (retail, luxury, travel, digital goods, ticketing) | fintech, iGaming, ecommerce, lending, gateways, crypto, banks | digital business broadly incl. iGaming, fintech, marketplaces | banking, gaming, travel, ecommerce, telco |

### Stable commonalities (evidence layer B)

Across the five sampled products (plus the two sibling-pass cross-checks):

1. **The protected object is the operator's own customer journey** — every product frames its scope as a journey across the digital business's customer-facing flows: account creation/access (all five), in-session activity, checkout/payment (all five), post-transaction (fulfillment, disputes, returns; four of five with chargeback/dispute handling explicit).
2. **Touchpoint evaluation into enforcement decisions** — each received interaction is evaluated (rules and/or ML over enriched signals) and resolved into an actionable decision the operator's flow executes: approve/decline on orders; allow/challenge/block on account events; review/queue class in between. Documented directly at all five (Tier 1: Forter, SEON; Tier 2: Riskified, Sift, Arkose) and in both sibling cross-checks.
3. **Signal enrichment as the evaluation substrate** — device intelligence/behavioral signals, digital footprint / identity-attribute intelligence (email/phone/IP), network/IP reputation; plus journey/entity context (account history, persona linking).
4. **Cross-operator network intelligence is a dominant but not universal posture** — Sift, Riskified, Forter, Arkose claim shared networks; SEON's documented machinery evaluates the customer's submitted data + labeled history (network posture not asserted from its docs).
5. **Chargeback/commercial-outcome feedback** — chargebacks/disputes are collected as ground truth at Forter, Riskified, Sift, Arkose (warranty), and framed as the primary loss at SEON (whose Feedback/Label API is the documented tuning path). Confirmed account-fraud and abuse outcomes flow back similarly.
6. **Human review exists in two places** — operator-side queues/analyst consoles (SEON case management, Sift workflows/queues, Riskified Control Center overrides) and vendor-side analysts (Riskified 24/7 threshold adjusters, Arkose SOC, Forter implementation/QA). Fully-automated decisioning is the stated posture at Forter ("100% automated") and Riskified Account Secure ("without spending time setting rules or responding to alerts").
7. **Lists override or anchor scores** — documented at SEON (blacklist/whitelist auto-outcomes) and in the sibling cross-checks (Castle lists); consistent with the §08 pass's finding.
8. **Abuse/policy-fraud classes are first-class, not afterthoughts** — promotion/reseller/returns/INR/limited-item abuse (Forter), refund/promo/reseller abuse (Riskified), promo abuse/multi-accounting (SEON), bonus abuse/fraud farms (Arkose), account abuse (Sift).
9. **Embedding into the operator's flow at the moment of the interaction** — decisions returned synchronously at signup/login/checkout decision points (all five); the operator's application executes the action (capture funds, cancel, allow login, require verification).

## Canonical Model

```text
Operator's digital business
  └── Customer journey (account creation → login → in-session activity → checkout/payment → post-transaction)
        └── Journey touchpoints instrumented/embedded (client-side token + server decision calls)
              └── Per-interaction evaluation (rules + models over enriched signals + entity/persona history + network intelligence)
                    └── Enforcement decision returned into the flow at that moment
                          (approve/allow · challenge/step-up · decline/block · review)
                    └── Confirmed commercial outcomes (chargebacks/disputes, confirmed account fraud, abuse)
                          └── feed back: per-operator tuning, labels, network intelligence
                    └── measured on: fraud loss vs approved revenue
```

## Abstraction Levels

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product is no longer this Type:

1. **The protected journey** — the operator's own customer-facing journey across its digital properties (at minimum account creation/access and payment/transaction touchpoints; typically in-session and post-transaction as well) held as one protected surface. Remove → point tooling (a chargeback recoverer, a signup CAPTCHA) or security tooling with no journey anchor.
2. **Touchpoint evaluation into enforcement decisions** — each interaction received at a journey touchpoint is evaluated for fraud/abuse risk and resolved into an actionable decision returned into the operator's flow at that moment — approve/allow, challenge/step-up, decline/block, or review — spanning money decisions (approve/decline an order) and access decisions (allow/challenge/block an account event). Remove → passive analytics/alerting or a raw score/data feed with no journey enforcement.
3. **The fraud-loss accountability loop** — the platform is measured on the operator's commercial fraud losses versus approved revenue, and confirmed outcomes — chargebacks/disputes above all, plus confirmed account fraud and policy abuse — flow back to tune evaluation (per-operator tuning, labels, cross-operator network intelligence where present). Remove → generic security event monitoring with no commercial loss economy.

Jointly-held is load-bearing: 1 alone = a journey-mapped UX/analytics layer; 2 without 1 = a scoring service; 3 without 1+2 = chargeback reporting.

### L1 — Common Mature Structure

- Client-side instrumentation (JS snippet / SDK / beacon generating per-session/device tokens, collecting device + behavioral signals) alongside server decision APIs
- Signal-enrichment breadth: digital footprint (email/phone/IP reputation, breaches), device intelligence, behavioral biometrics
- Entity/persona intelligence: account profiles, identity linking across records, cross-operator network intelligence ("new-to-you users are often not new to the network")
- Rules engine + ML scoring with explainability (rule-hit transparency; AI-generated insights/rule suggestions)
- Managed lists (block/allow/monitor) overriding or anchoring scores
- Abuse-policy machinery (promo, reseller, returns/INR, limited-item policy types with monitor/decline outcomes)
- Review queues / case management (operator-side and/or vendor-side analysts)
- Chargeback/dispute ingestion and (in some) dispute-recovery modules
- Dashboards: block rates, chargeback trends, decision accuracy, analyst performance
- Onboarding discipline: historical data upload, monitoring-first (listen) mode before enforcement, data validation, sandbox testing
- Step-up orchestration (3DS recommendations, verification challenges) between allow and block
- APIs + webhooks + sandbox environments

### L2 — Variant / Optional Structure

- **Commercial model**: tooling (operator owns outcomes) vs guarantee/warranty (vendor financially liable for approved transactions — Riskified Chargeback Guarantee, Arkose Card Testing Warranty, Signifyd per §08 pass) vs score-feed (Sift Score API)
- **Journey scope**: full-journey platforms vs transaction-centered (order decisioning) vs identity-touchpoint-centered (signup/login enforcement)
- **Automation posture**: operator-tuned console (SEON transparency-first) vs vendor-managed/fully automated (Riskified Account Secure, Forter)
- **Data posture**: cross-merchant network intelligence vs own-data evaluation
- **Segment tuning**: ecommerce/retail, travel, marketplaces, iGaming, fintech, telco
- **Bundled adjacencies**: AML screening (SEON), identity verification, payment optimization/3DS/card vaulting (Forter), bot management/edge (Arkose), agentic-AI defense (Arkose Agent Trust Manager, Forter Agentic Commerce — era-current)
- **Deployment**: SaaS API + browser/mobile instrumentation; PSP-embedded editions (Forter Element)

### L3 — Vendor-specific (Research Notes only)

- Forter: Approve/Decline/Not Reviewed state names; forterTokenCookie/forterMobileUID token names; Listen Mode with documented "around 7-14 days" duration; test emails (approve@forter.com …); MONITOR_POTENTIAL_* abuse recommendation names; merchantPolicyId; compensationStatus object; 1B-persona claim; Element for PSPs; Agentic Commerce line.
- Riskified: storefront Beacon; Smart Linking; Decision Optimizer; Control Center; product names (Chargeback Guarantee, Adaptive Checkout, Policy Protect, Dispute Resolve, Account Secure); allow/notify/challenge account decision; false-decline identification; "2-3X stronger detection" and similar marketing figures.
- SEON: Fraud API naming; AI Insights Score; AI Rule Suggestions; blacklist/whitelist/custom-list semantics; Label API; exact industry list.
- Sift: Digital Trust & Safety positioning; Clearbox; Payment Protection/Account Defense/Sift Score API names; workflow names in console mock (Create Order - User, Transaction Workflow, Queues, Chargeback, ATO); Accept/Block/Watch manual decision labels; 1T+ events and 2.1B "authentic digital citizens" claims; FIBR/Digital Trust Index.
- Arkose: Arkose Titan; Bot Manager/Agent Trust Manager/Arkose Edge/Device ID/Email Intelligence/Phishing Protection names; adaptive-challenge economics; ACTIR; 225+ signals claim; Card Testing Warranty.
- Marketing figures (persona counts, event volumes, signal counts, latency, percentage improvements) deliberately excluded from the final document.

## Vendor-specific Findings

See L3. Not promoted: Forter's Not-Reviewed condition list and Listen Mode (product-documented onboarding discipline — generalized in the final document only as a monitoring-first pattern with weak wording); Riskified's vendor-analyst threshold adjustment (managed-model posture); SEON's three-list semantics (illustrative implementation of lists).

## Boundary Findings

| Neighboring Type | Relationship | Distinction test |
|---|---|---|
| Fraud Detection Platform (§08) | near-twin; same decision machinery, different organizing frame | §08 documents the org-agnostic fraud-operations decision loop (activity records → evaluation → decision + human review path → feedback) with bank/issuer/claims deployments in scope; this leaf centers the **digital business's customer journey** as the protected surface, with enforcement decisions (incl. challenge class) returned at journey touchpoints and the merchant fraud-loss economy (chargebacks, policy abuse, liability models) as ground truth. Remove the journey frame and merchant loss economy → §08's Type remains. Remove the org-agnostic operations framing → this Type remains. |
| Account Abuse Protection (§15) | sibling under §15; heavily bundled | Account abuse protection centers the **account lifecycle** (access, creation, account-linked privileges); this leaf centers the **journey + commercial fraud** (payments, chargebacks, policy abuse) with account touchpoints included. Remove transaction/payment/chargeback/abuse coverage → account abuse protection remains; remove account-event enforcement → transaction-fraud tooling remains. Products bundle (Sift Account Defense ≈ both). |
| Bot Management / DDoS Protection | adjacent; bot engines feed fraud platforms | Bot management is traffic-centric and account-agnostic at the edge (availability, scraping, forms); this Type is journey-centric and fraud-objective (money, accounts, policy abuse). Arkose bundles both — Bot Manager is a component of its fraud platform, not the Type itself. |
| Identity Verification / KYC | adjacent, bundled at signup | IDV is point-in-time real-world identity proofing (documents/biometrics, pass-fail); this Type is continuous behavioral/technical fraud-risk evaluation across the journey. Verification results serve as evaluation signals. SEON bundles both. |
| AML Platform (§08) | adjacent, bundled | AML's objective is regulatory compliance (suspicious-activity reporting, sanctions screening); this Type's objective is fraud loss and revenue. SEON documents both in one suite with shared case management; consistent with §08 pass's convergence note. |
| Payment Orchestration Platform | consumer of decisions | Orchestration routes charges across providers and may call fraud services as flow participants (recorded in that pass's research); the fraud platform owns the risk model and the fraud decision. |
| Chargeback/Dispute Management (recovery) | adjacent module | Recovery workflows fight/represent chargebacks after the fact (Riskified Dispute Resolve, Forter Chargeback Recovery as product lines); the fraud platform's core is deciding before/at the interaction, with disputes as feedback. |
| SIEM / Threat Intelligence | different domain | Security telemetry and attacker infrastructure vs the operator's customer commercial interactions. No journey touchpoints, no chargeback economy. |
| Retail Loss Prevention / Shrink (§05) | domain sibling | Physical-store loss events (theft, shrink) vs digital-journey fraud; different objects, different flows. |

### Joint-review dispositions (both prior flags)

1. **vs fraud-detection-platform (§08)** — the §08 pass's proposed placement for this leaf ("attack/abuse prevention posture on identity/session surfaces") is **refuted by this sample**: every product marketing itself as a fraud prevention platform centers commercial fraud (payments, chargebacks, abuse) across the customer journey; identity/session-only products (Castle, DataDome Account Protect) were correctly documented by the account-abuse pass as that sibling. **Keep-both RATIFIED** with the containment seam above: shared decision machinery; §08 = org-agnostic fraud-operations loop (human review path in its core; single-decision-point deployments at institutions documented there); §15 = journey-protection frame for digital businesses (enforcement vocabulary incl. challenge; merchant fraud-loss economy; liability models). Residual convergence risk recorded: vendors ship both framings under one product, and the seam will blur further.
2. **vs account-abuse-protection (§15)** — the account-abuse pass's boundary test is **confirmed from this side**: the account-lifecycle vs journey+commercial-fraud seam holds, with heavy product bundling (Sift) as the known overlap zone.

### Historical / market-sample check (per §24)

- **Thin ancestors satisfying the core**: a merchant's manual fraud desk reviewing suspicious orders before fulfillment (journey touchpoint evaluation → ship/hold/cancel decision, chargeback lessons applied by hand); AVS/CVV checks and stolen-card blocklists at checkout; risk-based step-up at the payment touchpoint (3-D Secure class — the challenge decision); early merchant plugins scoring orders against shared bad-card lists. None require client-side SDKs, ML, or cloud.
- **Correctly excluded**: standalone CAPTCHA/bot filters with no fraud-loss loop (components below the Type); issuer single-point authorization scoring and claims-fraud systems (§08 territory — single decision points of an institution's operation, not a customer-journey protection surface); workforce insider-risk (no customer journey); external brand-abuse takedown (digital-risk-protection territory, per that pass's note).
- The candidate L0 holds for old, regional, and implementation-poor realizations; no era-current technology (client SDK, ML, network intelligence, guarantee models) is baked into the core.

## Uncertainties

1. **Sift's integration shape** (client snippet, event API details) unverified — homepage-only evidence; all Sift structure marked Tier 2.
2. **Arkose's decision API shape** (how risk decisions vs enforced challenges are returned) unverified — docs unreachable across two passes; only vendor pages describe the mechanism.
3. **Network-intelligence posture at SEON** not asserted from its docs (only cross-product framing); treated as variant, not common-to-all.
4. **Fail-open vs fail-closed** for this market's products not documented in this pass's reachable sources (sibling pass documented fail-open for Castle/DataDome account-event products); kept out of the final document.
5. **Category naming drift**: vendors also sell this category as "Digital Trust & Safety" (Sift), "Commerce Protection" (Signifyd), "ecommerce risk management" (Riskified), "fraud prevention" (Forter/SEON). The directory's §15 leaf name matches the Sift/Forter/SEON usage. Whether the maintainers prefer one consolidated fraud-platform leaf remains a taxonomy question (recorded in STATUS.md, not silently resolved here).

## Final Synthesis

**Fraud Prevention Platform** (§15) is the digital business's own fraud-protection platform: a system embedded across the operator's customer journey — account creation and access, in-session activity, checkout and payment, post-transaction outcomes — which evaluates each customer interaction for fraud and abuse risk at the touchpoint where it happens, returns an enforcement decision the operator's flow executes at that moment (approve/allow, challenge/step-up, decline/block, or review — spanning money decisions on orders and access decisions on account events), and runs a fraud-loss accountability loop in which confirmed commercial outcomes (chargebacks and disputes above all, plus confirmed account fraud and policy abuse) feed back into evaluation, tuning, and — in the market's dominant posture — cross-operator network intelligence.

Its machinery (event → evaluate → decide → review → feedback) is shared with the §08 Fraud Detection Platform; what organizes this Type is the journey-protection frame for digital businesses, the enforcement decision vocabulary at journey touchpoints, and the merchant fraud-loss economy, including the guarantee/warranty commercial models in which the vendor stands financially behind its approvals. The defining core is small and implementation-agnostic: a merchant fraud desk with AVS/CVV checks, a stolen-card blocklist, 3-D Secure-style step-up, and chargeback lessons applied by hand satisfies it without any modern apparatus.
