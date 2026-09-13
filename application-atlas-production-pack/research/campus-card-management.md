# Research Notes — Campus Card Management

## Research Goal

Understand what a Campus Card Management application actually is, from real products and the industry's own professional body: what the central objects are, how credentials are issued and administered, what privileges a campus credential carries, how use at service points is evaluated and recorded, how accounts are funded, and where the boundary lies with adjacent Types (SIS, physical access control, stored-value wallets, student billing, housing).

## Initial Boundary (hypothesis before research)

- Expected core: institution-issued ID credential + cardholder records + service privileges (access, dining, stored value) + acceptance points + lifecycle administration.
- Likely confusions: physical access control systems (door side), Student Information System (affiliation source), stored-value/digital wallets (payment mechanics), Student Billing (charge posting), Campus Housing Management (residence access + meal plans), Digital Credential Platform (false friend — "credential" means academic achievement there, not an access/payment instrument).

## Research Questions

1. What is the central object — the card, the cardholder, or the account?
2. What privileges/entitlements does a campus credential carry, and which are definitional vs optional?
3. How does issuance work (identity vetting, photo, production, mobile provisioning)?
4. How is a use at a service point evaluated and recorded (online vs offline, allow/deny, transaction record)?
5. How are privileges funded and provisioned (deposits, meal plans, activity flags)?
6. What integrations are standard (SIS, housing, POS, door access, vending/laundry/print, banking)?
7. What roles operate the system (card office, dining/cashier, admins, cardholders)?
8. What exceptions matter (lost/stolen cards, temporary cards, offline operation, recarding)?
9. Where is the boundary with PACS, SIS, wallets, billing, housing?

## Representative Products

| Product | Vendor situation | Why sampled |
|---|---|---|
| Illumia (CS Gold / Transact campus lines) | CBORD and Transact Campus merged and rebranded as Illumia (Roper subsidiary); claims 1,111+ institutions, 12M students served | North American market leader; ID/card services + campus commerce + dining |
| Secanda (SECANDA ID / Cashless / MICANDA POS) | German RFID campus-card vendor (30 years in RFID) | European cross-check; education = identification + building access + cashless payment |
| NACCU (National Association of Campus Card Users) | Industry association (founded 1993) for campus credential professionals | Tier-1 industry documentation: Terminology Guide, blog, career/board context; defines the profession's own vocabulary |

Attempted but unreachable (recorded as sourcing limitation): TouchNet OneCard (403 ×2), Atrium Campus (403 ×2), Heartland Campus Solutions (transport error), Wikipedia "Campus card" (timeout ×2). NACCU sponsor roster confirms these vendors exist in the market (Atrium and Illumia at "Pinnacle" sponsor level; Secanda, Acre Security, Allegion, Agilysys, ColorID, HID also sponsors).

## Sources

- NACCU Terminology Guide — https://www.naccu.org/terminology-guide (fetched 2026-09-06; full A–Z captured)
- NACCU — "Demystifying Campus Cards: What We Wish Everyone Understood" — https://www.naccu.org/news/demystifying-campus-cards-what-we-wish-everyone-understood (2025-09-05 post; fetched 2026-09-06)
- NACCU — "What One Person Card Offices Reveal About the Modern Campus Card Office" — https://www.naccu.org/news/what-one-person-card-offices-reveal-about-the-modern-campus-card-office (2026-07-15 post; fetched 2026-09-06)
- Illumia — Campus Access Management and Safety (ID and Card Services) — https://illumiatech.com/solutions/higher-education/campus-access-management-safety (fetched 2026-09-06; cbord.com/products/cs-gold redirects here)
- Illumia — Commerce (Higher Education) — https://illumiatech.com/solutions/higher-education/commerce (fetched 2026-09-06)
- Illumia — Food, Nutrition, and Dining Services — https://illumiatech.com/solutions/higher-education/food-nutrition-dining-services (fetched 2026-09-06)
- SECANDA — https://www.secanda.com/en/ (fetched 2026-09-06)
- NACCU home page (sponsor roster, career center job titles) — https://www.naccu.org/ (fetched 2026-09-06)

Evidence layers used below: **A** = directly observed on a specific source; **B** = cross-product/industry commonality; **C** = canonical inference.

## Source Observations

### NACCU Terminology Guide (industry association — Tier 1)

Key observations (evidence A for the industry's own definitions; B when NACCU states commonality):

- **Cardholder**: "Any individual who is issued a campus credential (e.g. plastic card, mobile card or wearable) and participates in the plans, services, and activities regulated by the program." → the cardholder is the central person record; credential form is explicitly multi-format.
- **Credential**: "Represents the various types of campus card formats including plastic card, mobile card and wearables used for verifying a person's identity."
- **ID Card / One-Card System**: "In a campus one-card system, a single ID card is used for multiple purposes such as meal plans, flexible spending, facility access, library circulation, and more." One-Card System definition: "a wide range of services are available and accessible to cardholders via a single ID card… ID verification, meal plans, flexible spending accounts, library access, facility access, event access/ticketing, vending, laundry, copiers, time and attendance, and more." Institutions without one-card systems "may require patrons to carry several cards."
- **Card Lifecycle Management (CLM)**: "Various states of a cardholder's credential(s) such as active, lost/stolen, damaged, provisioned, suspended, or removed."
- **Card Production**: "vetting a cardholder's identity, taking a photo, printing and testing an ID card, and issuing it to a cardholder… 3 to 5 minutes"; some institutions accept photos via web/email beforehand.
- **Identity Vetting/Proofing**: "verifying a person's identity by cross checking… institutional databases and secondary forms of ID… critical… before issuing an ID card to prevent identity theft." Also: "ID cards are considered identity credentials and many campus ID card offices provide essential identity vetting and proofing services."
- **Transaction**: "The record created by and stored on a campus card system when a card is used to make a purchase, enter a door or facility, or other activity… time and date… cardholder's primary ID number, the card number, the terminal or card reader… the amount… and an indication if the transaction was valid or denied… flags… online or offline… swiped or manually entered… some POS systems also include… menu items."
- **Transaction Processing**: "initiated by a card swipe (or manual entry), evaluated by the system, either allowed or denied, and subsequently stored… update appropriate cardholder account and transaction files." Online = real-time host validation; offline = local database at reader, uploaded later.
- **Online vs Offline**: online readers "can operate in an offline mode if communications are disrupted, temporarily storing transaction data until communications are restored." Legacy offline systems stored balances on the card (debit/"junk" stripe) — "rapidly being phased out and replaced with online applications."
- **Declining Balance Account/Debit Account**: "pre-deposited amount of funds that declines as the card is used… A single cardholder may have one or more declining balance accounts (e.g., meal plan, flexible spending, vending)… replenished… at a point of sale terminal, kiosk, or online application." Board meal plans = special declining balance where unit = meal.
- **Declining Balance Plan**: rules — "beginning and end dates, rules for when the plan can be used in different locations, and maximum limits on individual transactions or daily transaction limits."
- **Board Plan**: set number of meals per period; deducted per dining-hall entry; unused usually forfeited.
- **Meal Plan / Meal Equivalency**: upfront purchase; equivalency trades a meal for value in cash operations; "Meal plans are often coupled with housing charges in what are typically referred to as room and board rates."
- **Flexible Spending Account**: campus debit account for "dining services, vending, copier, and laundry as well as bookstore and other retail services. Some… accepted at off-campus merchants. Schools commonly brand their flexible spending accounts with a marketable name."
- **Activity/Event flags**: "verify status or membership… if a fee must be paid to use health or fitness facilities, the campus card system would set activity/event flags on student records where the fees have been paid. Then a simple card swipe… would quickly check to verify if a student was eligible… flags can be configured for a specific date range… or… a certain number of uses."
- **Online Deposit**: "allow cardholders to replenish a debit account by logging on to a web application and using a credit card"; ACH/eCheck also used for deposits (lower fees, ~48h settlement, not guaranteed).
- **Credit Limit / credit accounts**: "Most campus card financial applications use debit accounts where funds must be available before they can be used… Some institutions do allow for credit accounts where the balance begins at zero and is then drawn into the negative… most commonly used with departmental accounts."
- **Merchant / Commission Rate / Settlement**: merchants accept the campus card (usually flexible spending); commission charged per transaction; settlement pays merchants (checks or electronic deposits) with a settlement statement; off-campus merchant program = "the campus transaction system acts as a card processor"; self-operated vs integration-partner models.
- **Door Access Control**: "When integrated with campus card systems, the ID card can act as the authorization device for entry… These systems also have extensive logging and reporting… Door access systems may be dedicated systems or a module of a broader campus card system." Door schedules define when doors unlock, when access plans are active, when alarms monitor.
- **Interface**: "Campus card systems are commonly interfaced to many other university systems… A common interface, present in almost all campus cards systems, is the interface to the university student information systems to allow updates on new students and changes in student status."
- **Applications**: Laundry (reader + multiplexor controls washers/dryers, debits account), Library (circulation; barcode→magstripe→RF evolution), Copier, Pay for Print (swipe at release station → deduct → release jobs), Vending (MDB bus; cash vs card pricing; commissions), Time and Attendance (swipe records shift start/stop).
- **Unattended Transaction**: vending/copier/laundry/kiosk; "higher level of risk for fraud since there is no cashier… in most cases the value… is relatively low."
- **Temporary Card**: issued to replace lost card; "most or all accounts and privileges of the permanent card are transferred to the temporary card upon issuance and deactivated on the misplaced permanent card."
- **Conference Cards / Non-photo ID**: serialized low-cost credentials for short-term groups; separate number ranges; some recycled.
- **Recarding**: issuing new cards to all/a large portion of the population to upgrade technology or format; requires reader/software conversion.
- **Mobile card / Pass / Provisioning / Wallet / Wearables**: mobile credential applied to phones/watches/wearables; provisioning = adding it; edge device readers unencrypt card number. Apple/Android device definitions (Apple Wallet, NFC).
- **Banking Program**: ID card integrated with a commercial bank account (PIN-based via debit networks, or signature-based via credit networks); revenue stream to school.
- **Card Format**: site code, card number length, issue code; ISO/IIN numbering for institutions with banking programs.
- **Multi-tenant vs single-tenant**: cloud deployment choice; "Some schools may not allow cloud systems in a multi-tenant environment."
- **PCI-DSS / PA-DSS / SAQ**: compliance machinery when credit cards are processed.
- **Disaster Recovery Plan**: continuity for the card system (redundant servers, offline transaction processing).
- **Schedules**: POS terminal schedules define meal periods/menus/pricing; door schedules define unlock times and access-plan windows; weekly or calendar-driven.
- **Transaction Response time**: "should average only a second or two per transaction" (qualitative industry guidance, not a standard).

### NACCU blog — "Demystifying Campus Cards" (2025-09-05)

- "The campus credential is truly the **gateway to life on campus**… It unlocks residence halls, pays for meals, verifies ticket purchases for campus events, enables printing, and provides access to transportation and recreation facilities."
- Mobile credentials/digital IDs: "moved beyond the wallet and into the digital lives of students."
- Data: "Every tap, swipe, or scan provides valuable insights into student behavior, campus engagement, and service utilization" → retention-risk signals, traffic patterns, safety logs, resource optimization.
- NACCU founded 1993; "the only member association dedicated to serving professionals who manage campus identification programs in higher education."

### NACCU blog — "What One Person Card Offices Reveal" (2026-07-15)

- The campus card office today is an **operations** function, not just ID production: "Construction projects. Access control. Financial systems. Student support programs. Mobile credentials. Merchant services. Process improvement. Emergency planning."
- "The campus credential touches identity, access, payments, dining, housing, recreation, events, and student services."
- Card offices increasingly involved early in construction projects (access control, credentialing planned during design).
- Programs observed: off-campus merchant programs, food-insecurity support via credential initiatives, dining partnerships, mobile-first strategies.
- Card offices typically sit under Auxiliary Services (career listings: "Auxiliary Services for Meal Plans & Cardinal Card Office", "Manager, Campus ID System").

### Illumia (CBORD + Transact merged; NA market leader — Tier 2)

- ID and Card Services: "A single credential that powers the campus experience."
  - "Multi-functional credentials for access, dining, events, parking, vending, and more"
  - "Multiple credential options: physical cards, mobile IDs, and biometrics"
  - Contactless technology; customizable card designs and system fields
  - "Robust reporting tools to track card use and student engagement"
  - "Support for on- and off-campus purchases"
  - Self-service: "credential resets, photo updates"
  - Security: "Instant lockdown capability", "deactivate lost credentials", MFA/biometrics for higher-risk facilities
- Mobile Credential product sheet: "NFC-enabled mobile credential for Apple, Samsung, and Google Wallet."
- Commerce: "cloud-based campus commerce system"; "Support for meal plans, stored value accounts, credit cards, and contactless payments"; fixed/mobile/self-service registers; centralized menu/pricing/location configuration; real-time sales/inventory visibility; loyalty/incentives.
- Dining: dining payments "across in-person, mobile, and self-service environments"; dining-management side (menus, nutrition, production) is a connected but distinct surface.
- Integration partners: Allegion, Assa Abloy, Genea, Alcatraz (access control); Aramark, Sodexo, Compass, Elior (food service operators); Nutrislice etc.
- Scale claims (marketing): 12M students/year, $53B transactions annually, 1,111+ institutions, 99.9% uptime.
- CS Gold 9: AI-powered natural-language insights over card-system data (product sheet reference).

### SECANDA (German vendor — Tier 2, European check)

- Positioning: "One secure ID – Many possibilities"; "solutions for managing your identities, contactless payment and access management."
- Education solution = "Identification, Access to buildings, Cashless payment."
- Product decomposition: SECANDA ID (identity/student-employee management), SECANDA CASHLESS (cashless payment), MICANDA POS (payment/fixed-pricing/vending terminals), NetPrinting, Access Control & Lockers, Infoterminal, Balance Check Terminal, Loaders (value loading), Counting Terminal, RFID cards & tags / card printers, Integration Interfaces, Digital Campus.
- Same verticals beyond education: industry (HR + parking + cashless + printing), healthcare, leisure & events (identification + event access + cashless + self-registration).
- Confirms the European shape: identification + building access + cashless spending, with meal-plan machinery much less prominent than in the NA sample.

## Cross-product Comparison

| Dimension | NACCU (industry view) | Illumia (NA leader) | Secanda (EU) |
|---|---|---|---|
| Central object | Cardholder + credential + plans/accounts/privileges | "single credential that powers the campus experience" | "One secure ID – many possibilities" |
| Privilege set | ID verification, meal plans, flexible spending, facility access, library, events, vending, laundry, copiers, T&A | access, dining, events, parking, vending; meal plans + stored value + credit cards | identification, building access, cashless payment, printing |
| Credential forms | plastic, mobile, wearables | physical cards, mobile IDs, biometrics | RFID cards/tags (plastic focus) |
| Acceptance surfaces | readers/edge devices, POS terminals, unattended (vending/laundry/copier/print) | fixed/mobile/self-service POS; door readers | payment/vending terminals, access control, printers |
| Lifecycle | CLM states: active, lost/stolen, damaged, provisioned, suspended, removed | instant deactivation of lost credentials, lockdown | implied by ID management (not detailed on fetched pages) |
| Funding | deposits (POS/kiosk/web, card/ACH), plans, activity flags | meal plans, stored value, credit cards | loaders, cashless accounts |
| Institutional integration | SIS interface "present in almost all campus card systems" | 300+ partners (access hardware, dining operators) | integration interfaces |
| Data/reporting | transaction records; engagement insights | reporting, dashboards, AI insights | — |
| Merchant economy | on/off-campus merchants, commissions, settlement | on- and off-campus purchases | — |

**Convergence (B/C):** all three sources agree the Type is organized around one institution-issued credential bound to a person, carrying multiple service privileges, used at evaluated service points, administered centrally. The privilege *mix* varies by region/segment (NA: meal plans + flexible spending dominate; EU: identification + access + cashless), which supports keeping the privilege set out of the defining core.

## Canonical Model (C)

```text
Institution-issued campus credential (plastic / mobile / wearable)
  bound to an identified cardholder (campus affiliation)
    └── privileges the credential carries
        ├── identity verification (photo/name/status)
        └── service entitlements (access, dining, spending, … — mix varies)
    └── evaluated, recorded use at service points
        └── transaction record (who / where / when / what / allowed-denied)
    └── centrally administered credential lifecycle
        (issue → use → replace/suspend → revoke)
```

L0 (defining invariant — minimal):
1. institution-issued credential bound to an identified cardholder
2. the credential as the person's instrument for identity verification and institution-defined service privileges
3. evaluated, recorded use at service points (allow/deny + transaction record)
4. centrally administered credential lifecycle

L1 (common mature structure): stored-value/declining-balance accounts; meal plans (board/debit/equivalency); door-access integration; SIS interface; card production + identity vetting; self-service portal/app (balances, deposits, lost-card reporting, photo upload, mobile provisioning); merchant program with commissions/settlement; mobile credentials/wallet passes; unattended applications (vending MDB, laundry, copier, pay-for-print); activity/event eligibility flags; temporary/conference cards; recarding; reporting/engagement analytics; card-office role model.

L2 (variant/optional): banking-program integration; credit (negative-balance) accounts; off-campus merchant programs (self-operated vs partner); offline/stored-on-card architectures (legacy, phasing out); biometrics/UWB/PKOC; time & attendance; library circulation; parking/events; multi-tenant cloud vs on-prem; parent/third-party deposits; food-insecurity programs; regional privilege mixes (NA meal-plan-centric vs EU access+cashless-centric); vertical adaptations (corporate, healthcare, senior living, K-12, leisure/events).

L3 (vendor-specific, stays here): CS Gold 9 AI insights; NetMenu; SECANDA Manager/Cashless/MICANDA POS/Infoterminal/Loaders/Counting Terminal product names; Illumia scale claims (12M students, $53B, 1,111+ institutions, 99.9% uptime); Reusables tap-to-reuse ID integration (Pomona College case); NACCU SAGs self-assessment program.

## Historical / Market-Sample Check (§24 applied)

- Older/regional: magnetic-stripe-only systems, offline "debit stripe" (junk stripe) systems where the balance lived on the card — still satisfy L0 (credential + privileges + evaluated use + lifecycle); NACCU notes these are being phased out, i.e., architecture is not definitional.
- Regional: Secanda (Germany) shows the same structure with a different privilege mix (no NA-style meal-plan machinery on its education page) → meal plans cannot be in L0.
- Platform-native: mobile-first campuses (wallet passes, no plastic) still satisfy L0 → physical card cannot be in L0.
- Small institutions: access-only or dining-only card programs still satisfy L0 (privileges may be a subset) → multi-service breadth is the *philosophy* (one-card), not the invariant.
- Chinese-style campus "all-in-one card" systems (not directly fetched in this pass) are widely described as the same structure; not asserted in the final document beyond the general regional-variant statement.

## Vendor-specific Findings

- Illumia: CS Gold 9 AI Q&A over card data; mobile credential for Apple/Samsung/Google Wallet; instant lockdown; biometric options; $53B/12M/1,111+ marketing stats.
- Secanda: hardware-centric decomposition (loaders, counting terminals, balance-check terminals); MICANDA POS family; strong locker/access-control pairing.
- NACCU: SAGs (Standards and Self-Assessment Guidelines) as a program-assessment tool; The Vault resource library; terminology stewardship.

## Boundary Findings

- **vs Physical Access Control System (PACS)**: NACCU explicitly allows door access to be "a dedicated system or a module of a broader campus card system." The differentiator is the center of gravity: PACS centers on doors/controllers/alarms; campus card centers on the cardholder and their multi-service privileges. Remove the person-centered multi-service privilege layer and keep only door permissions → PACS.
- **vs Student Information System**: SIS is the affiliation system of record; the card system consumes it ("present in almost all campus card systems" — NACCU). Remove the credential and acceptance layer → SIS.
- **vs Digital Wallet / Stored Value Wallet**: campus card accounts are institution-scoped, closed-loop, affiliation-bound, and bundled with identity + access privileges. Remove institution scoping and the identity/access layer → a wallet.
- **vs Student Billing System**: billing posts charges to student accounts (e.g., room & board); the card system captures point-of-service events and may hand charges off. Remove the credential/acceptance layer → billing.
- **vs Campus Housing Management**: housing owns room assignment/occupancy lifecycle; the card system consumes housing status for residence-hall access and couples meal plans with housing charges. Remove the credential → housing.
- **vs Digital Credential Platform**: false friend — "credential" there means verifiable academic achievement records; here it means an identity/access/payment instrument. No overlap in objects or workflows.
- **vs Event Credential/Badge Management**: conference cards exist inside campus card programs (NACCU), but event badging is event-scoped and transient; campus card is institution-scoped and persistent.
- **"去掉什么就变成另一个 Type" 判据**: remove the multi-service privilege layer → PACS or a pure ID badging tool; remove the institution/affiliation scoping → a wallet/loyalty scheme; remove the credential & acceptance layer → SIS/billing; remove identity verification → a pure stored-value card scheme.

## Uncertainties

- TouchNet OneCard, Atrium, Heartland documentation unreachable (403/transport errors) — the vendor sample rests on Illumia + Secanda; cross-product claims lean on NACCU industry documentation, which is itself a strong cross-member source but is North-America-centered.
- Wikipedia unreachable — historical depth (1970s–80s origins) not directly evidenced; kept out of the final document.
- Exact numeric parameters (deposit minimums, response-time standards, plan forfeiture rules) — NACCU gives qualitative guidance only; no precise numbers asserted in the final document.
- Meal-plan/housing billing coupling described as "often" by NACCU — kept qualitative.
- Mobile-credential wallet-platform details (which institutions, which tiers) — vendor marketing level only.

## Final Synthesis

A Campus Card Management application is the institution-side system that administers the campus credential program: it binds institution-issued credentials (plastic cards, mobile passes, wearables) to identified cardholders, grants and revokes the service privileges those credentials carry (identity verification plus entitlements such as building access, meal plans, and spending accounts), evaluates and records every use at campus service points, and manages the credential lifecycle (issue, replace, suspend, revoke) together with the funding, merchant-settlement, and reporting machinery around it. The defining core is deliberately small; the modern feature mass (meal plans, stored value, door integration, mobile wallets, merchant programs, analytics) is standard market structure, not definition. The Type's identity comes from the union of identity + privilege + acceptance + lifecycle under one institution-scoped administration — remove any one of those and the remainder becomes a different Type (PACS, wallet, SIS/billing, or pure badging).
