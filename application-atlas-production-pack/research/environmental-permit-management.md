# Research Notes — Environmental Permit Management

## Research Goal

Understand what Environmental Permit Management software really is: what the managed record is (the permit itself as an object with a lifecycle?), who operates the system (the regulated organization that holds the permits, or the agency that issues them), what the authorization lifecycle looks like inside the software, how permit conditions/limits are handled, and how this Type differs from its nearest neighbors — Environmental Compliance Management (obligation loop), the §24 government Permit Management leaf (agency-side permitting), Environmental Impact Assessment Platform (pre-approval assessment), EHS/HSE Platform, and the media-specific compliance Types.

## Initial Boundary

Working hypothesis at start:

- Core: the regulated organization's (permittee-side) system of record for the environmental permits it holds or seeks — each permit as a persistent record, its authorization lifecycle (application → issuance → amendment → renewal) as tracked work, its conditions/limits kept actionable.
- Nearest neighbors: Environmental Compliance Management (§21, processed 2026-09-08 — its pass flagged the sharpest seam and requested joint review from this side), Environmental Impact Assessment Platform (§21, processed 2026-09-08 — coupling flag), Permit Management (§24, unprocessed — agency-side permitting), Government Licensing Management (§24, processed), EHS/HSE Platform (§21, processed — holds permit tracking as common-not-defining), media-specific compliance Types (wastewater-compliance-management, emissions-monitoring-cems, waste-management-platform — unprocessed), Environmental Monitoring Platform (§21, processed).
- Confusable: permit-to-work / control-of-work (internal safety authorizations, different object), document management, generic project/application trackers, regulatory content services (Enhesa/RegScan-class — suppliers, not the Type).

## Prior-pass obligations this pass must discharge or cross-reference

1. **environmental-compliance-management (§21, processed 2026-09-08)** — flagged "vs environmental-permit-management — sharpest new seam in the environmental family: permit-as-object-lifecycle (application→issuance→amendment→renewal as the managed record) vs obligation-of-record-loop (permits one obligation SOURCE feeding the register; conditions managed as obligations among others); evidence: Intelex ships Permit Management and Compliance Tracking as separately packaged apps, Quentic embeds permit procedures inside its legal-compliance module, Cority lists permits inside the compliance record — products straddle, joint review recommended when that leaf is processed." THIS pass is that leaf's pass — the flag is discharged from this side (see Boundary Findings 1).
2. **environmental-impact-assessment-platform (§21, processed 2026-09-08)** — flagged "Coupling flag for unprocessed sibling environmental-permit-management: the EIA decision instrument frequently bundles or triggers sectoral permits (Chilean RCA; NSW consent) — joint review recommended when that leaf is processed; seam held = assessment of predicted effects + gate vs authorization lifecycle." Discharged from this side (Boundary Findings 2).
3. **ehs-hse-platform (§21, processed 2026-09-08)** — recorded "compliance machinery (legal/obligation registers, permit tracking, statutory recordkeeping)" as standard capabilities NOT definitional for EHS. Consistent: this leaf is where permit machinery is the center. Cross-referenced.
4. **construction-safety-management (§17, processed)** — recorded construction permit-to-work (hot work, confined space) as an internal authorization workflow inside the safety program, explicitly "not a boundary conflict with government permit management (different domain)". This pass adds the environmental-permit contrast (Boundary Findings 8).
5. **government-licensing-management (§24, processed)** — its permit-vs-license test ("a permit authorizes one specific proposed work or event and is consumed by it; a license is a standing, holder-anchored authorization re-determined by renewal") maps imperfectly onto environmental authorizations — noted in Boundary Findings 4 as a nuance for the §24 Permit Management pass.

## Research Questions

1. Who operates the system — the permittee organization or the issuing agency? (The directory carries both §21 Environmental Permit Management and §24 Permit Management; the split must be drawn.)
2. What is the primary record — the permit document, the permit as structured record, the application, or the conditions?
3. What does the authorization lifecycle look like inside the software (application, review, grant, amendment, renewal, expiry) and how much of it is tracked?
4. How are permit conditions/limits handled — held as text, structured, deconstructed into tasks, monitored against thresholds?
5. What renewal/expiry machinery exists (clocks, advance notifications, calendars)?
6. What agency-facing outputs exist (agency-format reports, submittal-ready documents, shared dashboards)?
7. How does the permit record relate to the organization's compliance work (obligations, inspections, monitoring) — same system, sibling modules, or handoff?
8. What packaging shapes exist (standalone product vs suite module vs feature inside media/compliance products)?
9. What separates this Type from environmental compliance management, government permitting, EIA platforms, and permit-to-work?

## Representative Products

Selected for market representation, differing product philosophy, and differing customer tier/region:

| Product | Pole | Tier / segment | Evidence level reached |
|---|---|---|---|
| Intelex (Permit Management application) | standalone named permit-management application inside an EHSQ platform | enterprise/mid, global | Tier-2 (application page) |
| Quentic (Legal Compliance module → Permit procedure) | permit procedures embedded in a legal-compliance module; EU vocabulary | mid-market, EU-centric | Tier-2 (module page + dedicated permit-procedure page) |
| Locus Technologies (Air Quality app; platform "Permit Tracking" feature) | permit compliance inside media/data-led platform apps | enterprise, US | Tier-2 (root + air-quality page) |
| Cority (Environmental Management) | permits inside enterprise multi-site compliance platform | large enterprise, high-risk industry | Tier-2 (environmental page; compliance page via sibling pass same date) |
| VelocityEHS (Environmental Compliance) | permit tracking inside media-specific compliance products (air/water/waste) | mid-market/enterprise | Tier-2 (environmental-compliance page) |

Boundary specimen (not a member of this Type): **Accela Environmental Health** — agency-side civic permitting platform, fetched to anchor the §24 seam.

Deliberately not sampled: Sphera (permit machinery evidenced only indirectly via the compliance pass; its Operational Compliance family is obligation/data-led); Enablon/Benchmark ESG (same suite-module pole); Enhesa/RegScan (content suppliers); agency-side platforms beyond the Accela specimen (Cloudpermit/OpenGov/Tyler — §24 territory). **Domain-recycling hazard recorded:** eraenvironmental.com — historically the domain of an EHS software vendor — now serves a stormwater/erosion consulting firm (Pueblo, CO); the vendor formerly at that domain could not be reached and no claims are made about it.

## Sources

Fetched 2026-09-08 (research date):

- Intelex — https://www.intelex.com/products/applications/permits-management-software/ — Tier-2
- Quentic — https://www.quentic.com/software/legal-compliance/ and https://www.quentic.com/software/legal-compliance/permit-procedure/ — Tier-2
- Locus — https://www.locustec.com/ and https://www.locustec.com/applications/ehs-compliance/air-quality/ — Tier-2
- Cority — https://www.cority.com/products/environmental-management/ — Tier-2
- VelocityEHS — https://www.ehs.com/solution/environmental-compliance/ — Tier-2 (air-emissions page returned an image-only response on first attempt; compliance page used instead)
- Accela (boundary specimen) — https://www.accela.com/solutions/environmental-health/ — Tier-2

Source-access limitations: no authenticated help-center / operational documentation was reachable for any sampled product (all evidence is product/solution-page level). No precise operational parameters (status vocabularies, numeric limits, default reminder windows, exact report formats) are asserted anywhere. The compliance-management pass (same date) independently fetched Intelex's compliance page, Cority's compliance page, Sphera, Quentic, and VelocityEHS — its observations are cross-referenced where marked. One product mismatch rejected: eraenvironmental.com (stormwater consulting firm, domain recycled — see Representative Products note).

## Product Observations

### Intelex — Permit Management application (evidence layer A, Tier-2)

- Positioning: "Intelex Permit Management software streamlines the process of issuing and tracking permits, reducing administrative burden and automating workflows… centralizing data, enabling easy access, monitoring and reporting."
- Headline bullets: "Deconstruct complex permit information into tasks and workflows"; "Stay on top of new and changing regulations with Enhesa and Regscan"; "Track permits to completion with integrated workflows"; "Centralize key permit information across your organization."
- "Permit Management software delivers a centralized, user-friendly database to manage permits, ensure timely renewals and enable better decision-making."
- "Automatic notifications ensure that permit thresholds are never in danger of being crossed."
- "Stay on top of permit renewals, compliance status and overdue tasks with automatic notifications."
- "Compliance reports can be generated into the regulatory agency's format ready for submittal."
- Vendor's own FAQ definition: "Permit management software is a digital solution designed to streamline and automate the management of permits and regulatory compliance within an organization. It helps organizations with the application, review, approval, implementation and renewal of permits."
- Beneficiaries (FAQ): "manufacturing, chemicals, construction, mining, oil and gas, energy and government agencies."
- Configurability (FAQ): "Out-of-the-box forms can be configured to allow for different permit types, approval workflows, compliance tasks and more."
- AI deconstruction: "Using artificial intelligence and machine learning, deconstruct regulations, standards and permits into succinct and accurate checklists, tasks and workflows through our partnership with ehsAI."
- Demo framing: "Help avoid unnecessary shutdowns, fines and reputational damage; Track permits to completion with integrated workflows."
- Placement: Permit Management is listed under the Environmental Management application family (beside ESG Management, Compliance Tracking, Inspection Management, Air Emissions, Water Quality, Waste Management).
- Testimonials: City of Tempe — "Achieved the highest possible confidence in compliance status with regard to all environmental rules, regulations and permits" (a municipal permittee); Campbell's — "extend all our environmental information to all the plant sites… our policies, our training, documents and permits."

### Quentic — Legal Compliance module → Permit procedure (evidence layer A, Tier-2 ×2)

- Module page: "Permits and requirements — When commissioning new facilities or modifying existing ones, you must obtain permits from relevant authorities to ensure occupational safety and environmental protection. With Quentic legal compliance tracking software, you can keep track of all approval procedures and application and inspection processes, successfully organizing the documentation of results and implementation of requirements."
- Module FAQ: "You can handle facility permits along with approval procedures and organize and track required inspections."
- Dedicated permit-procedure page ("Manage permits efficiently"), four capability groups:
  - **Track permits**: "Keep systematic records on pending and approved applications"; "Clarify the legal requirements for each application"; "List contact details for responsible authorities and involve them in the permit process easily."
  - **Design a plan**: "Break your permit processes down into individual phases"; "Log your progress and any necessary follow-ups"; "Check the status of current applications quickly and easily"; "Keep track of the documents that have been submitted and received."
  - **Monitor results**: "Keep an index of permits received"; "Get automatic notifications when a permit is soon to expire"; "Note any special conditions or secondary regulations."
  - **Manage your schedule**: "Plan for regular inspections of your facilities"; "Arrange follow up procedures where necessary"; "Keep track of inspections that have already been completed."
- Reminder management: "Quentic can send you email reminders when important permits are pending or you have a deadline the next day. To ensure that you never miss an application deadline again, plan well into the future and tell Quentic how much advance notice you need."
- Context: permits sit inside the Legal Compliance module beside the legal register, facility/equipment register, technical inspections, and contract management; legal-register updates come from "expert legal databases."

### Locus Technologies — Air Quality app + platform (evidence layer A, Tier-2 ×2)

- Root page: "Need to track Title V permits? There's an app for that." (Air Quality app named as the answer.)
- Air page: "Our clients easily manage emissions inventory and permit compliance programs"; "Manage air emissions inventory and permit compliance programs with Locus emissions management software."
- "Locus streamlines emissions tracking and reporting requirements for various programs, including: GHG, Fenceline, Title V, and LCFS."
- Platform "Popular features within our apps" list includes **"Permit Tracking"** (linked to the Risk & Compliance app).
- Dashboards "share custom dashboards and real-time data with your team or regulators"; reporting streams include Title V monitoring reports and Discharge Monitoring Reports (site-level "I Need Help With…" entries).
- Structure: 30+ purpose-built apps on one platform; air/water/waste/refrigerant apps each carry their compliance machinery; permit tracking is a named platform feature rather than a standalone product.

### Cority — Environmental Management (evidence layer A, Tier-2)

- "Centralized Multi-Site Compliance — Manage permits, inspections, emissions, waste, and corrective actions from one configurable platform designed for regulated global operations."
- Compliance calendaring praised by customer (Koch Industries): "competitively advantaged… when it comes to environmental software and compliance calendaring, offering robust calculations."
- Via the compliance pass (same date, same vendor): the compliance record "centralize[s] permits, obligations, and records for audit readiness"; Regulation Scanning (Enhesa/RegScan/STP content) identifies "applicable regulations, permits, and obligations"; permits appear inside the centralized compliance record rather than as a separately named product.

### VelocityEHS — Environmental Compliance (evidence layer A, Tier-2)

- FAQ: "From monitoring and calculation to **permit tracking** and Title V reporting, the VelocityEHS Environmental Compliance solution scales to your needs."
- "Pre-built forms for regulatory reporting, including Title V, NPDES, RCRA"; "Auto-populate fields in chemical reports, such as TRI/Form R."
- Media products: Air Emissions ("compliance with air emissions standards like Title V requirements"), Water Quality ("built-in workflows for NPDES"), Waste Management ("from shipment manifesting to container tracking").
- Boundary contrast observed on the same site: a separate **"Permit to Work"** product is sold under Contractor Safety (electronic permit-to-work, control of work) — internal work authorizations, a different object from regulatory environmental permits.

### Accela — Environmental Health (boundary specimen, agency-side; evidence layer A, Tier-2)

- "The only end-to-end platform for the entire environmental health lifecycle" — sold to government agencies ("Trusted by 900+ Government agencies").
- Scope: "Food facility inspections, septic permits, complaint investigations, pool and spa oversight."
- "Operators can apply for permits, pay fees, upload documents, and check application status online, any time." — the operator is the *external applicant* on the agency's platform.
- "Configurable workflows route applications and inspections automatically, trigger renewal reminders, and send notifications to operators without manual follow-up."
- Lifecycle graphic: citizen application → staff reviews → permit/license issuance → inspection → renewals. The agency owns the pipeline; the permittee participates through it.

## Cross-product Comparison

| Structure / capability | Intelex | Quentic | Locus | Cority | VelocityEHS | Layer |
|---|---|---|---|---|---|---|
| Permit portfolio held as records (centralized permit information/index) | ✔ "centralize key permit information" | ✔ "index of permits received" | ✔ app for tracking Title V permits | ✔ permits in the platform | ✔ permit tracking | A (5/5) |
| Authorization process tracked (pending applications, phases, documents) | ✔ "application, review, approval… track permits to completion" | ✔ "pending and approved applications", phases, "documents submitted and received" | not directly evidenced | not directly evidenced | not directly evidenced | A (2 direct; 3 weaker) |
| Renewal/expiry clocks + notifications | ✔ "ensure timely renewals", renewal dashboards | ✔ expiry notifications, configurable advance notice | platform notifications (general) | compliance calendaring (sibling pass) | not explicit | A (2–3 direct) |
| Conditions/requirements held on the permit and made actionable | ✔ deconstruct into tasks/workflows; threshold notifications | ✔ "special conditions or secondary regulations"; "implementation of requirements" | ✔ permit compliance tied to emissions tasks/reporting | ✔ permits + corrective actions | ✔ permit tracking with Title V reporting | A (5/5, depth varies) |
| Agency-facing outputs | ✔ "regulatory agency's format ready for submittal" | ✔ authority contacts "involved in the permit process" | ✔ dashboards shared with regulators | ✔ regulator-ready (sibling pass) | ✔ pre-built Title V/NPDES/RCRA forms | A (5/5) |
| Regulatory content feeds | ✔ Enhesa/RegScan | ✔ expert legal databases (register) | not explicit | ✔ Enhesa/RegScan/STP (sibling pass) | not explicit | A (2–3) |
| Permit-linked inspections | sibling Inspection Management app | ✔ "plan for regular inspections… as part of your permits process" | sibling Audits & Inspections app | ✔ permits + inspections | not explicit | A (2 direct) |
| Media machinery adjacency (air/water/waste) | sibling apps | separate Environmental Management module | sibling apps (core of the pole) | Environmental Cloud | media products are the core | A (5/5) |
| AI assistance | ✔ ehsAI deconstruction | suite-level AI | AI claims (general) | ✔ Cortex agents | VelocityAI (general) | A (era-current) |
| Multi-site organization anchoring | ✔ "across your organization" | ✔ sites/facility register | ✔ multi-facility dashboards | ✔ multi-site | ✔ enterprise | A (5/5) |

### What never appears alone

No sampled product ships permit tracking without conditions/obligation linkage; no sampled compliance product omits permits entirely. The permit object and the compliance loop co-occur in every suite — packaging decides which is the centered, named product. The strongest single piece of evidence for the seam: Intelex sells Permit Management and Compliance Tracking as two separately packaged applications over one platform.

### What varies structurally

- Packaging spectrum: standalone named application (Intelex) → dedicated sub-function inside a legal-compliance module (Quentic) → named feature inside platform apps (Locus "Permit Tracking") → unnamed capability inside compliance/media products (Cority, VelocityEHS).
- Lifecycle depth: application-side tracking directly evidenced at Intelex and Quentic; Locus/Cority/VelocityEHS evidence is permit-compliance/reporting-led.
- Media scope: all-media portfolio (Intelex, Quentic) vs air-led (Locus, VelocityEHS Air).
- Regime vocabulary: US program names (Title V, NPDES, RCRA) vs EU approval-procedure vocabulary (Quentic: "approval procedures", authorities, commissioning/modification of facilities).
- Permittee types: industrial enterprises; municipal operators (City of Tempe testimonial at Intelex); the FAQ's beneficiary list includes government agencies (agencies can be permittees for their own facilities).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Environmental Permit Management is the regulated organization's operator-side system of record for the environmental permits it holds or seeks. Remove any of these and it stops being recognizable:

1. **The environmental permit portfolio of record** — a persistent, individually identified record per environmental authorization the organization holds or seeks (air emission permits, discharge permits, waste permits, water withdrawals, operating permits…), carrying the issuing authority, the permitted facility/activity, the permit type, its status, and its key dates. Without it: a document library or a spreadsheet of permits.
2. **The managed authorization lifecycle** — each permit's path (application → authority review → grant/denial → amendment → renewal → expiry/termination) held as tracked work: phased processes, documents submitted and received, deadlines, and renewal/expiry clocks. Without it: a static permit index; without the portfolio, a generic application/project tracker.
3. **The permit's operative conditions kept actionable** — the conditions, limits, and special regulations the permit imposes are recorded on the permit record and connected to the work that keeps the permit valid (tasks/workflows, notifications, permit-linked inspections) and to the outputs the authority expects. Without it: an expiry calendar with no permit substance; without 1+2, an obligation register — the environmental-compliance-management center.

Jointly-held is load-bearing: 1 alone = permit document library; 2 without 1 = generic process tracker; 3 without 1+2 = obligation register (compliance management); 1+2 without 3 = permit expiry calendar; 1+3 without 2 = permit inventory with no authorization work.

Historical/market-sample check: the pre-software environmental manager's permit binder satisfies all three structures — permits filed as records (1), application correspondence files and renewal dates kept per permit (2), condition summary sheets tied to calendar entries and task lists (3) — without content feeds, AI, dashboards, or cloud delivery. 2000s-era permit modules satisfy it without AI deconstruction. The definition survives the historical check; modern machinery (content feeds, AI, dashboards, integrations) is NOT part of the invariant.

### L1 — Common Mature Structure (standard capabilities in mature products)

- Multi-site permit register/inventory with organization hierarchy anchoring.
- Renewal/expiry calendars with configurable advance notifications and reminders.
- Condition/requirement deconstruction into tasks and workflows (increasingly AI-assisted).
- Permit document management: applications, permits, correspondence, documents submitted and received.
- Authority/agency contact records and interaction tracking.
- Threshold notifications tied to permit limits.
- Agency-format report generation and submittal-ready outputs.
- Regulatory content feeds (Enhesa/RegScan-class) keeping requirements current.
- Permit-linked inspection scheduling and follow-ups.
- Dashboards: permit status, renewals due, overdue tasks, compliance standing.
- Audit trail, roles/permissions, multi-site roll-up.
- Integration spine: ERP, historians/emissions systems, monitoring data.

### L2 — Variant / Optional Structure

- Packaging poles: standalone named application vs legal-compliance module vs named feature inside platform apps vs unnamed capability inside media/compliance products.
- Media scope: all-media portfolio vs air-led (Title V) vs water/waste-led.
- Regime packaging: US program vocabulary vs EU approval-procedure vocabulary vs multi-jurisdiction.
- Application-side depth: full application-prep tracking vs tracking only held permits and their renewals.
- Permittee type: industrial enterprises, municipal operators, developers/infrastructure owners; agencies as permittees of their own facilities.
- AI depth: none → content updates → AI deconstruction of permits into checklists.
- Scale: single facility to multi-site global programs.

### L3 — Vendor-specific (research notes only)

- Intelex: ehsAI partnership (AI/ML deconstruction of regulations/standards/permits into checklists); Enhesa/RegScan partnership; "1,400 clients / 3.5M users" claims; City of Tempe / Campbell's / J.D. Irving testimonials; demo framing "avoid unnecessary shutdowns, fines and reputational damage."
- Quentic: reminder phrasing ("tell Quentic how much advance notice you need"); permit procedure positioned for "commissioning new facilities or modifying existing ones"; module sits beside legal register, equipment register, technical inspections, contract management; Berliner Wasserbetriebe quote; AMCS Group ownership.
- Locus: "Need to track Title V permits? There's an app for that" marketing line; 30+ app ecosystem; "Permit Tracking" as a named platform feature under Risk & Compliance; 18,000+ users / 98% renewal claims; Excel two-way sync; SOC 1/2 Type 2.
- Cority: Cortex AI agents; Koch Industries compliance-calendaring quote; CorityOne platform framing; "1,500+ global organizations" claim.
- VelocityEHS: media product names (Air Emissions, Water Quality, Waste Management); hybrid calculation engine; OSIsoft PI interface; separate Permit-to-Work product under Contractor Safety; Accelerate platform naming.

## Vendor-specific Findings

- All evidence is Tier-2 (product/solution pages); no operational parameters asserted anywhere in the final document.
- Intelex is the only sampled product that markets a standalone "Permit Management Software" application; the others realize the machinery as module/feature — the Type is heavily module-realized, which is itself a market-structure finding.
- The regulatory-content layer (Enhesa/RegScan/expert legal databases) is supplied by specialist providers — content supply is a standard capability, not the Type.
- The agency-side environmental permitting market (Accela-class civic platforms) is a different operator of the same lifecycle — recorded as boundary evidence, not Type evidence.

## Boundary Findings

1. **vs Environmental Compliance Management (§21, processed 2026-09-08) — DISCHARGES that pass's joint-review flag from this side.** Verdict: keep both, RATIFIED from this side on the center-of-gravity test. This Type centers the permit as an object with an authorization lifecycle (application → issuance → amendment → renewal as the managed record); environmental compliance management centers the obligation register + conformance loop, where permits are one obligation SOURCE among regulations and conditions are managed as obligations among others. Evidence: Intelex ships Permit Management and Compliance Tracking as separately packaged apps (the permit app centers application/review/approval/renewal; the compliance app centers the regulation→task loop); Quentic embeds permit procedures inside its legal-compliance module as one capability group; Cority, Locus, and VelocityEHS hold permits inside compliance/media products. Products straddle heavily — the market realizes both centers in one estate, and packaging decides which is the named product. Removal tests: remove the obligation register and keep the permit lifecycle → this Type; remove the permit lifecycle and keep the register + conformance loop → compliance management. The compliance pass drew the identical seam from its side; both sides agree.
2. **vs Environmental Impact Assessment Platform (§21, processed 2026-09-08) — DISCHARGES that pass's coupling flag from this side.** Seam held: EIA assesses predicted effects of a proposed project and produces a pre-approval decision/gate; this Type manages the authorization lifecycle of permits that authorize ongoing operations under conditions. The EIA decision instrument frequently bundles or triggers sectoral permits (the EIA pass documented Chilean RCA and NSW consent) — the coupling is real but the centers differ. Removal test: remove the effects-assessment machinery and keep authorizations → this Type.
3. **vs Permit Management (§24, unprocessed) — NEW flag for that pass.** This pass holds §21 Environmental Permit Management on the **permittee-side** reading: the regulated organization manages its own permits. The agency-side permitting market (application intake, review, issuance, inspection, renewal administration over *external applicants'* applications — Accela Environmental Health specimen: "Operators can apply for permits… check application status online" on the agency's platform) belongs to §24 Permit Management. The discriminator is whose permits/applications the system manages (own portfolio vs others' application pipeline), not who the customer is — Intelex's FAQ lists government agencies among beneficiaries, and a municipal permittee (City of Tempe) uses operator-class tooling for its own permits. Two nuances for the §24 pass: (a) environmental operating permits are frequently *standing* authorizations kept alive by renewals (Title V-class), which behaves like the government-license pattern on the permittee side, while construction-phase environmental permits (stormwater) are consumed by the project — the §24 permit-vs-license test maps imperfectly onto environmental authorizations; (b) environmental permitting is a major domain inside government permitting platforms (septic permits, environmental-health permits at Accela) — joint review recommended when §24 Permit Management is processed.
4. **vs Government Licensing Management (§24, processed)** — that pass's permit-vs-license distinction (consumed-by-one-job vs standing holder-anchored authorization) is drawn for government systems; environmental authorizations straddle it (see 3b). No direct overlap with this Type's center; cross-referenced.
5. **vs Government Inspection Management (§24, processed)** — opposite sides of the enforcement relationship: the agency examines; the permittee maintains the permit record that answers inspections. Permit-required inspections interlock the Types; the objects differ.
6. **vs media-specific compliance Types (wastewater-compliance-management, emissions-monitoring-cems, waste-management-platform — §21 siblings, unprocessed; environmental-monitoring-platform — processed)** — permit tracking demonstrably lives inside media-led products (Locus Air: "emissions inventory and permit compliance programs"; VelocityEHS: "from monitoring and calculation to permit tracking and Title V reporting"). Candidate seam: the operational media object/data (discharge point, emission source, waste stream) vs the authorization object (the permit and its lifecycle). Module-convergence specimen recorded; flags left for those passes.
7. **vs EHS/HSE Platform (§21, processed)** — consistent with that pass's holding: permit tracking is common-but-not-defining there; here it is the center. Removal test: remove incidents/occurrences and keep the permit portfolio + lifecycle → this Type.
8. **vs Permit to Work / control of work (contractor-safety family; construction-safety-management §17 processed)** — internal operational authorization of hazardous work (hot work, confined space) vs regulatory environmental authorization from an authority. VelocityEHS sells Permit to Work as a separate product beside its environmental compliance line — the market itself separates the objects. Different Types.
9. **vs Contaminated Site Management (§21, processed)** — remediation activities may require permits; the site record + contamination profile is that Type's center. Cross-reference only.
10. **Naming note** — market vocabulary: "Permit Management Software" (Intelex), "Permit Tracking" (Locus, VelocityEHS), "Permit procedure / approval procedures" (Quentic, EU), unnamed "permits" inside compliance platforms (Cority). One label collision to watch: the bare word "permit management" also names the §24 government Type and the permit-to-work family — all three appear in this research; the directory leaf is held on the environmental permittee-side reading.

## Uncertainties

- No Tier-1 operational documentation reached for any sampled product; all claims are product/solution-page level. Status vocabularies, numeric limits, default reminder windows, and exact report formats are intentionally absent from both documents.
- The lifecycle leg (application-side tracking) is directly evidenced at two products (Intelex, Quentic); Locus/Cority/VelocityEHS permit evidence is compliance/reporting-led — the lifecycle leg is held at full strength only where evidenced and at moderate strength for the data-led pole.
- Whether a standalone pure-play environmental permit product population exists outside EHS suites at scale is untested (search constrained; the one candidate domain was recycled).
- The agency-side environmental permitting market was sampled only through the Accela specimen; its internal structure belongs to the §24 Permit Management pass.
- Sphera's permit-specific machinery was not fetched this pass (evidence via the compliance pass only).
- The exact relationship between permit records and obligation registers inside one deployment (auto-sync vs manual linkage vs parallel records) could not be examined at page level — held as an open integration question.

## Final Synthesis

Environmental Permit Management is the regulated organization's operator-side system of record for its environmental permits. Its defining core is the jointly-held trio of (1) the permit portfolio of record — each environmental authorization held as a persistent identified record with authority, scope, status, and dates; (2) the managed authorization lifecycle — application, authority review, grant, amendment, renewal, and expiry held as tracked work with phases, documents, deadlines, and renewal clocks; and (3) the permit's operative conditions kept actionable — conditions/limits recorded on the permit and connected to tasks, notifications, inspections, and agency-facing outputs. The market realizes the Type across a packaging spectrum — one standalone named application (Intelex), a dedicated permit-procedure function inside a legal-compliance module (Quentic), a named platform feature (Locus), and unnamed capability inside compliance/media products (Cority, VelocityEHS) — with the permit object and the compliance loop co-occurring in every suite. The Type is distinct from environmental compliance management (obligation-loop center), from agency-side government permitting (§24 — external application pipeline), from EIA platforms (pre-approval effects assessment), and from permit-to-work (internal work authorizations); it feeds and is fed by all of them.
