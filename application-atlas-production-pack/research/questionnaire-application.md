# Research Notes — Questionnaire Application

Date: 2026-09-08
Slug: `questionnaire-application`
Directory leaf: Questionnaire Application (§03.11 Forms & Data Collection)

## Research Goal

Understand what a "Questionnaire Application" is as an Application Type: what the questionnaire is as an object in real products, who authors it and who answers it, how it is fielded, what a response is, what the loop's output is — and, above all, how this leaf relates to its three §03.11 siblings: Online Form Builder (processed 2026-09-08), Polling Application (processed 2026-09-08), and Survey Platform (unprocessed). Both processed siblings pre-hung flags for this pass:

- online-form-builder: "vs questionnaire-application — likely near-alias of Survey Platform or of this Type's instrument layer; that pass should decide" (research/online-form-builder.md §Boundary Findings #2)
- polling-application: "NEW FLAG for survey-platform + questionnaire-application (§03.11, unprocessed): vendor-drawn lines from both sides (StrawPoll 'not representative surveys'; Polly 'Ditch the survey and send a polly'), seam = single lightweight question instrument with instant aggregate vs instrument battery with measurement/analysis as deliverable"

## Initial Boundary (pre-research hypothesis)

- Hypothesis: in research methodology, "questionnaire" names the *instrument* (the structured set of questions) and "survey" names the *activity/method* that administers it. A "questionnaire application" may therefore be the survey software Type under its instrument-first lexical variant, rather than a distinct Type.
- Competing hypothesis: a distinct market meaning exists — e.g., scored/validated assessment instruments (clinical, psychometric), field-enumeration data collection, or the Chinese-market 问卷 super-instrument (questionnaire + exam + vote + form).
- Likely confusions:
  - Survey Platform (§03.11 sibling, unprocessed) — suspected alias
  - Online Form Builder (processed) — shared instrument machinery; form's center is the per-submission record
  - Polling Application (processed) — small instrument + instant aggregate
  - Employee Survey Platform (processed) — workforce-population slice of the survey core
  - Psychometric Assessment Platform / Candidate Assessment Platform (processed) — validated instrument + scoring for selection
  - ePRO / eCOA Platform (processed) — protocol-scheduled regulated clinical instruments
  - Examination Platform (§23, unprocessed) — grading-centered instrument
  - Audience Response System (§26, processed) — live session container
  - Research Panel Platform / Market Research / Consumer Research platforms (§06) — research services around the instrument

## Research Questions

1. What is the questionnaire as an object inside products that carry the word — questions, pages, scales, logic? How is it stored, named, versioned?
2. Who authors it, and from what (scratch, templates, question banks, AI, paste)?
3. How is it fielded — channels, launch/activation, open/close, quotas, panels, sampling?
4. What is a response — structure, metadata, partial saves, identity/attribution and anonymity options?
5. What is the loop's output — per-question aggregates, statistics, exports, reports? How deep is the analysis, and is statistics export (SPSS/R/Excel) a defining realization?
6. Do research-methodology features (randomization, rotation, pretesting, multi-wave, response-latency capture, printable documentation) belong in the core or to the academic variant?
7. Does any product population answer to "questionnaire" that is structurally NOT a survey platform (scored assessments, exams, forms, votes bundled as modes)?
8. What lexical evidence exists (product self-description, manual chapter names) that "questionnaire" and "survey" are the same Type under two words?
9. Historical check: does the paper questionnaire (printed instrument → fielded → returned → tabulated) satisfy the derived core?
10. Removal tests vs form builder and polling: what exactly drops out at each seam?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| SurveyMonkey | mass-market/enterprise general-purpose survey leader; 400+ templates; Audience panel | the category's center of gravity; deep Tier-1 help center; uses "survey" as the object name |
| SoSci Survey | academic/research-methodology pole (German market, international docs) | manual vocabulary itself distinguishes "questionnaire" (instrument) from "survey" (activity); methodology-grade features; export-to-SPSS/R workflow |
| LimeSurvey | open-source self-hosted pole (cloud + CE) | full object model (survey → question groups → questions), activation lifecycle, responses & statistics, paper (QueXML PDF) export |
| QuestionPro | commercial SaaS with market-research suite and CX/EX packaging | explicit questionnaire vocabulary in feature/content layers; research models (conjoint, MaxDiff, NPS); kiosk/offline |
| 问卷星 WJX (wjx.cn) | regional Chinese pole where 问卷 ("questionnaire") is the primary product noun | instrument-first naming; super-instrument modes (survey/exam/360/vote/form/assessment/booking); edit→send→report loop on the homepage |

Rejected/abandoned samples:
- Google Forms — free platform-native pole; all Google properties were unreachable in the online-form-builder pass (×3 failures) and were not re-attempted here; used only as positional context.
- Qualtrics — enterprise research/experience suite; already deeply sampled by processed neighbor passes (employee-survey-platform Tier-1, voice-of-customer Tier-1); re-sampling would duplicate evidence.
- StrawPoll/Polly — sampled by the polling-application pass; their vendor-drawn seam lines ("not representative surveys" / "ditch the survey") are reused from that pass as recorded evidence.
- KoboToolbox/ODK/SurveyCTO (field data collection) — not fetched this pass; noted in Boundary Findings as an unverified adjacency only.

## Sources

Tier 1 (official operational documentation):
- SurveyMonkey Help Center — https://help.surveymonkey.com/en/ (fetched 2026-09-08)
  - Creating Surveys topic hub — https://help.surveymonkey.com/en/create/ (structure: Creating Surveys [Designing a Survey / Question Types / Using Survey Templates]; Sending Surveys [Ways to Send, Email invitation collector, Audience]; Analyzing Results [Understanding Your Results / Viewing Individual Responses / Sharing & Exporting Results])
  - "Creating Great Surveys" — https://help.surveymonkey.com/en/surveymonkey/create/creating-a-survey/ (creation paths: Build with AI, templates, blank Design Survey editor with Build/Style tabs, copy existing survey, copy-paste questions; Question Bank; logic: question skip logic, advanced branching; Preview survey; "Publish your survey to send it out to respondents"; modify past surveys that have already collected responses — copy carries questions/logic/theme but "you're responsible for sending")
- SoSci Survey user manual (wiki) — https://www.soscisurvey.de/help/doku.php/en:start (fetched 2026-09-08)
  - Overview: manual parts — Part 1 "Creating and Designing the Questionnaire" (en:create:start), Part 2 "Preparing and Launching the Survey" (en:survey:start), Part 3 "Data Retrieval and Questionnaire Documentation" (en:results:start); "An Online Questionnaire in 5 Minutes"; self-hosted survey server option ("Licence for a local Survey Server")
  - Part 1 structure (fetched): Question Types (Selection: simple/horizontal/dropdown/multiple; Selection Sequence [records response latency]; Scale, Slider/VAS, Polarity Profile [semantic differential], Image Scale [star rating/Kunin]; Text input incl. cloze; Ranking; Assignment task; IAT; File Upload; Screenshot; Captcha; functional elements: Random generator, Device/request variables, Internal variables, Teilnehmer-Verwaltung [address list]; communication elements); Composing the Questionnaire (texts, images, media, PHP code, JavaScript, access restrictions); Questionnaire Layouts; Multilingual Questionnaires; accessibility for visually impaired participants; Filters and Conditional Questions (simple + PHP filters); Rotation; Randomisation (incl. urns); Voucher codes; "Counting Score for Answers"; individual feedback; multi-level structure (nested questionnaires); Multi-Wave Survey; Timer; Questionnaire for Smartphones
  - Part 3 structure (fetched): Data Retrieval — import into SPSS (three documented paths), GNU R, OpenOffice Calc, Excel; API for Data Retrieval; Coding and return values; Additional variables; Changing Completed Questionnaires; Delete Data; Documentation in Research Papers; printable questionnaire for a thesis; Complete Survey Project (phaseout)
- LimeSurvey Manual (wiki) — https://manual.limesurvey.org/LimeSurvey_Manual (fetched 2026-09-08)
  - "LimeSurvey allows users to quickly create intuitive, powerful online forms and surveys"; open source, self-host or Cloud
  - Object model: Introduction – Surveys (import/copy/list/delete/export; Survey groups); Survey structure (Survey → Question groups → Questions); Question types catalog (Array variants incl. dual scale, 5/10-point, Increase-Same-Decrease, Numbers, Texts, Yes-No-Uncertain; Date; Equation; File upload; Gender; Numerical input; Ranking; List dropdown/radio; List with comment; Multiple choice ± comments; Short/Long/Huge free text; Multiple short text; Text display; Yes-No; Language switch)
  - Survey machinery: Survey participants (formerly Tokens); Email bounce tracking; Quotas; Assessments; Panel integration; Email templates; Central Participant Database (CPDB); Label sets
  - Lifecycle: Testing a survey → Activating a survey → Running a survey safely → Changing an active survey (restricted) → Closing a survey → Iterate survey
  - Results: Responses (survey results) — response summary; Data entry; Statistics (simple/expert mode); Timing statistics; Export/Import responses; Partial (saved) responses; Batch deletion
  - Presentation/logic: themes + question themes; ExpressionScript engine (conditions/branching); Multilingual survey; QueXML PDF export (paper questionnaire); Data encryption; REST/RemoteControl 2 API
- 问卷星 WJX product site — https://www.wjx.cn/ (fetched 2026-09-08)
  - Positioning: "问卷星_不止问卷调查/在线考试" (WJX — more than questionnaire surveys/online exams); "一站式调研工具" (one-stop research tool)
  - Homepage three-step loop: 编辑问卷 (edit questionnaire: batch question entry, "90多种题型" 90+ question types across questionnaire/form/exam/vote, 跳转/关联/引用 logic, skin/red-envelope/password settings) → 发送问卷 (send questionnaire: link + QR private/mass sending, WeChat official-account/mini-program, SMS/email one-to-one, custom link parameters for system integration) → 数据报表 (data reports: Excel/SPSS download, data dashboard, cross-analysis and online SPSS analysis, sharing/collaboration)
  - Application modes as parallel product families: 问卷调查 (surveys: internal/academic/user/market), 在线考试 (online exams), 报名表单 (registration forms), 360度评估 (360 assessment), 在线测评 (psychometric assessments), 在线投票 (voting), 收款 (payments), 预约 (booking), 通讯录 (address book), 打卡接龙 (chains), 员工体验管理 (employee experience), 客户体验管理 NPS (customer experience)
  - Research machinery: 调研模型 (research models: satisfaction, MaxDiff, Conjoint, KANO, concept test, product comparison, brand funnel); 样本服务 (sample services incl. global sample); decision-analytics product (决策鹰)
  - Editions: free (students/individuals) → enterprise tiers (标准/尊享/旗舰) → local deployment & 信创 (Xinchuang domestic-IT) → international edition (surveymars.com); help center at /help/help.aspx (not fetched)

Tier 2 (official product surfaces, positioning/features only):
- QuestionPro — https://www.questionpro.com/ (fetched 2026-09-08): positioning "Online Survey Software and Tools"; product family Survey Software / Research Suite / Customer Experience / Employee Experience; feature blocks (Likert scale, Conjoint, NPS, Offline Surveys kiosk, Survey Logic incl. looping/text piping); Academic + Nonprofit pricing; comparison pages (Qualtrics/SurveyMonkey alternatives); scale claims (5.3M users, 10B questions answered — vendor claims). Help center https://www.questionpro.com/help/ listed but deep articles not fetched this pass.
- SurveyMonkey product/enterprise menus inside fetched help pages (templates taxonomy incl. 360-degree evaluation, event registration form; Audience research panel; Enterprise admin/security; Wufoo and GetFeedback as sibling products).

Unreachable / limited:
- support.google.com / Google Forms — not attempted (previous pass ×3 failures; per one-to-two-failure rule).
- QuestionPro help-center article depth — root and feature pages fetched; deep help articles not fetched; QuestionPro observations held at positioning/feature-title strength.
- WJX help center — not fetched; WJX evidence is product-site level (homepage + navigation + application-mode pages).
- SoSci Survey English Part 2 (en:survey:start) — not fetched; Part 2 title and existence verified from the manual overview.

## Product Observations

### SurveyMonkey (evidence layer A — help center, fetched 2026-09-08)

- Object: the "survey". Help topics organized as Creating Surveys → Sending Surveys → Analyzing Results — the three-phase loop is the help center's own top-level taxonomy.
- Creation paths (Creating Great Surveys): Build with AI (type a goal or paste survey content → draft); templates ("500+ expert-built templates", filterable by plan/category); blank editor (Design survey tab with Build and Style sub-tabs); copy an existing survey ("questions, logic, theme, and other survey design settings are carried over... you're responsible for sending"); copy-paste questions; buy responses via Audience.
- Instrument machinery: add/edit questions and page elements; Question Bank of pre-written questions; per-question settings shaping "your respondent's experience"; Logic options — question skip logic ("control which questions respondents see next based on their answer"), advanced branching; Preview survey to catch "errors or logic issues"; Style/theme settings.
- Fielding: "Publish your survey to send it out to respondents to get responses"; Ways to Send Your Survey; email invitation collector; Audience (buy responses when you don't have your own respondent list).
- Results: Understanding Your Results; Viewing Individual Responses; Sharing & Exporting Results; benchmark data tied to a profile.
- Collaboration: teams work with others on survey design, publishing, and analysis; team survey templates; enterprise seats/roles.
- Domain breadth: templates/use-cases span customer satisfaction, employee engagement, market research, event feedback, registration, NPS — general-purpose instrument, not domain-bound.
- Sibling products under the same vendor: Wufoo (forms) and GetFeedback (CX) — the vendor itself separates form-builder and survey/experience product lines.

### SoSci Survey (evidence layer A — official wiki manual, fetched 2026-09-08)

- Lexical split, in the manual's own chapter titles: Part 1 "Creating and Designing the **Questionnaire**" (the instrument), Part 2 "Preparing and Launching the **Survey**" (the activity), Part 3 "Data Retrieval and **Questionnaire** Documentation" (the instrument's record). "An Online Questionnaire in 5 Minutes" is the instrument tutorial; a survey project contains questionnaires.
- Question-type taxonomy is methodology-grade: selections (single/multiple/dropdown; Selection Sequence records response latency); batteries/Matrix questions (Scale, Slider/analogue VAS, Polarity Profile = semantic differential, Image Scale = star/Kunin); text inputs incl. cloze; Ranking; Assignment task (latency); Implicit Association Test; File upload; Screenshot; Captcha; functional elements (random generator, internal variables, device variables, address list/contact management); communication elements (collect contact data separately, e-mail to a personal contact, mailing-list opt-in).
- Questionnaire composition: pages; texts; images; media; PHP code (scripting tier); JavaScript; access restrictions; layouts; multilingual questionnaires; accessibility for visually impaired participants; smartphone questionnaires.
- Methodology machinery: filter questions (simple + PHP filters); using an answer in later questions (transfer responses); rotation; randomisation incl. urn randomisation; vouchers; scoring ("Counting Score for Answers") with individual feedback; multi-level (nested) questionnaires; multi-wave surveys; timers; observational-study counters; consent page ("Obtaining the Participant's Consent").
- Output: data download formatted for SPSS (three documented import paths), GNU R, OpenOffice Calc, Excel; REST-ish data API; coding and return values per question type; additional variables; delete/restore data; "Changing Completed Questionnaires" (owner-side correction of collected data exists as a named, guarded operation); questionnaire printable documentation for a thesis appendix; "Complete Survey Project" phase-out.
- Deployment: hosted on the vendor's survey server, or self-installed by companies/organizations/universities (server installation + local license) — self-hosting is a deployment variant, not the definition.
- No in-product statistical modeling claimed in the English manual; the loop ends at structured data + documentation, feeding external statistics software. (A "data evaluation online" page exists for s2survey.net only.)

### LimeSurvey (evidence layer A — official manual, fetched 2026-09-08)

- Positioning: "create intuitive, powerful online forms and surveys"; open source; Cloud or self-hosted CE — both documented as first-class deployments.
- Object model: Survey (import/copy/list/delete/export; survey groups) → Question groups → Questions (with subquestions and answer options). A question-type catalog spans arrays/matrix batteries (incl. dual scale, 5/10-point choice, Increase-Same-Decrease, Numbers, Texts, Yes-No-Uncertain), list (radio/dropdown), list with comment, multiple choice ± comments, ranking, free-text tiers, numerical input, date, gender, equation, file upload, text display, language switch.
- Instrument logic: ExpressionScript engine (conditions, relevance/branching, computed equations); check question logic; survey logic file; regular expressions; default answers; label sets (shared answer scales).
- Fielding machinery: Survey participants (the feature historically named Tokens) with email bounce tracking; email templates with placeholders; publication & access settings; quotas (Survey quotas); panel integration; Central Participant Database (CPDB) for reusable respondents.
- Lifecycle with a hard state gate: Testing a survey → **Activating a survey** (structure locked for data collection) → Running a survey safely → "Changing an active survey" (explicitly restricted) → Closing a survey → Iterate survey (reset responses for re-running).
- Results: Responses (survey results) — response summary; browsing responses; **Data entry** (owner-side manual entry of responses); Statistics in simple and expert mode; timing statistics; export/import responses; partial (saved) responses visible to the owner; batch deletion; data encryption; REST/RemoteControl 2 API.
- Paper bridge: QueXML PDF export — the instrument printed as a paper questionnaire (plus TSV survey-structure export), and manual data entry to key paper responses back in.
- Assessment feature: "Assessments" (score-based feedback on the survey) exists as a survey-menu item — scoring machinery present but a named feature, not the manual's center.

### QuestionPro (evidence layer A at positioning/feature-title level, fetched 2026-09-08)

- Self-description: "Online Survey Software and Tools"; family = Survey Software (starter) / Research Suite ("enterprise-grade research tools for market research professionals") / Customer Experience / Employee Experience.
- Feature layer carries the instrument vocabulary and research machinery: Likert Scale (5/7/9-point), Conjoint Analysis, NPS, Survey Logic (looping, text piping), Offline Surveys (kiosk), heatmaps, synthetic data, video-AI open-end analysis, AI survey generation ("idea to full survey in under 60 seconds" — vendor claim).
- Domain packaging: academic pricing, nonprofit pricing, government cloud, industry editions (automotive, gaming, healthcare...) — audience packaging on the same instrument core.
- The root page does not lead with "questionnaire" as the object name (it leads with survey/research); the questionnaire term lives in the feature/blog/template layer — consistent with the lexical-field finding that the two words are interchangeable in this family.

### 问卷星 WJX (evidence layer A — product site, fetched 2026-09-08)

- The questionnaire IS the product noun: 问卷星 ("Questionnaire Star"). Homepage claim of cumulative usage (3.84亿 questionnaires published, 277.29亿 responses — vendor claim, L3).
- The three-step loop is printed on the homepage: **编辑问卷 → 发送问卷 → 数据报表** (edit questionnaire → send questionnaire → data reports), with per-step machinery listed (batch question entry; 90+ question types; jump/associate/quote logic; skins/red-envelope incentives/passwords; link+QR, WeChat, SMS/email, parameterized links for system integration; Excel/SPSS download, dashboards, cross-analysis, online SPSS analysis, sharing).
- Super-instrument packaging: survey / online exam / registration form / 360 assessment / psychometric assessment / online voting / payment / booking / address book / chains / employee experience / customer experience NPS as parallel application modes of one platform — the questionnaire core extended sideways into neighboring instrument Types (exams, votes, forms), which the market ships under one product in this region.
- Research-grade depth in a consumer-priced product: research models (satisfaction, MaxDiff, Conjoint, KANO, concept test, product comparison, brand funnel), sample services (paid respondent panels incl. global sample), enterprise editions, local deployment & domestic-IT (信创) edition, international edition.
- English-market equivalent positioning: "one-stop research tool" — the questionnaire platform as the survey platform of the Chinese market.

## Cross-product Comparison

| Dimension | SurveyMonkey | SoSci Survey | LimeSurvey | QuestionPro | 问卷星 WJX | Layer |
|---|---|---|---|---|---|---|
| Authored question instrument as stored object (questions + answer formats + ordering) | Yes (survey: questions, pages, settings) | Yes (questionnaire: questions, pages, composition) | Yes (survey → question groups → questions) | Yes (survey; feature blocks for question types) | Yes (问卷 with 90+ question types) | B |
| Question-type palette incl. closed choice, scale/Likert, open text, matrix/array | Yes (Question Types topic; Question Bank) | Yes (selections, scales, sliders, polarity, batteries) | Yes (arrays, lists, scales, free text) | Yes (Likert, NPS, conjoint feature blocks) | Yes (90+ types claim) | B |
| Instrument logic (branching/skip, mandatory, validation) | Yes (skip logic, advanced branching) | Yes (filter questions simple+PHP; response checks) | Yes (ExpressionScript conditions; check logic) | Yes (Survey Logic incl. looping/piping) | Yes (跳转/关联/引用) | B |
| Research-methodology machinery (randomization, rotation, multi-wave) | Not observed at help-top level (random assignment exists in product; not fetched) | Yes (randomisation, urns, rotation, multi-wave, latency) | Yes (ExpressionScript covers; quotas; timing statistics) | Partial (looping/piping; MaxDiff/conjoint models) | Yes (models; multi-mode) | A/B mixed — variant-grade, not universal |
| Launch/publication as a state transition | Yes ("publish your survey to send it out") | Yes (Part 2: Preparing and Launching the Survey) | Yes (explicit Activate survey; changing active survey restricted) | Implied (send/publish) | Implied (编辑→发送) | B (activation gate directly documented in 2/5) |
| Distribution channels: link, embed/QR, email/SMS, panel | Yes (ways to send; email collector; Audience) | Yes (address list, personal codes; Part 2) | Yes (participants/tokens, email templates, panel integration) | Yes (implied; kiosk/offline feature) | Yes (link/QR, WeChat, SMS/email, parameterized links) | B |
| Respondent identity optional (open link default; anonymous ↔ attributed modes) | Yes (open link common; Audience for strangers) | Yes (open access + address list/personal codes as modes) | Yes (open vs token/participant-tracked) | Yes (implied; panel) | Yes (open + 联系人/通讯录 machinery) | B — settings axis, not invariant |
| Response captured as per-respondent record | Yes (individual responses view) | Yes (interviews; changing completed questionnaires) | Yes (responses browse; partial saves; data entry) | Yes (implied) | Yes (回收答卷) | B |
| Compiled per-question results + aggregate statistics as the loop's output | Yes (Understanding Your Results; benchmarks) | Data retrieval to external statistics (SPSS/R/Excel) is the documented output; online evaluation minimal | Yes (response summary; statistics simple/expert) | Yes (dashboards; research models) | Yes (数据报表: cross-analysis, dashboards, SPSS) | B — depth varies, aggregate output invariant |
| Export of response data to external analysis | Yes (sharing & exporting results) | Yes (SPSS/R/Calc/Excel/API; coding manual) | Yes (export responses; TSV structure; QueXML) | Yes (implied) | Yes (Excel/SPSS) | B |
| Owner-side correction/editing of collected responses | Named caution: copy carries design but "already collected responses" are what you avoid modifying (modify-past-surveys guidance) | Yes ("Changing Completed Questionnaires" named, guarded) | Yes (data entry; import responses; iterate resets) | Not observed | Not observed | A/B mixed — product-dependent, do not generalize |
| Templates/question banks | Yes (500+; team templates) | Yes (question management/templates) | Not headline (label sets; import survey) | Yes (templates; sample questions) | Yes (问卷模板 by scenario) | B |
| AI assistance | Yes (Build with AI; Import with AI) | Not observed | Not observed | Yes (AI generation, video AI, dashboards) | Yes (AI 助手) | B — era-current |
| Scoring/assessment capability | Not observed at help-top level | Yes (Counting Score; individual feedback) | Yes (Assessments feature) | Yes (NPS/conjoint models) | Yes (测评/考试 modes) | B — feature-level, variant |
| Paper questionnaire output | Not observed | Yes (printable questionnaire documentation) | Yes (QueXML PDF export) | Not observed | Not observed | A (2/5) — variant |
| Paid respondent panel / sample service | Yes (Audience) | Not observed | Yes (panel integration [bring-your-own]) | Not observed at root | Yes (样本服务, global sample) | B — commercial variant |
| Self-hosted deployment | No (SaaS) | Yes (server installation; local license) | Yes (CE core; Cloud also) | Not observed | Yes (本地部署/信创) | B — deployment variant |
| Domain packaging (CX/EX/academia/government editions) | Yes (use-cases/roles/industries) | Academic positioning | Community + enterprise plans | Yes (CX/EX/gov/academic) | Yes (education/enterprise editions) | B — packaging |
| Sibling-mode expansion (exams/votes/forms as product modes) | No (vendor splits forms to Wufoo, CX to GetFeedback) | No | No (forms vocabulary admitted in positioning but one object) | No (separate product lines) | Yes (exam/vote/form/booking/payment modes on one platform) | A (1/5) — regional packaging variant |
| Language/region breadth | 20+ UI languages | de/en wiki; multilingual questionnaires | 40+ manual translations; multilingual surveys | 10+ languages | Chinese-primary + international edition | B |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Four jointly-held structures:

1. **The authored question instrument** — a stored, named, re-editable questionnaire: a set of questions, each with a defined answer format (closed options, scales, open text, and commonly matrix batteries, rankings, uploads), organized into an ordered structure (pages/sections/question groups), carrying presentation settings and response-shaping logic (branching/skip, mandatory, validation). Remove it → a mailing list or a statistics package; what the Type authors no longer exists.
2. **Administration of the instrument to respondents** — the instrument is put to a population of respondents: launched/published, distributed through channels (link, embed, email, SMS, panel, kiosk), with collection that opens and closes. Remove it → a question-bank/design document or a one-off interview script; there is no fielded instrument.
3. **The response** — each person's completion is captured as a record of answers bound to the instrument's questions, with metadata (time, identity/attribution or anonymity posture, partial/completion state). Remove it → ephemeral audience interaction; nothing accumulates.
4. **The compiled results** — responses are aggregated into per-question results/statistics and exportable datasets (spreadsheets/SPSS/R-class formats), the deliverable the loop exists to produce. Remove it → per-submission records processed one by one (form-builder territory), or a raw log.

Jointly-held is load-bearing:
- 1 alone = a questionnaire design / question bank (a document, not a loop).
- 1+2 without 3+4 = distribution with nothing retained.
- 1+3 without 2+4 = self-entry with no respondents.
- 2+3 without 1+4 = response capture with no authored instrument.
- 1+3 without 4 = per-response records as the center → Online Form Builder's defining output.
- 1+2+3+4 with a single-question instrument and instant ephemeral aggregate → Polling Application.

Historical / market-sample check (§24): the paper questionnaire satisfies all four legs without any software — a printed instrument (questions + answer options + scales), fielded by post/field workers (administration), returned sheets bound to the instrument (responses), and hand/summary tabulation per question (results). LimeSurvey's QueXML PDF export and SoSci's printable-questionnaire documentation are the software's own bridges back to that form. The mail-survey era, the CATI-era telephone instrument, and the modern web instrument all fit; the definition names no channel, no cloud, no AI, no specific question-type count, and no specific statistics depth.

### L1 — Common Mature Structure (cross-product, not definitional)

- Creation accelerators: template libraries (scenario-organized), question banks, duplicate-and-adapt, copy-paste import, AI drafting (era-current).
- Broad question-type palette beyond the minimal: rating/Likert scales, NPS-style questions, ranking, matrix/array batteries, file upload, contact/demographic questions; per-question settings (required, validation, randomize options).
- Presentation: themes/branding, page/section organization, progress indication, mobile-responsive fill, conversational/one-question-per-page presentation poles in some products.
- Distribution machinery: link/QR/email/SMS/embed/kiosk; email invitation collectors with templates and reminders; response windows (open/close, start/end); close messages.
- Respondent-population machinery: contact lists/address books, tokens/participant tracking, reusable participant databases, panel integration, quotas.
- Attribution & anonymity controls: open anonymous collection ↔ tracked/attributed collection; one-response-per-person style controls; partial (save-and-resume) responses.
- Results & analysis: per-question summary tables/charts, response browsing including individual responses, cross-analysis/cross-tabs at the research-grade pole, dashboards, sharing/reporting.
- Data exit: export to Excel/CSV and — at the research-grade pole — SPSS/R-class statistical formats with coding/value documentation; APIs.
- Collaboration & governance: teams, roles/permissions, sharing; enterprise security posture (SSO, encryption, compliance packaging); multilingual instruments.
- Methodology-grade extras at the academic pole: randomization, rotation, multi-wave, response-latency capture, pretest/pilot flows, printable instrument documentation, consent pages.

### L2 — Variant / Optional Structure

- Depth of in-product statistics: from simple summaries (mass-market) to expert-mode statistics (FOSS) to external-statistics handoff as the documented workflow (academic) — the analysis deliverable's depth is a variant axis, its existence is not.
- Scoring machinery: score computation with individual feedback (research grade), NPS/conjoint/MaxDiff model packaging (commercial research grade), assessment features (FOSS) — present as named features, not the core.
- Paid respondent supply: audience/panel purchase (mass-market), sample services (regional), bring-your-own panel integration (FOSS).
- Regional super-instrument packaging: questionnaire platform extending into online exams, voting, forms, 360 assessments, psychometric assessment, booking, payment as sibling modes of one product (Chinese-market realization); elsewhere the same vendor separates forms (Wufoo-class) and CX (GetFeedback-class) product lines instead.
- Self-hosting (FOSS core, academic server license, regional domestic-IT editions) vs SaaS-only.
- Kiosk/offline administration for field or venue collection.
- Domain/audience packaging: academic/nonprofit pricing, industry editions, government cloud — packaging on the same core.
- Paper-instrument output (PDF export, printable documentation) as a bridge to mixed-mode research.

### L3 — Vendor-specific (research notes only)

- SurveyMonkey: help taxonomy Create/Send/Analyze; Audience panel product; copy-survey behavior (design carried, sending manual); team templates; GetFeedback and Wufoo as separate sibling product lines; benchmark-data profiles; 400–500+ template claims.
- SoSci Survey: manual vocabulary (questionnaire = instrument, survey = activity/project); question-type catalog (Selection Sequence latency, Polarity Profile, IAT, cloze, urn randomisation, multi-level nested questionnaires); "Changing Completed Questionnaires" as a named guarded operation; s2survey.net online evaluation; server self-hosting for universities; printable thesis documentation.
- LimeSurvey: object trio survey/question group/question; Tokens → Survey participants rename; activation state gate with restricted changes to active surveys; iterate survey (reset responses); simple/expert statistics; CPDB; label sets; ExpressionScript; QueXML PDF; SGQA identifiers; data encryption; RemoteControl 2 API.
- QuestionPro: product family split (Survey/Research Suite/CX/EX); looping & text piping; video-AI open-end analysis; synthetic data/digital twin; XDay event; scale claims (5.3M users, 10B answers); comparison-marketing pages.
- WJX 问卷星: the 问卷 super-instrument mode family (exam/360/vote/form/assessment/booking/payment/contacts/chains); 编辑→发送→报表 homepage loop; red-envelope incentives; WeChat/mini-program distribution; 决策鹰 decision product; 信创/local deployment edition; surveymars.com international edition; cumulative-volume claims.

## Vendor-specific Findings

- **The market's own lexical split is the central finding**: a product can name the object "survey" (SurveyMonkey, LimeSurvey, QuestionPro) while a peer names it "questionnaire" (WJX; SoSci's manual uses "questionnaire" for the instrument and "survey" for the project/activity). Both vocabularies describe the same four-part loop. No researched product has machinery that exists only under one name and not the other.
- **The activation gate differs in strictness**: LimeSurvey documents activation as a hard state transition with restricted changes to active surveys; SurveyMonkey documents copy-vs-modify guidance ("already collected responses"); SoSci documents a guarded "Changing Completed Questionnaires" operation. Strictness is product-dependent; the underlying rule — instrument structure and collected responses are coupled — is common.
- **Analysis deliverable depth is deliberately uneven**: the academic pole's documented output ends at structured data for external statistics software (SPSS/R); the mass-market pole keeps summaries/dashboards in-product. Do not define the Type by either pole's analysis depth.
- **Sibling-product strategy differs by region**: the same global vendor separates forms and CX into different product lines (SurveyMonkey → Wufoo/GetFeedback), while the regional Chinese platform ships exams/votes/forms/assessments as modes of one questionnaire product. Neither strategy is structural for the Type.
- **Identity posture is a settings axis everywhere**: open/anonymous collection and tracked/attributed collection (contact list, tokens, address book) coexist in every sampled product.

## Boundary Findings

1. **vs Survey Platform (§03.11 sibling, UNPROCESSED) — ALIAS VERDICT from this pass.** The derived core (authored question instrument → administration to respondents → response capture → compiled results) is exactly the survey-software core as framed by processed neighbor passes: employee-survey-platform frames the authored survey as "the questionnaire as the central object" with distribution, collection, and aggregated results; voice-of-customer-platform frames the generic survey machinery it builds programs on; research-panel-platform frames survey platforms as "instrument authoring/fielding to non-persistent respondents"; online-form-builder frames the survey Type as measurement/analysis-centered over shared instrument machinery. The lexical evidence (SoSci's own manual; WJX's product noun; QuestionPro's interchangeable usage) shows "questionnaire" and "survey" are two names for one product population: every product led by one word answers to the other, and no structural machinery separates them. Verdict: keep-both as lexical-variant alias, cross-referenced documents (this one from the instrument angle), consolidation recommended at a taxonomy pass. **JOINT REVIEW WITH survey-platform IS PENDING — that pass must ratify or rebut; this document is the counterparty.**
2. **vs Online Form Builder (processed) — seam CONFIRMED on the output-object test.** Form builder's defining output is the persisted per-submission record produced for downstream use (view/export/route/integrate each entry); the questionnaire's defining output is the compiled per-question results the instrument was fielded to produce. Instrument breadth is a second marker (multi-question batteries with scales/logic vs free field sets). The two share the fill-and-collect machinery, which is why straddling is common (one form-builder sample sells Survey & Quiz templates beside order forms). Removal test: remove the compiled-results leg and center per-submission processing → Online Form Builder.
3. **vs Polling Application (processed) — seam CONFIRMED from this side, discharging that pass's flag.** Poll = a small instrument (one question, at most a few) whose aggregate is the immediate, consulted deliverable, with low-friction participation; questionnaire/survey = an instrument battery whose deliverable is measurement compiled after fielding. StrawPoll's own "not representative surveys" and Polly's "ditch the survey" marketing lines draw the same seam from the poll side. Recurring instruments accumulating into measurement programs drift to the survey/questionnaire family (polling pass's own note on Polly pulse → Employee Survey Platform).
4. **vs Employee Survey Platform (processed) — consistent with that pass.** That Type binds the same instrument core to the workforce population and employment lifecycle (roster, anonymity engineering, HRIS sync, manager-scoped results). Remove the workforce orientation → this generic instrument core remains. 360-evaluation questionnaires sit on that seam; that pass already owns them.
5. **vs Audience Response System (processed) — consistent.** ARS = facilitator-run live session container with the aggregate displayed back to the same co-present room; a questionnaire is a durable fielded instrument answered in participants' own time. The polling pass ratified the session-container test; it applies unchanged here.
6. **vs Psychometric Assessment Platform / Candidate Assessment Platform (processed) — different center.** Those Types center validated/scoring instruments bound to an evaluation decision (candidate selection, measurement of a person); the questionnaire application centers the instrument's fielding and its compiled results for the instrument owner's question, with scoring an optional feature. A questionnaire that becomes a standardized scored hiring instrument crosses into assessment territory (both processed passes define that crossing).
7. **vs ePRO / eCOA Platform (processed) — different center.** Regulated protocol-scheduled administration of validated clinical instruments inside a study, with auditable per-assessment records feeding a clinical dataset; the questionnaire application has no protocol/participant/study structure. That pass's own removal test ("remove the schedule discipline → ad-hoc survey tool") lands on this leaf.
8. **vs Examination Platform (§23, unprocessed) — probable seam.** Grading/assessment-centered instruments for instruction with scoring pass/fail semantics vs the questionnaire's measurement results. The elearning-authoring pass left a related flag (quiz-maker siblings inside authoring suites); this pass asserts only a tentative seam, decision left to that pass. WJX's online-exam mode is the observed packaging straddle.
9. **vs Market Research / Consumer Research / Research Panel platforms (§06) — services vs instrument.** Those Types center research services/studies/panels (research design, fielding as a service, panel populations); the questionnaire application is the instrument software itself. QuestionPro's Research Suite and WJX's sample services show vendors spanning both.
10. **vs field data-collection tools (KoboToolbox/ODK/SurveyCTO — NOT FETCHED, unverified)** — these appear to realize the same instrument core with offline/enumerator deployment as the variant; no claims made this pass; noted as an adjacency a future pass should check.
11. **Removal tests** ("去掉什么就变成另一个 Type"):
    - Remove the compiled-results leg, center per-submission records → Online Form Builder.
    - Shrink the instrument to one question with an instant ephemeral aggregate → Polling Application.
    - Remove the authored instrument (no question object) → distribution/statistics machinery without a subject.
    - Remove fielding to respondents → question bank/design tool.
    - Bind the population to the workforce + program machinery → Employee Survey Platform.
    - Bind the instrument to a validated scored evaluation of a person for selection → Psychometric/Candidate Assessment.
    - Add protocol-scheduled regulated administration inside a study → ePRO/eCOA.
    - Add the live co-present session container → Audience Response System.

## Uncertainties

- **Survey-platform joint review pending** — the sibling leaf was not yet processed when this pass ran. The alias verdict is derived from this pass's own product research plus the recorded framings of processed neighbors (employee-survey, voice-of-customer, research-panel, online-form-builder, polling). The survey-platform pass must ratify (or rebut) the alias; both documents stand until then.
- **QuestionPro evidence is positioning/feature-title level** (root + feature blocks; help-center article depth not fetched). No operational claims are made from QuestionPro alone.
- **WJX evidence is product-site level** (homepage + navigation; help center not fetched). Its super-instrument mode family is documented from the vendor's own navigation, held as packaging evidence, not operational detail.
- **SoSci Survey Part 2 (launch/fielding) title verified but content not fetched** — fielding claims from SoSci rest on the overview, Part 1's access-restriction/address-list machinery, and Part 3's "Controlling of your return".
- **Google Forms (free platform-native pole) unsampled** (previous pass ×3 failures); the free-tool tier is therefore under-represented, consistent with the form-builder pass's limitation.
- **Exact question-type counts, plan limits, response quotas, retention defaults** — vendor claims (e.g., "90+ question types", "500+ templates", cumulative-volume figures) are recorded as claims, not asserted as Type facts.
- **In-product analysis depth (cross-tabs, dashboards)** observed at feature-title level for QuestionPro/WJX; LimeSurvey's simple/expert statistics observed at manual-TOC level. No precise analysis-capability claims are made.
- **Field data-collection tools (ODK family) not fetched** — adjacency recorded, unverified.

## Final Synthesis

The Questionnaire Application is the survey software Type under its instrument-first name. Its defining core has four jointly-held structures: an authored question instrument (questions with answer formats, ordered structure, response-shaping logic), administration of that instrument to a population of respondents through distribution channels with open/close control, the response as a captured per-completion record bound to the instrument, and the compiled per-question results/exportable dataset as the loop's deliverable. The market evidence is lexical as much as structural: the instrument/activity word pair (questionnaire/survey; 问卷/调研; Fragebogen/Umfrage) splits across products and manuals, but every product that leads with "questionnaire" carries exactly the survey platform's machinery, and no product carries questionnaire machinery that survey platforms lack. The leaf is therefore recorded as an alias of Survey Platform — both documents stand cross-referenced, this one written from the instrument angle — with joint review pending the survey-platform pass. The seams to the processed siblings hold: form builder keeps per-submission records as its center, polling keeps the small instrument with the instant aggregate, and the population-bound/regulated/scoring siblings (employee survey, assessments, ePRO) each add structure this generic instrument core does not carry.
