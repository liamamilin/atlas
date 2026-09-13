# Research Notes — Progress Billing

Research date: **2026-09-10**

## Research Goal

Understand what a Progress Billing application is from real products: what the recurring billing cycle on a construction contract looks like as software — the pay application / progress billing document as an object, how the amount due is computed from work completed to date, how retainage and change orders enter the computation, how the document moves through submission → review → certification → payment, who operates it from which side of the money, and where its boundary sits against neighboring Types — especially Construction Contract Administration (§17, processed; joint-review flag), Change Order Management (§17, processed), Construction Claims Management (§17, processed; "progress claims" polysemy), Project Controls Platform (§17, processed; forward note), Invoicing/Billing Platform (§08), and Accounts Receivable Management.

## Initial Boundary (pre-research hypothesis)

- Core purpose: the periodic billing cycle against a construction contract — the contractor (or subcontractor) bills the paying party for work completed to date via a recurring, cumulative billing document (pay application / progress billing / progress claim / application for payment), computed against the contract's schedule of values, with retainage withheld and approved change orders incorporated, submitted to the paying party, reviewed, revised, certified, and paid.
- Users: project accountants / billing specialists, project managers, controllers/CFOs (billing side); owner's reps, owner project accountants, construction managers (review side); subcontractors submitting through portals.
- Neighbors: Construction Contract Administration (holds the contract record the billing attaches to), Change Order Management (owns the change instrument that feeds billing), generic Invoicing (transaction-anchored one-off invoices), Billing Platform (§08 generic vendor billing), AR/Collections (downstream of certification), Construction Cost Management (the cost mirror).
- Risks: (a) the leaf may collapse into generic invoicing; (b) overlap with contract administration's payment machinery (the pre-hung joint-review flag); (c) the market name varies by region and seat (progress billing / pay application / progress claim / application for payment / AIA billing / interim application).

## Research Questions

1. What is the unit of record — the pay application / progress billing document — and what structure does it carry (billing period, SOV lines, previous/current/cumulative columns, retainage)?
2. How is the amount due computed (percent complete vs dollars vs quantities; stored materials; change orders; carry-over from previous applications)?
3. What lifecycle does the billing document move through (draft → submit → review line-by-line → revise & resubmit → approve/certify → paid), and who performs each step?
4. How do retainage and stored materials work in the billing cycle?
5. How do approved change orders enter the billing (timing rules, wrong-period warnings)?
6. How does the cycle mirror across tiers (GC→owner upstream, sub→GC downstream) and seats (GC, owner, specialty contractor)?
7. What compliance machinery rides on the billing (lien waivers, insurance certificates)?
8. What regional/form regimes exist (AIA G702/G703, GC-custom digitized forms, statutory progress claims)?
9. How does the billing basis vary (lump-sum SOV, unit price, T&M/cost-plus rates, one-off)?
10. Where does the billing cycle end and AR/collections/ERP accounting begin?

## Representative Products

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| Procore | Multi-party construction platform; market leader; richest public Tier-1 docs | Defines the invoicing/progress-billing tool family for GC, owner, and specialty-contractor seats with billing periods, invite-to-bill, line-item review, retainage |
| InEight (Contract + Billings) | Enterprise project-controls suite; splits SOV pay apps (Contract) from T&M/cost-plus billing (Billings) | Shows the suite-module packaging pole and the billing-basis split inside one vendor |
| Siteline | Standalone subcontractor-side billing SaaS | The purest standalone pole: pay apps built to each GC's specs, digitized forms, AR/collections extensions |
| GCPay (Autodesk) | Standalone GC-side pay-application exchange platform | The GC-side exchange pole: automated pay-app workflow between GCs and subs, lien waivers, compliance, e-payments |
| Knowify | SMB trade-contractor platform, QuickBooks-centric | The small-contractor pole: G702/G703 generation, retainage, CO timing warnings, ERP sync |

Unreachable / not sampled: Buildertrend (403 + timeout ×2 — residential builder pole unobserved, consistent with prior passes), CMiC billing page (404), Sage 300 CRE / Foundation (not attempted after sample saturation). No claims drawn from these.

## Sources

Successfully fetched 2026-09-10:

1. Procore Support — Invoicing tool landing page (Tier 1; tutorial catalog: Billing Periods create/manual/automatic/edit; Subcontractor Invoices about/create/invite-to-bill/on-behalf/SSOV/review/revise-resubmit/retainage set-release/payment schedule/export; Owner Invoices create/edit/email/export/summary preview/prefill/retainage/group-row billing; point-of-view dictionary table Invoicing↔Progress Billings; stored-materials and change-order release notes) — https://support.procore.com/products/online/user-guide/project-level/invoicing
2. Procore Support — "About Subcontractor Invoices" tutorial (Tier 1; commitment prerequisite 'Approved' status, billing period definition start/end/due date in Open status, invoice contacts vs invoice administrators, line-item review approve/reject, revise & resubmit until all lines approved, DocuSign, ERP export) — https://support.procore.com/products/online/user-guide/project-level/invoicing/tutorials/about-subcontractor-invoices
3. InEight — InEight Billings product page (Tier 2; T&M/cost-plus billing, rate tables by project/client/WBS, third-party markups with line-item exceptions, retroactive & future rate adjustments, billing status billed/approved/disputed, unbilled revenue, accruals, ERP integration, stand-alone or bundled) — https://ineight.com/products/ineight-billings/
4. InEight — Software Capabilities of InEight Billings (Tier 2; T&M billing capture, invoice review & approval workflow with audit logs, payment status & analytics, actual-cost integration, reporting & audit trail) — https://ineight.com/software-capabilities-of-ineight-billings/ (content verified via search index + product page cross-reference)
5. InEight — learn.ineight.com Billings start page + User Guide (Tier 1; "track, report on, and bill for cost reimbursable contracts… define project specific resource billing rates, markups, resource classifications, and generate billing batches"; rate tables with effective dates; Timecenter integration; bi-directional Platform integration WBS/Pay Items in, batched LEMs and invoices out) — https://learn.ineight.com/Billings/Content/Categories/TopicsStartPage.htm
6. InEight — Software Capabilities for InEight Contract (Tier 2; Progress Payment Invoicing: invoices from the SOV showing current/previous/cumulative billed, generated from field-reported progress and accepted quantities, retainage calculation, batch invoices, backup attachment; Subcontractor Invoice Portal: pay requests, progress quantities, payroll, change amounts, approval workflow, invoice ledger) — https://ineight.com/software-capabilities-for-ineight-contract/
7. Siteline — homepage + Pay App Management feature page (Tier 2; pay apps to each GC's specs, 23,000+ digitized forms from 17,000+ GCs, system-handled calculations and carry-over from previous months, taxes, over/under-billing vs costs, billing types lump sum/unit price/T&M/one-off, revision tracking, digital signatures, auto-submit to GC portals, ERP sync after GC finalization, lien waivers, compliance, change-order tracking with approved COs added to SOV, AR reporting, forecasting, collections, lien rights) — https://www.siteline.com , https://www.siteline.com/feature/construction-payment-application-software
8. GCPay — homepage (Tier 2; "automates the payment application process between general contractors and subcontractors"; AFPs processed; lien waivers; compliance documents; electronic payments; ERP integration; reporting; official AIA documents; GC/sub/PM personas; "approve and send off an owner bill") — https://www.gcpay.com
9. Knowify — AIA billing page (Tier 2; G702/G703 generation with retainage, stored materials, change orders handled automatically; auto-generated SOVs; enter completed work in dollars or percentages; approved COs included for the correct billing period with wrong-period warnings; official AIA forms via AIA Contract Documents partnership; retainage tracked by phase with reminders for separate release invoices; QuickBooks sync; pay-app advances via partner) — https://knowify.com/aia-billing/

Prior-pass sources reused for cross-boundary consistency: research/construction-contract-administration.md (Procore glossary: SOV, retainage, AIA billing/G702/G703, progress payment; InEight Contract pay-app detail), STATUS.md forward notes from project-controls-platform, subcontractor-management, construction-claims-management, construction-cost-management passes.

Unreachable (abandoned per network rules): Buildertrend (403 root, timeout help center), CMiC billing URL (404), InEight /billings and /products/billings (404 ×2 — correct URL found via search).

## Product Observations

### Procore (multi-party platform — evidence layer A unless noted)

- **Invoicing tool purpose (Tier 1)**: "simplify the invoice collection, review, and approval process on all of your construction projects… Generate accurate invoices for owner and subcontractor contracts; streamline the collection, review, and approval process with billing stakeholders; increase confidence that invoice amounts match work completed to reduce rework and prevent overbilling." Designed for users with Admin permission on Commitments and/or Prime Contracts.
- **Prerequisite chain (Tier 1)**: a subcontractor invoice "originates in the Project Commitments tool"; the commitment must be in 'Approved' status before an invoice can be created; a billing period must exist and be in 'Open' status; "a billing period defines the start, end, and due date for submitting an invoice." Billing periods can be created manually or automatically.
- **Two submission models (Tier 1)**: invoice contacts (downstream collaborators granted submission rights — "invite to bill", accept/decline, submit, revise & resubmit) vs invoice administrators (internal users who gather paper/digital invoices and create them on behalf of the vendor).
- **Line-item review (Tier 1)**: "Once submitted, an invoice administrator can review each line item on the invoice's Schedule of Values to approve or reject it"; if one or more lines are rejected, "users can make fixes and corrections until all the line items on the invoice's Schedule of Values are Approved." Optional DocuSign signature; optional ERP export.
- **SOV machinery (Tier 1)**: Subcontractor Schedule of Values (SSOV) created by admins or updated by invoice contacts; manage rows/columns on the invoice's SOV; group-row billing on owner invoices (Beta); owner-invoice prefill from costs; summary preview.
- **Retainage (Tier 1 tutorials + prior-pass glossary)**: set or release retainage on subcontractor invoices and on owner invoices; completed-work vs stored-material retainage types (prior pass); sliding-scale retention rules (AU); warning banner when retainage is released; stored materials on invoices incl. unit/quantity-based contracts; automated movement of stored materials.
- **Change orders on invoices (Tier 1 release notes)**: "Add and Remove Change Orders from Commitment Invoice"; change-order titles display on owner-invoice PDFs.
- **Owner side (Tier 1)**: create/edit/email/export owner invoices; create a record for a payment received; review an owner invoice (owner as collaborator); create a contractor invoice on behalf of a contractor (owner side); create and send contractor invoice invitations.
- **Payments (Tier 1)**: payments-issued tab for invoicing; payment schedules (AU/NZ legal notice context); Procore Pay lien waivers included in subcontractor-invoice backups.
- **Seat-relative naming (Tier 1 dictionary table)**: the tool is **Invoicing** for general contractors and owners but **Progress Billings** for specialty contractors; Prime Contracts ↔ Funding ↔ Client Contracts; Subcontractor SOV ↔ Contractor SOV. The specialty-contractor tutorial set is literally titled "Set Up Progress Billings", "Create Client Progress Billings", "Review Progress Billings".

### InEight (suite module — evidence layer A for product pages, B for cross-module split)

- **Two billing products, two bases**: InEight **Contract** carries progress payment invoicing — "prepare invoices based on the Schedule of Values, showing current, previous, and cumulative billed amounts. Payment applications can be generated automatically from field-reported progress and accepted quantities, with full support for retainage calculation. You can batch invoices by contractor or project and attach supporting backup—such as timesheets or installed quantity reports." Plus a subcontractor invoice portal (pay requests, progress quantities, payroll data, change order amounts, approval workflow, status notifications, document versioning, ledger of past invoices). InEight **Billings** is a separate product for T&M/cost-plus billing — rate tables (personnel/equipment/material/line-item rates with effective dates, reusable by project/client/WBS), third-party markups (defaults + line-item exceptions, automated validation), retroactive and future-scheduled rate adjustments with audit trail, billing batches, LEMs (labor/equipment/material reports) generated from field-captured hours, billing status (billed/approved/disputed), unbilled revenue, accruals, ERP integration.
- **learn.ineight.com (Tier 1)**: "InEight Billings provides the toolset to quickly and easily track, report on, and bill for cost reimbursable contracts. Project managers and administrators can define project specific resource billing rates, markups, resource classifications, and generate billing batches for daily cost reporting, client approvals, and invoicing, as required by the contract." Integration: hours from Plan & Progress via Timecenter; bi-directional with Platform (WBS and Pay Items in; batched LEMs and invoices out to recognize earned revenue).
- **Packaging evidence**: Billings "can work as stand-alone construction billing software or be bundled with other InEight modules"; supports lump-sum contracts too but "delivers the greatest value on time-and-materials and cost-plus contracts."

### Siteline (standalone subcontractor-side — evidence layer A for product pages)

- **Positioning**: "Construction Billing Software for Subcontractors. Generate, submit, and manage pay apps, lien waivers, and compliance docs—precisely to each GC's specs—to eliminate payment delays."
- **Pay apps to the GC's specs**: "Produce digital versions of any GC's required forms as well as whichever primary lien waivers are required… automatically submit final pay apps to the GC's required portals… every form looks like its paper version, but our system handles calculations and carry-over from previous months. We even handle taxes, whether a single or multiple tax rates apply." 23,000+ pay-app and lien-waiver forms from 17,000+ GCs digitized.
- **Billing types supported**: lump sum, unit price, time & materials, one-off invoices.
- **Over/under-billing visibility**: "easily see on each project if you're billing in excess of your costs to ensure you're billing enough each month" (subs finance jobs; billing ahead of costs matters).
- **Collaboration & revision**: update SOVs in Siteline, "generate, review, sign, and submit pay apps. Leave comments, track revisions, and auto-send reminders"; digital signatures; real-time status of every pay app across clients, filterable by status/PM/division.
- **Change orders**: "Track the status of your unapproved change orders. Know which ones are proceeding with work anyway, and ensure that approved ones are added to your SOV."
- **ERP discipline**: "Pay app revisions in your ERP is a wonky workflow that creates credits and debits. With Siteline, update pay apps in seconds, then once finalized by the GC, sync billing over to your ERP."
- **Extensions around the cycle**: lien waiver collection from lower tiers, compliance document tracking, A/R reporting (aging, fastest/slowest-paying GCs), billing & cash-flow forecasting, collections management (tasks, reminders), lien rights management (state-specific deadlines, notices, certified delivery), customer management (how every GC pays).

### GCPay (GC-side exchange platform — evidence layer A for product page)

- **Positioning**: "GCPay is a powerfully simple software that fully automates the payment application process between general contractors and subcontractors… cloud-based construction software for managing pay applications, lien waivers, electronic payments and more."
- **Personas**: CFOs (monthly statements, policies for accuracy of reports and billing), project managers ("tracking and reviewing pay applications to ensure compliance is met and waivers are collected—then approve and send off an owner bill"), controllers (AP/AR, job cost, cash flow), project accountants ("ensure that project billings are issued and payments collected and distributed").
- **Machinery**: construction accounting workflows & automations; create & exchange lien waivers; collaboration & compliance documents; ERP integration; electronic payments between GCs and subs; birdseye reporting & dashboards; official AIA documents support.
- **Scale claims (vendor-stated, not asserted in final doc)**: $27.9B+ AFPs processed this year; 2.7M+ lien waivers exchanged; 48,000+ active companies.

### Knowify (SMB trade pole — evidence layer A for product page)

- **Positioning**: "Generate accurate G702/G703 pay apps in minutes — with retainage, stored materials, and change orders handled automatically."
- **SOV generation**: "Automatically generate detailed schedules of values to create pay applications with ease. Simply enter completed work in dollars or percentages, include stored materials, and let Knowify handle the rest."
- **Change-order timing**: "Automatically include approved change orders for the correct billing period, and get warnings when you're about to bill for a change order in the wrong billing period."
- **Official forms**: "Create official branded G702/G703 forms through Knowify's partnership with AIA Contract Documents, when required by clients."
- **Retainage**: "Automatically track retainage by phase and get reminders to create separate invoices when ready, ensuring you collect all retained funds."
- **Accounting**: QuickBooks Online sync of pay-app and retainage info; pay-app advances through a lending partner (variant, not core).

## Cross-product Comparison

| Dimension | Procore | InEight (Contract+Billings) | Siteline | GCPay | Knowify |
|---|---|---|---|---|---|
| Unit of record | Subcontractor invoice / owner invoice (pay application) per billing period | Pay application (Contract, SOV-based) / billing batch + LEM (Billings, T&M) | Pay app per project per month | Pay application (AFP) between GC and sub | G702/G703 pay app |
| Anchored to contract | Commitment (Approved status) / prime contract | Contract with SOV / contract rates | Each GC's contract & required forms | GC–sub agreement | Contract with SOV |
| Computation basis | SOV lines, amount- or unit/quantity-based; stored materials | SOV current/previous/cumulative (Contract); rates × captured costs (Billings) | SOV with system-handled carry-over from previous months; taxes | Pay-app workflow (detail on vendor pages) | SOV; completed work in dollars or percentages; stored materials |
| Billing periods | First-class configured objects (open/close/due dates, manual or automatic) | Batching by period (billing batches) | Monthly cycle implied ("carry-over from previous months") | Periodic workflow (not directly evidenced) | Billing period correctness enforced (wrong-period CO warnings) |
| Retainage | Set/release on invoices; completed-work + stored-material types; sliding scale (AU) | Full retainage calculation (Contract) | Retention tracked/collected ("uncollected retention" pain point) | Not directly evidenced on fetched page | Tracked by phase; reminders for separate release invoices |
| Change orders | Added/removed on commitment invoices; titles on owner-invoice PDFs | Change amounts entered in vendor portal; Change product upstream | Approved COs added to SOV; unapproved CO status tracked | Change-order solution page exists | Approved COs auto-included for correct period; wrong-period warnings |
| Review cycle | Line-item approve/reject; revise & resubmit until all approved | Invoice review & approval workflow with audit logs | Generate, review, sign, submit; comments; revision tracking; GC kick-backs eliminated | Automated review/approval workflows | (Sub-side; GC review external) |
| Multi-party collaboration | Invite to bill; create on behalf; owner reviews contractor invoices; owner as collaborator | Subcontractor invoice portal (submit, quantities, payroll, status) | Submit to GC portals; collect lower-tier waivers | GC↔sub exchange; sub compliance | (Sub-side; QuickBooks sync) |
| Compliance/lien waivers | Lien waivers in invoice backups (Procore Pay) | Compliance sibling product | Lien waiver generation/collection; compliance tracking; lien rights | Lien waivers + compliance documents core features | (Not on AIA page) |
| Payment recording | Payments issued/received tabs; payment received records; payment schedules | Payment status received/approved/paid/disputed; accruals | A/R reporting; collections; forecasting | Electronic payments between GCs and subs | Payment processing; advances (partner) |
| Forms/export | PDF/DOCX export; owner-invoice PDFs; AIA forms in glossary | Client-ready billing packages; branded invoice formats | Digitized GC-specific forms (23k+); exact paper look | Official AIA documents | Official G702/G703 via AIA partnership |
| ERP/accounting | ERP export/integration | Bi-directional ERP; actuals import | Sync after GC finalization (avoiding credit/debit mess) | ERP integration | QuickBooks sync |
| Seat | GC (default), owner, specialty contractor (Progress Billings) | Contractor/project teams (capital construction) | Subcontractor | GC (and subs) | Trade contractor (sub/SMB) |
| Billing basis variants | Amount-based vs unit/quantity-based | SOV-based vs T&M/cost-plus (split across two products) | Lump sum, unit price, T&M, one-off | Pay apps (AIA tradition) | SOV-based (G702/G703) |

Reading of the comparison:
- The pay application as a recurring, contract-anchored, cumulative billing document is present in all five (B).
- Computation from completed work against the contract's payment breakdown, with previous applications deducted, is present wherever computation detail is documented (Procore, InEight, Siteline, Knowify — B; GCPay implied).
- The submission → line-item review → revise/resubmit → approval cycle is directly documented in Procore (A), InEight (A), Siteline (A), GCPay (A at positioning level); the review authority is the paying/receiving party or its representative.
- Retainage machinery is documented in four of five (Procore, InEight, Siteline context, Knowify) — common, not definitional (a 0%-retainage contract still bills).
- Compliance documents (lien waivers) ride on the billing flow in four of five — common.
- Seat-relative naming is structural: the same document family is "owner invoices" upstream, "subcontractor invoices" downstream, "progress billings" from the specialty-contractor seat, "progress claims" in Australian usage (B; Procore dictionary is A).
- The billing basis varies (lump-sum SOV, unit price, T&M/cost-plus) and one vendor (InEight) even splits the two bases across two products — variant, not identity.

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as progress billing:

1. **The pay application as unit of record.** A recurring, numbered, cumulative billing document against a specific contract — not a one-off invoice for a delivered transaction. Each application belongs to a billing period in the contract's life, and the series of applications spans the contract from first billing to final account. Remove → a form template or an invoice generator.
2. **Cumulative contract-anchored computation of the amount due.** The amount due is computed — not stated — from the contract's payment breakdown (schedule of values, pay items, or rate schedule): work completed to date per line (entered as dollars, percentages, or quantities), plus billable items the contract allows (stored materials, approved changes), minus previous applications, with the contract's withholdings (retainage) carried. Each application arithmetically continues the previous ones. Remove → generic invoicing (amount stated, not computed) or a standalone calculator.
3. **The two-party submission–review–certification cycle.** The billing party prepares and submits; the paying/reviewing party reviews (characteristically line by line), rejects or accepts, the billing party revises and resubmits, and the document reaches a certified/approved state that becomes the payable record. Both sides of the cycle are modeled. Remove → a batch invoice generator or an approval workflow with no billing semantics.

Jointly-held load-bearing: (1 alone = a pay-app form template; 2 alone = a billing spreadsheet calculator; 3 alone = generic document approval; 1+2 without 3 = self-service billing calculator; 1+3 without 2 = document workflow with no money computation; 2+3 without 1 = payment tracking with no document of record).

Test against the historical check: the paper-era pay application — a typed AIA G702/G703, a UK interim valuation prepared by the contractor and assessed by the quantity surveyor, a hand-taxed progress claim under a statutory payment regime — satisfies all three invariants: a numbered recurring application, computation from measured/valued work against the contract breakdown with previous applications deducted and retention held, and a submit→assess→certify cycle between the parties. The definition is not over-fitted to current cloud platforms.

### L1 — Common Mature Structure

Present across the sample; makes the Type workable but does not define it:

- **Schedule of values management** — building and maintaining the line-item payment breakdown (by cost code or trade); vendor-authored SOVs in multi-party flows; group rows; amount-based vs unit/quantity-based lines.
- **Retainage/retention machinery** — per-contract withholding terms, completed-work vs stored-material retainage, release through later applications or separate release invoices, regional variants (sliding-scale retention), release reminders.
- **Stored materials billing** — billing for materials delivered/stored but not installed, with documentation and movement tracking.
- **Change-order incorporation** — approved changes added to the payment breakdown and billed in the correct period; wrong-period warnings; unapproved-change exposure tracked separately.
- **Billing periods** — configured open/close/due dates per project, manual or automatic generation, gating submission.
- **Compliance documents in the payment flow** — lien waivers (conditional/unconditional, progress/final), insurance certificates, and other compliance requirements collected alongside the pay application; missing documents hold payment.
- **Multi-party collaboration** — invite-to-bill / vendor portals for submission; create-on-behalf for vendors who bill on paper; status notifications; comment threads; revision tracking.
- **Line-item review tooling** — per-line approve/reject, revise & resubmit loops, review audit trails.
- **Payment recording and status** — payments issued/received recorded against applications; statuses (submitted/reviewed/approved/paid/disputed); payment schedules; accruals and aging.
- **Form generation and export** — owner/GC-specified forms (AIA G702/G703, digitized GC-custom forms), PDF/branded exports, digital signatures.
- **ERP/accounting synchronization** — certified billings synced to corporate accounting (commonly only after approval, to avoid credit/debit churn from revisions).
- **Billing health reporting** — billed vs unbilled, over/under-billing vs costs, A/R aging, cash-flow forecasting, per-customer payment behavior.

### L2 — Variant / Optional Structure

- **Billing basis** — lump-sum SOV (percent or dollar entry), unit-price/quantity-based, T&M/cost-plus rate-based (rate tables, markups, daily LEMs), milestone/payment-schedule-based; one suite may split bases across products.
- **Operating seat** — GC billing the owner (upstream/revenue), owner reviewing and paying contractor bills, subcontractor billing the GC, GC reviewing sub bills; the same cycle mirrored at every contract tier.
- **Regional/form regimes** — US AIA G702/G703 tradition; GC-custom digitized forms; statutory progress-claim regimes (Australia/NZ); UK-style interim applications; jurisdiction-specific lien-waiver forms.
- **Packaging** — tool inside a multi-party construction platform; standalone module of a project-controls suite; standalone billing product (sub-side or GC-side); module of construction ERP/accounting; SMB trade-contractor platform feature.
- **Money-adjacent extensions** — electronic payments between parties, pay-app advances/financing, lien-rights management, collections workflows, WIP reporting.
- **T&M-specific machinery** — resource rate tables with effective dating, markup rules, retroactive rate adjustments, field-hour capture integration.

### L3 — Vendor-specific (research notes only)

- Procore: point-of-view dictionaries (Invoicing ↔ Progress Billings; Prime Contracts ↔ Funding ↔ Client Contracts), invoice contacts vs invoice administrators, invite-to-bill, SSOV/CSOV labels, billing-period objects, Procore Pay lien waivers, DocuSign on invoices.
- InEight: the Contract/Billings product split (SOV pay apps vs T&M rate billing), rate tables with effective dates, LEMs, Timecenter/Plan & Progress hour integration, bi-directional Platform sync (WBS/Pay Items in, batched LEMs/invoices out).
- Siteline: 23,000+ digitized GC forms from 17,000+ GCs; auto-submit to GC portals; lien-rights management with state-specific deadlines; "bill 6x faster" marketing metrics.
- GCPay: AFP processing scale claims; Autodesk ownership; electronic payments between GCs and subs.
- Knowify: official AIA forms via AIA Contract Documents partnership; pay-app advances via lending partner (Billd); QuickBooks-first positioning.

## Vendor-specific Findings

See L3 above; none promoted to the canonical core. Vendor-stated figures (Siteline's "3 weeks faster / 6x / 43%", GCPay's "$27.9B+ AFPs", Procore glossary's "5-10% common retainage") are marketing or vendor-stated and are not asserted in the final document.

## Rejected Findings

- **Retainage as definitional** — rejected: ubiquitous in the sample but a contract with no retainage still generates pay applications; retention is a contract term carried by the billing, not the billing's identity.
- **The schedule of values as the only definitional computation basis** — rejected: unit-price and T&M/cost-plus billing compute against pay items and rate schedules instead; the invariant is the contract's payment breakdown, of which the SOV is the common lump-sum implementation.
- **AIA G702/G703 as definitional** — rejected: one regional form tradition among several; GC-custom digitized forms and statutory regimes serve the same structure.
- **Lien waivers / compliance as definitional** — rejected: common gating machinery around the payment, present in most products but absent in minimal configurations.
- **AR/collections/forecasting as core** — rejected: extensions around the cycle (strongest at the sub-side standalone pole); the billing cycle is the center.
- **Electronic payments as core** — rejected: one product's differentiator; the certification→payment handoff can be recorded without in-product payment rails.
- **"Progress billing = generic invoicing with recurring invoices"** — rejected: the amount due is computed from contract completion state against a payment breakdown, cumulatively, and certified by the counterparty — none of which generic invoicing requires.

## Boundary Findings

1. **vs Construction Contract Administration (§17, processed — DISCHARGES the joint-review flag).** The contract-administration pass defined its Type as the contract-side anchor (contract record, live value, SOV as contract structure, retainage terms, payment attachment) and explicitly left "the periodic billing/pay-application cycle" to this leaf. This pass confirms the split from the other side: the center here is the **billing cycle and the application document itself** — the recurring series, the cumulative computation, the submission/review/certification lifecycle. The market bundles the two (Procore hosts owner invoices under Prime Contracts and sub invoices under Commitments; InEight puts pay apps inside Contract) and also splits them (Procore ships a dedicated Invoicing tool; InEight ships a separate Billings product) — the directory's line (contract record vs billing cycle) is defensible and is honored here. Keep-both. The shared overlap zone: payment status tracking and retainage terms appear on both sides of the seam (contract-side anchor vs billing-cycle machinery).
2. **vs generic Invoicing Application.** Generic invoicing states an amount due for a delivered transaction; progress billing computes the amount due from contract completion state against the contract's payment breakdown, deducts previous applications, and passes the document through counterparty review and certification. Remove the contract-anchored cumulative computation and the certification cycle → generic invoicing.
3. **vs Billing Platform (§08).** Generic billing platforms bill standing commercial commitments (subscriptions, usage) on the vendor's own terms; progress billing bills a counterparty-certified share of a contract's earned value. Different object worlds; the shared word "billing" is superficial.
4. **vs Change Order Management (§17, processed).** Change orders are priced amendments with their own lifecycle; once approved they enter the payment breakdown and are billed through pay applications. This Type consumes approved changes; it does not manage the change instrument. Products confirm: Siteline tracks CO status and adds approved COs to the SOV; Knowify warns about wrong-period CO billing; Procore adds/removes COs on commitment invoices.
5. **vs Construction Claims Management (§17, processed — polysemy note).** The claims pass recorded that "payment claims"/"progress claims" (Australian statutory usage) name the pay application — payment certification — not a dispute claim. This pass confirms: the progress claim in that usage is this Type's unit of record. The word collision is naming, not structure.
6. **vs Project Controls Platform (§17, processed — forward note honored).** Progress billing is the revenue mirror of cost/performance control: both share SOV/retainage vocabulary and both consume field progress, but controls measure cost and schedule performance against a baseline while this Type converts progress into certified billings. Keep-both, as the controls pass expected.
7. **vs Accounts Receivable Management / Collections.** Once certified, the approved application becomes a receivable; sub-side standalone products (Siteline) extend into AR aging, collections, and forecasting. The billing cycle (through certification) is the center; AR/collections are adjacent capabilities that can live in the same product without redefining the Type.
8. **vs Construction Cost Management (§17, processed).** Cost management owns budget/forecast/actuals (the cost mirror); over/under-billing visibility connects the two but the budget is a different object.
9. **vs Subcontractor Management (§17, processed).** That pass deliberately excluded money machinery from its core (relationship-level money status only); this Type is that money machinery for contracted work.
10. **vs Construction Closeout Management (§17, processed).** Closeout owns project-end acceptance and deficiencies; the final pay application, final retainage release, and final account are this Type's terminal documents (with contract administration holding the contract-level closure).

## Uncertainties

- Buildertrend (residential builder pole) unreachable (403/timeout ×2); the residential/SMB variant beyond the trade-contractor pole is described without product claims, consistent with prior passes.
- GCPay's pay-app computation detail (SOV handling, retainage screens) not directly evidenced on the fetched page; GCPay used for the GC-side exchange posture and compliance/payment machinery (B evidence, qualified).
- Owner-side certification authority (architect vs owner's rep vs contract administrator) not directly documented in fetched sources; described conceptually. The AIA form's own name ("Application and Certificate for Payment") is vendor-documented via Knowify/Siteline.
- UK interim valuation machinery not source-verified this pass (no UK vendor sampled); regional generalization held at L2 with the AU/NZ and US evidence only.
- Exact invoice status vocabularies vary by product; statuses described conceptually (Procore's per-line approve/reject and InEight's received/approved/paid/disputed are documented).
- Statutory payment-act timing rules (e.g., reference dates, adjudication clocks) not researched; not asserted.

## Final Synthesis

Progress Billing is the construction contract's revenue-cycle system: it manages the recurring, cumulative billing document — the pay application (progress billing / progress claim / application for payment) — through which a performing party bills the paying party for work completed to date. Its defining core is three structures held together: the pay application as a numbered, periodic, contract-anchored unit of record; the cumulative computation of the amount due from the contract's payment breakdown (completed work per line, plus billable stored materials and approved changes, minus previous applications, with retainage carried); and the two-party submission → line-item review → revise & resubmit → certification cycle that turns the application into the payable record. Around that core, mature products add schedule-of-values management, retainage and stored-materials machinery, change-order incorporation with period correctness, configured billing periods, lien-waiver and compliance collection, vendor portals and invite-to-bill, form generation (AIA G702/G703 and GC-custom digitized forms), payment recording, ERP synchronization, and billing-health reporting. The cycle mirrors at every contract tier (sub→GC, GC→owner) and renames itself with the operator's seat (invoicing, progress billings, progress claims). Its realization is uniformly as a module or tool inside construction platforms, suites, and ERPs — with standalone poles on both the subcontractor side (billing to each GC's specs) and the GC side (pay-app exchange with subs). The sharpest seams: contract administration holds the contract record the billing attaches to; change-order management owns the instrument that feeds it; generic invoicing lacks the cumulative contract-anchored computation and certification; and AR/collections begin where certification ends.
