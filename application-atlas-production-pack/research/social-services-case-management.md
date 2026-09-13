# Research Notes — Social Services Case Management

## Research Goal

Understand what a "Social Services Case Management" application is as an Application Type: who operates it, what objects exist inside it (people/households, cases, programs, eligibility determinations, assessments, service plans, authorizations, case notes), how the casework lifecycle flows, what roles and rules matter, and where the Type's boundary sits — especially against the processed siblings **Nonprofit Case Management** (§25), **Child Welfare Management** (§24), and **Probation & Parole Management** (§24), whose passes left joint-review flags for this leaf, and against the unprocessed §24 neighbors **Public Sector Case Management**, **Public Benefits Management**, and **Housing Assistance Management**.

## Initial Boundary

Initial hypothesis: the government social/human-services agency's casework system of record — state/county human-services departments (US), local-authority adult social care (UK), municipal social services (EU). People apply for or are referred into public social-service programs; the agency determines eligibility/need against public program rules; an accountable caseworker carries the case through assessment → planning → service delivery → review → closure; everything is documented for public accountability.

Adjacent Types to separate:
- Nonprofit Case Management — same casework spine, private operator, org-defined programs, funder accountability.
- Child Welfare Management — statutory child-protection specialization.
- Probation & Parole Management — supervision under legal authority with conditions and sanctions.
- Public Benefits Management — program/benefit-centric eligibility and issuance (unprocessed sibling).
- Public Sector Case Management — generic government casework without the social-services person/program model (unprocessed sibling).
- Public Employment Service Platform — labor-market intermediation (processed; employment-services casework is a program-area variant here).

## Research Questions

1. Who operates this software (government levels, commissioned providers)?
2. What are the core objects and how do they relate (person/household, case, program, eligibility, assessment, plan, service, note)?
3. What is the eligibility/need determination loop and where does it sit relative to the case?
4. What is the casework lifecycle (intake → … → closure) and its states?
5. What roles exist (caseworker, supervisor, eligibility worker, administrator, client) and how do they shape workflow?
6. What accountability machinery exists (reporting, compliance, audits, mandated windows)?
7. What money/benefit machinery exists (benefit programs, billing, personal budgets, charges)?
8. What is common-but-not-definitional (portals, mobile/offline, AI, multi-program unification, HMIS)?
9. Where are the boundaries with the sibling Types (removal tests both directions)?

## Representative Products

| Product | Vendor | Pole | Tier |
|---|---|---|---|
| CaseWorthy (incl. ClientTrack, ServTracker, MediSked applications) | CaseWorthy (Eccovia merged 2025) | US multi-program human-services platform selling to nonprofits AND local/state government (government vertical page) | Tier 2 |
| WellSky Human Services (Aging & Disability et al.) | WellSky | US state agencies + community-based organizations: aging/disability, protective services, Medicaid waivers, vocational rehabilitation, OAA programs; "44 states" claim | Tier 2 |
| Liquidlogic Adults Case Management (LAS) | System C (Liquidlogic) | UK local-authority adult social care — statutory casework (Care Act), personal budgets, multi-agency | Tier 2 |
| Northwoods Traverse (Adults & Aging; Economic Assistance program areas) | Northwoods | US county departments of social services — documentation-first casework across adult & aging + economic assistance (Medicaid/SNAP/TANF/LIHEAP) | Tier 2 |

Selection rationale: four different vendors; four different customer tiers (state agencies, county departments, UK local authorities, mixed gov/nonprofit platforms); different product philosophies (unified multi-program platform vs state-program suite vs statutory casework with deep finance vs documentation-first county casework). Child-welfare program areas deliberately excluded from the sampled evidence (sibling Type; Northwoods sells Traverse for Child Welfare as a separate program area — used as boundary corroboration only).

## Sources

Fetched 2026-09-09 (all Tier 2 official product pages; no Tier-1 help-center documentation reachable — see Uncertainties):

- CaseWorthy — https://caseworthy.com/ (root); https://caseworthy.com/who-we-serve/government-and-public-sector/ ; https://caseworthy.com/platform/caseworthy-platform/
- WellSky — https://wellsky.com/ (root); https://wellsky.com/human-services-software/ ; https://wellsky.com/aging-disability/
- System C / Liquidlogic — https://www.systemc.com/ (root; liquidlogic.co.uk redirects here); https://www.systemc.com/local-government/adult-social-care/
- Northwoods — https://www.teamnorthwoods.com/traverse/traverse-program-areas/ ; https://www.teamnorthwoods.com/traverse/traverse-program-areas/traverse-for-economic-assistance/

Not reachable (recorded limitations): footholdtechnology.com (403 ×1 — abandoned), olmsystems.com (transport error ×2 — abandoned), tyler.com/products/caseworker/ (404), northwoods.com (wrong company — diagramming libraries; correct domain is teamnorthwoods.com). Sibling-pass evidence used as corroboration: research/nonprofit-case-management.md (Apricot, Casebook, CaseWorthy, Lamplight), research/child-welfare-management.md (Northwoods Traverse child-welfare program area, Casebook), research/probation-parole-management.md.

## Product A — CaseWorthy

### Key observations (Layer A unless noted)

- Positioning: "purpose-built, mission-critical software platform for case & program management… across the spectrum of human services"; serves "1,000+ Nonprofit organizations, local and state governments who touch more than 41% of the US population". Marketing stats: "15M+ Individual & Family Cases Supported", "300M+ Case Notes Recorded", "700K+ Community Workers, Providers & Locations Supported", "$22.3B+ in Claims Processed", "4B+ Services Delivered".
- Government vertical page ("Government Case Management — Unified Case Management for Public Sector Employees"): "streamline case management across city, county, and state agencies"; program areas listed: Health & Human Services, Immigration & Refugee Assistance, Disaster & Emergency Response, Housing & Utility Assistance, Student & Education Programs, Workforce Guidance.
- Named capability blocks on the government page: Easy-to-Use Case Worker Interface ("input any information about a client or service with just a few clicks"); Client Engagement Portal ("complete forms, sign documents, explore services, and contact case managers"); Cross-Department Data Aggregation ("at the city, county, state, or federal level"); **Assessments & Eligibility ("Assessment and budgeting tools to rapidly identify program eligibility and service requirements from client information, streamlining intake processes")**; Robust Reporting & Analytics ("pre-defined formats or customizable templates to meet various stakeholder needs"); Secure Data Management.
- Role model on the government page: Case Managers, Program Directors, Agency Leadership, IT Administrators, Clients & Constituents, Grant & Compliance Officers ("Track funding sources and allocations across programs… Maintain documentation for audits"), County & City Administrators.
- Platform page: "Unified Client & Program Data — single, shared view of your client and program information across funding streams and partners"; "Configurable Case Management — Configure workflows, forms, assessments, and service plans… without custom code"; "Operational & Compliance Reporting — standard, ad hoc, and funder-ready reporting"; "Service Delivery & Tracking — Track services, utilization, and outcomes in real time across programs… what is delivered, to whom, and with what results"; applications ClientTrack (multi-program/funding-stream case management), ServTracker (aging services), MediSked (HCBS/I/DD, "Medicaid-supported service delivery").
- Security: role-based access, encryption, "support the rigorous demands of government and human services organizations", HIPAA-class compliance framing.
- Home-page loop framing: "Intake That Accelerates Services — Capture critical data, determine eligibility in real time, and connect clients to services"; "Care Delivery — Design intelligent care plans, coordinate services seamlessly, and continuously monitor progress"; "Reporting That Secures Funding and Proves Impact — audit-ready reporting".
- Program-area breadth (Who We Serve): aging, behavioral health, I/DD, education, employment & career, family services, homelessness & HMIS, government, veterans, survivor services.

## Product B — WellSky Human Services

### Key observations

- Positioning: "Intelligent human services software for aging and vulnerable populations"; "WellSky software for social services supports a wide range of programs, including home- and community-based services for aging and disability, homeless management information systems, technologies for adult protective services, case management for vocational rehabilitation agencies, and versatile documentation tools for multi-program non-profits."
- **Core-loop sentence (Layer A, strongest single formulation in the sample): "WellSky solutions are purpose-built to manage intake, eligibility, care plans, service delivery, outcomes tracking, and reporting."**
- Market footprint claims: "44 states use WellSky human services software"; "over 50% of AAAs in the U.S."; state agencies + community-based organizations both served.
- State Program Solutions: Medicaid Waivers, Vocational Rehabilitation, Older Americans Act, Protective Services, Incident Management, Managed LTSS. Community Program Solutions: Aging & Disability, Information & Referral, Community-Based Organizations, Housing & Homelessness, Blood Centers.
- Aging & Disability page: "automates every step of the care process, from eligibility and intake, to assessments and care planning, to financial processing"; AAAs/ADRCs managing "Older Americans Act programs and other services funded by federal grants and state and local funds"; "track all client touches and facilitates secure, role-based collaboration among everyone in the care network, reducing duplicative tasks while allowing information to be shared across programs"; reporting "comply with funding source requirements"; billing "automatically bill third-party organizations, including Medicaid"; ombudsman module "track and manage nursing home complaint investigations from intake through closure… compliance with the Older Americans Act Performance System (OAAPS)"; modules include Assessment Designer, Service Delivery Manager, Caregiver Module; Mobile Assessments "with or without the internet".
- Case studies: Oklahoma Department of Human Services ("serves over 18,000 elderly and disabled members… paper-based system caused long wait times… to enroll and to receive services"); Georgia Division of Aging Services; Care Connect network ("single system for intake, assessment, eligibility screening, referrals, and care coordination").
- Compliance framing: "simplify financial management and reporting to lock in compliance with federal requirements".

## Product C — Liquidlogic Adults Case Management (System C)

### Key observations

- Positioning: "market leader, AI powered case management system designed to meet evolving requirements within Adults Social Care"; used by UK county/borough councils (Cheshire East, Suffolk, East Sussex, Oxfordshire, Stoke-on-Trent logos).
- Process scope (Layer A): "handles a wide range of processes, including contacts, referrals, assessments, personal budgets, reablement plans, care and support planning, plus service commissioning… management of both funded adults and self-funders".
- Statutory framing: "customisable pathways that support statutory casework and ensure regulatory compliance in daily practice"; East Sussex case study: "helping the council meet increasing demand and Care Act obligations"; safeguarding, DoLS, and Shared Lives Carers named as incorporated machinery.
- Multi-agency: "Delegation functionality enables real-time multi-agency contributions to assessments and forms… delegate sections of an assessment or form to different users or teams"; Delegation Portal extends to external agencies ("Health practitioners or Best Interest Assessors… contribute directly to assessments and forms, without the need to access the wider… system"); "Configurable privacy settings protect sensitive data".
- Finance depth: "full suite of finance functionality to support all elements of contracts, payments, and charges, including detailed support around personal budgets"; financial assessments; separate Social Care Finance product (ContrOCC) and Commissioning product in the same family.
- Worktrays (interface evidence): "configurable individual Practitioner, Manager, Workgroup, Waiting List, and Budget Worktrays, along with intelligent form design".
- Mobile/offline: "mobile working is supported via wireless hotspots or 3G networks, and offline working is available out of the box through the widely used Briefcase functionality".
- Multi-agency applications: "different organisations can have their own referral and assessment forms while sharing the same data".
- Roles addressed: Director of Adult Social Care, Finance Director, Chief Executive.
- Single-record framing: "a comprehensive, single view of a person or family from one system" (adults + children + education on one platform).

## Product D — Northwoods Traverse

### Key observations

- Positioning: "Purpose-built software for the everyday realities of health and human services work… Traverse serves adult & aging, child support, child welfare, and economic assistance program areas. Each area brings its own pressures, documentation demands, and regulatory requirements."
- Foundation framing: "agencies that need strong documentation, configurable workflows, and clear visibility across daily operations".
- **Adult & Aging focus areas (Layer A): adult protective services (APS), developmental disabilities services, home- and community-based care, long-term care coordination, mental health services, guardianship support, in-home supportive services.**
- **Economic Assistance page: "Simplify complex eligibility processes, support remote work, and empower client self-service"; "Manage applications, verifications, and eligibility information that update instantly within electronic case files"; "You move applications, verifications, and eligibility decisions across multiple programs. And you do it while meeting strict deadlines." Programs: Cash Assistance, Child Care Assistance, Energy Assistance, LIHEAP, Medicaid, SNAP, TANF, Workforce Programs.**
- Workflow machinery: "Automatically route documents, forms, and verifications by program"; "Supervisor Oversight — Give supervisors instant visibility into workers' caseloads and due dates"; "meeting all required service response windows"; operational metrics ("Track worker activity, client engagement, and program performance").
- Cross-program view: "Traverse's modular structure allows you to securely share information across program areas… Cross-departmental visibility lessens the need for clients to repeat their stories."
- Regulatory adaptation: "adapting to changing state and federal requirements… configurable workflows, documentation tools, and reporting abilities."
- Customers named: Cleveland County Department of Social Services (child support), Wilson County Department of Social Services ("Traverse streamlines the communication between workers and supervisors… real-time interaction and document review").
- Grove = human-powered case-aide/administrative support service (not software) — vendor-specific.

## Cross-product Comparison

| Structure | CaseWorthy | WellSky | Liquidlogic Adults | Traverse | Verdict |
|---|---|---|---|---|---|
| Identified person/household records for people served | "Individual & Family Cases", 360° client view | "client touches", care network | "single view of a person or family" | "people and families you serve" | **All 4 — core** |
| Case opened under a public program, carried by an accountable caseworker | case & program management; case managers | case management for state programs | statutory casework pathways; Practitioner/Manager worktrays | electronic case files; caseloads | **All 4 — core** |
| Eligibility/need determination against public program rules | "determine eligibility in real time"; Assessments & Eligibility block | "intake, eligibility…" first-class; "eligibility screening" | assessments + financial assessments (Care Act gate) | "applications, verifications, and eligibility decisions" | **All 4 — core (public-mandate marker)** |
| Assessment machinery | assessments configurable | assessments + Assessment Designer | assessments (FormFlow AI) | verifications/documents | **All 4 — core** |
| Service/care plan | "Design intelligent care plans" | "care plans" | "care and support planning", reablement plans | (documentation-first; plan implied in case files) | **3–4 — core** |
| Service delivery/authorization tracking | "Track services, utilization, and outcomes" | "service delivery" | service commissioning; funded adults & self-funders | service-delivery visibility | **All 4 — core** |
| Documented casework record (notes/forms/documents on the case) | "300M+ Case Notes", comprehensive case notes | documentation tools | forms/assessments/notes | "strong documentation", electronic case files | **All 4 — core** |
| Upward/public accountability reporting | funder-ready, audit-ready; compliance officers | "comply with federal requirements", OAAPS | regulatory compliance, Care Act obligations | "meet mandates", service response windows, state/federal requirements | **All 4 — core** |
| Supervisor oversight of caseloads | program directors/leadership visibility | role-based collaboration | Manager worktrays | Supervisor Oversight (explicit) | **All 4 — core** |
| Money layer (billing/claims/budgets/charges) | $22.3B claims; budgeting tools | bill Medicaid; financial processing | personal budgets, contracts, payments, charges | (not foregrounded) | **3/4 — common, depth varies** |
| Client portal / self-service | Client Engagement Portal | (not foregrounded on fetched pages) | citizen access portals (integration copy) | "empower client self-service" | **3/4 — common** |
| Mobile / offline field work | mobile access (FAQ) | Mobile Assessments offline | Briefcase offline | remote work support | **4/4 — common, era-current** |
| Multi-program unification in one system | central positioning | central positioning | adults+children+education platform | modular cross-program sharing | **4/4 — dominant posture, not definitional** |
| AI assistance | Cara AI copilot | (AI elsewhere in suite) | FormFlow AI Assistant | (not foregrounded) | **2/4 — era-current, optional** |
| Specific program areas (aging/APS/economic/vocational…) | all listed as verticals | all listed as solutions | adult social care only | program areas listed | **variant axis — program-agnostic core** |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The served person/household of record** — persistent identified records for the people (with household/family context) who apply for or receive the agency's public social services. Remove → people registry/CRM.
2. **The public-program casework episode** — a case opened for a person under a government social-service program, gated by the agency's recorded determination of that person's eligibility/need against the program's public rules, assigned to an accountable caseworker, and carried through a tracked lifecycle (intake → assessment → determination → plan → service delivery → review → closure). Remove the public-program gate + government mandate → Nonprofit Case Management (org-defined programs, funder accountability); remove the episode container → eligibility engine with no casework memory.
3. **The documented casework record under public accountability** — dated, attributed notes, assessments, and service/authorization records accumulating on the case as the person's service history, reported upward to public oversight (compliance, audits, mandated reporting). Remove → empty case shells / task tracker; remove the public-accountability leg → private casework notes with no oversight loop.

Jointly-held load-bearing: 1 alone = contact database; 2 without 1 = workflow with no person model; 3 without 2 = activity log; 1+2 without 3 = empty case shells; 1+3 without 2 = client CRM with notes (pre-casework posture); 2+3 without 1 = anonymous task log.

### L1 — Common Mature Structure

- Assessment machinery (configurable forms/assessments; assessment designers)
- Service/care planning and service-delivery/authorization tracking (what is delivered, to whom, with what result)
- Supervisor oversight of caseloads, worktrays/work queues, deadlines
- Referral machinery (in and out; multi-agency contribution)
- Money layer: benefit-program linkage, billing/claims (Medicaid-class), personal budgets/charges (depth varies by regime)
- Reporting/analytics for oversight and funding bodies
- Role-based security and confidentiality of sensitive client data
- Client portal / self-service; document management; duplicate checking

### L2 — Variant / Optional Structure

- Program-area specialization (aging/disability, adult protective services, economic assistance, vocational rehabilitation, veterans, housing/homelessness, employment services) — the Type is program-agnostic; program areas are configuration, not structure
- Regime machinery: US federal/state program reporting (OAAPS-class), UK Care Act pathways/DoLS, Medicaid waiver billing, personal budgets vs claims vs grants — regional/regulatory variants
- Operator realization: government-operated vs government-commissioned provider administering public programs (context gradient; the public-program gate is the invariant, not the employer)
- Mobile/offline field capture; AI documentation assistance; citizen portals; multi-agency delegation portals; ombudsman/incident modules; HMIS integration

### L3 — Vendor-specific (Research Notes only)

- CaseWorthy: ClientTrack/ServTracker/MediSked application names; CORE data lakehouse; Cara AI copilot; apBuilder configurator; "Admin as a Service"; marketing stats (15M+ cases, $22.3B claims).
- WellSky: ClearCare integration; ombudsman module; SHIP Reporter; Resource Directory; "44 states"/"50% of AAAs" claims; Oklahoma/Georgia case studies.
- System C/Liquidlogic: FormFlow AI Assistant (with Microsoft); Briefcase offline; ContrOCC finance; Delegation Portal; worktrays naming.
- Northwoods: Grove (human case-aide service); module naming; "2 hours per worker per day" claims; program-area packaging.

## Vendor-specific Findings

See L3. None promoted to the canonical document except as de-branded illustrations of variants (e.g., personal budgets as a UK-regime finance depth variant; ombudsman complaint investigations as a program-area module).

## Boundary Findings

**1. vs Nonprofit Case Management (§25, processed) — JOINT REVIEW DISCHARGED from this side. Keep-both RATIFIED.** The casework spine (person records + bounded episode + documented record) is shared. The seam is the **operator + mandate line**: nonprofit CM's cases open under the organization's OWN defined programs with funder accountability; this Type's cases open under government social-service programs with eligibility/need determined against public rules and accountability to public oversight. Same-product straddles prove a context line, not a feature line: CaseWorthy sells one platform to both nonprofits and local/state governments; WellSky serves state agencies AND community-based organizations with the same machinery. Removal tests hold both directions: strip the public-program gate + public accountability → nonprofit casework remains; add them → this Type. Consistent with the nonprofit pass's prediction (keep-both, seam-defined siblings).

**2. vs Child Welfare Management (§24, processed) — JOINT REVIEW DISCHARGED from this side. Keep-both RATIFIED.** Child welfare is the statutory child-protection specialization: protected person is a minor, mandated-report screening, safety/risk assessment with legal force, out-of-home placement machinery, court-anchored permanency, need-to-know confidentiality. This Type's generic core requires none of those; its populations are adults and families in general (aging, disability, economic hardship). Vendor corroboration: Northwoods sells Traverse for Child Welfare as a separate program area from Traverse for Adults & Aging and Traverse for Economic Assistance — the vendor's own program-area line matches the Type line. Removal tests: strip the statutory protection loop + placement/permanency → this Type; add them → child welfare.

**3. vs Probation & Parole Management (§24, processed) — JOINT REVIEW DISCHARGED from this side. Keep-both RATIFIED.** The discriminator recorded by that pass holds: legal authority (court order/paroling release) + ordered conditions + sanction/revocation consequence machinery. This Type has supportive casework with eligibility/need determination but no legal authority, no ordered conditions, no sanctions/revocation path. Removal test: strip authority + conditions + consequences → supportive casework = this Type; add them → probation & parole.

**4. vs Public Sector Case Management (§24, unprocessed) — FLAG for that pass.** Generic government casework (intake → route → work → close) lacks the social-services person/household model and the eligibility/need determination against public program rules. Test: does the system know what a program eligibility determination is, and does it carry a served-person model with household context? If not → generic public sector case management.

**5. vs Public Benefits Management (§24, unprocessed) — FLAG for that pass.** Seam = case-centric vs program/benefit-centric. Here the eligibility determination happens INSIDE a person's casework episode and the case is the unit of record; benefit calculation/issuance/recertification at program scale (the benefit as the managed object) is Public Benefits Management territory. Corroboration from this side: Traverse's economic-assistance machinery is electronic-case-file-centric (applications/verifications/eligibility decisions in case files), not benefit-issuance machinery; WellSky's center is the care process even where it bills Medicaid.

**6. vs Housing Assistance Management (§24, unprocessed) — light note.** Per the affordable-housing pass's recorded note, voucher/assistance administration (caseload, not stock) sits inside the assistance-administration side; when run as casework under public program rules it is a program-area workflow variant of this Type. Operator-side property/stock management is the other Type. Flag left for that pass's joint review.

**7. vs Pastoral Care Management (§25, processed) — held from this side.** That pass recorded "eligibility/program/benefits machinery is the discriminator" — confirmed: the public-program eligibility/need determination machinery is definitional here and absent from pastoral care; large churches take case-like shapes (gradient, not wall).

**8. vs Immigration Case Management (§24, processed).** That Type adjudicates externally filed requests for immigration processes (decision made in the system); this Type delivers supportive services (no status adjudication). CaseWorthy lists "Immigration & Refugee Assistance" as a program area — settlement/assistance casework for immigrants is a program-area variant here, distinct from the immigration authority's adjudication machinery.

**9. vs Public Employment Service Platform (§24, processed).** PESP is labor-market intermediation (vacancy pool, jobseeker registration, placement). Employment/workforce services run as casework (Traverse "Workforce Programs"; CaseWorthy "Employment & Career") are a program-area variant of this Type when delivered as public casework; the intermediation platform is the other Type.

**10. vs Care Plan Management / Care Coordination (§22, health).** Health care plans are clinical/assessed-needs records without the public-program eligibility gate and public-accountability framing; the behavioral-health/I-DD verticals of this Type straddle toward health EHR (recorded by the nonprofit pass; same gradient observed here via CaseWorthy MediSked and WellSky IDD).

**"去掉什么就变成另一个 Type" 判据汇总**: remove the public-program gate + government mandate → Nonprofit Case Management; remove the casework episode (keep program-level eligibility + issuance) → Public Benefits Management; add statutory child-protection loop → Child Welfare Management; add legal authority + conditions + sanctions → Probation & Parole Management; remove the person/household + eligibility model → Public Sector Case Management; remove the person model → generic workflow tool; remove documentation → task tracker; remove public accountability → private casework notes.

## Historical / Market-Sample Check

- Paper-era county welfare office (conceptual check): a case folder — application form, eligibility determination (means test), caseworker's dated visit/contact notes, service authorizations/vouchers, closure summary, reports compiled for state/federal overseers — satisfies all three L0 legs at analog level. No cloud, no portals, no AI required.
- Paper-era UK adult social care: contact/referral record, needs assessment, care plan, home-care arrangements, charges ledger, committee/oversight reporting — satisfies the same three legs.
- Church/municipal alms and poor-relief records (person + assistance episode + visitation notes + overseer reporting) satisfy the core — matching the beneficiary pass's parallel church-registry check from the registry side.
- Conclusion: the L0 does not over-fit to the current SaaS, portal, AI-assisted market shape. The definition names no portals, no specific program areas, no billing machinery, no AI.

## Uncertainties

1. **No Tier-1 operational documentation reachable for any sampled product** — all direct evidence is Tier 2 official product pages (CaseWorthy support center, WellSky support hub, and System C customer centre exist but were not fetched / are login-gated). No exact case-state vocabularies, numeric limits, default values, or timing rules are asserted; the final document describes lifecycle and structures conceptually.
2. The precise object relationship between case, program enrollment, and eligibility determination inside products (one determination per case vs per program vs per benefit) is not verified; products likely differ.
3. The eligibility machinery's depth varies: Traverse's economic-assistance pole is documentation/workflow-centric (eligibility decisions recorded in case files), while dedicated eligibility-engine/benefit-issuance systems (Public Benefits Management territory) were not sampled — the seam is asserted structurally, pending that sibling's pass.
4. OLM Mosaic (the other major UK adult social care system) unreachable (transport error ×2); the UK pole rests on one vendor family (System C/Liquidlogic). Foothold AWARDS unreachable (403); the US Medicaid-funded human-services pole is evidenced indirectly through CaseWorthy MediSked and WellSky claims/billing copy.
5. Relative market weight of the poles (state agencies vs county departments vs commissioned providers vs mixed platforms) could not be quantified from accessible sources.
6. Whether any product population self-labels "social services case management" to the exclusion of "human services case management" was not tested directly; the market uses both labels plus "public sector/government case management" for the same machinery (CaseWorthy uses all three).
7. Non-US/EU regimes (Nordic/German municipal social services) not sampled; the jurisdiction-neutral framing is structural, corroborated only by the UK pole.

## Final Synthesis

Social Services Case Management is the government social-services agency's casework system of record. Its defining core is three jointly-held structures: the served person/household of record; the public-program casework episode (a case opened under a government social-service program, gated by a recorded eligibility/need determination against public program rules, assigned to an accountable caseworker, carried through a tracked lifecycle to recorded closure); and the documented casework record under public accountability (dated attributed notes/assessments/service records accumulating on the case, reported upward to public oversight). Around this core, mature products add configurable assessments, service/care planning with delivery and authorization tracking, supervisor oversight of caseloads, referral machinery, a money layer (benefit-program linkage, billing/claims, personal budgets/charges — depth varies by regime), reporting/analytics for oversight bodies, role-based security, client portals, and mobile/offline field capture. The Type is program-agnostic: aging/disability, adult protective services, economic assistance, vocational rehabilitation, housing assistance, and employment services are program-area configurations, not separate Types. The market realizes the Type at several poles — state-agency suites, county department casework, UK statutory adult social care, and multi-program platforms sold to both governments and commissioned providers. The Type is bounded by Nonprofit Case Management (org-defined programs vs public-program mandate), Child Welfare Management (statutory child-protection specialization), Probation & Parole Management (legal authority + conditions + sanctions), Public Benefits Management (case-centric vs benefit-centric, flagged), Public Sector Case Management (generic casework without the person/eligibility model, flagged), and the health care-plan family (no public-program gate).
