# Research Notes — Tax Preparation Application

Research date: 2026-09-10

## Research Goal

Understand what a Tax Preparation Application actually is as an Application Type: what its system of record is, what its defining core is, how the preparation work flows through it, and where its boundaries sit against the neighboring tax-family leaves in the directory (Tax Filing Platform, Tax Compliance Platform, Corporate Tax Management, Tax Administration System) and against adjacent Types (Payroll System, Accounting Software, tax calculators, Personal Finance Management).

This pass carries three inherited joint-review flags from prior tax-family passes:

1. **corporate-tax-management pass (2026-09-07)**: naming-overlap flag for the tax family; working discriminator held there: "submission mechanics (filing platform)" vs "**single-taxpayer document-sourced preparation (tax preparation application)**" vs "entity–jurisdiction–period tax position computed from the books (corporate tax management)" vs "transaction/document compliance (tax compliance platform)". Joint review recommended when this leaf is processed.
2. **tax-compliance-platform pass (2026-09-10)**: scope question for the tax family; seam vs Tax Preparation Application held there as "consumer/individual income-tax preparation (interview-driven personal return); different users, objects, and workflow."
3. **tax-filing-platform pass (research 2026-09-10)**: "Joint review with tax-preparation-application is recommended when that leaf is processed; this pass holds the discriminator 'submission mechanics'." That pass drew the seam as: Preparation's system of record = **the formed return** (gathering the taxpayer's documents/situation, interviewing, computing, producing the return draft; filing commonly integrated as the closure step of preparation); Filing Platform's system of record = the submission and the authority's response.

## Initial Boundary

Working hypothesis at start:

- A Tax Preparation Application is the taxpayer-side application whose defining job is to form a complete tax return for one taxpayer (filing unit) from the taxpayer's own situation: gathering tax facts (documents, imports, answers), assembling them into the jurisdiction's required return structure, computing the tax under that jurisdiction's rules, reviewing the result, and producing the finished return ready for signature and submission.
- Nearest neighbors: Tax Filing Platform (submission machinery — the mirror image), Tax Compliance Platform (transaction-level indirect-tax determination), Corporate Tax Management (organization's books-derived provision), Tax Administration System (the authority's receiving side), Payroll System (feeder of wage/income documents and withholding), Accounting Software (feeder of business books), Tax Calculators / Personal Finance (estimate vs return).
- Known ambiguity: market vocabulary uses "tax preparation software," "tax filing software," and "tax software" almost interchangeably for consumer DIY products. The Type boundary must be drawn on the center of gravity of the system of record, not marketing labels.

## Research Questions

1. What is the unit of record — the formed return, the submission, or the taxpayer's situation?
2. What does "preparation" consist of mechanically: situation intake (interview vs form entry vs import), form/schedule assembly, computation, review?
3. Who holds and maintains the tax rules content, and who authors what?
4. Where does e-filing sit — definitional or integrated closure step? (Decisive for the Tax Filing Platform seam.)
5. What varies across filer classes (consumer self-preparer, professional preparer firm, entity/business returns) and across regimes (US federal+state, Canada NETFILE/CRA + Revenu Québec)?
6. What is the professional-preparer mode: how does the same preparation core serve a firm preparing hundreds of client returns?
7. What money surfaces (refund/balance due, bank products) ride the preparation, and are any definitional?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers/regimes:

| Product | Pole | Access status |
|---|---|---|
| TurboTax (Intuit) — US, DIY + Expert tiers | consumer DIY guided-interview pole, dominant share, expert-assisted variants riding the same product | Fetched (root + DIY how-it-works page + guarantees/disclosures) |
| TaxAct (Taxwell) | value-positioned consumer DIY + business entity returns + professional | Fetched (consumer root + professional root + FAQs) |
| TaxAct Professional | professional preparer pole (CPAs/EAs/preparer firms preparing many client returns) | Fetched (product root, workflow add-ons) |
| UFile (Thomson Reuters) — Canada | regional-regime pole (CRA NETFILE + Revenu Québec), desktop + online + pro + corporate (T2) + volunteer (CVITP) variants | Fetched (root + product family) |

Attempted but unreachable (bot protection) — recorded as sourcing limitations, not compensated from model memory:

- hrblock.com (403) — the hybrid in-person-preparer + software pole could not be fetched; its posture is evidenced indirectly through the Expert Full Service / Xpert Full Service tiers of the sampled products
- drakesoftware.com (403) — the professional-pole market leader could not be fetched; TaxAct Professional carries the professional pole's evidence (note: Drake is a TaxAct family brand)
- taxslayerpro.com (403); freetaxusa.com (403, also in the tax-filing pass)

## Sources

- TurboTax — https://turbotax.intuit.com/ (root; product tiers; guarantees; Important Details disclosures) — fetched 2026-09-10
- TurboTax — https://turbotax.intuit.com/personal-taxes/online/file-your-own-taxes/ (DIY product page; preparation flow; FAQs) — fetched 2026-09-10
- TaxAct — https://www.taxact.com/ (consumer root; product ladder; FAQs; guarantees) — fetched 2026-09-10
- TaxAct Professional — https://www.taxact.com/professional/ (professional root; pricing models; workflow add-ons; e-signature and EFIN resources) — fetched 2026-09-10
- UFile — https://www.ufile.ca/ (Canada root; NETFILE certification; Auto-fill; product family) — fetched 2026-09-10
- Sibling research (context alignment, not primary evidence): research/tax-filing-platform.md, research/tax-compliance-platform.md, research/corporate-tax-management.md, research/tax-administration-system.md

Evidence layers used below: **A** = directly observed on a fetched official source for a specific product; **B** = cross-product commonality across the fetched sample; **C** = canonical inference from comparison and Type-boundary reasoning.

## Product Observations

### TurboTax (US) — consumer DIY guided-interview pole (Layer A)

- Self-description of the DIY product: "Just answer simple questions and we'll guide you through filing your taxes"; the DIY page's promise: "Upload your forms and answer a few questions to get your max refund with 100% accuracy—guaranteed."
- Situation intake is multi-channel: "Snap a photo, upload your docs, or import them directly from your employer or financial institution." Mobile photo capture with autofill ("1099-K Snap and Autofill", "1099-NEC Snap and Autofill") documented per form type.
- The interview guides the taxpayer's situation: coverage spans W-2 income, interest/dividends, education credits, EITC/CTC, retirement distributions, mortgage/property-tax deductions, donations, self-employment/gig, investments/crypto, rental property — the situation determines the path.
- Review machinery: "TurboTax Do It Yourself double-checks your return for errors as you go, and before you file" (FAQ), plus a named final-check step ("Complete Check™"). AI-assisted guidance (Intuit Assist) explains the tax outcome along the way.
- Coverage ladder keyed to situation complexity: Free Edition (simple Form 1040 only, eligibility scoped — "~37% of filers qualify," explicit lists of included/excluded situations) → Deluxe → Premier (investments) → Self-Employed/Premium; business situations supported via Expert Assist/Full Service Business and TurboTax Business desktop (with explicit unsupported-entity lists: C-Corps 1120, Trusts/Estates 1041, tax-exempt — those entity returns are out of scope for the online products).
- Expert tiers ride the same product and the same return: Expert Assist ("advice from tax experts as you file, as well as a final expert review") and Expert Full Service ("a tax expert will do your taxes, start to finish… The tax expert will sign your return as a preparer") — the handoff is a service layer over one preparation core, with preparer-signature semantics ("the tax expert may be required to sign as the preparer").
- Closure and retention: pay-when-you-file gate at the "e-file, print, file by mail" moment ("Satisfaction Guaranteed: Some versions… may be used without charge up to the point you decide to print or electronically file"); Tax Return Access "up to seven years of tax returns we have on file for you"; Easy Online Amend (post-acceptance amendment with product/year-dependent windows); extension filing and prior-year filing as standing options.
- Guarantees attach to the preparation: 100% Accurate Calculations ("lifetime of your return, which Intuit defines as seven years"), Maximum Refund ("if you get a larger refund or smaller tax due from another tax preparation method by filing an amended return…"), Audit Support. Refund/balance-due money rails (direct deposit, refund-advance loans, pay-from-refund) are disclosed as separate add-on programs.

### TaxAct (US) — value-positioned consumer + business + professional (Layer A)

- The company's own scope statement is preparation-first: "Our services help customers prepare their tax returns. We offer federal and state DIY tax preparation, tax planning tools, and access to tax advice. We also provide tools to help you import tax data, calculate your deductions and credits, and maximize your tax refund."
- Product ladder mirrors the situation-complexity scoping: Free (W-2/students, eligibility FAQ) → Deluxe (home ownership, child/dependent care, HSA) → Premier (stocks/crypto, home sale, rental) → Self-Employed (freelance, sole proprietor); the FAQ's included/excluded situation lists parallel TurboTax's.
- Named optimization machinery: "Deduction Maximizer guides you step by step through the process of completing your return in a way that helps you uncover additional tax advantages… by checking dozens of additional deductions."
- Business returns are a first-class line: "Our tax filing options for businesses apply to Partnerships, C Corporations, S Corporations, Sole Proprietors, and Tax-Exempt Orgs."
- Professional line: "we offer a tax preparation software called TaxAct Professional, which is specifically designed for professionals including Certified Public Accountants (CPAs), Enrolled Agents (EAs), and tax preparers. TaxAct Professional features tax preparation tools, e-filing options, and comprehensive support."
- Post-acceptance states are explicit: "Check E-file Status" / "Check Refund Status" surfaces; the satisfaction guarantee covers "your e-file was rejected by the IRS or State and you cannot re-file"; E-File Concierge phone service for federal e-file status changes.
- Guarantees: Maximum Refund ("If, using the same information, a registered user… receives a larger refund or owes a smaller tax due amount using another online tax preparation product, we will refund the… purchase price"), $100k Accuracy Guarantee, Satisfaction (pay when you print or e-file). AI in-product assistant (SmartFile AI: "Ask questions, understand what to do next, and move through your return").
- Scale/heritage claim: "Over 113 million returns filed… through TaxAct Consumer and TaxAct Professional software since 2000." Family brands: Drake Software, 1040.com, Taxwell. Prior-year filing, extension filing, refund advance/transfer (bank products) as riders.

### TaxAct Professional — professional preparer pole (Layer A)

- Positioning: "Powerful, professional tax software" for firms; "A legacy of 25 years and over 110 Million successfully processed e-files."
- Practice-scale pricing models: "Unlimited bundles for high-volume firms filing both individual and business returns"; "Low-volume bundle with 20 or 40 returns for smaller practices"; "Pay-per-return for maximum flexibility" — the unit of consumption is the return, at firm scale.
- Client-situation intake at practice level: "Easy Import Clients Data — Save time, increase efficiency and decrease errors with TaxAct's import options."
- Signature machinery is first-class: in-product E-Signatures "available for tax year 2025 on tax return documents, such as e-file authorization forms (federal Form 8879 and state equivalents), applications for Bank Products, and other documents related to tax preparation services."
- Client collaboration add-ons: "Client Exchange — A secure way to exchange documents with your clients"; "Client Portals by Drake Software — Your Hub for Client Collaboration"; client-facing "reports and tools to easily provide clients with customized tax planning information."
- Regulatory-identity resources: "Apply / Verify Your EFIN," PTIN resources, "IRS Requirements" articles for new preparers — the preparer's own authorization regime is part of the product's world.
- Bank products at the practice level: "Pay-by-Refund" (refund transfers), "Cash Advances," "Software Purchase Assistance" — with ERO (Electronic Return Originator) enrollment semantics disclosed by the partner banks; the preparer firm, not the taxpayer, is the enrolled party.
- Free Evaluation Edition "does not include the ability to file returns with the IRS" — evaluating the preparation without the filing act is an explicitly supported posture.

### UFile (Canada) — regional-regime pole (Layer A)

- Positioning: "UFile is a Canadian tax software"; 20+ years serving Canadian taxpayers; Thomson Reuters/Tax & Accounting brand.
- Regime machinery: "UFile is Netfile Certified — File your tax return directly with the CRA (and Revenu Quebec) electronically **instead of printing and mailing it in**." This vendor's own phrasing frames e-transmission as the modern alternative to the preparation product's print-and-mail posture — direct evidence that print-and-mail preparation is inside the Type.
- Authority-data import: "Auto-fill my return — Automatically download your tax information from most tax slips from the CRA."
- Situation coverage framed by complexity poles: self-employment ("from simple to the most complex"), investment income ("capital gains and losses, all in one place"), rental properties.
- Optimization claim attached to preparation: "UFile explores every possible tax-saving opportunity – automatically"; "UFile makes preparing your tax return easy-to-use" — the vendor's own verb for the product is *preparing*.
- Product family spans the filer-class and deployment axes on one preparation core: UFile ONLINE (web), UFile WINDOWS (desktop), UFile PRO (professional), UFileT2 (corporate T2 returns), prior tax years, UFile CVITP (the Community Volunteer Income Tax Program — free software for volunteers preparing returns for low-income taxpayers).
- Triple Guarantee (Accuracy, Satisfaction, Best Tax Result); retail heritage visible in a store locator.

## Cross-product Comparison

| Structure | TurboTax US | TaxAct consumer | TaxAct Professional | UFile (Canada) |
|---|---|---|---|---|
| Return as the persistent unit of record (filing unit × authority × year) | ✓ (multi-year access: "seven years of tax returns on file") | ✓ | ✓ (per-client returns at firm scale) | ✓ (prior tax years product line) |
| Situation intake: interview Q&A | ✓ (center of gravity) | ✓ ("step-by-step guidance") | secondary | ✓ |
| Situation intake: document/photo/import | ✓ (snap/upload/import from employer/financial institutions) | ✓ (import tax data; mobile photo) | ✓ ("Easy Import Clients Data") | ✓ (CRA Auto-fill) |
| Prior-year carryforward / prior-year filing | ✓ | ✓ | ✓ | ✓ (prior-years line) |
| Situation→forms assembly (eligibility-driven form selection) | ✓ (free-tier scoping lists which situations/forms are included) | ✓ (situation ladders per edition) | ✓ (individual + business entity forms) | ✓ (self-employment/investment/rental poles) |
| Computation under vendor-maintained rules | ✓ (100% Accurate Calculations Guarantee) | ✓ ($100k Accuracy Guarantee) | ✓ | ✓ (Accuracy guarantee) |
| Review before completion (errors "as you go and before you file") | ✓ ("double-checks… Complete Check") | ✓ (alerts; AI assistant) | ✓ ("alerts built into the system" — user review) | ✓ (implied by guarantees; optimization claim) |
| Optimization layer (deduction/credit maximization) | ✓ ("max refund" framing) | ✓ (Deduction Maximizer) | ✓ (tax planning reports for clients) | ✓ ("every possible tax-saving opportunity") |
| Signature/authorization step | ✓ (self-serve; expert "will sign your return as a preparer") | ✓ | ✓ (e-signature on Form 8879 e-file authorizations) | ✓ (NETFILE signature flow) |
| E-filing integrated | ✓ | ✓ (e-file status surfaces) | ✓ (EFIN regime) | ✓ (NETFILE-certified) |
| Print-and-mail posture available | ✓ ("print, file by mail" as the billing-gate alternative) | ✓ ("prior to printing or e-filing") | ✓ (evaluation edition excludes filing; printing implied) | ✓ ("instead of printing and mailing it in") |
| Multi-authority handling | ✓ (federal + state) | ✓ (federal + state) | ✓ (state products) | ✓ (CRA + Revenu Québec) |
| Refund/balance-due money surfaces | ✓ (+ bank products) | ✓ (+ bank products) | ✓ (practice-level bank products, ERO) | ✓ (refund timing claim) |
| Entity/business returns | partial (S-corp/partnership via Expert; Business desktop for 1120/1041) | ✓ (1120/1120-S/1065/990-class per marketing) | ✓ (individual + business) | ✓ (UFileT2) |
| Service tiers over the same core (expert assist / full service) | ✓ (Expert Assist / Full Service) | ✓ (Xpert Assist / Full Service) | n/a (the firm IS the preparer) | n/a |
| Free/volunteer variant | ✓ (Free Edition, eligibility-scoped) | ✓ (Free Edition, eligibility-scoped) | — | ✓ (free tiers; CVITP volunteer program) |
| Desktop realization | ✓ (TurboTax Desktop line) | ✓ (Download software) | ✓ (practice editions) | ✓ (UFile WINDOWS) |

## Canonical Model

### L0 — Defining Invariant (minimal)

The Tax Preparation Application is the **taxpayer-side return-formation system of record**: it forms a complete tax return for one taxpayer filing unit, from that unit's own tax situation, under the jurisdiction's tax rules, and produces the finished return ready for signature and submission. Three jointly-held structures:

1. **The return of record** — a persistent, identified return per taxpayer filing unit × tax authority jurisdiction × tax year/period, accumulating the situation across working sessions and carried across years (prior-year access, carryforwards), retained after completion. Remove → a tax calculator/estimator, or advice content.
2. **Situation-driven assembly of the complete return** — the taxpayer's tax-relevant facts gathered through structured intake (guided Q&A, form-based entry, document/photo upload, data import from employers/financial institutions/authority accounts, prior-year carryforward) are mapped through eligibility logic into the jurisdiction's form/schedule structure: the application determines which forms and schedules the situation requires and assembles the whole return. Remove → a generic form-filler or an interview wizard with no tax object.
3. **Computation and closure under maintained jurisdictional tax content** — tax is computed under rates, rules, and form logic that the vendor maintains and updates as law changes (the taxpayer authors facts, never the rules); the assembled return is checked (error/completeness diagnostics, commonly optimization of deductions/credits) and closed as a complete, authority-acceptable artifact — produced for signature, electronic transmission, or printing/mail — and retained. Remove → a spreadsheet or a bare estimate tool.

Framer: the taxpayer side (the person/filing unit whose return it is, or a professional preparer acting for many such units) — never the tax authority's own administration.

Jointly-held load-bearing:

- 1 alone = a document folder / an e-file status tracker
- 2 without 1+3 = a Q&A wizard over nothing
- 3 without 1+2 = a tax calculator (estimate in, estimate out)
- 1+2 without 3 = a document organizer
- 1+3 without 2 = an estimator with a storage box
- 2+3 without 1 = a one-shot worksheet

### L1 — Common Mature Structure

- **Integrated e-filing as the closure step** — the formed return is transmitted through the authorized channel with status tracking (transmitted/accepted/rejected) and rejection-correction; every sampled product integrates this, and the billing gate sits at the e-file/print moment. Integration ≠ definition (see Boundary Findings).
- **Print-and-mail posture** — the completed return can be printed and mailed; vendor phrasing treats this as the standing alternative to e-transmission.
- **Prior-year continuity** — prior-year return access, prior-year filing, carryforward amounts; multi-year retention windows (one vendor defines the return's "lifetime" as seven years).
- **Authority-data import** — pulling tax slips/documents from the authority's systems (CRA Auto-fill) or from employers/financial institutions.
- **Optimization/review layer** — deduction/credit maximizers, "every tax-saving opportunity" scanning, named final-check passes; guarantees (accuracy, maximum refund) marketed on top.
- **Refund/balance-due money surfaces** — refund presentation and timing, direct-deposit setup; refund-based fee payment common at the consumer pole.
- **Multi-authority orchestration** — federal + state (US); CRA + Revenu Québec (Canada); per-authority returns from one preparation session.
- **Free-tier eligibility scoping** — free editions scoped by situation complexity with explicit included/excluded situation lists.
- **Signature/authorization step** — self-declaration for self-preparers; e-file authorization forms and preparer signatures in the professional mode.

### L2 — Variant / Optional Structure

- **Intake philosophy** — guided interview first (consumer pole) vs form-driven entry (professional pole) vs import-first. The decisive variant axis, not a boundary.
- **Filer class** — individual income-tax returns; business/entity returns (partnerships, S-/C-corps, trusts/estates, tax-exempt, corporate T2); scope limits per product are explicit.
- **Operator mode** — self-preparation; expert-assisted (advice + review riding the same return); full-service (expert prepares and signs); professional practice mode (firm prepares many client returns).
- **Regime realization** — US authorized-provider e-file with federal/state split; Canada NETFILE certification with CRA/Revenu Québec dual returns; other regimes substitute their own certification/channel machinery.
- **Deployment surface** — online, desktop (download/boxed), mobile app with photo capture; the desktop line survives in every sampled family.
- **Business-model riders** — free tiers, pay-when-you-file gates, refund-based fee payment, bank products (refund advance, refund transfer), audit support/defense tiers, AI assistants.
- **Institutional variants** — volunteer/community programs (CVITP) providing the same preparation core free to eligible populations.

### L3 — Vendor-specific (Research Notes only)

- TurboTax: "Complete Check™" final-check name; seven-year "lifetime of your return" framing; Easy Online Amend windows per product/year (e.g., DIY amend online through October 31, 2028 for TY2025); Refund Advance loan ladder ($250–$4,000 in $250 steps, max 50% of anticipated refund; Full Service tier up to $10,000); File Now Pay Later terms; Credit Karma Money account coupling; Expert hours windows; "~37% of filers qualify" free-tier scoping; 1099-K/1099-NEC snap-autofill per edition; business-product exclusion lists (C-Corp 1120, 1041, tax-exempt, >5 state filings).
- TaxAct: "Deduction Maximizer" and "Xpert Assist"/"Xpert Full Service" brand names; $100k Accuracy Guarantee; E-File Concierge phone service; "over 113 million returns filed since 2000" claim; family brands (Drake, 1040.com, Taxwell); SmartFile AI naming; price-comparison marketing vs TurboTax.
- TaxAct Professional: unlimited/low-volume(20–40)/pay-per-return pricing ladder; EFIN/PTIN application resources; Form 8879 e-signature scope (excluding 990/1041); bank-product partner names (Republic Bank, TPG) and ERO enrollment semantics; "Client Portals by Drake Software"; free evaluation edition explicitly excluding IRS filing.
- UFile: NETFILE certification framing; CRA Auto-fill; "Triple Guarantee" composition; UFile WINDOWS desktop and UFileT2 corporate lines; CVITP volunteer edition; retail store locator; Protégez-Vous recommendation badge.

## Vendor-specific Findings

See L3. The most tempting over-generalizations and their rejection:

- **"A tax preparation application is an interview"** — rejected. The interview is the consumer pole's intake style; professional products are form-driven with import; UFile documents Auto-fill import as a peer path. The canonical concept is structured situation intake, realized by interview, forms, import, or photo.
- **"Preparation includes e-filing"** — rejected as definitional. Every sampled product integrates e-filing, but the preparation core is complete without it: print-and-mail is a standing posture ("instead of printing and mailing it in"); a professional evaluation edition explicitly supports preparation without any filing capability; the sibling Tax Filing Platform pass already assigned submission mechanics to the filing side. E-filing is L1 common integrated closure.
- **"Preparation means maximizing your refund"** — rejected as definitional. Optimization layers are universal in the sample but are a review/assurance layer (and a marketing frame), not the structure; guarantees attach to outcomes, not to the object model.
- **"Tax preparation is a consumer category"** — rejected. The professional practice mode (firm-scale, per-return pricing, client collaboration, EFIN/bank-product machinery) and entity/business returns are structurally the same preparation core at different scales; the CVITP volunteer variant extends it further.
- **"The application computes from your books"** — rejected. Book-derived computation is Corporate Tax Management's leg; here the taxpayer's situation facts (documents, answers, slips) are the source, with bookkeeping imports as one intake channel for business situations.

## Boundary Findings

### vs Tax Filing Platform (sibling leaf; research 2026-09-10) — JOINT REVIEW DISCHARGED

The market straddles: the same products (TurboTax, TaxAct) are marketed as both "tax preparation" and "tax filing" software, and both passes sampled them. The structural seam is the **center of gravity of the system of record**:

- Tax Preparation Application (this Type): the **formed return** — situation intake, assembly, computation, review, closure as a finished, signable return. Filing is commonly integrated and is the closure step of preparation.
- Tax Filing Platform (sibling): the **submission and the authority's response** — authority-bound assembly, authorized-channel transmission, acknowledgment, correction/amendment loop. Preparation may be in-product, minimal (import-native information-return filing), or absent.

Pure-pole products exist on both sides: preparation-centric realizations whose filing act is one closure button (and which can print-and-mail instead), and filing-only platforms fed by data prepared elsewhere. The bundled consumer middle is the straddle zone. **RATIFIED from this side: keep-both**, consistent with the corporate-tax-management pass's "single-taxpayer document-sourced preparation" vs "submission mechanics" discriminator and with the tax-filing pass's own mirror-image framing. Removal tests both ways: remove submission machinery (keep formed return + print/mail) → still unmistakably this Type; remove situation intake and computation (keep submission + status) → the filing platform, not this Type.

### vs Tax Compliance Platform (processed 2026-09-10)

Transaction-level tax determination against maintained jurisdictional content is that Type's defining leg; here tax figures are computed at return level from the taxpayer's situation, with no transaction stream and no per-transaction record of record. The compliance platform accumulates taxable transactions into obligations; this Type forms one return per filing unit per period from that unit's facts. The compliance pass's own seam note ("consumer/individual income-tax preparation… different users, objects, and workflow") is CONFIRMED; keep-both.

### vs Corporate Tax Management (processed 2026-09-07)

Corporate tax management's object of record is the entity–jurisdiction–period tax position computed **from the books** (provision pipeline, close, evidence). Here the object of record is the **formed return** sourced from the taxpayer's situation documents/answers, and the taxpayer is a person/filing unit (or a firm's client), not a corporate group provision. The corporate pass's "single-taxpayer document-sourced preparation" discriminator is CONFIRMED from this side; keep-both. (Feeder relationship: business books may feed business-return preparation as an import, without any provision machinery.)

### vs Tax Administration System (§24, processed 2026-09-09)

The authority's system of record (taxpayer registration, obligation accounts, assess→post→settle) vs the taxpayer-side formation of the declaration that enters it. One return is an input to the other system's loop. The government-operated free-filing portal is a boundary pole of the filing family, not of preparation: authority portals accept submissions but do not carry the taxpayer's multi-year preparation estate.

### vs Payroll System (§09, processed)

Payroll runs the wage money loop and, in full-service form, remits payroll taxes and produces wage/income documents (W-2/1099-class). Those documents are among the situation facts this Type consumes. Payroll withholding computations are per-paycheck employer-side; return preparation is per-period taxpayer-side. Feeder/embedded relationship; keep separate.

### vs Accounting Software (§08, processed) and Bookkeeping

Accounting software holds the books of record for a business; business-return preparation consumes summaries of those books as one intake channel (imports documented at the professional pole and consumer self-employed pole). No ledgers of record exist in this Type. Keep separate.

### vs Tax Calculators / Personal Finance Applications

A calculator produces an estimate from entered numbers and holds nothing of record; a preparation application assembles the complete authority-acceptable return, decides which forms the situation requires, and retains it. Sampled products expose calculators as free companion tools (TaxCaster-class) — the estimate is the marketing surface, the return is the product. Keep separate.

### Historical / market-sample check (§24)

Would older, regional, platform-native, or differently positioned products still fit? Yes:

- **Desktop era**: every sampled family ships a desktop line (TurboTax Desktop, TaxAct download, UFile WINDOWS, TaxAct Professional practice editions); the current desktop realizations demonstrate the core without web/mobile/AI machinery. Earlier desktop generations that only printed the return for mailing satisfy the L0 core unchanged — preparation ≠ transmission.
- **Paper era**: the professional preparer's client organizer + worksheets + hand computation on jurisdiction forms is the ancestor artifact; the software Type digitizes the organizer (structured intake), the worksheet math (computation), and the form assembly. The L0 phrasing (situation-driven assembly + computation + closure as an authority-acceptable artifact) covers the desk of a preparer without any era machinery.
- **Regional regimes**: the Canadian pole (NETFILE + CRA Auto-fill + Quebec dual returns) satisfies the core with entirely different certification and channel machinery; the definition names no regime, form catalog, or authority.
- **Volunteer/free poles** (CVITP) and **firm-scale poles** (pay-per-return) satisfy the same three structures.

The definition therefore does not over-fit the current consumer web-interview era.

## Uncertainties

1. **H&R Block** (the hybrid in-person-preparer + software pole) could not be fetched (403, also in the tax-filing pass). Its posture is evidenced indirectly through the Expert Full Service tiers of the sampled products; no H&R Block-specific operational claims are made.
2. **Drake Software** — the professional-pole market leader — could not be fetched (403); TaxAct Professional carries the professional pole's evidence alone. Drake-specific practice features (client portals rebranded for TaxAct) are visible through the TaxAct disclosures but not verified on Drake's own surfaces.
3. **FreeTaxUSA / TaxSlayer** (budget poles) unreachable in both sibling and current passes; the budget pole's structure is assumed to match the consumer DIY pole but no independent evidence was gathered.
4. **Exact review/diagnostic behavior per product** (what the error checks cover, what "Complete Check"-class passes validate) was not researched per-product; the review closure is held at conceptual level.
5. **Non-sampled regimes** (UK, Australia, Germany, etc.): assertion strength held at "regimes substitute their own machinery," consistent with the tax-filing pass.
6. Whether the market will keep "tax preparation" and "tax filing" as separate commercial categories or converge further on one bundled label is a market question; the structural seam is recorded and jointly ratified for the taxonomy.

## Final Synthesis

The Tax Preparation Application is the taxpayer-side return-formation system of record. Its defining core is exactly three jointly-held structures: the return of record (one persistent return per taxpayer filing unit × jurisdiction × year, carried across sessions and years), situation-driven assembly of the complete return (structured intake — interview, forms, documents, imports — mapped through eligibility logic into the jurisdiction's form structure, the application deciding what the situation requires), and computation and closure under maintained jurisdictional tax content (vendor-maintained rules, checked and closed as a complete authority-acceptable artifact ready for signature, transmission, or print-and-mail, and retained). Everything else — integrated e-filing, refund money rails and bank products, optimization layers and guarantees, expert service tiers, free-tier scoping, multi-authority orchestration, desktop/mobile surfaces, professional practice workflows, volunteer programs — is common, variant, or boundary, not definition. The Type is era- and regime-agnostic by construction: a desktop product that only prints satisfies it as fully as an AI-assisted web interview. All three inherited tax-family joint-review flags are discharged from this side: the formed return (this Type) vs submission machinery (Tax Filing Platform) seam is RATIFIED keep-both; return-level situation computation (this Type) vs transaction-level determination (Tax Compliance Platform) and books-derived provision (Corporate Tax Management) seams are CONFIRMED.
