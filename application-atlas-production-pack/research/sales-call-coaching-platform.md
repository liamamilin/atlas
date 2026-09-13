# Research Notes — Sales Call Coaching Platform

Research date: 2026-09-07

## Research Goal

Understand what a Sales Call Coaching Platform actually is as an Application Type: what objects exist inside it, what its users do with them, what workflow turns recorded (or simulated) sales calls into seller skill development, and how the Type is bounded against Conversation Intelligence Platform, Contact Center Quality Management, AI Meeting Assistant, Sales Engagement Platform, and Revenue Intelligence Platform.

## Initial Boundary (hypothesis before research)

- Hypothesis: the Type is the coaching-first realization of sales conversation software. Its unit of work is a sales call artifact (recording + transcript) evaluated against skill criteria, with feedback attached to a specific seller, and the seller's development tracked over time.
- Closest siblings: Conversation Intelligence Platform (same capture layer, insight-first), Contact Center Quality Management (same evaluation machinery, support-agent population), AI Meeting Assistant (single-meeting record, no development loop), Sales Engagement Platform (executes calls rather than develops sellers).
- Risk flagged up front: the directory carries both "Conversation Intelligence Platform" and "Sales Call Coaching Platform" in §07; the boundary must be carved by primary object / primary job, not by feature lists, because almost every product in this space ships both.

## Research Questions

1. What is the primary object: the call, the seller, the score, or the coaching act?
2. What forms does structured evaluation take (scorecards, Q&A, ratings, AI scoring, self- vs manager scoring)?
3. What are the feedback acts and where do they attach (timestamped comments, scorecard answers, private vs public)?
4. How does the system identify who needs coaching (insights, trackers, alerts, rep-requested feedback)?
5. How is coaching activity itself tracked (coach inbox, coaching metrics, manager-of-managers views)?
6. How does the exemplar loop work (finding and sharing "what good sounds like")?
7. What is the simulation pole (AI role-play): how does practice-before-the-call differ structurally from review-after-the-call?
8. What CRM/deal linkage exists, and is it definitional?
9. Where does real-time (in-call) coaching sit?
10. What separates this Type from Conversation Intelligence and Contact Center QM?

## Representative Products

Selected for market representativeness, documentation completeness, differing product philosophy, and differing packaging:

| Product | Philosophy / pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Gong | Category archetype; coaching module inside a conversation-intelligence/revenue platform; AI Call Reviewer auto-scoring | Enterprise | Tier 1 (extensive help center, machine-readable index) |
| Mediafly Coach (ExecVision heritage) | Coaching-first conversation intelligence; rep self-scoring vs manager scoring; smart alerts | Mid-market/enterprise | Tier 1 (community knowledge base) |
| Salesloft Conversation Intelligence | CI embedded in a sales-engagement suite; "system of action"; live in-call coaching cards | Enterprise | Tier 2 (product page; help center unreachable) |
| Second Nature | Simulation/role-play pole: AI buyers, practice before the call, certification programs | Enterprise (incl. contact-center populations) | Tier 2 (product page; help desk JS-rendered) |

Chorus (ZoomInfo) was considered as a fifth product but its help properties are unreachable (403 ×2); dropped rather than filled from memory.

## Sources

- Gong Help Center (reached 2026-09-07):
  - Introduction to coaching — https://help.gong.io/docs/introduction-to-coaching
  - Create coaching workflows — https://help.gong.io/docs/create-coaching-workflows
  - All about scorecards — https://help.gong.io/docs/all-about-scorecards
  - Help index (llms.txt) listing coaching, scorecard, feedback, initiative, tracker pages — https://help.gong.io/llms.txt
- Mediafly Community Knowledge Base — Coach (reached 2026-09-07):
  - Call Card — https://community.mediafly.com/knowledge-base/article/call-card
  - Coach KB collection — https://community.mediafly.com/knowledge-base/articles/Coachkb
- Salesloft (reached 2026-09-07):
  - Conversation Intelligence product page — https://salesloft.com/platform/conversations
- Second Nature (reached 2026-09-07):
  - Product page — https://secondnature.ai/ (help.secondnature.ai is a JS-rendered Pylon desk; not readable)

Unreachable / abandoned: help.salesloft.com (404/JS), help.zoominfo.com + chorus.ai (403 ×2), www.mediafly.com marketing pages (JS shell).

## Product Observations

### Gong (Tier 1 — evidence layer A)

- Coaching is a first-class module ("Enable Essentials/Enable" packages) addressed to sales managers, managers-of-managers, and enablement; reps are the coached population (AE/SDR roles defined).
- Feedback acts on a call page: timestamped comments in the transcript/timeline (public, private, or limited visibility; rep can be tagged and replies count as feedback), feedback requests (rep → manager), "mark as feedback given" (records offline coaching, e.g. from a 1:1), and call scoring.
- Scorecards: created per coaching opportunity (SDR outbound, discovery, demo, kickoff, initiatives, onboarding/certification); each is a set of questions with scoring guides anchoring what each answer value means; the "scored user" can be the call host or another attendee (e.g. an SE or AE when the SDR hosts); visibility of a completed scorecard is configurable.
- AI Call Reviewer: suggests scorecard answers during manual review or scores calls automatically against the scorecard criteria — explicitly framed as scaling structured feedback.
- Coaching inbox (Coaching > Coaching inbox): shows how coaching was distributed over time, when each rep last received feedback, and open requests; vendor recommends a weekly review cadence (vendor guidance, not a Type rule).
- Coaching metrics for managers-of-managers: per-manager coaching stats, frequency trends, drill-down to which calls received feedback.
- Coaching needs identification: team insights surface where coaching is needed; trackers monitor key phrases in calls/emails "enabling data-driven coaching"; search can filter calls by overall call score and scorecard name; filtering for high-scoring calls finds "what good sounds like" — reps are pointed to peer calls to hear exemplars.
- Strategic initiatives: initiative boards track adoption of messaging/methodology rollouts through calls (scorecards attached to initiatives).
- Call capture: records web-conference calls (consent profiles exist), supports uploaded recordings; calls can be associated to accounts/opportunities; snippets and sharing (internal/external) exist.
- Scoring rollout guidance: build scorecards → enable scorers (managers, peers, or enablement as scorers; KPI targets like "one scored call per rep per month" are vendor recommendations) → learn from data (which reps struggle, which teams adopt methodology).

### Mediafly Coach (Tier 1 — evidence layer A; ExecVision heritage)

- "Coach" is the conversation-intelligence product line; the call card is the central surface: call details, coach/share/sync-to-Salesforce/delete actions, playback controls, multi-speaker talk tracks, keywords & topics (tracked with mention counts, clickable into the transcript), transcript, comments (timestamped, on selections of the talk track).
- Scorecard: "a checklist for how the call should have gone" — reps can grade themselves; managers grade the same conversation to identify gaps between rep and management self-assessment. (Distinctive dual-scoring pattern.)
- Activity tab tracks per-user actions: shares, alerts, comments, highlights, scorecards, percentage of the call listened to, feedback requested. The system observes and records coaching engagement itself.
- Share flows: internal share lands in the recipient's Coach inbox; external share by email with audio-only, password-protection, and access-expiry controls.
- Coach button / "request call coaching" — coaching can be initiated by manager or requested by rep.
- Call library with tags; uploads of calls; sources include Zoom, Outreach, etc.; AI call summary (generative, with next steps and Q&A extraction) is an org-level toggle.
- Smart alerts (trigger- and trend-based, out-of-the-box types), weekly digests, notification settings — the platform pushes coaching moments to managers.
- Settings sections: Onboarding, Basics, Smart Alerts, integrations (Salesforce, Slack, custom/CI API).

### Salesloft Conversation Intelligence (Tier 2 — evidence layer A-lite, product page; help center unreachable)

- Conversation Intelligence is one module of a revenue platform ("system of action") alongside sales engagement (Cadence), deal management, forecasting, analytics. Log-in domains show the Salesloft/Clari merge; the CI module is marketed under "Conversation Intelligence Software."
- Recorded/transcribed/analyzed calls: AI call summaries, smart chapters, speaker talk-time, action items by attendee, follow-up email generation, automated CRM updates, searchable conversations ("instant answers across every call").
- Coaching-specific claims: coaching moments become tasks in rep workflows ("turning sales coaching from a weekly meeting into a continuous part of how deals get done"); automatic call scoring; objection tracking across the pipeline; team adoption dashboards.
- Live in-call coaching: AI guidance cards surface during live calls triggered by words (e.g., a discount request surfaces negotiation guidance); battlecards surface in real time on calls.
- Vendor FAQ explicitly separates CI from call recording (recording captures audio; CI analyzes and turns it into structured signals) and CI from sales intelligence (external data vs what happens inside deals).

### Second Nature (Tier 2 — evidence layer A-lite, product page; help desk JS-rendered)

- Completely different pole: the call being coached does not have to have happened. AI role plays simulate buyers (moving/video avatars, multi-persona meetings) for discovery calls, objection handling, cold calls.
- The platform: enablement/L&D teams design structured role-play programs and assign scenarios; reps practice with a conversational AI "virtual pitch partner"; the AI scores the performance and gives feedback; certification processes are gamified; manager insights/analytics feed coaching conversations ("managers love the insights they get… so they can focus on the things they need to focus on").
- Integrations: SCORM/LTI to LMS, CRMs, SAML, conference tools. Populations extend beyond sales (support agents, HR) — the same machinery serves other conversation-based roles.
- Also markets a "Deal Coach" for coaching on live deals (AI-driven deal guidance) — a newer adjacent capability, observed only at marketing level.

## Cross-product Comparison

| Structure | Gong | Mediafly Coach | Salesloft CI | Second Nature | Strength |
|---|---|---|---|---|---|
| Call library of recorded sales calls | yes (native capture + upload) | yes (capture + upload, tags) | yes (auto capture) | n/a (simulated calls instead) | 3/4 direct; simulated pole replaces the library |
| Simulated/AI-generated call artifact | no | no | no | yes (core) | 1/4 — product-specific pole, but maps to the same "call artifact" slot |
| Structured evaluation (scorecards) | yes (Q&A scorecards, scoring guides) | yes ("checklist for how the call should have gone") | yes (automatic call scoring claimed) | yes (AI scoring against criteria) | 4/4 — different forms, one structure |
| Timestamped feedback/comments on call moments | yes | yes | implied (coaching moments) | (feedback after simulation) | 3/4 direct |
| Feedback request in both directions (rep→coach, coach→rep) | yes (Request feedback) | yes (request call coaching) | — | — | 2/4 direct — common, not definitional |
| Coaching activity tracked (inbox, who/when/what) | yes (coaching inbox, mark-as-given) | yes (activity tab, coach inbox) | yes (moments→tasks, adoption dashboards) | yes (programs, completion) | 4/4 |
| Manager/leadership coaching oversight | yes (coaching metrics per manager) | — (weekly digests, alerts) | yes (team adoption dashboards) | yes (manager insights) | 3–4/4 |
| Identify who needs coaching (analytics/alerts) | yes (insights, trackers) | yes (smart alerts, trends) | yes (objection tracking, risk views) | yes (skill analytics) | 4/4 — forms vary widely |
| Exemplar loop (find/share what good sounds like) | yes (filter by score, share calls/snippets, peer listening) | yes (share, tags/libraries) | — | — | 2/4 direct — common |
| Conversation analytics (talk time, topics/keywords) | yes (trackers, topics) | yes (keywords & topics with counts) | yes (talk time, objection tracking) | — | 3/4 |
| AI-generated call summary | yes (AI Call Reviewer context) | yes (AI call summary) | yes (AI call summaries) | — (AI feedback instead) | 3/4 |
| AI-assisted scoring | yes (AI Call Reviewer) | — | yes (automatic scoring claimed) | yes (AI scores simulations) | 3/4 |
| Self-scoring vs manager scoring comparison | — | yes (explicit) | — | — | 1/4 — product-specific pattern |
| Live in-call coaching cards | — | — | yes (battlecards, live guidance) | — | 1/4 — product-specific |
| Real calls associated to deals/CRM | yes (associate to account/opportunity) | yes (sync to Salesforce) | yes (automated CRM updates) | LMS/CRM integrations | 3–4/4 — common |
| Certification/onboarding programs | scorecards used for certification tasks | onboarding settings | — | yes (gamified certification) | 2/4 direct — common in enablement-leaning products |
| Consent/recording governance | yes (consent profiles, skip codes) | external-share controls | — | — | 2/4 — governance surface exists where capture is native |

## L0 / L1 / L2 / L3 abstraction

### L0 — Defining Invariant

Three structures. Remove any one and the product stops being a sales call coaching platform:

1. **Sales call artifacts as the unit of development.** A library of identifiable call artifacts — recordings with transcripts, or AI-simulated role-play calls — each bound to the seller who made it. The call, not the course or the quota, is what gets worked on.
2. **Structured evaluation and feedback bound to a specific call and a specific seller.** Scorecards / evaluation questions / ratings (by manager, peer, enablement, the rep themself, or AI), plus situated feedback (timestamped comments at call moments). Feedback must attach to the concrete call artifact, not float as generic praise.
3. **A managed seller-development loop over the coaching population.** The system identifies coaching needs across sellers, routes evaluation/feedback to the right people (assigned scoring, feedback requests, coach inboxes), and tracks the coaching activity itself — who coached whom, when, on what, and how the seller progresses. Without this loop the same capture machinery is conversation intelligence or call QA, not coaching.

### L1 — Common Mature Structure (cross-product, not definitional)

- Conversation analytics over the call library: talk-time ratios, question counts, topic/keyword trackers with mention counts, objection occurrence — used to locate coaching needs.
- AI-derived call understanding: automatic summaries, next steps, highlights; AI-suggested or fully automatic scorecard answers.
- Exemplar sharing: search/filter for high-scoring calls, snippets, internal/external share flows, tagged libraries of "what good sounds like."
- Manager/leadership layer: coach inboxes, coaching metrics per manager, adoption dashboards, weekly digests.
- CRM/deal linkage: associating calls to accounts/opportunities, syncing coaching artifacts to the CRM, CRM updates from calls.
- Roles: rep (coached), frontline manager (primary coach), manager-of-managers/enablement (oversight, program design); scoring roles can include peers and AI.
- Recording governance: consent profiles/notifications, private calls, retention/visibility controls.

### L2 — Variant / Optional Structure

- Source of the call artifact: real recorded calls (web-conference/phone capture, uploads) vs AI-simulated role plays vs both.
- Scoring style: manual manager scoring, rep self-scoring with manager comparison, peer scoring, AI auto-scoring — and cadence (vendor-recommended cadences are guidance, not structure).
- Coaching program formalism: initiative boards, certification programs, gamified certification, coachable-moments-as-tasks; first-class "coaching plan" objects appear in the market but were not directly observed in this sample.
- Live (in-call) coaching: real-time guidance cards/battlecards during the call — single-product observation in this sample.
- Coaching scope: sales-only vs extended to support/CS/HR populations (simulation vendors serve multiple conversation-based roles).
- Enablement-suite packaging: coaching as a module of a broader enablement/CI/revenue platform vs standalone coaching product.

### L3 — Vendor-specific (research notes only)

- Gong: Enable/Enable Essentials package names; AI Call Reviewer; "mark as feedback given"; skip codes for unrecorded calls; initiative boards; scored-user selection (host vs attendee); vendor-recommended cadences (one scored call per rep per week/month); Gong Labs data cited as scorecard inspiration.
- Mediafly: Coach360/Intelligence360 packaging; call-card layout (talk tracks, activity % listened); external-share password/expiry controls; smart alerts with trigger/trend types; Coach inbox as share destination; articles imported from Zendesk (ExecVision-era docs).
- Salesloft: module renamed "Conversation Intelligence" (formerly Conversations); login on copilot.clari.com (Clari merger); live coaching cards triggered by keywords like "Discount"; system-of-action positioning; G2/Gartner/Forrester badge claims.
- Second Nature: moving/video avatars, multi-persona meetings, Deal Coach, "34%/6x/46%" marketing stats (vendor-claimed, unverified), SCORM/LTI/LMS angle, 30+ languages claim, try-me simulation URLs.

## Rejected Findings (considered and NOT promoted)

- "Scorecards are the definitional evaluation form." → The abstract structure is *structured evaluation bound to call + seller*; Second Nature scores simulations without a classic scorecard UI, and Mediafly's checklist is one form of it. Scorecards = the common implementation, not the invariant.
- "Coaching plans are a defining object." → Not directly observed in this sample (Gong documents coaching *workflows*, not plan objects; Chorus's plan object was not reachable). Kept as market-reported L2, not core.
- "Real-time in-call coaching is part of the Type." → One product (Salesloft) in sample; treated as variant.
- "CRM association is definitional." → Second Nature's core works without deal linkage; CRM linkage is common but not constitutive.
- "Talk-time/sentiment metrics define the Type." → That layer defines Conversation Intelligence; here it is an input to coaching, present but not constitutive.
- "The Type is only about post-call review." → Second Nature's simulation pole coaches *before* the call; the invariant had to be written as "call artifact (real or simulated)" to hold both poles.

## Historical / Market-Sample Check

- Would older products fit? The 2013–2016 first-generation conversation-coaching products (ExecVision-era) already show: call library, scorecards, coaching boards, manager review — they satisfy the L0 without modern AI summaries or auto-scoring. ✓
- Pre-software practice: managers reviewing taped/recorded sales calls with the rep, paper evaluation rubrics, "call libraries" of exemplary recordings circulated for training. This satisfies structures 1–2 but not 3 (no system-managed loop over the population) — correctly, because it is the practice the software Type organizes, not an earlier form of the Type. The L0 is not overfitted to any single capture mechanism, AI capability, or vendor.
- Contact-center agent evaluation platforms (QA scorecards over recorded support calls since the 1990s) satisfy the *machinery* but not the sales-scoped population/criteria — supporting the decision to keep "sales call/seller" in the Type's scope and treat agent-QA as the neighboring Type.
- Regional/platform check: the definition does not depend on web-conference capture (uploads fit), on English/American sales methodology, or on any specific CRM.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (remove what → becomes the other) |
|---|---|---|
| Conversation Intelligence Platform (§07 sibling, unprocessed) | sharpest seam — shared machinery | Both capture and analyze sales conversations. Remove the managed seller-development loop (coaching tracking, feedback routing, progress) → org-scale conversation analytics = CI. Remove the org-insight layer as end product and keep the development loop → this Type. Most CI products embed coaching modules and vice versa; the split is by primary object/end product, not by features. Flag for joint review. |
| Contact Center Quality Management (§07 sibling, unprocessed) | same evaluation machinery, different population/criteria | QM evaluates recorded interactions of support agents against service-quality/compliance criteria, typically inside contact-center suites with calibration/dispute workflow. This Type coaches sales reps against sales-skill/revenue criteria. Population + evaluation intent is the discriminator. Flag for joint review. |
| AI Meeting Assistant (§03.10, processed) | upstream capture sibling | Assistant's primary object = single-meeting record for immediate use; coaching platform's primary object = the seller's development across many calls. Consistent with the ai-meeting-assistant pass's framing (single meeting vs org-scale coaching over recorded calls). |
| Revenue Intelligence Platform (§07, processed) | consumer/input relationship | RI consumes conversation analysis as captured signal feeding a revenue model; here conversation analysis feeds a coaching model. Aligned with the revenue-intelligence pass ("coaching is CI's end product → standalone Type"). |
| Sales Engagement Platform / Sales Dialer (§07 siblings, unprocessed) | execution vs development | SEP/dialer products *execute* outbound work (sequences, dialing) and happen to record calls; this Type *develops* the seller. Suite bundling (Salesloft Cadence + CI; Gong Engage + Dialer) makes the boundary commercial, not structural. |
| Corporate LMS / Sales Enablement platforms | content-development sibling | LMS manages courses/content consumption; this Type manages call-artifact-based skill development. Enablement suites (Mediafly) span both, with Coach as the conversation module. |
| Meeting Recording & Transcription Application | input layer | Recording/transcription is the raw material; the Type's deliverable is evaluated, coached, progressing sellers. |

**Boundary issues to record in STATUS.md:**

1. sales-call-coaching-platform ↔ conversation-intelligence-platform: joint review required when CI is processed; working split = primary object (seller-development loop vs org-scale conversation insight).
2. sales-call-coaching-platform ↔ contact-center-quality-management: same machinery, different population/criteria; joint review recommended.
3. Sourcing limitation: Salesloft and Second Nature evidenced at product-page level only (help centers unreachable/JS-rendered); Chorus dropped (403); precise feature depths for those two products are correspondingly weakened.

## Uncertainties

1. Whether first-class "coaching plans" (assigned, dated development actions) are standard: reported by market knowledge but not directly observed in the reachable sample — kept out of the final document's standard-capability list as an explicit named object; the *function* (routed feedback + tracked activity) is evidenced.
2. Real-time in-call coaching breadth: observed in one product; market presence (e.g., real-time agent-assist vendors) known but not verified here.
3. Second Nature's post-simulation scoring detail (criteria structure, rubric depth): help desk not readable; only product-page claims.
4. Salesloft's automatic scoring and adoption dashboards: marketing-level claims; operational depth unverified.
5. Consent/recording governance breadth: directly observed in Gong and Mediafly share controls; not verified for the other two.
6. Coaching-object integration depth (e.g., scorecard results written to CRM fields, coaching data in BI): surfaced only at marketing level (Salesloft CRM updates claim).

## Final Synthesis

A Sales Call Coaching Platform is a seller-development application whose unit of work is the sales call artifact — a real recorded call or an AI-simulated role play — bound to the seller who made it. Around that artifact it provides structured evaluation (scorecards/evaluation questions answered by managers, peers, enablement, the rep, or AI) and situated feedback (timestamped comments at call moments), and it manages the development loop itself: surfacing who needs coaching, routing evaluations and feedback between coaches and reps, tracking coaching activity and progress over time. Conversation analytics, AI summaries, exemplar-call sharing, CRM/deal linkage, and manager-level oversight are the standard machinery that makes the loop work at scale; the source of calls (recorded vs simulated), scoring style, program formalism, and live in-call guidance are variants. The Type's edges: it ends where conversation analytics becomes the end product (Conversation Intelligence), where the evaluated population is support agents with QA criteria (Contact Center Quality Management), and where the object is the deal/revenue model rather than the seller (Revenue Intelligence).
