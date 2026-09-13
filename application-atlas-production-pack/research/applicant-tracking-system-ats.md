# Research Notes — Applicant Tracking System / ATS

Research date: 2026-09-06
Leaf: Applicant Tracking System / ATS (§09 HR, Workforce & Talent)
Slug: applicant-tracking-system-ats

---

## Research Goal

Understand what an Applicant Tracking System actually is from real products: the objects it manages (jobs/requisitions, candidates, applications), how candidates enter and move through the hiring pipeline, how hiring teams evaluate and decide, where the process ends (hire → handoff), and where the boundary lies against sibling leaves (Recruiting Management Platform, Job Board, Career Site Platform, Interview Scheduling Platform, Offer Management Platform, Candidate Assessment Platform) and neighbors outside the section (HRIS, Employee Onboarding Platform, sales CRM, Admissions Management as a structural analog).

## Initial Boundary

Hypothesis before research:

1. Core use: manage the employer side of hiring — from an open position through candidate intake, evaluation, decision, and offer.
2. Primary users: recruiters, recruiting coordinators, hiring managers, interviewers — inside the hiring organization; variant: agency recruiters serving client companies.
3. Nearest types: Recruiting Management Platform (possible near-alias), Job Board (candidate-side discovery), Career Site Platform (publishing surface), Interview Scheduling / Assessment / Offer Management (capability leaves), HRIS & Employee Onboarding Platform (post-hire), CRM (client-side for agencies).
4. Key unknowns:
   - Is the job/requisition object definitional or only common?
   - Is candidate-vs-application separation (one person, multiple applications) universal?
   - How far do modern ATS products extend (CRM, onboarding, HRIS) without becoming a different Type?
   - Is "ATS" vs "Recruiting Management Platform" one category or two?

## Research Questions

1. What are the core objects, and how do they relate (job → pipeline → application → candidate)?
2. What is the lifecycle of the demand side (job creation → approval → open → filled/closed)?
3. How do candidates enter (application form, job boards, referrals, agencies, manual entry, sourcing)?
4. How does the pipeline work — stages, advance/reject actions, who may move candidates?
5. How does evaluation work (scorecards/evaluations, interview plans, debrief, bias controls)?
6. How do scheduling, communication, and candidate-facing surfaces work?
7. What happens at the end (offer machinery, hire, rejection, handoff to HRIS/onboarding)?
8. What rules matter (permissions, compliance surfaces like EEOC/OFCCP and GDPR, rejection reasons, data retention)?
9. What varies by segment (SMB vs enterprise vs staffing agency vs suite module)?
10. Where are the boundaries against the sibling and neighbor Types?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers and market sides.

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| Greenhouse Recruiting | Mid-market/enterprise; "structured hiring" philosophy (scorecards, interview plans, job approvals); excellent public help center | Tier 1 (multiple help-center articles + full topic map) |
| Workable | SMB/mid-market generalist "recruiting software" with hiring-plan/requisition machinery; strong public help center | Tier 1 (multiple help-center articles + section maps) |
| Ashby | Newer generation, analytics-first all-in-one; consolidated knowledge base | Tier 1− (knowledge-base index pages with section titles; no deep article fetched) |
| Bullhorn | Staffing-agency side (ATS + CRM for agencies; placements instead of hires) | Tier 2 (official product page + FAQ; help center not fetched) |
| Tellent Recruitee | European SMB; jobs/pipelines/careers-site in one; modular "Hubs" | Tier 1− (help center home + Jobs collection index; no deep article fetched) |

Deliberately not sampled (noted for breadth check): suite-embedded recruiting modules (Workday Recruiting, SAP SuccessFactors Recruiting), legacy enterprise ATS (Oracle Taleo), regional products (Teamtailor, Moka, BeiSen), single-feature point tools.

## Sources

All fetched 2026-09-06.

Greenhouse (Tier 1):
- Support home: https://support.greenhouse.io/hc/en-us
- Create a new job: https://support.greenhouse.io/hc/en-us/articles/200668380-Create-a-new-job
- All Recruiting topics (full section map): https://support.greenhouse.io/hc/en-us/categories/360000310871-All-Recruiting-topics
- Visual Candidate Pipeline: https://support.greenhouse.io/hc/en-us/articles/4874727408795-Visual-Candidate-Pipeline
- Jobs and job openings: https://support.greenhouse.io/hc/en-us/articles/4402057774747-Jobs-and-job-openings
- Job openings section (incl. "Close reasons for job openings"): https://support.greenhouse.io/hc/en-us/sections/360007233072-Job-openings
- Rejections section (incl. "Rejection reason requirement", "Auto-reject", "Unreject candidate"): https://support.greenhouse.io/hc/en-us/sections/360003929651-Rejections

Workable (Tier 1):
- Help home: https://help.workable.com/hc/en-us
- Recruiting category (section map): https://help.workable.com/hc/en-us/categories/115001812807
- Requisition statuses: pending, approved, open, reserved, filled: https://help.workable.com/hc/en-us/articles/9470641768343-Requisition-statuses-pending-approved-open-reserved-filled
- Candidate profile in pipeline view overview: https://help.workable.com/hc/en-us/articles/115012857047-Candidate-profile-in-pipeline-view-overview
- Candidate profile & pipeline view section (incl. disqualification reasons, candidate sources, blocking candidates): https://help.workable.com/hc/en-us/sections/115003474887-Candidate-profile-pipeline-view

Ashby (Tier 1−):
- Knowledge base home: https://docs.ashbyhq.com/
- Jobs & Openings collection: https://docs.ashbyhq.com/jobs-and-openings
- Applications collection: https://docs.ashbyhq.com/applications

Bullhorn (Tier 2):
- ATS product page + FAQ: https://www.bullhorn.com/products/applicant-tracking-system/

Tellent Recruitee (Tier 1−):
- Help center home (collection map): https://support.recruitee.com/
- Jobs collection: https://support.recruitee.com/en/collections/45740-jobs

Cross-references from already-processed leaves (context, not new evidence):
- research/employee-onboarding-platform.md (ATS→onboarding seam; "slots between ATS and HRIS" market framing)
- research/admissions-management.md (§ vs ATS: structural analog, application→review→decision)
- research/employee-record-system.md, research/people-analytics-platform.md, research/organization-design-platform.md (ATS named as integration/data source)

---

## Product A — Greenhouse Recruiting

### Key observations (Layer A unless noted)

**Job as the central demand-side object.**
- "Create a new job" is the entry action ("When your organization is ready to begin the hiring process for a new job… select Create a Job"). Jobs are created from templates: Copy an Existing Job, Sample Job (provides "Attributes for Scorecard" and "Stages for Interview Plan"), or Blank Job.
- Job creation does not open the job: "A job that has yet to receive approval is considered a **Draft**… The job will be considered **Open** after all necessary approvals are granted." Job approvals are a distinct section (job approvals; offer approvals separate).
- "Jobs and job openings": "a **job** refers to a specific position with the same hiring process and a candidate pool. A **job opening**, on the other hand, refers to the specific individual you are trying to fill… each job contains one or more job openings." Openings support custom fields, approvals, and **close reasons** ("Close reasons for job openings").

**Pipeline and stages.**
- "Visual Candidate Pipeline" lives on a job's Pipeline tab: "Each interview **stage** created by your admin during the job setup process is displayed in its own column"; candidates are dragged between stages to advance ("Users with the permission to *advance candidates* can drag and drop a candidate to another stage").
- The pipeline surfaces per-candidate state: days in stage, referral flag, private-candidate flag, internal applicants; color coding by the *next required internal action* (red = internal action needed e.g. scheduling an interview or making an offer; yellow = scorecard/feedback needed; gray = no internal action, e.g. "an availability or self-schedule request that is pending candidate action"). Stage-transition automation rules exist (lightning-bolt icon).

**Candidates and applications.**
- Section structure confirms objects: Candidates and applications general info, Candidate profiles, Rejections, Resumes, Custom fields, Candidate tags, EEOC and OFCCP, Candidate survey, Bulk edit, Candidate notifications.
- Rejections are structured: rejection reasons are managed objects (create/hide/delete), a "Rejection reason requirement" exists, rejection emails, rejection questions, auto-reject, and "Unreject candidate or prospect" (rejection is reversible).
- Prospect object (CRM section): prospects, Prospect Posts, CRM pools & stages — pre-application relationship tracking alongside applications (separate CRM module).

**Hiring team and permissions.**
- Sections: User levels and job-based permissions, Job Admin permissions, Hiring team roles, Permission policies. Create-a-job article states permissions per action ("Job Admins, who can create new jobs and request job approvals, and Site Admins").

**Sourcing and intake.**
- Sections: Job ads, Referrals, Job board tracking links, Source tracking, Social media; Job boards: Careers page, External job boards, Internal job boards (internal mobility); Agencies section (agency recruiters submit into the system).

**Evaluation and interviews.**
- Sections: Scorecards, Interviews, Take-home tests, Forms, Scheduling and calendars (Google/Outlook), Candidate testing, Video interviewing, Reference check, Candidate background check — all as product sections or integration categories.

**Offers and the end of the pipeline.**
- Offers section: Create and edit offers, Offer fields, Offer document, Offer section; Approvals section: Offer approvals. HRIS and onboarding integration section + HRIS Link + Workday section confirm the post-hire handoff.

**Compliance and reporting.**
- Sections: GDPR, CCPA; Reports (Essential reports, Report Builder, dashboards, BI Connector); DE&I reports; Audit log.

## Product B — Workable

### Key observations

**Jobs, requisitions, and the Hiring Plan.**
- Recruiting category sections: Job creation, Application form, Hiring team, Workflows, Jobs page; Candidates & job boards; Candidate interaction (profile & pipeline view, communicating, internal screening, Events/Interviews, Assessments & Video Interviews, E-signature and offer documents); Hiring Plan.
- Requisition lifecycle (article, Layer A): Draft → Pending (approval workflow) → Approved → Open; Rejected; Reserved ("an offer has been sent to a candidate and is pending internal approval or acceptance"); On hold; Filled ("when a candidate is moved to the **Hired** stage in the pipeline and attached to the requisition"); Canceled. "Each requisition created with Workable's Hiring Plan must be approved before it can be opened." Approval is an enterprise/premier/recruiting-plan structure ("What is the difference between a job and a requisition?" exists as an FAQ — job vs requisition distinction mirrored like Greenhouse's job vs opening).
- Explicit binding of demand side to outcome: "Accepting an offer alone does not mark the requisition as filled; the candidate must be explicitly moved to hired."

**Pipeline and candidate profile (article, Layer A).**
- "Every job in Workable has its own recruiting pipeline… how many active candidates are under consideration for each stage."
- Candidate profile = record + action surface: toolbar actions — email, text, schedule event, comment, **evaluate**, **disqualify**, **move to next stage**; more actions — request e-signature, request background check, request reference check, save (talent pool), snooze, share, copy/move to job, delete, edit.
- Candidate profile content: application-provided info (work experience, education, skills), resume, custom fields, contact details, **source**, referral info, evaluations for current stage; timeline tabs: Profile / Timeline / Communication / Review (evaluations, assessments, video interviews, reference & background checks) / Comments ("Candidates will never see these comments") / Offer (e-signature + audit trail) / Files; side panel shows "Other candidacies" — one candidate, multiple applications.
- Disqualification is structured: qualified vs disqualified tabs; customizable disqualification reasons (FAQ); blocking candidates for all jobs; candidate sources tracked.

**Intake and distribution.**
- Sections: Job boards (posting), Careers page, Adding candidates ("Search with AI, resume, or manual entry"), Referrals portal, Job performance/visibility.
- Application form builder per job; automated actions; candidate surveys.

**Roles.**
- Hiring team section; guides split for Admins / Hiring managers; toolbar actions vary by "the member's role in the job and the job stage".

**Compliance.**
- Security, privacy and compliance section; GDPR purge referenced in requisition FAQ ("In cases of GDPR purged candidates…").

## Product C — Ashby

### Key observations (index-level; treat details as unverified)

- Knowledge base structure: Jobs & Openings (creating & opening jobs, job postings, job templates, compensation, **openings management**, confidential jobs, "when and how do I close out a job?"); Applications (application forms, application requests, **global application rules & auto reject**, form field connectors, **application review**, candidate fraud detection, **tracking the source of an application**, "updating the status on a job consideration", application limits); Candidates; Sourcing & Outreach; Interviews & Scheduling; Surveys, Assessments & Activities; Emails & Candidate Texting; **Offers & E-Signatures**; Integrations (incl. a **post-hire** category); **Ashby Analytics**.
- Role-based getting-started guides: admin, hiring manager, interviewer, sourcer, recruiter, recruiting coordinator (Layer A for role structure).
- Positioning: "ashby is a powerful all in one recruiting tool" — recruiting-suite framing on an ATS core.

## Product D — Bullhorn (staffing-agency variant)

### Key observations (product-page level)

- Positioning: "ATS & CRM" for staffing agencies — "Manage candidates, jobs, shifts, and clients in one platform."
- The agency-side object vocabulary differs: job **orders** for clients, **placements** as the outcome, **clients** as an account layer ("While your ATS handles candidate management and placements, the CRM helps you track sales activity, win new business, and manage your pipeline of leads").
- Automation examples named: "sending candidate updates, scheduling interviews, managing **job order approvals**, and even aspects of candidate sourcing."
- Onboarding exists as a **separate product** (Bullhorn Onboarding) — the ATS ends at placement; post-hire is a different line.
- Search & Match: AI candidate search over the agency's own database ("pulls the best candidates from your database, ranks them by fit, and connects them to the right jobs").

## Product E — Tellent Recruitee (European SMB)

### Key observations (index-level)

- Help collections: Jobs ("Create and manage your job openings, hiring pipelines, and application forms") — create a new job, application form per job, share jobs, manage jobs, departments, tags, job status change, schedule publish/close, multiple languages; **Pipeline** (customize pipeline view, workflow automations); Candidates; CareersHub (careers site); Calendar and scheduling; Email; Texting; Talent pools; Search (Boolean); Reporting & analysis; ReferralsHub; **Requisition approvals**; Compliance and information security; Acquisition (job board campaigns); AgencyHub (agency management); WhatsApp Hiring; Marketplace integrations.
- Same core vocabulary as US products: jobs → hiring pipelines → candidates; requisition approvals present even at SMB tier.

---

## Cross-product Comparison

| Dimension | Greenhouse | Workable | Ashby | Bullhorn | Recruitee | Reading |
|---|---|---|---|---|---|---|
| Demand-side object | Job (+ openings with close reasons) | Job + requisition (Hiring Plan) | Job + openings | Job order (for client) | Job (+ requisition approvals) | A position/job object exists in every sample — definitional; headcount/openings/approval machinery is a common refinement |
| Application lifecycle | Draft → approved → Open job; pipeline stages per job | Requisition Draft→Pending→Approved→Open→Filled/Canceled | Job open/close; "job consideration" status | Job order → placement | Job status; publish/close scheduling | Demand side has its own lifecycle; candidate pipeline hangs off it |
| Pipeline | Stages as columns; drag-drop advance; action-state color coding | Per-job pipeline; stage counts; stage selector | Interview stages (section) | Placements pipeline | Hiring pipelines | Tracked stage workflow is universal — definitional |
| Candidate intake | Application, agencies, referrals, manual/prospect | Application, AI-search, resume, manual; job boards; referrals | Application forms + requests; source tracking | Resume parse, sourcing over own DB | Application forms; job board campaigns; referrals; AgencyHub | Multiple intake channels; all recorded against source |
| Candidate vs application | Candidate profile; prospects separate | "Other candidacies" — candidate with multiple applications | Candidates separate object | Candidate vs contact vs submission | Candidates with multiple jobs | Candidate record + per-position application/consideration is the shared shape |
| Evaluation | Scorecards, interview plans, take-home tests | Evaluate action; evaluation hiding rule | Surveys/assessments (section) | Candidate rating/fit scoring | Evaluations | Structured evaluation is common, not definitional |
| Scheduling | Self-schedule references; calendar integrations | Schedule events; calendar sync | Interviews & Scheduling section | Scheduling automation | Calendar & scheduling | Common capability, often embedded |
| End of pipeline | Offers + offer approvals; hire; HRIS/onboarding integrations | Offer e-sign → Hired stage → requisition Filled | Offers & E-signatures; post-hire integrations | Placement; onboarding is separate product | Offer documents (E-sign) | Offer machinery + explicit hired state + handoff is universal; exact states vary |
| Rejection | Rejection reasons (required), auto-reject, unreject, rejection emails | Disqualify with customizable reasons; disqualified tab; blocking | Auto-reject rules | — | — | Structured, reason-coded rejection is the norm across in-house samples |
| Roles/permissions | Job-based permissions, hiring team roles | Role+stage-dependent toolbar; hiring team | Six role guides | Recruiter/sales split | Team and roles | Multi-role hiring team is common; granularity varies |
| Compliance | EEOC/OFCCP, GDPR, CCPA sections; audit log | GDPR purge; compliance section | Trust center | — | Compliance collection | Regulatory surfaces are segment/geography-dependent |
| CRM layer | Separate CRM module (prospects) | Talent pool | Sourcing & Outreach | CRM is half the product (client CRM) | Talent pools | Pre-application relationship tracking is a common add-on, strongest on agency side |
| Analytics | Reports/BI sections | Reporting category | Ashby Analytics | Reporting & Analytics product | Reporting & analysis | Common; depth varies |
| AI | Sourcing Automation, AI section | Workable Agent, agentic jobs, AI search | AI features section | Amplify AI throughout | AI job descriptions | Common modern layer; no definitional weight |

## Abstraction Levels

### Level 0 — Defining Invariant

Four properties. Remove any one and the product is no longer recognizable as an ATS:

1. **Employer-side operation** — the operator is the hiring organization (or staffing firm acting for client employers); users are its recruiting staff and hiring managers. The system manages hiring *for* the employer, not job search *for* candidates.
2. **Position as demand-side object** — candidates are tracked against named openings/jobs/requisitions the employer wants filled. Without this, the product is a contact database or a posting channel, not an ATS.
3. **Candidate records with per-position applications** — identified person records, each carrying one or more applications/considerations bound to a position, with intake source.
4. **Tracked selection workflow toward a recorded outcome** — each application moves through a defined pipeline of selection stages (screen/interview/offer…) under recruiter action, ending in recorded terminal outcomes: hired or rejected (rejection reason-coded; in the agency variant, placed).

Historical check (§24): 1990s resume-database ATS (requisition + parsed applicant records + status codes), regional products, platform-native employer tools, and SMB trackers all satisfy this without scorecards, self-scheduling, approvals, job-board syndication, AI, or CRM layers. The four properties hold across eras and regions; nothing needs further abstraction.

### Level 1 — Common Mature Structure

Present across the sampled products; expected in the market, not definitional:

- demand-side lifecycle machinery: job approval workflows, requisitions/openings with headcount, close/cancel reasons
- posting distribution: careers page hosting, external job-board syndication, social sharing, posting scheduling
- application forms with screening questions; source tracking; auto-reject rules
- hiring team model: recruiters, coordinators, hiring managers, interviewers; job-scoped permissions; hiring manager self-service
- interview machinery: interview plans per stage, self-scheduling/availability requests, calendar sync, panel coordination
- structured evaluation: scorecards/evaluations, debrief, take-home tests, integrated assessments and video interviews
- offer machinery: offer creation, offer documents with e-signature, offer approval gates, hired state
- rejection machinery: reason-coded disqualification, rejection emails, unreject, candidate blocking
- candidate communication: email/text templates, unified inbox, activity timeline, internal-only comments
- candidate database: talent pools, saved candidates, searching (incl. Boolean/AI), tags, referrals portal
- relationship layer for pre-application prospects (recruiting CRM, strongest on the agency side where client CRM is bundled)
- analytics: funnel/stage/source reporting, time-in-stage, hiring-plan dashboards
- compliance surfaces: EEOC/OFCCP-style demographic reporting, GDPR retention/purge, audit logs
- post-hire handoff: HRIS/onboarding integrations; export of the hired candidate's record

### Level 2 — Variant / Optional Structure

- operator side: in-house talent acquisition vs staffing agency (client accounts, job orders, placements, bill rates) vs RPO
- packaging: standalone ATS vs suite module (HRIS/HCM suites embed recruiting) vs all-in-one talent-acquisition suite
- segment depth: SMB lightweight vs enterprise configurability (approval chains, custom objects, sandbox, BI export)
- AI posture: none → assistive (drafting, matching, auto-reject, fraud detection) → agentic
- internal mobility (internal job boards, internal applicants) as first-class flow
- confidential/restricted jobs and private candidates
- regional/regulatory packaging (EEOC/OFCCP vs GDPR-first vs others), multi-language postings
- channel depth: texting, WhatsApp, video interviewing, background/reference checks as bundled vs integrated vs absent

### Level 3 — Vendor-specific (research notes only)

- Greenhouse: job setup flow steps; Sample Job template providing scorecard attributes + interview plan stages; Prospect Posts; Visual Candidate Pipeline color semantics (red/yellow/gray by next internal action); stage-transition automation rules ("lightning bolt"); private-candidate visibility rules; MyGreenhouse candidate portal branding; per-tier packaging (Core/Plus/Pro).
- Workable: Hiring Plan "Reserved" requisition status (offer out for approval/acceptance); "must be explicitly moved to hired" rule; evaluations hidden from co-panelists until submitted (bias rule; admins excluded); SEEK verified-profile integration; "agentic jobs" AI mode; snooze; plan-gated features (requisitions on enterprise/premier/recruiting plans).
- Ashby: candidate fraud detection; "form field connectors"; "application requests" (outbound invitations to apply); global application rules; job-consideration status terminology.
- Bullhorn: Amplify AI (drafting, 90+ prompts, Ask-Amplify chat); tearsheet-style workflow; Middle Office; Time & Expense; Connexys/Jobscience/Salesforce-based lines; 300+ partner marketplace.
- Recruitee: CareersHub / ReferralsHub / AgencyHub / "WhatsApp Hiring" module naming; Tellent suite membership.

## Rejected Findings

- "ATS = job posting tool" — rejected. Posting/syndication is intake (L1); an ATS still functions for candidates added manually or via agencies (Workable explicitly supports manual entry; Greenhouse supports agency submission).
- "ATS = recruiting CRM" — rejected. Prospects/talent pools are a relationship layer (L1); the CRM module is separable (Greenhouse ships it as a module; Bullhorn bundles client CRM for the agency variant but the candidate pipeline remains distinct).
- "Requisition approval workflows are definitional" — rejected. Approval machinery is L1 (plan-gated in Workable; optional in Greenhouse openings). Older/simpler ATS run without them.
- "Scorecards/structured interviewing define the ATS" — rejected. This is one philosophy (Greenhouse-branded "structured hiring"); other sampled products evaluate with lighter machinery. Evaluation evidence capture is L1.
- "Job-board syndication is part of the definition" — rejected. Some intake channel must exist, but which channels is variant; posting is a common L1 capability, not the invariant.
- "Agency/staffing ATS is a different Type" — rejected as separate Type. Same four invariants hold (position=job order, candidates, applications/submissions, tracked pipeline → placement); differences are operator-side, object naming, and the bundled client CRM — variant structure (L2).
- "AI features are now definitional" — rejected. All sampled products have AI layers, but pre-AI and low-AI products remain fully recognizable ATS.

## Boundary Findings

### vs Recruiting Management Platform (sibling leaf §09, next in directory)

The market uses "applicant tracking system," "recruiting software," and "recruiting management platform" nearly interchangeably: Workable calls itself "recruiting software" with an ATS core; Ashby calls itself "an all in one recruiting tool"; Bullhorn's product page is literally titled "applicant tracking system software." No sampled product draws a structural line between the two names. Reading of the evidence: "ATS" names the candidate-tracking core (the four invariants); "recruiting management platform" is the market's umbrella framing when sourcing CRM, scheduling, analytics, and employer-branding tools are bundled around that core. Probable Alias/umbrella relationship — flagged for joint review when Recruiting Management Platform is processed. This leaf documents the candidate-tracking core; suite breadth is L1/L2.

### vs Job Board (sibling leaf §09)

Job board = candidate-side discovery surface (search jobs, apply); ATS = employer-side management surface (track applicants). The seam is the application: the ATS receives what the job board delivers. Evidence: Greenhouse/Workable/Recruitee all have "job boards" sections meaning *distribution to* external boards; none of them provides candidate-side search. Test: remove the employer's hiring pipeline → what remains is a board; remove candidate-side discovery → the ATS remains intact.

### vs Career Site Platform (sibling leaf §09)

Careers site = employer-branding/publishing surface; ATS products either host one (Greenhouse Careers page section, Recruitee CareersHub, Workable Careers page section) or feed one. Publishing is L1; the site alone has no pipeline. Test: delete the pipeline → publishing site remains (that's Career Site + Job Board territory); delete publishing → ATS remains.

### vs Interview Scheduling Platform (sibling leaf §09)

Scheduling appears in every sampled ATS as embedded machinery (Greenhouse scheduling sections with self-schedule flows; Workable schedule-event action; Ashby Interviews & Scheduling; Recruitee Calendar and scheduling). Standalone scheduling products exist but serve as integrations. Capability-of-Type, not its own Type boundary conflict — but standalone scheduling products are typically integration partners, and the leaf should be checked against the "capability vs Type" rule when processed.

### vs Candidate Assessment Platform / Background Check Platform / Offer Management Platform (sibling leaves §09)

Same pattern: assessment, background/reference checks, and offer documents/e-signature appear in every sampled ATS as embedded or integrated capabilities (Greenhouse sections: Candidate testing, Reference check, Candidate background check, Electronic signatures, Offers; Workable toolbar actions: evaluate, background check, reference check, e-signature; Ashby: Offers & E-Signatures; assessments integrations). Deep-functioning standalone products exist in these niches; inside the ATS they are steps of the pipeline. Boundaries held; flagged for awareness during those leaves' passes.

### vs HRIS / Employee Onboarding Platform (§09)

The seam is the hiring event. The ATS owns candidate → offer → hired; onboarding begins at the hiring event (already documented in research/employee-onboarding-platform.md: "the ATS owns candidate → offer; onboarding begins at the hiring event"; Click Boarding positions itself "between ATS and HRIS"). Evidence of the seam from the ATS side: Greenhouse has an "HRIS and onboarding" integration section plus HRIS Link; Workable offers "export the candidate to your HRIS" from the profile; Ashby's integrations include a "post-hire" category; Bullhorn ships Onboarding as a separate product line. Test: remove the hiring-event trigger and post-offer task machinery → ATS remains; remove the candidate pipeline → onboarding remains.

### vs CRM (Sales, §07)

In-house ATS keeps a prospect/talent CRM at most (Greenhouse CRM module). Agency ATS (Bullhorn) bundles a *client*-facing CRM — sales pipeline for winning business — alongside the candidate pipeline. These are two different relationship graphs (client organizations vs candidates) inside one product; the sales CRM remains its own Type. No boundary change proposed.

### vs Admissions Management (§23; processed leaf)

Structural analog already recorded in research/admissions-management.md: application → completeness → review → decision → offer, but with different population (students vs job applicants), demand-side objects (programs/terms vs jobs/requisitions), and compliance semantics. Related Type, not the same; the resemblance supports the shared abstraction (application-review pipeline) without merging.

### vs Candidate Search Platform / Talent Sourcing Platform / Candidate Profile Platform / Resume Builder (sibling leaves §09)

Search/sourcing = discovering people (inbound discovery, outbound identification), typically feeding the ATS database (Workable "Search with AI" exists *inside* an ATS; Bullhorn Search & Match "pulls from your database"). Profile platform/resume builder = candidate-side artifacts. The ATS consumes all of these as intake or enrichment. Boundary: management/progression of applications vs discovery/artifact creation.

---

## Uncertainties

1. **Ashby internal behavior** — evidence is knowledge-base-index level; no deep article fetched. Do not make precise Ashby claims; "application requests," "job consideration," and fraud detection are documented feature names only.
2. **Bullhorn object semantics** — product-page evidence only (help.bullhorn.com not fetched). "Job order," "placement," "tearsheet" naming is confirmed at positioning level; exact lifecycle states unverified.
3. **Recruitee deep behavior** — collection index only; requisition-approvals and pipeline mechanics unverified beyond feature existence.
4. **Suite-embedded modules** (Workday Recruiting, SAP SuccessFactors) not sampled; the L0 is abstract enough to cover them (same four invariants inside a suite), but no direct evidence gathered this pass.
5. **Regional products** (Teamtailor, Moka, BeiSen) not sampled; historical desktop-era products not sampled directly — historical check relies on structural reasoning, marked as inference (layer C).
6. **Exact stage vocabularies** vary per product and were deliberately not enumerated as canon (Greenhouse default stages exist but full lists were not pulled).
7. **Candidate-facing surfaces** (portal, self-service status) only partially evidenced (Greenhouse "MyGreenhouse candidates" section title; self-schedule requests pending candidate action) — kept at L1 with moderate wording.

---

## Final Synthesis

An Applicant Tracking System is the employer-side system for running hiring. Its defining core is small: a hiring organization operates it; it tracks named positions/jobs it wants to fill; it holds identified candidate records that carry one or more applications bound to those positions; and each application moves through a tracked selection pipeline — intake → screening → interviews → offer — ending in recorded, reason-coded terminal outcomes (hired or rejected). In the staffing variant the same core runs on behalf of client employers, with job orders, placements, and a bundled client CRM.

Around that core, every mature product adds the same furniture: demand-side lifecycle machinery (job approvals, requisitions/openings with headcount), posting and distribution (careers page, job boards, referrals), application forms with source tracking, a hiring team with role-scoped permissions, interview scheduling, structured evaluation (scorecards), offer machinery with e-signature and approvals, rejection machinery, candidate communication and database/talent pools, funnel analytics, compliance surfaces, and the handoff of the hired record to HRIS/onboarding. Packaging varies — standalone ATS, suite module, all-in-one recruiting platform, agency stack — but the Type is the structure, not the packaging.

The strongest taxonomy flag: "ATS" and "Recruiting Management Platform" are not visibly different structures in the market; the latter reads as the umbrella framing of the same core plus bundled capabilities. Joint review recommended. Capability siblings (interview scheduling, assessment, offer management, background check) appear in every sampled ATS as pipeline-embedded or integrated functions, which is consistent with the directory carving them out as capability leaves; no change proposed from this side.
