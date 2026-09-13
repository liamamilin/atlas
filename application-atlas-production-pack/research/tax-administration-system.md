# Research Notes — Tax Administration System

## Research Goal

Understand what a **Tax Administration System** actually is as an Application Type: the software a government revenue authority uses to administer taxes. Establish the defining core, the common mature structure around it, the variant axes, and the boundaries against the closest neighboring Types — especially the already-processed sibling **Property Tax Administration** and the taxpayer-side **Tax Preparation / Tax Filing** Types from the Finance section.

## Initial Boundary (hypothesis before research)

- Core use: the revenue authority's system of record — register taxpayers, hold tax accounts, receive/assess declarations, post payments and refunds, pursue arrears, run compliance and disputes.
- Primary users: authority staff (registration, processing, assessment/audit, collection, appeals, service) plus external taxpayers, agents, and third-party information reporters.
- Nearest neighbors: Property Tax Administration (§24 sibling), Tax Preparation Application / Tax Filing Platform / Corporate Tax Management / Tax Compliance Platform (§08 Finance, taxpayer/corporate side), Government Revenue Management (§24), Government Service Portal (§24), Government Licensing Management (§24).
- Expected key distinction from the property-tax sibling: taxpayer-anchored obligation accounts fed by declarations/assessments, vs parcel-anchored bills fed by a certified roll and levies.
- Unknowns: which vendors' documentation is reachable; whether the COTS market documents enough structural detail; whether enforcement/audit belongs to the defining core or the common mature layer.

## Research Questions

1. What is the system of record? (taxpayer? tax account? return? assessment? debt?)
2. How does a taxpayer enter the system — registration, identifiers, registration lifecycle?
3. How do obligations arise: returns/declarations, withholding and information reports, authority assessments?
4. What is the assessment loop — self-assessment posting, automated third-party matching, compliance-check assessments, assessment time limits?
5. How does money post: payments, credits, refunds, arrears, statutory charges (penalties/interest)?
6. What enforcement machinery exists: payment plans/installment agreements, liens, levies, refund offset, enforced collection?
7. How do compliance/audit and dispute/appeal work as case machinery on the same accounts?
8. What interfaces exist: officer workbenches, taxpayer self-service, agent authorization, notices, reporting?
9. Where exactly are the boundaries: vs taxpayer-side filing software, vs property tax administration, vs government revenue management, vs government service portals?

## Representative Products

Selected for market representativeness, different product philosophies (purpose-built COTS platform vs in-house national systems), different customer levels (US states + international agencies, UK national, US federal), and documentation quality:

1. **Fast Enterprises — GenTax** — the flagship commercial off-the-shelf tax administration platform (US state revenue agencies + international revenue authorities). Official brochure and solutions pages.
2. **HM Revenue & Customs (HMRC, UK)** — national revenue authority; its official service guidance and published internal operational manuals document the administration machinery in depth (in-house systems).
3. **Internal Revenue Service (IRS, US)** — federal revenue authority; official taxpayer-facing operational documentation documents the tax account, assessment, collection, and dispute machinery (in-house systems).

Market anchors sampled but not usable as product samples: SAP (official pages unreachable, 2×404), CGI (unreachable, 2×404), IRAS Singapore (unreachable, 2×404), Oracle (public-sector page reachable but documents no tax administration product — used only as a market-structure anchor).

## Sources

| # | Source | URL | Reachability |
|---|---|---|---|
| S1 | Fast Enterprises — Solutions (GenTax overview) | https://www.fastenterprises.com/solutions/ | fetched 2026-09-09 |
| S2 | Fast Enterprises — GenTax brochure (2026-05 PDF) | https://fwbprod-v2static.fastenterprises.com/assets/pdf/solution/gentax-brochure-2026-05.pdf | downloaded + text-extracted 2026-09-09 |
| S3 | HMRC — Self Assessment: detailed information (collection) | https://www.gov.uk/topic/personal-tax/self-assessment | fetched 2026-09-09 |
| S4 | HMRC — Compliance Handbook (internal manual index) | https://www.gov.uk/hmrc-internal-manuals/compliance-handbook | fetched 2026-09-09 |
| S5 | IRS — Payment plans; installment agreements | https://www.irs.gov/payments/payment-plans-installment-agreements | fetched 2026-09-09 |
| S6 | IRS — Understanding your CP2000 series notice | https://www.irs.gov/individuals/understanding-your-cp2000-notice | fetched 2026-09-09 |
| S7 | Oracle — Government industry page | https://www.oracle.com/industries/public-sector/ | fetched 2026-09-09 (market anchor only) |
| S8 | Sibling pass: applications/property-tax-administration.md + research notes | local | 2026-09-09 |

Unreachable (recorded limitations): SAP tax-and-revenue solution pages (404 ×2), CGI tax administration pages (404 ×2), IRAS myTax Portal pages (404 ×2).

---

## Product 1 — Fast Enterprises GenTax (evidence layer A: official brochure + solutions pages)

### Key observations

- Self-labels: "TAX ADMINISTRATION SOFTWARE"; "A COMPLETE TAX ECOSYSTEM IN ONE TRUSTED PLATFORM" (S2 headline). Lexical evidence that the market's flagship product names itself exactly after the leaf.
- Scale claims (vendor-stated, take as marketing-grade): 70+ revenue agencies served, 35+ U.S. states, 10+ countries, 25+ years, "billions of dollars processed and distributed annually", IRS Publication 1075 compliance (federal tax information safeguarding).
- "All core functions through one integrated, purpose-built solution" (S2, vendor's own framing of the core set):
  - seamless integration between **accounting and payment processing**
  - support for **hundreds of tax types and fees**
  - **complete customer and account management**
  - **compliance, workflow, and interface management**
  - **expedited refunds and returns processing**
  - capacity for **high-volume, complex tasks**
  - **fraud prevention and identity verification**
- "Beyond the basics" layer (S2): 24/7 self-service portals, AI-driven virtual assistant, centralized contact center, business-intelligence tools, **advanced collections and audit support**, customer banking tracking / routing-number validation, ACH + digital wallets, **Modernized e-File**, Streamlined Sales Tax.
- Solutions page pillars (S1): Customer Engagement ("web-based self-service"), Process Automation, **Financial Integrity ("backed by accounting and payment functions")**, **Compliance & Enforcement ("maximize collection recoveries and the fulfillment of obligations")**, Fraud Mitigation & Identity Verification, Business Intelligence, Single-System Simplicity.
- Adjacent paid services: Fast Audit Services, Fast Collection Services, Fast Identity Verification Services (S1) — audit and collections are big enough functional areas to be packaged as standalone services.

### Reading

GenTax's own enumeration of the core set aligns with a taxpayer/account substrate ("customer and account management"), many tax types, a returns/refunds processing pipeline, an accounting+payment spine, and a compliance/collections/audit layer. Portal, AI assistant, contact center, BI, e-File, wallets are explicitly framed as beyond-the-basics/era-current layers — useful anti-overfit evidence from the vendor's own framing.

## Product 2 — HM Revenue & Customs (evidence layer A: official service guidance + published internal manuals)

### Key observations (S3, S4)

- Self Assessment service loop (S3): check whether a return is required → register → file online (or via commercial software — "Use software to help complete your Self Assessment tax return") → pay the bill → understand the bill (SA302 tax calculation) → keep records → claim refunds → **disagree with a tax decision or penalty** (appeals) → penalties for late filing/payment → "If you cannot pay your tax bill on time" (payment support).
- Compliance Handbook (S4) — the authority's statutory machinery, published as operational guidance:
  - **record keeping** requirements; **information and inspection powers**; **data gathering powers**
  - **litigation and settlement strategy**
  - **assessing time limits** (time limits for assessments)
  - penalties for **failure to file on time**, **failure to notify**, **inaccuracies**, **VAT/excise wrongdoing**, **failure to pay on time**
  - **interest** on unpaid amounts; **reasonable excuse**; **special reduction**
  - publishing details of **deliberate tax defaulters**; **electronic sales suppression** (evasion technology); sanctions for **dishonest tax agents**
  - **"How to do a compliance check"** — the operational core of the audit function
  - **"The One to Many Approach"** — mass, non-individualized compliance activity
  - **agent operational guidance** — tax professionals as a governed external role
- Multiple regimes administered under one authority: income tax (Self Assessment), VAT, excise, plus penalties machinery spanning them.

### Reading

HMRC documentation shows the full authority-side machinery around the taxpayer account: declaration → assessment (self-assessment plus authority assessment with statutory time limits) → payment → refund → arrears with penalties/interest → enforcement through a compliance-check machinery with statutory information/inspection powers → dispute machinery. It also shows that "administration" includes governed external roles (agents) and mass-processing approaches (one-to-many).

## Product 3 — Internal Revenue Service (evidence layer A: official taxpayer-facing operational documentation)

### Key observations (S5, S6)

- Taxpayer account substrate: "Your Online Account" exposes **refunds, payments, tax records**; tax account viewing requires identity authorization with security checks; balance and payment history visible; **tax record (transcript)** as the extractable account artifact; identity-protection PIN (IP PIN) machinery; EIN/ITIN registration surfaces.
- Registration: EIN application (employer identification), ITIN application (W-7) — taxpayer identification as a first-class administrative process.
- Filing/assessment loop — CP2000 (S6): income/payment information **received from third parties (employers, financial institutions)** is matched against the filed return; discrepancies generate a **proposed change** notice: "This notice isn't a bill and your response may be required"; taxpayer agrees/disagrees with documentation; unresolved discrepancy escalates to "another notice and a bill"; amended returns (1040-X) feed the same loop; appeal rights documented (Publication 5, Independent Office of Appeals); representation via power of attorney (Form 2848).
- Collection machinery (S5): **payment plans** — short-term (≤180 days) and long-term **installment agreements** with eligibility thresholds, setup fees, default/reinstatement semantics; while an installment agreement is pending/in effect the IRS is "generally prohibited from levying" and collection time is suspended; enforcement instruments: **Notice of Federal Tax Lien** and **IRS levy**; the whole process documented in Publication 594 ("The IRS Collection Process"); **future refunds applied to the tax debt** (refund offset); **penalties and interest accrue until the balance is paid in full**; **statutes of limitations for assessing, collecting and refunding tax** (a first-class concept); "enforced collection actions" as a named concept; offer in compromise as an alternative resolution; Taxpayer Advocate Service and Low Income Taxpayer Clinics as taxpayer-protection surfaces.
- Other administration surfaces: notices and letters index, Criminal Investigation, Whistleblower Office, Tax Pros portal (tax-professional role), Taxpayer Bill of Rights.

### Reading

IRS documentation confirms the same loop from a different tradition (fully self-assessed federal income/employment taxes): third-party information + filed returns → automated matching → proposed assessments → bills → collection machinery (plans, offset, liens, levies) under statutory time limits → dispute/appeal machinery. The account (balance, payments, transcripts) is the persistent spine.

---

## Cross-product Comparison

| Structure / capability | GenTax (COTS) | HMRC (UK national) | IRS (US federal) | Evidence layer | Classification |
|---|---|---|---|---|---|
| Registered taxpayer / customer population with identifiers | "complete customer and account management" | registration into Self Assessment; agent registration | EIN / ITIN / IP PIN; identity-authorized online account | A×3 (B) | **Defining** |
| Tax-type-structured accounts under one taxpayer | "support for hundreds of tax types and fees" | income tax, VAT, excise… under one authority | account per tax type; transcripts per period | A×3 (B) | **Defining** |
| Declarations/returns intake & processing | "returns processing"; Modernized e-File | file online / via software | file, e-file, amended returns | A×3 (B) | **Defining** |
| Assessment (self-assessment posting + authority assessment) | "compliance, workflow…management" (implicit) | self-assessment + compliance-check assessments with **assessing time limits** | self-assessment + **automated third-party matching → proposed changes** | A×2 strong + A×1 implicit (B) | **Defining** (assessment as the loop's conversion step) |
| Payments/credits posting against the account | "accounting and payment processing" integrated | pay the bill; understand the bill | online account balance/payment history; Direct Pay/EFTPS rails | A×3 (B) | **Defining** |
| Refunds | "expedited refunds" | claim a tax refund | refunds as top-level nav; reduced-refund offsets | A×3 (B) | **Defining** (settlement's negative side) |
| Arrears as tracked state + statutory charges | collections; (charges implied) | penalties + interest machinery (late filing/notify/pay, inaccuracies) | penalties + interest accrue until paid; collection statutes of limitation | A×2 strong + A×1 implicit (B) | **Defining** (arrears tracking); charges = Common |
| Debt/enforcement machinery (plans, liens, levies, offset) | "advanced collections" (service packaging) | "if you cannot pay" support; collection powers | payment plans/installment agreements, liens, levies, refund offset, enforced collection | A×2 strong + A×1 high-level (B) | Common mature |
| Compliance/audit case machinery | "audit support" / Fast Audit Services | compliance checks, information/inspection powers, litigation & settlement, one-to-many | audits, Criminal Investigation, whistleblower | A×3 (B) | Common mature |
| Dispute/appeal machinery | not confirmed in reachable sources | "disagree with a tax decision or penalty"; litigation strategy | Independent Office of Appeals; Publication 5 protest rights | A×2 (B) | Common mature (NOT confirmed for GenTax — do not attribute) |
| Notices/correspondence as governed procedure | interface management (weak) | letters/notices; publishing defaulters | notices and letters index; "notice isn't a bill" semantics | A×2 strong + A×1 weak (B) | Common mature |
| Taxpayer self-service portal / online account | 24/7 self-service portals (vendor "beyond basics") | online services | Online Account | A×3 (B) | Common mature |
| Agent/tax-professional authorization | not confirmed | agent operational guidance; dishonest-agent sanctions | Form 2848 POA; Circular 230; Tax Pros portal | A×2 (B) | Common mature |
| Third-party information reporting & matching | not explicit | data gathering powers | CP2000 matching of employer/financial-institution reports | A×1 strong + A×1 indirect (B) | Common mature |
| Registration-side identity/fraud machinery | fraud prevention and identity verification | (identity surfaces implicit) | IP PIN; identity theft affidavit | A×1 explicit + A×1 (B) | Common mature |
| AI assistant / contact center / BI | explicit (beyond basics) | digital assistant (S3) | (help surfaces) | A×2 (B) | Era-current / optional |
| Multi-entity distribution of collected money | — (not claimed) | — | — | — | NOT generic: property-tax sibling structure; treasury settlement here is simpler |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

The revenue authority's system of record, jointly held by three structures:

1. **The registered taxpayer population of record** — identified persons and entities registered with the authority under identifiers, with a registration lifecycle. Remove → a civic registry or a payments page with no subject.
2. **Tax-type-structured obligation accounts** — each taxpayer holds accounts organized by administered tax type; obligations arise per period from declarations/returns, withholding/information reports, and authority assessments; balances carry assessed liabilities, posted payments/credits, and tracked arrears. Remove → a contact database or an anonymous ledger.
3. **The assess→post→settle loop** — declared/reported facts are processed into assessed liabilities; payments and credits post against accounts; overpayments are refunded; unpaid balances persist as tracked arrears awaiting the authority's next step. Remove → registration with static balances, or a cash office.

Jointly-held load-bearing analysis:

- 1 alone = a civic/registration database (or CRM-shaped registry)
- 2 without 1 = a generic ledger/accounting system
- 3 without 1+2 = payment processing / a cash office
- 1+2 without 3 = registry with static balances — no administration
- 1+3 without 2 = general revenue cashiering for persons, not tax administration
- 2+3 without 1 = anonymous tax accounting with no addressable taxpayer

### L1 — Common Mature Structure (very common, not definitional)

- statutory charges machinery: penalties for late filing / late payment / inaccuracies; interest on unpaid balances
- debt & enforcement machinery: payment plans/installment agreements, liens, levies, refund offset, enforced collection; collection time limits
- compliance/audit case machinery: risk-based selection, compliance checks with information/inspection powers, litigation & settlement, one-to-many mass compliance
- dispute/appeal machinery: objection/appeal cases, independent appeals bodies
- notices/correspondence as governed procedure (proposed-change semantics, "not a bill" distinction, escalation to bills)
- taxpayer self-service portals / online accounts (balance, records, transcripts)
- agent/tax-professional authorization and portals
- third-party information reporting (withholding reports, employer/financial-institution reports) and matching
- e-filing intake interfaces (return submission channels)
- identity verification / fraud-prevention machinery
- accounting, revenue reporting and reconciliation to the treasury

### L2 — Variant / Optional Structure

- assessment tradition: full self-assessment ↔ official/administrative assessment regimes
- tax-type breadth: a single tax ↔ "hundreds of tax types and fees"; income/VAT/payroll/excise/fees mixes
- jurisdiction grain: national ↔ state/provincial ↔ municipal (municipal grain drifts toward property-tax/local-revenue territory)
- customs integration: unified revenue authority ↔ separate customs administration
- identifier schemes: dedicated TINs ↔ reuse of general identity numbers (SSN-style) ↔ multiple identifier types (EIN/ITIN/IP PIN…)
- payment rails: online direct pay, batch/electronic federal-style systems, card/wallets
- regime-specific compliance programs: publishing deliberate defaulters, whistleblower offices, voluntary disclosure, special reduction/reasonable-excuse doctrines
- registration drivers: proactive registration ↔ registration-on-first-filing
- deployment and build: in-house national systems ↔ COTS platforms ↔ ERP-suite public-sector solutions (vendor docs unreachable — see limitations)
- era-current layers: AI virtual assistants, contact centers, BI/risk analytics

### L3 — Vendor/Agency-specific (stays in Research Notes)

- GenTax: FastCore platform framing; brochure metrics (70+ agencies / 35+ states / 10+ countries / billions processed); Streamlined Sales Tax support; Fast Audit/Collection/Identity-Verification service packaging
- IRS: CP2000 notice series identifiers; EFTPS, Direct Pay, IP PIN program names; user-fee amounts and eligibility thresholds (e.g., $50,000/$100,000 online-application thresholds, 180-day short-term window); Publication numbers (594, 5, 5181); notice-of-lien/levy instrument names
- HMRC: SA302, internal-manual CH-code structure, "One to Many" label, PDDD (publishing deliberate defaulters) policy name
- None of these names/numbers may appear as canonical structure.

### Anti-overfitting checks

- **Shared-implementation ≠ invariant**: all three samples are self-assessment-flavored, but official-assessment regimes (common in continental traditions) also run tax administration — assessment tradition stays L2. The invariant is the conversion of declared/reported/assessed facts into account liabilities, not who computes the number.
- **Era-current ≠ definitional**: portals, e-file, AI assistants, BI are all L1/L2; the paper-era office (taxpayer registers, assessment registers, receipt ledgers, arrears books) satisfies L0 with none of them.
- **Single-source claims kept product-specific**: refund-offset mechanics documented directly only in IRS materials (elevated to B only as "common" behavior, not canonical); GenTax appeals machinery unconfirmed — appeals kept at L1 on HMRC/IRS evidence only.

## Rejected Findings

- **"Multi-entity distribution" as generic core** — the taxing-entity apportionment/distribution structure is the property-tax sibling's defining machinery. National tax administration settles to the treasury; GenTax's "distributed annually" phrasing refers to payment/refund flows, not entity apportionment. Rejected as a canonical element of this Type.
- **"Tax types = the defining unit"** — tempting (GenTax: "hundreds of tax types"), but a one-tax authority is still a tax administration. The invariant is the tax-type *structuring of accounts*, not the count/breadth.
- **"Portal-first" definition** — the citizen-facing portal is the most visible modern surface but is L1; administration machinery (assessment, arrears, compliance) is the Type's center.
- **"Billing-driven" definition (levy × rate)** — that is the property-tax variant's billing model. Generic tax administration is declaration/assessment-fed, not roll-fed.
- **CRM framing** — "customer and account management" (GenTax's phrase) must not be read as CRM; the "customer" is a statutory taxpayer with obligation accounts, not a commercial relationship record.

## Boundary Findings

| Neighbor | Seam | Test |
|---|---|---|
| **Property Tax Administration** (processed sibling) | substrate + feed + settlement: parcel-anchored bills fed by certified values × levies, money apportioned to taxing entities ↔ taxpayer-anchored obligation accounts fed by declarations/assessments, money settled to the treasury | remove the parcel/roll/levy machinery and administer taxpayer obligations → this Type; remove the taxpayer/obligation substrate and bill parcels from a roll → the sibling. Adjacent local taxes (business/fees) may bundle into either; the anchor defines the leaf. Keep both. |
| **Tax Preparation Application / Tax Filing Platform** (§08) | side of the transaction: taxpayer-side preparation/submission tools ↔ authority-side system of record; the return is the hand-off artifact (e-file programs are the interface) | the prep tool has no account of record, no assessment, no arrears; the administration system never prepares the return for the taxpayer. Keep separate. |
| **Corporate Tax Management / Tax Compliance Platform** (§08) | producer ↔ receiver: corporate provision/compliance machinery produces filings and provisions ↔ the administration system receives, assesses, and enforces them | corporate platforms model the company's tax position; the administration system models the jurisdiction's taxpayers. Keep separate. |
| **Government Revenue Management** (§24, unprocessed) | breadth: revenue accounting/collections across government sources ↔ tax-specific administration machinery (registration, assessment, compliance, disputes) | flag for that leaf's pass: overlap risk is real and the seam should be drawn from its own research. |
| **Government Service Portal** (§24) | surface ↔ system: the tax administration's self-service portal is a surface of this Type; a Government Service Portal aggregates many services across agencies | portal-only products without the administration machinery are a different Type. |
| **Government Licensing Management** (§24) | purpose of registration: authorization to operate ↔ creation/maintenance of tax obligation accounts (fees may ride along on tax platforms) | licensing's core object is a permission; this Type's core object is a liability account. |
| **Accounting Software / General Ledger** (§08/§10) | accounts of a business ↔ statutory tax accounts of a jurisdiction's taxpayers, driven by declarations/assessments with statutory charges and enforcement | double-entry bookkeeping machinery is not the subject here. |
| **Customs / Global Trade** (§10/§24) | duties on goods at borders are often administered by the same authority, but the customs core (goods declarations, tariffs, border process) is distinct machinery | unified-authority bundling is a variant, not a merge. |

**"Remove-what" summary for the closest seam:** remove the certified roll, the levy machinery, and the taxing-entity distribution, and add taxpayer registration, declarations/returns, and authority assessment → what remains is this Type. Remove taxpayer registration, declarations, assessment, compliance and disputes — leaving parcel bills fed by values × levies → what remains is the sibling.

## Uncertainties

1. **COTS market breadth under-sampled.** Only one COTS vendor (GenTax) was directly documented. SAP, CGI, and IRAS pages were unreachable (2×404 each, recorded per the network rule); Oracle documents no tax-administration product on its reachable public-sector page. Vendor-side market-structure claims are kept at moderate strength; no structural claim rests on the unreachable vendors.
2. **No help-center-level operational documentation for COTS products.** GenTax evidence is brochure/solutions-grade: it names functional areas but not workflows. All operational depth (assessment semantics, collection steps, notice behavior) comes from authority-side official documentation (HMRC, IRS), whose systems are in-house. The canonical model is therefore anchored on the *function* across jurisdictions, not on COTS product internals.
3. **GenTax appeals/dispute machinery unconfirmed** — not named in reachable materials. Kept out of any product-level claim.
4. **Regional coverage is UK/US-weighted.** Official-assessment traditions, unified customs+tax authorities, and non-Anglophone regimes are covered conceptually only; the definition was deliberately kept free of self-assessment assumptions to absorb this.
5. **Fees vs taxes boundary** — GenTax supports "tax types and fees"; where non-tax local levies end and tax begins is fuzzy and jurisdiction-specific. Noted as a variant axis; no taxonomy change proposed.
6. **Government Revenue Management overlap** — flagged for that leaf's own research pass; no directory change made from this side.

## Historical / Market-Sample Check

- **Paper-era tax office**: registers of taxable persons, assessment registers, receipt ledgers, arrears books, notice letters, appeals to a board — satisfies L0 in full with zero modern machinery. ✔
- **Mainframe-era national systems** (1960s-onward in-house master files): same loop, batch-processed — satisfies L0. ✔
- **Official-assessment regimes** (authority computes the liability): still registration + tax-type accounts + assess→post→settle — the definition does not bake in self-assessment. ✔
- **Single-tax small authorities** (one local levy + fees): tax-type-structured accounts still hold — breadth is L2. ✔
- **Platform-native/merged authorities** (tax + customs + social contributions in one system): the tax-administration core remains identifiable inside the merged system; merging is a variant. ✔

## Final Synthesis

A **Tax Administration System** is the revenue authority's system of record for administering taxes. Its defining core is exactly three jointly-held structures: (1) the **registered taxpayer population of record** — identified persons and entities under the authority's identifiers, with a registration lifecycle; (2) **tax-type-structured obligation accounts** — each taxpayer's accounts per administered tax type, whose balances carry assessed liabilities, posted payments/credits, and tracked arrears; and (3) the **assess→post→settle loop** — declarations/returns and authority assessments are processed into account liabilities, payments and credits post against them, overpayments are refunded, and unpaid balances persist as tracked arrears. Around this core, mature systems add the statutory machinery that makes administration real: charges (penalties/interest) on delinquency, governed notices, debt & enforcement (payment plans, liens, levies, refund offset), compliance/audit case machinery with information powers, dispute/appeal machinery, self-service portals, agent authorization, third-party information matching, and revenue reporting to the treasury. The Type is taxpayer-anchored and declaration/assessment-fed — which is precisely what separates it from the parcel-anchored, roll-fed, levy-driven Property Tax Administration sibling — and it is the authority-side system of record, which separates it from all taxpayer-side preparation/filing software. Lexical confirmation: the market's flagship COTS product self-labels "Tax Administration Software."
