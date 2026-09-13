# Research Notes — Card Processing Platform

Research date: 2026-09-07
Leaf: Card Processing Platform (DIRECTORY §08 Finance, Banking, Insurance & Investment; siblings: Card Issuing Platform, Card Management System)
Slug: card-processing-platform

## Research Goal

Determine what a "Card Processing Platform" is as an Application Type: its defining core, its standard capabilities, its variant space, and its boundaries against the neighboring payment/card Types — especially the two directory siblings (Card Issuing Platform, Card Management System) and the processed Payment Processing Platform leaf, both of which left open boundary flags awaiting this pass.

## Initial Boundary

Initial hypothesis (from directory position + prior sibling research):

- The leaf sits under §08 next to Card Issuing Platform and Card Management System, so the expected reading is **issuer-side** card processing: the transaction-rail machinery operated on behalf of card issuers (banks/fintech issuers) on card-network rails — as opposed to Payment Processing Platform, which the processed leaf recorded as merchant-side acquiring.
- The card-issuing-platform pass (2026-09-07) recorded a working split: Issuing = program/card governance + funding binding + spend-control decisioning + transaction lifecycle; Card Processing = transaction-rail machinery (switching/interchange/clearing-settlement as infrastructure); Card Management = issuer-side card record administration (traditional bank shape, unsampled). It flagged joint review with this leaf.
- The payment-processing-platform pass recorded: "same word 'processing', expected opposite network sides … boundary expected to hold but untested (no issuer-side product sampled) — confirm when Card Processing Platform is processed."
- Known risk: modern issuer-side products fuse issuing + processing (same-products overlap pattern), so the Type may be an emphasis pole rather than a cleanly separable market category.

## Research Questions

1. What does the market mean by "issuer processing" / "card processing" on the issuer side? What is the platform's center of gravity?
2. What happens to a card transaction on the issuer side, step by step (authorization → clearing → settlement), and which parts does the processing platform own?
3. Who makes the authorization decision — the platform or the issuer's own system? Is this division of labor configurable, and is that configurability itself structural?
4. Who holds the cardholder balance ledger — the platform or the issuer's core? What are the consequences for authorization and posting?
5. What is stand-in processing (STIP) and how do products handle issuer-system downtime?
6. What clearing/settlement machinery does the platform run (presentment matching, interchange, scheme fees, settlement advisories, reconciliation)?
7. What surrounds the rail: card management, rules/limits, fraud/3DS, disputes/chargebacks, tokenization, reporting, portals, APIs?
8. Does a classic bank-heritage processor fit the same core as a modern cloud API processor (historical/market-sample check)?
9. Where exactly is the seam vs Card Issuing Platform, Card Management System, and Payment Processing Platform — and do the removal tests hold?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer eras/segments:

1. **Thredd** (formerly Global Processing Services) — global issuer processor, bank-grade, debit/credit/prepaid, strong fintech/embedded-finance base; **full public documentation portal** (Tier-1). The deepest available sample.
2. **Paymentology** — global cloud-native issuer processor ("issuing & processing platform"), banks + fintechs + telcos + super apps across many markets; **public developer portal** (Tier-1) with transaction-lifecycle guides.
3. **Fiserv (Card Services)** — classic US bank-heritage card processor for financial institutions (debit/credit end-to-end processing); product pages only (Tier-2) — represents the traditional bank pole.

Cross-checks reused from the processed sibling research (research/card-issuing-platform.md): Stripe Issuing, Adyen Issuing, Marqeta, Lithic — all sampled issuing platforms run issuer-side authorization processing themselves (fusion evidence).

Rejected/abandoned samples (network-restricted, see Sources): Pismo, i2c, TSYS, FIS, Galileo.

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

**Thredd (Tier-1 docs portal + Tier-2 site)**
- https://www.thredd.com/ (platform positioning)
- https://www.thredd.com/platform (platform overview)
- https://www.thredd.com/platform/core-processing (three processing modes)
- https://www.thredd.com/platform/system-of-record (real-time system of record + FAQ)
- https://docs.thredd.com/ (documentation portal index)
- https://docs.thredd.com/EHI_Guide_JSON.htm (External Host Interface guide, incl. release notes 5.0.x–5.5)

**Paymentology (Tier-1 dev portal + Tier-2 site)**
- https://www.paymentology.com/ (positioning)
- https://www.paymentology.com/en/processing-overview
- https://developer.paymentology.com/docs/start-get-started (Banking.Live portal index)
- https://developer.paymentology.com/v3.0/docs/txn-lifecycle-overview
- https://developer.paymentology.com/v3.0/docs/txn-authorization
- https://developer.paymentology.com/v3.0/docs/txn-clearing-settlement-reconciliation
- https://developer.paymentology.com/v3.0/docs/txn-stip

**Fiserv (Tier-2 product pages — classic pole)**
- https://www.fiserv.com/en/who-we-serve/bank.html
- https://www.fiserv.com/en/solutions/card-services.html

**Sibling research cross-checks**
- research/card-issuing-platform.md (Stripe/Adyen/Marqeta/Lithic observations; boundary flags)
- research/payment-processing-platform.md (merchant-side definition; open flag text)

**Unreachable (network-restriction rule applied; no memory-fill)**
- Pismo: docs.pismo.io transport error ×2 → abandoned.
- i2c: www.i2c.com returned an unrelated company's site (SAI360); docs.i2c.com transport error → abandoned.
- TSYS: www.tsys.com transport error → abandoned. FIS: fisglobal.com timeout → abandoned.
- Galileo: unreachable in the sibling card-issuing pass (galileo.io = unrelated medical company; galileo-ft.com 403) — not retried.
- Thredd "Key Concepts Guide" / "Introduction to Card Payments" online HTML rendered empty (PDFs exist but gated/not fetched); their topic lists were still observable from the portal index.

## Product Observations

### Thredd (evidence layer A unless noted)

**Positioning.** "The AI-first issuer processing platform"; "a global, bank-grade issuer processing platform for debit, credit, and prepaid"; "direct scheme connectivity"; "End-to-end card issuing and processing — issue and manage prepaid, debit, and credit cards, both virtual and physical, through a single integrated processing platform." Clients include fintechs, digital banks, B2B payments, embedded finance, OTAs, gaming, expense management, crypto cards; BIN sponsors listed separately.

**Core Processing — three processing modes (Tier-1 product page + EHI guide).**
- **Gateway Processing (EHI mode 1):** "You hold the balance, manage authorisations, and handle stand-in processing. Thredd provides Mastercard and Visa connectivity and the full card management toolset." Mode 1 = "where you manage authorisations": full decisioning control, real-time authorisation responses, rapid financial advices for every transaction.
- **Cooperative Processing (mode 2):** "Thredd authorises transactions against balances managed jointly, with authorisation override and stand-in services included." Mode 2 = "where Thredd manages authorisations": balance updates, message verification, matching and adjustments. EHI notes: in Mode 2 the client can override Thredd's decline code 51 (insufficient funds) with a more specific decline reason; Master Virtual Cards support "approve with load" in Mode 2.
- **Full-Service Processing (mode 3):** "Thredd manages everything: scheme connectivity, balance ledger, and transaction authorisation."
- **Gateway Processing with STIP (mode 4)** exists as a named EHI mode (mode 5 decommissioned). EHI terminology introduced in release 5.0.14.

**External Host Interface (EHI) — the authorization integration (Tier-1).**
- EHI is for "payment transaction authorisation and/or subscription to the EHI real-time payment transaction data feed" (XML and JSON variants).
- GetTransaction message: Thredd sends the scheme authorization to the external host; the host responds approve/decline. Response codes (DE39) documented; authorization codes generated for approved **and** declined authorizations; partial approvals and declines with reason codes supported; incremental authorizations and authorization reversals with matching IDs; financial notifications require mandatory acknowledgement.
- Transaction matching: Matching_Txn_ID populated for presentments, authorization reversals, incremental authorizations and their reversals.
- Transaction status codes: "Cleared (C)" and "Settled (S)" impact the card balance.
- **Clearing files (direct quote from release notes):** "Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly."
- STIP: response code 96 may trigger scheme Stand-In Processing depending on STIP setup; Visa STIP reason codes; STIP Balance Update endpoint in the API Hub; Gateway-with-STIP mode updates balances via SOAP web services.
- Interchange: Interchange_Amount_Fee / Interchange_Amount_Fee_Settlement fields carry the interchange fee received in EHI messages; FAQ covers acquirer- and issuer-side network fees.
- Card controls in the message flow: card status codes (incl. temporary blocks G5/G6 settable by the Fraud Transaction Monitoring service), card usage groups, CVV2 pre-checks (blank CVV2 → authorize/decline per card-usage-group settings), AVS results, PIN change/unblock processing codes, Account Status Inquiry, single vs dual message systems, cut-off messages, AFD (automated fuel dispenser) flows, OCT/AFT, tokenization fields (TAF, PaymentToken), dynamic CVV2, FIDO device-binding codes, 8-digit BINs/SubBIN, multi-currency (incl. CNH).

**Real-Time System of Record (Tier-1 product page + FAQ).**
- "One auditable source of truth for every account, balance and transaction"; real-time balances across every account and instrument; full traceability and auditability; one source of truth shared across markets and products.
- Account hierarchy: parent accounts, sub-clients, product-level rules — supports aggregators, BIN sponsor relationships, multi-regional programmes; changes at one level don't affect other programmes.
- Balance management: multiple funding sources, instruments, currencies; multi-currency balances within one account structure (automated FX conversion on roadmap).
- Transaction controls: spending limits, merchant category restrictions, authorisation rules at the product-account level.
- Multi-instrument support: multiple instruments (physical, virtual, tokenised wallets) attached to one account.
- Composable integration via dedicated API endpoints; FAQ: "replaces batch-based reconciliation with a live, auditable view"; "A traditional ledger records credits and debits. The Thredd real-time system of record goes further — it includes the account hierarchy, product-level rules, and control configurations"; underpins both debit and credit (credit origination/servicing via a credit partnership).

**Surrounding machinery (docs portal index, Tier-1).** Cards REST API / API Hub; SOAP web services; Fees Guide (set up and manage card fees per card product); Physical Card Configuration; Virtual Cards; Master Virtual Cards; Card Generation Interface Specification (XML data prep for card production); Card Transaction System (test transactions); PSD2/SCA guide; L2/L3 Enhanced Scheme Data + Fleet EDS reporting; Global Transaction/Balance Reporting; 3D Secure services (Cardinal, Apata); Fraud Transaction Monitoring; Payments Dispute Management (chargebacks); Fraud Reporting to Mastercard; **Thredd Portal** ("online administration application for viewing and managing cards and transactions"); legacy Smart Client; **Automated Back Office** ("automated transaction reconciliation, Scheme reporting and network fee management"); Discover Global Processing; Tokenisation Service; SMS and IVR cardholder self-service guides; webhooks; PANFinder; card chip parameters; pre-release notifications (PRNs); country support; glossary.

**Platform overview (Tier-2).** Unified issuing (debit/credit/prepaid/virtual in one platform); modern architecture (single API, cloud, multi-region resilience); configurable by design (parent programme down to individual account); real-time ledger + control; AI-powered decisioning (fraud monitoring, credit decisioning, onboarding); back office ("automate reconciliation, disputes and reporting"); card controls ("set, manage and update card rules without reissuing cards"); digital wallets (Apple Pay/Google Pay); risk management; data + reporting; BIN-sponsorship matching service; stablecoin-backed programmes; agentic-commerce readiness (Visa Agentic Ready Programme).

**Marketing figures (L3, excluded from final doc):** 325m+ cards, 2.5bn+ transactions/year, 50+ countries (homepage) vs 1bn+ transactions annually, 130+ clients, 47 countries, 99.99% uptime (system-of-record page) — internally inconsistent marketing numbers.

### Paymentology (evidence layer A unless noted)

**Positioning.** "The Ultimate Global Card Issuer Processor"; "Paymentology's issuing & processing platform helps banks & fintechs to launch innovative, secure, and flexible card payment products." Processing overview: "From authorisation to settlement. One platform." — "one single API connecting your card programmes to global payment networks." Use cases span fintechs, digital banks, banks, telcos, lenders, travel, expense management, remittance, government, acquirers/PSPs (as an issuing-revenue audience, not acquiring), super apps, crypto/stablecoin players.

**Authorization (Tier-1 dev portal).** "Authorization is the first step in processing a scheme transaction, to verify the cardholder and financial status."
- **External authorization:** "implemented where the client holds the balance of the account and real-time transmission of the FAST Interface messages is required. Banking.Live responds to authorization messages based on non-financial checks, client-defined transaction rules, and the client partakes in the authorization process." → "Remote Store of Value products use external authorization."
- **Internal authorization:** "implemented where Paymentology holds the balance of the account and no real-time transmission of the FAST Interface messages is required. Banking.Live handles the responses to authorization messages based on financial and non-financial checks as well as client-defined transaction rules." → "Local Store of Value products use internal authorization."
- **Passive authorization:** the client does not partake in the decision but receives FAST messages in real time (preferably when Paymentology holds the balance).
- **Authorization flow (six steps):** (1) receive authorization message from the card scheme (Mastercard, Visa, Mada); (2) initial checks — CVV, expiry, crypto, tokenisation, tracks, PIN; (3) rules-engine analytics — alerts, fraud, fees; (4) route the authorization as a FAST message (ISO 8583 with enhanced fields) to the bank; (5) receive the retail bank / programme manager decision; (6) perform final checks and store the financial decision.

**Clearing, settlement, reconciliation (Tier-1 dev portal).**
- Clearing = "the process of exchanging clearing data" — file exchange between parties per cutoff times; presentments flow acquirer→issuer; the scheme clearing system "accepts the data, edits it, computes, applies the appropriate fees, and then routes it"; "clearing messages contain data but do not actually exchange or transfer funds."
- FAST presentment flow: (1) receive presentment file from the scheme; (2) match presentment data to the preceding authorization, assigning a unique reference; (3) route FAST presentment data to the client; (4) no client response required.
- Clearing file format: scheme IPM files based on ISO 8583-1993; MTI types 1240 Presentment, 1442 Chargeback, 1644 Administrative, 1740 Fee Collection.
- Presentment→authorization matching fields: DE38 (authorization code), DE2 (card number), DE42 (merchant ID), DE4 (amount); secondary DE63/DE42/DE37/DE7/DE12. Vendor claims matching succeeds in ">99%" of cases; outlier cases exist (forced presentment without authorization, manual key-ins, amount/detail differences at presentment).
- Settlement = "the process that facilitates the movement of funds between issuers and acquirers"; the scheme calculates each customer's net position and performs settlement functions: "sending advisements; transferring funds (when applicable)"; "Settlement can be performed only after clearing has occurred."
- The platform forwards raw network settlement reports to clients (Visa VSS-110/110-M/111, EP reports; Mastercard T112/T140/TQR4; mada TLF + settlement file) and daily reports (authorizations, presentments, interchange, fees).
- **Responsibility table (launch responsibilities):** platform responsible for receiving/processing raw network clearing files, delivering clearing data via webhooks, delivering raw settlement files, delivering daily reports; client responsible for receiving clearing webhooks and processing credits/debits, reconciliation of the data, and transferring funds for settlement.
- Reconciliation guidance: match approved transactions against the authorizations report, cross-check against the presentments report, verify against the scheme settlement report; discrepancies reviewed by the client's reconciliation team.

**Stand-in Processing (Tier-1 dev portal).**
- "STIP refers to the procedure where transactions are managed by an alternate entity when the primary decision-making party is temporarily incapacitated due to maintenance, technical disruptions, or other factors."
- **Basic STIP:** the STIP provider declines transactions if no response arrives within a predefined timeframe. **Enhanced STIP:** the provider can also approve transactions meeting client-defined criteria (spend limits, risk thresholds, card products); balance listing optional (online FAST responses, balance-update API, or batch files).
- Store-and-Forward (SAF): during a STIP event the platform answers the network and queues an advice message, delivered automatically to the client's system when it is back online.

**Surrounding machinery (dev portal index, Tier-1).** Card lifecycle guides (cards/accounts created, issued, managed; tokenization; PIN management); transaction lifecycle guides (authorization, PIN verification, declined transactions, transaction rules, fees, limits, STIP, clearing/settlement/reconciliation, clearing and settlement data, online vs offline settlements, chargeback funds, API vs manual chargebacks, refunds and reversals, incremental authorization, transfers, scheme-specific transactions, card-present/not-present, AFD); data exchanges (FAST Transaction Interface, remote messages, scheduled reports); security & fraud prevention (PaySecure API); user interface (PayControl); tools (Card Test Simulator); API Explorer; support platform. Issuing menu: debit/prepaid/credit/hybrid/virtual/numberless cards, crypto & stablecoins, tokenization, BIN sponsoring.

**Vendor figures (L3):** "120 data lines per transaction" (Data Intelligence page); ">99%" matching; import "within 3 minutes … typically completed within 10 minutes"; scheme timing details relayed (Visa International Settlement ~03:00 PT; Mastercard six clearing cycles; mada cutovers 06:30/04:00).

### Fiserv Card Services (evidence layer A at product-page level; classic pole)

- Audience: banks and credit unions ("More than 1 in 3 U.S. financial institutions use account processing solutions from Fiserv"; ~10,000 FI clients — marketing figures, L3).
- **"Benefit from end-to-end processing — Increase operating efficiency with fast, secure processing services for debit and credit – from authorization to clearing and settlement."** (direct quote — the classic processor spine in one sentence)
- "Access ATM and payment networks — Participate in leading U.S. payment networks and provide comprehensive ATM and cash management services."
- Solution set: Credit Solutions ("complete credit card program"), Debit Solutions, Card Risk Management ("reducing debit and credit card fraud … risk mitigation and management services"), CardHub (next-generation digital cardholder experience on a "single, unified platform"), Payment Networks, ATM Solutions, Portfolio Optimization (rewards programs + consulting), Dispute Expert (Ethoca Alerts — dispute experience), Digital Issuance (eliminate the wait for a physical card).
- Interpretation: the classic bank-side card processor bundles the same rail spine (authorization → clearing → settlement, network access) with card-program services (risk, disputes, cardholder digital experience, portfolio consulting) — the issuing/program side is sold as part of the same relationship. Operational docs not public (Tier-2 only).

### Cross-checks from sibling research (layer B)

- Stripe Issuing, Adyen Issuing, Marqeta, Lithic (sampled in research/card-issuing-platform.md) all run issuer-side authorization processing themselves and manage card records (status/PIN/limits) — modern issuing products fuse the processing rail. Lithic even names a section "Card Issuance & Processing".
- Galileo (issuer-processor heritage) unreachable — the pure fintech-heritage API-processor pole has no direct product evidence in either pass.

## Cross-product Comparison

| Dimension | Thredd | Paymentology | Fiserv Card Services |
|---|---|---|---|
| Self-label | "issuer processing platform"; "end-to-end card issuing and processing" | "Card Issuer Processor"; "issuing & processing platform" | "Card Services … processing services for debit and credit" |
| Client base | fintechs, digital banks, B2B/embedded finance, BIN sponsors | banks, fintechs, telcos, super apps, remittance, government | US banks and credit unions |
| Scheme connectivity | direct (Mastercard, Visa; Discover app documented) | direct (Mastercard, Visa, Mada) | "leading U.S. payment networks" + ATM networks |
| Authorization decisioning | configurable: Gateway (client decides) / Cooperative (platform decides, client overrides) / Full-Service (platform decides) / Gateway-with-STIP | configurable: External (client decides) / Internal (platform decides) / Passive (platform decides, client informed) | not exposed at product-page level (end-to-end service) |
| Balance ledger holder | configurable: client-held (gateway) / joint / platform-held (full-service); real-time system of record | configurable: client-held (Remote Store of Value) / platform-held (Local Store of Value) | not exposed (bank-heritage: issuer core typically holds) |
| Clearing/settlement | batch clearing files from networks; presentment matching; cleared/settled statuses affect balance; interchange + network fee fields; automated back office (reconciliation, scheme reporting, network fee management) | presentment files received and matched to authorizations; raw settlement reports forwarded; daily presentment/interchange/fee reports; client reconciles and transfers settlement funds | "from authorization to clearing and settlement" (product-page level) |
| STIP | named modes incl. Gateway-with-STIP; STIP balance update endpoint; scheme STIP triggers | Basic vs Enhanced STIP; store-and-forward advices; balance listing via API/batch | not exposed |
| Rules/controls | spending limits, MCC restrictions, authorization rules per product account; card usage groups; card status codes | client-defined transaction rules; Decision Engine evaluates every transaction in real time; fees; limits | Card Risk Management services |
| Fraud/3DS | Fraud Transaction Monitoring; 3DS (Cardinal/Apata); fraud reporting to scheme | Fraud Control Services; 3DS; PaySecure | Card Risk Management; Dispute Expert/Ethoca |
| Disputes | Payments Dispute Management guide (chargebacks) | chargeback guides (funds processing, API vs manual) | Dispute Expert |
| Card management | full card management toolset; card generation interface; physical/virtual configuration; PIN | card lifecycle guides; PIN management; tokenization | card lifecycle digitally; Digital Issuance |
| Tokenization/wallets | Tokenisation Service Guide; digital wallets | tokenization; push provisioning; wallet support | (not on fetched page) |
| Operator surfaces | Thredd Portal (view/manage cards and transactions); legacy Smart Client | PayControl UI; Client Portal (real-time tracking, rules on the fly, reconciliation automation) | CardHub (cardholder-facing); Card Expert (portfolio analytics) |
| Integration | Cards REST API / API Hub; SOAP; EHI (XML/JSON); webhooks; CTS test system | Banking.Live APIs; FAST interface; webhooks; scheduled reports; Card Test Simulator | not public |
| Delivery posture | cloud-native, multi-region, composable | cloud-native, agnostic, global redundancy | bank-heritage suite (not exposed) |

**Stable across all three (layer B):** issuer-side scheme connectivity; real-time authorization participation with configurable division of labor; cardholder account/balance record (held or mirrored); authorization→clearing→settlement lifecycle with presentment matching, interchange/fees, settlement advisories and reconciliation; STIP fallback; rules/limits/controls; fraud screening + 3DS in the flow; disputes/chargebacks; card management toolset; operator portal + APIs + reporting; test tooling.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

A **Card Processing Platform** is the **issuer-side transaction-rail infrastructure of card payments**: operated for card issuers, directly connected to card networks, it runs the issuer's side of every card transaction. Four properties; remove any one and the product is no longer this Type:

1. **Issuer-side scheme connectivity** — the platform is the issuer's processing point on card-network rails: it receives the scheme-routed transaction stream (authorizations, presentments, fee collections, chargebacks) for its clients' issued cards.
2. **Real-time authorization processing** — for each attempted transaction it takes part in the approve/decline decision: performing card-data and rule checks itself, and either deciding directly (against balances and rules it holds) or relaying the request in real time to the issuer's system and returning its response.
3. **Cardholder account/balance record** — transactions post against cardholder accounts carrying balances; the platform either holds that ledger itself or works in real time against the issuer-held ledger (the store-of-value axis; the record itself is invariant, its holder is not).
4. **Transaction lifecycle through clearing and settlement** — it processes the scheme's clearing files (presentments matched to authorizations, fees, interchange), supports the settlement cycle (advisories, reconciliation data), and records the resulting account movements (authorization hold → cleared → settled, with reversals, refunds, chargebacks).

**Removal tests (去掉什么就变成另一个 Type):**
- Remove scheme connectivity + authorization participation → issuer-side card record administration (Card Management System territory).
- Remove the cardholder account/balance record → a pure network message switch, not a processing platform.
- Remove clearing/settlement processing → an authorization-only gateway (partial rail).
- Move to the merchant side (underwrite sellers, route payments inward, fund merchants) → Payment Processing Platform (acquiring).
- Remove the rail machinery and keep only program/card governance → Card Issuing Platform emphasis.
- Remove card semantics entirely and just hold/move balances → core-banking/ledger territory.

### L1 — Common Mature Structure (standard capabilities)

- **Configurable division of labor** (the processing-mode dial): gateway ↔ cooperative ↔ full-service; external ↔ internal ↔ passive authorization. Cross-product structural finding (Thredd 3+1 named modes; Paymentology 3 authorization types) — the strongest candidate for a Type-level pattern beyond L0.
- **Stand-in processing (STIP)**: basic (decline on timeout) and enhanced (approve per client criteria, optionally with balance listing); store-and-forward advices delivered on recovery.
- **Transaction rules engine**: spend limits, merchant-category restrictions, authorization rules scoped at programme/product/account/cardholder level.
- **Fraud screening and 3DS inside the flow**; fraud monitoring services; fraud reporting to schemes.
- **Dispute/chargeback machinery** on the issuer side (creation, funds processing, API vs manual handling).
- **Fees machinery**: program fee configuration, interchange data fields, network/scheme fee collection and reporting.
- **Card management toolset**: card status lifecycle, PIN management, card-generation data prep, physical/virtual card configuration.
- **Tokenization and digital-wallet enablement** (push provisioning, token lifecycle).
- **Operator portal** (view/manage cards and transactions), **automated back office** (reconciliation, scheme reporting, network fee management), **reporting/data exchanges** (transaction/balance reports, raw scheme settlement reports, daily presentment/interchange/fee reports).
- **APIs + webhooks + sandbox/test transaction simulators.**
- **Multi-currency** balances and processing; **account hierarchies** for aggregators/BIN sponsors/multi-programme operators.
- Cardholder self-service channels (IVR, SMS) in some products.

### L2 — Variant / Optional Structure

- **Store-of-value axis** (who holds the ledger): platform-held (local) vs issuer-held (remote) vs joint — the same axis Thredd exposes as modes and Paymentology as Remote/Local Store of Value.
- **Product scope**: debit/prepaid vs credit (credit adds origination/servicing; at one sampled product delivered via partnership).
- **Client base**: banks vs fintechs/embedded finance vs aggregators/BIN sponsors.
- **Scheme coverage**: Visa/Mastercard baseline; Discover, mada and other regional schemes vary by product.
- **BIN sponsorship** as a service (matching programmes to sponsors).
- **Delivery posture**: cloud-native API-first vs bank-heritage suite.
- **Emerging**: stablecoin-backed settlement, agentic-commerce readiness, AI decisioning framing.
- **Cardholder-experience layers** (digital card surfaces) and **portfolio/consulting services** — classic-pole bundling.

### L3 — Vendor-specific (research notes only; excluded from final document)

- Thredd: EHI mode numbering (1/2/3/4; mode 5 decommissioned); decline-code-51 override in Cooperative mode; MVC approve-with-load; card status codes G5/G6 set by FTM; 3DS Cardinal/Apata service names; Smart Client (legacy); PANFinder; PRN release process; API Hub/cardsapidocs; Thredd Cloud; Discover Global Processing application; B Corp certification; "AI-first" branding; inconsistent scale figures (325m cards / 2.5bn txn vs 1bn+ txn / 130+ clients / 47 countries / 99.99% uptime).
- Paymentology: Banking.Live platform name; FAST interface name (ISO 8583 "with enhanced fields"); PayControl UI; PaySecure API; Card Test Simulator; TID/RID identifiers; "120 data lines per transaction"; ">99%" matching claim; 3-minute/10-minute import claims; Remote/Local Store of Value naming; Lume platform name; Decision Engine / Data Intelligence / Fraud Control Services module names; mada support; scheme timing details relayed in docs (Visa International Settlement ~03:00 PT; Mastercard six clearing cycles + Mexico seventh; mada cutovers 06:30/04:00); Jonet sample set.
- Fiserv: CardHub, Dispute Expert/Ethoca Alerts, Credit Choice, Card Expert, Digital Issuance, Portfolio Optimization, agentOS, FIUSD; scale claims (1-in-3 FIs, ~10,000 clients).

## Rejected Findings

- **"Card processing platform = merchant-side payment processing."** Rejected: same word, opposite network side. The issuer-side flows documented at two products run toward the issuer (presentments delivered TO the issuer's processor; the issuer transfers settlement amounts; interchange received by the issuer side). Merchant-side acquiring is the processed Payment Processing Platform leaf.
- **"The platform always holds the cardholder balance."** Rejected: gateway/external modes explicitly put the balance with the client (issuer); the invariant is the record + real-time interface, not the holder.
- **"The platform always makes the authorization decision."** Rejected: gateway/external modes give the issuer full decisioning control; the platform performs checks and relays. The invariant is participation in the real-time decision, not ownership of it.
- **"Issuer processing requires virtual cards / APIs / cloud."** Rejected: the classic bank pole (Fiserv) sells the same spine without exposing any of these; L0 is deliberately implementation-neutral.
- **"STIP is a niche feature."** Rejected as a classification: it appears as a named mode at one product and a first-class guide at another; treated as common-mature structure (L1), not L0 — a platform without STIP would still be a card processing platform.
- **"Scale/uptime figures as structure."** Marketing figures (L3); excluded.
- **"Credit processing = consumer lending platform."** Rejected: credit card processing shares the same rail; origination/servicing depth varies (partnership-sourced at one product) and belongs to variant space.

## Boundary Findings

1. **vs Card Issuing Platform (sibling, processed) — the central boundary; joint-review flag discharged with evidence.** The working split recorded by the issuing pass is confirmed and sharpened: **issuing centers the program side** (create/govern cards, cardholders, funding binding, spend controls, card lifecycle); **processing centers the rail side** (scheme connectivity, authorization switching, balance ledger, clearing/settlement, interchange, STIP, reconciliation). The market fuses both: Thredd sells "end-to-end card issuing and processing", Paymentology an "issuing & processing platform", and the issuing pass found Stripe/Adyen/Marqeta/Lithic all process authorizations themselves. The two directory leaves therefore overlap on the same products and differ in emphasis — same overlap pattern as Payment Gateway vs Payment Processing Platform. Removal tests: strip the rail machinery (scheme connectivity/authorization/clearing) → program-governance tooling (issuing emphasis); strip program/card governance → pure rail processing (this leaf). **Joint review still recommended** (three card leaves, two real structures at most).
2. **vs Card Management System (sibling, unprocessed).** Classic processors include card management (statuses, PIN, plastic, card generation) as part of end-to-end processing — "the full card management toolset" is what the gateway mode provides alongside connectivity. A standalone Card Management System reading = record administration without rail participation (the removal-test residue). Near-alias territory with issuing from the traditional-bank era; **flag retained for joint review**; this pass adds the observation that card management appears as a *component* of processing at both deeply sampled products.
3. **vs Payment Processing Platform (processed) — open flag RESOLVED: boundary holds.** Confirmed opposite network sides. Payment processing = merchant-side acquiring (underwrites sellers, administers processing accounts, routes payments into networks, settles/funds merchants). Card processing = issuer-side (the issuer's processing point; cardholder accounts; issuer authorizations; settlement with the scheme as the issuer's counterparty; interchange on the issuer side). Evidence: issuer-side products describe presentments arriving *to* the issuer side and the *issuer* transferring settlement amounts; the acquiring leaf describes the opposite direction. The payment-processing-platform leaf's recorded uncertainty ("no issuer-side product sampled") is discharged.
4. **vs Payment Gateway (§08).** Gateway = merchant-side acceptance front end (capture surfaces, secure transmission). Card processing platform = issuer-side rail. Different sides of the network; no market confusion observed.
5. **vs Core Banking System (§08).** The bank's deposit/credit ledger. Processing platforms either hold a program-scoped balance ledger (local store of value / full-service) or interface in real time with the issuer's core (remote store of value / gateway); they do not replace the bank's books. In gateway mode the bank's core remains the balance holder and decision maker.
6. **vs Fraud Detection Platform (§15, processed).** Embedded, program-scoped fraud screening inside the authorization flow (rules, alerts, scheme fraud reporting) vs the standalone cross-industry fraud operations system (signal enrichment, case management, model loops). Overlap real; centers differ. Consistent with the issuing pass's finding.
7. **vs Digital Wallet (§08).** Tokenization/wallet enablement is an output of the processing platform serving cardholder-side wallets; the wallet holds credentials and initiates payments, the processor runs the rail behind the credential.
8. **vs AML / Transaction Monitoring Platform (§08/§15).** Scheme/program-scoped fraud monitoring inside processing vs institution-wide AML compliance (sanctions, SAR workflows). Distinct registers.
9. **vs Corporate Card & Spend Platform (§08, unprocessed).** Spend-side software operated by the card-using company; the processing platform is program-side infrastructure operated by the issuer/program owner. Consistent with the issuing pass's seam.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- **Classic mainframe-era issuer processors** (TSYS/FIS/Fiserv heritage; bank card centers): cardholder master files, batch-oriented posting, host-to-host authorization interfaces — but the same spine: network connectivity, real-time authorization, posting to cardholder accounts, clearing/settlement file exchange. Fiserv's current product page confirms the spine survives today in classic form ("from authorization to clearing and settlement", network access, dispute management). **Fits.** (Direct operational docs unreachable — structural inference + Tier-2 product-page evidence; recorded in Uncertainties.)
- **Regional processors** (mada via Paymentology; Discover via Thredd): same spine over different schemes and regions. **Fits.**
- **Modern API-first processors** (Thredd/Paymentology today; Galileo/Pismo/i2c class): same spine with APIs, webhooks, real-time ledgers. **Fits.**
- **Scheme-internal processing** (the networks' own switching): not a client-facing platform; outside the Type.

The L0 does not require cloud, APIs, virtual cards, fintech clients, or any particular scheme — no over-fitting to the current generation. The strongest over-fitting risk (requiring platform-held balances or platform-made decisions) was deliberately excluded: the division of labor is the variant dial, not the invariant.

## Uncertainties

1. **Classic-pole operational depth**: TSYS and FIS unreachable; Fiserv evidence is product-page level (Tier-2). The classic processor's internal workflow (batch cycles, host interfaces, statementing) is structurally inferred, not directly observed. Assertion strength for the classic pole is reduced accordingly.
2. **Modern fintech-heritage API pole**: Pismo, i2c, Galileo all unreachable in this pass (and Galileo in the sibling pass). The pole is represented structurally (Thredd/Paymentology are themselves modern cloud processors) and by sibling-research cross-checks (Stripe/Adyen/Marqeta/Lithic fusion), but no Galileo-class product was directly documented.
3. **Credit processing depth**: at Thredd, credit programmes use the system of record "alongside origination and servicing capabilities provided through our credit partnership"; Fiserv sells complete credit programs. Credit-specific machinery (statements, interest cycles, payments) varies and was not directly observed at operational depth.
4. **Interchange/scheme-fee calculation vs reporting**: evidence shows interchange data fields, fee-collection message types, and network-fee management; whether the platform *calculates* (vs reports/reconciles) scheme fees varies and was not directly evidenced. Kept generic in the final document.
5. **Settlement funding responsibility in full-service modes**: Paymentology's responsibility table shows the client transferring settlement funds (gateway-heritage posture); whether full-service/platform-held modes change this was not directly evidenced. Kept generic.
6. **Three-leaf taxonomy**: Card Issuing Platform / Card Management System / Card Processing Platform may be two real structures (program side vs rail side) with Card Management as a traditional-era alias/component. Joint review recommended; not resolved unilaterally.

## Final Synthesis

A **Card Processing Platform** is the **issuer-side transaction-rail infrastructure of card payments**: operated for card issuers (banks, fintech issuers, BIN-sponsored programmes), directly connected to card networks, it receives the scheme-routed transaction stream for its clients' cards, takes part in the real-time authorization decision for every attempted transaction (deciding itself against balances and rules it holds, or relaying to the issuer's system and returning its response), posts the transaction against a cardholder account whose balance it either holds or mirrors in real time, and carries the transaction through its full financial lifecycle — clearing files matched to authorizations, interchange and scheme fees, settlement advisories, reconciliation, reversals, refunds, and chargebacks — with stand-in processing keeping the rail alive when the issuer's systems are down.

The defining core is small (issuer-side scheme connectivity + real-time authorization participation + cardholder account/balance record + clearing/settlement lifecycle). The most distinctive structural finding beyond the core is the **configurable division of labor**: the same platform can run as a pure connectivity gateway (issuer holds balances and decides), a cooperative hybrid, or a full-service processor (platform holds the ledger and decides) — exposed as named modes at both deeply sampled products. Everything else — STIP, rules engines, fraud/3DS, disputes, card management, tokenization, portals, reporting, multi-currency, account hierarchies — is standard mature structure; product scope (debit/prepaid/credit), client base, scheme coverage, and delivery posture are variant space.

The Type sits on the issuing side of the card rails, opposite the merchant-side payment processing Types. Its deepest unresolved boundary is with the directory siblings Card Issuing Platform (program side vs rail side, fused in the same modern products) and Card Management System (record administration as the removal-test residue) — joint review recommended, flags discharged/updated in STATUS.md.
