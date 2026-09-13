# Research Notes — Accounts Payable Automation

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "Accounts Payable Automation" actually is as an Application Type: what objects exist inside it, how a supplier invoice flows through it, what its defining structure is (as opposed to what modern products merely commonly bundle), and where its boundaries lie against Invoice Processing Platform, Procure-to-pay Platform, Accounting Software, Accounts Receivable Management, Expense Management, and Payment Processing.

## Initial Boundary

Initial hypothesis (to be verified, not final):

- Core: automates the AP cycle — supplier invoice intake, data capture, GL coding, PO matching, approval routing, ERP posting, and often payment execution.
- The supplier invoice is likely the central object; the ERP/accounting system is likely the system of record the AP layer posts into.
- Nearest neighbors: Invoice Processing Platform (sibling §08 — possible overlap), Procure-to-pay Platform (§10), Accounting Software (§08), Accounts Receivable Management (§08), Expense Management Platform (§08), Payment Processing Platform (§08), Approval Workflow Platform (§10).
- Main unknowns: is payment execution definitional or common? Is PO matching definitional (non-PO invoices exist)? Is supplier management definitional? Is "Invoice Processing Platform" the same Type under another name?

## Research Questions

1. What is the central object, and what lifecycle/states does it move through?
2. How does invoice capture work (channels, extraction, structured record)?
3. How does GL coding / accounting distribution work?
4. How does matching work (2-way/3-way, PO/receipt; what happens with non-PO invoices)?
5. How does approval routing work (rules, thresholds, delegation, surfaces)?
6. How does payment execution work, and is it definitional?
7. How does the ERP/accounting integration work (system of record, sync direction)?
8. What supplier/vendor management exists and where does it sit?
9. What roles and surfaces exist (AP clerk, approver, controller, supplier, accountant)?
10. What are the boundaries against Invoice Processing Platform, P2P, accounting software, expense management, payment processing?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Philosophy / tier | Access result |
|---|---|---|
| Stampli | pure-play AP automation grown into P2P; "the invoice is the workspace" collaboration philosophy; ERP-centric; mid-market | root + AP product page with operational FAQ fetched (Tier 2) |
| BILL (Bill.com) | SMB financial operations platform; AP+AR+spend; payments-network philosophy; accountant-firm channel | root + AP product page with operational FAQ fetched (Tier 2) |
| Tipalti | mid-market/global; global payment infrastructure + supplier onboarding + tax compliance philosophy | root + AP product page with operational FAQ fetched (Tier 2) |
| Basware | enterprise; "Invoice Lifecycle Management" / touchless processing + e-invoicing network + compliance philosophy; shared-service-center scale | root + AP solutions page with FAQ fetched (Tier 2) |

Rejected/considered: AvidXchange (vertical mid-market; docs not fetched — sample already spans tiers), Coupa/Zip (procurement-first P2P — belongs to the P2P boundary discussion, not the AP core), QuickBooks-class built-in bill pay (accounting-software capability, used as boundary anchor only).

Analyst-category confirmation: Basware's own pages reference the "Gartner Magic Quadrant for Accounts Payable Applications" and "Forrester Wave: Accounts Payable Invoice Automation Software" — the market treats "AP automation / AP applications" as one recognized category.

## Sources

Tier 2 (official product pages, directly fetched; all include operational FAQs):

- Stampli — homepage: https://www.stampli.com/ ; AP Automation product page: https://www.stampli.com/ap-automation-platform/
- BILL — homepage: https://www.bill.com/ ; Accounts Payable product page: https://www.bill.com/product/accounts-payable
- Tipalti — homepage: https://tipalti.com/ ; AP Automation page: https://tipalti.com/ap-automation/
- Basware — homepage: https://www.basware.com/en ; AP Automation solutions page: https://www.basware.com/en/solutions/ap-automation

Source-access limitation: the operational help centers were unreachable from the research environment on 2026-09-06 — support.stampli.com (2 transport errors), help.bill.com (2 transport errors). Basware support (ServiceNow portal) and Tipalti's Zendesk were not attempted after the pattern was established. Consequently all product evidence is Tier 2 (vendor product pages, which for all four vendors carry detailed operational FAQs describing capture, coding, matching, approval, ERP sync, and payment). UI-level mechanics (exact field names, queue behavior, exact state labels) were not directly observed and are not asserted. Vendor-marketed performance numbers (e.g., accuracy rates, country counts, invoice volumes) are recorded below as vendor claims only, never as facts.

## Product Observations

### Stampli

Key observations (Layer A unless noted):

- Positioning: "Procure-to-Pay Platform for Finance Teams" — modules: Procurement, AP Automation, Vendor Management, Payments (Direct Pay), Expense Management (reimbursements, cards), Intelligence (Stampli AI, Deep Finance). AP Automation is the named core module. (A)
- AP philosophy: "Your inbox is not an accounts payable system… one connected workspace." "The invoice is the workspace — every question, document, change, approval, and status update stays on the invoice." (A)
- AI: "captures and codes every line, identifies vendors, predicts approvers, flags duplicates, and learns from your team's decisions." (A)
- Matching: "Match invoices to POs and receipts at the line level. Discrepancies, documents, and discussion stay together for faster resolution." FAQ: "supports applicable purchase-order matching workflows, including line-level comparison of invoices with purchase orders and receipts." (A)
- Approvals: "Route invoices by entity, amount, department, vendor, or your own rules. Trays, reminders, and mobile approvals." (A)
- ERP relationship: "Use your ERP's vendors, accounts, dimensions, POs, and validation rules throughout the process, so invoices arrive complete and ready to post—without changing the ERP." FAQ: "The ERP remains the system of record, and approved invoice data is synchronized or posted only through the configured review and integration process." (A)
- Capture channels (FAQ): "email, upload, or the vendor portal"; AI extracts data and suggests coding "using available ERP context, while AP reviews the record." (A)
- Controls (FAQ): role-based access, configurable routing, approval history, documents, comments, transaction changes retained with the invoice — "traceable record for oversight, close, and audit support." (A)
- Operating models (FAQ): "Configurable work queues, routing, roles, and approval paths can support shared services, business units, local approvers, and hybrid models." (A)
- Roles marketed to: CFO, Controller, AP Teams, Approvers. Mobile apps exist. (A)
- Vendor claims (not asserted as facts): 89% of work handled by AI; 400k+ invoices/week; $400B+ cumulative spend. (A, as claims)

### BILL (Bill.com)

Key observations:

- Positioning: "AI-powered financial operations platform" — AP & AR, Spend & Expense, credit. AP page: "erases the busywork from capturing invoices, routing approvals, and processing payments—syncing seamlessly with your accounting software." (A)
- Capture (FAQ): "Vendors can email a digital invoice directly to your dedicated AP address… drag and drop pdf scans… or snap a picture with your mobile phone." AI/OCR "reading them and extracting data… collecting and entering that information for your review." (A)
- Coding/matching: "BILL AI automatically codes multi line item bills… BILL also automates 2- and 3-way matching—checking invoices against POs and receipts." (A)
- Approvals: "Tailor your approval workflows to fit your business rules with BILL handling the routing… Track every step, send reminders, and approve from anywhere." FAQ: "If a new invoice should require 3 approvals before it gets paid, the platform will automatically route that invoice to the right people." (A)
- Payments: "ACH, virtual card, physical check, or even international wire… pay with just a few clicks." Network framing: "access to millions of vendors across the BILL network." (A)
- Accounting sync: "Sync your BILL data with your accounting software to keep your general ledger up to date automatically." FAQ: "The data entered in BILL is automatically synced and posted to your general ledger." 2-way sync with QuickBooks, NetSuite, Intacct, Xero, Dynamics. (A)
- Duplicate/fraud: "invoice matching and purchase order matching, flagging potential duplication to reduce the chance that you'll pay the same bill twice"; "intelligent approach to vendor onboarding and validation." (A)
- Multi-entity: "centralized, automated AP. Approve, review, and pay bills across entities and locations all in one place." (A)
- Accountant channel: Accountant Console — firms "manage bill pay for clients." 1099 filing product. (A)
- Vendor's own definition of the Type (FAQ "What is AP automation?"): "uses automation technologies and digital processes to streamline the accounts payable process… They read and store each invoice, manage billing communication, and make payments… Any good accounts payable automation solution will use your own approval processes." (A)
- Vendor claims (not asserted): 99% field-capture accuracy; 8.3M network members; $345B annual payment volume. (A, as claims)

### Tipalti

Key observations:

- Positioning: "Finance Automation… across accounts payable, mass payments, procurement, expenses, and treasury in one connected suite." AP Automation sub-modules: Supplier Management, Invoice Processing, Global Payments, Tax Compliance, Automated Payment Reconciliation, PO Matching. (A)
- End-to-end framing: "From supplier onboarding, invoice processing, PO matching, and reconciliation, all in one system." (A)
- Supplier management: "multi-language, self-service supplier onboarding… capture accurate supplier details, reduce status inquiries"; tax ID validation across 60+ countries, W-9/W-8BEN-E collection, compliance-list screening, KPMG-approved tax form validation (vendor claim), 1099/year-end reporting. (A)
- Invoice processing: "AI captures header and line-item data, codes invoices, routes approvals, and matches POs in a seamless system." (A)
- Payments: "Execute payments across 200+ countries and territories in 120 currencies and more than 50 payment methods" (vendor claim); regulated as a money services business (US/Canada) and e-money institution (UK) — payment infrastructure is a first-class product pillar. (A)
- Reconciliation: "Sync spend data to your ERP in real-time to simplify reconciliation… and accelerate the month-end close across all entities." (A)
- Vendor's own workflow description (FAQ "How does AP software work?"): "AP software starts by automatically capturing data from invoices, whether they come in by email, PDF, or paper. It then matches each invoice to purchase orders and other documents—like shipping receipts or inspection reports… Next, the invoice is routed to the correct approvers based on your company's workflow… After approval, the system syncs the invoice data with your ERP and stores a complete audit trail of the transaction." (A)
- Vendor's own definition (FAQ "What is AP automation?"): "digitizing and streamlining how companies manage invoices and payments. It replaces manual tasks—like data entry, paper handling, and chasing approvals—with automated workflows for invoice capture, PO matching, approvals, payments, and reconciliation." (A)
- Multi-entity: "consolidated HQ payer account with multiple sub-entities"; roll-up spend views. (A)
- AI agents: Invoice Capture, PO Matching, Reporting, Bill Approvers, Purchase Request, Tax Form Scan, ERP Sync Resolution, Expense Receipt Scan. (A)
- Roles: AP Team, Controllers, CFO, Procurement, Operations, Developers & IT. (A)
- Mass Payments is a separate product line (marketplace/publisher payouts) — adjacent to AP, not the same object model. (A)

### Basware

Key observations:

- Positioning: "AI-Driven Invoice Lifecycle Management & AP Automation"; "Invoice Lifecycle Management, powered by Governed Autonomy: fully compliant, fully protected, and auditable at every decision." (A)
- Vendor's own definition (FAQ "What is AP Automation?"): "aims to optimize the process of receiving and processing of supplier invoices. AP automation enables more of your AP process to be touchless, meaning that most tasks are automated, requiring minimal human effort." (A)
- PO-based matching: "enables the use of any combination of invoices, POs, goods receipts, quality checks, contracts, etc. at the line or header level for straight-through processing of PO-based invoices. And when information is missing, recognition methods review the available data to calculate the best matching scenario." (A)
- Non-PO handling: "addresses recurring invoices that may not have POs… rent, utility charges, and mobile phone plans… learns and identifies recurring invoices and supports the automation of these invoices—whether they are based on schedules, budgets, or amounts." (A)
- Coding: "SmartCoding is a machine-learning based solution automating coding for invoices that are not linked to a purchase order… Based on historical coding and invoice header data… generates very accurate invoice coding proposals." (A)
- Routing: "smart routing functionality ensures that invoices are automatically sent to the appointed approval workflow… the system automatically determines the recipient." (A)
- ERP relationship (FAQ): "An AP automation solution does not replace your ERP system(s) but complements them to automate all AP related processes… integrate with 250+ ERP systems simultaneously" (vendor claim); "If you are using a different procurement solution to create POs or generating POs from your ERP — that's no problem at all. Our superior integration capabilities will pull that PO data into Basware and automatically match your invoice to it." (A)
- e-Invoicing Network: receiving/sending e-invoices, invoice enrichment, archive (Vault), interoperability; compliance hub with country mandates (France, Germany). (A)
- AP Assurance: AP Protect, AP Audit & Recovery, Statement Matching — verification of "accuracy, completeness, and authenticity before payment and throughout its lifecycle." (A)
- Target profile: "Globally operating organizations… More than 50.000 invoice transactions per year… Finance Shared Service Centers… Multi-ERP environments." (A)
- KPI framing: touchless processing %, electronic invoicing %, paid-on-time %. (A)
- Payment: "Authorize payments up to 30x faster" (vendor claim) — payment *authorization* is emphasized; native payment execution is not a headline pillar (unverified depth; see Uncertainties). (A)

## Cross-product Comparison

| Structure | Stampli | BILL | Tipalti | Basware | Assessment |
|---|---|---|---|---|---|
| Supplier invoice as central managed object | yes ("invoice is the workspace") | yes (bills) | yes (invoice processing) | yes (invoice lifecycle) | **L0** |
| Multi-channel capture into a structured record | email / upload / vendor portal | dedicated AP email / drag-drop / mobile photo | email / PDF / paper | e-invoicing network / SmartPDF / email | **L0** (capture exists in all; the channel mix is L1/L2) |
| Verification + approval gate before release | yes (rules by entity/amount/dept/vendor; trays; mobile) | yes (custom workflows; reminders; mobile) | yes (routes approvals; approver agent) | yes (smart routing; governed autonomy limits) | **L0** |
| Accounting handoff (GL coding + ERP posting/sync) | yes (ERP system of record; ERP-aligned coding) | yes (synced and posted to GL) | yes (real-time ERP sync; reconciliation) | yes (complements ERP; 250+ ERPs claim) | **L0** |
| Data extraction (OCR/ML/AI) with human review | yes | yes | yes | yes | L1 (the structured record is L0; the extraction technology is L1) |
| GL coding automation (learned proposals) | yes | yes | yes | yes (SmartCoding) | L1 |
| PO/receipt matching (2-way/3-way, line/header) | yes (line-level) | yes (2- and 3-way) | yes (2- and 3-way) | yes (any combination, line/header) | L1 (non-PO invoices are a first-class path in all four) |
| Duplicate detection / fraud checks | yes | yes | yes | yes (AP Protect) | L1 |
| Payment execution | yes (Direct Pay) | yes (ACH/check/card/international; network) | yes (global payments infrastructure) | authorization emphasized; execution depth unverified | L1 (common in modern products; not definitional — see historical check) |
| Supplier/vendor management | yes (module + portal) | yes (network, onboarding validation) | yes (self-service onboarding, tax forms) | yes (supplier resources; network onboarding) | L1 |
| Audit trail / role-based access | yes | yes | yes | yes ("auditable at every decision") | L1 |
| Exception/collaboration layer on the invoice | yes (questions/decisions on invoice) | yes (messages in app) | yes (exceptions surfaced; sync-resolution agent) | yes (exceptions routed) | L1 |
| Analytics / spend visibility | yes (Deep Finance) | yes (reporting) | yes (AI insights) | yes (Basware Insights) | L1 |
| AI assistants/agents | yes | yes | yes | yes | L1 (current-era implementation of capture/coding/routing) |
| Tax compliance depth (W-9/W-8, VAT, 1099) | not prominent | 1099 filing | major module | tax code handling, 50+ countries claim | L2 (region/segment) |
| Multi-entity / multi-currency / multi-ERP | yes | yes | yes (headline) | yes (headline) | L2 (scale) |
| e-Invoicing network / government mandates | no | no | yes (European network links) | yes (core pillar) | L2 (region) |
| Procurement (requisitions/POs) | yes (module) | yes (module) | yes (module) | yes (P2P suite) | L2 (suite extension) |
| Expense management / cards | yes | yes | yes | no | L2 (suite extension) |
| Accountant/partner channel | partners page | Accountant Console (major) | partner portal | consultancy/reseller partners | L2 (channel) |

Convergence summary (Layer B): all four products implement the same spine — capture → structured record → validate (supplier, duplicate, coding) → match (if PO-based) → route → approve → post to accounting → (commonly) pay → reconcile/archive. All four explicitly subordinate themselves to an ERP/accounting system of record. All four frame "touchless" or "AI does the routine work" as the goal while keeping human accountability.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

1. **Supplier invoice as the central managed object** — a third-party document asserting money owed by the organization, held as a tracked record with amount, supplier, dates, and lifecycle state.
2. **Capture into a structured, tracked invoice record** — incoming documents (whatever the channel) are transformed into structured data the system can validate, route, and post.
3. **Verification and approval gate** — the invoice is checked (accounting validity; purchasing match where applicable) and must pass an authorization gate governed by the organization's own rules, with accountable humans (or governed automation acting under human-set limits) before it is released.
4. **Accounting handoff** — the approved invoice is recorded against the organization's books: GL/account-dimension coding, supplier liability, posting/sync into the ERP or accounting system.

Remove any one and the Type collapses: without (1) it is generic document workflow; without (2) it is a shared inbox; without (3) it is uncontrolled data entry; without (4) it is an invoice collaboration tool with no accounting consequence — not *accounts payable* automation.

Deliberately **not** in L0 (tested and demoted):

- **Payment execution** — universal in the current sample but not definitional. Historical check: 2000s-era invoice-imaging/workflow systems (ReadSoft/Kofax lineage) and ERP-native invoice workflows did capture + match + approval + ERP posting with payment left to the ERP/bank, and were still AP automation. Basware today leads with invoice lifecycle and payment *authorization*, not execution. → L1.
- **PO matching** — all four support it, but non-PO invoices (rent, utilities, services) are a first-class path in every product (Basware ships a dedicated "InvoiceAI for Non-PO Invoices"; Tipalti's SmartCoding-style coding handles non-PO). The Type works without POs. → L1.
- **Supplier management** — supplier master data must exist somewhere, but in ERP-centric products it is *pulled from the ERP* (Stampli: "use your ERP's vendors"); native onboarding portals are common, not definitional. → L1.
- **AI/OCR extraction** — the structured record is L0; the extraction technology is an implementation (template OCR → ML → LLM agents). → L1.
- **Duplicate detection, audit trail, analytics, e-invoicing, tax compliance, multi-entity** — all common or variant. → L1/L2.

### L1 — Common Mature Structure

- data extraction (OCR/ML/AI) with field-level proposals and human review
- GL coding automation (learned proposals, line-level distribution, ERP dimensions)
- PO/receipt matching (2-way/3-way; line or header level) with exception queues
- approval workflow engine (rules by amount/entity/department/vendor; delegation; reminders; email/mobile approval surfaces)
- duplicate detection and payment-fraud checks
- payment execution (ACH/check/card/wire/international; scheduling; early-payment discounts)
- supplier/vendor management (self-service onboarding, payment-status inquiry)
- ERP/accounting sync (system-of-record relationship; posting; reconciliation support)
- continuous audit trail and role-based access / segregation of duties
- exception and collaboration layer attached to the invoice (comments, questions, documents)
- analytics (cycle time, touchless rate, spend visibility, cash-flow impact)
- AI assistants/agents for capture, coding, matching, approver suggestion, sync resolution

### L2 — Variant / Optional Structure

- e-invoicing network connectivity and government mandates (EU: France/Germany/Italy; Latin America fiscal invoicing — not sampled)
- tax compliance depth (W-9/W-8BEN-E collection, VAT ID validation, withholding, 1099/year-end reporting)
- multi-entity / multi-currency / multi-ERP scale (shared-service-center operating models)
- procurement extension (requisitions, PO creation, intake) → shades into P2P suites
- expense management / corporate cards extension
- payment-adjacent financial services (payment networks, cash accounts, FX, virtual cards)
- accountant/bookkeeper firm channel (managing client AP)
- deployment: cloud SaaS (current norm) vs historical on-prem imaging/workflow
- industry editions (construction, healthcare, real estate, nonprofits)

### L3 — Vendor-specific (stays in Research Notes)

- Stampli: "invoice as workspace" collaboration model; Trays; Direct Pay; Deep Finance; Billy AI branding
- BILL: member network effects; Divvy cards; Cash Account (banking-adjacent); Accountant Console; 1099 filing product
- Tipalti: Mass Payments product line; MSB/e-money regulatory posture; KPMG-approved tax validation (vendor claim); named AI agents
- Basware: Invoice Lifecycle Management / Governed Autonomy branding; SmartPDF/SmartCoding/InvoiceAI; e-invoicing Vault; AP Protect / AP Audit & Recovery / Statement Matching; Trustpair acquisition (announced)

## Rejected Findings

- **"AP automation = payments"** — rejected as definition. Payment execution is the most monetized layer (BILL, Tipalti) but the historical sample and Basware's current positioning show the Type stands without it. Payments = L1.
- **"AP automation requires PO matching"** — rejected: non-PO invoices are a first-class path in all four products.
- **"AP automation replaces the ERP"** — rejected by all four vendors' own statements; the ERP/accounting system remains the system of record. The Type is a layer *beside/on top of* the ledger.
- **"AI is definitional"** — rejected: AI is the current-era implementation of capture/coding/routing; template-OCR and even manual-keying-with-workflow predecessors satisfied the same structure.
- **"Touchless rate targets are structural"** — vendor KPI marketing; the structural fact is the governed automation limit, not a specific percentage.

## Boundary Findings

1. **vs Invoice Processing Platform (sibling leaf, §08)** — the market treats invoice processing as the document-centric *core* of AP automation: Tipalti lists "Invoice Processing" as a sub-module of AP Automation; Basware's AP automation page is entirely about invoice processing; Stampli maintains separate educational pages for "invoice processing" and "AP automation" where processing is the capture/exception stage of the AP cycle. Structural test: an invoice-processing product centers capture/extraction/validation/routing of invoice documents; an AP automation product carries the invoice through coding, approval, accounting posting, and (commonly) payment. Remove coding+posting+payment → invoice processing remains; add them → AP automation. **Probable capability/parent-child relationship rather than two independent Types — flagged for joint review when Invoice Processing Platform is processed.**
2. **vs Procure-to-pay Platform (§10)** — P2P adds the upstream procurement cycle (requisition, sourcing, PO creation, receiving). AP automation consumes POs from *any* source (Basware FAQ explicitly matches invoices against POs generated in other systems/ERPs). Test: remove requisition/PO-creation → AP automation remains; make them primary → P2P. Note the suite-creep pattern: Stampli, Tipalti, and Basware all now market P2P suites with AP as the anchor module — evidence that AP is the core and procurement the extension, not vice versa.
3. **vs Accounting Software (§08)** — accounting software holds the books and implements lightweight bill-pay as an L1 surface; AP automation is a specialized layer that adds capture, matching, workflow, and payment at scale *while posting into* the ledger. Test: remove the ledger/statements → AP automation still functions (it posts to an external ERP); remove the AP layer → accounting software remains. Consistent with the accounting-software research note (§08 sibling), which classified standalone AP automation as the mid/enterprise-depth point capability.
4. **vs Accounts Receivable Management (§08)** — mirror image: AR centers customer invoices and money in; AP centers supplier invoices and money out. Some platforms ship both sides as one product (BILL AP & AR) — related Types sharing a platform, not one Type.
5. **vs Expense Management Platform (§08)** — expense is employee-initiated spend (receipts, reimbursement); AP is supplier-initiated invoices. Different intake, different objects, different approval semantics. Vendors bundle both (Stampli, Tipalti, BILL) as suite extensions.
6. **vs Payment Processing Platform (§08)** — payment processing moves money as its primary object (checkout, payouts); in AP automation the payment is one downstream step of the invoice lifecycle and carries approval/accounting context. Tipalti's separate Mass Payments line (marketplace payouts without supplier invoices) illustrates the split: same rails, different object model.
7. **vs Approval Workflow Platform (§10)** — generic approval engines lack the invoice object, matching semantics, and accounting handoff; in AP products the workflow engine is an L1 component, not the Type.
8. **ERP-native AP modules** — the AP subledger inside an ERP (invoice entry, matching, approval, payment) satisfies the L0 loop but is the ERP's accounting structure, not the standalone automation Type; the market category (analyst MQ/Wave naming) refers to the dedicated layer. Recorded as an observation, no taxonomy change proposed.

## Historical / Market-Sample Check

- **2000s invoice-imaging & workflow systems** (ReadSoft/Kofax/Perceptive lineage): scan/capture → OCR/template extraction → matching → approval workflow → ERP posting; payment left to ERP/bank. Satisfies L0 with none of: AI agents, native payments, supplier portals, e-invoicing networks. ✓
- **ERP-native AP workflows** (e.g., SAP MM/FI invoice verification): invoice entry against PO, matching, release strategy, payment run. Satisfies the L0 loop inside the ledger itself; the standalone Type is the same loop as a dedicated layer. ✓ (reasoned, not fetched)
- **Regional check**: EU e-invoicing mandates (France receiving mandates in force, Germany phased to 2028 — per Basware's compliance pages) add L2 intake/compliance structure; the L0 does not depend on mandates. Latin American fiscal e-invoicing (e.g., Mexico CFDI) was not sampled; the L0 is designed to accommodate it (invoice object + validation + posting) but this is inference, not observation.
- **Small-organization check**: BILL's nonprofit/SMB customers satisfy the same core with lighter configuration. ✓
- Conclusion: L0 does not over-fit the current AI/payments era.

## Uncertainties

1. Help centers for Stampli and BILL were unreachable (2 transport errors each); all product evidence is Tier 2 product pages with operational FAQs. UI-level mechanics (exact state labels, queue behavior, field names) are not asserted anywhere in the final document.
2. Exact invoice state machines vary by product and were not directly observed; the final document describes conceptual states only.
3. Basware's native payment-execution depth (executes payments vs authorizes/hands off) is unverified — treated as product-specific uncertainty; the final document does not claim Basware executes payments.
4. Latin America fiscal e-invoicing and EDI-heavy retail AP were not sampled; L0 fit is inferred.
5. Vendor-marketed numbers (accuracy %, country counts, invoice volumes, network sizes) are recorded as claims only and are excluded from the final document.
6. Whether any mainstream AP automation product ships *without* duplicate detection was not verified; duplicate detection is placed in L1 (common) rather than L0 on cross-product evidence, not universality.

## Final Synthesis

Accounts Payable Automation is the dedicated application layer that carries an organization's supplier invoices from arrival to accounting: **supplier invoice as central managed object → capture into a structured record → verification (coding, duplicate/supplier checks, PO/receipt matching where applicable) → approval under the organization's own rules → posting into the ERP/accounting system**, with payment execution, supplier self-service, tax compliance, and e-invoicing connectivity as the common modern extensions. The ERP stays the system of record; the AP layer's signature is the governed pipeline that makes invoices *complete, validated, approved, and audit-traceable before they hit the books*. Products differ mainly in where they sit on three gradients: document-processing depth (touchless enterprise vs collaborative mid-market), payment execution (native rails vs handoff), and suite breadth (pure AP vs P2P/expense/cards). The Application Document will present the defining core and standard capabilities in natural language; variants name the L2 options; L3 stays in these Research Notes.
