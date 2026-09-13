# Research Notes — Contact Center Quality Management

Research date: 2026-09-07

## Research Goal

Determine what Contact Center Quality Management (QM/QA) software is as an Application Type: its defining core, standard capability set, variants, and boundaries against the already-processed **Contact Center Platform** (parent Type, which documents QM as an attachable module), **Workforce Management for Contact Centers / Agent Scheduling** (WFO sibling), and **Sales Call Coaching Platform** (flagged cross-family pair from STATUS.md Boundary Issues, 2026-09-07: "same evaluation machinery … split adopted this pass by population and criteria … flagged for joint review when Contact Center Quality Management is processed"). This pass must discharge that flag from this side.

## Initial Boundary (working hypothesis)

Contact center QM = the structured evaluation of contact-center agents' handled interactions (recordings, transcripts, tickets, screen captures) against defined standards, producing scored evaluation records that accumulate into per-agent quality measurement, closed with feedback/coaching and (commonly) calibration and appeal machinery.

Easily confused with: Contact Center Platform (runs interactions), WFM (staffing/time), Conversation Intelligence / Support Conversation Analytics (org-scale insight), Sales Call Coaching (same machinery, sales population), Voice of Customer (customer-sourced feedback).

## Research Questions

1. What is the unit of evaluation, and what is the evaluated population? (ticket vs call vs omnichannel interaction; human agents vs bots)
2. What does an evaluation form/scorecard contain, and who authors it?
3. How are interactions selected for evaluation (sampling vs 100% auto-QA)?
4. What happens after scoring: feedback, coaching, disputes/appeals, calibration?
5. How does QM relate to the contact center platform's own recording and monitoring capabilities?
6. How do standalone QA products differ from suite modules and help-desk-native QA?
7. Where exactly is the seam with sales-call coaching, conversation analytics, and VoC?
8. Historical check: would paper-checklist, tape-review, side-by-side-monitoring-era QA satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different philosophies, different customer tiers:

| Product | Pole | Evidence reached |
|---|---|---|
| Verint Quality Automation (+ Calabrio ONE / QM Intelligence) | enterprise WFO suite, automation-first | product page + FAQ (Tier 2), case-study claims |
| NICE CXone Quality Management | enterprise WEM suite inside CCaaS platform | product page + FAQ (Tier 2) |
| Amazon Connect (Contact Lens evaluations) | suite-native module of a CCaaS, self-service | official admin guide (Tier 1) |
| MaestroQA | QA-first standalone SaaS, help-desk-integrated | site (Tier 2) + help center structure (Tier 1) |
| Zendesk QA (klausapp.com now serves it) | help-desk-native QA (ex-Klaus) absorbed into ticketing suite | product page (Tier 2) |

Corroborating (not primary sample): Genesys Cloud CX quality documentation (SPA; not reachable this pass), Zendesk QA help-center articles (calibration/scorecard guidance reachable via vendor blog links), Playvox (not fetched — dropped, evidence would likely repeat).

## Sources

- Verint — AI Contact Center Quality Management (quality-and-compliance product page + FAQ, incl. "What is automated contact center quality management?", QA-vs-QM distinction, Calabrio consolidation FAQ) — https://www.verint.com/quality-and-compliance/
- NICE — AI Quality Management (CXone product page + FAQ) — https://www.nice.com/products/quality-management
- Amazon Connect admin guide — Contact Lens: evaluate agent and self-service interaction performance — https://docs.aws.amazon.com/connect/latest/adminguide/evaluations.html ; Contact Lens overview — https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens.html
- MaestroQA — product pages (Quality Assurance, AutoQA, Screen Capture) — https://www.maestroqa.com/features/quality-assurance ; help center: QA Workflows collection (Automations incl. grading assignments, Appeals collection: enable appeals, appeal deadlines, decision reasons, multi-approval, appeals table; Calibrations and Grader QA; Rubrics; Coaching; Screen Capture) — https://help.maestroqa.com/en/collections/12012624-qa-workflows
- Zendesk QA (klausapp.com redirect) — product page: AutoQA 100% coverage, Spotlight, Real-time QA, AI Agent QA, targeted coaching, calibration/scorecard guidance articles — https://www.zendesk.com/service/quality-assurance/ (fetched via klausapp.com)

Unreachable / not used: Genesys Cloud Resource Center quality articles (SPA "Loading…" shell, 1 attempt — not retried per network-受限 rule), Verint help-center bodies, NICE help center (known unreachable from prior pass), Playvox.

## Product Observations

### Verint Quality Automation (incl. Calabrio ONE / QM Intelligence) — Tier 2

Evidence layer A (directly observed on official pages):

- Vendor-articulated definition: "the long-standing practice of capturing customer calls and scoring agents on their performance and compliance to internal and external standards"; historically manual and voice-limited, now AI-scaled to 100% across voice and digital, human and bots.
- Feature set named on the page: Interaction Capture (real-time monitoring + screen recording of voice, digital, AI-agent interactions), Custom Evaluation Forms (build/modify templates, align to compliance standards), 100% Automated Evaluation Scoring, Unified Dashboard/Reporting (audio + screen recordings + contact info + evaluation forms in one desktop view), Agent Coaching (auto-assign personalized targeted coaching), Performance Metric Tracking (role-based scorecards, real-time agent visibility, self-correction, request coaching).
- Compliance framing: PCI-DSS, TCPA, industry regulations, internal policies; automated capture/evaluation to identify compliance risks; meta-tagging for audit retrieval.
- QM → action: data from QM auto-triggers coaching sessions; WFM integration finds optimal coaching time without hurting service levels.
- QA vs QM (vendor FAQ): QA evaluates agent performance/adherence during interactions; QM takes the broader view (analyze QA data + other metrics → trends → strategic improvements).
- Calabrio now part of Verint; Calabrio QM Intelligence positioned as "manual → automated" transition product; both evaluate human and AI interactions.
- Customer claims (marketing, not operational fact): Fiserv coverage from 1% → 96% of calls via Quality Bot; quality scores +37% (dental/vet supplier). Numbers are vendor claims — kept in notes only.

### NICE CXone Quality Management — Tier 2

Evidence layer A:

- Positioned inside Workforce Empowerment/WEM family alongside WFM, Performance Management, Recording Management, Interaction Analytics, Feedback Management (VoC).
- "Evaluate 100% of interactions with AI and deliver effective coaching to agents"; Auto Score for 100% "unbiased evaluation coverage"; Evaluation Summaries (AI-generated summaries/recommendations, strengths, skill gaps, next-best coaching actions).
- Same quality standards applied across channels: voice, chat, digital — "and even CRM tickets" (Zendesk tickets named explicitly in FAQ).
- Agents receive personalized scorecards, evaluation packages, dashboards — transparency framing ("understand what great service looks like").
- Customizable evaluation forms, coaching templates, reporting dashboards.

### Amazon Connect / Contact Lens evaluations — Tier 1 (operational)

Evidence layer A (admin guide):

- "Define custom performance evaluation criteria to assess, monitor and improve how agents and automated systems (bots, AI agents) interact with customers" — evaluation targets both human agents and automated handlers.
- Manual evaluations for all contact types (voice, chat, email, task); automated evaluations for voice/chat contacts analyzed by conversational analytics; automated evaluation of both agent interactions and automated interactions.
- Procedure: search contact → Contact details → Evaluations panel (lists in-progress/completed evaluations) → choose evaluation form → Start evaluation → sections collapsible → Save as Draft or Submit → Completed; warning if optional questions skipped. Evaluation statuses: in progress / Draft / Completed.
- Reviews happen "alongside recordings, transcript, conversation summaries and analytics in a single view".
- Integrated coaching: "provide feedback to agents highlighting their strengths and opportunities to improve".
- Evaluation permissions are distinct user permissions (evaluation-and-coaching-permissions).
- Screen recordings reviewed "to ensure adherence to quality standards, compliance requirements, and best practices… identify coaching opportunities".
- Conversational analytics covers sentiment, themes, agent compliance risks; automatic redaction of sensitive data (privacy machinery adjacent).

### MaestroQA — Tier 2 site + Tier 1 help-center structure

Evidence layer A:

- QA feature page: "customers not only QA their support team but other customer-facing teams and back-office teams that don't interact directly with customers" — evaluation population extends beyond support agents.
- AutoQA: "scores 100% of tickets using your own criteria — customizable through LLMs, phrase matching, and process-based logic"; framed as replacement for random sampling.
- Screen Capture: "audit execution across systems… validate SOP compliance" — screen-level evidence beyond the conversation record.
- Named feature machinery: Scorecard Builder, Workflow Automations (assign and evaluate agent performance), Calibrations ("achieve alignment with calibration workflows"), Reporting (quality data + operational metrics), Transcriptions, Root Cause Analysis.
- CEO letter: "We started as a Contact Center QA company" — heritage pole; now repositioned as "AI Conversation Data Quality Platform" with QA and Coaching as the Action layer.
- Help center (Tier 1 structure): QA Workflows collection — "conduct Agent QA, Grader QA, Calibrations, and more"; Automations sub-collections: "Automate Creating and Sharing Grading Assignments", "Automate Sharing Feedback"; Appeals collection: Enable Appeals, "I Have a Question About My Score", Agent QA Appeal Decision Reasons, Multi-Approval Agent QA Appeals, The Appeals Table, Appeals by User Group, Setting Appeal Deadlines for Agent QA; Calibrations and Grader QA: Team Calibrations, GraderQA; Rubrics collection (evaluation form authoring); Coaching collection; Screen Capture; helpdesk integrations (Zendesk etc.), data-warehouse + API ingest, Assembled (WFM) / Seismic (LMS) / Workday integrations.
- Evidence layer B inferences from structure: evaluator role ("grader") is distinct from admin; grading assignments are assignable/shareable work; agent appeals are a first-class workflow with deadlines and decision reasons; grader quality is itself measured (GraderQA).

### Zendesk QA (formerly Klaus) — Tier 2

Evidence layer A:

- klausapp.com now serves Zendesk's QA product page (market consolidation observation; standalone Klaus brand absorbed into Zendesk QA add-on — purchase model: add-on to Support/Suite plans).
- AutoQA: 100% coverage incl. AI agents and voice; out-of-the-box categories (Empathy, Solution, Tone) + custom prompt-based categories.
- Spotlight: automatic flagging of churn risk, escalations, knowledge gaps → routes high-risk tickets to human review.
- Real-time QA: live risk/opportunity signals during unfolding conversations.
- AI Agent QA: scoring AI-agent conversations with human quality standards, side-by-side score comparison.
- Targeted coaching: 1:1 coaching and training sessions from QA insights.
- Guidance articles: QA scorecard building, calibration of reviews; customer story references "IQS" (internal quality score) — product-specific naming.
- Data controls: retention period selection, content hiding from agents/admins.

## Cross-product Comparison

| Dimension | Verint/Calabrio | NICE CXone | Amazon Connect CL | MaestroQA | Zendesk QA (ex-Klaus) |
|---|---|---|---|---|---|
| Evaluation unit | interactions (voice+digital, human+bot) | interactions incl. CRM tickets | contacts (voice/chat/email/task) | tickets + conversations + screen sessions | tickets/conversations incl. voice |
| Form | custom evaluation forms | custom evaluation forms | custom evaluation forms (sections, optional questions, draft/submit) | rubrics/scorecards | scorecards (out-of-box + custom prompt categories) |
| Evaluator | supervisors/analysts + automation | supervisors + AI | any user with evaluation permission | graders (dedicated role) + AutoQA | reviewers + AutoQA |
| Selection | manual → AI 100% | AI 100% coverage | manual any-contact + auto on analyzed contacts | AutoQA 100% + grading assignments | AutoQA 100% + Spotlight risk targeting |
| Calibration | implied ("unbiased", advanced workflows) | consistency framing | — | first-class (Team Calibrations, GraderQA) | first-class (calibration guidance) |
| Appeals | — (not on page) | — (not on page) | — (not on page) | first-class (deadlines, decision reasons, multi-approval) | — (not on page) |
| Coaching closure | auto-assigned coaching, WFM-timed | evaluation summaries → coaching moments | integrated coaching feedback | Coaching module | 1:1 coaching/training |
| Compliance scoring | explicit (PCI/TCPA framing) | — (compliance not foregrounded on page) | explicit (sensitive data, screen recording compliance) | SOP/compliance via screen capture | risk flagging (churn/loop/dead air) |
| Screen evidence | screen recording feature | — (recording mgmt sibling) | screen recordings | Screen Capture | — |
| Bots/AI-agent evaluation | yes (human + bots) | yes | yes (explicit) | AI chatbot monitoring use case | AI Agent QA |
| Packaging | WFO/CX-automation suite module (Calabrio merged in) | WEM suite module inside CCaaS | CCaaS-native module | standalone SaaS over help desks/warehouse | help-desk-suite add-on |

## Abstraction (L0–L3)

### L0 — Defining Invariant

Smallest structure without which the product stops being recognizable as contact-center quality management:

```text
Agent population under quality evaluation (identified members of a
customer-contact operation, each carrying a standing quality record)
└── Their actual service interactions as evaluation material,
    retained as reviewable records (recordings / transcripts /
    screen recordings / tickets)
    └── The evaluation form: the operation's defined standard
        (criteria + scoring rules) applied per interaction
        └── The evaluation record: one scored evaluation bound to
            one agent's one interaction, attributed to an evaluator,
            accumulating into the per-agent quality record
```

- Remove the agent-as-subject → conversation analytics (insight about conversations, no one held to account).
- Remove the interaction records → generic performance-review/KPI scoring with no evidence of actual service.
- Remove the defined standard (form) → ad-hoc listening/monitoring, not managed quality.
- Remove the recorded, accumulating evaluation → one-off audit or a monitoring log; no quality program.

Historical check (§24): paper-checklist QA over tape-review era satisfies this core (form + interaction + per-agent scores); side-by-side live monitoring with a scoring form satisfies the material clause in its observed-live form; premise-era WFO suites satisfy it. Passes.

### L1 — Common Mature Structure

- Evaluation assignment machinery: sampling strategies (random, targeted/risk-based, alert-triggered, quotas per agent), grading assignments/queues routed to evaluators.
- Automated evaluation (auto-QA): AI scoring of all interactions against the same forms/criteria, with human review of flagged exceptions — the dominant modern transition axis ("manual sampling → automated 100%").
- Feedback & coaching closure: results shared with the agent (scorecards, evaluation packages), coaching sessions/notes, auto-assigned targeted coaching/training; coaching time coordinated with WFM.
- Calibration & evaluator quality: calibration sessions comparing evaluator scores on the same interaction; scoring of graders themselves.
- Appeals/disputes: agent challenges a score; tracked decision with reasons, deadlines, sometimes multi-step approval. (Tier-1 direct in one product; present in category practice — common, not universal.)
- Compliance scoring: regulatory and policy adherence checks (sensitive-data handling, script/disclosure adherence), supported by screen recording alongside voice.
- Reporting: quality scores by agent/team/form/question over time, evaluator agreement, correlation of quality with CSAT/NPS-type metrics.
- Integration spine: contact center/CCaaS (recordings + metadata), help desks (tickets), CRM, screen capture, data warehouse/API, coaching/LMS and WFM handoffs.
- Roles & permissions: evaluators/analysts, QA managers, supervisors, agents (own results), admins; evaluation rights as distinct permissions; content-visibility controls.
- AI-agent/bot evaluation: applying the same forms to conversations handled by automated systems (era-typical; now documented across all five sampled).

### L2 — Variant / Optional

- Packaging: WFO/WEM-suite module vs CCaaS-native module vs standalone QA SaaS over help desks vs help-desk-suite add-on.
- Material scope: voice-only heritage → voice+digital → tickets/chats → +screen recordings/session capture.
- Auto-QA depth: manual-only sampling; AI-assisted selection; AI-100% with human validation; real-time (in-flight) evaluation.
- Population: support agents (core); extension to back-office/non-customer-facing teams via screen capture; external/mystery-shopper-style evaluation programs (adjacent practice, rarely the software's center).
- Program formality: ad-hoc reviews vs formal program (quotas, calibration cadence, scorecard governance).
- Regulated-industry tuning (finance/healthcare), BPO multi-client governance.
- Quality-vs-performance composites: quality scores folded into broader agent performance scorecards/gamification.

### L3 — Vendor-specific (notes only)

- Verint Quality Bot / Calabrio QM Intelligence product split; Coaching Bot, Wrap-Up Bot naming; Fiserv 1%→96% coverage claim.
- NICE Auto Score / Evaluation Summaries naming; Enlighten lineage.
- MaestroQA Rubrics / GraderQA / Appeals Table / user-group appeal config naming; "conversation data platform" repositioning.
- Zendesk AutoQA / Spotlight / Real-time QA / AI Agent QA / IQS naming; ex-Klaus consolidation.
- Amazon Connect Contact Lens naming; evaluation statuses Draft/Completed mechanics; S3 export configuration.
- Market consolidation: Calabrio → Verint; Klaus → Zendesk. (Facts observed on official surfaces; useful context, not Type structure.)

## Rejected Findings (not promoted)

- "QM = speech analytics" — speech/conversation analytics is the sibling capability feeding QM (trend/topics/sentiment); evaluation-of-agents is the different object. Not definitional.
- "QM = 100% AI scoring" — several sampled products still market manual-sampling programs as the base; automation is the common modern direction, not the invariant.
- "QM = performance management" — performance scorecards/gamification exist in the suite family but are composite layers over quality + productivity metrics; a QM product exists without them.
- "QM includes customer surveys" — VoC/Feedback Management is a separate module family (NICE ships it as its own product); correlation with CSAT is reporting, not evaluation.
- "Coaching is definitional" — rejected for this Type: the assurance/audit function (score against standards, evidence, compliance) stands alone; coaching closure is standard-but-not-defining (contrast with the sales pole, where the development loop is definitional).
- Precise coverage percentages, score weights, default quotas, retention periods — vendor claims; kept in notes, not asserted.

## Boundary Findings

1. **vs Contact Center Platform (parent, processed)** — parent runs interactions: queues, distribution, agent workspace, live monitoring, recording. QM evaluates the retained record against defined standards and manages the evaluation program. The parent doc already lists QM as an "adjacent module — evaluates recorded interactions; analysis over the interaction record, not distribution." QM can run standalone over any platform's records (integrations), so it holds as an independent Type whose dominant realization is a module. Remove distribution/recording from a QM product and it still is one; remove evaluation from a contact center platform and it still is one. Boundary holds.
2. **vs Workforce Management for Contact Centers / Agent Scheduling (processed)** — WFM object is staffing/time (forecast, schedule, adherence); QM object is quality of interactions. WFO-suite integration seam: QM triggers coaching; WFM finds the coaching slot. Both stand.
3. **vs Sales Call Coaching Platform (processed; STATUS flag) — DISCHARGED.** Same machinery (retained call/interaction artifacts, scorecards, moment-anchored feedback, coaching tracking). The split adopted by the sales pass is confirmed from this side: population (support/center agents vs sales reps), criteria (service-quality/compliance standards vs sales-skill/deal criteria), and institutional frame (QM carries the operation's assurance function — compliance scoring, calibration of evaluators, appeals, quotas are the standard QM machinery; development-first coaching is the sales pole's center of gravity; simulation/practice artifacts are a sales-pole variant with no QM counterpart in sample). Capture context differs (contact center/CCaaS/help-desk records vs conferencing/sales-engagement recordings). Joint review effectively completed by mutual passes; both Types stand. Residual overlap: products that coach support agents are marketed by both families — population-based reading keeps them separate; noted for directory review only if a vendor consolidation makes the seam vanish.
4. **vs Support Conversation Analytics (§07 sibling, unprocessed)** — org-scale insight over support conversations (topics, trends, VoC signals) vs per-agent evaluation against standards. Expected boundary: analytics has no evaluation form, no evaluated population, no per-agent standing record. MaestroQA's repositioning (QA company → conversation data platform) shows the families converging at the data layer while keeping QA workflows as the action layer. Flag for that pass to reference this seam.
5. **vs Voice of Customer Platform** — customer-sourced feedback vs internal evaluation of the agent's work; QM reports correlate with CSAT/NPS but the scored subject differs (agent's interaction vs customer's experience). Separate Types.
6. **vs Employee Performance Management (§09)** — generic workforce performance reviews vs interaction-evidence quality evaluation. A QM product's quality record can feed performance management, but the interaction-record + evaluation-form machinery is the Type's identity.
7. **Naming observation** — market uses "Quality Assurance (QA)" and "Quality Management (QM)" for the same product family (Zendesk "QA", MaestroQA "QA", directory leaf "Quality Management"; Verint's FAQ itself distinguishes the terms as evaluation vs broader program). Treated as one Type with both labels; not a taxonomy conflict.

## Uncertainties

- Verint and NICE claims rest on product pages + FAQs; their help-center operational detail (form field types, default quotas, permission granularity) was not reachable — capability-level claims only; no numeric defaults asserted anywhere in the final document.
- Genesys Cloud quality documentation (a major suite-native pole) could not be fetched (SPA shell) — Genesys is used only as unverified market context.
- Appeals machinery is Tier-1-documented in only one sample product; treated as common-not-universal.
- Agent self-evaluation exists in the family (NICE FAQ: agents access own scorecards/packages; sales-pole analog), but its form varies; kept qualified.
- Playvox and Scorebuddy (SMB standalone pole) not fetched; the standalone pole is covered by MaestroQA, but SMB-tier specifics are under-evidenced.
- Real-time/in-flight QA is documented on two product pages; extent of adoption not verified.
