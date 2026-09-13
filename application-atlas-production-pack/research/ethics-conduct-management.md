# Research Notes — Ethics & Conduct Management

Research date: **2026-09-06**

## Research Goal

Understand what an Ethics & Conduct Management application actually is as a software type: what objects exist inside it, who operates it, how a conduct situation moves through the system, and where its boundary lies against neighboring directory leaves (Whistleblowing/Speak-up, Corporate Investigation Management, Compliance Policy Management, Compliance Management Platform, GRC Platform, HR/Employee Relations Case Management).

## Initial Boundary (working hypothesis before research)

The leaf sits in directory §11 Legal, Risk, Compliance & Governance, surrounded by siblings that are easy to confuse:

- Whistleblowing / Speak-up Platform (adjacent leaf)
- Corporate Investigation Management (adjacent leaf)
- Compliance Management Platform, Compliance Policy Management (adjacent leaves)
- Governance Risk & Compliance Platform (suite umbrella)
- HR Case Management / Employee Relations Case Management (HR sibling)

Hypothesis: the type is the ethics/integrity *program* platform (code of conduct, conflict-of-interest disclosure, gifts & hospitality registers, attestations, training, program metrics), with speak-up intake and investigations as bundled or neighboring structures rather than the defining center. To be verified against real products.

## Research Questions

1. What are the core objects? (disclosures? cases? policies? attestations? registers?)
2. What is the life of a conflict-of-interest disclosure from submission to outcome?
3. How do gifts & hospitality registers work (entry, thresholds, approvals)?
4. Is the speak-up/hotline channel part of this type or a separate type that gets bundled?
5. Is code-of-conduct attestation defining or common? Where does it stop being this type and start being Policy Management?
6. Who are the users and roles (program owner, reviewers, employees, approvers)?
7. What does the "program" layer contribute (campaigns, analytics, benchmarking, board reporting)?
8. What varies by region/regulation/industry, and what varies only by vendor?

## Representative Products

| Product | Why chosen | Position |
|---|---|---|
| NAVEX (NAVEX One, Disclosure Management, EthicsPoint, PolicyTech) | Largest incumbent; full E&C program suite; hotline heritage (EthicsPoint) | Enterprise |
| SAI360 | GRC suite with explicit ethics module set (Conflicts of Interest, Gifts & Hospitality, Disclosure Management, Code of Conduct, Whistleblower Hotline, E&C Training) | Mid/enterprise, learning-integrated |
| LRN (Catalyst) | Major E&C program platform from a training/advisory heritage — notably **no hotline/incident module** | Enterprise |
| Vault Platform (now Diligent) | Modern challenger positioned as misconduct/speak-up — used as a **boundary-informing** sample | Growth/mid |
| OneTrust (Convercent) | Context sample: ethics-program product line no longer listed in OneTrust's current product catalog (requested URL redirects to generic products page) | Market context only |

## Sources

All fetched 2026-09-06. Vendor product pages (Tier 2). Tier-1 help centers (support.navex.com, my.onetrust.com, SAI360 login areas) were not fetched; operational claims below are therefore calibrated to product-page evidence, and no precise numeric defaults/thresholds are asserted anywhere.

- NAVEX One platform page — https://www.navex.com/en-us/platform/ ✅
- NAVEX COI Disclosure Management — https://www.navex.com/en-us/platform/coi-disclosure-management-software/ ✅
- NAVEX /en-us/products/ethicspoint/ — 404 (replaced by platform + disclosure pages; not retried)
- SAI360 homepage/platform — https://www.sai360.com/ ✅
- SAI360 Gifts & Hospitality — https://www.sai360.com/solutions/compliance-management/gifts-and-hospitality ✅
- SAI360 /solutions/ethics-line/ — 404 (module reachable from nav; not retried)
- LRN Catalyst products — https://lrn.com/products/ ✅
- Vault Platform — https://www.vaultplatform.com/ ✅
- OneTrust ethics-program-management URL — redirected to generic https://www.onetrust.com/products/ page; ethics line absent from current catalog ✅ (used as market-context evidence only)

## Product Observations

### NAVEX — NAVEX One platform + Disclosure Management

Evidence layer: **A (directly observed)** unless noted.

- Platform positioning: GRC platform unifying "speak-up, policy, training, disclosures, risk management and third-party risk on one platform" with a "shared data foundation, security model and reporting layer".
- Product families under NAVEX One: Whistleblowing & Incident Management (EthicsPoint Professional/Essentials, WhistleB), **Disclosure Management (COI)**, Ethics & Compliance Training, Policy & Procedure Management (PolicyTech) + Code of Conduct, Risk & Governance (IRM) + Screening & Monitoring (RiskRate) + Third-Party Risk + Regulatory Change Management.
- Disclosure Management: "receive and monitor potential conflicts of interest (COIs) disclosed by your employees, including gifts, travel and entertainment".
  - Configurable questionnaires "by disclosure type, policy need or employee group"; targeted follow-up questions by disclosure type.
  - "Capture the facts behind a potential conflict to measure risk, not just a yes-or-no answer."
  - Routing: "Send each item to the right reviewer", "Set review paths using combinations of disclosure and employee attributes", assign reviewers, keep supporting documents connected.
  - Request extra detail for incomplete submissions (direct messaging); review-status queue; escalation notifications for incomplete/delayed reviews.
  - In-year updates when circumstances change (outside work, gift, role change, new business relationship); amended responses kept connected to the original disclosure.
  - Annual campaigns + onboarding + "recurring attestations"; employee reminders.
  - Proxy submission by authorized admin with audit trail ("Complete by Proxy").
  - Link related disclosures for reviewer context.
  - Reporting: trends by disclosure type, patterns by employee group/role/location/category, review status and volume, reports for audits/leadership/program oversight.
  - Disclosure types named: conflicts of interest, gifts, entertainment, family connections, outside employment, board roles, vendor relationships.
- Employee side: Compliance Hub portal — submit anonymous reports, access policies and codes of conduct, complete training, ask compliance questions (AI assistant).
- Cross-module narrative: "How a whistleblowing report can reveal a broader pattern of risk → connects to requirements → drive policy and control updates → policy updates shape training and attestations → training reduces repeat issues."
- "Capture and resolve conflict of interest disclosures to reduce hidden internal risks over time."
- COI–ABC link: COIs "involve the same decisions anti-bribery, anti-corruption and third-party controls are designed to protect: who gets business, who approves spend, how vendors are selected."
- Scale claim: 13,000+ customers.

### SAI360 — platform + Gifts & Hospitality / COI / Code of Conduct modules

Evidence layer: **A (directly observed)**.

- Platform: GRC suite, 20+ configurable modules; ethics cluster explicitly present: **Conflicts of Interest, Gifts & Hospitality, Disclosure Management, Code of Conduct, Ethics & Compliance Training, Whistleblower Hotline, Policy Management**, plus non-ethics modules (Enterprise Risk, Incident Management, TPRM, IT Risk, Internal Audit, Regulatory Compliance, Internal Controls, Business Continuity).
- Gifts & Hospitality module: "employees can easily submit disclosures using guided forms, while automated workflows route approvals based on policy thresholds, region, and risk… enforces gift-giving limits, centralizes data".
  - Submit individually or in bulk; conditional fields, validation rules, batch submission.
  - Simplified "Risk Portal" for employees without full system access.
  - Preview impact on gift limits before submission.
  - Giving/receiving limits by value, region, gift type, third-party relationship; auto-approve low-risk submissions; route exceptions to designated reviewers; escalate high-risk items via rule-based workflows.
  - Multi-currency auto-conversion to base currency.
  - Dashboards: submission volume, outliers, high-risk gift types, approval rates, policy exceptions; audit-ready reports.
  - "All gift and hospitality data is stored in a centralized, searchable repository with complete audit trails, submission history, and approval records."
- Conflicts of Interest module: "Streamline conflict disclosure, review, and resolution workflows. Automate monitoring to detect high-risk relationships and activities. Maintain an auditable trail of conflict submissions and actions. Empower employees to disclose conflicts easily to surface hidden conflicts."
- Code of Conduct module: dynamic, branded, interactive code ("150+ flexible and customizable modules built around your risk areas"); "Connect policies, training, and disclosures within the experience"; "Track acknowledgment and reinforce cultural expectations."
- E&C Training: assign learning by role, location, or risk exposure; **embed disclosures within a training course**; monitor completion.
- AI layer: platform dashboard shows "Code of conduct attestation completed %", "Training exposure — risk linked to overdue learning", "Missed attestations increasing people risk" — attestation/training state treated as risk input.

### LRN — Catalyst suite

Evidence layer: **A (directly observed)**.

- Positioning: "LRN Catalyst is a modular suite of ethics and compliance management solutions, purpose-built to help leaders design, deploy, and effectively manage their programs."
- **Catalyst Disclosures**: "simplifies and automates the collection of disclosures and attestations with embedded workflows and customizable templates seamlessly integrated into employee processes. The platform's workflow engine collects additional, contextual information, creating robust compliance audit trails and streamlining tracking." Features: "Automated end-to-end disclosure management; Centralized data tracking and reporting; Customizable disclosure templates and workflow configurations."
- Smart Code of Conduct: code of conduct as an interactive website with "embedded engagement analytics and insights" on how employees interact with the code.
- E&C Culture Assessment (ECCA): survey-based culture measurement across "10 key dimensions".
- Catalyst Reveal: analytics/benchmarking, "continuously benchmark learning efficacies, enhance ethical culture… real-time monitoring and alerting".
- Catalyst Mobile: complete training, access policies/codes of conduct, ask questions.
- Catalyst Supplier: deploy code of conduct + training to third-party suppliers with dedicated instance.
- Catalyst Reach/Design: training delivery and authoring; integrations HRIS (Workday, SuccessFactors, ADP), SSO/SAML/SCIM, SCORM/xAPI/AICC.
- **No hotline/incident-reporting module in the suite** — the platform is training + disclosures/attestations + code + culture + analytics.
- Scale claim: 2,500+ organizations.

### Vault Platform — boundary-informing sample (now part of Diligent)

Evidence layer: **A (directly observed)**.

- Positioning: "Workplace misconduct and Speak Up solution"; "Active Integrity platform".
- Structure: Reporting channels (mobile app, Open Reporting, VaultTalk, GoTogether group reporting, anonymous or identified) + Resolution Hub (case management: "Investigate and quickly manage cases through to resolution, with cross-department collaboration", reporter communication) + Integrity Insights (analytics, "ethical health").
- Use cases: fraud, discrimination, harassment & bullying, bribery, ESG violations, personal safety.
- **No conflict-of-interest / gifts / attestation machinery visible** — the product is the speak-up + case side of the same market.
- Acquired by Diligent (2025); "Book a Demo" links to Diligent One Speak Up.

### OneTrust (Convercent) — market context

Evidence layer: **A (catalog observation)**.

- Requested URL /products/ethics-program-management/ resolves to the generic OneTrust products page; current catalog lists Consent & Preferences, Privacy Automation, AI Governance, Tech Risk & Compliance, Third-Party Management, Data Use Governance — no ethics-program line. Convercent (an ethics-program specialist acquired in 2021) is no longer merchandised as a distinct product family on the current site. Treated as evidence that the ethics-program category is consolidated into broader GRC platforms, and as a caution against citing OneTrust/Convercent as a current representative.

## Cross-product Comparison

| Structure | NAVEX | SAI360 | LRN | Vault | Judgment |
|---|---|---|---|---|---|
| COI/conflict disclosure intake (configurable forms) | ✔ explicit | ✔ explicit | ✔ explicit (Disclosures) | ✖ | **Core (all three E&C platforms)** |
| Gifts/hospitality/entertainment disclosure | ✔ named type | ✔ dedicated module | implied (disclosures generally) | ✖ | Core (as disclosure type; register depth varies) |
| Routing to reviewer + recorded review/outcome | ✔ explicit | ✔ explicit | ✔ explicit | (cases only) | **Core** |
| Durable register / audit trail of disclosures & actions | ✔ | ✔ ("centralized, searchable repository… audit trails") | ✔ ("robust compliance audit trails") | ✖ | **Core** |
| Code of conduct + acknowledgment/attestation | ✔ (Code of Conduct, attestations) | ✔ (Code of Conduct module, attestation dashboards) | ✔ (Smart Code, disclosures+attestations) | ✖ | Common mature structure (near-universal in E&C platforms; standalone disclosure tools exist without it) |
| Training/communication assignment tied to roles | ✔ | ✔ | ✔ (heritage core) | ✖ | Common mature structure |
| Speak-up/hotline intake | ✔ (EthicsPoint) | ✔ (Whistleblower Hotline) | **✖ not offered** | ✔ (the whole product) | Common bundling, **not defining** (LRN counterexample; Vault proves it is its own product cluster) |
| Misconduct case management | ✔ (EthicsPoint case flow) | ✔ (Incident Management / Hotline case mgmt) | ✖ | ✔ (Resolution Hub) | Belongs to speak-up/investigation siblings; bundled here by some |
| Program analytics / benchmarking / board reporting | ✔ (Analytics & Benchmarking, "board-ready insights") | ✔ (Analytics & Reporting) | ✔ (Reveal) | ✔ (Integrity Insights) | Common mature structure |
| Culture measurement | via benchmarking | via AI risk signals | ✔ (ECCA) | ✔ ("ethical health") | Optional |
| Third-party/supplier ethics extension | ✔ (RiskRate, TPRM) | ✔ (TPRM module) | ✔ (Catalyst Supplier) | ✖ | Optional extension toward TPRM |
| Employee self-service portal | ✔ (Compliance Hub) | ✔ (Risk Portal) | ✔ (Mobile) | ✔ (mobile app) | Common mature structure |
| HRIS/SSO integration | ✔ (APIs) | ✔ | ✔ (explicit list) | ✔ (integrations) | Common mature structure |
| Policy threshold enforcement for gifts (limits, auto-approve, currency conversion) | partial (disclosure routing by attributes) | ✔ explicit | not observed | ✖ | Variant/optional (SAI360-depth is product-specific) |
| Proxy/assisted submission | ✔ explicit | not observed | not observed | ✖ | Vendor-specific detail |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The organization-run record system for its conduct/integrity program:

1. **Conduct-situation disclosure intake** — members of the organization declare conduct-relevant situations through structured, configurable forms (conflicts of interest, outside interests/employment, gifts/hospitality/entertainment, family connections, board/vendor relationships).
2. **Routed review with recorded determination** — each disclosure is routed by program-defined rules to a reviewer; the review produces a recorded, attributable outcome (assessed / more info requested / managed / mitigated / accepted / escalated).
3. **Durable program register** — disclosures, amendments, supporting documents and determinations persist as an organization-level, queryable, auditable register over time (the program's system of record).

Removal tests:
- Remove intake→review→register loop → what remains is training/learning delivery (a learning platform) or a policy library (Policy Management). Not this type.
- Remove the register/system-of-record nature → a survey or form tool. Not this type.
- Keep only reporting-channel intake of *others'* misconduct (no self-disclosure registers, no determinations, no program registers) → that is the Whistleblowing / Speak-up Platform.
- The type is organization-scoped (company as the operator) and population-scoped (workforce, optionally extended to third parties).

Note: a pure COI+gifts disclosure tool (no attestation, no hotline, no training) is still recognizably within this type — so attestation/training/hotline cannot be in L0.

### L1 — Common Mature Structure

- **Conduct-standards corpus + attestation**: code of conduct (often as an interactive/branded artifact) and conduct policies distributed to the workforce, with acknowledgment/attestation tracked per person; attestation state feeds program risk views.
- **Recurring campaigns and in-year updates**: onboarding disclosure, annual/periodic disclosure or attestation campaigns, reminders, and in-year updates when circumstances change.
- **Speak-up intake + case handling**: web/mobile/hotline reporting channels (anonymity support), triage → assignment → investigation/resolution, reporter communication. Bundled by some vendors (NAVEX, SAI360, Vault as pure-play); absent in a major platform (LRN).
- **Training & communication**: ethics/compliance course assignment by role/location/risk; disclosures embedded in training flows.
- **Program oversight surfaces**: dashboards (disclosure volume, review status, attestation/training completion, patterns by group/role/region), benchmarking, audit-ready and board-facing reporting.
- **Role model**: program administrator (configures forms/rules/routing), reviewers/adjudicators (ethics officers), employees (disclosers/attesters), managers/approvers, executives/board (reporting), optionally hotline operators.
- **Reminders/escalations** for incomplete or delayed reviews; AI-assisted summaries of submissions.
- **Employee self-service portal** unifying disclosures, policies, training, questions.
- **Integrations**: HRIS (population data), SSO/SAML, SCORM/LMS standards where training is included.

### L2 — Variant / Optional Structure

- Packaging posture: standalone disclosure module vs full E&C program suite vs module inside a broad GRC platform vs speak-up-led platform adding program features.
- Speak-up bundling: in-house hotline vs outsourced call-center operation vs no channel at all.
- Regulatory regime emphasis: US (SOX/FCPA/DOJ expectations), EU Whistleblowing Directive, UK Bribery Act, Sapin II — shapes channels, anonymity, retention, but not the core model.
- Industry overlays: healthcare/pharma (transfer-of-value/sunshine-type registers), government/contractor, financial services.
- Gift-register depth: simple log vs thresholds/limits with auto-approval, pre-submission limit preview, multi-currency normalization.
- Third-party extension: supplier codes of conduct, supplier training, third-party screening/monitoring.
- Culture measurement: survey-based culture assessment; engagement analytics on the code.
- Delivery: SaaS multi-tenant vs on-prem; SMB editions vs enterprise; mobile app depth; language/localization; AI depth (summaries, intake assistance, pattern detection).

### L3 — Vendor-specific (kept out of final document)

- NAVEX: NAVEX One, Nira AI agent, EthicsPoint Professional/Essentials, PolicyTech, RiskRate, WhistleB; "Complete by Proxy"; Compliance Hub; 13,000+ customers claim.
- SAI360: GRC Elevate 6.0; Risk Portal; "150+ code modules"; specific dashboard mock metrics; 5M users / 33% of Fortune 500 claims.
- LRN: Catalyst brand family (Reach, Design, Reveal, Mobile, Supplier, Phishing, AdminAI); Smart Code of Conduct; ECCA "10 key dimensions"; "DOJ-ready reporting"; 2,500+ organizations claim.
- Vault: Active Integrity, GoTogether, VaultTalk, Resolution Hub, Integrity Insights; Diligent acquisition (2025).
- OneTrust/Convercent: ethics line no longer merchandised (2026 catalog observation).

## Vendor-specific Findings

- Threshold/limit enforcement machinery for gifts (limits by value/region/type/relationship, auto-approve, currency normalization, pre-submission limit preview) — documented in depth only by SAI360 → keep qualitative and product-flagged.
- Proxy submission with audit trail — NAVEX only.
- Code-of-conduct engagement analytics (interaction tracking) — LRN Smart Code (and culture dashboards elsewhere) → optional.
- "Embed disclosures within a training course" — SAI360 explicit; consistent with the program-integration philosophy elsewhere → optional pattern.

## Boundary Findings

- **vs Whistleblowing / Speak-up Platform** (sharpest seam): speak-up products center on the *reporting channel + report record + reporter protection + case handling* (Vault: channels + Resolution Hub; NAVEX EthicsPoint as a standalone family; SAI360 Whistleblower Hotline as a distinct module). Ethics & Conduct Management centers on *self-disclosed conduct situations + attestation + program registers*. Proof of seam: LRN is a major E&C program platform with **no** hotline module; Vault is a major speak-up platform with **no** COI/gifts/attestation machinery. Test: remove disclosure/attestation/register machinery and keep the channel → whistleblowing platform; remove the channel → still Ethics & Conduct Management.
- **vs Corporate Investigation Management**: investigation depth (interviews, evidence, case files, findings) is the sibling's center; E&C keeps review at the program level (assessment, management/mitigation decision) and hands deep investigation out.
- **vs Compliance Policy Management / Policy Management**: policy authoring/versioning/approval lifecycle is the sibling; here policies are consumed as the standard being attested to and enforced through disclosure rules.
- **vs Compliance Management Platform**: obligations/controls/regulatory-change machinery is the sibling; E&C is people-conduct-centered. The two coexist inside GRC suites (NAVEX, SAI360), which is why the seam matters.
- **vs Governance Risk & Compliance Platform**: the GRC platform is the suite umbrella; Ethics & Conduct Management is the ethics/employee-conduct slice of it.
- **vs Employee Relations Case Management / HR Case Management**: HR case work (grievances, discipline, accommodation) is employee-relations machinery; E&C cases are conduct-integrity matters handled under the ethics program, often crossing into HR/HRIS data.
- **vs Third-party Risk Management**: supplier codes/screening are extensions; third-party lifecycle management is the sibling.
- Historical check (§24 logic): the category's hotline-era ancestors (e.g., EthicsPoint before platformization; EU-directive-era pure speak-up tools) fit the whistleblowing sibling, not this type — the definition holds because nothing in L0 depends on a hotline, a specific regulation, or a specific era. Spreadsheet-era COI management (pre-software) satisfies the *activities* (disclose, review, register) but not a software application — L0 describes exactly the software envelope around those activities.

## Uncertainties

- Exact attestation-cycle semantics (what re-certification means per product, frequency defaults) — NAVEX documents campaigns/onboarding/recurring attestations qualitatively; per-product defaults were not verified in Tier-1 docs → final document stays qualitative ("periodic campaigns", "at onboarding").
- Whether LRN supports gift/hospitality registers specifically (page says "disclosures" generally) → gifts treated as a common disclosure type, register depth varies.
- Speak-up channel operational details (call centers, language coverage, anonymization mechanics) not researched — owned by the whistleblowing sibling anyway.
- OneTrust/Convercent current status (deprecated vs rebranded vs moved) not confirmed beyond catalog absence.
- Review-outcome vocabularies differ per vendor ("resolve", "manage", "mitigate", "approve") — canonical wording kept generic.

## Final Synthesis

Ethics & Conduct Management is the organization's ethics-program record system: it captures what its people declare about their own conduct-relevant situations (conflicts of interest, outside activities, gifts and hospitality), routes each declaration through a program-defined review that ends in a recorded determination, and keeps the whole trail as durable, auditable registers. Around this loop, mature products add the conduct-standards corpus with tracked attestation, recurring disclosure campaigns, training and communication, commonly a speak-up channel with case handling, program analytics and board reporting, and an employee self-service portal — all organized by an ethics-program role model. Its neighbors own the pieces it only borrows: the reporting channel (whistleblowing platform), the deep investigation (corporate investigation management), the policy lifecycle (policy management), the obligation/controls mapping (compliance management), the suite umbrella (GRC platform).
