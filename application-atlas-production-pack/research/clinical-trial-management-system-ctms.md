# Research Notes — Clinical Trial Management System / CTMS

## Research Goal

Understand, from real products, what a CTMS actually is and how it works: the core objects, the operational workflow of a managed clinical trial, the roles, the rules, and the boundaries against EDC / eTMF / IRT-RTSM / recruitment / site-management siblings.

## Initial Boundary (hypothesis before research)

- CTMS = the operational management system for running clinical trials (study setup → site activation → enrollment/conduct → monitoring → closeout), distinct from:
  - EDC (electronic capture of clinical/subject data per protocol)
  - eTMF (regulatory trial document archive)
  - IRT/RTSM (randomization and trial-supply logistics)
  - Clinical Trial Recruitment Platform (recruitment-first machinery)
  - Clinical Trial Site Management (separate directory leaf — boundary to verify)
- Suspected core objects: Study, Site, Investigator/Personnel, Subject, Visit, Milestone, Monitoring visit, Budget/Payment, Document/Report, Deviation.

## Research Questions

1. What is the central object — the study? how is it structured (protocol, sites, calendar)?
2. How are sites and study personnel managed and tracked through activation?
3. How is participant/subject operational tracking handled (screening, enrollment, visits, windows)?
4. How does sponsor-side monitoring (CRA visits, reports, findings, action items) work in the system?
5. How do budgets, milestone payments, expenses, and site/institution billing work?
6. What compliance surfaces exist (deviations, IRB notifications, billing compliance, audit trails, approvals)?
7. What integrations define the CTMS's position in the eClinical stack (EDC, eTMF, RTSM, EMR/EHR, IRB systems)?
8. How do sponsor/CRO-centric and site/institution-centric CTMS differ, and do they share one model?
9. What does the system look like day-to-day (dashboards, trackers, logs, reports)?

## Representative Products

| Product | Vendor | Operational pole | Customer tier | Notes |
|---|---|---|---|---|
| RealTime-CTMS | RealTime eClinical Solutions | Site / site network / SMO / AMC (also sells to sponsors/CROs) | SMB–mid + enterprise network edition | Standalone site-business CTMS; bundled suite (SOMS) |
| OnCore | Advarra (ex-Forte Research) | Academic medical centers / cancer centers / institutions | Enterprise institutional | "Enterprise CTMS for academic medical centers and research institutions" |
| Clinical Conductor | Advarra | Research sites, site networks, hospitals, health systems | Mid | Site-business CTMS with financial focus |
| Clinion CTMS | Clinion | Sponsor / CRO | Mid enterprise | Suite-integrated (EDC/RTSM/eTMF/eSource/eConsent/ePRO) |

Attempted but unreachable (abandoned per network rules): Veeva Vault CTMS (transport ×2), Medidata CTMS (404 ×2), Oracle Clinical One (404 ×2), Castor CTMS pages (404 + transport). Enterprise-suite pole is covered by Clinion; deep user-manual-level evidence for the largest vendor suites is missing — see Source-access Limitation.

## Sources

All fetched 2026-09-07.

- RealTime eClinical — homepage (https://realtime-eclinical.com/) and CTMS solution page (https://realtime-eclinical.com/solutions/ctms/)
- Advarra — homepage (https://www.advarra.com/), OnCore CTMS page (https://www.advarra.com/solutions/sites/ctms/oncore/), Clinical Conductor CTMS page (https://www.advarra.com/solutions/sites/ctms/clinical-conductor/)
- Clinion — homepage (https://www.clinion.com/) and CTMS product page (https://www.clinion.com/clinical-trial-management-system/), incl. product screenshots (CTMS dashboard, milestone tracker, deviation report, reports & letters workflow, invoices, workflow configuration)

Evidence layers: A = directly observed on the fetched page for that product; B = cross-product commonality across the sample; C = canonical inference from comparison + boundary reasoning.

## Product A — RealTime-CTMS (site pole)

Key observations (A-layer unless noted):

- Vendor self-describes the platform as serving "clinical research sites, site networks, academic medical centers, sponsors, and CROs"; CTMS is one module of a wider "Site Operations Management System (SOMS)" bundle that includes eSource, eReg/eISF (regulatory documents), participant portal/eConsent, payments (SitePay/GlobalPay), texting, mobile app.
- CTMS marketing pillars (CTMS page):
  - **Recruitment**: grow a patient database (website/Facebook ads/SubjectWell integrations), website integration to list enrolling studies, landing pages, pre-screening; "Instant CTMS sync creates subject profiles automatically from website form submissions"; remarketing via email/SMS campaigns.
  - **Visit / CRC management**: "View upcoming visits, overdue visits, and pending actions"; "Track patient visits … electronic log for a comprehensive overview of visit statuses"; "automated study target dates and window calculations, text reminders, and Outlook integration"; alerts/notifications for tasks and follow-ups; reporting incl. "study enrollment metrics, prescreening logs, visit tracking logs, staff productivity."
  - **Study finances**: "Manage contracts and budgets with study procurement milestone tracking, complete accounting for both simple and complex study budgets, automated screen fail ratio and max tracking, as well as study milestone payment tracking"; "automated processes for earnings, expenses, receivables, and payables at both visit and study levels"; custom report builder ("inSites").
  - **Enterprise CTMS**: centralize accounting/recruitment/reporting across "large site networks, hospitals, and university systems"; centrally manage "an unlimited number of sites, studies, personnel, finances, and reporting in over 30 countries"; aggregate reporting with BI connectivity; unlimited user profiles; MFA + SAML; quick-launch into per-site study areas; network-wide enrollment progress with drill-down to site level.
- Positioning line: "RealTime-CTMS is the foundational solution for our eClinical platform … purpose-built to empower clinical research sites to streamline all aspects of trial execution, including recruitment, CRC activities, finances, site management, and more."
- Metrics claims (vendor-published, treat as claims only): 3000+ sites, 600,000+ patient visits/year, 14 hours saved per study activation, 5× faster inspection readiness, 75% reduction in monitoring visit costs.

## Product B — OnCore (institutional/academic pole)

Key observations:

- Positioning: "Clinical Trial Management System (CTMS)" — "the industry's most adopted clinical trial management system, built in collaboration with leading academic medical centers and cancer centers"; "Enterprise CTMS for academic medical centers and research institutions"; FAQ: fits institutions conducting "fifty to 500+ active trials."
- Value pillars:
  - "Ensure compliant billing processes — centralize billing information … improve budgeting, and simplify routing across teams and systems."
  - "Boost research operations management — gain visibility and financial oversight into all areas of clinical research using a standardized system."
  - "Automate information between systems — seamlessly integrate OnCore with your electronic medical record (EMR) system, such as Epic or Cerner, to increase patient safety, billing compliance, and operational efficiency."
  - "Better manage protocol timelines — **oversee the entire study lifecycle from protocol setup and activation to subject screening, registration, and study close-out**."
  - "Reporting and analytics for insight — comprehensive dashboards … co-developed with Advarra's Onsemble customer community."
- Connected ecosystem (integration list): CRPC Billing Grid (EMR), Demographics (EMR), Subject/Protocol Information (EMR), General ledger, eIRB (via OnCore API), Advarra eReg, Advarra eSource, Advarra Analytics, Advarra Payments.
- FAQ reveals module structure: "An enterprise OnCore license includes clinical research management, billing compliance, and numerous integrations. Additional modules such as biospecimen management are licensed separately."
- Case-study framing: revenue recovery and cost reduction for UCSF; billing-compliance emphasis ("The interface between OnCore and Epic has put us in a much better place in terms of billing compliance" — Yale).
- Community: Onsemble — user community co-shaping dashboards/analytics.

## Product C — Clinical Conductor (site-network/health-system pole)

Key observations:

- Positioning: "A scalable CTMS designed to optimize operational and financial efficiency for research sites, site networks, hospitals, and health systems."
- Value pillars:
  - "Boost profitability — run your research as a business with budgeting, billing, and reporting tools designed specifically for clinical research sites."
  - "Enhance visibility — advanced reporting and analytics … optimize operational workflows, and gain visibility into finances."
  - "Streamline enrollment — patient recruitment and enrollment tools … track progress in detail."
  - "Improve participant engagement — add-on modules to … reduce no-shows" (CCText two-way HIPAA-compliant texting; CCPay real-time participant stipend reimbursements to debit cards "issued and tracked in Clinical Conductor").
  - "Connect your technology and EHR — integrate with Advarra's eReg and eSource, use Clinical Conductor's APIs, and integrate with Epic."
- Dashboards with commentary "throughout the life of a study, which is especially helpful with audits" (customer quote); "real-time visibility into patient journeys across all sites, along with real-time financial projections and compliance monitoring"; "view complete patient lists, and manage appointments and stipends from a single screen."
- Case-study framing: recovering unbilled study payments (Ascension) — the CTMS as the financial-reconciliation system for site business.
- Companion products eReg (21 CFR Part 11 regulatory document management) and eSource+EDC are sold separately and integrated — boundary evidence that document management and data capture are NOT part of the CTMS core.

## Product D — Clinion CTMS (sponsor/CRO pole)

Key observations (incl. screenshots):

- Positioning: "Centralize study management — track milestones, monitor sites, and manage budgets in one integrated system"; "Gain complete trial oversight with a centralized CTMS that unifies project tracking, monitoring, and financials. Integrated with EDC and RTSM, it delivers real-time visibility and operational clarity for CROs and sponsors." FAQ: "Sponsors, CROs, study managers, and site coordinators managing multi-site trials, timelines, or budgets all benefit from a CTMS."
- Dashboard screenshot (A): panels for **Study Information** (study name, protocol ID, site count), **Protocol Deviations** (per study/site/location with deviation counts), **Upcoming Visits** (visit type — "Pre-Site Selection Visit", "Interim Monitoring Visit", "Site Closeout Visit" — with dates and assigned CRA), **IP Status** (total investigational product, IP issued to sites, balance).
- **Protocol Deviation module**: "Systematically identify, document, and manage all protocol deviations in a centralized log." Standardized capture form: deviation level (Site, Subject, or Visit), Major/Minor classification, predefined categories (e.g., Informed Consent, IMP Related), corrective (CA) and preventive (PA) actions, IRB notification dates. Centralized tracking dashboard with filters (PD ID, title, date, classification, category); automated email notifications for submission/review/sign-off to CRC, CRA, PM, and Investigator.
- **Study Milestones**: "complete, end-to-end view of your entire study timeline, from the trial initiation to final database lock"; real-time planned-vs-actual comparison; flag deviations from the study plan.
- **Reports & Letters**: post-visit documentation workflow — system prompts the CRA/PM-CSM to produce the Confirmation Letter, Thank You Letter, Non-Selection of Investigational Sites Letter, Activation Letter, Follow-up Letter, and Monitoring Report "within a mandatory timeline"; report auto-routed to approval levels (L2), approver can approve / comment / revert; configurable multi-level workflows (L1 to L5); templates; supporting-document attachment; action items tracked to closure; time-stamped audit trail.
- **Action Items**: CRAs add action items during visits with priorities and due dates, assign owners; pending tasks carry forward into future reports until closed; unique IDs; dashboards show task status across sites.
- **Financial management**: milestone-based invoicing — "Once the milestone is marked as achieved, the CTMS will automatically trigger an email and allow the Project Manager to raise invoices for achieved milestones from professional costs"; expense management for site personnel (PIs, CRCs) and external vendors with configurable approval hierarchy and resubmission loop; "audit-ready financial records — complete, immutable, time-stamped financial history."
- **System administration & configuration**: study admins define master data, financial entities (sponsors/vendors, tax, invoice formatting), five-level approval hierarchies for milestones/reports/deviations/expenses/monitoring plans, configurable notifications ("100+ automated notifications and reminders" — vendor claim), study calendar (weekends, holidays) for scheduling.
- **Integration**: native EDC/RTSM/eTMF + third-party EDC/RTSM/eTMF connectivity; "all clinical, operational, and regulatory data flows into one unified platform."
- Compliance posture: 21 CFR Part 11 / Annex 11 / ISO 27001 badges (era-common for the category).

## Cross-product Comparison

| Structure / capability | RealTime | OnCore | Clinical Conductor | Clinion | Layer |
|---|---|---|---|---|---|
| Study/protocol as central identified object | A | A ("protocol setup…activation…close-out") | A | A (Study Information/protocol ID) | L0 (C: canonical) |
| Site network + study personnel as managed population | A (sites, personnel, enterprise roll-up) | A (institution, teams, routing) | A (sites, networks, staff) | A (sites, CRA assignment, staff) | L0 |
| Protocol-anchored operational events tracked vs plan (milestones, visit calendar, target dates/windows) | A (target dates, window calculations) | A (protocol timelines; lifecycle) | A (appointments, study dashboards) | A (milestones planned-vs-actual; visit types) | L0 |
| Recorded operational conduct history (auditable) | B (reporting, inspection readiness) | B | A (dashboards w/ commentary for audits) | A (time-stamped audit trails) | L0 |
| Subject/participant operational tracking (screening→enrollment→visits) | A (visit logs, subject profiles, visit statuses) | A (subject screening, registration) | A (patient lists, appointments, patient journeys) | A (dashboard subject count; deviations at subject/visit level) | L1 (near-universal; depth varies by pole) |
| Budget & payment machinery (budgets, milestone payments/invoicing, expenses, receivables/payables) | A | A (billing compliance, financial management, Advarra Payments) | A (budgeting/billing, unbilled recovery, stipends) | A (milestone invoicing, expenses, financial entities) | L1 (present in all 4; not definitional) |
| Monitoring-visit machinery (CRA visits, reports/letters, findings, action items) | C (site pole sees visits; monitoring-cost claim) | C (not directly observed) | C (not directly observed) | A (monitoring visits, monitoring reports, L1–L5 routing, action items) | L1 (sponsor/CRO pole core; site pole weaker) |
| Protocol deviation logging | B (site CTMS typically records; not directly observed) | B (not directly observed) | B (compliance monitoring mentioned) | A (full deviation module) | L1 |
| Documents/correspondence tracking | B (pairs with separate eReg/eISF product) | A (eIRB/eReg integrations) | B (pairs with separate eReg) | A (reports & letters; not the eTMF) | L1 |
| Dashboards / KPI reporting | A (enrollment metrics, BI) | A (dashboards co-developed, accrual/activation/effort) | A (dashboards, financial projections) | A (dashboard panels, filters, notification config) | L1 |
| Role-based access, approvals, audit trail | B (MFA/SAML; unlimited profiles) | B (routing across teams) | B | A (L1–L5 hierarchies, audit trails) | L1 |
| Integrations (EDC/eTMF/RTSM/EMR/IRB/GL) | A (eSource, eReg, Outlook, SubjectWell; API) | A (EMR Epic/Cerner, GL, eIRB, eReg, eSource, Payments, Analytics) | A (eReg, eSource, Epic, APIs) | A (EDC/RTSM/eTMF native + third-party) | L1 |
| Recruitment machinery (database, funnels, prescreening) | A | C (not observed) | A (recruitment/enrollment tools) | C (not observed) | L2 (site pole; depth varies) |
| Participant engagement (texts, portals, stipends) | A (Text, MyStudyManager) | C | A (CCText, CCPay) | C | L2 |
| Billing-compliance machinery vs EMR charge grids | C | A (CRPC billing grid, IHE) | B | C | L2 (institutional variant) |
| Biospecimen management | — | A (separately licensed module) | — | — | L2 (institutional variant) |
| Feasibility / site-selection / pipeline analytics | A (Devana, TrialAlign — separate products) | C | C | C | L2 (sponsor-side adjacency) |
| IP/trial-supply visibility | C | C | C | A (IP status dashboard panel; RTSM sold separately) | L2 (rollup only; full supply = RTSM) |

## Canonical Model (synthesis)

**L0 — Defining Invariant** (remove any one and the product stops being a CTMS):

1. **The clinical study (protocol) as the central managed object** — an identified, protocol-defined trial that everything else hangs off. Without it, the product is generic project management or a site CRM.
2. **The site & personnel network as the operational population** — the locations (and their staff/roles) that execute the study, activated and tracked as managed records. (A single-site deployment still models the site explicitly.)
3. **Protocol-anchored operational events planned and tracked against actuals** — milestones, visit schedules/targets, activation steps: the system records plan vs actual progress of trial conduct over time.
4. **A recorded, auditable operational history of trial conduct** — enrollments, visits, monitoring, deviations are recorded as attributable operational records in a shared system of record used by multiple roles.

**L1 — Common Mature Structure** (present across the sample; expected in market but not definitional):

- subject/participant operational tracking (screening, enrollment status, visit schedules, windows, overdue visits)
- budget & payment machinery (study/site budgets, milestone-triggered invoicing, expenses, receivables/payables, participant stipends in site pole)
- monitoring machinery (CRA visit scheduling, monitoring reports/letters, findings, action items with owners/due dates)
- protocol deviation logging (standardized capture, classification, CAPA, IRB/ethics notification)
- operational documents & correspondence (visit reports, activation/follow-up letters; distinct from the eTMF archive)
- dashboards / KPI / analytics (enrollment, accrual, cycle times, financial reconciliation)
- role-based access, multi-level approval workflows, audit trails, notification machinery
- integrations: EDC, eTMF, IRT/RTSM, EMR/EHR, IRB/eReg systems, general ledger/ERP, BI

**L2 — Variant / Optional Structure**:

- operational pole: sponsor/CRO-centric (milestones, monitoring, invoices to sponsor) vs site/institution-centric (recruitment, visit operations, billing compliance, participant engagement) vs network/enterprise aggregation
- recruitment depth (patient databases, website funnels, prescreening, remarketing)
- participant engagement extras (two-way texting, portals, stipend/debit-card payments)
- institutional billing-compliance machinery (EMR charge grids, coverage analysis)
- biospecimen management; feasibility/site-selection/pipeline intelligence (often adjacent products); IP visibility rollups (full supply = RTSM); AI assistance (era-current)

**L3 — Vendor-specific** (research notes only): Clinion's L1–L5 approval levels, named letter set, "100+ notifications", "professional costs" invoicing, cost/startup-reduction claims; RealTime's SOMS bundling, inSites report builder, Devana/TrialAlign adjacency, GlobalPay/SitePay, 30-country and ROI claims; OnCore's Onsemble community, RPE/IHE CRPC integrations, Epic/Cerner specifics, biospecimen licensing, "fifty to 500+ trials" fit guidance; Clinical Conductor's CCText/CCPay modules, Ascension unbilled-recovery claim.

## Boundary Findings

- **vs EDC (Electronic Data Capture)**: EDC captures clinical/subject data per protocol (CRFs); CTMS manages the operational execution (who/where/when/how-much). Direct evidence of separation: Clinion sells EDC and CTMS as separate integrated products; RealTime and Advarra sell eSource/EDC separately from CTMS; Clinion FAQ lists "site coordinators" as CTMS users for management, not data entry. Integration seam: enrollment/visit data flows into CTMS dashboards.
- **vs eTMF / eReg**: regulatory document archive vs operational tracking. Clinion sells eTMF separately ("DIA-based prebuilt structure, audit trails"); RealTime sells eReg/eISF separately; Advarra sells eReg separately; CTMS keeps visit reports/letters/correspondence but the master regulatory file is the eTMF's job. Joint-review-worthy but clean.
- **vs IRT/RTSM**: randomization and trial-supply logistics are a separate Type (Clinion sells RTSM separately; CTMS only shows IP rollups on its dashboard).
- **vs Clinical Trial Recruitment Platform**: recruitment-first machinery vs full operational management. Site-pole CTMS bundles recruitment surfaces (RealTime: database, funnels, prescreening; Clinical Conductor: enrollment tools). Boundary: recruitment platform's managed object is the candidate funnel; CTMS's is the study×site×participant operation. Flag: sibling leaf overlap.
- **vs Clinical Trial Site Management (directory sibling)**: real market products ("site CTMS") sit exactly between the two labels — RealTime/Clinical Conductor are called CTMS by their own vendor and are site-operated. The directory has both leaves; the distinction is likely framing (trial-operational system used by sites vs site-business management) and needs joint review. Recorded as boundary issue.
- **vs Clinical Data Management**: data cleaning/query management after capture — different function, no overlap observed in sampled CTMS.
- **vs Project & Work Management**: generic tasks/projects vs protocol-anchored objects, regulated vocabulary (deviations, monitoring, IRB), regulated audit/approval requirements, and study financial semantics. A PM tool cannot be relabeled a CTMS without the protocol/site/subject/regulatory structure.
- **vs Practice Management/EHR**: care delivery vs research conduct; the EMR appears in CTMS land only as an integration partner (OnCore's Epic/Cerner integration for demographics/billing).

**"去掉什么就变成另一个 Type" tests**:
- Remove protocol-anchored milestones/visits → generic project manager.
- Remove study/sites (operational trial structure) → CRM or site-business tool.
- Remove operational-conduct recording (keep only data capture) → EDC.
- Remove operational tracking (keep only documents) → eTMF/eReg.
- Remove everything but candidate funnel → recruitment platform.
- Remove randomization/supply (never in CTMS) → RTSM.

## Historical / Market-Sample Check (per §24)

Would older/regional/platform-native CTMS fit the L0? Yes: 1990s–2000s sponsor CTMS (desktop/client-server study trackers with sites, milestones, monitoring logs, investigator grants) and single-site paper-replacement systems satisfy the four-part core without websites, EMR integrations, texting, BI, or AI. The L0 is era-independent; recruitment funnels, participant apps, billing-compliance grids, and enterprise BI are modern accretions kept in L1/L2. ✓

## Uncertainties

- Deep user-manual-level behavior (exact state machines for site activation, visit-window rule syntax, payment-trigger conditions) could not be observed: vendor help centers are largely customer-gated; fetched evidence is product/marketing pages + screenshots. All final-doc claims are calibrated accordingly (no precise defaults/time windows asserted).
- Enterprise-suite CTMS (Veeva Vault CTMS, Medidata, Oracle) unreachable this pass; the sponsor/CRO pole rests on Clinion + cross-product inference. If the enterprise suites materially differ (e.g., aggregate-only enrollment tracking), L1 subject-tracking depth might need a variance note — already written conservatively.
- Whether the industry would call site-operated systems "CTMS" vs "site management" is settled by vendor self-labeling (RealTime and Advarra both say "CTMS"), but the directory's separate "Clinical Trial Site Management" leaf needs a joint-review decision.
- Monitoring machinery evidence is strongest for the sponsor/CRO pole (Clinion); OnCore/Clinical Conductor monitoring features were not directly observed.

## Final Synthesis

A CTMS is the **operational system of record for conducting clinical trials**. Its world = the study (protocol) as central object × the sites/personnel executing it, with the trial's operational plan (milestones, visit schedules, activation steps) tracked against actual progress, and conduct events (enrollments, visits, monitoring, deviations) recorded as an auditable operational history. Mature products add subject-level visit tracking, budget/payment machinery, monitoring workflows, deviation logging, correspondence, dashboards, role-governed approvals, and integrations across the eClinical stack (EDC/eTMF/RTSM/EMR/IRB/GL). Two stable poles — sponsor/CRO-centric and site/institution-centric — share the same skeleton and differ in which standard capabilities are deepest. It is neither the data-capture system (EDC), nor the document archive (eTMF), nor the randomization/supply system (IRT/RTSM), nor a recruitment funnel.
