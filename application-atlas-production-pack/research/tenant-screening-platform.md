# Research Notes — Tenant Screening Platform

## Research Goal

Understand what a Tenant Screening Platform actually is as an Application Type: what exists inside it, who uses it, how a screening actually flows from request to report to rental decision, which rules shape it, and where its boundary sits against the neighboring rental-side Types (Rental Application Platform, Residential Property Management, Property Showing Platform) and the consumer-report Types (Background Check Platform, Employment Verification Platform, Identity Verification, Credit Scoring).

## Initial Boundary

Working hypothesis before research:

- A tenant screening platform is the rental side's consumer-report machinery: it compiles an applicant person's credit, criminal, eviction, and income data into reports that a landlord/property manager uses to decide whether to rent.
- Nearest neighbors: Background Check Platform (same consumer-report grammar, employment decision context), Rental Application Platform (the application record and decision flow), Residential Property Management (the suite whose leasing pipeline embeds screening), Employment Verification Platform (income/employment facts as a component).
- Prior passes left forward flags to discharge here:
  - rental-application-platform (2026-09-09): seam = consumer-report machinery vs reports attached to an application record; keep-both proposed.
  - property-showing-platform (2026-09-09): showing platforms embed light pre-screening as a scheduling gate; the screening system of record is the sibling Type.
  - residential-property-management (2026-09-09): screening inside RPM = reports attached to applications in the leasing pipeline; the consumer-report machinery is not the RPM record; keep-both proposed.
  - background-check-platform (2026-09-06) listed "engine re-aims (tenant/trust/personal)" as L2 — this pass must draw the seam explicitly.

## Research Questions

1. What is the unit of record — what does a "screening" look like as a persistent object?
2. What report products exist (credit, criminal, eviction, income, identity, score) and how are they packaged?
3. Who initiates a screening (landlord-invite vs tenant-initiated) and who pays (tenant-paid vs landlord-paid)?
4. How does the applicant-side flow work (consent, identity verification, SSN handling, payment)?
5. What data sources feed the reports (bureaus, courts, registries, bank/payroll connections)?
6. How do jurisdiction rules shape the product (coverage limits, conditional acceptance, fee caps, voucher rules, portable reports)?
7. What compliance machinery is structural (adverse action, dispute, requester-side verification)?
8. Where does the rental decision happen — platform or requester?
9. What are the hosting forms (standalone product, toolset module, suite module, venue-embedded)?
10. How does this Type differ from Background Check Platform and Rental Application Platform?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| TransUnion SmartMove | bureau-native (the data supplier sells screening directly) | defines the report-package vocabulary; tenant-consent flow |
| RentSpree | standalone SaaS screening product (landlord + agent/MLS pole) | dashboard/request tracking, automated adverse action, jurisdiction documentation |
| TurboTenant | landlord-first free toolset with screening embedded (independent landlords) | tenant-paid economics, Snappt fraud detection, portable-report rules |
| RentPrep | human-verified service pole (FCRA-certified screener review) | different verification philosophy; enterprise tier |
| Zillow Rental Manager | venue-embedded screening inside a listings platform | Experian+CIC supply, requester-side identity verification, application manager |

Rejected as primary samples: RealPage and AppFolio (enterprise/suite poles) — official pages unreachable (404 ×2 each); noted as sourcing limitation, their structure corroborated indirectly by the residential-property-management pass (Buildium/TransUnion, AppFolio/FolioScreen, Rent Manager/AmRent integrations).

## Sources

Research date: 2026-09-10. All Layer-A unless noted.

- TransUnion SmartMove — https://www.mysmartmove.com/ (root: how-it-works steps, report products, packages, FAQ, adverse-action template link, dispute-process link, jurisdiction disclaimer)
- RentSpree — https://www.rentspree.com/tenant-screening (product page + FAQ schema); https://support.rentspree.com/en/screening-restrictions-and-limitations (help center: coverage maps, conditional acceptance, CA SB 267, fee-cap table)
- TurboTenant — https://www.turbotenant.com/tenant-screening/ (product page + 25-question FAQ schema: flow, SSN handling, freeze/fraud-alert behavior, portable TSRs, FCRA/FHA rules, state-law variation)
- RentPrep — https://rentprep.com/ (packages, human-verification process, add-ons, enterprise tier, Stessa delivery)
- Zillow Rental Manager Help Center — https://help.zillowrentalmanager.com/hc/en-us/articles/4404822950291 (report composition: Experian + CIC); https://help.zillowrentalmanager.com/hc/en-us/articles/360058413693 (requester-side identity verification, application manager)
- CFPB tenant-screening-report explainer and FTC landlord guidance — referenced verbatim inside TurboTenant/RentSpree official FAQ text (Layer B, not fetched directly)

Sourcing limitations: RealPage and AppFolio official pages unreachable (404). Zillow marketing site JS-walled in prior passes; the Zendesk help center was reachable this pass. Non-US tenant screening (UK referencing, Canada) not sampled — all five products are US-market; assertions below are calibrated to the US sample with regime-agnostic phrasing where possible.

## Product Observations

### TransUnion SmartMove (bureau-native)

Key observations (Layer A):

- Report products: Credit Report, ResidentScore (proprietary score "predicts rental eviction risk"), Criminal Background Report, Eviction Related Report, Income Insights ("tells landlords which applicants need additional income verification"), Identity Check Report.
- Packaged bundles: SmartCheck Premium / Plus / Basic — tiered report packages at per-request prices.
- Flow (documented 4 steps): create free landlord account (basic property info) → invite applicant by email, select reports bundle and who pays → applicant receives email and authenticates their identity → reports delivered to landlord.
- Subject gate: "They consent online to share the reports with the property owner"; "as soon as authorization is received and their identity is verified, reports are delivered."
- Who pays: "Choose who pays (where permitted)" — tenant-pay or landlord-pay.
- Soft pull: "No impact to their credit score."
- Compliance surfaces: Adverse Action Template offered; dedicated Rental Screening Dispute Process page; jurisdiction disclaimer ("Criminal Report and Eviction Related Proceedings Report are subject to federal, state, and local laws that may limit or restrict SmartMove's ability to return some records").
- Timing claim: most reports same day.
- Tenant-side signup exists (tenant can start the flow themselves).

### RentSpree (standalone SaaS)

Key observations (Layer A):

- Positioning: screening powered by TransUnion (credit/background/eviction) + Finicity (bank-verified income); free for landlords/agents; per-report pricing ($39.99 standard, $49.99 comprehensive; income verification $10 add-on).
- Report composition: credit report with ResidentScore; criminal background (national registries — sex offender, Most Wanted, OFAC — plus local court jurisdictions); eviction history (25M+ records claim); bank-verified income (deposit data instead of forgeable documents); reference checks (comprehensive package).
- Flow: create free account + add property → share application link → review completed reports in one dashboard → accept or decline from dashboard.
- Dashboard statuses observed in product screenshot: Ready / Started / Invited.
- Compliance automation: "accept/deny button that sends the required [adverse action] notice directly to the applicant"; conditional approvals; screening restrictions by jurisdiction.
- Jurisdiction documentation (help center): criminal-coverage state map with dated availability; eviction records unavailable in KY, LA, ME, SD, WY and not returned for NY applications; MA fault/no-fault eviction action notes; conditional-acceptance jurisdictions (Cook County IL, Detroit MI, Washington DC, Montgomery County MD, New Jersey); CA SB 267 — voucher holders may substitute evidence of assistance for a credit report, so RentSpree will not provide credit reports on those applicants; screening-fee cap table (CA $64, NY $20, MA prohibited, etc.).
- Agent pole: 300+ MLS integrations; agents generate screening requests from listings and share results with owners.
- Screening sits inside a wider rental toolset (listing syndication, applications, lease, rent collection) — screening is one module.

### TurboTenant (landlord-first toolset)

Key observations (Layer A):

- Screening embedded in a free landlord toolset (marketing, applications, leases, rent collection, accounting, maintenance); "screening runs inside the same account."
- Flow (documented 3 steps): enter applicant email or phone → send screening request → applicant approves, verifies identity (enters their own SSN; "landlords never collect or handle the SSN"), pays the fee → landlord notified to pull the report.
- Report composition: TransUnion credit report (score, score factors, tradelines, payment history, inquiries, collections) + nationwide criminal (300M+ records claim) + 50-state eviction check (failure to pay rent; judgments for rent/possession/money; unlawful detainers; writs and warrants) + snapshot summary at top.
- Income verification (Pro plan): self-reported income checked against TransUnion data + Snappt document-fraud detection (pay stubs/bank statements tampering; employer is a real business).
- Economics: tenant pays ($45 or $55 by landlord plan); landlord $0; landlord-pay option exists; "the report only generates once the fee is paid."
- Operational rules: identity verification expires after 30 days; credit freeze blocks the pull (applicant must lift it), fraud alert adds verification steps; bureau requires landlord's mailing address/phone before releasing reports; screening possible without an application on file (email/phone only).
- Portable tenant screening reports: in CO, CA, IL, MD, RI, NY, WA applicants may submit a portable report instead of paying a new fee; validity windows vary (30–90 days).
- Compliance framing: FCRA (written consent required; adverse-action notice naming the agency, free copy, dispute rights — template offered) + Fair Housing Act; state/local variation (criminal/eviction lookback limits, source-of-income protection, fee caps; Cook County bars criminal checks until after a conditional offer).
- Subject rights: tenant can access their own screening report; free copy within 60 days of denial; dispute inaccuracies.

### RentPrep (human-verified service)

Key observations (Layer A):

- Packages: Credit Report Only $29 (automated SmartMove package: full credit report, ResidentScore, bankruptcies); Full Background Check Only $29 (FCRA-Certified Screener Review, SSN verification, nationwide criminal & sex offender, nationwide evictions, judgments & liens, bankruptcies; landlord-pay only); Complete $49; Enterprise (50+ doors: custom workflows, tier screening, applicant-pay options, dedicated account rep, API integration).
- Human-verification process (documented 3 steps): (1) applicant identity "pre-verified" by an FCRA-certified screener comparing name/SSN/DOB against databases; (2) background check run, screeners "verify every record to reduce the frequency of false matches"; (3) final report checked for FCRA compliance — "non-compliant records are omitted."
- Add-ons: Income Verification $10 (bank-connected: balances, income streams, insufficient-funds history, up to 24 months of transactions); Income & Employment Verification $15 (payroll-provider data: employment status, job title, employer, hire dates, pay frequency, YTD gross/net).
- Reports delivered inside Stessa (Roofstock) platform; 2M+ screenings since 2007 claim.
- Enterprise pole explicitly positions against "the default option provided by your property management software" — evidence that suite-embedded screening is the norm it competes with.

### Zillow Rental Manager (venue-embedded)

Key observations (Layer A):

- Screening attached to the rental application inside a listings venue: "an identity verified renter application with a freshly pulled credit report, criminal background check, and housing court records."
- Supply structure differs from TransUnion pole: credit report by Experian (accounts, balances, on-time/late payment counts, collections, inquiries, public records incl. addresses/employers/bankruptcies); background check by CIC (nationwide housing court record search, sex offender search, nationwide criminal search).
- "In some cases, background checks are modified to reflect state and local legal requirements" — CIC regulatory-compliance tool referenced.
- Requester-side gate: landlords must verify their own identity (name/DOB/address + privacy questions; SSN optional) before viewing applicants' detailed reports — "helps us protect the privacy of renters' sensitive information and comply with the Fair Credit Reporting Act."
- Multi-employee property managers: one designated "application manager" must complete ID verification.
- Package structure: application + reports bundled; separate background-only or credit-only orders possible (per section article list).
- Tenant-initiated: renters apply to listings and the reports pull as part of the application; fee paid by applicant (landlord can pay).

## Cross-product Comparison

| Dimension | SmartMove | RentSpree | TurboTenant | RentPrep | Zillow RM |
|---|---|---|---|---|---|
| Hosting form | standalone bureau product | standalone SaaS (+ toolset) | landlord toolset module | standalone service (+ Stessa) | venue-embedded |
| Unit of record | screening request per applicant | screening request per property/applicant | screening request per applicant (application optional) | order per applicant | application with attached reports |
| Credit data | TransUnion | TransUnion | TransUnion | TransUnion (SmartMove package) | Experian |
| Criminal/eviction data | TransUnion | TransUnion | TransUnion + Rent Butter | in-house + databases | CIC |
| Income verification | Income Insights (flags who needs verification) | Finicity bank-verified | TransUnion check + Snappt fraud detection | bank add-on + payroll-provider add-on | not observed in sampled articles |
| Rental-specific score | ResidentScore | ResidentScore | TransUnion score | ResidentScore | not observed |
| Initiation | landlord invite or tenant signup | landlord/agent invite or application link | landlord invite (application optional) | landlord order | tenant applies to listing |
| Who pays | either (where permitted) | applicant typically; caps apply | applicant ($45/$55) or landlord | either (background-only landlord-pay) | applicant (landlord can pay) |
| Subject identity gate | applicant authenticates | applicant completes + verifies | applicant approves + verifies (own SSN) | FCRA-certified screener pre-verifies | applicant verified; landlord also verified |
| Requester gate | account + property info | account | account + bureau-required contact info | account | requester ID verification + application manager |
| Adverse action | template | automated notice on deny | template + FCRA guidance | FCRA compliance check on report | FCRA framing |
| Dispute path | dedicated dispute process | support + restrictions doc | free copy + dispute rights | FCRA-certified review | via bureau |
| Jurisdiction filtering | disclaimer | coverage maps + conditional acceptance + fee caps + SB 267 | state-law guides + portable TSRs | non-compliant records omitted | CIC compliance tool |
| Decision location | landlord | landlord (accept/deny buttons) | landlord | landlord | landlord |
| Human review | none observed | none observed | none observed | FCRA-certified screener review | none observed |
| Customer tier | independent landlords/PMs | landlords + agents (MLS) | independent landlords ≤50 doors | small landlords + enterprise 50+ | independent landlords + small PMs |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a tenant screening platform:

1. **The screening request as the unit of record.** A persistent, identified request to evaluate a specific applicant person for a rental decision — bound to the requesting party (landlord/manager/agent) and typically to a property or application context, carrying the requested report package and its lifecycle state (requested → subject authorization → in progress → report ready → used in decision). Initiation is two-sided-capable: landlord-invited or applicant-initiated. Remove → an order form, or a raw data lookup with no managed request.

2. **Consumer-report production over the applicant's records.** The platform's core machinery: compiling the person's credit history, criminal records, eviction/court records, identity attributes, and income/employment data from data sources (credit bureaus, courts, registries, bank/payroll connections) into packaged report products whose composition serves the tenancy decision — credit + eviction + affordability at the center, criminal records standard, income verification the common extension. Remove → a form tool or decision note with no report machinery (= Rental Application territory), or a generic data lookup.

3. **The subject-authorized, purpose-bound release.** The report is produced and delivered only under the applicant's authorization (or the regime's lawful basis), bound to the tenancy-evaluation purpose; the applicant is a rights-holding data subject (sees their own report, can dispute inaccuracies), and the requester carries use-obligations (adverse-action duties when the report is used against the applicant). The requester side is itself gated (account verification; at some poles requester identity verification). Remove → unregulated data brokering, or a consent form with nothing behind it.

Jointly-held load-bearing tests:

- 1 alone = request log / order form
- 2 without 1 = raw credit-puller / data lookup
- 3 without 1+2 = consent form with no report
- 1+2 without 3 = unregulated people-search/data brokering (not the market's tenant screening)
- 1+3 without 2 = rental-application territory (declared qualifications, no machinery)
- 2+3 without 1 = one-off report pulls with no managed request lifecycle

The rental decision itself stays with the requester: the platform produces reports and compliance machinery; it does not decide the tenancy. (Cross-product: all five sampled products deliver reports to the landlord, who accepts/declines — RentSpree's accept/deny buttons execute the landlord's decision and generate the notice.)

### L1 — Common Mature Structure

Present across the sample; expected in mature products but not definitional:

- Tiered report packages with optional add-ons (every product sells packages, composition varies)
- Rental-specific risk score (ResidentScore-class) predicting rental/eviction behavior rather than lending risk
- Income verification as a first-class component (bank-connection, payroll-provider, or document-upload + fraud detection)
- Applicant identity verification inside the flow (KBA questions; SSN entered by the applicant, never handled by the landlord)
- Requester-side gating (account setup with property/contact info; at one pole full requester identity verification before viewing reports)
- Adverse-action support (templates at minimum, automated notices at the mature pole; conditional-acceptance handling)
- Subject access + dispute path (tenant can view own report; dispute inaccuracies; free copy after denial)
- Request-tracking dashboard (statuses like invited/started/ready; report archive)
- Who-pays choice with jurisdiction fee rules (tenant-paid dominant; landlord-pay option; fee caps)
- Application adjacency (screening attaches to a rental application; screening without an application also possible)
- Multi-applicant handling (screen each adult; co-applicants)
- Jurisdiction-aware report filtering (coverage maps, lookback limits, conditional-acceptance jurisdictions, voucher substitutions)

### L2 — Variant / Optional Structure

- Initiation direction: landlord-invited vs tenant-initiated (portable tenant screening reports; state-mandated reuse with validity windows)
- Payer: tenant-paid vs landlord-paid vs fee-capped regimes
- Data supplier: TransUnion / Experian / CIC / Finicity / Snappt / Rent Butter / payroll providers — the platform is often an integrator over bureau/court/data-vendor supply
- Verification philosophy: fully automated instant reports vs human FCRA-certified review (false-match reduction, non-compliant record omission)
- Hosting form: standalone product / module in a landlord toolset / module in a property-management suite / embedded in a listings venue
- Customer tier: independent landlords / agents via MLS / professional PMs / enterprise operators (API integration, tier screening, dedicated reps)
- Distribution pole: agent/MLS channel
- Adjacent capabilities some products add: reference checks, rent reporting/credit building, listing syndication

### L3 — Vendor-specific (Research Notes only)

- ResidentScore, Income Insights, SmartCheck package names (TransUnion)
- Finicity bank-verification, Snappt fraud detection, Rent Butter partnership (TurboTenant/RentSpree supply chains)
- CIC regulatory-compliance tool, Experian supply (Zillow)
- FCRA-Certified Screener Review as branded process (RentPrep)
- Application manager role (Zillow)
- Specific fee-cap tables and dated coverage maps (RentSpree)
- Stessa co-brand delivery (RentPrep)
- Specific price points ($25–$55 packages; $45/$55 tenant fees)

## Historical / Market-Sample Check

- Pre-FCRA screening (local rental/credit bureaus serving landlords by phone/paper; landlord reference calls) satisfies structures 1–2 but not 3: no formal subject-authorization gate existed. The modern Type is defined by the regulated consumer-report structure; the gate is retained in L0 because it is universal and load-bearing across the entire researched market (every sampled product makes authorization the trigger for the pull). Phrased regime-agnostically ("subject authorization or the regime's lawful basis") so non-US regimes fit structurally.
- Non-US check: UK tenant referencing, Canadian screening products were not sampled. The L0 is written without FCRA-specific vocabulary; jurisdiction machinery appears in L1 as "jurisdiction-aware filtering," which is where regional regimes differ. Assertion strength for non-US markets: not asserted.
- Platform-native check: venue-embedded (Zillow) and suite-embedded (RPM suites, per prior passes) screening satisfy the same three structures — hosting form is not definitional.

## Vendor-specific Findings

See L3 above. Notable: the requester-side identity-verification gate (Zillow) is currently single-product in the sample — held as L1-adjacent observation, not promoted; bureau-required requester contact info (TurboTenant) similarly.

## Rejected Findings

- "Tenant screening = criminal background check" — rejected: credit + eviction + income are at least as central; some jurisdictions bar criminal checks until conditional offer; credit-only products exist.
- "Screening includes the rental application form" — rejected: the application is the sibling Type's record; decoupling observed in-product (RentSpree report-only orders; TurboTenant screening without application; Zillow help center separates Applications from Screening reports).
- "The platform decides the tenant" — rejected: all sampled products keep the decision with the requester.
- "Screening is always instant" — rejected: human-review pole exists; timing depends on subject completion (authorization, identity, payment).
- "Tenant screening is a US-only shape" — not asserted; sample is US; L0 phrased regime-agnostically.

## Boundary Findings

1. **vs Background Check Platform (§09, processed 2026-09-06)** — shared grammar: screening order on an identified individual, subject-authorized execution, composed screens against records/data sources, jurisdiction-filtered findings, decision kept with the customer, adverse-action + dispute machinery. Seam: the report package and decision context. Tenant screening centers credit + eviction + income/affordability for a tenancy decision, with requester population spanning unprofessional small landlords to large operators, tenant-initiated/tenant-paid flows and portable reports common; background check centers criminal/court/registry/employment screens for employment eligibility with organization-initiated orders. Removal tests hold both directions: strip the rental package composition → a background check platform remains; strip criminal/court machinery → a tenant screening platform (credit+eviction+income) remains. The background-check pass's "engine re-aims (tenant)" note is hereby refined: same engine family, different definitional package — keep-both.
2. **vs Rental Application Platform (§17, processed 2026-09-09)** — DISCHARGES its forward flag: keep-both RATIFIED. The application Type's record is the declared-qualifications application + decision flow; this Type's record is the screening request + consumer-report machinery. In-product decoupling confirmed in this pass's sample (RentSpree report-only orders and application-without-reports; TurboTenant screening without an application; Zillow help center separates "Rental Applications" from "Screening reports"). The consent/identity-verification flow appears on both sides but serves different records.
3. **vs Residential Property Management (§17, processed 2026-09-09)** — DISCHARGES its forward flag: keep-both RATIFIED. Screening inside RPM suites appears as reports attached to applications in the leasing pipeline (Buildium/TransUnion, AppFolio/FolioScreen, Rent Manager/AmRent, TurboTenant tenant-paid per that pass); the consumer-report machinery is not the RPM record (tenancy/portfolio is). Suite-embedded screening = this Type at module grain.
4. **vs Property Showing Platform (§17, processed 2026-09-09)** — DISCHARGES its forward note: pre-screening in showing platforms is a scheduling gate (hard-gate or question-flow) over viewing requests, not report machinery; the screening system of record is this Type. Seam held.
5. **vs Employment Verification Platform (§09, processed 2026-09-06)** — income/employment verification appears inside tenant screening as a report component (SmartMove Income Insights flags who needs verification; RentPrep payroll add-on; RentSpree Finicity). The employment-verification Type's record is the employment record + verification request producing confirmed facts; in tenant screening it is one component of a multi-report package for a tenancy decision. That pass's "industry packaging (tenant-screening)" L2 note is consistent: same verification capability, different packaging host.
6. **vs Identity Verification (§15, processed 2026-09-08)** — identity verification is a gate component inside the screening flow (applicant authenticates; requester verifies at one pole), not this Type's record.
7. **vs Credit Scoring Application (§13, processed 2026-09-08)** — rental-specific scores (ResidentScore-class) are subject-measure production embedded as a report component; the score's purpose (rental eviction-risk prediction) is rental-context-bound.
8. **vs Fraud Prevention Platform (§15, processed 2026-09-08)** — document-fraud detection (Snappt-class) is a component of income verification here; the protected-journey framing of that Type does not apply.
9. **vs Tenant/Resident Portal (§17, processed 2026-09-10)** — different subject: prospective applicant under evaluation vs existing resident with occupancy-anchored self-service.

No directory change requested. Keep-both structure ratified for all flagged seams.

## Uncertainties

- Enterprise/large-operator pole (RealPage, AppFolio, Yardi screening) not directly sampled this pass — official pages unreachable. Their structure is inferred from the residential-property-management pass's observations (suite-embedded screening with bureau integrations) and RentPrep's enterprise-tier feature list (API, tier screening, custom workflows). Assertion strength for the enterprise pole: moderate.
- Non-US markets unsampled; regional regime differences (UK referencing/guarantor structures, Canadian provinces) not documented.
- Whether requester-side identity verification (Zillow) is spreading across the market: single-product evidence in this sample.
- Exact report-retention periods, score ranges, and per-jurisdiction lookback windows: deliberately not stated (precision not supported by fetched evidence at canonical level).
- Income Insights' exact mechanics (which data flags whom): vendor-proprietary; described only at capability level.

## Final Synthesis

A Tenant Screening Platform is the rental side's consumer-report machinery. Its defining core is three jointly-held structures: the screening request as the unit of record (an identified applicant person bound to a requesting party and rental context, with a managed lifecycle); consumer-report production over that person's credit, criminal, eviction, identity, and income records, packaged for the tenancy decision; and the subject-authorized, purpose-bound release (the applicant's authorization gates the pull, the applicant holds access/dispute rights, the requester carries adverse-action obligations, and the rental decision itself stays with the requester). Everything else — packages, rental scores, income verification, dashboards, who-pays economics, jurisdiction filtering, human review, hosting form, initiation direction — is common mature structure or variant. The Type shares its regulatory grammar with Background Check Platform but is defined by its rental report package and tenancy decision context; it shares its subject with Rental Application Platform but is defined by report machinery rather than declared qualifications.
