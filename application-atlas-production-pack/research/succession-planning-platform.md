# Research Notes — Succession Planning Platform

## Research Goal

Understand what a Succession Planning Platform actually is as an Application Type: what objects exist inside it, who operates it, how succession work flows through it, what rules and states govern it, and where its boundary sits against neighboring HR/talent Types (Talent Review, Career Development, Internal Talent Marketplace, Skills/Competency Management, Performance Management, Workforce Planning).

## Initial Boundary

Initial hypothesis (to be tested, not final):

- Core purpose: maintain plans that ensure continuity of key roles — identify critical positions, attach candidate slates, evaluate readiness, develop candidates, and surface coverage/bench risk.
- Primary users: HR/talent management staff and senior line managers/executives; NOT the employee as a self-service actor (contrast with Career Development).
- Nearest neighbors: Talent Review Platform (meeting/calibration machinery), Career Development Platform (employee-side growth), Internal Talent Marketplace (open expression of mobility), Skills/Competency Management (requirements substrate), Performance Management (ratings input), Workforce Planning (headcount demand/supply).
- Known confusion risk: "succession planning software" is also marketed for business-owner succession (financial advisory practices, family businesses) — a different subject (ownership transfer), expected to be out of scope for this §09 HR leaf.

## Research Questions

1. What is the planning subject — a position, a job, a person, or all three?
2. What exactly is a "succession plan" as an object? What attributes and states does it carry?
3. How do candidates enter a slate (nomination, search, pools, AI)? What candidate attributes are tracked?
4. How is readiness expressed and used? Is it time-based, category-based, or score-based?
5. What evaluation machinery feeds the slate (performance/potential ratings, 9-box, talent review meetings)?
6. What development machinery attaches (development plans, learning, talent pools)?
7. What analytics exist (bench strength, coverage, risk of loss)?
8. What interfaces exist (plan workspace, org chart, meeting dashboard, person profile)?
9. What rules matter (privacy/confidentiality, ownership, access derivation, alerts, plan status)?
10. Where is the boundary vs Talent Review / Career Development / Internal Talent Marketplace / Competency Management / Workforce Planning?
11. Does the definition survive older/lighter implementations (paper succession charts, spreadsheet replacement charts, 9-box-only tools)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Evidence level |
|---|---|---|
| Oracle Fusion Cloud Talent Management (Talent Review & Succession) | enterprise HCM suite module, deep operational docs | Tier 1 (two full PDF guides, 2025) |
| SAP SuccessFactors (Career and Talent Development) | enterprise HCM suite module | Tier 2 (product pages + FAQ) |
| Workday (Talent Optimization → Succession Planning) | enterprise HCM suite module | Tier 2 (product page) |
| PeopleFluent (Succession & Development) | specialist talent suite, mid-to-large, regulated industries | Tier 2 (product pages) |
| TalentGuard (Succession Planning) | mid-market specialist | Tier 2 (product page) |
| Mitratech Trakstar (Succession Planning use case) | mid-market light pole (9-box reporting) | Tier 2 (use-case page) |

Rejected/abandoned: Cornerstone (marketing URLs 404 ×2, help.csod.com JS shell), Trapolo (transport error ×2), SumTotal docs (transport error), Workday community docs (login-gated).

## Sources

- Oracle, "Using Talent Review and Succession Management" (G34441-01, 2025) — https://docs.oracle.com/en/cloud/saas/talent-management/fautr/using-talent-review-and-succession-management.pdf (fetched 2026-09-08)
- Oracle, "Implementing Talent Review and Succession Management" (G34433-01, 2025) — https://docs.oracle.com/en/cloud/saas/talent-management/fatrs/implementing-talent-review-and-succession-management.pdf (fetched 2026-09-08)
- Oracle Talent Management docs hub — https://docs.oracle.com/en/cloud/saas/talent-management/index.html
- SAP, Talent Management product page + FAQ — https://www.sap.com/products/hcm/talent-management.html
- SAP, Career and Talent Development product page — https://www.sap.com/products/hcm/career-talent-development.html
- Workday, Talent Optimization product page — https://www.workday.com/en-us/products/talent-management/talent-optimization.html
- PeopleFluent, Talent Management + Succession & Development pages — https://www.peoplefluent.com/products/talent-management-software/ , https://www.peoplefluent.com/products/talent-management-software/succession-and-development/
- TalentGuard, Succession Planning Software page — https://www.talentguard.com/succession-planning-software
- Mitratech (Trakstar), Succession Planning use case — https://mitratech.com/solutions/human-resources/use-cases/succession-planning/

Research date: 2026-09-08.

## Product A — Oracle Fusion Cloud Talent Management (Tier 1, direct observation)

### Succession planning purpose (vendor's own definition)

- "Succession planning or succession management can help you to identify successors for key employees."
- Advantages listed: ensure a smooth transition to key jobs and positions; identify workers who are ready now, or who can become ready by developing the necessary skills, for jobs and positions that are likely to become vacant; plan the career development of candidates.

### The succession plan object (Layer A evidence)

- Managed in a dedicated "Succession Plans" work area; overview page lists plans the user can access; default filter shows only Active plans.
- Plan attributes: name, description, plan type, status (Active/Inactive), Private flag, job/position + business unit/department/grade scoping attributes, alerts section.
- Plan types (system lookup): Incumbent ("replace a specific person"), Job ("candidates for a job, such as Business Analyst"), Position ("candidates for a position, such as Senior Vice President for Sales").
- Incumbents: named incumbent (incumbent-type plans) or inferred incumbents ("any person who holds the job or position for which the succession plan is created"); a scheduled "Succession Plan Incumbents" process keeps the incumbent table current with org transfers.
- Plan owners: one or more owners, each with an Administrator Type role — Administrator (full control incl. rename, privacy, owners), Candidate Manager (add/remove candidates, update readiness/risk), Viewer (view only). Private plans require at least one administrator.
- Plan privacy: private plans visible only to named owners + super users; nonprivate plans additionally visible to anyone with access to the named/inferred incumbent. Access examples worked through transfer scenarios (access follows incumbent data-security, not just ownership).
- Plan history: audit page showing date, changed attribute, old/new values, who made the change; grouped by date; baseline from 22B release.
- Alerts (configurable per plan): candidate moves to the plan role; candidate moves to a different role; incumbent changes roles (incumbent plans only). "Moved to plan role" is determined by comparing plan attributes (job/BU/department/grade or position/BU/department) with the candidate's new role.

### Candidates and candidate attributes (Layer A)

- Ways to add candidates: search employees within security access; external candidates; talent pool members (from pools the user owns); Best-Fit candidates (match against the job/position model profile); AI-suggested candidates (based on model profile; replaces Best-Fit when enabled).
- Candidate attributes shown: date added, readiness, status (Active/Inactive), current job title; counts of other plans the person is a candidate in.
- Readiness: "How soon a person can take up the job or position of the plan", selected from a configurable lookup (HRM_READINESS_CATEGORY, extensible; delivered values "Ready now" and "No readiness available"; example values "Ready now, Ready in 1-2 years, Ready in 3-4 years"). Readiness levels of all candidates = bench strength for the job/position ("if no candidate is likely to be ready in the next 2 years, the bench strength is poor").
- Candidate Ranking: order of preference across the whole plan or within a readiness category.
- Interim Successor flag: "can't be considered as an actual prospect but can perform the duties of the incumbent... until an actual successor is identified."
- Risk of Loss ("likelihood of a person leaving"), Impact of Loss ("real or perceived effects on an organization when a person leaves"), Willingness to Relocate, Job Criticality — stored in talent profiles, surfaced on the person's Succession Planning tab.
- External candidates: stored separately from internal candidates; NOT the same as recruiting candidates and not available in the Recruiting work area; minimal attributes (last name required; first name, job title, email, phone optional); cannot carry risk-of-loss/impact-of-loss/relocation values.
- Maximum 500 candidates per plan (error if exceeded) — product-specific precise limit.

### Evaluation machinery (Layer A)

- Talent review meetings: template-configured; review population; reviewers submit ratings pre-meeting (performance, potential, overall competencies, overall goals, impact of loss, risk of loss, talent score, custom ratings); facilitator calibrates on a box-chart matrix dashboard during the meeting; Holding Area for unassessed workers; notes, tasks, and goal assignment; meeting submission freezes data and writes ratings back to worker profiles.
- Box chart matrix: configurable axes/views combining any of the delivered ratings; the performance×potential view is the classic 9-box shape (product supports configurable combinations).
- Talent score: "overall value to the organization using a rating model your organization defines... factors beyond performance and potential... might include readiness, ability to mentor, and learning agility."
- Best-Fit analysis: person-to-job, person-to-person, job-to-job, job-to-person profile matching against model profiles; default results show profiles with ≥90% match (product-specific default).
- Succession plans and talent pools can be added as review content; workers can be dragged from the meeting dashboard into plans/pools; plans can be created from the meeting.

### Development machinery (Layer A)

- Talent pools: standing groups of members; development goals can be assigned to a pool "to groom" members for a target job; pool members added as succession plan candidates.
- Journeys: a "Succession Readiness" checklist event can be triggered when a candidate's readiness equals "Ready Now" — assigning manager tasks such as "Create training plans for the candidate" and "Add development goals for the candidate."

### Interfaces (Layer A)

- Succession Plans work area (Succession Overview page; plan detail with Plan Info / Candidates / Owners / Alerts sections).
- Succession Organization Chart: hierarchical chart for a manager and reports with 5 tabs — Directs with Plans, Directs Without Plans, All Reports with Plans, Succession Plans (plans where the person is incumbent, candidates grouped by readiness), Candidate in Plans; red flag on person cards when impact of loss / risk of loss / job criticality is high.
- Person spotlight Succession Planning tab: plans where the person is incumbent, plans where the person is a candidate, talent pools, risk/impact/criticality.
- Talent Review meeting dashboard (box chart, table view, filters, drag-to-plan).
- Plan History page.

### Security (Layer A)

- Function security: View Succession Plan / Create Succession Plan privileges; HR specialists have them by default; managers can create plans for direct/indirect reports via My Team actions.
- Data security: candidate search restricted by data security profiles; custom data roles with securing conditions possible; super users can view/add any candidate.
- Privacy: private vs nonprivate plans; access derived from ownership + incumbent relationship; transfers change access (worked examples).

## Product B — SAP SuccessFactors (Tier 2)

- FAQ: "SAP SuccessFactors supports succession planning by helping organizations identify high-potential employees, map talent to critical roles, and build internal talent pipelines. AI-driven insights surface candidates based on skills, performance, and readiness, so leaders can make more informed succession decisions."
- Career and Talent Development: "Build a robust talent pipeline and evaluate potential successors with AI-assisted insights"; "Strategic talent planning for intelligent skills-based decisions"; skills model at the center.
- Career and Talent Development Assistant: "Streamline succession planning by surfacing risks and delivering actionable insights with clear mitigation steps."
- 1H 2026 release highlights: "Succession Planning and Career Development Agents" (AI agents), skills governance UI.
- Interpretation: same structural pattern (critical roles → talent pipeline → readiness/skills-based candidate evaluation → risk surfacing), delivered as a suite module with AI layering. No operational detail reachable (help portal JS-gated).

## Product C — Workday (Tier 2)

- Talent Optimization product family; Succession Planning is a named feature: "Supercharge succession planning with smart tools for identifying critical positions and talent gaps. Proactively plan for worker movement and develop high-potential individuals for a future-proof leadership pipeline."
- Sibling features in the same module: Career Hub (employee career development), Manager Insights Hub, Talent Marketplace (internal opportunities), Skills Cloud.
- Interpretation: succession = critical positions + talent gaps + high-potential development + worker-movement planning; sits beside (not inside) the employee-facing career/marketplace surfaces. No operational detail reachable (community docs gated).

## Product D — PeopleFluent (Tier 2)

- "Succession planning software... A complete, flexible, functional toolset that gives you what you need to make the right decisions about your organization's future."
- Fill Your Talent Pool: "Search for your next leaders or grow them"; "Keep track of top-performing, high-potential employees and candidates and map their career path options. Not in a spreadsheet, but in a tool that integrates with other data. So you can maintain their development and fill your leadership pipeline."
- Understand Your Bench: "How deep is your bench?... keep tabs on your current talent - their skills, strengths, and potential - so you can determine who needs more development and who's ready to step up."
- Uncover Gaps & Plan Succession Scenarios: strengths and skills gaps today and in the future; "intuitive drag-and-drop interface to analyze your gaps, and calibrate your succession plans according to your talent pool and business needs"; "see where your leadership vulnerabilities are."
- Analytics: "Use predictive analytics to determine who is likely to leave based on past trends"; "Drill down to see when and where replacements will be required"; "Ensure your development plans are effective, and that you have sufficient coverage for each of the key positions."
- Suite context: unified talent profiles, high configurability, "in-depth permissioning"; regulated-industry focus.

## Product E — TalentGuard (Tier 2)

- Talent pool builder: "Proactively manage succession risks and role vacancies with internal talent pools. Evaluate how well candidates match the role profile and alert management to flight risks."
- Targeted internal talent search: "verified skills, competencies, performance, career aspirations, manager recommendations."
- Objective candidate evaluation: "Compare candidates side-by-side based on match percentage, time-to-readiness, previous roles, preferences."
- "A clear view of future needs": "managers to see their teams' bench strengths, tenure risks, and gaps in role succession."
- Ideal candidate finder: define the ideal candidate's skills/experiences, find internal matches.
- FAQ names the 9-box grid as "the primary tool used in succession planning discussions"; describes 4 stages (assessment, development, readiness, transition) and the 5 D's (Define, Discover, Develop, Deploy, Drive).
- Coverage plans for key roles; "goes beyond replacement charts."
- Packaging: Succession Planning ships in the top bundle with Performance Management, Certification Tracking, 360 Feedback.

## Product F — Mitratech Trakstar (Tier 2, light pole)

- Succession Planning use case = 9-Box Grid Reporting ("See your entire workforce or segment by department... from Top Talent to Underperformers"), hidden competency ratings for potential ("discreetly collected"), unbiased data collection from performance reviews/check-ins, compensation recommendations via hidden review sections.
- Interpretation: at the light end of the market, a "succession planning" capability can be little more than performance×potential grid reporting over performance-review data — no persistent per-role slates documented on this page. This is the thin edge of the Type; held as a variant pole, not the definition.

## Cross-product Comparison

| Structure | Oracle | SAP | Workday | PeopleFluent | TalentGuard | Trakstar |
|---|---|---|---|---|---|---|
| Key role/position as planning subject | Plan types Incumbent/Job/Position | "map talent to critical roles" | "identifying critical positions" | "coverage for each of the key positions" | "role vacancies", role profile match | (not per-role on page) |
| Candidate slate per role | Candidates section w/ status/ranking/interim flag | "talent pipeline" | "talent gaps", pipeline | talent pool + pipeline | internal talent pools | — |
| Readiness standing per candidate | readiness lookup (time-based) | "readiness" in AI insights | — | "who's ready to step up" | time-to-readiness, match % | — |
| Performance×potential matrix | box chart in talent review meetings | — | — | — | 9-box grid | 9-box grid (the page's whole content) |
| Development linkage | talent pools w/ dev goals; readiness-triggered checklists | development plans (suite) | "develop high-potential individuals" | "maintain their development" | development plan module | — |
| Risk of loss / retention risk | Risk of Loss + Impact of Loss ratings | "surfacing risks" | "plan for worker movement" | predictive flight-risk analytics | flight-risk alerts, tenure risks | — |
| Bench/coverage analytics | bench strength via readiness distribution | talent pipeline | talent gaps | bench depth, coverage | bench strengths, gaps | — |
| Org-chart surface | Succession Organization Chart | — | — | — | — | — |
| External candidates | yes (separate store) | — | — | "employees and candidates" | — | — |
| Confidentiality machinery | private plans, owner types, super users | — | — | in-depth permissioning | — | hidden rating sections |
| AI candidate suggestions | AI-suggested candidates (replaces Best-Fit) | AI insights + agents | AI-powered | predictive analytics | AI/verified skills | — |

### Canonical abstraction (Layer C inference)

The Type is an organization-side system of record for continuity of key roles. The jointly-held defining structure:

1. **The key role of record** — an identified job/position (or a specific person's role) that the organization plans continuity for. Remove → a generic talent pool or HRIS roster.
2. **The candidate slate** — named internal candidates attached to that role (external candidates a variant). Remove → a role catalog with no successors.
3. **Readiness standing** — a maintained evaluation of how prepared / how soon ready each candidate is against that role. Remove → a contact list; the "succession" semantics disappear.

Everything else is common mature structure (development linkage, ratings/matrix machinery, risk-of-loss, bench analytics, org-chart surface, governance/privacy, alerts) or variant/optional (external candidates, AI suggestions, interim-successor flags, ranking schemes, meeting machinery, compensation linkage).

## L0 / L1 / L2 / L3

### L0 — Defining Invariant

- Key role of record (identified job/position/person's role planned for continuity)
- Candidate slate attached to that role (named internal candidates)
- Readiness standing of each candidate against the role, maintained over time

Jointly-held is load-bearing: role without slate = role catalog; slate without role = talent pool; slate+role without readiness = name list.

### L1 — Common Mature Structure

- Incumbent linkage (named or inferred incumbent; vacancy awareness)
- Role requirements / success profile (competencies/skills model) used for matching and gap analysis
- Development linkage for candidates (development plans/goals, talent pools, learning)
- Performance & potential evaluation feeding the slate (talent review meetings, 9-box-style matrices, calibration)
- Risk of loss / impact of loss / retention-risk signals
- Bench strength / coverage analytics
- Org-chart-anchored navigation of plans
- Plan governance: owners, privacy/confidentiality, change history/audit
- Movement alerts (candidate promoted into/out of the role; incumbent changes)

### L2 — Variant / Optional

- External (non-employee) candidates
- AI-suggested candidates / AI agents
- Interim-successor designation; candidate ranking schemes
- Willingness-to-relocate and other candidate preference data
- Talent review meeting machinery depth (calibration, holding areas, notes/tasks)
- Compensation linkage
- Emphasis poles: emergency/contingency succession vs long-term development pipelines
- Scope: executive-only vs all critical roles vs whole-workforce grid reporting
- Light pole: 9-box reporting without persistent per-role slates (Trakstar page)

### L3 — Vendor-specific (research notes only)

- Oracle: plan types Incumbent/Job/Position; HRM_READINESS_CATEGORY lookup (delivered "Ready now"/"No readiness available"; example values "Ready in 1-2 years", "Ready in 3-4 years"); 500-candidate plan limit; Succession Plan Incumbents scheduled process; owner types Administrator/Candidate Manager/Viewer; super user role; Best-Fit ≥90% default; Holding Area; talent score; Journeys "Succession Readiness" checklist event; person spotlight; plan history baseline 22B.
- SAP: Career and Talent Development Assistant; Succession Planning Agent (1H 2026); Talent Intelligence Hub skills governance.
- Workday: Talent Optimization module naming; Career Hub; Manager Insights Hub; Talent Marketplace; Skills Cloud.
- PeopleFluent: drag-and-drop scenario modeling; OrgPublisher org-charting product; Reflektive performance product.
- TalentGuard: Automate/Engage/Optimize bundles; WorkforceGPT; ideal candidate finder; 4-stage and 5-D frameworks (marketing frameworks).
- Trakstar: hidden competency rating sections; compensation recommendations via hidden sections.

## Vendor-specific Findings

See L3 above. None of these were promoted into the canonical document.

## Boundary Findings

- **vs Talent Review Platform (§09 sibling, unprocessed)**: the closest seam. Oracle ships both in one book ("Talent Review and Succession Management"); talent review meetings produce/calibrate performance-potential ratings over a review population, while succession plans hold the per-role slates and readiness. The meeting is a process/event; the plan is a persistent record. In the sampled market they are deeply interlocked (plans added as meeting content; workers dragged from meeting dashboards into plans). Recommend joint review when talent-review-platform is processed; proposed seam: talent review = the evaluation/calibration event machinery; succession = the role-anchored plan of record that consumes those evaluations.
- **vs Career Development Platform (processed 2026-09-07)**: confirmed from this side — succession plans are organization-owned, confidential, role-anchored records; career development plans are employee-owned growth plans. Oracle keeps them in different work areas with different privacy models (private succession plans vs employee-visible development goals).
- **vs Internal Talent Marketplace (processed 2026-09-07)**: confirmed — curated slates vs open expression of interest; marketplace opportunities are visible and appliable, succession slates are confidential and nomination-based.
- **vs Skills/Competency Management (processed 2026-09-07)**: confirmed — competency/skills models are the requirements substrate ("role profile", "model profile") that succession consumes for matching and gap analysis; succession holds no competency model of its own.
- **vs Performance Management**: performance ratings are an input to evaluation (and to 9-box axes); performance management owns the review cycle, not the slate.
- **vs Workforce Planning**: workforce planning is headcount demand/supply planning over aggregates; succession is named-candidate continuity planning for specific roles. (Workday sells both in different product families.)
- **vs Org Chart Management**: the org chart appears as a navigation surface (Oracle's Succession Organization Chart; PeopleFluent's OrgPublisher sibling product) but the record of succession is the plan, not the chart.
- **vs HRIS/HCM**: succession is a talent module inside suites (Oracle/SAP/Workday) and also exists as standalone specialists (PeopleFluent, TalentGuard) — packaging is a variant, not a boundary.
- **Out-of-domain namesake**: "succession planning software" for business-owner succession (financial advisory practice sale/transition, family business succession, dealership succession) plans the transfer of business OWNERSHIP, not workforce roles. Different subject, different objects (valuation, deal, legal transfer). Not this Type; no directory leaf claims it — noted for taxonomy awareness, no action taken.
- **Light-pole drift**: a tool that only produces 9-box reporting over performance data (Trakstar page) lacks the per-role slate + readiness record; held as the Type's thin edge / capability slice rather than a separate Type.

## Uncertainties

- No Tier-1 operational docs were reachable for SAP, Workday, PeopleFluent, TalentGuard, or Trakstar (help portals JS-gated/login-walled/unreachable). Their evidence is product-page level; claims resting on them are calibrated to positioning-level strength.
- Readiness label sets vary by product and are configurable (Oracle's are lookups); no Type-wide standard labels asserted.
- Slate-size limits, approval/nomination workflows, and calibration mechanics beyond Oracle are unverified; no precise numbers asserted as Type-wide facts.
- The exact market boundary between "Talent Review Platform" and "Succession Planning Platform" as separately purchased products could not be verified (no standalone talent-review-only product docs sampled); flagged for the sibling pass.
- Nomination/approval workflow depth (e.g., manager nominates → HR approves) is documented only implicitly at Oracle (security-gated creation); not asserted as a standard workflow.

## Final Synthesis

A Succession Planning Platform is the organization-side system of record for continuity of key roles. Its defining core is three jointly-held structures: the key role of record (a job, position, or a specific person's role the organization plans continuity for), the candidate slate (named internal candidates attached to that role), and the readiness standing of each candidate against that role (a maintained evaluation of preparedness/time-to-readiness). Around this core, mature products add: incumbent linkage, role-requirement profiles for matching, development machinery for candidates (development plans, talent pools, learning), performance/potential evaluation machinery (talent review meetings, 9-box-style matrices), risk-of-loss signals, bench/coverage analytics, org-chart navigation, governance (owners, privacy, audit), and movement alerts. Variants include external candidates, AI suggestions, interim-successor designations, and scope poles from executive-only to whole-workforce grid reporting. The Type is packaging-agnostic (suite module or standalone specialist). Historical check passes: paper-era key-position succession charts (position, incumbent, successors, readiness notes, development notes) and spreadsheet replacement charts satisfy the core without any modern machinery.
