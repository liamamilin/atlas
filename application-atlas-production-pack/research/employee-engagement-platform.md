# Research Notes — Employee Engagement Platform

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what an Employee Engagement Platform actually is as an Application Type: its defining core structure, its standard capabilities, its variants, and its boundaries against neighboring Types in directory section 09 (Employee Survey Platform, Employee Communication Platform, Employee Recognition Platform, Employee Experience Platform, Performance Management Platform, Employee Wellbeing Platform) and the structural analog Voice of Customer Platform (section 07).

## Initial Boundary

Working hypothesis before research:

- Core use: measure workforce engagement/attitudes through surveys, aggregate confidential results into scores/trends/benchmarks, and drive action (insights → plans → follow-up).
- Primary users: HR / people-analytics teams as program owners; leaders and managers as results consumers and action owners; employees as respondents.
- Nearest Types: Employee Survey Platform (generic instrument), Employee Communication Platform (distribution), Employee Recognition Platform (awards), Employee Experience Platform (suspected umbrella), Performance Management (individual outcomes).
- Prior context: STATUS.md line 93 (employee-communication-platform pass) already flags "engagement platforms center surveys/recognition/listening while ECP centers targeted distribution" and treats "employee experience platform" as umbrella positioning.
- Unknowns: is recognition core or common? Is the action loop defining (vs the Survey Platform leaf)? Anonymity mechanics? Continuous vs annual cadence?

## Research Questions

1. What is the central object — survey, program, metric, or action plan?
2. What is the survey program lifecycle (create → schedule → distribute → respond → analyze → act)?
3. How is confidentiality/anonymity enforced (thresholds, aggregation, indirect-identification protection)?
4. What measurement outputs exist (engagement index, driver analysis, eNPS, benchmarks, trends, heatmaps)?
5. What does the "action" side look like (action plans, manager toolkits, follow-up questions)?
6. What role does recognition play — core, common, or adjacent Type?
7. What cadences exist (annual baseline, pulse, continuous, lifecycle/event-based)?
8. Which roles use which surfaces (admin vs manager vs employee)?
9. What is the HRIS's role (population source, attributes, segments)?
10. Where are the boundaries vs Survey / Communication / Recognition / Experience / Performance Types?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

1. **Culture Amp** — pure-play employee engagement leader; science-led; mid-market/enterprise; deep Intercom-based help center. Philosophy: survey science + benchmarks + action plans, expanding into a broader employee-experience suite.
2. **Workday Peakon Employee Voice** — enterprise continuous-listening product embedded in the Workday ecosystem. Philosophy: always-on employee voice tied to HR data.
3. **Qualtrics Employee Experience (EmployeeXM)** — engagement as one solution inside an experience-management (XM) platform. Philosophy: multi-channel listening + AI actioning + EX-to-business-outcome linkage.
4. **Workleap Officevibe** — SMB / manager-centric lightweight pulse + anonymous feedback + recognition. Philosophy: bottom-up, manager-first, quick to adopt.
5. **WorkTango** — recognition-first vendor whose Surveys & Insights and Recognition & Rewards are separate products bundled into an "Employee Experience Platform". Used primarily for boundary evidence (recognition vs engagement).

## Sources

Tier 1 (official operational documentation):

- Culture Amp Support Guide — https://support.cultureamp.com/ (root; collections: Survey Admin Hub, Participant Hub, Manager Hub, Account Admin Hub, Anytime Feedback & Shoutouts, Performance Admin Hub, People Analytics)
- Culture Amp — "Confidentiality Protections in Reporting": https://support.cultureamp.com/en/articles/7048386-confidentiality-protections-in-reporting
- Culture Amp — "Understanding Pulse Surveys": https://support.cultureamp.com/en/articles/7048336-understanding-pulse-surveys
- Culture Amp — "Survey Classification Types": https://support.cultureamp.com/en/articles/7048335-survey-classification-types
- Workday Peakon Employee Voice Help Center — https://help.peakon.com/hc/en-us (structure only; see limitations)
- Qualtrics — Employee Experience product page: https://www.qualtrics.com/employee-experience/
- Qualtrics Support — Employee Experience / 360 onboarding: https://www.qualtrics.com/support/employee-experience/ (redirected to 360 project guide)
- Workleap (Officevibe) — product page: https://officevibe.com/ (served as workleap.com/officevibe)
- Workleap Help Center — "Workleap Officevibe & anonymity": https://help.workleap.com/en/articles/10281766-workleap-officevibe-anonymity
- WorkTango — product page: https://www.worktango.com/

### Source-access Limitations

- **Peakon**: article pages are JS-rendered; two fetch attempts (help.workday.com transport error; help.peakon.com returned only the help-center shell). Evidence for Peakon = help-center section structure (Surveys; Comments; Taking Action → Action Planning, Improve Hub; Reporting → Manager Dashboard, Personal Dashboard; Benchmarking; Confidentiality and Data Visibility; Employee Records; Company Structure; Employee Sync; Workday Integration; Mobile App; Multiple Language Support; User Permissions). Structural existence is directly observed; operational detail is NOT. All Peakon-specific claims are kept at structure level.
- **Qualtrics**: the engagement-specific support section could not be reached (support root redirected to a 360-project guide; getting-started path 404). Engagement observations rest on the official product page (marketing tier) plus the 360 support page. Claims about Qualtrics engagement mechanics are stated more weakly.
- **WorkTango**: product page only; help center not fetched. Used for positioning/boundary evidence, not operational mechanics.
- No universal numeric defaults are claimed: confidentiality thresholds observed are product-specific and configurable (Culture Amp example uses a reporting group minimum of 5 in its documentation example; Officevibe uses 3 respondents for scores and 5 members for anonymous feedback).

## Product Observations

### Culture Amp (evidence layer A unless noted)

Structure (from help-center nav):

- Account Admin Hub: employee data file import, partial/full imports, hierarchy (reporting lines), demographics (incl. sensitive demographics), roles & permissions, HRIS sync (Workday, BambooHR, Dayforce, Paylocity, HiBob, Personio, Namely, Gusto, ADP, SAP SuccessFactors, UKG, and more via file/SFTP/API), SSO (SAML: Okta, Entra ID, Google, Ping), Slack/Teams apps, data-center location.
- Survey Admin Hub: "Surveys and Programs" page; Programs (recurring containers); create/duplicate/close/reopen/archive/delete survey; editing questions after launch has documented impact; attributed vs unattributed formats; survey classification types; engagement survey guidance (science, cadence methodology, statistical significance, random sampling); question design (Likert formats, branching, display rules, mandatory questions, multilingual, demographic piping); report factors (engagement index questions, driver questions, eNPS); demographics; participants (bulk upload, kiosk mode for employees without email/computers, SMS invitations); confidentiality; communications (invites, reminders, sender name, variables); preview; launch; results (scores calculation, trend, heatmaps, driver/impact analysis, correlation, text analytics, AI comment summaries/comparisons, focus agent); benchmarks & comparisons (incl. importing external/historical data); report sharing (filtered reports, leader-based hierarchy reports, viewers/owners, participation report); exports (PowerPoint, CSV, raw data extracts with warning text, de-identified extracts).
- Participant Hub: taking surveys (employee side).
- Manager Hub: manager-facing results and action.
- Adjacent modules (separate hubs): Performance Admin Hub (reviews), Anytime Feedback & Shoutouts (recognition/feedback), Development & Goals, 1-on-1s, Skills Coach, AI Coach, People Analytics (retention insights).

Confidentiality article (direct observation):

- Two anonymity formats exist: **attributed** and **unattributed** (confidential) surveys.
- **Direct identification protection**: a configurable "reporting group minimum" — groups with responses below the minimum are hidden in reports. Documentation example uses 5; the value is account/survey-configurable.
- **Comments group minimum**: a separate (typically higher) minimum for displaying comment groups.
- **Indirect identification protection**: three levels — None / Basic (recommended default) / Strong. Basic: if a filter includes a group with only 1 individual, the next smallest group's responses are also hidden (even if above the minimum) to prevent inference. Strong: additionally protects any group below the minimum by hiding the next smallest group.
- **Leader-based reporting removal rule**: in full-reporting-line leader reports with drill-down, some responses may be removed to prevent triangulation when a leader has enough indirect reports but too few direct reports.
- Raw data extracts are gated: enabling raw data is a deliberate act; extracts carry required warning text; de-identified extracts are available via request.

Pulse surveys article (direct observation):

- Pulse = shorter, more frequent surveys; Culture Amp recommends pulse surveys take no longer than ~4–5 minutes (~20 questions) — vendor guidance, not a platform limit.
- Trend tracking via repeating the outcome index (Engagement Index) plus driver/impact questions; post-survey action questions (what was communicated, involvement in action planning, perceived change).
- Cadence guidance: survey at about the rate meaningful change can occur; no fixed universal interval.
- Randomized-question surveys and automatic sampling are explicitly not supported/recommended (reliability, fatigue, representativeness).

Survey classification types article (direct observation):

- **Baseline**: full engagement survey; engagement index + topic questions (Leadership, Strategy, Company Performance, Collaboration, Learning & Development); driver analysis (correlation of topic responses with engagement responses); industry benchmarks; confidential format most common.
- **Trend**: shorter follow-up (e.g., 10–15 questions when baseline was ~50) tracking progress on actions; can run in pulse mode; confidential format.
- **Diagnostic**: domain deep-dives (Manager Effectiveness, Leadership, Values, Benefits), ~25–50 questions; per-manager action planning from results.
- **Event-based**: candidate, onboarding, exit, training; long-running/always-open; analyzed by cohort rather than as a single snapshot.

### Workday Peakon Employee Voice (evidence layer A for structure; layer B/C only beyond that)

Help-center structure (direct observation of section names):

- Getting Started; Release Notes.
- Surveys: Survey Setup, Survey Communications, Survey Branding, Survey Questions, Attribute Data Collection (demographics via survey attributes), Answering Surveys (employee guide).
- Comments: Comments, Responding to Comments, Topics (AI topics).
- Taking Action: Action Planning, Improve Hub.
- Reporting: Manager Dashboard, Reporting, Personal Dashboard.
- Benchmarking: Benchmark Settings, Benchmarking, Participation per segment.
- Account Settings: Personal Account, Company Account, **Confidentiality and Data Visibility**, Technical Specifications, Multiple Language Support, Mobile App.
- User Management: User Permissions, Employee Records, Company Structure (attributes and segments).
- Integrations: SSO, Employee Sync Integrations, Data Export using API, Survey Notification Integrations, Workday Integration.

Interpretation (layer C, structure-level): same core loop — employee records + company structure as population; surveys with attributes; comments; action planning; manager/personal dashboards; benchmarking; confidentiality as a first-class settings area. Continuous-listening positioning ("Employee Voice") is the vendor philosophy; the help center does not show (to this research) whether continuous cadence is mandatory — treat "continuous listening" as Peakon's posture (L2), not the Type's invariant.

### Qualtrics Employee Experience (evidence layer A for 360 support page; layer A marketing for product page)

Product page (official, marketing tier):

- Positioning: "Close the gap between feedback and action"; listening channels span pulse surveys, always-on feedback, and passive listening; AI-surfaced themes.
- Capability blocks: Employee Engagement & Pulse Surveys; Employee Lifecycle Management (auto-triggered touchpoints, e.g., Day 1 / Week 1 / 30-day onboarding checks); 360 Development Feedback; Lifecycle Intelligence (candidate → onboarding → engagement → development scores); Enhanced Actioning (AI comment analysis; personalized insights and recommended actions per manager); Retention Analytics (flight-risk simulation); EX benchmarks; linking EX data to CX/business outcomes.
- FAQ claims: continuous listening vs annual surveys; managers get personalized action recommendations; AI theme detection over open-text.

Support (360 onboarding guide, direct observation):

- Employee Experience platform objects: **Projects** (survey + participant workflow + subject report template + messages), **Participant**, **Subject** (feedback recipient), **Evaluator** (feedback provider), **Directory** (central list of all EX project participants for the organization), Brand Administrator / Employee Insights Administrator roles.
- 360 projects run in waves (nominations → evaluations → report access).
- This confirms the EX platform holds an organization-scoped participant directory and project machinery — the same population pattern as other sampled products.

### Workleap Officevibe (evidence layer A)

Product page (official):

- Positioning: "Employee Survey and Feedback Management Software for SMBs"; engagement in 3 steps: (1) get real information — pulse and custom surveys, anonymous feedback, Good Vibes recognition cards; (2) get a clear picture — survey/feedback/turnover/Good Vibes reports, AI-powered highlights; (3) act with an AI coach — recommended actions, feedback reply assistance.
- Score display example: engagement score out of 10, participation %, per-metric scores (e.g., recognition metric).
- Modules: Performance Reviews, Meetings & 1:1s, Team Health & Feedback, People & Org (directory). Integrations: Slack, Teams, HRIS tools.
- FAQ: "We ensure feedback is anonymous, shown only when privacy rules are met"; managers and admins access reports.

Anonymity help article (direct observation — key rule evidence):

- Individual answers are never displayed; only aggregated results.
- **Scores require a minimum of 3 active members** having answered; threshold mechanics differ per report (metric/sub-metric scores use a shorter default window such as last 30 days; the question report uses a 3–6 month rolling window at team level).
- **Anonymous feedback requires a minimum of 5 members** (active and/or inactive) in the team.
- Text answers are anonymous by default; the respondent can choose to reveal identity.
- Managers see feedback aggregated **by "week of [date]"** (temporal aggregation).
- Company-wide scores visible to all managers; team reports only to managers with access.
- Standard question bank: 122 survey questions ("we use the answers from our 122 Survey questions").

### WorkTango (evidence layer A, product page only)

- "Employee Surveys & Insights and Recognition & Rewards — available individually or bundled within WorkTango's holistic Employee Experience Platform."
- Surveys & Insights: employee lifecycle surveys, engagement surveys, dashboards & insights, action planning, anonymous conversations, benchmarks; "unlimited surveys"; response rate, sentiment highlights, factor summary in dashboards.
- Recognition & Rewards: recognition, rewards marketplace, incentives, service awards & milestones, nominations & awards, wellness.
- Interpretation: recognition and engagement-measurement are **separate product lines** that bundle into an experience platform — direct evidence that recognition is an adjacent Type, not part of the engagement core.

## Cross-product Comparison

| Aspect | Culture Amp | Peakon | Qualtrics EX | Officevibe | WorkTango |
|---|---|---|---|---|---|
| Employee population from org data | Employee data file, hierarchy, demographics; HRIS sync (many systems), SFTP, API | Employee Records; Company Structure (attributes/segments); Employee Sync; Workday Integration | Directory of EX participants; admins manage users | HRIS integrations; Slack/Teams | HRIS integrations |
| Survey programs | Programs; baseline/trend/diagnostic/event-based; engagement, pulse, onboarding, exit, 360, inclusion, DEI, wellbeing templates | Survey setup/questions/communications; attribute collection | Engagement & pulse; lifecycle auto-triggers; 360 projects | Pulse + custom surveys; 122-question bank | Engagement + lifecycle surveys; unlimited surveys |
| Confidentiality machinery | Attributed vs unattributed; reporting group minimum; indirect-identification levels; leader removal rule; gated raw data | Dedicated "Confidentiality and Data Visibility" area (structure observed) | Not directly observed for engagement | 3-respondent score threshold; 5-member feedback threshold; weekly aggregation; optional identity reveal | Anonymous conversations (mechanics not fetched) |
| Measurement outputs | Engagement index, report factors, eNPS, driver/impact analysis, correlation, heatmaps, trends, benchmarks | Manager/personal dashboards; reporting; benchmarking; participation per segment | Pulse dashboard (score + trend); lifecycle intelligence; retention analytics | 0–10 scores; participation; metric/sub-metric scores; turnover report; AI highlights | Dashboards; factor summary; sentiment; response rate; benchmarks |
| Action side | Action plans page; post-survey action questions; focus agent | Action Planning; Improve Hub; responding to comments | Enhanced actioning: personalized manager insights + recommended actions | AI coach recommended actions; feedback reply assistance | Action planning with recommended plans |
| Recognition | Shoutouts (secondary module) | Not in help-center structure | Not core | Good Vibes cards (bundled) | Separate product line (bundled) |
| Manager surface | Manager Hub; leader-based hierarchy reports; report viewers/owners | Manager Dashboard | Personalized manager insights | Manager reports (weekly aggregation) | Leader tools |
| Employee surface | Participant Hub; kiosk mode; SMS; Slack/Teams apps | Answering surveys; mobile app; personal dashboard | Survey response surfaces | Slack/Teams; anonymous feedback | Mobile survey |
| Benchmarks | Benchmark insights; comparisons; external import | Benchmarking + settings | EX benchmarks (claimed "world's largest set") | Not observed | Benchmarks |
| Adjacent modules | Performance, goals, 1-on-1s, skills coach, people analytics | Workday HCM adjacency | 360, candidate experience, retention analytics | Performance reviews, meetings & 1:1s, people & org | Coach, feedback, leader tools |

### What is universal (candidate defining core)

Across all five products (layer B):

1. **Workforce measurement population** — employees exist in the product as identified members with org-sourced attributes (department, location, manager/hierarchy, tenure…), used for segmentation and results slicing. Every product syncs or imports this from HR data.
2. **Survey programs as the measurement instrument** — question sets administered to the population or segments, as one-off or recurring programs (baseline/pulse/lifecycle/diagnostic).
3. **Confidentiality-protected aggregation** — individual responses are never exposed; results appear only as aggregates behind minimum-response rules and anti-inference protections. Directly observed in Culture Amp and Officevibe; structurally present in Peakon (dedicated settings area) and WorkTango (anonymous conversations); not directly observed for Qualtrics engagement.
4. **Action loop** — results produce insights that are assigned to owners (leaders/managers) who run follow-up actions; the loop closes with re-measurement (trend/pulse) and post-survey action questions. Present in all five (Culture Amp action plans; Peakon Action Planning/Improve Hub; Qualtrics enhanced actioning; Officevibe AI coach actions; WorkTango action planning).

### What is common but not defining (L1)

- Engagement index / outcome score; driver (impact/correlation) analysis; eNPS.
- Benchmarks and comparisons (industry, historical, hierarchical).
- Demographic heatmaps and slicing; participation tracking per segment.
- Manager dashboards; leader-based (hierarchy) reporting; report sharing with viewers/owners.
- Comment collection + text analytics (+ AI summaries in current products).
- Lifecycle surveys (onboarding, exit); pulse cadence; survey templates and curated question banks.
- Multi-language surveys; kiosk/SMS reach for deskless employees; Slack/Teams delivery.
- HRIS sync + SSO; roles (admin / program owner / manager / employee); mobile app.
- Survey communications (invites, reminders) — a small comms surface inside the loop.

### Variant / optional (L2)

- Recognition & rewards (bundled in some products; a separate Type when primary).
- Performance modules (reviews, goals, 1-on-1s) bundled by the same vendors as separate modules.
- Wellbeing content (survey domains or program modules).
- Always-on/passive listening channels; retention/flight-risk analytics; EX↔CX linkage (Qualtrics posture).
- Continuous-listening vs annual-census philosophy (vendor posture, not structure).
- Attributed vs unattributed default posture; anonymity strictness levels.
- HCM-suite embedding (Workday) vs standalone; SMB lightweight vs enterprise science-led packaging.
- AI assistance (comment summaries, recommended actions, AI coaches) — common recently, not defining.

### Vendor-specific (L3 — research notes only)

- Culture Amp: "Focus agent", "Multi-signal Intelligence™", protection level names (None/Basic/Strong), "Feedback Digest", survey champions, PowerPoint export, Pave/Figures compensation integrations.
- Officevibe: "Good Vibes" cards, 122-question bank, exact 3/5 thresholds and weekly aggregation, 30-day / 3–6-month report windows.
- Peakon: "Improve Hub", AI Topics.
- Qualtrics: "Insights Explorer", iowa-style ROI claims, "world's largest set of EX benchmarks" (marketing claim).
- WorkTango: "Constellation", "Coach".

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

```text
Workforce measurement population
  (employees as identified members with org-sourced attributes;
   individual responses held confidential)
└── Measurement instrument
    (survey programs administered to the population or segments)
    └── Protected aggregated results
        (scores / trends / comparisons; individual answers never exposed)
        └── Action loop
            (insights → owned follow-up actions → re-measurement)
```

Four properties. Remove any one and the product stops being this Type:

- Remove the workforce population → generic survey tool (Employee Survey Platform).
- Remove the instrument → HRIS/analytics without listening.
- Remove confidentiality-protected aggregation → a survey tool with exposed individual data; the trust model of engagement measurement collapses.
- Remove the action loop → a survey/reporting tool; the "engagement platform" framing (listen → understand → act) collapses into the Survey Platform leaf.

### L1 — Common Mature Structure

Engagement index & driver analysis; eNPS; benchmarks/comparisons; heatmaps & demographic slicing; participation tracking; manager dashboards & leader-based reports; comment analytics (+AI); lifecycle surveys; pulse cadence; templates/question banks; multi-language; kiosk/SMS/Slack/Teams reach; HRIS sync + SSO; roles; mobile app; survey communications; report sharing permissions.

### L2 — Variant / Optional

Recognition & rewards; performance modules; wellbeing; always-on/passive listening; retention/flight-risk analytics; EX↔CX linkage; continuous vs annual posture; attributed vs unattributed defaults; HCM-embedded vs standalone; SMB vs enterprise packaging; AI assistance depth.

### L3 — Vendor-specific

See Vendor-specific list above; stays out of the final document except as neutral examples where useful.

### Historical / market-sample check (§24)

- Older/regional engagement survey offerings (annual census via generic survey tools + manual analysis, regional providers) satisfy the L0: population + instrument + aggregated results + action — no continuous listening, no recognition, no AI required.
- HCM-native modules (Workday Peakon; SAP SuccessFactors-style listening) satisfy the L0 with the population sourced in-suite.
- Therefore the definition must not require: continuous cadence, recognition, benchmarks, AI, or any specific survey science branding. All of those are L1/L2.

## Vendor-specific Findings

(see L3 above; none promoted to the canonical document)

## Boundary Findings

1. **vs Employee Survey Platform (sibling leaf, §09)** — The survey platform is the generic instrument (any audience, any purpose: customers, research, events). The engagement platform is workforce-specific program machinery: employee population + confidentiality model + engagement-specific analytics (index, drivers, benchmarks) + action loop. Test: remove the workforce population and the action loop → an Employee Survey Platform remains. Risk: the two leaves overlap heavily; engagement platforms contain a survey engine. Flagged for joint review.
2. **vs Employee Communication Platform (sibling leaf, §09; prior flag STATUS.md line 93)** — ECP centers organization-authored targeted distribution (push); EEP centers the listening/measurement loop (pull + measure + act). Overlap: engagement platforms include survey communications (invites/reminders); comms platforms include pulse surveys as an interaction layer; Workvivo-class products span both. Test: remove the measurement loop → comms platform remains; remove targeted distribution → engagement platform remains. Consistent with the prior flag.
3. **vs Employee Recognition Platform (sibling leaf, §09)** — Recognition centers peer/manager awards, points, and redemption; engagement centers measurement. WorkTango ships them as separate products bundled in one suite (direct evidence); Culture Amp ships Shoutouts as a secondary module; Officevibe bundles Good Vibes cards. Test: remove the measurement loop → recognition platform remains. Flagged for joint review when Employee Recognition Platform is processed.
4. **vs Employee Experience Platform (sibling leaf, §09)** — Umbrella positioning used by the same vendors for the same or bundled structures (WorkTango "holistic Employee Experience Platform"; Qualtrics Employee Experience; Workleap). Consistent with prior flags (employee-communication-platform pass). Probable umbrella/alias, not a distinct structure. Flagged for joint review.
5. **vs Performance Management Platform (§09)** — Performance centers individual work outcomes (goals, reviews, compensation-linked); engagement centers workforce attitudes. Vendors bundle both as separate modules (Culture Amp Performance Admin Hub; Workleap Performance). 360/manager-effectiveness surveys straddle (they are diagnostic surveys about managers, delivered through the engagement machinery).
6. **vs Employee Wellbeing Platform (§09)** — Wellbeing appears as survey domains (psychosocial health surveys) or program modules inside engagement platforms; a dedicated wellbeing platform centers health program delivery. Gradient, not wall.
7. **vs Voice of Customer Platform (§07)** — Structural analog: population → instrument → protected aggregation → action loop, applied to customers. Different population, different rules (no employment relationship, no HRIS), different analytics. Related Type sharing a pattern.
8. **Naming observation** — "Employee engagement software/platform" is the dominant market term for this Type; "employee listening" and "employee voice" are posture names (Qualtrics, Peakon) for the same core.

## Uncertainties

- Peakon operational mechanics (confidentiality thresholds, cadence defaults, action-plan structure) not directly observed — JS-rendered docs; claims kept at structure level.
- Qualtrics engagement-specific confidentiality mechanics not directly observed; product-page claims only.
- WorkTango help center not fetched; mechanics unknown.
- Whether the action loop is *defining* vs *merely common* is a judgment call; evidence: 5/5 sampled products have it, and the directory's separate Employee Survey Platform leaf supports treating it as the differentiator. Recorded as a canonical inference (layer C).
- Exact confidentiality thresholds are product-specific and configurable; no universal default is claimed.
- The market increasingly bundles engagement + recognition + performance + comms into "employee experience" suites; the leaf's independence depends on the center-of-gravity test, which this research applies consistently.

## Final Synthesis

An Employee Engagement Platform is defined by a small core: the organization's workforce as a measured, confidentiality-protected population; survey programs as the measurement instrument; aggregated results (scores, trends, comparisons) that never expose individuals; and an action loop that turns results into owned follow-up and re-measurement. Everything else the market associates with the category — engagement indexes, driver analysis, eNPS, benchmarks, heatmaps, manager dashboards, pulse cadences, lifecycle surveys, recognition, AI — is standard mature structure or variant posture, not definition. The Type sits between the Employee Survey Platform (generic instrument, no workforce program frame) and the Employee Communication Platform (targeted distribution), with recognition and experience-platform framings as adjacent or umbrella structures.
