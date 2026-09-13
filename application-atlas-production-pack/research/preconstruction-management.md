# Research Notes — Preconstruction Management

## Research Goal

Understand what "Preconstruction Management" software actually is as an Application Type: what unit of record it manages, what workstreams it coordinates, how the pre-award phase of construction work is organized inside real products, and where its boundaries sit against the neighboring construction Types (Construction Estimating, Construction Bidding Platform, Construction Project Management, Construction Cost Management, Quantity Takeoff).

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Preconstruction Management is the contractor-side (and possibly owner-side) system for the phase **before construction award**: opportunity/pursuit → takeoff/estimate → subcontractor/supplier solicitation → bid leveling → award decision → handoff to execution.
- Nearest neighbors: Construction Estimating (the pricing discipline), Construction Bidding Platform (the solicitation/distribution network), Construction Project Management (post-award delivery), Construction Cost Management (post-award cost control), Quantity Takeoff (quantity output).
- Known prior-pass evidence: the construction-estimating pass (2026-09-07) recorded "vs Preconstruction Management (pricing discipline inside the umbrella)" — i.e., estimating already treats this leaf as the umbrella it sits inside. The construction-project-management pass documented the project container persisting award→closeout, implying precon lives before that container (or before award within it).
- Risk to test: is this leaf a real Type with its own invariant, or merely an umbrella/alias over estimating + takeoff + bidding?

## Research Questions

1. What is the unit of record? Is there a persistent "pursuit/bid/opportunity" object, or do products only carry estimates and bid packages?
2. How is the money content of a pursuit assembled (estimate, budget, quotes) and does it live inside the pursuit?
3. How does the supply-chain solicitation loop work (packages, invitations, bid intent states, coverage, leveling)?
4. How does the pursuit resolve (award decision) and how does the handoff to execution work (estimate→budget, bid→contract/PO)?
5. Which capabilities are common mature structure vs variant: takeoff, prequalification, design coordination/BIM, opportunity sourcing, analytics?
6. Who are the users (GC precon teams, estimators, bid managers, subs, owners) and how do the operator poles differ?
7. Do older/regional products (paper-era bid desks, UK tender management, residential design-build) fit the same definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Procore (Preconstruction: Tender/Bid Management, Estimating, Takeoff, BIM) | GC platform leader; connected precon-to-execution platform | Market-leading GC platform; explicit "Preconstruction" product family with phase flow |
| InEight (Estimate + platform) | Enterprise capital projects; estimate-centric connected suite | Deep estimating machinery (structures, benchmarking, quote management); enterprise tier |
| STACK (Takeoff & Estimate + Bid Management + Plan & Spec) | Specialty contractors / subs; takeoff-estimate-bid workbench | Subcontractor-side pole; self-labels "preconstruction platform"; help center reachable |
| ConstructConnect (Project Intelligence + Takeoff/Estimating + Bid Management/SmartBid) | Find-work + bid management suite; GC and sub sides | "Complete preconstruction workflow" framing; bid-day coverage focus; network side |
| Kahua (Bid Management) | Owner / enterprise PMIS pole | Owner-side procurement posture: bids generated from approved budgets, public solicitations, award→contract |

Rejected/abandoned samples: Buildxact (residential precon pole — 403, consistent with the estimating pass), ConWize (European bid management — transport errors ×2), Autodesk Construction Cloud (403, consistent with prior passes), Destini (UK bid management — 403).

## Sources

All fetched 2026-09-09 unless noted.

- Procore — Preconstruction software: https://www.procore.com/en-sg/preconstruction
- Procore — Tender Management: https://www.procore.com/en-sg/tender-management (US equivalent /bid-management)
- Procore — Estimating: https://www.procore.com/en-sg/estimating
- Procore — Products index: https://www.procore.com/en-sg/products
- InEight — Platform root: https://ineight.com/
- InEight — Estimate: https://ineight.com/products/ineight-estimate/
- STACK — root: https://www.stackct.com/
- STACK — Help Center root: https://support.stackct.com/hc/en-us
- STACK — Help Center Takeoff & Estimate category: https://support.stackct.com/hc/en-us/categories/47341050127891-STACK-Takeoff-Estimate-TE
- ConstructConnect — root: https://www.constructconnect.com/
- ConstructConnect — Bid Management: https://www.constructconnect.com/products/bid-management
- Kahua — root: https://www.kahua.com/
- Kahua — Bid Management: https://kahua.com/solutions/bid-management/

Source-access limitations:

- Procore support site (support.procore.com) returned 404 on all attempted paths (×3) — product pages (Tier 2) used instead; no help-article-level operational detail for Procore.
- Buildxact 403 (root); ConWize transport error ×2; Autodesk Construction Cloud 403; Destini 403 — all abandoned per the retry rule; no claims based on them.
- Kahua /solutions/preconstruction 404; the bid-management solution page was used.
- STACK help center reached at category level (section list); individual articles not fetched.
- Consequence: no precise numeric limits, exact state-machine labels, or default settings are asserted in the final document; vendor marketing numbers (network sizes, ROI percentages) are recorded here as vendor claims only.

## Product A — Procore (Preconstruction family)

### Key observations (evidence layer A unless noted)

- Procore markets a dedicated **"Preconstruction software"** family: "Connected Preconstruction: Plan Smarter, Build Better — Win more profitable work, deliver more predictable project outcomes, and stay connected from planning through closeout."
- The precon page organizes the phase as a flow: **Design → Plan → Tendering → Execute → Learn**.
  - Design: BIM / Design Coordination, 3D Takeoff, clash resolution workflows, escalate coordination issues to RFIs.
  - Plan: "Go from takeoff to final estimate with a single click"; estimates with "flexible tools and integrated cost models"; "seamless handoffs from estimating to course of construction"; "Keep financial data connected from preconstruction through closeout."
  - Tendering: "Create packages, find the strongest possible tenders, and convert tenders to trade partners on one connected platform"; "Source prequalified trade partners from a centralised, validated network"; "Track tender activity across projects and generate performance insights"; "Compare apples-to-apples with structured tender forms and automated tender levelling"; "Centralise all tender files, decisions, and communication to streamline award and handoff"; analytics + historical tender data for vendor selection.
  - Execute: "Convert accepted estimates into project budgets"; "Sync field teams with preconstruction data to minimise startup delays"; "Quickly and easily price changes during construction."
  - Learn: "Track estimating accuracy, tender coverage, and qualification outcomes"; trends across trades/regions/project types; "Connect preconstruction data with downstream performance."
- **Tender Management** page: "Streamline the entire construction tendering process, from creating packages to awarding bids, on one connected platform."
  - Organise all tender documents, drawings, specs in one place; create/manage tender invitations per project; central directory of subcontractors and suppliers; automated notifications/reminders to improve response rates.
  - Side-by-side comparison of subcontractor bids; **level tenders** to account for different scopes and pricing; analyse bids and estimates against project budgets and bill of quantities; track performance data and **win rates**.
  - "Once a bid is won, convert it to a subcontract or purchase order in a single click"; data flows into Procore Financials; awarded tenders link to project drawings/documents.
- **Estimating** page: takeoff (2D/3D auto-mapped, AI floor-plan detection, auto-count, plan overlay, customisable database of parts/assemblies/equipment/services) → estimate (adjust material prices, labour units, profit margins) → customer-facing proposal; historical cost data validates pricing assumptions; "Move directly from a quantity takeoff to a final tender without losing data in manual transfers"; "Move directly from estimate to contract and financials."
- FAQ: preconstruction software "designed for everyone involved in a project, including owners, general contractors, and specialised contractors… a collaborative hub for all stakeholders to manage designs, tenders, and cost estimates."

## Product B — InEight (Estimate + platform)

### Key observations

- Platform framing: "purpose-built applications that manage all phases of capital projects, starting with accurate pre-planning and ending with predictable completion and commissioning." Estimate + Schedule are grouped under "Pricing and Scheduling" (the preconstruction side of the platform).
- **InEight Estimate**: "Win more of the right jobs at the right price… From conceptual planning to final proposal, deliver consistent, high-quality bids."
  - **Flexible estimate structures**: crew setups, activity structures, cost breakdowns, work breakdown structures, templates — "configure estimates to match real-world execution."
  - **Built-in benchmarking**: "compare estimate values to high, low, and average costs and productivity rates from past projects" — variance identification against historical/as-built data.
  - **Bid Wizard**: "streamlines estimate creation through reusable templates, predefined workflows, and standardized data."
  - **Quote management**: "Centralized subcontractor and vendor pricing within the estimating workflow supports efficient quote comparison, late-stage updates, and bids based on current, competitive cost information."
  - Supports "the full range of construction estimating needs, from early-stage conceptual and feasibility estimates to detailed bid and control estimates."
  - "Evaluate alternative execution approaches during the bid phase… identify smarter paths of construction."
- Integrations: Primavera P6 (scheduling), Bluebeam (takeoff), InEight Control ("align estimates with actuals, forecasts"), Change ("receive estimated and priced change orders"), Contract ("share vendor and contract data across procurement and estimating"), Schedule ("time-phase estimate data"), Model ("import quantities and scope from 3D models"), Report & Explore.
- Deployment: cloud **or on-premises**; FAQ explicitly says Estimate "can operate as a stand-alone construction estimating solution or bundled with other InEight modules."
- FAQ names "bid management tools" among Estimate's capabilities.

## Product C — STACK

### Key observations

- Self-label: "STACK is the premier AI preconstruction platform where estimating teams complete faster takeoffs, build sharper estimates, and turn every project into measurable revenue, profit, and win-rate growth." Nav groups a **Preconstruction** solution family.
- Workflow: **Evaluate → Takeoff → Estimate → Build**.
  - Evaluate (Plan & Spec Management): "Centralize drawings, surface answers, and get your projects bid-ready" — AI reads sheets, auto-names pages, flags revisions.
  - Takeoff: linear/area/count/volume measurement, AI auto-count, version compare/overlay.
  - Estimate: "Quantities flow straight into live estimates"; worksheet-style estimating with items and assemblies; AI "pressure-tests pricing"; regional cost data integration; ERP connectors; STACK for Excel.
  - Build: "Carry the same scope and budgets into the field — RFIs, daily reports, photos, and markup keep the build on track without rekeying a thing."
- Takeoff & Estimate product bundle named contents: "Quantity & Material Takeoff, Detailed Estimates & Proposals, **Bid Management**."
- Who We Serve: Specialty Contractors (first), General Contractors, Suppliers & Manufacturers, Owners & Developers.
- Help center (Tier 1): TE category described as "streamlines preconstruction by enabling fast digital takeoffs, accurate estimates, and seamless team collaboration for more competitive bids." Sections: **Projects** (create a project and add project information; create a project from an external source; upload project files; copy a project or plan sheets; project list; project permissions), Plans & Takeoffs, Estimates, Reports, Calendar, **Libraries** (import items into a library; library permissions; variables), Integrations, Troubleshooting.
- Integrations include Procore, QuickBooks, FollowUp CRM (a construction CRM), Dodge (project lead source), planHub (bid network), Buildertrend, Acumatica.

## Product D — ConstructConnect

### Key observations

- Root framing: "**The complete preconstruction workflow** — All the products you need, from first lead to won bid." Three steps: **Find Projects → Takeoff & Estimating → Manage Bids**. "ConstructConnect Platform — The connected precon suite."
- **Project Intelligence** (Find): "Find and Qualify Projects to Bid" — search active projects by keyword/trade/location/stage against a live dataset; project stages shown include Conceptual, Sub-Bidding, GC Bidding; bid dates; "carry the details straight into takeoff and bid management when a job is worth pursuing."
- **Bid Management** (Manage): "Keep every step of your bidding process organized, from first invitation to final award. Find, prequalify, and invite subcontractors, then track responses in real time, so you have the coverage you need to walk into your bid day with confidence."
  - SEND: "Create projects and bid packages in just three simple steps—add details, upload documents, and select trades"; automatic filtering "and only reach subcontractors that match your project's trades and service area"; branded Invitations to Bid, addenda, updates.
  - PLAN (coverage): "Increase bid responses by inviting your own network or use our recommended bidders"; "setting bid goals and identifying where you might need more coverage"; "Track subcontractor activity based on activity on current projects, bidding history, and our proprietary engagement score."
  - ORGANIZE: upload/organize/rename project documents; "Automatically sort trade lists and map them to your preferred Construction Specifications Institute (CSI) codes."
  - RISK MANAGEMENT: "Prequalify bidders with industry-standard or custom forms"; "Review safety, performance, and financial records before sending out invites to bid"; vendor reviews and owner compliance.
- Bid-board UI (illustrative screenshots): bidders listed per package with **bid intent states** (Bidding / Did Bid / Not Bidding / Under Review / No Response / Bid Received) and bid amounts.
- FAQ: "ConstructConnect® Bid Management is an online tool that helps general contractors easily organize, track, and send bid invitations to subcontractors"; subcontractors "can view the details and submit their bid through our platform—even without a subscription."
- Pairs with takeoff/estimating products (On-Screen Takeoff, PlanSwift, Quick Bid — "Turn takeoffs into fast bids", QuoteSoft).
- Subcontractor side: "respond to multiple general contractors, keep track of general contractors through the bid boards."

## Product E — Kahua (Bid Management)

### Key observations

- Page framing: "**Manage every bid, from ITB to contract.** Create bid packages, invite vendors, manage Q&A, compare proposals, and move awarded bids into contracts. Keep your construction bid management software connected to budgets, approvals, and the project record."
- Capabilities: "Manage invitation-to-bid (ITB) workflows, bidder communication, **bid rooms**, **public solicitations**, Q&A, award notifications, and contract creation in one connected environment."
- "**Generate bids from approved budgets** — Tie released bids directly to budgeted resources, so teams can start with approved financial data instead of rebuilding or reconciling the record later." (Owner-side posture: the pursuit's money content comes from the approved budget, not a self-built estimate.)
- "Use predefined workflows, customizable forms, and role-based permissions to capture project-specific details and manage the invitation to bid process (ITB) consistently."
- Bid room: "give vendors access to bid documentation, and manage bidder communication."
- Public construction bids: "Give bidders access to the same information, submission requirements, and supporting documentation."
- "**Move awards into contracts without starting over** — Select winning proposals, notify vendors, and carry the bid, award, and contract record forward as work moves into contracting."
- FAQ: "Construction bid management software helps teams create bid packages, invite vendors, manage bidder communication, compare responses, issue award notifications, and move awarded bids into contracts."
- Users: "owners, general contractors, construction managers, procurement teams, project controls teams, and program teams."
- Connections: "approved budgets, cost management, project controls, document management, contract workflows, portfolio visibility, and reporting."

## Cross-product Comparison

| Structure / capability | Procore | InEight | STACK | ConstructConnect | Kahua | Layer |
|---|---|---|---|---|---|---|
| Pursuit/bid opportunity as persistent record (project + bid packages, status toward award) | Y (tender packages per project; award/handoff) | Y (estimate for a bid, conceptual→final proposal) | Y (Projects; create from external source) | Y (create projects and bid packages; first invitation→final award) | Y (bid packages on a project; ITB→contract) | B |
| Priced scope assembled for the pursuit (estimate/budget content) | Y (takeoff→estimate→proposal; budgets) | Y (estimate structures, benchmarking) | Y (live estimates from takeoff) | Y (paired takeoff/estimating products; Quick Bid) | Y* (bids generated **from approved budgets** — money content carried, not self-built) | B |
| Supply-chain solicitation (packages → invitations → responses with intent states) | Y (tender invitations, directory, notifications) | Y (quote management: sub/vendor pricing, comparison, late-stage updates) | Y (Bid Management in TE bundle) | Y (ITBs, filtering, coverage, engagement tracking) | Y (invite vendors, bid rooms, public solicitations, Q&A) | B |
| Leveling / structured comparison to a common basis | Y ("apples-to-apples… automated tender levelling") | Y (quote comparison within estimating) | partial (estimates compared; leveling not named) | Y (bid goals, coverage gaps; leveling via paired tools) | Y ("compare proposals") | B |
| Award resolution + handoff to execution | Y (convert won tender → subcontract/PO; estimates → project budgets) | Y (estimate → Control budget/Contract/Schedule) | Y (carry scope/budgets into the field) | Y ("from first invitation to final award") | Y (award → contract creation) | B |
| Takeoff (2D/3D/AI) feeding the estimate | Y | partial (integrates Bluebeam; Model import) | Y (core) | Y (dedicated products) | N | B (common, not definitional) |
| Subcontractor/supplier directory + prequalification | Y (prequalified network) | partial (vendor data via Contract) | partial (network invites) | Y (prequal forms, safety/financial review) | Y (vendor management) | B (common) |
| Opportunity/lead sourcing (finding work to bid) | N | N | partial (Dodge integration) | Y (Project Intelligence, leads) | N | B (variant) |
| Design coordination / BIM in precon | Y (BIM, 3D takeoff, clash → RFI) | partial (Model import) | partial (plan/spec AI) | N | N | B (variant) |
| Historical cost data / benchmarking | Y (historical cost validation) | Y (benchmarking vs past projects) | Y (regional cost data) | partial | N (budget-carried) | B (common) |
| Win-rate / performance analytics | Y (win rates, tender coverage) | partial (Report & Explore) | Y (win-rate growth framing) | Y (engagement scores, activity) | partial (analytics module) | B (common) |
| Document/drawing management for the bid | Y (tender docs, drawings, specs) | partial (Document module) | Y (plan & spec management) | Y (upload/organize/rename, CSI mapping) | Y (bid documentation, bid rooms) | B (common) |
| Cloud-only | Y | N (cloud or on-prem) | Y | Y | Y | B (variant) |

\* Kahua carries the pursuit's money content from approved budgets rather than building an estimate in-product — the generalized form of the structure.

**Reading:** all five products organize the pre-award phase around a persistent pursuit (project + bid/tender packages) that carries priced scope, runs a solicitation-and-comparison loop over the supply chain, and resolves in an award that hands priced scope to execution. The disciplines (takeoff, estimating, prequalification, design coordination, lead sourcing) appear as workstreams inside that pipeline with different depths per product — not as the definition itself.

## Canonical Abstraction

### L0 — Defining Invariant (four jointly-held structures)

1. **The pre-award pursuit as the unit of record.** A persistent identified record of a prospective construction undertaking the organization is pursuing — a bid, tender, or opportunity — carrying the pursuit's context (prospective customer/owner, bid/tender date, documents) and advancing through a status toward the award decision. Remove → an estimating tool or a bid-solicitation tool with no pursuit container (or a generic CRM pipeline).
2. **The priced scope assembled for the pursuit.** The pursuit's money content: an estimate or budget built or carried for this specific prospective project — from quantities, rates, historical costs, and commonly subcontractor/supplier quotes — revised as the pursuit advances. Remove → an opportunity tracker with no construction price (CRM territory).
3. **The supply-chain solicitation and leveling loop.** The pursuit's scope is packaged into trade/scope packages and offered to subcontractors and suppliers, whose responses (bid-intent states, prices, documents) are collected, compared on a common basis (leveled), and folded into the pursuit's price and the award decision. Remove → a single-estimator pricing workbench (Construction Estimating territory).
4. **The award resolution and handoff.** The pursuit terminates in a recorded outcome (won / lost / no-bid); on a win, the priced scope converts into the project's budget, commitments, or contracts and hands off to execution. Remove → pre-award work that never resolves; the phase boundary that makes it "pre"-construction dies.

Joint load-bearing:

- 1 alone = opportunity/lead tracker (CRM)
- 2 alone = Construction Estimating
- 3 alone = bid solicitation network (Construction Bidding Platform territory)
- 4 alone = an award record
- 1+2 without 3+4 = estimating with pursuit context but no supply-chain loop (self-perform estimating pole)
- 1+3 without 2 = a bid desk with no price assembly
- 2+3 without 1 = estimating + quote collection with no pursuit container
- 1+2+3 without 4 = pre-award work that never resolves — phase management incomplete

### L1 — Common Mature Structure

- Takeoff (2D/3D, AI-assisted) feeding the estimate
- Cost libraries / historical cost data / benchmarking against past projects
- Subcontractor/supplier directory with prequalification (forms, safety/financial review)
- Structured bid/tender forms and apples-to-apples comparison (leveling)
- Coverage tracking (which trades have responses) with reminders/notifications
- Document/drawing/spec management for the bid (addenda, revisions)
- Win/loss and performance analytics (win rates, estimating accuracy, vendor engagement)
- Reusable estimate structures/templates; proposal/bid-form output
- Integrations to accounting/ERP and project management platforms

### L2 — Variant / Optional Structure

- Operator pole: GC/main contractor (solicit and level trades) vs specialty contractor (respond to invitations; own takeoff/estimate/bid) vs owner/program side (public solicitations, bid rooms, bids from approved budgets)
- Segment: commercial GC vs heavy civil vs residential/design-build (proposal to the owner; supplier quotes rather than trade leveling)
- Regional tradition: US bid culture (ITB, bid leveling, CSI codes) vs UK/Commonwealth tender culture (tender packages, BOQ, prequalification questionnaires, frameworks)
- Opportunity sourcing included (find work to bid) vs starting from an incoming RFP/ITB
- Estimate depth: conceptual-to-control-estimate range (enterprise pole) vs takeoff-driven pricing (SMB/sub pole)
- Design coordination/BIM inside precon (present/absent)
- Suite member vs standalone point tool; cloud vs on-prem

### L3 — Vendor-specific (research notes only)

- Procore: one-click tender→subcontract/PO conversion; unlimited-user licensing claim; "Explore Preconstruction" phase flow naming (Design/Plan/Tendering/Execute/Learn)
- InEight: Bid Wizard; benchmarking against high/low/average historical costs; Excel cell-level linking; on-prem deployment option; Estimate↔Control/Change/Contract/Schedule/Model data flows
- STACK: STACK IQ conversational AI; STACK for Excel (Velixo partnership); plan/spec AI (auto page naming, revision flagging); FollowUp CRM / Dodge / planHub integrations
- ConstructConnect: engagement score; recommended bidders; network-size and project-count marketing figures (450,000+ professionals, 825,000+ projects — vendor claims); Takeoff BOOST; SmartBid/iSqFt product lineage; CSI auto-mapping
- Kahua: bid rooms; public-solicitation support; bids generated from approved budgets; Noa AI / kBuilder Canvas (platform-level)

## Vendor-specific Findings

See L3. Marketing figures (network sizes, ROI percentages, customer counts) observed on vendor pages are recorded as vendor claims and are not carried into the final document.

## Boundary Findings

1. **vs Construction Estimating (§17, processed 2026-09-07).** Estimating is the pricing discipline: the estimate as priced line items decomposing the work, pre-award purpose, ending by design at award. Preconstruction Management is the pursuit-level management layer that *contains* estimating as one workstream and adds the pursuit container, the supply-chain solicitation/leveling loop, and the award handoff. Removal test: strip the pursuit container + solicitation loop from a precon product → a Construction Estimating tool remains. The estimating pass itself recorded this seam ("pricing discipline inside the umbrella"). Consistent; keep both.
2. **vs Construction Bidding Platform (§17, unprocessed sibling).** The bidding platform's center of gravity is the multi-party solicitation/distribution network — public bid boards, ITB distribution to large sub networks, subcontractor-side bid tracking across GCs. Preconstruction Management's center is the single organization's pursuit-to-award pipeline (pursuit record + priced scope + leveling + award handoff). Overlap: bid solicitation machinery is shared; ConstructConnect straddles both (Bid Management + project-lead network + sub-side bid boards). **Joint review recommended when Construction Bidding Platform is processed.** Proposed seam: whose record is it — the network's solicitation venue vs the company's pursuit pipeline.
3. **vs Construction Project Management (§17, processed 2026-09-07).** Post-award delivery vs pre-award pursuit. The CPM pass documented the project container persisting award→closeout with the multi-org community and cross-org coordination record; precon lives before award (or before the project container exists). The handoff seam is designed and documented from both sides (estimates → project budgets; won tenders → subcontracts/POs; bids → contracts). Keep both.
4. **vs Construction Cost Management (§17, processed 2026-09-07).** Pre-award pricing vs post-award cost control. The budget-from-estimate handoff was confirmed from the cost side in that pass; this pass confirms the same seam from the precon side. Keep both.
5. **vs Quantity Takeoff (§17, unprocessed sibling).** Quantity output vs pursuit management. Takeoff is a contained capability inside precon (and inside estimating); a takeoff tool has no pursuit record, no solicitation loop, no award. Keep separate; ratify at that leaf's pass.
6. **vs CRM / Lead Management (§06/§07).** Pursuit tracking without priced construction scope and trade-package solicitation is CRM. The seam is real in the market: STACK integrates FollowUp CRM (a construction CRM) and Dodge (lead source) rather than replacing them. The pursuit here is construction-shaped: its content is priced scope and trade packages, its loop is supply-chain leveling, its terminal event is an award handoff into construction execution.
7. **vs Procurement Management / Strategic Sourcing (§10).** Both solicit offers from suppliers, but precon solicitation is construction-trade-shaped (CSI/trade packages, bid leveling, prequalification for construction risk, award into construction contracts) and phase-scoped to pre-award. Generic sourcing platforms are purchase-side and category-generic. Adjacent, keep separate.
8. **vs Proposal Management (§07, processed 2026-09-06).** Proposal management assembles the seller-side offer document for a deal and captures the buyer's decision. Precon bid submission is construction-shaped (tender forms, BOQ, leveling, award machinery, handoff into construction). The estimating pass already held this seam for bid-form output. Keep separate.

**Umbrella question (the leaf's main taxonomy risk):** is Preconstruction Management merely an alias for estimating + takeoff + bidding bundled? Resolution: **no** — the Type has its own unit of record (the pursuit) and its own terminal event (award resolution + handoff), and every sampled product organizes the phase around that pipeline rather than around a toolbox. The disciplines are workstreams inside it. However, the boundary with Construction Bidding Platform is the one seam that needs joint review (finding 2), because bid solicitation machinery is genuinely shared.

## Historical / Market-Sample Check

- **Paper-era bid desk** (mid-20th-century GC): ITB letter or plan-room notice opens a pursuit (ledger card); estimator does takeoff and prices the estimate; sub quotes solicited by phone/telegraph and leveled on a bid-day sheet; bid submitted; win/loss recorded; the estimate becomes the job's budget in the cost ledger. All four L0 structures present with zero modern machinery. **Passes.**
- **UK/Commonwealth tender management** (tender packages, BOQ, PQQ/ESQ prequalification questionnaires, framework agreements): same pipeline in tender vocabulary. **Passes** (vocabulary variant).
- **Residential design-build** (Buildxact-class, unreachable this pass but documented in the estimating pass's market knowledge): opportunity → takeoff/estimate → quote/proposal to the owner → win → job. The solicitation loop is supplier-shaped rather than trade-leveling-shaped; the generalized loop still applies. **Passes** (segment variant).
- **Owner-side procurement** (Kahua): solicitations issued from approved budgets to GCs, public bid rooms, award → contract. Money content carried rather than self-built. **Passes** (operator-pole variant).
- Conclusion: the definition is not over-fitted to the modern US GC bid-desk implementation. Takeoff, AI, cloud, prequalification forms, and specific state labels are all era-current or regional machinery, not invariants.

## Uncertainties

1. The exact boundary with **Construction Bidding Platform** (unprocessed) — bid solicitation machinery is shared; ConstructConnect straddles. Joint review recommended.
2. The **residential/SMB pole** (Buildxact-class) could not be fetched this pass (403) — the residential variant reading rests on the estimating pass's market knowledge plus the general structure, not on fresh direct evidence. Assertion strength for that pole: reduced.
3. **European bid-management specialists** (ConWize, Destini) unreachable — the UK/Commonwealth tender-culture variant is asserted from structural reasoning and regional vocabulary, not from direct product observation this pass.
4. Whether **opportunity/lead sourcing** (finding work to bid) should eventually be claimed by a separate Type (project-lead platforms) or held as a precon variant — ConstructConnect includes it in its precon workflow; Procore/InEight/STACK do not. Held as variant here.
5. Help-center-level operational detail (exact state machines, permission models, numeric limits) was not reachable for Procore, Kahua, ConstructConnect, or InEight; the final document deliberately avoids precise operational claims.

## Final Synthesis

Preconstruction Management is the organization's system of record for the pre-award phase of construction work. Its defining core is the **pursuit-to-award pipeline**: a persistent pursuit record (bid/tender/opportunity) that carries priced scope assembled for that specific prospective project, runs a solicitation-and-leveling loop over the subcontractor/supplier supply chain, and resolves in a recorded award decision whose outcome hands the priced scope into execution (budget, commitments, contracts). Estimating, takeoff, prequalification, design coordination, and lead sourcing are workstreams and capabilities inside this pipeline — common mature structure or variants, not the definition. The Type is phase-scoped, not tool-scoped: it is realized by GC platforms (Procore), enterprise estimate-centric suites (InEight), subcontractor workbenches (STACK), find-work-plus-bid-management suites (ConstructConnect), and owner-side PMIS modules (Kahua). The sharpest open seam is with Construction Bidding Platform (shared solicitation machinery; joint review recommended).
