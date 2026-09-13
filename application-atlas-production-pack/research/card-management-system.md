# Research Notes — Card Management System

Research date: 2026-09-10
Leaf: Card Management System (DIRECTORY §08 Finance, Banking, Insurance & Investment)
Slug: card-management-system

## Research Goal

Understand what a Card Management System (CMS) actually is as an Application Type: the issuer-side software that manages payment cards over their lifecycle. Determine its defining core, its standard capabilities, its variants, and its boundaries against the two sibling leaves (Card Issuing Platform, Card Processing Platform) and against neighboring Types (Core Banking System, digital banking/cardholder apps, campus card management).

## Initial Boundary

- The leaf sits in §08 among Card Issuing Platform / Card Management System / Card Processing Platform — three adjacent leaves that market products visibly span. Suspected family relationship from the start (analogous to the merchant-payment-platform resolution).
- "Card management system" is a polysemous industry term: it also names ID-badge/access-card systems (physical security) and campus-card systems (§23 has its own leaf). NIST even defines "card management system" for PIV government ID cards. This pass scopes to the payments meaning, which the directory's §08 placement disambiguates.
- Nearest confusions: Card Issuing Platform (program creation), Card Processing Platform (transaction machinery), Core Banking System (accounts/ledger), cardholder-facing mobile banking apps.

## Research Questions

1. What is the core object — what does the "card" record carry, and how does it relate to the cardholder and the account?
2. What is the card lifecycle and its status model?
3. What operational acts does the system perform (issue, activate, block, reissue, renew, replace, PIN, limits)?
4. What is the card product / program layer and is it definitional?
5. Who operates the system, through which surfaces (workbench, API, IVR, batch)?
6. Where is the boundary with Card Issuing Platform and Card Processing Platform?
7. How do digital cards, tokens, and wallet provisioning fit?
8. Historical check: do mainframe-era / regional / domestic-scheme card systems satisfy the same core?

## Representative Products

Selected for market representativeness, documentation quality, product philosophy, and customer tier:

| Product | Vendor | Tier / philosophy | Why selected |
|---|---|---|---|
| Marqeta Core API | Marqeta | Modern API-first issuing platform (fintech/BaaS tier) | Richest public operational docs; the "Powered by/Managed by" program model |
| Mastercard Processing Core (CMS) | Mastercard | Scheme-owned issuer processing | Its documentation literally names the "Card Management System (CMS)" and defines its object model |
| Way4 Card Issuing | OpenWay | Independent enterprise card software (banks/processors) | URL is literally "way4-card-management-system"; classic full-lifecycle issuer platform |
| PowerCARD-Issuer | HPS Worldwide | Global mid-tier suite (banks, credit unions, retailers) | QKS SPARK Matrix leader in the "Card Management Systems (CMS)" category |
| Total Issuing (TS2 / PRIME) | FIS (TSYS) | Heritage top-tier issuer processor | The classic issuer-processing stack now packaged as "Total Issuing" |
| Card Suite / Banktech issuing | Tietoevry | Regional European issuer suite | Uses the exact phrase "Card management system" as a named capability |
| Issuing API | Stripe | API-first issuing (platform/embedded tier) | Public docs for card management operations (replacements, PINs, controls) |
| Treasury Prime issuing API | Treasury Prime | BaaS issuing | Minimal clean example: card issued against account + card product + person |

Primary sample for comparison: Marqeta, Mastercard Processing CMS, Way4, PowerCARD-Issuer, FIS Total Issuing. Tietoevry, Stripe, Treasury Prime used as corroborating witnesses.

## Sources

Tier 1 (official operational documentation — fetched directly):

- Marqeta — "About Cards" developer guide: https://www.marqeta.com/docs/developer-guides/about-cards (fetched 2026-09-10)
- Marqeta — "Card Transitions" API reference: https://www.marqeta.com/docs/core-api/card-transitions (fetched 2026-09-10)
- Marqeta — "Card Products" API reference: https://www.marqeta.com/docs/core-api/card-products (search excerpt, 2026-09-10)
- Marqeta — "DiVA API Card Views": https://www.marqeta.com/docs/diva-api/cards (search excerpt, 2026-09-10)
- Stripe — Issuing docs index: https://docs.stripe.com/issuing/cards (fetched 2026-09-10)
- Mastercard — "Card Management System" guide: https://developer.mastercard.com/mastercard-processing-core/documentation/guides/card-management-system (search excerpt; page is JS-rendered, direct fetch returned no content)
- Mastercard — "Card Lifecycle" guide: https://developer.mastercard.com/mastercard-processing-core/documentation/guides/card-lifecycle (search excerpt; same JS limitation)
- OpenWay — "Way4 Card Issuing" product page: https://openwaygroup.com/way4-card-management-system (fetched 2026-09-10)
- HPS — "PowerCARD-Issuer" product page: https://www.hps-worldwide.com/product/powercard-issuer (search excerpt, 2026-09-10)
- HPS — "Card Issuing" business page: https://www.hps-worldwide.com/your-business/card-issuing (search excerpt, 2026-09-10)
- FIS — "Total Issuing Solutions": https://www.fisglobal.com/products/total-issuing and tsys.com issuer pages (search excerpts, 2026-09-10)
- Tietoevry — "Card issuing software": https://www.tieto.com/en/industries/financial-services/card-issuing (search excerpts, 2026-09-10)
- Treasury Prime — "Card Issuance" guide: https://docs.treasuryprime.com/docs/issuing-a-card (search excerpt, 2026-09-10)
- Cuscal — FAQ "What is a Card Management System (CMS)?": https://www.cuscal.com/faqs/issuing-faqs/what-is-a-card-management-system-cms (fetched 2026-09-10)
- MS Solutions — "SPARK CORE – Cards Management System (CMS)": https://www.mssolutions-group.com/use-case/spark-issuing-suite/cms (search excerpt, 2026-09-10)
- CLAI Payments — "Card Lifecycle Management / EVERYCARD": https://clai.com/card-lifecycle-management (search excerpt, 2026-09-10)
- QKS Group press releases — SPARK Matrix for Card Management Systems 2023/2024 (globenewswire/prnewswire excerpts, 2026-09-10)
- Stripe — "What is an Issuer Processor?": https://stripe.com/en-sg/resources/more/issuer-processor-basics (search excerpt, 2026-09-10)
- Adyen — "The evolution of modern card issuing": https://www.adyen.com/knowledge-hub/modern-card-issuing (search excerpt, 2026-09-10)
- NIST CSRC glossary — "card management system" (PIV context): https://csrc.nist.gov/glossary/term/card_management_system (search excerpt, 2026-09-10)

Source-access limitations:

- Mastercard developer documentation pages are JS-rendered; direct fetch returned empty content. Evidence for Mastercard Processing CMS relies on search-engine excerpts of the same official pages. Assertions from this source are kept at the level the excerpts support.
- FIS/TSYS and Tietoevry pages are marketing/product pages (Tier 2), not deep operational docs; claims from them stay at capability level.
- No vendor pricing, SLA numbers, or internal architecture claims were used.

## Product Observations

### Marqeta (Core API) — evidence layer A (direct fetch)

- "A card is a payment device that enables a user to conduct transactions at merchants. Cards can be physical or virtual. You can also tokenize cards for use in digital wallets."
- Card object is first-class: stores token, user token, card product token, fulfillment/personalization, expiration; Marqeta-provided: last_four, PAN, PIN, expiration date, barcode, **state and state reason**.
- KEY QUOTE: "Funds are not loaded onto or directly associated with a card. Rather, a card is a device used to access funds held in a user or business account."
- Each card has an associated **card product** object ("operates like a template when creating new cards, but the association continues — updating the card product affects each associated card throughout the card's lifetime") and a **user** object (cardholder + account).
- Card product config: card_life_cycle (activate_upon_issue, expiration_offset, reloadability, update_expiration_upon_activation), transaction controls, spend controls, digital-wallet tokenization controls; some overridable at card level.
- Lifecycle: issuance → activation → suspension/limitation/termination → expiration (auto-terminate at expiry). "Cards must be activated before use." Physical cards ship unactivated; virtual cards active immediately (typical).
- States manipulated via `/cardtransitions`; transition targets ACTIVE / SUSPENDED / TERMINATED; LIMITED state exists (temporarily non-functional except card-on-file transactions such as recurring charges).
- Transition **channel** values: ADMIN (Dashboard), API, FRAUD (Marqeta or card network), IVR, SYSTEM (e.g., suspended due to excessive failed PIN entries) — operator dashboard, program API, phone channel, and system-initiated transitions are all first-class.
- Rich **reason_code** taxonomy: activated first time, requested by you, inactivity, lost, stolen, cloned, compromised, expired, failed KYC, PIN retry limit reached, OFAC match, death notification, etc.
- Reissue: same PAN (e.g., damaged/expired) or new PAN (lost/stolen); reissue chains tracked (Card A > Card B > Card C); source card can be auto-terminated or left active.
- Lost/stolen/damaged playbook: lost → reissue with new PAN + suspend/terminate; stolen → reissue with new PAN + terminate; damaged → reissue with same PAN + terminate.
- PIN setting methods: iframe widget, IVR, `/pins` endpoint.
- Number of active/suspended cards per user configurable; activation validations (birth date, phone, SSN); cards can be moved between users/accounts (feature-gated).
- Digital wallet tokens: provisioned per card; state can be synchronized with card state on transition; tokens reassigned to reissued card on activation.
- Single-use vs multi-use cards (via velocity controls); bulk card orders; DiVA reporting views aggregate card inventory by state (card_created_date, card_activation_date, card_state, card_type).

### Mastercard Processing Core (CMS) — evidence layer A via search excerpts (JS-render page)

- Documentation literally titled "Card Management System". "The system uses three main classes of objects: **Client**, **Contract (account contract and card contract)**, **Card plastic (physical or virtual cards)**."
- "Clients can own many contracts, both account contracts and card contracts." — account contract and card contract are distinct object classes.
- "Card plastic sequenceNumber makes card management possible, as you can track all Plastic issued. The first card issued is assigned the sequence number '1'."
- "Only the expiry date and CVC change during renewal. The Primary Account Number (PAN), cardholder name, and PIN do not change."
- Card lifecycle: "issuing, activating, blocking, closing, and renewing or replacing a card."
- "Card activation means changing the card Plastic status in the Card Management System (CMS) from **Locked to Active**."
- Reissue operations: REISSUE (damaged card still in cardholder's possession; also physical mirroring an existing virtual card), RENEW / RENEW_D (expiring/expired; physical/virtual), REPLACE / REPLACE_D (replacement; physical/virtual).
- "The Mastercard Processing Card Management System (CMS) was not intended to serve as Customer Relationship Management (CRM) system. The CMS stores only basic information about the client, accountContract, and cardContract" — customData available for extensions.
- If issuers don't want to handle PAN, alternative **cbsNumber** is generated by the CMS or provided by the **Core Banking System** — explicit integration boundary with core banking.
- cardContractNumber stores the PAN (up to 19 digits, usually 16); card contract stores data directly related to the card.
- Classifiers on card contract (e.g., contactless flag, Automatic Billing Updater).

### OpenWay Way4 Card Issuing — evidence layer A (direct fetch, product page)

- URL slug is literally "way4-card-management-system"; positioned as "real-time payments platform… launch and scale modern payment products".
- "End-to-end full card lifecycle card and account management": digital on-boarding; data preparation & card personalization; instant issuing; account and transaction management; flexible fees/pricing/billing; flexible authorization controls; clearing and settlement; card stock management; tokenization; disputes; fraud prevention; loyalty.
- Card/non-card product types: credit, debit, prepaid, virtual, corporate/business/commercial, payroll, travel/multi-currency, crypto-backed, gift/retailer, BNPL, tokens, fleet/fuel, meal vouchers, multi-account cards.
- "95% parameter-driven" configuration: "New products, services, and processing rules are configured—not coded… Pricing, fees, limits, customer eligibility, loyalty rules, risk controls, authorization logic, channel settings, and lifecycle workflows, can be defined through business rule-based configuration."
- "Intuitive UI (Workbenches)" listed as a system characteristic; automated daily processes; extensive API catalogue.
- Multi-institution, multi-currency, multi-country, multi-language; white-label issuing; complex account hierarchies; deployment on-premise/cloud/SaaS/hybrid.
- Scale claims (200M+ cards/installation, 5,500 TPS) — vendor marketing numbers, recorded here only as positioning, not used in the final document.

### HPS PowerCARD-Issuer — evidence layer A via search excerpts

- "Complete services for issuance and management of all payment types in all formats (credit, debit, prepaid, etc.)… supports all kind of issuers, from small to large and global financial institutions, banks, credit companies, retailers and private card processing companies."
- "Full multi-currency, multi-product, multi-institution and multi-language capabilities and manages card portfolios across different countries and for different issuers on a single global platform."
- Module map: **Card Management Module** + Customer Account Management (Credit Account Module, Prepaid Account Module) + Issuer Clearing & Settlement Management + Fraud Management + Chargeback Management + Reporting + Loyalty + Security Management (HSM interfaces) + interfaces to bank host.
- "PowerCARD Connect' APIs… more than 120+ APIs to allow any third party system to trigger services or use data stored on PowerCARD."
- "At the heart of PowerCARD-Issuer is a powerful relational database, giving a consolidated view of the customer and the customer's transactions."
- Business page: issuers need "to manage all card types… through all stages of their lifecycle"; "daily involvement from business, marketing, IT and operation functions."
- QKS Group positions HPS as leader in "SPARK Matrix for Card Management Systems (CMS)" (2023, 2024) — the analyst category name matches this leaf.

### FIS Total Issuing (TS2 / PRIME, ex-TSYS) — evidence layer B (product pages)

- "TSYS joins FIS as Total Issuing™ Solutions." TS2: "an end-to-end platform for consumer and commercial card payments. Its flexible, API-first architecture connects onboarding, servicing, authorizations, risk and fraud management, digital experiences, loyalty, communications and scheme-agnostic, real-time virtual card issuance."
- PRIME in the Cloud: "API-centric and cloud-native platform… supporting consumer credit, debit, unlimited currency prepaid and commercial cards with a single customer view… virtual cards, wallets and tokenized payments."
- FIS glossary line: "Card issuing platforms enable banks and fintechs to launch, manage and process credit, debit and prepaid card programs."
- Global Payments/TSYS issuer-solutions line: "Issuer processing manages transaction authorization, servicing, fraud prevention and payment operations across credit, debit and prepaid card programs."

### Tietoevry Card Suite — evidence layer B (product pages)

- Capability literally named "**Card management system**: Manage products, cardholders, lifecycle events, authorisation logic, token management, and operational workflows from a unified platform."
- "Tieto Banktech's issuing software helps banks and issuers create, manage, and process all card programs across the full card lifecycle. This includes card product setup, cardholder management, authorization, settlement, billing, invoicing, PIN management, reporting, APIs, physical and digital card production, loyalty and wallet support."
- "lifecycle management for customers, cards, accounts, and tokens"; debit/credit/prepaid/virtual/physical/digital/combination products; SaaS and BPO deployment options.

### Stripe Issuing — evidence layer A (direct fetch, docs index)

- "Use the Stripe Issuing API to create, manage, and distribute payment cards for your business."
- Manage-cards surfaces: replacement cards ("Replace cards that are expired, damaged, lost, or stolen"), PIN management ("Let your cardholders manage their personal identification numbers"), spending controls ("Set rules on cards and cardholders to control spend"), digital wallets, real-time authorizations, disputes.
- Cardholders and card bundles/designs are first-class concepts; physical cards involve design/bundle/ship steps.

### Treasury Prime — evidence layer A via search excerpt

- "Using our API, the entire card lifecycle—from issuing, to activation, to deactivation—can be managed programmatically."
- To issue a card you need: Account ID + Card Product ID + Person ID → issue → activate (PATCH card status to "active"). Card issued *against* an account, derived from a card product, owned by a person.

### Corroborating industry witnesses

- Cuscal (Australian payments company) FAQ: "A Card Management System (CMS) is a software solution that facilitates the issuance, management, and control of payment cards, such as credit, debit, or prepaid cards. It plays a crucial role in the administration of card-related processes within financial institutions and card-issuing organisations."
- MS Solutions SPARK CORE CMS: "acts as the card product configuration & lifecycle orchestration layer of the SPARK Issuing Suite"; "Manage the complete card lifecycle, from issuance and activation to renewal, blocking, and replacement, through a single centralized platform"; "manages card portfolios, product configuration, lifecycle events, and operational controls, while integrating with other SPARK modules for transaction processing, fraud management, clearing, and dispute handling."
- CLAI EVERYCARD: "control the entire card lifecycle — from issuance to cancellation"; "inventory, activations, blocking, renewals, replacements"; "physical and digital cards. Including printing, personalization, delivery, and smart activation."
- Stripe issuer-processor explainer: "Card issuance and life-cycle management: The processor lets issuers instantly create and manage physical and virtual cards. It generates card numbers, activates or reissues cards, manages personal identification numbers (PINs), blocks lost ones, and more."
- Adyen: "Traditional banks were the first to develop card issuing solutions. Initially built for the bank's own use, these solutions lacked the capabilities to easily integrate with other systems." Modern issuing = "flexible API-driven technology."
- NIST (different domain): "The system that manages the lifecycle of a PIV Card application" — shows the term's breadth beyond payments; scoped out here.

## Cross-product Comparison

| Dimension | Marqeta | Mastercard Processing CMS | Way4 (OpenWay) | PowerCARD-Issuer (HPS) | Total Issuing (FIS/TSYS) | Tietoevry | Stripe Issuing |
|---|---|---|---|---|---|---|---|
| Card as first-class record with own identity (PAN/token) + status | ✔ (card object, state + state reason) | ✔ (card plastic + card contract) | ✔ (full card lifecycle) | ✔ (card management module) | ✔ | ✔ ("cards" lifecycle) | ✔ |
| Card distinct from account | ✔ explicit ("device used to access funds") | ✔ (account contract ≠ card contract; cbsNumber/core-banking link) | ✔ (card AND account management) | ✔ (card module + separate credit/prepaid account modules) | ✔ (single customer view over accounts) | ✔ ("customers, cards, accounts, tokens") | ✔ (cards attach to Treasury balances) |
| Lifecycle states with transitions | ✔ (ACTIVE/SUSPENDED/LIMITED/TERMINATED; transitions endpoint) | ✔ (Locked → Active; blocking; closing) | ✔ (lifecycle workflows configurable) | ✔ ("all stages of their lifecycle") | ✔ | ✔ ("lifecycle events") | ✔ (activate/deactivate; replacements) |
| Issue / reissue / renew / replace operations | ✔ (original vs reissue; same/new PAN rules) | ✔ (REISSUE/RENEW/REPLACE, physical & virtual variants) | ✔ (instant issuing; card stock) | ✔ | ✔ (virtual card issuance) | ✔ (physical & digital card production) | ✔ (replacements for expired/damaged/lost/stolen) |
| Activation as explicit gated step | ✔ (validations; activate_upon_issue config) | ✔ (Locked → Active) | ✔ | ✔ | ✔ | ✔ (cardholder support: activation) | ✔ |
| PIN management | ✔ (iframe/IVR/API) | ✔ (PIN unchanged at renewal) | ✔ | ✔ (HSM interfaces) | ✔ | ✔ (PIN management) | ✔ |
| Spend limits / controls at card level | ✔ (velocity controls; transaction controls) | ✔ (classifiers) | ✔ (authorization controls; limits) | ✔ | ✔ (authorization controls) | ✔ (spending controls) | ✔ (spending controls) |
| Card product / program template layer | ✔ (cardproduct object) | ✔ (productCode; product definition at onboarding) | ✔ (95% parameter-driven product configuration) | ✔ (multi-product) | ✔ (multiproduct) | ✔ (card product setup) | ✔ (card bundles/designs) |
| Digital wallet tokenization | ✔ (token lifecycle; state sync) | ✔ (tokenization listed) | ✔ | ✔ (PowerCARD-Tokenisation separate product) | ✔ (wallets, tokenized payments) | ✔ (token management; wallet enrolment) | ✔ |
| Physical fulfillment (production, personalization, shipping, card stock) | ✔ (fulfillment config; bulk orders) | ✔ (personalization file) | ✔ (data prep & personalization; card stock management) | ✔ | ✔ | ✔ (physical card production) | ✔ (design/bundle/ship) |
| Operator workbench / dashboard | ✔ (Dashboard = ADMIN channel) | ✔ (GUI Workbench) | ✔ (Workbenches) | ✔ (back-office) | ✔ (servicing) | ✔ (workplace) | ✔ (Dashboard) |
| Programmatic API | ✔ (Core API) | ✔ (Processing APIs) | ✔ (API catalogue) | ✔ (120+ APIs) | ✔ (API-first) | ✔ (API layer) | ✔ (Issuing API) |
| IVR / phone channel integration | ✔ (IVR channel; getbypan) | — (not surfaced in excerpts) | — | — | — | ✔ (24/7 phone support service) | — |
| Transition reason taxonomy | ✔ (32+ reason codes) | partial (reissue types) | — (configurable rules) | — | — | — | — |
| Bundled transaction processing (authorization/clearing/settlement) | ✔ (JIT funding; network loads) | ✔ (processing core) | ✔ | ✔ (clearing & settlement module) | ✔ | ✔ (authorization, settlement) | ✔ (real-time authorizations) |
| Bundled credit account machinery (statements, interest, billing) | partial (credit API separate) | ✔ (account contracts) | ✔ (fees, pricing, billing) | ✔ (credit account module) | ✔ (credit programs) | ✔ (billing, invoicing) | — |
| Fraud / disputes / chargebacks | ✔ (FRAUD channel; chargebacks in DiVA) | — (separate guides) | ✔ | ✔ (fraud + chargeback modules) | ✔ (fraud & disputes module) | ✔ (optional features) | ✔ (disputes) |
| Loyalty | — | — | ✔ | ✔ | ✔ | ✔ | — |
| Multi-institution / processor posture | ✔ (Managed vs Powered by programs) | ✔ (issuer onboarding) | ✔ (multi-bank; white-label) | ✔ (multi-institution) | ✔ (processor heritage) | ✔ (SaaS/BPO) | ✔ (Connect platforms) |

Legend: ✔ = directly observed in that product's official material; — = not surfaced in the material consulted (absence not asserted); partial = observed in limited form.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

Three jointly-held structures over one binding:

1. **The card as a managed record distinct from the account.** A payment card — physical or virtual, two forms of the same credential — held as an individually identified record bound to a cardholder and to a funding account/contract, carrying its own payment identity (PAN or token), form factor, and status. The card is a device that accesses money held elsewhere; it is not itself the account or the balance. (Remove → account management / core banking territory.)

2. **The card lifecycle as managed state.** The card record moves through a managed lifecycle — issued/inactive → active → suspended/blocked/limited → expired/replaced/renewed → closed/terminated — with each transition recorded (channel + reason), driven by issuer operations, cardholder requests, and system events (expiry, fraud, PIN retry limits). (Remove → a static card registry / inventory list.)

3. **Card-level control operations.** The issuer's operational acts on the card object: issue, activate, block/unblock/suspend, reissue/renew/replace (with same-PAN vs new-PAN semantics), PIN set/reset, and per-card spend limits/controls. (Remove → passive tracking or disconnected ops tooling.)

Binding: the issuer's own payment-card portfolio (credit, debit, prepaid, commercial — physical and virtual). (Remove the binding → generic credential/token lifecycle management.)

Jointly-held load-bearing:
- 1 alone = card inventory/registry
- 2 without 1 = lifecycle machinery over nothing
- 3 without 1+2 = disconnected operations
- 1+2 without 3 = passive tracking nobody operates
- 1+3 without 2 = one-off ops with no lifecycle memory
- 2+3 without 1 = transitions over nothing

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Card product / program template layer (product object from which cards derive behavior; configuration-driven product factory)
- Digital wallet tokenization and token lifecycle (provisioning, state synchronization, reassignment on reissue)
- Physical card fulfillment machinery (production, personalization, shipping, card stock/inventory)
- Bundled real-time authorization and transaction processing (the processing-platform function, commonly co-shipped)
- Operator workbench (card search, card detail, lifecycle actions) and programmatic APIs as twin surfaces
- Reporting/analytics over card inventory and lifecycle events
- Cardholder-facing self-service surfaces (activate, block, PIN) delivered through the issuer's channels

### L2 — Variant / Optional Structure

- Credit-account machinery (statements, interest, billing, repayments) — credit-card variant
- Fraud monitoring, disputes/chargebacks — commonly bundled, module-level
- Loyalty and promotional campaigns
- Multi-institution / white-label / processor posture (BPO, CaaS)
- IVR/phone-channel integration for activation and PIN
- Instant issuance (in-branch/in-app immediate physical or virtual card)
- Single-use / ephemeral cards; bulk card orders
- Deployment: on-premise, cloud, SaaS, hybrid
- Regional scheme support (domestic schemes, Shariah-compliant programs, multi-currency travel cards)

### L3 — Vendor-specific (Research Notes only)

- Marqeta: "Managed by Marqeta" vs "Powered by Marqeta" program models; DiVA reporting API; UX Toolkit; JIT funding; GPA accounts; reason-code v2 program configuration; barcode on card; reissue-chain limit (source card reissued once).
- Mastercard Processing: client/accountContract/cardContract object naming; cbsNumber; classifier codes (CTLS_FLAG, ABU); sequenceNumber semantics; explicit "not a CRM" statement.
- OpenWay: "95% parameter-driven" positioning; Way4 Workbenches; fleet/CaaS/BNPL packaging.
- HPS: PowerCARD-Connect 120+ APIs; module names (Card Management Module, Credit/Prepaid Account Modules).
- FIS: Total Issuing TS2 / PRIME product names; "single customer view."
- Tietoevry: Banktech brand; SaaS + BPO delivery model.

## Historical / Market-Sample Check

- Mainframe-era issuer systems (the classic bank card systems and early TSYS-class processors): managed card records with status codes, activation, blocking, renewal, PIN — all core structures present without APIs, cloud, tokenization, or product factories. Fits L0. ✔
- Regional/domestic-scheme card systems (e.g., domestic debit schemes, private-label retail cards): same card record + lifecycle + operations under a non-international scheme. Fits. ✔
- Prepaid/gift/fleet/payroll card programs: card bound to a prepaid or corporate account rather than a credit line. Fits (Way4 and Tietoevry explicitly cover these). ✔
- Virtual-only card programs (no physical fulfillment at all): card record + lifecycle + operations fully present; physical fulfillment is L1/L2, not required. ✔
- Adyen's historical framing ("Traditional banks were the first to develop card issuing solutions. Initially built for the bank's own use…") confirms the Type predates the modern API packaging. ✔
- The definition does NOT depend on: phone/app channels, real-time processing, tokenization, card-product factories, or credit semantics. Historical check passed.

## Vendor-specific / Rejected Findings

- **Rejected for core**: "card issuing platform = program creation only" — the market's issuing platforms (Marqeta, Stripe, FIS) all carry full card-lifecycle management; program creation is packaging emphasis, not a structural difference.
- **Rejected for core**: real-time authorization as definitional — batch-era card management existed; authorization belongs to the processing function that commonly bundles with CMS.
- **Rejected for core**: credit-card semantics (statements/interest) — debit/prepaid/fleet/gift programs satisfy the Type without them.
- **Rejected for core**: tokenization/digital wallets — absent historically; modern common structure only.
- **Rejected**: "CMS is a CRM" — Mastercard's own docs explicitly deny it ("not intended to serve as CRM"); the CMS stores basic client/card data, with CRM-type richness living elsewhere.
- **Rejected**: NIST/PIV and campus-card readings of "card management system" — different domains (government ID, campus services); scoped out by the §08 placement.

## Boundary Findings

- **vs Card Issuing Platform**: The market uses "card issuing platform" for the modern packaging (API-first, program-launch oriented, BaaS/embedded-finance posture — Marqeta, Stripe, Adyen, Highnote) and "card management system" for the classic issuer-side lifecycle category (QKS SPARK Matrix category name; Mastercard's own docs; Cuscal FAQ). The underlying card-lifecycle machinery is the same; products visibly span both names (Way4's CMS URL sells "Card Issuing"; FIS sells the same stack as "Total Issuing"). Disposition: one product family, two packaging cuts — the issuing-platform cut is program-creation/launch-centric (who can start a program, how fast, through which APIs), the CMS cut is lifecycle-operations-centric (who runs the cards day to day). Keep both leaves; record family relationship in STATUS Boundary Issues.
- **vs Card Processing Platform**: Processing = the transaction machinery (authorization, clearing, settlement, switching). CMS = the card object's lifecycle record and operations. Stripe's own issuer-processor explainer lists card issuance and lifecycle management as a function *inside* issuer processing — the functions bundle constantly. Seam: if the product's center of gravity is moving transactions, it is the processing leaf; if it is maintaining card records and their states, it is this leaf. Keep both.
- **vs Core Banking System**: The account/ledger is the core bank's record; the card is a device accessing it. Mastercard's CMS models account contract and card contract as separate objects and explicitly links out to the Core Banking System (cbsNumber). Marqeta states funds live in user/business accounts, not on cards. Seam: money-of-record vs payment-credential-of-record.
- **vs Digital Banking Application / cardholder app**: Customer-facing surfaces (mobile banking, white-label cardholder apps) call into the CMS; the CMS is issuer-side operations. Tietoevry ships the cardholder app as a separate product.
- **vs Campus Card Management (§23)**: Campus cards bind to campus service entitlements (meal plans, access, print); payment-network card programs bind to funding accounts under scheme rules. Different binding, same word. Keep both; no directory change.
- **vs SIM/eSIM Management (§19)**: Both are "credential device lifecycle" shapes, but the SIM leaf's binding is telecom subscriptions. No overlap in market or buyers.
- **"去掉什么就变成另一个 Type" 判据**: Remove the card-as-distinct-from-account structure → core banking/account management. Remove the lifecycle → static registry. Remove issuer-side operations → cardholder app or analytics. Remove the payment-card binding → generic credential management or campus/ID card systems.

## Uncertainties

- Exact state-name sets vary by product (Marqeta: ACTIVE/SUSPENDED/LIMITED/TERMINATED + unactivated; Mastercard: Locked/Active + blocked/closed). The canonical state model is written conceptually; exact labels are vendor-specific.
- Whether "Card Issuing Platform" as a directory leaf will be documented as the same family (its own pass will decide; flagged for joint review).
- The precise split of authorization logic between CMS and processing platform varies by installation (Way4 and PowerCARD ship both; Marqeta runs authorization internally). Not resolvable at Type level; recorded as variant.
- IVR integration depth beyond Marqeta not confirmed in consulted material; kept as variant-level observation.
- Tietoevry's "Card management system" capability wording is from a product page (Tier 2); treated as corroborating, not load-bearing.

## Final Synthesis

A Card Management System is the card issuer's card-lifecycle system of record. Its defining core is three jointly-held structures: (1) the card as a managed record distinct from the account — an identified payment credential (physical or virtual) bound to a cardholder and a funding account, carrying its own PAN/token, form factor, and status; (2) the card lifecycle as managed state — issued → active → suspended/blocked/limited → expired/replaced/renewed → closed, with every transition recorded by channel and reason; (3) card-level control operations — issue, activate, block/unblock, reissue/renew/replace with same-PAN vs new-PAN semantics, PIN management, and per-card spend controls. The binding is the issuer's own payment-card portfolio. Everything else — card products as templates, tokenization, physical fulfillment, bundled authorization/clearing, credit machinery, fraud/disputes, loyalty, workbench vs API packaging — is common mature structure or variant, not definition. The Type is the operations-centric cut of the card-issuing product family whose program-creation cut is named "card issuing platform" and whose transaction-machinery cut is named "card processing platform."
