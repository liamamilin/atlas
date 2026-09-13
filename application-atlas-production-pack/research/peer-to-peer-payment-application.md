# Research Notes — Peer-to-peer Payment Application

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Peer-to-peer Payment Application actually is as an Application Type: the core objects, the transfer lifecycle, how participants are identified and addressed, where money comes from and goes, what rules govern the movement, and where the Type ends relative to Digital Wallet, Merchant Payment infrastructure, and Banking applications.

## Initial Boundary (hypothesis before research)

- Core hypothesis: the defining job is direct money movement between two identified individuals, initiated by one of them — not merchant acceptance, not account banking, not messaging.
- Nearest neighbors in DIRECTORY §08: Digital Wallet, Mobile Wallet, Stored Value Wallet, Merchant Payment Platform, Payment Gateway, Payment Processing Platform, Payment Orchestration Platform, Digital Banking Application, Mobile Banking Application.
- Expected confusions: (a) modern P2P products are usually embedded inside wallets/super-apps — is the leaf a capability rather than a Type? (b) several P2P products now accept business payments — does that collapse the boundary with merchant payment?

## Research Questions

1. What is the central object (the transfer) and what lifecycle states does it have?
2. How are participants identified and addressed (email / phone / username / QR / contacts)?
3. Where do funds come from and where do they land (linked bank account, card, stored balance, direct bank-to-bank)?
4. How do requests, splitting, and group settle-up work?
5. What rules matter: verification/KYC, limits, holds, cancellation/irrevocability, privacy, business-use restrictions?
6. What interfaces exist: standalone app, embedded in banking app, embedded in OS wallet/messaging, web, QR in person?
7. Where does the Type end: business acceptance, social feed, banking features, crypto, cross-border?

## Representative Products

| Product | Philosophy | Customer tier | Why sampled |
|---|---|---|---|
| PayPal | web-era P2P inside a broad commerce/wallet platform; email/username addressing; optional balance account | consumer + business | the original P2P service; strong docs |
| Venmo | mobile-first social P2P; feed, payment notes, per-payment privacy; balance + cards | consumer (+ SMB profiles) | the social-P2P pole |
| Zelle (evidenced via Chase, a participating bank) | bank-network P2P embedded in banking apps; no stored balance; direct bank-to-bank | bank customers | the bank-embedded pole; opposite of balance model |
| Apple Cash | platform-native P2P inside OS Wallet/Messages; stored balance at a partner bank | Apple device owners | the platform-native pole; explicit business-use prohibition |

Cash App (Block) was a fifth candidate (P2P-extended-into-banking pole) but cash.app/help returned 403 twice and was abandoned per the retry rule; no claims are made from it. Google Pay support timed out once and was not retried.

## Sources

Tier 1 (official operational documentation):
- Venmo Help Center — https://help.venmo.com/ (topic tree); article "Cancel Payment" https://help.venmo.com/cs/articles/cancel-payment-vhel148 (fetched 2026-09-06)
- Apple Support — "Set up Apple Cash" https://support.apple.com/en-us/HT207886 (fetched 2026-09-06)

Tier 2 (official product pages):
- PayPal — "Transfer money online" https://www.paypal.com/us/webapps/mpp/send-money-online (fetched 2026-09-06; includes operational FAQ: send/request steps, funding methods, balance account, QR, PayPal.Me, pools)
- Venmo — https://venmo.com/ and "Send & Receive" how-it-works https://venmo.com/send-receive/start (fetched 2026-09-06; feed, privacy settings, Groups, fees, direct deposit)
- Chase — Zelle overview/FAQ https://www.chase.com/personal/zelle (fetched 2026-09-06; enrollment, addressing, limits posture, cancellation rule, QR, no purchase protection)

Unreachable (recorded limitations):
- zellepay.com — 403 on /faq and /how-it-works (2 attempts, abandoned). Zelle evidence carried by Chase's official page (Tier 2, partner-bank framing).
- cash.app/help and cash.app/en-US/help — 403 ×2 (abandoned). Cash App excluded from evidence base.
- support.google.com Google Pay send/receive article — timeout ×1 (not retried).

## Product Observations

### PayPal (evidence layer A on the fetched page; product-page level)

Key observations:
- Send flow (official FAQ): Go to Send → enter recipient's name, PayPal username, email, or mobile number → enter amount, choose currency, add note → choose payment type and payment method → review transaction including fees → Send.
- Request flow (official FAQ): Go to Request → select person → amount + note → Review → "Request Now".
- Funding methods for domestic personal payments: linked bank account, debit card, PayPal balance, or Amex Send Account (no fee); other cards (fee — 2.90% + fixed fee per the page; precise numbers stay in these notes).
- Balance model: holding/using a balance requires a "PayPal Balance account", created when the user first receives money ("Accept the Money" → transfer to bank or keep in PayPal).
- Addressing surfaces: name/username/email/mobile search; PayPal.Me username links; shareable PayPal links via text/DM/email; QR code for in-person receive ("display your QR code for customers to scan").
- Cross-product P2P: send/receive between PayPal and Venmo accounts by searching phone number across apps.
- Group mechanics: "Pool money" (group pooling for gifts/trips) and "Split Bills" how-to.
- Cross-border: 110+ countries via the separate Xoom service (cash pickup, bank deposit, mobile wallets); Xoom has its own fees/FX and compliance review.
- Business acceptance: "Start selling" onboarding on the same send/receive page; QR framed for customers.
- Positioning: the page self-describes the app as "your do-it-all digital wallet" — P2P is one surface of a wallet platform.

### Venmo (evidence layer A on help-center article + product pages)

Key observations:
- Transfer immediacy & irrevocability (help article "Cancel Payment"): "When you send a payment on Venmo, the money will be sent to the recipient right away. There isn't a way to cancel a payment once it's sent."
- Pending states (same article): (a) recipient's phone/email unverified → sender can "take back the payment" or have the recipient verify; (b) payment still processing with the sender's bank → estimated completion date shown in app; canceling via the bank after Venmo marks it completed creates a loss the user must repay; (c) purchase/card authorizations may still be processing with the merchant.
- Wrong-recipient handling: sent to a stranger → contact support; sent to wrong friend → ask them to pay back; received from a stranger → contact support, "do not attempt to pay the stranger back on your own".
- International payments "are processed differently" (separate article).
- Social layer (product page): payments land in a feed ("the good times continue right into your feed"); custom payment notes and emojis; per-payment privacy Public / Friends / Private; "Payments will always default to the most restrictive privacy settings between payment partners".
- Groups (product page): Venmo Groups — create/invite group, add expenses as they occur, adjust each member's share, settle with Pay/Request, "we'll take care of the math".
- Funding & fees (product page FAQ): free to send from Venmo balance, linked bank account, or debit card; 3% fee when funding with a linked credit card (precise number stays in notes).
- Balance management: move money between Venmo and bank; direct deposit (account/routing numbers; early payday framing); transfers are reviewed and "may result in delays or funds being frozen or removed".
- Extensions: Venmo Debit Card (Mastercard, spend balance anywhere), Venmo Credit Card, checkout in apps/online, pay local businesses "the same way you pay your Venmo friends", gift cards, crypto buy/sell (via Paxos; not deposits, not FDIC-insured), business profiles, Stash rewards program, iMessage & Siri payments (help article listed).
- Help-center topic tree confirms the object inventory: Payments & Transfers, Wallet (banks/cards/crypto), Disputes, Business & Charity Profiles, Tax Center, Buying & Selling.

### Zelle (via Chase — evidence layer A for Chase's description of Zelle; layer B for the network model)

Key observations:
- Model: Zelle is offered inside 2,000+ U.S. banking apps; at Chase there is "no new app to download" — it lives in the Chase Mobile app and on chase.com.
- Enrollment: customer enrolls (choose primary email → accept service agreement → one-time activation code). Recipients must be enrolled at a participating bank.
- Addressing: recipient's U.S. mobile number or email; contacts sync from the phone; Zelle QR code ("send and receive money to the right person, without typing an email address or U.S. mobile number"); Zelle Tag (username-like ID, currently for small-business customers).
- Fund location: money goes directly into the recipient's bank account — "no need to use another app to cash out"; no stored balance anywhere.
- Speed: usually a few minutes when both sides enrolled; select transactions 1–3 business days (Chase's own timing table; precise timings stay in notes).
- Irrevocability: "Zelle® payments cannot be reversed." Cancellation is possible only while the payment is pending because the recipient has not yet enrolled (activity page → "Cancel This Payment").
- Limits: daily dollar send limits; Chase "dynamically determines the limit for each transaction … based on a number of factors including your recipient", with tier limits (details in Chase's service terms).
- Requests & splitting: send, request, split; splitting can start from a card/checking charge ("Split" button on account activity → Request and Split flow); future-dated and recurring payments supported.
- Protection posture: "Neither Zelle® nor Chase provide protection if you make a purchase of goods using Zelle® and then do not receive them…" — explicit no-purchase-protection stance; scam warnings ("only send money to people you know and trust").
- Scope: U.S. bank accounts only; "people and businesses you know and trust such as your personal trainer, babysitter, neighbor" — small-business payments are in scope.
- Fees: no consumer fee at Chase for send/receive/request.

### Apple Cash (evidence layer A — Apple support article)

Key observations:
- Setup: Settings → Wallet & Apple Pay → turn on Apple Cash; requires 18+, U.S. residence, compatible device, two-factor authentication, iCloud sign-in on each device. Identity verification required for full features; after verification the account is FDIC-insured (service provided by Green Dot Bank; Apple is not the bank).
- Balance model: money received "is automatically and securely kept in your Apple Cash balance"; balance visible in Wallet; add money; transfer to bank account.
- Send surfaces: send in Messages or Wallet; "Tap to Cash" — send to someone nearby without sharing phone number or email (near-field addressing).
- No fee to send, receive, or request.
- Business-use prohibition (footnote): "You can't use person-to-person payments with Apple Cash for business-related activities, like operating a business or paying employees." — explicit P2P-only scoping.
- Extensions: purchases via Apple Pay / virtual card number (Visa), pay Apple Card balance, Daily Cash from Apple Card, Apple Cash Family (under-18 accounts with their own limits).
- Limits: minimum/maximum amounts documented in a separate article; family accounts and Tap to Cash have rolling 7-day caps (precise numbers stay in notes).
- Regional: U.S. only.

## Cross-product Comparison

| Dimension | PayPal | Venmo | Zelle (Chase) | Apple Cash |
|---|---|---|---|---|
| Parties | individuals; business selling also supported | individuals; business profiles also supported | "people and businesses you know and trust" | individuals only; business use explicitly prohibited |
| Recipient addressing | name/username/email/mobile; PayPal.Me link; QR; cross-app phone search | Venmo profile/friends; phone/email | U.S. mobile or email; contacts sync; QR; Zelle Tag | Apple Account contacts in Messages/Wallet; Tap to Cash nearby |
| Where money lands | PayPal Balance account (optional) or bank | Venmo balance or bank | recipient's bank account directly (no balance) | Apple Cash balance (partner-bank stored value) |
| Funding sources | bank, debit, balance, credit card (fee) | balance, bank, debit (free); credit card (fee) | enrolled bank account | linked debit/balance |
| Send flow | recipient → amount/currency/note → payment type + method → review fees → send | in-app pay, immediate | enroll → recipient → amount → send | Messages/Wallet → amount → send |
| Request | yes (structured request flow) | yes (+ group settle-up) | yes (+ split from account activity) | yes (in Messages) |
| Irrevocability | review step before send; fees disclosed | cannot cancel once sent; pending-unverified recipient can be taken back | cannot reverse; cancel only while recipient unenrolled | security checks may delay availability |
| Social layer | none (links shared in chat) | feed + per-payment privacy + notes/emojis | none | none (Messages thread context) |
| Group mechanics | pool money; split bills | Venmo Groups (shared expense ledger + settle-up math) | split a charge | — |
| Business acceptance | yes | yes (business profiles; pay local businesses) | yes (small businesses) | prohibited |
| Verification | account + email confirm; balance account | identity verification for balance use | enrollment + activation code | identity verification → FDIC pass-through |
| Limits | yes | yes | daily send limits, dynamically determined per transaction | min/max; family caps |
| Cross-border | via separate Xoom service | "processed differently" | U.S.-only | U.S.-only |
| Platform form | standalone app + web | standalone app (+ iMessage/Siri) | embedded in banking apps + bank web | embedded in OS Wallet/Messages |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

1. **Personal account for an identified individual** — each party holds an account tied to a real person (identity may be verified to varying depth).
2. **Direct transfer between two identified individuals, initiated by one of them** — the sender names an amount and an addressable recipient; money moves from value the sender controls to value the recipient can access.
3. **Recorded transfer with a completion state** — every transfer is a durable record that moves through states (at minimum: initiated → completed, with pending/failed paths) and remains in the user's history.

Remove any of these and the Type stops being recognizable: no identified parties → anonymous cash/merchant checkout; no direct person-to-person initiation → merchant payment infrastructure; no record/completion state → physical cash.

### L1 — Common Mature Structure (very common, not defining)

- Recipient addressing layer: phone/email/username-handle/QR + device contacts sync
- Money requests, including reminders, and bill splitting / group settle-up
- Linked funding sources (bank account, debit/credit card) and/or stored balance with cash-out to bank
- Transaction history (searchable, per-participant)
- Identity verification / KYC gates and transaction limits
- Pending/hold states and wrong-recipient handling paths
- Notifications for incoming requests/payments
- Fee model that varies by funding method (standard bank/balance funding commonly free; card funding and instant transfers commonly priced)

### L2 — Variant / Optional Structure

- Social layer: shared feed of payments, per-payment privacy settings, notes/emojis (Venmo pole; absent in the other three)
- Balance model: stored balance vs direct bank-to-bank with no balance (Zelle pole)
- Platform embedding: standalone app vs embedded in banking apps vs embedded in OS wallet/messaging
- Business acceptance: business profiles / small-business payments (present in three of four; explicitly prohibited in one)
- Protection posture for commercial payments: payment-type distinction with buyer protection vs explicit no-purchase-protection stance
- Cross-border: excluded vs delegated to a separate remittance service
- Banking extensions: direct deposit/paycheck, issued debit card, early-payday framing
- Regional super-app embedding (QR-centric P2P inside messaging/super-apps) — market-known, not directly evidenced in this sample

### L3 — Vendor-specific (research notes only)

- Venmo: Groups mechanics, Stash rewards, gift cards, iMessage/Siri payments, 3% credit-card funding fee, crypto via Paxos
- PayPal: PayPal.Me links, PayPal links, pool money, Amex Send Account, Xoom (110+ countries), 2.90%+fixed card fee, PayPal–Venmo cross-app P2P
- Zelle: tier-based dynamically determined daily limits, Zelle Tags, Chase's per-recipient tier display
- Apple Cash: Tap to Cash, Apple Cash Family ($2,000 rolling 7-day caps), Daily Cash, Green Dot Bank issuance, virtual Visa card number

## Rejected Findings

- "Phone number is the identity" — rejected. PayPal addresses by email/username; Apple Cash by Apple Account; Zelle by email or mobile. The invariant is an addressable personal identifier, not the phone.
- "Stored balance is the core" — rejected. Zelle moves money bank-to-bank with no balance; balance is one implementation of where value sits.
- "Social feed is part of the Type" — rejected. Only one of four sampled products has it; it is a product philosophy (variant), not structure.
- "P2P apps are banks" — rejected. Balance/direct-deposit/card features are extensions; no sampled product centers a bank-account relationship (Apple Cash's FDIC insurance is pass-through via a partner bank; Venmo states it is not a bank).
- "Instant completion is definitional" — rejected. Zelle documents multi-day paths for some transactions; pending states exist everywhere. Speed is a competitive property, not structure.

## Boundary Findings

- **vs Digital Wallet / Mobile Wallet**: wallets center on paying merchants with stored credentials/value; P2P centers on person↔person transfer. In the current market P2P is usually embedded inside a wallet product (PayPal self-describes as a digital wallet; Apple Cash lives inside Apple Wallet). Structural test: remove merchant payment → the P2P job remains; remove P2P → the wallet remains. The two leaves are related Types that frequently ship as one product; this leaf documents the person-to-person money-movement job.
- **vs Merchant Payment Platform / Payment Gateway / Payment Processing Platform**: those are merchant-side acceptance and settlement infrastructure (underwriting, merchant accounts, acquiring). Here both parties are natural persons; even when small businesses are paid (Zelle, Venmo business profiles), the flow keeps personal-account semantics rather than merchant acquiring.
- **vs Stored Value Wallet**: stored value is one funding implementation (Zelle has none). Not the boundary of this Type.
- **vs Digital Banking Application / Mobile Banking Application**: banking centers on a bank-account relationship (deposits, statements, branch/credit services). P2P centers on transfers between people; Zelle is literally a feature inside banking apps but its object model is the transfer, not the account. Gradient where P2P apps add direct deposit/cards.
- **vs remittance / cross-border transfer (no dedicated leaf)**: cross-border movement with FX and cash-out networks is a distinct job; sampled products either exclude it (Zelle, Apple Cash: U.S.-only) or delegate to a separate service (PayPal → Xoom).
- **vs Cryptocurrency Exchange**: crypto buy/sell inside Venmo/PayPal is an adjacent asset-trading capability, not P2P money movement.
- **"去掉什么就变成另一个 Type" 判据**: remove the person-to-person direction (recipient becomes a merchant with acquiring semantics) → Merchant Payment infrastructure; remove the money movement (keep the conversation) → messaging; remove the identified individuals → anonymous/cash-like instruments; remove the transfer record → not a financial application.

## Uncertainties

- Cash App unreachable (403 ×2): the "P2P extended into full banking/bitcoin" pole is under-evidenced; no claims made from it. If later processed, expect the same core with heavier banking extensions (L2).
- zellepay.com unreachable: network-level claims rest on Chase's official description (partner-bank Tier 2). Zelle's own consumer FAQ might differ in detail; no network-level operational numbers asserted.
- Venmo help center is a JS app: only some articles rendered; send/request UI mechanics asserted at structure level, not button level.
- Exact fees, limits, and timings are vendor-specific and change over time; deliberately excluded from the final document (cross-product qualitative statement only: funding-method-dependent fees).
- Regional super-app P2P (WeChat Pay/Alipay QR model) not directly evidenced in this sample; treated as a known variant posture with no structural claims.

## Final Synthesis

A Peer-to-peer Payment Application is an application through which **individuals send money directly to other individuals**: each party holds a personal account tied to an identified person; the sender addresses the recipient through a personal identifier (phone, email, username/handle, QR, or contacts), names an amount, and the application executes a recorded transfer from value the sender controls to value the recipient can access, tracking it through a completion state and keeping it in a persistent history.

Everything else commonly associated with the category — requests and splitting, stored balances, social feeds, business profiles, cards, direct deposit, cross-border delegation — is mature market structure layered on that core, varying by product philosophy: standalone balance apps (PayPal, Venmo), bank-network embedded services (Zelle), and platform-native wallet payments (Apple Cash).
