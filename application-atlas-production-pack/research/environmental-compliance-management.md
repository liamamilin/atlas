# Research Notes — Environmental Compliance Management

## Research Goal

Understand what an Environmental Compliance Management application really is: what records it keeps (obligations? permits? tasks? monitoring results?), how obligations enter and stay current, what tracked work it runs, how compliance status is evaluated and evidenced, how nonconformance is handled, and how it differs from the surrounding §21 cluster (EHS/HSE platform, Environmental Management System, Environmental Permit Management, Environmental Monitoring Platform, media-specific compliance leaves, Sustainability/ESG leaves) and from the generic §11 Compliance Management Platform.

## Initial Boundary

Working hypothesis at start:

- Core: a regulated organization's operator-side system of record for its environmental legal obligations — obligations from permits/regulations/consents held as records scoped to sites → tracked compliance work (monitoring, sampling, inspections, calculations, reports, renewals) → evidence-backed compliance status → nonconformance/exceedance handling → regulator/auditor-facing demonstration.
- Nearest neighbors: EHS/HSE Platform (broader, occurrence-centric; processed 2026-09-08 — its pass explicitly held "compliance machinery (legal/obligation registers, permit tracking, statutory recordkeeping)" as common-but-not-defining there), Environmental Management System (ISO 14001-style broader, unprocessed), Environmental Permit Management (permit lifecycle, unprocessed), Environmental Monitoring Platform / CEMS (data acquisition, unprocessed), Compliance Management Platform (§11 generic, processed), Waste/Wastewater compliance leaves (media-specific, unprocessed), Sustainability/ESG (voluntary disclosure, unprocessed).
- Confusable: task management, document management, monitoring data platforms, regulatory content services (Enhesa/RegScan-class — content suppliers, not the Type).

## Prior-pass obligations this pass must discharge or cross-reference

1. **ehs-hse-platform (§21, processed 2026-09-08)** — recorded "compliance machinery (legal/obligation registers, permit tracking, statutory recordkeeping — content regional, machinery common)" as standard capabilities NOT definitional for EHS; no explicit joint-review flag against this leaf, but the seam must be drawn from this side (occurrence register + corrective loop vs obligation register + conformance loop).
2. **compliance-management-platform (§11, processed 2026-09-07)** — its Boundary Findings #9 listed "domain compliance Types (HR/privacy/entity/environmental)" as the domain-instance pattern and (erroneously) marked environmental as processed; this pass supplies the environmental domain instance and confirms the pattern from this side.
3. **contaminated-site-management (§21, processed 2026-09-07)** — site-centered contamination lifecycle; different center (site record + contamination profile), no direct overlap with the obligation loop; cross-referenced only.
4. **carbon-trading-platform (§21, processed)** — venue for carbon instruments; unrelated to the operator-side obligation loop; no action.

## Research Questions

1. What is the primary record — obligation/requirement? permit? task? monitoring result? calculated emission?
2. How do obligations enter the system (regulatory content libraries, permit conditions, custom authoring) and how is applicability determined and kept current?
3. How are obligations organized (by site/facility, by media — air/water/waste, by program)?
4. What does tracked work look like (compliance calendars, tasks/jobs, monitoring schedules, inspections, report cycles, renewals) and how are owners/deadlines handled?
5. How is compliance status evaluated (per-obligation status, exceedance detection, violation/nonconformance tracking) and what evidence backs it?
6. How do corrective actions and enforcement responses flow?
7. What regulator/auditor-facing outputs exist (agency-format reports, audit-ready records, defensible-number traceability)?
8. How do monitoring data and calculations participate (as evidence, as report inputs)?
9. What separates this Type from EHS platform, EMS, permit management, monitoring platforms, and the generic compliance platform?

## Representative Products

Selected for market representation, differing product philosophy, and differing customer tier/region:

| Product | Pole | Tier / segment | Evidence level reached |
|---|---|---|---|
| Cority (CorityOne Compliance Management; Enviance heritage) | enterprise EHS-suite module; obligation register + AI applicability + content providers | large enterprise, high-risk industry | Tier-2 (product/solution pages ×2) |
| Intelex (Compliance Tracking + Permit Management applications) | configurable platform; regulations→jobs→tasks + calendar + applicability reviews | enterprise/mid | Tier-2 (application pages ×2) |
| Sphera (SpheraCloud Environmental Accounting; Operational Compliance family) | data/calculation-led; defensible environmental numbers | enterprise heavy industry | Tier-2 (solution page + FAQ) |
| Quentic (Legal Compliance module) | European mid-market module; legal register + permits + inspections | mid-market, EU-centric | Tier-2 (module page + root) |
| VelocityEHS (Environmental Compliance solution) | media-specific products (air/water/waste) + regulatory report forms | mid-market/enterprise | Tier-2 (solution page + FAQ) |

Deliberately not sampled: Dakota Software (regulatory-content-led pole — dakotasoft.com returned empty responses twice, abandoned per network rules; the content-led pole is evidenced indirectly via the Enhesa/RegScan/STP integrations observed at Cority/Intelex and Quentic's "expert legal databases"); Enablon/Benchmark Gensuite (same suite-module pole as sampled products); Enhesa/RegScan (content suppliers, not the Type); Locus Technologies (already sampled by the contaminated-site pass as an environmental-data-platform candidate — avoided to prevent product mismatch).

## Sources

Fetched 2026-09-08 (research date):

- Cority — https://www.cority.com/products/environmental-management/ and https://www.cority.com/corityone/compliance-management-software/ — Tier-2
- Intelex — https://www.intelex.com/products/applications/compliance-tracking-software/ and https://www.intelex.com/products/applications/permits-management-software/ — Tier-2
- Sphera — https://sphera.com/product-solutions/environmental-compliance/ — Tier-2 (incl. vendor FAQ defining environmental compliance)
- Quentic — https://www.quentic.com/ and https://www.quentic.com/software/legal-compliance/ — Tier-2
- VelocityEHS — https://www.ehs.com/solution/environmental-compliance/ — Tier-2

Source-access limitations: no authenticated help-center / operational documentation was reachable for any sampled product (all evidence is product/solution-page level). No precise operational parameters (task frequencies, status vocabularies, numeric limits, exact report formats, default settings) are asserted anywhere. Vendor-published customer counts and marketing claims are recorded here only, not promoted. Two product mismatches were rejected: eraenvironmental.com (stormwater consulting firm, not the EHS software vendor) and dakotasoftware.com (Adagio accounting developer, not the EHS regulatory-content vendor).

## Product Observations

### Cority — CorityOne Compliance Management (evidence layer A, Tier-2)

- Positioning: "EHS Compliance Management Software for Multi-Site Operations"; Environmental Compliance is the named solution inside the CorityOne EHS+ platform (Environmental Cloud spans air emissions, water, waste, chemical management).
- "See Every Obligation in One Place": centralize regulations, permits, actions, and audit status across every site "so EHS, Operations, and Risk teams work from a single compliance record."
- "Stay Ahead of Regulatory Changes": "dynamic applicability monitoring identifies new requirements early, automatically routing actions to the right people before deadlines."
- "Audit-Ready, Every Day": real-time dashboards and configurable reports "turn compliance data into board ready, regulator-ready, and auditor ready insight."
- Capabilities listed: Regulation Scanning (Cortex AI agents using Enhesa, RegScan, and STP content to "identify applicable regulations, permits, and obligations"); Automated Compliance Actions ("trigger tasks, alerts, and actions… corrective actions, and escalations"); Centralized Compliance Record ("centralize permits, obligations, and records for audit readiness"); Dashboards & Metrics; Scalable & Configurable Design.
- How-it-works triad: identify applicable regulations → automate compliance workflows (task assignments, notifications, corrective actions, escalations) → monitor compliance performance (dashboards, regulatory readiness).
- Customer quote (water utility): "It tracks permits, compliance events, waste shipments, and key info to keep us organized and on top of everything." Environmental page testimonial praises "compliance calendaring" and "robust calculations" with end-user-editable calculations.

### Intelex — Compliance Tracking + Permit Management (evidence layer A, Tier-2)

- Compliance Tracking: "understand, monitor and prove adherence to the multitude of complex and rapidly changing EHS regulatory requirements… whether locally or across the globe."
- Structure: "reducing complex regulations into simple jobs, and then into tasks/subtasks, all to establish accountability"; "manage and share a monthly calendar so everyone is aware of their assigned job/task/subtask deadlines."
- Centralized repository per regulation: "source, domain (air, safety, etc.), applicability status, associated tasks, past audit history, related findings, related CAPAs and other documentation."
- Applicability assessments: "automatically schedule regular applicability reviews to keep regulatory exposure profiles up to date. Attach a requirement to a site, region or any identifier within an organizational hierarchy."
- Automation: "compliance tasks, due dates, renewal dates, job escalations, threshold exceedance warnings."
- Content supply: APIs integrate "leading regulatory content providers including Enhesa or RegScan so you can quickly pull the desired regulatory language into your compliance application."
- Audit dashboards: "person responsible, requirements being audited, findings, CAPAs and overall completion percentage."
- Permit Management (sibling app): "application, review, approval, implementation and renewal of permits"; "deconstruct complex permit information into tasks and workflows"; "automatic notifications… permit thresholds"; "compliance reports can be generated into the regulatory agency's format ready for submittal"; AI/ML deconstruction of "regulations, standards and permits into… checklists, tasks and workflows" via the ehsAI partnership.

### Sphera — SpheraCloud Environmental Accounting (evidence layer A, Tier-2)

- Vendor's own definition: "Environmental compliance is the practice of collecting, validating, calculating and reporting environmental data so a regulated company can defend its license to operate and avoid facility shutdowns."
- Pain framing: scattered data across "site logs, lab systems and ERP platforms"; opaque data lineage; operational changes threatening thresholds; inability to "defend your numbers" to a regulator → "risks losing your license to operate."
- Product: "one governed data source across every site" for air, water, waste and chemical reporting programs (TRI named); "connects the complete TRI workflow to one traceable environmental data foundation."
- TRI mechanics: determine reportability (manufactured/processed/otherwise-used quantities "against chemical-specific thresholds, including contributions from mixtures"); standardize codes centrally; "trace values" — "connects TRI reporting data to governed operational sources, calculations and supporting records, so teams can trace and explain reported values."
- Integration: "connects to the operational systems, historians and enterprise platforms you already run, unifying environmental data into one governed model."
- Compliance-to-sustainability bridge: "Approved environmental data flows into sustainability and reporting workflows, so regulatory filings and public disclosures draw on the same validated numbers."
- Family context: Operational Compliance = Compliance Assurance Software + Regulatory Compliance Software (CyberRegs); Environmental Accounting = Air/GHG Emissions, Refrigerant Compliance, Waste Management, Water Emissions Management.

### Quentic — Legal Compliance module (evidence layer A, Tier-2)

- Positioning: European EHS & sustainability suite; Legal Compliance module = "Minimize your risk of liability by ensuring sustainability and EHS legal certainty"; "demonstrate legally compliant actions at all levels of your organization."
- Legal register: "record and update relevant legal standards and obligations centrally… automated notifications of relevant changes"; "maintain an up-to-date legal register with automated updates from expert legal databases."
- Practical approach: "Make abstract legal provisions manageable, easily identifying specific impacts, duties, and to-dos."
- Facility register: inventory of equipment/machinery per site, shareable reports.
- Permits and requirements: "keep track of all approval procedures and application and inspection processes… organizing the documentation of results and implementation of requirements."
- Inspections and maintenance: "inspection schedule highlights your upcoming appointments… Inspection results that require action are then automatically integrated into your future inspection itinerary."
- Contract management (suppliers/service providers) with renewal/termination reminders — adjacent capability inside the same module.
- Environmental Management is a separate module (resources/costs tracking); ISO 14001/45001 certification support is a suite-level use case.

### VelocityEHS — Environmental Compliance solution (evidence layer A, Tier-2)

- Positioning: "Track your air emissions and wastewater discharges, hazardous and solid wastes, and speed up complex regulatory reporting, all in a single software solution."
- Three media products: Air Emissions ("hybrid calculation engine, emissions mapping, and real-time air monitoring"; Title V-class requirements); Water Quality ("real-time calculations, a library of validated equations, and visibility of every discharge point"; NPDES-class workflows); Waste Management ("from shipment manifesting to container tracking"; RCRA-class; "tracks every waste stream, from generation to disposal").
- Benefits triad: centralize environmental compliance data (calculation engine, emission formulas, data validation); level up internal and external reporting ("pre-built forms for regulatory reporting, including Title V, NPDES, RCRA"; "auto-populate fields in chemical reports, such as TRI/Form R"); share success (KPIs to leadership).
- Integration: OSIsoft PI interface (historian connectivity).
- FAQ: compliance data "turns environmental data into ESG insights"; ISO 14001 alignment named.
- Note: a separate "Compliance Management" product exists under the Safety solution (obligation tracking for safety programs) — the vendor splits compliance machinery by domain.

## Cross-product Comparison

| Structure / capability | Cority | Intelex | Sphera | Quentic | VelocityEHS | Layer |
|---|---|---|---|---|---|---|
| Environmental legal obligations held as records (regulations, permits, requirements) scoped to sites | ✔ "single compliance record" (regulations, permits, obligations) | ✔ centralized repository per regulation w/ applicability status | ✔ governed requirements behind reporting programs (thresholds) | ✔ legal register of "legal standards and obligations" | ✔ permit tracking + media requirements | A (all five) |
| Applicability determination / scoping to sites & activities | ✔ dynamic applicability monitoring | ✔ applicability assessments, scheduled reviews, org-hierarchy attachment | ✔ reportability determination vs thresholds | ✔ "identifying specific impacts, duties" | implicit (media scoping) | A (4 of 5 direct) |
| Tracked compliance work (tasks/jobs, calendar, owners, deadlines, renewals) | ✔ automated compliance actions, tasks, alerts, escalations | ✔ jobs→tasks/subtasks, monthly calendar, due/renewal dates | weak in evidence (report-cycle framing) | ✔ duties/to-dos, inspection schedule, reminders | ✔ compliance tasks framing | A (4 of 5 direct) |
| Evidence of conformance retained against obligations (results, calculations, inspections, audit history) | ✔ audit status + centralized records | ✔ past audit history, findings, documentation per regulation | ✔ traceable values to governed sources | ✔ documentation of results; demonstrate compliance | ✔ calculations, monitoring, validation | A (all five) |
| Compliance status visibility (dashboards, overdue, upcoming) | ✔ real-time dashboards | ✔ dashboards, compliance status, overdue tasks | ✔ visibility into compliance risk | ✔ quick overview, filters | ✔ KPIs, real-time access | A (all five) |
| Nonconformance → corrective action path | ✔ corrective actions, escalations | ✔ findings + related CAPAs | not direct | ✔ inspection results requiring action → future itinerary; action management in Core | not direct | A (3 of 5 direct) |
| Regulator/auditor-facing outputs (agency-format reports, audit-ready records) | ✔ regulator-ready, auditor-ready reports | ✔ reports "into the regulatory agency's format ready for submittal" | ✔ defensible TRI submissions, trace-and-explain | ✔ demonstrate legally compliant actions | ✔ pre-built Title V/NPDES/RCRA/TRI forms | A (all five) |
| Permit tracking as first-class object | ✔ permits in the record | ✔ dedicated Permit Management app | not direct | ✔ permits & requirements (approval procedures) | ✔ permit tracking (Title V) | A (4 of 5 direct) |
| Third-party / expert regulatory content supply | ✔ Enhesa, RegScan, STP | ✔ Enhesa, RegScan (+ ehsAI deconstruction) | in-house regulatory content | ✔ "expert legal databases" + partner network | not explicit | A (4 of 5) |
| Media-specific calculation & data machinery (air/water/waste) | ✔ environmental cloud + "robust calculations" | sibling apps (air/water/waste) exist | ✔ core of the pole (calculations, thresholds) | separate Environmental Management module | ✔ core of the pole (calculation engine, validated equations) | A/B |
| Multi-site organization anchoring (sites/facilities hierarchy) | ✔ every site | ✔ site/region/org hierarchy | ✔ every site | ✔ sites, facility register | ✔ multi-location | A (all five) |
| Integration spine (historians, ERP, lab/monitoring systems) | ✔ ERP/HR/operational integrations | ✔ APIs | ✔ historians, operational systems | ✔ Connect integration layer | ✔ OSIsoft PI | A/B |
| Sustainability/ESG extension | suite-level (Sustainability Cloud) | ESG apps sibling | ✔ same validated numbers flow to disclosures | Sustainability module sibling | ✔ compliance data → ESG insights | A (era-current) |
| AI assistance (regulation scanning, deconstruction) | ✔ Cortex AI agents | ✔ ehsAI deconstruction | not direct | not direct | AI platform claims (general) | A (2 of 5 direct; era-current) |

### What never appears alone

No sampled product ships an obligation register without tracked work and status/evidence machinery; none ships compliance task tracking without an obligation structure behind it. The trio (obligations → tracked work → evidence-backed status) co-occurs in all five — the strongest cross-product signal (layer B).

### What varies structurally

- Center of gravity: obligation-register + task/calendar-led (Cority, Intelex, Quentic) vs environmental-data/calculation/reporting-led (Sphera, VelocityEHS) — two poles of one Type, not two Types (both poles carry obligations + evidence + regulator-facing outputs).
- Regulatory regime packaging: US program-centric (Title V, NPDES, RCRA, TRI named at VelocityEHS/Sphera/Cority) vs EU legal-register/ISO-centric (Quentic: liability, legal certainty, ISO 14001) vs global multi-jurisdiction (Cority/Intelex "locally or across the globe").
- Packaging: EHS-suite module (Cority, Quentic, VelocityEHS) vs configurable multi-app platform (Intelex) vs data-platform solution (Sphera).
- Where media machinery lives: inside the compliance solution (VelocityEHS, Sphera) vs sibling applications/modules (Intelex, Quentic, Cority Environmental Cloud).
- Content supply: third-party providers (Enhesa/RegScan/STP) vs in-house content vs partner legal databases.
- AI depth: applicability scanning and regulation/permit deconstruction into tasks (Cority, Intelex) — era-current.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

An Environmental Compliance Management application is a regulated organization's operator-side system of record for meeting its environmental legal obligations. Remove any of these and it stops being recognizable:

1. **The environmental obligation register** — the requirements the organization has determined it must meet under environmental law (permit conditions, regulations, approval/consent requirements), held as structured records scoped to the organization's sites/facilities/activities, with applicability maintained. Without it: a task manager, a document library, or a monitoring data platform.
2. **Obligation-driven compliance work** — the recurring and event-driven activities the obligations require (monitoring, sampling, inspections, calculations, report preparation, renewals, notifications), scheduled, assigned, and tracked to owners and deadlines. Without it: a static legal register.
3. **Evidence-backed compliance status with a correction path** — per-obligation conformance state maintained from retained evidence (results, calculations, inspection outcomes, submitted reports); exceedances and nonconformances surfaced and driven to corrective action; the record kept demonstrable to regulators and auditors. Without it: a compliance calendar with no compliance judgment, or analytics with no operating record.

Jointly-held is load-bearing: 1 alone = legal register/document library; 2 without 1 = generic task/calendar management; 3 without 1+2 = monitoring/audit analytics; 1+2 without 3 = calendar with no status; 1+3 without 2 = snapshot assessment with no operating loop.

Historical/market-sample check: the pre-software environmental manager's permit binder + compliance calendar + sampling/monitoring logs + violation log + agency correspondence file satisfies all three structures without content libraries, AI, dashboards, or cloud delivery; 2000s-era environmental compliance suites (Enviance-class) satisfy it without AI applicability scanning. The definition survives the historical check; modern machinery (content feeds, AI scanning, calculation engines, ESG bridges) is NOT part of the invariant.

### L1 — Common Mature Structure (standard capabilities in mature products)

- Regulatory content supply: third-party legal/regulatory databases (Enhesa/RegScan/STP-class) or in-house expert content feeding the register, with change notifications.
- Applicability machinery: site/region/org-hierarchy scoping of requirements; scheduled applicability reviews; increasingly AI-assisted regulation scanning and deconstruction of regulations/permits into tasks.
- Permit tracking as a first-class object: permit inventory, conditions, renewal clocks, threshold notifications.
- Compliance calendar / recurring task generation with reminders, escalations, and overdue visibility.
- Media-specific data & calculation machinery (air emissions, water discharges, waste streams) producing the numbers that evidence conformance and feed reports.
- Regulatory report generation, including agency-format forms and reportability/threshold determinations.
- Audit/inspection support: audit history per requirement, findings, inspection schedules with results feeding future itineraries.
- Corrective action / CAPA linkage for findings and exceedances.
- Dashboards: compliance status, upcoming deadlines, overdue tasks, exceedance warnings; multi-site roll-up.
- Multi-site organization anchoring, roles/permissions, audit trail.
- Integration spine: historians/PI, ERP, lab/monitoring systems, APIs.
- Management-system alignment (ISO 14001-class) and sustainability/ESG data bridges.

### L2 — Variant / Optional Structure

- Center-of-gravity poles: obligation-register/task-led vs environmental-data/calculation/reporting-led.
- Regulatory regime packaging: US program-centric vs EU legal-register/ISO-centric vs global multi-jurisdiction.
- Packaging: EHS-suite module vs configurable multi-app platform vs standalone environmental suite vs data-platform solution.
- Content monetization: third-party content subscriptions vs in-house content vs partner networks.
- AI depth: none → content updates → AI applicability scanning/deconstruction.
- Scale: single-facility vs multi-site enterprise; regional hosting postures.
- Sustainability/ESG extension depth (data bridge vs full ESG suite adjacency) — drift boundary vs Sustainability Management Type.

### L3 — Vendor-specific (research notes only)

- Cority: Cortex AI agents; "Compliance Permit Analysis Agent"; Enhesa/RegScan/STP content; Koch Industries compliance-calendaring testimonial; Central Arizona Project quote; CorityOne Environmental/Health/Safety/Sustainability/Quality cloud split.
- Intelex: ehsAI partnership (AI/ML deconstruction of regulations/permits into checklists); Enhesa/RegScan APIs; City of Tempe/RIT/Virgin Atlantic testimonials; "1,400 clients / 3.5M users" claims; Compliance Tracking vs Permit Management as separately packaged apps.
- Sphera: SpheraCloud Environmental Accounting; CyberRegs; TRI-specific machinery (manufactured/processed/otherwise-used thresholds, mixtures contributions, code standardization); "defend your license to operate" framing; Wolters Kluwer ownership.
- Quentic: Legal Compliance module spanning occupational-safety AND environmental law; facility register and contract management inside the module; Berliner Wasserbetriebe quote; AMCS Group ownership; German hosting posture; "1,200 customers" claim.
- VelocityEHS: hybrid calculation engine; OSIsoft PI interface; pre-built Title V/NPDES/RCRA/TRI Form R forms; separate Safety-side Compliance Management product; "15K customers / 10M users" claims.

## Vendor-specific Findings

- All evidence is Tier-2 (product/solution pages); no operational parameters asserted anywhere in the final document.
- The two poles (register-led vs data-led) are both directly evidenced; the register-led pole is the richer documented (Cority/Intelex/Quentic), the data-led pole is sharply articulated by Sphera's own FAQ definition and VelocityEHS's media products.
- The regulatory-content layer (Enhesa/RegScan/STP/expert legal databases) is supplied by specialist providers in most products — content supply is a standard capability, not the Type itself.

## Boundary Findings

1. **vs EHS/HSE Platform (§21, processed 2026-09-08)** — Verdict: keep both. EHS platform's defining core is the organization-wide multi-domain occurrence register (incidents, near misses, hazards, observations, findings) + shared corrective-action loop; this Type's defining core is the obligation register + conformance loop. The EHS pass itself held "compliance machinery (legal/obligation registers, permit tracking, statutory recordkeeping)" as common-but-not-defining there — this leaf is where that machinery is the center. Removal tests: remove occurrences/incidents → environmental compliance management; remove the obligation register → EHS platform. Shared surfaces (inspections, corrective actions, training) are integration points, not collapses.
2. **vs Compliance Management Platform (§11, processed)** — Confirms the generic pass's domain-instance pattern from this side: the generic Type runs a domain-agnostic obligations→work→evidence loop on framework/regulation templates; the environmental instance carries the environmental domain object model (permits and consent conditions as obligation sources, media limits, emissions/discharge/waste calculations, monitoring evidence, agency-format reports, regulator-facing demonstration). Keep both; same reading as financial/HR/privacy/entity compliance.
3. **vs Environmental Permit Management (§21 sibling, unprocessed)** — Sharpest new seam. Candidate discriminator: permit-as-object-lifecycle (application → issuance → amendment → renewal is the managed record) vs obligation-of-record-loop (permits are one obligation SOURCE; the register + conformance loop is the center). Evidence from this side: Intelex ships Permit Management and Compliance Tracking as separate apps (permit app centers application/review/approval/renewal; compliance app centers the regulation→task loop); Quentic holds permit procedures inside the legal-compliance module as one register section; Cority lists permits inside the compliance record. Products straddle; joint review recommended when that leaf is processed.
4. **vs Environmental Monitoring Platform / Emissions Monitoring (CEMS) / Air & Water Monitoring (§21 siblings, unprocessed)** — Monitoring Types center data acquisition/validation/analysis from sensors and samples; here monitoring results enter as evidence of conformance against limits and as report inputs. Removal test: remove the obligation register and status loop → monitoring platform. Integration spine (historians, PI-class feeds) is the documented meeting point (Sphera, VelocityEHS).
5. **vs Environmental Management System (§21 sibling, unprocessed)** — EHS pass already flagged joint review. From this side: the ISO 14001-style management system centers the broader environmental management cycle (policy, aspects/impacts, objectives, operational control, management review) with "evaluation of compliance" as one clause; this Type centers the legal-obligation loop itself. Candidate seam: management-system cycle vs obligation-conformance loop; compliance management is typically a component inside EMS-supporting suites (Quentic sells both modules). Joint review recommended.
6. **vs Waste Management Platform / Hazardous Waste Management / Wastewater Compliance Management (§21 siblings, unprocessed)** — Media-specific operational Types center the operational object (waste stream/manifest/container; discharge point). In this sample, media machinery appears as products/modules inside environmental compliance solutions (VelocityEHS Waste Management product; Sphera Waste Management software) — overlap specimen. Candidate seam: operational media object vs obligation register; the compliance Type aggregates across media. Flag for those passes.
7. **vs Sustainability Management / ESG Reporting / GHG Accounting (§21 siblings, unprocessed)** — Voluntary disclosure frameworks vs regulatory obligations; the bridge is documented (Sphera: "regulatory filings and public disclosures draw on the same validated numbers"; VelocityEHS FAQ) — extension, not core. Center-of-gravity test decides placement.
8. **vs Regulatory Change Management (§11, processed)** — RCM centers the change event; this Type centers the standing register the changes feed. In this sample change arrives via content-provider updates + applicability reviews (Intelex scheduled reviews; Cority dynamic applicability monitoring; Quentic automated legal-database updates) — consistent with the RCM pass's seam; no separate RCM module observed in this sample.
9. **vs Government Inspection Management (§24, processed)** — Opposite sides of the enforcement relationship: the agency examines; the regulated organization maintains the record that answers inspections. The audit-ready posture (Cority "auditor ready"; Intelex audit history) is this Type's response surface, not a government register.
10. **Naming note** — Market labels overlap: "Environmental Compliance" (VelocityEHS, Sphera), "EHS Compliance Management" (Cority), "Legal Compliance" for EHS+environmental law (Quentic), "Compliance Tracking" (Intelex). One label collision to watch: Cority's module is named "Compliance Management" — same name as the §11 generic leaf; packaging naming, not taxonomy.

## Uncertainties

- No Tier-1 operational documentation reached for any sampled product; all claims are product/solution-page level. Status vocabularies, task frequencies, numeric limits, and exact report formats are intentionally absent from both documents.
- Sphera's task/calendar machinery is weakly evidenced (its pole is data/calculation-led); the L0 "tracked work" leg is held from the four other products plus Sphera's report-cycle framing at reduced strength.
- VelocityEHS's obligation-register depth is not directly evidenced (its environmental page emphasizes media data/reporting; its obligation-tracking product sits under Safety) — its register leg is held at moderate strength.
- Quentic's register spans occupational safety AND environmental law; the environmental-only split inside the module could not be examined — held as module-level evidence.
- The regulatory-content-led pure-play pole (Dakota Software-class) was not directly sampled (domain unreachable); its existence is evidenced indirectly via the content-provider integrations at four sampled products.
- Whether a standalone (non-EHS-suite) environmental compliance product population exists at scale is untested; the sampled market delivers overwhelmingly as suite modules/platform solutions.

## Final Synthesis

Environmental Compliance Management is the environmental-domain instance of the compliance-management pattern: a regulated organization's operator-side system of record whose defining core is the jointly-held trio of (1) the environmental obligation register — permits, regulations, and consent requirements held as site-scoped records with maintained applicability, (2) obligation-driven compliance work — the monitoring, sampling, inspection, calculation, reporting, and renewal activities the obligations require, tracked to owners and deadlines, and (3) evidence-backed compliance status with a correction path — retained evidence per obligation, surfaced exceedances/nonconformances driven to corrective action, and a record kept demonstrable to regulators and auditors. Mature products add regulatory content feeds, applicability machinery (increasingly AI-assisted), permit tracking, compliance calendars, media-specific calculation engines, agency-format report generation, audit support, and integration spines into historians/ERP/monitoring systems. The market splits into an obligation-register/task-led pole and an environmental-data/calculation/reporting-led pole — two centers of gravity of one Type, not two Types. Delivery is overwhelmingly as a module of an EHS/EHS&S suite or platform, with the permit, monitoring, media, and EMS leaves holding as separate Types around it.
