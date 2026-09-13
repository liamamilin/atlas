# Research Notes — Financial Compliance Management

Research date: 2026-09-06
Slug: financial-compliance-management
Directory leaf: Financial Compliance Management (§08 Finance, Banking, Insurance & Investment)

## Research Goal

Understand what "Financial Compliance Management" software actually is as an Application Type: what the managed object is, who operates it, what core structures recur across market products, how the compliance work flows, and where the Type's boundaries sit against neighboring Types (generic Compliance Management Platform, Regulatory Reporting, AML, Regulatory Change Management, Ethics & Conduct Management, GRC).

## Initial Boundary

Initial hypothesis (before research):

- Core use: software for regulated financial institutions (broker-dealers, RIAs/asset managers, banks, credit unions, insurers, fintechs) to run their regulatory compliance program — obligations tracking, compliance calendars/tasks, policies, attestations, employee conduct compliance (personal trading, gifts, outside business activities), licensing/registration, breaches, and regulator-facing evidence.
- Users: Chief Compliance Officer and compliance team; employees as compliance subjects; supervisors; internal audit; board.
- Nearest neighbors: Compliance Management Platform (§11, generic), Regulatory Reporting Platform (§08), AML Platform (§08), Regulatory Change Management (§11), Governance Risk & Compliance Platform (§11), Ethics & Conduct Management (§11), HR Compliance Management (§09), Tax Compliance Platform (§08).
- Key open question: is this a distinct Type or merely a finance-vertical variant of the generic Compliance Management Platform?

## Research Questions

1. What is the central managed object — the firm's compliance program? obligations? the employee? policies?
2. What compliance activities are managed (calendars, attestations, certifications, disclosures, preclearances, reviews, cases)?
3. Which finance-specific objects exist (registered persons, brokerage data feeds, restricted lists, MNPI, gifts, political contributions, individual accountability regimes)?
4. How does regulatory change flow into the system?
5. How are violations/issues handled and evidenced?
6. What evidence/reporting is produced, and for whom (board, regulators, exams)?
7. Who are the users and what surfaces do they get (compliance console vs employee portal)?
8. Where are the boundaries vs generic compliance management, regulatory reporting, AML, communications surveillance?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers/segments:

1. **Comply (formerly ComplySci)** — US securities segment (RIAs, wealth managers, broker-dealers, private funds, investment banks, insurance companies). Employee-conduct-heavy + firm program management. Kroll-owned. Rich official product pages.
2. **StarCompliance** — global enterprise financial services (asset managers, broker-dealers, digital asset firms, private equity, banking). Employee conduct + individual accountability regimes (UK/Singapore/Ireland/Australia) + control room. Multi-jurisdictional configurability philosophy.
3. **ACA Group (ComplianceAlpha)** — investment management globally; three-pillar philosophy (advisory + managed services + technology). Explicit regulatory-obligations content library; employee compliance; marketing review; AML checks; eComms; control room.
4. **Ncontracts (Ncomply)** — US banking/credit-union/mortgage/fintech segment. Obligations/regulatory-change-centered compliance management (no employee-conduct pole). Provides the counterweight proving the Type is broader than securities conduct.

Boundary anchors (not primary samples):

- **MetricStream** (generic GRC) — unreachable (403 ×1); boundary argued qualitatively.
- **Smarsh / Global Relay** (communications archiving & surveillance) — not fetched; boundary supported by the sampled products themselves, which treat eComms archiving as a separate module/product line.
- **MyComplianceOffice** — lost sample: mco.com now hosts an unrelated PE portfolio-operations company ("MCO" / Regent). Recorded as market anchor only.

## Sources

All fetched 2026-09-06. Evidence layer A (direct observation) unless noted.

- Comply — https://www.comply.com/ (home), /solutions/employee-compliance/, /solutions/firm-compliance/ (official product pages)
- StarCompliance — https://www.starcompliance.com/ (home; full solutions/platform/who-we-serve navigation)
- ACA Group — https://www.acaglobal.com/ (home), /technology/compliance-oversight/compliance-management/ (product page + FAQ)
- Ncontracts — https://www.ncontracts.com/ (home), /products/compliance-management-software (Ncomply product page + FAQ + case studies)
- compliancealpha.com — JS-rendered SPA, spinner only (1 fetch, abandoned per network rule)
- metricstream.com — 403 (1 fetch, abandoned)
- mco.com — repurposed domain, unrelated company

Sourcing limitation: no help-center / user-guide / operational-manual level documentation was reachable for any sampled product. All evidence is official product pages, solution pages, and vendor FAQs (Tier 2). Consequence: no precise operational defaults, numeric limits, or state-machine details are asserted anywhere; regulatory citations (e.g., SEC Rule 206(4)-7, Reg BI, SMCR) are recorded as vendor-stated alignments, not verified regulation text.

## Product Observations

### Comply (formerly ComplySci)

Positioning: "360-Degree Regulatory Compliance for Financial Services" for RIAs, wealth managers, broker-dealers, private funds, investment banks, insurance companies. [A]

Two named top-level solution pillars: **Employee Compliance** and **Firm Compliance** (plus Communications Archiving as a separate solution). [A]

Employee Compliance: [A]
- Trade Monitoring: direct broker feeds ("industry's largest network of direct broker feeds" — vendor claim), automated preclearance, real-time alerts, monitoring across accounts and asset types (incl. digital assets), complete audit trail for regulators.
- Code of Ethics: administer certifications, attestations, trading, gifts, OBAs; restricted lists, private placements; guided workflows, templates, version control for the code itself.
- Conflicts of Interest: automate preclearance and approvals; track firm initiatives (deals), employee meetings, MNPI access; request/disclosure workflow for employee wall-crossing; add deal-related securities to restricted lists.
- Case Management: central capture/track/resolve of potential violations; configurable role-based routing workflows; full audit trail.
- Reporting & Analytics: customizable dashboards; export reports for stakeholders and regulators.
- Political Contributions Monitoring (pay-to-play): aggregate/monitor public contribution records; automate preclearance; flag and document violations.
- Individual Accountability (SMCR): assign senior manager functions, log roles, track responsibilities; fitness and propriety assessments; certify senior managers; demonstrate firm structure/reporting lines.

Firm Compliance: [A]
- Compliance Calendar: pre-populated tasks tailored to firm type; assignment; ownership and completion visibility; audit-trail reports.
- Risk Assessments: step-by-step risk items; low/medium/high ratings; link policies; export for audits/board/internal analysis.
- Annual Review: guided workflow tied to SEC Rule 206(4)-7 (vendor-stated); documentation builds through the year into a final report.
- Intelligent Policy Builder: draft/update/manage Policies & Procedures, Code of Ethics, Written Supervisory Procedures, AML Manual; version control and edit tracking.
- ComplyAI Policy Guide: plain-language answers sourced from the firm's approved materials, with citations and access controls.
- Best Interest Compliance (Reg BI, vendor-stated): account/product/rollover recommendation comparison tools.

Preclearance UX: employees submit preclearance requests conversationally (Teams/Slack/MCP-connected assistants); every submission evaluated against firm rules and returned approved / denied / routed for manual review, with complete audit trail. [A]

Communications Archiving: WORM-compliant capture/review/store of email, websites, text (iMessage/WhatsApp), social posts — a separate solution line. [A]

Services: registration services, regulatory filings, regulatory compliance consulting, managed services. [A]

Onboarding: data load, configuration, broker-feed outreach and setup, supervisor training; "typical onboarding takes approximately 6-8 weeks" (vendor claim). [A]

### StarCompliance

Positioning: "Compliance, Connected" — employee and firm compliance in one connected platform; real-time trade approval, expenses, risk management. [A]

Employee Compliance (ECOI): [A]
- Conflicts of Interest umbrella with sub-modules: Personal Account Dealing; Crypto Dealing (pre-clearance + post-trade oversight; vendor claims 35+ exchanges, 30+ blockchains, 200+ tokens); Private Investments (declarations for non-publicly traded investments); Gifts & Hospitality (given or received; anti-bribery framing); Outside Business Activities (employee disclosures for external engagements); Political Donations & Activities (pay-to-play thresholds); Firm Trade Surveillance (firm trades vs watch/restricted lists); Sales Compliance Review.
- Broker-Dealer Registration: licensing and registration processes for employees.
- Individual Accountability: SMCR (UK), IAC (Singapore), IAF (Ireland), FAR (Australia) — four named regional regimes.
- Training & Competency: track training, manage certifications.

Firm Compliance (CCR): [A]
- Compliance Control Room: manage conflicts, monitor deal teams, wall-crossing workflows.
- MNPI Management: wall crossings, insider lists, restricted lists.

Platform: Data Management, StarAssist (AI assistant), GuideMe (in-app guides), Reporting & Analytics, Star Mobile, Star Security, Star Technology. [A]

Who: compliance teams ("single, user-friendly system to monitor and manage employee activity and behavior"), HR, technology teams. Financial services: asset managers, broker-dealers, digital asset, private equity, banking. [A]

Positioning themes: on-demand configurability ("respond quickly to new regulations"), multi-jurisdictional support, intuitive UX ("drive employee adoption"), cloud-ready. [A]

Vendor claims (L3): 1.35M users, 500+ clients, 99% retention. [A-claim]

### ACA Group (ComplianceAlpha)

Positioning: "the only end-to-end governance, risk, and compliance partner for financial institutions" — advisory + managed services + technology. Founded by former regulators. [A]

Technology → Compliance Oversight: [A]
- **Compliance Management**: "Digitize compliance calendar and workflows with integrated risk and policy management." Details from product page/FAQ: content library of regulatory obligations and best practices curated by ACA experts (Compliance Content Library); policy management; compliance calendar and activity management; customizable dashboards and reports; link policies to risks and controls; dynamic record linking for change management; audit history; WORM-compliant storage for investigations/resolutions; near real-time activity tracking; supports internal/external audits and regulatory inquiries; manages separate compliance programs (affiliates, jurisdictions) sharing as much or as little framework/data as needed; integrates with transaction monitoring platforms and other GRC tools.
- Marketing and Financial Promotion Reviews: automate review/approval of marketing, sales, promotional materials.
- eLearning and Education: centralize compliance training; IAR continuing education (vendor-stated NASAA rule alignment).
- AML and Sanction Checks: screening module.
- Cybersecurity and Risk Technology.

Technology → Surveillance and Monitoring: [A]
- eComms Capture, Archive, and Surveillance (separate product line).
- **Employee Compliance**: "Manage personal trading, certifications, and conflict disclosures in one platform." ISP (Intelligent Statement Processing) uses AI to extract personal trading data from PDF statements.
- Market Abuse Surveillance; Transaction Cost Analysis; Control Room Compliance (deals, sensitive-data access, permissioned workflows); Research Compliance (expert-call oversight).

Managed Services: compliance operations; reporting and filing (Form ADV, 13F, Form PF, Blue Sky — vendor-stated); surveillance and monitoring; outsourced CCO; mock exams; FCA authorisation support. [A]

Industries: asset managers/investment advisers, broker-dealers, hedge funds, investment companies, private markets, wealth managers. [A]

### Ncontracts (Ncomply)

Positioning: compliance management software for financial institutions (banks, credit unions, mortgage lenders, fintechs, wealth management; US). Part of an integrated risk suite (ERM, vendor, findings, audit, continuity, lending compliance). [A]

Ncomply features: [A]
- Tailored Regulatory Alerts: notifications on regulatory changes with Federal Register summaries, deadlines, and suggested action plans, tailored by organization size, products, services, examiner, geography.
- Regulatory Library: searchable database of guidance documents, US/state rules and laws, industry news (vendor counts: ~5,000 guidance docs, 6,000+ rules/laws, 11,000+ news items — L3).
- Requirements Builder: assess regulatory requirements for new products, services, or business expansions.
- Policy Management: version control, automated reminders, board approval tracking; centralized library; customizable policy templates drafted by compliance experts.
- Complaint Management (Ntelligent): log/investigate/resolve complaints; AI classification of regulatory implications.
- Exam-Ready Reporting: reports for stakeholders, management, and examiners; audit trails; sign-off tabs; citation maps (FAQ).
- Task management, due-date/deadline monitoring, document repository, interdepartmental collaboration (task reminders, progress tracking, assignments).
- Compliance Library: model forms, procedures, checklists, calculators built on regulators' model language.
- Nquiry AI compliance agent: cited, auditable answers; Compliance Concierge expert escalation.

FAQ-defined concept: "A compliance management system (CMS) is a framework financial institutions use to efficiently navigate and manage compliance obligations... It is also a regulatory requirement." [A-claim]

Case studies (L3 claims): 160-hour process → 30 hours; 33% compliance workload reduction; examiner feedback positive.

Notably absent: employee personal trading, gifts, MNPI, individual accountability — the banking pole runs on obligations/policies/tasks/complaints, not employee-conduct workflows.

## Cross-product Comparison

| Dimension | Comply | StarCompliance | ACA ComplianceAlpha | Ncontracts Ncomply |
|---|---|---|---|---|
| Segment | US securities (RIA/BD/funds) | Global enterprise financial services | Global investment management | US banks/CUs/mortgage/fintech |
| Center of gravity | Employee conduct + firm program | Employee conduct + accountability regimes | Obligations + conduct + services layer | Obligations / regulatory change + policies |
| Employee as compliance subject | Core (named pillar) | Core (named pillar) | Core (named module) | Not central |
| Explicit obligations register | Implicit (calendar + policies) | Implicit (workflows + configurability) | Explicit (Content Library) | Explicit (Regulatory Library + Requirements Builder) |
| Regulatory change feed | Yes ("address new regulations") | Yes (configurability posture) | Yes (CCL continuously updated) | Yes (tailored alerts + action plans) |
| Compliance calendar / tasks | Yes (pre-populated) | Workflows | Yes (calendar + activity mgmt) | Yes (tasks, deadlines, reminders) |
| Policy governance | Yes (builder, version control) | Implicit in workflows | Yes (policy mgmt, linked to risks/controls) | Yes (version control, board approval) |
| Attestations / certifications | Yes | Yes (training/certifications) | Yes | Not emphasized |
| Personal trading / preclearance | Yes (broker feeds) | Yes (incl. crypto) | Yes (incl. AI statement processing) | No |
| Gifts / OBA / political contributions | Yes | Yes | Via managed services | No |
| MNPI / control room | Yes (COI module) | Yes (Control Room + MNPI) | Yes (Control Room) | No |
| Individual accountability regimes | SMCR | SMCR/IAC/IAF/FAR | — | — |
| Licensing / registration | As a service | Yes (BD Registration module) | As a service | — |
| Marketing / promotion review | — | Sales Compliance Review | Yes | — |
| Compliance training | — | Yes (Training & Competency) | Yes (eLearning) | Knowledge-base videos |
| Risk assessment of program | Yes | — | Yes (risks ↔ controls) | Via sibling Nrisk |
| Case / violation handling | Yes (Case Management) | Via workflows | Investigations (WORM) | Complaints |
| Exam/evidence posture | Audit trail, exam ready | Audit-ready | Audit trail, WORM storage | Exam-ready, examiner-facing reports |
| Services layer | Registration/filings/consulting | — | Advisory/managed/OCCO/mock exams | Services |
| AI | Policy Guide, MCP preclearance | StarAssist | Encore AI, ISP, AI Insights | Nquiry, Complaint Ntelligence |

### Stable commonalities (evidence layer B)

Across all four products:
1. The managed thing is the **firm's compliance program** — a firm-scoped container, not an individual's and not a product's.
2. **Tracked compliance activities** with ownership, deadlines, completion status (calendar/tasks/workflows) — universal.
3. **Auditable evidence posture** — every product explicitly sells the audit trail / exam readiness / regulator-facing reporting.
4. **Regulatory change as an input** that must update the program (policies, requirements, tasks).
5. **Policies as governed documents** (explicit in 3 of 4; embodied in workflow rules in the 4th).
6. **Employee population as a governed registry** (all four manage people-related compliance, though only securities-facing ones run conduct workflows on it).
7. **Reporting upward and outward** — dashboards for the compliance team, reports for management/board, exports for regulators/examiners.

### Poles (evidence layer B)

- **Conduct pole** (Comply, Star, ACA): the employee as compliance subject — personal trading with preclearance and broker data feeds, gifts & hospitality, outside business activities, political contributions, COI/MNPI, individual accountability, licensing.
- **Obligations pole** (Ncontracts, ACA's Compliance Management module): regulatory change → requirements → policies → tasks → exam-ready evidence.

Both poles share the same program machinery (activities, policies, evidence). The poles differ in what is being complied with: conduct rules binding individuals vs regulatory obligations binding the firm.

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the software stops being financial compliance management:

1. **Firm-scoped regulatory compliance program as the managed object** — the system of record for a financial institution's compliance program, anchored in obligations imposed by financial regulators.
2. **Tracked compliance activities** — recurring and event-driven compliance work (tasks, reviews, attestations, disclosures) assigned to owners, deadline-tracked, and driven to recorded completion.
3. **Auditable compliance evidence** — actions, decisions, and outcomes preserved as an attributable, retrievable record whose audience is the regulator/examiner (the "prove it" posture).

Remove the financial-regulatory context → generic work management. Remove tracked activities → a document library. Remove the evidence posture → ordinary workflow tooling. Remove any of the three → no longer recognizable as this Type.

### Level 1 — Common Mature Structure

- Policy / code-of-ethics governance (versioned documents, approval, attestation)
- Compliance calendar of recurring obligations and deadlines
- Regulatory change monitoring feeding obligations → activities
- Employee as compliance subject: personal trading (preclearance + post-trade monitoring via broker feeds), gifts & hospitality, outside business activities, political contributions, conflicts-of-interest disclosures
- Attestation / certification campaigns with outstanding-tracking and follow-ups
- Restricted / watch / insider lists as shared reference data
- Compliance risk assessment linked to policies/controls
- Case management for potential violations
- Reporting/dashboards for CCO, management, board; regulator-facing exports
- Compliance training tracking
- Licensing / registration tracking of regulated persons
- Marketing / financial-promotion review
- Employee self-service portal (disclosures, requests, attestations, training)

### Level 2 — Variant / Optional Structure

- Individual accountability regimes (SMCR UK, IAC Singapore, IAF Ireland, FAR Australia) — regional
- MNPI / control-room machinery — deal-driven firms (investment banks, brokers, private funds)
- Annual-review tooling tied to SEC Rule 206(4)-7 — US adviser-specific
- Best-interest / fiduciary recommendation comparison — US broker-dealer-specific
- Communications archiving & surveillance integration — adjacent module/product line
- AML / sanctions screening integration — module or managed service
- Complaint management with regulatory classification — banking pole
- Multi-jurisdiction / multi-program (affiliate) structures
- Managed services / advisory bundling (OCCO, filings, mock exams) — services-led packaging
- Segment packaging (RIA vs BD vs bank vs asset manager vs fintech)
- AI assistance (policy Q&A, conversational preclearance, statement processing, complaint triage)
- Vendor-maintained regulatory content libraries as substrate

### Level 3 — Vendor-specific (research notes only)

- Comply: ComplyAI MCP Server (preclearance in Teams/Slack/Claude/ChatGPT), illumis (political contributions), ComplianceGuardian (formerly NRS), AccountCompare/PeerCompare/RolloverAnalyzer, 6–8 week onboarding claim, "industry's largest network of direct broker feeds" claim.
- StarCompliance: StarAssist, GuideMe, Star Mobile, crypto coverage numbers (35+ exchanges / 30+ blockchains / 200+ tokens), 1.35M users / 500+ clients / 99% retention claims, ETHIX360 heritage.
- ACA: ComplianceAlpha platform name, Master Content Library / Compliance Content Library, Encore AI, ISP (Intelligent Statement Processing), Pre-Call Screening, Ethos (ESG), Vantage (cyber), Mirabella (FCA), 1,400+ professionals / 6,350+ clients claims.
- Ncontracts: Nquiry, Ntelligence, Complaint Ntelligence (90%+ accuracy claim), Compliance Concierge, library counts (~5,000 / 6,000+ / 11,000+), case-study stats (160→30 hours, 33% workload).

## Rejected Findings

- **"Financial compliance management = regulatory reporting."** Rejected. In the sampled products, filing production appears as managed services (ACA "Reporting and Filing", Comply "Regulatory Filings") or sibling systems; the compliance platform tracks filing deadlines in the calendar but does not center on producing filings. Regulatory Reporting remains a separate Type.
- **"Financial compliance management = AML transaction monitoring."** Rejected. Detection/screening appears only as an integrated module (ACA AML & Sanction Checks), a policy artifact (Comply's AML Manual in the policy builder), or a managed service. The compliance program wraps detection; it is not detection.
- **"Employee conduct compliance is the defining core."** Rejected at L0. The banking pole (Ncontracts) operates a full compliance-management product without employee-conduct workflows. Conduct is the dominant L1 pole in securities-facing products, not the invariant.
- **"This is just generic GRC with finance branding."** Rejected. The finance-specific object set (registered persons, brokerage data feeds, restricted lists, MNPI/insider lists, individual accountability regimes, pay-to-play) and the regulator-exam evidence posture are structural, not cosmetic. (MetricStream unreachable — boundary argued from sample; kept qualitative.)
- **"Compliance management software replaces the compliance function."** Rejected. Vendors pair software with advisory/managed services (ACA explicitly; Comply services; Ncontracts expert content); the system records and coordinates human compliance work; determinations remain human.

## Boundary Findings

1. **vs Compliance Management Platform (§11)** — closest boundary. Shared machinery: obligations, controls, activities, audits, training. Distinction: this Type is the finance-domain instance — obligations come from financial regulators, evidence is built for financial-regulator exams, and finance-specific conduct objects (registered persons, personal trading, MNPI, gifts, individual accountability) are first-class. Generic compliance management lacks the conduct-object layer and the exam posture. **Joint-review flag**: §11 sibling unprocessed; the two leaves are genuinely close and the market sells both shapes under similar names.
2. **vs Regulatory Reporting Platform (§08)** — filings production vs program management. Calendar tracks filing deadlines; production of filings is a service or separate system.
3. **vs AML Platform (§08)** — detection/screening of financial crime vs management of the compliance program. AML appears here as policy, module, or service.
4. **vs Regulatory Change Management (§11)** — the change feed is an input here (alerts → requirements → tasks); RCM as a Type centers on the change-tracking slice itself.
5. **vs Ethics & Conduct Management (§11)** — gifts/COI/attestation overlap is real, but here those objects are anchored in securities codes of ethics, market-abuse risk, brokerage data, and registered-person status; ethics platforms serve the generic corporate ethics program.
6. **vs Communications archiving/surveillance (Smarsh/Global Relay category; no directory leaf)** — capture/archive/review of eComms is a separate product category; sampled products bundle it as a distinct module (Comply) or separate product line (ACA).
7. **vs HR Compliance Management (§09)** — employment-law compliance vs financial-regulatory compliance; different obligation domains, different regulators.
8. **vs GRC Platform (§11)** — umbrella vs finance slice; financial compliance management is one program domain inside a GRC estate.
9. **vs Tax Compliance Platform (§08)** — tax domain vs financial-conduct/prudential domain.

"Remove X → becomes another Type" tests:
- Remove the financial-regulatory context → generic Compliance Management Platform (§11).
- Remove the program machinery (activities/evidence) and keep detection → AML/surveillance platform.
- Remove employee-conduct objects → obligations-centered compliance management (banking pole still fits — so conduct is not defining).
- Remove the firm scope → no recognizable Type (a personal compliance tool is not a market category).

## Uncertainties

- No help-center/user-guide access for any sampled product; all claims are product-page/FAQ level. No numeric limits, default values, or state names asserted in the final document.
- Regulatory citations (SEC 206(4)-7, Reg BI, SMCR, NASAA IAR CE, pay-to-play rules) are vendor-stated alignments; regulation text not independently verified.
- Insurance-sector compliance management (NAIC-style) not sampled; likely fits the L0 but unverified — noted as a segment gap.
- MetricStream (generic GRC anchor) unreachable; the §11 boundary rests on the sampled products' own framing plus category reasoning.
- MyComplianceOffice lost to domain repurposing; the securities-conduct category is evidenced by three products instead of four.
- Exact relationship between "compliance calendar" content and vendor-maintained obligation libraries (pre-populated vs self-built) varies by product and could not be pinned down.

## Final Synthesis

Financial Compliance Management is the finance-domain compliance-program system of record. Its defining core is small: a firm-scoped compliance program, tracked compliance activities, and an auditable evidence trail for regulators. On top of that core, mature products add two recognizable poles: (1) the conduct pole — the employee as compliance subject, governed through disclosure, attestation, preclearance, and monitoring workflows fed by brokerage data and restricted lists; and (2) the obligations pole — regulatory change converted into requirements, policies, tasks, and exam-ready evidence. Regional accountability regimes, deal-driven control rooms, communications-surveillance integration, and services-led packaging are variants. The Type is distinct from generic compliance management by its financial-regulator context and finance-specific conduct objects, and distinct from detection Types (AML, surveillance) by managing the program rather than the transactions.
