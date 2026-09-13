# Research Notes — Change Order Management (Construction)

Research date: **2026-09-07**

## Research Goal

Understand what a construction Change Order Management application actually is from real products: what objects exist inside it, what lifecycle a change goes through, who participates, what rules gate the workflow, how it attaches to project money (contracts, budget, billing), and where its boundary lies against neighboring Types (Construction Cost Management, Progress Billing, Construction Claims Management, RFI Management, Engineering Change Management).

## Initial Boundary (pre-research hypothesis)

- Core purpose: manage changes to a construction contract's scope, price, and time as formal documented objects — identification → itemization/pricing → multi-party review/approval → execution into contract sum, schedule, and billing.
- Users: general contractors, construction managers, owners/owner reps, architects, subcontractors, cost controllers.
- Neighbors: Construction Cost Management (broader), Construction Contract Administration (broader), Progress Billing (downstream), Construction Claims Management (the disagreement path), RFI Management (information, not change), Engineering Change Management (§16 — different domain despite the shared word "change"), Purchase Order Management, Approval Workflow Platform.
- Risks: this leaf may be only a module of Construction Cost Management / Construction Project Management; must check whether it stands as a recognizable Type of its own (market evidence suggests yes — a whole product category "construction change order management software" exists, e.g. InEight markets "Construction Change Order Management" as a product headline).

## Research Questions

1. What is the object model? Is there a distinction between an identified/potential change and an executed change order?
2. What lifecycle/status states do change objects carry, and which states affect project financials?
3. How is a change priced (line items, SOV, quote/RFQ solicitation, pricing forms)?
4. Who reviews and approves? How do multi-party (owner / GC / sub) flows work across contract tiers?
5. How do approved changes propagate into budget, commitments, and billing?
6. What exception patterns exist (rejection, void, no-charge, time-only impact, backcharge, directives/claims when agreement fails)?
7. How does the audience vocabulary differ (GC vs owner vs specialty contractor vs residential)?
8. Packaging: standalone product, platform module, ERP module?

## Representative Products

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| Procore | Commercial GC / multi-party platform, market leader; richest public Tier-1 docs | Defines the multi-tier multi-party model |
| InEight Change | Enterprise capital projects / project-controls suite; standalone change module posture | Cost-control philosophy; issue-based change capture |
| CMiC | Construction ERP for GCs; single-database financials-first | ERP-embedded posture; auto-propagation to subcontracts |
| BuildBook | Residential custom builders/remodelers; client-experience product | Market-context check for the residential SMB pole (feature-list level only) |

## Sources

Successfully fetched 2026-09-07:

1. Procore Support — FAQ "What is a change order?" — https://support.procore.com/faq/what-is-a-change-order (Tier 1)
2. Procore Support — FAQ "What is a change event?" — https://support.procore.com/faq/what-is-a-change-event (Tier 1)
3. Procore Support — FAQ "What are the default statuses for change orders in Procore?" — https://support.procore.com/faq/what-are-the-default-statuses-for-change-orders-in-procore (Tier 1)
4. Procore Support — FAQ "What are the different change order tier settings in Project Financials?" — https://support.procore.com/faq/what-are-the-different-change-order-tier-settings-in-project-financials (Tier 1)
5. Procore Support — FAQ "What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?" — https://support.procore.com/faq/what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors (Tier 1)
6. Procore Support — Glossary of Terms — https://support.procore.com/references/construction-management/glossary-of-terms (Tier 1; definitions extracted for Change Event, Change Order, Change Order Request, Potential Change Order, Construction Change Directive, Changed Condition, Client Request, Backcharge, Prime Contract, Schedule of Values)
7. InEight — "InEight Change — Construction Change Order Management" product page + FAQ — https://ineight.com/change (Tier 2)
8. CMiC — "Change Order Management" business-needs page — https://www.cmicglobal.com/products/business-needs/change-order-management (Tier 2)
9. BuildBook — public feature index pages (project management tools; residential builder positioning) — https://buildbook.co/ (Tier 2, market context only)

Unreachable (attempted, abandoned after 1–2 failures per network rules — recorded as source-access limitation, no claims drawn from these):

- Autodesk Construction Cloud help (JS-rendered shell; second URL 404)
- Buildertrend help center (timeout; transport error; marketing site 403)
- Kahua (empty response; product URL 404)
- Trimble e-Builder help (empty response)
- Oracle Primavera Unifier docs (404 on both attempted URLs)
- JobProgress (403), CoConstruct (404), BuildBook change-order feature URL (404)

## Product Observations

### Procore (evidence layer A — directly observed, Tier-1 docs)

- **Definition (CO)**: "A Change Order (CO) is a written record of a contract modification that details any amendment(s) to the original agreement's scope of work." Contracts are executed with a defined scope; work added, substituted, or deleted (designs, conditions, schedules, costs) typically requires an approved change order.
- **Initiators**: change orders can be initiated by a variety of entities — funding source, project owner, contractor, subcontractor.
- **Common reasons**: design changes; drawing errors and omissions; inaccurate or incomplete specifications; unexpected job site conditions; material and crew substitutions.
- **Contract-relative**: a CO is created on a specific contract object — client contract, commitment, funding, or prime contract — and requires appropriate permissions on that contract.
- **Change events**: "any change that affects the original scope of a construction project... causes a change to the project schedule, or results in unexpected costs. It allows your project's team members and stakeholders to prepare for a cost change before it becomes an actual cost." Sources of change events include owner requests, design flaws, unforeseen issues from vague documents. Also used to document **backcharges** (recovering costs a party was contractually obligated to perform: repairing sub damage, cleanup, defective materials, reinstallation, safety compliance, equipment costs).
- **RFQ loop**: after a change event is created, an RFQ is sent to subcontractors; subs respond with documentation of potential cost and schedule impact (or the GC enters the response on their behalf); responses reviewed; then a Potential Change Order (PCO) is created.
- **Process chain (documented)**: Create Change Event → Create RFQs → Review RFQ Responses → Create Prime PCO from Change Event → Create Commitment PCO from Change Event.
- **PCO (glossary)**: created to track a change in a work condition when the change is expected to result in extra work/cost over and above the agreed-upon cost in a contract.
- **Change Order Request (COR) (glossary)**: "a Procore-specific package... contain[ing] one or more PCOs... a formal request sent to a project's Owner that groups multiple PCOs for a single scope of work into a single package for review and approval."
- **Default statuses** (shared list for change order / PCO / change order request): Draft (default for new items), Pending – In Review, Pending – Not Pricing, Pending – Pricing, Pending – Proceeding, Pending – Not Proceeding (PCO/CO package only), Pending – Revised, Approved, Rejected, Void (PCO only), No Charge. Financial reflection: Approved values → 'Approved Changes' column in Budget; Pending statuses → 'Pending Changes' column; Draft/Rejected/Void/No Charge → not reflected.
- **Tier configuration**: per contract tool (prime contracts, commitments, funding, client contracts) a 1-tier, 2-tier, or 3-tier setting determines how many steps the workflow requires:
  - 1-tier: create the change order directly; send to the counterparty for approval (owner for prime contract COs; downstream collaborator for commitment COs).
  - 2-tier (default on the contract/funding side): create PCOs first, then group PCOs into one change order and send for approval. Note: recommended where billing does NOT require grouping all approved change orders for the month into a single combined change order for final signature.
  - 3-tier ("uncommon"): PCOs → individually or grouped into a change order request → COR submitted for approval → after approval grouped into a single change order sent for approval.
  - The setting is fixed once change orders exist ("After you create one or more change orders... you cannot change your setting").
- **Approval direction**: prime-contract/funding/client-contract change orders go *up* to the owner/funding source; commitment change orders go *down* to the downstream collaborator.
- **Collaborator-initiated changes**: option (beta) to allow downstream collaborators to submit their own field-initiated PCOs.
- **SOV link**: SOV line-item values from change objects reflect into the Budget tool (Standard Budget View).
- **POV dictionaries (audience vocabulary)**: same machinery renamed per audience — GC view "Prime Contract Change Order" on "Prime Contracts" tool with "Subcontract/Subcontractor"; Owner view "Funding Change Order" on "Funding" tool with "Contract/Contractor"; Specialty contractor view "Client Contract Change Order" on "Client Contracts" tool. Also "Invoicing" vs "Progress Billings" tool naming.
- **Related glossary instruments**: Construction Change Directive (CCD) = "legal command initiated by the Owner... typically after a disagreement, that directs a Contractor to abide by a mandatory order. It differs from a change order in that a change order is subject to an agreement between the two parties." Changed Condition = unanticipated condition not reasonably expected when the contract was entered. Client Request = change in performance of work initiated by the client. Backcharge = money a buyer holds back from a seller to recover costs of the seller's incomplete/defective work.

### InEight Change (evidence layer A for its own claims, Tier-2 product page)

- Positioned as "Construction Change Order Management" — a standalone change module that can be implemented alone, combined with modules, or within the full platform; capital construction context.
- **Issue tracking**: "Track the entire change lifecycle from identification through approval... Log and manage every construction issue with a clear record of description, cause, scope, and responsible party."
- **Impact analysis**: "Evaluate how each potential change affects the project timeline and budget before decisions are made. By linking issues to project financials and routing them through a standardized change order approval workflow..." — cost AND schedule impact assessed pre-decision.
- **Visibility**: "continuous updates on pending and approved construction change orders"; tracking "from the field to the office in one centralized process."
- **Compliance/documentation**: "complete change order details alongside full contract data... Built-in audit trails... resolve disputes"; tracking pricing, responsible parties, schedule impacts, work areas in one place.
- **Users (self-described)**: contract administrators, project managers, and team members tracking issues, routing approvals, managing change orders.
- Screenshot asset named "PCOSummary" (PCO terminology in use); platform neighbors: Contract (contracts and payments), Control (budget/forecast), Billings.

### CMiC (evidence layer A for its own claims, Tier-2 business-needs page)

- ERP-embedded change order management on a "single database platform" with embedded project controls.
- **Cascade**: "When a change order is created, you can simply approve the change order request, and the system will automatically create all the necessary changes to the subcontracts."
- **Anticipation**: "With the ability to anticipate potential change requests, your project team can predict how unexpected costs will affect your project budget — and how to bill your subcontractors and suppliers accordingly."
- Scope-creep control, real-time synchronization of owner requests and updates to stakeholders; alignment with "the original and proposed contract terms."
- Related article title uses "PCO Construction & Change Orders" (potential change order terminology in the ERP context too).

### BuildBook (evidence layer A for its own public feature list; market context only)

- Residential custom builder/remodeler client-experience product. Public feature index lists: Sales Proposal, Estimating, Job Costing, Scheduling, **Client Selections**, Budgets, Invoices, Client Dashboard, Daily Logs, etc. — **no change-order feature page** in the headline feature set.
- Reading (weak, market-context): in the residential client-facing pole, client-approved changes are often organized around "client selections" (choose a different tile → budget changes) and budget/invoice updates rather than a formal multi-tier change order register. This is a single observation from a feature list; treated as a signal, not a finding.

## Cross-product Comparison

| Dimension | Procore | InEight Change | CMiC | Shared? |
|---|---|---|---|---|
| Change as formal contract-relative record | CO on prime contract / commitment / funding / client contract | change orders with "full contract data" alongside | COs tied to contracts/subcontracts on one database | Yes (A×3) |
| Identification-stage precursor object | Change Event (+PCO) | Issue (description, cause, scope, responsible party) | "potential change requests" | Yes (A×3, different names) |
| Quote/pricing solicitation to vendors | RFQ to subcontractors with cost+schedule response | implied in standardized workflow | implied ("bill your subcontractors and suppliers accordingly") | Yes (strongest in Procore, A) |
| Grouping/package for review | PCO → COR → CO (2/3-tier) | PCO summary; lifecycle identification → approval | change order request → approve → auto sub changes | Yes (A×3) |
| Approval by counterparty/owner | explicit (owner approves prime COs; downstream approves CCOs) | "standardized change order approval workflow", approvals routed | "approve the change order request" | Yes (A×3) |
| Cost impact itemization | SOV line items per change | pricing tracked per change | budget prediction | Yes (A×3) |
| Schedule/time impact | change events affect schedule; RFQ responses include schedule impact | schedule impacts tracked per change; timeline impact analysis | schedule alignment emphasis | Yes (A×3) |
| Budget reflection, pending vs approved | Budget columns: Pending Changes vs Approved Changes | links issues to project financials; update forecasts immediately | predict effect on project budget | Yes (A×3); the explicit pending/approved split observed in Procore only |
| Downstream cascade (owner CO → sub COs) | prime PCO + commitment PCO from same change event; CCOs | — (not stated on fetched page) | "automatically create all the necessary changes to the subcontracts" | Yes (A×2) |
| Backcharge / cost recovery from vendors | documented use of change events for backcharges | — | — | Single-product (Procore) |
| Status model granularity | 11 default statuses incl. pending-pricing / proceeding / not-proceeding / revised / void / no-charge | status of every change order tracked | — | Fine-grained states = product-specific; draft/pending/approved/rejected family = cross-product |
| Audience vocabulary layer | POV dictionaries (GC/owner/specialty) | contract administrator language | ERP/GC language | Multi-party vocabulary is a real market structure (A×2: Procore POV table + CMiC subcontract cascade) |
| Audit trail / dispute posture | approved-change edit restrictions; permissions | built-in audit trails, dispute resolution | real-time sync "avoiding potential disputes" | Yes (A×3) |
| Packaging | platform module (Project Financials) | standalone module or platform module | ERP-embedded | Packaging varies; all three = module of a larger system |

## Canonical Model (synthesis)

### L0 — Defining Invariant (minimal)

1. **Contract-relative change records** — changes are captured as discrete, documented change objects attached to a specific contract on the project (an upstream contract with the client/owner, or a downstream commitment with a vendor/subcontractor). Without attachment to a contract, it is a generic change log, not this Type.
2. **Itemized commercial impact** — each record itemizes the scope change and its cost impact (and, in mature practice, its schedule impact), accumulating to a revised contract amount. Without itemized impact it is a note, not a change order.
3. **Counterparty approval gate** — a record advances from proposed to executed only through a recorded review/approval (typically the party who must pay or accept the change). Without the approval gate it is a claim or a directive, not change order management.
4. **Execution into project money** — the approved change updates the contract/committed amount and flows into the project's financial machinery (budget, billing). Without execution, the tool is a document generator, not management.

Historical check (paper-era and regional products): a paper change order on a contract form satisfies all four properties (record, itemization, agreement/signature, contract modification); UK-style "variation orders" satisfy the same structure under different names; older construction ERP change order modules (register + pricing + approval + contract update) satisfy it too. The definition does not depend on the modern platform form.

### L1 — Common Mature Structure

- Identification-stage precursor objects (potential change / issue / change event) capturing cause, description, responsible party before money is agreed
- Quote solicitation to vendors (RFQ) with cost + schedule responses feeding pricing
- Multi-stage progression with grouping (potential change(s) → request package → change order) and a configurable number of steps per contract
- Status model: draft; pending family (in review / being priced / proceeding or not while pending / revised); approved; rejected; void/withdrawn; no-charge
- Schedule-of-values line items per change; budget views distinguishing pending vs approved change values
- Time/schedule impact tracked alongside cost; time-only changes possible
- Revisions, attachments/documents, signatures, audit trail
- Change reason/type taxonomy (owner request, design error/omission, unforeseen conditions, substitutions)
- Register/dashboard across all changes: status, values, net contract change, pending exposure
- Cascade across contract tiers: one root change priced up to the client and down to vendors
- Integration into budget, commitments, billing, schedule; links to RFIs/drawings/daily logs

### L2 — Variant / Optional Structure

- Audience POV (GC vs owner-side capital program vs specialty contractor vs residential client-facing) — same machinery, different vocabulary and emphasis
- Pricing forms (agreed lump sum, unit rate, documented time-and-material work), markups/overhead handling, contingency funding of changes (not directly evidenced in fetched pages — inferred weakly from "latest cost/latest price" cost-basis FAQ and industry practice; keep weak)
- Field-initiated changes submitted by downstream collaborators
- Backcharges / non-client cost recovery as change objects
- Owner directives (e.g. CCD-style instruments) and the claims path when agreement fails
- Public-sector/private owners; design-build delivery; multi-prime contracts
- Terminology: change order / variation / change request / potential change order naming varies by market and contract form

### L3 — Vendor-specific (research notes only)

- Procore: PCO/COR/COBLI names; tier settings per tool; 11 default statuses with exact labels; POV dictionaries (Owner Terminology V2, Specialty Contractor Terminology); "No Charge" and "Pending – Not Proceeding" semantics; Standard Budget View columns; field-initiated PCO beta; "cannot change tier setting after first CO" rule
- InEight: Issue object with description/cause/scope/responsible-party fields; PCOSummary; module names (Contract, Control, Billings, Plan & Progress)
- CMiC: single-database platform claims; auto-creation of subcontract changes on approval
- BuildBook: no change-order feature page; Client Selections/Budgets as the residential change surface (signal only)

## Vendor-specific Findings

- Procore's three-tier configuration (1/2/3 steps) is a vendor-specific formalization of an industry practice (multiple review rounds before a combined contract change is signed); the 2-tier PCO→CO default and the 3-tier COR mechanism should not be generalized as universal.
- Procore's "Pending – Proceeding / Not Proceeding" distinction (whether work proceeds before approval) is product-specific naming of a real industry concept (work proceeding at risk); treat as common concept, product-specific mechanics.
- CMiC's automatic subcontract update on approval is vendor-specific machinery; the general pattern (prime change cascading to sub changes) is cross-product (Procore supports parallel prime/commitment PCOs from one change event).
- InEight's issue-first capture (cause + responsible party per issue) is its own flavor of the identification stage.

## Boundary Findings

- **vs Construction Cost Management**: cost management spans budget, commitments, forecasts, cash flow, and billing; change order management is the specific machinery for *contract changes*. Remove the contract-relative change lifecycle → cost management continues functioning (budgeting/forecasting). Remove the change machinery from a cost platform → a large hole appears exactly where contract changes live, but budgeting still exists. Different centers of gravity: money-over-time vs change-to-contract.
- **vs Construction Contract Administration**: broader (contracts, payments, insurance, bonds, compliance). Change orders are one instrument within contract administration; the change record with itemized impact is this Type's center, not the contract file.
- **vs Progress Billing**: billing *consumes* approved changes (change orders appear as billing line items; Procore notes grouping approved COs into a combined change order for final signature when billing requires it). A billing application is defined by the periodic billing cycle; it does not manage change proposals, pricing negotiation, or rejection.
- **vs Construction Claims Management**: the decisive seam is *agreement*. A change order records an agreed change (glossary: "subject to an agreement between the two parties"); a claim asserts additional payment/time when agreement is absent; directive-style instruments (CCD) impose an owner command after disagreement. A dedicated change order tool manages the agreement path; it does not adjudicate disputes.
- **vs RFI Management**: an RFI asks a question; it may *surface* a change but carries no price, no contract attachment, no approval-to-execute.
- **vs Submittal Management / Construction Field Management**: unrelated objects (shop drawings, quality/safety).
- **vs Engineering Change Management (§16)**: shares the word "change" and the proposal→review→approve shape, but the world is different: ECM changes *product/design data* (ECR/ECN against parts, BOMs, revisions) in manufacturing; construction change order management changes *contracts' scope/price/time* among commercial parties with payment consequences. Remove the commercial contract/counterparty structure → ECM; remove the design-data/BOM structure → this Type. Distinct Types despite surface similarity.
- **vs Purchase Order Management**: POs (and PO change orders) are procurement transactions; a commitment change order on a PO-shaped contract is a CO-management object, but purchase order management is defined by the procurement order lifecycle, not by contract-scope change machinery.
- **vs Approval Workflow Platform**: generic routing lacks the contract-relative object, itemized SOV/impact, and execution-into-money semantics.
- **Type standing**: the leaf stands as a Type of its own — there is a named market category ("construction change order management software", per InEight's own headline), the object model and lifecycle are stable across products, and it is sold standalone as well as embedded.

## Uncertainties

1. **Residential/SMB pole under-sampled** — Buildertrend/JobProgress/CoConstruct unreachable; only BuildBook's feature list (no change-order page) as a signal. Whether residential client-facing products implement a full change-order register or mostly "selections + budget change" flows is not confirmed. The L0 is written so that a client-approval flow still fits (contract-relative, itemized, approved, executed into budget/billing).
2. **Pricing forms** (lump sum / unit rate / T&M / allowances / markup rules) are standard industry content but were not directly evidenced in the fetched pages (only a cost-basis FAQ title and generic "pricing" mentions). Kept at qualified strength; no defaults or formulas asserted.
3. **Owner-side capital-program tools** (e-Builder, Unifier, Kahua) unreachable; the owner-side perspective is evidenced indirectly via Procore's owner dictionary/funding tier and CMiC's owner-request language. No owner-side-specific claims made.
4. **Whether every product tracks schedule impact** as a first-class field (Procore RFQ responses and InEight do) vs schedule-only-in-documents — asserted as common, not universal.
5. Exact status lists, approval limits, notification timing, and signature mechanics are product-specific; none asserted in the final document beyond the conceptual state family.
6. "Variation order" terminology claim is general industry knowledge, not source-verified this pass; kept as a terminology note only.

## Final Synthesis

A construction Change Order Management application is the system of record for the *change-to-contract* lifecycle on a construction project: it captures identified changes to any contract's scope (from any party), itemizes their cost and schedule impact, solicits and consolidates pricing, routes the change through review to the counterparty's recorded approval, and executes the approved change into the contract amount and the project's budget and billing. Its defining shape is four properties — contract-relative records, itemized impact, counterparty approval gate, execution into project money. Around that core, mature products add identification-stage precursors, quote loops, multi-stage grouping, status models separating pending from approved money, register/dashboard views, cascades across contract tiers, and audit trails for dispute defense. The Type sits between Construction Cost Management (its usual host and broader sibling), Progress Billing (its downstream consumer), Construction Claims Management (the disagreement path it is designed to avoid), and Engineering Change Management (a same-word/different-world manufacturing Type).
