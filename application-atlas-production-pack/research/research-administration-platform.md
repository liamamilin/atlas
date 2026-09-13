# Research Notes — Research Administration Platform

Research date: 2026-09-09

## Research Goal

Understand what software in the "Research Administration Platform" category actually does: its core objects (proposal, award, fund, subaward, agreement), the pre-award and post-award workflows it digitizes, its users and interfaces, its rules and lifecycle behavior, and how it differs from adjacent Application Types (Research Grant Management, Research Information Management / CRIS, Research Funding Discovery, IRB / IACUC / Research Compliance, ERP grants accounting, Government Grants Management, Research Project Management).

## Initial Boundary

Working hypothesis before research:

- This Type is the research institution's administrative system of record for sponsored research: the system that carries a funding undertaking from proposal development through institutional approval and sponsor submission to award setup and post-award administration (funds, effort, subawards, modifications, closeout).
- Likely confusion sets:
  - **Research Grant Management** (adjacent directory leaf) — possibly the same product population under a different name; the market itself uses "grant management" and "research administration" interchangeably.
  - **Research Information Management / CRIS** — research information (publications, activities, expertise) vs funding administration.
  - **Research Funding Discovery Platform** — opportunity search vs administration.
  - **IRB / Research Ethics, Animal Research Ethics / IACUC, Research Compliance Management** — committee review machinery vs funding administration; often bundled in the same suites.
  - **Government Grants Management** — the sponsor/funder side of the same transaction.
  - **ERP / grants accounting** — post-award financial depth vs the research-language award view.
  - **Research Project Management** — managing the research work itself vs administering its funding wrapper.
- Unknowns going in: whether the pre-award loop is definitional or optional; how deep post-award financials go before becoming ERP territory; whether compliance modules are part of the Type or bundled siblings; regional (non-US) variants; whether standalone (non-suite) products dominate.

## Research Questions

1. What is the central object, and does it span pre-award and post-award as one record or two?
2. What does the pre-award loop look like (authoring, budgeting, routing, submission, post-submission follow-up)?
3. What does the post-award loop look like (award setup, funds/spend, effort, subawards, modifications, closeout)?
4. Who uses the system, in which roles, and what does each role see?
5. How do budgets work (rates, cost share, personnel)?
6. How does sponsor submission work (system-to-system? which sponsors?) and is it definitional or regional machinery?
7. Where do compliance touchpoints (COI, export control, protocol congruency) attach?
8. How do agreements (contracts, MTAs, NDAs) and internal funding fit?
9. Where are the boundaries with ERP financials, CRIS, funding discovery, and the sponsor-side systems?

## Representative Products

Sampled (direct evidence this pass):

1. **Cayuse** (Award Management solutions: Fund Finder, Proposals (S2S), Sponsored Projects, Fund Manager, Project Effort, Agreements, Insights; plus Compliance Management, Vivarium Management, Technology Transfer siblings) — commercial cloud suite; higher education, healthcare, life sciences, nonprofit, government; US origin with documented international operations (Canada, Ireland, UK, Middle East, APAC).
2. **Kuali Research** (Sponsored Programs, Internal Opportunities, Conflict Management, Export Control, Human/Animal/Biosafety Ethics Review, GrantRisk) — commercial cloud suite; higher education from R1 scale to emerging research programs; US origin with Canadian customers; configurable form/workflow platform philosophy.

Sampling rationale: both are current, marketed products with reachable official product pages; one Tier-1 help-center corpus reachable (Kuali). They differ in philosophy (Cayuse: pre-built deep lifecycle modules; Kuali: configurable forms/workflow platform) and both span pre-award through post-award, matching the dominant packaging of this market.

Attempted but not reachable (Source-access Limitation):

- **Huron Research Suite** — huronresearchsuite.com transport errors (also unreachable in the 2026-09-06 IACUC pass).
- **InfoEd Global** — infoed.org transport errors (also unreachable in the IACUC pass).
- **Worktribe** (UK research management) — worktribe.com 403 on both www and bare domain.
- **Aurora** (enterprise research administration) — aurora.org 403.
- **ResearchMaster** (Australia/NZ) — researchmaster.com.au timeout.
- **Grants.gov** (US sponsor-side portal, wanted for boundary context) — 403.

Sample skew note: both verified products are US-origin commercial suites sold to research institutions. Legacy on-prem vendors, institution-built systems, UK/EU regional vendors, and ERP-embedded grants modules are plausible parts of the market but unverified this pass. Cross-product claims below are calibrated accordingly.

## Sources

Tier 2 (official product pages):

- Cayuse — Sponsored Projects product page: https://www.cayuse.com/sponsored-projects/ (fetched 2026-09-09)
- Cayuse — Award Management overview: https://www.cayuse.com/award-management/ (fetched 2026-09-09)
- Cayuse — Proposals (S2S) product page: https://www.cayuse.com/award-management/proposals-s2s/ (fetched 2026-09-09)
- Cayuse — Fund Manager product page: https://www.cayuse.com/award-management/fund-manager/ (fetched 2026-09-09)
- Cayuse — The Cayuse Suite: https://www.cayuse.com/the-cayuse-suite/ (fetched 2026-09-09)
- Kuali — Research Administration overview: https://www.kuali.co/products/research (fetched 2026-09-09)
- Kuali — Sponsored Programs product page: https://www.kuali.co/products/sponsored-programs (fetched 2026-09-09)

Tier 1 (operational documentation):

- Kuali Help Center — "What is Kuali Research?" (module-by-module suite description): https://kuali.zendesk.com/hc/en-us/articles/27090467314075-What-is-Kuali-Research (fetched 2026-09-09)
- Kuali Help Center — "Navigating Kuali" (Action List, My Documents, suite navigation): https://kuali.zendesk.com/hc/en-us/articles/40899745658651-Navigating-Kuali (fetched 2026-09-09)

Source-access Limitation: vendor support portals requiring sign-in (Cayuse Support: https://support.cayuse.com — not fetched this pass) and five unreachable vendors (see above) mean no step-by-step operational manuals were observed for most of the market. All precise operational facts (exact routing steps, numeric validation counts, rate tables, form field taxonomies) are reported only as they appear verbatim on the reachable pages. No such detail was filled in from model memory. Claims that rest on a single product are marked product-specific.

## Product A — Cayuse

### Key observations (Evidence Layer A — directly observed on official pages)

- Positioning: "a comprehensive, cloud-based platform designed to streamline research administration. Our suite of connected apps covers the full research lifecycle, from proposal submission to funding management and protocol compliance." Award Management line: "Find, manage, and submit grants, proposals, funding, and effort—all in one place."
- Suite structure: Platform (centralizes task management, unifies user data, role-appropriate access) + Award Management (Fund Finder, Proposals (S2S), Sponsored Projects, Fund Manager, Project Effort, Agreements, Insights) + Compliance Management (Outside Interests/COI, Human Ethics, Animal Oversight, Hazard Safety, Risk & Compliance) + Vivarium Management + Technology Transfer.
- Sponsored Projects (the lifecycle hub): "Collaboratively manage research and grants from beginning to end"; "the central hub for research administrators, giving you full transparency into the entire research lifecycle"; "tracking project submissions from inception through close-out with clarity". Dashboard overview items: "Accounts, Awards, Personnel, Subawards, Tasks". Role-based dashboards for "administrators and PIs" with "instant access to the status, documents, and next steps for their projects".
- Routing: "Flexible, conditional routing automatically respects your organizational hierarchy and gives you complete control." Automated notifications "trigger review tasks or notifications to teams based on specific user roles". Central task manager with "clear records, linked attachments, and required reviews always organized and audit-ready".
- Smart forms: "Progressive logic and customer-configurable smart forms make the pre- and post-award processes smooth sailing for all stakeholders."
- Proposals (S2S): system-to-system federal submission — "Navigate interactive federal 424 submission forms, automatically filling common fields and validating entries"; "single submission portal for 30+ agencies"; "1,500 real-time validations"; "sensitive language detection for 700+ phrases"; "covers 100% of grant opportunities posted by NIH, NSF, AHRQ, CDC, NIFA, ONR, CDMRP, DoD, and other U.S. federal agencies"; "Full multi-project proposal functionality … for even the most complicated NIH grants"; "Manage, update, and escalate proposal budgets … copy over budgets to meet different agency requirements"; "Subaward creation and import functionality".
- Fund Manager (post-award financials): "Gain greater transparency and control over research funding, from sponsored research to institutional funds"; "future spending projections help track what's been spent and when a project is forecasted to hit zero"; "Connect with your existing Enterprise Resource Planning (ERP), General Ledger (GL), payroll, and eRA systems to reduce duplicate data entry"; "what-if scenarios with projections tools"; "financial summaries and P&L statements"; "Ensure you're following uniform guidance with one-stop transaction reviews in the user-friendly Fund Review tool"; funding types: "sponsored research, institutional funds, hard money, clinical income, and clinical trials"; "uses grants and contracts language, not accounting jargon".
- Project Effort: "import payroll and other relevant data for automated effort monitoring and certification, ensuring full compliance with federal effort certification and payroll verification mandates."
- Agreements: "consolidating all information related to your agreements in one central location, with visibility for both external and internal stakeholders to accelerate reviews with automated notifications."
- Insights: "on-demand access to centralized award data and trends, with role-specific dashboards."
- Market posture: serves "Higher Education, Healthcare, Life Sciences, Nonprofit, Government"; international page: "solutions approved for operations in Canada, Ireland, the United Kingdom, the Middle East, and the APAC region"; customer quotes from universities, academic medical centers, health systems.

## Product B — Kuali (Research suite / Sponsored Programs)

### Key observations (Evidence Layer A — directly observed on official pages and Tier-1 help center)

- Positioning: "our powerful, flexible, user-friendly research administration and compliance suite. Choose the individual products that meet your needs, or maximize your reach with our deeply-integrated suite." Category label in site navigation: "RESEARCH ADMINISTRATION".
- Suite products: Sponsored Programs, Internal Opportunities, Conflict Management, Export Control, Human Ethics Review, Animal Ethics Review, Biosafety Review, GrantRisk, Build for Research (no-code forms/workflow extension).
- Sponsored Programs ("The heart of your research enterprise") capabilities as marketed:
  - "Ease the burden for researchers with a streamlined proposal development experience … easy-to-navigate forms and embedded help."
  - "Gather the approvals you need with powerful, configurable workflow. Manage your team's workload with administrative tools and insights."
  - "Capture key award information, track changes over time, and integrate with your financial system for a seamless post-award process."
  - "Track negotiation activity, manage subawards, and create processes for NDAs, MTAs, and other types of agreements."
  - "It's not always about research. Training, public service, and other scholarly activities are important too. Keep everything in one place with our flexible solution."
- "What's in the box" (named data types):
  - **Sponsored Proposals** — "Create proposals, route them internally for review and approval, track their submission to the sponsor, and capture post-submission activities such as just-in-time and revised budget requests."
  - **Budget Creator** — "personnel salary data for named personnel combined with TBD positions and other direct costs, and with your organizational rates (IDC, fringe benefit, inflation, and more) automatically applied based on rate types and object code configurations for both requested and cost-shared funds."
  - **S2S** — "your researchers use the same, familiar interface whether the proposal requires S2S or not. We handle all the complexity."
  - **Negotiations** — "Capture data and track activities related to agreement negotiations, whether contracts, MTAs, NDAs, or other types of agreements."
  - **Awards** — "Establish a system of record for award information, including key award data, terms and conditions, and required deliverables. Manage changes over the life of an award, track account distributions, non-financial updates, and keep sponsor and internal award documents in a single location."
  - **Subawards** — "Track data related to outgoing subawards and link subaward records to the associated award. Track invoicing associated with outgoing subawards."
- Add-on pattern (institution-built extensions on the same platform): facility use application, researcher gift routing, no cost extension request, advance account request, PI eligibility form, equipment use form, notice of intent to submit proposal, project closeout form.
- Help-center module descriptions (Tier 1):
  - Internal Opportunities — "Establish and promote internal proposal opportunities and limited submission competitions, manage applications to those competitions, and distribute to review panels for selection and/or funding decisions."
  - Conflict Management — "Allow researchers to disclose their financial interests, outside professional activities, project sponsors, types of research, and completed training. Connect sponsored projects that are also captured in Kuali for easy access during review."
  - Export Control — "Track data and obtain organizational approvals related to export controlled projects including visa requests for international personnel and visitors, foreign travel requests … Integrate export control projects with pre- and post-award data, protocols, and conflict management records. Create Technology Control Plans and route through internal workflow."
- Platform navigation (Tier 1): **Action List** — "documents that require your action (Approve, Acknowledge, or complete a Task)"; **My Documents** — "all the documents you've initiated/saved or submitted in the system"; suite switcher; spaces for organizational units.
- Platform machinery: Form Designer, Workflow Builder ("Make form sections visible, hidden, or editable at a given workflow stop"), insights dashboards, "Shared configuration lets you keep track of sponsor, subawardee, and person data", "Deep integration with other parts of the Kuali suite", GraphQL APIs, "Sophisticated Group and Role Management", SaaS continuous delivery.
- Scale framing: "Whether you're an R1 concerned about scale and volume, a school with an emerging research program thinking about staffing levels and process improvement, or somewhere in between."
- Case-study framing: University of Baltimore "replaced paper-based research administration"; Western New England University "centralize pre-award … replacing fragmented email-based workflows".

## Cross-product Comparison

| Dimension | Cayuse | Kuali | Read |
|---|---|---|---|
| Central object | Sponsored project spanning proposal → award → closeout ("inception through close-out") | Sponsored Proposals + Awards as linked records ("system of record for award information") | Common |
| Pre-award authoring by researcher | Smart forms, progressive logic | Streamlined proposal development, guided forms, embedded help | Common |
| Budget development | Budget tracking, escalation, copy across agency requirements | Budget Creator: personnel salary, TBD positions, direct costs, organizational rates (IDC, fringe, inflation), requested + cost-share | Common (Kuali detail deeper on page) |
| Institutional routing/approval | "Flexible, conditional routing automatically respects your organizational hierarchy" | "Gather the approvals you need with powerful, configurable workflow"; Action List (Approve/Acknowledge/Task) | Common |
| Sponsor submission | Proposals (S2S): federal system-to-system, 30+ agencies, 424 forms | S2S module; "same, familiar interface whether the proposal requires S2S or not" | Common (US-federal machinery; both treat non-S2S submission as normal) |
| Post-submission follow-up | Tracked in Sponsored Projects | "just-in-time and revised budget requests" | Common |
| Award record | Awards + Accounts on dashboard; Fund Manager as fund view | Awards: key data, terms & conditions, deliverables, anticipated/obligated amounts, account distributions, documents | Common |
| Post-award financials | Fund Manager: spend tracking, projections, what-if, P&L, transaction review; ERP/GL/payroll integration | "integrate with your financial system for a seamless post-award process" | Common (Cayuse depth deeper on page; Kuali delegates ledger to institutional finance system) |
| Effort reporting | Project Effort (payroll import, certification) | Not observed on fetched pages | Product-specific-leaning; treat as Common-Optional |
| Subawards | Dashboard item; subaward creation/import in proposals; Fund Manager oversight | Subawards: outgoing subawards linked to award, invoicing | Common |
| Agreements/negotiations | Agreements module (centralized agreement info) | Negotiations (contracts, MTAs, NDAs) | Common |
| Compliance touchpoints | Separate Compliance Management line (COI, IRB, IACUC, IBC) on same platform | Sibling products (Conflict Management, Export Control, Ethics Reviews) integrated with pre-/post-award data | Common (packaged as sibling modules, not the core) |
| Internal funding | Fund Manager covers "institutional funds, hard money" | Internal Opportunities (internal competitions, limited submissions, review panels) | Common (different realizations) |
| Dashboards/analytics | Role-based dashboards; Insights | Insights dashboards; document dashboard | Common |
| Configurability | "Fully configure flexible workflows"; customer-configurable smart forms | Form Designer + Workflow Builder; configurable forms & workflow | Common |
| Role model | Role-based dashboards, role-triggered tasks | Group and Role Management; role-scoped access | Common |
| Non-research scholarly work | (not itemized on fetched pages) | "Training, public service, and other scholarly activities … keep everything in one place" | Common-Optional |
| Suite packaging | Suite of connected apps + Platform layer | Suite of products + Build extension | Common |
| Deployment | Cloud SaaS | Cloud SaaS, continuous delivery | Common in sample |
| Regional reach | Approved for Canada, Ireland, UK, Middle East, APAC | Canadian customers visible in logo wall | Common (regime machinery unverified) |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

1. **The sponsored project as the institution's record of record** — a persistent, identified record of one research funding undertaking, binding the institution's proposed/awarded research to an external sponsor and to money terms; it spans the pre-award phase (the proposal — what is requested) and the post-award phase (the award — what was committed), with the award linked back to the proposal it resulted from. Remove → a generic project tracker, a document store, or a bare award registry.
2. **The institutional pre-award loop** — the proposal is assembled by the researcher/team in structured forms, budgeted under the institution's rate and cost rules, routed through the institution's review/approval hierarchy, submitted to the sponsor, and followed up (post-submission requests, revised budgets) through the same record. The institution, not the individual, is the submitting party. Remove → the sponsor's own application portal, or a word processor + email chain; the institutional gate is what disappears.
3. **The post-award administration loop** — the accepted award is set up as the institution's funded record (terms, deliverables, amounts, account distributions); spend is tracked against it in research language (with the institutional finance systems as the transaction substrate), personnel commitments/effort are administered against it, subawards are issued and invoiced under it, and changes over the award's life (amendments, extensions, rebudgeting) are recorded on it, through to closeout. Remove → a proposal pipeline with no award memory, or pure grants accounting inside an ERP.

Jointly-held load-bearing analysis:

- 1 alone = award registry / project list
- 2 without 1 = a submission tool with no memory
- 3 without 1+2 = grants accounting (ERP territory)
- 1+2 without 3 = pre-award pipeline only (proposal tooling)
- 1+3 without 2 = post-award-only administration
- 2+3 without 1 = approval workflow + accounting with no project identity

Historical/market-sample check: the paper-era research office — proposal file with budget worksheets and rate sheets, routing sheet with signatures, award letter filed, account set up in the ledger, subaward agreements, effort/payroll certification forms, closeout file — satisfies all three legs with no software. Legacy on-prem "electronic research administration" systems (the eRA generation) satisfy the same structure. Regional regimes (UK full-economic-costing proposals, EU framework-programme proposals, Canadian/Canadian-style agency workflows) realize the same loop with different sponsor machinery — the L0 therefore names no specific sponsor portal, no S2S protocol, no US federal forms, and no effort-certification mandate. Cayuse's own international posture (approved for Canada, Ireland, UK, Middle East, APAC) and Kuali's treatment of S2S as an optional interface ("whether the proposal requires S2S or not") support keeping those out of the invariant.

### L1 — Common Mature Structure (both sampled products agree unless noted)

- Structured proposal forms with progressive logic / guided authoring and embedded help for researchers.
- Budget development as rate-governed computation: personnel salary data, TBD positions, other direct costs, institutional rates (indirect/F&A, fringe benefit, inflation), cost share alongside requested funds.
- Configurable institutional routing/approval workflows that mirror organizational hierarchy; conditional routing; role-triggered tasks and notifications.
- A personal action list / worklist of documents awaiting the user's action (approve, acknowledge, complete task), and a personal "my documents" view.
- Award record as system of record: key award data, sponsor terms and conditions, required deliverables, anticipated/obligated amounts, account distributions, sponsor and internal documents.
- Post-award financial view in research language: spend vs budget, projections/what-if forecasting, spend-down management, summaries for stakeholders; integration with ERP/GL/payroll systems as the transaction substrate.
- Outgoing subawards linked to the prime award, with subaward invoicing tracked.
- Agreement/negotiation tracking for contracts, MTAs, NDAs adjacent to awards.
- Compliance touchpoints attached to the project record: conflict-of-interest/financial-interest disclosure, export-control review, protocol links (human/animal/biosafety) — realized as sibling modules integrated with pre-/post-award data.
- Role-based dashboards and cross-portfolio reporting/analytics for administrators; self-service status for PIs.
- Shared person/sponsor/subawardee master data across modules.
- Audit-readiness posture: linked attachments, approval histories, retained records.
- Suite integration platform layer (unified tasks, user data, APIs) when sold as a suite.

### L2 — Variant / Optional Structure

- Packaging: full suite vs single products vs institution-built extensions on the platform (Kuali add-on pattern) vs ERP-embedded grants modules (unverified this pass).
- Sponsor-submission machinery: US federal system-to-system (Grants.gov-class agency portals, multi-project NIH proposals, federal form sets) — regional machinery, not definitional; non-S2S submission is a first-class path in both sampled products.
- Effort reporting/certification: explicit at Cayuse (payroll import, certification, tied to federal mandates); not observed on Kuali's fetched pages — Common-Optional, region-dependent.
- Funding-type breadth: sponsored research, institutional funds, hard money, clinical income, clinical trials (Cayuse Fund Manager); internal competitions/limited submissions (Kuali Internal Opportunities); gift routing (Kuali add-on).
- Regional regime packaging: US federal uniform-guidance artifacts vs UK/EU/Canada/APAC regimes (Cayuse international approvals; regime-specific machinery unverified in detail).
- Non-research scholarly activity administration (training, public service) alongside sponsored research (Kuali).
- Institution scale and office structure: R1 volume vs emerging programs; centralized vs decentralized research offices (Cayuse case-study framing).
- Clinical/industry-funded billing flows inside the fund view (Cayuse funding types).
- Configuration philosophy: pre-built deep lifecycle modules vs configurable form/workflow platform.

### L3 — Vendor-specific Structure (kept out of final document)

- Cayuse: module names (Sponsored Projects, Fund Manager, Project Effort, Proposals (S2S), Fund Finder, Agreements, Insights, Outside Interests, Hazard Safety, Vivarium Operations/Vet Care/Schedules, Inventions), Cayuse Platform / Report Connector, marketing metrics ($45.3B federal funding processed in 2025, 99.9% first-time submission success, 67% review-time reduction, "1,500 real-time validations", "700+ phrases" sensitive-language detection, "30+ agencies"), customer names/testimonials (LSU Health Shreveport, High Point University, Stephen F. Austin, Texas A&M, UCLA Medical Center, Denver Health, Providence, University of Melbourne, Oakland University, OSU-CHS).
- Kuali: module names (Sponsored Programs, Internal Opportunities, GrantRisk, Build for Research), "The heart of your research enterprise" tagline, Kuali Build add-on catalog items, GraphQL APIs, Spaces/Suite Switcher navigation specifics, institutional branding feature, customer names (University of Maryland, UC San Diego, Kent State, Utah State, UA Huntsville).
- Unreachable-vendor context: Huron Research Suite, InfoEd, Worktribe, Aurora, ResearchMaster — existence plausible from market knowledge but unverified this pass; no claims made.

## Vendor-specific Findings

See L3. Additional product-specific observations that must not generalize:

- Only Cayuse's fetched pages document effort reporting/certification as a named capability (Project Effort).
- Only Cayuse's fetched pages document the fund-level financial view depth (what-if projections, P&L statements, transaction review tool, named funding types including clinical income and clinical trials).
- Only Kuali's fetched pages document internal funding competitions (Internal Opportunities) and the add-on form catalog (no-cost extension request, PI eligibility, notice of intent, project closeout form).
- Only Kuali's Tier-1 help center documents the Action List / My Documents navigation model verbatim.
- Only Cayuse documents S2S depth (agency coverage, multi-project proposals, budget copy across agency requirements).

## Boundary Findings

- **Research Grant Management** (adjacent directory leaf): the sampled population self-describes with both labels — Cayuse's page titles are "Grant Management Software | Research Lifecycle Management" and "Pre-Award & Post-Award Grant Management Software", while its category narrative is "research administration"; Kuali's category is "Research Administration" with the product named "Sponsored Programs". The two directory leaves appear to describe substantially the same product population; this pass defines Research Administration Platform as the institution-wide platform spanning the full sponsored-research lifecycle (pre-award through post-award administration, with compliance touchpoints and agreements). Taxonomy issue recorded for STATUS.md; a joint review is recommended when Research Grant Management is processed.
- **Research Information Management / CRIS**: CRIS centers on the institution's research information (publications, activities, expertise, outputs); this Type centers on the funding undertaking. Integration point: awards feed research-information systems (funding metadata attached to outputs). Boundary test: remove the proposal/award/money machinery and what remains (publications, profiles) is CRIS, not this Type.
- **Research Funding Discovery Platform**: opportunity search is a bundled capability here (Cayuse Fund Finder sits inside Award Management), not the defining structure. Funding-discovery products hold opportunity databases without proposal/award records. Boundary test: remove proposal/award records → funding discovery.
- **IRB / Research Ethics Management, Animal Research Ethics / IACUC, Research Compliance Management**: committee-review machinery over protocols vs funding administration over sponsored projects. Both sampled vendors ship the compliance side as sibling products integrated with pre-/post-award data (Kuali help center: "Connect sponsored projects … for easy access during review"; "Integrate export control projects with pre- and post-award data, protocols, and conflict management records"). Boundary test: remove the money/proposal/award machinery → compliance committee platform.
- **Government Grants Management** (and sponsor-side portals such as Grants.gov-class systems): the sponsor side of the same transaction — the funder's intake, review, and award machinery. This Type is the grantee institution's side. The proposal crosses between them. Boundary test: whose record of record is it — the funder's opportunity/applications or the institution's undertaking?
- **Grantmaking Platform / Nonprofit Grant Management**: funder-side foundations (grantmaking) and nonprofit program-grant administration respectively. The research-administration center is the sponsored research project with research-specific machinery (effort, subawards, sponsor terms, research compliance touchpoints); nonprofit grant management centers on program delivery funded by grants. Adjacent, not identical.
- **ERP / Financial Management (grants accounting)**: the ledger of transactions lives in institutional finance systems; this Type holds the award/fund view in research language and integrates with ERP/GL/payroll (Cayuse Fund Manager explicitly "Connect with your existing ERP, GL, payroll, and eRA systems"; Kuali "integrate with your financial system"). Boundary test: if the system's center is the chart of accounts and ledger postings rather than the sponsored project, it is ERP territory.
- **Research Project Management**: managing the research work itself (scientific tasks, milestones, progress) vs administering the funding wrapper around it. Different central object.
- **CTMS**: clinical trial conduct management vs the funding/administration wrapper (clinical trials appear here as a funding type in Cayuse Fund Manager). Different object and regime.

## Uncertainties

1. Market breadth: only two products verified this pass, both US-origin commercial suites. Legacy on-prem vendors (Huron, InfoEd), UK/EU regional vendors (Worktribe), institution-built systems, and ERP-embedded grants modules are plausible but unverified; claims calibrated to "the researched sample" and "commonly".
2. Operational depth (exact routing step taxonomies, form field structures, rate-table mechanics, validation catalogs, closeout checklists) — not observed; support portals were not fetched. Final document avoids precise operational claims.
3. Whether effort reporting is universal in the category (explicit only at Cayuse within the sample) — kept Common-Optional.
4. Regional regime machinery (UK fEC/TRAC, EU Horizon, Canadian agency workflows) — asserted only at the level of vendor international-operations statements; no regime-specific workflow detail verified.
5. The exact relationship between this leaf and the Research Grant Management leaf (alias vs narrower slice) — unresolved; recorded for joint review.
6. Sponsor-side systems (Grants.gov, Research.gov, agency portals) — wanted for boundary context; Grants.gov returned 403; boundary reasoning rests on the grantee-side evidence plus the S2S interface descriptions.

## Final Synthesis

The Application Type is best modeled as: **the research institution's administrative system of record for sponsored research**. One central object — the sponsored project — carries the entire administrative lifecycle: proposed by the researcher in structured, budget-computed forms; routed through the institution's approval hierarchy as the institution's own submission; converted into an award record holding sponsor terms, deliverables, amounts, and account distributions; then administered for the life of the award — spend tracked against budget in research language over the institutional finance substrate, personnel commitments and (where mandated) effort certified, subawards issued and invoiced, agreements negotiated, modifications recorded, and everything carried to closeout in an audit-ready state.

Around this loop, mature products add: rate-governed budget engines, system-to-system sponsor submission (regional machinery), compliance touchpoints (COI, export control, protocol congruency) realized as integrated sibling modules, internal-fund and agreement administration, role-scoped dashboards and analytics, and a platform layer unifying tasks, person/sponsor master data, and APIs.

The Type's identity is neither "a grant form tool" nor "an accounting module": the defining discriminator is that the institution — not the individual researcher — is the administering party, and the sponsored project is the durable record through which the institution gates what goes to sponsors, then administers what sponsors gave, from inception to closeout.
