# Research Notes — Affordable Housing Management

Research date: 2026-09-06
Leaf: Affordable Housing Management (DIRECTORY.md §17 Construction, Real Estate & Facilities)
Slug: affordable-housing-management

---

## Research Goal

Understand what an Affordable Housing Management application actually is as an Application Type: what objects it manages, how the assisted-tenancy lifecycle flows, what distinguishes it from general residential property management, and how the definition holds across regulatory regimes (US HUD/tax-credit programs vs UK social housing) and operator types (private owners, nonprofits, public housing authorities, state agencies).

## Initial Boundary

Working hypothesis before research:

- The Type is operator-side software for rental housing whose tenancy is governed by housing-program rules (subsidized or income-restricted housing).
- The expected differentiator vs Residential Property Management is a compliance layer: applicant eligibility (income limits), certification/recertification of household eligibility, program-constrained rent, and reporting to program authorities.
- Neighboring Types to watch: Residential Property Management, Housing Assistance Management (§24, likely the government/agency-administrator view), Tenant/Resident Portal, Student Housing Management, HOA/Community Association Management, Rent Collection Platform, Property Maintenance Management.
- Risk: the market phrase "affordable housing" is used loosely (including unregulated cheap housing and listing portals); the Type must be anchored on program-governed operation, not on price level.

## Research Questions

1. What are the core objects (program, property, unit, applicant, household, certification, rent, subsidy, inspection, report)?
2. How does the applicant pipeline work (application → waiting list → preference ordering → eligibility determination → offer → move-in)?
3. How does the certification/recertification lifecycle work (income/asset calculation, verification, annual/interim cycles)?
4. How is program rent determined, and how do subsidy payments flow (tenant share vs subsidy billing)?
5. What compliance reporting and file-audit machinery exists (HUD 50059/TRACS/MINC, 50058/PIC, state HFA reports, agency reviews)?
6. How are mixed portfolios modeled (units layered with multiple programs, set-asides, market-rate units alongside affordable units)?
7. What property-operations capabilities are bundled (maintenance, accounting, portals) and are they core or add-on?
8. What differs across regimes and operator types (US operator vs PHA vs UK registered provider)?

## Representative Products

Selected for market representation + documentation accessibility + different philosophies + different customer tiers/regimes:

| Product | Vendor | Segment / philosophy | Evidence level obtained |
|---|---|---|---|
| Yardi Breeze Premier (Affordable Housing) | Yardi | Full-suite property management with affordable compliance as a property-type configuration; SMB/mid-market | Tier 1–2 (feature page + vendor explainer article) |
| MRI Affordable Housing (+ Public Housing line) | MRI Software | Global real-estate technology suite; affordable as compliance module beside PMX | Tier 2 (product pages, A-Z catalog) |
| Emphasys Elite (PHA division) | Emphasys Software | Dedicated public-housing-authority software since 1976; agency-side (HCV/LIPH) | Tier 2 (product + program pages) |
| MRI Social Housing (UK) | MRI Software UK | UK registered-provider / local-authority regime; tenancy-and-asset-centric | Tier 2 (solution + product pages) |
| RealPage (affordable line) | RealPage | Major US operator-side vendor | Positioning only — see Source-access Limitations |

Additional observation: bostonpost.com (a long-standing dedicated US affordable-compliance vendor) now redirects to the MRI Software homepage — evidence of market consolidation into the suite vendors (recorded as an observation; no acquisition details asserted).

## Sources

Fetched 2026-09-06:

- Yardi Breeze — Affordable Housing features page: https://www.yardibreeze.com/affordable-housing-features/ (Tier 2)
- Yardi Breeze blog — "Affordable Housing Compliance Made Easy": https://www.yardibreeze.com/blog/2019/09/affordable-housing-compliance-made-easy/ (vendor explainer; program/process description)
- MRI Software — Affordable Housing Software: https://www.mrisoftware.com/products/affordable-housing-compliance-software/ (Tier 2)
- MRI Software — A-Z Products catalog: https://www.mrisoftware.com/products/ (Tier 2; confirms Public Housing line: PHA Pro, Voucher Management, WaitListCheck, Online Application Management; Automated Income Verification; Fee Accounting)
- Emphasys Software — corporate page: https://emphasys-software.com/ (Tier 2; PHA/HFA division split)
- Emphasys PHA — home: https://emphasyspha.com/ (Tier 2)
- Emphasys PHA — Housing Programs: https://emphasyspha.com/housing-programs/ (Tier 2; program inventory)
- Emphasys PHA — Elite HCV Housing: https://emphasyspha.com/elite-hcv-housing/ (Tier 2; module/workflow detail)
- MRI Software UK — Social Housing: https://www.mrisoftware.com/uk/solutions/social-housing/ (Tier 2)
- MRI Software UK — Housing & Tenancy Management: https://www.mrisoftware.com/uk/solutions/social-housing/housing-and-tenancy-management/ (Tier 2)
- bostonpost.com — redirect to https://www.mrisoftware.com/ (observation only)

Failed / limited sources (per retry discipline):

- realpage.com/affordable-housing/ (404), realpage.com/property-types/affordable-housing/ (404), help.realpage.com (page states Help Center moved behind product login / Unified Platform) — RealPage operational documentation unreachable; RealPage retained as market anchor at positioning level only.
- yardi.com/products/property-management-software/ (403) and resources.yardi.com brochure (403) — Yardi enterprise-level pages unreachable; Yardi evidence rests on Breeze surfaces.
- civica.com/en-gb/products/cx-housing/ (404) — UK alternative vendor not used.
- necsws.com/products/housing-management/ — returned an image only, no text content; not used as evidence.

## Product Observations

### Product A — Yardi Breeze Premier, Affordable Housing configuration (US, operator side)

Evidence layer: A (directly observed on official pages).

Key observations:

- Affordable housing is sold as a property-type configuration of a general property-management product ("Affordable Housing features" alongside Residential/Commercial/Self Storage/Associations/Manufactured Housing) — the compliance layer sits on a shared PM spine.
- Compliance module explicitly covers: "Manage Low-Income Housing Tax Credit, HUD 50059, Rural Development HOME and Local programs"; "Generate and electronically submit TRACS & MINC files"; "Receive and distribute housing assistance and subsidy payments"; "Track member, family, asset, income and expense information"; "Produce and file required tax credit and project-specific rent reports"; "Manage set asides for low income housing"; "Streamline waiting list management"; "Perform mass recertifications".
- The vendor explainer describes the compliance problem in process terms: providers record details about clients from first contact through moveout and must report that data throughout the year; applicant finances (income, assets, family size) must match property requirements; funding sources want detailed reports "pretty often throughout the year"; surprise on-site audits exist; the software "documents the eligibility status of every applicant and resident, including households that don't qualify for assistance"; workflows guide intake; built-in reporting templates export compliance data in multiple formats and interface with online reporting sites (electronic transfer, no hand-keying).
- Rent collection includes "Receive and distribute housing assistance and subsidy payments" and — notably — "Control against unauthorized rent increases (market-rate units only)", confirming mixed market-rate/affordable portfolios inside one product.
- Add-ons extend the compliance loop: RentCafe Affordable Housing ("online applications and certifications... online lease execution" with e-signatures); agency reporting and voucher processing services; "fast file audits for all applicant and resident certifications"; ScreeningWorks Pro (criminal/credit/eviction screening); Verification Services (income/asset verification reports merged into the system); Investment Manager (investor portals, capital commitments/distributions — the LIHTC syndicator/investor side).
- Standard PM capabilities bundled: maintenance/work orders, accounting (GL/AP/AR, escrow/trust accounts, 1099 e-filing), owner statements, CRM queues, websites.

### Product B — MRI Affordable Housing + Public Housing (US, operator + agency side)

Evidence layer: A (directly observed on official pages).

Key observations:

- Positioning: "Uncomplicate compliance reporting, voucher, and waitlist management" — compliance reporting, voucher management, and waitlist management are the three named pillars.
- Compliance reporting: "Automate compliance and centralize reporting for mixed portfolios or multiple subsidy types, including HUD Multi-Family, Tax Credit, HOME, USDA Rural Development, and more."
- Voucher management: "Manage forms and reporting with ease, from issuance to expiration, including eligibility, lease-up, and recertification through simplified rent calculations, inspection tracking, and TRACS submissions." — full voucher lifecycle inside the same family.
- Waitlist management: "ensuring compliance with various program rules and automating prospective renter communications... from one central hub."
- Applicant/resident portals: renters can "apply to a waitlist, complete certifications and recerts, submit requests, and update their information" — self-service certification is a first-class portal function.
- Surrounding capabilities: resident communications (recertification reminders via text/email/phone), screening ("support fair housing"), asset management/investment reporting, fee accounting as an outsourced service, accounting/financial management.
- Separate Public Housing line (PHA Pro, Voucher Management, WaitListCheck, Online Application Management) — the agency-administrator side is packaged as its own product line beside the operator-side affordable module.
- Automated Income Verification exists as a named product — third-party income/asset verification is a distinct integration point.
- Vendor-published scale claims (marketing numbers, not asserted in final doc): 500+ affordable owners/operators, 1m+ families housed, ~70k average monthly online applications.

### Product C — Emphasys Elite (US, public housing authority side)

Evidence layer: A (directly observed on official pages).

Key observations:

- Dedicated PHA software vendor ("since 1976"; PHA division claims PHAs use its products to manage more HUD-subsidized units than any other provider — vendor claim). Positioning explicitly contrasts with private-sector PM tools: "Many of the technology solutions available to PHAs were actually designed for the private sector, with the needs of public housing addressed as an afterthought."
- Program inventory supported: Housing Choice Voucher (Section 8), Low Income Public Housing, Multifamily/50059s, Homeownership, Moving to Work, Family Self-Sufficiency, Rural Development, Mutual Help (Native American homeownership), Shelter Plus Care, RAD (PBV/PBRA), Tax Credits/LIHTC, 50058 special programs (line 2n: ROSS, EHV, VASH).
- Elite HCV modules and workflow vocabulary:
  - Waiting List: "collecting applicant data, making eligibility determinations and drawing names from the lists"; multiple waiting lists across programs; "meets HUD Fairness Standards, determining applicant position by federal and local preferences, bedroom requirements, and application date and time".
  - HCV: "voucher management, RFTA, lease-ups, retroactive adjustments, re-exam processing, HQS inspections, rent reasonableness, PIC validation/submission, appeals tracking and FSS"; "Suite includes all of HUD's required forms".
  - HCV Financials: GL/AP/AR/bank book; "program centric, centralized, or project-based accounting across multiple funds".
  - FSS: track services, "calculate escrow payments and interest proration, process payments".
  - HQS Inspections: scheduling, quality-assurance inspections, correspondence, inspection history, automatic reinspections; mobile field capture (HQS Mobile Touch) syncing to the suite; NSPIRE compatibility highlighted (including NSPIRE-V for HCV effective October 1, 2025 — vendor statement).
  - Landlord Portal: landlords view "HAP registers by resident, status of inspections and re-inspections, and up-coming recertifications"; prospective landlords list units; voucher holders search units by geography.
- MyHousing Portals (applicant/resident self-service), Administration Accounting, business-intelligence dashboards (Elite Insight Analytics), hosting, data conversion services.

### Product D — MRI Social Housing (UK, registered providers / local authorities)

Evidence layer: A (directly observed on official pages).

Key observations:

- The UK regime packages the same fundamental job differently: "Housing & Tenancy Management" (Housing Enterprise as the core housing management system), Finance Management, Asset & Repairs, Housing Options (property listings/advertising homes, homelessness, rough sleepers, case management), Digital Essentials (resident portals, SMS, e-signatures, document management), Legislative Reporting (tenant satisfaction measures — complaints, antisocial behaviour, asset management, repairs).
- Tenancy-side named products: Income Analytics (predictive rent-arrears analytics, early intervention, tenancy sustainment), Tenancy Analytics (single support-profile view), Housing Service Charges ("legislative requirements in achieving transparency with your billing"), HomeSwapper (mutual exchange service), Safer Communities ("report, monitor and track anti-social behaviour, domestic abuse and other tenancy breaches"), Customer Central (housing CRM, 360 view), Housing Mobile (field workforce).
- Regulatory frame is legislative/reporting-driven ("various obligations and regulations"; tenant satisfaction measures) rather than per-household income certification — the UK regime's compliance center of gravity differs from the US one.
- Scale claims (vendor marketing, not asserted in final doc): 850+ social housing clients UK/IE, 5.7M homes managed, 280+ local authority clients, "82% of social housing units across UK & Ireland supported".

### Product E — RealPage (US, operator side) — positioning only

Evidence layer: limited (official operational docs unreachable; see limitations). RealPage is a major US vendor in this market and markets affordable-housing compliance products (widely known industry position), but no operational detail was verified in this pass. The final document does not rely on RealPage for any structural claim.

## Cross-product Comparison

| Dimension | Yardi Breeze Premier (US operator) | MRI Affordable/PH (US operator+agency) | Emphasys Elite (US PHA) | MRI Social Housing (UK provider) |
|---|---|---|---|---|
| Program as object attached to stock | yes — LIHTC, HUD 50059, RD, HOME, local programs; set-asides | yes — HUD Multi-Family, Tax Credit, HOME, USDA RD, "multiple subsidy types" | yes — HCV, LIPH, 50059, RAD, LIHTC, RD, MTW, FSS, Mutual Help, Shelter Plus Care | regime-level regulation (legislative obligations) rather than per-unit program tags |
| Applicant eligibility determination | yes — document eligibility of every applicant/resident incl. non-qualifying households | yes — eligibility inside voucher lifecycle; waitlist compliance with program rules | yes — waiting list "making eligibility determinations" | allocations/homelessness machinery in Housing Options (eligibility by allocation law, not income certification) |
| Waiting list with ordered demand | yes — streamlined waiting list management | yes — central hub, program rules, automated communications | yes — multiple lists, preferences, bedroom requirement, date/time ordering | waiting/allocations lists (choice-based lettings, homelessness duty) |
| Certification/recertification of household | yes — mass recertifications; online certifications via add-on | yes — residents complete certifications/recerts in portal; recert reminders | yes — re-exam processing; upcoming recertifications visible to landlords | not the center — tenancy sustainment instead |
| Income/asset calculation & verification | yes — member/family/asset/income/expense tracking; Verification Services add-on | yes — Automated Income Verification product | yes — income determination in HCV workflow; HUD forms included | income analytics = rent-arrears analytics (different meaning of "income") |
| Program-constrained rent | yes — rent reports; unauthorized-increase control on market-rate units only | yes — rent calculations inside voucher lifecycle | yes — payment standard calculations, rent reasonableness | rent standard context; service charges transparency |
| Subsidy money flows | yes — receive and distribute subsidy/HAP payments | yes — voucher management incl. TRACS submissions | yes — HAP registers; FSS escrow; program-centric accounting across funds | housing benefit / rent collection (arrears focus) |
| Regulatory reporting output | yes — TRACS & MINC electronic submission; tax credit & project-specific rent reports | yes — centralized compliance reporting; TRACS | yes — PIC validation/submission; HUD 50058/50059 forms | yes — legislative reporting, tenant satisfaction measures |
| Inspections | (not surfaced on fetched pages) | yes — inspection tracking in voucher lifecycle | yes — HQS/NSPIRE scheduling, mobile capture, reinspections | repairs/asset compliance (different regime: stock condition, not HQS) |
| Resident/applicant portal | yes — RentCafe Affordable Housing (applications, certifications, e-sign lease) | yes — apply, certify/recert, requests, info updates | yes — MyHousing Portals; applicant portal | yes — self-service portals, SMS |
| Landlord/partner portal | (not surfaced) | (not surfaced) | yes — landlord portal with HAP registers, inspection status | n/a (owners are the providers themselves) |
| Maintenance/work orders | yes | (bundled via PMX family) | yes — LIPH maintenance scheduling | yes — Asset & Repairs, Housing Mobile |
| Accounting | yes — full GL/AP/AR, escrow/trust | yes — accounting & financial management | yes — HCV Financials GL/AP/AR/bank book | yes — Finance Management |
| Mixed market-rate + affordable | yes — explicit market-rate-unit rent-increase control | yes — "mixed portfolios" | n/a (PHA stock is program stock) | n/a (tenure mix instead) |

### What is shared (candidate common structure)

1. Housing programs as first-class rules attached to the housing stock (US: per-unit/per-project program tags; UK: regime-level obligations).
2. An applicant pipeline that ends in a recorded eligibility determination (income/eligibility criteria; waiting lists with rule-based ordering).
3. A per-household certification record that must be created at move-in and renewed on program cycles (US sample: annual recertification, interim recertification, mass recerts; portal self-service certification).
4. Rent that is not freely set: derived from program rules (rent limits/income-based share/utility allowances/payment standards/rent reasonableness), with subsidy money flows where the program pays.
5. Outward-facing compliance artifacts: regulatory reports (often electronically submitted in program-specific formats), certification files available for agency audit, inspection records.
6. A property-operations layer (leases/charges, rent collection/AR, maintenance, accounting) shared with general property management.
7. Self-service portals for applicants/residents (and, on the voucher side, landlords).

### Where products differ

- Center of gravity: operator-side compliance (Yardi/MRI affordable) vs agency-side program administration (Emphasys Elite, MRI Public Housing line) vs regime-level tenancy management (MRI UK).
- The meaning of "income" shifts: US = household income determination for eligibility/rent; UK = rent-account income collection/arrears.
- Inspections: US = HQS/NSPIRE/REAC-style program inspections; UK = stock/asset compliance and repairs.
- Subsidy flows: central in voucher/public-housing US products; absent in LIHTC-only operation (rent restriction without subsidy payments); UK = housing-benefit-era rent collection and arrears.

## Canonical Model (draft, pre-abstraction)

```text
Housing Program (rules: eligibility criteria, rent rules, reporting duties)
  └─ attached to Property / Unit (units may carry program layers; mixed portfolios)
Applicant / Waiting List
  └─ Application → eligibility determination (income/eligibility criteria)
Household (members, income, assets)
  └─ Certification (move-in) → Recertification (program cycle; interim events)
      └─ Program Rent (tenant share [+ utility allowance] [+ subsidy share])
          └─ Charges / payments / subsidy billing
Compliance Record (certification files, reports, inspections)
  └─ submitted to / reviewed by Program Authority
Property Operations (lease, maintenance, accounting) — shared PM layer
```

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Program-restricted housing stock** — the managed units/tenancies are bound to housing-program rules (a program is a first-class object attached to the stock or the regime).
2. **Eligibility-governed occupancy** — applicants/households are determined eligible or ineligible against program criteria, and that determination is recorded.
3. **Household certification with renewal obligation** — the household's eligibility/income record is certified at occupancy and must be re-verified on program-defined cycles or events.
4. **Program-constrained rent** — rent is derived or capped by program rules (limits, income-based share, allowances), not freely set by the operator; may split into tenant payment and subsidy.
5. **Compliance evidence outward** — the system produces the records/reports the program authority requires (reports, certification files, inspection records).

Rationale: remove 2–5 and the product is generic Residential Property Management; remove 1 and eligibility/certification have no anchor. Property operations (maintenance, accounting, portals) are NOT L0 — a compliance-first affordable system without deep PM tooling still belongs to this Type.

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- waiting-list management (multiple lists, preference criteria, bedroom-size matching, date/time or lottery ordering, list openings)
- online applications and applicant/resident portals (including self-service certification/recertification)
- income/asset calculation worksheets and third-party income/asset verification integrations
- household composition tracking (members, family, assets, income, expenses)
- program rent calculation machinery (contract rent vs tenant rent share, utility allowances, rent reasonableness in voucher contexts)
- subsidy/HAP billing and receipt-distribution where the program pays
- regulatory report generation and electronic submission in program-specific formats
- unit-level program layering for mixed portfolios (set-asides, income targeting)
- program inspections (scheduling, mobile field capture, reinspection)
- rent collection/AR and delinquency handling
- maintenance/work orders
- document management / certification file for agency audit
- accounting (GL/AP/AR, owner statements)
- compliance dashboards/analytics
- landlord/partner portals (voucher-side)
- tenant screening

### L2 — Variant / Optional Structure

Depends on regime, operator type, program mix, scale, deployment:

- regulatory regime: US HUD Multifamily (50059/TRACS), US Public Housing (50058/PIC), Housing Choice Voucher administration, LIHTC/state HFA reporting, USDA Rural Development, HOME, local programs; UK social housing (tenancy/arrears/ASB/service charges/tenant satisfaction measures/mutual exchange/homelessness options); other national regimes
- operator type: private owner/agent, nonprofit operator, public housing authority (landlord + administrator), state/local housing finance agency (allocation & compliance monitoring), syndicator/investor reporting side
- program shape: project-based assistance (units) vs tenant-based vouchers (assistance follows the household; issuance→lease-up→HAP→portability workflow)
- mixed-income composition (market-rate units alongside program units in one property)
- supportive/special-needs housing overlay (case management, services, FSS escrow)
- portfolio scale and multi-entity structures; deployment (cloud SaaS, hosted, on-prem)

### L3 — Vendor-specific Structure

Stays in Research Notes:

- Yardi: RentCafe Affordable Housing, Verification Services, ScreeningWorks Pro, Investment Manager, CHECKscan/PayScan, agency reporting & voucher processing services, "mass recertifications" as a named capability
- MRI: PHA Pro, WaitListCheck, Voucher Management, Online Application Management, Automated Income Verification, Fee Accounting service, UK products (Housing Enterprise, Income Analytics, Tenancy Analytics, Housing Service Charges, HomeSwapper, Safer Communities, Customer Central, Housing Mobile), MRI Agora
- Emphasys: Elite HCV/LIPH modules, MyHousing Portals, HQS Mobile Touch, Elite Insight Analytics, Emphasys University, RAR (Reasonable Accommodation Request), Certification Generator, Address Management
- Vendor-published numbers (not asserted in final doc): MRI "500+ affordable owners/operators", "70k average monthly online applications", "82% of UK social housing units"; Emphasys "since 1976", landlord-portal "reduced phone calls by up to 70%"; Yardi Breeze pricing ($3/unit/month affordable, $400 minimum)

## Vendor-specific Findings

- Yardi Breeze's "control against unauthorized rent increases (market-rate units only)" is direct evidence that mixed market-rate/affordable portfolios are a normal configuration, and that rent-change control is program-scoped.
- Emphasys's positioning ("private-sector tools treat public housing as an afterthought") is direct vendor testimony that the PHA/agency side has distinct enough requirements to sustain dedicated products.
- MRI's UK/US split (same vendor, two different product families for the two regimes) is strong evidence that regime is a variant axis, not the Type boundary.
- bostonpost.com redirecting to mrisoftware.com indicates consolidation of dedicated compliance vendors into suites (observation only).

## Boundary Findings

1. **vs Residential Property Management** (closest neighbor): shares the entire property-operations spine (units, leases, charges, rent collection, maintenance, accounting). The differentiator is the program layer: eligibility determination, certification/recertification, program-constrained rent, compliance reporting. Structural test: remove the program/compliance layer → a residential PM product remains; remove deep PM tooling → an affordable compliance/management system remains. Vendors themselves ship both as one suite with affordable as a property-type configuration (Yardi Breeze) or a module beside PM (MRI) — related Types sharing a spine, not duplicates.
2. **vs Housing Assistance Management (§24 sibling)**: this leaf is operator-side (running program-restricted housing); §24's Housing Assistance Management is expected to be the program-administrator side (agency administering assistance/casework). The boundary is porous in reality: a PHA is simultaneously landlord (public housing), administrator (vouchers), and program recipient; Emphasys and MRI both sell agency-side and operator-side lines. Flag for joint review when Housing Assistance Management is processed.
3. **vs Tenant/Resident Portal**: the portal is a delivery surface (L1) of this Type, not a competing Type; in affordable products the portal uniquely carries certification/recertification self-service.
4. **vs Student Housing Management**: eligibility by enrollment/student status with academic-cycle leasing; different programs and rules; adjacent Type.
5. **vs HOA/Community Association Management**: ownership governance and assessments, not rental tenancy under program rules.
6. **vs Rent Collection Platform / Property Maintenance Management**: capabilities inside this Type (and inside RPM), not the defining layer.
7. **Regime naming**: "affordable housing management" (US operator framing), "public housing management" (PHA framing), "social housing management" (UK framing) all denote the same underlying Type under different regimes — regime is L2. The directory leaf name uses the US-market term; no rename proposed.
8. **Voucher administration**: tenant-based voucher administration (issuance, RFTA, lease-up, HAP, portability) is a workflow variant inside the same Type (no unit stock under management in the same sense) — kept as a variant, not a separate Type; noted as a possible future split if the directory ever grows a dedicated leaf.

## Uncertainties

- RealPage's affordable products could not be verified (help center moved behind product login; root URLs 404). The market-share picture among US operator-side vendors is therefore incomplete; no structural claim depends on RealPage.
- Exact report formats, submission deadlines, income-calculation method details (e.g., specific HUD handbooks), and state names were deliberately not asserted: vendor pages name TRACS, MINC, 50059, 50058, PIC, HQS/NSPIRE, but operational specifics live behind customer logins.
- Whether waiting-list machinery should be L0 was resolved as L1 (eligibility determination is the invariant; the queue is the common mechanism). A fully-occupied property with no open list still requires certification machinery.
- UK-side evidence is from one vendor family (MRI UK); the UK regime description is therefore asserted more cautiously (regime-level obligations, tenancy/arrears/ASB center of gravity) without claiming UK market structure exhaustively.
- NEC Housing and Civica pages were not usable (image-only / 404); no UK-native second sample obtained.

## Historical / Market-Sample Check

- Emphasys has sold PHA software since 1976; the L0 (program rules + eligibility + certified household + program rent + reporting) describes that era's systems as well as current SaaS — no anachronism detected.
- UK housing management systems predate the current tenant-satisfaction-measures regime; the L0 still holds (program-governed tenancy + regulated rent + reporting duty).
- Older US systems were 50059/TRACS batch-report generators on top of basic PM; the L0 holds. Modern additions (portals, verification APIs, analytics) sit at L1.
- Conclusion: the definition is not over-fitted to the current SaaS era.

## Final Synthesis

Affordable Housing Management is the operator-side application Type for running rental housing whose occupancy and rents are governed by housing-program rules. Its defining core is a five-part chain: program-restricted stock → eligibility-governed occupancy → certified household records with renewal obligations → program-constrained rent (often split tenant/subsidy) → compliance evidence produced for the program authority. Around that core, mature products add the standard property-operations layer (waiting lists, portals, inspections, maintenance, accounting) and vary by regulatory regime (US HUD/tax-credit vs UK social housing being the two regimes documented here), operator type (owner/agent vs housing authority vs state agency), and program shape (project-based vs voucher-based). The Type is best understood as Residential Property Management plus a governing program/compliance layer that changes what occupancy, rent, and reporting mean.
