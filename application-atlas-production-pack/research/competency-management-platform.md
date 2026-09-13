# Research Notes — Competency Management Platform

## Research Goal

Understand what a Competency Management Platform actually is as an Application Type: what objects exist inside it (competency models/frameworks, role requirements, per-person competency profiles, assessments, gaps), how the define → assign → assess → compare → act loop runs, who uses it, what rules govern it, and where the boundary lies against neighboring Types (Skills Management Platform, Career Pathing, Performance Management, Corporate LMS, Assessment/Psychometric platforms, Certification Management, Succession Planning, HRIS, Workforce Planning).

Directory context: leaf "Competency Management Platform", section 09 (HR, Workforce & Talent). Research date: 2026-09-07.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: an organization-defined competency framework (competencies with definitions and proficiency levels) + role requirements + per-person assessed competency profiles + gap analysis, feeding talent decisions (development, staffing, succession, compliance).
- Suspected confusions:
  - Skills Management Platform (§09 sibling, unprocessed): the market uses "skills" and "competency" interchangeably; suspected one family with two naming traditions.
  - Career Pathing Application (§09, processed): that pass recorded "competency framework definition and assessment are the primary object there; here the framework is consumed as node requirements" — confirm from this side.
  - Performance Management Platform (§09, processed): its related-types table says competencies appear inside reviews as criteria; the competency platform's defining object is the skill model and gap data — confirm.
  - Corporate LMS / Employee Learning Platform: learning as the remedy for gaps vs the record of competence.
  - Psychometric Assessment Platform (§09, processed): standardized psychological instruments vs organization-defined capability frameworks.
  - Certification Management (§09, processed): credential standing vs assessed capability.
  - HRIS: records the workforce vs governs capability.

## Research Questions

1. What is a "competency" in these products — definition, behavioral indicators, proficiency levels?
2. What is the framework/library object and how is it governed (created, versioned, approved)?
3. How do per-person competency profiles get populated (self-assessment, manager assessment, multi-rater, observed validation, HRIS import, AI inference)?
4. What does the assessment/validation workflow look like, especially in regulated/operational settings?
5. What gap analysis exists (individual, team/matrix, organizational)?
6. How does competency data flow into other talent processes (development, staffing, succession, performance, hiring)?
7. What roles use the system and what can each do?
8. What interfaces exist (matrix views, dashboards, assessment surfaces, search)?
9. Where is the boundary vs Skills Management Platform, and is the directory split defensible?
10. Historical check: do older/regional/non-AI implementations (paper competency dictionaries, skills matrices, spreadsheet-era systems) fit the same core?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Evidence quality |
|---|---|---|---|
| Avilar (WebMentor Skills) | classic competency-management specialist, compliance-heavy | SMB/mid-market + regulated orgs | Tier-1 product pages + FAQ (direct) |
| TalentGuard | governance/standards specialist ("skills trust") | mid-market/enterprise | Tier-1 product pages (direct) |
| SAP SuccessFactors Talent Management | enterprise HCM suite module, skills-first | enterprise | Tier-1 product page (direct; help-portal docs not fetched) |
| Oracle Talent Management (Dynamic Skills) | enterprise HCM suite module, AI skills | enterprise | Tier-1 product page (direct; docs not fetched) |
| Kahuna (Skills Manager) | frontline/operational competency validation | enterprise frontline (healthcare, energy, manufacturing, field service) | Tier-1 product pages + FAQ (direct) |

Rejected/abandoned samples: HRSG (dedicated competency-software vendor — www.hrsg.com timed out ×3, abandoned per network rule); HealthStream (healthcare competency — timed out ×2, abandoned); kahuna.com is an unrelated novel site; getkahuna.com transport error; cornerstoneondemand.com skills page 404.

## Sources

- Avilar — https://www.avilar.com/ , https://www.avilar.com/competency-management/webmentor-skills.html , https://www.avilar.com/competency-management/the-avilar-competency-model.html (fetched 2026-09-07)
- TalentGuard — https://www.talentguard.com/ , https://www.talentguard.com/platform (fetched 2026-09-07)
- SAP — https://www.sap.com/products/hcm/talent-management.html (fetched 2026-09-07)
- Oracle — https://www.oracle.com/human-capital-management/ , https://www.oracle.com/human-capital-management/talent-management/ (fetched 2026-09-07)
- Kahuna — https://kahunaworkforce.com/ , https://kahunaworkforce.com/kahuna-skills-manager/ (fetched 2026-09-07)

Source-access limitations: vendor help-center / operational documentation (SAP Help Portal, Oracle docs, Kahuna datasheets) was not reachable in this pass; evidence is from official product/marketing pages and FAQs. Assertion strength calibrated accordingly: no precise numeric limits, defaults, or state names claimed beyond what fetched pages state. HRSG and HealthStream unreachable — no claims rest on them.

## Product Observations

### Avilar — WebMentor Skills (evidence layer A)

- Self-positioning: "Competency Management System"; tagline "Track, Assess, and Grow Workforce Skills—Your Way"; explicitly anti-one-size-fits-all ("tailored to your workforce challenges").
- Key features listed: define job roles and skills (start from the Avilar Competency Model to map roles and required competencies); assess employee skills via online assessments at scale; analyze skills gaps and strengths with detailed reporting; automated compliance reporting; build development plans and training strategies to close gaps.
- FAQ definition: "Competency management software helps organizations define, assess, and manage employee skills, knowledge, and behaviors to align with business objectives."
- FAQ key features: competency mapping, skills gap analysis, role-based skill assessments, development plan creation, reporting and analytics, integration with LMS or HR systems, security and compliance.
- FAQ integrations: LMS, HRIS, ATS, performance management systems, talent management suites. Importable data: employee information, competency frameworks, role definitions, training history, performance data.
- Avilar Competency Model: 350+ skills clustered into 50+ skill groups; three components (professional skills, leadership skills, occupational/industry/job-role skills); usable as-is or customized.
- Customers: hospital training consortium (quote mentions "assess competencies… track compliance, monitor recertification timelines, and quickly find the right skill sets"), defense, engineering, criminal justice academy — compliance/qualification-heavy organizations.
- Deployment: cloud-hosted or licensed for on-premise installation. 25+ years in business.
- Case-study framings: quality-goal training targeting, project team staffing, M&A skill-gap closure.

### TalentGuard (evidence layer A)

- Self-positioning: "Enterprise Skills Trust & Readiness Intelligence (ESTRI)"; "the role and skills system of record alongside the systems you already own"; pitch is defensible, evidence-backed workforce decisions vs self-reported data.
- Named failure modes the product targets: no agreed standard (business units define roles differently), no approval record, no usable readiness signal (match scores / manager instinct).
- Nine modules mapped to six steps: (01) WorkforceGPT — generates job and skill profiles per role ("the raw standard your experts will review and approve"); (02) Intelligent Role Studio — governance: approvals, versions, publishing, "a named approver and date on every change"; Certification Tracking — credentials verified and current, "governed, not self-reported"; (03) Talent Assessment — "measures every employee against the approved standard — producing a validated level, a readiness score, and a specific gap list"; Performance Management — reviews/360 tied to the same competency standard; (04) Career Pathing — next roles based on validated skills against approved standards; (05) Development Planning — converts verified gaps into targeted development plans; (06) Succession Planning + Talent Insights — evidence-based succession calls traced gap-by-gap; board-ready intelligence.
- Architecture: integrates with Workday, SAP SuccessFactors, UKG, ADP, LMS, ATS; configurable workflows/approval chains/data models; full API access; SSO/SCIM, role-based access, complete audit log on every standard, approval, and decision; SOC 2.
- "Every decision in step 06 traces back to the standard built in step 01 — that's the evidence chain."

### SAP SuccessFactors Talent Management (evidence layer A, product-page level)

- Positioning: "Accelerate your skills strategy with AI-enabled insights across the talent lifecycle in a unified talent management system."
- Skills-first framing: "Use AI-enabled capabilities to drive skills-based talent decisions and mobility… Skills inferencing based on continuous performance data reveals hidden strengths."
- Career and Talent Development: AI-generated personalized development plans "to close skill gaps faster"; AI-highlighted career paths; succession risk surfacing.
- FAQ: "A skills-first approach prioritizes demonstrated skills and competencies over job titles… using skill profiles, assessments, and targeted learning to match people to roles, accelerate internal mobility, reduce bias, and close skill gaps faster."
- Suite modules around it: Recruiting (ATS), Onboarding, Learning (LMS with compliance training), Performance & Goals (reviews tied to skills-focused goals), Compensation.
- Note: SAP's current vocabulary is "skills"; the competency-framework heritage (competency library in Performance & Goals) was not directly verifiable from fetched pages — help-portal docs not fetched.

### Oracle Talent Management / Dynamic Skills (evidence layer A, product-page level)

- Positioning: "a unified, AI-embedded cloud solution powered by a single talent profile that connects people, work, and skills data."
- FAQ: "Oracle Dynamic Skills uses embedded AI to unify and continuously enrich your organization's skills data into a single, current view. That AI then matches people to opportunities and provides skills insights to improve hiring, learning, upskilling, mobility, scheduling, and workforce planning."
- Benefits: "single source of truth for employee data, skills, learning, performance, succession, and compensation"; "targeted upskilling helps address organizational skills gaps"; AI surfaces growth opportunities and career moves.
- Succession: AI identifies successors, evaluates readiness, monitors bench strength; talent review/calibration workspace.
- Note: same calibration caveat as SAP — suite product page, not operational docs.

### Kahuna — Skills Manager (evidence layer A)

- Self-positioning: "frontline workforce readiness platform, built on skills and competency management software that validates competency, not just completion"; "always know who's ready now and who's ready next."
- Industries: energy, healthcare, manufacturing, field service — each with a dedicated "competency management" page. Customers: SLB, Shell, P66, Weatherford, Wellstar, Stanford Children's, Cedars-Sinai.
- Four-step workflow: Curate ("create and maintain dynamic skills frameworks") → Assign ("align the right skills to the right roles") → Assess ("validate proficiency where work happens with objectivity") → Develop ("address skills gaps with targeted development plans").
- Features: flexible skills and assessment frameworks (configurable workflows, validation methods, equivalencies, prerequisites "to match the level of rigor each skill requires"); automated skills/competency assignments based on job role, location, job code, or custom field; team matrix in a single view (full competency profile of the team, spot gaps, search workers with specific skills across shifts and locations); employee dashboard (skills, required actions, career progression); talent finder (search workforce for specific skills/competency requirements to fill roles, cover shifts, staff projects); capability planning (model skills required for initiatives, identify who's qualified, uncover gaps for staffing/succession); analytics & reporting (readiness, compliance, skill gaps).
- Mobile app with offline capability and shared-device use; assessments/validations "anytime, anywhere."
- Explicit boundary claims: "Most LMS and HR systems track training completions or employee records but don't… show whether someone is actually qualified for the job"; blog title "Your HRIS Wasn't Built for Technical Competency Management."
- Integration: flat-file or API; HRIS (Workday, UKG, SAP, Oracle), LMS (Cornerstone, SumTotal, Degreed, Docebo), clinical systems (Epic, Cerner).
- Suite siblings: Ladder (career development paths), CertIQ (certification tracking, lapse flags, audit prep), Insights (workforce analytics), Skills Aggregator (announced).

## Cross-product Comparison

| Dimension | Avilar | TalentGuard | SAP SF | Oracle | Kahuna |
|---|---|---|---|---|---|
| Organization-defined framework/library as managed object | ✓ custom competency models; starter model available | ✓ job/role/skill standards, AI-drafted then expert-approved | ✓ skill profiles / skills data unified | ✓ skills data unified & enriched | ✓ dynamic skills frameworks curated |
| Proficiency levels / expectations | ✓ (model-based) | ✓ validated level vs approved standard | ✓ skill profiles + assessments | ✓ skills view (depth not detailed on page) | ✓ configurable rigor, validation methods, prerequisites, equivalencies |
| Role/job requirement mapping | ✓ map roles to required competencies | ✓ role standards | ✓ skills-based role matching | ✓ skills ↔ roles/opportunities | ✓ assign skills to roles; auto-assign by role/location/job code |
| Per-person assessed profile | ✓ assessments at scale | ✓ validated level + readiness score | ✓ skill profiles, inferencing from performance data | ✓ single talent profile | ✓ employee dashboard, validated skills |
| Assessment machinery | ✓ online assessments | ✓ Talent Assessment module | ✓ assessments | ✓ (implied via profile) | ✓ multi-method validation where work happens |
| Gap analysis | ✓ skills gap analysis, strengths | ✓ specific gap list, gap-by-gap | ✓ close skill gaps | ✓ skills gaps addressed | ✓ spot gaps (matrix), gap closure |
| Development linkage | ✓ development plans, training strategies | ✓ Development Planning module | ✓ AI-generated development plans | ✓ targeted upskilling | ✓ targeted development plans |
| Decision/deployment use | ✓ staffing, succession, audits | ✓ succession, promotion defense | ✓ mobility, succession readiness | ✓ mobility, succession, scheduling | ✓ talent finder (staffing/shifts), capability planning |
| Compliance/audit orientation | ✓ automated compliance reporting, recertification tracking | ✓ audit trail, evidence chain, certification tracking | ✓ (suite compliance training adjacent) | — (not on page) | ✓ audit-ready skill records, survey/audit prep |
| Integration spine | ✓ LMS/HRIS/ATS/performance | ✓ Workday/SAP/UKG/ADP/LMS/ATS, API | ✓ suite-native | ✓ suite-native | ✓ HRIS/LMS/clinical, API/flat file |
| Roles | admin/HR, manager, employee | experts/approvers, employees, leaders | employee, manager, HR | employee, manager, HR | admin, manager, validator, frontline employee, ops leader |
| AI posture | none claimed | AI-drafted standards (WorkforceGPT) | AI inferencing, AI plans | AI enrichment, matching | none claimed on fetched pages |
| Vocabulary | "competency" primary | "skills" (governance framing) | "skills" | "skills" | "skills and competency" mixed |

Cross-product commonalities (evidence layer B): all five hold (1) an organization-defined framework as a managed object, (2) role-attached expectations, (3) a per-person assessed profile, (4) an explicit comparison producing gaps/standing, (5) action linkage from gaps (development and/or deployment), (6) an integration spine into HR systems. Assessment machinery and reporting are present in all five; AI is present in only two of five — not definitional.

## Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Organization-defined competency model
  (maintained library of competencies with definitions + proficiency expectations,
   attached to the contexts that require them — commonly roles)
└── Per-person competency profile
    (assessed/validated standing against the model)
    └── Standing/gap comparison
        (person vs expectation — the managed output that drives talent decisions)
```

Three properties. Remove the model → an unstructured skill-tag list inside an HRIS. Remove the per-person profile → a published framework catalog (a career-ladder document). Remove the comparison → a skills inventory with no normative force (a data layer, not a management application).

Historical check: paper competency dictionaries with annual manager assessments, spreadsheet skills matrices (Fähigkeitsmatrix-style), and 1990s–2000s client-server competency modules all satisfy this core without AI, cloud, or any specific assessment mechanic — the definition is not over-fitted to the current AI-skills era.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- framework/library management tooling (create, organize, version; governance/approval workflows at the enterprise pole)
- role/job requirement mapping with expected proficiency per competency
- assessment machinery (self-assessment, manager assessment, multi-rater; observed validation with named validators at the operational pole)
- gap analysis at individual, team/matrix, and organizational levels
- development linkage (gaps → development plans / training recommendations; handoff to LMS)
- reporting/analytics (readiness, coverage, compliance)
- integration spine (HRIS employee/role import; LMS/ATS/performance handoffs; API)
- role model: HR/admin builds and governs; managers assess and view teams; employees self-assess and view requirements
- search/deployment surfaces (find people by competency)

### L2 — Variant / Optional Structure

- vocabulary pole: competency-framework-led (behavioral definitions, levels) vs skills-ontology-led (dynamic taxonomies, AI-inferred)
- assessment rigor: lightweight rating vs validated/observed sign-off with prerequisites, equivalencies, expiration/revalidation
- compliance/audit orientation (regulated industries) vs talent-development orientation
- AI posture: AI-inferred skills, AI-drafted frameworks, AI-generated development plans vs none
- off-the-shelf competency libraries vs fully custom models
- packaging: standalone specialist vs HCM-suite module vs frontline operational platform
- adjacent bundled modules: career pathing, succession, performance, certification tracking, opportunity marketplace
- deployment: cloud vs on-premise
- industry tuning: healthcare (nursing competency), energy, manufacturing, field service
- staffing/shift-scheduling consumption of competency data (frontline pole)

### L3 — Vendor-specific (research notes only)

- TalentGuard: ESTRI category coinage; WorkforceGPT; Intelligent Role Studio; named-approver-and-date governance; "evidence chain" framing; nine-module architecture; SOC 2 claim.
- Avilar: Avilar Competency Model (350+ skills / 50+ groups claim); WebMentor Skills/LMS product family; pricing claims (from $1.00/user/month; $2,500 one-time setup); on-prem licensing option.
- Kahuna: Skills Manager / Ladder / CertIQ / Insights / Skills Aggregator product names; Maui mobile app; shared-device offline use; "ready now / ready next" slogan.
- SAP: Growth Portfolio / Talent Intelligence Hub naming (from prior passes' context; not verified this pass), Joule assistants, Career and Talent Development Assistant.
- Oracle: Dynamic Skills, Opportunity Marketplace, Career Coach agent, Team Talent Calibration workspace, Growth Portfolio-era naming.

## Vendor-specific Findings

See L3 above. None of these enter the canonical model. Notably, two vendors (TalentGuard, Kahuna) ship career-pathing, succession, and certification modules as separate products beside their competency core — confirming those are adjacent Types, not part of this one.

## Boundary Findings

1. **vs Skills Management Platform (§09 sibling, unprocessed) — the load-bearing seam.** The sampled market mixes the two vocabularies at product level: Avilar titles its product "WebMentor Skills" under a "Competency Management System" umbrella; Kahuna alternates "skills management software" and "competency management software" across pages; SAP/Oracle use "skills" only. No sampled product maintains a hard skills/competency product split. Working resolution for this pass: Competency Management Platform is defined by the assessment-and-qualification process over an organization-defined model (this leaf); Skills Management Platform should be defined (at its own pass) around the skills ontology/inventory as a governed data asset supplying other systems (the internal-talent-marketplace pass already flagged the feeds-vs-consumes seam). Because products span both framings, a joint review / possible merge decision is recommended when skills-management-platform is processed. Recorded in STATUS Boundary Issues.
2. **vs Career Pathing Application (processed)** — confirmed from this side: career pathing consumes the framework as node requirements; competency management owns framework definition and assessment. Vendor-documented separation: TalentGuard ships Career Pathing as a separate module; Kahuna ships Ladder separately.
3. **vs Performance Management Platform (processed)** — confirmed: performance management owns the review cycle; competency management owns the model and assessed standing. TalentGuard ships Performance Management as a separate module "tied to the same competency standard"; SAP infers skills from performance data across product boundaries.
4. **vs Corporate LMS / Employee Learning Platform** — Kahuna's explicit positioning: LMS tracks completion; competency management validates qualification. Learning is the remedy for gaps, not the record of competence. Avilar and SAP ship LMS as separate products. Handoff seam: gaps → learning assignments.
5. **vs Psychometric Assessment Platform (processed)** — standardized psychological instruments with norm groups vs organization-defined capability frameworks with role expectations. Different object of record; instrument results may feed competency profiles (variant linkage).
6. **vs Certification Management (processed)** — credential standing granted by a certifying body vs assessed capability against an org framework. Kahuna (CertIQ) and TalentGuard (Certification Tracking) ship credential tracking as separate modules beside competency validation.
7. **vs Succession Planning Platform (unprocessed)** — succession consumes readiness/gap data for critical roles; competency management supplies it. Separate modules at TalentGuard, SAP, Oracle.
8. **vs HRIS** — Kahuna's explicit claim: HRIS records the workforce but wasn't built for technical competency validation. HRIS is the integration source for people/roles, not the system of record for assessed capability.
9. **vs Workforce Planning Platform (unprocessed)** — capability planning surfaces overlap (Kahuna Capability Planning); workforce planning owns demand/supply planning over time; competency management owns the capability record that feeds it.

## Uncertainties

- SAP/Oracle evidence is product-page level; operational docs (help portals) were not fetched. Suite-side assessment mechanics (e.g., how competency assessments are scheduled, rated, and approved inside the suites) are inferred from FAQ-level statements only — kept out of precise claims.
- HRSG (a dedicated competency-software vendor with off-the-shelf libraries) could not be reached; the off-the-shelf-library pole is evidenced only via Avilar's starter model.
- The healthcare/clinical competency sub-market (HealthStream et al.) could not be directly examined; the operational pole rests on Kahuna alone — claims about validation workflows (checklists, preceptor sign-off, expiration) are calibrated to Kahuna's public pages and marked product-specific where appropriate.
- Whether the market will sustain a durable product-level split between "competency management" and "skills management" is genuinely open; recorded as a boundary issue rather than resolved unilaterally.
- Exact proficiency-scale conventions (numeric levels, behavioral anchors) vary and were not deeply verified per product; no scale counts are claimed.

## Final Synthesis

A Competency Management Platform is the organization's system of record for workforce capability: it maintains the organization-defined competency model (competencies with definitions and proficiency expectations, attached to roles), records each person's assessed or validated standing against that model, and turns the comparison — gap or qualification — into the data that drives development, staffing, succession, and compliance decisions.

The defining core is three structures: the managed competency model, the per-person competency profile, and the standing/gap comparison. Framework governance, assessment machinery, gap views, development linkage, analytics, and the HRIS/LMS integration spine are standard capabilities. AI inference, off-the-shelf libraries, operational validation rigor, compliance orientation, industry tuning, and packaging shape are variants. The Type is packaging-agnostic: standalone specialists, HCM-suite modules, and frontline operational platforms all realize the same core.
