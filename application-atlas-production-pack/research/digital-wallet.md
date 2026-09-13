# Research Notes — Digital Wallet

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)
Directory leaf: `Digital Wallet` (§08 Finance, Banking, Insurance & Investment; sibling of Mobile Wallet, Stored Value Wallet)
Slug: `digital-wallet`

---

## Research Goal

Establish what a Digital Wallet is as an Application Type — the third and final pass over the §08 wallet trio. Two sibling passes (stored-value-wallet, mobile-wallet, both processed 2026-09-08) left explicit counterparty records constraining this pass:

- `research/stored-value-wallet.md` §Boundary Findings #1: Digital Wallet is "the credential container: stores payment instruments (cards/tokens/passes) and pays from linked external accounts; holding a user-funded balance is optional… the seam is structural, not per-product."
- `research/mobile-wallet.md` §Boundary Findings #1 + §Final Synthesis: Digital Wallet is "the holder-side credential/value container reachable from any surface (web checkout accounts, cloud wallets), where the payment act happens wherever the checkout happens." The counterparty record requires that this pass's defining core **must not swallow the carried-device execution surface** (Mobile Wallet's substance) and must not reduce Digital Wallet to "an account container that only funds payments executed elsewhere" (the funding-source residue below the Mobile Wallet Type). If this pass judged the two leaves as one Type split by surface, the instruction was to escalate to a maintainer joint review rather than silently merge.
- `research/peer-to-peer-payment-application.md` (processed 2026-09-06) flagged a joint review with all three wallet leaves; the stored-value pass partially discharged it (P2P = embedded capability; keep-both).
- `research/crypto-wallet.md` (processed) warns "wallet" names different things across the directory (keys vs fiat containers).

This pass must define Digital Wallet on its own evidence, keep or contest the trio seam, and discharge the outstanding flags from this side.

---

## Initial Boundary

Working hypothesis at start:

- Candidate core: a holder-side container that stores the user's payment instruments (cards/credentials, and commonly other wallet items), lets the user manage that instrument set, and participates in payments across whatever surface the user is on (web checkout, in-app, in-store, device).
- Nearest neighbors: Mobile Wallet (processed — carried-device surface), Stored Value Wallet (processed — prepaid balance), Peer-to-peer Payment Application (processed — transfer core), Crypto Wallet (processed — keys), Payment Gateway / Processing / Orchestration / Merchant Payment Platform (payee-side, processed), Card Issuing Platform / Card Management System (issuer-side, processed), Digital Banking Application (bank relationship, processed), Checkout Platform (merchant-side flow, processed), Password Manager (storage without payment), Government Digital Identity / Digital Credential Platform (document/identity wallets), Store Credit / Gift Card Management / Campus Card / Cashless Venue (scoped value programs).
- Known unknowns at start: whether "reachable from any surface" can be a positive invariant (device-only wallets might fail it); whether instrument management is separable from the container; whether tokenization is definitional or implementation; how much of the "any surface" pole can be evidenced given that the cloud-checkout wallet category's official pages (Visa/Mastercard Click to Pay) were expected to be hard to reach.

---

## Research Questions

1. What does the wallet hold, in the vendor's own words — instruments, value, other items?
2. Where does the instrument set live (account, device, both), and how does it persist across surfaces/devices?
3. How do instruments enter and leave the wallet (add, verify, manage, remove), and who gates that?
4. What exactly does the wallet contribute at payment time — credential, representation, identity, method selection?
5. What does the payee see (raw instrument vs representation)?
6. What rides in the same container beyond payment instruments (value, passes, IDs, keys)?
7. How do the operator postures differ (platform vendor, OEM, fintech, network, bank, telco)?
8. Remove-tests against every neighbor; and the trio-defining question: does the container structure stand on its own without the device surface and without the balance?

---

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different container homes:

| Product | Container home | Philosophy / position | Why sampled |
|---|---|---|---|
| PayPal (digital wallet) | user account (cloud/server-side) | fintech account-container; linked instruments + optional Balance account; web + app + in-store | self-describes as a digital wallet; FAQ directly addresses the wallet naming; the account-container pole; hybrid case |
| Apple Wallet / Apple Pay | device platform with account-associated card set | platform-native container ("place where you store cards") + device payment execution | vendor-articulated container-vs-execution split; strongest operational documentation; shows device surface as a separate structure |
| Google Wallet / Google Pay | Android platform / Google account | OS-native wallet, cards/passes/IDs | Android-side market anchor — official pages unreachable this pass (consistent with sibling passes) |
| Samsung Wallet | Galaxy device | OEM wallet, broad credential scope | second OS-family pole; reached first-hand by the mobile-wallet pass same day (cross-pack) |
| Visa / Mastercard Click to Pay | network-operated cloud checkout | the network-run online-checkout wallet category | attempted this pass — Visa 404, Mastercard 403; anchor only, no structural claims |

---

## Sources

Reached this pass (official, Tier 2 product pages):

- PayPal — Digital Wallet / app page: `https://www.paypal.com/us/digital-wallet` (page title "All-In-One Payment App | Digital Wallet"; FAQ "What is a mobile wallet app, and is PayPal a digital wallet? PayPal is an online payment system… You can link your bank account, credit card, or debit card. You can also have a balance in your PayPal account."; card-link limits 4 unverified / 24 verified in FAQ copy; "Biometrics and passkeys secure your account before you buy"; pay "online, in-store, or in the app"; Pay in 4 / Pay Monthly; Send/Request/Pool; "A PayPal Balance account is required to hold and use a balance"; "PayPal Digital, Inc. is chartered as a limited purpose trust company by the New York State Department of Financial Services"; 400M+ active accounts, "over 25 years in business"). Fetched 2026-09-08.
- Apple — Apple Pay overview: `https://www.apple.com/apple-pay/` (setup via Wallet app, card add by tapping card to iPhone back or manual entry, "verify your information with your bank or card issuer"; "device-specific number and unique transaction code… actual card number isn't shared… not stored on Apple servers"; "Every purchase requires Face ID, Touch ID, or a passcode"; online/in-app Apple Pay button; "On a non-Safari browser, scan the Apple Pay code with your iPhone camera and use your iPhone to complete your purchase"; card transfer "to the new device in one easy step"; Apple Cash "a digital card in Wallet"; connected-card balance view; "No. Apple does not charge any fees"; "Any card used in Apple Pay is offered by the card issuer"; "Neither Apple Inc. nor Apple Payments Services LLC is a bank"). Fetched 2026-09-08.
- Apple — Wallet product page: `https://www.apple.com/wallet/` ("Carry one thing. Everything."; "Apple Wallet is an app… that securely and conveniently organizes your eligible credit and debit cards, transit passes, boarding passes, tickets, identity cards, keys, order tracking details, rewards cards, and more — all in one place."; FAQ: "What is the difference between Apple Pay and Apple Wallet? Apple Pay is a safe way to pay and make secure purchases in stores, in apps, and on the web. Apple Wallet is the place where you store your credit or debit cards so you can use them with Apple Pay."; "your card information is securely associated with your Apple Account — helping you add and manage your cards and passes across devices"; store/rewards/prepaid cards in Wallet; loyalty auto-redemption; pay-later options added in Wallet; ID/badge/key/pass surfaces; "unique transaction code"). Fetched 2026-09-08.

Cross-pack corroboration (first-hand fetches by sibling passes, same production pack):

- `research/mobile-wallet.md` (2026-09-08): Samsung Wallet page (`samsung.com/us/apps/samsung-wallet/` — Knox on-device storage, add-card with bank authentication, passes/IDs/keys/passwords, Tap to Transfer); Apple Pay page details (device-specific number, per-device lifecycle); M-PESA hub (line-identity balance wallet).
- `research/stored-value-wallet.md` (2026-09-08): PayPal US home (`paypal.com/us/home` — "It's your do-it-all digital wallet"; Balance-account footnotes; "PayPal is a financial technology company, not a bank"; Add Cards and Banks / Add Cash / Direct Deposit).
- `research/card-issuing-platform.md` (2026-09-07): "digital wallet tokenization (Apple/Google-class provisioning)" as an issuer-side standard capability; `applications/card-issuing-platform.md`: "Cards can be tokenized into digital wallets, where the wallet pays with a network token standing in for the card."
- `research/corporate-card-spend-platform.md`: cardholder wallet receipts show wallet device numbers instead of card numbers.

Not reached (abandoned per network rule after 1–2 failures):

- Google Wallet: `https://support.google.com/wallet` (timeout; sibling pass additionally timed out on `wallet.google.com` and `pay.google.com` twice). Market anchor only; no operational claims sourced from Google.
- Visa Click to Pay: `https://usa.visa.com/pay-with-visa/click-to-pay.html` (404). Mastercard Click to Pay: `https://www.mastercard.us/en-us/personal/pay-with-mastercard/click-to-pay.html` (403). Category anchor only.
- Wikipedia "Digital wallet" (historical framing attempt): `https://en.wikipedia.org/wiki/Digital_wallet` (timeout; second Wikipedia-family timeout recorded in this pack). No historical lineage names are asserted anywhere in this pass.

Consequence: no precise numeric limits, no fee schedules, no security-architecture internals (secure-element names, token-scheme names), and no market-share figures are asserted. Claims are calibrated to the three reached pages plus cross-pack corroboration.

---

## Product Observations

### PayPal — Evidence layer A

From the official Digital Wallet page:

- **Self-identification as the Type.** Page title "Digital Wallet"; FAQ explicitly pairs the sibling terms: "What is a mobile wallet app, and is PayPal a digital wallet? PayPal is an online payment system… You can link your bank account, credit card, or debit card. You can also have a balance in your PayPal account."
- **The container is the account, not a device.** Instruments (linked bank accounts, credit cards, debit cards) live in the user's account; the app is one surface among several (pay "online, in-store, or in the app"; "sign up for free online" — the account exists and is usable off-device).
- **The instrument set is user-curated and gated.** "How many cards can I add… You can link 4 cards to your unverified account… When your account is verified, you can link up to 24 cards" — linking is a managed, verified, bounded instrument set (numeric detail: research notes only).
- **A balance is an optional, distinct structure.** "A PayPal Balance account is required to hold and use a balance" (footnote; also for pools) — the balance is a specific account type inside the wallet product, separable from the linked-instrument container. Cross-pack (stored-value pass, PayPal home): "It's your do-it-all digital wallet"; "PayPal is a financial technology company, not a bank."
- **The wallet contributes identity/verification to the payment.** "Biometrics and passkeys secure your account before you buy. Your transactions are encrypted." Purchase Protection attaches to wallet-mediated purchases.
- **P2P rides the wallet.** Send/Request/Pool/Split in the same app — consistent with the P2P pass's embedded-capability finding.
- **Longevity of the account-container shape.** "over 25 years in business" — the account container predates the smartphone-wallet era (A-layer for the fact; the era inference is C-layer).
- Adjacencies on the same page: crypto (via a NYDFS-chartered affiliate), Savings, PayPal Debit Card, Pay in 4 / Pay Monthly credit, offers/rewards, order tracking, business/seller surfaces.

### Apple Wallet / Apple Pay — Evidence layer A

From the official Apple Pay and Wallet pages:

- **Vendor-articulated container-vs-execution split.** Wallet FAQ: "What is the difference between Apple Pay and Apple Wallet? Apple Pay is a safe way to pay and make secure purchases in stores, in apps, and on the web. Apple Wallet is the place where you store your credit or debit cards so you can use them with Apple Pay." — the container (store) and the payment act (pay) are named as two different things.
- **The container holds an instrument set.** "Apple Wallet is an app… that securely and conveniently organizes your eligible credit and debit cards, transit passes, boarding passes, tickets, identity cards, keys, order tracking details, rewards cards, and more — all in one place." Credit/debit, prepaid, store, and rewards cards are all wallet content; non-payment items ride the same container.
- **The container is account-associated and cross-device.** "Your card information is securely associated with your Apple Account — helping you add and manage your cards and passes across devices" — the card set persists above the single device, while provisioning into individual devices remains an explicit step ("You'll have the option to add your card to your other devices at the same time"; "If you upgrade your iPhone, you can transfer your cards to the new device in one easy step").
- **Instrument management runs through the wallet.** Add by tapping the card to the phone or manual entry, then "verify your information with your bank or card issuer"; connected cards expose balance and activity inside Wallet ("view your card balance right in Wallet"); pay-later options can be "add[ed]… in Wallet."
- **What the payee sees is a representation, not the raw instrument.** "Apple Pay uses a device-specific number and unique transaction code. So your actual card number isn't shared by Apple with merchants or stored on Apple servers." (Cross-pack: corporate-card pass records wallet device numbers on receipts.)
- **Device execution is a separate surface structure.** In-store: device gesture + contactless tap; per-purchase device verification ("Every purchase requires Face ID, Touch ID, or a passcode"). On non-Apple browsers the checkout surface is a desktop/web browser and the phone completes the act via scanned code — the checkout happens wherever it happens; the device supplies the payment. This is exactly the Mobile Wallet structure riding this container.
- **Issuer relationship preserved; operator not a money mover.** "Any card used in Apple Pay is offered by the card issuer"; "Apple does not charge any fees when you pay with Apple Pay"; "Neither Apple Inc. nor Apple Payments Services LLC is a bank."
- **Value inside the container is a distinct structure.** Apple Cash is "a digital card in Wallet" spendable with Apple Pay — a balance-shaped value class inside the same container (serviced by a partner bank per footnotes).
- **Container extends beyond payment.** IDs, badges, student IDs, home/hotel/car keys, transit cards, boarding passes, order tracking — the "Carry one thing. Everything." positioning.

### Google Wallet / Google Pay — Evidence layer C (anchor only)

- Official pages unreachable this pass and in the sibling pass (timeouts ×3 cumulative across `support.google.com/wallet`, `wallet.google.com`, `pay.google.com`). Retained as the Android-side OS-native wallet anchor; the card-issuing pass's "Apple/Google-class provisioning" language corroborates that issuers provision card credentials into it. No operational claims sourced from Google.

### Samsung Wallet — Evidence layer A via sibling pass (cross-pack)

- From `research/mobile-wallet.md` (first-hand fetch 2026-09-08): OEM wallet holding "debit/credit cards, loyalty and membership cards, boarding passes, digital IDs, digital car/home keys, passwords"; add card with "authenticate with your bank"; "on-device data storage and encryption" (Knox); device-executed payment; Tap to Transfer P2P. Confirms the same container+management+participation structure on a second OS family, with the device surface explicitly present (Mobile Wallet structure riding along).

### Visa / Mastercard Click to Pay — Evidence layer C (anchor only)

- Both official pages unreachable (404 / 403). Listed only as the network-operated online-checkout wallet category anchor. **No structural claims** are made from this product.

---

## Cross-product Comparison

| Dimension | PayPal | Apple Wallet/Pay | Google Wallet | Samsung Wallet | Click to Pay |
|---|---|---|---|---|---|
| Container home | user account (cloud) | device platform + Apple-Account-associated card set | Android/Google account (anchor) | Galaxy device (Knox) | network cloud (anchor) |
| What it holds | linked instruments (banks/cards); optional Balance account; crypto | cards (credit/debit/prepaid/store/rewards); passes, IDs, keys, tickets | cards + passes + IDs (anchor) | cards + passes + IDs + keys + passwords | card credentials for checkout (anchor) |
| Instrument management | link/unlink with verification tiers (4/24 limits in FAQ copy) | add (tap/manual) + issuer verification; manage across devices; balance/activity view; pay-later add | (anchor) | capture + bank authentication | (anchor) |
| What payment draws on | linked instrument or Balance account (user-selected) | held instrument via device token/device-specific number | (anchor) | held instrument via device credential | (anchor) |
| Surfaces served | online checkout, in-app, in-store, P2P | web (incl. non-Apple browsers via code handoff), in-app, in-store, P2P | (anchor) | in-store tap, in-app, P2P | online checkout (anchor) |
| Payee sees | wallet-mediated method (Purchase Protection attaches) | device-specific number + transaction code, not the card number | (anchor) | device credential | (anchor) |
| User verification | biometrics/passkeys on account | Face ID/Touch ID/passcode per purchase | (anchor) | fingerprint/PIN per payment | (anchor) |
| Value inside container | yes — Balance account (distinct structure) | yes — Apple Cash digital card | — | — | — |
| P2P inside | yes (send/request/pool/split) | yes (Apple Cash, Messages/Tap to Cash) | — | yes (Tap to Transfer) | — |
| Non-payment items | — | passes, IDs, keys, tickets, order tracking | (anchor) | passes, IDs, keys, passwords | — |
| Operator posture | fintech ("not a bank"; balance servicing and crypto via regulated affiliates) | platform vendor ("not a bank"; issuer offers the card; no consumer fees) | platform vendor (anchor) | device OEM | card network (anchor) |
| Device required? | no (web account) | yes for execution, container is account-associated | (anchor) | yes | no (anchor) |

Reading: every sampled product is a **holder-side container of payment instruments with user-operated instrument management, participating in payments as the payer-side structure**. Everything else varies: where the container lives (account vs device vs both), what else rides in it (value, passes, keys), which surface executes the act (checkout flow vs device), what the payee sees (wallet-mediated method vs device-specific number), and the operator's posture. No two products agree on any of those variables — they agree only on the container/management/participation structure.

---

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Removing any one stops the product being a Digital Wallet:

1. **The holder-side instrument container of record** — a persistent wallet maintained for the user that holds the user's payment instruments as its content: added cards (credit/debit/prepaid — commonly store and rewards cards too) and their digital representations, optionally alongside wallet value and other credentials. The container is **user-owned and general-purpose**: it serves the user across merchants, surfaces, and time — it is not one merchant's saved-card list and not an institution's record system. *Remove → card-on-file inside a single merchant's checkout account; an instrument list with no wallet around it.*
2. **User-operated instrument management** — the user curates the instrument set through the wallet: adding/linking instruments (commonly gated by issuer/bank verification), viewing and managing them, selecting among them, and removing them. The wallet is where this lifecycle is operated and where instruments persist between payments. *Remove → a static credential vault / browser autofill store (storage with no managed instrument lifecycle), or issuer-side card management of one issuer's own card.*
3. **Payer-side participation in payments** — when the user pays, the payment draws on a held instrument supplied through the wallet, on whatever surface the payment happens (web checkout, in-app, in-store, device tap, person-to-person); the wallet stands behind the payment as the holder-side structure, and what the payee receives is typically wallet-mediated rather than the raw instrument. This Type does **not** own the execution surface: where the act is executed and verified on a carried device, the product additionally realizes the Mobile Wallet structure; where payments draw on a user-held prepaid balance, the product additionally realizes the Stored Value Wallet structure. *Remove → credential storage with no payment participation (a card safe), or a payee-side acceptance product.*

Jointly-held is load-bearing:

- 1 without 2+3 = a card vault / autofill data store.
- 2 without 1+3 = managing a single issuer's card in that issuer's channel (card-management territory), not a cross-instrument wallet.
- 3 without 1+2 = a one-shot checkout method (typed card at guest checkout), not a wallet.
- 1+2 without 3 = credential storage that never pays (document safe).
- 1+3 without 2 = an express lane with no standing instrument home (checkout-feature territory).

Historical/market-sample check passes at this level: the account-container shape long predates the smartphone wallet (the sampled account wallet documents over 25 years of operation; its container+management+checkout structure requires no device, no NFC, no balance, no P2P, no tokenization — the linked-instrument set is the substance); today's OS wallets satisfy the same structure with the device surface added on top (that surface is the Mobile Wallet contribution, not part of this core); a user's card set associated to an account and manageable across devices is documented vendor-side (Apple: card information "securely associated with your Apple Account… across devices"). No smartphone, no NFC, no stored balance, no app is required by the core.

### L1 — Common Mature Structure (expected in mature products, not definitional)

- Digital representation of instruments (tokenization): the payee receives a device-specific number / network token / unique transaction code instead of the raw card number; the raw number is not stored on the wallet operator's servers (vendor-explicit on the Apple pages; cross-pack corroboration from wallet device numbers on corporate-card receipts).
- Issuer/bank verification gating instrument addition ("verify your information with your bank or card issuer"; "authenticate with your bank"; verification-tiered link limits).
- Multi-instrument holding with per-instrument management (view, default/select, remove, replace; numeric link limits in some products — research notes only).
- Express checkout buttons / one-tap online payment flows (the wallet as the pre-filled payer at checkout; cross-pack: the checkout-platform pass treats wallet buttons as lanes inside checkout).
- In-store/device execution when the instrument is provisioned to a device (the Mobile Wallet structure riding the container).
- Payment activity/history; instrument balance views where the issuer supports connected accounts.
- P2P send/request/pool/split riding the same wallet (per the P2P pass: embedded capability, not the boundary).
- Optional wallet value inside the container (a balance account or digital card; holding/using it may require a specific account type).
- Non-payment items riding the same container in platform/OEM wallets: passes, tickets, transit cards, IDs, badges, keys, order tracking, loyalty/rewards cards (absent from account-only wallets).
- Security/privacy posture: biometric/passkey/PIN verification; privacy controls over what merchants receive.
- Rewards/loyalty redemption and offers applied at checkout; pay-later/installment options attached to instruments or added through the wallet.
- No-consumer-fee posture for paying (where the operator is not the money mover).

### L2 — Variant / Optional Structure

- **Container home**: account/cloud (server-side, usable off-device) vs device-hosted (per-device with replacement transfer) vs hybrid (account-associated card set with explicit per-device provisioning).
- **Operator posture**: OS/platform vendor, device OEM, fintech (explicitly not-a-bank), card network, bank, telco; where value is held, regulated servicing often sits with partner institutions.
- **Instrument scope**: general-purpose open-loop cards vs restricted/specialty instruments (store cards, single-network instruments).
- **Surface emphasis**: web-checkout-first vs device-first vs merchant-code/QR markets.
- **Value classes inside** (where balance exists): spend-only promotional value vs withdrawable balance (per the stored-value pass).
- **Crypto buy/hold riding the wallet** (product-specific).
- **Super-app embedding**: the wallet as one module of a larger finance/commerce platform.
- **Regional channel shapes**: line-identity realizations, agent-assisted loading (belonging primarily to the sibling Types when those structures dominate).
- **Seller-side twins** (accepting with the same device) exist as separate products/Types (Mobile POS).

### L3 — Vendor-specific (research notes only)

- Apple: Wallet-vs-Pay naming split in the FAQ; "Carry one thing. Everything."; Apple Cash as a "digital card in Wallet" serviced via Green Dot Bank; Tap to Cash; Apple Card via Goldman Sachs with Daily Cash/Savings; Hide My Email; connected-card balance ("Get Account Balance & Activity"); Express Mode transit; Digital ID from passport; order tracking via on-device mail parsing; one-step card transfer on device upgrade; Apple Cash Family and Tap to Cash rolling limits (numeric — research notes only); QR handoff from non-Apple browsers.
- PayPal: 4-card (unverified) / 24-card (verified) link limits; "A PayPal Balance account is required to hold and use a balance" (also pools); Pay in 4 ($30–$1,500, PayPal Inc. as lender) and Pay Monthly (WebBank as lender; in-store single-use card valid 24 hours post-approval); PayPal Digital Inc. NYDFS limited-purpose trust charter (crypto); Purchase Protection; receiving-fee model; 400M+ active accounts claim; "over 25 years".
- Samsung (via sibling pass): Knox on-device storage/encryption; Samsung Pass passwords in the wallet; UWB/NFC keys; Tap to Transfer; installments via third party.
- Google: nothing sourced (unreachable across both passes).
- Visa/Mastercard Click to Pay: nothing sourced (unreachable); category anchor only.

---

## Rejected Findings (considered, rejected as core)

- **"Digital wallet requires a mobile device / = mobile wallet"** — rejected. The account-container pole (PayPal; the network-checkout category) exists without device dependency; the counterparty record explicitly forbids swallowing the carried-device surface. The device surface, when present, is the Mobile Wallet structure realized alongside.
- **"Digital wallet requires a balance"** — rejected. OS wallets hold no balance; PayPal's balance is a distinct account type ("required to hold and use a balance") inside the product. The balance, when it is the defining draw-from, is the Stored Value Wallet.
- **"P2P is definitional"** — rejected (P2P pass; embedded capability in all sampled wallets, absent from pure checkout wallets).
- **"Tokenization/device-specific numbers are definitional"** — rejected. The account-container pole pays from linked instruments without device-hosted tokens; tokenization is the dominant modern implementation for network cards, an L1 implementation of "what the payee receives is wallet-mediated."
- **"Express checkout button = the wallet"** — rejected (checkout-platform pass framing): the button is a lane inside the merchant's checkout; the wallet is the payer-side container standing behind it.
- **"Any saved card at a merchant = a digital wallet"** — rejected. Card-on-file is merchant-scoped storage inside the merchant's account system; the wallet is user-owned, general-purpose, and cross-merchant.
- **"Non-payment items (IDs, keys, passes) are definitional"** — rejected. First-class in platform/OEM wallets, absent from account wallets. → L1/L2.
- **"Wallet = finance super-app"** — rejected. Savings/credit/invest/crypto modules appear across samples as add-ons; none is needed for the Type.
- **"Crypto wallet is the same Type"** — rejected (crypto-wallet pass): user-held blockchain keys vs fiat payment instruments; naming conflation only.
- **"The wallet operator is a bank"** — rejected. Sampled postures explicitly disclaim bank status ("fintech, not a bank"; "Neither Apple… is a bank"); issuers offer the instruments; value servicing sits with partner institutions.

---

## Boundary Findings

Each boundary carries a remove-test (what to strip so the remainder is the other Type).

1. **vs Mobile Wallet (§08 sibling, processed 2026-09-08) — counterparty record DISCHARGED, keep-both ratified from this side.** The seam is structural: Digital Wallet is what holds the credential (the instrument container, reachable from whatever surfaces the user uses); Mobile Wallet is where the wallet lives and the payment act happens (carried device, device-executed and device-verified, exposing device identity). *Remove the carried-device home/execution → Digital Wallet. Add them → Mobile Wallet.* This pass does **not** merge the two leaves and does **not** claim the device execution surface in the core; conversely it confirms the container structure is substantive on its own (container + management + payer-side participation), not a funding-source residue — the residue warning is answered by L0 legs 1+2. The wallet-trio seam is now recorded consistently from all three passes: **what holds the credential (this Type) / where the wallet lives and pays (Mobile Wallet) / where the payment draws from (Stored Value Wallet)**. No maintainer escalation needed: this pass judges the two leaves as two Types sharing content, per the recorded seam — not one Type split by surface.
2. **vs Stored Value Wallet (§08 sibling, processed 2026-09-08) — seam confirmed from the container side.** The seam is where a payment draws from: a user-held prepaid balance inside an operator-maintained account (Stored Value) vs held external instruments supplied by the container (this Type). Hybrid products (PayPal's Balance account inside the self-described "digital wallet"; Apple Cash inside Apple Wallet) ship both structures in one product. *Remove the prepaid-balance-as-spend-source → Digital Wallet. Make the balance the spend source → Stored Value Wallet.*
3. **vs Peer-to-peer Payment Application (processed 2026-09-06) — flag DISCHARGED from this side.** P2P is an embedded capability of wallets (PayPal send/request/pool/split; Apple Cash; Tap to Transfer); the wallet core is container + management + payer-side participation. *Remove merchant/bill spending → P2P remains; remove P2P → wallet remains.* All three wallet passes now record the same keep-both resolution.
4. **vs Crypto Wallet (processed)** — same word, different asset class and custody: user-held blockchain keys with chain-anchored state vs fiat payment instruments held for rail payments. *Strip the fiat instruments and add user-held key material → Crypto Wallet; add back rail payments with issuer instruments → this Type.*
5. **vs Payment Gateway / Payment Processing Platform / Payment Orchestration Platform / Merchant Payment Platform (processed)** — payee-side acceptance infrastructure vs holder-side container. Their own passes record wallets as payer-side method types inside them. *Remove the payer's instrument home and keep acceptance → gateway/processing; remove acceptance and keep the instrument home → this Type.*
6. **vs Card Issuing Platform / Card Management System (processed)** — issuer-side credential creation/governance vs holder-side storage and presentation. Issuing's "digital wallet tokenization (Apple/Google-class provisioning)" is this Type's intake flow; the container the credential lands in is this Type. *Remove the consumer-facing container → issuing/management.*
7. **vs Digital Banking Application (§08, processed)** — a bank relationship of record (deposit accounts, digital onboarding, banking obligations) vs an instrument container that pays from instruments the user already holds elsewhere. Bank apps provision cards INTO wallets (interconnection, not identity). *Keep the bank relationship of record → banking; keep only the instrument container and payment participation → wallet.*
8. **vs Checkout Platform / E-commerce storefront (processed)** — merchant-side sale-completion flow vs payer-side instrument home. Express wallet buttons are lanes inside a checkout; the container they draw on is the wallet. *Remove the payer-side container → checkout.*
9. **vs Password Manager / credential vault** — general secret storage without payment participation, issuer verification, or payer-side standing. *Add managed payment instruments that actually pay → wallet; strip payment participation from the wallet → vault.*
10. **vs Store Credit / Stored Value Platform / Gift Card Management / Campus Card Management / Cashless Venue Platform (processed)** — merchant- or institution-scoped value programs (issued, owed, or institution-administered value, closed-loop) vs the user-owned general-purpose instrument container. *Scope the container to one merchant/institution's value → those Types; generalize → this Type.*
11. **vs Government Digital Identity / Digital Credential Platform (processed)** — identity issuance and authentication vs payment instrument holding. Both share the "wallet" container metaphor; the content differs (identity documents vs payment instruments). *Swap payment instruments for issued identity credentials → identity wallet territory.*
12. **vs Personal Finance Management Application (processed)** — PFM observes accounts held elsewhere; the wallet holds instruments it pays with. *Remove payment participation and add cross-account observation → PFM.*
13. **Historical thin shapes recorded for the §24 check**: carrier-billing one-offs (no container) and merchant card-on-file (no user-owned cross-merchant container) fall outside the Type; the long-lived account-container shape (25+ years, per the sampled operator) falls inside it with no modern capability in the core.

---

## Uncertainties

1. **Google Wallet structure** — unreachable this pass and in the sibling pass (timeouts ×3 cumulative). Anchor only; its current cards/passes/IDs scope and provisioning flow are not evidenced first-hand here. If a future pass reaches Google documentation, verify against this file's comparison table.
2. **Network-operated checkout wallets (Click to Pay category)** — both network pages unreachable (404/403). The category is retained as an anchor only; no structural claims sourced from it. The "cloud checkout wallet" pole is instead evidenced through PayPal's web account surface and Apple's non-Apple-browser handoff.
3. **Historical lineage naming** — the account-container shape's pre-smartphone history is evidenced only by the sampled operator's own "over 25 years" statement; earlier named wallet services were not researched (source unreachable) and no lineage names are asserted.
4. **Removal/deletion semantics** — whether removing an instrument from the container revokes all provisioned copies across surfaces was not directly evidenced on the reached pages; phrased generically or omitted from the final document.
5. **Wallet-value regulatory packaging** — partner-bank servicing structures are evidenced (Apple Cash/Green Dot; PayPal footnotes) but jurisdictional classifications were not researched; kept generic.
6. **Numeric limits, fees, availability windows** (card-link counts, Apple Cash family limits, Pay in 4 bounds) — present in reached copy but research-notes only; none asserted in the final document.
7. **Whether balance-wallet markets migrating to bank rails (stored-value pass observation) also thins the container structure** — not researched; the container structure persisted across all sampled products regardless of draw-from mix.

---

## Final Synthesis

The Digital Wallet is the **user's own container for payment instruments**: a persistent, user-owned, general-purpose wallet that holds the user's added cards and payment credentials, is curated by the user through add/verify/manage/remove instrument management, and participates in payments as the payer-side structure — payments draw on held instruments, supplied through the wallet, on whatever surface the user is paying from. Everything else observed — device execution, tokenization, balances, P2P, passes/IDs/keys, express buttons, rewards, crypto — is common mature structure or variant coloring, and much of it is the wallet-trio siblings' substance riding the same product: the carried-device surface is Mobile Wallet, the prepaid balance draw-from is Stored Value Wallet, the transfer core is P2P.

The directory's wallet trio resolves as three structural seams, now confirmed from all three passes: **what holds the credential** (this Type) / **where the wallet lives and the payment act happens** (Mobile Wallet) / **where the payment draws from** (Stored Value Wallet). Real products routinely combine the structures; the seams are structural, not per-product.

Leaf verdict: **keep-both ratified** with Mobile Wallet (and with Stored Value Wallet) — the counterparty records are discharged, the trio seam stands, no maintainer escalation required.

Historical check passes: the account-container wallet satisfies the three-leg core with no smartphone, no NFC, no balance, no P2P, and no tokenization in the core; merchant card-on-file and carrier-billing one-offs fail the user-owned container/participation legs and stay outside; platform-native wallets satisfy with the device surface as an added structure, not a definitional one.
