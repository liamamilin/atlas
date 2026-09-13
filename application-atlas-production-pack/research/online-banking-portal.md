# Research Notes — Online Banking Portal

## Research Goal

Understand **Online Banking Portal** as an Application Type: the bank-operated, browser-delivered web channel through which an existing consumer customer services their banking relationship. Establish the defining core, the standard capability set, and the boundary against the sibling consumer-banking leaves in DIRECTORY.md §08 — especially **mobile-banking-application** (same servicing core, different surface) and **digital-banking-application** (processed 2026-09-08, whose definition explicitly names this leaf as the "servicing portal for an account opened elsewhere") — plus business-banking-portal, wallet/P2P/PFM, core banking system.

This pass also carries **half of a two-sided joint review** pre-hung by the digital-banking-application pass: the consumer-surface trio (online-banking-portal / mobile-banking-application / digital-banking-application) overlaps almost totally on daily servicing; the seam lives on the relationship-lifecycle leg. The mobile-banking-application pass is still unprocessed, so this pass records its half and keeps the joint-review flag alive.

## Initial Boundary (working hypothesis before research)

- Core use: an existing bank customer logs in from a browser to view accounts, move money, view/download statements, manage cards, and administer their details — without bank staff.
- Users: retail/consumer banking customers; bank staff are not primary users of this surface.
- Nearest neighbors: mobile-banking-application (surface sibling), digital-banking-application (scope sibling), business-banking-portal (customer-tier sibling), digital wallet / P2P payment / PFM (no bank relationship of record), core banking system (internal system of record behind it).
- Likely confusion: with mobile banking (nearly identical object model) and with "digital banking" (banks market the combined channel under one label).
- Unknowns going in: whether any structural (non-surface) seam between portal and app can be found; how much product-line servicing and application-funnel activity lives inside portals; how regional rails shape the payments leg; what the historical check requires.

## Research Questions

1. What are the core objects of the portal? (accounts, transactions, payees, transfers/payments, statements, cards, profile/security settings, alerts)
2. What are the main workflows? (registration/enrollment, login/auth, daily check-and-act loop, money movement, document retrieval, card handling, profile administration)
3. What rules shape behavior? (enrollment gates, step-up authentication, transfer limits and verification, session-based access, institution obligations, maintenance windows)
4. What separates this Type from the mobile app sibling, the digital-banking sibling, the business portal, and from wallet/P2P/PFM/aggregators?
5. Historical / market-sample check: does the definition over-fit the modern multi-channel web portal? Would an older, regional, or differently positioned web portal still fit?

## Representative Products

| Product | Institution | Region | Why sampled |
|---|---|---|---|
| Wells Fargo Online | Wells Fargo Bank, N.A. | US | large universal bank; official online-banking pages + access agreement reachable |
| NetBank | Commonwealth Bank of Australia | AU | named consumer web portal with rich public capability documentation; different market rails |
| Barclays Online Banking | Barclays Bank UK PLC | UK | large UK retail bank; explicit "ways to bank" framing, security-device auth, guarantee |
| DBS internet banking | DBS Bank Ltd | SG | weak Tier-2 only (marketing homepage reachable); used to confirm the internet-banking login surface exists as a distinct surface in an Asian market |

Product-philosophy / customer-tier diversity is constrained: bank portals are bank-operated channels, not vendor products, so "different vendors" means "different institutions and markets". Three strong samples across three markets plus one weak signal is sufficient for the common-structure claims below.

## Sources

- Wells Fargo — "Mobile and online banking with Wells Fargo" (product page, fetched 2026-09-08): https://www.wellsfargo.com/online-banking/ — includes enrollment link (oam.wellsfargo.com/oamo/identity/enrollment), Online Access Agreement link, supported-browsers page link, Zelle FAQ link, transfer-verification footnote.
- CommBank — "NetBank" (product page, fetched 2026-09-08): https://www.commbank.com.au/digital-banking/netbank.html — plus linked support pages (multi-factor authentication at logon, BPAY how-to, PayID, card activation).
- Barclays — "Online Banking" (product page, fetched 2026-09-08): https://www.barclays.co.uk/ways-to-bank/online-banking/ — includes registration/login URLs under bank.barclays.co.uk/olb/, PINsentry guide link, Online Banking guarantee link, error-codes tool, service status site link.
- DBS — personal banking homepage (fetched 2026-09-08): https://www.dbs.com.sg/personal/landing/dib — Login link to internet-banking.dbs.com.sg, "Terms & Conditions Governing Electronic Services", "Scheduled Maintenance", "Update Personal Particulars", "Instant Apply".
- Wikipedia "Online banking" — attempted twice 2026-09-08, both timed out → abandoned; historical claims kept structural, no precise historical dates/products asserted.
- Capital One (https://www.capitalone.com/digital/online-banking/) — 404; HSBC (https://www.hsbc.co.uk/online-banking/) — 404; abandoned after one attempt each.

## Product A — Wells Fargo Online (US)

### Key observations (evidence layer A unless noted)

- The web surface has its own product name ("Wells Fargo Online®") alongside the mobile app, marketed together: "use Wells Fargo Online® when it's more convenient to be on your computer." (confirms web = the computer-side surface of one channel)
- Enrollment is a distinct flow ("Enroll now" → identity/enrollment URL) — separate from opening an account; FAQ confirms account opening can also happen online, but the online-banking page frames enrollment for existing customers.
- Top-level capability framing: "Manage your accounts", "Transfer money and pay bills", "Plan for your financial future."
- The channel is governed by a dedicated legal document: "Online Access Agreement" — the portal has its own agreement layer between customer and institution.
- Supported-browsers page exists ("Supported Browsers and Wells Fargo Mobile® app Requirements") — the browser surface has explicit technical requirements.
- Transfers to/from other U.S. financial institutions require setup and verification ("verification may take 1–3 business days" — vendor-specific timing, kept here only).
- Zelle integration under the online-banking help tree (market rail for person-to-person payments).
- FICO Score display available to enrolled customers of eligible consumer accounts (vendor-specific extra; educational score disclaimer).
- Security Center (check/update security settings, scam tips); username/password FAQ surfaces; fraud-reporting surface.
- Site footer continuity "© 1999 - 2026" (weak observation; the web channel is long-lived).

## Product B — NetBank, Commonwealth Bank (AU)

### Key observations

- Self-description: "A secure, online place for you to manage your finances" — "day-to-day banking from your laptop or desktop computer with NetBank." (browser/desktop framing explicit)
- Registration distinct from account opening: "Register for NetBank… using your CommBank card" or with existing client number/password; requires valid email + mobile number. New customers who open an Everyday account online are "automatically registered for NetBank" — opening funnel exists adjacent to the portal, but the portal's center is servicing.
- Logon: client number + password; if the customer has the CommBank app, an app notification confirms the logon attempt before web access is granted (multi-factor via the app; documented on a dedicated MFA support page).
- Basics listed by the bank itself: view balance; check statements and transactions; transfer to someone or between own accounts; find ATM/branch; update personal details.
- Account organization: show/hide accounts, group accounts, nicknames — user-side organization of the account list.
- Payments: manage PayID; one-off and multiple transfers (to address-book payees or not); scheduled transfers; BPAY one-off/recurring; BPAY View (bills delivered into NetBank with alerts/reminders) + AutoPay; international money transfers; receiving from overseas.
- Cards: activate debit/credit cards and choose PIN; change credit limit; amend daily limit; Lock/Block/Limit (credit) and Lock/Block/Alert (debit); lost/stolen protection at home or overseas.
- Loans/mortgages serviced inside the portal: view loan balance and statements, make extra repayments, change repayment amount/frequency, refix rate, top up loan.
- Travel surface: travel notice ("Tell us before you go"), travel money card activation/reload.
- Business inside the consumer portal: "NetBank business support" — payroll, cash-flow tools, real-time balances, threshold notifications, scheduled payment groups, bank feeds to accounting software (Xero/MYOB). (Confirms the business-banking-portal pass's flag: sole-trader/SMB absorption varies by institution — here inside the consumer portal.)
- Interest & Tax Summary (one-pager of interest earned/charged) — institution-produced document retrieval.
- Product redesign in progress ("a new NetBank is coming") — the portal is a continuously maintained product.

## Product C — Barclays Online Banking (UK)

### Key observations

- Framing under "Ways to bank" — Online Banking is one named channel among branch, phone, and the app: "Prefer to do your banking on a bigger screen?" (browser/desktop framing explicit)
- Register / Log in as separate actions (registration URL under bank.barclays.co.uk/olb/registration; login under /olb/authlogin) — registration grants access to an existing relationship.
- Age gate: "You need to be 16 or over to access online banking."
- Core trio listed by the bank: see balance; transfer between your accounts; search your transactions.
- Payments: UK and international payments; schedule standing orders; stop a cheque. (paper-era banking behaviors serviced digitally — cheque culture)
- Paperwork: see statements, request paper copies, download records, customise financial reports.
- Alerts: balance updates, payment notifications, overdraft notifications — set by the customer.
- Profile: change address, contact number and other personal details "in just a few steps."
- Card management: check PIN, report lost/stolen, order a new card, track the new card's delivery journey.
- In-portal application funnels: open a savings account, apply for a loan (soft-check rate first), get insurance, join Premier Banking — applications start inside the portal.
- Cross-product-line servicing: Smart Investor (investments) "manage in Online Banking."
- Login help: an error-code lookup tool for the most common login error codes.
- Security: PINsentry — a physical device generating unique eight-digit codes to "confirm your identity, authorise transactions and log in… giving you full access to all the features" (implies tiered feature access by authentication method — baseline vs elevated). Vendor-specific mechanism, kept here.
- "Online Banking guarantee" — an explicit fraud-protection guarantee attached to the digital channel.
- Operated-service signals: BSI Kitemark for Secure Digital Banking, ISO 27001, Cyber Essentials certifications; separate service-status site (status.uk.barclays).
- New-account opening is routed through the mobile app (QR code → download app → begin application), not through the web portal — the portal's center remains servicing, opening funnels for product lines notwithstanding.

## Product D — DBS internet banking (SG) — weak evidence

### Key observations (reduced strength)

- A separate "Login" link points to a dedicated internet-banking host (internet-banking.dbs.com.sg) — the web login surface exists distinct from the digibank app.
- "Terms & Conditions Governing Electronic Services" — the electronic channel has its own agreement layer (matches Wells Fargo's Access Agreement pattern).
- "Scheduled Maintenance" page — the service has maintenance windows (matches Barclays status-site signal).
- "Update Personal Particulars", "Instant Apply" (online applications) — profile administration and application funnels present.
- The homepage marketing emphasizes the digibank app; the web portal is not the headline surface at this institution. (Weak signal for the app-primary drift; recorded as observation, not generalized.)

## Cross-product Comparison

| Structure / capability | Wells Fargo Online | NetBank (CommBank) | Barclays Online Banking | DBS (weak) | Layer |
|---|---|---|---|---|---|
| Browser/desktop "bigger screen" surface, distinct from the app | Y ("on your computer") | Y ("laptop or desktop") | Y ("bigger screen") | Y (separate internet-banking host) | B |
| Bank's own channel bound to real accounts at the institution | Y | Y | Y | Y | B |
| Enrollment/registration distinct from account opening | Y (Enroll) | Y (Register with card) | Y (Register) | (not observed) | B |
| Login with step-up/second factor | Y (Security Center posture) | Y (app-approval MFA) | Y (PINsentry device, tiered access) | (Digital Token marketed) | B (mechanisms vendor-specific) |
| Channel's own legal agreement | Y (Online Access Agreement) | (T&C framework present) | (T&C apply) | Y (Electronic Services T&C) | B (naming varies) |
| Balance + transaction history/search | Y | Y | Y | (assumed, not observed) | B |
| Transfers own↔own and to others | Y (external banks need setup+verification) | Y (one-off, multiple, scheduled) | Y (UK + international) | (PayNow/GIRO marketed) | B |
| Bill-pay / market rails | Y (Zelle) | Y (BPAY, BPAY View, PayID) | Y (standing orders; cheque stop) | Y (PayNow/GIRO marketed) | B (rails are market-specific) |
| Scheduled/recurring payments | (implied by bill pay) | Y (scheduled transfers, recurring BPAY) | Y (standing orders) | (GIRO) | B |
| Statements/documents download | Y (Access Agreement; help tree) | Y (+ Interest & Tax Summary) | Y (+ paper copies, custom reports) | — | B |
| Card management (activate/PIN/limits/lock/replace) | (app-side emphasized) | Y (rich) | Y (rich) | — | B |
| Profile/personal-details administration | Y | Y | Y | Y | B |
| Alerts/notifications | Y (Security Center context) | Y (threshold + bill reminders) | Y (balance/payment/overdraft) | — | B |
| Loan/mortgage servicing in portal | (implied by eligible accounts incl. loans) | Y (rich) | (product pages adjacent) | — | B (depth varies) |
| In-portal application funnels (savings/loan/insurance) | Y (open checking online — adjacent) | Y (open Everyday account) | Y (savings, loan, insurance, Premier) | Y (Instant Apply) | B |
| Investments/wealth view inside portal | (FICO score; financial tools) | Y (super tracking) | Y (Smart Investor) | Y (digiWealth marketing) | B (depth varies) |
| Travel notice | — | Y | — | — | product-common, not universal on fetched pages |
| Fraud guarantee / scam education | Y (tips) | Y (security capabilities) | Y (guarantee + education) | Y (Scam Defence) | B |
| Operated-service signals (status/maintenance, browser requirements) | Y (supported browsers) | Y (redesign rollout) | Y (status site, error-code tool) | Y (maintenance schedule) | B |
| SMB tools inside consumer portal | — | Y (NetBank business support) | — | — | product-specific |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures; remove any one and the product stops being an Online Banking Portal:

1. **The bank relationship of record operated behind the portal.** The portal is operated by (or for) a regulated banking institution as its own customer channel and is bound to the customer's real account(s) held at that institution: the balance and transaction history shown are the money of record, and the institution's obligations (identity-verified relationship, statements, dispute handling, fund protection) reach through the portal. Remove → PFM dashboard / aggregator / wallet.
2. **The browser-delivered self-service servicing surface for an existing relationship.** The customer already holds the relationship (opened in a branch, through an app funnel, or another channel); the portal is where they service it themselves — observing account state, moving money, retrieving documents, administering details — session by session, without bank staff. Carrying the complete relationship lifecycle (digital opening → use → administer → close) is NOT this leaf's defining job. Remove the browser surface → mobile-banking-application territory; remove "existing relationship" → digital-banking-application; remove self-service → branch/assisted channels.
3. **Money movement executed from the portal.** The customer initiates real money movements against the account from the portal: transfers between own accounts, payments to people/companies/billers, scheduled payments. The portal is an operating surface, not merely a viewer. Remove → read-only statement viewer; combined with (2) alone, single-product-line servicing portals (e.g., loan servicing).

Jointly-held is load-bearing:
- 1 alone = PFM/aggregator
- 2 alone = generic web account portal (utility/insurance account management)
- 3 without 1+2 = payments/P2P app
- 1+2 without 3 = statement/document portal (loan-servicing territory)
- 1+3 without 2 = the mobile-banking surface (sibling leaf)
- 2+3 without 1 = wallet/money app over non-bank value

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Enrollment/registration flow granting access to the existing relationship (distinct from account opening)
- Step-up / multi-factor authentication (app-approval, device tokens, physical security devices) with tiered access where elevation unlocks all features
- Payee/address-book management; one-off, bulk, scheduled and recurring payments
- Market-specific payment rails (Zelle, BPAY/PayID, standing orders/direct debits, PayNow/GIRO, SEPA-family rails)
- International payments/remittances
- Statements and institution-produced documents (download, paper-copy request, tax/interest summaries, custom reports)
- Card lifecycle management (activate, PIN, limits, lock/block, replace, track delivery)
- Alerts/notifications (balance, payment, overdraft, bill reminders, threshold)
- Profile/personal-details administration; contact-detail currency as fraud prevention
- Account organization (nicknames, groups, show/hide)
- Loan/credit-line servicing (balance, statements, repayment changes, top-ups)
- In-portal application funnels for product lines (savings, loans, insurance, premier tiers)
- Investment/wealth views inside the portal (depth varies)
- Secure support entry (help trees, error-code tools, messaging), fraud/scam education, channel fraud guarantees
- Operated-service signals: supported browsers, status pages, scheduled maintenance, rolling redesigns
- Travel notices

### L2 — Variant / Optional

- Regional bill-pay culture: payer-side bill orchestration (BPAY View) vs payee-directed rails (PayID/PayNow/Zelle) vs instruction classics (standing orders, cheque stop)
- Authentication posture: password + step-up vs physical security devices vs app-approval; tiered vs uniform feature access
- Relationship breadth: transaction-account focus vs whole-relationship servicing (loans, mortgages, investments inside one portal)
- Business absorption: SMB/sole-trader tools inside the consumer portal (CommBank) vs separate business portal (the sibling leaf's tiering)
- Opening-adjacent behavior: portals that route new-account opening to the app (Barclays), portals with adjacent opening funnels (CommBank, Wells Fargo FAQ)
- Age/eligibility gates for portal access (16+ observed in one market)
- Paper-era behaviors digitized (cheque stop, paper-copy requests) — region/culture dependent
- App-primary drift: institutions marketing the app as headline and the portal as the "bigger screen" companion

### L3 — Vendor-specific (kept here only)

- NetBank naming, BPAY View AutoPay, Interest & Tax Summary, superannuation tracking, "Lock, Block, Limit/Alert" branding
- PINsentry eight-digit codes and feature-tier gating (Barclays)
- Wells Fargo Online® branding, Online Access Agreement naming, FICO Score display with educational disclaimer, Zelle licensing, 1–3 business-day external-bank verification footnote
- Barclays error-code lookup tool, Online Banking guarantee naming, Premier Banking join flow
- DBS Digital Token, digiWealth/Multiplier marketing, Scam Defence naming

## Historical / Market-Sample Check

- The definition deliberately excludes from the core: smartphone apps, push notifications, specific MFA mechanisms, cloud/AI features, specific payment rails, and any named market. A browser portal for accounts opened in a branch satisfies all three L0 legs.
- The Type is long-lived and web-native: the leaf names the web-era digitization of branch-era servicing. Pre-web remote banking channels (dial-up/Videotex-era home banking) are the documented ancestor; per the evidence rules of this pass (no historical source reachable — Wikipedia timed out twice), no precise historical product claims are made. The structural check holds: such ancestors carried the servicing + money-movement core on non-web terminals, which is why the *surface* (browser portal) is held as part of this leaf's defining presentation and the ancestor is recorded as the thin pre-history, not a required form.
- Consistency with the digital-banking-application pass: that pass's historical check explicitly held that a 2000s web-only portal for branch-opened accounts "correctly fails the digital-opening leg → separate online-banking-portal leaf." This pass confirms the same seam from the portal side.
- Regional check: US / UK / AU / SG samples all satisfy the core with different rails and auth postures; nothing in the core is region-specific.

## Vendor-specific Findings

See L3 above. The most consequential product-specific finding: SMB/sole-trader tooling inside a consumer portal (CommBank NetBank business support) — relevant to the business-banking-portal pass's flag that sole-trader absorption varies per institution (consumer-portal routing vs separate product).

## Boundary Findings

- **vs Mobile Banking Application (sibling leaf, unprocessed)** — the hardest boundary. The observed object model and daily-servicing capability set are near-identical across surfaces; the same institution presents them as one channel ("Mobile & Online Banking"). The seams observed: (a) surface — browser/desktop session vs installed app; (b) capability distribution — some capabilities lean app-side (e.g., app-approval as the web portal's second factor; app-only functions such as mobile check deposit in US practice), and the portal leads for "bigger screen" long-form tasks. Removal test recorded: strip the browser surface → the mobile sibling; the servicing core itself is shared. **Taxonomy problem recorded:** with the surface held in L0 leg 2, the two leaves are cleanly separable; with the surface abstracted away, they collapse into one Type. The directory currently holds them as two leaves on the surface seam — consistent with both prior sibling passes — and the two-sided joint review (pending the mobile-banking-application pass) should decide keep-both vs merge. This pass contributes its half and keeps the flag alive.
- **vs Digital Banking Application (processed)** — scope seam on the relationship-lifecycle leg: the portal services an existing relationship; the digital-banking application carries digital opening, administration, and closing inside the product. Confirmed from this side: registration/enrollment flows everywhere are distinct from account opening; Barclays routes new-account opening to the app, not the portal.
- **vs Business Banking Portal (processed)** — customer-tier seam (personal relationship vs organization with per-user entitlements). Complication recorded: one sample embeds SMB tools inside the consumer portal, so the seam is real but its product expression varies by institution (matches the business-banking-portal pass's finding).
- **vs Commercial Banking Platform** — corporate tier with treasury-grade rails; structurally different product, different customer.
- **vs Mortgage Borrower Portal / single-product-line servicing portals** — these carry structures 1+2 without 3 (servicing + documents, no money movement) for one product line; the online banking portal services the whole relationship with movement capability.
- **vs Digital Wallet / Mobile Wallet / Stored Value Wallet** — wallets hold payment instruments or wallet value; no bank account of record, no institution obligations reaching through. A bank portal provisions cards into wallets — interconnection, not identity.
- **vs Peer-to-peer Payment Application** — moves money between people from arbitrary funding sources; in-portal transfers to people are a capability of this Type, not the Type.
- **vs Personal Finance Management Application** — PFM aggregates across institutions or manages records manually; operates no bank account of record.
- **vs Core Banking System** — the institution's internal system of record; the portal is the customer-facing edge operating on top of it.
- **vs Retail Trading Platform / Brokerage Platform** — investment servicing may appear inside a bank portal (one sample), but the investment house is a separate Type; the portal remains the bank-relationship surface.
- **vs Customer Portal / Self-service Support Portal (§07)** — generic company portals share the "self-service servicing" leg but lack the regulated bank relationship of record and executed money movement.
- **vs Customer-to-Business Messaging / payment gateways** — different actors entirely (merchant-side machinery).

## Uncertainties

- The portal↔app seam is surface-only on current evidence; whether the directory keeps two leaves or merges them is deferred to the joint review with the mobile-banking-application pass (still unprocessed).
- DBS evidence is weak (marketing homepage only); its observations are used only to confirm the existence pattern of a separate internet-banking surface, electronic-services agreement, and maintenance windows — not for capability detail.
- Precise operational details deliberately not asserted in the final document: session timeout values, transfer cut-off times, default limits, document retention windows, specific MFA step sequences, per-country feature availability.
- Wells Fargo's page is a combined "Mobile & Online Banking" marketing page; its web-portal-specific capability detail (beyond enrollment, agreement, supported browsers, transfers, Zelle, FICO) is thinner than CommBank/Barclays pages. Claims resting on it alone are kept weak.
- No historical source was reachable; the historical check is structural, not product-cited.

## Final Synthesis

An Online Banking Portal is a regulated banking institution's browser-delivered self-service channel, bound to the customer's real accounts at that institution (the money of record), through which an existing customer services the relationship without staff — observing account state, executing money movement, retrieving institution-produced documents, managing cards, and administering personal details — session by session, from a "bigger screen." The defining core is the triple: bank relationship of record + browser self-service servicing surface for an existing relationship + executed money movement. Registration, step-up authentication, payee management, scheduled payments, statements, card lifecycle, alerts, profile administration, loan servicing, in-portal application funnels, and operated-service signals are the standard mature capability set; regional rails, auth mechanisms, business absorption, and relationship breadth are the variant axes. The Type sits between the mobile app (same servicing core, different surface — joint review pending) and the digital banking application (complete digitally-conducted relationship), behind the customer-facing edge of the core banking system.
