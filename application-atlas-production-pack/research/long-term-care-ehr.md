# Research Notes — Long-term Care EHR

Research date: 2026-09-08
Slug: long-term-care-ehr
Directory leaf: Long-term Care EHR (§22 Healthcare & Life Sciences)

## Research Goal

Understand what a Long-term Care EHR actually is as an Application Type: who uses it, what core objects exist inside it, what workflows organize daily work in a residential long-term care facility, and how it differs from the generic (acute/ambulatory) EHR and from adjacent post-acute Types (Home Health EHR, Hospice Management, Skilled Nursing Facility Management, Senior Living systems).

## Initial Boundary

Working hypotheses before research:

1. Core use: the electronic health record for facilities where people **live** and receive ongoing care — nursing homes, skilled nursing facilities (SNF), assisted living / senior living, care homes, CCRCs, long-stay rehabilitation.
2. Primary users: nurses and nursing/care assistants (round-the-clock care staff), assessment/MDS coordinators, facility leadership (DON, administrator), therapists, dietitians, social services, activities staff, prescribers, billing/HIM staff.
3. Nearest Types: Electronic Health Record / EHR (acute), Home Health EHR / Management, Hospice Management, Skilled Nursing Facility Management, Care Plan Management, Nursing Information System, Senior Living operations software.
4. Likely boundary: the LTC EHR is organized around a **resident's standing life in the facility** (years-long stay, daily living care, recurring assessment cycles) rather than around episodic encounters (acute) or per-visit care in the person's own home (home health).
5. Unknowns at start: Is the US regulatory assessment machinery (MDS/PDPM) definitional or a regional realization? Is billing/RCM part of the Type? Is eMAR part of the record core or a separable module? Do non-US care-home systems (UK "digital social care records") belong to this Type?

## Research Questions

1. What is the unit of record — how is the "resident" established, and what does the record span?
2. What core objects exist (resident, stay/census, assessment, care plan, orders, MAR, care documentation, billing linkage)?
3. How does the assessment → care plan → daily care → documentation loop actually run?
4. How does the medication loop work (orders → MAR → medication pass), and is it part of the record or a separate product?
5. What roles exist and how do permissions follow discipline?
6. What rules/constraints matter (record-keeping as legal record, correction/audit, census-driven finance, regulator reporting)?
7. Where is the boundary vs acute EHR, home health, hospice, SNF management, senior living operations?
8. Historical/regional check (§24): does a paper-era nursing home chart fit? Does a UK care-home system without MDS fit?

## Representative Products

| Product | Vendor / positioning | Segment | Why selected |
|---|---|---|---|
| PointClickCare — EHR for Skilled Nursing Facilities | Dedicated LTC/post-acute vendor; describes itself as market-leading ONC-certified post-acute EHR | North America, SNF + senior living + CCRC + pharmacy ecosystem | Market-leading dedicated LTC EHR; deep ecosystem packaging |
| MatrixCare (ResMed) | Multi-setting suite (SNF, senior living, life plan community, home health, hospice, private duty) | North America, mid/large operators | Different philosophy: one EHR across the care continuum; strong pharmacy/interoperability story |
| MEDITECH Expanse (Post-Acute care setting) | Acute-care EHR vendor with long-term care as one care setting | Hospitals/health systems operating LTC, IRF, SNF | Acute-EHR-embedded pole: LTC module inside a hospital EHR |
| Person Centred Software — mCare | UK "Digital Care Planning System / Digital Social Care Record System" | UK care homes (residential + nursing), also AU | Regional pole without US machinery (no MDS, no payer claims) — critical for the historical/regional check |

Dropped during research:
- American HealthTech (healthtech.net) — the domain now redirects to PointClickCare; AHT was absorbed into PointClickCare and has no independent reachable documentation. (Also: ahtech.com is an unrelated Michigan smart-home installer — name collision noted.)
- Epic Long-Term Care — epic.com returned HTTP 403 on the product page; per the source-restriction rule the vendor was abandoned after the failure rather than retried, and the acute-EHR-embedded pole is evidenced by MEDITECH instead.
- WellSky / Netsmart — not fetched; the four-product sample already showed stable cross-product commonality (stop condition reached).

## Sources

All fetched 2026-09-08 (Tier 2 official product pages unless noted):

1. PointClickCare — "EHR for Skilled Nursing Facilities" — https://pointclickcare.com/products/skilled-nursing/
2. PointClickCare — "Electronic Medication Administration Record (eMAR)" — https://pointclickcare.com/products/emar/
3. MatrixCare — "Skilled nursing software" — https://www.matrixcare.com/skilled-nursing-software/
4. MatrixCare — "Interoperability for post-acute and long-term care" (MatrixCare Exchange: Data Manager, QHINs, Direct Secure Messaging) — https://www.matrixcare.com/skilled-nursing-interoperability/ (reached via /products/skilled-nursing/ redirect)
5. MEDITECH — "Post Acute" care setting — https://ehr.meditech.com/ehr-solutions/post-acute
6. Person Centred Software — home page ("Digital care management and software for care homes") — https://personcentredsoftware.com/
7. Person Centred Software — "Digital Care Planning System (mCare)" — https://personcentredsoftware.com/products/digital-care-system
8. https://www.healthtech.net/ — observed redirect to PointClickCare (evidence of AHT absorption; single observation)

Not reachable: PointClickCare help center (login-gated), MatrixCare customer help, Epic product pages (403). Vendor pricing pages not used.

Evidence layers used below: **A** = directly observed on a fetched official page of one product; **B** = observed across multiple representative products; **C** = canonical inference from cross-product comparison and Type-boundary reasoning.

---

## Product Observations

### PointClickCare — EHR for Skilled Nursing Facilities (evidence A)

- Self-description: "secure and fully integrated cloud-based platform" for skilled nursing; "ONC-certified post-acute EHR"; care transitions, care teams, clinical + financial outcomes.
- "Key Functionality" pillars observed verbatim on the product page:
  - **System** — dashboards, robust security (single sign-on, master patient index).
  - **Revenue Cycle Management** — "holistic financial view… billing, accounts receivable, collections and claims"; "secure trust fund management".
  - **Clinical Documentation** — "point of care documentation… capturing care plans accurately… document resident allergies, capture weights, vitals, and allowable ranges… Automate MDS submission to iQIES."
  - **Care Transitions and Operations** — "track resident status throughout their care journey", "resident event calendars, validate insurance coverage, and document incident reports".
  - **Order Management** — "comprehensive mobile-enabled medication and treatment administration system that guarantees real-time accuracy in medication ordering and distribution"; document management/storage/archiving.
- Value packages: Integrated Pharmacy Orders ("real-time electronic exchange of medication ordering" with the pharmacy), Practitioner Engagement, Integrated Lab and Imaging, Nursing Support, Advanced Insights.
- Separate sibling products: EHR for Senior Living; eMAR; QuickMAR (group homes); Pharmacy Connect (for LTC pharmacies); Marketplace (400+ integrations per homepage); developer portal.
- Terminology: resident; med pass; MAR/TAR binders (paper being replaced); POC ("Point of Care" product link).
- eMAR page (A): "mobile-enabled medication and treatment administration system"; "right medication, right dose, right route, right time for the right resident"; barcode administration; resident photographs; "interactive dashboards provide shift supervisors and clinical leadership with immediate visibility to late or missed med passes, with the ability to drill down"; color-coded dashboards organize tasks "by resident and pass time"; "users can clearly see residents or doses that have not been administered"; medication images, interaction warnings, drug information sheets; "automated workflow prompts enforce the capture of supporting documentation including vitals and progress notes"; eMAR "automatically updates pertinent resident information in the EHR"; replaces month-end changeover of paper MAR; **eMAR is part of the EHR for SNFs core package, "not available as a standalone product"**.
- Multi-country footprint (Ontario data point via MEDITECH page, evidence A on MEDITECH's page): Canadian LTC homes on PointClickCare exchange data with hospitals over MEDITECH's Traverse Exchange.

### MatrixCare (ResMed) — Skilled Nursing Software (evidence A)

- Self-description: "comprehensive EHR solution designed to manage the needs of both post-acute and long-term care residents"; "one global EHR solution eliminates the need for multiple systems".
- Observed capabilities: automated data entry ("approve auto-populated fields"); "alerts and audits can help you maintain regulatory compliance"; "clinical dashboards show real-time resident data"; "revenue cycle management tools… boost cash flow and streamline reporting".
- Explicit MDS readiness block: "Support for MDS updates — right at your fingertips… prepared for a new MDS on October 1, 2023" (confirms MDS as a product-maintained regulatory surface).
- Pharmacy: customer quote "MatrixCare implements PCOE without needing changes to a pharmacy workflow… within a matter of just a few days… other eMARs" — confirms pharmacy-coupled eMAR as the standard pattern.
- Quote: "Charting is done electronically as care is given, so staff can spend more time with patients providing the care they need and deserve."
- Modules named: MyAnalytics (census, financial AR, readmissions, quality measures — powered by Azure/Power BI), Clinical Advanced Insights (predictive trends, staffing forecasts), Enterprise Financials.
- Interoperability page (A): MatrixCare Exchange: Data Manager — "imports key patient information directly into the EHR, allows for faster admissions"; "If there are medication orders that remain active on a patient or resident's chart, they are clearly identified. The user can add new orders, make changes to active orders, or continue orders without changes"; automatic cross-check of nationwide health data networks when a patient/resident record is created or updated; QHINs (documents: history & physical, encounter summaries, continuity of care, discharge/transfer summaries); Direct Secure Messaging (referrals; "data import of demographics, medications, allergies, diagnosis"; "attached documents including plan of care, visit notes, orders"; "text and document-based messages can be added to a patient record").
- Language: "patient or resident" used interchangeably across settings; "plan of care" appears as a document class.

### MEDITECH Expanse — Post-Acute care setting (evidence A)

- Self-description: "comprehensive, integrated EHR provides the clinical, administrative, and financial tools to manage the complex needs of patients and residents across different environments, including long-term care, long-term acute care, inpatient rehabilitation, and skilled nursing facilities."
- LTC-specific feature list observed verbatim: "Flexible care plans; Support for MDS and IRF-PAI requirements; Leave of absence management; Split and consolidated billing; Medicare/Medicaid bed certification; Resident financials and allowances."
- Case managers use a Community Care Transition Portal for transitional case management.
- Home Care and Hospice are separate care settings (sibling solutions) — LTC is explicitly its own setting within the same EHR.
- Interoperability data point: "In Ontario, Traverse Exchange is enabling bi-directional data exchange across Canadian hospitals and over 300 long-term care homes using PointClickCare" — independent confirmation that the LTC home's system of record in that ecosystem is the LTC EHR (PCC), exchanging with the acute EHR.

### Person Centred Software — mCare (evidence A, UK regional pole)

- Self-description: "Digital Care Planning System… the UK's most widely used care management system… over 8,000 care providers every day to evidence all aspects of care, from creating and managing person-centred care plans to risk assessments, charts and much more."
- Scale claims: "Over 10M quality care notes logged every day"; "160K residents cared for"; "80K care staff using… every day" (vendor claims, recorded as claims).
- Users named: care home managers, nurses, carers, owners.
- Features observed: **Care Delivery App** ("through a clinical grade hand-held device, carers and nurses can evidence care as it happens during their shift"); **Care Monitoring** ("oversight of critical information covering care plans, risk assessments, daily records and charts, as well as information for audit purposes and inspections"); **Care Planning** ("person-centred care plans meet both the social and medical needs of the people you support"); **Group Reporting** (KPIs for a single home or across a group); **eRed Bag** ("automatically produces a hospital pack for your residents for paramedics and hospital staff"); **GP Connect** ("view your residents GP records from within our Digital Care System").
- Companion eMAR products: ATLAS eMAR ("electronic medicines management system"), Camascope eMAR (acquired 2026); eMAR supports CQC audits/inspections evidence.
- Regulator alignment: CQC ratings/inspections recurring theme; NHS Assured Solution; PRSB; DCB0129; "compliant with the 14 NHS Digital Social Care Record (DSCR) standards".
- Sectors: residential care, nursing homes, retirement living, learning disabilities, mental health support; also Australia localization.
- **No US machinery**: no MDS, no payer claims/RCM, no PDPM anywhere on fetched pages. Daily notes, care plans, risk assessments, charts, eMAR, inspection evidence = the substance.

### Observed redirect (evidence A, single observation)

- healthtech.net (American HealthTech's former domain) now serves the PointClickCare homepage — the dedicated-LTC-EHR market is consolidating around the leading vendor; AHT dropped as a sample product.

---

## Cross-product Comparison

| Structure | PointClickCare | MatrixCare | MEDITECH Expanse (Post-Acute) | PCS mCare (UK) | Layer |
|---|---|---|---|---|---|
| Resident as unit of record (standing, whole-stay) | resident chart; master patient index; "track resident status throughout their care journey" | "post-acute and long-term care residents"; resident/patient record cross-checked at every update | "patients and residents" across LTC/LTACH/IRF/SNF; bed certification | residents; person-centred record for people in the home | B |
| Assessment-driven structure | care plans captured; MDS submission automated to iQIES | MDS update readiness maintained by vendor | "Support for MDS and IRF-PAI requirements"; "Flexible care plans" | risk assessments; observations and charts; person-centred care plans | B |
| Care plan / plan of care as organizing object | "capturing care plans accurately" | plan of care as document class in exchange; resident engagement/care coordination solutions | "Flexible care plans" | "person-centred care plans" are the product's center | B |
| Shift/point-of-care documentation of everyday care | "point of care documentation"; POC product; vitals/weights with allowable ranges | "charting is done electronically as care is given" | Expanse for Nurses (same nursing documentation layer) | "evidence care as it happens during their shift" on hand-held device; 10M notes/day claim | B |
| Medication orders + administration record (eMAR) | eMAR in SNF core package; pharmacy order exchange package; barcode; med-pass dashboards | PCOE/eMAR with pharmacy workflow unchanged; active med orders identified and reconciled at admission | Expanse Pharmacy module under the same EHR (implied by integrated platform; pharmacy listed as solution) | ATLAS/Camascope eMAR companion products | B |
| Census / occupancy / bed-and-stay management | master patient index; resident status; insurance validation | census reporting in MyAnalytics | Medicare/Medicaid bed certification; leave of absence management | less explicit (digital reception; residential context) | B (US pole strongest) |
| Regulatory/compliance evidence machinery | ONC certification; MDS→iQIES automation | "alerts and audits… regulatory compliance"; MDS changes | MDS/IRF-PAI support | CQC inspection evidence; NHS DSCR standards; DCB0129 | B (regime-specific realizations) |
| Billing/RCM tied to census and payer programs | RCM pillar: billing, AR, collections, claims, trust funds | RCM tools; Enterprise Financials | split/consolidated billing; resident financials and allowances | **absent** in fetched material (UK social care) | B-with-exception → not definitional |
| Interoperability with hospital + pharmacy | care transitions; lab/imaging; pharmacy orders; national network products | Exchange Data Manager, QHINs, DSM | Traverse Exchange; transition portal | GP Connect; eRed Bag; NHS integrations | B |
| Incident / safety reporting | incident reports (care transitions & operations) | alerts and audits | (via EHR base) | care monitoring for audits; nursecall messaging | B (thin in one product) |
| Multi-disciplinary content beyond nursing | mealtime solutions; practitioner engagement | nutrition management; resident engagement; ambient sensing | therapies as adjacent solution | wellbeing & activities; dementia care | B |
| AI / predictive analytics | AI workflows; Chart Advisor; Advanced Insights | Clinical Advanced Insights; ambient sensing | Expanse AI (suite-level) | IQ care intelligence | B (current-era, not definitional) |

### Commonalities that survived (candidates for the canonical core)

Across all four sampled products, without exception:

1. A persistent, individually identified **resident record** held by the facility, spanning the person's whole stay, covering medical, functional and social domains.
2. A recurring **assessment → care plan → care delivery → documentation** loop that organizes the facility's work around each resident.
3. **Shift-based documentation of everyday care** (including personal care/ADL-class content) as the way the record grows — not encounter-based charting.
4. A **medication administration record** workflow (orders → scheduled administration rounds → documented administration), realized as integrated eMAR or a tightly coupled companion module.

### Common but not definitional (L1 candidates)

- Census/ADT/bed management; occupancy analytics.
- Regulatory assessment instruments as maintained content (MDS/IRF-PAI in the US; CQC/DSCR alignment in the UK).
- Billing/RCM coupled to census and payer programs (US pole; absent in UK sample).
- Interoperability intake from hospitals/referral sources and pharmacy order exchange.
- Oversight dashboards (late/missed med passes, care monitoring, KPIs), incident reporting, infection prevention, skin/wound.
- Practitioner/provider remote engagement; e-prescribing; lab/imaging exchange.
- Multi-disciplinary modules (therapy, nutrition/dining, activities/wellbeing).

### Variant / optional (L2 candidates)

- Regulatory-regime realization: US (MDS → federal submission, PDPM-era analytics, Medicaid per-diem billing, trust funds) vs UK (DSCR standards, GP Connect, CQC evidence, eRed Bag) vs other jurisdictions.
- Segment packaging: dedicated LTC suite vs multi-setting continuum suite vs LTC module inside an acute EHR.
- Senior living / assisted living packaging with lighter clinical depth (separate SKUs at two sampled vendors).
- Standalone eMAR products for smaller/group-home settings.
- Deployment: cloud SaaS dominant in sample; legacy on-prem in the historical population.

### Vendor-specific (L3 — research notes only)

- PointClickCare: Advisor add-ons (Chart/Billing/Referral), PDPM Coach, Apploi hire/schedule, Mealtime Solutions, trust fund management as package, QuickMAR, Pharmacy Connect for LTC pharmacies, Study Buddy/real-world data products.
- MatrixCare: MyAnalytics (Azure/Power BI), ambient sensing, Exchange Data Manager as a named module, PCOE branding.
- MEDITECH: Traverse Exchange, Community Care Transition Portal, Expanse Genomics integration (suite-level, not LTC-specific).
- PCS: Wellbeing & Activities platform (Oomph), Digital Reception, staff dependency tool, nursecall messaging service, maintenance management, IQ.

---

## Canonical Model (three-layer synthesis)

### L0 — Defining Invariant (deliberately minimal)

A Long-term Care EHR is the facility-held system of record for people who live in a residential long-term care setting. Its defining core is three jointly-held structures:

1. **The resident standing record** — a persistent, individually identified health-and-care record per admitted resident, held by the facility, spanning the entire stay (potentially years), combining medical content (diagnoses, orders, medications, vitals) with functional and social content (personal care, cognition, behavior, preferences). The facility admits, houses and discharges the person; the record is organized around that standing residency, not around episodes of treatment.
   - Remove → an encounter-based clinical system (generic EHR territory).
2. **The assessment → care plan → everyday care loop** — structured assessments of the resident's needs, risks and status feed a care plan that directs and schedules the resident's daily care across disciplines; delivered care is documented back against the plan, and reassessment continues the cycle.
   - Remove → a chart archive / document store; the planned, ongoing, multidisciplinary character of long-term care disappears.
3. **Operational care documentation with a medication administration record** — nursing and care staff record care as delivered, per shift, at the point of care; medication orders flow into a scheduled administration record whose entries (doses given/held/refused) are part of the legal record.
   - Remove → planning documents with no operational record; the daily work of the facility is no longer captured.

Historical check (§24): the paper-era nursing home chart — admission record, physician orders, care plans, ADL flow sheets, daily nursing notes, MAR/TAR binder — satisfies all three structures; 1990s client-server nursing-home systems satisfy; the UK care-home digital social care record (no MDS, no payer claims) satisfies. Conversely the check rejects over-fitting: MDS-specific machinery, PDPM, iQIES submission, ONC certification, cloud delivery, barcode scanning and AI are all realizations, none of them is in the core.

### L1 — Common Mature Structure

- Census/occupancy and stay management (admission, transfer, discharge, bed/room, leave of absence).
- Regulatory assessment instruments maintained as product content (MDS/IRF-PAI in the US; standards-alignment sets in the UK).
- eMAR with safety framing (right drug/dose/route/time/person), med-pass dashboards, barcode/photograph aids.
- Interoperability: referral/hospital intake with reconciliation (demographics, meds, allergies, diagnoses, documents), pharmacy order exchange, lab/imaging results, GP-record access (UK).
- Oversight surfaces: real-time dashboards for late/missed care and med passes, care monitoring, group KPI reporting.
- Billing/RCM coupled to census and payer programs (US pole), including resident financials/trust allowances where the regime requires.
- Practitioner engagement (remote provider order/visit workflows), e-prescribing.
- Incident reporting, infection prevention, skin/wound documentation.
- Multi-disciplinary modules: therapy, nutrition/dining, activities/wellbeing.

### L2 — Variant / Optional

- Regulatory regime (US MDS/PDPM/claims vs UK DSCR/GP Connect/CQC vs other).
- Segment packaging: SNF post-acute short-stay pole vs long-stay custodial pole vs assisted living/senior living pole (lighter clinical, more hospitality/services).
- Platform packaging: dedicated LTC suite vs multi-setting continuum vendor vs module inside an acute EHR.
- Standalone eMAR products; group-home/lighter-settings SKUs.
- Deployment and scale: cloud vs legacy; single home vs large chains (group reporting).

### L3 — Vendor-specific

See Vendor-specific list above (Advisor add-ons, PDPM Coach, ambient sensing, MyAnalytics branding, Traverse Exchange, Oomph, Digital Reception, etc.).

## Boundary Findings

- **vs Electronic Health Record / EHR (acute/ambulatory)**: same family, different organizing principle. An acute EHR is organized around encounters/treatments for episodic illness; the LTC EHR is organized around the resident's standing life in the facility and the daily-care loop. The acute-EHR-embedded realization (MEDITECH) shows the boundary is the care-model objects, not the vendor: when the same EHR serves LTC, it must still carry care plans, resident financials/bed certification, med-pass machinery. **Remove test**: strip the resident-standing-record + care-plan loop + shift care documentation → the product is a generic EHR; add encounters/diagnosis-driven treatment as the primary object → it is an acute EHR.
- **vs Home Health EHR / Management**: home health delivers per-visit care in the person's own home; no facility census/bed context; different assessment instruments (US: OASIS-class) and billing. The resident is not living in the service's premises. Multi-setting vendors (MatrixCare) sell these as separate solutions.
- **vs Hospice Management**: hospice is a program of end-of-life care across settings (IDT, plan of care, bereavement); its system centers on the program/episode of hospice care. Hospice residents inside a nursing home still generate the facility's LTC record; the organizing objects differ.
- **vs Skilled Nursing Facility Management (sibling leaf)**: heavy overlap — US LTC EHR products bundle operational/financial management (RCM, AR, census). The directory keeps both leaves; the defensible seam is: LTC EHR = the clinical record of record for residential care; SNF Management = the facility's operational/administrative bundle (which in the US market is usually the same platform). Recorded as a boundary issue for joint review.
- **vs Senior Living / Assisted Living operations**: assisted-living products emphasize services, wellness coordination, move-in/dining/retail; clinical depth varies. Two sampled vendors package "Senior Living EHR" separately from "SNF EHR". The LTC EHR Type covers the clinical record wherever residency is the context; senior-living operations software without a care record is a different Type.
- **vs Care Plan Management**: care planning is a defining structure *inside* this Type, not a standalone application in this context.
- **Market consolidation note**: the leading dedicated-LTC vendor absorbing another veteran LTC vendor (observed redirect) suggests the dedicated-LTC-EHR population is consolidating but the Type itself remains distinct from acute EHR.

## Uncertainties

1. Tier-1 operational manuals (vendor help centers) were not reachable; the medication-pass and assessment-cycle details below the level of product pages are asserted only at moderate strength (no numeric windows, frequencies or defaults stated anywhere in the final document).
2. Epic's LTC offering could not be verified (HTTP 403); the acute-EHR-embedded pole rests on MEDITECH alone. If Epic's LTC module materially differs (unknown), the pole characterization might need revisiting — risk is low for the Type definition since the pole only tests packaging, not the core.
3. PCS billing absence is evidence of absence on fetched marketing pages only; UK care-home systems may have invoicing integrations not surfaced here. Billing remains L1/L2 (US-common) rather than core either way.
4. MEDITECH's eMAR/pharmacy behavior inside its LTC module was inferred from the integrated-suite description; not directly observed as a dedicated eMAR screen.
5. Senior living / assisted living packaging varies by vendor (separate SKU vs same platform) — kept as a variant; if a future pass on the sibling leaf shows the operational packages dominate, the LTC EHR / SNF Management seam may need the joint review recorded below.

## Final Synthesis

The Long-term Care EHR is best understood as **the resident-centered system of record for facilities where people live and receive ongoing care**. Three jointly-held structures define it: (1) the resident standing record spanning the whole stay and combining medical with functional/social content; (2) the assessment → care plan → everyday care loop that organizes the facility's multidisciplinary work; (3) shift-based operational care documentation including a medication administration record. Everything else — census/bed machinery, regulatory assessment instruments, billing/RCM, interoperability, dashboards, AI — is common mature structure or regime-specific realization. The Type's boundary vs the generic EHR is the care model (standing residency + daily-care loop vs episodic encounter); its boundary vs home health and hospice is the residential-facility context; its boundary vs facility-management software is the clinical record of record.
