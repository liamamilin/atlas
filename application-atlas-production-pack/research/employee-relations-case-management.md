# Research Notes — Employee Relations Case Management

Research date: 2026-09-06
Slug: employee-relations-case-management
Directory leaf: Employee Relations Case Management (§09 HR, Workforce & Talent)

## Research Goal

Understand what Employee Relations (ER) Case Management is as an Application Type: what the central object is, how sensitive workplace matters (complaints, grievances, allegations, disciplinary issues) are captured, who handles them, what the handling process looks like, what confidentiality/fairness rules shape the system, and where the boundary lies against HR Case Management (service requests), Whistleblowing/Speak-up platforms, Corporate Investigation Management, HRIS/employee records, and generic case management.

## Initial Boundary (working hypothesis before research)

- Core guess: software that turns a reported workplace people-matter into a confidential, tracked case — intake (named or anonymous), triage/assignment, investigation/fact-finding, determination, outcome, follow-up — for HR/ER teams, with role-restricted access and an audit trail.
- Likely confusions:
  - HR Case Management / HR service delivery (employee-as-customer service requests vs sensitive matters)
  - Whistleblowing / Speak-up platforms (intake channel vs handled case)
  - Corporate Investigation Management / ethics case management (§11 Legal domain; same case pattern, different owning function/population)
  - HRIS / Employee Record System (employment record vs matter-process layer)
  - Generic Business Case Management Platform (case pattern without the ER-specific subject matter and confidentiality regime)
  - Complaint & Escalation Management (customer population)
- Unknowns: is the Type always bundled with anonymous-reporting/hotline intake? How broad is the case-type range? Is it sold standalone or embedded in HCM/HR-service-delivery suites? What happens after resolution (aftercare, retaliation monitoring)?

## Research Questions

1. What is the central record? What data defines a case (parties, issue type, context)?
2. How do cases enter the system (manager, employee self-report, hotline, anonymous, HR-created)?
3. What is the case lifecycle from intake to closure, and which states/steps recur across products?
4. How are parties handled (reporter, subject/respondent, witnesses) — including anonymity and two-way contact?
5. What investigation support exists (interview planning, evidence, timelines, findings)?
6. What access/confidentiality/audit rules are structural (role-based access, privilege, audit trail)?
7. What happens after a decision (retaliation check-ins, aftercare, follow-up)?
8. What analytics exist and what do organizations do with them (trends, hotspots, benchmarking)?
9. How is the capability packaged (standalone ER platform, multi-department investigation platform, HCM/HRSD suite module)?
10. Where are the boundaries vs service-request case management, speak-up platforms, and legal/corporate investigation tools?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies (pure-play ER vs multi-department investigations vs reporting-first misconduct platform) + different customer tiers/geographies (US enterprise, North America multi-sector, UK/education).

| Product | Category / philosophy | Tier of evidence |
|---|---|---|
| HR Acuity | Pure-play employee relations & HR case management platform ("from intake through aftercare"); ER-practitioner methodology-led | Tier 2 (official product pages + FAQs) |
| Case IQ | Configurable investigation case management platform; HR/ER is one investigation type among ethics, fraud, security, Title IX | Tier 2 (official product pages + FAQs) |
| Culture Shift | UK "misconduct management" platform; named/anonymous reporting + case management + analytics; strong higher-education/public-sector presence | Tier 2 (official product pages + FAQs) |

Boundary probes attempted but abandoned (see Source-access Limitation): NAVEX (case-management page 404 ×2), ServiceNow HR Service Delivery (timeout ×2), Atlassian Jira Service Management HR page (404). No Tier 1 help-center documentation was reachable in-sample; all evidence is Tier 2 official product/FAQ pages.

## Sources

- HR Acuity — home page (platform pillar nav; positioning): https://www.hracuity.com/
- HR Acuity — "Employee Relations & HR Case Management Software": https://www.hracuity.com/platform/hr-case-management/
- HR Acuity — "HR Workplace Investigation Management Software": https://www.hracuity.com/platform/investigation-management/
- HR Acuity — "Anonymous Workplace Reporting Software": https://www.hracuity.com/platform/anonymous-employee-reporting/
- Case IQ — home page (product suite, FAQ, case types): https://www.caseiq.com/
- Case IQ — "Case Management Software for Every Investigation": https://www.caseiq.com/product/case-management-software
- Culture Shift — home page (Report + Support™ platform): https://www.culture-shift.co.uk/
- Culture Shift — "Case management for consistent, auditable, and defensible outcomes": https://www.culture-shift.co.uk/case-management

## Product Observations

### Product A — HR Acuity (evidence layer A unless noted)

- Positioning: "the industry-leading platform for HR case management and investigations from intake through aftercare"; audience is enterprise HR/ER teams; secondary audiences: Legal/Ethics & Compliance, DEI, C-suite.
- Platform pillar structure (site nav): anonymous/ethics reporting (web + hotline), HR Case Management, Documentation, Workplace Investigations, managER (for people leaders), Performance Improvement Plans, Analytics, Integrations, AI, Workplace Accommodations, Union Grievances, Confidentiality & Security.
- Case management page claims: "Every conversation, document, decision, and outcome centralized in one secure platform with role-based access"; analytics "transforms your case data into a real-time picture of organizational health with exclusive benchmarking"; "Guided workflows and AI-supported investigation frameworks… so every case is handled with rigor, fairness and defensibility"; "Audit-Ready Documentation — Every case captured completely and consistently from the moment it opens — structured for audits, EEOC reporting, and legal scrutiny."
- Stakeholder framing: ER leaders (audit trail that "holds up" when something escalates); Legal & Compliance ("documented, consistent process with role-based access and attorney-client privilege protections built in from the start"); CHROs (benchmarking, real-time trends "before they become legal risks").
- Investigation methodology (proprietary, three phases): **Plan** (blueprint + interview planning with guided templates and AI support), **Investigate** (built-in interview protocols; thorough, fair fact-gathering compliant with policies/regulations), **Determine** (review findings, determine course of action; "stakeholder approvals"; "Retaliation check-ins also fall under this phase").
- Interview tooling: AI-powered interview guides/templates; "ask the right people the right questions, protect attorney-client privilege and help your enterprise remain compliant with the latest laws, regulations and EEOC requirements."
- Aftercare: "Comprehensive ThroughCare™ — Empower your team to support employees after difficult workplace events… ready-to-use task sets and reminders that ensure seamless follow-up."
- Permissions: "Robust Role-Based Permissions — Ensure confidentiality, allow attorney client privilege as needed and manage handoffs to decision-makers to guard against retaliation."
- Manager surface: managER gives people leaders "the tools, guidance and context to respond with speed, consistency and confidence" (60% of ER leaders say managers miss the mark — vendor stat).
- AI: olivER companion — case summaries, writing assistance, risk flags, "explainable suggestions… never make decisions on your behalf."
- Anonymous reporting FAQ (intake→case mechanics): "Every report — whether submitted via web or phone — automatically converts into a structured case record"; investigators "assign cases, track actions, document findings and maintain a complete audit trail within the same system." Anonymous reporters get "a secure PIN so they can log in and follow updates without revealing their identity"; "Two-Way Anonymous Messaging — Securely message anonymous reporters and convert issues into investigations with their consent." Intake: 35 languages / 56 countries; live agent hotline support; named or anonymous.
- Analytics dimensions (FAQ): trends by issue type, business unit/department, geography, time period, allegation category, case resolution metrics.
- Explicit boundary statements (FAQ): "Spreadsheets and HRIS systems weren't built for the legal exposure… no audit trail, no guided investigation workflow and no way to ensure consistent issue handling"; "Ticketing tools were built to route requests and close them out. They were not built for the nuance and complexity of workplace investigations. A help desk queue has no privilege flag, no guided investigation workflow, no defensible audit trail and no way to separate access by role when a matter is sensitive."
- Regulatory anchors: EEOC (US), whistleblower-protection laws "across multiple jurisdictions."

### Product B — Case IQ (evidence layer A unless noted)

- Positioning: end-to-end compliance and case management suite (case management, whistleblower hotline, compliance monitoring, approvals & disclosures, third-party management). Departmental audiences include HR (alongside Ethics/Compliance, Title IX); testimonial from a "Lead, Labour & Employee Relations" and an HR department use case: HR "track[s] 'situations' that come to their attention… assign cases to staff, automatically maintain the history of the case and also set notifications for important due dates."
- Case-type breadth ("One Platform for Every Investigation Type"): Ethics & Compliance (code of conduct, bribery, FCPA), **HR & Employee Relations (harassment, discrimination, retaliation, ER disputes)**, Fraud, Security/Health & Safety, Title IX, Complaints/Ombuds/SIU.
- FAQ definition of the case lifecycle (generic, useful): "capture, organize, investigate, and resolve sensitive matters in one secure system"; "intake reports, assign owners, manage tasks and deadlines, store evidence and notes, document actions, and report on trends and outcomes"; "capture reports from multiple channels, triage and assign cases, manage evidence and interviews, track tasks and milestones, document findings, and close cases with a complete audit trail."
- Intake: omni-channel — web, portal, email, hotline, integrations; "Anonymous and two-way communication"; "Guided intake forms that capture consistent, complete details" (branded forms, 30+ field types, conditional logic); "Automatic case linking to surface related incidents early."
- Triage/routing: "Auto-assign cases by type, region, severity, or workload. Notify, escalate, update — without lifting a finger."
- Workflow: configurable and automated workflows; different workflows by case type, department, country, or issue; tasks, notifications, reminders, escalations, status updates.
- Investigation support: evidence and notes storage; interviews; findings documentation; AI assistant (Clairia) generating summaries, building timelines, surfacing insights.
- Security/access: role-based permissions, "confidentiality controls, secure access, and detailed case visibility settings… only the right people can view or act on sensitive case data"; "Full audit trails for every action and decision."
- Analytics: report builder (75+ chart types), dashboards (trends, risks, repeat issues), workload monitoring, one-click investigation reports/exports, case linking and pattern detection.
- Integration: SSO, connectors, SFTP, REST API; "HRIS/employee data (e.g., Workday, SAP SuccessFactors, BambooHR) to support routing and reporting" — i.e., employee population data is synced from the HR system.
- Compliance posture: SOC 2 Type II, GDPR-ready; hotline product with 100+ languages and three levels of anonymity (bundled module feeding case management).

### Product C — Culture Shift (evidence layer A unless noted)

- Positioning: UK "workplace reporting & compliance platform"; "Take control of workplace misconduct before it becomes a whistleblowing issue." Product: Report + Support™ = reporting + case management + analytics + training/campaigns. Customers skew higher-education/public sector/third sector plus private sector; deployments may cover students as well as employees (higher-ed pages; "workplace or campus misconduct").
- Reporting intake: "Anonymous or named reporting — Give people a safe, trusted way to speak up"; two-way anonymous messaging ("secure, anonymous communication between reporters and case handlers, so critical context can be gathered without breaking confidentiality"); also **support-only** use: "Not only to report, but you can also ask for support through the system" (i.e., intake is not always a formal complaint).
- Case management page: "every report is handled consistently, documented clearly, and tracked from disclosure to resolution."
  - Smart triage: "Automatically route reports to the right team or individual based on risk, type, or location. Prioritise high-risk cases, assign ownership instantly."
  - Workflow management: "Define and enforce your organisation's response process with structured, trackable workflows. Monitor progress in real time, ensure key steps are completed."
  - Audit and case history: "Every interaction, decision, and update is logged in a secure, time-stamped record… fully auditable case history that supports compliance, internal reviews, and external scrutiny."
  - Ownership/prioritization: "Clear ownership, prioritisation, and real-time tracking ensure no case is overlooked."
  - Dashboard (screenshot): report statuses, assigned advisors, roles, time open.
- Analytics: "Name matching & advanced analytics — Identify repeat names, behaviours, and patterns across reports"; real-time visibility into organizational risk; trends "pushed up into committee structures" (customer quote).
- People model: "advisors" / "case handlers" / "case workers" terminology (support-oriented), rather than "investigators."
- Regulatory anchors: UK Employment Rights Act 2025 ("all reasonable steps" to prevent sexual harassment), Worker Protection Act 2023, FCA non-financial misconduct, Office for Students Condition E6, NHS Sexual Safety Charter; compliance-evidence framing ("evidence compliance in practice").
- Problem framing (why the Type exists): inconsistent handling → "unfair or unsafe outcomes"; lack of auditable records → "struggle to evidence how cases were managed"; manual processes → delays, missed steps, cases "falling through the cracks."

### Cross-product Comparison

| Dimension | HR Acuity | Case IQ | Culture Shift | Interpretation |
|---|---|---|---|---|
| Central object | Case record ("every conversation, document, decision, and outcome centralized") | Case record for "sensitive matters" | Report/case tracked "from disclosure to resolution" | **Shared: confidential case record as the central object** |
| What defines a case | Workplace issue handled by ER/HR; allegation category; parties | Sensitive matter; investigation type (HR/ER = harassment, discrimination, retaliation, ER disputes) | Report of misconduct/unwanted behaviour (or support request) | **Shared: reported people-matter with issue typing** |
| Intake channels | Web + phone hotline, named or anonymous, live agents; auto-converts to case record | Web, portal, email, hotline, integrations; guided forms | Named/anonymous web reporting; support requests | **Shared: multi-channel intake, incl. anonymous; intake becomes a case** |
| Anonymity handling | Secure PIN for reporter status; two-way anonymous messaging; consent to convert to investigation | Anonymous + two-way communication | Two-way anonymous messaging; name matching across reports | **Common: anonymity-preserving two-way contact** |
| Triage/routing | Guided workflows; methodology-led | Auto-assign by type, region, severity, workload; escalations | Auto-route by risk/type/location; prioritize high-risk; instant ownership | **Shared: rule-based routing + prioritization + owner assignment** |
| Process structure | Plan → Investigate → Determine (proprietary methodology); guided templates | Configurable workflows per case type/department/country | Structured, trackable workflows; "define and enforce your response process" | **Shared: structured, enforced, standardized process** (specific methodologies are vendor-specific) |
| Investigation tooling | Interview templates/protocols, AI interview questions, timelines | Evidence + notes storage, interviews, findings documentation, AI summaries/timelines | Lighter: case handling, advisors, documentation, audit | **Common: fact-finding support; depth varies by product philosophy** |
| Parties | Reporter, subject, decision-makers handoffs; "guard against retaliation" | Reporter (may be anonymous), subjects; case linking across incidents | Reporter, subject ("repeat names"), advisors | **Shared: party linkage incl. repeat-pattern awareness** |
| Confidentiality/access | Role-based access; attorney-client privilege flag | Role-based access, case visibility settings | "Organised and secure"; auditable records | **Shared: role-restricted access as a structural feature** |
| Audit | "Complete audit trail"; audit-ready for EEOC/legal scrutiny | "Full audit trails for every action and decision" | Time-stamped record of every interaction/decision/update | **Shared: time-stamped audit history** |
| Outcome/determination | Determine findings + stakeholder approvals + course of action | Document findings; close cases | Resolution tracking; outcomes documented | **Shared: documented resolution closes the case** |
| Aftercase follow-up | Retaliation check-ins; ThroughCare™ aftercare task sets | Pattern detection to prevent recurrence (not aftercare per se) | Support avenue; prevention framing | **Common: post-resolution follow-up; depth varies** |
| Analytics | Trends by issue type/unit/geography/time/allegation/resolution; benchmarking | 75+ chart types, dashboards, workload, one-click reports | Trends, hotspots, name/behaviour matching | **Shared: aggregate trend/hotspot analytics as a first-class output** |
| Manager involvement | managER tool for people leaders | HR assigns cases to staff | Advisors/case handlers | **Common: manager/handler surfaces beyond the ER core team** |
| HR system relationship | Integrations incl. Workday partnership | HRIS data sync (Workday, SuccessFactors, BambooHR) for routing/reporting | Not evidenced in fetched pages | **Common: employee population data drawn from HR systems** (C unverified) |
| Case-type breadth | ER-focused + accommodations, PIPs, union grievances, ethics hotline | Very broad: ethics, fraud, security, Title IX, complaints | Misconduct-focused incl. campus (student) misconduct | Breadth is a packaging philosophy, not a defining trait |
| Regulatory framing | EEOC, whistleblower laws (multi-jurisdiction) | FCPA, Title IX, SOC 2/GDPR | UK ERA 2025, Worker Protection Act, FCA, OfS, NHS charter | **Jurisdiction packs are variant-level** (B/C) |
| Packaging | Standalone ER platform (suite of ER modules) | Suite spanning compliance + investigations | Reporting-first platform + training/campaigns | No single packaging shape; all bundle intake + cases + analytics |

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

```text
Reported workplace people-matter
└── Confidential case record (sensitive by design)
    ├── Party & organizational linkage (reporter / subject / witnesses / handler; unit, location, issue type)
    ├── Managed handling process (assigned owner → triage → fact-finding/action → documented resolution)
    └── Retained, attributable history of the handling (who did/decided what, when)
```

Four properties. Remove any one and the Type stops being recognizable:

- **Confidential case record of a reported workplace people-matter** — a complaint, grievance, allegation, conflict, or conduct issue about identifiable people in the organization, held as a discrete structured record. Not public, not a feed, not a knowledge article. Without sensitivity/confidentiality the object degrades into a public tracker or a service ticket.
- **Party & organizational linkage** — the matter binds to the people involved and the organizational context (who reported, about whom, witnesses, where/which unit, what kind of issue). Without party linkage it is a generic issue log.
- **Managed handling process** — the case has an owner and moves through a defined, enforced process (triage/assignment → information gathering / investigation steps → determination) rather than freeform notes. Without this it is a document store.
- **Retained, attributable history ending in a documented resolution** — every action/decision is recorded against the case and the case ends in a recorded outcome. This is what makes the record defensible. Without it, the software cannot serve its purpose (fairness review, audits, legal scrutiny).

Historical check (§24-style): a pre-SaaS union-grievance tracker or an HRIS-held disciplinary log fits these invariants (grievance → parties → steps → outcome, access-restricted). A public bug tracker fails property 1; a help-desk ticket for "reset my benefits password" fails it too (service request, not a sensitive people-matter). The invariants survive era/geography/platform changes.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected in mature products but not definitional:

- **Multi-channel intake** incl. named employee self-reporting (web form/portal), manager-raised entries, and anonymous reporting channels; intake automatically becomes a structured case record.
- **Anonymous-reporter support**: secure status access for anonymous reporters; two-way messaging that preserves anonymity; consent-based escalation of an anonymous report to a formal case.
- **Triage & routing rules**: categorization (issue/allegation type), routing by type/region/severity/workload, risk-based prioritization, instant owner assignment.
- **Task machinery**: tasks with owners and due dates, reminders, notifications, escalation.
- **Fact-finding support**: interview planning/templates/protocols, evidence and document storage, timelines, notes; depth varies (investigation-centric products are deeper).
- **Access & privilege controls**: role-based permissions with per-case visibility; privilege marking (e.g., attorney-client privilege); confidentiality controls.
- **Time-stamped audit trail** of every action/decision/update.
- **Process standardization**: configurable workflow templates per case type / department / geography; "the same process for similar cases" as an explicit goal.
- **Case linking & pattern detection**: connecting related incidents/repeat names/behaviours across cases.
- **Aggregate analytics**: trends by issue type, unit, geography, time; hotspots; repeat-pattern analysis; report/one-click exports for leadership, boards, regulators.
- **Post-resolution follow-up**: retaliation check-ins, aftercare/support task sets (depth varies by product).
- **HR-system integration**: employee/population data synced from HRIS for routing, attribution, reporting; SSO.
- **Manager/handler surfaces**: tools for people leaders or distributed case handlers to raise and progress issues.

### L2 — Variant / Optional Structure

- **Scope breadth**: ER-only platform vs multi-department investigation platform (ethics/compliance, fraud, security, Title IX, ombuds) sharing one case engine.
- **Hotline bundling**: staffed 24/7 multilingual hotline services vs web-form-only intake.
- **Adjacent ER modules**: union grievance handling, workplace accommodations, performance improvement plans.
- **Jurisdiction/sector packs**: US EEOC-oriented documentation; UK Worker Protection/ERA "all reasonable steps" evidence; education-sector regimes (OfS), health-sector charters (NHS); sector deployments (universities include student misconduct).
- **Report vs support intake posture**: formal complaints only vs "report and support" (requests for help/advice that may never become formal cases).
- **AI assistance**: summaries, timelines, interview-question generation, drafting (vendor-specific AI features sit here; AI support itself is becoming common).
- **Benchmarking data services**: peer comparison of case volumes/timelines/outcomes.
- **Packaging**: standalone ER platform; module of a compliance/risk suite; (probable, less evidenced) HCM/HR-service-delivery suite embedding.

### L3 — Vendor-specific Structure (research notes only)

- HR Acuity: proprietary Plan/Investigate/Determine methodology; olivER AI companion; managER; ThroughCare™; Speakfully heritage; ER/Q maturity model; benchmark study.
- Case IQ: Clairia AI assistant; hotline with 100+ languages and three anonymity levels; 30+ intake field types / 75+ chart types; investigative benchmark report.
- Culture Shift: Report + Support™ branding; "advisors" terminology; activation & awareness campaigns; Training Academy; name matching; Culture Shifters annual report.

## Vendor-specific Findings

- The Plan/Investigate/Determine structure is HR Acuity's branded methodology (single-vendor); the underlying "plan the fact-finding → gather facts → decide" arc is a natural shape of the work, but the named methodology must not be presented as the Type's standard.
- Clairia (Case IQ) and olivER (HR Acuity) are branded AI assistants; "AI assistance across the case lifecycle" is a trend, but the specific capabilities are vendor-specific.
- Culture Shift's "support-only" requests (ask for help without reporting misconduct) are a distinctive intake posture; other sampled products center on formal reports.
- Name matching across reports (Culture Shift) vs case linking across incidents (Case IQ) are two product-specific implementations of the same repeat-pattern concern.

## Boundary Findings

| Neighbor | Relationship | Distinction (and "remove what to become the other Type") |
|---|---|---|
| **HR Case Management** (§09 sibling) | sibling / overlapping | HR service delivery frames the employee as a customer raising **service requests** (questions, transactions: address change, policy question, enrollment) resolved against SLAs with knowledge bases; ER case management handles **sensitive people-matters** with investigation logic, fairness constraints, privilege, and defensibility. Remove the sensitive-matter + investigation/confidentiality regime → HR service-request case management; add service-request catalog + tiers + SLAs → HR Case Management. HR Acuity's FAQ states the contrast explicitly ("a help desk queue has no privilege flag, no guided investigation workflow, no way to separate access by role"). Note: some vendors sell both under one HR case-management umbrella — the sibling leaf needs a joint pass. |
| **Whistleblowing / Speak-up Platform** (§11) | upstream intake sibling | Speak-up platforms center on **safe disclosure**: anonymity guarantees, channel coverage, multilingual intake, regulatory compliance for reporting. ER case management centers on the **handled case lifecycle**. In the sample, vendors bundle both (hotline/reporting module → auto-converts to case). Remove the case-handling lifecycle → speak-up platform; remove the anonymous-channel machinery → pure case handling. |
| **Corporate Investigation Management** (§11) | same pattern, different owner/population | Same case/investigation structure applied to corporate/legal matters (fraud, bribery, security) owned by legal/ethics/security functions. Multi-department products (Case IQ) literally share one engine across both. ER case management is the HR-owned slice whose subject is workplace conduct between people in the organization. |
| **HRIS / Employee Record System** (§09) | process layer over the record | The HRIS is the system of record for employment data; ER case systems typically **sync** employee data from it (Case IQ FAQ) and do not manage employment records themselves. Remove the case process → HRIS. |
| **Complaint & Escalation Management** (§07) | analogous shape, different population | Customer-facing complaint handling shares the case pattern but the parties are customers/companies, not employees, and the fairness/employment-law regime is absent. |
| **Business Case Management Platform** (§10) | generic pattern | Generic case management provides record+routing+lifecycle without the ER-specific subject matter, party/fairness semantics, and confidentiality regime. ER CM is a domain instantiation of the case pattern. |

## Uncertainties

- **Evidence tier**: no Tier 1 operational documentation (help-center walkthroughs, field lists, screenshots of case detail pages) was reachable in-sample; all findings rest on Tier 2 official product pages and FAQs. Conceptual structure is well supported; **exact state names, field lists, and numeric parameters must not be asserted** in the final document.
- **Suite embedding**: evidence that ER case management ships as a module inside HCM/HR-service-delivery suites is indirect (integration/partnership claims, the ticketing-vs-case-management contrast). ServiceNow/Workday/NAVEX fetches failed (2 attempts each) — abandoned. Packaging claims kept moderate.
- **Lifecycle state names** vary and were not directly observed; the lifecycle is written conceptually (intake → triage → handling → resolution → aftercare).
- **Post-resolution practices** (retaliation check-ins, aftercare) are evidenced mainly by one product (HR Acuity) — treated as Common-to-Optional, stated with qualification.
- **"Support-only" intake** (Culture Shift) may be broader in the market (ombuds-style) than the sample shows; recorded as a variant with limited evidence.
- **Analytics depth claims** (benchmarking, 75+ chart types, 30+ field types) are vendor marketing figures — kept in Research Notes only.

## Final Synthesis

Employee Relations Case Management is the HR-side case management Type for **sensitive workplace people-matters**. Its defining core is small: a confidential case record about a reported matter involving identifiable people; linkage of that matter to parties and organizational context; an owner-assigned, enforced handling process that moves from intake through fact-finding to a documented resolution; and a retained, attributable history of everything said and done along the way. Around this core, mature products converge on: multi-channel intake (increasingly with anonymous reporting and two-way anonymous messaging), rule-based triage and prioritization, task and deadline machinery, interview/evidence support, role-based access with privilege marking, time-stamped audit trails, case linking and pattern detection, aggregate trend analytics aimed at prevention, and post-resolution follow-up. Scope breadth (ER-only vs multi-department investigations), hotline bundling, jurisdiction packs, sector deployments (universities incl. students), AI assistance, and benchmarking are variant-level. The Type's two sharpest boundaries: against HR service-delivery case management (service requests vs sensitive matters — different objects, different access regime, different stakes) and against speak-up platforms (disclosure channel vs handled case — usually bundled, conceptually distinct).
