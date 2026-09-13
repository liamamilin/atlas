# Research Notes — Environmental Impact Assessment Platform

Research date: 2026-09-08

## Research Goal

Understand what software called an "Environmental Impact Assessment (EIA) Platform" actually is in the market: what objects it holds, who uses it, how the assessment work flows through it, what the legally-shaped process looks like inside the software, and how it differs from neighboring environmental-software Types (permit management, compliance management, environmental data/monitoring platforms, site assessment, LCA).

## Initial Boundary

Initial hypothesis before research:

- EIA is a legally mandated, pre-approval process: a proponent of a proposed project must assess its predicted environmental effects (baseline → impacts → significance → mitigation → residual → monitoring), submit the assessment to a competent authority, and obtain an environmental decision before proceeding.
- Software in this space is likely either (a) authority-operated electronic EIA systems (single-window submission, review, public consultation, registry), or (b) proponent/consultant-side tooling (authoring, screening, data). Hypothesis: the publicly documented center of gravity is the authority-operated system.
- Nearest confusable Types: Environmental Permit Management, Environmental Compliance Management (already processed), Environmental Site Assessment, Environmental Data Platform, Environmental Monitoring Platform, government Permit Management / Planning & Zoning, public comment platforms, Life Cycle Assessment Application.

## Research Questions

1. What is the "project of record" and who is the "proponent of record"? How is identity handled?
2. What does the assessment document consist of (baseline, impacts, significance, mitigation, monitoring)? How does the platform structure it?
3. What is the process the assessment moves through (screening, scoping, submission, review, consultation, decision, post-decision)?
4. What roles exist (proponent, consultant, authority, expert committees, sector agencies, citizens) and what can each do?
5. What surfaces exist (submission workspace, public registry, comment surface, maps, dashboards)?
6. What rules govern behavior (admissibility, signatures, statutory windows, sensitive information, fees, modifications, appeals)?
7. What happens after the decision (conditions, compliance documents, monitoring)?
8. Where is the boundary with permit management, compliance management, site assessment, and data/monitoring platforms?

## Representative Products

Selection logic: EIA is jurisdictional by construction — the process is defined by national/subnational law. The publicly documented implementations of EIA platforms are overwhelmingly authority-operated systems with rich official documentation (user manuals, FAQs, process pages). Five products across four jurisdictions + one process reference:

1. **e-SEIA / SEA (Chile)** — Servicio de Evaluación Ambiental's electronic SEIA system. Fullest single-window realization: proponent/consultant/citizen profiles, electronic file, two instrument tracks, citizen participation, pre-entry determination, decision + appeals.
2. **EPBC Act Public Portal (Australia, federal)** — referral-based national environmental assessment portal: referral lodgment, public comment on the screening decision, project registry, offsets register, payments.
3. **NSW Major Projects Hub (Australia, state)** — state significant development/infrastructure assessment inside the planning portal: authority-issued assessment requirements, EIS exhibition, submissions, determination, post-approval documents.
4. **US EPA NEPA process + NEPAssist (US)** — process documentation for the agency-authored NEPA model (CATEX/EA/EIS ladder) + EPA's environmental screening tool.
5. **Find a National Infrastructure Project — Planning Inspectorate (UK)** — NSIP registry with search, map, process guide, participation guide (home page evidence only; process guide fetch failed).

Rejected/unreachable candidates (recorded as limitations, no claims built on them):

- **PARIVESH (India MoEFCC)** — large national single-window EIA/EC system; parivesh.nic.in timed out twice.
- **Canadian Impact Assessment Registry (IAAC)** — 403; canada.ca timed out twice.
- **National EPA EPBC process pages (nationalepa.gov.au)** — timed out twice (portal itself fetched fine).
- **European Commission EIA pages** — server error.
- **BLM ePlanning (US NEPA documents/comment)** — 403.
- **Commercial proponent/consultant-side EIA suites** — no official documentation located through two search-engine attempts (results polluted); no assertions made about them as products. Consultant-facing behavior in this research is grounded only in the roles evidenced inside the authority-operated platforms (see per-product observations).

## Sources

All fetched 2026-09-08 unless noted.

- SEA Chile (Servicio de Evaluación Ambiental):
  - Portal root — https://sea.gob.cl/ (nav: e-SEIA login, project search, PAC portal, pertinencia, manuals, maps, consultant register, RCA review, statistics)
  - Process page — https://sea.gob.cl/evaluacion-de-impacto-ambiental/cual-es-el-proceso-de-evaluacion-de-impacto-ambiental (DIA vs EIA instruments, minimum contents, timelines, PAC, appeals)
  - e-SEIA FAQ — https://www.sea.gob.cl/soporte/preguntas-frecuentes-e-seia (8 profile types, titular correctness, signature tiers, PAC observation flow, pertinencia platform)
  - User manuals — https://www.sea.gob.cl/manuales-de-usuarioa (geoinformation manual, signature configuration, e-pertinencia manual; agency manuals behind login)
- EPBC Act Public Portal (Australia):
  - Root — https://epbcpublicportal.environment.gov.au/ (nav: guides, all projects, notices, open for comments, offsets register; referral comment under s74(3), 10 business days; payments)
  - Guides & resources — https://epbcpublicportal.environment.gov.au/guides-resources/ (PMST, Significant Impact Guidelines, mapping guidelines)
  - All EPBC Projects — https://epbcpublicportal.environment.gov.au/all-referrals/ (filter fields)
  - Glossary — https://epbcpublicportal.environment.gov.au/guides-resources/glossary (controlled action, PPA/PDP, project area, footprints, impacts, alternatives, split referrals, sensitive information, level of confidence, waivers)
- US EPA:
  - NEPA review process — https://www.epa.gov/nepa/national-environmental-policy-act-review-process (CATEX/EA/EIS ladder, EIS contents, NOI/scoping/draft/final/ROD)
  - NEPAssist — https://www.epa.gov/nepa/nepassist (screening tool description)
- NSW Planning Portal (Australia, state):
  - Major Projects hub — https://www.planningportal.nsw.gov.au/major-projects (surfaces incl. post-approval documents, community quote)
  - Assessment — https://www.planningportal.nsw.gov.au/major-projects/assessment (SSD/SSI, whole-of-government assessment, REAP scheme)
  - Projects list — https://www.planningportal.nsw.gov.au/major-projects/projects (status lifecycle vocabulary)
- UK Planning Inspectorate:
  - Find a National Infrastructure Project — https://infrastructure.planninginspectorate.gov.uk/ (registry, search, map, process/participation guides)

## Product Observations

### e-SEIA / SEA (Chile) — evidence layer A unless noted

- **Project entry**: proponent ("titular") creates the project in the system; if the titular is a company, entry must go through the company's legal representative profile. Documents required for *admisibilidad* (admissibility) depend on titular type. All resolutions — including the final *Resolución de Calificación Ambiental* (RCA) — are generated in the name of the registered titular. [A]
- **Role model — 8 private-sector profiles**: Titular Persona Natural; Representante Legal; Administrador de Empresa; Ciudadano; Representante de Organización; Consultor Ambiental (processes DIA/EIA on behalf of a titular who contracted the consultancy); Administrador de Consultora (contracts consultants, responds to consultancy requests, assigns projects to consultants); Consultor de una Consultora. Profiles are acquired/derived through "Herramientas Administrativas". [A]
- **Two instrument tracks**: DIA (Declaración de Impacto Ambiental) vs EIA (Estudio de Impacto Ambiental), with different statutory evaluation timelines (60/120 days + 30/60-day extensions), different public-participation rules (PAC always for EIA; only on request for DIA if the project generates environmental burdens), indigenous consultation where significant impact on indigenous peoples (EIA), and different appeal channels (Executive Director vs Committee of Ministers). [A]
- **Assessment content standard** (regulatory minimum contents, RSEIA arts. 12–19): project description; determination and justification of the *área de influencia* (area of influence); detailed description of the area of influence — *línea de base* (baseline); (EIA) prediction and evaluation of environmental impacts; justification that art. 11 significant effects do/do not exist; (EIA) mitigation, repair, compensation plans; contingency prevention and emergency plans; (EIA) environmental variable monitoring plan (*plan de seguimiento*); compliance plan for applicable environmental legislation incl. sectoral permits (PAS); voluntary commitments. [A]
- **Pre-entry screening**: *Consulta de Pertinencia* — a separate electronic platform (pertinencia.sea.gob.cl) where a proponent asks the authority whether a given project/activity must enter the SEIA at all; online progress tracking; three signature modalities. [A]
- **Citizen participation (PAC)**: citizen profile → "Ver Proyectos en PAC" → list of projects in participation → submit observation with attachments → sign and send. Organization representatives do the same as organizations. Dedicated PAC portal pages; citizens can request PAC opening on DIAs. [A]
- **Electronic file & signatures**: projects processed electronically; advanced electronic signature (FEA, accredited certificate/token) enables fully electronic processing without paper copies at the oficina de partes; simple signature requires paper formalization; visualization plug-ins for signed documents; automated notification emails for pending activities. [A]
- **Public registry/search**: search projects by name, region, presentation type (DIA/EIA), presentation date, qualification date, project state, productive sector, typology; sector taxonomy includes mining, energy, aquaculture, sanitary, ports, transport, etc. [A]
- **Maps**: interactive project map, territorial analysis, and a *baseline* map (líneas de base of EIAs); geoinformation manual with a term dictionary and templates for georeferenced submissions. [A]
- **Post-decision and governance**: RCA review procedure section; *Recursos de Reclamación* (appeals) portal with progress dashboard; certified consultant register (art. 81(f) law 19.300); monthly statistical reports of projects in the SEIA. [A]
- Support manuals for signature tokens, browser plug-ins, document handling; SEA/agency-facing manuals require authorized login. [A]

### EPBC Act Public Portal (Australia, federal)

- **Process shape**: a person ("person proposing to take the action", PPA) submits a **referral**; the Minister invites **public comment on each referral** regarding whether the proposed action is a **controlled action** (portal states this runs under s74(3) of the EPBC Act for 10 business days). Assessment and approval follow for controlled actions; the approval is issued to the PPA, who is responsible for compliance with approval conditions. [A]
- **Roles**: PPA (proponent); **proposed designated proponent** (PDP) — person nominated by the PPA to fulfill assessment requirements, may act on the PPA's behalf, can be the same person; **referring party** — "might be your environmental consultants or someone else helping you prepare and complete your referral". [A]
- **Screening self-service**: the **Protected Matters Search Tool** "should be used to help work out if you need to lodge a referral or avoid impacts in the project area"; Significant Impact Guidelines advise on determining whether an action is likely to have a significant impact. [A]
- **Project registry**: searchable/filterable list of all EPBC projects — EPBC number, project name, **proposer/approval holder name**, industry type (mining, energy generation renewable/non-renewable, exploration marine/non-marine, transport air/land/water, waste, water, aquaculture, tourism...), jurisdiction, valid-date range. Separate surfaces: **All notices**, **Open for comments**, **Offsets register**. [A]
- **Glossary of canonical terms**: controlled action; significant impact (importance judged by sensitivity/value/quality of environment + intensity/duration/magnitude/extent); project area; disturbance footprint; avoidance area; buffer area; directly/indirectly impacted (incl. downstream/upstream and facilitated third-party action); **proposing alternatives** — "any ways the action has been considered to proceed and including the option of not proceeding... including those which are feasible but are not proposed"; split referrals / staged developments; sensitive information (protected-matter locations, culturally sensitive info, commercial-in-confidence — agency may seek consent before publishing); **Level of Confidence** rating for data currency/accuracy/reliability (High/Medium/Low with concrete criteria); fee payment and waiver rules. [A]
- **Payments**: invoicing and payment services for EPBC projects run through the portal (portal banner). [A]
- Spatial data requirements: mapping guidelines explain how to prepare and provide maps/boundary data "for each stage of the EPBC Act environmental assessment process". [A]

### NSW Major Projects Hub (Australia, state)

- **Framing**: state significant development (SSD) / state significant infrastructure (SSI) under the Environmental Planning & Assessment Act 1979 requires approval from the Minister for Planning or the Independent Planning Commission; the Department "co-ordinates a whole-of-government assessment of the impacts of the projects against the triple bottom line"; "Community participation is an essential part of the assessment process". Elsewhere on the same hub: "Community participation is a critically important component of the **environmental impact assessment** of State significant projects." [A]
- **Lifecycle states** (filter vocabulary of the project list — direct evidence of the process stages the platform models): Prepare SEARs (Secretary's Environmental Assessment Requirements = authority-issued scoping requirements) → Prepare EIS → Review Application → Arrange Exhibition → Exhibition → Collate Submissions → Response to Submissions → Assessment → Recommendation → Determination; Withdrawn; plus Modification reports and SSD/SSI Modifications. [A]
- **Public surfaces**: find a project (filters by status, local council area, development type, industry type, assessment type); **On Exhibition** — current exhibitions where the public has its say; submissions on state significant applications "must be made online through the NSW Planning Portal". [A]
- **Proponent side**: account login to "manage applications"; **post-approval documents** lodging service (post-decision compliance documents go into the same platform). [A]
- **Quality machinery**: **REAP** — Registered Environmental Assessment Practitioner scheme "provides environmental assessment quality assurance for state significant projects"; agency directory for contacting assessment agencies; engagement guidelines for state significant projects. [A]

### US EPA — NEPA process + NEPAssist

- **Process ladder** (process documentation, not a product UI): Categorical Exclusion (CATEX) → Environmental Assessment / Finding of No Significant Impact (EA/FONSI) → Environmental Impact Statement (EIS). [A — process doc]
- **EIS flow**: agency publishes Notice of Intent (starts **scoping** — agency and public define issues and alternatives) → draft EIS published for public review → final EIS responds to substantive comments → **Record of Decision** (agency's decision, alternatives considered, mitigation and monitoring plans). Supplements required on substantial changes/new information. [A — process doc]
- **EIS content structure**: cover sheet, summary, purpose and need, **alternatives including the proposed action**, **affected environment** (baseline), **environmental consequences** (effects and their significance), scoping summary, list of preparers, appendices. [A — process doc]
- **Who authors**: in this model the federal agency itself develops the proposal and prepares the EIS (with cooperating agencies); the "proponent" of the assessment is the agency — a structurally different posture from proponent-submitted regimes. [A — process doc]
- **NEPAssist**: "a tool that facilitates the environmental review process and project planning... draws environmental data dynamically from EPA GIS databases and web services and provides immediate **screening** of environmental assessment indicators for a **user-defined area of interest**... raises important environmental issues at the **earliest stages of project development**." [A]
- Citizen participation in NEPA documented on adjacent EPA pages (commenting, obtaining EIS copies). [B]

### Find a National Infrastructure Project (UK Planning Inspectorate)

- **Public registry** of Nationally Significant Infrastructure Projects (power stations, highways, power lines): search by project name or **applicant**; complete list; **map view**. [A]
- Guides: "See the process" (decision-making process guide — from pre-application through examination to decision; page fetch failed, 502 ×2 — structure asserted only from home-page description) and "How to have your say on a project"; separate information for professional users and for "submitting a project" (gov.uk collection). [A for surfaces; the process-stage detail unverified]

## Cross-product Comparison

| Structure | e-SEIA (CL) | EPBC (AU-federal) | NSW (AU-state) | US NEPA/EPA | UK PINS | Layer |
|---|---|---|---|---|---|---|
| Proposed project as identified record with proponent of record | titular (persona/empresa), resolutions issued in titular's name | PPA / approval holder; referral by a "person" | SSD/SSI application by applicant | federal action by lead agency | project / applicant | A×5 |
| Consultants recognized as a distinct working role | Consultor Ambiental + consultora profiles | referring party (consultants) | REAP practitioners (quality assurance) | list of preparers | professional users | A×4 |
| Pre-entry screening step | consulta de pertinencia (separate platform) | referral + controlled-action decision (+ PMST self-check) | SSD/SSI classification (+ SEARs) | CATEX determination | (unverified) | A×4 |
| Scoping: authority fixes required assessment content | (content fixed by RSEIA arts.) | assessment approach follow referral | SEARs issued by Department | scoping process after NOI | scoping (unverified) | A×3+ |
| Assessment of record: project description + affected area/baseline + predicted effects & significance + mitigation + monitoring | DIA/EIA minimum contents incl. baseline, impact prediction/evaluation, mitigation/reparation/compensation, plan de seguimiento | significant impact framework, footprints, direct/indirect impacts, offsets | EIS assessed against SEARs | affected environment + environmental consequences + ROD mitigation/monitoring | EIA documents in registry | A×4 |
| Alternatives incl. not proceeding | (regime-specific) | proposing alternatives (glossary) | (regime-specific) | alternatives incl. proposed action | (unverified) | A×2+ |
| Public/stakeholder consultation with structured submission | PAC (always EIA; conditional DIA) + indigenous consultation | referral comment 10 business days (s74(3)) | Exhibition + mandatory online submissions | scoping + draft-EIS comment | "have your say" guide | A×5 |
| Authority review with expert/agency input | evaluation commissions (COEVA), sectoral pronunciamientos (PAS) | Minister/agency assessment | whole-of-government assessment + agency directory | lead + cooperating agencies | examining authority | A×4 |
| Decision instrument that gates the project | RCA in the name of the titular | approval to the PPA with conditions | Minister/IPC determination | ROD | development consent | A×5 |
| Conditions / offsets / commitments | compliance plan + voluntary commitments + RCA conditions | approval conditions; offsets register | conditions of consent | ROD mitigation & monitoring | (unverified) | A×4 |
| Modification / amendment sub-process | project modifications | change of proponent/transfer policy | SSD/SSI Modifications + mod reports | supplemental EIS | (unverified) | A×4 |
| Post-decision compliance artifacts | compliance plan → follow-up; monitoring plan | approval-holder condition compliance | post-approval documents lodging | ROD monitoring | (unverified) | A×3 |
| Public registry with search + map | project search + mapa de proyectos | all projects + filters + notices | project list + spatial viewer | (EIS database elsewhere) | registry + map | A×4 |
| Electronic identity + signature for binding acts | FEA tokens vs simple signature | sign-in + payment | portal account | (agency-side) | (unverified) | A×3 |
| Fees/payments | (not observed) | invoicing + payments + waiver | (not observed) | (not observed) | (unverified) | A×1 → Optional |
| Appeals/reconsideration | recursos + Comité de Ministros | (review rights exist; not fetched) | (unobserved) | (not in fetched pages) | (unverified) | A×1 → Variant |
| Two-tier instrument depth (declaration vs full study) | DIA vs EIA | (via controlled-action decision) | (via SSD/SSI + SEARs depth) | CATEX/EA/EIS ladder | (unverified) | pattern across 3 → Common, not definitional |
| Statistical reporting | monthly SEIA reports | (not observed) | (not observed) | (not observed) | (unverified) | A×1 → Optional |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Three structures held jointly:

1. **The proposed project of record** — a specific proposed development project or activity, identified with a proponent of record and a defined location / area of influence, entered into the platform before the project may proceed. Remove → environmental data platform, monitoring platform, or compliance tooling with nothing under assessment.
2. **The environmental assessment of record for that project** — a structured assessment produced to a legally defined content standard: description of the project and its affected environment (baseline), prediction and evaluation of effects and their significance, mitigation measures, and monitoring/follow-up commitments. Remove → permit tracker, planning-application file, or document manager with no assessment of effects.
3. **The authority-facing evaluation that gates the project** — the assessment is submitted to the competent environmental authority and moves through a legally defined evaluation process (screening/acceptance → review → consultation → decision), ending in an environmental decision instrument on which the project's ability to proceed depends. Remove → an internal environmental study or research-reporting tool.

Jointly-held is load-bearing:
- 1 alone → project registry (projects with no assessment or gate)
- 2 without 1+3 → consultancy study workspace / environmental reporting
- 3 without 2 → permit-application tracking (authorization without effects assessment)
- 1+2 without 3 → environmental study project (no regulatory gate)
- 1+3 without 2 → planning-application tracker

### L1 — Common Mature Structure

- Screening / pre-entry determination (pertinencia platform; controlled-action referral decision + PMST; CATEX) — authority-side or self-service, distinguishing "must assess / must not / must not proceed without assessment"
- Authority-issued scoping of the assessment (SEARs; scoping process; statutorily fixed minimum contents)
- Public/stakeholder consultation phase with structured, attributable submissions and authority responses (legally near-universal across the sample, but a platform could omit it and still be an EIA platform)
- Public project registry: search, filters (sector/industry/location/status), notices, published documents, often a map
- Electronic submission with account identity and (where law requires) signature mechanisms; admissibility checks tied to proponent identity
- Expert/agency input machinery (sector agencies, expert committees, cooperating agencies)
- Decision instrument with conditions/commitments; mitigation hierarchy incl. offsets/compensation
- Modification/amendment sub-processes for changing approved projects
- Post-decision compliance artifacts (monitoring reports, condition-compliance documents lodged into the platform)
- Recognized consultant role (preparation/processing on behalf of the proponent)

### L2 — Variant / Optional Structure

- **Operator/side posture**: authority single-window (Chile), planning-portal-embedded state assessment (NSW), referral-based federal portal (EPBC), agency-authored (US NEPA — the "proponent" is the agency)
- **Tiered assessment depth**: lighter instrument vs full study (DIA/EIA; EA/FONSI/EIS) — common but regime-specific
- Appeals/reconsideration machinery; committee-of-ministers review
- Fees/payments and waivers
- Indigenous / customary-owner consultation tracks
- Consultant registration or certification schemes (consultores register; REAP)
- Data-quality rules for submitted evidence (Level of Confidence ratings)
- Sensitive-information handling (withheld locations, cultural/commercial sensitivity)
- Statistical reporting/dashboards; baseline/territorial map services
- Strategic/environmental assessment of plans and programs (plan-level sibling) — adjacent variant
- Language/jurisdiction packaging (the platform exists per legal regime)

### L3 — Vendor/Jurisdiction-specific (kept in notes)

RCA / Resolución de Calificación Ambiental; COEVA evaluation commissions; Comité de Ministros; consulta de pertinencia platform; FEA token signatures and Panel Único de Firmas; e-SEIA 8-profile model; s74(3) 10-business-day referral comment; PMST; MNES vocabulary; SPRAT database links; SEARs; SSD/SSI identifiers (SSD-nnnnnn); REAP scheme; NSW status vocabulary; NOI/Federal Register/EPA Notice of Availability; ROD; FONSI; NEPAssist GIS layer set; offsets register surface; invoicing/payment receipts issue.

## Vendor-specific / Rejected Findings

- **"EIA platform = government single-window"** — rejected as definition. The single-window is the dominant *operator posture* in the sample, but the L0 (project + assessment + authority gate) also fits agency-authored (NEPA) and planning-embedded (NSW) postures. Defining the Type by the Chile/India single-window shape would be operator-posture overfitting.
- **"EIA platform = consultation platform"** — rejected. Participation is one legally-shaped phase; Petition/Public-comment platforms make participation the whole object.
- **"EIA platform = environmental data/GIS platform"** — rejected. Baseline maps and screening tools (NEPAssist, PMST) feed the assessment; the platform's subject is the project's assessment and gate, not the data corpus.
- **"Two-track DIA/EIA instruments"** — not promoted to core; it is Chile's (and analogously NEPA's) tiered-depth implementation. Abstracted to L2 "tiered assessment depth".
- **"Offsets register"** — EPBC-specific surface realization of the common mitigation-hierarchy concept.
- **Specific statutory day-counts** (60/120 days etc.) — jurisdictional facts, kept out of the canonical document.
- **8-profile role taxonomy** — e-SEIA-specific; abstracted to proponent/consultant/citizen/authority roles.

## Boundary Findings

- **vs Environmental Permit Management** (§21 sibling): permits authorize operating under conditions over the authorization's lifecycle; EIA predicts effects of a *proposed* project and produces a pre-approval decision. Seam: the EIA decision instrument often *is* a permit or bundles sectoral permits (Chilean RCA; NSW consent) — coupling is deep, but the center of gravity differs (assessment of effects vs authorization lifecycle). "Remove the assessment-of-effects machinery and keep authorizations → Environmental Permit Management."
- **vs Environmental Compliance Management** (processed 2026-09-08): compliance = standing obligation register + recurring obligation-driven work for an operating organization; EIA = one-time (per project) prospective assessment + gate. Seam artifact: post-decision condition compliance inside EIA platforms is project-linked and narrower than the org-wide obligation register.
- **vs Environmental Site Assessment** (§21 sibling): ESA assesses existing/retrospective contamination of a site (due diligence); EIA assesses prospective effects of a not-yet-approved project.
- **vs Environmental Data Platform / Environmental Monitoring Platform**: they hold/produce the data; EIA consumes baselines and commits to monitoring. NEPAssist demonstrates the seam from inside: a screening tool explicitly supporting "the earliest stages" of review, not the review itself.
- **vs Permit Management / Planning & Zoning Management (§24 government)**: EIA is the environmental-effects leg of what planning/permitting systems do across all domains; where EIA is embedded (NSW), the platform is a planning system whose environmental leg still carries the L0 above. Keep separate: removing zoning/land-use machinery leaves EIA intact.
- **vs Life Cycle Assessment Application**: LCA models product/process footprints with no project subject in place, no authority gate, no consultation phase.
- **vs Petition / Public Comment / Civic Engagement platforms**: consultation here is bounded to a project's assessment phase, tied to a decision instrument.
- **vs Monitoring & Evaluation Platform (nonprofit)**: name collision — M&E "impact assessment" is retrospective measurement of program outcomes; EIA is prospective prediction of project effects under a legal gate.
- **vs Document Management / e-filing**: documents are the medium; the object of record is the project's assessment and its gate.

## Taxonomy Notes (for STATUS Boundary Issues)

- The leaf sits in §21 (Environment, Sustainability & Climate — mostly enterprise-side environmental software), but the market realization of this Type is overwhelmingly **authority-operated jurisdictional platforms**. The proponent/consultant side participates through roles inside these platforms; standalone commercial proponent-side EIA suites were not documentable from official sources. Recorded as a sourcing/market-structure observation.
- Deep coupling with Environmental Permit Management (the EIA decision frequently bundles permits) — flagged for that leaf's future pass.

## Uncertainties

- **PARIVESH (India)** unreachable: cannot confirm its workflow details; no claims built on it. The "single-window" pole rests on Chile + the two Australian systems.
- **Commercial proponent/consultant-side EIA tooling**: no official docs found; consultant-side behavior is evidenced only inside authority platforms (roles, preparation requirements, signature/processing rights). The final document describes proponent/consultant activity at that evidenced level.
- **UK process stages** beyond the home-page description unverified (502 ×2).
- **Depth of post-decision compliance machinery** varies; NSW post-approval documents observed as a lodging service only.
- **Appeal mechanisms** directly observed only in Chile.
- Exact statutory timelines, document formats, and fee amounts vary by jurisdiction and were deliberately excluded from the canonical document.

## Final Synthesis

An Environmental Impact Assessment Platform is the software that carries the environmental impact assessment process for proposed projects: it holds the proposed project as an identified record with a proponent of record; it structures the environmental assessment of record (baseline → predicted effects and significance → mitigation → monitoring commitments) to a legally defined content standard; and it moves that assessment through the authority's evaluation — screening, scoping, review with agency/expert input, public consultation — to a decision instrument that gates the project, with modifications and post-decision compliance artifacts tracked in the same record. The dominant market realization is the authority-operated jurisdictional system (single-window or portal-embedded), with proponents, their consultants, sector agencies, expert committees, and citizens as distinct roles on the same record. Everything else — instrument tiers, appeals, fees, consultant registers, maps, statistics — is variant or optional structure.
