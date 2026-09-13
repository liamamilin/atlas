# Research Notes — Stored Value Wallet

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)
Directory leaf: `Stored Value Wallet` (§08 Finance, Banking, Insurance & Investment; sibling of Digital Wallet, Mobile Wallet)
Slug: `stored-value-wallet`

---

## Research Goal

Establish what a Stored Value Wallet is as an Application Type: what exists inside it, what users do with it, how money moves, which rules shape behavior, and where its boundaries sit against the sibling wallet leaves (Digital Wallet, Mobile Wallet), the already-processed neighbors (Peer-to-peer Payment Application, Store Credit / Stored Value Platform, Campus Card Management, Cashless Venue Platform, Payment Gateway / Processing Platform, Crypto Wallet), and unprocessed neighbors (Gift Card Management, Card Issuing Platform, Digital Banking Application).

---

## Initial Boundary

Working hypothesis at start:

- Core: a consumer payment application whose payment instrument is the user's own prepaid monetary balance, loaded in advance and drawn down by spending.
- Nearest neighbors: Digital Wallet / Mobile Wallet (credential containers, unprocessed siblings), Peer-to-peer Payment Application (transfer-core, processed), Digital Banking Application (bank-account relationship), Store Credit / Stored Value Platform (merchant-side program, processed), Campus Card Management / Cashless Venue Platform (institution/venue-scoped closed loops, processed), Gift Card Management (instrument programs, unprocessed), Card Issuing Platform (B-side, unprocessed), Crypto Wallet (naming conflation, processed).
- Known unknowns: how the market distinguishes "stored value wallet" from "digital wallet" in practice; whether balance withdrawal is definitional or optional; how loading paths vary across regions; the regulatory posture of the balance.

Prior art inside this production pack that constrains this pass:

- `research/peer-to-peer-payment-application.md` §Boundary Findings flagged a joint review: "P2P is almost always embedded inside a wallet product… stored value is one funding implementation rather than the boundary… flagged for joint review when those leaves are processed."
- `research/crypto-wallet.md` boundary issues warn that "wallet" names three different things in this directory: Crypto Wallet (keys), Digital/Mobile/Stored Value Wallet (fiat credential/value containers), and colloquial exchange-balance "wallets".
- `applications/cashless-venue-platform.md` and `applications/campus-card-management.md` both define their boundaries against "Digital Wallet / Stored Value Wallet" as the general-purpose, user-owned remainder.
- `applications/store-credit-stored-value-platform.md` defines the seam: consumer-side general-purpose wallet vs merchant-side closed-loop program system of record.
- `applications/payment-gateway.md` / `payment-processing-platform.md` treat wallets as payer-side payment method types (gateways are payee-side).

---

## Research Questions

1. What is the central object — how do products name and expose the user's stored monetary value?
2. How does value enter the balance (loading / top-up / cash-in paths)?
3. How does spending work — what does a payment draw against, and at which acceptance points?
4. Does value leave the wallet again (withdrawal / cash-out), and is that core or optional?
5. What account lifecycle shapes usage (registration, verification, limits, closure)?
6. Which channels carry the wallet (app, USSD/SIM toolkit, web, card, agent counter)?
7. How do closed-loop and open-loop acceptance differ across products?
8. Remove-tests against every neighbor listed above.

---

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different geographies/tiers:

| Product | Geography | Philosophy / position | Why sampled |
|---|---|---|---|
| M-PESA (Safaricom) | Kenya / East Africa | telco-anchored mobile money; agent cash network; USSD-first, no smartphone required | strongest A-layer operational documentation reached; different channel philosophy |
| PayPal (consumer, US) | global / US | hybrid wallet: credential container + optional Balance account; fintech-not-bank posture | explicit Balance-account structure in official copy; boundary case carrying wallet + balance in one product |
| GCash (G-Xchange / Mynt) | Philippines | mobile-first finance super-app with cash-in/out outlet network; BSP-regulated issuer | cash-in/cash-out as first-class services; regional South-East-Asia shape |
| Paytm | India | former wallet-first leader; current official site is UPI/bank-rail-centric | market-drift data point: wallet-first markets migrating to bank rails; reachable evidence weak |
| Venmo | US | P2P-first wallet with balance | anchor only — official pages unreachable this pass |

Venmo and Paytm are retained as market anchors without operational claims, per the source-access limitation rule.

---

## Sources

Reached (official, Tier 2 product/ops pages):

- Safaricom — M-PESA services hub: `https://www.safaricom.co.ke/personal/m-pesa` (nav exposes: Register For M-PESA; Send Money; Deposit At Agent; Request Money; Tuma Popote; M-PESA Reversal; Check Balance / Change Pin / Unlock Pin; Consumer Tariffs & Limits; M-PESA to Bank and Bank to M-PESA Tariffs; Lipa na M-PESA — Pay to Paybill / Pochi la Biashara / Pay Online; M-PESA Global; channels: M-PESA Super App, USSD *334#, SIM Toolkit, MySafaricom App). Fetched 2026-09-08.
- PayPal — US consumer home: `https://www.paypal.com/us/home` (incl. footnotes: "A PayPal Balance account is required to hold and use a balance"; "A PayPal Balance account is required to create a pool"; "A PayPal Balance account is required to use PayPal Savings"; "The [PayPal Debit] Card is linked to your PayPal Balance Account"; "PayPal is a financial technology company, not a bank"; nav: Add Cards and Banks / Set Up Direct Deposit / Add Cash; Send / Request / Pool Money). Fetched 2026-09-08.
- GCash — consumer home: `https://www.gcash.com/` (services: Send — Express Send; Pay — Pay QR, Bank Transfer, Tap to Pay, Load, Bills, Global Pay; Cards — GCash Card; Cash In; Cash Out; Receive Money Abroad; Pera Outlets; GSave/GCredit/GLoan/GStocks etc.; "regulated by the Bangko Sentral ng Pilipinas"; 94M users / 6M merchants claims). Fetched 2026-09-08.
- Paytm — consumer home: `https://paytm.com/` (UPI/bank-centric positioning; "Cashback … can be used to pay for goods & services sold by merchants that accept 'Pay with Paytm'"). Fetched 2026-09-08.

Not reached (abandoned after 1–2 failures each, per network rule):

- PayPal legal hub / user agreement (`paypal.com/us/legalhub/...` 404 ×2) — balance-account legal terms unread.
- GCash Help Center (`help.gcash.com` 403).
- Paytm terms and conditions page (redirects to generic home; no wallet terms reached).
- Venmo (`venmo.com/legal/us-user-agreement/` 406).
- Safaricom "Get Started / Register" deep page (404; hub page retained instead).

Consequence: operational precision (KYC-tier limits, fee schedules, balance-expiry rules, withdrawability classes, closure procedures) is **not** asserted anywhere; claims are calibrated to what the reached pages support.

---

## Product Observations

### M-PESA (Safaricom) — Evidence layer A

From the official services hub:

- Intro copy frames the whole motion set: "easy to deposit, send, withdraw or request money", with recipient-name confirmation (Hakikisha) and transaction reversal.
- **Loading**: "Deposit At Agent" (cash-in through a human agent network); "M-PESA to Bank and Bank to M-PESA Tariffs" (bank transfer both directions).
- **Spending**: "Send Money" / "Tuma Popote" (transfers); "Lipa na M-PESA" — "Pay to Paybill", "Pay to Pochi la Biashara", "Pay Online" (payments to registered businesses/merchants); merchant-side world (Business Paybill, Business Till) is documented as a separate business surface.
- **Account management**: "Check Balance", "Change Pin", "Unlock Pin", "Reset Pin", "M-PESA Statement" (user-visible balance and record surfaces), "Register For M-PESA" (registration as an explicit getting-started step).
- **Limits/fees**: a standing "Consumer Tariffs & Limits" publication exists as a product surface.
- **Channels**: M-PESA Super App and Mini Apps, USSD *334#, SIM Toolkit, MySafaricom App — the wallet deliberately runs on non-smartphone channels.
- **Adjacencies** (add-ons, not the wallet core): M-Shwari (savings/loans), Fuliza (overdraft), M-PESA Global (international send; Western Union / PayPal / Alipay interop), M-TIBA (health wallet).

Balance structure is implied by the deposit/send/withdraw trio rather than spelled as "balance account" on this page — treated as A- (direct, but indirect wording).

### PayPal (US consumer) — Evidence layer A

From the official US home page and footnotes:

- **The balance is an explicit, distinct structure**: "A PayPal Balance account is required to hold and use a balance"; also required for money pools and for PayPal Savings — i.e., a specific account type whose function is holding spendable value.
- **Loading**: "Add Cash" and "Set Up Direct Deposit" sit beside "Add Cards and Banks" under "Manage Your Money" — cash, payroll, and linked instruments as entry paths.
- **Spending**: PayPal checkout online/in stores; "Send Money"; the PayPal Debit Card "is linked to your PayPal Balance Account" — balance-backed card spending at Mastercard acceptance.
- **Self-positioning**: "It's your do-it-all digital wallet" — PayPal self-describes as a digital wallet that *also* carries a balance account; the two structures coexist in one product.
- **Posture**: "PayPal is a financial technology company, not a bank, and is not FDIC-insured"; PayPal Savings is a separate product "held at Synchrony Bank" with FDIC insurance — bank-account-ness is explicitly kept outside the balance structure.
- Adjacencies: crypto buy/sell/hold, Pay in 4 / Pay Monthly credit, rewards, savings goals.

This product demonstrates the hybrid shape: credential container + stored-value balance in one app, with the balance being the part this Type is about.

### GCash (G-Xchange / Mynt) — Evidence layer A (balance indirect) / A- 

From the official consumer home:

- **Cash In and Cash Out are first-class top-level services**, alongside "Pera Outlets" (partner outlets for cash in/out) and "Receive Money Abroad" — the in/out motions are the structural spine of the service list.
- **Spending**: Pay QR, Tap to Pay, Load (airtime), Bills, Global Pay, Commute/Transportation; Bank Transfer listed as a money-movement service.
- **Transfers**: Express Send (P2P send).
- **Card companion**: GCash Card (physical card offering).
- **Regulatory posture**: "G-Xchange, Inc. (GCash) is regulated by the Bangko Sentral ng Pilipinas" — an issuer-company posture, not a bank.
- Scale claims: 94M users, 6M merchants and social sellers.
- Adjacencies: GSave (savings), GCredit/GLoan (credit), GStocks/GFunds/GBonds/GCrypto (invest).

The home page does not literally document the balance ledger; the cash-in/cash-out + services structure implies it. Marked A- and treated as cross-product commonality (layer B) rather than sole support for any core claim.

### Paytm — Evidence layer B/C (anchor + drift)

- Current official home is UPI/bank-rail-centric ("Pay anyone directly from your bank account… using Paytm UPI or Directly from your Bank Account"); the historically wallet-first product no longer documents the wallet on reachable pages.
- Retained fact: loyalty cashback "can be used to pay for goods & services sold by merchants that accept 'Pay with Paytm'" — evidence that at least one product maintains a value class that is spendable at acceptance points (a restricted, spend-only value class).
- Usage: market anchor for India; drift data point (wallet-first → bank-rail-first market migration). No operational wallet claims made from this product.

### Venmo — Evidence layer C (anchor only)

- Official pages unreachable this pass (406). Listed as market anchor for the P2P-first shape only; consistent with the P2P pass's earlier finding (Venmo ships cards/checkout around a P2P core).

---

## Cross-product Comparison

| Dimension | M-PESA | PayPal | GCash | Paytm | Venmo |
|---|---|---|---|---|---|
| Persistent user account | yes (registered line/ID) | yes (account; Balance account distinct) | yes (app account) | yes | yes (anchor) |
| Prepaid balance as spend source | yes (deposit→send/withdraw) | yes (explicit Balance account) | implied by Cash In/Out services | not documented on reachable pages | anchor |
| Loading: cash via agents/outlets | yes (Deposit At Agent) | yes (Add Cash) | yes (Cash In / Pera Outlets) | — | — |
| Loading: bank transfer | yes (Bank to M-PESA) | yes (Add Cards and Banks) | yes (Bank Transfer) | — | — |
| Loading: payroll/direct deposit | — | yes (Set Up Direct Deposit) | — | — | — |
| Spending: in-store merchant | yes (Paybill/Till) | yes (debit card, checkout) | yes (Pay QR, Tap to Pay) | — | — |
| Spending: online | yes (Pay Online) | yes (checkout) | yes (Global Pay) | — | — |
| Spending: bills | yes (Paybill) | subscriptions surface | yes (Bills) | yes (bill payments hub) | — |
| P2P send / request | yes | yes | yes (Express Send) | yes | yes (core) |
| Withdrawal / cash-out | yes (withdraw; M-PESA to Bank) | implied by cards/banks link (not explicit on reached page) | yes (Cash Out) | — | — |
| Companion card | — | yes (debit card linked to balance) | yes (GCash Card) | — | yes (anchor) |
| Balance/history user surfaces | yes (Check Balance, Statement) | yes (app money management) | yes (app; indirect) | — | — |
| Published tariffs/limits | yes (Consumer Tariffs & Limits) | fees pages exist (not reached) | fees/limits in help (not reached) | — | — |
| Channels beyond smartphone app | USSD *334#, SIM Toolkit, agents | web + app | app | app | app |
| Non-bank operator posture | telco | "fintech, not a bank" | BSP-regulated issuer | fintech | fintech (anchor) |
| Savings/credit/invest add-ons | M-Shwari, Fuliza | Savings (bank-held), credit, crypto | GSave, GCredit, GLoan, GStocks… | broad suite | — |
| Recipient confirmation / reversal | yes (Hakikisha; Reversal) | — | — | — | — |

Reading: the four structural motions — account → load → spend-against-balance → observe (balance/history) — appear across every product with reachable evidence; withdrawal/cash-out appears in the mobile-money shapes and is implied in PayPal; every other repeated feature (agent networks, USSD, QR, bills, companion cards, savings/credit suites) varies by product or philosophy.

---

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Four jointly-held structures. Removing any one stops the product being a Stored Value Wallet:

1. **The wallet account of record** — a persistent balance container attributed to a holder and maintained by the wallet operator, outliving individual transactions. The holder is carried by whatever identity substrate the product uses (full identity, phone number, credential/PIN — abstract, not fixed). *Remove → bearer single-purpose instruments (vouchers, one-shot codes) with no maintained holder container.*
2. **The prepaid balance of record** — the user's own monetary value held in that account **in advance of spending**; the balance is the reservoir every payment draws from. *Remove → a credential container paying from linked external instruments (Digital Wallet territory), or a points/loyalty ledger (not monetary value).*
3. **The loading path** — standing ways value enters the balance from outside (bank transfer, card top-up, cash at agent/outlet, payroll/direct deposit, refunds/rewards credit). *Remove → a single-endowment account (gift-card-like); no ongoing prepaid life.*
4. **Spending against the balance** — the wallet's own payment motion: a payment (merchant, bill, online, transfer — mix varies by product) is authorized by drawing down the stored balance at the wallet's acceptance points, rather than by charging a linked external instrument. *Remove → a top-up register / savings jar; not a payment wallet.*

Jointly-held is load-bearing:

- 2+3+4 without 1 = anonymous prepaid voucher (PIN/cash-code instruments).
- 1+3+4 without 2 = wallet paying from linked instruments = credential wallet (Digital Wallet).
- 1+2 without 3 = single-endowment closed account (gift-card shape).
- 1+2+3 without 4 = a holding/savings place, not a payment wallet.

### L1 — Common Mature Structure (expected in mature products, not definitional)

- User-visible current balance and a transaction history (the wallet as its own statement).
- Linked funding sources (bank accounts, cards) feeding the loading path.
- Cash-out / withdrawal (to bank, or cash via agent/outlet) — common but not universal (closed-loop variants may forbid it).
- P2P send/request between wallet users.
- Merchant-acceptance surfaces of the era (QR codes, tap, checkout buttons, paybill numbers).
- Bill payment as a spend category.
- Security surfaces (PIN, app lock, recipient confirmation); published tariffs/limits.
- Registration/verification gating what an account can do (category-level; specifics vary and were not asserted).
- Companion physical/virtual card drawn against the balance (common in several shapes).

### L2 — Variant / Optional Structure

- **Acceptance scope**: open-loop general-purpose vs closed-loop (operator-scoped: retailer, campus, venue, transit) — closed loops with an operating institution are separate Atlas Types; the generic wallet is the user-owned remainder.
- **Operator posture**: telco, fintech, licensed e-money issuer, or bank-issued; regulatory classification of the balance (e-money/prepaid vs deposit) varies by jurisdiction.
- **Channel philosophy**: smartphone-app-first vs USSD/SIM-toolkit/agent-counter-first (no-smartphone wallets).
- **Identity substrate**: phone number, email/account, national ID/KYC, PIN/credential.
- **Withdrawability classes of value**: some products distinguish spend-only value (promotional cashback) from withdrawable balance (evidenced at Paytm for the former concept).
- **Super-app embedding**: the wallet as one module among lending/savings/invest/shopping.
- **Cross-border**: international send/receive/remittance partners.
- **P2P-first vs spend-first** internal emphasis.

### L3 — Vendor-specific (research notes only)

- M-PESA: Hakikisha recipient-name confirmation; M-PESA Reversal; Pochi la Biashara; Fuliza overdraft; M-Shwari; M-PESA Global interop list; Tuma Popote.
- PayPal: Pools (requires Balance account); PayPal Savings held at Synchrony Bank; PYUSD/crypto via Paxos; Pay in 4/Pay Monthly credit; rewards points categories.
- GCash: G-branded suite (GSave/GCredit/GLoan/GStocks/GFunds/GBonds/GCrypto/GGives); Pera Outlets; GCash Jr; GLife mini-programs.
- Paytm: Soundbox; UPI-centric repositioning; Paytm loyalty cashback mechanics.

---

## Rejected Findings (considered, rejected as core)

- **Agent cash network as core** — defining for mobile-money variants; absent as a defining structure in app-first products (PayPal has no agent counter in its core motions). → L2 variant.
- **QR-code payment as core** — era- and region-specific; M-PESA's merchant pay is paybill-number-based and predates QR. → L1/L2.
- **Smartphone app as core** — USSD/SIM-toolkit wallets run without one. → rejected; channel is a variant.
- **P2P transfer as core** — wallets can be spend-first; P2P services can be balance-less (bank-rail). Embedded-but-not-defining. → L1, boundary documented.
- **Bill payment as core** — common spend category, absent from several products' core motions. → L1.
- **Specific KYC tiers / numeric limits / fee schedules as core** — category exists (published limits are real) but specifics are jurisdiction- and product-specific and were not reliably reachable. → L1 category, no numbers asserted.
- **E-money regulation as definitional** — regulatory posture varies (telco float, e-money institution, bank product); it shapes the operator, not the application's user-facing structure. → context only.
- **Multi-currency wallets as core** — product-specific capability. → L2.
- **Savings/credit/invest modules as core** — super-app drift; every sampled product carries some, none is needed for the Type. → L2/L3.
- **"Digital wallet = any app that pays" as this Type** — would collapse the credential-container sibling leaves into this one; rejected in favor of the balance-based seam.

---

## Boundary Findings

Each boundary carries a remove-test (what to strip so the remainder is the other Type).

1. **vs Digital Wallet (§08 sibling, unprocessed)** — the credential container: stores payment instruments (cards/tokens/passes) and pays from linked external accounts; holding a user-funded balance is optional. *Remove the user-held prepaid balance (spend always draws from linked instruments) → Digital Wallet. Add the prepaid balance as the spend source → this Type.* Hybrid products (PayPal self-described "do-it-all digital wallet" carrying a distinct Balance account) ship **both structures in one product**; the seam is structural, not per-product. This pass's §Boundary Findings are the counterparty record for the digital-wallet pass.
2. **vs Mobile Wallet (§08 sibling, unprocessed)** — "mobile wallet" names the form factor, not a different value structure; most wallet products are mobile. Likely a form-factor Variant judgment for its own pass. *Remove the device emphasis → same structure.* Flagged for the mobile-wallet pass.
3. **vs Peer-to-peer Payment Application (processed)** — P2P core is transfer between identified individuals; wallet core is the prepaid spending account. P2P is a frequent wallet capability; stored value is one funding implementation for P2P. *Remove merchant/bill spending → P2P remains; remove P2P → wallet remains.* This pass **resolves from this side** the joint review flagged by the P2P pass: keep both Types; wallet P2P is a capability, not the boundary.
4. **vs Digital Banking Application / Mobile Banking Application (§08)** — a bank account is a deposit relationship (statements, interest, overdraft as banking product); the wallet balance is prepaid value held by a non-bank (or bank-program) operator and spent down. PayPal's own copy enforces the seam ("fintech, not a bank"; Savings explicitly a separate bank-held product). *Remove the prepaid-balance-as-instrument and add the deposit-account relationship → banking.*
5. **vs Store Credit / Stored Value Platform (processed)** — merchant-side system of record for a closed-loop value program (issuance, liability, redemption rules) vs consumer-side spending wallet. That pass's test adopted here: *value spends only at the issuing merchant's channels → Store Credit platform territory; value is the user's own general spending balance → this Type.*
6. **vs Campus Card Management / Cashless Venue Platform (processed)** — institution- or venue-scoped closed loops bundled with access privileges / venue operations and venue-administered funding. *Remove the institution/venue scoping and its privilege layer → a (closed-loop) stored value wallet.* Consistent with both passes' recorded remove-tests.
7. **vs Gift Card Management (§05.15, unprocessed)** — single-merchant (or single-network) instrument programs; no ongoing loading, no multi-purpose account. *Single endowment, spend-only, instrument-shaped → Gift Card / Store Credit territory; ongoing loading into a user account → this Type.*
8. **vs Card Issuing Platform (§08, unprocessed)** — B-side issuing/processing infrastructure behind prepaid cards and wallet rails vs the consumer-facing wallet application. *Remove the consumer surface → issuing platform.*
9. **vs Payment Gateway / Payment Processing Platform (processed)** — payee-side acceptance infrastructure; wallets appear inside them as payment method types. Payer-side vs payee-side seam confirmed from this side.
10. **vs Crypto Wallet (processed)** — same word, different asset class: user-held blockchain keys vs operator-held fiat prepaid balance. The crypto-wallet pass's remove-test (strip key control + chain-anchored state) applied in reverse here: *strip the fiat prepaid balance and add user-held key material → Crypto Wallet.*
11. **Anonymous prepaid instruments** (PIN calling-card codes, cash vouchers) — historical/regional shapes that satisfy load+spend but fail the persistent holder-attributed account leg; recorded as instruments, not wallets. Prepaid calling-card *accounts* (persistent PIN accounts with balance, top-up, usage draw-down) satisfy all four L0 legs — the §24 historical check anchor.

---

## Uncertainties

1. **GCash balance ledger** — evidenced indirectly (Cash In/Cash Out services, app structure); help center unreachable. No sole-support claims rest on it.
2. **PayPal balance-account legal terms** (withdrawability, fee classes, value classes) — legal hub 404; the reached page proves the structure exists and what it is *for*, not its fine rules. No precision asserted.
3. **Paytm wallet current status** — not documented on reachable pages; retained as anchor + drift note only.
4. **Venmo / Cash App** — unreachable; anchors only.
5. **Withdrawal as universal** — A-evidenced in mobile-money shapes, implied-but-not-explicit in PayPal's reached page; held as L1 common, not core.
6. **Whether the unprocessed Digital Wallet / Mobile Wallet passes will accept the proposed seam** — flagged for joint review; this pass takes the balance-based position and records it.
7. **Regulatory classification of balances** across jurisdictions (e-money vs deposit vs telco float) — not researched in depth; posture kept generic.

---

## Final Synthesis

The Stored Value Wallet is the **consumer-side prepaid money account**: the defining structure is the user's own monetary balance held in a persistent wallet account, loaded through standing entry paths, and spent down as the wallet's own payment instrument, with the user facing balance and history as the standing record. Everything else observed — agent networks, USSD channels, QR codes, companion cards, P2P, bill pay, super-app suites, regulatory packaging — is common mature structure or variant coloring, not definition.

The wallet trio in the directory splits on one question: **where does a payment draw from?** A credential container draws from linked external instruments (Digital Wallet); the Stored Value Wallet draws from the user's own prepaid balance inside the wallet. Products routinely carry both structures; the Type boundary is structural, not per-product. Mobile Wallet names a form factor and is expected to resolve as a variant.

Historical check passes: prepaid calling-card accounts and prepaid airtime credit (balance + top-up + usage draw-down, no smartphone, no QR, no KYC-apparatus) satisfy the four-leg core; paper meal vouchers and single-use vouchers fail the account leg and are correctly instruments, not wallets; institution-scoped closed loops (campus, venue, transit purses) carry extra operating context that makes them separate Types, not definitions of this one.
