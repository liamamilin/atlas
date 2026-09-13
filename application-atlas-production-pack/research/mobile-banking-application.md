# Research Notes — Mobile Banking Application

## Research Goal

Understand **Mobile Banking Application** as an Application Type: the bank-operated, installed-app servicing surface through which an existing consumer customer services their banking relationship from a personal mobile device. Establish the defining core, the standard capability set, and the boundary against the sibling consumer-banking leaves in DIRECTORY.md §08 — especially **online-banking-portal** (same servicing core, browser surface) and **digital-banking-application** (complete digitally-conducted relationship) — plus business-banking-portal, wallet/P2P/PFM, core banking system.

This pass carries the **decisive third side of the two-sided joint review** pre-hung by the digital-banking-application pass (2026-09-08) and contributed to by the online-banking-portal pass (2026-09-08): the consumer-surface trio (online-banking-portal / mobile-banking-application / digital-banking-application) overlaps almost totally on daily servicing; the portal pass recorded the seams as (a) the delivery surface itself and (b) capability distribution, and asked this pass to either **ratify keep-both-as-two-surface-leaves** or **recommend consolidation into one servicing Type with surface variants**.

## Initial Boundary (working hypothesis before research)

- Core use: an existing bank customer opens the bank's installed app on a phone/tablet to view accounts, move money, deposit checks, manage cards, and administer details — without bank staff.
- Users: retail/consumer banking customers; bank staff are not primary users.
- Nearest neighbors: online-banking-portal (surface sibling), digital-banking-application (scope sibling), business-banking-portal (customer-tier sibling), digital wallet / P2P payment / PFM (no bank relationship of record), core banking system (internal substrate).
- Likely confusion: with the web portal (near-identical object model, same institution, marketed as one channel) and with "digital banking" (combined-channel marketing label).
- Unknowns going in: whether the app surface has structural machinery of its own (device binding, push, camera capture, app-as-second-factor) or is merely a small-screen skin of the portal; how capability is distributed between app and web; whether app registration is distinct from account opening; what the historical check requires.

## Research Questions

1. What are the core objects of the mobile banking app? (accounts, transactions, payees, transfers/payments, deposits, cards, alerts, statements, profile/security settings)
2. What are the main workflows? (app download/registration/activation, login/auth, daily check-and-act loop, money movement, mobile deposit, card control, in-app support)
3. What rules shape behavior? (enrollment gates, device binding, biometrics, deposit verification holds, channel agreements, fraud guarantees, session behavior, OS requirements)
4. How is capability distributed between the app and the web portal at the same institution — and does the app carry structurally distinct machinery?
5. What separates this Type from the portal sibling, the digital-banking sibling, the business portal, and from wallet/P2P/PFM/aggregators?
6. Joint review: with the surface held in the defining core, do the two servicing leaves separate cleanly — and is the surface load-bearing or cosmetic?
7. Historical / market-sample check: does the definition over-fit the modern smartphone app? Would an older or differently positioned mobile banking client still fit?

## Representative Products

| Product | Institution | Region | Why sampled |
|---|---|---|---|
| Chase Mobile® app | JPMorgan Chase Bank, N.A. | US | largest US bank; dedicated mobile-banking product page with FAQ defining mobile banking |
| Bank of America Mobile Banking | Bank of America, N.A. | US | explicit Mobile-vs-Online FAQ defining the surface difference and capability distribution; Erica virtual assistant |
| Wells Fargo Mobile® app | Wells Fargo Bank, N.A. | US | combined "Mobile & Online Banking" page — same source the portal pass used, observed here from the mobile side for direct cross-surface comparison |
| CommBank app | Commonwealth Bank of Australia | AU | app-headline institution; rich capability detail (QR cardless, CallerCheck, PayID); same institution's NetBank observed by the portal pass |
| Barclays app | Barclays Bank UK PLC | UK | "ways to bank" framing; app as the opening funnel; cheque deposit via camera; same institution's Online Banking observed by the portal pass |

Product-philosophy / customer-tier diversity is constrained: mobile banking apps are bank-operated channels, not vendor products, so "different vendors" means "different institutions and markets". Three US + one AU + one UK sample across five institutions is sufficient for the common-structure claims below; the two institutions overlapping with the portal pass (CommBank, Barclays) were deliberately kept for direct cross-surface comparison.

## Sources

Fetched 2026-09-10:

- Chase — "Mobile banking features with Chase Mobile® App" (product page): https://www.chase.com/digital/mobile-banking [Tier 2]
- Bank of America — "Online and Mobile Banking Features and Digital Services" (product page + Mobile/Online FAQ): https://www.bankofamerica.com/digital-banking/mobile-banking.go [Tier 2]
- Wells Fargo — "Mobile and online banking with Wells Fargo" (product page): https://www.wellsfargo.com/online-banking/ [Tier 2]
- CommBank — "The CommBank app" (product page + FAQs): https://www.commbank.com.au/digital-banking/commbank-app.html [Tier 2]
- Barclays — "The Barclays app" (product page + FAQs): https://www.barclays.co.uk/ways-to-bank/mobile-banking-app/ [Tier 2]

Sibling research used for joint-review context (read, not re-fetched):

- research/online-banking-portal.md (processed 2026-09-08) — portal-side observations incl. CommBank app-approval MFA for NetBank logons, Barclays app-routed account opening
- research/digital-banking-application.md (processed 2026-09-08) — scope-seam framing and the pre-hung joint review

Unreachable this pass: none attempted beyond the five above; deep help-center trees (e.g., Chase/BofA/CommBank support articles) were not fetched — product pages + FAQs were the reachable layer. Per the source-limitation rule, precise operational details (deposit hold durations, transfer cut-offs, default limits, session timeout values beyond what pages state) are not asserted.

## Product A — Chase Mobile® app (US)

### Key observations (evidence layer A unless noted)

- Named product "Chase Mobile® app" alongside chase.com online banking; site footer lists "Mobile Banking" and "Online Banking" as separate links — two named surfaces of one channel.
- The bank's own definition (FAQ): "Mobile banking is a service provided by banks that allows you to conduct financial transactions remotely using your bank's verified app on your mobile device."
- Function list (FAQ): view transaction history, view account balances, view eStatements, deposit checks, set alerts, send a message to customer support, transfer funds between accounts, pay bills, manage credit or debit card.
- Chase QuickDeposit℠ — deposit checks by taking a picture with the phone/tablet camera; "funds will generally be available the next business day" (vendor-specific timing, kept here only).
- Zelle® in-app (send/receive, split bills, future/recurring payments); "more than 2,200 banking apps in the U.S. offer Zelle®" (market rail).
- Lock and unlock debit/credit card "right from your phone"; replacement flow.
- Biometric login: Apple Face ID / Touch ID, Google Fingerprint Login.
- Fraud monitoring 24/7 with text/email/call alerts on unusual credit-card activity.
- "Our online and mobile banking commitment to you" — reimbursement commitment for unauthorized transactions through mobile or online bill pay/transfer (channel-level guarantee; Digital Services Agreement PDF linked).
- Digital wallet provisioning: "add your cards for contactless payments through many digital wallets."
- Financial tools in the app: Spending and Budgeting tool, Autosave (recurring transfers), Credit Journey (free credit score, "no Chase account required").
- J.P. Morgan Wealth Management investing inside the app (open account, trade, transfer between investment and banking accounts).
- New device: "download the Chase Mobile® app again and log in with your credentials."
- App available for phones and tablets, iOS and Android; app-store distribution + QR code + SMS-style download links.

## Product B — Bank of America Mobile Banking (US)

### Key observations

- "Mobile and Online Banking" presented as one program with two surfaces; navigation separates "Mobile Banking" and "Digital/Online Banking".
- **The decisive FAQ (verbatim):** "What is the difference between Mobile and Online Banking? Mobile Banking allows you to access your account information from almost anywhere using the Mobile app on your wireless device. Online Banking requires you to access your account through your web browser. Most features are available in both Online Banking and the Mobile app, however there are some exceptions, for example Erica and Mobile Check Deposit which are available only in the Mobile app."
- Enrollment: "You can enroll in either Mobile Banking or Online Banking, and your User ID and password are the same." — one credential across surfaces; enrollment distinct from account opening; guided enrollment demos for each surface.
- Erica® — virtual financial assistant (servicing needs, financial questions, connecting to specialists) — "only available in the Mobile Banking app."
- Mobile Check Deposit — app-only; "subject to verification and not available for immediate withdrawal" (verification hold semantics).
- Zelle® in app or online; bill pay (one-time/recurring, reminders); transfers; domestic/international wires — in both surfaces.
- Alerts: "Device must support ability to receive push notifications. Mobile app alerts are not available for all devices or in our web-based Mobile Banking." — push is app-side machinery.
- Statements: view/download up to 18 months online; order copies up to 7 years; paperless settings; check images online.
- Security: security meter ("Check your account security level, enable more security features"), Security Center, scam red flags; $0 Liability Guarantee for debit card.
- Account scope: checking, savings, credit/lending AND Merrill investing accounts — whole-relationship servicing.
- Card management: debit and credit card surfaces; digital wallets; BankAmeriDeals (cash-back offers; requires Online/Mobile enrollment).
- Financial wellness: Life Plan®, Spending & Budgeting Tool.
- Order checks/deposit tickets via app or website; order-status tracking.
- "Mobile Banking requires that you download the Mobile Banking App and is only available for select mobile devices." — device/OS gating.
- Online Banking Service Agreement — the channel's agreement layer.

## Product C — Wells Fargo Mobile® app (US)

### Key observations

- Named products on one page: "Wells Fargo Mobile® app" and "Wells Fargo Online®" — "Manage your money on the Wells Fargo Mobile® app when you're on the go. And use Wells Fargo Online® when it's more convenient to be on your computer." (the two-surface framing, verbatim; same source the portal pass cited, here read from the mobile side)
- Top-level capability framing (channel-wide): "Manage your accounts", "Transfer money and pay bills", "Plan for your financial future."
- "Redesigned Security Center in the Wells Fargo Mobile® app": check/update security settings, security best practices, scam tips — security posture surfaced app-side.
- One shared enrollment link for the channel (identity/enrollment URL) — enrollment distinct from account opening.
- "Supported Browsers and Wells Fargo Mobile® app Requirements" page — the app surface has explicit mobile-OS requirements.
- Text-to-download: text a shortcode (IPH/AND) to receive the app link — carrier-dependent distribution.
- Online Access Agreement governs the channel; fraud-protection guidance.
- FICO Score display for enrolled customers of eligible consumer accounts (educational score disclaimer) — vendor-specific extra.
- Account opening online possible (18+, SSN/ITIN, physical US address, own mobile number) — adjacent opening funnel, not the app's center.
- Apple Pay / Face ID / Touch ID / Apple Watch / iCloud Keychain trademarks — biometric + wearable + wallet provisioning signals.

## Product D — CommBank app (AU)

### Key observations

- Named product "CommBank app" with separate logons for NetBank (web) and CommBiz (business) — three distinct surfaces at one institution; the app is the headline surface ("Join over 9 million users").
- Card management in seconds: manage digital wallets, change PIN, lock card, report lost/stolen.
- PayID (mobile number/email as payment address); send money, pay bills, check balances.
- QR Cardless: QR-code deposits and withdrawals at CommBank ATMs — "can only be completed with the CommBank app on CommBank app registered devices" (device-bound capability; daily limits apply).
- Real-time alerts for suspicious activity and transactions — "You must enable push notifications on your registered device."
- CallerCheck: verify a caller claiming to be CommBank "by sending a secure notification to the CommBank app" — **the app as the institution's trust anchor**. NameCheck: payment-detail validation reducing incorrect payments.
- Biometric login: fingerprint, Face ID, passcode.
- Insights (spending, bills, investing, savings in one place); in-app share trading (CommSec Pocket / individual accounts); savings goals (GoalSaver).
- CommBank Yello rewards; in-app Travel Booking (third-party provided — Hopper).
- 24/7 in-app support: virtual assistant 'Ceba' ("ask questions, lock your card, update details and more") + specialist messaging back in the app.
- Registration requirements (FAQ): 14+, Australian residential address, valid email + mobile, one physical ID; "Setup takes about 10 minutes."
- **Non-customer use:** "Do I need to be a CommBank customer to use the app? No — you can still download the CommBank app and use select features like cardless cash deposits… You'll need to verify your identity before getting started." — app registration can precede full customer status; servicing still requires the relationship.
- Auto log-off after 15 minutes of inactivity (adjustable) — vendor-specific value, kept here.
- App OS requirements: Android 8.0+, iOS 15.0+.
- Personal↔business account switching inside the one app ("see your finances in one place") — sole-trader absorption inside the consumer app (matches business-banking-portal pass's flag).
- CommBank Companion — AI assistant "now in testing" (era-current layer, not definitional).

## Product E — Barclays app (UK)

### Key observations

- Framed under "Ways to bank" — the app is one named channel among Online Banking, Telephone Banking, and physical locations; "Join 12 million Barclays customers using our app."
- **The app as opening funnel (verbatim):** "The quickest way to open a new bank account is using our app" — QR code → download → begin application (18+, UK only). Confirms the portal pass's observation that Barclays routes new-account opening to the app.
- Pay and transfer money between accounts; add cards to Apple Pay and Google Wallet.
- Spending insights ("personalised insights on your spending").
- Card control: "set limits for different payment types, get a reminder of your PIN, and temporarily freeze your card if it's been lost or stolen."
- In-app asynchronous messaging: "Send us a message straight from the 'Help' section of our app… just log back in when you're ready to see if we've replied."
- Pay in a cheque: "our app can use your device's camera to take a picture" — UK mobile cheque deposit (paper-era behavior digitized through the camera).
- Age gate: "You need to be 11 or over to use the app" — LOWER than the portal's 16+ online-banking gate (portal pass observation); app access is the broader gate.
- Business/wealth account holders can use the app "but you won't have access to all the app's features" — feature distribution by relationship type.
- Device constraints: Android (Go edition) not supported; Android tablet users directed to the Barclaycard app — per-device-family capability distribution.
- Dedicated "How to register" help page — app registration as a distinct flow.
- Service-status site; security certifications (Cyber Essentials, Kitemark, ISO 27001).

## Cross-product Comparison

| Structure / capability | Chase Mobile | BofA Mobile | Wells Fargo Mobile | CommBank app | Barclays app | Layer |
|---|---|---|---|---|---|---|
| Named app product alongside a named web portal | Y (Chase Mobile® / chase.com) | Y (Mobile / Online Banking; FAQ defines the difference) | Y (Wells Fargo Mobile® / Wells Fargo Online®) | Y (CommBank app / NetBank) | Y (Barclays app / Online Banking) | B |
| Bank's own channel bound to real accounts at the institution | Y | Y | Y | Y | Y | B |
| App enrollment/registration distinct from account opening | Y (download + login with credentials) | Y (enroll in either surface; same User ID/password) | Y (shared channel enrollment link) | Y (register: 14+, ID; non-customers get select features) | Y ("How to register" flow) | B |
| Balance + transaction history | Y | Y | Y | Y | Y | B |
| Money movement executed in-app (transfers / bill pay / P2P rail) | Y (transfers, Zelle, bill pay) | Y (transfers, bill pay, Zelle, wires) | Y (transfer/pay) | Y (PayID, bills, send money) | Y (pay and transfer) | B |
| Camera-based capture (mobile check/cheque deposit) | Y (QuickDeposit) | Y (app-only; verification hold) | (US practice; not on fetched page) | — (QR cardless cash instead) | Y (cheque via camera) | B (3/5 observed; market-dependent) |
| Card controls from the app (lock/freeze, PIN, limits, lost/stolen) | Y (lock/unlock) | Y (card management) | (Security Center posture) | Y (lock, PIN, wallets, lost/stolen) | Y (limits, PIN reminder, freeze) | B |
| Biometric / device-bound login | Y (Face ID/Touch ID/Fingerprint) | (security features; device gating) | Y (Face ID/Touch ID marks) | Y (fingerprint, Face ID, passcode; registered devices) | ("latest security features") | B (mechanisms vendor-specific) |
| Push notifications / alerts | Y (alerts; fraud texts) | Y (push; "not available… in our web-based Mobile Banking") | (Security Center) | Y (real-time alerts; push on registered device) | (not on fetched page) | B |
| App-only capability distribution | Y (QuickDeposit emphasized) | Y (Erica + Mobile Check Deposit app-only — FAQ verbatim) | Y (Security Center redesigned in app) | Y (QR cardless requires app on registered device; CallerCheck via app) | Y (cheque deposit via camera) | B |
| App as trust anchor / second factor for other surfaces | (not observed) | (not observed) | (not observed) | Y (CallerCheck; NetBank logon approved via app — portal pass) | (not observed) | product-specific (CommBank) |
| In-app support (messaging / virtual assistant) | Y (message customer support) | Y (Erica) | (security tips only) | Y (Ceba + specialist messaging) | Y (async messaging) | B |
| Digital wallet provisioning | Y | Y | Y (Apple Pay marks) | Y | Y (Apple Pay/Google Wallet) | B |
| Financial management tools in-app | Y (budgeting, Autosave, Credit Journey) | Y (Life Plan, Spending & Budgeting) | Y (financial tools) | Y (Insights, goals) | Y (spending insights) | B |
| Investments/wealth inside the app | Y (J.P. Morgan WM) | Y (Merrill accounts) | (FICO score) | Y (CommSec Pocket trading) | (limited for wealth accounts) | B (depth varies) |
| Rewards / offers surfaces | Y (Chase Offers, Rewards) | Y (BankAmeriDeals) | — | Y (Yello, Travel Booking) | Y (rewards) | B |
| ATM/branch locator | Y | Y | Y | Y | Y | B |
| Channel agreement layer | Y (Digital Services Agreement) | Y (Online Banking Service Agreement) | Y (Online Access Agreement) | (T&C in app) | Y (app T&Cs) | B (naming varies) |
| Fraud guarantee / reimbursement commitment | Y ("online and mobile banking commitment") | Y ($0 Liability Guarantee) | (fraud protection guidance) | (security guarantees) | (secure banking) | B |
| Age/eligibility gate for app use | (not observed) | (not observed) | (18+ to apply online — opening, not app use) | Y (14+ to register) | Y (11+ to use) | B (values vary; product/market-specific) |
| Device/OS requirements | Y (phones + tablets, iOS/Android) | Y ("select mobile devices") | Y (app requirements page) | Y (Android 8.0+/iOS 15.0+) | Y (no Android Go; tablet → Barclaycard app) | B |
| Opening funnel in/through the app | (not observed on page) | (open account online — adjacent) | Y (FAQ: open checking online) | Y (register in app; non-customer limited use) | Y ("quickest way to open" — verbatim) | B |
| Personal↔business switching in one app | — | — | — | Y | — | product-specific |
| New-device recovery | Y (re-download + credentials) | (password reset flow) | — | (log-off/auto-log-off) | (registration help) | B (weak, varies) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures; remove any one and the product stops being a Mobile Banking Application:

1. **The bank relationship of record operated behind the application.** The app is operated by (or for) a regulated banking institution as its own customer channel and is bound to the customer's real account(s) held at that institution: the balance and transaction history shown are the money of record, and the institution's obligations (identity-verified relationship, statements, dispute handling, fund protection) reach through the app. Remove → wallet / PFM / aggregator.
2. **The installed-app self-service servicing surface for an existing relationship.** The customer already holds the relationship (opened in a branch, through an app funnel, or another channel); the app is an installed client on the customer's personal mobile device — distributed as an application, signed into with the bank's credentials, carrying the servicing loop session by session without bank staff. Carrying the complete relationship lifecycle (digital opening → use → administer → close) is NOT this leaf's defining job. Remove the installed-app surface → online-banking-portal territory; remove "existing relationship" → digital-banking-application; remove self-service → branch/assisted channels.
3. **Money movement executed from the application.** The customer initiates real money movements against the account from the app: transfers between own accounts, payments to people/companies/billers, card controls that affect spending. The app is an operating surface, not merely a viewer. Remove → read-only balance/statement viewer.

Jointly-held is load-bearing:
- 1 alone = PFM/aggregator
- 2 alone = a generic company account app (any institution's mobile account center)
- 3 without 1+2 = P2P/payments app
- 1+2 without 3 = balance/statement viewer app
- 1+3 without 2 = the web-portal sibling (same servicing core, browser surface)
- 2+3 without 1 = wallet/money app over non-bank value

### L1 — Common Mature Structure (standard capabilities, not definitional)

- App enrollment/registration flow granting access to the existing relationship (distinct from account opening); shared credentials with the web surface where observed (one User ID/password across surfaces at one US sample)
- Biometric/passcode device login; device/OS requirements; new-device recovery
- Push notifications and alerts (balance, payment, fraud, security) — app-side machinery
- Camera-based capture where the market has the paper instrument: mobile check/cheque deposit (US/UK samples)
- Card lifecycle controls from the app: lock/freeze, PIN view/change, per-payment-type limits, lost/stolen replacement, digital-wallet provisioning
- In-app support: messaging (often asynchronous) and virtual assistants
- ATM/branch locator
- Financial management tools: spending insights, budgeting, savings goals, credit-score displays
- Rewards/offer surfaces tied to enrolled cards
- Investment/wealth views inside the app (depth varies by institution)
- Channel agreement layer (Digital Services Agreement / Online Banking Service Agreement / Online Access Agreement / app T&Cs — naming varies)
- Fraud guarantees / reimbursement commitments attached to the digital channel
- Cross-surface capability distribution: most features in both app and web, with named app-only exceptions (the banks' own framing)

### L2 — Variant / Optional Structure

- Market rails: Zelle (US), PayID/BPAY (AU), UK faster-payments culture — rail names are market-specific
- Deposit/cash culture: camera check deposit (US/UK) vs QR cardless cash at own ATMs (AU)
- App-as-trust-anchor posture: app-approval of web logons, caller-verification through app notifications (observed at CommBank; product-specific leaning, recorded as variant)
- Age/eligibility gates for app use (11+ UK, 14+ AU observed; values vary by institution/market)
- Personal↔business account switching inside the consumer app (sole-trader absorption; varies by institution)
- Opening funnel in the app (one UK sample routes new-account opening through the app; others keep opening adjacent)
- App-primary drift: the app marketed as the headline surface, the portal as the "bigger screen"/"on your computer" companion
- Virtual assistants as branded implementations of in-app support (product-specific names)
- Wearable/companion-device support; auto log-off timers (vendor-specific values)
- Feature distribution by relationship type (business/wealth accounts get reduced app feature sets)

### L3 — Vendor-specific (kept here only)

- Chase: QuickDeposit, Pay Over Time, Credit Journey, Chase Offers, Autosave, "online and mobile banking commitment" naming
- BofA: Erica, BankAmeriDeals, Life Plan, $0 Liability Guarantee, SafeBalance feature restrictions, security meter
- Wells Fargo: Wells Fargo Mobile®/Online® naming, text-to-download shortcode, FICO Score display with educational disclaimer, 1–3 business-day external-transfer verification footnote
- CommBank: Ceba, CallerCheck, NameCheck, QR Cardless, CommBank Yello, CommBank Companion (AI, in testing), 15-minute auto log-off, GoalSaver
- Barclays: 11+ age gate, Barclaycard app for Android tablets, wealth/business feature limits, "quickest way to open" positioning

## Joint Review Disposition (consumer-surface trio)

**Ratified: keep-both-as-two-surface-leaves (portal + mobile app), with digital-banking-application as the third scope sibling.** Reasoning from the mobile side:

1. **The servicing core is shared** — confirmed. Object model and daily-servicing capability set are near-identical across the app and web surfaces at the same institutions (CommBank and Barclays observed from both sides across the two passes). This matches the portal pass's prediction exactly.
2. **But the surface is load-bearing, not cosmetic.** The installed-app surface carries structurally distinct machinery that the browser surface does not and cannot carry the same way:
   - device-bound identity (registered devices, biometric/passcode login, device/OS gating, new-device recovery)
   - the push-notification channel (one sample states app alerts are "not available… in our web-based Mobile Banking")
   - camera-based capture (check/cheque deposit; QR cardless cash bound to "app registered devices")
   - app-store distribution with per-OS requirements and per-device-family feature distribution
   - app-only capability distribution at every sampled bank — one bank's FAQ defines the difference itself ("Erica and Mobile Check Deposit… available only in the Mobile app")
   - the app-as-second-factor topology (one sample's web logons are approved through the app; caller verification runs through app notifications)
3. **The banks themselves name and separate the two surfaces** — Chase Mobile® vs chase.com, Wells Fargo Mobile® vs Wells Fargo Online®, CommBank app vs NetBank, Barclays app vs Online Banking, BofA Mobile vs Online Banking — while marketing them as one channel. The directory's two leaves mirror the market's own product structure.
4. **With the surface held in the defining core, the two leaves separate cleanly** (removal test: strip the installed-app surface → the portal sibling; strip the browser surface → this leaf). With the surface abstracted away they collapse — which is why the shared servicing core is documented as the common structure of both leaves, not duplicated as two definitions.
5. The scope seam against digital-banking-application is confirmed from this side: app enrollment/registration is distinct from account opening at every sample; opening funnels exist in/through apps (one UK sample routes opening through the app) but the sampled traditional-bank apps service existing relationships as their center. The digital-banking leaf carries the relationship lifecycle (digital opening → administration → closing); the two servicing leaves do not.

No directory change made unilaterally; this entry discharges the joint-review flag in STATUS.md.

## Historical / Market-Sample Check

- The definition deliberately excludes from the core: biometrics, push notifications, camera deposit, app-store distribution specifics, specific payment rails, virtual assistants, rewards, any named market or OS. An installed mobile banking client without any of these — servicing an existing relationship with money movement — satisfies all three L0 legs.
- The Type is long-lived: bank mobile clients predate the smartphone era (feature-phone installed clients). Per this pass's evidence rules (no historical source fetched), no precise historical product claims are made; the structural check holds because nothing modern is required by the core.
- Boundary note (not a failure): browser-on-phone banking (WAP-era "mobile internet banking") is the portal's surface rendered on a mobile device — it belongs to the portal sibling's surface family, not to the installed-app leaf. SMS/USSD banking is a command channel without a servicing surface — the thin ancestor, not a form of this Type.
- Regional check: US / UK / AU samples all satisfy the core with different rails, deposit cultures, and auth postures; nothing in the core is region-specific.
- Consistency with sibling passes: the digital-banking pass held that a 2000s web-only portal for branch-opened accounts fails the digital-opening leg (→ separate portal leaf); this pass confirms the servicing-surface family (portal + app) sits on the same side of that scope seam.

## Vendor-specific Findings

See L3 above. The most consequential: CommBank's app-as-trust-anchor posture (CallerCheck; app-approved NetBank logons per the portal pass) — the strongest observed case of the app being the security anchor for the whole channel rather than one surface among several. Recorded as variant, not promoted: no other sampled bank documents the equivalent on its fetched pages.

## Rejected Findings

- "Mobile banking = the bank's whole digital channel" — the banks' own pages separate Mobile from Online (BofA FAQ verbatim; Wells Fargo two-product framing); the combined-channel marketing label ("Mobile & Online Banking") does not merge the surfaces.
- "Requires biometric login" — observed at 3–4 samples but not universal on fetched pages; common implementation, not invariant.
- "Requires mobile check deposit" — market-dependent (US/UK yes; AU sample substitutes QR cardless cash); capability, not invariant.
- "The app is where accounts are opened" — one sample routes opening through the app (Barclays, verbatim); others keep opening adjacent; the sampled apps' center is servicing an existing relationship. Opening-in-app is variant, not definitional (otherwise the leaf collapses into digital-banking-application).
- "Push notifications are definitional" — app-side machinery, but a servicing app without push still satisfies the core; common, not invariant.
- "Non-customer app use" (CommBank: download + select features without being a customer) — single-source; held product-specific.

## Boundary Findings

- **vs Online Banking Portal (sibling, processed 2026-09-08)** — surface sibling; the hardest boundary, now DISCHARGED. Shared servicing core confirmed from this side; the seams are the delivery surface (installed app vs browser session) and capability distribution (app-only features at every sample; app-as-second-factor at one). Joint review ratified keep-both (see Joint Review Disposition above).
- **vs Digital Banking Application (processed 2026-09-08)** — scope seam on the relationship-lifecycle leg: the app services an existing relationship; the digital-banking application carries digital opening, administration, and closing inside the product. Confirmed from this side: enrollment/registration everywhere distinct from account opening; opening funnels in apps are variant, not the center.
- **vs Business Banking Portal (processed)** — customer-tier seam (personal relationship vs organization with per-user entitlements). Complication re-confirmed from the mobile side: one sample switches personal/business accounts inside the consumer app — sole-trader absorption varies by institution (matches both prior passes' findings).
- **vs Commercial Banking Platform / Cash Management Platform** — corporate tier with treasury-grade rails; structurally different product, different customer.
- **vs Digital Wallet / Mobile Wallet / Stored Value Wallet** — wallets hold payment instruments or wallet value; no bank account of record. The banking app provisions cards INTO wallets — interconnection, not identity.
- **vs Peer-to-peer Payment Application** — moves money between people from arbitrary funding sources; in-app P2P rails (Zelle, PayID) are capabilities of this Type, not the Type.
- **vs Personal Finance Management Application** — PFM aggregates across institutions or manages records manually; operates no bank account of record. In-app insights/budgeting are capabilities over the bank's own data.
- **vs Core Banking System** — the institution's internal system of record; the app is the customer-facing mobile edge operating on top of it.
- **vs Retail Trading Platform / Brokerage Platform** — investment servicing inside the app (Merrill, J.P. Morgan WM, CommSec Pocket) is a capability; the investment house is a separate Type.
- **vs Customer Portal / Self-service Support Portal (§07)** — generic self-service without the regulated bank relationship of record or executed money movement.
- **vs Mortgage Borrower Portal / single-product-line servicing apps** — those carry servicing + documents without whole-relationship money movement; the mobile banking app services the whole consumer relationship.

## Uncertainties

1. Deep help-center trees were not fetched (product pages + FAQs were the reachable layer). Precise operational details — deposit hold durations, transfer cut-offs, default limits, session timeouts (beyond the one stated value), per-country feature availability — are deliberately not asserted in the final document.
2. Wells Fargo's page is the combined "Mobile & Online Banking" page; its app-specific capability detail beyond the Security Center is thin. Claims resting on it alone are kept weak.
3. The app-as-trust-anchor posture rests on one institution (CommBank, plus its NetBank logon-approval observed by the portal pass); held as variant/product-specific.
4. Age-gate values (11+, 14+) are two data points; the pattern "apps may gate access by age" is asserted, the values are not generalized.
5. No historical source was fetched; the historical check is structural, not product-cited.
6. Non-customer app use (CommBank) is single-source; the edge of the Type where app registration precedes customer status is not exhaustively verified.

## Final Synthesis

A Mobile Banking Application is a regulated banking institution's installed-app self-service channel, bound to the customer's real accounts at that institution (the money of record), through which an existing customer services the relationship without staff — observing account state, executing money movement, capturing deposits with the device camera where the market has paper instruments, controlling cards, receiving push alerts, and reaching support — from a personal mobile device, on a surface the institution ships and maintains as a distinct named product beside its web portal. The defining core is the triple: bank relationship of record + installed-app self-service servicing surface for an existing relationship + executed money movement. Enrollment, biometric/device-bound login, push alerts, card controls, in-app support, locators, financial tools, rewards, investment views, channel agreements, and fraud guarantees are the standard mature capability set; market rails, deposit culture, app-as-trust-anchor posture, age gates, personal/business absorption, and opening funnels are the variant axes. The Type is the mobile sibling of the online banking portal (same servicing core, load-bearing different surface — joint review ratified keep-both) and the servicing-surface sibling of the digital banking application (which carries the complete digitally-conducted relationship), behind the customer-facing edge of the core banking system.
