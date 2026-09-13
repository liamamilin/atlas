# Research Notes — Internal Talent Marketplace

## Research Goal

Understand what an Internal Talent Marketplace (ITM) actually is as an application Type: what objects exist inside it, who uses it, how internal opportunities and employees are brought together, how interest is resolved into internal movement, and where the boundary lies against neighboring HR Types (Career Development Platform, ATS/Recruiting, Skills Management, Job Board, Succession Planning, Resource Management).

## Initial Boundary

Working hypothesis at start:

- Core purpose: match the organization's own employees to internal opportunities (open roles, short-term projects/gigs, mentorships) and manage the resulting internal mobility.
- Primary users: employees (demand side), managers/talent teams who post opportunities (supply side), HR/talent leadership who govern.
- Most likely confusions:
  - Career Development Platform (career paths/plans vs live opportunity matching)
  - ATS / Recruiting Management Platform (external hiring vs internal matching)
  - Skills Management Platform (skills data feeds matching but is opportunity-less)
  - Job Board (public vs internal audience)
  - Succession Planning Platform (curated slates vs open expression of interest)
  - Resource Management / PSA (project staffing execution vs talent-mobility brokerage)
- Historical-check concern: the "marketplace" framing (AI matching, skills graphs, gig catalogs) is the current dominant implementation. The definition must be abstract enough to cover pre-AI internal job posting with manual matching, and regional/older internal vacancy boards.

## Research Questions

1. What object classes exist (opportunities: roles, projects/gigs, mentorships, learning; employee career profiles)?
2. What does the supply side do — who creates opportunities, from what data, with what attributes?
3. What does the demand side do — how do employees discover, get recommended, express interest?
4. How does matching work and in which directions does it run?
5. What governed workflow resolves interest into an outcome (review, approval/release, selection, placement)?
6. What rules matter (eligibility, mobility policies, manager consent, profile completeness)?
7. What roles exist and what interfaces does each face?
8. How does the product sit in the HR stack (HRIS/ATS/LMS integration)?
9. Where is the Type boundary against neighboring Types?

## Representative Products

Selected for market representativeness + different product philosophies + different delivery poles:

| Product | Pole | Why sampled |
|---|---|---|
| Gloat | Category-defining standalone AI talent marketplace (now "agentic HR" platform) | pioneer; enterprise; defined the category vocabulary |
| Fuel50 | Career-science-led standalone platform (skills ontology + marketplace) | matching grounded in expert-curated ontology rather than scraped data |
| Workday (HiredScore AI for Talent Mobility) | HCM-suite module | matching embedded in the system of record; manager-activation posture |
| SAP SuccessFactors (Career and Talent Development / Opportunity Marketplace) | HCM-suite module, second major suite | suite-side confirmation; skills-model-centered framing |
| Eightfold AI | Talent-intelligence platform with separate project/resource staffing products | two-sided marketplace evidence; enterprise talent sharing; resource-management seam |

All evidence below was gathered from official vendor surfaces on 2026-09-07.

## Sources

Fetched successfully (Tier 2 official product surfaces; Tier 1 operational docs were not reachable — see Uncertainties):

- Gloat — Talent marketplace explained: https://gloat.com/platform/talent-marketplace/
- Gloat — Platform overview: https://gloat.com/platform/
- Gloat — Intelligent Tools: https://gloat.com/ai-technology/intelligent-tools/
- Fuel50 — Talent Marketplace: https://fuel50.com/products/talent-marketplace
- Fuel50 — root site / product navigation: https://fuel50.com/
- Workday — AI for Talent Mobility (HiredScore): https://www.workday.com/en-us/products/talent-management/ai-talent-mobility.html
- Workday — Talent Management: https://www.workday.com/en-us/products/talent-management.html
- SAP — Talent Management: https://www.sap.com/products/hcm/talent-management.html
- SAP — Career and Talent Development: https://www.sap.com/products/hcm/career-talent-development.html
- Eightfold — Talent Intelligence Platform: https://eightfold.ai/products/talent-intelligence-platform/
- Eightfold — Project Marketplace: https://eightfold.ai/capabilities/project-marketplace/

Attempted and abandoned (1–2 attempts each, per network rules):

- SAP Help Portal (help.sap.com/docs/...) — returned an empty JavaScript shell twice; operational docs unreachable.
- Eightfold product documentation (docs.eightfold.ai) — redirects to SSO login.
- Workday product deep-link (talent-marketplace.html) — 404; current product surface is "AI for Talent Mobility".
- Fuel50 opportunity-marketplace.html — 404; current surface is products/talent-marketplace.
- Eightfold use-cases/internal-mobility — 404; current surfaces are capabilities + learn pages.

Consequence: evidence is strongest at the positioning/capability level (official product pages) and weakest at operational click-path level (help-center workflows). Assertion strength in both files is calibrated accordingly: no precise eligibility rules, approval chains, time windows, or numeric limits are claimed.

## Product Observations

### Gloat

Evidence layer: A (direct quotes from official Gloat pages).

- Vendor definition: "A talent marketplace is an AI-driven digital platform that matches employees with internal opportunities based on their skills, interests, and career goals." Opportunity types named: "internal job openings, projects, or mentorships"; also "projects, gigs, and mentorships."
- Mechanism: "uses AI or algorithms to match employees with internal job openings, projects, or mentorships based on their skills and interests. It collects workforce data, analyzes fit, and recommends opportunities."
- Internal-candidate bias posture: "internal candidates that the platforms suggest are recommended based on their skills and experiences, and nothing else" (democratization framing).
- Cultural/workflow reality acknowledged by the vendor: "talent hoarding" — managers restricting cross-functional opportunities even when the worker is interested; mitigation is named a core adoption best practice.
- Feature set named: career pathing ("present users with a few different options for what direction their careers can take"), mentoring ("generate suggestions based on your employees' skills, interests, and professional ambitions"), project and gig marketplace ("They can post a project on their platform and gain access to internal candidates with the exact skills they're looking for").
- Intelligent Tools (product architecture, 2026 positioning): "Personalized Matching Engine — Connects people to the right roles, learning, gigs, and mentors. Personalized to their skills, trajectory, and goals." "Role Progression Router — Maps every viable next step from any role." "Readiness Index — Scores how ready each person is for their next role." "Talent Pipeline — Manages internal and external talent pools." "Trigger Agent — Sets rules that trigger actions" (example: readiness score crossing a threshold fires a workflow). "Entity Generator — Creates new roles, jobs, projects." "Algorithmic Equity Layer — Checks every recommendation for bias before it reaches a user."
- "Agentic Mobility" use case composed of Matching Engine + Role Router + Talent Pipeline + Trigger Agent: "Surface internal movement opportunities."
- Deployment: HCM integrations (Workday, SAP SuccessFactors, Oracle); delivery into Microsoft Teams, Slack, Copilot. Scale claims (300,000 employees single-day deployment; customer savings figures) are marketing claims — recorded, not propagated.

### Fuel50

Evidence layer: A.

- Product family "Talent Marketplace" with sub-products: Mobility, Development, Gigs, Succession; plus Skills Intelligence (ontology, architecture, inventory) as the data foundation.
- Positioning: "Talent Marketplace connects employees to roles, projects, career paths, and growth opportunities based on skills, aspirations, values, and goals."
- Mobility: "Shows employees which internal roles their evolving skills unlock and the exact steps to get there"; "Surfaces qualified internal candidates for open roles and cross-functional moves instantly, cutting time-to-fill"; "Reveals ready-now internal candidates based on skills and readiness, not just titles."
- Gigs: "Matches people to stretch projects where they apply new skills on live business problems"; "Auto-matches employees to critical initiatives based on skills, availability, and interests, so you stand up project teams in days without adding headcount."
- Development: "Personalized, people-science-driven growth plans that map each employee's skills to target roles."
- Insights: "Live view of skills supply and demand across the enterprise"; scenario modeling for "build-versus-buy-versus-borrow" decisions.
- AI Career Advisor agent: "connects employees to relevant gigs, roles, mentors, and learning, personalized to their profile, values, and aspirations"; "the single entry point to Fuel50's full internal talent marketplace platform"; delivered in Slack/Teams/HR systems.
- Matching-data philosophy: "built on an expert-curated skills ontology, not AI-scraped data"; people-science validation; AI fairness/compliance posture.
- Integration: "integrates with leading HRIS, ATS, and LMS systems, including Workday and SAP SuccessFactors, layering skills intelligence and internal talent marketplace capabilities across your existing HR technology stack."
- Footnote: vendor self-identifies as a pioneer of the internal mobility market (analyst quote on site).

### Workday (HiredScore AI for Talent Mobility)

Evidence layer: A.

- Positioning: "Talent Mobility Agent takes the friction out of internal mobility by aligning talent to opportunities and proactively delivering personalized coaching and streamlined actions right in the flow of work."
- Key capabilities listed: personalized employee job matching; proactive career guidance via Microsoft Teams or email; streamlined internal recruiting; **manager-activated talent mobility**; real-time notifications and alerts; employee data optimization; internal mobility dashboard.
- Matching rule: "Employees are automatically aligned with open roles based on skills, experience, interests, and company mobility rules" — policy-aware matching.
- Employee surfaces: "Career Guide" showing "personalized job opportunities"; career profile where employees "update skills, experience, and education to further personalize job recommendations."
- Profile quality loop: "Employees get nudged to complete their profiles with timely, AI-powered reminders—powering better talent data, job matches, and decisions."
- Manager side: "Manager-activated talent mobility" (manager as gate); "Streamlined internal recruiting" (recruiter participation in internal hiring).
- Leadership analytics: "internal mobility dashboard displaying employee engagement and recommendation engagement"; "With holistic and employee-level insights, leaders can track progress."
- Customer story framing: opportunities delivered "based on experience and interests, company mobility policies, and business needs."

### SAP SuccessFactors (Career and Talent Development / Opportunity Marketplace)

Evidence layer: A at page level; operational detail not verified (help portal unreachable).

- Solution = Career and Talent Development within the SuccessFactors suite; includes "Personalized opportunity marketplace recommendations aligned to skills and aspirations."
- "Help employees discover personalized opportunity recommendations based on skills with an AI talent marketplace."
- "Empower employees to explore recommended roles and career paths and evaluate their readiness with AI-assisted career and skills insights."
- "Set and update aspirational development goals with AI."
- Mentorship: "Connect mentors and mentees based on skill matching."
- Succession: "Build a robust talent pipeline and evaluate potential successors with AI-assisted insights."
- Skills foundation: "A single, integrated skills model to put skills at the center of your talent strategy"; skills inferencing from continuous performance data ("reveals hidden strengths"); talent intelligence hub named as the skills data source (Grundfos customer story: "single source of skills data").
- Suite FAQ framing: AI improves "internal matching", "personalizing learning and career recommendations", "surfacing predictive insights (such as turnover risk and succession readiness)".

### Eightfold AI

Evidence layer: A.

- Project Marketplace (most explicit two-sided mechanics in the sample): "employees browse a list of internal company projects to surface projects that match their skills and preferences. Managers find employees with the skills they need and invite them to join their projects. AI matching automates the process with the best-fit people for each project, and the projects that most interest each person, without bias."
- Talent Management product: features "Internal mobility", "Talent Marketplace" (project marketplace capability), "Talent redeployment" ("match your workforce potential to open roles"), "Talent upskilling/reskilling."
- Data posture: "Eightfold connects skills, aspirations, and daily work to dynamically surface opportunities for growth."
- Workforce Exchange: "self-service talent intelligence" for employees; "Enterprise Talent Sharing" (multi-entity talent sharing).
- Separate Resource Management product: "Project staffing is easier with an AI-powered approach that matches skills to work" — the vendor itself splits marketplace (development mobility) from resource management (delivery staffing).
- Career Hub / Career Planner: "Self-Service Career Tools", "Career Path Discovery."
- Responsible-AI surfaces: published matching-model bias audits (evidence of governance maturity in the category).

## Cross-product Comparison

| Dimension | Gloat | Fuel50 | Workday | SAP SuccessFactors | Eightfold |
|---|---|---|---|---|---|
| Internal roles in catalog | A: "internal job openings" | A: "internal roles" / "open roles" | A: "open roles" | A: "recommended roles" | A: "open roles" (redeployment) |
| Projects/gigs as opportunity type | A: projects, gigs | A: Gigs sub-product | B: implied (not named on page) | C: not named on fetched pages | A: Project Marketplace |
| Mentorship pairing | A | A (agent connects mentors) | C: not named | A: "connect mentors and mentees" | B: skills-mentoring capability exists |
| Employee career profile | A: skills/trajectory/goals | A: profile, values, aspirations | A: career profile w/ skills/experience/education | A: skills model + aspirations | A: skills, aspirations, daily work |
| Matching → employee (recommendations) | A | A | A | A | A |
| Matching → owner (candidate discovery/invite) | A: Talent Pipeline | A: "surfaces qualified internal candidates" | A: streamlined internal recruiting | A: succession pipeline building | A: "Managers find employees... invite them" |
| Manager consent/release gate | A: anti-hoarding guidance | B: standard (not explicit) | A: "manager-activated talent mobility" | B: standard (not explicit) | B: standard (not explicit) |
| Policy/eligibility-aware matching | A: Governance Engine | A: fairness/compliance posture | A: "company mobility rules"/"mobility policies" | C: not explicit | A: "without bias" claim + audits |
| Career pathing / next-step discovery | A: Role Progression Router | A: "which internal roles their skills unlock... exact steps" | A: coaching | A: "explore recommended roles and career paths" | A: Career Planner |
| Readiness/gap signals | A: Readiness Index | A: readiness, "see what they are missing" | B: coaching implies | A: "evaluate their readiness" | B: implied |
| Profile-completion prompting/inference | B | C: ontology-based profiling | A: "nudged to complete their profiles" | A: skills inferencing from performance data | B: HCM data ingestion |
| Learning linkage | A: "roles, learning, gigs, mentors" | A: "gigs, roles, mentors, and learning" | B | B: "personalizing learning and career recommendations" | B: upskilling features |
| Mobility analytics | B: Report Generator | A: Insights (supply/demand) | A: internal mobility dashboard | B | B: engagement reporting implied |
| Notifications / flow-of-work delivery | A: Teams/Slack/Copilot | A: Slack/Teams agent | A: Teams or email | B: Joule/Teams (suite) | B: Teams support page |
| HCM/ATS/LMS integration | A: Workday/SF/Oracle integrations | A: HRIS/ATS/LMS incl. Workday & SAP | A: is the HCM | A: is the HCM | A: "unleash the data in your HCM" |
| Succession linkage | A: agentic succession | A: Succession sub-product | B | A | A: succession-planning capability |
| Delivery pole | standalone platform | standalone platform | suite module | suite module | standalone platform |

Cross-product commonalities (evidence layer B unless noted):

- Every sampled product runs a catalog of internal opportunities open only to the organization's own workforce (A in all five).
- Every sampled product maintains an employee-side representation (skills/experience/interests/aspirations) used by matching (A in all five).
- Every sampled product recommends opportunities to employees; four of five also surface candidates to opportunity owners/managers (Workday via recruiters, SAP via succession/mentorship machinery — B with A at four).
- Manager/owner participation is structural (posting, inviting, approving/releasing) in all five (B; "manager-activated" explicit only at Workday, anti-hoarding explicit at Gloat).
- AI-based matching is the current dominant mechanism (all five self-describe AI matching — A), but it is the mechanism layer, not the object structure.
- Mobility is policy-governed (explicit "company mobility rules" at Workday; governance/fairness machinery at Gloat, Fuel50, Eightfold — B).
- Career pathing, readiness signals, learning linkage, succession linkage, analytics, and HCM integration recur across the sample (B).

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

The smallest structure without which the product stops being an Internal Talent Marketplace:

1. **An organization-posted population of internal opportunities** — openings/engagements (roles; commonly also projects/gigs/assignments, sometimes mentorships) created and maintained by the organization, open only to its own workforce. Remove internal-only scope → it becomes a Job Board / ATS.
2. **An employee-side talent representation** — each employee carries a capability/interest profile (skills, experience, interests, aspirations, capacity; declared, imported, or inferred) that participates in matching. Remove it → a plain internal job-posting list.
3. **A two-sided connection mechanism** — the system connects the two sides: opportunities recommended to employees, and matching employees surfaced to opportunity owners. Self-identified application, rule-based search, and AI scoring are all valid realizations of this mechanism. Remove it → two disconnected databases.
4. **Governed resolution into internal movement** — expressed interest is worked through a managed process (owner review, current-manager release/approval, eligibility/mobility policy, selection) ending in placement or participation recorded as an outcome. Remove it → an opportunity feed/notice board, not a managed mobility system.

§24 historical check: AI matching, skills ontologies, gig catalogs, readiness scores, and chat-agent delivery are all removed from the invariant. An HRIS-era internal job posting module with manual search-and-apply plus an internal transfer approval path satisfies 1+3(self-identification as degenerate matching)+4 but lacks 2 — and indeed the market does not call that an internal talent marketplace; it calls it internal job posting. The Type's recognition threshold is the two-sided structure (talent side visible to the system). The definition therefore survives the historical check by design: the modern marketplace is the mature realization of "two-sided matching," not the definition itself. Regional/older products with rule-based matching (skill-tag searches, HR-curated candidate lists) still satisfy the core.

### L1 — Common Mature Structure

Present in most mature current products; expected by the market; not definitional:

- Opportunity-type portfolio: full-time internal roles + short-term projects/gigs + mentorship pairings (roles everywhere; gigs A in 4/5; mentorship A in 3/5)
- AI matching engine scoring employee↔opportunity fit (5/5)
- Career path exploration and next-step discovery (5/5 at some strength)
- Readiness/gap signals ("what am I missing", readiness scores)
- Profile building incl. inference from HCM/performance data and completion nudges
- Push delivery: proactive notifications/recommendations in flow of work (Teams/Slack/email/chat agents)
- Manager/opportunity-owner consoles (post opportunities, review matches/applicants, release team members)
- Mobility analytics (application/match/movement dashboards)
- HRIS/ATS/LMS integration spine (or being the HCM itself)
- Succession/talent-pipeline linkage
- AI governance posture (bias auditing, explainability, equity layers)

### L2 — Variant / Optional Structure

- Opportunity-type emphasis: role-first internal mobility vs gig/project-led agility vs balanced portfolio
- Delivery pole: standalone platform vs HCM-suite module
- Matching philosophy: deep-learning over broad talent data vs expert-curated ontology/people-science
- Scope: single-organization vs enterprise talent sharing across affiliated entities
- Surface: dedicated portal vs embedded in collaboration tools vs both
- Anonymized/blind candidate presentation, equity-specific program features
- Depth of internal-recruiting integration (requisition-aware internal roles)
- Program posture: opt-in development marketplace vs policy-driven redeployment (restructuring support)

### L3 — Vendor-specific (research notes only)

- Gloat: Loomra semantic layer; 14-tool toolkit (Semantic Retriever, Entity Retriever, Matching Engine, Role Progression Router, Predictive Attrition Modeler, AI Disruption Modeler, Future-State Readiness Index, Profile Builder, Trigger Agent, Entity Generator, Entity Updater, Talent Pipeline, Algorithmic Equity Layer, Report Generator); composable "Agentic Mobility" recipe; Microsoft Teams/Copilot/Slack delivery; customer claims (Schneider Electric 200,000 hours / $15M; Seagate $1.4M in 4 months; Mastercard 900,000 hours; 300,000-employee single-day deployment).
- Fuel50: Mosaic heritage; Mobility/Development/Gigs/Succession packaging; guided "Journeys"; Career Advisor Agent + Agentic Hub + MCP server; expert-curated skills ontology positioning; five consecutive SOC 2 audits claim; New York Anti-Bias compliance claim.
- Workday: HiredScore acquisition branding ("HiredScore AI for Talent Mobility"); Talent Mobility Agent; Career Guide; "manager-activated talent mobility"; internal mobility dashboard; case-study metrics (30% increase in internal application rates; 1.4× higher-quality internal applicants; 2.3× movement likelihood; 5% retention improvement).
- SAP: Opportunity Marketplace naming; Talent Intelligence Hub; skills governance UI; Joule; Career and Talent Development Assistant; certificates as talent attribute (1H 2026 release note).
- Eightfold: Workforce Exchange (enterprise talent sharing); Project Marketplace; Resource Management split; TalentForge; published matching-model bias audit results; Fosway/G2 badges.

## Rejected Findings

- "An ITM is the gig economy inside the enterprise." Rejected as definitional: gigs/projects are one opportunity family; role-only deployments satisfy the core.
- "An ITM requires AI matching." Rejected: mechanism is variant (rule-based, search-driven, manual curation all satisfy the two-sided connection requirement); AI is the current dominant mechanism, not the invariant.
- "An ITM includes learning delivery." Rejected: learning is a linked action/opportunity reference; the LMS remains a separate Type.
- "An ITM is a project-resource-management tool." Rejected: staffing execution for billable/delivery projects is a distinct Type (Eightfold ships both as separate products); the marketplace's purpose is capability development + internal mobility, not delivery staffing.
- "Succession planning is part of the ITM." Rejected as identity: succession is curated slate governance; the marketplace is open expression of interest. Linkage is common, not definitional.
- "Employee profiles must be built by AI inference." Rejected: declared/imported profiles satisfy the core; inference is a maturity feature.

## Boundary Findings

1. **vs Career Development Platform** — sharpest seam; the career-development-platform pass already flagged the internal-opportunity-marketplace seam as bundled-adjacent (discharged from this side here). Discriminator: object of record. Career development centers on employee-owned development plans anchored to paths/competencies (planning growth); the marketplace centers on a managed opportunity population and placement workflow (transacting mobility). Career pathing lives on both sides (paths are navigational aids in marketplaces; the plan is the record in career development). Bundling is universal at the specialist pole (Fuel50 Development vs Mobility as sibling sub-products) — packaging, not type identity.
2. **vs ATS / Recruiting Management Platform** — external hiring manages requisitions and external candidate pipelines; the marketplace's candidate population is the org's own employees. Suites converge operationally: internal roles often remain requisitions, and the marketplace "feeds" internal candidates into that process (Workday "streamlined internal recruiting"). Direction of value: ATS = hire from outside; marketplace = move from inside. A marketplace does not manage external candidate pipelines; an ATS does not maintain two-sided talent/opportunity matching.
3. **vs Skills Management Platform** — skills ontology/inventory is the data foundation the marketplace consumes (Fuel50 packages them as separate product families; SAP's talent intelligence hub feeds its marketplace). Skills platforms can exist with no opportunity population; a marketplace without skills data degenerates to title-matching. Feeds-vs-consumes relationship.
4. **vs Job Board** — audience and governance. Job boards advertise to the public and capture applications; the marketplace is closed to the workforce and manages the full mobility path (approval, release, placement). Also the internal-posting-module boundary: internal job posting inside an ATS is a capability slice, not this Type (no talent-side representation).
5. **vs Succession Planning / Talent Review Platform** — succession is governance over critical roles with curated slates and readiness data; the marketplace is open access where any employee may express interest. Products link them (succession candidates can be cross-referenced; pipeline building appears in both), but the participation model differs fundamentally.
6. **vs Resource Management / PSA** — matching skills to *work* for delivery/billing purposes vs matching people to opportunities for development/mobility purposes. Eightfold's own product split (Resource Management vs Project Marketplace) is the cleanest evidence that the market treats these as distinct.
7. **vs Employee Onboarding / Mentoring platforms** — mentoring is one opportunity type inside the marketplace; standalone mentoring platforms manage program lifecycle depth beyond pairing. Onboarding begins after placement; the marketplace ends at placement.

"Remove-and-flip" judgments: remove internal-only scope → Job Board/ATS; remove the opportunity population → Skills Management/Career Pathing; remove the talent-side representation → internal job posting (capability); remove governed resolution → opportunity feed; remove development/mobility intent → Resource Management.

## Uncertainties

- **Tier-1 operational docs unreachable** for all five products in this pass (SAP help portal JS-shell; Eightfold docs SSO-gated; Workday/Gloat/Fuel50 help centers not located on public web). All operational claims (approval-chain specifics, eligibility rules, gig time-allocation semantics, notification cadences, anonymization behavior) are therefore either unstated or kept at "mature products commonly / depending on the product" strength. No numeric limits or time windows appear in the final document.
- Workday evidence is product-page level; whether gigs/projects are a first-class Workday opportunity type is not verified (marked B/C).
- SAP evidence is page-level; the depth of Opportunity Marketplace's workflow integration with Employee Central (e.g., transfer processing) is inferred, not observed — kept as structural expectation, not claim.
- Gloat/Fuel50 customer-outcome numbers are vendor marketing — excluded from the final document entirely.
- Category naming drift: Workday currently sells this capability under "AI for Talent Mobility"; Eightfold under "Talent Marketplace"/"Project Marketplace"; SAP under "Opportunity Marketplace"; Gloat/Fuel50 under "Talent Marketplace". Name varies, referent stable — recorded as a taxonomy observation, not a problem.
- Cross-entity talent sharing (Eightfold Workforce Exchange) suggests a possible multi-org variant; not enough evidence to decide whether it is a variant or a drift toward a separate Type — left as variant with a note.

## Final Synthesis

An Internal Talent Marketplace is a two-sided internal-mobility brokerage: the organization maintains a population of opportunities open to its own workforce; each employee carries a capability/interest representation; a connection mechanism recommends opportunities to employees and surfaces matching employees to opportunity owners; and expressed interest is resolved through a governed process — owner review, manager release, mobility policy — into recorded internal movement (transfer, project participation, mentorship pairing).

The defining structure is fourfold (opportunity population · talent representation · two-sided connection · governed resolution). AI matching, skills ontologies, career pathing, readiness scoring, gig catalogs, succession linkage, analytics, and flow-of-work delivery are the standard capability layer that makes the Type valuable in its current market form but do not define it. The Type stands between the planning layer (career development, skills management, succession) and the systems of record (HRIS, ATS), consuming their data and handing back placements.
