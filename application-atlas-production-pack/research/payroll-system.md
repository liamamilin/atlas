# Research Notes — Payroll System

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a "Payroll System" actually is as an Application Type: what objects exist inside it, how a pay cycle flows through it, what its defining structure is (as opposed to what modern products merely commonly bundle), and where its boundaries lie against Time & Attendance System, HRIS/HCM, Global Payroll Platform (sibling leaf), Accounting Software, Compensation Management, and PEO/EOR services.

## Initial Boundary

Initial hypothesis (to be verified, not final):

- Core: an employer-operated system that pays employees — employee pay records, a recurring pay cycle, gross-to-net computation (earnings minus taxes/deductions), payment issuance, and pay records.
- The pay run over a pay period is likely the central unit of work; the employee pay record is likely the central object.
- Nearest neighbors: Time & Attendance System (§09 sibling — input provider), HRIS/HCM (§09 — record master), Global Payroll Platform (§09 sibling — possible overlap), Accounting Software (§08 — GL receiver), Benefits Administration (§09 — deduction elections), Compensation Management Platform (§09 — pay planning vs pay execution), PEO/EOR (service model, not software).
- Main unknowns: is tax filing/deposit definitional or common? Is direct deposit definitional? Is employee self-service definitional? Is contractor payment definitional? Is "Payroll System" vs "Global Payroll Platform" one Type or two?

## Research Questions

1. What is the central object, and what lifecycle does a pay run move through?
2. What setup must exist before the first run (company, employees, pay schedules, compensation, tax setup)?
3. What inputs feed a run (salary vs hourly, time imports, tips, commissions, one-off items)?
4. How does gross-to-net computation work (earnings, pre/post-tax deductions, statutory withholdings)?
5. How is payment executed (direct deposit, checks, other rails), and is payment execution definitional?
6. How does the tax loop work (withholding at run time, deposit, filing, year-end forms), and is it definitional?
7. What records does the system keep (register, pay stubs, history, year-end forms)?
8. What employee-facing surface exists (self-service), and is it definitional?
9. What roles and permissions exist (payroll admin, approver, employee, accountant)?
10. What corrections exist (off-cycle runs, retro pay, amendments)?
11. What integrations matter (time & attendance, HRIS, accounting/GL, benefits)?
12. How do regional regimes vary (US federal/state/local vs GCC vs India vs Canada), and does the core hold across them?
13. Where is the boundary against Global Payroll Platform, Time & Attendance, HRIS, accounting, comp management, PEO/EOR?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Philosophy / tier | Access result |
|---|---|---|
| Square Payroll | POS-embedded payroll for very small businesses (restaurants/retail/services); contractor-only variant; US | Product page + 2 Tier-1 help articles (run payroll; federal tax payments) fetched |
| Xero Payroll (powered by Gusto) | payroll embedded in cloud accounting; SMB; US edition (Gusto engine) | Product page with operational FAQ fetched (Tier 2) |
| Zoho Payroll | suite-native standalone payroll shipped as regional editions (GCC / Canada / India / USA); SMB | Multi-region product page fetched (Tier 2) |
| Rippling Payroll | HCM-platform-native payroll (single employee data spine); SMB→enterprise; US + separate Global Payroll product | Product page with operational FAQ + platform framing fetched (Tier 2) |

Considered/rejected: Gusto (direct site 403; capabilities partially observed through Xero's "powered by Gusto" page — treated as indirect evidence), ADP (403), Paylocity (JS-only), Sage (403), Patriot Software (403), QuickBooks Payroll (timeout). Enterprise-tier structures (ADP/Workday-class multi-entity payroll) are therefore under-sampled; assertion strength reduced accordingly.

## Sources

Tier 1 (official operational documentation, directly fetched):

- Square Support Center — "Run payroll for W-2 employees": https://squareup.com/help/us/en/article/5855-run-payroll
- Square Support Center — "Make federal payroll tax payments": https://squareup.com/help/us/en/article/5683-square-payroll-federal-tax-filings

Tier 2 (official product pages with operational FAQs, directly fetched):

- Square Payroll — https://squareup.com/us/en/payroll
- Xero Payroll — https://www.xero.com/us/payroll/
- Zoho Payroll — https://www.zoho.com/payroll/
- Rippling Payroll — https://www.rippling.com/en-US/payroll

Source-access limitation: Gusto (gusto.com, support.gusto.com JS-rendered/403), ADP (403), Paylocity (JS-only), Sage (403), Patriot (403), QuickBooks Payroll (timeout) were unreachable from the research environment on 2026-09-06. Gusto's role is partially evidenced through Xero's official "Xero Payroll, powered by Gusto" page. No precise operational details are asserted for unreachable vendors; enterprise-tier mechanics (multi-entity payroll, union/certified payroll, GL-grade payroll accounting) are not claimed.

## Product Observations

### Square Payroll

Key observations (Layer A unless noted):

- Positioning: "Easily run payroll, pay taxes, and stay ahead of compliance"; "Pay employees from your dashboard, import timecards and tips, and process payroll faster." (A)
- Pay-run workflow (Tier-1 help article, directly observed): Staff > Payroll > Run payroll → Pay employees > Regular payroll > Start run → confirm **Pay Period** and **Pay Date** → select payment method ("Use Employee's Payment Method" or "Pay All Employees by Check") → import time and wages (timecards, tips, commissions from Square Shifts or supported third-party timecard apps) or manually enter hours (Rate, Reg Hours, Overtime at 1.5x, Additional) → add line items next to Gross Pay (Double, Tips Already Paid, Paycheck Tips, PTO, Sick Leave, Commissions) → Adjustments screen (confirm deduction/contribution amounts; add reimbursements — "reimbursements are not taxed") → Review detailed breakdown of the pay run and the bank withdrawal → **Confirm Withdrawal** to approve and process. (A)
- Permission rule: "Only account owners can run payroll." (A)
- Timing rule: "To make sure your direct deposit recipients receive their pay on payday, process payroll by 8 PM PT on your due date." (A)
- Payment methods: direct deposit, manual check (PDF download for printing), Cash App. (A)
- Employee notification: "Square calculates your taxes for you and automatically emails your employees to let them know when they get paid"; employees with a Square Payroll login receive an email with a link to view pay stubs. (A)
- Tax loop (Tier-1 help article): "Square Payroll is a full service payroll provider, handling your federal and state tax filings and payments on your behalf"; "calculates and withholds all federal payroll taxes. These amounts are then debited from your bank account and used to pay taxes on your behalf"; per-run tax amounts visible in the **Withdrawal Summary**; "Payroll taxes are withheld each time you process payroll." (A)
- Tax mechanics: deposits via EFTPS on a semi-weekly schedule (within three days of pay date; FUTA quarterly); forms handled: 941 (quarterly), 940/944/1099-NEC (annual), W-2/W-3 (SSA); filing frequency (941 vs 944) configurable in Tax info settings, with retroactive filing on change; completed forms stored as PDFs; employer must provide physical W-2/1099 copies unless employees consent to electronic delivery. (A)
- Guarantee: IRS-certified reporting agent; covers penalties/fines for its own errors; audit support. (A)
- Off-cycle payments: separate flow ("Make off-cycle payments"); unlimited pay runs and off-cycle payments at no extra cost. (A)
- Contractors: separate run path; contractor-only product tier generates and files 1099-NEC. (A)
- Multistate: locations across multiple states/localities; work locations (e.g., home) drive correct unemployment tax. (A)
- Time input: imports timecards and tips from Square POS/Shifts or "a supported third-party timecard application"; commission importing from sales. (A)
- Benefits: health insurance and 401(k) via partners (SimplyInsured, Guideline); employer contribution changes made with the partner, deductions flow into payroll Adjustments. (A)
- Accounting: syncs with QuickBooks Online. (A)
- Speed options: Two-Day Payroll; Instant Payments funded from Square balance. (A, product-specific)

### Xero Payroll (powered by Gusto)

Key observations:

- Positioning: "Xero Payroll, powered by Gusto, brings full-service payroll directly into Xero. Pay your team, automate tax filings, and meet your compliance obligations with a clear view of your cash flow." (A)
- Pay-run surface: payroll dashboard showing "upcoming and past payroll runs with dates and payment amounts" and a "Run Payroll" action button; "next payroll schedule" visible. (A)
- Pay schedules: "Pay on your schedule (weekly, bi-weekly, semi-monthly, off cycle)." (A)
- Payment: "Direct Deposit (2-day, 4-day)"; FAQ: "pay your team's wages directly into their bank accounts." (A)
- Taxes: "calculates, files, and pays your federal and state taxes for you. It also withholds any deductions and generates tax forms"; "Automated payroll tax filings"; "Complete end-of-year tax handling (W-2s and 1099s)." (A)
- Employees + contractors: "If you employ contractors, you can pay them and file the 1099s… The software then sends the 1099s to your contractors." (A)
- Employee self-service: "Xero Me app (24/7 mobile and web access to pay stubs and tax documents)"; "Payday email notifications"; "Employees update their own info"; W-2s downloadable as PDFs. (A)
- Onboarding: "Self-onboarding"; setup "in around 15 minutes" (vendor claim). (A, as claim)
- Benefits & time off: "Easily manage benefits"; "Manage time off (PTO accruals)." (A)
- Accounting handoff: "Automatically bring your payroll expenses and liabilities into your Xero general ledger"; "Reduce manual reconciliation." (A)
- Jurisdiction: "Support for all 50 states (no extra cost)"; "automatically applying the right tax rate for the jurisdiction"; multistate living situations handled. (A)
- Migration: free data transfer from QuickBooks Payroll or ADP; "Expert validation of historical data." (A)
- Note: Xero's US payroll is literally the Gusto engine inside Xero's shell — evidence that payroll is a distinct engine that can be embedded in an accounting product. (A)

### Zoho Payroll

Key observations:

- Positioning: "Payroll software built for businesses across regions" — shipped as regional editions: GCC, Canada, India, USA. (A)
- GCC edition: "automated calculations, contributions, allowances, and timely pay slips"; "built-in coverage for social security, pension (GPSSA, GOSI, SIO, SPF, PIFSS, GRSIA, ADPF), end-of-service rules, and WPS requirements"; leave/attendance/holidays unified; "Run payroll in English or Arabic, create flexible salary components and schedules." (A)
- Canada edition: "automated salary calculations, benefits, deductions, and accurate final payments"; "federal and provincial laws, including CPP/QPP, EI, QPIP, statutory holidays, vacation pay, T4, RL1, and ROE." (A)
- India edition: "Automatic payroll computation… We do the math so you don't have to"; "Statutory compliance and taxes: PF, PT, ESI, LWF, and IT are all handled"; "Built-in integration with HRMS platform." (A)
- USA edition: "Centralized payroll management — access and organize your employees' records from one secure place"; "Complete payroll — unlimited hourly or salary payroll with multiple pay schedule options"; "Tax compliance — accurate federal and state tax deductions for full compliance with reports for easy tax filing." (A)
- Accounting: "Zoho Payroll is tightly integrated with Zoho Books… Record payroll expenses automatically to the right journals." (A)
- Payment: "Automate salary payments through secure integrations with partner banks. Distribute payslips and payroll forms online." (A)
- Employee self-service: "Employee-friendly self-service portal — effortlessly organize and download crucial payroll documents"; "Tax saving investment declarations can be quickly and easily submitted online" (India-specific). (A)
- Reporting: "Download ready-to-share payroll reports that paint a complete picture about your organization's payroll costs." (A)
- Note: one product family, four statutory regimes — the same core (records, schedules, computation, payslips, payment, reports) under different compliance wrappers. (A/B)

### Rippling Payroll

Key observations:

- Positioning: "Payroll software that runs accurately and on time—every time"; part of a single-employee-data-spine platform ("single source of truth for all business data related to employees"). (A)
- HCM sync: "HR data—like new hires, salary changes, and benefits deductions—flow directly and automatically into Payroll. No manual errors or work required." (A)
- Run + tax automation: "Click 'run' and let Rippling handle the rest. We automatically calculate payroll taxes and file them with the correct federal, state, and local agencies at precisely the right time." (A)
- Run comparison: "Rippling lets you compare your current pay run with previous ones to catch discrepancies before final approval. Easily dig into changes in gross pay, taxes, deductions, and more with a single click." (A)
- AI: add one-off bonuses via prompt; compare payroll costs across entities; employees get instant answers about pay changes. (A)
- Scheduling: "Run payroll on your schedule — stay flexible and process payroll as often as you need — at no extra charge." (A)
- Pay types: "Select from default pay types or customize your own on a one-off or recurring basis." (A)
- Self-service: "letting current and past employees view pay stubs and tax forms at any time." (A)
- Permissions: "Automatically control who can view, create, manage, and approve pay runs." (A)
- Accounting: "Integrate with industry-leading accounting systems like Xero, QuickBooks, and NetSuite." (A)
- Tax form storage: "securely stores electronic copies of all employee tax forms (like W-2s and 1099s) with each employee's profile… even after an employee leaves." (A)
- Withholding flow: "Employee withholdings automatically flow into payroll, so you'll never need to manually enter withholding amounts." (A)
- Vendor's own definition of the activity (FAQ): "Payroll management is the process of paying your employees and contractors accurately and on time. It includes calculating wages, managing deductions (like taxes and benefits), handling garnishments, and maintaining all necessary financial records while ensuring compliance with regulations." (A)
- Vendor's own process description (FAQ): "starts with collecting employee information and setting up a pay schedule. Then, for each pay period, it involves calculating gross pay, deducting taxes and other withholdings, filing taxes with the appropriate agencies, and, finally, issuing payments to your employees and contractors — all while keeping precise records." (A)
- Product family: Payroll (US) and Global Payroll are separate products; EOR and PEO are separate offerings — vendor-confirmed structural separation. (A)

## Cross-product Comparison

| Structure | Square | Xero (Gusto) | Zoho | Rippling | Assessment |
|---|---|---|---|---|---|
| Employer-maintained employee pay records (compensation terms, withholding/deduction elections) | yes (employee setup, payment methods, W-4-based withholding) | yes (self-onboarding; employees update own info) | yes ("access and organize your employees' records from one secure place") | yes (HR data flows in; withholdings flow in) | **L0** |
| Recurring pay cycle (pay schedule → pay period → pay run as unit of work) | yes (Pay Period + Pay Date confirmed per run; payment schedule editable) | yes (weekly/bi-weekly/semi-monthly; dashboard shows next schedule) | yes ("multiple pay schedule options"; flexible schedules) | yes ("run payroll on your schedule") | **L0** |
| Gross-to-net computation per employee per run | yes (hours/earnings → adjustments/deductions → net; taxes calculated) | yes ("withholds any deductions"; "confidence in your calculations") | yes ("automatic payroll computation… We do the math") | yes ("calculating gross pay, deducting taxes and other withholdings") | **L0** |
| Payment issuance to employees | yes (direct deposit / check / Cash App) | yes (direct deposit 2-day/4-day) | yes (partner-bank salary payments) | yes (implied; "issuing payments") | **L0** |
| Durable pay records (register, pay stubs, history) | yes (pay stubs emailed; Withdrawal Summary; reports) | yes (pay stubs in Xero Me; past runs on dashboard) | yes (payslips distributed online; payroll reports) | yes (pay stubs; tax forms stored per employee profile) | **L0** |
| Statutory tax withholding inside the computation | yes (federal taxes calculated/withheld each run) | yes | yes (regime-specific: PF/ESI/IT; CPP/EI; GPSSA/GOSI…) | yes (federal/state/local) | **L0 as "statutory withholdings where the regime requires"** (regime-specific composition is L2) |
| Full-service tax filing & deposit with agencies | yes (EFTPS, 941/940/944, W-2/W-3, guarantee) | yes ("calculates, files, and pays") | partial ("reports for easy tax filing" — US edition wording suggests reports, not full-service filing) | yes ("file them with the correct federal, state, and local agencies") | **L1** (common in modern US products; not definitional — see historical check) |
| Direct deposit as default payment method | yes (plus check/Cash App) | yes | yes (partner banks) | yes | L1 (method is L1/L2; issuance is L0) |
| Employee self-service (stubs, tax forms, info updates) | yes (login + emailed stub links) | yes (Xero Me) | yes (portal; India declarations) | yes (current + past employees) | L1 |
| Time & attendance import as run input | yes (Square Shifts or third-party timecards) | not prominent on page | yes (leave/attendance unified in GCC/India editions) | yes (Time & Attendance is a sibling product) | L1 (input; ownership of time tracking is L2) |
| Off-cycle / one-off runs | yes (dedicated flow; unlimited) | yes ("off cycle") | not prominent | yes (one-off pay types; bonuses) | L1 |
| Pay-run review/approval before release | yes (Review → Confirm Withdrawal; account-owner-only) | yes (Run Payroll action) | not directly observed | yes (compare to last run before final approval; approve permission) | L1 (control depth varies) |
| Accounting/GL handoff | yes (QuickBooks sync) | yes (expenses + liabilities into GL) | yes (Zoho Books journals) | yes (Xero/QuickBooks/NetSuite) | L1 |
| Benefits deductions administration | yes (partner benefits; deductions in Adjustments) | yes ("easily manage benefits") | yes (benefits + custom leave policies, US edition) | yes (benefits deductions flow in) | L1 |
| Contractor payment + year-end forms | yes (separate path; 1099-NEC; contractor-only tier) | yes (pay + file 1099s) | not prominent on page | yes (contractors product) | L1 |
| Year-end forms (W-2/1099-class) | yes | yes | yes (T4/RL1 Canada; India forms) | yes | L1 |
| Roles/permissions | yes (account owner runs payroll) | not prominent | yes ("secure access controls… work across departments") | yes (view/create/manage/approve pay runs) | L1 |
| Reports/analytics | yes (payroll reports) | yes (dashboard of runs) | yes (payroll cost reports) | yes (cost reports across entities; AI insights) | L1 |
| Run-change comparison tooling | not observed | not observed | not observed | yes (compare to last pay run) | L2 (product-specific in sample) |
| AI assistance (prompts, employee Q&A) | no | no | no | yes | L2 (current-era, product-specific in sample) |
| Multi-jurisdiction scope | yes (multistate US) | yes (all 50 states) | yes (4 regional editions as separate sites) | US product + separate Global Payroll | L2 (scope gradient; see Boundary Findings) |
| Embedded vs standalone | embedded in POS suite | embedded in accounting | standalone suite (HRMS-integrated) | platform-native in HCM suite | L2 (packaging) |
| Service posture | full-service provider + guarantee + IRS-certified agent | full-service (Gusto engine) | software + reports (self-filing posture in US wording) | software + automated filing | L2 (service model) |
| Speed options (next-day/2-day/instant) | yes (Two-Day, Instant Payments) | yes (2-day/4-day) | not observed | not observed | L2 (product-specific) |
| Workers' comp add-on | yes (pay-as-you-go, synced) | not observed | not observed | not observed | L2 |

Convergence summary (Layer B): all four products implement the same spine — employer-maintained employee pay records → recurring pay schedule → per-period pay run that gathers earnings inputs (time/salary/one-offs) → gross-to-net computation (earnings − statutory withholdings − deductions) → review/approval → payment issuance → durable pay records (register, pay stubs, history) → (commonly) automated tax filing/deposit and year-end forms → (commonly) GL handoff. All four treat the pay run as the unit of work and the employee pay record as the anchor object. Differences are packaging (POS/accounting/HCM/standalone), service posture (full-service vs software), and jurisdictional wrappers.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

1. **Employer-maintained employee pay records** — identified employees (and, in variants, contractors) held with compensation terms (salary or rates), payment instructions, and withholding/deduction elections, maintained by the employer.
2. **Recurring pay cycle** — a pay schedule defines pay periods; the **pay run** over a period is the unit of work the operator executes.
3. **Gross-to-net computation per employee per run** — earnings for the period (from pay terms plus period inputs such as hours, tips, commissions, one-off items) minus statutory withholdings (where the regime requires employer withholding) and agreed deductions equals net pay.
4. **Payment issuance + durable pay records** — net pay is issued to each employee through a payment method, and each run leaves durable records: a run register and per-employee pay statements/history.

Remove any one and the Type collapses: without (1) it is a generic payment disbursement tool; without (2) it is ad-hoc bonus disbursement, not a payroll *system*; without (3) it is a payment batch tool with no pay computation; without (4) it is a calculator — not a system of record for what people were paid.

Deliberately **not** in L0 (tested and demoted):

- **Tax filing/deposit with agencies** — universal in the current US sample but not definitional. Historical check: desktop-era payroll computed withholding and printed tax reports/forms for manual filing and still was payroll. Zoho's US edition wording ("reports for easy tax filing") shows a software-only posture coexisting with full-service providers. Regional check: statutory roles differ by regime (some regimes withhold little or nothing at employer level). → L1.
- **Direct deposit** — method, not essence. Historical payroll paid by printed check; Square still offers "Pay All Employees by Check"; Zoho pays through partner banks. → L1 (method) / L2 (specific rails).
- **Employee self-service** — historical payroll had none; all four sampled products have it, but it is an access surface, not the computation. → L1.
- **Time & attendance ownership** — time data is an input; Square imports from third-party timecard apps; Rippling ships T&A as a separate product. → L1 (input), L2 (ownership).
- **Contractor payment** — common and increasingly packaged (Square contractor-only tier), but the employee pay spine is the core; contractor-only is a variant. → L1.
- **Accounting/GL handoff, benefits administration, HR onboarding, reports, roles** — common mature structure. → L1.
- **AI assistance, run-comparison tooling, instant/speed options** — current-era or product-specific. → L2.

### L1 — Common Mature Structure

- automated tax computation, filing, and deposit with agencies (full-service posture in the US sample), including filing-frequency handling and agency-form generation (941/940/944-class, W-2/1099-class, or regime equivalents)
- direct deposit as the default payment method (with check and other rails as alternatives)
- employee self-service: pay stubs, year-end tax forms, personal-info updates, payday notifications
- time & attendance import as the run's hours input (own module or third-party)
- off-cycle / one-off pay runs (bonuses, corrections, terminations)
- pay-run review and approval before release (breakdown review, bank-withdrawal confirmation, permission-gated execution)
- accounting/GL handoff (payroll expenses and liabilities posted or synced to the books)
- benefits and deduction administration (deductions/contributions applied in the run)
- new-hire onboarding into payroll (self-onboarding flows, tax-election capture)
- year-end form generation and distribution (W-2/1099-class or regime equivalents)
- payroll reports (costs, registers, tax liability)
- roles and permissions (who can run/approve payroll; employee-scoped access)
- garnishments and reimbursement handling (per Rippling's own definition; Square reimbursements)

### L2 — Variant / Optional Structure

- jurisdiction/regime wrapper: US federal/state/local; Canada (CPP/EI/T4/ROE); India (PF/ESI/PT/LWF/IT, investment declarations); GCC (social insurance schemes, end-of-service, WPS wage-protection rails, Arabic UI)
- scope gradient: single-jurisdiction payroll vs multi-country/global payroll (Rippling ships these as two products; Zoho ships regional editions of one product)
- worker mix: W-2 employees only vs employees + contractors vs contractor-only products
- packaging: standalone product vs embedded in POS (Square), accounting (Xero/QuickBooks), or HCM platform (Rippling)
- service posture: self-service software vs full-service provider (files/deposits on the employer's behalf, penalty guarantees, certified-agent status) vs PEO/EOR (co-employment — different Type)
- industry editions: restaurants/hospitality (tips, tipped wages), retail (commissions, multiple rates), construction (certified payroll — not sampled), healthcare etc.
- speed options: next-day/2-day/instant pay (product-specific rails)
- time-off/PTO management depth (accruals, balances) — overlaps Leave & Absence Management
- workers' compensation integration; equity compensation (not sampled)
- deployment: cloud SaaS (current norm) vs historical desktop/on-prem

### L3 — Vendor-specific (stays in Research Notes)

- Square: Cash App as a payment rail; 8 PM PT processing cutoff; Two-Day Payroll; Instant Payments from Square balance; Square Payroll Guarantee; IRS-certified reporting agent status; commission import from Square Shifts sales; Withdrawal Summary naming
- Xero: Xero Me employee app; "powered by Gusto" engine licensing; free white-glove data transfer; setup-time marketing claim
- Zoho: regional edition structure (GCC/Canada/India/USA as separate sites); WPS integration; India tax-saving investment declarations; Zoho Books journal automation
- Rippling: compare-to-last-pay-run tooling; AI prompt flows (add bonuses, entity cost comparison, employee pay Q&A); single-employee-spine platform framing; Payroll vs Global Payroll vs EOR product split

## Rejected Findings

- **"Payroll = tax filing"** — rejected as definition. Filing/deposit is the most marketed layer in the US sample, but the historical sample (desktop-era payroll printing forms for manual filing) and Zoho's software-posture wording show the Type stands without it. Filing = L1.
- **"Payroll = direct deposit"** — rejected: payment method is an implementation (check, cash, bank transfer, Cash App). Issuance is L0; the rail is L1/L2.
- **"Payroll requires employee self-service"** — rejected: an access surface, not the computation. L1.
- **"Payroll is an HR module"** — rejected: standalone payroll exists (Square, Zoho, contractor-only products); HR integration is L1/L2. The dependency direction is real (payroll consumes HR/time data) but not definitional.
- **"Payroll = paying contractors"** — rejected: contractor payment is a common extension; the W-2/employee spine is the core. Contractor-only products are a variant.
- **"Payroll requires US-style multi-agency tax machinery"** — rejected: Zoho's regional editions show the same core under GCC/India/Canada regimes with entirely different statutory structures; L0 phrases withholding as "where the regime requires."
- **"Gross-to-net always includes income-tax withholding"** — rejected as universal: regimes differ in what employers must withhold; the L0 keeps the computation generic (earnings − statutory withholdings where applicable − deductions).

## Boundary Findings

1. **vs Global Payroll Platform (sibling leaf, §09)** — Rippling ships "Payroll" (US) and "Global Payroll" as **separate products** (vendor-confirmed split), while Zoho ships one product as **regional editions**. The structural test: a Payroll System runs pay for employees under one (or a few) jurisdictions where it holds deep statutory machinery; a Global Payroll Platform consolidates pay runs across many countries, typically orchestrating in-country payroll providers or owning multi-country compliance. Remove multi-country consolidation → payroll remains; make multi-country orchestration the primary object → global payroll. **Probable adjacent-Types-sharing-a-core relationship — flagged for joint review when Global Payroll Platform is processed.**
2. **vs Time & Attendance System (sibling, §09)** — time data is the run's input, not the payroll core. Square imports timecards from "a supported third-party timecard application"; Rippling ships Time & Attendance as a separate product feeding payroll. Test: remove pay computation/payment → T&A remains; remove time tracking → payroll remains (salaried payroll needs no time data). Related Types in a producer→consumer relationship.
3. **vs HRIS / HCM (§09)** — the HRIS holds the employee master; payroll consumes it (Rippling: "HR data—like new hires, salary changes, and benefits deductions—flow directly and automatically into Payroll"; Zoho: "Built-in integration with HRMS platform"). Payroll can be standalone with its own minimal employee records (Square). Test: remove HR breadth (recruiting, performance, org) → payroll remains; remove pay computation/payment → HRIS remains.
4. **vs Accounting Software (§08)** — payroll posts expenses and liabilities into the books (Xero: "into your Xero general ledger"; Zoho: "to the right journals"; Square/Rippling: sync). Accounting products may embed payroll (Xero Payroll, QuickBooks Payroll) but the payroll engine is a distinct structure with its own objects (pay runs, withholding, pay stubs) that the ledger lacks. Consistent with the accounting-software research note, which classified payroll as an L2 extension of accounting software.
5. **vs Compensation Management Platform (§09)** — comp management plans pay (bands, merit cycles, equity planning); payroll executes pay. Not sampled in depth (reasoned boundary); the sampled products show compensation *terms* as payroll inputs, not planning structures.
6. **vs PEO / EOR (§09)** — a service model where the provider becomes the employer of record and runs payroll as the legal employer; payroll software is a tool of the actual employer. Rippling ships Payroll, Global Payroll, EOR, and PEO as four separate offerings — vendor-confirmed separation.
7. **vs Payment Processing Platform (§08)** — payroll pays employees out of employer funds as a computed obligation; payment processing moves merchant commerce money. Different object models (pay run vs transaction); payroll's payment step commonly rides bank rails, not card networks.
8. **Payroll bureau / service-bureau lineage** — ADP-class providers historically ran payroll as an outsourced *service* (employer submits data, bureau computes/pays/files). Modern products productize this as "full-service" software. The Type as documented is the employer-operated system; the bureau is a service posture (L2), not a separate structure. Recorded as an observation; enterprise bureau mechanics under-sampled (see Uncertainties).

## Historical / Market-Sample Check

- **Desktop-era payroll (1980s–90s lineage)**: employee master with pay/rate and tax-election fields + weekly/biweekly/monthly pay periods + gross-to-net computation against stored tax tables + check printing + pay registers and printed year-end forms filed manually. Satisfies L0 with none of: e-filing, direct deposit, self-service, cloud, AI. ✓ (reasoned from the structure the sampled products still implement; not asserted as specific product facts)
- **Regional check**: Zoho's own regional editions (GCC: WPS + end-of-service + social insurance; India: PF/ESI/PT/IT + investment declarations; Canada: CPP/EI/T4/ROE) demonstrate the same core (records → schedule → compute → payslip → pay → report) under different statutory wrappers; the L0 phrase "statutory withholdings where the regime requires" keeps regimes like minimal-withholding jurisdictions inside the definition. ✓
- **Platform-native check**: the same core appears embedded in a POS (Square), an accounting product (Xero), and an HCM platform (Rippling) — packaging does not change the structure. ✓
- **Service-posture check**: full-service providers (Square's guarantee, certified-agent status) and software-only postures (Zoho US "reports for easy tax filing") both satisfy the core. ✓
- Conclusion: L0 does not over-fit the current full-service, direct-deposit, self-service era.

## Uncertainties

1. Gusto's own documentation was unreachable (403/JS); Gusto capabilities are evidenced indirectly through Xero's official "powered by Gusto" page. Gusto-specific mechanics are not asserted anywhere.
2. ADP, Paylocity, Paycor, Sage, Patriot, QuickBooks Payroll were unreachable (403/JS/timeout). Enterprise-tier structures (multi-entity payroll accounting, union/multi-union rules, certified payroll, multi-country bureau orchestration) are under-sampled; the final document does not claim them.
3. Exact pay-run state machines vary by product and were only directly observed for Square (start → hours/earnings → adjustments → review → confirm withdrawal → processed); the final document describes conceptual states only.
4. Precise cutoffs, deposit schedules, and form lists (Square's 8 PM PT, semi-weekly EFTPS, 941/940/944/W-2) are product- and jurisdiction-specific; recorded here, not asserted as universal in the final document.
5. Zoho's US edition tax-filing depth (full-service vs reports-only) is ambiguous from the fetched page wording; treated as uncertain and not relied upon.
6. Employee self-service depth (what employees may change) varies and was not directly observed per product beyond Xero ("employees update their own info") and Rippling (stubs/forms for current and past employees).
7. Whether any mainstream payroll product ships without any employee self-service today was not verified; self-service is placed in L1 on cross-product evidence, not universality.

## Final Synthesis

A Payroll System is the employer-operated system of record for paying people: **employer-maintained employee pay records → a recurring pay cycle whose unit of work is the pay run → per-employee gross-to-net computation (period earnings − statutory withholdings where applicable − deductions) → payment issuance → durable pay records (register, pay statements, history)**. Around this core, mature products add the compliance and convenience layers that dominate marketing: automated tax filing/deposit and year-end forms, direct deposit, employee self-service, time imports, off-cycle runs, GL handoff, benefits deductions, and permissions. Products differ mainly on four gradients: packaging (standalone vs POS/accounting/HCM-embedded), service posture (software vs full-service provider), jurisdictional scope (single-jurisdiction vs global), and worker mix (employees vs contractors). The Application Document will present the defining core and standard capabilities in natural language; variants name the L2 options; L3 stays in these Research Notes.
