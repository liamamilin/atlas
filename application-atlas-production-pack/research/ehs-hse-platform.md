# Research Notes — EHS / HSE Platform

## Research Goal

Understand what an EHS / HSE Platform (Environment, Health & Safety; "HSE" = Health, Safety, Environment — same market, different acronym ordering, common outside North America) actually is as a software Type: what objects it manages, who uses it, how EHS work flows through it, what rules and states matter, and where its boundaries sit against construction safety, environmental point systems, compliance/GRC platforms, sustainability/ESG platforms, and asset/maintenance systems. Produce a vendor-neutral canonical model.

Research date: 2026-09-08.

## Initial Boundary

- **Working hypothesis:** an organization-wide operational system of record for the EHS program — anchored to the operating organization and its sites/facilities — that registers EHS occurrences and findings across domains (safety + environmental at minimum) and runs them through a corrective-action management loop.
- **Likely users:** EHS/HSE managers, safety officers, facility/site managers, employees (reporting, training), contractors, executives.
- **Nearest neighbors:** Environmental Management System (§21 sibling leaf), Environmental Compliance Management / Environmental Incident Management / Hazardous Materials Management / Waste Management Platform (§21 point leaves), Sustainability Management / ESG Reporting (§21), Compliance Management Platform / GRC (§11), Construction Safety Management (§17, joint review recommended by that pass), CMMS/EAM (§16), Employee Wellbeing Platform (§9), Incident Management (§14, IT domain), Environmental Monitoring Platform / CEMS (§21).
- **Unknowns to resolve:** Is multi-domain breadth (safety + environment) definitional or only common? Where does the compliance machinery sit — core or common? Is sustainability an extension or drift into another Type? How does the anchor differ from Construction Safety Management?

## Research Questions

1. What are the core objects (org structure/sites, incidents, findings, actions, inspections, chemicals, permits, training, documents, environmental registers)?
2. What is the defining workflow (capture → investigate → act → close) and which domain loops share the same engine?
3. Which capabilities are definitional vs common vs optional vs vendor-specific?
4. Who are the roles and how do rights differ (EHS manager / supervisor / employee / contractor / executive)?
5. What rules matter (audit trail, action-verification closure, escalation, regional recordkeeping, access control)?
6. Boundary tests vs the neighbors listed above, including the pre-registered joint-review discriminator with Construction Safety Management (anchor: organization-wide operations & facilities vs project/site + multi-employer workforce).

## Representative Products

| Product | Posture | Segment | Documentation used |
|---|---|---|---|
| VelocityEHS | pure-play EHS platform, chemical/SDS heritage (MSDSonline), "Accelerate" connected platform, 8 solution areas | mid-market → enterprise, global | Tier 2 (root + incident-management product page) |
| Cority | enterprise pure-play, occupational-health heritage (Medgate), "CorityOne" converged EHS+ platform (Environmental/Health/Safety/Quality/Sustainability clouds) | large enterprise, high-risk industries | Tier 2 (root + incident-management product page) |
| Quentic | European modular SaaS, EHS + sustainability, explicit "Core + modules" architecture, ISO-management-system positioning, Germany-hosted option | European mid-market → enterprise | Tier 2 (root + core page) |
| Intelex | EHSQ platform (EHS + Quality), broad application library under one platform, Fortive-owned | mid-market → enterprise | Tier 2 (root) |

Boundary probes (used to hold boundaries, not as representatives): SafetyCulture (now surfaced as "Mitti (by SafetyCulture)" — self-described "workplace operations system" for frontline teams; inspection/ops-led, not an EHS program system of record). Attempted but unreachable (source-access limitation): Enablon / Wolters Kluwer (403 ×2), SAP EHS product page (404). The GRC-suite-module pole and the ERP-embedded pole are therefore under-sampled; claims about them are kept general.

## Sources

- VelocityEHS — https://www.ehs.com/ , https://www.ehs.com/solution/safety/incident-management/ [fetched 2026-09-08]
- Cority — https://www.cority.com/ , https://www.cority.com/corityone/incident-management-software/ [fetched 2026-09-08]
- Quentic — https://www.quentic.com/ , https://www.quentic.com/software/quentic-core/ [fetched 2026-09-08]
- Intelex — https://www.intelex.com/ [fetched 2026-09-08]
- SafetyCulture / Mitti (boundary probe) — https://safetyculture.com/ [fetched 2026-09-08]
- Enablon — https://www.wolterskluwer.com/en/solutions/enablon [403], https://www.enablon.com/ [403] — abandoned per network rules
- SAP EHS — https://www.sap.com/products/erp/ehs.html [404] — not sampled

No customer-gated help centers were reachable in this pass; evidence is product/positioning pages (Tier 2). Operational details (exact status names, numeric limits, default values) are NOT carried into the final document.

## Product Observations

### VelocityEHS (evidence layer A per item unless noted)

- Positioning: "one connected EHS platform"; Accelerate platform with **8 solution areas**: Safety, Ergonomics, Chemical Management, Contractor Safety & Permit to Work, Operational Risk, Sustainability, Environmental Compliance, Industrial Hygiene. "24+ EHS products on one centralized and secure platform."
- Safety products: Incident Management, Audits, Inspections, Observations, Compliance Management, **Action Management** ("schedule, assign, and track action items across your entire EHS program, organization-wide"), Safety Meetings, Training & Learning.
- Incident Management: capture "incident, near-miss, and hazard data anywhere, anytime, even offline" via mobile; **QR-code access** "eliminating login barriers"; centralized/standardized incident data **across locations**; reporting & trend analysis with auto-distributed reports; **OSHA Forms 300/300A/301 + ITA export** (US regulatory recordkeeping); AI tools (PSIF insights, description/hazard analyzers, root-cause identifier, corrective-action advisor).
- Environmental Compliance: Air Emissions, Water Quality, Waste Management. Chemical Management: SDS management, chemical inventory, ingredient indexing, GHS secondary labeling, regulatory reporting. Contractor: electronic Permit to Work, Contractor Safety, Visitor Management, Control of Work. Operational Risk: JSA, risk analysis, risk verification/assurance, Management of Change. Industrial Hygiene: IH program management, samples & equipment, medical surveillance, respirator fit test. Sustainability: GHG management, materiality assessments.
- Industries page: manufacturing, chemical, food & beverage, pharma, oil & gas, healthcare, retail, mining, construction, municipalities, transportation, utilities, education, etc.
- Customer quotes emphasize: "pulls multiple EHS functions into one platform… track chemical data, safety documentation, and compliance requirements across multiple locations… dashboards… clear visibility into trends and outstanding actions" (G2 review); "safety program focused on consistency and user participation" (Komatsu).

### Cority (evidence layer A)

- Positioning: "the world's only fully-converged EHS platform" / "CorityOne" — five clouds: **Environmental, Health, Safety, Sustainability, Quality** ("EHS+"). "One platform. One source of truth."
- Incident Management page: "Capture incidents, near misses, and observations in real time… mobile-first, offline access, guided forms"; "Capture and classify incidents with configurable workflows, **severity scoring**, and **standardized data models** to ensure **consistency across sites and teams**"; "**Assign, track, and verify corrective and preventive actions** with automated workflows that ensure accountability and timely resolution"; investigations with "guided methodologies" (root cause); "Maintain complete **audit trails**, regulatory alignment… including alignment with **ISO 45001, ISO 14001, ISO 9001, and OSHA reporting requirements**"; dashboards/trend analysis/CAPA recommendations.
- Platform-wide: Risk Management, Incident Management, Audits & Inspections, Compliance Management, Learning Management, Document Control, Management of Change, myCority Mobile EHS, Reporting & Analytics, Cortex AI.
- Health cloud: occupational health (exams, exposures, worker health), industrial hygiene. Environmental cloud: air emissions, waste, chemicals, water. Safety cloud: permit to work, ergonomics. Quality cloud. Sustainability cloud: carbon/ESG data.
- Industries: high-risk poles (chemicals, construction, manufacturing, mining & metals, oil & gas), regulated (aerospace, automotive, pharma), plus corporate, government, healthcare.

### Quentic (evidence layer A)

- Positioning: "EHS & sustainability: united in one software"; "premier SaaS provider for EHS and sustainability management"; support for ISO 9001 / 14001 / 45001 / 50001 management systems; "software hosted in Germany" (regional posture).
- **Quentic Core** = "the foundation… a software database to which all other Quentic modules are tightly linked". Core features (explicit list):
  - **Corporate structure** — "design your EHS programs… to align with specific company departments, **site units, equipment, and job positions**"; modules connect to this framework.
  - **Document management** — storage, **version control, review and approval**.
  - **Findings management / root-cause analysis** — "managing findings from audits or safety walks… define and allocate responsibilities… thorough root cause analysis."
  - **Action management** — "organize corrective and preventive actions… plan individual action steps, comprehensively monitor progress, and report results."
  - **Escalation management** — "rules for reminder and escalation… automatically notified when deadlines are approaching or action is required."
  - **System administration** — user rights, system settings, master data, custom report templates; access "for different stakeholders based on tasks and purpose."
- Modules: Health & Safety, Occupational Health, Hazardous Chemicals (SDS/chemical management), Risks & Audits, Incidents & Observations, Legal Compliance, Online Instructions (training incl. third-party visitors), Control of Work, Environmental Management ("track resources and costs"), Sustainability (carbon accounting, CSRD, climate disclosure), Processes.
- Use cases: audits & certifications, risk assessments, indicator reporting, **Integrated Management System (ISO compliance)**, SDS management, safety instructions, CSRD support, third-party training.

### Intelex (evidence layer A)

- Positioning: "EHSQ Software Partner"; "The Most Powerful Platform for EHSQ & Sustainability Management"; five solution groups: **Health & Safety, Environment & Sustainability, Quality & Supplier, Risk Management, ESG**.
- Health & Safety applications: Case Management, Claims Management, Action Plan Management, Asset Management, Audit Management, Mobile, Compliance Tracking, Process Hazard Analysis, Root Cause Analysis, Incident Management, Inspection Management, Document Control, Communications Management.
- Environment: ESG Management, **Permit Management**, Compliance Tracking, Inspection, Audit, Document Control, Training Management, Compliance Automation.
- Quality: Supplier, Management of Change, **CAPA (Corrective and Preventive Action)**, Complaints, Nonconformance, Inspection, Audit, Document Control, Training.
- Risk: Near Miss Reporting, Process Hazard Analysis, Operational Risk, Management of Change.
- "Intelex EHS Management System — manage safety, compliance, and sustainability in a single system."
- Incident Management: "manage incidents from incident occurrence to the close out of the final corrective action and beyond."

### SafetyCulture / Mitti (boundary probe, evidence layer A)

- Self-description: "Mitti (by SafetyCulture) — Workplace Operations System"; "The operations system for every site, shift and standard"; "built for frontline teams."
- Feature set: inspections (checklists → workflows), AI issue capture, training, task management, issue reporting, communications, documents, analytics, **asset maintenance, sensors & IoT, contractor management, investigations**.
- Posture: center of gravity is frontline operational execution (checks, tasks, assets) rather than the corporate EHS program of record; no environmental registers (air/water/waste), no chemical/SDS management, no permits visible on the fetched surface. Useful as the "inspection-led adjacent" pole: shares the record→task loop but not the EHS register breadth or compliance machinery.

## Cross-product Comparison

| Structure | VelocityEHS | Cority | Quentic | Intelex | Assessment |
|---|---|---|---|---|---|
| Organization/site anchoring | "standardize incident data across locations" | "consistency across sites and teams", "standardize at scale" | Core "corporate structure": departments, site units, equipment, job positions | platform-wide applications on shared backbone | **Common to all; core candidate (B)** |
| Incident / near-miss / observation register | Incident Management + Observations | incidents, near misses, observations | Incidents & Observations | Incident Management + Near Miss Reporting | **Common to all; core candidate (B)** |
| Corrective/preventive action loop | Action Management, org-wide | "assign, track, and verify CAPA" | Action management + escalation | Action Plan Management + CAPA | **Common to all; core candidate (B)** |
| Investigation / root cause | AI Root Cause Identifier | guided methodologies | root-cause analysis | Root Cause Analysis | **Common to all (B)** |
| Audits & inspections | Audits + Inspections | Audits & Inspections | Risks & Audits | Audit + Inspection Management | **Common to all (B)** |
| Risk assessment | JSA, Risk Analysis | Risk Management | risk assessments | Risk Management + PHA | **Common to all (B)** |
| Compliance machinery | Compliance Management + OSHA forms | compliance + ISO 45001/14001/9001 alignment, audit trails | Legal Compliance module | Compliance Tracking + Permit Management | **Common to all (B); forms differ by region** |
| Document control | SDS library (chemical docs) | Document Control | Document management (version, review/approval) | Document Control | **Common to all (B)** |
| Training / instruction | Training & Learning | Learning Management | Online Instructions (incl. third parties) | Training Management | **Common to all (B)** |
| Permit to work / control of work | Permit to Work + Control of Work | Permit to Work | Control of Work | Permit Management | **Common to all sampled — but industrial-flavored; treated as common, not defining** |
| Chemical management (SDS/inventory) | heritage core | Chemical Management | Hazardous Chemicals | (not surfaced on fetched page) | Common (3/4 observed) |
| Environmental registers (air/water/waste) | Air/Water/Waste | Environmental cloud | Environmental Management (resources & costs) | Permit/compliance tracking under Environment | Common, depth varies (B) |
| Occupational health / IH | IH + medical surveillance | Health cloud (exams, exposures) | Occupational Health | (not surfaced) | Common in enterprise pole (3/4 observed) |
| Contractor / third-party safety | Contractor Safety + Visitor Mgmt | (implied via PtW) | third-party training, Control of Work | (not surfaced) | Common (B) |
| Mobile low-barrier capture | offline + QR no-login | mobile-first, offline | Quentic App | Mobile (online/offline) | **Common in current products (B)** |
| Dashboards / leading-lagging analytics | trend analysis, dashboards | analytics | Quentic Analytics | reporting | **Common (B)** |
| Sustainability / ESG / GHG extension | Sustainability area | Sustainability cloud | Sustainability module | ESG | **Common in 2026 sample but an extension beyond the EHS program core — treated as optional/extension** |
| Management of Change | MOC | MOC | (Processes) | MOC | Common in process-industry pole (3/4 observed) |
| Quality (CAPA/nonconformance) | — | Quality cloud | (Processes mentions quality) | Quality group | Segment-dependent (B) |
| Ergonomics | dedicated area | dedicated | — | — | Vendor-strength-dependent |
| AI assistance | VelocityAI/Vēlo | Cortex AI | Quentin + report assistant | Intelex AI | Era-common (B) |

Key comparative conclusions:

1. **The loop is the engine.** All four products describe the same spine: capture occurrence/finding → classify/investigate (root cause) → corrective/preventive action with owner and due date → track with reminders/escalation → verified closure. Intelex phrases it literally ("from incident occurrence to the close out of the final corrective action").
2. **The anchor is organizational.** All four bind records to corporate/site structure and emphasize cross-site standardization. None anchors to a temporary project.
3. **Multi-domain breadth is structural.** All four span safety AND environmental (and usually health/chemical) under one record system with one anchor and one loop. Single-domain tools exist (SDS-only, inspection-only, safety-only) but the sampled platforms integrate.
4. **Compliance machinery is common but regionally realized.** US OSHA forms (VelocityEHS), ISO management-system alignment (Cority, Quentic), legal registers (Quentic), permit tracking (Intelex). The *machinery* is common; the *regulatory content* is regional.
5. **Sustainability is an extension.** All four ship it, but it rides on the EHS core and is a separate Type in the directory (Sustainability Management Platform). Treat as optional extension, note drift.
6. **Permit-to-work is common in the sampled industrial skew** but is an operational gating capability, not the program spine.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

An EHS / HSE Platform is an **organization-wide operational system of record for the EHS program**, defined by three jointly-held structures:

1. **The organization-wide anchor.** Every record attaches to the operating organization and its standing structure — sites/facilities/locations, organizational units, equipment, job positions, people. Remove → a project-scoped tool (Construction Safety Management anchors to project/site + multi-employer workforce), an asset tool, or a personal tool.
2. **The multi-domain EHS record register.** A persistent register of EHS occurrences and findings spanning more than one EHS domain — health & safety events (injuries, illnesses, near misses), hazards/observations, inspection/audit findings, and environmental program records (releases, waste, emissions, chemicals) — as one integrated record system. Remove → point tools (environmental-only EMS, SDS-only chemical management, inspection-only checklist tools).
3. **The corrective-action management loop.** Occurrences and findings convert into owned, deadline-tracked corrective and preventive actions, investigated for root cause where warranted, escalated when overdue, and closed with verification; the loop is shared across domains. Remove → an incident log or statistics register, not management software.

Jointly-held is load-bearing: (1+2 without 3) = a log; (2+3 without 1) = a generic tracker; (1+3 without 2) = a bare task system.

### L1 — Common Mature Structure

- incident/near-miss/hazard reporting (mobile, offline, low-barrier capture such as QR/no-login entry in current products)
- inspection & audit programs (schedules, checklists/templates, findings)
- risk assessment (JSA, operational risk, process hazard analysis)
- chemical management (SDS library, inventory, GHS labeling)
- permit-to-work / control of work
- compliance machinery: legal/obligation registers, permits, compliance calendars, regulatory recordkeeping support
- document control (versioned policies/SOPs with review/approval)
- training & instruction (assignment, currency tracking, online instruction incl. third parties)
- contractor & visitor safety
- occupational health / industrial hygiene (surveillance, exposures, medical monitoring)
- environmental registers (air, water, waste, resource use)
- dashboards, leading/lagging indicators, cross-site trend analysis
- role model (EHS manager/administrator, site supervisor, employee, contractor, executive) with per-site/per-role rights
- audit trail and attributable records

### L2 — Variant / Optional Structure

- sustainability/ESG/GHG extension (EHS+ / EHSQ convergence, quality modules)
- management of change
- ergonomics programs (dedicated at two sampled vendors)
- AI assistance (era-common: description analysis, root-cause suggestions, report generation)
- ERP-embedded (SAP-style) and GRC-suite-module packaging (under-sampled in this pass — kept general)
- chemical-led vs occupational-health-led vs inspection-led product heritages
- regional regulatory regimes (US OSHA recordkeeping vs EU directives vs ISO-based programs) and regional hosting/data-residency posture
- industry tuning (manufacturing, chemical, oil & gas, mining, construction, healthcare, municipalities, retail/logistics)
- scale packaging (mid-market modular vs enterprise converged suite)

### L3 — Vendor-specific (kept in Research Notes)

- VelocityEHS: Accelerate platform naming, VelocityAI/Vēlo assistant, PSIF insights, 3D SSPP ergonomics, ActiveEHS methodology, QR-code incident entry, OSHA ITA export path, MSDSonline heritage.
- Cority: CorityOne "EHS+" five-cloud architecture, Cortex AI with "human-in-the-loop" framing, Medgate occupational-health lineage, myCority mobile.
- Quentic: "Quentic Core" as named central database, Quentin agent, Germany hosting, explicit ISO 9001/14001/45001/50001 certificate positioning, DQS certificates.
- Intelex: EHSQ naming, application-library packaging (dozens of named apps), Essentials packages, Fortive ownership, free-trial funnel.
- SafetyCulture/Mitti: frontline-operations positioning, 5-star benchmarking, sensors/IoT, insurance offering.

## Boundary Findings

1. **vs Construction Safety Management (§17, processed — joint review discharged here).** Adopted discriminator = anchor. Construction Safety anchors records to construction projects/sites and the multi-employer site workforce (subcontractors, inductions, crews); EHS/HSE Platform anchors to the organization-wide operations and facilities population. General EHS vendors sell to construction customers, but the Type's record system is organization-anchored, not project-anchored. Remove the organization anchor and re-anchor to projects → Construction Safety Management; remove the project anchor here → this Type.
2. **vs Environmental Management System (§21 sibling leaf, unprocessed).** The EMS leaf is the environmental-dominant point (ISO 14001-style environmental program management); EHS/HSE Platform integrates environmental WITH health & safety under one anchor/loop. Proposed discriminator: single-domain environmental program vs integrated multi-domain EHS. Flag for joint review when the EMS leaf is processed (recorded in STATUS.md Boundary Issues).
3. **vs Environmental point leaves (Environmental Incident Management, Hazardous Materials Management, Waste Management Platform, Environmental Monitoring/CEMS, §21).** These are domain point systems; the EHS platform commonly embeds equivalents as modules (all sampled products ship waste/air/water or chemical modules). Discriminator: one integrated multi-domain record system vs single-regime depth. Monitoring/CEMS additionally differs by being measurement/sensor-centric rather than program-record-centric.
4. **vs Compliance Management Platform / GRC (§11).** EHS platform = operational EHS activities (events, findings, actions at sites) with compliance machinery attached; compliance/GRC = enterprise compliance program (obligations, controls, policies, audits across all domains). Quentic's Legal Compliance module and Intelex's Compliance Tracking are the shared surface; remove the operational EHS register and loop → compliance platform. (Consistent with the regulatory-change-management pass: "site-level inspection/audit/permit machinery belongs to EHS systems.")
5. **vs Sustainability Management / ESG Reporting (§21).** Sustainability platforms are metric/disclosure-centric (carbon, frameworks, reports); EHS platforms are occurrence/finding/action-centric. All four sampled EHS platforms extend into sustainability ("EHS+"), but the center of gravity remains the operational record + loop. Center-of-gravity test decides placement.
6. **vs CMMS / EAM (§16).** Asset-maintenance systems center on equipment upkeep; EHS platforms center on people/environmental occurrences and program compliance. Shared surfaces: permit-to-work/LOTO, pre-use equipment checks (Intelex even ships an Asset Management app — drift noted, not definitional). Remove the EHS register/loop and keep assets → CMMS/EAM.
7. **vs Employee Wellbeing Platform (§9).** Wellbeing platforms center on holistic health programs (mental, fitness, engagement); EHS occupational health modules center on exposure surveillance and medical compliance tied to regulatory obligations.
8. **vs Incident Management (§14, IT).** Same word, different world: IT service incidents vs EHS occurrences. No structural relationship beyond the generic case-management shape.
9. **vs inspection-led frontline operations tools (SafetyCulture/Mitti probe).** They share the record→task loop but lack the EHS register breadth (no environmental registers, no chemical/SDS, no permits) and are positioned as workplace operations systems. Center-of-gravity + register-breadth test separates them.

## Historical / Market-Sample Check (§24 analog)

- Would a paper-era corporate EHS program still fit? Yes — a binder-per-site program (incident logs, inspection checklists, training records, permits, MSDS binders, waste manifests) satisfies the three L0 structures without software-era features (dashboards, AI, mobile).
- Regional check: UK/EU "HSE" systems, German Arbeitsschutz/Umwelt programs, Japanese ISO-driven programs — same structures under different regulatory vocabularies. Quentic (Germany-hosted, ISO-positioned) vs VelocityEHS (US OSHA-anchored) demonstrates the regional variation without breaking the core.
- Platform-native check: ERP-embedded EHS (SAP) and GRC-suite modules carry the same core as a module; packaging differs. (Under-sampled — kept general.)
- Occupational-health-led lineage (Medgate → Cority) started health-first and grew the same register/loop — the core survives without environmental depth at the origin, confirming that the loop + anchor are older and more stable than the full domain breadth. (The multi-domain breadth is treated as the platform's identity, with the note that single-domain deployments are point-realizations.)

## Uncertainties

1. Enablon (GRC-suite pole) and SAP (ERP-embedded pole) were unreachable; claims about those packagings are general, not evidence-backed in detail.
2. Exact status models, numeric limits, retention rules, and default configurations were not accessible (no customer-gated help centers); the final document deliberately avoids such precision.
3. Whether single-domain safety-only platforms should be admitted as deployments of this Type or as point Types — resolved pragmatically: the platform Type's identity includes multi-domain integration; safety-only products are treated as point realizations drifting toward their own Types. This could merit joint review if a safety-management-platform leaf is ever carved.
4. Permit-to-work appears in all four sampled products; the sample skews industrial, so "common" (not defining) is the calibrated strength.

## Final Synthesis

The EHS / HSE Platform is the organization-wide operational system of record for the EHS program. Its defining structure is three jointly-held things: the organization/site anchor; the multi-domain EHS record register (health & safety + environmental, with health/chemical/compliance machinery as the common extensions); and the corrective-action management loop with investigation and escalation that turns every occurrence and finding into owned, tracked, verified closure. Around that spine, mature products standardize the classic program machinery — inspections/audits, risk assessment, chemicals/SDS, permits, documents, training, contractors, occupational health, environmental registers — and current products add mobile low-barrier capture, cross-site analytics, AI assistance, and an optional sustainability extension. The anchor is the discriminator vs Construction Safety Management (organization vs project); the register breadth is the discriminator vs environmental/chemical point systems; the operational loop is the discriminator vs compliance/GRC program platforms; the occurrence/action center of gravity is the discriminator vs sustainability metric platforms.
