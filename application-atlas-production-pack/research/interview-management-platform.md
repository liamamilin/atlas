# Research Notes — Interview Management Platform

Research date: 2026-09-10

## Research Goal

Determine what an Interview Management Platform actually is as an Application Type: what core structure makes it recognizable, what the market's product classes are, and — critically — how it separates from two already-processed neighbors: Interview Scheduling Platform (§09 sibling, joint-review flag against this leaf) and the ATS / Recruiting Management Platform (which embeds scorecards and interview kits as capabilities).

## Initial Boundary

- Working hypothesis: this Type is the evaluation-and-program machinery around the interview stage of hiring — interview plans, guides, scorecards, feedback, debriefs, interviewer enablement — as distinct from (a) the scheduling logistics of booking interviews and (b) the ATS pipeline that wraps the whole hiring process.
- The sibling pass (interview-scheduling-platform, 2026-09-07) proposed the split: "scheduling logistics = Interview Scheduling Platform; evaluation + program machinery = Interview Management Platform", flagging the risk that this leaf is only a suite-framing variant. This pass must ratify or refute.
- Nearest other neighbors: Candidate Assessment Platform, Psychometric Assessment Platform (measurement vs judgment), meeting-notes/AI-notetaker products, sales conversation-intelligence products, AI-screening/video-interviewing products.

## Research Questions

1. What objects does an interview management product actually manage? (plans, guides, scorecards, notes, records, programs?)
2. Is the structured interview plan (questions/competencies per role and stage) a defining structure or a common feature?
3. Where does feedback live — in the product or pushed into the ATS? What exactly is exchanged with the ATS?
4. Is interviewer training/coaching/certification definitional or program-level common structure?
5. Does a standalone product class exist, or is this only ever embedded in ATSs and scheduling suites?
6. Where does the seam with Interview Scheduling Platform actually fall in real products?
7. Where do AI-screening / AI-interviewer products cross into or out of this Type?
8. Historical check: do pre-AI, pre-recording, paper-era structured-interviewing practices satisfy the proposed core?

## Representative Products

Selected for market representation, different product philosophies, different customer tiers, and coverage of the packaging poles:

| Product | Pole | Evidence quality this pass |
|---|---|---|
| BrightHire | "Interview intelligence" category creator; recording/insights-centered; enterprise | Tier-1/Tier-2 official pages (home, what-is-II, AI notes) — directly fetched |
| Metaview | AI-notetaker origin; now agentic recruiting platform (drift pole); notes core | Tier-1 help center index (llms.txt, ~60 doc titles) + product site — directly fetched |
| Employ AI Interview Companion (formerly Pillar) | Live in-interview companion; guides + feedback collection; ATS-embedded (Lever); acquired by Employ Inc. | Tier-2 official product page — directly fetched |
| Hirevue (+ acquired HireGuide technology) | AI-interviewer screening platform carrying structured-interview tooling (guides/scorecards/compare); enterprise | Tier-2 official pages (hireguide.com now redirects to Hirevue AI Interviewer page) — directly fetched |
| GoodTime (boundary probe, not a sample member) | Scheduling-first product extending into interviewer enablement | Tier-2 official home — directly fetched |

Notes on sample drift: HireGuide was acquired by Hirevue (announced on hireguide.com itself) and Pillar was absorbed by Employ Inc. as "AI Interview Companion". Both retain their original feature structure inside the acquirer, so both remain usable as poles — with the acquisition itself recorded as market-consolidation evidence.

## Sources

- BrightHire — https://brighthire.com/ (home), https://brighthire.com/interview-intelligence/ ("What is Interview Intelligence?"), https://brighthire.com/ai-interview-notes/ (product page incl. FAQ). Fetched 2026-09-10.
- Metaview — https://metaview.app/ (home), https://support.metaview.ai/ + https://support.metaview.ai/llms.txt (full documentation index; page titles quoted below). Fetched 2026-09-10.
- Employ Inc. — https://www.employinc.com/ai-interview-companion/ (formerly Pillar). Fetched 2026-09-10.
- Hirevue / HireGuide — https://www.hireguide.com/ (redirects to Hirevue AI Interviewer page with Before/During/After feature taxonomy; carries the HireGuide acquisition notice). Fetched 2026-09-10.
- GoodTime — https://goodtime.io/ (boundary probe; goodtime.com returns an empty directory index — domain move). Fetched 2026-09-10.
- Not fetched this pass: Greenhouse/Lever structured-hiring help centers (ATS-embedded pole). Evidence for that pole rests on the recruiting-management-platform pass's recorded observations plus this pass's in-ATS scorecard-autofill documentation (Metaview extension pages). Related sibling records: interview-scheduling-platform (2026-09-07), recruiting-management-platform (2026-09-07), candidate-assessment-platform (2026-09-07), psychometric-assessment-platform (2026-09-06), meeting-scheduling-application (2026-09-08).

## Product Observations

### BrightHire

Layer A (directly observed):

- Self-labels: "Interview Intelligence Platform"; "The most advanced hiring intelligence platform"; frames the whole product as "a system of action" alongside the hiring team; category page: "Interview Intelligence sits on top of the tools you already use… in the heart of the hiring process, interviews."
- Product modules: Interview Planning; AI Interviewer (screening); AI Interview Notes; Interview Insights; Integrations; Compliance and Security. Homepage flow frame: Plan → Screen → Interview → Decide → Improve.
- Category definition (vendor's own): "By automatically recording and transcribing interviews, and creating a set of highlights that can be revisited and shared, interview intelligence unlocks valuable data from every interview conversation and brings that information to the center of important hiring decisions."
- Before/During/After structure on the category page: Before = "Automatically create structured interview plans" (questions ported from the ATS) + interviewer prep from prior highlights; During = live guidance and feedback, recording/transcription, "focus on candidates, not on taking notes"; After = highlights, native collaboration, "automatically transfer them to your ATS", async review "to accelerate hiring decisions and avoid scheduling bottlenecks".
- AI Interview Notes page: "AI interview notes are structured summaries of hiring interviews… BrightHire structures these notes around the competencies your team defined before the interview, maps them to your ATS scorecard fields, and pushes them directly into your ATS. Generic meeting notetakers produce raw transcripts with no connection to hiring rubrics or evaluation criteria."
- Scorecard auto-draft: "maps AI-generated notes to your specific ATS scorecard fields and pushes them after the interview ends. The interviewer reviews, adjusts if needed, and submits in one click." In-ATS UX: "1-click scorecard completion", "Interview highlights playable in your ATS".
- Consent/compliance: automatic consent notifications before interviews with opt-out; SOC 2 Type II; GDPR/CCPA; customers own data and control retention; zero-data-retention options; role-based access controls; AI bias audits (babl.ai).
- Insights: measure interview quality, spot patterns, AI coaching agent delivering "personalized interview coaching to every interviewer", best-of interview clips; "Recruiter & Interviewer Training" solution page.
- Explicit boundary language vs meeting notetakers (FAQ) and vs Metaview (a "BrightHire vs. Metaview" comparison page exists).
- Vendor-specific extensions observed: candidate fraud detection (AI-assisted answers, proxy interviews, deepfake signals); always-on AI screening interviewer.

### Metaview

Layer A (directly observed):

- Self-label has drifted: "The Agentic Recruiting Platform" with agents for Sourcing, Application Review, Screening, Notes (Notetaker), Reports — "you only use and pay for the agents you need". The notes layer is the origin core; sourcing/screening are extensions.
- Help-center structure (Tier-1, from llms.txt):
  - "Notes Overview — Turn every hiring conversation into structured, decision-ready notes"
  - Capture: Automatic Scheduling (calendar connection), Manual Invites, Ongoing Calls, Phone Calls, Upload Recordings, Import Transcripts, Record From Your Browser; joins Google Meet/Zoom/Teams/Webex.
  - Notes page: Templates ("Fix the structure of your notes without scripting the conversation"), Transcript And Recording ("The raw record of the call"), TLDR, Snippets ("Show a hiring manager the answer"), Assistant ("Ask what a candidate said and get a cited answer"), editing/formatting/sources.
  - Conversation Details — "The title, type, and properties that drive templates, sync, and reports."
  - Participants — "Who is an interviewer, who is the candidate, and why it matters" (participant typing drives template/sync logic).
  - Share And Export, Collections, Access And Permissions, Deleting And Redacting.
- Browser extension: "AI-powered scorecard autofill, session browsing, and candidate lookup directly into your browser" with dedicated Ashby and Greenhouse scorecard-autofill pages ("Metaview helps you complete Greenhouse scorecards faster by autofilling key sections using your interview conversations").
- Scheduling-side integrations documented as integrations, not features: Calendly, GoodTime ("Learn how to use Metaview alongside GoodTime"), Google/Outlook Calendar, Paradox.
- ATS integration list: ~40 ATSs (Ashby, Greenhouse, Lever, Workday, SAP SuccessFactors, iCIMS, SmartRecruiters, Teamtailor, Zoho Recruit…).
- AI Skills (program-level machinery): Interview Prep ("what's been covered, what's still unknown, and what to ask next"); Interview Debrief ("Build an evidence matrix for a candidate or a full slate — what each round tested, where interviewers agree, and what nobody covered"); Interviewer Coaching ("Review interview technique against a defined framework, with the actual transcript moments as evidence"); Interview Intelligence ("Answer questions across hundreds of interviews using AI fields — with the calibration discipline that makes the numbers trustworthy"); Role Launch ("Turn one intake conversation into a role brief, interview plan, note templates…").
- Reports: "Organize interview data and uncover insights with Reports."
- Privacy: Notifications, Privacy Configurations, Access And Deletion Requests (DSAR machinery).
- FAQ (Layer A): "Your scorecards, your hiring process, and your definition of 'great.'" — configurable outputs; ICP refinement from hiring decisions.

### Employ AI Interview Companion (formerly Pillar)

Layer A (directly observed):

- Self-label: "Smarter Hiring with Interview Intelligence — AI Interview Companion by Employ… (formerly Pillar)"; "Build a consistent, streamlined interview process."
- Capability blocks: "Meet Your New Interview Assistant" (proactive AI insights — building guides, flagging gaps, recommending next steps; "Work directly in Lever with your assistant – no extra tools or tabs needed"); "Automate your Interview Summaries & Feedback Collection"; "Run a Standardized Interview Process" ("Guide interviewers, live in the interview"; "Collect feedback in real time"; "Serve recommended skills-based questions"; "Reduce bias and standardize the process"); "Automate your Interviewer Coaching" ("coachable moments after interviews"; "Training Center"; candidate sentiment); "Enable Skills-Based Hiring" ("Compare candidate skills with video clips and skills-based feedback").
- AI-Generated Interview Guide: "Paste your job description, and our AI will generate your interview questions."
- Governance disclaimer: "AI Interview Companion assists with transcription and summarization. It does not provide candidate scoring or hiring recommendations."
- Integration spine: "Connect Employ's AI Interview Companion to your ATS, video, and calendar tools."
- Marketing stats on page (90%+ scorecard completion, 12 minutes saved, 32% attrition decrease) — vendor claims, not asserted anywhere downstream.

### Hirevue (+ acquired HireGuide technology)

Layer A (directly observed):

- hireguide.com now serves Hirevue's AI Interviewer page; banner: "Hireguide's team and technology have been acquired by Hirevue" (press release linked). Hirevue self-label: "Enterprise AI Interviewer" — AI screening interviews built on "validated hiring science", with scoring tied to competency rubrics ("Every score ties back to evidence from the interview and your competency rubric"), calibration mode, governance controls (decision trails, bias monitoring, permissions), 40+ ATS integrations.
- The page's interview-feature taxonomy (inherited from the HireGuide structured-interviewing technology) is organized Before/During/After/Throughout:
  - Before: Skill-Based Guides; Templates; Training.
  - During: AI Notes and Recording; Candidate Feedback; Integrations.
  - After: Compare Candidates; Skill Scorecards; Equitable Hiring.
  - Throughout: Analytics; Structured Interviews; Compliance and Security.
- "One Platform" framing: interviews + assessments in one place; AI interviewer works with live notes for hiring managers.
- Vendor claims (78% prefer AI screening; IO-Psych validation) — not asserted downstream.

### GoodTime (boundary probe)

Layer A (directly observed):

- Self-label: "Smarter Interview Scheduling, Better Experiences"; GoodTime Hire = "Complex interview scheduling and more, perfected with AI"; "We're the leader in complex enterprise-level interview scheduling. From simple 1:1 interviews to multi-day panels, we handle interviewer selection, messaging, reminders, rescheduling, and more."
- Feature groups: Efficiency (Interview Scheduling; Applicant Screening; Workflow Automation; SMS & WhatsApp), Experience (Candidate Experience; Interviewer Experience — selection, auto-replacement, interviewer portal; Interviewer Training — custom training paths and auto-shadowing), Intelligence (Interview Intelligence — AI insights; Dashboards & Hiring Analytics).
- Uses the phrase "interview management" for coordination scope: "automated 90% of interview management tasks" (i.e., scheduling/coordination tasks). Naming hazard for this Type.
- No guides, question banks, scorecards, notes-capture, or debrief machinery anywhere in the feature list. ATS integration partners (8) mirror the scheduling pass's deployment spine.

## Cross-product Comparison

| Structure | BrightHire | Metaview | Employ AIC (Pillar) | Hirevue (+HireGuide) | GoodTime (probe) |
|---|---|---|---|---|---|
| Role-level interview plan / guide design (questions, competencies, per stage) | ✓ structured plans, ATS question import | ✓ Role Launch plans + note templates | ✓ AI-generated guides, recommended questions | ✓ Skill-Based Guides, Templates | — |
| Structured feedback instrument (scorecard / rating criteria) | ✓ auto-draft → ATS scorecard fields | ✓ scorecard autofill (Ashby, Greenhouse) | ✓ real-time feedback collection | ✓ Skill Scorecards | — |
| Per-interview record incl. capture of what happened | ✓ recording + transcription + AI notes | ✓ notetaker notes + transcript + recording (+uploads/imports) | ✓ transcription & summarization | ✓ AI Notes and Recording | — |
| Live in-interview guidance | ✓ real-time guide | prep brief (Interview Prep skill) | ✓ live guidance | — (screening-centered page) | — |
| Candidate comparison / debrief surface | ✓ summaries, topic coverage, AI assistant | ✓ Interview Debrief evidence matrix | ✓ compare skills with clips | ✓ Compare Candidates | — |
| Interviewer coaching / training | ✓ coaching agent + training solution | ✓ Interviewer Coaching skill | ✓ coachable moments + Training Center | ✓ Training | ✓ Interviewer Training |
| Program analytics / quality measurement | ✓ Insights | ✓ Reports + Interview Intelligence skill | ✓ (interview data claims) | ✓ Analytics | ✓ Dashboards (scheduling-centric metrics) |
| Booking/scheduling engine | — (joins calendar-created events) | — (integrates Calendly/GoodTime/Paradox) | — (calendar integrations) | — (scheduling serves AI screens) | ✓ CORE |
| ATS as deployment spine | ✓ deep, in-ATS scorecard UX | ✓ ~40 ATSs | ✓ works in Lever | ✓ 40+ | ✓ 8 partners |
| Consent / privacy machinery | ✓ consent notifications, opt-out, retention | ✓ notifications, privacy configs, DSARs | ✓ fairness framing | ✓ governance, decision trails | ✓ bias protection |

Reading of the table:

- The top six rows are present across all four interview-side products (Layer B) and absent at the scheduling pole (Layer A, GoodTime).
- The scheduling row is present only at the scheduling pole; the interview-side products explicitly consume scheduling through integrations (Metaview's "alongside GoodTime" doc is the cleanest single artifact: the two product classes meet at an integration boundary, not inside one core).
- ATS integration is universal — the deployment spine — with scorecard exchange (product → ATS fields) as the characteristic data flow.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **The structured evaluation design of record per role** — the organization's interview plan held in the system: what to evaluate (competencies/criteria), what to ask, distributed across the role's interview stages/interviewers. The organization authors it (free-form, from a JD, from a library — implementations vary); the system holds and operates it. Remove → ad-hoc conversations with no managed program (a question bank alone, or nothing).
2. **The interview record as managed unit** — a persistent record per interview bound to the candidate × hiring context (role/application) × interviewer(s), carrying its evaluation instrument (its guide slice and its scorecard criteria) and the recorded outcome of the interview — the completed evaluation at minimum; in modern products additionally notes/summary/transcript. Remove → generic meeting-notes tool, a survey form, or a bare question library.
3. **The feedback-to-decision loop** — interviewer evaluations are captured, aggregated into a decision-ready form (per-candidate synthesis, comparison across candidates/interviewers, debrief surfaces), and feed the recorded hiring decision (recorded in-product or in the connected ATS). Remove → form collection or a notes archive with no decision loop.

Jointly-held is load-bearing:

- 1 alone = question library / interview-question content site
- 2 alone = meeting notetaker (Metaview/BrightHire both make exactly this contrast in their own FAQ language)
- 3 alone = survey tool
- 1+2 without 3 = guides + notes archive, no decision loop
- 2+3 without 1 = unstructured feedback collection — hiring-shaped but not a managed interview program
- 1+3 without 2 = templates and aggregate reports with no per-interview record

### L1 — Common Mature Structure (not definitional)

- Capture layer: recording, transcription, AI-generated structured notes mapped to the organization's competencies (manual note-taking is the historical form; AI notes are era-current)
- Scorecard auto-draft / autofill pushed into ATS scorecard fields; in-ATS UX via browser extension or native embedding
- Live in-interview guidance (companion mode inside the video call)
- Candidate comparison and debrief surfaces (evidence matrices, highlights, clips)
- Interviewer enablement: coaching, training paths, best-of clip libraries, quality measurement (the "program machinery" the sibling pass predicted — confirmed common, but not definitional: see anti-overfit)
- Program analytics: interview quality, question coverage, fairness/consistency patterns, calibration
- Consent and privacy machinery (notification, opt-out, access control, retention, redaction)
- ATS integration as the deployment spine; calendar/video integrations for capture
- AI assistant over interview content (cited answers about a candidate or across interviews)

### L2 — Variant / Optional Structure

- AI-conducted screening interviews (AI interviewer) — BrightHire Screen, Metaview Screening, Hirevue's core; rides the same record/feedback machinery but is candidate-side evaluation territory
- Candidate fraud detection signals (BrightHire)
- Video-clip libraries and skills-based clip comparison (Pillar, BrightHire highlights)
- Candidate sentiment analysis (Pillar)
- Calibration workflows proving AI/human agreement (Hirevue)
- Packaging: standalone companion vs ATS-embedded structured-hiring module (Greenhouse-class) vs suite module (Hirevue) vs scheduling-suite extension (GoodTime's training/intelligence)
- Segment/audience variants: executive search & agency use (Metaview BD use cases), high-volume vs corporate
- Capture breadth: phone calls, uploads, transcript imports, browser recording (Metaview)
- Zero-data-retention and compliance postures (BrightHire)
- Multi-language interview capture/notes (Metaview)

### L3 — Vendor-specific (research notes only; excluded from the final document)

- BrightHire: Zoom-native Interview Assistant without a per-call bot; Teams capture methods (recorder@brighthire.ai / #brighthire); babl.ai bias audits; "Excellence Layer" and Plan→Screen→Interview→Decide→Improve naming; Shine community; 28%-faster-feedback and 25,000-candidate study claims; "BrightHire vs. Metaview" comparison page.
- Metaview: llms.txt support index; AI Skills taxonomy (Role Launch, Day-One Brief, Sourcing Copilot, Talent Research…); MCP integration; ICP-learns-from-decisions loop; screening/application-review credits; in-page support-bot help center; "45 seconds to start" claim.
- Employ/Pillar: Lever-native positioning; Training Center; candidate sentiment; 90%/12-minutes/32% marketing claims.
- Hirevue: HireGuide acquisition; IO-Psych validation and rubric builder; calibration mode; white-labeling; 78%-prefer-AI-screening claim; 30-min/60%/30%/40% outcome claims.
- GoodTime: Cori AI agent; auto-shadowing; auto-replacement; industry vertical packaging; 88%/75%/85% ROI claims.

## Vendor-specific Findings

- Consolidation into suites: HireGuide → Hirevue; Pillar → Employ Inc. (alongside ATSs JazzHR/Lever/Jobvite). Both absorbed products retain their feature structure — the market treats this machinery as a distinct layer worth acquiring, supporting Type separability.
- Platform drift: Metaview has re-branded from interview-notes tool to "Agentic Recruiting Platform" (sourcing/screening agents added); BrightHire added AI screening and planning. Drift is upstream (toward full-funnel recruiting), while the interview-evaluation core remains the shared spine.
- Naming hazard: "interview management" is used by scheduling vendors (GoodTime: "automated 90% of interview management tasks" for coordination) and by this Type's products for evaluation/program machinery. Directory naming does not match market usage exactly; substance does.

## Anti-overfitting / Rejected Findings

- **"Interview intelligence" (recording-centered) is not the definition.** It is one philosophy pole (BrightHire's category name). A product with manual notes and paper-era scorecards satisfies the core — see historical check.
- **AI notes/transcription are not definitional.** Era-current capture layer; the defining capture is the recorded evaluation outcome, however produced.
- **Interviewer training/certification is not definitional.** Confirmed common (5/5 sampled incl. the scheduling probe) but the Metaview core ships it as an add-on skill, not product structure, and GoodTime ships training with zero evaluation machinery — symmetric proof that training neither requires nor defines this Type.
- **AI scoring is not definitional.** Explicit disclaimer at Employ AIC ("does not provide candidate scoring or hiring recommendations") vs scoring pole at Hirevue — a philosophy axis, not a Type boundary; human-judgment support is the center.
- **Panel/loop construction is not definitional here** — it lives in scheduling machinery + ATS stages; both neighbors' passes recorded it there.
- **In-ATS embedding is packaging, not identity** — the standalone class exists (4/4 sampled standalone products integrated with, not inside, ATSs).
- **Phone/email/identity, calendars, video conferencing** — surrounding infrastructure, not core.

## Historical / Market-Sample Check (§24 style)

- Paper-era structured interviewing satisfies all three L0 legs with zero software machinery: a printed interview guide per role (leg 1), a paper scoring sheet per interview per interviewer filed against the requisition (leg 2), and a panel debrief with the decision recorded on the requisition file (leg 3). Behavioral/interview-panel methodology predates the software category by decades.
- Early ATS-era practice: scorecard forms and interview guides stored in the ATS or in shared documents, feedback chased by coordinators by email — same core, different transport. (Consistent with the recruiting pass's observation that scorecards/interview scheduling are standard embedded capabilities in ATSs.)
- Therefore: recording, AI notes, ATS APIs, calendars, coaching agents, and consent portals are all excluded from the defining core. The check passes.

## Boundary Findings

1. **vs Interview Scheduling Platform — JOINT REVIEW DISCHARGED, keep-both RATIFIED.** The scheduling Type's core is booking logistics (interview record as booking × availability reconciliation × managed confirm/reschedule lifecycle). This Type's core is the interview's evaluation substance (design → capture → feedback → decision-ready evidence) plus program machinery. Corroboration from real products: GoodTime's core is scheduling with no guides/scorecards; BrightHire/Pillar/Metaview have no booking engines and explicitly integrate with schedulers (Metaview documents "alongside GoodTime"; BrightHire auto-joins calendar-created events). Shared zone: the interview record (candidate × role × interviewer × time) and interviewer pools — which is why the market bundles both in suites and uses overlapping vocabulary. The sibling's proposed split (scheduling logistics vs evaluation + program machinery) is confirmed; the "if the market does not support a separable product class" risk is refuted by the standalone class itself.
2. **vs ATS / Recruiting Management Platform.** The ATS owns requisition → application → pipeline stages → offer, and embeds interview kits/scorecards as capabilities. This Type centers the interview evaluation program and integrates with the ATS as its deployment spine (4/4). The seam is center of gravity: pipeline ownership vs interview-evaluation ownership. ATS-embedded structured hiring is a packaging variant of both; recorded, no directory change proposed.
3. **vs Candidate Assessment Platform / Psychometric Assessment Platform.** Those Types administer vendor-owned standardized instruments with standardized scoring; this Type supports human-conducted interviews where interviewers record judgment against the organization's own criteria. Employ AIC's disclaimer ("does not provide candidate scoring") marks the center; Hirevue's AI-scoring pole straddles toward assessment. Consistent with both sibling passes' recorded boundaries.
4. **vs AI Interviewer / screening.** When the AI conducts the interview (Hirevue's core label; BrightHire Screen; Metaview Screening), the product is doing candidate-side evaluation — screening/assessment territory riding this Type's record/feedback machinery. The sampled platforms span it as an extension; the human-interview management core remains this Type's center. No separate directory leaf exists for AI interviewing — recorded as packaging drift inside sampled suites, not a taxonomy change request.
5. **vs Meeting Notes Application (§03.10).** BrightHire's own FAQ: "Generic meeting notetakers produce raw transcripts with no connection to hiring rubrics or evaluation criteria." Metaview types participants (interviewer vs candidate) and drives templates/sync/reports from conversation type. Seam: notes bound to hiring semantics (candidate × role × scorecard fields × consent regime) vs general meeting capture.
6. **vs Conversation Intelligence Platform (§06, sales).** Same recording/transcript/AI machinery, different domain semantics (sales methodology vs hiring rubric). Held as a domain-parallel seam; not directly sampled this pass (weak confidence, flagged for that leaf's pass).
7. **Taxonomy note.** Video interviewing (candidate-side recorded interviews, Spark Hire-class) has no §09 directory leaf; Hirevue spans interviewing + video interviewing + assessment. Recorded here only; no directory edit made.

## Uncertainties

- SMB/lightweight end under-observed: the reachable sample skews enterprise/mid-market; no standalone SMB pure-play surfaced. Assertions about small-team configurations avoided in the final document.
- The ATS-embedded pole (Greenhouse/Lever native structured-hiring docs) was not fetched this pass; it rests on the recruiting pass's recorded evidence plus this pass's in-ATS autofill documentation. Final-document claims about ATS embedding are kept coarse.
- Market vocabulary may continue migrating ("interview management" used for coordination by scheduling vendors); future passes touching either leaf should re-check the naming hazard.
- Metaview/BrightHire platform drift (sourcing/screening agents) may reshape the category; as of the research date the interview-evaluation core was constant across all sampled products.

## Final Synthesis

The Interview Management Platform stands as a separable Application Type: a dedicated product class (interview intelligence / interview companion / structured-interview tooling) exists alongside ATSs and scheduling platforms, integrates with both as its deployment spine, and is the object of acquisition by suite owners (HireGuide→Hirevue, Pillar→Employ).

Its defining core is three jointly-held structures: the role's structured evaluation design of record; the per-interview record carrying its evaluation instrument and recorded outcome; and the feedback-to-decision loop that aggregates interviewer evaluations into a decision-ready form. The sibling pass's proposed split is ratified — scheduling logistics vs evaluation + program machinery — and the suite-framing risk is refuted. Interviewer enablement (training/coaching/quality) is confirmed as the common program layer the sibling predicted, held out of the defining core.
