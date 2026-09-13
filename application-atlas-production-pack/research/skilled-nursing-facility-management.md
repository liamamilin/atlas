# Research Notes — Skilled Nursing Facility Management

## Research Goal

Understand what "Skilled Nursing Facility Management" software actually is in the market: what objects it holds, what work it runs, how it relates to the already-processed Long-term Care EHR Type (which left an open joint-review flag against this leaf), and where its boundaries sit against Healthcare Revenue Cycle Management, Hospital/Bed Management, and regional (UK) care home management software.

## Initial Boundary

Working hypothesis before research:

- A skilled nursing facility (SNF) is a facility providing 24/7 licensed nursing and rehabilitation care, in the US largely reimbursed by public payers (Medicare/Medicaid) on a per-diem basis.
- "SNF Management" is likely the facility's business/operations system of record: census, payer mix, billing/AR, compliance reporting, staffing — as distinct from the resident clinical record (the LTC EHR core).
- Nearest neighbors: Long-term Care EHR (sibling, joint review pending), Healthcare Revenue Cycle Management, Hospital Management / Bed & Capacity Management, Practice Management, Home Health EHR/Management, Hospice Management.
- Known market structure (inherited from the LTC EHR pass): US vendors bundle record + operations in one platform; the seam is clinical record of record vs business/operations layer.

## Research Questions

1. What is the census in an SNF system — is it a first-class object, and what state does it carry (occupancy, beds, payer mix, days)?
2. How does the money path work — what is billed, to whom, on what basis (per-diem? claims? invoices?), and how tightly is it coupled to the census?
3. What assessment/compliance machinery exists, and is it coupled to payment (assessment drives payment level) or only to regulator reporting?
4. What operational modules are standard (staffing, admissions/referrals, trust funds, GL/AP, payroll) and which are optional?
5. Where is the seam to the LTC EHR core — do products exist at each pole (management-without-record, record-without-management)?
6. Does a regional (UK) analog fit the same definition, or is the Type US-market-shaped?
7. What is the role of outsourced revenue-cycle services relative to software?

## Representative Products

| Product | Vendor | Pole / rationale | Evidence tier reached |
|---|---|---|---|
| PointClickCare (EHR for SNF + add-ons) | PointClickCare | Market leader; bundled record + operations suite | Tier-2 product pages (products hub, SNF EHR platform page) |
| MatrixCare Skilled Nursing | ResMed / MatrixCare | Established enterprise suite, same bundled posture | Tier-2 product pages (SNF software page) |
| WellSky Long-Term Care + WellSky Revenue Cycle Services | WellSky | Platform vendor + the outsourced-RCM-services pole (money path without record) | Tier-2 product/service pages (LTC platform page, SNF RCM services page) |
| Person Centred Software (mCare / Connected Care) | Person Centred Software | UK regional analog (care home management, record-led) | Tier-2 product pages (home page / platform) |
| ADL Data Systems | ADL | Legacy finance-led regional pole | UNREACHABLE (2 attempts) |
| CarePlanner | CarePlanner (UK) | UK care home management with invoicing | UNREACHABLE (2 attempts) |

Selection notes: three US bundled-suite vendors at different scales/philosophies, one services pole (outsourced RCM) that proves the money path can exist as a managed operation, one UK regional analog for the historical/regional check. ADL and CarePlanner were chosen for the finance-led legacy pole and UK invoicing depth respectively; both unreachable, recorded as a sourcing limitation.

## Sources

- PointClickCare — Products hub: https://pointclickcare.com/products/ (fetched 2026-09-09)
- PointClickCare — EHR for Skilled Nursing Facilities: https://pointclickcare.com/products/skilled-nursing-platform/ (fetched 2026-09-09)
- MatrixCare — Skilled Nursing Software: https://www.matrixcare.com/skilled-nursing-software/ (fetched 2026-09-09; note: /solutions/skilled-nursing/ redirects to the interoperability page)
- WellSky — Long-Term Care: https://wellsky.com/long-term-care/ (fetched 2026-09-09)
- WellSky — Revenue Cycle Services for Skilled Nursing: https://wellsky.com/services/revenue-cycle-services/skilled-nursing/ (fetched 2026-09-09)
- Person Centred Software — home/platform: https://www.personcentredsoftware.com/ (fetched 2026-09-09)
- ADL Data Systems — https://www.adldata.com/ and https://adldata.com/ — FAILED (empty response / transport error, 2 attempts each form) — abandoned
- CarePlanner — https://www.careplanner.co.uk/ and https://careplanner.co.uk/ — FAILED (transport error, 2 attempts) — abandoned

Source-access limitation: all reachable evidence is Tier-2 (official product/marketing pages). Vendor help centers are login-gated (consistent with the LTC EHR pass observation). No Tier-1 operational documentation (user guides, billing manuals) was reachable. Therefore: no precise operational facts (claim windows, billing-cycle mechanics, PDPM rates, month-end close rules, numeric limits) are asserted anywhere in this research or the final document; all such detail is deliberately unstated. Marketing scale numbers observed (e.g., PCS "10M notes/day", "160K residents") are recorded here as vendor claims only, not used as evidence of structure.

## Product Observations

### PointClickCare (Layer A — direct, Tier-2)

- Products hub organizes the Skilled Nursing line as: "EHR for SNF" platform + Value Packages (Advanced Insights, Integrated Lab and Imaging, Integrated Pharmacy Orders, Nursing Support, Practitioner Engagement) + Value Add-ons (Chart Advisor, **Billing Advisor**, **Referral Advisor**, **Apploi Hire and Onboard**, **Apploi Schedule**, Automated Care Messaging, **PDPM Coach**, Mealtime Solutions, **General Ledger/Accounts Payable**, Virtual Health, Canadian Lab Orders). The add-on taxonomy itself shows the operations bundle: billing, referrals/admissions, scheduling, PDPM (payment-model) coaching, GL/AP.
- SNF EHR platform page positions the product as "a secure and fully integrated cloud-based platform... optimizes clinical and financial outcomes", ONC-certified post-acute EHR.
- "Key Functionality" list (five areas):
  1. **System** — dashboards, single sign-on, master patient index.
  2. **Revenue Cycle Management** — "Generate a holistic financial view and optimize billing and collections. Create, submit, track and appeal claims. Streamline financial operations and maximize revenue while providing a secure trust fund management experience."
  3. **Clinical Documentation** — point-of-care documentation, care plans, allergies/vitals/weights, "Automate MDS submission to iQIES."
  4. **Care Transitions and Operations** — "track resident status throughout their care journey", resident event calendars, "**validate insurance coverage**", incident reports.
  5. **Order Management** — mobile-enabled medication and treatment administration (eMAR-shaped).
- Industry-solutions navigation for Skilled Nursing surfaces the operator's problem list: "Improve your Financial Health", "Increase Occupancy", "PDPM with Confidence", "Ensure Quality and Compliance", "CMS Facility Assessment Template", staffing shortage pages.
- Interpretation: one platform carries BOTH the LTC EHR core (record, care plans, eMAR) AND the management core (claims, AR, trust funds, insurance validation, occupancy, PDPM machinery). The bundle is explicit.

### MatrixCare (Layer A — direct, Tier-2)

- SNF page: "comprehensive EHR solution... manage the needs of both post-acute and long-term care residents"; "One global EHR solution eliminates the need for multiple systems"; "Revenue cycle management tools can improve operational processes that help your facility boost cash flow and streamline reporting"; "Alerts and audits can help you maintain regulatory compliance".
- Named modules: **MyAnalytics** ("insights into key areas of your business – from **census and financial accounts receivable** to readmissions and quality measures"), **Clinical Advanced Insights** ("Forecast staffing needs"), **Enterprise Financials** ("Manage all aspects of accounting and operational finances with one integrated module... budgeting and cash flow").
- Dedicated banner: "Support for MDS updates—right at your fingertips. We're prepared for a new MDS on October 1, 2023" — the MDS assessment instrument is a first-class product concern (payment-driving regulatory machinery).
- Skilled Nursing solutions nav: CRM, Financial & operations management, Referral management, Regulatory compliance, Revenue Cycle Management (shared SKU family with senior living/LTC), Nutrition management, Retail management, Resident engagement, Interoperability.
- Interpretation: same bundled posture; census + AR named together as the business KPIs; MDS machinery explicit.

### WellSky (Layer A — direct, Tier-2; two surfaces)

- Long-Term Care platform page: "Intelligent Medical Record™ platform that supports the entire continuum of long-term care"; all-in-one across skilled nursing / AL-IL / intermediate care / CCRC; related products: **WellSky Payroll**, **Revenue cycle management software** ("one-touch billing... Quickly identify and resolve issues with billing and collections"), **Revenue cycle services** (outsourced billing/collections/audit), **Financial management software** ("multi-facility accounting, depreciation forecasts, and check processing"). Testimonial from an **MDS Coordinator**.
- SNF Revenue Cycle Services page (the services pole): "improve cash flow times, increase collections, and contain costs for skilled nursing and other long-term care facilities... navigating payer complexities, **managing CBOs** [central business offices]". Three named capabilities:
  1. **Payer management framework** — "experience with all payers and rates across **Medicare, Medicaid, HMO, Hospice, Private, and Patient Liability**" — the payer-category structure of SNF billing, stated explicitly.
  2. **Cross-department communication** — "admissions, case management, social work, discharge planning, and billing" must coordinate for "accurate A/R management"; cash posting/bookkeeping transparency.
  3. **Denial conversions** — "fighting inappropriate denials... undertake **appeals**"; "aged A/R", "reduce your **DSO**".
- Interpretation: the money path (payer-categorized per-stay billing → AR → denials/appeals) is substantial enough to exist as a standalone managed service for SNFs — strong evidence that the payer-driven revenue cycle is a defining leg of the operations layer, independent of any clinical record.

### Person Centred Software (Layer A — direct, Tier-2; UK regional analog)

- "Digital care management and software for care homes"; Connected Care platform: mCare digital care planning (a "Digital Social Care Record System"), eMAR (ATLAS / acquired Camascope), care intelligence (IQ), wellbeing & activities, resident experience, learning & development, and a **"Care home operations"** solution area (staff dependency tool, digital reception, maintenance management, digital signage, nursecall messaging).
- Compliance framing is **regulator-evidence-shaped**: "helps with CQC inspections and compliance", "evidencing care for UK regulators with mCare", "prove to CQC the quality of care".
- **No payer-billing / per-diem census machinery is visible** on the reachable pages: no claims, no payer mix, no AR worklist. Funding/invoicing is not surfaced as a module.
- Interpretation: the UK analog is record-led (care record + operations tooling + regulator evidence), not payer-revenue-led. The US-style census→claims→AR money path is not a universal feature of "nursing home management software" worldwide — it is the shape of the US reimbursement regime.

### ADL Data Systems / CarePlanner — UNREACHABLE

No observations. Sourcing limitation recorded; the legacy finance-led pole and UK invoicing depth remain undocumented. Assertions are calibrated to the 4-product reachable sample.

## Cross-product Comparison

| Structure | PointClickCare | MatrixCare | WellSky (software) | WellSky (RCM services) | PCS (UK) | Evidence layer |
|---|---|---|---|---|---|---|
| Census / occupancy / resident status tracking | ✔ ("track resident status", "Increase Occupancy") | ✔ (census in MyAnalytics) | ✔ (LTC platform) | ✔ (admissions↔billing coordination) | partial (occupancy-shaped ops tools) | B |
| Payer/funding categorization of residents | ✔ (insurance validation) | ✔ (RCM) | ✔ | ✔ explicit (Medicare/Medicaid/HMO/Hospice/Private/Patient Liability) | ✘ not visible | B (US) |
| Claims / billing / AR with denials & appeals | ✔ ("create, submit, track and appeal claims") | ✔ (RCM tools, cash flow) | ✔ ("one-touch billing") | ✔ (denials, appeals, aged A/R, DSO) | ✘ not visible | B (US) |
| Assessment machinery coupled to payment | ✔ (MDS→iQIES automation, PDPM Coach) | ✔ (MDS updates support) | ✔ (MDS coordinator usage) | ✔ (payer/rate expertise implies it) | ✘ (CQC evidence instead) | B (US) |
| Trust funds | ✔ (explicit) | — | — | — | ✘ | A (single-product explicit) |
| GL / AP / accounting | ✔ (add-on) | ✔ (Enterprise Financials) | ✔ (financial management software) | — | ✘ | B |
| Payroll / staffing / scheduling | ✔ (Apploi Schedule add-on) | ✔ (staffing forecast in Advanced Insights) | ✔ (WellSky Payroll) | — | ✔ (staff dependency tool) | B |
| Referrals / admissions pipeline | ✔ (Referral Advisor) | ✔ (Referral management) | ✔ (admissions in RCM framing) | ✔ | ✘ | B |
| Clinical record / care plans / eMAR | ✔ | ✔ | ✔ | ✘ (services pole) | ✔ (record-led) | B |
| Regulator-facing reporting | ✔ (quality/compliance pages) | ✔ (alerts/audits) | ✔ | — | ✔ (CQC evidence) | B |

Reading: the three US software vendors bundle record + operations; the services pole carries the money path without a record; the UK pole carries the record without the payer machinery. The **census + payer-categorized money path + payment-coupled assessment cycle** combination is what all US-side evidence shares and what neither the services pole (no record) nor the UK pole (no payer machinery) duplicates.

## Canonical Model

### Level 0 — Defining Invariant (three jointly-held structures)

1. **The census of record** — the facility's resident population held as persistent census state over time: admissions/discharges/transfers, occupancy and bed state, and each resident's payer/funding category. The census is the master operational object; every other structure hangs off it.
   - Remove → an admissions tracker or bed board with no population memory.
2. **The census-driven payer money path** — billing and receivables generated from census days under each resident's payer category: per-diem claims/invoices to public payers, managed care, and private payers; coverage/authorization tracking; denial and appeal handling; AR management to collection.
   - Remove → a census tracker with no economics; or generic claim processing with no facility census (= Healthcare RCM territory).
3. **The reimbursement-coupled assessment & compliance cycle** — the recurring structured assessment/reporting operations bound to the census that determine payment level and satisfy regulator reporting obligations (in the US realized as the MDS assessment cycle driving case-mix payment, plus staffing-hour and quality reporting).
   - Remove → generic billing/AR (the "skilled" coupling dies); or a bare compliance-submission utility.

Jointly-held load-bearing tests:
- 1 alone = occupancy/bed board or admissions tracker.
- 2 without 1 = generic healthcare billing/RCM.
- 3 without 1+2 = compliance reporting utility.
- 1+2 without 3 = lodging-style per-diem billing (hotel-PMS-shaped) — loses the skilled-care payment coupling.
- 1+3 without 2 = census + assessments with no money path.
- 2+3 without 1 = claims processing without facility state = payer-side RCM.

### Level 1 — Common Mature Structure

- Bundled clinical record (care plans, point-of-care documentation, eMAR) — universal in US software suites, absent at the services pole; it is the LTC EHR sibling core, not this Type's definition.
- Trust funds (resident funds held in custody) — US-common, explicit in one sampled product.
- GL/AP and multi-facility accounting; payroll.
- Staffing/scheduling and staffing-forecast analytics.
- Referral/admissions pipeline from hospitals (CRM-shaped).
- Analytics dashboards over census, AR, quality, readmissions.
- Interoperability/exchange with hospitals and pharmacies.
- Month-end close machinery (implied by AR/census KPIs; precise mechanics undocumented — not asserted).

### Level 2 — Variant / Optional Structure

- **Reimbursement regime** (the dominant variant axis): US Medicare/Medicaid per-diem claims with case-mix assessment machinery (MDS/PDPM-era), consolidated-billing-style rules, staffing-hour reporting; UK local-authority/private fee funding with CQC evidence; fully private-pay markets.
- Single facility vs multi-facility chains (regional/enterprise roll-ups, multi-facility accounting).
- Software vs outsourced revenue-cycle services (the money path delivered as a managed operation).
- Ancillary/therapy management, dining/nutrition, resident engagement, retail.
- AI/insight layers (predictive staffing, payment coaching).

### Level 3 — Vendor-specific (research notes only)

- PointClickCare add-on names (Billing Advisor, PDPM Coach, Chart Advisor, Referral Advisor, Apploi Schedule/Hire), "Automate MDS submission to iQIES" wording, ONC-certification positioning.
- MatrixCare module names (MyAnalytics, Enterprise Financials, Clinical Advanced Insights), the "new MDS on October 1, 2023" banner.
- WellSky branding (Intelligent Medical Record™, SkySense AI™), the payer list wording (Medicare, Medicaid, HMO, Hospice, Private, Patient Liability), "nearly 100% collections" marketing claim.
- PCS branding (mCare, ATLAS eMAR, Camascope acquisition, IQ), scale claims (10M notes/day, 160K residents, 80K staff, 8,000 providers).
- Inherited observation from the LTC EHR pass (not re-verified this pass): American HealthTech's domain redirects to PointClickCare — market consolidation of a legacy SNF financials vendor into the leading suite.

## Vendor-specific Findings

See Level 3 above. Additionally: MatrixCare and WellSky sell sibling SKUs for senior living / life-plan communities sharing the RCM/financials family — the SNF-specific content (payer machinery, MDS) is what differentiates the SNF SKU; this supports treating the payer-coupled operations as the SNF Management core rather than generic senior-care operations.

## Boundary Findings

1. **vs Long-term Care EHR (joint review discharge)** — CONFIRMED from this side. The seam is record-of-record vs operations-of-record:
   - LTC EHR core (per the processed sibling): resident standing record + assessment→care-plan loop + shift care documentation + medication administration record.
   - SNF Management core (this pass): census of record + census-driven payer money path + reimbursement-coupled assessment/compliance cycle.
   - US platforms bundle both cores in one product (observed in all three US vendors) — the leaves are separable analytically, not by vendor packaging. Poles exist on both sides: the outsourced-RCM-services pole carries the money path with no clinical record; the UK record-led pole carries the record with no payer machinery. The MDS assessment is the shared object on the seam: clinical content inside the EHR, payment-driving compliance object inside the management system. **Keep-both RATIFIED.**
2. **vs Healthcare Revenue Cycle Management** — generic RCM processes claims for providers without holding a facility's census/occupancy/payer-mix state. SNF Management's money path is census-driven and facility-bound (per-diem days × payer category). A claims engine without the census is RCM territory.
3. **vs Hospital Management / Bed & Capacity Management** — hospital bed management is encounter-driven acute flow (admit→discharge→transfer throughput); the SNF census is long-stay, per-diem, payer-categorized, and coupled to case-mix assessment. Different unit of economic time (encounter vs census day).
4. **vs Practice Management System** — ambulatory scheduling + fee-for-service billing around encounters; no facility census, no per-diem public-payer machinery.
5. **vs Employee Scheduling / Payroll** — staffing is a common module (and a regulatory reporting input in the US), not the core; staffing products lack census/money/assessment.
6. **Regional boundary (UK)** — the UK care home management analog is record-led (care record + operations tooling + CQC evidence) and does not surface the payer-census machinery. The Type as named ("Skilled Nursing Facility") is US-market-shaped; the regional analog sits closer to the LTC EHR / care-record territory. Taxonomy note recorded below.
7. **vs Senior Living operations** — private-pay services/ hospitality-shaped operations vs payer-driven skilled care; the sibling-SKU question (Senior Living EHR) belongs to the senior-living leaf when processed.

## Uncertainties

- Help centers login-gated at all three US vendors; no Tier-1 operational documentation reached. Precise billing-cycle mechanics, claim submission windows, month-end close rules, and PDPM-era specifics are deliberately unstated.
- ADL Data Systems (legacy finance-led pole) and CarePlanner (UK invoicing depth) unreachable ×2 each — the finance-led software pole is evidenced only indirectly (via WellSky's RCM software/services framing and the inherited AHT observation).
- Whether UK care home products carry local-authority invoicing as a first-class module — unverified.
- Historical software products (pre-case-mix era nursing home billing systems) not directly researched; the historical check was performed at the conceptual level (paper-era nursing home office: census book + per-diem billing + payment-relevant resident certification) rather than against named legacy products.
- The exact split of MDS functionality between "EHR" and "management" SKUs inside one vendor's packaging is not observable from marketing pages.

## Taxonomy Notes (for STATUS.md Boundary Issues)

- The leaf is US-market-shaped: "skilled nursing facility" is a US regulatory facility class, and the payer-census machinery that defines the management core is the shape of US public reimbursement. The UK regional analog (care home management) is record-led and does not surface this machinery; it sits closer to the LTC EHR / digital-social-care-record territory. The Type definition above is written at the abstract level (census + funding-source money path + assessment/compliance cycle) so that non-US funding regimes can instantiate it, but the observed market realization is US-dominant.
- Forward note for sibling leaves: the same record-vs-management seam likely applies to home-health-ehr-management and hospice-management when processed.

## Final Synthesis

Skilled Nursing Facility Management is the facility's business operations system of record. Its defining core is three jointly-held structures: the census of record (resident population as persistent census state with payer/funding categories, occupancy, and admission/discharge history), the census-driven payer money path (per-diem claims/invoices by payer category with coverage tracking, denials/appeals, and AR), and the reimbursement-coupled assessment & compliance cycle (recurring structured assessments and regulator reporting that determine payment level). The resident clinical record is the sibling LTC EHR core, commonly bundled in US platforms but not definitional here; the money path can even be delivered as an outsourced service, and the record can exist without the payer machinery (UK pole). The Type is US-market-shaped in its dominant realization while remaining abstractable to other funding regimes.
