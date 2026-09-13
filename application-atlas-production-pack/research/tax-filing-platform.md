# Research Notes — Tax Filing Platform

Research date: 2026-09-10

## Research Goal

Understand what a Tax Filing Platform actually is as an Application Type: what its system of record is, what its defining core is, how the filing work flows through it, and where its boundaries sit against the neighboring tax leaves in the directory (Tax Preparation Application, Tax Compliance Platform, Corporate Tax Management, Tax Administration System) and against adjacent Types (Payroll System, Legal E-filing Platform, Regulatory Reporting Platform).

This pass also carries two joint-review flags from prior tax-family passes:

1. **tax-compliance-platform pass (2026-09-10)**: "tax-filing-platform's defining scope untested here, joint review recommended at that pass (determination-in-scope = decisive test)" — the decisive test is whether transaction-level determination against maintained tax content is in scope.
2. **corporate-tax-management pass (2026-09-07)**: naming-overlap flag for the tax family; working discriminator held there: "submission mechanics (filing platform)" vs "single-taxpayer document-sourced preparation (tax preparation application)" vs "entity–jurisdiction–period tax position computed from the books (corporate tax management)" vs "transaction/document compliance (tax compliance platform)".

## Initial Boundary

Working hypothesis at start:

- A Tax Filing Platform is the filer-side system whose defining job is to get a tax return (or tax information return) from a filer to the tax authority in the authority's required electronic format, through the authorized channel, and to manage the authority's response (acceptance/rejection, correction, amendment).
- Nearest neighbors: Tax Preparation Application (forming the return from documents/interview), Tax Compliance Platform (transaction-level determination + compliance record), Corporate Tax Management (provision computed from books), Tax Administration System (the authority's own side), Payroll System (payroll tax filings embedded), Legal E-filing Platform (same submission shape, different domain).
- Known ambiguity: in market vocabulary, "tax filing platform" and "tax preparation software" are used almost interchangeably for consumer DIY products (TurboTax-class). The Type boundary must be drawn on structure, not marketing vocabulary.

## Research Questions

1. What is the system of record — the formed return, or the submission and its authority response?
2. What does "filing" consist of mechanically: format/schema, authorized channel, acknowledgment, correction loop?
3. Is tax computation (determination) in scope? At what level (return-level vs transaction-level)?
4. What varies across regimes (US federal+state, Canada NETFILE, UK MTD) and across filer classes (consumer, business information returns, professional preparers)?
5. Where does the consumer DIY market (which bundles preparation and filing) sit relative to the sibling leaf Tax Preparation Application?
6. What is the government-side boundary (authority-operated filing portals, certification regimes)?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different filer classes/regimes:

| Product | Pole | Access status |
|---|---|---|
| TurboTax (Intuit) — US | consumer DIY filing, preparation-bundled, dominant share | Fetched (product root + disclosures) |
| TurboTax (Intuit) — Canada | same product family in a different regime (NETFILE certification, Quebec dual returns) | Fetched (product root + FAQ) |
| TaxAct (Taxwell) | consumer DIY + professional + business; value positioning | Fetched (product root + e-file status page) |
| Yearli (Greatland) | business information-return e-filing, import-native (W-2/1099/1095) | Fetched (product root) |
| GOV.UK (HMRC) | authority-side reference for the receiving end (VAT returns, MTD software mandate) | Fetched (guidance pages) |

Attempted but unreachable (bot protection / transport errors / closed service) — recorded as sourcing limitations, not compensated from model memory:

- irs.gov (404 on two paths) — the US authority-side e-file description could not be fetched directly
- tax1099.com, help.zenwork.com (403 / transport error)
- hrblock.com (403)
- cleartax.in / clear.in (403)
- taxslayer.com, freetaxusa.com (403)
- drakesoftware.com (403)
- canada.ca (timeout)
- efile.com — reachable but the service has **closed** (market fact: a consumer e-file provider exited; former customers directed to IRS transcript services)

## Sources

- TurboTax US — https://turbotax.intuit.com/ (product root, filing options, guarantees, disclosures) — fetched 2026-09-10
- TurboTax Canada — https://turbotax.intuit.ca/ (product root, NETFILE FAQ, CRA Auto-fill, Quebec dual-return FAQ) — fetched 2026-09-10
- TaxAct — https://www.taxact.com/ (product root) and https://www.taxact.com/post-filing/efile-refund-status (e-file/refund status) — fetched 2026-09-10
- Yearli — https://www.yearli.com/ (product root, plans, how-it-works, FAQ) — fetched 2026-09-10
- GOV.UK — https://www.gov.uk/vat-returns and https://www.gov.uk/submit-vat-return/how-to-send-vat-return (VAT return mechanics, MTD-compatible software mandate) — fetched 2026-09-10
- eFile.com — https://www.efile.com/ (closure notice) — fetched 2026-09-10

Evidence layers used below: **A** = directly observed on a fetched official source for a specific product; **B** = cross-product commonality across the fetched sample; **C** = canonical inference from comparison and Type-boundary reasoning.

## Product Observations

### TurboTax (US) — consumer DIY filing, preparation-bundled pole (Layer A)

- Self-positioning is filing-first in vocabulary ("File Taxes Online", "Ways to file") while the product's machinery is the full preparation-to-filing path: DIY guided interview, Expert Assist (advice + final review), Expert Full Service (expert prepares and signs), desktop, prior-year filing, extension filing.
- Document/data intake: "Snap a photo, upload your docs, or import them directly from your employer or financial institution."
- E-file acceptance is a first-class recorded milestone: refund-advance eligibility and disbursement are explicitly keyed to "the IRS accepts your e-filed federal tax return"; refund tracking ("Where's my refund") is a standing surface; refund timing language ties to e-file acceptance.
- Post-acceptance lifecycle: amendment ("Easy Online Amend" with product- and year-dependent windows), prior-year return access (up to seven years of returns on file), extension filing.
- Business model variants riding the filing: Refund Advance loans, File Now Pay Later, refund-based fee payment, audit support/defense, maximum-refund and accuracy guarantees.
- Free-edition eligibility is scoped by form complexity (simple Form 1040 only); business products have explicit situation limits (e.g., stated limits on state filings and unsupported entity types).
- Payment timing: "pay only when you are ready to e-file, print, file by mail" — the e-file/print moment is the billing gate.

### TurboTax Canada — same family, different regime (Layer A)

- NETFILE regime documented in-product: "Implemented by the Canada Revenue Agency (CRA) in 2001, NETFILE is an electronic tax filing service… NETFILE allows you to use various approved software (such as TurboTax) to submit your return directly to the CRA online." And: "Income tax preparation software companies must seek NETFILE certification from the CRA for tax preparation software products to be used in conjunction with CRA's NETFILE electronic tax filing service." All 2025 products are stated as NETFILE-certified.
- Authority-data import: CRA "Auto-fill my return" pulls slips and carry-forward amounts from the filer's CRA account; prior-year T1 upload for switching.
- Multi-authority variant: Quebec residents file two separate returns — T1 to the CRA and TP1 to Revenu Québec — both supported in-product.
- Refund tracker as a live surface; spousal returns optimized together; pay-when-you-file billing gate at e-file/print; CRA-certified badges; prior-year filing.

### TaxAct — consumer DIY + professional + business (Layer A)

- "Authorized e-file provider" badge displayed on product pages; "Check E-file Status" and "Check Refund Status" as standing post-filing surfaces; "E-File Concierge" service provides phone support specifically for "federal e-file status changes".
- Rejection is an explicit handled state: the satisfaction guarantee covers the case where "your e-file was rejected by the IRS or State and you cannot re-file".
- Scale claim: "Over 113 million returns filed: Based on e-filed federal returns through TaxAct Consumer and TaxAct Professional software since 2000."
- Billing gate at the filing moment ("start free and pay when you file… prior to printing or e-filing").
- Family of products across filer classes: consumer 1040 editions, business returns (partnerships, C/S corps, sole proprietors, tax-exempt), and TaxAct Professional for CPAs/EAs/preparers with "tax preparation tools, e-filing options"; family brands include Drake Software, 1040.com, Taxwell.
- Extension filing, prior-year filing, state refund tracking, refund advance/transfer (bank products), audit defense.

### Yearli (Greatland) — business information-return e-filing, import-native pole (Layer A)

- Scope: "complete W-2, 1099 & 1095 filing with federal agencies, states, and recipients in one workflow" — including quarterly filing (employer quarterly returns class).
- Data enters by entry **or import**: "Add form information manually or import data from compatible accounting, payroll, or tax software" — 40+ integrations plus a generic import template. The platform does not need to be where the data was prepared.
- Pre-submission validation: "Yearli helps check your entries and flags potential issues before you submit"; TIN matching (per-form or unlimited by plan) to reduce errors.
- Transmission is handled by the platform's authorized e-file service: "You don't need a Transmitter Control Code (TCC) to file 1099 forms with Yearli. Our authorized e-file service handles the process for you" — the filer does not need their own authorization to transmit.
- Recipient delivery: copies to employees/contractors by print-and-mail or secure online delivery, alongside agency filing.
- Multi-client workflows for accountants, PEOs, and service providers filing on behalf of multiple businesses; volume-tiered plans; deadline-driven season with peak-pricing windows; a deadlines page as a standing surface.

### GOV.UK (HMRC) — authority-side reference (Layer A, receiving end)

- The VAT Return is a periodic obligation (typically quarterly accounting period) with a fixed deadline (one calendar month and 7 days after period end, also the payment deadline).
- Submission channel is regulated: "You must submit your VAT Return using accounting software that's compatible with Making Tax Digital" — the authority maintains a list of compatible software; paper returns carry penalties unless exempt.
- Receipt is checkable by the filer: "You can use your VAT online account to check if HMRC has received your VAT return."
- Corrections are a documented post-submission path ("Correct errors in your VAT Return").
- This confirms from the authority's side the same structure the filer-side products implement: authority-bound form/period/deadline, authorized-software channel, receipt/acknowledgment state, correction loop.

### eFile.com — market fact (Layer A)

- The service has closed; the site thanks customers and directs former users to IRS transcript services. A consumer e-file provider exiting the market is direct evidence that the filing layer is a competitive, consolidating market — and that filing history outlives the platform (filers must retrieve their own records from the authority afterward).

## Cross-product Comparison

| Structure | TurboTax US | TurboTax CA | TaxAct | Yearli | GOV.UK (authority) |
|---|---|---|---|---|---|
| Filing unit of record (filer × authority × form/period) | ✓ | ✓ | ✓ | ✓ | ✓ (obligation side) |
| Authority-bound form/format/deadline machinery | ✓ | ✓ | ✓ | ✓ | ✓ (defines it) |
| Authorized/certified channel | ✓ (authorized provider) | ✓ (NETFILE certification) | ✓ (authorized provider badge) | ✓ (authorized e-file service, TCC handled) | ✓ (MTD-compatible software list) |
| Transmission + acknowledgment/receipt state | ✓ (accept milestone, refund keyed to it) | ✓ | ✓ (e-file status, rejection handled) | ✓ (files with agencies; validation before submit) | ✓ (check receipt in online account) |
| Correction / amendment path | ✓ (Easy Online Amend) | ✓ (amended-return guarantee language) | ✓ (rejection → re-file) | ✓ (corrections implied by validation loop; corrections service in market) | ✓ (corrections guidance) |
| In-product preparation (interview/computation) | ✓ (center of gravity) | ✓ | ✓ | minimal (entry/import; validation only) | n/a (accounting software holds the data) |
| Data import from external systems | ✓ (employer/financial import, photo) | ✓ (CRA Auto-fill, prior-year T1) | ✓ (import tax data) | ✓ (40+ integrations, generic template) | — |
| Recipient copies (W-2/1099 class) | n/a | n/a | n/a | ✓ (print/mail or secure online) | — |
| Multi-authority splitting | ✓ (federal + state) | ✓ (CRA + Revenu Québec) | ✓ (federal + state) | ✓ (federal + state) | single authority |
| Refund/balance-due money surfaces | ✓ (+ bank products) | ✓ | ✓ (+ bank products) | n/a | payment deadline on authority side |
| Professional/preparer mode | ✓ (Expert Full Service) | ✓ | ✓ (TaxAct Professional) | ✓ (multi-client service providers) | — |
| Government-operated equivalent | — | — | — | — | ✓ (VAT online account) |

## Canonical Model

### L0 — Defining Invariant (minimal)

The Tax Filing Platform is the **filer-side system of record for submitting a tax return (or tax information return) to a tax authority through the authority's authorized electronic channel, and for managing the authority's response**. Three jointly-held structures:

1. **The filing of record** — a persistent, identified submission unit: one filer × one authority × one form/period, carrying the reported figures and the filer's identity, held with lifecycle state (in preparation → transmitted → accepted / rejected → corrected / amended). Remove → a tax calculator or a form editor.
2. **Authority-bound validity** — the submission is assembled into the exact form, format, and deadline the specific authority requires for that filing (form catalog, schema/validations, certification requirements), so that the authority can accept it. Remove → a generic form/document tool.
3. **Authorized-channel transmission with recorded acknowledgment** — the platform transmits through the authorized e-file path (as an authorized provider, via certified software, or through the authority's own channel) and records the authority's official response (accepted / rejected with reasons), driving the correction-and-refile loop; filing status is first-class, user-visible state. Remove → a print-and-mail preparer or a PDF generator.

Framer: the filer side (taxpayer, business, or a preparer/service acting for the filer) — not the authority's own administration.

Jointly-held load-bearing:

- 1 alone = tax form worksheet / document editor
- 2 without 1 = a form library / rule content
- 3 without 1+2 = generic e-delivery / upload portal
- 1+2 without 3 = return preparation with print-and-mail (Tax Preparation Application territory)
- 1+3 without 2 = e-delivery with no tax validity
- 2+3 without 1 = a bare transmitter / the authority's own gateway infrastructure

### L1 — Common Mature Structure

- **Filing status as a user-visible surface** — e-file status tracking (transmitted / accepted / rejected), refund tracking keyed to acceptance, and in one sampled product a paid concierge service for status changes. All sampled commercial products expose this.
- **Correction and amendment loop** — rejected-return correction and re-transmission; post-acceptance amendment (amended returns); corrections guidance on the authority side.
- **Data intake from external sources** — import from employers/financial institutions/government accounts (CRA Auto-fill), photo/upload of documents, integration imports from accounting/payroll/tax software (40+ in the import-native pole), generic import templates.
- **Deadline machinery** — deadline pages, reminders, extension filing, peak-season pricing windows.
- **Money surfaces** — refund/balance-due presentation, refund timing expectations, direct-deposit setup; bank products (refund advance, refund transfer, pay-later) common at the consumer pole.
- **Multi-authority handling** — federal + state (US), CRA + Revenu Québec (Canada); per-authority submission and receipt tracking.
- **Preparer/service mode** — professionals and service providers filing on behalf of many filers (multi-client workflows, preparer signing).
- **Guarantees and support tiers** — maximum-refund, accuracy, audit-support guarantees; expert-assist/full-service tiers.

### L2 — Variant / Optional Structure

- **In-product preparation depth** — full guided interview with computation (consumer pole) vs minimal entry/import with validation only (information-return pole) vs none (managed filing where the provider assembles and files). The decisive variant axis, not a boundary.
- **Filer class** — individual income tax; business income tax (entity returns); information returns (W-2/1099/1095 class with recipient copies); quarterly employer returns.
- **Regime realization** — US authorized-provider e-file with federal/state split; Canada NETFILE certification + Quebec dual returns; UK MTD-compatible-software mandate; other regimes substitute their own certification/channel machinery.
- **Operator** — commercial platform vs government-operated free filing portal (the authority's own surface).
- **Business-model riders** — free tiers scoped by form complexity, pay-when-you-file billing gates, refund-based payment, bank products, audit defense, expert review tiers.
- **Surfaces** — web, desktop, mobile app, snap-a-photo intake, AI assistants.

### L3 — Vendor-specific (Research Notes only)

- TurboTax: "Easy Online Amend" windows differ by product tier and year; refund-advance loan mechanics (WebBank, Credit Karma Money account requirements, eligibility exclusions); Expert Full Service same-day validation call; seven-year return-access framing ("lifetime of your return").
- TaxAct: "E-File Concierge" phone service for federal e-file status changes; $100k accuracy guarantee; 113M+ e-filed returns since 2000 claim; family brands (Drake, 1040.com, Taxwell).
- Yearli: TCC-handling framing ("you don't need a Transmitter Control Code"); per-form vs unlimited TIN matching by plan; peak-pricing date windows; volume-tiered plan ladder (Core/Performance/Premier/Custom).
- TurboTax Canada: NETFILE certification framing; CRA Auto-fill requires CRA My Account enrollment; Quebec TP1 handling excluded from one service tier.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical core. The most tempting over-generalizations and their rejection:

- **"A filing platform prepares your taxes"** — rejected as definitional. The import-native pole (Yearli) files returns whose data was prepared entirely elsewhere; the UK MTD regime explicitly separates the accounting software (which holds the data) from the submission act. Preparation is the consumer pole's front half, not the Type's invariant.
- **"A filing platform computes your tax"** — rejected at transaction level. Return-level computation exists where preparation is in-product (consumer pole); transaction-level determination against maintained tax content is the Tax Compliance Platform's defining leg and is out of scope here. This discharges the determination-in-scope decisive test from the tax-compliance-platform pass.
- **"Filing always includes refund tracking"** — common (all consumer-pole products) but absent in the information-return pole (no refund exists for W-2/1099 filings) and meaningless for balance-due-only filers. L1, not L0.
- **"Filing platforms are consumer products"** — rejected. The business information-return segment and professional preparer segment are substantial and structurally identical at the core.

## Boundary Findings

### vs Tax Preparation Application (sibling leaf, still unprocessed)

The market straddles: consumer DIY products are marketed as both "tax preparation software" and "tax filing platforms"; the same products (TurboTax, TaxAct) appear in both framings. The structural seam is the **center of gravity of the system of record**:

- Tax Preparation Application: the formed return — gathering the taxpayer's documents/situation, interviewing, computing, producing the return draft. Filing is commonly integrated but is the closure step of preparation.
- Tax Filing Platform: the submission and its authority response — the return (formed in-product, imported, or prepared by a service) moves through authority-bound assembly, authorized-channel transmission, acknowledgment, and the correction/amendment loop. Preparation may be in-product, minimal, or absent.

Pure-pole products exist on both sides: preparation-centric products whose filing is one button, and filing-only platforms (Yearli-class import-native e-filing; managed/AutoFile services) that never touch preparation. The bundled consumer middle is the straddle zone. **Joint review with tax-preparation-application is recommended when that leaf is processed**; this pass holds the discriminator "submission mechanics" consistent with the corporate-tax-management pass.

### vs Tax Compliance Platform (processed 2026-09-10)

Decisive test discharged: **transaction-level determination is NOT in scope** for the filing platform. The compliance platform determines tax per transaction against vendor-maintained jurisdictional content, accumulates a tax transaction record of record, and runs an obligation-to-filing pipeline over its own accumulated records (including managed filing execution). The filing platform's tax figures arrive already computed (return-level, from preparation or import); it owns the submission act and the authority's response, for any return whose data exists regardless of who computed it. Keep-both confirmed from this side; the compliance pass's flag is RATIFIED with this scope.

### vs Corporate Tax Management (processed 2026-09-07)

Corporate tax management's object of record is the entity–jurisdiction–period tax position computed from the books (provision); e-filing is one closure step of that computation. The filing platform has no computation of record — it is the submission machinery. Consistent with that pass's discriminator ("keep only submission and remove computation/evidence → filing platform"). Confirmed.

### vs Tax Administration System (§24, government)

The receiving authority's system of record (tax rolls, assessment, collection, the administration's own registers) vs the filer-side submission system. The boundary pole: **government-operated filing portals** (HMRC's VAT online account; IRS Direct File-class services; NETFILE's own channel) — same submission mechanics, but owned and operated by the authority as part of its administration. Commercial filing platforms exist precisely because filers need preparation, guidance, multi-authority orchestration, and record-keeping beyond what the authority's own portal offers. Recorded as a boundary pole, not a separate Type question.

### vs Payroll System (processed)

Payroll systems embed payroll-tax deposits and filings (full-service payroll providers file and remit on the employer's behalf). That filing function is embedded in the payroll money loop; the filing platform is standalone submission machinery that also serves information returns, income-tax returns, and any other authority filing. Payroll-filing is a feeder/embedded case, not this Type's center.

### vs Legal E-filing Platform (§11)

Same abstract shape — submission to an authority in a required format with recorded acceptance/rejection — but a different domain world: courts and legal instruments vs tax authorities and tax returns; different validity machinery (court rules vs tax schemas/certification); different consequences. Separate Types; the shared shape is worth noting, not merging.

### vs Regulatory Reporting Platform (§13)

Filing/submission machinery for regulator deliverables (taxonomies, validations, submissions) is structurally adjacent. Tax filing is distinguished by taxpayer identity binding, the authorized-provider/certification regime, and the money consequences (refund/balance due). Keep separate.

### Historical / market-sample check (§24)

The Type is **e-file-era by origin**: US e-file began as a pilot in the 1980s with professional transmitters; NETFILE dates to 2001 (per TurboTax Canada's own FAQ); MTD-compatible-software mandates are 2019+. The pre-electronic predecessor artifact — the paper return completed and mailed — is not a form of this Type; print-and-mail-only preparation software belongs to the preparation side. Early-era realizations (desktop software transmitting electronically with paper signature documents; professional ERO/transmitter services) satisfy the L0 core: transmission through the authorized channel plus recorded acknowledgment plus correction. The definition therefore does not over-fit the current consumer web-app era.

## Uncertainties

1. **Tax1099 / Zenwork** could not be fetched (403). Its self-description as an "IRS-authorized e-filing platform" for information returns is market-known, but no operational detail from it is asserted in this pass; Yearli carries the import-native pole's evidence alone.
2. **IRS authority-side e-file documentation** (irs.gov) unreachable; the authorized-provider/acknowledgment mechanics are evidenced from the filer-side products' own disclosures and the UK authority's guidance rather than from the US authority directly.
3. **Non-US commercial poles** (India, UK commercial software, Australia) unreachable in this pass; regime variation is evidenced via TurboTax Canada (NETFILE) and GOV.UK (MTD) only. Assertion strength for other regimes is held at "regimes substitute their own machinery" level.
4. **Exact status vocabularies** (per-product state names for e-file status) were not researched per-product; the canonical states (transmitted / accepted / rejected / corrected) are held at conceptual level.
5. Whether the market will keep "Tax Filing Platform" and "Tax Preparation Application" as separate commercial categories or converge on one bundled category is a market question, not resolvable here; the structural seam is recorded for joint review.

## Final Synthesis

The Tax Filing Platform is the filer-side submission system of record. Its defining core is exactly three jointly-held structures: the filing of record (filer × authority × form/period, with lifecycle state), authority-bound validity (the form/format/deadline/certification machinery that makes the authority able to accept it), and authorized-channel transmission with recorded acknowledgment (transmit, receive accepted/rejected, correct and refile, amend). Everything else — in-product preparation, refund tracking, money rails, guarantees, expert tiers, recipient copies, multi-authority orchestration, government-operated equivalents — is common, variant, or boundary, not definition. The Type is e-file-era by origin; the paper return plus postal mail is its predecessor artifact, not a form of it. The two prior tax-family flags are discharged: determination (transaction-level) is out of scope (vs Tax Compliance Platform), and the "submission mechanics" discriminator is held (vs Corporate Tax Management); a new joint-review flag is recorded for Tax Preparation Application, whose center (the formed return) is this Type's mirror image.
