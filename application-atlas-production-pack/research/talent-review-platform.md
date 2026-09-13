# Research Notes — Talent Review Platform

## Research Goal

Understand what a Talent Review Platform actually is as an Application Type: what objects exist inside it, who operates it, how a talent review flows through it, what rules and states govern it, and where its boundary sits against neighboring HR/talent Types (Succession Planning, Performance Management, Career Development, Internal Talent Marketplace, People Analytics, Skills/Competency Management, Workforce Planning).

This pass also resolves the joint-review recommendation left by the succession-planning-platform pass (2026-09-08): proposed seam "talent review = the evaluation/calibration event machinery over a population; succession = the role-anchored persistent plan of record".

## Initial Boundary

Initial hypothesis (to be tested, not final):

- Core purpose: run structured, usually periodic reviews in which managers and leaders evaluate a population of workers (high-potential talent, key roles' incumbents, or whole departments) on evaluative dimensions — classically past performance and future potential — calibrate those judgments across evaluators, and produce outcomes (talent pools, succession slates, development actions).
- Primary users: HR/talent staff and line managers/executives; the reviewed employee is normally NOT a direct user (confidential by nature).
- Nearest neighbors: Succession Planning Platform (role-anchored plan of record), Performance Management Platform (individual past-performance occasion), Career Development Platform (employee-side), People Analytics (reporting), Competency/Skills Management (requirements substrate).
- Known confusion risks: (1) "performance calibration" tools (normalize manager performance ratings) share the calibration mechanism but lack the talent dimension and outcomes; (2) 9-box-only reporting tools look like talent review but have no governed occasion; (3) the leaf ships mostly as a suite module, not a standalone product category.

## Research Questions

1. What is the review subject — a population, a person, a role? How is the population selected?
2. What exactly is a "talent review meeting" as an object? What lifecycle/states does it carry?
3. What evaluative dimensions are used? Is performance × potential (9-box) definitional or just the dominant implementation?
4. What does "calibration" concretely mean in-product? Who may adjust ratings and when?
5. What outcomes does a review produce, and where do they land (profiles, pools, plans, goals, tasks, notes)?
6. How do reviews interlock with succession plans and talent pools?
7. What roles exist (facilitator, reviewer, observer, admin) and what can each do?
8. What confidentiality rules apply? Can reviewed workers see their own placement?
9. What interfaces exist (meeting dashboard, matrix, preparation surface, person drill-down)?
10. Where is the boundary vs Performance Management / Succession / Career Development / Analytics?
11. Does the definition survive older/lighter implementations (paper talent review meetings, grid-only reporting tools)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Evidence level |
|---|---|---|
| Oracle Fusion Cloud Talent Management (Talent Review & Succession Management) | enterprise HCM suite module; the only Tier-1 operational docs found | Tier 1 (two full PDF guides, 2025, cached text) |
| SAP SuccessFactors (Career and Talent Development) | enterprise HCM suite module, skills-first framing | Tier 2 (product page) |
| Workday (Talent Optimization) | enterprise HCM suite module, AI/mobility framing | Tier 2 (product page; datasheet thin) |
| PeopleFluent (Talent Management / Succession & Development) | standalone specialist talent suite, mid-to-large, regulated industries | Tier 2 (product pages) |
| TalentGuard (Succession Planning) | mid-market specialist, competency/skills-first | Tier 2 (product page + FAQ) |
| Mitratech Trakstar (Succession Planning use case) | mid-market light pole (9-box grid reporting, no meeting machinery) | Tier 2 (use-case page) |

Rejected/abandoned per network rule: Cornerstone (marketing URL 404; help site JS shell — 2 strikes in the prior succession pass, not retried), Leapsome calibration page (404 ×2), Engagedly (404), Culture Amp succession URL (404), DuckDuckGo search (timeout), Workday datasheet PDF (binary, thin marketing content).

## Sources

- Oracle, "Using Talent Review and Succession Management" (G34441-01, 2025) — https://docs.oracle.com/en/cloud/saas/talent-management/fautr/using-talent-review-and-succession-management.pdf (fetched 2026-09-08; cached text reused from the succession pass)
- Oracle, "Implementing Talent Review and Succession Management" (G34433-01, 2025) — https://docs.oracle.com/en/cloud/saas/talent-management/fatrs/implementing-talent-review-and-succession-management.pdf (fetched 2026-09-08; cached text)
- SAP, Career and Talent Development product page — https://www.sap.com/products/hcm/career-talent-development.html (fetched 2026-09-08)
- Workday, Talent Optimization product page — https://www.workday.com/en-us/products/talent-management/talent-optimization.html (fetched 2026-09-08)
- PeopleFluent, Talent Management + Succession & Development pages — https://www.peoplefluent.com/products/talent-management-software/ , https://www.peoplefluent.com/products/talent-management-software/succession-and-development/ (fetched 2026-09-08)
- TalentGuard, Succession Planning Software page — https://www.talentguard.com/succession-planning-software (fetched 2026-09-08)
- Mitratech (Trakstar), Succession Planning use case — https://mitratech.com/solutions/human-resources/use-cases/succession-planning/ (fetched 2026-09-08)
- Prior-pass context: research/succession-planning-platform.md, applications/succession-planning-platform.md, applications/performance-management-platform.md (Related Types rows)

Research date: 2026-09-08.

## Product A — Oracle Fusion Cloud Talent Management (Tier 1, direct observation)

### Key observations (evidence layer A throughout)

**Framing.** "The talent review process involves one or more talent review meetings. Its purpose is to evaluate workers who are part of the review population, assess their strengths, and address areas of risk for the organization." A dedicated Talent Review work area (My Client Groups > Talent Review) hosts create/edit/conduct of meetings.

**Stakeholders.**
- Facilitators: HR specialist or organizational business leader. Manage and conduct the meeting; add development/performance goals for the review population; create tasks; create notes; add workers to talent pools and succession plans; create pools/plans from the meeting. Only facilitators and Talent Review super users can conduct the meeting; multiple facilitators allowed.
- Participants: line managers. Review worker profile/performance/goals/compensation before the meeting; calibrate ratings of the review population; view worker data (competencies, degrees) on the worker's "person spotlight". Participants can be designated reviewers or observers.
- Review access can be granted to other managers below a reviewer in the hierarchy to submit data for their own direct reports.

**Ratings (evaluative dimensions).** Any of these delivered ratings can be included in a meeting template: Performance, Potential, Overall Competencies, Overall Goals, Impact of Loss, Risk of Loss, Talent Score; custom ratings from Profiles also possible. "You can review worker ratings for any level of the organization… as a single group, or filter workers by job, location, or other categories." Rating updates made in the meeting appear in worker profile data, identifiable as "talent review ratings" — distinct from performance evaluation ratings. FAQ: changing the performance rating in a talent review does NOT affect the performance evaluation rating; the talent-review rating is recorded separately in the profile.

**Meeting lifecycle (states).** Template → meeting creation → content preparation → conduct → submit (Complete) → manage notes/tasks. Concrete states observed:
- Before meeting start date: facilitators can open the meeting and only view the dashboard.
- On/after meeting start date: status changes to "In progress"; changes allowed.
- On facilitator submit: "The meeting status changes to Complete and you can no longer update ratings" — but viewing, notes, tasks, and adding workers to pools/plans remain possible.
- Reopening a completed meeting is a supported governed operation (with process-job statuses "Process job in progress"/"Process job error" to monitor deletion/reopen).
- Deleting a completed meeting removes it and REPLACES the ratings sent to profiles with the ratings effective before the deleted meeting; notes and tasks are deleted.

**Meeting creation.** Facilitator selects a template, schedules the meeting (meeting date), selects the content available for pre-meeting preparation, selects participants (reviewers vs observers), and identifies the review population. Optional "data submission deadline" (server time zone) gates reviewer preparation; reminder notifications can be sent; facilitators get notified when reviewers submit.

**Review population selection.** Three methods: Find by criteria (name/person number; filters incl. manager + direct/all reports, matrix-manager reporting relationships, location, assignment status, worker type, management level), Find in talent pool, Find by analysis (a saved BI analysis). Employees from other organizations than the business leader's can be included. Population can be reviewed and trimmed before continuing.

**Content preparation.** Reviewers submit ratings for their direct and indirect reports before the meeting: performance, potential, overall competencies, overall goals, impact of loss, risk of loss, talent score. Submitted changes appear in the reviewed workers' profiles. Prior ratings from previous completed meetings can be pulled in for comparison ("Talent Review Prior Ratings"; a prior-rating date range can be set; only the most recent rating in range is considered).

**Conducting the meeting.** Facilitator starts the meeting; participants provide information about worker ratings; the facilitator calibrates the ratings on the dashboard. Workers not assessed before the meeting appear in a "Holding Area" (if enabled) and can be dragged onto the box chart and back; on submit, holding-area workers' ratings for that meeting are set to blank in profiles. Facilitator actions during the meeting: view/update the box chart; review profile and compensation details per worker (person spotlight); compare current data to previous meetings; compare a worker to another worker or to a job profile; open the org chart of the reviewed organization; add workers to talent pools or succession plans (if included in the template); move workers between box chart and Holding Area; assign performance and development goals (goals created in the meeting are automatically assigned to the worker as individual goals, visible in the worker's goal/career pages); assign tasks to anyone in the organization; create notes for workers; save or submit (submit freezes the data).

**Meeting dashboard.** Box chart matrix (graph view) plus table view; display options (e.g., age, mobility) with per-box or across-boxes summary counts color-coded by legend; filter/find workers; actions per meeting template configuration.

**Box chart configurability (Implementing guide).** Templates (Manage Talent Review Templates page) configure: ratings options; box chart matrix options; data options; analytic options; population filters; actions options; color code options; display options; potential assessment questionnaire; notification settings. Box chart views: XY View (two ratings as axes) or Single Rating View (one rating as lone measure); the number of boxes derives from the rating models' category counts (e.g., 2-category performance × 3-category potential = 6 boxes, 2×3) — i.e., the matrix is NOT inherently 3×3; the 9-box is the classical instance. Facilitators can switch views during the meeting and update the ratings exposed as views.

**Outcomes and integration.**
- Ratings written back to worker profiles on submit (as talent-review ratings, a distinct source).
- Goals: facilitator can assign performance/development goals from the goal library; workers see them in their own goal pages.
- Tasks: assigned to anyone in the organization; tracked to completion on a Tasks page.
- Notes: created for workers; can be hidden/unhidden by the note's subject or an HR specialist with access.
- Talent pools: can be created from the meeting; review populations can be rolled up into pools and re-used as future populations ("Roll up talent review populations").
- Succession plans: can be associated with the meeting; workers added from the meeting dashboard; plans created from the meeting. "How Succession Plans, Talent Pools, and Talent Reviews Work Together": set up meetings with associated plans/pools; add pool members to the review population; add review-population members to plans/pools during the meeting.
- Reporting: calibrated ratings appear in reports only after the facilitator submits the meeting; OTBI subject area gated by a specific duty privilege.

**Access/confidentiality.** Plan privacy and ownership determine plan access in talent review meetings; security profiles scope talent pool visibility; review access delegation is explicit (grant to subordinate managers). The reviewed worker is not a meeting actor; nothing in the guides suggests workers see their own talent-review placement (their visibility is limited to goals assigned to them).

## Product B — SAP SuccessFactors (Tier 2, positioning-level)

- Career and Talent Development = "skills-based development and talent planning"; "Strategic talent planning for intelligent skills-based decisions"; "Build a robust talent pipeline and evaluate potential successors with AI-assisted insights"; "Make intelligent, skills-based decisions and identify priorities for growth at the team level."
- Confirms: talent planning as a distinct activity inside the suite; potential evaluation of successors; team-level growth priorities. No operational meeting machinery visible at this evidence level. Help portal not reachable (JS-gated per prior pass).

## Product C — Workday (Tier 2, positioning-level)

- Talent Optimization: "Talent visibility and talent pipeline"; Succession Planning with "smart tools for identifying critical positions and talent gaps"; Manager Insights Hub ("automated insights and timely suggestions about their team's career growth"); Career Hub; Talent Marketplace.
- Confirms: talent visibility/pipeline as a suite capability; manager-facing insights surfaces. No talent-review meeting machinery visible at this evidence level; community docs login-walled.

## Product D — PeopleFluent (Tier 2, positioning-level)

- Succession & Development: "keep track of top-performing, high-potential employees… map their career path options"; "Understand Your Bench… their skills, strengths, and potential"; "calibrate your succession plans according to your talent pool and business needs" via "an intuitive drag-and-drop interface"; predictive analytics for flight risk; gap/trend analysis; scenario modeling.
- Unified Talent Profiles centralize job, job history, goals, competencies, skills, salary awards, career ambitions.
- Confirms: calibration vocabulary, potential/bench framing, drag-and-drop people surfaces, risk analytics. Meeting machinery not visible at this evidence level.

## Product E — TalentGuard (Tier 2, positioning-level)

- Succession: talent pool builder, targeted internal talent search (verified skills, competencies, performance, career aspirations, manager recommendations), objective candidate evaluation (side-by-side match %, time-to-readiness), bench strength/tenure risk views, ideal-candidate finder.
- FAQ: "A '9-box grid' helps leaders compare employees side by side, identify gaps, and guide discussions about who is prepared to advance."
- Confirms: 9-box as discussion guide; competency/skills-first evaluation substrate. No meeting machinery visible at this evidence level.

## Product F — Mitratech Trakstar (Tier 2, positioning-level; the light pole)

- "9-Box Grid Reporting: See your entire workforce or segment by department in a 9-Box Grid report to uncover where your workforce lands from Top Talent to Underperformers."
- "Hidden Competency Ratings: …key competencies around Potential through scores given in a hidden section, discreetly collected without sharing any sensitive information."
- Unbiased data collection via performance reviews and check-ins; compensation recommendations via hidden sections.
- Confirms: performance × potential grid computed from review data as REPORTING; potential collected discreetly via hidden review sections. No governed review occasion, no facilitator/calibration act, no meeting lifecycle — the light pole of the Type.

## Cross-product Comparison

| Structure | Oracle (A) | SAP (B) | Workday (B) | PeopleFluent (B) | TalentGuard (B) | Trakstar (B) |
|---|---|---|---|---|---|---|
| Selected review population | explicit (criteria/pool/analysis) | implied (talent planning) | implied (talent pipeline) | implied (high-potential tracking) | implied (pools/search) | whole workforce/segment (report scope) |
| Governed review occasion (meeting lifecycle) | explicit (template→prepare→conduct→complete) | not visible | not visible | not visible | not visible | ABSENT (reporting only) |
| Evaluative ratings incl. future potential | explicit (performance, potential, competencies, goals, risk/impact of loss, talent score) | "evaluate potential successors" | implied | "strengths and potential" | 9-box, competencies | performance × potential (hidden potential ratings) |
| Calibration across evaluators | explicit (facilitator calibrates on dashboard) | not visible | not visible | "calibrate your succession plans" (drag-and-drop) | "guide discussions" | absent |
| Recorded people outcomes | explicit (profile write-back, pools, plans, goals, tasks, notes) | pipeline building | pipeline | succession plans, development | pools, readiness | none beyond the report |
| Matrix visualization | box chart (configurable N×M) | not visible | not visible | implied | 9-box | 9-box report |
| Risk of loss / flight risk | explicit ratings | not visible | not visible | predictive flight risk | flight-risk alerts | absent |

Reading: the population + evaluative-assessment-with-potential + outcomes pattern is visible across all six; the governed occasion with calibration is explicit only at Oracle and vocabulary-supported at PeopleFluent/TalentGuard; the light pole (Trakstar) keeps population + assessment but drops the occasion — confirming the occasion is load-bearing for the full Type and that grid-only tools are a capability slice.

## Canonical Abstraction

### L0 — Defining Invariant (four jointly-held structures)

```text
Review population (selected workers under joint assessment)
└── Governed review occasion (facilitated meeting/process with a lifecycle)
    └── Calibrated evaluative assessment (per-person ratings incl. a future-oriented
        dimension, adjusted across evaluators)
        └── Recorded people outcomes (ratings to records + durable outcomes per person)
```

1. **Review population** — a deliberately selected set of workers brought under joint assessment (by hierarchy, criteria, pool, or saved analysis). Remove → individual performance reviews or HR reporting with no review subject.
2. **Governed review occasion** — a scheduled, facilitated meeting/process with named facilitators and participants, a preparation phase, and a conclude-and-freeze lifecycle. Remove → static grid reporting (Trakstar pole) or people analytics.
3. **Calibrated evaluative assessment** — per-person evaluative ratings across the population, classically spanning past performance AND future potential (plus configurable dimensions), adjusted and agreed across evaluators during the occasion rather than set by one manager alone. Remove → performance management (individual, past-focused) or uncalibrated manager opinion.
4. **Recorded people outcomes** — the review concludes into durable outcomes attached to people: calibrated ratings written to worker records, talent pool membership, succession candidacy, development goals, tasks, notes. Remove → a discussion with no record.

Jointly-held is load-bearing: population without occasion = grid-reporting slice; occasion without population = generic meeting tool; assessment without calibration = performance-rating normalization (adjacent to performance management); outcomes without assessment = note-taking; 1+3 without 2 = computed 9-box report; 2+3 without 4 = a discussion with no record.

The future-oriented dimension is held inside L0 (as part of the assessment's character, not as a named "potential rating"): what makes a review a TALENT review is that it judges what people could become, not only what they did. The exact axis set (performance × potential, competencies, risk/impact of loss, talent score) is configurable — the classical 9-box is the dominant instance, not the invariant (Oracle documents 2×3 and single-rating views).

### L1 — Common Mature Structure

- Talent matrix / box chart as the meeting's central visualization (classically 3×3 performance × potential; configurable dimensions and views in mature products)
- Pre-meeting content preparation (reviewers submit ratings for their people before the meeting; deadline- and reminder-governed)
- Facilitator / reviewer / observer role separation; review-access delegation down the hierarchy
- Prior-ratings comparison (current meeting vs previous completed reviews)
- Person-level drill-down during the meeting (profile, competencies, goals, compensation)
- Notes and tasks attached to reviewed workers, tracked after the meeting
- Hand-off to talent pools and succession plans (add workers from the meeting; pools roll up populations)
- Risk-of-loss / impact-of-loss (flight-risk) ratings
- Write-back of calibrated ratings to worker profiles as a distinct, labeled rating source

### L2 — Variant / Optional Structure

- Population scope: high-potential/key-talent only vs whole departments/organization
- Cadence: annual cycle vs rolling/ad-hoc reviews
- Reusable meeting templates (configurable blueprints: ratings, matrix views, actions, population filters, notifications)
- Potential assessment questionnaires
- Display overlays (demographics, mobility, diversity) for representation checks
- Employee visibility of outcomes: typically none for ratings/placement; development goals assigned in the review may be visible to the worker
- AI-era assistance (AI-suggested ratings/successors, agents)
- Suite module vs standalone packaging

### L3 — Vendor-specific (research notes only)

- Oracle: Talent Review work area; Manage Talent Review Templates; Holding Area; person spotlight; deep links; OTBI subject areas + duty privilege; Transaction Design Studio; meeting statuses (In progress / Complete; process-job statuses for delete/reopen); data-submission deadline in server time zone; deletion restoring prior ratings; scheduled processes; Talent Review super users; goals auto-assigned as individual goals.
- SAP: AI-assisted successor evaluation; talent intelligence hub; Succession/Career Development agents (1H 2026 release notes).
- Workday: Manager Insights Hub; Career Hub; Talent Marketplace framing.
- PeopleFluent: scenario modeling; drag-and-drop calibration of succession plans; predictive flight-risk analytics; OrgPublisher lineage (sibling product).
- TalentGuard: match percentage, time-to-readiness, ideal-candidate finder (succession-side machinery).
- Trakstar: hidden sections on performance reviews for potential ratings; 9-box grid report; compensation recommendations via hidden sections.

## Vendor-specific Findings

None of the L3 items were promoted into the canonical document. The box chart's configurability (N×M, single-rating views) is Oracle-documented; it is used to justify keeping "9-box" OUT of the defining core, but the specific template machinery stays in research notes.

## Boundary Findings

- **vs Succession Planning Platform (§09 sibling, processed 2026-09-08) — joint review RESOLVED**: the proposed seam holds from this side. Talent review is the evaluation/calibration EVENT machinery over a population: meetings are occasions that conclude and freeze (Oracle: submit → Complete → ratings locked; deletion restores prior ratings). Succession is the role-anchored persistent RECORD: plans hold role + slate + readiness between and across occasions. Interlock confirmed in-product (Oracle): plans/pools associate with meetings; pool members feed review populations; review-population members are added to plans/pools from the meeting dashboard. Keep both Types. Test: remove the occasion and persist per-role slates → succession; remove the per-role record and keep the population occasion → talent review.
- **vs Performance Management Platform (processed)**: performance management evaluates ONE employee's completed performance over an occasion and is employee-visible; talent review evaluates a POPULATION for talent decisions, is future-oriented, and is confidential. Performance ratings are an input (Oracle pulls overall performance ratings from performance documents as one possible source). Performance-rating calibration (normalizing manager ratings) is a mechanism talent review borrows; a calibration-only tool lacks the potential dimension and the talent outcomes → stays in performance-management territory.
- **vs Career Development Platform (processed)**: organization-owned confidential evaluation vs employee-owned visible growth plan. Outcomes cross over: goals assigned in a talent review become the worker's individual goals (Oracle) — the review assigns INTO the career-development system but does not own it.
- **vs Internal Talent Marketplace (processed)**: curated confidential evaluation vs open expression of interest in visible opportunities.
- **vs People Analytics Platform**: analytics reports on talent data; talent review is the governed occasion that PRODUCES judgments (calibrated ratings) — analytics consumes them. A reporting-only 9-box tool is analytics-shaped, not talent-review-shaped.
- **vs Skills/Competency Management (processed)**: competency ratings are evaluation inputs; the competency model lives in the skills layer (Oracle: overall competencies rating comes from Profiles).
- **vs Workforce Planning Platform (processed)**: aggregate headcount demand/supply vs named-people evaluation. Different subject grain.
- **vs Employee Engagement / Survey Platform**: sentiment measurement vs capability judgment; different objects entirely.
- **Light-pole drift**: 9-box-only reporting tools (Trakstar page) lack the governed occasion; held as the Type's thin edge / capability slice, consistent with how the succession pass held its own light pole.
- **Packaging note**: no standalone talent-review-only product was sampled; the Type ships predominantly as a module/capability of talent management suites. The directory leaf is kept as a Type (the machinery is real and structurally distinct), with packaging recorded as a variant.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit? Paper-era talent review: an annual talent review meeting with pre-printed 9-box grids, managers submitting ratings beforehand, an HR-facilitated discussion moving names on the grid, outcomes recorded as pool membership, succession chart entries, and development notes. All four L0 structures present without any software: population ✓, occasion ✓, calibrated assessment ✓, recorded outcomes ✓. The definition does not depend on cloud, templates, AI, or even the 9-box specifically (any governed matrix of evaluative dimensions qualifies). Conversely, a modern dashboard that only COMPUTES a 9-box report fails the occasion leg — correctly held as a capability slice. Historical check passed.

## Uncertainties

- Only Oracle provided Tier-1 operational documentation. SAP, Workday, PeopleFluent, TalentGuard, and Trakstar claims rest on product-page (positioning-level) evidence; meeting-machinery specifics (templates, holding area, statuses, deadlines) are asserted only for Oracle and not generalized to the Type.
- No standalone talent-review-only product was found in the sampled market; whether a pure-play segment exists is unverified.
- Whether any product exposes potential ratings or grid placement to the reviewed employee is unverified; held as an open question (Oracle evidence shows workers see goals assigned to them, not their placement).
- Calibration mechanics beyond Oracle (e.g., SAP's calibration capability) unverified.
- The relative market weight of "talent review" as a separately purchased capability vs a bundled succession feature could not be verified from public pages.

## Final Synthesis

A Talent Review Platform is the organization-side machinery for governed evaluative review of a selected worker population. Its defining core is four jointly-held structures: the review population, the governed review occasion (facilitated meeting with a prepare→conduct→conclude lifecycle), the calibrated evaluative assessment (per-person ratings classically spanning past performance and future potential, adjusted across evaluators), and recorded people outcomes (calibrated ratings written to worker records plus durable outcomes: pool membership, succession candidacy, development goals, tasks, notes). The dominant visualization is the performance-by-potential matrix (9-box), but the matrix is an implementation of the assessment structure, not the invariant. The Type's closest sibling is the Succession Planning Platform: event vs record — reviews conclude and freeze; succession plans persist. The Type's thin edge is grid-only reporting, which keeps the population and the assessment but drops the governed occasion.
