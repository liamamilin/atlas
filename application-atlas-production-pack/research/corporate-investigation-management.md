# Research Notes — Corporate Investigation Management

Research date: 2026-09-07
Leaf: Corporate Investigation Management (§11 Legal, Risk, Compliance & Governance)
Slug: corporate-investigation-management

## Research Goal

Understand what "Corporate Investigation Management" software actually is as an Application Type: what its central objects are, how an investigation moves through the system, what machinery supports fact-finding, who uses it, what rules govern it, and where its boundaries lie against the many sibling case/investigation Types in the directory (whistleblowing/speak-up, ethics & conduct, employee relations case management, internal audit, eDiscovery/legal hold, legal matter management, retail loss prevention, AML/fraud, cyber incident response, public-sector case management).

## Initial Boundary

Initial hypothesis (pre-research): the Type is the corporate-side system for running internal investigations into alleged wrongdoing — misconduct, fraud, harassment, policy violations, whistleblower reports, security incidents — from intake through evidence, interviews, findings, and resolution. The central object is a confidential investigation case. Nearest neighbors:

- Whistleblowing / Speak-up Platform (§11) — the intake channel + reporter protection side
- Ethics & Conduct Management (§11) — program-level conduct registers (processed pass says it "hands deep investigation out")
- Employee Relations Case Management (§09) — HR-owned slice of the same pattern (processed pass flagged this leaf for joint review)
- Internal Audit Management (§11) — methodology-driven assurance vs allegation-driven fact-finding (processed pass, conceptual boundary)
- eDiscovery Platform / Legal Hold Management (§11) — evidence machinery for legal matters
- Retail Loss Prevention Platform (§05.25) — retail-loss investigations (processed pass names this leaf as the generic sibling)
- AML Platform / Fraud Detection Platform (§08/§15) — detection-centered financial-crime work
- Cyber Incident Response Platform (§15) — technical security incidents
- Public Sector / Law Enforcement Case Management (§24) — government analogs

Prior-pass flags to discharge:
- research/employee-relations-case-management.md: "employee-relations-case-management vs whistleblowing-speak-up-platform / corporate-investigation-management (§11): sampled products bundle anonymous-reporting/hotline intake with case handling (intake auto-converts to cases) and multi-department products share one case engine across HR/ER, ethics, fraud, security and Title IX — intake channel vs handled case, and HR-owned vs legal-owned slices of one investigation pattern; flagged for joint review when those leaves are processed."
- research/ethics-conduct-management.md: "vs Corporate Investigation Management: investigation depth (interviews, evidence, case files, findings) is the sibling's center; E&C keeps review at the program level."
- research/internal-audit-management.md: "vs Corporate Investigation Management — investigations pursue facts for a specific matter (allegation-driven); internal audits are methodology-driven, program-scoped examinations producing standing assurance. Conceptual boundary (C-layer; not product-tested in this pass)."
- research/retail-loss-prevention-platform.md: "corporate investigation management handles legal/HR/compliance investigations with legal holds, matter management; LP case management handles retail-loss investigations with ORC linking, recovery, prosecution support, LE collaboration."

## Research Questions

1. What is the central object (case / investigation / matter / incident)? What does it carry?
2. What is the investigation lifecycle, and which states are organization-defined vs product-defined?
3. What fact-finding machinery exists (evidence storage, interviews, tasks, notes, timelines)?
4. How does intake work, and is intake machinery definitional or bundled from the speak-up sibling?
5. Who are the users and roles (investigators, case managers, decision-makers, admins, reporters)?
6. What findings/outcome structures exist (substantiation, actions, remediation)?
7. What rules matter (confidentiality, role-based access, implicated-party exclusion, anonymity, privilege, audit trail, retention)?
8. What reporting/analytics exist (cycle times, substantiation rates, trends, board reporting)?
9. Where are the boundaries against the sibling Types listed above?

## Representative Products

| Product | Philosophy / segment | Why sampled | Evidence tier |
|---|---|---|---|
| Case IQ (formerly i-Sight) | Pure-play, multi-department investigation case management (ethics, HR/ER, fraud, security, Title IX, complaints/ombuds/SIU) | The configurability pole; one engine across departments; 25+ year lineage (i-Sight) | Tier 2 (official product pages + FAQ + case study) |
| NAVEX (EthicsPoint Professional / Whistleblowing & Incident Management) | Suite-embedded case management inside the largest ethics/GRC platform | The compliance-program pole; enterprise whistleblowing + incident management; tier ladder (Essentials/WhistleB/Professional) | Tier 2 (official product pages) |
| Vault Platform (now Diligent) | Speak-up-led platform whose case-management product is "Resolution Hub" | The speak-up-led pole; shows the intake→case handoff explicitly; EU/UK heritage | Tier 2 (official product pages) |
| HR Acuity | Methodology-led workplace investigation management (ER/HR-owned slice) | The methodology pole (Plan/Investigate/Determine); HR-slice with privilege and fairness machinery | Tier 2 (official product page + FAQ) |
| Exterro (FTK) | Boundary-informing only — digital-forensics-centered "corporate investigations" | Shows the evidence-analysis pole that is NOT this Type (Product Mismatch recorded) | Tier 2 (official use-case page) |

Selection notes: Resolver (corporate security slice) was preferred as a fifth sample but was unreachable (403 ×2 on www and apex) — abandoned per network rules; the security-department pole is therefore under-sampled. NAVEX case-management page 404 ×2 in the employee-relations pass; this pass reached NAVEX via the whistleblowing-solutions and EthicsPoint Professional pages.

## Sources

- Case IQ — home page (suite, FAQ, security, integrations): https://www.caseiq.com/
- Case IQ — "Case Management Software for Every Investigation" (case types, lifecycle FAQ, intake/routing/AI/reporting): https://www.caseiq.com/product/case-management-software
- NAVEX — "Whistleblowing Software & Solutions" (definition of whistleblowing software, three-tier ladder, case-management mechanics): https://www.navex.com/en-us/platform/whistleblowing-software-solutions/
- NAVEX — "EthicsPoint Professional" (configurable case management, implicated-party safeguards, data intelligence, status visuals): https://www.navex.com/en-us/platform/whistleblowing-software-solutions/ethicspoint-professional/
- Vault Platform — home page (Active Integrity: reporting channels / Resolution Hub / Integrity Insights): https://vaultplatform.com/
- Vault Platform — "Resolution Hub" (case management product page): https://vaultplatform.com/products/resolution-hub/
- HR Acuity — "HR Workplace Investigation Management Software" (Plan/Investigate/Determine, interview protocols, permissions, privilege, FAQ): https://www.hracuity.com/platform/investigation-management/
- Exterro — "Corporate Investigations" use case (FTK-centered; boundary-informing): https://www.exterro.com/use-cases/corporate-investigations
- Cross-referenced (prior passes): research/employee-relations-case-management.md (HR Acuity + Case IQ observations), research/ethics-conduct-management.md, research/internal-audit-management.md, research/retail-loss-prevention-platform.md, research/complaint-escalation-management.md (Case IQ heritage), research/construction-safety-management.md (investigation/retention machinery analog)

## Product A — Case IQ (evidence layer A unless noted)

Positioning: "Case Management, Compliance & Hotline Solutions"; "Case Management Software for Every Investigation"; "80,000+ investigators"; 25+ years of industry knowledge (i-Sight heritage).

- **One platform, many case types** (explicit list): Ethics & Compliance Investigations (code of conduct, bribery, kickbacks, FCPA risk); HR & Employee Relations Cases (harassment, discrimination, retaliation, ER disputes); Fraud Investigations (theft, embezzlement, expense and procurement fraud); Security, Health & Safety (workplace violence, data breaches, physical threats); Title IX Investigations (sex-based misconduct, student welfare, campus reports); Complaints, Ombuds & SIU Cases (customer concerns, ombuds escalations, insurance SIU claims).
- **Definition via FAQ**: "Case management software helps organizations capture, organize, investigate, and resolve sensitive matters in one secure system… manage reports, document findings, track progress, and close cases consistently."
- **What it does (FAQ)**: "intake reports, assign owners, manage tasks and deadlines, store evidence and notes, document actions, and report on trends and outcomes."
- **Lifecycle (FAQ)**: "capture reports from multiple channels, triage and assign cases, manage evidence and interviews, track tasks and milestones, document findings, and close cases with a complete audit trail… a more consistent and defensible process from intake to closure."
- **Intake**: omni-channel — "web, portal, email, hotline, and integrations"; "anonymous and two-way communication"; "guided intake forms that capture consistent, complete details"; custom intake forms with "30+ field types", conditional logic, no code.
- **Routing**: "Auto-assign cases by type, region, severity, or workload. Notify, escalate, update — without lifting a finger."
- **Case linking**: "Automatic case linking to surface related incidents early"; "Case linking and pattern detection to prevent recurrence."
- **AI**: Clairia — "generating summaries, building timelines, surfacing insights… standardized, consistent responses with built-in Playbooks."
- **Confidentiality**: "role-based permissions, confidentiality controls, secure access, and detailed case visibility settings… only the right people can view or act on sensitive case data"; "Role-based access and secure collaboration across departments."
- **Audit**: "Full audit trails for every action and decision."
- **Analytics**: "75+ chart types", workload monitoring, trend analysis, "One-click investigation reports and data exports for stakeholders", board-ready reports.
- **Anti-spreadsheet framing (FAQ)**: "Excel, SharePoint, and email were not designed as investigation case management software… structured intake, workflow automation, secure collaboration, audit trails, reporting, and role-based access controls."
- **Case study (Prairie State College)**: previously "managed HR, Title IX, ethics, and security investigations across spreadsheets, email, and shared drives"; moved to "one secure case management system, using configured workflows, automatic routing, and complete audit trails to close cases faster and document every step."
- **Integrations**: HRIS (Workday, SAP SuccessFactors, BambooHR), SSO (Okta, Azure AD), SFTP, REST API; "HR, legal, compliance, hotline, or ERP systems."
- **Departments served**: Ethics/Risk/Compliance, HR, Title IX. Security posture: SOC 2 Type II, GDPR-ready, data residency options.

## Product B — NAVEX (EthicsPoint / Whistleblowing & Incident Management) (evidence layer A)

Positioning: "AI-powered whistleblowing software"; suite = NAVEX One GRC platform; 13,000+ customers; 88M employees supported.

- **Vendor's own definition of the category**: "Whistleblowing software is a secure system organizations use to receive, document and manage reports of misconduct or compliance concerns. It typically combines reporting channels with structured case records so disclosures are handled consistently and defensibly."
- **Tier ladder**: Essentials (fast-start hotline + "straightforward case management"), WhistleB (EU/GDPR-first, European hosting), Professional (enterprise: "AI-assisted investigations, configurable workflows, advanced analytics").
- **Case-management mechanics**: "Use centralized workflows, guided forms and automated processes to move cases from report intake to resolution with clarity and consistency."
- **Uniform handling**: "Capture reports securely through web, mobile and phone channels; Guide reviewers with clear questions and structured case fields; Track actions and updates with a complete, auditable case history; Standardize documentation so similar cases follow the same fair process."
- **Configurable case management (Professional)**: "Automate assignments, approvals and escalations, and update assignments across multiple cases at once"; "Control case access and visibility with role-based permissions and AI-enhanced safeguards that help prevent implicated parties from accessing sensitive case information"; "Standardize reporting metrics to ensure consistency across global teams"; "Design forms and up to two custom workflows for specific teams, departments or regions."
- **Data intelligence**: "Identify patterns across case types, teams and regions"; "Surface related cases with AI-assisted analysis to uncover repeat behaviors, emerging risks and investigation patterns earlier"; "Visualize results in Power BI dashboards… board-ready reporting"; "Summarize complex case details with built-in AI tools."
- **Connected compliance**: "Link reports to related policies and training to uncover recurring causes"; "Share data securely between teams and systems"; "Export consistent, audit-ready data for leadership and regulators."
- **Reporter side**: machine translations for reports and follow-ups; 24/7 web/phone/mobile; "anonymous or named reporting options"; coverage extends to "contractors and suppliers."
- **Governance/oversight**: "Control who can access case information, keep activity logged and auditable, and see which cases individual users have viewed or edited."
- **Product-visual state names (product-specific, L3)**: dashboard progress chart shows "Investigation Completed, In Progress, Unreviewed, Investigation Started, Review Complete"; notifications "notifying assignees of status change, primary issue, and tier change"; case notification email with "case due date."
- **Datasheet framing**: "EthicsPoint incident management system creates consistency in the intake, reporting, resolution and analysis of incidents that pose risks to your organization."

## Product C — Vault Platform / Diligent (evidence layer A)

Positioning: "Workplace misconduct and Speak Up solution"; now part of Diligent; "Active Integrity platform" = Reporting channels + Resolution Hub + Integrity Insights.

- **Resolution Hub (case management product)**: "Communicate, collaborate, and close out audit-ready case files in the Resolution Hub, your all-in-one source of truth for running effective investigations."
- **Intake→case handoff (explicit)**: "Reports submitted by employees are routed to the most appropriate Case Manager, who is then notified to begin the investigation process. All incident information, including evidence, is gathered and stored in the Vault Resolution Hub to streamline the investigation process. Case Managers are even able to communicate with reporters from directly within the report itself."
- **Cross-department collaboration**: "Investigate and quickly manage cases through to resolution, with cross-department collaboration. All in one place."
- **Use cases**: Fraud, Discrimination, Harassment & Bullying, Bribery, ESG Violations, Personal Safety.
- **Solutions by buyer**: CEOs, Compliance, DEI, Employees, HR, Legal.
- **Security**: GDPR compliant, ISO 27001, SOC 2; TLS/AES-256; EU/UK data centers.
- **Intake channels (sibling products)**: mobile app, Open Reporting, VaultTalk; anonymity ("anonymous individual") and collective reporting ("GoTogether®").

## Product D — HR Acuity (evidence layer A)

Positioning: "Next Generation HR Workplace Investigations Management Software"; "Building Safer Workplaces for 5 Million Enterprise Employees"; ER-practitioner methodology-led.

- **Purpose**: "Conduct consistent, compliant workplace investigations that uphold neutrality, confidentiality and fairness… structured, transparent fact-finding, reducing legal and reputational exposure."
- **Proprietary three-step methodology**: **Plan** ("Create a blueprint for your investigations and plan your interviews with guided templates and AI support"), **Investigate** ("Use built-in interview protocols to build trust and ensure efficient, thorough and fair investigations that comply with organizational policies and regulations"), **Determine** ("Review your findings and determine a course of action. Then maintain a secure, centralized source of truth for your documentation, with role-based access controls to protect sensitive information").
- **Feature set**: Interview templates and AI-powered interview guides; "Robust Role-Based Permissions — Ensure confidentiality, allow attorney client privilege as needed and manage handoffs to decision-makers to guard against retaliation"; ThroughCare™ (post-case employee support with task sets and reminders); "Defensible AI".
- **Compliance framing**: "protect attorney-client privilege… remain compliant with the latest laws, regulations and EEOC requirements."
- **FAQ**: "Workplace investigation management software streamlines how organizations address workplace investigations… tracks all investigation details in one accessible location"; "HR Acuity centralizes all investigation data — tasks, interviews, decisions and outcomes — in a shared system that enables visibility for authorized stakeholders."
- **Platform siblings**: Ethics & Compliance Hotline, Anonymous Workplace Reporting, Case Management, Documentation, Analytics, Union Grievances, Workplace Accommodations.
- **Buyers**: Employee Relations & HR; Legal, Ethics & Compliance; DEI; C-Suite.

## Product E — Exterro (boundary-informing; Product Mismatch recorded)

- Exterro's "Corporate Investigations" use case today centers **FTK digital forensics**: "analyze digital evidence with unmatched precision and speed—while maintaining the confidentiality, defensibility, and repeatability required…"
- Workflow: Collect (imaging) → Verify (hashing) → Process (artifact analysis) → Analyze (AI review/search) → Report ("defensible reports for HR or legal teams—ready for audit, arbitration, or litigation") → Remediate.
- Roles named: Corporate Security & Investigations Teams; Legal & Compliance Officers; HR & Employee Relations Professionals; Data Privacy & Governance Analysts; Internal Audit & Risk Management Teams.
- Triggers named: insider data theft/IP misuse; employee misconduct/policy violations; regulatory/compliance audit investigations; data breach/unauthorized access; "HR investigations requiring defensible evidence handling."
- **Assessment**: evidence-analysis machinery (forensics), not a case-lifecycle system of record. Belongs to Digital Forensics Platform (§15) / eDiscovery (§11) territory. Recorded as Product Mismatch for this leaf; used only to mark the evidence-tooling boundary. (Historically Exterro also marketed Legal GRC investigation management; current site does not surface it — unverified, see Uncertainties.)

## Cross-product Comparison

| Dimension | Case IQ | NAVEX EthicsPoint Pro | Vault Resolution Hub | HR Acuity | Interpretation |
|---|---|---|---|---|---|
| Central object | case (multi-type) | case / incident | case (born from report) | investigation (within case framework) | **Case of record is universal** |
| Origin of a case | omni-channel intake (web/portal/email/hotline/integrations) | web/phone/mobile reports, anonymous or named | employee report routed to Case Manager | anonymous reporting + direct ER intake | Intake machinery common; case can also be created by staff directly (HR Acuity) |
| Routing/assignment | auto-assign by type/region/severity/workload | automated assignments, approvals, escalations, bulk update | routed to "most appropriate Case Manager" | assignment + handoffs to decision-makers | **Managed routing is universal** |
| Lifecycle | intake→triage→assign→evidence/interviews→tasks→findings→close (audit trail) | intake→resolution; states incl. Unreviewed/Investigation Started/In Progress/Review Complete/Investigation Completed | report→case manager notified→investigate→resolution | Plan→Investigate→Determine | **Managed lifecycle to a recorded resolution is universal**; exact states product-defined |
| Fact-finding record | evidence + notes storage, tasks/milestones, timelines | structured case fields, complete auditable case history | incident info + evidence gathered in hub | tasks, interviews, decisions, outcomes centralized | **Evidence/interview/task accumulation on the case is universal** |
| Determination | "document findings, and close cases" | resolution + outcomes visualization | "close out audit-ready case files" | "review your findings and determine a course of action" | **Recorded finding/outcome at closure is universal** |
| Confidentiality | role-based permissions, case visibility settings | role-based permissions + implicated-party safeguards + view/edit logging | secure, audit-ready | role-based access, attorney-client privilege, anti-retaliation handoffs | **Confidentiality regime is universal**; implicated-party exclusion explicit in one product |
| Reporter communication | anonymous + two-way | follow-ups, machine translations | communicate within the report | (post-case ThroughCare) | Common; depth varies |
| Case linking / patterns | automatic case linking, pattern detection | AI-assisted related-case surfacing, repeat-issue detection | (Integrity Insights analytics) | trends/hotspots analytics | Common (B) |
| Analytics/reporting | 75+ chart types, dashboards, one-click reports | Power BI dashboards, benchmarks, board-ready exports | Integrity Insights | analytics, benchmarking, C-suite reporting | Common (B) |
| AI assistance | Clairia (summaries, timelines, playbooks) | Nira (intake guidance, summaries, translations, related cases) | (Diligent AI framing) | AI planning + interview question generation | Current-market common, not definitional |
| Integrations | HRIS, SSO, SFTP, REST API | HR/risk/policy systems, Power BI | Workday | Workday partnership, HRIS | Common (B) |
| Regulatory framing | FCPA, Title IX, industry pages | EU Whistleblowing Directive, SOX, DOJ guidance | EU whistleblowing toolkit | EEOC, employment law | Variant by jurisdiction (B) |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The confidential case of record** — a persistent, individually identified record of a specific allegation or matter of potential wrongdoing (who/what is alleged, against whom, under what policy or law), held under a restricted, role-gated access regime because its content is sensitive and legally consequential. Remove → a generic case tracker (bug tracker / service desk class), not investigation management.
2. **The managed investigation lifecycle** — the case moves through an organization-defined path from intake/triage through assignment and fact-finding to closure; states, stages, and routing rules are configured by the organization, not fixed by the software. Remove → an evidence archive or allegation log with no managed process.
3. **The fact-finding record with a recorded determination** — evidence, interview records, notes, and tasks accumulate on the case as the durable investigation record, and the case closes with a recorded finding (substantiated / unsubstantiated class) and recorded outcome/actions. Remove → intake register or ticket queue; the "investigation" semantics disappear.

Jointly-held is load-bearing: 1+2 without 3 = workflow tool over allegations; 1+3 without 2 = document store; 2+3 without 1 = generic case management.

### L1 — Common Mature Structure

- multi-channel intake (web forms, hotline, email, mobile, integrations) with anonymous-or-named reporting
- automated routing/triage (by type, region, severity, workload), approvals, escalations, bulk actions
- configurable workflows, forms/questionnaires, and case categories per department/region
- two-way reporter communication (including anonymous follow-up)
- case linking / related-case surfacing / repeat-pattern detection
- audit trail of case activity (including who viewed/edited)
- dashboards, metrics, benchmarking (cycle times, substantiation rates, trends), board-ready exports
- AI assistance (summaries, drafting, translation, related-case detection, intake guidance)
- integrations (HRIS, SSO, policy/training systems, APIs)
- role model: investigators/case managers, decision-makers, administrators; reporters as external submitters

### L2 — Variant / Optional Structure

- department-specific configurations: HR/ER, ethics & compliance, fraud, corporate security, Title IX, ombuds, SIU
- hotline operations as a bundled service (24/7 live answer, multilingual intake specialists)
- regulatory alignment packages (EU Whistleblowing Directive, SOX, EEOC, DOJ guidance framing)
- legal-owned machinery: privilege flags, legal hold, eDiscovery/forensics integration
- post-case care and remediation tracking
- data residency / hosting choices (EU hosting), on-prem (forensics pole)
- program-level analytics and benchmark data

### L3 — Vendor-specific (Research Notes only)

- Case IQ: Clairia AI; 30+ intake field types; 75+ chart types; three anonymity levels; 100+ language hotline; benchmark report (450+ teams)
- NAVEX: EthicsPoint Essentials/Professional tiers; WhistleB; Nira AI; Power BI dashboards; "up to two custom workflows" limit; implicated-party AI safeguards
- Vault: Resolution Hub; Open Reporting; VaultTalk; GoTogether®; Integrity Intelligence
- HR Acuity: Plan/Investigate/Determine methodology; olivER AI; ThroughCare™; managER; ER/Q maturity model
- Product-specific state names (NAVEX visual): Unreviewed / Investigation Started / In Progress / Review Complete / Investigation Completed

## Historical / Market-Sample Check (§24 logic)

- Pre-software practice: corporate security, legal, and HR departments ran investigations with paper case files, typed interview notes, and memo-to-file outcomes — the L0 structures (case record + managed path + fact-finding + determination) all present without any digital machinery.
- Hotline-era (EthicsPoint lineage, ~1999→): case management attached to hotline intake — satisfies L0 without AI, cloud, or multi-channel web intake.
- Spreadsheet-era (documented in-sample): Prairie State College "managed HR, Title IX, ethics, and security investigations across spreadsheets, email, and shared drives" — the pre-platform reality; the L0 structures were carried by process discipline, not software.
- Regional: EU products (WhistleB, Vault) are GDPR/Directive-first; US products frame SOX/EEOC/Title IX; both fit L0 unchanged.
- Conclusion: nothing in L0 depends on a hotline, a specific regulation, AI, cloud, or multi-channel intake. The definition does not encode the current compliance-suite implementation.

## Vendor-specific / Rejected Findings

- **Rejected**: "Corporate Investigation Management = whistleblowing hotline + case management." The hotline is the sibling Type's center; in-sample vendors bundle both, but a case engine without hotline machinery (HR Acuity direct intake; Case IQ sold standalone) satisfies the Type.
- **Rejected**: "Investigation management = digital forensics." Exterro's corporate-investigations pole is evidence analysis without a case lifecycle — a different Type (recorded as Product Mismatch).
- **Rejected**: "Plan/Investigate/Determine is the standard lifecycle." It is HR Acuity's branded methodology (single-vendor); the underlying plan→gather→decide arc is natural to the work but the named methodology must not be canonicalized.
- **Rejected**: "AI assistance is part of the Type." Universal in the 2026 sample but absent in the hotline-era and spreadsheet-era realizations; current-market common only.
- **Rejected**: "Implicated-party exclusion is universal." Explicitly documented in one product (NAVEX); role-gated restriction is universal in-sample, the specific implicated-party safeguard is kept qualified.
- **Rejected**: "Multi-department shared engine is definitional." Case IQ demonstrates it; department-specific products (HR Acuity) satisfy the Type with one department's configuration.

## Boundary Findings

1. **vs Whistleblowing / Speak-up Platform (§11 sibling — DISCHARGES the employee-relations joint-review flag)**: speak-up products center the reporting channel + report record + reporter protection + regulatory intake compliance; this Type centers the handled case lifecycle (fact-finding → findings → outcome). In-sample, vendors bundle both (Case IQ hotline product; NAVEX; Vault channels→Resolution Hub), and intake commonly auto-converts to a case. Test: remove the case-handling lifecycle → whistleblowing platform; remove the anonymous-channel machinery → investigation management remains. The seam is the object: report/channel vs case/investigation.
2. **vs Employee Relations Case Management (§09, processed)**: same case/investigation pattern, different owner and population. ER case management is the HR-owned slice whose subject is workplace conduct between people in the organization, with employment-law fairness machinery; this Type covers corporate/legal/security-owned matters (fraud, bribery, security, regulatory) and multi-department products (Case IQ) literally share one engine across both. Test: restrict the subject to employment conduct + ER regime → ER case management; generalize the subject and owner → this Type.
3. **vs Ethics & Conduct Management (§11, processed)**: consistent with the ethics pass — investigation depth (interviews, evidence, case files, findings) is this Type's center; E&C keeps review at the program level (disclosures, attestations, registers) and hands deep investigation out. Test: remove fact-finding depth → E&C program platform.
4. **vs Internal Audit Management (§11, processed)**: consistent with the internal-audit pass (conceptual, C-layer) — investigations are allegation-driven fact-finding for a specific matter; audits are methodology-driven, program-scoped examinations producing standing assurance. An audit finding can *intake* into an investigation; the objects differ (engagement/audit vs case).
5. **vs eDiscovery Platform / Legal Hold Management (§11)**: evidence collection/processing/production machinery for legal matters vs the investigation case lifecycle. Exterro evidence (A): the corporate-investigations pole is collect→verify→process→analyze→report over digital evidence, with no case-lifecycle object of record. Test: remove the case lifecycle → eDiscovery/forensics tooling; remove evidence-processing depth → investigation management. Investigations commonly *feed* eDiscovery when they become litigation.
6. **vs Legal Matter Management (§11)**: a matter is a legal engagement (litigation, transaction, dispute) owned by the legal department; an investigation is an internal fact-finding effort that may *escalate into* a matter. Different lifecycle endpoints (disposition/filing vs finding/outcome).
7. **vs Retail Loss Prevention Platform (§05.25, processed)**: consistent with the LP pass — LP case management handles retail-loss investigations with ORC linking, recovery, prosecution support, and law-enforcement collaboration; this Type handles corporate matters with legal/HR/compliance semantics. Same case machinery, different domain vocabulary and actors.
8. **vs AML Platform / Fraud Detection Platform (§08/§15)**: detection-centered systems whose case handling is embedded downstream of alerts/transaction monitoring; this Type is investigation-centered — allegations (from people) are the primary origin, though alerts can intake. Financial-crime investigation teams sit between the two; the seam is center of gravity (detection/decisioning vs fact-finding record).
9. **vs Cyber Incident Response Platform (§15, processed)**: security incidents are technical events (alerts, entities, IOCs) with response playbooks; corporate investigations are human-conduct allegations with interviews and findings. Overlap at insider-threat and data-exfiltration matters (Exterro's trigger list confirms the overlap zone), but the objects and workflows differ.
10. **vs HR Case Management (§09, unprocessed)**: per the ER pass — HR service delivery frames the employee as a customer raising service requests resolved against SLAs; investigation management handles sensitive matters with fact-finding and confidentiality. Joint pass recommended for the HR Case Management leaf.
11. **vs Public Sector Case Management / Law Enforcement Case Management (§24)**: government analogs carry statutory authority, public-record obligations, and (law enforcement) prosecutorial workflow; corporate investigation management is internal, employment-law-bound, and private. Same skeleton, different authority regime.
12. **vs Business Case Management Platform (§10, processed)**: generic case management provides record+routing+lifecycle without investigation semantics — no allegation subject, no fact-finding record, no findings/outcome, no confidentiality regime. This Type is a domain instantiation of the case pattern whose domain semantics are the Type.

## Uncertainties

- **No Tier 1 help-center documentation reachable in-sample.** All evidence is Tier 2 official product/FAQ/case-study pages. Precise operational mechanics (exact state machines, field-level behavior, retention defaults) are not verified and are not stated in the final document.
- **Corporate-security pole under-sampled**: Resolver unreachable (403 ×2). Security-department machinery (threat assessment teams, workplace violence prevention programs) is inferred only from Case IQ's case-type list ("workplace violence, data breaches, physical threats") — kept at case-type level, not workflow level.
- **Legal-owned investigation management**: Exterro's former Legal GRC investigation-management module is not surfaced on the current site (FTK-centered); its current state unverified. The legal slice is represented only through HR Acuity's privilege flags and the eDiscovery boundary.
- **Exact lifecycle states**: NAVEX's visual shows one product's state names; not generalized. The final document describes conceptual states with "exact labels vary by product."
- **Substantiation-rate reporting**: HR Acuity's stat ("only 26% of organizations are able to report on substantiation rates") implies substantiation tracking is a differentiator, not a universal — kept as common-not-universal.
- **Whether intake auto-conversion is universal**: explicit in Vault ("reports… routed to the most appropriate Case Manager") and implied in NAVEX/Case IQ; HR Acuity supports direct staff-created cases. Written as "commonly" in the final document.

## Final Synthesis

Corporate Investigation Management is the organization's system of record for internal investigations into alleged wrongdoing. Its defining core is three jointly-held structures: the **confidential case of record** (a persistent, identified, role-gated record of a specific allegation or matter), the **managed investigation lifecycle** (an organization-defined path from intake/triage through fact-finding to closure), and the **fact-finding record with a recorded determination** (evidence, interviews, notes, and tasks accumulating on the case, closing with a finding and recorded outcome). Around that core, mature products add multi-channel intake with anonymity, automated routing and configurable workflows, two-way reporter communication, case linking and pattern detection, audit trails, analytics and board reporting, AI assistance, and integrations with HRIS/policy/SSO systems. The Type is realized as pure-play multi-department case engines (Case IQ), suite-embedded compliance case management (NAVEX), speak-up-led platforms with case hubs (Vault/Diligent), and methodology-led department products (HR Acuity); the evidence-analysis pole (forensics/eDiscovery) is a neighboring Type, not this one. The intake channel belongs to the whistleblowing sibling; the handled case belongs here.
