# Research Notes — Public Benefits Management

## Research Goal

Understand the software that government agencies use to administer public assistance / social-protection benefit programs: what the system of record holds, how eligibility is determined, how benefits are calculated and issued, and how the ongoing lifecycle (recertification, change reporting, overpayment, appeals, reporting) is managed — and where this Type ends relative to social-services case management, housing assistance administration, payer claims processing, and employer benefits administration.

## Initial Boundary

- **What it likely is**: the government agency's benefit-program administration system — application intake, eligibility determination against program rules, benefit/entitlement calculation, issuance (payment/EBT/voucher), recertification, notices, appeals, program-integrity and federal reporting. Market vocabulary: "integrated eligibility system (IES)", "eligibility and enrollment", "public assistance system", "benefits administration" (government sense), "social program management", "MMIS eligibility side".
- **Nearest neighbors**: Social Services Case Management (case-centric), Housing Assistance Management (tenancy-bound subsidy), Health Plan Administration System / Payer Claims Processing (Medicaid MMIS claims machinery), Benefits Administration Platform (employer-side), Government Grants Management (grants to organizations), Public Employment Service Platform (employment services), Tax Administration (revenue, opposite money direction).
- **Unknowns**: whether unemployment-insurance (claims-shaped) systems belong here; whether MMIS claims machinery belongs here; how international (UK/Canada) social-security systems map.

## Research Questions

1. What is the unit of record — person, household, application, case, benefit period?
2. How does eligibility determination work (rules engine, verification, evidence)?
3. How is the benefit amount computed and issued (payment cadence, EBT, vouchers)?
4. What is the ongoing lifecycle (recertification/redetermination, change reporting, over/under-payment)?
5. What roles exist (intake worker, eligibility worker, supervisor, financial specialist, QC)?
6. What interfaces exist (worker portal, applicant/citizen portal, batch, interfaces to federal systems)?
7. Where is the seam vs social-services case management (case-centric) and vs payer claims processing (MMIS)?
8. Do older/regional systems (paper-era welfare office, UK/Canada programs) fit the same core?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer levels:

1. **Merative Cúram** (formerly IBM Curam Social Program Management) — the flagship commercial integrated-eligibility/social-program-management platform; used by US states, Social Security Scotland, Employment and Social Development Canada. Commercial platform philosophy.
2. **Canopy (Georgia DHS)** — open-source integrated eligibility system built and operated by a state agency (AGPLv3); exceptionally complete official documentation (architecture, ADRs, user guides, data models). Government-built philosophy; also documents the conventional vendor model it rejects (Georgia Gateway).
3. **Sagitec Neosurance** — commercial unemployment insurance / paid family & medical leave / disability insurance benefits administration for state workforce agencies. Claims-shaped benefit-program pole.
4. **State legacy systems** (Washington ACES, Minnesota MAXIS, Alaska EIS/ARIES) — government-operated mainframe/legacy eligibility systems documented in official RFPs and agency pages; the installed-base reality and the historical anchor.
5. **MMIS fiscal-agent systems** (Gainwell, Conduent) — researched for boundary evidence only (Medicaid claims machinery), not as representative products of this Type.

## Sources

- Merative — Cúram Integrated Eligibility and Enrollment product page (https://www.merative.com/curam/integrated-eligibility-enrollment) — fetched 2026-09-10. Tier 1/2.
- Canopy Documentation — Why Canopy? (https://canopy-c1fab5.gitlab.io/canopy/why-canopy.html) — fetched 2026-09-10. Tier 1 (official state documentation, extensive doc tree incl. user guides, ADRs, data models).
- Sagitec — Neosurance product page, overview brochure, Maryland case study (sagitec.com) — 2026-09-10. Tier 1/2.
- Washington State DSHS RFPs #2223-808 (ACES M&O) and #2223-814 (IE&E Platform) — official procurement documents describing ACES functions in detail. Tier 1 (government).
- Minnesota DHS — MAXIS description page (dhs.state.mn.us). Tier 1 (government).
- Alabama DHR — SNAP/TANF Information System RFP. Tier 1 (government).
- McKinsey — "Insights into better integrated eligibility systems" (2019) — market-structure context. Tier 3.
- Gainwell/Conduent MMIS materials + Indiana/Oklahoma/Mississippi Medicaid agency pages — boundary evidence. Tier 1/2/3.

## Product A — Merative Cúram

### Key observations (Evidence layer A — official product page)

- Positioning: "unified technology and business platform designed specifically for government health and human services programs – such as Medicaid, SNAP and TANF"; "health and human services platform for modern benefits delivery".
- Programs named: Medicaid (MAGI and Non-MAGI), SNAP, TANF, CHIP, LIHEAP, Child Welfare; configurable tools for state/local programs and rapid new-program creation (disaster/emergency programs explicitly supported).
- Core competency list ("Eligibility and entitlement"): eligibility and entitlement determination; automated payment scheduling; automatic overpayment case creation for tracking and recoupment; deduction configuration for recouping overpayments; capture & reuse evidence; household composition determination and display; multi-program payment consolidation; nominee payments; overpayment and underpayment calculation; prepayment entitlement verification; program-specific verification rules; rate change; retroactive change processing; handles multiple evidence changes, rule and rate changes.
- "Domain-specific eligibility and entitlement engine that can evaluate determinations across the lifespan of client interactions"; "temporal eligibility and entitlement rules engine" — determinations are time-aware (effective dating).
- Benefit management "coordinates service deliveries, including financial issuances and provider service authorizations".
- Financial management: "automated over- and under-payment determinations when reassessments are required".
- Roles: intake workers, eligibility workers, supervisors, financial specialists, quality control/oversight specialists.
- Client self-service: screening, application, account management portals ("citizen engagement").
- Data accuracy: automatic validation of received data, issues raised for worker/supervisor intervention, manual-verification identification; source control, audit trails, quality control; fraud-reduction features (suspicious entries escalated for supervisor review before authorization/payment).
- Integration: verification sources, federal/state/local systems, financial and accounting systems.
- Deployments cited: New York City (SNAP applications online), Social Security Scotland (new benefits agency, GBP 190m disbursed), Nevada county (homelessness prevention), Canada ESDC (Old Age Security modernization).

## Product B — Canopy (Georgia DHS)

### Key observations (Evidence layer A — official state documentation)

- Definition: "open-source integrated eligibility system built by Georgia DHS"; administers SNAP, TANF, Medicaid and CHIP, CAPS (child care), WIC. DHS caseworkers make eligibility determinations across programs legally belonging to four different state agencies.
- Scope statement: "Canopy handles eligibility and enrollment — application intake, determination, enrollment, renewal, notices, federal reporting."
- Companion system CRAIG handles child welfare case management — explicitly a distinct domain ("child welfare case data and eligibility data are distinct domains with distinct federal requirements"). Strong boundary evidence vs Social Services Case Management.
- Documented machinery (from doc tree and plans): person and household data model; rules engine (declarative versioned rulesets); application intake; SNAP eligibility incl. deductions, categorical eligibility, ABAWD work requirements; TANF eligibility incl. sanctions; Medicaid/CHIP eligibility (multiple coverage pathways); WIC nutritional risk; CAPS; verification (IEVS, SAVE); notice generation; fair hearings and appeals; IPV disqualification; enrollment and EBT issuance; renewals/recertification (interview, NOMI, denial, prorated reinstatement); overpayment recovery pipeline; federal reporting (SNAP, TANF, Medicaid, CMS-64/CMS-416/ACF-196 expenditure aggregation); worker portal + applicant portal; supervisor and analyst dashboards; RBAC matrix; audit.
- Determination as a first-class object: "a signed, tamper-evident object that records the outcome"; determination supersession; determination input snapshots; per-subject determinations.
- Program isolation driven by federal data-use law (IRS Pub 1075, SSA computer-matching agreements, USDA IEVS restrictions, HIPAA) — each program an independent service; the orchestrator "assembles determinations across programs, applies the federal eligibility hierarchy".
- The conventional model it documents and rejects: "one platform, one vendor, shared data" (Georgia Gateway, built 2017 by a single vendor) — the market's dominant integrated-eligibility packaging.
- Federal cost-sharing framework (90%/75%/50% FFP) — the regulatory-economic context of the market.

## Product C — Sagitec Neosurance

### Key observations (Evidence layer A — official product pages/brochure)

- Positioning: "fully integrated, browser-based application providing comprehensive functionality for Unemployment Insurance (UI) Tax, Benefits and Appeals administration"; also Disability Insurance and Paid Family & Medical Leave.
- Benefits-side machinery: initial and continued claims processing; benefit amount/effective-date/balance calculation across claim types; eligibility and wage determinations via workflows and wizards; payment requests with deductions; certifications; reopening past weeks; adjudication workflow (issue routing to adjudicators, wizards, pre-filled determination letters); overpayments (predictive fraud model, cross-match, collections); appeals; claimant self-service portal (update data, view payment history, respond to agency requests); program-integrity sampling (BAM/BTQ); federal reporting; SIDES integration.
- Vocabulary is claims-shaped ("claims", "adjudication") but the object world is a benefit program: a claimant's standing claim with weekly certification, computed benefit amount, recurring payment, and eligibility re-evaluation — structurally the same determination→entitlement→issuance→recertification spine as the IES pole.

## Product D — State legacy systems (Washington ACES, Minnesota MAXIS, Alaska EIS/ARIES)

### Key observations (Evidence layer A — official government documents)

- Washington ACES (RFP): "the eligibility determination and case maintenance system for TANF, SNAP, MAGI medical and long-term medical, Basic Food, Medicaid Programs… and others". Functions: client intake and screening (face-to-face and telephone); application processing incl. online; scheduling for eligibility determination and review; multi-program eligibility determination; "automated benefit calculation and benefit issuance via Electronic Benefits Transfer (EFT)"; client notifications; 80+ state and federal interfaces; reports/inquiries for operations, research, forecasting, budget. ~3 million active recipients; $160–170m monthly benefits distributed. Mainframe COBOL heritage with MAGI rules migrated to a business-rules engine (ODM) — the modernization pattern.
- Minnesota MAXIS (agency page): "used by state and county workers to determine eligibility for public assistance and health care. For cash assistance and food support programs, MAXIS also determines the appropriate benefit level and issues benefits." Single point of access, data entered once for cash/food/health care; uniform benefits statewide; IEVS income-verification automation for unreported-income detection.
- Alaska (RFP): legacy EIS mainframe "supporting eligibility determination and benefit administration for multiple public assistance programs" + modern ARIES for MAGI Medicaid; incremental modular modernization roadmap.
- Alabama STIS RFP: procurement language names the whole Type in one sentence — "an integrated information system that supports the application processing, eligibility determination, case management, and benefit issuance requirements" for SNAP and TANF, meeting federal (FNS/HHS) requirements. Also documents the "transfer system" market practice (one state's system transferred and configured for another).

## Product E — MMIS fiscal-agent systems (boundary evidence only)

- Gainwell (Indiana): Core MMIS contains member eligibility, provider enrollment, claim activity; fiscal agent processes FFS claims, ensures "accurate and timely payment to providers", processes provider claim disputes/appeals, collects member premiums.
- Oklahoma EDEA: "The MMIS system contains online information regarding claims adjudication, eligibility verification, prior authorizations…"
- Conduent Health Enterprise MMIS: claims adjudication, provider payment, encounter data, MCO monitoring.
- Reading: the MMIS's center of gravity is provider-facing claims adjudication and payment — the government-operated variant of payer claims machinery. Member eligibility lives in the MMIS as data consumed by providers, but the determination of that eligibility is the IES's job (increasingly modularized under MES/MITA). The two systems interlock (eligibility data flows IES→MMIS) but their centers differ.

## Cross-product Comparison

| Dimension | Cúram | Canopy | Sagitec Neosurance | State legacy (ACES/MAXIS) |
|---|---|---|---|---|
| Unit of record | person + household + case + determination (temporal) | person + household + application + signed determination | claimant + claim (initial/continued) + weekly certification | client/household + case + benefit period |
| Program frame | multi-program platform (Medicaid/SNAP/TANF/CHIP/LIHEAP/child welfare + custom) | multi-program (SNAP/TANF/Medicaid/CHIP/CAPS/WIC), program-isolated services | single-program family (UI/DI/PFML) | multi-program (cash/food/medical) |
| Eligibility determination | domain-specific temporal rules engine; evidence capture & reuse; verification rules | declarative versioned rulesets per program; verification (IEVS/SAVE); signed determinations | eligibility + wage determination workflows; fact-finding questionnaires | rules in COBOL/ODM; multi-program determination; IEVS |
| Benefit computation | entitlement engine; rate tables; retroactive change processing; multi-program payment consolidation; nominee payments | per-program issuance incl. deductions, proration | benefit amount/effective dates/balances; payment requests with deductions | "determines the appropriate benefit level and issues benefits" |
| Issuance | automated payment scheduling; financial issuances; provider service authorizations | enrollment + EBT issuance | benefit payments (EFT/debit card) | EBT/EFT issuance |
| Ongoing lifecycle | over/under-payment calculation; recoupment deductions; renewals | renewals/recertification; change reports → re-determination; overpayment recovery | continued claims/weekly certification; reopen past weeks; overpayments | scheduled redetermination/review; change processing |
| Accountability | audit trails, QC roles, fraud escalation | federal reporting pipelines; audit hash chains; fair hearings | BAM/BTQ sampling; federal performance measures | federal interfaces; accuracy bonuses; forecasting/budget reports |
| Portals | citizen self-service (screening/application/account) | applicant portal + worker portal | claimant/employer/TPA self-service | client-facing web portal (WA Connection) |
| Roles | intake/eligibility workers, supervisors, financial specialists, QC | caseworker, eligibility specialist, supervisor, state evaluator | adjudicators, staff, administrators | state and county workers |

## Canonical Model (L0/L1/L2/L3)

### L0 — Defining Invariant (deliberately small)

The government agency's benefit-program system of record, holding exactly three jointly-held structures:

1. **The applicant/household of record under a government benefit program** — persistent identified records for the people (with household/family composition) applying for or receiving a public assistance program whose rules are set outside the agency (statute/regulation); the household is the characteristic unit because eligibility and benefit levels are computed on it.
2. **The recorded eligibility-and-entitlement determination** — application intake → declared facts verified against evidence and authorized external sources → rules-based determination of eligibility AND the benefit amount/entitlement, recorded as a dated, attributable, effective-aware decision that gates everything downstream. Remove → eligibility calculator or intake form.
3. **The benefit issuance and ongoing lifecycle** — the determined entitlement converted into recurring benefit delivery (payment/EBT/voucher/service authorization) and maintained across time: recertification/redetermination on schedule and on reported change, over/under-payment handling, notices, appeals, and reporting under public accountability. Remove → one-shot determination with no program operation.

Jointly-held load-bearing: (1 alone = people registry; 2 without 1+3 = eligibility calculator; 3 without 1+2 = disbursement machinery; 1+2 without 3 = one-shot screening; 1+3 without 2 = payment rolls with no rules; 2+3 without 1 = anonymous transaction processing).

Binding: the operator is a government agency administering programs whose rules and funding come from statute (federal/state), with the served population the general public qualified by need — remove the government-program binding → generic case management or payroll-like disbursement.

### L1 — Common Mature Structure

- multi-program integration (one determination feeding several programs; cross-program data reuse)
- verification interfaces to external/federal data sources (income, identity, wage, asset)
- notices/letters generation; document management/imaging
- applicant/citizen self-service portal (screening, apply, status, upload)
- worker workflow with task management, scheduling, supervisory review
- appeals/fair-hearings machinery
- program-integrity: fraud flags, QC sampling, overpayment recoupment
- federal/state reporting and interfaces (dozens of them in the legacy pole)
- role-based security, audit trails
- business-rules engines with configuration (not code) for policy change

### L2 — Variant / Optional

- program family: health & human services (Medicaid/SNAP/TANF/CHIP/LIHEAP/child care/WIC) vs labor/employment (UI/DI/PFML) vs social security (OAS-class, Scotland new-agency) vs disaster/emergency programs
- claims-shaped vocabulary (UI: initial/continued claims, weekly certification) vs application-shaped vocabulary (SNAP/TANF: application/recertification) — same spine
- integration architecture: monolithic shared-data platform vs program-isolated services with signed determinations (Canopy) vs modular MES
- delivery channel of the benefit: EBT, EFT/direct deposit, check/warrant, voucher, provider service authorization, tax-credit-like instruments
- operator model: state-administered vs state-supplied/county-administered (MAXIS partnership), fiscal-agent-operated
- commercial platform vs government-built open source vs transferred state system vs bespoke integrator build
- employer/TPA-facing sides (UI tax side), provider-facing sides (Medicaid)

### L3 — Vendor-specific (Research Notes only)

- Cúram Action View (single-page caseworker console), temporal eligibility engine branding, nominee payments, deduction configuration for recoupment
- Canopy's Rust/Axum/Keycloak stack, JDM rulesets, AGPLv3 strategy, FTI audit hash chains
- Sagitec Xelence platform, Neofraud, SIDES integration, BEACON One-Stop (Maryland)
- ACES green screens, WACONN portal, ACOM/ACM subsystems; MAXIS county partnership

## Vendor-specific Findings

- Cúram's "temporal eligibility and entitlement rules engine" and Action View are vendor features, not Type structure.
- Canopy's program-service isolation via signed determinations is one (legally motivated) architecture; the dominant market model is the shared-data monolith it criticizes — architecture is variant, not invariant.
- Sagitec's "meets at least 70% of any state's requirements out of the box" is vendor marketing.
- Maryland BEACON fraud-freeze anecdote is product history, not Type structure.

## Boundary Findings

1. **vs Social Services Case Management (§24, processed)** — CONFIRMED keep-both on the case-centric vs benefit-centric seam exactly as that pass predicted. Evidence: Canopy's own documentation separates eligibility/enrollment (Canopy) from child-welfare case management (CRAIG) as "distinct domains with distinct federal requirements"; Cúram sells child welfare as a separate solution line from integrated eligibility. In this Type the determination→entitlement→issuance→recertification machinery at program scale is the center; supportive casework episodes are secondary or absent. Where a social-services agency runs economic assistance inside generic casework machinery (Northwoods Traverse economic-assistance program area), the same-product straddle is a context line, not a feature line.
2. **vs Housing Assistance Management (§24, processed)** — test answered: the sampled benefit systems do NOT bind assistance to a tenancy/rent liability and carry no landlord-facing payment administration; housing-type programs (when present, e.g., emergency/rental assistance variants) enter as just another benefit program with a household applicant. The tenancy binding + landlord payment administration remains that Type's differentiator. Keep-both CONFIRMED.
3. **vs Health Plan Administration System / Payer Claims Processing (§22, processed)** — the MMIS boundary note is answered with a split: Medicaid MMIS claims machinery (provider claims adjudication, fiscal-agent payment to providers, encounter data) is the government-operated variant of payer claims machinery and stays with payer-claims-processing territory; the eligibility-and-issuance side of Medicaid as a public benefit program (determining which residents are covered and issuing/ maintaining that coverage) belongs here. The seam is the counterparty: providers being paid for services (claims) vs households receiving assistance (benefits). The boundary is porous and increasingly modularized (member eligibility data flows IES→MMIS; MMIS consumes determinations). Keep-both with the counterparty test.
4. **vs Benefits Administration Platform (§09, processed)** — employer-side plan administration (enrollment elections, carrier files, payroll deductions) vs government-side public assistance (statutory programs, need-based eligibility, public funding). Different operator, funding, eligibility logic, accountability. Distinct Types; shared word "benefits" only.
5. **vs Government Grants Management** — grants flow to organizations under agreements; benefits flow to individuals/households under statutory entitlement rules. Distinct.
6. **vs Public Employment Service Platform** — job-matching/employment services vs benefit payment administration; UI benefits administration (this Type) coexists with reemployment services (that Type) in the same agency.
7. **vs Government Service Portal / Citizen Engagement** — the applicant portal is one surface of this Type, not the Type; the system of record is the agency-side machinery.
8. **Taxonomy note (from institutional-foodservice-management pass)** — K-12 school-nutrition program administration (eligibility determination + meal claims/reimbursement) is a program-family variant of this Type's machinery; recorded as a possible future consolidation, no directory change made.

## Historical / Market-Sample Check

- Paper-era welfare office: application form + case file + worker computing the grant against a rules table/manual + warrant/check issuance + scheduled redetermination visits + notice letters + state/federal reporting — satisfies all three L0 structures with zero software. Passed.
- Mainframe-era systems (ACES 1996, COBOL/IMS) satisfy the core. Passed.
- UK/Canada social-security analogs (Social Security Scotland on Cúram; Canada ESDC OAS on Cúram) — non-US regimes fit; program names are variant. Passed.
- Claims-shaped UI systems fit the same spine (determination→payment→recertification) with different vocabulary. Passed.
- Anti-overfit: EBT, federal interfaces, portals, business-rules engines, fraud analytics, CMS certification, multi-program integration, cloud — all common/variant, NOT definitional.

## Uncertainties

- No Tier-1 help-center articles for Cúram or Neosurance were reachable (product pages and brochures only); precise operational details (determination timeframes, notice deadlines, payment cadences) are deliberately not asserted.
- International non-English markets (continental Europe, Asia) not sampled; the UK/Canada evidence comes via vendor case-study mentions, not agency documentation.
- The exact market share / product count of the IES vendor market is not asserted (McKinsey 2019 figures are directional context only).
- Whether a future directory pass should treat "unemployment insurance system" as its own leaf or a variant of this Type is left to the taxonomy owner; this pass holds it as a program-family variant on the claims-shaped pole.

## Final Synthesis

Public Benefits Management is the government agency's benefit-program system of record. Its defining core is three jointly-held structures: the applicant/household of record under a government benefit program whose rules come from statute; the recorded eligibility-and-entitlement determination (verified facts → rules-based decision on eligibility AND benefit amount, effective-aware, attributable); and the benefit issuance and ongoing lifecycle (recurring delivery, recertification/redetermination, change reporting, over/under-payment, notices, appeals, public-accountability reporting). Everything else — multi-program integration, verification interfaces, portals, rules engines, EBT, fraud analytics, federal reporting — is common mature structure or variant, not definition.
