# Research Notes — Construction Contract Administration

Research date: **2026-09-07**

## Research Goal

Understand what a Construction Contract Administration application is from real products: what the contract object is in construction software, what machinery hangs on it (value, schedule of values, retainage, payment applications, compliance documents), what lifecycle a contract moves through, who operates it from which side of the money, and where its boundary sits against neighboring Types — especially Business Contract Administration / CLM (§10/§11), Change Order Management (§17, processed), Progress Billing (§17, unprocessed), Construction Cost Management (§17, unprocessed), and Construction Closeout Management (§17, processed).

## Initial Boundary (pre-research hypothesis)

- Core purpose: system of record for the executed contract file on a construction project — the upstream contract (owner ↔ contractor) and downstream commitments (subcontracts, purchase orders) — held as structured financial records with contract-relative money machinery: schedule of values, payment applications, retainage, contract closeout, plus compliance documents (insurance, bonds, lien waivers).
- Users: contract administrators, project managers/engineers, cost engineers, owners' reps, GC financials teams.
- Neighbors: generic CLM (repository + lifecycle + obligation dates, no construction money machinery), Change Order Management (owns the change instrument lifecycle), Progress Billing (owns the billing cycle), Construction Cost Management (budget/forecast), Construction Document Management (storage), Construction Claims Management (disagreement path).
- Risks: (a) the leaf may collapse into generic CLM as an industry alias — the prior business-contract-administration pass flagged it as an "industry sibling with change orders/progress billing"; (b) retainage/billing may overlap Progress Billing; (c) the leaf may be only a module of Construction Project Management. Must establish whether the market recognizes it as a distinct, nameable category.

Market validation of the category name: InEight sells "InEight Contract — Construction Contract Management Software"; Kahua sells "Construction Contract Management Software" as a named solution page ("Change & Contract Management"); Procore ships dedicated Prime Contracts / Commitments tools and defines "Contract Administration (CA)" in its glossary as "the practice of planning, negotiating, authoring, executing, and ensuring compliance with the terms and conditions of a construction contract." The category is nameable and distinct in the market.

## Research Questions

1. What contract objects exist (prime contract, client contract, commitment, subcontract, PO, funding) and what structured fields do they carry?
2. What lifecycle/status does a contract carry, and which actions change it (approval, signature)?
3. What money machinery is attached directly to the contract: schedule of values, payment applications/invoices, retainage, payments received/issued, closeout?
4. What compliance machinery is contract- or vendor-attached (insurance certificates, licenses, bonds, lien waivers), and does it gate payment?
5. How do change records attach to contracts (boundary vs Change Order Management)?
6. How does the two-direction structure work (money in from the funding party, money out to performing vendors), and how do the same contracts look from different audience positions?
7. How does this Type differ structurally from generic CLM?
8. Packaging: platform module, standalone module, ERP component?

## Representative Products

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| Procore | Multi-party construction platform; market leader; richest public Tier-1 docs | Defines the prime-contract / commitment model with per-audience naming |
| InEight Contract | Standalone contract-management module of a project-controls suite; enterprise capital projects | Purest product-centering on contracts + payments + compliance |
| Kahua | Owner-side and delivery-team platform ("system of record for owners and delivery teams") | Owner/program-side operation of the same machinery |
| CMiC | Construction ERP, single-database financials-first | ERP posture: contracts/subcontracts inside corporate accounting |

Unreachable / not sampled: Oracle Primavera Unifier (docs 404 ×2 — the classic owner-side capital-contract system is structurally represented by Kahua + InEight instead), Autodesk Construction Cloud, Trimble e-Builder (JS/blocked in the prior change-order pass), Buildertrend/CoConstruct (residential SMB; 403/404 in prior pass). No claims drawn from these.

## Sources

Successfully fetched 2026-09-07:

1. Procore Support — Glossary of Terms — https://support.procore.com/references/construction-management/glossary-of-terms (Tier 1; extracted definitions: Contract Administration ×2, Prime Contract, Client Contract, Commitment, Subcontract, Purchase Order, Funding, Retainage, Retention, Schedule of Values, Lien Waiver, Performance Bond, Pending Revised Contract, Stored Materials, Progress Payment, Insurance Manager, AIA Billing, G702/G703, Multiple Prime Contracts/Client Contracts/Fundings, Bond, Claim)
2. Procore Support — Prime Contracts tool landing page — https://support.procore.com/products/online/user-guide/project-level/prime-contracts (Tier 1)
3. Procore Support — Commitments tool landing page — https://support.procore.com/products/online/user-guide/project-level/commitments (Tier 1)
4. Procore Support — "About the Prime Contracts Tool" tutorial — https://support.procore.com/products/online/user-guide/project-level/prime-contracts/tutorials/about-the-prime-contracts-tool (Tier 1)
5. Procore Support — "Enable Retainage on a Purchase Order or Subcontract" tutorial — https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/enable-retainage-on-a-purchase-order-or-subcontract (Tier 1)
6. InEight — "InEight Contract" product page + FAQ — https://ineight.com/contract (Tier 2)
7. InEight — "Software Capabilities for InEight Contract" capability matrix — https://ineight.com/software-capabilities-for-ineight-contract/ (Tier 2, detailed function/capability/why-it-matters table)
8. Kahua — "Construction Contract Management Software" solution page ("Change & Contract Management") — https://www.kahua.com/solutions/contract-management (Tier 2)
9. CMiC — "Change Order Management" business-needs page — https://www.cmicglobal.com/products/business-needs/change-order-management (Tier 2)
10. CMiC — "Construction Financials / Accounting" product page — https://www.cmicglobal.com/products/construction-financials/accounting (Tier 2)

Prior-pass sources reused for cross-boundary consistency: Procore change-order FAQ set + glossary (research/change-order-management.md), business-contract-administration research + application docs, construction-closeout-management research + application docs.

Unreachable (abandoned after 1–2 failures per network rules): Oracle Unifier docs (404 ×2), CMiC guessed contract URLs (404 ×2), Autodesk/Kahua-support not attempted further.

## Product Observations

### Procore (multi-party platform — evidence layer A unless noted)

- **Prime Contracts tool**: "create and manage a contract with an upstream client, and keep track of all change orders and related items." Create a prime contract with a comprehensive schedule of values (import CSV or add line items manually by cost code); manage contract access permissions; email completed contracts to stakeholders and change the contract status when approved; manage the Prime Contract Change Order (PCCO) process and approval workflow.
- **Contract register**: data table listing all contracts on the project; filter/sort/group (e.g., "see all the contracts in the 'Draft' status… or all contracts for a specific contractor or vendor"); status shown inline and editable by permitted users; expandable drawer listing associated change orders; grand totals for currency columns; export to DOCX/PDF.
- **Contract lifecycle actions**: Approve a Prime Contract; Edit; Delete; View Change History; Export; Create a Payment Received for a Prime Contract. Owner Invoices (billing the client) live inside the Prime Contracts tool (Beta tutorials: About / Create / Edit / Delete / Email / Export / Summary Preview).
- **Commitments tool**: "see the status and current value of all contracts and purchase orders. Easily pinpoint which contracts have been approved or determine the status of invoices and payments. Procore can be customized to produce your company's contract documents." Tutorials: Create a Commitment; Create Subcontracts; Create Purchase Orders; Approve and Sign a Subcontract; View Inclusions/Exclusions on a Subcontract; Enable Retainage on a Purchase Order or Subcontract; Add a Schedule of Values to a commitment; Subcontractor SOV (vendors invited to create their own SOV); Payments Issued tab; Create a Payment Schedule (AU/NZ legal notice); sliding-scale retention rules on subcontractor invoices (AU).
- **Retainage mechanics (tutorial)**: retainage enabled per contract under Advanced Settings → Invoice; two types — Completed Work Retainage and Stored Material Retainage; availability depends on the contract's accounting method (Amount-Based vs Unit/Quantity Based); release happens through subcontractor invoices ("Set or Release Retainage on a Subcontractor Invoice"); a warning banner appears on subcontractor invoices when retainage is released (release note).
- **Glossary definitions** (vendor-stated): Commitment = "a purchase order or subcontract. Both commitment types are contracts that represent a legally enforceable financial agreement between two parties." Prime Contract = owner-financed agreement with the general contractor; single or multiple per project. Client Contract = the same object named from the specialty-contractor side. Funding = funding-source ↔ contractor agreement. Subcontract = third party engaged for part of prime work. Retainage = "withholding of a portion of a contract amount until the work is deemed satisfactorily complete… A common practice is to withhold 5-10%…" (vendor-stated figure). SOV = "list of line items that details all of the agreed-upon costs… itemizes the contract amount into individual pay items… commonly used to determine progress payments." Lien Waiver, Performance Bond, Bid Bond defined. Insurance Manager = internal role ensuring contractor/vendor insurance policies and certificates are compliant and up to date. AIA Billing + G702/G703 = standardized pay-application forms. Pending Revised Contract = calculated column (Revised Committed + Pending Change Orders) — change machinery directly computed into contract value.
- **Configuration & governance**: granular permissions per tool; configurable fieldsets (required/optional/hidden); custom numbering for financial objects; privacy settings per commitment; ERP integration with accounting-acceptance workflow for commitments and change orders; DocuSign integration on contracts; (Beta) custom workflow templates for Prime Contracts/Commitments; "Restrict Non-draft edits to Contracts and Change Orders" setting; "Enable Always Editable Schedule of Values" setting; multiple prime contracts per project supported (with a FAQ on system limitations).
- **Audience-relative naming** (FAQ title verified; details from prior pass): the same tool family is named Prime Contracts (GC view), Client Contracts (specialty-contractor view), Funding (owner view).

### InEight Contract (standalone module of a project-controls suite — layer A)

- Positioning: "Centralized Contract Management for Capital Construction… manage your capital projects from procurement to closeout with InEight Contract, centralizing all contracts and related data."
- **Contract creation & lifecycle**: create, store, and manage contracts and subcontracts through closeout; monitor status "from award through change orders to closeout"; real-time dashboards surface pending actions such as unsigned contracts and outstanding approvals.
- **Automated contract generation**: templates + auto-fill; "the built-in Contract Writer uses your entered data to populate clauses, terms, and schedules."
- **Bid-to-contract conversion**: "convert a winning bid or estimate into a contract record with a single click, automatically populating scope, values, and vendor details."
- **Approval workflows**: multi-step flows based on contract value, role, or department; enforce signing authority; automated notifications; built-in audit logging.
- **Custom fields**: e.g., "insurance requirements, jurisdiction clauses, or internal KPIs."
- **Documents & e-signature**: attach all contract documents (PDFs, exhibits, addenda); route for e-signature via DocuSign; signatures captured and versioned.
- **SOV & line items**: "detailed Schedule of Values with unit prices, quantities, and total values for each contract line. As field progress… is reported, the system automatically calculates earned revenue per line item… maintain visibility into unbilled amounts." Multiple contracts per project with independent terms/values/progress.
- **Change logging in contract**: sync approved changes, updating revised contract values with full history; "every contract amendment—including dates, amounts, and approvals—is recorded." (Change machinery itself lives in the sibling product InEight Change; vendor change orders (VCOs) tracked within each contract record.)
- **Vendor management & compliance**: centralized directory of contractors and vendors "complete with insurance certificates, licensing information, and performance metrics. Automated reminders flag upcoming expirations or missing documentation." (Compliance is also a separate sibling product.)
- **Retention management**: track retention terms per contract; calculate withheld amounts per invoice; monitor release schedules; "a dedicated retainage ledger… alerted when retention milestones or release conditions are met."
- **Payments**: progress payment invoicing based on the SOV (current/previous/cumulative billed); payment applications generated from field-reported progress; retainage calculation; batch invoices; attach backup (timesheets, installed-quantity reports). Invoice review & approval workflows with multi-tier paths and dollar thresholds; timestamped audit trail. Payment statuses "invoice received, approved, paid, and disputed"; accruals; aging reports. Subcontractor invoice portal: vendors submit pay requests, enter progress quantities/payroll/change amounts, view status.
- **Financials integration**: committed vs uncommitted costs; actuals captured from ERP; bi-directional ERP integration ("single source of truth between project teams and corporate finance").
- **Packaging boundary evidence**: the InEight platform ships separate Billings, Change, Compliance, and Completions products — the Contract module is the contract record + payment tracking center, not the whole billing/cost stack.

### Kahua (owner/delivery platform — layer A)

- Positioning: "Manage contracts, commitments, change orders, pay requests, approvals, and budget impacts in one connected project record."
- "Construction contract management software helps teams manage the contract record as work changes. In Kahua, contracts stay connected to the financial and approval activity around them, so teams can understand what changed, who approved it, and how each decision affects the project."
- Change requests tied to "the work, vendor, and contract"; approved requests move into change orders "without rebuilding the record"; audit trail keeps "contracts, changes, signatures, attachments, approvals, and comments together so teams can answer questions later."
- Connect contract and cost activity with ERP, accounting, reporting, project controls.
- Named users: "Owners, general contractors, construction managers, program managers, project controls teams, procurement teams, finance teams, and compliance stakeholders."
- Sibling solutions confirm the seams: Sources of Funds, Cost Management, Audit & Compliance Controls, Budget & Cashflow Management are separate named capabilities.

### CMiC (construction ERP — layer A, lighter depth)

- Financials: AP, AR, Billing, Consolidated GL; "flows everything into both your general ledger and your job costing simultaneously."
- Cost Management: "manage job and labor costs, inventory, equipment, materials, and subcontracts — all in one place." Financial reporting "including owner contract, invoicing, cash receipts and projections."
- Change order machinery (prior-pass page): approving a change order request "will automatically create all the necessary changes to the subcontracts" — contract records and their changes live inside the ERP database.
- Integration seam: Oracle Textura listed as the "Subcontractor Payment Management" partner integration.

## Cross-product Comparison

| Dimension | Procore | InEight Contract | Kahua | CMiC |
|---|---|---|---|---|
| Contract object | Prime Contracts + Commitments (subcontracts/POs) + Funding; audience-relative names | Contracts and subcontracts (all types), procurement→closeout | Contracts + commitments in one connected record | Subcontracts/owner contracts inside ERP financials |
| Contract as structured record | Yes — register, statuses, configurable fields, values | Yes — contract records with scope, terms, line items, SOV | Yes — "the contract record as work changes" | Yes — ERP objects |
| Value maintenance on record | Original/revised/pending COs (PRC column) | Revised values updated from synced approved changes with history | Budget impacts visible with each decision | Single-database propagation |
| Schedule of values | Core (SOV per contract + subcontractor SOV) | Core (unit prices, quantities, earned per line) | Implied via pay requests/budget | Inside ERP billing/job cost (not directly evidenced) |
| Payment applications/invoices | Owner invoices on prime contracts; subcontractor invoices with invite-to-bill; payments issued/received tabs | Pay apps from SOV; statuses received→approved→paid→disputed; vendor portal | Pay requests in the connected record | Billing app + Textura for sub payment |
| Retainage | Enabled per contract; completed-work + stored-material types; release via invoices; AU sliding scale | Retention terms per contract; per-invoice withholding; dedicated retainage ledger; release alerts | Not directly evidenced | Retainage cash-flow article exists; product detail not verified |
| Compliance docs | Insurance Manager (role), glossary certs/bonds/lien waivers | Vendor directory with insurance certs, licensing, expiry reminders | Compliance stakeholders named as users; audit & compliance solution | Not directly evidenced |
| Approval workflow | Status changes + (Beta) workflow templates; approve actions | Multi-step by value/role/department; signing authority | Approvals preserved in audit trail | Approval triggers auto-propagation |
| E-signature | DocuSign integration | DocuSign | Signatures in audit trail | Not evidenced |
| ERP/accounting integration | Export + accounting acceptance | Bi-directional, single source of truth | Connect ERP/accounting/reporting | Is the ERP |
| Change linkage | PCCO/CCO on contract; CO drawer | Change log in contract; VCOs | Change requests→change orders tied to contract | Auto-created subcontract changes |
| Where change machinery lives | Separate Change Orders tool | Separate InEight Change product | Same solution page (change-centric framing) | Same ERP module |
| Where billing machinery lives | Invoicing under Prime Contracts/Commitments | Separate InEight Billings product (pay apps inside Contract) | Pay requests inside contract record | Billing app in Financials |

Reading of the comparison:
- The contract record + its value + payment attachment + lifecycle are present in all four (B).
- SOV and retainage are present where payment detail is directly documented (Procore, InEight) and implied elsewhere (B with qualification).
- Compliance documents are visible in three of four products (Procore glossary/role, InEight capability, Kahua stakeholder naming) — common, but with different depths (B; single-product depth for the retainage ledger detail).
- Audience-relative vocabulary (prime/client/commitment/funding) is structural in the sample (B), and audience-relative naming per operator is documented by Procore directly (A).
- Change machinery and (partly) billing machinery are organized *adjacent to* the contract record even inside the same product — supporting the directory's split of Change Order Management and Progress Billing as separate Types (B).

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as construction contract administration:

1. **Contract as structured project record.** Each executed agreement on a construction project is a system-owned record — identified counterparties, contract value, scope, dates — not a filed document. The agreements form the money skeleton of the project: the contract with the party funding the work, and the commitments to the parties performing it.
2. **Live value on the record.** The system maintains the contract's sum over time: original value, executed changes, revised value, pending movement. The contract's number is a maintained result, not static text.
3. **Contract-relative money movement.** Payments against the contract are requested, reviewed, and recorded on the record — payment applications/invoices reference the contract, accumulate against it, and payments issued/received are tracked against it, with amounts withheld under the contract's terms (retainage) carried by the record.
4. **Managed contract lifecycle.** The record moves through states — drafted, routed, approved/executed (signature recorded), active, completed/closed — with an audit trail of who did what.

Test against §24 (historical check): pre-software construction contract administration — the contract administrator's file of contract documents, measured work against the schedule of values, payment certificates, retention account, variation register, and final certificate — satisfies all four invariants on paper. Regional/administrative traditions (AIA architect-administration, UK QS interim certificates, owner capital-program contract offices) fit. The definition is not over-fitted to current cloud platforms.

### L1 — Common Mature Structure

Present across the sample; makes the Type workable but does not define it:

- **Schedule of values** — line-item breakdown of the contract sum (unit prices, quantities) used to compute earned amounts; subcontractor-authored SOVs in multi-party flows.
- **Retainage/retention machinery** — per-contract withholding terms, per-payment calculation, release at milestones/completion, dedicated ledgers, regional variants (sliding-scale retention).
- **The two-direction commitment structure** — upstream contracts and downstream subcontracts/POs administered as one object family, with changes cascading across tiers.
- **Contract documents & execution** — attachments (executed agreements, exhibits, addenda), e-signature, templates/auto-generation, bid-to-contract conversion.
- **Approval workflows with authority** — multi-step, value-threshold/role-based routing, signing-authority enforcement, audit logging.
- **Vendor compliance documents** — insurance certificates, licenses, bonds tracked against vendors/contracts with expiry reminders; lien waivers in the payment flow.
- **Payment status tracking** — invoice received → approved → paid → (disputed); payments issued/received tabs; accruals/aging.
- **Register & reporting** — project-level contract list with statuses/totals/filters; contract summaries (original, approved changes, pending, revised); committed vs uncommitted views.
- **ERP/accounting integration** — export/sync of contracts, changes, invoices for accounting acceptance.
- **Multi-party collaboration** — external collaborators see and act on their contracts through portals; privacy per contract.

### L2 — Variant / Optional Structure

- **Audience-relative packaging and naming** — prime contract vs client contract vs funding vs commitment; the operator's seat (GC, owner, specialty contractor) renames the same structures.
- **Funding sources as first-class objects** — owner-side capital programs track fundings parallel to contracts.
- **Compliance depth** — from a tracked certificate register to dedicated compliance products/modules (prequalification, licensing, bond tracking).
- **Regional payment machinery** — AU/NZ sliding-scale retention and payment schedules are documented; other regional regimes (UK schemes, civil-law retention variants) are expected but not source-verified this pass.
- **Segment weight** — residential/SMB implementations run lighter client-approval flows; capital/enterprise implementations carry formal multi-tier registers.
- **Cost-management adjacency** — committed-cost rollups and budget integration may live in the contract tool, a sibling cost module, or an ERP depending on packaging.
- **AI assistance** (era-current, present in the wider construction-platform market; not a defining structure).

### L3 — Vendor-specific (research notes only)

- Procore: PCCO/CCO/PRC terminology, Insurance Manager, Client Contracts/Funding tool renaming, per-tool permission templates, ERP "accounting acceptance" workflow, DocuSign fields FAQ.
- InEight: Contract Writer, vendor change orders (VCO) label, dedicated retainage ledger, Billings/Change/Compliance/Completions as separate products.
- Kahua: kBuilder Canvas, kCapture, "sources of funds" solution naming.
- CMiC: single-database auto-propagation, Oracle Textura partnership for subcontractor payments.

## Vendor-specific Findings

See L3 above; none promoted to the canonical core. The glossary's "5-10% common retainage" figure is vendor-stated and is not asserted in the final document.

## Rejected Findings

- **Change order machinery as part of the core** — rejected: products deliberately organize change management adjacent to (or inside, but distinct from) the contract record; the directory already carries Change Order Management as its own processed leaf. This Type holds the contract the changes attach to.
- **The full billing cycle as core** — rejected as definitional: payment attachment to the contract is core (L0-3), but the periodic billing cycle's detail belongs to Progress Billing; InEight literally ships Billings separately while Contract still tracks pay apps and statuses.
- **Budget/forecast/cash flow** — rejected: belongs to Construction Cost Management; contracts feed committed-cost views but the budget is a different object.
- **Insurance/bond compliance as definitional** — rejected for the core: present commonly, but a contract file without compliance tracking is still recognizable contract administration.
- **"Commitment" as the canonical term** — rejected as vocabulary; the underlying payer-payee agreement structure is canonical, the label is audience-relative.
- **Multi-prime/funding complexity as core** — rejected: supported by the sample but a single-contract project still satisfies the Type.

## Boundary Findings

1. **vs Business Contract Administration / Contract Lifecycle Management (§10/§11).** Generic CLM centers on any-contract lifecycle: repository, obligations, key dates, negotiation/redlining. Construction contract administration centers on project-anchored, money-bearing contracts: schedule of values, retainage, payment applications, commitment structure, compliance certificates. **Remove the construction money machinery (SOV, retainage, pay-app attachment) and you have generic CLM; remove the generic contract library (NDAs/MSAs not project-anchored) and add construction money, and you have this Type.** The two share lifecycle/approval/e-signature/AI, which is why they are easy to confuse; the market keeps them distinct (legal-tech vendors vs construction platforms). Prior business-contract-administration pass already recorded this leaf as "industry sibling with change orders/progress billing" — consistent with this pass.
2. **vs Change Order Management (§17, processed).** Change records are instruments administered *on* contracts; that leaf owns the change lifecycle (identification → pricing → approval → execution). This leaf owns the contract file the changes modify, and computes their effect into contract value. Products confirm the seam: Procore's change machinery is a separate tool; InEight ships Change separately. Consistent with the change-order pass's boundary note ("broader: covers the whole contract file").
3. **vs Progress Billing (§17, unprocessed).** The billing/pay-application cycle is the payment machinery's detail; this Type holds the contract-side anchor (contract value, SOV, retainage terms, payment tracking). **Flag for joint review with the progress-billing pass**: InEight bundles pay apps inside Contract while shipping a separate Billings product; Procore puts invoicing under Prime Contracts/Commitments. The products do not draw the line where the directory draws it; the directory's split is defensible (billing cycle vs contract record) but must be honored by the progress-billing pass from the other side.
4. **vs Construction Cost Management (§17, unprocessed).** Budget, forecast, and cash flow are cost objects; contracts feed them as commitments. Remove payment/SOV/retainage from this Type and add budget/forecast and you have cost management.
5. **vs Construction Closeout Management (§17, processed).** Closeout owns the project-end phase (deficiencies, deliverables, acceptance). This Type owns contract-level completion: final payment, retainage release, contract closure. The closeout pass already noted retainage/lien mechanics live here.
6. **vs Construction Document Management.** Document management stores files; this Type maintains structured, value-bearing records that files merely attach to.
7. **vs Subcontractor Management (§17, unprocessed) / vendor prequalification.** Vendor performance and prequalification are vendor-centric; this Type is contract-centric — the vendor directory here serves the contract record (compliance certificates), not workforce/performance management.
8. **vs Purchase Order Management (§10).** Generic procurement PO lifecycle is an office/procurement workflow; in construction, POs appear as commitments — one instrument within the project contract file.

## Uncertainties

- Oracle Primavera Unifier (the classic owner-side capital-contract system) unreachable; owner-side structure rests on Kahua + Procore owner mode (funding tools). No Unifier-specific claims made.
- Residential/SMB segment under-sampled (Buildertrend/CoConstruct unreachable in prior passes); the residential variant is described only as a lighter-weight expectation, without product claims.
- Exact default status lists for contracts were not directly verified (Procore's invoice-status FAQ not fetched); statuses described conceptually. Procore's "Draft" status as a contract status is documented.
- Non-US/CA/AU regional machinery (UK JCT/NEC interim certificates, payment-act notices) not source-verified — not asserted.
- CMiC's contract-administration depth (SOV, retainage screens) not directly evidenced; CMiC used only for the ERP-pole posture (B evidence, qualified).
- Kahua retainage/SOV detail not directly evidenced; Kahua used for record-connectedness, multi-party users, audit trail (A) and as packaging evidence.

## Final Synthesis

Construction Contract Administration is the construction-side system of record for the executed contract file of a project. Its defining core: contracts as structured project records (counterparties, value, scope) whose sums the system keeps live as changes execute; payment machinery attached directly to the contract (payment applications, payments issued/received, retainage withheld and released under the contract's terms); and a managed lifecycle from drafting through approval/signature to completion, with an audit trail. Around that core, mature products add the schedule of values, the two-direction commitment structure (subcontracts and POs as the same object family as the upstream contract), contract documents with e-signature and templates, value/role-based approval workflows, vendor compliance documents (insurance, licenses, bonds, lien waivers), payment-status tracking, registers and contract summaries, ERP integration, and multi-party portals. The market realization is uniformly as a module or tool family inside construction platforms and ERPs, with the operator's seat (owner, GC, specialty contractor) determining the vocabulary. The sharpest structural seam is with generic CLM (which lacks construction money machinery) and with Change Order Management / Progress Billing / Construction Cost Management, which own the change instrument, the billing cycle, and the budget respectively — the contract record is the object they all attach to.
