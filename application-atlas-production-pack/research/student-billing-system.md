# Research Notes — Student Billing System

Research date: 2026-09-09

## Research Goal

Understand what institution-side student billing software actually is and how it works: its core objects (student account, charge, statement/bill, payment plan, payment, refund), its lifecycle (assess → bill → collect → reconcile → refund), its rules (due dates, aid application, delinquency consequences), the roles involved (bursar/student accounts, business office, students/families, sponsors), and where its boundaries sit against neighboring Types (Financial Aid Management, Enrollment Management, SIS/School Management, Higher-Ed Administration, Campus Housing, Campus Card, and the generic §08 money Types: Billing Platform, Invoicing Application, Accounts Receivable Management, Payment Processing).

## Initial Boundary

Initial hypothesis at start of research:

- Student Billing System = the institution's receivable system for its students: charges assessed against enrolled students (tuition, fees, housing, and other campus charges), statements/bills presented, payments collected (including installment plans), financial aid applied as credits, refunds issued, balances tracked to resolution.
- Most likely confusions:
  - a module of an SIS / higher-ed administration system rather than a Type of its own
  - Financial Aid Management (awards vs charges; the disbursement handoff)
  - Enrollment Management (commitment document assembles charges + collects deposit; billing owns collection over time)
  - generic Billing Platform / Invoicing / AR software (§08) — is "student billing" just an industry-tuned variant?
  - Payment Processing Platform (rails vs ledger)
  - K-12 public-school fee/activity-fund systems (SchoolCash-class) — same fee-collection surface, different center
- Market structure guess: (a) higher-ed payments/tuition-management platforms (TouchNet/Transact, Nelnet Campus Commerce), (b) K-12 private-school tuition management (TADS, FACTS, Blackbaud), (c) SIS-embedded Student Accounts modules (Anthology/Ellucian, Workday), (d) K-12 public fee management (KEV Group/SchoolCash). All four needed sampling.

## Research Questions

1. What are the core objects? (student account/ledger, charge/assessment, statement/eBill, payment plan, payment, refund/credit balance, sponsor account?)
2. What is the canonical workflow from charge to resolved balance?
3. Where do charges come from (registration/tuition, fees, housing, meal plans, parking, athletics, incidentals)? Is tuition definitional?
4. How do payment plans work (institution-administered vs vendor-managed; semester plans, past-due plans, long-term plans, international plans)?
5. How does financial aid integrate (aid credited to the account; anticipated aid; auto-apply)?
6. What does the student/family see and do (bill view, account activity, pay, authorized payers, refund method choice)?
7. What roles exist (bursar/student accounts, business office, cashiering, sponsors, finance/GL)?
8. What rules matter (billing schedules/due dates, late consequences, delinquency→enrollment stakes, refund compliance, tax statements)?
9. How do K-12 and higher-ed realizations differ (tuition contract + installments vs per-period billing)?
10. Where is the seam with SIS/ERP (student data in, GL out), financial aid (awards in), housing/campus card (charges in)?
11. Is this Type distinct from generic billing/invoicing/AR — and what is the discriminator?
12. Does the K-12 public fee/activity-fund pole (SchoolCash-class) belong inside this Type or mark its boundary?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Nelnet Campus Commerce (campuscommerce.com) | higher-ed payments/tuition-management platform | deep product pages for Tuition Management (Payment Plans, Billing & Payments, Sponsor Billing, Refunds) + Business Office audience; the "student account" language explicit |
| FACTS (factsmgt.com, A Nelnet Company) | K-12 private/faith tuition management + accounting (US + AU/NZ) | deep pages: Payment Plans, Incidental Billing & Prepay Accounts, Advanced Accounting (AR subsidiary ledger), aid auto-credit; AU realization for regional check |
| TADS Tuition & Billing (VenturEd Solutions) | K-12 private tuition management sold beside Contracts & Deposits | direct evidence of the billing-vs-enrollment-commitment product split (root-level only; subpages 403) |
| Anthology Student — Student Accounts module (+ 1098-T Processing) | SIS-embedded pole | Tier-1 help-center structure: Student Accounts as a first-class department module beside Financial Aid; 1098-T as a separate release stream |
| KEV Group / SchoolCash (kevgroup.com) | K-12 public district fee + activity-fund accounting (boundary pole) | the no-tuition pole: fees, payments, school-level fund accounting; documents where the per-student account dissolves |

Historical / market-sample breadth: the K-12 public pole (KEV) and the AU realization (FACTS AU) avoid US machinery; the paper-era bursar office (student ledger card, term bill, payment receipts, refund vouchers, dunning letters) and the K-12 tuition coupon book are the pre-digital baselines used for the historical check.

## Sources

Fetched 2026-09-09 (WebFetch; markdown unless noted):

- FACTS homepage — https://factsmgt.com/ (Tier 2)
- FACTS Financial Intelligence — https://factsmgt.com/intelligence/financial/ (Tier 2)
- FACTS Accounting, Billing & Payments feature page — https://factsmgt.com/features/accounting-billing-payments/ (Tier 2)
- FACTS AU Payment Plans and Billing — https://factsmgt.com/features/payment-plans-billing-au/ (Tier 2)
- Nelnet Campus Commerce homepage — https://campuscommerce.com/ (Tier 2)
- Nelnet Tuition Management — https://campuscommerce.com/payment-solutions/tuition-management/ (Tier 2)
- Nelnet Billing & Payments — https://campuscommerce.com/payment-solutions/billing-and-payments/ (Tier 2)
- Nelnet Payment Plans — https://campuscommerce.com/payment-solutions/payment-plans/ (Tier 2)
- Nelnet Refunds — https://campuscommerce.com/payment-solutions/refunds/ (Tier 2)
- Nelnet Sponsor Billing and Payments — https://campuscommerce.com/payment-solutions/sponsor-billing-payments/ (Tier 2)
- Nelnet Business Office — https://campuscommerce.com/business-office/ (Tier 2)
- TADS homepage — https://www.tads.com/ (Tier 2, root level)
- Anthology Student Help home (module map) — https://help.anthology.com/CNS/26.2/WebClient/Content/TopNavHome.htm (Tier 1 structural; fetched as html to recover tile URLs)
- Anthology Student Accounts module page — https://help.anthology.com/CNS/26.2/WebClient/Content/tile-sa.htm (Tier 1; one-sentence scope, TOC JS-gated)
- Anthology Student Documentation Suite index (incl. 1098-T Processing release stream) — https://help.anthology.com/Content/DocSets/CNSDocSet.htm (Tier 1 structural)
- KEV Group homepage — https://www.kevgroup.com/ (Tier 2)

Unreachable / abandoned (per network-retry discipline):

- TouchNet — https://www.touchnet.com/ returned 403 (1 attempt; abandoned)
- Transact — https://www.transact.com/ now serves a different company (Pathwise K-12 transportation/compliance); the campus-commerce domain is gone (recorded as a market-structure observation, no product claims)
- TADS subpages (e.g. /solutions/tuition-and-billing/) — 403 (bot protection; consistent with the 2026-09-07 enrollment pass; TADS kept at root level)
- Blackbaud Tuition Management — https://www.blackbaud.com/products/blackbaud-tuition-management 404 (consistent with prior passes; abandoned)
- Ellucian product URLs guessed (student-finance, student-accounts) — 404 ×2 (abandoned; the financial-aid pass's Ellucian evidence used only)
- Nelnet help center (nbshubhelp.com) — login-gated
- Anthology Student Accounts topic tree — JS-gated; only the module-scope sentence retrievable; ERD available only as a 103 MB zip (not fetched)

Evidence quality note: this pass is anchored on official product pages (Tier 2) plus Tier-1 structural documentation (help-center module map, doc-suite index). Deep operational help articles (exact state machines, default values, limits) were not retrievable. Vendor numeric claims on marketing pages are recorded below as claims, never as facts.

## Product Observations

### Nelnet Campus Commerce (pole: higher-ed payments/tuition-management platform)

Evidence: A (directly observed on official pages).

Key observations:

- Category structure: **Tuition Management** (Payment Plans, Billing & Payments, Sponsor Billing and Payments, Refunds, Notify) + **Integrated Commerce** (Storefront, Cashiering, Checkout, Payment Forms) + Merchant Services. Audiences: Business Office, IT, Student Services, Enrollment Management.
- **Billing & Payments**: "A secure and convenient way for students to view their bill, access current account activity, and make payments on the go." "Send automated, consolidated bills that include everything from tuition and housing to parking and athletic fees. Plus, allow students to assign authorized payers to their account." "A home for all payments made on student accounts, plus integration with your ERP." Real-time payment updates ("payments, account activity, and agreements are all updated instantaneously"); billing notifications (text/email when bill is due); dashboard to track and report all payments; branded/customizable dashboards and forms.
- **Payment Plans**: "Tuition payment plans allow costs to be split into manageable monthly payments." Variants documented: *Actively Managed Payment Plans* (budget tuition/fees over the semester; the vendor "follow[s] up on delinquent payments", promotes plans, full-service support); *International Payment Plans* (pay in home currency); *Past Due Payment Plans* ("when students fall behind on payments or have a debt to repay… provide current and former students flexible payment options to get them back on track for enrollment and reduce outstanding receivables"); *Long-Term Payment Plans* ("flexibility of at least 12 months and up to 3 years"). Business-office page adds a "pre-collections process" for students who fall behind.
- **Refunds**: "A fast and flexible way to disburse Title IV refunds. Students can choose how they receive their refunds: through ACH, prepaid card, or paper check." Refunds management ("ensuring the right funds are issued to the right students before they are processed"); Title IV compliance ("meet refund processing times and offer fair distribution methods"); student status tracking "from distribution to deposit"; fraud prevention machinery.
- **Sponsor Billing and Payments**: employers/organizations billed instead of students ("as more employers offer tuition benefits…"); centralized sponsor account management, customized billing cycles per sponsor, pre-scheduled reminders, ERP sync.
- **Cashiering**: "Automate in-person student payments… In one, campus-wide system." **Checkout**: embedded branded checkout for third-party integrations and single real-time payments.
- Staff titles in quotes: "Director of Student Accounts" (Saint Joseph's University), "Manager Student Accounts and Cashiering" (Palomar College), "Director Student Accounts Receivable" (DMACC), "Director of Student Financial Services" (University of Redlands). One-off due-date adjustment quote: "The ability to adjust a student's due date on a one-off basis is so helpful…".
- Enrollment stakes framing: "Help students stay enrolled and on track" (Business Office); KCKCC partnership "giving those with past due balances a way to continue their education."
- Family portal: mycollegepaymentplan.com ("If you have a payment plan with an institution…"). Security posture: PCI Level 1, SSAE 18. ERP integration "with all major ERPs."
- Vendor metric claims: 1,300+ institutions; payments processed annually in the millions.

### FACTS (pole: K-12 private/faith tuition management + accounting; US + AU/NZ)

Evidence: A.

Key observations:

- Positioning: K-12 platform ("FACTS IQ" core + Admissions/Engagement/Financial/Success Intelligence). Financial Intelligence = "Payment plans, financial aid, and fundraising."
- **Payment Plans**: "Give families the flexibility to pay tuition over time with various payment plan configurations"; "Families can opt to spread out their tuition payments over time"; payments via ACH direct deposit, checks, debit/credit cards; "Auto-apply financial aid to tuition contracts/balances" ("Integration with FACTS' financial aid solution… Financial aid awards are automatically applied to tuition payment plans"); real-time dashboards "project accurate cash flow."
- **Incidental Billing & Prepay Accounts**: "Schools generate significant revenue beyond tuition. From extracurriculars, field trips, and lunches to scholarship and third-party program funding…"; "From technology to meals, childcare to field trip fees, streamline your incidental expenses and billing to families through a single system"; configurable billing schedules and due dates; automated reminders and payment tracking; prepay accounts; secure ACH/credit card.
- **Advanced Accounting**: "No matter what general ledger software you use, let FACTS become your accounts receivable subsidiary ledger"; "links general ledger entries to your bank accounts, institution accounts (charges), and adjustment reasons (credits) and houses all tuition and fee activity"; "One system to record all charges, credits, & payments"; audit preparation ("All charges, credits, and payments are housed in FACTS, producing accurate reporting").
- **Financial aid interplay**: "awards are automatically credited to a student's account, meaning approved financial aid is applied to tuition bills without extra steps."
- **Enrollment interplay**: "families can set up a payment plan during enrollment"; Enrollment Management "collect[s] contracts and sign[s] families up for payment plans."
- **Family side**: pay from the school app or family dashboard; mobile notification "New Billing Statement Available"; 24/7 portal access; AU page adds a FACTS Family/Parent Help Desk supporting families directly with payment queries.
- **Payment Forms**: collect/track payments "that fall outside tuition and fees" (event forms, permissions).
- AU realization (payment-plans-billing-au): "manages every tuition and invoicing charge from the first invoice to the final payment"; "School-Wide Invoicing — bring all non-tuition charges, from technology to excursions, into one system… a complete view of every family account"; direct debit and card payments; cash-flow dashboards.
- Security posture: PCI DSS Level 1, SSAE 18 audited. Vendor metric claims: 15K+ schools, 2M+ families, 7-minute average payment-plan enrollment, 2K+ schools on accounting.

### TADS Tuition & Billing (pole: K-12 private tuition management beside enrollment commitment machinery)

Evidence: A- (root level only; subpages 403).

Key observations:

- Product definition: "Tuition & Billing — Effortlessly manage payments, contracts, fees, grants, and discounts with an intuitive, all-in-one system that keeps school finances organized and saves time for families and staff."
- **Product split is the key evidence**: TADS ships **Contracts and Deposits** (enrollment commitment: "contract signing and deposit collection") as a separate product from **Tuition and Billing**, beside **Educate SIS**, Admissions, and Financial Aid. "Organizations adopt VenturEd Solutions to manage school admissions, enrollment, tuition management, financial aid, and payments."
- Audience: private/independent, international/boarding, faith-based K-12 schools. Vendor claims: 50+ years, 750k+ students served, 99% retention.
- Integration framing: "Integrate with popular SIS, Admissions, and Financial Aid software—including other VenturEd Solutions products."

### Anthology Student — Student Accounts module (+ 1098-T Processing) (pole: SIS-embedded)

Evidence: A for structure (Tier 1 help center); internals JS-gated.

Key observations:

- Official help home is department-oriented: Academic Records, Admissions, Career Services, Contact Manager, Faculty Workload, Financial Aid, Financial Aid Automation, Regulatory, **Student Accounts**, Student Experience, Student Services, System Administration. Student Accounts module scope: "The topics in this section are helpful for staff members who are responsible for Student Accounts."
- The student-money world is split across first-class modules: aid processing (Financial Aid / Financial Aid Automation), billing (Student Accounts), US regulatory content (Regulatory), and tax-statement processing (**1098-T Processing** — a separate release-notes stream with its own versioning, e.g. "Version 25.0.0"). The seams are documented structurally.
- Developer layer: REST APIs, service catalog, data model (ERD), Forms Builder, Workflow Composer, Portal — the SIS-embedded integration spine.
- Product context: Anthology Student 26.2 "with Regulatory US 26.9"; © Ellucian (post-acquisition).

### KEV Group / SchoolCash (pole: K-12 public district fee + activity-fund accounting — boundary case)

Evidence: A.

Key observations:

- Positioning: "K-12 School Accounting Software & Activity Funds… purpose-built for K-12 public schools across North America." "Connect fees, payments, and accounting in one centralized school finance system."
- Center of gravity: **school-level funds and accounting**, not a per-student account ledger: "full visibility from district to school to student"; school accounting solutions, payment & fee management, school disbursement solutions; bookkeepers, district finance offices, principals, coaches as roles; audit readiness (customer quotes cite Redbook and GASB-84 compliance, year-end closeout).
- Blind-spot framing (useful boundary evidence): "Traditional systems like ERPs and SISs weren't designed to manage school-level transactions, thus leaving gaps that cashboxes, spreadsheets, and personal payment apps quietly fill."
- Family side: "Pay any way, from anywhere… credit or debit, Apple or Google Pay, cash, check, online, in the office, or on the field." POS devices post "automatically to the right GL account."
- Integrations: "ERP + SIS + KEV form the foundation of complete financial visibility across school districts."
- Vendor claims: 1K+ districts, 28K+ schools.

## Cross-product Comparison

| Dimension | Nelnet Campus Commerce (HE) | FACTS (K-12 private, US+AU) | TADS (K-12 private) | Anthology Student Accounts (SIS module) | KEV SchoolCash (K-12 public, boundary) |
|---|---|---|---|---|---|
| Account holder | student account (+ authorized payers) | family account (tuition contracts) | family/school finances | student accounts (staff-managed) | school activity funds; student/parent payments at the edge |
| Charge sources | tuition, housing, parking, athletic fees, consolidated bills | tuition + incidentals (technology, meals, childcare, field trips, excursions) | payments, contracts, fees, grants, discounts | module-managed (internals JS-gated) | school fees, activity collections |
| Statement/bill | automated consolidated bills; bill-due notifications | billing statements ("New Billing Statement Available"); configurable schedules/due dates | (definition level) | module-managed | receipts/reports (fund-centered) |
| Payment plans | semester plans, actively managed, past-due, long-term (12mo–3yr), international (home currency), pre-collections | installment plans, actively managed, direct debit/card, plan sign-up at enrollment | tuition payment plans (product level) | module-managed | — (not the center) |
| Financial aid | business + financial aid offices manage billing together | aid auto-credited to the account / auto-applied to tuition contracts | grants/discounts managed in-product | Financial Aid is a separate module | — |
| Refunds | Title IV refunds; ACH/prepaid/check; student choice; compliance | (not surfaced on fetched pages) | (not surfaced) | module-managed | disbursements (school-side) |
| Third-party payers | sponsor billing (employers); authorized payers | third-party program funding; payment forms | — | module-managed | parents/public at events |
| Ledger/accounting | "home for all payments made on student accounts"; ERP integration | AR subsidiary ledger; GL entries ↔ bank accounts, institution accounts (charges), adjustment reasons (credits) | school finances organized | SIS data model; GL via ERP | school accounting + district GL |
| Delinquency | past-due plans, pre-collections, delinquent-payment follow-up | automated reminders; actively managed plans | (definition level) | module-managed | — |
| In-person payments | cashiering (campus-wide) | (not surfaced) | — | module-managed | POS devices in offices/fields |
| Tax/regulatory | Title IV refund compliance | PCI/SSAE posture | — | 1098-T Processing stream; Regulatory US module | GASB-84/Redbook (customer quotes) |
| Packaging | standalone payments platform beside the ERP/SIS | suite pillar beside SIS + admissions + aid | suite product beside Contracts & Deposits + SIS | SIS module beside Financial Aid | standalone district finance platform beside ERP+SIS |

Reading of the comparison:

- All five products share the same substrate: an institution-side money system whose **unit is the student/family account** (or, at the KEV pole, the school fund that student payments flow into), fed by **charges the institution assesses**, resolved through **presented bills and recorded payments**, and reconciled to the institution's **general ledger/ERP**.
- What varies: the charge mix (tuition-centric vs fee-centric), the payer (student vs family vs sponsor), the plan machinery (higher-ed semester plans vs K-12 tuition contracts), the regulatory weight (US Title IV/1098-T vs AU direct-debit regime vs public-district fund rules), and packaging (standalone platform vs suite pillar vs SIS module).
- The KEV pole is the informative boundary: it keeps fee collection and payments but centers school-level activity-fund accounting — the per-student account is no longer the organizing ledger. That is where this Type ends.

## Canonical Model

### L0 — Defining Invariant

Minimal structure without which the Type stops being recognizable as student billing:

1. **The student account as the running ledger of record** — a persistent, individually identified account per student (in K-12 billing realizations, effectively per family) held by the institution, accumulating charges, payments, credits, and aid application, and carrying a live balance at all times. Remove → a payment processor or one-off invoicing tool with no account memory.
2. **Institutional charge assessment against the enrolled population** — the institution defines its billable items (tuition and fees by academic period, plus campus-service charges) and posts them to student accounts, commonly sourced from other systems (registration, housing, campus services). The account holder exists because of enrollment, not because of a purchase. Remove → generic invoicing of arbitrary customers.
3. **The collection loop to a resolved balance** — the account is presented to the payer (statement/bill), payments are recorded against it (lump-sum or plan installments), and the balance is tracked to resolution — including returning credit balances to the student as refunds. Remove → a charge catalog nobody collects on, or a payment rail with no ledger.

Jointly-held is load-bearing: (1) alone = a spreadsheet ledger; (2) without (1) = an invoicing tool; (3) without (1)+(2) = a payment processor; (1)+(2) without (3) = a charge catalog with no money movement; (1)+(3) without (2) = generic accounts-receivable software.

Historical check (paper-era bursar office and K-12 tuition book): the student ledger card (running account), the term/fee bill presented to the family, payment receipts posted to the ledger, refund vouchers for credit balances, aid credits posted by the aid office, dunning letters for unpaid balances — all three legs satisfied with no software, no payment rails, no cloud. The K-12 public fee-collection pole satisfies the same legs with fees only — so **tuition is not definitional; "charges assessed by the institution against its enrolled population" is**.

### L1 — Common Mature Structure

Present across most sampled products; not definitional:

- statements/eBills — consolidated, itemized bills by period; bill-due notifications (text/email); statement-available notifications
- payment plans — installments over the term/year; institution- or vendor-administered ("actively managed"); past-due/recovery plans; long-term plans; international-currency plans
- student/family self-service — view bill, view account activity, pay online; authorized payers (students grant others permission to pay)
- financial aid application — aid/awards credited against charges (auto-apply to tuition contracts/balances); aid office and billing office working on the same account
- refunds/disbursements — credit balances returned to students; refund-method choice (ACH/prepaid card/check); status tracking; refund compliance where regulated
- notifications and reminders — bill-due, payment confirmation, delinquency follow-up/pre-collections
- reporting/dashboards — collections, outstanding balances, cash-flow projection, reconciliation, real-time payment reporting
- ERP/GL integration — the billing system as the AR subsidiary ledger; payments/charges synced to the institution's ERP; SIS integration for the population
- payment-method breadth — ACH/direct debit, cards, checks, cash, international currency; in-person cashiering
- security/compliance posture — PCI validation, SSAE-class audits, fraud prevention on refunds

### L2 — Variant / Optional Structure

Depends on segment, geography, regulatory regime:

- US higher-ed machinery: Title IV refund compliance (processing times, fair distribution), 1098-T tuition-statement tax processing, federal-aid disbursement interplay — regional (US) and stake-dependent
- sponsor/third-party billing — employers and organizations billed directly (tuition benefits); customized sponsor billing cycles
- K-12 tuition-contract shape — the payment plan as the tuition instrument, set up during enrollment alongside the enrollment contract; grants/discounts applied to the contract
- incidental billing and prepay accounts — non-tuition charges (meals, field trips, technology, childcare, excursions) and prepaid balances, dominant in K-12
- payment forms / storefront / checkout — collection surfaces for payments outside the billing cycle
- in-person cashiering as a campus-wide system
- holds/consequences on the student's standing for unpaid balances — the researched pages evidence the enrollment-stakes framing ("keep students enrolled", "a way to continue their education", "get back on track for enrollment"); precise hold mechanics (registration/transcript/diploma holds) are widely known in the market but were not directly documented in the reachable sources — kept qualified
- regional realizations — AU/NZ direct-debit regime with school-wide invoicing of excursions/technology; boarding/international schools; school-choice/SGO scholarship program administration (FACTS)
- public-district fee pole — fee collection without tuition, coupled to school-level activity-fund accounting (KEV pole; boundary, see below)

### L3 — Vendor-specific Structure

Stays in Research Notes only: Nelnet's plan-product names (Actively Managed / Past Due / Long-Term / International Payment Plans), Notify, Student Choice Refunds, QuikPay, Checkout, Project Horizon, mycollegepaymentplan.com; FACTS' Financial Intelligence / FACTS IQ packaging, Incidental Billing & Prepay Accounts, Advanced Accounting, Family Help Desk, ADF payback claims; TADS' Contracts & Deposits vs Tuition & Billing product split and Educate SIS pairing; Anthology's module names (Student Accounts, 1098-T Processing, Regulatory US) and Forms Builder/Workflow Composer; KEV's SchoolCash/ebase/ITR/ASBWorks family and Redbook/GASB-84 customer quotes; all vendor metric claims (1,300 institutions; 15K schools/2M families; 750k students; 1K districts/28K schools; 7-minute plan enrollment; $2M cash collection anecdote).

## Vendor-specific Findings

- Nelnet sells the plan machinery as vendor-operated services ("actively managed" — the vendor follows up on delinquent payments and staffs the service desk on the institution's behalf). FACTS documents the same posture in K-12 ("actively managed payment plans… without adding to your team's workload"). This service posture is common to both sampled payments platforms but is a packaging choice, not a defining structure — TADS/FACTS also support institution-administered plans.
- FACTS explicitly frames the billing system as the **AR subsidiary ledger** beside any GL — the clearest statement of the Type's accounting position: the student account population IS the institution's student receivable.
- TADS productizes the enrollment-commitment machinery (Contracts & Deposits) separately from billing (Tuition & Billing) — direct market evidence for the enrollment/billing seam recorded by the 2026-09-07 enrollment pass.
- Anthology/Ellucian structure confirms the SIS-embedded seams: Student Accounts vs Financial Aid vs Regulatory vs 1098-T as separately documented modules/streams.
- Market-structure observation: the Transact domain now serves an unrelated K-12 company (Pathwise) and TouchNet returned 403 — the historically prominent TouchNet/Transact student-accounts family could not be directly evidenced this pass; no claims made about it.

## Boundary Findings

- **vs Financial Aid Management**: the aid system owns awards and disbursement intent ("eligibility to fund release"); billing owns the account the money lands on. Direct evidence both directions: FACTS "awards are automatically credited to a student's account"; Nelnet "your business and financial aid offices… manage, organize, and accept online payments"; the aid pass recorded "sync with Student Accounts for seamless, auditable transactions." Award ≠ charge; the credit-to-account handoff is the designed seam.
- **vs Enrollment Management**: the commitment document assembles charges (tuition/fees/aid) and collects the deposit; billing owns invoicing, payment plans, and collection over time. Direct evidence: TADS ships Contracts & Deposits and Tuition & Billing as separate products; FACTS "families can set up a payment plan during enrollment" (the plan starts where the commitment ends). DISCHARGES the enrollment pass's student-billing flag from this side.
- **vs Student Information System / School Management System**: fees/billing exist as modules inside school systems (Fedena fees module per the school-management pass; Anthology Student Accounts module), but standalone tuition-management/billing products exist and are the market's dedicated layer (TADS, FACTS, Nelnet). The billing Type centers the money loop over the account population; the SIS centers the student record and school operations. The leaf stands as an independent Type realized both standalone and as modules.
- **vs Higher Education Administration System**: student money (billing + aid) is a module there; that pass itself recorded "student money (billing + aid) … separate leaf exists." Consistent — no conflict.
- **vs Campus Housing Management**: housing computes and schedules charges (terms, pro-rating, billing cycles) and exports them to the student account; the billing system collects. Downstream destination, per that pass's own boundary note.
- **vs Campus Card Management**: the card system captures point-of-service events and hands charges off; billing posts them to student accounts (e.g., room & board). Per that pass's boundary note.
- **vs generic Billing Platform / Invoicing Application / Accounts Receivable Management (§08)**: the discriminators are structural, not cosmetic — (a) the receivable population is the enrolled student body (families as effective payers in K-12), created by enrollment rather than by commercial transactions; (b) charges are assessed by institutional rule per academic period from multiple campus sources, not per sales transaction; (c) financial aid interacts with the balance as credits; (d) the balance carries enrollment stakes (delinquency threatens continuation); (e) the ledger is organized by student × period, not by invoice/customer. A generic billing platform lacks all five; a student billing system without them is just generic AR.
- **vs Payment Processing Platform (§08)**: rails vs ledger. The sampled platforms bundle processing (and sell it as a service), but the center is the account/ledger and the collection loop; processing is an embedded capability. A payment processor with no student account is below the Type.
- **vs K-12 public fee/activity-fund systems (KEV/SchoolCash pole)**: fee collection and parent payments match this Type's surface, but the center of gravity is school-level activity-fund accounting and district oversight — the per-student account is not the organizing ledger. Documented as the Type's boundary: remove the per-student/per-family account as the organizing structure and the product becomes school accounting software. If a directory leaf for that pole is ever added, it should be a separate Type (school activity-fund / district finance territory), not a variant of this one.
- **"Tuition management" market label**: the K-12 market's name for this Type's K-12 realization (TADS Tuition & Billing, FACTS Tuition Management, Nelnet tuition management). Same Type, different segment vocabulary.

## Uncertainties

- TouchNet/Transact (historically the largest US higher-ed student-accounts family) not directly evidenced (403 / domain redirect). The higher-ed pole rests on Nelnet Campus Commerce + Anthology structure; no claims made about TouchNet/Transact specifics.
- Anthology Student Accounts internals (forms, state machines, screens) JS-gated — module existence, scope sentence, and the 1098-T stream are Tier-1; everything else about that module is kept general.
- TADS subpages 403 — Tuition & Billing evidenced at product-definition level only; internal contract/fee machinery unknown.
- Hold mechanics (registration/transcript/diploma holds for unpaid balances) not directly documented in reachable sources; the enrollment-stakes framing is evidenced, the hold mechanism is not — kept qualified in both documents.
- Exact state names for account/charge/plan lifecycles are product-specific; no universal vocabulary asserted.
- Blackbaud Tuition Management and Ellucian product pages unreachable (404 ×3 total) — two major K-12/suite poles triangulated indirectly only.
- Refund machinery in the K-12 products was not surfaced on fetched pages (refunds documented in the higher-ed pole); refund depth in K-12 kept unasserted.
- Non-US higher-ed realizations (e.g., UK/EU student-finance bodies) not sampled; the AU K-12 realization is the only directly observed non-US pole.

## Final Synthesis

Student Billing System is the institution-side system of record for what its students owe and pay. Its defining core is three jointly-held structures: the **student account** as the running per-student/per-family ledger of charges, payments, credits, and aid, carrying a live balance; **institutional charge assessment** — the institution's billable items (tuition/fees by academic period plus campus-service charges) posted to those accounts, commonly sourced from registration, housing, and other campus systems; and the **collection loop** — bills/statements presented to the payer, payments recorded (lump-sum or plan installments), balances tracked to resolution, credit balances refunded. Around this core, mature products add statements/eBills, payment plans (including past-due and international variants), student/family self-service with authorized payers, financial-aid auto-credit, refund machinery, notifications, reporting/cash-flow dashboards, and ERP/GL integration as the AR subsidiary ledger. US regulatory machinery (Title IV refunds, 1098-T), sponsor billing, incidental/prepay accounts, tuition-contract shapes, and regional regimes are variants of segment and geography. The Type is realized as standalone payments/tuition-management platforms, K-12 tuition-management products beside enrollment-commitment machinery, and SIS-embedded Student Accounts modules. Its boundaries: financial aid feeds it credits (awards ≠ charges), enrollment management hands it committed families with deposits collected (collection over time lives here), housing and campus card feed it charges, the SIS supplies the population, the ERP/GL receives the accounting — and the K-12 public fee/activity-fund pole marks the outer edge where the per-student account dissolves into school-level fund accounting.
