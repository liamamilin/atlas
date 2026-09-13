# Research Notes — OKR / Goal Management Platform

## Research Goal

Understand what an OKR / Goal Management Platform actually is as an Application Type: the core objects it manages, the lifecycle goals go through, the check-in and alignment mechanics, the roles involved, and where its boundary sits against Performance Management, Project/Work Management, BI dashboards, and strategy-execution software.

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis):** software for defining organizational goals (usually Objectives with measurable Key Results), cascading/aligning them across levels, tracking progress via periodic check-ins, and reviewing/scoring them at period end.
- **Users (hypothesis):** executives (company goals), managers/team leads, individual contributors (personal goals), program owners (HR/people team, strategy/ops, PMO) administering the program.
- **Nearest neighbors:** Performance Management Platform (reviews/ratings/feedback), Project Management / Work Management (task execution), BI/Dashboard (metric measurement), strategy-execution / strategic portfolio management (broader), Employee Engagement (surveys).
- **Potential confusions:** a task tracker with a "goals" label; a KPI dashboard; a performance-review suite that stores objectives as review inputs.
- **Unknowns:** check-in field mechanics, scoring conventions, alignment models (cascade vs link), whether time-period governance is definitional, how deep permissions go.

## Research Questions

1. What are the core objects (objective, key result, initiative, metric/KPI, check-in, period, alignment link, owner)?
2. What is a goal's lifecycle (set → align → check in → review → score → close/carry over)?
3. What does a check-in capture, and at what cadence?
4. How is progress computed and rolled up (KR → objective → parent objectives)?
5. How does alignment work (strict cascade vs cross-links vs contribution models)?
6. What roles/permissions exist, and who administers the program?
7. What are the main interfaces (tree, list, check-in page, dashboards, admin console)?
8. What rules matter (ownership, transparency, timeboxing, mid-cycle edits, scoring)?
9. How do goals connect to performance reviews and other HR processes?
10. What variants exist (pure-play vs suite module vs strategy platform; OKR vs other goal frameworks; SMB vs enterprise)?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence quality reached |
|---|---|---|
| Microsoft Viva Goals | Suite-embedded OKR (Microsoft 365), enterprise | Tier 1 — Microsoft Learn docs (official operational docs). NOTE: product retired 2025-12-31; used as documented structural evidence, not a current-market sample |
| Profit.co | Multi-framework OKR platform (OKR + BSC + Hoshin Kanri), SMB→enterprise | Tier 2 — official site, FAQ, help-center structure |
| Lattice | Goals & OKRs module inside people-performance suite, mid-market/enterprise | Tier 2 — official product page + FAQ + changelog |
| Weekdone | Pure-play OKR + weekly reporting, SMB (10–1000 employees) | Tier 2 — official site + product page |
| WorkBoard | Enterprise AI-native strategy execution & OKR | Tier 2 — official homepage |

Rejected/abandoned samples: 15Five (help center login-walled; product URL 404), Perdoo (help center transport errors ×2), Tability (docs JS-rendered empty), Quantive (acquired by WorkBoard — trademark confirmed on workboard.com footer).

## Sources

Fetched 2026-09-08:

- Microsoft Learn — Viva Goals: Introduction (learn.microsoft.com/en-us/viva/goals/), Get to know OKRs (…/get-to-know-okrs), retirement notice (…/goals-retirement)
- Profit.co — homepage (profit.co), help center (profit.co/helpcenter/, /help-center/okr-manangement/), FAQ block on homepage
- Lattice — Goals product page (lattice.com/products/goals), FAQ, product-updates changelog excerpts
- Weekdone — homepage (weekdone.com) + product page (weekdone.com/product)
- WorkBoard — homepage (workboard.com)

**Source-access limitations (affecting assertion strength):**

- No Tier-1 operational help center was reachable for any **live** sampled product: 15Five help redirects to login; Lattice help center 404 on two URL patterns; Perdoo help transport-error twice; Tability and Weekdone help centers are JS-rendered (empty content). Microsoft Learn (Viva Goals) is the only fully operational-doc source, for a product now retired.
- Consequently, most claims below are Layer A only at product-marketing depth, or Layer B cross-product commonality. Per the evidence rules, this research avoids precise numeric/operational claims (scoring scales, KR counts, cadence defaults, privacy settings, permission matrices) because the evidence does not support that precision. No detail has been filled from model memory.

## Product Observations

### Microsoft Viva Goals (Microsoft Learn — official docs; retired product)

Evidence layer: A (operational docs).

- **Object vocabulary (verbatim from docs):** Objective = "a high-level description of something your team wants to accomplish"; Key result = "a quantifiable goal that helps you measure progress toward one of your objectives"; Initiative = "a focused effort geared toward helping you achieve one or more key results"; "Goal" is a catch-all term for objective, key result, or initiative.
- **Check-ins:** "Check-ins are how you update and share progress on your OKRs. When you update progress on a key result, it automatically updates the status of the parent objective as appropriate." → KR progress auto-rolls-up to parent objective status.
- **Alignment:** docs show company objective with nested marketing and product objectives (parent/child hierarchy).
- **Admin surfaces (TOC titles):** roles and permissions; create/edit teams and subteams; invite/remove users; manage OKR time periods; configure OKR model; review dashboard; close and score OKRs; integrations overview.
- **Retirement:** product retired 2025-12-31; no new feature development since Dec 2024; data export via API/Excel/PowerPoint recommended. (Market note: platform-suite OKR entrant exited.)

### Profit.co (official site + FAQ + help-center hub)

Evidence layer: A (official product surfaces); FAQ is vendor-claimed capability depth.

- **Module map (nav):** Strategy (OKRs, Strategy Roadmaps, Balanced Scorecard, Hoshin Kanri) / Performance (Performance Review, Employee Recognition, Pulse Surveys, Meetings) / Projects (Project Portfolio, Project Management, Tasks, Timesheets). → OKR sits inside a multi-framework strategy + performance + projects platform.
- **Cascade (FAQ, verbatim):** "Profit.co's cascade engine flows company-level objectives down through departments to individual contributors automatically. Every key result aligns to a parent OKR, creating a visual alignment map with live progress – so leaders always see how strategy is being executed across every team."
- **Multi-framework (FAQ, verbatim):** "natively supports OKRs, Balanced Scorecard, Hoshin Kanri, and Strategy Roadmaps… Organizations can run multiple frameworks simultaneously, with the same underlying data powering every view."
- **Check-ins:** dashboard screenshot caption "OKRs dashboard with check-in trends and contributing key results"; AI authoring describes "measurable objective with owners, targets and check-in cadence"; AI Progress agent "Monitors every OKR in real time and flags at-risk goals".
- **AI quality scoring:** "Scores every OKR for clarity and measurability, catching vague goals before they reach your teams." (era-current, vendor-specific implementation)
- **Reviews linkage:** "Link every review to OKR progress with 360° feedback, calibration…" → goals feed performance reviews in the same suite.
- **Lifecycle article title:** "The OKR Lifecycle: Planning, Executing, and Closing Quarterly Goals — the four phases of the OKR lifecycle — from drafting ambitious objectives to scoring results and carrying learnings into the next quarter."
- **Help center structure:** Super User Guide vs End User Guide → two-tier program/user role split.
- **Roles marketed:** CEO, HR Leaders, Individual Contributors, Managers, PMO Leaders, Strategy & Transformation, Operations Leaders.

### Lattice (product page + FAQ + changelog)

Evidence layer: A (official product surfaces).

- **Positioning (verbatim):** "Set, track, and align goals and OKRs in one place… Bridge strategy and execution through aligned objectives at every level — from leadership to individual work."
- **Goal cycles (FAQ):** "customizable goal cycles, visual progress tracking"; goals "can be customized or updated during the cycle" / "adjust goals mid-cycle to accommodate changing priorities."
- **Cascading vs non-cascading (FAQ, verbatim — key structural evidence):** "Cascading goals in Lattice are aligned to one another and **accept the progress of their supporting goals**, creating a hierarchical structure. Non-cascading goals are independent and do not inherit progress from other goals."
- **Suite linkage:** "OKRs in Lattice connect directly to 1:1s, performance reviews, and company-wide dashboards."
- **Integrations:** Slack, Teams, Jira.
- **Changelog signals:** "Needs Update" view (stale-goal surveillance), goal history, goal duplication, admin bulk updates — check-in enforcement and governance machinery.
- **Adjacent modules on same page:** 1:1s, Weekly Updates, Feedback, Q&A Boards, Habits → people-performance suite where goals are one module.

### Weekdone (homepage + product page)

Evidence layer: A (official product surfaces).

- **Cadence philosophy (verbatim):** "Set, track and align structured goals via quarterly OKRs. Know what everyone is doing via weekly check-ins." — quarterly OKRs + weekly check-ins/PPP as the product's signature rhythm.
- **Levels:** "Company, department, team and personal levels"; "Annual and quarterly OKRs"; "OKR hierarchy tree & company-wide alignment"; "Align and Link OKRs."
- **Goal shapes:** "Moonshot & roofshot goals"; "KPI and metric tracking"; "Projects and Initiatives"; "Link projects and tasks under OKRs."
- **Check-in mechanics:** "Weekly Plans, Progress, Problems reporting"; "Employee check-ins, insights and feedback"; "Notifications & reminders to engage employees"; "Customizable weekly planning form."
- **Status representation:** "Goal setting with color coded OKRs"; auto-colored OKR progress; "Understand OKR progress throughout the company at a glance."
- **Reporting:** "OKR, KPI and weekly progress dashboards"; hierarchy/tree views; "Automated e-mail reports"; TV dashboard slideshow for office display.
- **Suite adjacency:** continuous performance management module — pulse surveys, 5-point ratings, 1:1s, kudos/CFRs.
- **Tier:** "Built for SMBs. Ideal for 10 to 1000 employees."

### WorkBoard (homepage)

Evidence layer: A (official homepage, marketing depth).

- **Positioning (verbatim):** "AI-Native strategy, OKR and strategic portfolio management"; "Align OKRs across the enterprise"; "Agent-orchestrated OKR cycle."
- **Enterprise operating cadence:** "Automate MBRs, scorecards, and QBR materials and pre-reads" → goals feed executive business reviews.
- **System of record** named as a product surface ("Strategy, outcomes, initiatives, funding, OKRs, teams, skills, projects, operating model" in the knowledge graph).
- **Market consolidation note (footer, verbatim):** "Outcome Mindset, Method, Enterprise Results Management, and Quantive are trademarks of WorkBoard Inc." → Quantive (formerly Gtmhub), a leading independent OKR vendor, is now absorbed by WorkBoard.

## Cross-product Comparison

| Dimension | Viva Goals | Profit.co | Lattice | Weekdone | WorkBoard | Evidence |
|---|---|---|---|---|---|---|
| Goal of record: named objective w/ accountable owner | ✔ (objective, owned) | ✔ ("owners, targets") | ✔ (goals owned, assignable) | ✔ (per-level OKRs) | ✔ (OKRs owned by teams) | B (5/5) |
| Measurable outcomes under goals (key results) | ✔ (KRs quantifiable) | ✔ (KRs align to parent OKR) | ✔ (objectives + key results) | ✔ (KRs + KPIs/metrics) | ✔ (key results in scorecards) | B (5/5) |
| Alignment structure across levels | ✔ (nested company→team objectives) | ✔ (cascade engine, alignment map) | ✔ (cascading goals, hierarchy) | ✔ (hierarchy tree, align & link) | ✔ ("align OKRs across the enterprise") | B (5/5) |
| Progress roll-up through alignment | ✔ (KR update auto-updates parent status) | implied ("live progress" map, contributing KRs) | ✔ (cascading goals accept supporting progress) | implied (tree "total progress") | implied (scorecards) | B (5/5; explicit A in 2) |
| Recurring check-ins | ✔ (check-ins update/share progress) | ✔ (check-in trends, cadence config) | ✔ ("Needs Update" surveillance) | ✔ (weekly PPP check-ins) | ✔ (agent-orchestrated cadence) | B (5/5) |
| Time periods structure goals | ✔ (manage OKR time periods) | ✔ (quarterly lifecycle; "first OKR cycle") | ✔ (customizable goal cycles) | ✔ (annual + quarterly) | ✔ (QBR/MBR cadence) | B (5/5) |
| Period close / scoring / carry-over | ✔ (close and score OKRs) | ✔ (scoring results, carrying learnings) | not directly evidenced | not directly evidenced | implied (OKR cycle orchestration) | A×2, rest implied → keep generic |
| Status/health representation | ✔ (status per docs) | ✔ (at-risk flags) | ✔ (progress tracking, Needs Update) | ✔ (color-coded OKRs) | ✔ (scorecards) | B (5/5) |
| Initiatives/projects/tasks linked to goals | ✔ (initiative defined) | ✔ (initiatives/projects linked) | via Jira integration | ✔ (link projects & tasks under OKRs) | ✔ (initiatives/projects in graph) | B (5/5) |
| Leadership dashboards/reports | ✔ (review dashboard) | ✔ (dashboards, board reports) | ✔ (company-wide dashboards) | ✔ (dashboards, email reports, TV view) | ✔ (MBR/QBR automation) | B (5/5) |
| Program admin (teams, periods, roles) | ✔ (roles, teams, time periods pages) | ✔ (super user vs end user guides) | ✔ (admin-enabled features in changelog) | ✔ (company account setup) | ✔ (enterprise admin implied) | B (5/5) |
| Work-tool integrations | ✔ (integrations overview) | ✔ (Jira, Slack, Teams, 100+) | ✔ (Slack, Teams, Jira) | ✔ (integrations) | ✔ (connectors) | B (5/5) |
| KPI/metric tracking alongside goals | not directly evidenced | ✔ (BSC KPI dashboards) | not directly evidenced | ✔ (KPI and metric tracking) | ✔ (scorecards) | B (3/5) |
| Goals feed performance reviews | n/a (standalone) | ✔ (reviews link OKR progress) | ✔ (OKRs → reviews) | ✔ (appraisal reports) | ✔ (performance based on outcomes) | B (4/5; suite/enterprise pattern) |
| Weekly cadence as signature | — | — | — | ✔ (PPP weekly reporting) | — | product-specific emphasis |
| Multi-framework (BSC/Hoshin) | — | ✔ | — | — | strategy pillars variant | vendor-specific/optional |
| AI authoring/monitoring agents | — | ✔ (Athena) | ✔ (AI summaries era-current) | — | ✔ (agents) | era-current, optional |

## Canonical Model

### Level 0 — Defining Invariant

Three jointly-held structures. Removing any one stops the product from being recognizable as this Type:

1. **The organizational goal of record** — a persistent, individually identified goal stating a desired *outcome*, owned by an accountable owner (a person or a team), set within an organizational context at company/department/team/individual levels. Not a task, not a metric line — an owned commitment. (remove → task tracker / project plan / org-chart-with-labels)
2. **The alignment structure** — first-class links binding goals across organizational levels into a visible, navigable structure (hierarchy tree / alignment map). Each supporting goal declares what it supports; progress relationships follow the links. Alignment is an inspectable object of the system, not an implicit convention. (remove → flat goal list; static strategy poster)
3. **The measured check-in loop over a defined period** — goals run within defined time periods; they carry measurable outcomes (key results / metrics) whose values owners update through recurring check-ins; the system computes progress/health, rolls it up through the alignment structure, and surfaces attention flags; periods end with review/scoring and renewal. (remove → static strategy document; remove measured outcomes → aspiration board; remove periods/check-ins → perpetual metric board = BI territory)

**Jointly-held is load-bearing:** 1 alone = goal spreadsheet; 2 without 1 = org chart with nothing attached; 3 without 1+2 = metrics tracker; 1+3 without 2 = personal/team goal tracker (no org alignment); 1+2 without 3 = strategy map that never moves.

### Level 1 — Common Mature Structure

Present across the sample (evidence B) but not required to recognize the Type:

- check-in reminders/notifications and stale-goal surveillance ("needs update")
- status/health representation (color coding, on-track/at-risk flags); some products add confidence ratings and KR weighting (mechanics vary by product — not verified in detail)
- dashboards and reports per team/person/company; export/deck output for business reviews
- goal templates, examples, authoring guidance (increasingly AI-assisted)
- KPI/metric tracking alongside OKR goals
- initiatives/projects/tasks attached to key results (native or via integration)
- integrations: SSO/identity, HR systems, chat tools, work-management tools, data sources
- program administration: org-structure teams, period management, roles/permissions, methodology configuration
- end-of-period close/scoring and retrospectives
- suite adjacency: performance reviews, 1:1s, feedback/recognition, pulse surveys consuming goal data

### Level 2 — Variant / Optional Structure

- **Methodology packaging:** OKR (dominant), MBO-style goals, KPI trees, Balanced Scorecard, Hoshin Kanri, custom goal frameworks; multi-framework single-data-model products exist
- **Period length:** quarterly (dominant), annual, custom; period naming/carry-over rules vary
- **Alignment style:** strict top-down cascade; bottom-up support; free cross-team links; contribution weighting
- **Progress computation:** manual check-ins vs integration-driven auto-updates vs data-source bindings
- **Scoring conventions:** percentage, ordinal scales, qualitative status — no universal standard observed
- **Customer tier:** SMB self-serve vs enterprise program-with-services
- **Suite posture:** standalone pure-play vs module inside people suite vs module inside strategy-execution platform
- **Private/secret goals:** plausible and marketed in the category historically, but NOT verified in this pass — left unclassified

### Level 3 — Vendor-specific Structure (kept in notes only)

- Weekdone's weekly PPP (Plans–Progress–Problems) form as the check-in vehicle; moonshot/roofshot goal classes; TV dashboard
- Profit.co's Athena AI agents (OKR quality scoring, adaptive planning, review agents); BSC/Hoshin modules; cascade engine branding
- Lattice's cascading vs non-cascading goal setting switch; "Needs Update" view; goal duplication; Habits module adjacency
- WorkBoard's agent suite (Chief of Staff, Portfolio Analyst, Leadership Coach), Enterprise Knowledge Graph, MBR/QBR automation, "Outcome Mindset/Method" trademarks
- Viva Goals' M365 integration model; retirement migration tooling (Excel/PowerPoint/API export)

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- **Paper-era MBO program (Drucker-style, 1960s–1990s):** typed objective sheets per manager/employee (goal of record), an annual policy-deployment/cascade chart on the wall (alignment), annual progress reviews with handwritten updates (check-in loop over a defined period) — **satisfies all three legs at analog level.**
- **Hoshin Kanri policy deployment (Japan-origin):** x-matrix cascading annual objectives through catchball — satisfies goal-of-record + alignment; check-in leg satisfied by periodic review rituals.
- **Quarterly OKR spreadsheets (post-Google popularization, 2000s–2010s):** sheet of objectives/KRs with color-coded progress, aligned by row references, updated in weekly staff meetings — satisfies all three legs.
- **Conclusion:** the L0 does not overfit the current SaaS implementation. Quarterly length, scoring scales, confidence ratings, AI machinery, integrations are all era-current capabilities, not definitional.

## Vendor-specific / Rejected Findings

- **Rejected (no evidence fetched):** universal grading scale (e.g., 0.0–1.0), "3–5 objectives per level", "70% achievement = success" doctrine, default check-in frequencies, private-goal defaults, specific permission matrices. These are classic OKR-doctrine claims that were NOT verified in fetched sources; excluded from the final document.
- **Rejected as definitional:** weekly cadence (Weekdone emphasis only), multi-framework support (Profit.co), AI agent orchestration (WorkBoard/Profit.co/Lattice era-current), suite adjacency modules (4/5 but packaged separately).
- **Market-structure findings (notes only):** consolidation — Quantive/Gtmhub absorbed into WorkBoard; Ally.io became Microsoft Viva Goals, which was retired 2025-12-31; the category's independent pure-play pole persists (Weekdone, Tability, Perdoo).

## Boundary Findings

- **vs Performance Management Platform:** the closest sibling, deliberately NOT this Type. Performance platforms center review cycles, ratings, feedback, competencies. Goal platforms center the goal loop (set → align → check in → score). Suites ship both as separate modules and connect them (goal attainment feeds reviews) — connection is evidence of distinctness, not merger. Seam test: remove reviews/ratings → goal platform stands; remove goals → performance platform stands.
- **vs Project Management Application / Work Management Platform:** project tools manage work units (tasks, dependencies, schedules); goal platforms manage outcome commitments (owned, measurable, aligned, timeboxed). The initiative/project layer attached to key results is the bridge — products let work show *under* goals, but execution detail stays the project tool's job. Seam test: replace goals with tasks → project tool.
- **vs Business Intelligence / Dashboard Platform:** both render metrics; goal platforms attach ownership, check-ins, alignment, and period semantics to measures. A dashboard computes numbers; a goal platform makes someone accountable for moving them. Seam test: remove ownership/check-ins → BI dashboard.
- **vs Strategy-execution / Strategic Portfolio Management platforms (WorkBoard, Profit.co's broader suite):** strategy modeling, investment/portfolio decisions, scenario planning are broader machinery; the goal-management loop is the leaf's core. Products spanning both are suite cases, not boundary failures.
- **vs Employee Engagement Platform:** surveys/pulse/sentiment are a different subject entirely; they appear as adjacent modules (Weekdone, Profit.co) but the goal loop is untouched by their removal.
- **vs (sibling leaf) Government Performance Management / Institutional Effectiveness (higher-ed):** domain-specific planning-assessment machinery with its own structures; the org-goal loop defined here is generic-corporate. No alias claim.
- **"去掉什么就变成另一个 Type" 判据：** remove the alignment structure → personal/team goal tracker (To-do/goal-tracker territory); remove the measured check-in loop → static strategy map / org-chart annotation tool; remove goal-of-record semantics (outcomes, owners) → task tracker or BI dashboard; add review cycles/ratings as the center → Performance Management Platform.

## Taxonomy Notes

- The directory leaf name "OKR / Goal Management Platform" uses a slash reflecting market naming spread. Research supports ONE Type whose defining frame is organizational goal management; OKR is its dominant methodology packaging, not a definitional requirement (MBO/BSC/Hoshin/custom-goal products satisfy the core). No rewrite of the taxonomy needed.
- Sibling note for the record: institutional-effectiveness-platform (processed 2026-09-08) itself used "OKR-style goal tracker" as the description of what remains when its leg 1+3 exist without leg 2 — consistent with this pass's boundary.
- Recommend joint review with performance-management-platform when that unprocessed §09 sibling is attempted (suites blur the two; this pass held them distinct).

## Uncertainties

- Exact check-in field sets (confidence ratings, blocker fields, per-KR weighting) — only check-in existence, progress/status updates, and at-risk surveillance verified; field mechanics unverified.
- End-of-period scoring mechanics — "close and score" documented for Viva Goals and "scoring results and carrying learnings" in Profit.co's lifecycle framing; scale conventions unverified.
- Per-goal privacy/visibility controls — unverified in this pass; excluded from the final document.
- Plan-tier packaging differences (which capabilities are gated) — not researched; irrelevant to the canonical model.
- Depth of permission models beyond admin/user split — only Viva Goals doc evidence of roles/permissions surface; generic claim kept soft.

## Final Synthesis

An OKR / Goal Management Platform is the organization's goal-alignment system of record. Its defining core is three jointly-held structures: owned outcome goals held as records; a first-class alignment structure linking them across organizational levels; and a measured check-in loop over defined periods that keeps progress current, computed, and rolled up through the alignment structure. OKR is the market's dominant methodology packaging of this core, but the core is methodology-neutral. Everything else — cadence machinery, dashboards, scoring conventions, KPI tracking, initiative linkage, integrations, suite adjacencies, AI assistance — is common mature or optional structure. The Type is bounded from Performance Management (review/rating center), from Project/Work Management (task-execution center), from BI (measurement without accountability), and from strategy-execution platforms (broader strategy machinery).
