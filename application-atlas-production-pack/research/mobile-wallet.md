# Research Notes — Mobile Wallet

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)
Directory leaf: `Mobile Wallet` (§08 Finance, Banking, Insurance & Investment; sibling of Digital Wallet, Stored Value Wallet)
Slug: `mobile-wallet`

---

## Research Goal

Establish what a Mobile Wallet is as an Application Type: what lives inside it, what the user does with it, how a payment actually executes, which rules and lifecycle shape it, and — the central question this leaf inherits — whether it is a distinct Application Type at all or merely a form-factor naming of the wallet family. The stored-value-wallet pass (processed earlier the same day) explicitly flagged this leaf with the expectation of a "form-factor Variant judgment"; this pass must resolve that flag.

---

## Initial Boundary

Working hypothesis at start:

- Candidate core: a payment wallet whose home is the user's carried mobile device — the phone (or a paired wearable) holds the payment resources and is itself the surface on which payment is executed and verified.
- Nearest neighbors: Digital Wallet (unprocessed sibling — credential container), Stored Value Wallet (processed — prepaid balance account), Mobile POS (processed — the acceptance-side mirror), Peer-to-peer Payment Application (processed — transfer core embedded in wallets), Mobile Banking Application (deposit relationship), Crypto Wallet (processed — naming conflation), plus the pass/closed-loop neighbors (Event Ticketing, Campus Card, Cashless Venue).
- Prior-art constraints inside this production pack:
  - `research/stored-value-wallet.md` §Boundary Findings #2: "'mobile wallet' names the form factor, not a different value structure… Likely a form-factor Variant judgment for its own pass. *Remove the device emphasis → same structure.*" — and the wallet-trio seam: where a payment draws from (balance vs credential container vs mobile form factor).
  - `mobile-pos` (processed 2026-09-08): the ratified precedent for the structurally identical question — Mobile POS vs Retail POS resolved as **surface-defined sibling Types** (POS spine inherited; portability load-bearing; mobile-native products exist where the portable device is the entire product; named market category with vendor-articulated definitions).
  - `card-issuing-platform` (processed): "digital wallet tokenization (Apple/Google-class provisioning)" recorded as an issuer-side standard capability — i.e., the holder-side credential store those platforms provision into is exactly this Type's territory.
  - `research/corporate-card-spend-platform.md`: wallet receipts show wallet device numbers instead of card numbers — independent corroboration of device-identity-as-credential.
  - `peer-to-peer-payment-application` (processed): P2P is an embedded wallet capability; keep-both ratified.
  - `crypto-wallet` (processed): "wallet" naming conflation warning (keys vs fiat containers).
- Known unknowns at start: whether device-hosted credential storage (tokenization) is definitional or just the dominant implementation; whether proximity presentation (NFC tap) is definitional or a substrate variant; how mobile-money (line-identity, USSD) wallets fit; whether a balance inside the wallet belongs to this Type or to the Stored Value seam.

---

## Research Questions

1. What is the wallet's home surface — where does it live, and what does the vendor say about that?
2. What does the wallet hold — card credentials, value, passes, other credentials?
3. How does a payment execute — who is contacted, what is presented, what verifies the user?
4. How do resources enter the wallet (provisioning/linking/loading), and what gates them?
5. What lifecycle binds wallet contents to the device (per-device storage, transfer, suspension)?
6. What surfaces does the user actually face (wallet home, payment sheet, terminal presentation, history)?
7. How do the OS-native / OEM / fintech-app / mobile-money shapes differ structurally?
8. Remove-tests against every neighbor; and the leaf-defining question: is the mobile surface load-bearing enough for a distinct Type?

---

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different tiers/substrates:

| Product | Shape | Philosophy / position | Why sampled |
|---|---|---|---|
| Apple Pay / Apple Wallet | OS-native device wallet | credential container embedded in the device platform; tokenized cards; passes alongside | paradigm device-hosted wallet; strongest operational documentation reached |
| Samsung Wallet | OEM wallet on Galaxy | wallet + passes + IDs + keys + passwords in one app; watch companion | second OS-family pole; vendor-explicit on-device storage; broad credential scope |
| PayPal (mobile app) | fintech account-container wallet | account with linked instruments + optional balance; app as mobile surface; cross-surface | the account-container pole; FAQ directly addresses "mobile wallet" naming; hybrid case |
| M-PESA (Safaricom) | mobile money, line-identity | wallet bound to the phone line; USSD/SIM-toolkit channels; no smartphone required | the original "mobile wallet" market; non-smartphone channel variant; historical check anchor |
| Google Wallet / Google Pay | OS-native device wallet (Android) | cards, passes, IDs on Android | market anchor only — official pages unreachable this pass (2 timeouts) |

---

## Sources

Reached (official, Tier 2 product pages):

- Apple — Apple Pay overview: `https://www.apple.com/apple-pay/` (setup: Wallet app + card add by tapping card to iPhone back or manual entry + issuer verification; "built into iPhone, Apple Watch, Mac, iPad, and Apple Vision Pro"; in-store contactless acceptance; in-app/online Apple Pay button incl. QR-code handoff to iPhone on non-Apple browsers; "device-specific number and unique transaction code… actual card number isn't shared… not stored on Apple servers"; "Every purchase requires Face ID, Touch ID, or a passcode"; card transfer "to the new device in one easy step"; Apple Cash as a "digital card in Wallet" spendable with Apple Pay, sendable in Messages and via Tap to Cash; connected-card balance view in Wallet; no Apple fees; "Any card used in Apple Pay is offered by the card issuer"; Tap to Pay on iPhone acceptance side; Wallet "Carry one thing. Everything."). Fetched 2026-09-08.
- Samsung — Samsung Wallet product page: `https://www.samsung.com/us/apps/samsung-wallet/` ("A smart wallet is already in your Galaxy"; store credit/debit cards, loyalty/membership, boarding passes, digital IDs (Student ID, Driver's License, Company ID), digital car/home keys, passwords (Samsung Pass); add card by camera capture or tapping card to back of phone, authenticate with bank; "swipe up on your phone or Galaxy Watch, verify and tap"; "Wallet is protected by Samsung Knox… on-device data storage and encryption of your debit or credit cards"; cards usable on Galaxy Watch; Tap to Transfer to another user's debit card or smartphone; installment payments via third party). Fetched 2026-09-08.
- PayPal — Digital Wallet / app page: `https://www.paypal.com/us/digital-wallet` (FAQ: "What is a mobile wallet app, and is PayPal a digital wallet?"; link bank account/credit/debit cards; optional PayPal Balance account — "required to hold and use a balance"; pay online, in-store, in app; biometrics and passkeys secure the account; send/request/pool/split; crypto, Savings, PayPal Debit Card; card-link limits in FAQ copy). Fetched 2026-09-08.
- Safaricom — M-PESA services hub: `https://www.safaricom.co.ke/personal/m-pesa` (deposit/send/withdraw/request; Hakikisha recipient confirmation; reversal; Register For M-PESA; Check Balance / Change / Unlock / Reset PIN; M-PESA Statement; Consumer Tariffs & Limits; channels: M-PESA Super App + Mini Apps, USSD *334#, SIM Toolkit, MySafaricom App; Lipa na M-PESA — Paybill / Pochi la Biashara / Pay Online; M-PESA Global incl. Western Union / PayPal / Alipay / GlobalPay Card; credit & savings adjacencies M-Shwari, Fuliza, Halal Pesa; wealth MALI, Ziidi). Fetched 2026-09-08 (same hub as the stored-value-wallet pass earlier today; re-read for channel and device-line evidence).

Not reached (abandoned per network rule after 1–2 failures):

- Google Wallet: `https://wallet.google.com/` (timeout), `https://pay.google.com/intl/en_us/about/` (timeout). Google properties retained as market anchor only; no operational claims sourced from them this pass.
- (Carried over from sibling pass, same-day: PayPal legal hub 404, GCash help 403, Venmo 406 — consistent with the wallet-family sourcing situation.)

Consequence: claims below are calibrated to the four reached pages plus cross-pack corroboration; no precise numeric limits, no security-architecture internals (secure-element names, token-scheme names), no market-share figures are asserted anywhere.

Cross-pack corroboration (no new fetch needed):

- `applications/mobile-pos.md` / `research/mobile-pos.md` — acceptance-side mirror; contactless wallets as tender.
- `research/card-issuing-platform.md` — issuer-side provisioning into Apple/Google-class wallets.
- `research/corporate-card-spend-platform.md` — wallet device numbers on receipts instead of card numbers.
- `applications/event-ticketing-platform.md` — mobile-wallet passes as ticket credential implementation.
- `applications/cashless-venue-platform.md` — phone/mobile-wallet as credential generation for venue payments.
- `research/stored-value-wallet.md` — balance-carrying wallet structures (PayPal Balance; M-PESA balance motions).

---

## Product Observations

### Apple Pay / Apple Wallet — Evidence layer A

- **The wallet is part of the device platform.** "Apple Pay is built into iPhone, Apple Watch, Mac, iPad, and Apple Vision Pro." Setup begins in the Wallet app: tap the plus, add a card by tapping the card to the back of the iPhone (or manual entry), then "verify your information with your bank or card issuer."
- **Credential is device-specific, not the card.** "When you make a purchase, Apple Pay uses a device-specific number and unique transaction code. So your actual card number isn't shared by Apple with merchants or stored on Apple servers." (Cross-pack: corporate-card spend research independently records wallet device numbers on receipts.)
- **Every purchase is verified on the device.** "Every purchase requires Face ID, Touch ID, or a passcode."
- **Payment execution is a device act.** In store: "just double-click, tap" — a device gesture plus a contactless terminal ("works anywhere that takes contactless payments… vending machines and grocery stores to taxis and subway stations"). Online/in apps: the Apple Pay button with "a touch or glance"; on non-Apple browsers, "scan the Apple Pay code with your iPhone camera and use your iPhone to complete your purchase" — the phone completes the payment act even when the checkout surface is another computer.
- **Device-bound lifecycle.** Cards can be added to multiple devices at once; "if you upgrade your iPhone, you can transfer your cards to the new device in one easy step" — contents are managed per device, not per account login.
- **A balance can live inside the wallet container.** Apple Cash is "a digital card in Wallet" — money sent/received in Messages, spendable "with Apple Pay — in stores, in apps, and online"; Tap to Cash sends by holding two iPhones near each other. The container can carry instrument credentials AND wallet value without changing its nature.
- **Instrument-linked information.** Users can connect an eligible card account and "view your card balance right in Wallet."
- **Issuer relationship preserved.** "Any card used in Apple Pay is offered by the card issuer"; Apple charges no fees and is not a bank — the wallet is a holder-side surface over issuer instruments.
- **Acceptance-side mirror exists as a separate product surface.** "With Tap to Pay on iPhone, you can use an iPhone to accept contactless payments" — the seller-side twin (Mobile POS territory).
- **Wallet as carry-all.** The Wallet app ("Carry one thing. Everything.") holds cards and other passes — the container extends beyond payment.

### Samsung Wallet — Evidence layer A

- **OEM-embedded wallet.** "A smart wallet is already in your Galaxy" — the wallet ships with the device platform, opened by a swipe-up gesture or app icon.
- **Broad credential scope in one container:** debit/credit cards, loyalty and membership cards, boarding passes ("Add to Samsung Wallet" buttons from airline apps), digital IDs (Student ID, Driver's License, Company ID), digital car/home keys (NFC/UWB), and passwords (Samsung Pass).
- **Provisioning with issuer gate.** "Capture your card's information either with the camera or by tapping it to the back of the phone, then follow the steps to authenticate with your bank."
- **On-device credential storage, vendor-explicit.** "Wallet is protected by Samsung Knox, adding an extra layer of security with on-device data storage and encryption of your debit or credit cards."
- **Payment execution on the device.** "Just swipe up on your phone or Galaxy Watch5, verify and tap" — gesture, device verification (fingerprint or PIN), contactless tap. Watch as companion carrier of the same wallet.
- **P2P on the wallet.** Tap to Transfer: "send funds to another user's debit card or smartphone, regardless of their wallet or operating system."
- **Credit riding on rails.** Installment payments offered inside the wallet via a third-party provider — financing is an add-on, not wallet structure.

### PayPal (mobile app) — Evidence layer A

- **Self-description pairs the terms.** FAQ: "What is a mobile wallet app, and is PayPal a digital wallet? PayPal is an online payment system… You can link your bank account, credit card, or debit card. You can also have a balance in your PayPal account." — an account-based container whose app is the mobile surface.
- **The container is the account, not the device.** Instruments (linked cards/banks) and the optional PayPal Balance account ("required to hold and use a balance") live server-side; the app presents them. Numeric card-link limits appear in FAQ copy (research-note detail only).
- **Device-bound verification still governs the act.** "Biometrics and passkeys secure your account before you buy" — the carried device authenticates the user even though the credential store is the account.
- **Payment surfaces: online, in-store, in the app.** Pay-later options (Pay in 4 / Pay Monthly) ride on top; single-use in-store card mechanics appear in loan footnotes (detail only).
- **The wallet family overlaps in one product.** P2P send/request/pool/split, crypto, Savings, PayPal Debit Card — consistent with the P2P pass's "P2P embedded inside a wallet product" finding and the stored-value pass's hybrid observation (one product carrying credential-container + balance structures).

### M-PESA (Safaricom) — Evidence layer A (mobile-money pole)

- **The wallet is bound to the phone line.** "Register For M-PESA" registers the Safaricom line; the wallet's identity substrate is the phone number/line, and the PIN lives with the user's use of the device. Channels explicitly include non-smartphone surfaces: "M-PESA Super App and Mini Apps, USSD *334#, SIM Toolkit, MySafaricom App."
- **Payment execution happens on the user's device** (USSD menu, SIM toolkit, or app) — deposit at agent, send money, withdraw, pay Paybill/Till, pay online, bank transfers; balance check, PIN management, statement, published tariffs & limits, reversal, Hakikisha recipient-name confirmation.
- **Balance-centric** (the stored-value structure), but its *mobile* nature is line-identity + device-as-terminal — the same carried-device logic as app wallets, one substrate generation earlier.
- Adjacencies (not wallet structure): M-Shwari savings/loans, Fuliza overdraft, M-PESA Global remittance interop, GlobalPay Card, wealth products.

### Google Wallet / Google Pay — Evidence layer C (anchor only)

- Official pages unreachable this pass (two timeouts). Retained as the Android-side OS-native wallet anchor (cards, passes, IDs) — consistent with the card-issuing pass's "Apple/Google-class provisioning" language — but no operational claims are sourced from it here.

---

## Cross-product Comparison

| Dimension | Apple Pay/Wallet | Samsung Wallet | PayPal app | M-PESA | Google Wallet |
|---|---|---|---|---|---|
| Wallet home | device platform (iPhone/Watch/Mac/iPad/Vision Pro) | device platform (Galaxy phone/Watch) | mobile app over a web account | phone line (USSD/SIM toolkit/app) | Android device (anchor) |
| What it holds | tokenized card credentials; Apple Cash digital card; passes | card credentials; loyalty/membership; passes; IDs; keys; passwords | linked instruments + optional Balance account; crypto | prepaid balance (value) | cards + passes + IDs (anchor) |
| Credential storage | device-specific number; not the card number | on-device storage/encryption (Knox) | account server-side; device authenticates | line-identity + PIN | (anchor) |
| User verification | Face ID/Touch ID/passcode per purchase | fingerprint/PIN per payment | biometrics/passkeys | PIN on device menus | (anchor) |
| In-store execution | contactless tap after device gesture | tap after swipe-up + verify | in-store (mechanics vary; not detailed here) | Paybill/Till numbers; QR-era additions | (anchor) |
| Online/in-app execution | Apple Pay button; QR handoff to iPhone | (app-centric; SDK buttons) | express checkout in app/web | Pay Online (paybill rails) | (anchor) |
| Provisioning gate | issuer verification | bank authentication | account verification tier | line registration (+ SIM registration regime) | (anchor) |
| Device lifecycle | per-device add; transfer to new device in one step | per-device; watch companion | account persists across devices; passkeys device-bound | line-bound; SIM swap replaces device identity | (anchor) |
| P2P inside wallet | Apple Cash (Messages, Tap to Cash) | Tap to Transfer | send/request/pool/split | Send Money / Request Money | (anchor) |
| Value inside wallet | Apple Cash (a balance-shaped value class) | — | PayPal Balance | the wallet IS a balance | (anchor) |
| Passes container | yes ("Carry one thing. Everything.") | yes (boarding passes, IDs, keys) | — (tickets etc. appear as transactions, not passes) | — | yes (anchor) |
| Operator posture | device platform; "not a bank"; issuer offers the card | device OEM; Knox platform security | fintech (not a bank); balance account structure | telco mobile money | device platform |

Reading: every sampled product is a **holder-side payment wallet whose home and execution surface is the user's carried device or device-line**, with the user verified **on that device** at the moment of payment. Everything else varies: what is held (instrument credentials vs value vs both), how the credential is stored (device-hosted token vs account session vs line identity), which acceptance substrate is native (NFC tap vs QR/paybill vs express-checkout buttons), and whether passes/IDs ride the same container. No single substrate (NFC, app, smartphone) is universal — but the carried device/line is.

---

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Removing any one stops the product being a Mobile Wallet:

1. **The wallet as the holder's payment container** (the wallet-family spine, inherited): it holds the user's payment resources — instrument credentials (cards) and/or wallet value — attached through provisioning/linking/loading, and pays from them at the moment of exchange. *Remove → a device authenticating to nothing; not a wallet.*
2. **The carried device as the wallet's home**: the wallet lives on (or is bound to) the user's personal carried mobile device — the phone itself, or a wearable paired to it; for line-identity variants, the phone line. The user carries it in daily life, so it is present at the moment of payment. *Remove → a wallet accessed from fixed or arbitrary surfaces (web checkout account, cloud wallet) = Digital Wallet territory; or a physical card.*
3. **The device as the point of payment execution**: the payment act is performed on the device — presenting it to a contactless terminal, displaying or scanning a code, dialing the payment menu, or authorizing checkout on the device — and the act is guarded by device-bound user verification (device PIN/biometric). What the payment exposes is the device identity (device-specific number/transaction code), not the raw instrument. *Remove → payment executed elsewhere and merely funded by the wallet (wallet-as-funding-source residue, e.g., a saved payment method in a desktop checkout).*

Jointly-held is load-bearing:

- 2+3 without 1 = a phone with no payment resources — any authenticated app.
- 1+3 without 2 = a wallet that pays from other surfaces — the Digital Wallet / account-container shape.
- 1+2 without 3 = a wallet app that never executes payment on the device — funding-source-only, below the Type.
- 3 without 1+2 = a contactless card presented at a terminal — a card, not a wallet.

Historical/market-sample check passes at this level: Osaifu-Keitai-class mobile FeliCa wallets (mid-2000s Japan, pre-app-store phones) satisfy — wallet on the carried phone, device-hosted credential, tap execution; M-PESA-era mobile money (USSD/SIM toolkit, no smartphone, no NFC, no app) satisfies via line-identity + device-as-terminal + draw-down; early SMS carrier-billing for one-off purchases does not (no held payment resources, no wallet container) and is correctly outside. No NFC, no app store, no smartphone, no biometric is required by the core.

### L1 — Common Mature Structure (expected in mature products, not definitional)

- Instrument provisioning flows: capture card (camera / tap-card-to-phone) → issuer/bank verification → credential ready to pay.
- Device-specific credentialing for network cards (tokenization): the wallet presents a device-specific number/transaction code; the raw card number is not what merchants receive. (Dominant implementation in OS/OEM wallets; vendor-explicit on both Apple and Samsung pages; corroborated cross-pack by wallet device numbers on receipts.)
- Device-bound verification on every payment (Face ID/fingerprint/PIN/passkey class).
- Per-device lifecycle: add/remove per device, transfer to a replacement device, watch/wearable companions.
- Transaction history and (where applicable) balance views inside the wallet.
- In-app/online express-checkout buttons (wallet as one-tap payment on the web).
- P2P send/request riding the same wallet.
- The passes container: boarding passes, tickets, loyalty/membership cards, IDs, keys riding beside payment cards.
- No-wallet-fee consumer posture (where the wallet operator is not the value mover).

### L2 — Variant / Optional Structure

- **What the wallet holds**: pure credential container (OS wallets) vs value-carrying wallet (balance inside the container) vs line-identity balance wallet (mobile money). The balance axis belongs to the Stored Value Wallet seam when it is the defining structure; here it is a container content variant.
- **Acceptance substrate**: NFC contactless tap vs QR present/scan vs merchant-code/paybill rails vs on-device express checkout vs USSD/agent-assisted.
- **Wallet operator**: device platform (OS-native), device OEM, fintech app, telco (mobile money), or bank app provisioning cards into the device wallet.
- **Device family**: phone-first with wearable companion; watch/PC/vision surfaces as extensions of one wallet.
- **Regional channel shapes**: no-smartphone wallets (SIM toolkit/USSD) where the line is the wallet.
- **Financing/credit riding the wallet** (installments, pay-later) as add-on services.
- **Cross-border/remittance interop** (mobile money global sends).

### L3 — Vendor-specific (research notes only)

- Apple: Apple Cash as a "digital card in Wallet" with Tap to Cash (hold two iPhones near); connected-card balance view; Wallet "Carry one thing. Everything." positioning; Tap to Pay on iPhone (acceptance side); QR handoff from non-Apple browsers; no-fee statement; Apple Payments Services/Green Dot/Goldman Sachs service structure.
- Samsung: Knox on-device storage/encryption claim; Samsung Pass passwords in the wallet; UWB/NFC car keys; Tap to Transfer (cross-wallet send to debit card or smartphone); Splitit-powered installments; watch card companion.
- PayPal: FAQ card-link limits (4 unverified / 24 verified); Balance account requirement footnotes; Pay in 4 / Pay Monthly lender structures; single-use in-store card mechanics in loan footnotes; crypto/Savings modules.
- M-PESA: Hakikisha, M-PESA Reversal, Pochi la Biashara, Fuliza, M-Shwari, GlobalPay Card, Tuma Popote; USSD *334#; tariff publications.
- (Google Wallet specifics unreachable this pass — none recorded.)

---

## Rejected Findings (considered, rejected as core)

- **NFC tap as the defining interaction** — QR-first and paybill-rail wallets (M-PESA) and express-checkout-only wallets satisfy the Type without tap. → L2 substrate.
- **Smartphone app as required** — SIM-toolkit/USSD mobile money runs without one. → carried device/line abstraction; app is one substrate.
- **Device-hosted tokenization as definitional** — the PayPal app pays from an account store, not a device-hosted token; M-PESA's credential is the line. Tokenization is the dominant implementation for network cards in OS wallets, not the invariant. The invariant is that *what the payment exposes is device/line identity, not the raw instrument*, wherever the store physically sits. → L1 implementation; L0 keeps the exposure principle.
- **Biometric verification as definitional** — PIN-based USSD wallets qualify. → device-bound verification abstraction, method is a variant.
- **Balance inside the wallet as definitional** — OS wallets hold no balance. Balance-carrying products straddle into the Stored Value seam. → L2 content variant; boundary documented.
- **Passes/IDs/keys as definitional** — companion credentials riding the container; several sampled wallets lack them (PayPal, M-PESA). → L1/L2.
- **Issuer-bank card instruments as definitional** — mobile money draws on balances, not cards. → L2 content variant.
- **"Any wallet app that is on a phone" as the Type** — would collapse the Type into Digital Wallet and make the surface non-load-bearing; rejected because the execution-surface property (device executes and verifies the payment; device identity is what the transaction exposes) is the part that does real work. The stored-value pass's "remove the device emphasis → same structure" test is answered: removing the device emphasis removes the execution surface, which is not the same structure but the account-container structure.
- **Market-share/adoption claims as structure** — none asserted; not evidence of Type structure.

---

## Boundary Findings

Each boundary carries a remove-test (what to strip so the remainder is the other Type).

1. **vs Digital Wallet (§08 sibling, unprocessed — counterparty record for that pass)** — the container shape: Digital Wallet is the holder-side credential/value container reachable from any surface (web checkout accounts, cloud wallets), where the payment act happens wherever the checkout happens. Mobile Wallet is the wallet whose *home is the carried device and whose payment act is executed and verified on the device*. *Remove the carried-device home/execution → Digital Wallet. Add them → Mobile Wallet.* Hybrid products (PayPal app vs PayPal web checkout; Apple Pay has no non-device home) show the seam is structural, not per-product — same stance as the stored-value pass. This pass keeps both Types, mirroring the ratified mobile-pos/retail-pos resolution for the structurally identical question on the seller side.
2. **vs Stored Value Wallet (processed)** — the seam is where a payment draws from: user-held prepaid balance inside an operator-maintained account (Stored Value) vs the carried-device execution surface over held resources (Mobile Wallet). Balance-carrying mobile wallets (Apple Cash, PayPal Balance, M-PESA) ship both structures in one product; the boundary is structural. *Remove the device/line execution surface → the balance account remains (Stored Value); remove the balance leg → the device wallet remains.* This pass **discharges the stored-value pass's flag**: resolved as keep-both, surface-defined sibling — not a pure form-factor alias — on three grounds: (a) mobile-native products exist where the carried device is the entire wallet (OS wallets; Osaifu-Keitai-class; USSD mobile money); (b) the surface carries structural machinery (device-bound provisioning, device-identity exposure, per-device lifecycle, device-bound verification); (c) "mobile wallet" is a named market category with vendor-articulated definitions (PayPal's own FAQ pairs "mobile wallet app" and "digital wallet").
3. **vs Mobile POS (processed)** — mirror symmetry: the seller's carried acceptance surface vs the payer's carried payment surface. The same device can host both (Tap to Pay on iPhone accepts what Apple Pay presents; Samsung's Tap to Transfer moves money wallet-to-device). *Remove the payer side → Mobile POS; remove the acceptance side → Mobile Wallet.* Consistent with the mobile-pos pass's boundary treatment.
4. **vs Peer-to-peer Payment Application (processed)** — P2P is an embedded capability of wallets (Apple Cash, Tap to Transfer, PayPal send/request, M-PESA Send Money); the wallet core is held resources + execution surface. *Remove P2P → wallet remains; remove merchant/bill spending → P2P remains.* Re-confirms the ratified resolution from this side.
5. **vs Mobile Banking Application (§08 sibling)** — a bank app manages a deposit relationship (statements, transfers between accounts, banking products); a mobile wallet holds and spends payment resources at the point of exchange. Bank apps commonly provision cards INTO device wallets (issuer-side evidence in the card-issuing pass) — the device wallet is the credential holder at payment time. *Remove the deposit-relationship management and keep the point-of-exchange execution → Mobile Wallet; keep account/product servicing → banking.*
6. **vs Card Issuing Platform / Card Management System (processed)** — issuer-side credential creation and program machinery vs holder-side storage and presentation. Their tokenization capability ("Apple/Google-class provisioning") is this Type's intake flow. *Remove the consumer surface → issuing/management platforms.*
7. **vs Crypto Wallet (processed)** — same word, different asset class and custody: user-held blockchain keys vs device-hosted payment credentials/value. *Strip the fiat payment resources and add user-held key material → Crypto Wallet.*
8. **vs Event Ticketing Platform / Loyalty surfaces** — passes stored in the wallet are credentials issued by other systems' records; the wallet is the carrying surface, not the issuing system of record. *Remove pass storage → still a payment wallet; remove payment resources → a pass container is a capability, not this Type.*
9. **vs Campus Card Management / Cashless Venue Platform (processed)** — institution/venue-scoped closed loops with privilege layers and operator funding; the general-purpose carried wallet is the consumer-owned remainder. *Remove the institutional scoping → a (closed- or open-loop) mobile wallet.*
10. **Carrier-billing / one-off SMS payments** — historical thin shape: no held payment resources, no wallet container; correctly outside the Type (recorded for the historical check).

---

## Uncertainties

1. **Google Wallet** — official pages unreachable (2 timeouts); anchor only. Its exact current structure (cards/passes/IDs scope, provisioning flow) is not evidenced this pass; no claims sourced from it.
2. **Apple security architecture internals** — the vendor page says "device-specific number and unique transaction code"; deeper internals (secure element naming, token-scheme names) were not researched and are not asserted.
3. **PayPal in-store payment mechanics** — vary by market/platform (QR, cards, single-use instruments in loan footnotes); not asserted in detail; the account-container reading of the app is what the reached page supports.
4. **Samsung Pay legacy MST technology** — not mentioned on the reached current page; treated as unverified history, not used anywhere.
5. **Whether the unprocessed Digital Wallet pass will accept the surface-based seam** — flagged for joint review; this pass takes the surface-defined position and records it as the counterparty record.
6. **Numeric limits, fees, availability windows** (card-link counts, Apple Cash family limits, M-PESA tariffs) — present in reached copy but kept in research notes only; none asserted in the final document.
7. **Wealth/banking-adjacent modules** (Savings, installments, M-Shwari class) — recorded as adjacencies; their regulatory packaging varies and was not researched.

---

## Final Synthesis

The Mobile Wallet is the **consumer's payment wallet carried on the person**: the defining structure is the wallet spine (holds payment resources — instrument credentials and/or value — and pays from them) realized as a carried mobile device, with the device as the wallet's home and the payment act executed and verified on the device, exposing device identity rather than the raw instrument. Everything else observed — tokenization internals, NFC vs QR substrates, passes/IDs/keys containers, P2P, express-checkout buttons, watch companions, installments, remittance interop — is common mature structure or variant coloring.

The wallet trio in the directory now resolves as three structural seams, consistent across all three passes: **where the payment draws from** (user-held balance = Stored Value Wallet), **what holds the credential** (an account container reachable from any surface = Digital Wallet), and **where the wallet lives and the payment act happens** (the carried device = Mobile Wallet). Products routinely carry several structures at once (PayPal: account container + balance + mobile surface; Apple Pay: device container + Apple Cash balance; M-PESA: line-identity device wallet + balance). The seams are structural, not per-product.

Leaf verdict: **keep-both ratified as a surface-defined sibling Type** — the direct consumer-side parallel of the ratified mobile-pos/retail-pos resolution — with the variant-question explicitly recorded for the digital-wallet pass to counterparty-review.

Historical check passes: mid-2000s mobile-FeliCa phone wallets and USSD/SIM-toolkit mobile money satisfy the three-leg core with no smartphone app, no NFC, no biometric, and no app store; carrier-billing one-offs fail the container leg and stay outside; physical cards fail the wallet-container leg and stay outside.
