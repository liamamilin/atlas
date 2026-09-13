# Research Notes — Career Pathing Application

## Research Goal

Understand what a "Career Pathing Application" actually is as an Application Type: what the managed object is (the organization's career structure? the employee's plan? both?), how career paths are modeled in real products, who builds and maintains them, how employees consume them, and where the boundary lies against the already-processed sibling leaf **Career Development Platform** (which flagged this leaf for joint review), plus Skills Management, Internal Talent Marketplace, Succession Planning, Competency Management, and Org Chart Management.

## Initial Boundary

Initial hypothesis (pre-research):

- "Career pathing" is marketed both as a standalone product label (TalentGuard, historically Fuel50) and as a feature name inside career development / talent suites (SAP "Career Paths", Oracle "career paths", Lattice "Career Tracks").
- Candidate core: the organization-side career structure (roles, levels, progression routes, requirements) as a maintained object + employee-facing exploration with gap/readiness signals.
- The flagged question from career-development-platform research: is this leaf an independent Type or a capability slice of Career Development Platform (or Skills Management)? Candidate outcomes: keep-both with an architecture-vs-execution seam, or re-scope as capability.
- Nearest neighbors: Career Development Platform, Skills Management Platform, Internal Talent Marketplace, Succession Planning Platform, Competency Management Platform, Org Chart Management, Performance Management Platform.

## Research Questions

1. What is the central managed object in products sold as "career pathing" — the path library, the employee's plan, or the match?
2. What does a "career path" consist of structurally (nodes, links, requirements, levels, tracks/lattices)?
3. Who authors and maintains the structure, and through what governance workflow?
4. What does the employee-facing surface show (exploration, requirements, gap/readiness), and is it definitional?
5. How does pathing connect to development planning, marketplaces, succession, performance — as definition or as downstream consumer?
6. Is there a standalone product whose primary object is the path library itself, with no development-plan object? (tests the architecture-vs-execution seam)
7. Do older / lighter / regional forms (SAP-CDP-era career paths, engineering career ladders, competency ladders) fit the same core?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, and different customer tier:

| Product | Pole | Customer tier | Evidence quality |
|---|---|---|---|
| TalentGuard | standalone "Career Pathing Software" specialist (governance/evidence-chain philosophy) | enterprise | Tier-2 official product pages (root, Platform, dedicated Career Pathing page) — unusually explicit product definition |
| Fuel50 | career-pathing heritage specialist, now skills-architecture + talent-marketplace platform | mid-market → enterprise | Tier-2 official product pages (root, Skills Architecture, Mobility) |
| Progression | lightweight job-architecture / career-framework pole (positions + skills + levels; public framework library) | SMB / team → mid-market | Tier-2 official site (root, Features, Frameworks feature page) |
| Lattice (Grow) | mid-market people-platform module (Career Tracks + IDPs + reviews in one) | SMB → mid-market | Tier-2 official product page with FAQ |
| SAP SuccessFactors Career and Talent Development | enterprise HCM suite pole | enterprise | Tier-2 official product page |
| Oracle Grow (Oracle ME) | enterprise suite pole, employee-experience packaging | enterprise | Tier-2 official product page |

Market context (not sampled in depth): Workday (cookie-walled in prior runs), Cornerstone (help-center index reached; product-level docs not fetched), Gloat / Beamery (marketplace pole), Gaps/other job-architecture tools.

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

- TalentGuard — https://www.talentguard.com/ (root), https://www.talentguard.com/platform (nine-module platform map), https://www.talentguard.com/platform/career-pathing (dedicated Career Pathing product page)
- Fuel50 — https://www.fuel50.com/ (root), https://fuel50.com/products/skills-architecture, https://fuel50.com/products/mobility
- Progression — https://progressionapp.com/ (root), https://progressionapp.com/features, https://progressionapp.com/features/frameworks/
- Lattice — https://lattice.com/products/grow (Grow product page with FAQ; /products/career-growth was 404)
- SAP — https://www.sap.com/products/hcm/career-talent-development.html
- Oracle — https://www.oracle.com/human-capital-management/employee-experience/oracle-me/grow/
- Cornerstone — https://help.csod.com/ and https://help.csod.com/helpcenter/ (help-center index only; product-level docs not fetched)

Unreachable / abandoned (per network-limitation rule):

- SAP Help Portal (help.sap.com) — SPA shell for product slugs (confirmed in the paired career-development-platform run); not retried beyond one navigation.
- Oracle docs.oracle.com book pages — JS-gated (confirmed in paired run); not retried.
- Workday product pages — cookie-wall (confirmed in paired run); market context only.
- lattice.com/products/career-growth — 404; /products/grow used instead.
- help.csod.com root — redirect to helpcenter index; deeper product docs not fetched (sample already sufficient).

Consequence: all product evidence is Tier-2 (official product/marketing pages). These reliably establish positioning, object structure, capability vocabulary, and vendor-articulated boundaries, but not precise operational mechanics (path-viability thresholds, readiness-score formulas, approval state names, numeric limits). No precise numbers, defaults, or state names are asserted in the final document beyond what sources state.

## Product Observations

### TalentGuard (root + Platform + Career Pathing page)

Evidence layer: A (directly observed on official pages).

- Sells "Career Pathing Software" as a named module: "gives organizations the structured framework to define, validate, and operationalize internal mobility — grounded in skills trust, not assumption."
- Vendor's own definition: "Career Pathing is the enterprise practice of mapping explicit, skills-based routes between roles — enabling employees to understand what advancement requires, and enabling organizations to measure workforce readiness with precision." "In the TalentGuard platform, Career Pathing is not advisory. It is operationalized: role requirements are drawn from a governed skills ontology, employee readiness is assessed against those requirements, and every transition recommendation is traceable to a defensible standard."
- Platform = nine governed modules mapped to six steps; Career Pathing is step 04 "Plan the move" ("Identify realistic next roles and career options"), distinct from step 05 Development Planning ("Close the gap" — "Converts each verified gap into a targeted development plan") and step 06 Succession. Career Pathing sits between assessment and development: "Talent Assessment validates whether an employee's current skills are real... Career Pathing takes that verified readiness data and makes it actionable, showing each employee precisely what the next role requires, exactly where their gaps are, and what must change to close them."
- ESTRI framework (vendor-coined "Enterprise Skills Trust & Readiness Intelligence") — four disciplines behind career pathing: 01 Standards (Governed Skills Ontology: "Role profiles are built on normalized skill definitions — not free-text job descriptions"; taxonomy "governed, versioned, and extensible"), 02 Governance ("Career paths are not crowd-sourced. They are defined by HR architects with organizational authority, maintained by role owners, and governed through approval workflows. Every path reflects deliberate organizational design — not aggregated employee preference." Ownership, approval, version control at the role level), 03 Readiness (Assessed Skill Alignment: readiness scores from verified assessments, manager evaluations, developmental activity — "not self-reported claims alone"), 04 Auditability ("Every career path recommendation, readiness assessment, and progression decision is logged against the governing skill standard at the time the decision was made").
- Capability set (six, named): Role-to-Role Mapping ("Define lateral, diagonal, and vertical transitions between any roles... built from governed skill gap analysis — not organizational chart proximity alone"); Readiness Scoring & Gaps ("quantified readiness percentages and ranked skill gaps"); Skill Ontology Management ("normalized, versioned skills library... single source of truth across Career Pathing, Succession, and Learning"); Career Lattice Visualization ("Employees see all viable paths — upward, lateral, and across functions — rendered as an interactive lattice tied to real skill requirements. The visualization is governed data, not aspirational diagram"); Development Plan Integration ("Gap-closing activities... mapped to specific skill deficits on each career path. Plans are generated from the gap analysis, not from generic L&D catalogs"); Governance Logging ("time-stamped and linked to the governing skill standard").
- How-it-works (five steps): 1 Architect (HR architects configure the role library; each role associated with a governed skill profile — required skills, proficiency levels, proficiency weightings; role owners review/approve via structured workflow; outputs: role library, governed skill profiles, proficiency thresholds), 2 Map (define the career path network — which roles are adjacent, transition requirements, "what skill gap magnitude indicates a viable near-term path versus a developmental aspiration"; outputs: lateral & vertical paths, transition requirements, path viability thresholds), 3 Assess (multi-source evaluation: self-assessment, manager validation, credentialing/performance data; readiness scores computed against target roles in real time; gap reports at individual/team/org level; outputs: readiness scores, skill gap reports, team-level heat maps), 4 Activate (gap-specific development plans generated and assigned; readiness scores update as development milestones are verified; outputs: development plans, progress tracking, readiness trend reporting), 5 Audit (audit logs with timestamps, skill versions, decision rationale; workforce reporting: internal mobility rates, readiness distributions, path utilization; outputs: audit-ready decision logs, internal mobility analytics, CHRO-level reporting).
- Stakeholders: Chief People Officer, VP Talent Management, HRBP, Individual Contributor ("See what advancement actually requires — and track your progress").
- Ad-hoc vs governed contrast table: manager-dependent advice → platform-governed standardized role maps; self-reported skills → verified against governed ontology; unclear promotion criteria → explicit measurable readiness thresholds; lateral moves invisible → "Full lattice visibility — vertical and horizontal"; no record → audit trail; reactive to attrition → proactive readiness dashboards by role and function.
- Positioning: "TalentGuard runs as the role and skills system of record alongside the systems you already own" (integrates Workday, SAP SuccessFactors, UKG, ADP, LMS, ATS).
- Case-study claims (vendor-stated, not verified): Vonachen "80% surge in internal promotions... $1.2M saved on job architecture"; NHMB "90% reduction in job and skills management effort".

### Fuel50 (root + Skills Architecture + Mobility)

Evidence layer: A (directly observed on official pages).

- Current packaging: Talent Intelligence Platform = Skills Intelligence (Skills Ontology, Skills Architecture, Skills Inventory, Insights) + Talent Marketplace (Mobility, Development, Gigs, Succession).
- Skills Architecture page: "a living, governed skills taxonomy"; Talent Blueprint portal ("Lets administrators fine-tune the framework at any time... adapting to changing market conditions... without waiting on consultants or IT tickets"); Role Editor ("Gather Real-Time Feedback on Your Skills-Based Role Profiles from the People Who Know the Work Best" — SME input + AI-generated skill suggestions; "every edit tracked, attributed, and audit-ready"); Skills Ontology ("5,000+ skills, curated by Fuel50's People Scientists... detailed skill definitions, proficiency levels, and development actions that plug straight into career pathing, internal mobility, and skills-based workforce planning"); Learning Curve AI™ ("Automatically Apply Proficiency Levels to Every Skill... a smooth, realistic learning curve from entry-level to executive roles").
- FAQ (vendor-articulated architecture): "Skills Architecture is the backbone. The skills and proficiency data you define here powers everything downstream: Skills Inventory, career pathing, internal mobility, gigs, development, succession, and workforce planning. Accurate architecture in. Smarter matching, development, and decisions out."
- Mobility page: "JOURNEYS — Give Your People Clear, Skills-Based Career Paths"; "Employees see the skills they need to reach target roles; leaders see the internal pipeline behind every critical job — turning career pathing into a retention and workforce planning engine"; "The Career Path feature is a great addition! It's helped employees explore different fields within Lennox where their skills are transferable" (customer quote); "Career Journey profile" (customer quote); matching "runs on Fuel50's expert-driven skills ontology and skills architecture".
- Root page: Talent Marketplace "connects employees to roles, projects, career paths, and growth opportunities based on skills, aspirations, values, and goals"; analyst quote: "This is career pathing, development and succession for companies that are serious about this stuff"; customer quote: "we've built our skills architecture from scratch so there's a clear journey and pathway at every stage and every job, and we can even create careers that simply didn't exist before."
- Career Advisor Agent (AI): "explore career journeys, validate their skills, see gaps, receive hyper-personalized recommendations."

### Progression (root + Features + Frameworks)

Evidence layer: A (directly observed on official pages).

- Positioning: "Define and roll out job architecture to your whole organisation, in weeks. Provide your employees with clear career pathways that promote growth and retention."
- Framework object (vendor-defined triad): "Frameworks are made up of three things — positions, skills and levels." Positions: "outline the roles in your team, so everyone has a clear idea of the career pathways available." Skills: "a framework powered by skills forms the criteria needed to track and evidence development." Levels: "Levels explain what's expected of your team in their current role, and what they need to do and demonstrate to take their next career step."
- Build tooling: "Build beautiful frameworks in minutes, adding skills, competencies and behaviours"; AI Build Assistant ("trained on all of our library content, can help you define brilliant skills"); Library of starter skills and templates; "Compare any two roles in your organisation"; "Unlimited teams, parallel tracks and levels of seniority"; "Export your roles — downloadable positions."
- Sharing: "share your Progression frameworks with the world. Invite your team, and potential new hires, to explore, compare and plan freely. Different permission levels ensure only the right people can see and edit your work." Public Library: "share your own framework publicly in our library for others to build from, complete with custom colours and hiring links." Template library includes public frameworks (e.g., Medium engineering/product templates).
- People-side light structure: skill insight ("Find people within positions, or with specific skill levels for mentoring or re-organisation"; "Find most used and unused skills"), Focus Skills ("Allow team members to identify the skills to power growth"), Wins, Feedback, Work Feed, Check-ins ("Measure and grow"), Coach ("A career coach, for everyone, anytime"), Actions ("Stay on track").
- Anti-pattern named by vendor: "Say goodbye to the spreadsheet!" — the product replaces spreadsheet-published career ladders.
- Ownership note: "Talk to Us" and help now route to careerminds.com / support.careerminds.com (career-transition company acquired/integrated the product).
- Scale claims (vendor-stated): "155k skills created", "45,000 hours saved writing content".

### Lattice Grow (product page + FAQ)

Evidence layer: A (directly observed on official page).

- Product framing: "Employee growth... employee development tools that define growth paths and drive structured development." Named features: Competency Matrices ("Make role expectations and skill progression crystal clear with consistent competency frameworks"), Individual Development Plans ("Empower employees to own their growth with personalized IDPs and AI-powered growth areas"), Career Tracks ("Create transparent career paths using Lattice-built templates designed to scale"), 1:1 Integration, Manager Efficiency.
- FAQ (vendor-articulated pathing definition): "How does Lattice support career pathing? Lattice Grow includes Career Tracks, which let companies define clear growth paths by role and level. Employees can see what skills and competencies are expected at each stage, and managers can use that framework to guide development conversations and individual development plans."
- "What are Career Tracks in Lattice Grow? Career Tracks... illuminate pathways toward career advancement by outlining progression routes within your organization. They provide transparency, helping employees understand potential career paths and the competencies required for each step."
- Templates: "track templates with pre-loaded competencies, levels, and expectations that can serve as a starting point... customized to align with your company's specific competency framework."
- Changelog: "Competency & Competency Library Export — Export detailed competency data, including career track alignment and source information"; Grow UI updates for end-user and manager views.
- IDP integration: "IDPs... let managers and employees co-create structured development goals tied to performance, skills, and career tracks. Plans are built directly in Lattice and connect to 1:1s, feedback, and performance reviews." AI: "Lattice AI Agent powers Growth Areas in Grow, surfacing personalized development opportunities based on performance, goals, and feedback."

### SAP SuccessFactors Career and Talent Development (product page)

Evidence layer: A (directly observed on official page).

- Positioning: "guides employees and managers to shape careers through personalized, AI-driven interactions and growth opportunities"; "skills-based development and talent planning"; hero screenshot named "growport" (Growth Portfolio).
- Key features: "Empower employees to explore recommended roles and career paths and evaluate their readiness with AI-assisted career and skills insights"; "Set and update aspirational development goals with AI"; AI talent marketplace recommendations; "Build a robust talent pipeline and evaluate potential successors"; "Connect mentors and mentees based on skill matching."
- "A single, integrated skills model to put skills at the center of your talent strategy"; 1H 2026 release notes mention "a new skills governance UI in the talent intelligence hub" and "Succession Planning and Career Development Agents."

### Oracle Grow (product page)

Evidence layer: A (directly observed on official page).

- Positioning: "unifying learning, skill development, and career mobility"; part of Oracle ME / Fusion Cloud HCM.
- Career-management features: "Personalized career options — a visual of their career and development progress and reminders to stay on track"; "Personal AI career coach — visualize career growth possibilities by discovering different career roles and paths"; "AI-recommended career journeys"; "Skills-driven career mobility — Drive internal mobility by providing business-authored role guides in a personalized opportunity marketplace."
- Product tour: "Provide transparency into all the available opportunities — Empower individuals to visualize the different career paths available to them in the organization and review recommended roles... Help workers better qualify for specific careers of interest by enabling them to acquire the skills they need to level up and guiding them through career-based development journeys"; "Deliver clear role expectations and next steps with a personalized career scorecard."
- Architecture side: "Improve results with business-led, HR-architected upskilling"; "Business-authored role guides — Help leaders quickly create detailed role guides for critical positions with AI-suggested skills, tasks, and resources"; "Generative AI–assisted authoring"; "Act as a strategic advisor... provide governance with respect to skills taxonomies and program initiatives."

### Cornerstone (help-center index only)

Evidence layer: A for packaging vocabulary; no product-level docs fetched.

- Help Center index: Elevate = "Performance, Succession, Recruiting, Compensation, and Talent Marketplace"; Transform = "HR, Skills Transform, Skill Passport and Skyhive Enterprise 2.0". Career-path-level detail not observed in this run; treated as market context only.

## Cross-product Comparison

| Structure | TalentGuard | Fuel50 | Progression | Lattice Grow | SAP CTD | Oracle Grow |
|---|---|---|---|---|---|---|
| Organization-defined role/path library as the managed object | ✓ role library + governed skill profiles + path network (Architect/Map steps) | ✓ Skills Architecture ("the backbone") feeding career pathing | ✓ Frameworks = positions + skills + levels | ✓ Career Tracks (role × level paths, templates) | ✓ roles & career paths in the skills model | ✓ career roles/paths + business-authored role guides |
| Progression links between nodes (vertical/lateral) | ✓ role-to-role mapping: lateral, diagonal, vertical; transition requirements | ✓ career journeys/paths between roles | ✓ positions + levels; parallel tracks; compare positions | ✓ progression routes by role and level | ✓ career paths | ✓ career paths/roles |
| Requirements attached to nodes (skills/competencies + proficiency) | ✓ governed skill profiles, proficiency levels & weightings | ✓ skills + proficiency per role (Learning Curve AI) | ✓ skills per position; levels define expectations | ✓ competencies per level/track | ✓ integrated skills model | ✓ role guides with AI-suggested skills/tasks |
| Employee-facing personalized exploration | ✓ career lattice visualization; "what advancement actually requires" | ✓ Career Path feature / Journeys | ✓ explore, compare, plan; share with team & new hires | ✓ employees see expected competencies per stage | ✓ explore roles & career paths | ✓ visualize career paths; AI career coach |
| Gap/readiness signal vs target | ✓ readiness percentages, ranked gaps, heat maps | ✓ readiness signals | ✓ skills vs level expectations; focus skills | ✓ competency matrices (expectation clarity) | ✓ AI readiness insights | ✓ career scorecard, role expectations |
| Development linkage from gaps | ✓ separate Development Planning module fed by pathing | ✓ Development product in suite | ✓ light: focus skills, actions, check-ins | ✓ IDPs tied to tracks | ✓ aspirational development goals, AI plans | ✓ development journeys, playlists |
| Org-side authoring/governance workflow | ✓ HR architects, role owners, approvals, versioning, audit trail | ✓ Talent Blueprint admin portal, Role Editor SME workflow, audit-ready edits | ✓ manager-built; permission levels for view/edit | ✓ admin-customized track templates | ✓ skills governance UI | ✓ business-authored role guides, HR-architected, taxonomy governance |
| Skills/competency library management | ✓ normalized versioned ontology, single source of truth | ✓ Skills Ontology product | ✓ skill library + templates | ✓ competency library (+ export) | ✓ unified skills model | ✓ skills catalog / taxonomy governance |
| AI assistance | ✓ WorkforceGPT standards; AI suggestions | ✓ Learning Curve AI, Career Advisor Agent | ✓ AI Build Assistant, Coach | ✓ AI growth areas | ✓ AI insights, CTD assistant | ✓ AI career coach, gen-AI authoring |
| Analytics | ✓ mobility rates, readiness distributions, path utilization | ✓ Insights dashboards | ✓ skill insight (most used/unused skills) | ✓ competency export for analysis | (suite) | ✓ upskilling alignment dashboard |
| Opportunity marketplace (open roles) | ✗ not observed in pathing module | ✓ separate Mobility product | ✗ | ✗ | ✓ bundled recommendations | ✓ bundled opportunity marketplace |
| Succession linkage | ✓ separate module (pathing feeds it) | ✓ separate Succession product | ✗ | ✗ | ✓ bundled | ✓ (Talent Management sibling) |
| Performance integration | ✓ performance module feeds readiness | (suite) | ✗ (check-ins/wins instead) | ✓ reviews/1:1s integration | ✓ skills inference from performance | (suite) |

### Reading of the comparison

- The **organization-defined career structure** (roles/positions + levels + progression links + per-node requirements) is present in all six products and is the operational center of what every vendor means by "career pathing."
- **Employee-facing personalized exploration** ("you are here → what's next → what it takes") is present in all six and is the second half of every vendor definition (TalentGuard: "enabling employees to understand what advancement requires"; Lattice: "Employees can see what skills and competencies are expected at each stage"; Oracle: "visualize the different career paths available to them").
- **Quantified readiness scoring** is common at the enterprise pole (TalentGuard, Fuel50, SAP) but not advertised as a scored object at the lightweight/mid-market pole (Progression, Lattice) — Common, not defining.
- **Development linkage** is present in five of six, but TalentGuard ships it as a *separate module* that pathing feeds, and Progression reduces it to light tracking (focus skills/actions/check-ins) — so development planning is a downstream consumer, not part of the pathing definition.
- **Governance/authoring workflow** is present in all six but scales enormously — from Progression's "managers build frameworks with permission levels" to TalentGuard's architect/owner/approval/version/audit chain — Common, with the enterprise-governance depth being variant.
- **Marketplace, succession, performance** are bundled-adjacent or separate products — Optional.
- Packaging spans: standalone specialist module (TalentGuard), skills-platform substrate (Fuel50), lightweight standalone (Progression), people-platform module (Lattice), HCM-suite module (SAP, Oracle). The structure+exploration core survives all packagings.

## Canonical Model

### L0 — Defining Invariant (minimal)

A Career Pathing Application is recognizable when all of the following hold:

1. **Organization-defined career structure as the managed, maintained object** — a governed library of roles/positions (commonly grouped into families or tracks) with levels and defined progression relationships between them (vertical, lateral, cross-functional). The structure is authored and maintained at organization level; employees consume it, they do not create it.
2. **Requirements attached to the structure** — each role/level node carries defined requirements (skills or competencies with expected proficiency). The structure is a requirements map, not a title hierarchy.
3. **Personalized employee-facing exploration** — an identified employee, positioned at their current role/level, can explore the structure and see what specific target roles/levels require relative to their own profile ("you are here → what's next → what it takes").

Remove #1 → a personal goal tool or skills self-assessment with no organizational structure. Remove #2 → an org chart or job-title catalog. Remove #3 → a job-architecture authoring back office (a different, admin-only tool) or a static framework document/publisher.

### L1 — Common Mature Structure

- Gap/readiness signals against target nodes (quantified readiness scores, ranked skill gaps, heat maps — depth varies by pole)
- Development linkage (gap → development actions/learning; plans generated from gap analysis in the deeper pole)
- Skills/competency library management (normalized definitions, proficiency scales, reuse across roles)
- Authoring/governance workflows (role owners, approvals, version control; audit trails at the enterprise pole)
- Templates and starter content (framework templates, skill libraries)
- AI assistance (framework drafting, skill suggestions, path recommendations, conversational career coaches) — era-common
- Manager/HRBP surfaces (career conversations grounded in the structure and the person's gaps)
- Analytics (path utilization, internal mobility rates, readiness distributions, skill coverage)

### L2 — Variant / Optional Structure

- Opportunity marketplace integration (open internal roles matched to people) — bundled in suite poles and Fuel50; absent in TalentGuard's pathing module, Progression, Lattice (as observed)
- Succession planning linkage (critical roles, successor pools fed by readiness)
- Performance review integration (review outcomes feeding profiles/gaps)
- Path topology emphasis: ladder (vertical within a track) vs lattice (lateral/diagonal across functions) — products differ in how loudly they advertise cross-functional moves
- Anchor implementation: skills-ontology-led (skills with proficiency per role) vs competency-framework-led (competencies with levels) — both realizations of the same requirement concept
- Packaging: standalone specialist vs skills-platform substrate vs lightweight team tool vs people-platform module vs HCM-suite module
- Customer scale and governance depth: enterprise audit/evidence chains vs team-level permission-light sharing
- Public framework sharing (publishing frameworks outside the organization, with hiring links)
- Job-architecture depth (job families, role profiles as comp-relevant artifacts)

### L3 — Vendor-specific (research notes only)

- TalentGuard: ESTRI framework and "Enterprise Skills Trust & Readiness Intelligence" coinage; WorkforceGPT; Intelligent Role Studio; "path viability thresholds"; proficiency weightings; evidence-chain positioning ("Every decision in step 06 traces back to the standard built in step 01"); Vonachen $1.2M job-architecture savings and NHMB 90% effort-reduction claims; SOC 2.
- Fuel50: Talent Blueprint portal; Role Editor; Learning Curve AI™; Skills Ontology "5,000+ skills" curated by People Scientists; Career Journey profile; "Career Path feature" (Lennox customer quote); Tim Sackett analyst quote; Skills Data Accelerator; MCP Server; SOC2 ×5 / NY Anti-Bias / ISO 42001 claims.
- Progression: positions+skills+levels triad as the vendor's own framework definition; AI Build Assistant trained on library content; Public Library with custom colors and hiring links; Medium engineering/product public templates; wins/work feed/focus skills/check-ins/coach feature set; Careerminds ownership and support routing; "155k skills created" / "45,000 hours saved" claims; progression.fyi.
- Lattice: Grow product name; Career Tracks templates with pre-loaded competencies; competency library export with career-track alignment; AI Agent-powered Growth Areas; IDP ↔ 1:1 ↔ review integration; G2 badge claims.
- SAP: "Growth Portfolio" (growport) packaging; Career and Talent Development Assistant; Talent Intelligence Hub + skills governance UI; Joule; skills inferencing from performance data; 1H 2026 Succession Planning and Career Development Agents.
- Oracle: Oracle ME packaging; Dynamic Skills; business-authored role guides with generative-AI authoring; career scorecard; upskilling alignment dashboard; skills development ROI.

## Rejected Findings (considered for L0, rejected)

- **Quantified readiness scoring** — rejected: only the enterprise pole advertises scores (TalentGuard, Fuel50, SAP); Progression and Lattice define expectations without scored readiness. The invariant is *requirements visibility against the person*, not a score.
- **Development-plan integration** — rejected: TalentGuard ships Development Planning as a separate module that Career Pathing feeds; Progression has no development-plan object at all. Pathing's job ends at "what it takes"; closing the gap is the consumer side.
- **Governance/audit machinery (approvals, versioning, evidence chains)** — rejected: enterprise-era/scale addition; Progression runs the same core with permission levels only.
- **Visual canvas rendering of paths** — rejected: implementation choice; the competency-led pole realizes the structure as levels/frameworks rather than drawn paths.
- **A specific skills-ontology implementation** — rejected: the requirement object is invariant; whether requirements are expressed as ontology skills or competency-framework levels is variant.
- **Marketplace/matching** — rejected: bundled-adjacent; Fuel50 itself separates Mobility (open roles) from the pathing substrate.
- **AI career coaches** — rejected: era-common (L1), absent in older forms that still fit the Type.

## Boundary Findings

- **vs Career Development Platform (the flagged joint review)**: the seam is **architecture-and-exploration vs plan-execution**. Career Pathing's managed object is the *organization's career structure* plus its employee-facing *exploration*; Career Development Platform's managed object is the *employee's development plan* (goals + actions tracked over time). Vendor-documented separation: TalentGuard's own platform map puts Career Pathing (step 04, "Plan the move") and Development Planning (step 05, "Close the gap") in different modules with different jobs; Fuel50's FAQ separates Development from the architecture that powers it; Lattice's FAQ describes Career Tracks (pathing) and IDPs (planning) as distinct features. Progression demonstrates a standalone product at the architecture pole with no development-plan object. Conversely, career-development platforms exist whose plan is the star and whose path library is thinner (competency-framework-anchored). **Conclusion: keep both Types with the architecture-vs-execution seam; the boundary is real but soft — most market products bundle both sides on one substrate.**
- **vs Skills Management Platform**: the skills inventory/ontology as primary object vs the career structure as primary object. In career pathing the skills library is instrumental — it supplies node requirements. Fuel50 itself splits these into separate product families (Skills Intelligence vs Talent Marketplace).
- **vs Internal Talent Marketplace**: the marketplace's managed object is the *open opportunity* (roles, gigs, projects) with matching; career pathing's object is the *structure + exploration*, which typically precedes and feeds the marketplace. Fuel50 separates Mobility (open roles) from Journeys (paths).
- **vs Succession Planning Platform**: succession is organization-side and role-critical (critical roles, successor pools, readiness *for the role*); career pathing covers the *whole* role structure and *every* employee's exploration. TalentGuard explicitly chains them (pathing feeds succession).
- **vs Competency Management Platform**: competency framework definition and assessment are the primary object there; here the framework is consumed as node requirements inside the progression structure.
- **vs Org Chart Management**: org chart models the reporting structure of *people*; career pathing models the progression structure of *roles* with requirements. Different object, different consumer.
- **vs Job-architecture authoring back offices** (not a directory leaf): a tool with only the org-side structure and no employee-facing exploration is a job-architecture tool, not career pathing — the employee surface is what makes it "pathing."

### "去掉什么就变成另一个 Type" 判据

- 去掉 employee-facing exploration（只留组织侧架构工具）→ job-architecture authoring back office
- 去掉 per-node requirements → org chart / job-title catalog
- 去掉 organization-defined structure（员工自定目标与行动）→ Career Development Platform / personal goal tool
- 把 managed object 换成 employee's development plan → Career Development Platform
- 把 managed object 换成 open opportunities → Internal Talent Marketplace
- 把视角换成 critical roles + successor pools → Succession Planning
- 把 skills inventory 变成中心对象 → Skills Management Platform

## Historical / Market-Sample Check (§24)

- Older form: the SAP-CDP-era "Career Paths" object (2000s–2010s enterprise suites) — career path trees linking roles and competencies with an employee-side exploration surface, no AI, no marketplace, no skills graph. Fits L0 fully.
- Pre-tool regional/practice form: engineering "career ladders" published as spreadsheets/documents — the exact anti-pattern Progression names ("Say goodbye to the spreadsheet!"). The ladder-as-document lacks managed exploration, which is why the software Type exists; the *structure* concept (positions + levels + expectations) is identical.
- Lightweight pole: Progression (team-level frameworks, public library, permission-light sharing) fits L0 with none of the enterprise governance machinery — proving L0 does not require audit chains, readiness scores, or marketplaces.
- Competency-led regional suites implement the structure as framework levels rather than drawn paths — fits L0 via the requirements-attached-to-nodes abstraction.
- Products that would NOT fit: pure org-chart tools (no requirements/progression semantics), job-description repositories (no employee exploration), pure mentoring products, pure opportunity marketplaces (no maintained structure as the object).
- Conclusion: L0 as abstracted (structure + requirements + exploration) survives the historical check; governance depth, readiness scoring, AI, marketplaces, and public sharing are era/scale additions, correctly kept out of L0.

## Uncertainties

1. No Tier-1 operational documentation was obtained for any sampled product (all evidence is Tier-2 official product pages; Cornerstone help-center index reached but product docs not fetched; SAP help portal SPA). Precise mechanics — path-viability thresholds, readiness-score formulas, approval state names, versioning granularity — are therefore NOT asserted anywhere.
2. The market itself is ambivalent about whether "career pathing" is an independent category or a capability label: TalentGuard sells it as a module, Fuel50 embeds it under Mobility/Development, Lattice embeds Career Tracks in Grow, SAP/Oracle fold it into talent development, Progression sells the whole product as job architecture/pathways. This is recorded as a boundary issue for joint review with career-development-platform.
3. Workday Career Hub / Talent could not be observed (cookie wall) — market context only; no claims.
4. Progression's integration under Careerminds (career-transition company) may shift product direction; observations reflect the site as fetched.
5. Terminology varies by vendor (career path / track / journey / lattice / framework); the canonical abstraction treats them as one structure object with topology and rendering as variants.
6. Fuel50's "career pathing" is described as downstream of Skills Architecture; the exact boundary between Fuel50's Skills Architecture product and its career-path surfaces is vendor-internal packaging, not a Type boundary.

## Final Synthesis

A Career Pathing Application is the organization's career-structure system: it maintains the governed library of roles, levels, and progression routes — each node carrying defined skill/competency requirements — and exposes that structure to individual employees as personalized exploration ("you are here → what's next → what it takes"), commonly with gap/readiness signals and downstream development linkage. Its defining core is small and survives every packaging observed: standalone governance-heavy specialist (TalentGuard), skills-platform substrate (Fuel50), lightweight team framework tool (Progression), people-platform module (Lattice), and enterprise HCM-suite modules (SAP, Oracle). The joint-review question with Career Development Platform resolves as **keep-both with an architecture-vs-execution seam**: pathing owns the structure and the exploration; the development platform owns the employee's plan; vendors themselves separate the two (TalentGuard's step 04 vs step 05; Lattice's Career Tracks vs IDPs), and a standalone architecture-pole product exists (Progression) — but the market overwhelmingly bundles both on one substrate, so the boundary should be reviewed jointly rather than treated as sharp.
