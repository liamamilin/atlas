# Research Notes — Employee Survey Platform

Research date: 2026-09-06
Cross-references: research/employee-engagement-platform.md §Boundary Findings #1 (flags this leaf for joint review: "every sampled engagement platform contains a full survey engine; the differentiator is the workforce program frame — a superset/capability gradient, not a wall"); applications/employee-engagement-platform.md (sibling final doc, processed 2026-09-06).

## Research Goal

Determine what an Employee Survey Platform is as an Application Type: its minimal defining structure, its standard mature capabilities, its variants, and — critically — its position between two already-processed neighbors: the generic **Survey Platform** (§03.11 Forms & Data Collection) and the **Employee Engagement Platform** (§09 sibling, processed earlier the same day). Resolve the joint-review flag recorded in STATUS.md line 263.

## Initial Boundary

Working hypothesis before research:

1. Core use: authoring and running questionnaires aimed at an organization's employees, collecting responses, producing results.
2. Users: HR/people teams as operators; employees as respondents; managers as scoped consumers.
3. Nearest neighbors: Survey Platform (generic instrument), Employee Engagement Platform (workforce program frame), Online Form Builder, Polling Application, Voice of Customer Platform, 360/performance tooling.
4. Likely confusion: the market mostly sells "employee survey software" under engagement framing; the leaf may be an audience variant of Survey Platform or a subset of Employee Engagement Platform.
5. Unknowns: whether any structural machinery is unique to the employee context (vs. generic survey tools), and where the engagement frame starts.

## Research Questions

1. What is the central object, and what lifecycle does it carry (draft → live → closed)?
2. How are respondents addressed: open links, contact lists, or an employee roster? Is participation tracked against a population?
3. What does authoring look like (question types, templates, logic, translations)?
4. What distribution channels exist (email, link, SMS, kiosk, embed, mobile)?
5. How is anonymity handled — collection toggle, launch-time format choice, or reporting-engine protection?
6. What is genuinely employee-specific: HRIS sync, lifecycle survey types (onboarding/exit/pulse), manager-scoped reporting?
7. Where exactly does the engagement program frame (index/driver/benchmarks, action loop) begin?
8. Where is the wall vs. generic Survey Platform, Form Builder, Polling, VoC?

## Representative Products

Selected for market representation, documentation quality, and spread across product philosophies and customer tiers:

| Product | Pole | Tier |
|---|---|---|
| SurveyMonkey | generic survey instrument; employee feedback is one use case among many | self-serve SMB→enterprise |
| Qualtrics (Survey Platform / CoreXM) | research-grade survey engine; employee solutions layered above | enterprise |
| Culture Amp | employee-science pure-play; survey machinery embedded in an engagement frame | mid-market→enterprise |
| TINYpulse (by WebMD Health Services) | lightweight pulse-first engagement product | SMB→mid-market |
| QuestionPro (Workforce / Employee Experience) | survey vendor with a dedicated workforce line above a generic engine | SMB→enterprise |

## Sources

Tier 1 (official operational documentation) unless noted:

- SurveyMonkey Help Center root: https://help.surveymonkey.com/en/ (fetched 2026-09-06)
- SurveyMonkey — Making Responses Anonymous: https://help.surveymonkey.com/en/send/collecting-responses/anonymous-responses/ (fetched 2026-09-06; article body extracted)
- SurveyMonkey — Employee Feedback use case: https://www.surveymonkey.com/use-cases/employee-engagement/ (fetched 2026-09-06; Tier 2)
- Qualtrics Support — Getting Started with Surveys: https://www.qualtrics.com/support/survey-platform/getting-started/survey-platform-overview/ (fetched 2026-09-06)
- Qualtrics Support home (module structure): https://www.qualtrics.com/support/ (fetched 2026-09-06)
- Culture Amp Support Guide — Survey Classification Types (full Survey Admin Hub navigation tree): https://support.cultureamp.com/en/articles/7048335-survey-classification-types (fetched 2026-09-06)
- TINYpulse product page (WebMD Health Services): https://www.tinypulse.com/ (fetched 2026-09-06; Tier 2)
- TINYpulse Support Center structure: https://tinypulse.zendesk.com/hc/en-us (fetched 2026-09-06)
- QuestionPro Workforce / Employee Experience page incl. FAQ: https://www.questionpro.com/workforce/ (fetched 2026-09-06; Tier 2 — product page + FAQ, not deep help-center articles)
- Sibling-pass sources reused as cross-referenced evidence: Culture Amp Confidentiality Protections in Reporting, Understanding Pulse Surveys; Workday Peakon help center structure; Qualtrics Employee Experience product page (see research/employee-engagement-platform.md §Sources)

## Product Observations

### SurveyMonkey (evidence layer A for structure; A for anonymity article)

- Employee feedback is packaged as a **use case** (`/use-cases/employee-engagement/`, titled "Employee Engagement Survey Platform") alongside Customer Satisfaction, Event Feedback, Registration Forms, Market Research, NPS. HR is one "role" page among Marketing/CX/IT. 360-Degree Employee Evaluation is one template among "400+ templates". → the generic instrument with the workforce as an application area, not the product's frame.
- Help center structure: create surveys, collect responses (collector types: web links, email invitations, others, respondent authentication), analyze results.
- **Anonymity (direct, article-level)**: "The Anonymous Responses collector option lets you choose whether or not to track and store identifiable respondent information in survey results." It is a per-collector setting that must be turned on **before** sending; "it's not possible to make existing responses anonymous. Changing the setting only applies to new responses." Email invitations track email/IP/name/custom data by default; anonymous mode excludes respondent information (two exclusion levels observed). IP addresses are recorded in backend logs and deleted after a fixed retention period (13 months stated).
- No engagement program frame observed at the core-product level (no action plans, no engagement index machinery in the surveyed help structure).

### Qualtrics — Survey Platform / CoreXM (evidence layer A)

- Support structure: "Getting Started with Surveys" describes the **survey project** as the foundational project type in a catalog of project types; a survey project contains: **Survey tab** (create questions, customize what respondents see, quotas, access control, publish/versions, preview), **Workflows tab** (automations, e.g. trigger a follow-up survey days after completion, or create a ticket), **Distributions tab** (send via email, SMS, or "a single, anonymous link"; contact lists may be created first), **Data & Analysis tab** (individual responses, edit, export), **Results tab** (dashboard of results; buildable dashboard pages with charts/filters), **Reports tab** (paginated, PDF-friendly reports).
- Sharing/permissions: projects can be shared; tab access is permission-controlled; some features are license/add-on gated.
- The same engine underlies "XM for Strategy & Research" and "XM for Employee Experience" (support home offers both as separate getting-started tracks; Employee Experience projects are a distinct project creation path). → engine + solution layering, directly observed.
- EmployeeXM specifics were NOT fetched this pass (sibling pass recorded product-page-level evidence only).

### Culture Amp (evidence layer A — richest employee-context machinery)

Survey Admin Hub navigation (directly observed):
- **Managing a Survey**: Surveys and Programs page; Programs; Create a Survey; Duplicate; "Understanding the Impact of Editing Survey Questions After Launch"; Resend Survey Invitations and Reset Responses; Update Demographics in an Attributed Survey; Close the Survey; Reopen a Closed Survey; Delete; Archive; Authenticated Capture for Surveys.
- **Survey Classification and Formats**: "Attributed and Unattributed Survey Formats"; "Survey Classification Types" (classification of surveys by purpose).
- **Question Design**: Question Types Used in Surveys; branching logic; demographic branching; mandatory questions; Likert response formats; multilingual surveys; question import; display rules; driver questions ("The Science Behind our Driver Questions").
- **Demographics**: choose demographics before launch; self-reporting demographics; demographic piping; import/prepare demographics.
- **Participants**: add participants before launch; bulk upload; adding participants to a launched survey; **Kiosk Mode** "for employees without designated email addresses or computers" + kiosk codes; invitation status of participants.
- **Confidentiality**: Confidentiality Protections in Reporting; Report Filters; Raw Data Extracts (with required warning text; de-identified extracts on request; enabling raw data on a survey).
- **Communications**: survey invites; scheduled reminders; SMS invitations; sender name; communication variables.
- **Launching**: separate guides for launching attributed vs unattributed surveys.
- **Results**: how scores are calculated; trend for surveys and programs; heatmaps; impact/driver analysis; correlation; AI comment summaries/comparisons; text analytics; export to PowerPoint.
- **Benchmarks & Comparisons**: benchmark insights; comparisons; importing historical/external comparisons.
- **Sharing Reports**: report sharing with viewers/owners; filtered reports; **leader-based hierarchy reports**; participation reports.
- **Employee data (population)**: Create Your Employee Data File; Import Employee Data; hierarchy upload; deactivated vs former employees; HRIS integrations (Workday, BambooHR, Dayforce, Paylocity, HiBob, Personio, Namely, Gusto, ADP, SAP SuccessFactors, UKG, and more — direct sync, SFTP, API); SSO (SAML via Okta/Entra ID/Google/Ping); Slack/Teams apps.
- Interpretation: the full employee-survey machinery (population, formats, confidentiality, participants, channels, results) exists here as the substrate of an engagement-framed product. The engagement layer (index, drivers, benchmarks, action plans — Platform Actions Plans Page also observed) sits on top.

### TINYpulse (evidence layer A for structure; Tier 2 for positioning)

- Product page (WebMD Health Services): "employee engagement and pulse survey platform"; feature list: Pulse Surveys, Peer Recognition (Cheers), Anonymous Feedback, 1-on-1 Coaching Tools, Action Planning. Modules: Engage, Coach, Onboard, Retention.
- Support center structure (direct): **Engage** — "Create, Schedule, and Organize Engage Surveys" (question sets provided by TINYpulse or custom surveys; scheduling); "Setting up a Themed Series" (collections of surveys measuring a larger theme); "Survey Responses for Managers" (managers view results for direct and indirect reports); **Automated Exit Surveys** (schedule/send exit surveys automatically; deactivate leaving employees); Announcements; Custom Branding.
- Interpretation: pulse-first lightweight product; survey engine (scheduling, question sets, manager-scoped results, automated lifecycle triggers) plus engagement add-ons (recognition, coaching).

### QuestionPro — Workforce / Employee Experience (evidence layer B; Tier 2 product page + FAQ)

- Product family: Survey Software, Research Suite, CX, **Employee Experience** — one survey engine under multiple solution lines; also a dedicated `/employee-survey-software.html` page ("create, send and analyze employee surveys... map your employee experience from onboarding to exit").
- FAQ (direct quotes): "QuestionPro Employee Experience is an employee survey and analytics platform that helps organizations measure, understand, and improve the employee journey from hire to exit. It combines engagement surveys, pulse surveys, 360-degree feedback, people analytics dashboards, and action planning in one platform."
- Lifecycle coverage: "You can run onboarding, engagement, pulse, culture, 360-degree leadership feedback, and exit surveys from a single platform."
- Anonymity: "Respondent Anonymity Assurance, a confidential demographics roster, and role-based data access so individual responses can never be traced back to an employee."
- Population: "connects to your HRIS through FTP and API-based employee roster integration, keeping demographics current and survey distribution automatic."
- Action layer: "Empower Action Planning"; key driver analysis; eNPS tracking; role-based dashboards.
- Interpretation: same layering as Qualtrics/Culture Amp — generic survey engine + workforce solution line; the workforce line carries the program frame.

## Cross-product Comparison

| Structure | SurveyMonkey | Qualtrics | Culture Amp | TINYpulse | QuestionPro WE | Layer |
|---|---|---|---|---|---|---|
| Authored survey as central object w/ lifecycle | A (collectors/publish) | A (survey project, publish/versions) | A (create/duplicate/close/reopen/archive) | A (create/schedule) | B | B |
| Respondents addressed as a managed list/population | A (email invitations track contacts) | A (contact lists) | A (participants, bulk upload, HRIS) | A (employee base; exit automation deactivates leavers) | B (HRIS roster integration) | B |
| Participation tracking & reminders | A (email invitation tracking) | A (distributions) | A (invitation status, reminders) | B (implied) | B | B |
| Question editor + types + logic | A | A (question types guide) | A (question types, branching, display rules) | A (custom + provided sets) | B | B |
| Templates / question banks incl. HR purposes | A (400+ templates incl. 360) | A (survey library) | A (curated templates, classification) | A (provided question sets, themed series) | B | B |
| Anonymity as pre-launch design decision | A (collector option, pre-send, not retroactive) | A (anonymous link distribution) | A (attributed vs unattributed launch formats) | B (anonymous feedback feature) | B (Anonymity Assurance) | B |
| Confidentiality-protected reporting (thresholds) | — (not observed) | — (not observed at core) | A (protections in reporting, raw-data gating) | — (not observed) | B (role-based access claim) | B (employee-specialized products) |
| Multi-channel distribution (email/link/SMS/kiosk/embed) | A (collector types) | A (email/SMS/anonymous link; offline app) | A (email/SMS/kiosk/Slack/Teams) | B | B (Teams/Slack integrations) | B |
| HRIS/directory sync for population | — (not observed) | — (contacts generic) | A (extensive HRIS/SFTP/API) | B (integrations category) | B (FTP/API roster) | B (employee-specialized) |
| Lifecycle survey types (onboarding/exit/pulse) | B (templates) | B (EX project track) | A (pulse; lifecycle via programs) | A (Onboard module; Automated Exit Surveys) | B (onboarding→exit) | B |
| Results: per-question summaries, trends, exports | A | A (Data & Analysis, Results dashboards) | A (scores, trend, heatmaps, exports) | A (Survey Responses for Managers) | B (dashboards) | B |
| Manager-scoped results | — (not observed) | B (project sharing) | A (leader-based hierarchy reports, viewers/owners) | A (managers see direct/indirect reports) | B (role-based dashboards) | B |
| Engagement index / driver analysis / benchmarks | — | — (EX layer, not core) | A | B (drivers via reports) | B (key driver analysis, eNPS) | B (program frame) |
| Action planning / follow-up loop | — | — (Workflows automation only) | A (Actions Plans page) | B (Action Planning feature) | B (Empower Action Planning) | B (program frame) |
| Research-grade methods (quotas, randomization, panels) | A (audience panel; quotas in help structure) | A (quotas, screening) | — | — | B (Research Suite line) | B (generic-instrument pole) |

Reading: the **instrument loop** (author → distribute/collect → results) is universal. The **workforce machinery** (population management, participation tracking, anonymity formats, HR-lifecycle survey types, manager scoping) is common and concentrated in employee-specialized products. The **program frame** (engagement analytics + action loop) appears only in products that also sell engagement — it is the sibling Type's defining layer, not this Type's.

## Canonical Abstraction

### L0 — Defining Invariant

```text
Authored survey (question set as the central managed object)
└── addressed to the organization's employees (respondent population)
    └── distribution & response collection (tracked participation)
        └── aggregated results (responses compiled into readable results)
```

Four properties. Remove any one and the product stops being recognizable as this Type:

1. **Authored survey** — a questionnaire (questions, response options, structure) is the unit of work. Without it there is no survey product.
2. **Employee respondent population** — the survey is addressed to the organization's own workforce as its audience, and results are read against that employment context. Without it the product is a generic Survey Platform.
3. **Distribution & response collection** — the platform delivers the survey and captures responses; participation is commonly tracked against the population. Without it the survey is not operational.
4. **Aggregated results** — responses are compiled into per-question and overall results the survey owner can inspect and export. Without it the loop has no output.

§24 historical check: paper-based employee census surveys (HR distributes to a known roster, collects forms, tabulates results) satisfy all four; HCM-embedded survey modules satisfy them with the population sourced in-suite; early web survey tools used by HR satisfy the loop with loosely-maintained populations. Therefore the definition must NOT require: digital channels, HRIS sync, anonymity thresholds, engagement analytics, AI, pulse cadence, or any specific survey science. All of those are L1/L2.

### L1 — Common Mature Structure

- Question editor with question types (multiple choice, rating/Likert scales, NPS/eNPS-style, open text, demographic) and logic (branching, display rules, mandatory questions)
- Templates and curated question banks, including HR-purpose sets (engagement, pulse, onboarding, exit, 360)
- Anonymity as a pre-launch design decision: attributed vs anonymous/unattributed formats; in employee-specialized products, reporting-engine-level confidentiality protections (minimum-response thresholds, gated/de-identified raw data)
- Participant/population management: bulk upload, HRIS/directory sync, hierarchy, invitation status, non-responder targeting
- Multi-channel distribution: email invitations, web/anonymous links, SMS, kiosk mode, collaboration-suite embeds, mobile/offline apps
- Reminders and participation tracking
- Survey lifecycle management: draft → live → closed, with reopen/archive/delete and edit-after-launch warnings
- Results views: per-question summaries, trend across rounds, filters, exports (CSV/PowerPoint/PDF)
- Multi-language surveys
- Roles and scoped access: admins, survey owners, managers (scoped results), respondents
- Scheduling and recurring programs (pulse cadences, themed series, event-triggered surveys such as automated exit surveys)

### L2 — Variant / Optional Structure

- Engagement program analytics: engagement index, driver/impact analysis, benchmarks (the Employee Engagement Platform's defining layer)
- Action planning / follow-up loop and manager toolkits
- Always-on anonymous feedback channels and continuous-listening posture
- 360/multi-rater evaluation programs (straddles Performance Management)
- AI assistance (survey generation, comment summarization, sentiment/themes)
- Research-grade methods: quotas, respondent screening, randomization, panel sampling (the generic/research pole)
- Offline/kiosk modes for deskless workers (L1-adjacent; presence varies)
- Workflow automation (trigger follow-up surveys, create tickets)
- White-label/branding, incentives, custom variables

### L3 — Vendor-specific (stays out of the final document)

- SurveyMonkey: collector model (web link / email / other collectors), two-level anonymous exclusion, 13-month IP retention, use-case packaging, Audience Panel
- Qualtrics: project/tab architecture (Survey / Workflows / Distributions / Data & Analysis / Results / Reports), contact lists, license-gated features, Brand Administrator roles
- Culture Amp: survey classification system, authorization codes for unattributed surveys, kiosk codes, raw-data warning text, Focus agent, demographic piping, benchmark import templates
- TINYpulse: Engage/Coach/Onboard/Retention module split, Themed Series, Cheers for Peers, Suggestions
- QuestionPro: Respondent Anonymity Assurance (branded), unlimited-users pricing posture, OPTM360, Empower Action Planning

## Vendor-specific Findings

See L3 above; none promoted to the canonical document.

## Boundary Findings

1. **vs Employee Engagement Platform (sibling leaf — JOINT REVIEW RESOLVED)**. Confirmed: capability gradient, not a wall. The engagement platform = this Type's instrument machinery **plus** the workforce program frame (employee population with confidentiality machinery as defining structure, engagement analytics, action loop, listening posture). Directional tests: remove the program frame (index/driver/benchmarks + action loop + listening posture) from an engagement platform → an Employee Survey Platform remains; remove the workforce orientation from an Employee Survey Platform → a generic Survey Platform remains. Both leaves are definable; no taxonomy change. **Refinement of the sibling's test**: the sibling phrased the test as "remove the workforce population and the action loop → an Employee Survey Platform remains", which conflates this leaf with the generic Survey Platform. Corrected layering: population+confidentiality are shared/standard equipment across both §09 leaves; the differentiator is the program frame. The sibling's final document already describes this leaf as "closest sibling — generic survey instrument for any audience and purpose"; this pass sharpens that: this leaf is the instrument **specialized to the workforce context**, not the fully generic instrument.
2. **vs Survey Platform (§03.11)**. The generic instrument serves any audience (customers, research panels, event attendees, employees) with no workforce machinery. This leaf adds the employee-context layer: managed employee population, participation tracking against it, anonymity as standard equipment, HR-lifecycle survey types, manager-scoped reporting. SurveyMonkey is the live demonstration of the gradient: the same product markets employee feedback as one use case among five. Thin wall (audience/context specialization); both leaves kept; recorded as a gradient, not a wall.
3. **vs Online Form Builder (§03.11)**. Forms capture structured submissions (registrations, applications, requests) into record/table output for processing; surveys measure attitudes/opinions through scales and aggregate analysis. Different output object and different analysis model.
4. **vs Polling Application (§03.11)**. Polls are single-question, instant, often live-audience instruments; surveys are multi-question instruments with a managed lifecycle and population.
5. **vs Voice of Customer Platform (§07)**. Structural analog: instrument + program frame applied to customers. Different population, different rules (no employment relationship, no HRIS), different analytics. Same pattern as the sibling's finding #7.
6. **vs Performance Management Platform (§09)**. 360/multi-rater surveys straddle: they are diagnostic surveys about individuals delivered through survey machinery, but performance management centers goals/reviews/compensation. Vendors bundle both.
7. **vs Candidate Assessment / Psychometric Assessment (§09)**. Assessments evaluate identified individuals against criteria for decisions (hiring, development); surveys measure a workforce's attitudes in aggregate. 360 is the straddling case.
8. **vs People Analytics Platform (§09)**. Downstream consumer: survey results are one input to broader workforce analytics; this Type owns the instrument and the collection loop.
9. **Naming observation**: the market sells this structure under "employee survey software", "employee engagement survey software", "employee voice/listening", and "workforce research" — the survey-instrument layer is the stable core across all labelings.

## Uncertainties

- SurveyMonkey help-center articles beyond the anonymity page were not fetched (nav-heavy pages); its results/analysis mechanics are known only at structure level.
- Qualtrics EmployeeXM specifics not fetched this pass; CoreXM structure directly observed; EmployeeXM claims rest on the sibling pass's product-page-level evidence.
- TINYpulse article bodies only partially observed (promoted articles); its anonymity handling and threshold behavior not directly observed.
- QuestionPro evidence is product-page/FAQ level (Tier 2); help-center deep dives not fetched; "Respondent Anonymity Assurance" mechanics are a vendor claim, not independently verified.
- Whether the employee-population element of L0 should be relaxed to "any managed respondent population" (making this leaf a pure alias of Survey Platform) is a taxonomy judgment; this pass keeps the workforce orientation as the leaf's distinguishing property and records the gradient in STATUS.md.
- Exact confidentiality thresholds, retention periods, and channel availability are product-specific and configurable; no universal defaults are claimed.

## Final Synthesis

An Employee Survey Platform is defined by a small core: an authored questionnaire, addressed to the organization's employees as its respondent population, distributed and collected through the platform, and compiled into aggregated results. Around that core, mature products add the workforce-context machinery that makes employee surveying practical — population management synced from HR, participation tracking and reminders, anonymity as a deliberate pre-launch format with confidentiality-protected reporting, HR-lifecycle survey types, multi-channel reach including deskless workers, and manager-scoped results. The engagement program frame (engagement index, driver analysis, benchmarks, action planning, continuous listening) is the adjacent superset that defines the sibling Employee Engagement Platform Type; the fully generic multi-audience instrument defines the §03.11 Survey Platform. This leaf is the middle layer: the survey instrument specialized to the workforce.
