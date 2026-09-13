# Research Notes — Research Grant Management

## Research Goal

Determine what "Research Grant Management" products actually are, and — per the TAXONOMY FLAG left by the processed sibling pass **research-administration-platform** (2026-09-09) — run the **alias-vs-narrower-slice test**:

> if its sampled population is the same pre-award→post-award lifecycle, alias resolution with this leaf is the likely outcome; if it samples a narrower grant-lifecycle slice or a different population, document the seam.

Secondary goals: establish the Type's core model from direct product evidence, hold the seams the sibling listed (funder side, ERP substrate, CRIS, funding discovery, compliance siblings, project management, nonprofit grant management), and check the definition against older / non-US-regime products.

## Initial Boundary

Working hypothesis before research:

- Research Grant Management = software used by research institutions (universities, teaching hospitals, research institutes) to manage the grants they **receive** — from finding opportunities and preparing proposals, through award acceptance, to spending the money and closing out.
- The institution is the grantee; the sponsor/funder is external. This is the **recipient side** of the funding transaction.
- Nearest neighbors:
  - **Research Administration Platform** (§23 sibling, processed) — likely the same population (the flag).
  - **Grantmaking Platform** — funder side (foundations giving money out).
  - **Government Grants Management** — sponsor side (government agencies awarding).
  - **Nonprofit Grant Management** — grantee side but for program delivery, not research.
  - **Research Funding Discovery Platform** — opportunity databases without award records.
  - **Research Information Management / CRIS** — research information (publications, expertise), not funding administration.
  - **ERP / grants accounting** — the ledger substrate beneath the award view.
  - **Research Project Management** — the research work itself, not the funding wrapper.
- Unknowns: whether a distinct "grant-management-only" (e.g., post-award money only) product population exists; whether regional (UK/EU/AU) products differ structurally; whether PI-facing personal grant trackers form a population.

## Research Questions

1. What objects exist in these systems, and what is the unit of record?
2. What lifecycle does a grant carry in the system (phases, states, terminal events)?
3. Who operates the system — administrators, PIs, approvers, finance offices — and what does each do?
4. **Alias test**: is the sampled population the same as research administration's? Does lexical evidence run both directions?
5. **Narrower-slice test**: is there a product population doing only part of the grant lifecycle (e.g., post-award money only) under the "grant management" name?
6. Where does money live — in this system or in the institutional finance systems?
7. Which capabilities are definitional vs common vs regime-dependent vs vendor-specific?

## Representative Products

Selected for market position + documentation reachability + independence from the sibling's sample where possible:

| Product | Why selected | Reachability |
|---|---|---|
| **Cayuse** (Award Management line) | market-leading US suite; the sibling sampled it — re-fetched here for the grant-management-labeled page (lexical evidence) | fetched 2026-09-09 |
| **Kuali Research** (Sponsored Programs) | second US suite; sibling sampled it — re-fetched here incl. Tier-1 help-center article | fetched 2026-09-09 |
| **InfoEd Global** (Grants & Contracts suite) | **fresh sample** — the sibling could not reach it; self-labels "research administration" while its product pages are named "grant management" — the strongest both-directions lexical evidence | fetched 2026-09-09 |

Attempted and unreachable (abandoned after 1–2 failures each, per network rules): Huron Research Suite (transport error ×2), Worktribe (403 ×2), Streamlyne Research (transport error ×2), ResearchMaster AU (timeout). Aurora not attempted after three same-market failures. Consequence: the verified sample is three US-origin commercial suites; market-breadth claims are calibrated accordingly.

## Sources

All fetched 2026-09-09 directly from vendor surfaces:

- Cayuse — Award Management page (page title "Pre-Award & Post-Award Grant Management Software"): https://www.cayuse.com/award-management/
- Kuali — Research Administration product page: https://www.kuali.co/products/research
- Kuali Help Center — "What is Kuali Research?" (Tier-1): https://kuali.zendesk.com/hc/en-us/articles/27090467314075-What-is-Kuali-Research
- InfoEd Global — homepage: https://www.infoedglobal.com/
- InfoEd Global — Pre-Award Grants Management: https://www.infoedglobal.com/products/pre-award-grants-management/
- InfoEd Global — Post-Award Grants Management: https://www.infoedglobal.com/products/post-award-grants-management/
- InfoEd Global — Grants & Contracts suite: https://www.infoedglobal.com/products/grants-and-contracts/
- InfoEd Global — SPIN Global Suite: https://www.infoedglobal.com/products/spin-global-suite/

Sibling-pass sources (2026-09-09, recorded in research/research-administration-platform.md): Cayuse Sponsored Projects / Award Management / Proposals S2S / Fund Manager / Suite pages; Kuali Research product + Sponsored Programs pages + two help-center articles.

## Product A — Cayuse (Award Management line)

### Key observations (evidence layer A unless noted)

- **Self-labeling runs both directions on one page.** Browser title: "Pre-Award & Post-Award Grant Management Software". H1: "Award Management Software". Subhead: "Manage the full grant lifecycle from pre-award to post-award in one integrated system." Suite narrative (nav): "streamline research administration… covers the full research lifecycle, from proposal submission to funding management and protocol compliance." Benchmark report titled "The 2026 State of Grant and Research Management Benchmark Report."
- **Capability set** (the page's own taxonomy): Funding Search (Fund Finder) → Grant Proposal Management (Proposals S2S: "interactive federal 424 submission forms, automatically filling common fields and validating entries") → Research Lifecycle Management (Sponsored Projects: "proposal and grant administration, tracking project submissions from inception through close-out") → Agreement Management (Agreements: "consolidating all information related to your agreements in one central location") → Grant Financial Management (Fund Manager: "from sponsored research to institutional funds… multi-year projects… track what's been spent and when a project is forecasted to hit zero") → Effort Reporting (Project Effort: "import payroll and other relevant data for automated effort monitoring and certification") → Reporting & Analytics (Insights: "role-specific dashboards").
- **Lifecycle language**: FAQ answers "How do Cayuse's solutions support the pre-award to post-award grant lifecycle?" — "Centralizing award and subaward management… track progress, budgets, and expenses across pre-award and post-award workflows."
- **Routing/approval as a first-class mechanism**: "Digital routing and approval workflows for proposals, contracts, and effort reporting… traceable digital histories of approvals and correction requests."
- **Audiences**: academic institutions, healthcare organizations, research nonprofits, life sciences organizations, government institutions; international operations documented for Canada, Ireland, UK, Middle East, APAC.
- Marketing metrics on the page (vendor claims, layer A but promotional — not promoted to structure): "1,500 smart validations", "99.9% first time successful submission rate", "50% faster proposal completion", "spend-to-zero performance on 75% of awards".

## Product B — Kuali Research

### Key observations

- **Category naming**: product page title "Kuali Research | Streamline Research Administration"; H1 "SOFTWARE FOR THE FUTURE of Research administration"; nav category "RESEARCH ADMINISTRATION"; the sponsored-programs product is the grant side of it.
- **Suite composition** (product page): Sponsored Programs + Conflict Management + Human Ethics Review + Animal Ethics Review + Biosafety Review + Internal Opportunities + Export Control + Kuali Build (no-code extension). Compliance modules are siblings of the grant product, not the grant product itself.
- **Tier-1 help-center article "What is Kuali Research?"** describes Sponsored Proposals:
  - "Create proposals, route them internally for review and approval, track their submission to the sponsor, and capture post-submission activities such as just-in-time and revised budget requests."
  - Budget creator: "makes use of your personnel salary data for named personnel combined with TBD positions and other direct costs, and with your organizational rates (IDC, fringe benefit, inflation, and more) automatically applied based on rate types and object code configurations for both requested and cost-shared funds."
  - Agreements: "Capture data and track activities related to agreement negotiations… often also used to track MTAs, NDAs, and other, similar types of agreements."
  - Award: "Establish a system of record for award information, including key award data, terms and conditions, and required deliverables. Track and manage changes in anticipated and obligated award amounts over the life of an award, track account distributions, non-financial updates, and keep sponsor and internal award documents in a single location."
  - Subawards: "Record data and documentation related to outgoing subawards and link subaward records to the associated award. Manage subaward invoices."
  - Internal Opportunities: "internal proposal opportunities and limited submission competitions… distribute to review panels for selection and/or funding decisions."
- **Grant-management vocabulary in the vendor's own white paper** (listed on the product page): "Grant Administrator Onboarding Guide… Administrators manage the grant lifecycle: pre-award proposals, award setup, and post-award compliance."
- **Institutional extensibility examples** (product page): facility use application, researcher gift routing, no-cost extension request, advance account request, PI eligibility form, equipment use form, notice of intent to submit proposal, project closeout form — the institution extends the grant record's workflow with local forms.

## Product C — InfoEd Global

### Key observations

- **Both names on the same pages, explicitly equated.** Homepage title: "Electronic Research Administration Software"; H1: "The World's Leading Research Administration Software"; "eRA Software Systems for Universities, Institutions, and Corporations". Product menu: "Pre Award Grants Management Software" and "Post Awards Grant Management". Pre-award page: "InfoEd Global's sponsored projects eRA system helps institutions manage their Grants and Contracts portfolio through the entire lifecycle from Pre-award Grants through to Post-Award Grant Management." The same sentence contains "eRA system", "Grants and Contracts portfolio", and "Grant Management".
- **Suite composition**: SPIN Global Suite (funding opportunities), Pre-Award, Post-Award, Research Compliance, Clinical Trials, Animal Facilities, Research Outputs, Technology Transfer; "over 20 tightly integrated modules"; "Built and improved upon by research experts for over 30 years" (vendor longevity claim).
- **Pre-award machinery** (product page):
  - Proposal Development: "Web-based, online portal for preparing applications for any sponsor including US Federal agencies accepting applications through Grants.gov. All agencies and forms are supported for system-to-system (S2S) submission." "Collect applications for internal funding/limited submission competitions." "Multiple users can simultaneously access the application record to link personnel, build budgets, upload documents."
  - Auto-population: institutional data (UEI, EIN); stored profile info and "current COI case status" when personnel are added; "Human, animal, or environmental safety research protocols can easily be linked to proposals to display real-time status information."
  - Validation: "Automated data checking to confirm electronic submission/S2S applications conform with Grants.gov requirements. Integrated with NIH's pre-submission validation web service."
  - Budgets: "automatically calculates fringe benefits, applies inflation, determines F&A, tracks cost sharing… Multiple budget versions can be saved."
  - Routing: "Electronically route proposals for internal review via pre-defined pathways that can automatically recognize and adapt to proposal-specific criteria such as inclusion of human research participant activity meriting IRB notification."
  - Sub-awards: "Sub-awards and subprojects are fully supported. Sub-recipient risk analysis and sub-recipient monitoring features are included with our Entity Management module."
- **Post-award machinery** (product page):
  - Post Award Management module: "creating and tracking awards. Copy requested budgets when appropriate or record award budgets manually"; "all types of external or internal awards with support for personnel and non-personnel direct costs, indirect costs (F&A), subprojects, and sub-awards"; "view and manage awards and accounts on a grant year basis"; "Track award terms and conditions using a customizable database of standard terms"; "View award and expenditure data sorted by general ledger account codes or by common sponsor budget category labels."
  - Post-award requests: "pre-award/at risk spending, change of PI or other key personnel, and re-budgeting adjustments."
  - Finance integration: "Publish award data to your institutional financial system to facilitate account setup and retrieve expenditure data"; "Track informal 'soft' encumbrances on award accounts"; "Automatically spawn F&A transactions and publish those to the financial system."
  - Deliverables/payments: "Establish and track deliverables, scheduled payments, and milestones"; "View payables, receivables, aging… generate invoices using customizable templates"; "Analyze expenditures, forecast future expenses, and perform re-budgeting."
  - Companion modules named "in concert with": Conflicts of Interest, Agreements/Negotiations, Current/Pending Support, Time & Effort.
- **Grants & Contracts suite page** (the module both grant-management pages point into):
  - "For over 30 years, principal investigators and research administrators have been relying on the InfoEd Grants and Contracts Suite to automate and streamline every step of Grants and Awards management."
  - SPIN: "approximately 40,000 funding opportunities across thousands of governments, foundations, and commercial entities"; SMARTS automated matching/notifications; "Create a proposal directly from SPIN search results."
  - Pre-award core functions: funding opportunities → proposal development → "Comprehensive routing utilities support web-based processing of proposals for internal review and approval with electronic signature tracking" → sponsored projects tracking ("Additional post-submission information, just-in-time materials and award notices can be tracked").
  - Post-award core functions: "Upload and process Notice of Award and enter offered award budget information"; "Manage budget revisions, monitor sub-awards, and manage/track project deliverables. Automatically generate new grant accounts in institutional financial system based on final approved award budgets"; "Import and display expenditure data from institutional financial system."
  - Financial Tracking: "automatically routes and matches Sponsor accounts to institutional financial accounts using the sponsor rules and reporting requirements."
  - Lifecycle span: "From the Notice of Award through closeout, the InfoEd Post-Award Solution simplifies the complexities and provides complete support of post-award management of grants and contracts."

## Cross-product Comparison

| Structure | Cayuse | Kuali | InfoEd | Reading |
|---|---|---|---|---|
| One sponsored-project record spanning proposal → award | Sponsored Projects ("inception through close-out") | Sponsored Proposals + award system of record, linked | Proposal Development → Proposal Tracking → Post Award ("data flows seamlessly from Pre-award to Post Award") | **Core** (3/3) |
| Institutional routing/approval gate before submission | "digital routing and approval workflows for proposals" | "route them internally for review and approval" | "routing utilities… internal review and approval with electronic signature tracking"; pathways adapt to criteria (IRB trigger) | **Core** (3/3) |
| Budget computed under institutional rules | budget tools in Sponsored Projects; Fund Manager forecasting | budget creator: salary data + TBD positions + org rates (IDC, fringe, inflation), requested + cost-share | "automatically calculates fringe benefits, applies inflation, determines F&A, tracks cost sharing"; multiple versions | **Core** (3/3) |
| Sponsor submission machinery | Proposals S2S (federal 424 forms, validations) | submission tracked; S2S implied by "track their submission to the sponsor" | Grants.gov S2S "all agencies and forms"; NIH validation service | Common; **regime-dependent depth** (US federal heaviest) |
| Award as system of record (terms, deliverables, amounts, distributions) | Fund Manager + award data in Insights | explicit "system of record for award information… anticipated and obligated amounts… account distributions" | Notice of Award processing; terms database; grant-year accounts | **Core** (3/3) |
| Spend view in research language over finance integration | Fund Manager ("what's been spent… forecasted to hit zero") | dashboards/views; financials integration via platform | expenditure import; burn rate; sponsor↔institutional account mapping; soft encumbrances | **Core** (3/3); depth varies |
| Subawards linked to prime award | "award and subaward management" | "link subaward records to the associated award. Manage subaward invoices" | sub-awards/subprojects; sub-recipient risk analysis & monitoring | **Core** (3/3) |
| Agreements / negotiations | Cayuse Agreements (contracts; central location) | agreements module; MTAs/NDAs | Agreements/Negotiations module | Common (3/3) |
| Effort / payroll commitment | Project Effort (payroll import, certification) | effort in sibling products (per sibling pass) | Time & Effort module | Common; **regime-dependent** |
| Compliance touchpoints on the grant record | compliance line beside Award Management | COI/ethics/export siblings; COI status auto-populated into proposals (per help article) | COI case status auto-populated; protocols linked real-time; IRB-triggered routing | Common (3/3); realized as sibling modules |
| Funding-opportunity search bundled | Fund Finder | (not on the research page; sibling pass noted it absent there) | SPIN + SMARTS, proposal creation from search results | Optional/bundled (2/3) |
| Internal funding competitions | (not observed on fetched page) | Internal Opportunities module | "internal funding/limited submission competitions" | Optional (2/3) |
| Post-award change management (rebudget, reassign, extend) | Fund Manager oversight; workflows | "changes in anticipated and obligated award amounts"; no-cost extension form example | re-budgeting, change of PI, pre-award/at-risk spending, no-cost extensions | **Core** (3/3) |
| Closeout as named phase | "inception through close-out" | project closeout form (institution-built example) | "From the Notice of Award through closeout" | Common (3/3, one via extension example) |
| Role-scoped analytics/dashboards | Insights (role-specific dashboards) | insights dashboards, document dashboard | ad-hoc reporting + BI, security-embedded | Common (3/3) |

## The Alias Test (vs Research Administration Platform)

The sibling pass defined **Research Administration Platform** as "the institution-wide platform spanning the full sponsored-research lifecycle (pre-award through post-award administration + compliance touchpoints + agreements)" and flagged this leaf for the alias-vs-narrower-slice test. Results from this pass's independent evidence:

### 1. Same population

All three products fetched here are the same systems the sibling pass (and the market) calls research administration:

- **Cayuse**: one page carries both names — title "Pre-Award & Post-Award Grant Management Software" vs suite narrative "streamline research administration". The sibling sampled the same vendor's Sponsored Projects/Fund Manager pages as research administration.
- **Kuali**: category "Research Administration"; the grant product is "Sponsored Programs"; the vendor's own white paper describes administrators managing "the grant lifecycle: pre-award proposals, award setup, and post-award compliance".
- **InfoEd**: homepage self-label "The World's Leading Research Administration Software"; product pages "Pre-Award Grants Management Software" / "Post Award Grants Management Software"; one sentence equates them: "sponsored projects eRA system… from Pre-award Grants through to Post-Award Grant Management."

Lexical evidence runs **both directions in all three products** — the strongest form of alias evidence available short of a vendor statement of equivalence.

### 2. Same structure

This pass's independent sample reached the same core the sibling documented: a sponsored-project record spanning proposal and award; an institutional pre-award loop (assemble → budget → route → submit); a post-award administration loop (set up → funds/effort/subawards → changes → closeout). No structural element was found in this sample that the sibling's core model lacks, and none in the sibling's model that this sample lacks.

### 3. Narrower-slice test — negative

- The only "grant-management-only" structures observed are **modules inside the same suites** (Cayuse Fund Manager, InfoEd Post Award Management), not standalone products forming a population.
- Products named "grant management" outside this population serve different parties: grantmaking platforms (funder side), government grants management (sponsor side), nonprofit grant management (program-delivery grantee side) — all already separate Types in the directory.
- No product population was found that manages research grants without the pre-award institutional machinery (i.e., a post-award-only research product population). The post-award money view presupposes the award record, which presupposes the proposal record in every sampled suite.

### 4. Verdict

**ALIAS CONFIRMED.** Research Grant Management ≡ Research Administration Platform — one market family behind two directory names. "Research administration" names the institutional function and office; "grant management" names the funding lifecycle the software carries. Per the typeface-design ≡ font-editor and survey ≡ questionnaire precedents: **keep both leaves, each with a lens document, cross-referenced**; merge/canonical-name decision escalated to directory-level review; DIRECTORY.md untouched.

- applications/research-administration-platform.md — the institution/function lens (sibling, already written).
- applications/research-grant-management.md — the funding-lifecycle/money lens (this pass).

## Canonical Model

### L0 — Defining Invariant

The same core the sibling pass established, phrased from the funding side. Three jointly-held structures:

1. **The grant as the institution's unit of record** — one persistent, identified record of one funding undertaking, spanning the proposal phase (what the institution requests) and the award phase (what the sponsor committed: terms, deliverables, anticipated/obligated amounts, account distributions), living from request to closeout. Remove → a proposal editor or a finance report, not grant management.
2. **The institutional gate** — the institution, not the individual researcher, owns the submission: proposals route through institutional review/approval before reaching the sponsor, and the institution is the accountable party of record. Remove → the sponsor's application portal or a personal document tool.
3. **Administration of the funded money to closeout** — after the award: spend tracked against budget in research language, personnel commitments/effort administered, subawards issued and invoiced under the prime award, every change (rebudgeting, reassignment, extension) recorded on the award, through closeout. Remove → a submission pipeline with no award memory, or pure grants accounting inside an ERP.

Jointly load-bearing: (1) alone = a grants database; (2) without (1) = an approval workflow tool; (3) without (1)+(2) = a finance report; (1)+(2) without (3) = pre-award pipeline only; (1)+(3) without (2) = researcher-side grant tracking, not institutional administration.

### L1 — Common Mature Structure

Present across the sample, not definitional:

- rate-governed budget development (fringe, F&A/indirect, inflation, cost share; multiple versions)
- configurable routing workflows with conditional logic and e-signature/approval histories
- personal action lists / role-scoped dashboards and analytics
- agreement and negotiation tracking (contracts, MTAs, NDAs)
- compliance touchpoints on the grant record (COI status, protocol links, export-control reviews) — realized as sibling modules
- audit-ready record-keeping (attachments, approval histories)
- shared master data (person, sponsor, subawardee records)
- funding-opportunity search bundled (2/3 observed directly)
- internal funding competitions / limited submissions (2/3)
- closeout as a named terminal phase (3/3, one via institution-built extension)

### L2 — Variant / Optional Structure

- **Regime machinery**: system-to-system submission into sponsor portals, federal form catalogs, pre-submission validation services, effort certification — US-federal-heavy; other regimes substitute their own portals and costing rules.
- **Funding-type breadth**: sponsored research only vs portfolios including institutional funds, philanthropic funds, clinical/industry income administered in the same fund view.
- **Packaging**: full connected suites vs à la carte products vs institution-built extensions on top (Kuali Build examples: gift routing, no-cost extension, PI eligibility).
- **Institution scale/structure**: R1 volume vs emerging programs; centralized vs decentralized routing.
- **Regional regimes**: US vs UK/EU/APAC operations (Cayuse documents international operations; structure claimed regime-independent, machinery not).

### L3 — Vendor-specific Structure

(Research notes only; none of this enters the final document as structure.)

- Cayuse module names: Fund Finder, Proposals (S2S), Sponsored Projects, Cayuse Agreements, Fund Manager, Project Effort, Insights; marketing metrics ("1,500 smart validations", "99.9% first-time submission rate", "50% faster", "spend-to-zero on 75% of awards", "50–70% faster reports").
- Kuali module names: Sponsored Programs, Internal Opportunities, GrantRisk, Kuali Build; the institution-built extension examples list.
- InfoEd module names: SPIN, SMARTS, Proposal Development, Proposal Tracking, Post Award Management, Financial Tracking, Entity Management, Time & Effort, Current/Pending Support, ITEMS, ICAG, eRAI; SPIN scale claims ("40,000+ opportunities, 12,000+ sponsors"); "30+ years" longevity claim; "over 20 tightly integrated modules".

## Vendor-specific Findings

- InfoEd is the only sampled vendor whose **product taxonomy itself** splits "Pre-Award Grants Management" and "Post-Award Grants Management" as named product lines — evidence that even where the market uses the narrowest grant vocabulary, the unit remains one sponsored-projects system spanning both.
- Kuali is the only sampled vendor documenting **institution-built workflow extensions** as a first-class pattern (no-code forms/workflows on top of the grant record).
- Cayuse is the only sampled vendor with a **dedicated effort-certification product** on its award-management page (payroll import → certification); InfoEd carries Time & Effort as a module; Kuali's effort lives in sibling products per the sibling pass. Effort machinery is common but packaging varies.
- SPIN-style **funding-opportunity databases with profile-based matching** are a bundled capability (InfoEd SPIN/SMARTS, Cayuse Fund Finder); Kuali's fetched research page does not show one — bundling is optional, not definitional.

## Boundary Findings

1. **vs Research Administration Platform — ALIAS (resolved this pass).** See the Alias Test section. Both leaves stand with lens documents; merge decision escalated.
2. **vs Grantmaking Platform / Government Grants Management (funder/sponsor side).** The same transaction — proposal in, award out — is administered by two systems on two sides. This Type is the recipient institution's side; those Types are the funder's side (foundations; government agencies). The proposal record crosses between them.
3. **vs Nonprofit Grant Management.** Grantee side too, but the money funds program delivery, not research; the research-specific machinery (sponsor terms & conditions, effort certification, F&A/indirect-cost rates, subaward monitoring under a prime award, research-compliance touchpoints) marks this Type. A foundation grant to a nonprofit program has no analog of most of these.
4. **vs Research Funding Discovery Platform.** Opportunity search is a bundled capability here (SPIN, Fund Finder) — discovery products hold opportunity databases and matching without proposal/award records; the moment an application becomes a routed institutional record, the grant-management system is in play.
5. **vs Research Information Management / CRIS.** CRIS holds the institution's research information (publications, activities, expertise); this Type holds its funding undertakings. Awards feed CRIS (funding metadata on publications), not the reverse.
6. **vs ERP / Financial Management.** The institutional ledger, chart of accounts, and payroll live in the finance systems; this Type holds the award/fund view in research language over that substrate (account mapping, expenditure import, F&A transaction publication — InfoEd documents the mechanics most explicitly). A system that became the general ledger would be drifting into ERP territory.
7. **vs Research Project Management.** The research work itself (milestones, scientific progress, tasks) vs the funding wrapper around it. The grant record tracks money and obligations, not experiments.
8. **vs IRB / IACUC / Research Compliance Management.** Committee review over protocols vs administration of funding. The systems interlock (protocol status linked into proposals; IRB-triggered routing; COI status auto-populated) and suites ship both as sibling products — interlock, not identity.
9. **Historical / market-sample check.** The pre-digital research office — paper proposals with routing sheets and institutional signatures, typed budget sheets computed with institutional rate figures, card files of award terms and deliverables, ledger-based fund tracking, subaward correspondence files — satisfies all three L0 structures with no software, no S2S, no dashboards. One sampled vendor documents 30+ years of continuous development (early-1990s origin), and the "eRA" (electronic research administration) label itself names the digitization of an older administrative practice. The definition therefore does not depend on any current-era machinery. Regional regimes (UK/EU/APAC documented as served markets by one sampled vendor) fit the same core with their own submission machinery.

## Uncertainties

- **Market breadth**: Huron Research Suite, Worktribe, Streamlyne, ResearchMaster, Aurora unreachable — the verified sample is three US-origin commercial suites. Claims about the broader market (especially UK/EU/AU regional products) are calibrated; no structural claim rests on an unreachable vendor.
- **Closeout depth**: documented as a named phase at Cayuse ("inception through close-out") and InfoEd ("Notice of Award through closeout"); at Kuali observed only as an institution-built closeout form example. Closeout machinery depth is treated as common, not precisely characterized.
- **PI-facing personal grant trackers**: no product population found in-sample for individual-researcher grant tracking as a distinct Type; existence beyond the sample unverified.
- **Effort certification regime dependence**: all three sampled vendors carry effort machinery, but its obligatoriness is regime-dependent (US federal); whether non-US products omit it entirely is unverified (Cayuse documents international operations without detailing their effort posture).
- **Internal opportunities**: observed at Kuali and InfoEd; not observed on Cayuse's fetched page (may exist elsewhere in the suite) — held optional, not definitional.

## Final Synthesis

Research Grant Management is the **funding-lifecycle lens** on the Type the atlas documents as Research Administration Platform: the research institution's system of record for the grants it receives and administers. The defining core is the grant as a persistent institutional record spanning proposal and award, moved by an institutional gate before anything reaches the sponsor, and administered as money, effort, subawards, and recorded changes through to closeout. The market uses "research administration" and "(research) grant management" interchangeably for these systems — every sampled product self-labels with both — and no narrower grant-only product population exists. The alias is recorded; both documents stand, this one from the money-and-lifecycle angle, the sibling's from the institution-and-function angle.
