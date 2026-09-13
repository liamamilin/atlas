# Research Notes — Skills Management Platform

## Research Goal

Determine whether "Skills Management Platform" (directory §09 HR, Workforce & Talent) is a coherent Application Type distinct from its close siblings — Competency Management Platform, Internal Talent Marketplace, Career Pathing Application, Career Development Platform, HCM/HRIS — and if so, extract its defining core, standard structure, and boundaries from real products.

Special obligation carried into this pass: the competency-management-platform pass (2026-09-07) recommended a joint review, with the working resolution "Competency Management Platform = the assessment-and-qualification process over an organization-defined model; Skills Management Platform's distinct pole = the skills ontology/inventory as a governed data asset supplying other systems". The internal-talent-marketplace pass flagged "vs Skills Management (feeds matching, no opportunities)". This pass must ratify, refine, or reject those seams from the skills side.

## Initial Boundary

Working hypothesis before research:

- Core use: give an organization a governed skills vocabulary, per-person skills records against it, and population-level "who knows what" visibility, to feed staffing, development, mobility, and planning decisions.
- Primary users: HR/talent/L&D administrators, managers; employees as subjects; other systems as consumers.
- Nearest neighbors: Competency Management Platform (qualification process), Internal Talent Marketplace (opportunities), Career Pathing (career structure), HCM (people records), LXP/LMS (learning delivery), Workforce Planning (demand/supply over time).
- Likely confusion: "skills management" vs "competency management" vocabulary overlap — known from the sibling pass to be heavy.
- Unknowns: does a distinct product category exist outside HCM suites? What is the minimal pure-play core? Where does assessment/validation sit? Is AI inference definitional or era-typical?

## Research Questions

1. What is the primary managed object — is a skills taxonomy/ontology a first-class governed object, or merely a tag list on profiles?
2. How are per-person skill records populated (self-assessment, supervisor assessment, validation, AI inference) and how much does this vary?
3. What does the platform let users DO with the inventory (search people by skill, matrix, gap views, supply/demand, reports)?
4. How does the platform relate to roles/teams — is role-attachment definitional?
5. How does the platform supply other systems (API, integrations, embedded-in-suite)?
6. Where does the assessment-and-qualification process sit — in this Type or the sibling's? (Joint-review obligation.)
7. Would older/lighter implementations (spreadsheet skills matrices, 1990s skills-inventory modules) fit the proposed core? (Historical check.)
8. Do opportunity-less skills platforms hold together as a Type distinct from the Internal Talent Marketplace?

## Representative Products

Selected to span market poles (product philosophy × customer tier):

1. **Skills Base** (skills-base.com) — self-contained skills management & intelligence software; pure-play inventory tool; mid-market/operational industries (manufacturing, engineering, mining, energy, government). Full Tier-1 knowledge base reachable.
2. **TechWolf** (techwolf.com) — AI "skills intelligence" data layer; API-first; enterprise; inference from work signals; integrates into Workday/SAP/Visier; explicitly no employee-facing app.
3. **Gloat — Skills Foundation** (gloat.com) — skills ontology/architecture layer inside a broader talent-orchestration platform (Workforce Graph, Talent Marketplace); enterprise.
4. **Kahuna — Skills Manager** (kahunaworkforce.com) — frontline operational "advanced skills management"; validation-led; healthcare, energy, manufacturing, field service. Deliberately included as the seam case: the same vendor vocabulary spans "skills management" and "competency management" (the competency pass also sampled Kahuna).

Rejected/considered: Skills Base's old domain skillsbase.com is parked/for sale (product lives at skills-base.com — noted as sourcing caveat); Spatrix-class micro tools (docs too thin to add beyond Skills Base's pole); Degreed/360Learning (LXP pole — learning delivery is primary, would be an out-of-Type sample); Eightfold (talent intelligence spans recruiting + skills, broader than the Type); Workday Skills Cloud / SAP / Oracle skills (suite-embedded — covered as variant via HCM pass evidence and TechWolf/Gloat integration pages, not sampled directly).

## Sources

All fetched 2026-09-07:

- Skills Base — https://www.skills-base.com/ (product pages: /tour, /skills-tracking-software, /skills-assessment-tool, /skills-inventory-tool, /skills-matrix-software, /competency-skill-mapping-software, /skills-gap-analysis-tool, /sam-ai, /ai-skills-intelligence); Knowledge Base — https://support.skills-base.com/kb/ and Setup Guide https://support.skills-base.com/kb/articles/11000072681-3-step-guide-to-getting-started (Tier 1: data entities, assessments, targets, people finder, REST API endpoints, settings)
- TechWolf — https://www.techwolf.com/ (homepage: Skills/Work/Market Intelligence positioning, use cases, integrations); Developer portal — https://developers.techwolf.ai/reference/latest/API%20Documentation/Introduction/Introduction (REST API introduction)
- Gloat — https://gloat.com/skills-foundation/ (Skills Architecture / Skills Inventory / Skills Management sections); platform/ai-technology navigation (Knowledge Graph, use-case category "Skills: Inventory, gap analysis, and matching")
- Kahuna — https://kahunaworkforce.com/kahuna-skills-manager/ (product page + FAQ + workflow Curate→Assign→Assess→Develop + integration logos)

Sibling-pass evidence used for boundary calibration (not re-fetched): research/competency-management-platform.md, research/internal-talent-marketplace.md (per STATUS), research/career-pathing-application.md, research/career-development-platform.md, research/human-capital-management-hcm.md (Workday Skills Cloud note).

Source-access limitations:
- skillsbase.com is a parked domain for sale — the vendor's live domain is skills-base.com; recorded to avoid future confusion.
- TechWolf's site is JS-heavy; most nav items render as previews; evidence limited to homepage + API introduction. No deep API reference pages pulled.
- Gloat and Kahuna pages are marketing/FAQ level; no operational help centers were fetched in this pass.
- No claims below rest on unreachable sources; precise customer-story numbers (e.g. employee counts) are kept as vendor marketing figures in research notes only.

## Product Observations

### Skills Base (evidence layer A — Tier-1 KB + product pages)

Positioning: "Skills Management & Intelligence Software… Turn workforce skills and capability data into trusted intelligence for strategic planning, capability risk, workforce development and better people decisions." Explicit anti-pattern: "Replace disconnected spreadsheets and assumptions."

Data model (from KB, Tier 1):
- **Skills** — "the core of Skills Base"; specific capabilities (examples given: CSS, HTML, JavaScript), grouped in **Skill Categories** (hierarchical containers; categories are not assessable, skills are).
- **Skill Sets** — the set of skills a person is assessed on; 4 inheritance methods: Team / Role / All (every skill in the instance) / Custom (manually selected categories). A person inherits from exactly one method.
- **Roles** — position titles that can carry skill sets; **Teams** — org grouping (permissions + skill assignment); **Locations** — geographic attribute of people (used in People Finder); **People** — with or without login accounts.
- **Qualifications module** (optional) — tracks achievements/certifications; free-text or pre-defined mode; expiry notifications (vendor documents a 30-day default — product-specific detail).
- **Rating Scheme** — global for all skills (skills and interest rated on separately configurable scales; label overrides per category; N/A handling excluded from calculations).
- **Competency Targets** (optional) — expected skill levels set for a Team or Role; progress tracked as "Competency %" against target; feeds gap reports.
- **Assessments** — self-assessment and supervisor assessment types (each optional/enabled per Security Group); comments; rolling assessment intervals (default rolling period; fixed per-team dates on some licenses); pre-fill of previous ratings.
- **Interest levels** — a separate rating of a person's interest in each skill (assessed by default only in self-assessments).

Surfaces (Tier 1):
- Skills directory (taxonomy administration, rating-label overrides), Roles/Teams/People/Locations directories, per-entity dashboards (person, team, role, location) with gadget lists (top skills, most skilled, people with similar skills, keen to improve…).
- **People Finder** — find people by skill level, interest level, location, qualification.
- Reports: **Heat Matrix** (color skills matrix), Capability Matrix, Competency Analysis (bubble chart, enterprise license), Training Analysis, Report Builder, Permissions/Activity logs; exports for assessment data, skill assignments, targets, trends.
- REST API endpoints: Skills, Skill Ratings, Skill Categories, People, People Finder, Teams, Roles, Targets, Qualifications (+2.0 versions), Skill Query; SSO; regional hosting; Security Groups (view/read/write privileges per record type; a person has exactly one Security Group; supervisor = holder of the People>Assess privilege).
- **Training module** (add-on): maps external LMS/online content to skills and levels; training automatically suggested from current level and targets.
- AI layer: "Ask Sam" natural-language chat over the skills data; "Insights" automated AI intelligence engine (product pages).

Marketing-page pillars: Build (taxonomy) → Map (skills↔roles/teams/locations) → Assess (methodology) → Report (matrices, gap analysis) → Develop (training/career pathways) → Find (People Search) → Integrate (APIs to HR, LMS, CRM, BI). Customer quotes emphasize resource allocation ("assign engineers to projects"), L&D targeting, technician skills, new-hire training time (vendor-quoted outcomes — marketing figures, not operational claims).

### TechWolf (evidence layer A — homepage + API introduction; operational docs not pulled)

Positioning: "The data layer for the AI era of work… We connect three datasets that have never lived together: what your workforce can do, how their work is changing, and where the labour market is heading. All in one data layer, accessible inside the systems and agents you already use." Skill Engine™ is a registered trademark.

Skills Intelligence: "real-time visibility on the skills of your workforce… Replace static taxonomies with a dynamic, evidence-based view of your talent supply and demand." Purpose-built inference models "ingest raw work signals and transform them into a unified, high-fidelity picture of jobs, skills, and tasks unique to your organization."

Key structural facts:
- Employee-level skill records: customer-story figures cite "employees mapped into one unified skills taxonomy" and employees with "personalized skills signatures" (marketing figures).
- Delivery posture: no new employee app — "You don't need another app to onboard your employees in… the TechWolf data comes to life in your existing tech stack or where you use your agents." Integrations: "integrates directly into Workday's Skills Cloud", "seamlessly into SAP SuccessFactors", Visier; developer portal with REST API ("access to entity and skill data, and utility endpoints to provide additional insights").
- Use cases: skill gap analysis, strategic workforce planning, skill-based hiring, internal mobility, targeted upskilling, AI transformation readiness, role redesign.
- AI governance emphasis (ISO 27001/42001 badges; "defensible, academic-grade data").

### Gloat — Skills Foundation (evidence layer A — product page; marketing level)

Positioning: "Orchestrate skills and work with dynamic, AI-powered infrastructure… enables HR leaders to orchestrate skills data seamlessly across systems. By unifying data, it streamlines planning and integration… continuously updates and harmonizes data."

Three sections on the page:
- **Skills Architecture** — "Map skills for every role": real-time job architecture including the skills required for every role; AI recommendations on job design.
- **Skills Inventory** — "Get a comprehensive view of employee skills… where critical skills sit across your organization. Expand visibility into skills beyond employees' current roles."
- **Skills Management** — "Manage skills, wherever they sit": connect "any data set or system methodology into the Gloat platform to get one, holistic view of the jobs and skills in your company. Reduce fragmentation between varied data layers."

Context: Skills Foundation is one layer of the Gloat platform (Workforce Graph "People, jobs, skills connected"; Talent Marketplace; Agile Workforce Applications). Use-case category "Skills: Inventory, gap analysis, and matching". HCM integrations: Workday, SAP SuccessFactors, Oracle HCM; agent surfaces via Teams/Copilot.

### Kahuna — Skills Manager (evidence layer A — product page + FAQ)

Positioning: "Advanced Skills Management for Effective Competency Software… Validate Frontline Skills… see workforce readiness in real time, validate critical skills, and close gaps before they impact safety, compliance, and performance." One centralized skills management solution replacing "spreadsheets, siloed systems, and outdated processes".

Documented workflow (four steps): **Curate** (create and maintain dynamic skills frameworks) → **Assign** (align skills to roles; automated assignment based on job role, location, job code, or custom fields) → **Assess** ("Validate proficiency where work happens with objectivity"; configurable workflows, validation methods, equivalencies, prerequisites "to match the level of rigor each skill requires") → **Develop** (targeted development plans addressing gaps).

Surfaces named: Assessment Frameworks, Skill Assignments, Team Matrix ("see what your teams can do… spot gaps, manage assignments, search for workers with specific skills across shifts and locations"), Employee Dashboard (skills, required actions, career progression; current and prospective roles), Talent Finder ("find individuals who meet specific skills or competency requirements. Fill roles, cover shifts, staff projects"), Capability Planning ("model the skills required for any initiative, identify who's truly qualified, uncover gaps… staffing, succession planning, resource allocation"), Analytics & Reporting.

Other: mobile app with offline + shared-device support; integrations via flat file or API (LMS: Cornerstone, SumTotal; HRIS: Workday, SAP; scheduling: Kronos/UKG; clinical: Epic, Cerner). FAQ boundary statement: "Most LMS and HR systems track training completions or employee records but don't use skills testing software or skills inventory software to show whether someone is actually qualified for the job… Kahuna Skills Manager is designed specifically to manage and validate skills… define role requirements, assess skills in real time through multiple assessment methods, and validate job readiness." Industries pages are named "…-competency-management" while the product is "Skills Manager" — the vocabulary straddle in one vendor.

## Cross-product Comparison

| Structure | Skills Base | TechWolf | Gloat Skills Foundation | Kahuna Skills Manager |
|---|---|---|---|---|
| Maintained skills taxonomy/vocabulary as a first-class object | Yes — Skills + Skill Category hierarchy, "custom skills taxonomies" | Yes — "one unified skills taxonomy"; dynamic, evidence-based; replaces static taxonomies | Yes — Skills Architecture; AI-updated, harmonized across data layers | Yes — "dynamic skills frameworks" (Curate) |
| Per-person skills records | Yes — People with skill ratings (+ interest levels) | Yes — per-employee skill profiles / "skills signatures" (AI-inferred) | Yes — Skills Inventory view of employee skills | Yes — Team Matrix / Employee Dashboard |
| Population-level "who knows what" surface | Yes — People Finder, Heat Matrix, Capability Matrix, dashboards, Skill Query API | Yes — supply/demand and gap views; data consumed inside other systems | Yes — "where critical skills sit"; inventory + matching use cases | Yes — Talent Finder, Team Matrix search across shifts/locations |
| Recorded proficiency standing per skill | Yes — rating scale (global scheme, label overrides) | Yes — inferred skill data (method not documented at fetched depth) | Not explicit at fetched depth (skills data harmonized) | Yes — validated proficiency levels |
| Role/team attachment of skills | Common path but optional — Skill Sets via Team/Role/All/Custom | Yes — job architecture with skills per role | Yes — skills required per role | Yes — automated assignment by role/location/job code |
| Expectation/target vs standing comparison | Optional — Competency Targets + Competency % | Yes — skill gap analysis use case | Yes — gap analysis use case | Yes — gaps → development; readiness framing |
| Assessment/validation machinery | Self + supervisor assessment types (optional each) | No manual assessment documented — AI inference from work signals | No manual assessment documented — AI harmonization | Validation-first: methods, equivalencies, prerequisites, mobile/offline |
| Development linkage | Training module maps LMS content to skills; suggestions from level+targets; career pathways | Targeted upskilling use case | L&D use cases (upskilling/reskilling) in the platform | Develop step; development plans |
| Supply to other systems | REST API; HR/LMS/CRM/BI integrations | Defining posture — API/data layer into Workday/SAP/Visier/agents | Foundation for the wider platform; HCM integrations | Flat-file/API integrations incl. LMS, HRIS, scheduling, clinical |
| Interests/aspirations | Yes — interest level as separate rating | Not observed at fetched depth | Not observed at fetched depth | Career progression visibility (Employee Dashboard; Ladder is a separate product) |
| Certification/qualification tracking | Optional Qualifications module with expiry | Not observed | Not observed | Separate CertIQ product |
| Employee-facing surface | Yes — self-assessments, dashboards | Explicitly none ("no new app") | Via platform agents (Teams/Copilot) | Yes — mobile app, shared device, offline |
| AI positioning | Layer over the data (Ask Sam, Insights) | Core inference engine | Core (AI-powered, continuously updated) | Not emphasized (validation-first) |

Reading: four different products, four different philosophies (self-contained tool / API data layer / platform foundation / validation-led operational), and the same three-part skeleton underneath: governed skills vocabulary → per-person skills records → population-level inventory visibility. Everything else (role attachment, expectation comparison, assessment rigor, development linkage, API supply, interests, certifications, AI) varies by product or pole.

## Canonical Abstraction

### L0 — Defining Invariant

The Type's smallest stable structure, without which a product is not recognizable as a skills management platform:

```text
Organization's skills taxonomy
  (a governed, maintained vocabulary of skills — however shallow or deep —
   giving the workforce one capability language)
└── Per-person skills records
    (identified members of the organization × skills from the taxonomy,
     each carrying a recorded standing — level, endorsement, validation,
     or inferred signal)
    └── Population-level inventory visibility
        (the "who knows what" working surface: search people by skill,
         skills matrix, coverage/gap views over the whole workforce)
```

Removal tests:
- Remove the taxonomy → per-person profile tags with no shared language: an HCM profile feature, not this Type.
- Remove the per-person records → a published framework/taxonomy catalog with no workforce data: not this Type.
- Remove population-level visibility → per-person skill storage inside an HR record: a profile capability, not a platform of this Type.

Historical check: spreadsheet skills matrices (a defined skill list + per-person levels + a matrix view), 1980s–90s skills-inventory modules, and paper skill banks all satisfy this core without AI, API, cloud, role mapping, or assessment workflows. The core is deliberately implementation-neutral about how records are populated (self-rating, supervisor assessment, validation sign-off, or AI inference) and whether role expectations exist.

### L1 — Common Mature Structure

Present across most of the sample; practical but not definitional:

- Role/team attachment — skills assigned to roles or teams and inherited by members (automated requirement/assignment machinery at the operational pole).
- Expectation/target comparison — expected levels per role/team vs actual standing; gap as the pivot for development and staffing.
- Assessment machinery — self, supervisor, or validated assessment types with schedules/re-assessment cadence (realization varies; at the intelligence pole replaced by inference).
- Development linkage — gaps mapped to training/career pathways; training content imported from LMS or suggested; completions do not confer standing.
- People search / talent finder as a first-class surface (staffing, projects, shifts).
- Reporting/analytics — skills matrices, heat maps, capability/gap dashboards, exports.
- API/integration supply — REST APIs and connectors into HRIS/LMS/BI/scheduling; at the intelligence pole this is the dominant delivery posture (the "data asset supplying other systems" framing).
- AI layer — either as inference engine (populating records from work signals) or as query/insight layer over the inventory; era-typical, not universal in function.
- Permissions model scoped by role/team/security group; audit logs at the operational pole.

### L2 — Variant / Optional

- Interest/aspiration tracking as a separate rating dimension.
- Qualification/certification tracking with expiry (module or separate product).
- Employee-facing app vs no-app (data-layer pole); mobile/offline/shared-device support.
- Industry tuning (healthcare/energy/manufacturing/field service vs knowledge-work enterprise).
- Validation rigor depth (validation methods, equivalencies, prerequisites — the operational seam with competency management).
- Market-data overlays (external labor-market intelligence adjacent to the internal inventory).
- Packaging: standalone tool / API data layer / platform foundation / HCM-suite-embedded skills cloud.

### L3 — Vendor-specific (research notes only)

- Skills Base: 4 skill-set inheritance methods; global rating scheme with per-category label overrides; N/A calculation exclusion; rolling assessment interval with per-team fixed dates on some licenses; single-Security-Group-per-person rule; qualifications-expiry notification default (30 days, extendable); Ask Sam / Insights branding; enterprise-license Competency Analysis bubble chart.
- TechWolf: Skill Engine™ trademark; "skills signature" concept; Stanford Human Agency Scale reference for automation scores; Work Intelligence / Market Intelligence sibling lines.
- Gloat: Skills Foundation as one layer beside Workforce Graph / Talent Marketplace / Agile Workforce Applications; Governance Engine; Teams/Copilot agent surfaces.
- Kahuna: Curate→Assign→Assess→Develop four-step framing; Maui mobile app; CertIQ and Ladder as sibling products; integration logos (Epic, Cerner, Kronos…).
- Customer-story figures (HSBC 250k+ employees mapped, Ericsson 100k+ skills signatures, Workday 15% time-to-hire) are vendor marketing metrics — not used in the final document.

## Vendor-specific / Rejected Findings

- "Skills management = AI inference" — rejected as definitional. Skills Base and Kahuna operate with human assessment/validation as the primary population mechanism; the historical check (spreadsheet era) passes without AI.
- "Skills management = role-attached requirements" — rejected. Skills Base documents skill sets inherited from Team/Role/All/Custom; role attachment is a common realization, not the definition (role-attached expectations are the sibling Type's core).
- "Skills management = competency management under another name" — rejected as full alias (see Boundary Findings), but accepted as heavy vocabulary overlap.
- "Interest levels" and "certification tracking" — observed in only part of the sample → optional/variant.
- "Global single rating scheme" — Skills Base-specific detail; not generalized.

## Boundary Findings

1. **vs Competency Management Platform (closest sibling; joint-review obligation from the competency pass).** Evidence from this side supports keep-both with a center-of-gravity seam, refining the sibling's working resolution:
   - Shared skeleton: both hold a capability vocabulary, per-person records, and gap/standing comparisons. Market vocabulary overlaps (Kahuna: product named Skills Manager, industries pages named competency management; the competency pass observed Avilar titling a product "WebMentor Skills" under a "Competency Management System" umbrella).
   - The seam adopted here: **a skills platform's managed object is the inventory** — the vocabulary and the per-person records as a queryable organizational data asset; assessment is one input mechanism, role expectations are optional (Skills Base: All/Custom skill sets; targets optional; TechWolf/Gloat: no qualification process at all). **A competency platform's managed object is the qualification process** — the governed model with role-attached expected proficiency, assessment/validation rigor, qualification states, and audit evidence; the inventory is the byproduct.
   - Decisive evidence: TechWolf and Gloat run no assessment-and-qualification process (inference/harmonization instead; no validation workflow, no compliance evidence chain) yet are unambiguously skills platforms; conversely, the competency pass's sample (Avilar, TalentGuard) centers governance of the standard and qualification evidence. The seam is a gradient with real poles, not a clean line — Kahuna-class operational products straddle it (validation rigor + audit readiness on one side, inventory/matrix/finder on the other).
   - Outcome: joint-review flag DISCHARGED from this side with keep-both + center-of-gravity test; cross-reference recorded in both directions.
2. **vs Internal Talent Marketplace.** Confirms the marketplace pass's "feeds matching, no opportunities" flag: TechWolf lists internal mobility as a use case (supplying match data) and Gloat operates a Talent Marketplace as a separate platform line — the skills layer posts no opportunities and manages no expression-of-interest/placement workflow. Boundary: opportunity brokerage (marketplace) vs capability data asset (this Type).
3. **vs Career Pathing / Career Development Platform.** Confirms both passes' "library instrumental vs primary" seam: career pathing attaches skill requirements to role nodes; career development plans act on profile context. Here the vocabulary+records themselves are the managed object. Development linkage (gaps → training) is common-but-not-definitional here.
4. **vs HCM / HRIS.** HCM holds people/employment records; skills appear as profile attributes (the HCM pass noted Workday Skills Cloud as suite-specific machinery). The skills platform owns the capability vocabulary and inventory as its primary object with dedicated machinery (taxonomy editors, matrices, finders, APIs) and exchanges data with the HCM. Boundary: person-of-record vs capability inventory.
5. **vs Corporate LMS / Employee Learning Platform.** Kahuna's FAQ states the market's own boundary: LMS/HR systems "track training completions… but don't show whether someone is actually qualified". Gaps flow to the learning system; completions do not confer skills standing. Boundary: learning delivery vs capability record.
6. **vs Workforce Planning Platform.** Skill-gap analysis and workforce-readiness views feed planning; demand/supply modeling over time, scenario/headcount planning remain the planning Type's objects (TechWolf even pairs a separate Work Intelligence line).
7. **vs Technical Assessment Platform.** External-candidate skill testing vs internal workforce inventory; different population (candidates vs employees), different unit (test events vs standing records).
8. **vs Performance Management Platform.** Review cycles vs capability standing; skills may feed reviews as criteria.
9. **Capability-slice check (is this a Type at all?).** The counter-hypothesis — "skills management is just HCM profile data" — fails: pure-play products (Skills Base) exist with the inventory as the entire product; API-first data layers (TechWolf) exist as standalone companies; Gloat sells a skills foundation as a distinct layer. The Type holds.

## Uncertainties

- Gloat's per-person record mechanics (proficiency values, population methods) are not visible at the fetched depth — the inventory claim rests on the product page's own "comprehensive view of employee skills" language (evidence strength A for existence, weaker for mechanics).
- TechWolf's operational details (how skill levels are represented, whether employees see or correct their profiles) are behind the JS site and deeper API docs — not pulled; no operational claims made.
- The exact market share / typical customer size of the pure-play pole vs the intelligence pole is unknown; sampling was by philosophy, not market size.
- Whether suite-embedded skills clouds (Workday/SAP/Oracle) would satisfy L0 independently was not verified by direct fetch in this pass — carried from the HCM pass's Workday Skills Cloud note + TechWolf/Gloat integration pages (calibrated, not directly sampled).
- The competency seam is a gradient; products at the Kahuna position could reasonably be claimed by either Type. If the directory is ever consolidated, the seam (not the vocabulary) is the tiebreaker to re-examine.

## Final Synthesis

A Skills Management Platform is the organization's capability inventory: a governed skills vocabulary, per-person skill records against it, and population-level visibility over the whole ("who knows what"). Its managed object is the inventory as a data asset — populated by whatever mechanism the product philosophy favors (self/supervisor assessment, validated sign-off, AI inference), optionally organized by roles and targets, and supplied onward to staffing, development, mobility, and planning systems. The qualification process over role-attached expectations belongs to the sibling Type; opportunities belong to the marketplace; learning delivery belongs to the LMS; the person-of-record belongs to the HCM. The Type survives the historical check (spreadsheet matrices and 1990s skills-inventory modules fit) and the capability-slice check (pure-play and API-first standalone products exist). Keep-both with Competency Management Platform ratified on a center-of-gravity seam; joint-review flag discharged from this side.
