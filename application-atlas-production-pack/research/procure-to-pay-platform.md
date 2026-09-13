# Research Notes — Procure-to-pay Platform

## Research Goal

Understand how real procure-to-pay (P2P) products work as applications: what objects exist inside them, how the buying chain flows from internal demand to payment, which controls govern each transition, and where the boundary lies against Accounts Payable Automation, Purchase Order Management, Procurement Management, Strategic Sourcing, Invoice Processing, and ERP.

## Initial Boundary (working hypothesis before research)

- Core use: an organization-facing platform that runs the buying chain — request → purchase order → receipt → supplier invoice → payment — under the organization's own approval and policy structure.
- Primary users: employees/requesters, buyers/purchasers, procurement staff, AP/finance, budget-owning approvers, suppliers.
- Nearest neighbors: Accounts Payable Automation (already processed — its notes pre-define this boundary), Purchase Order Management, Procurement Management Platform, Strategic Sourcing / E-sourcing, Invoice Processing Platform, ERP, Expense Management Platform, Supplier Portal, Spend Analysis Platform, Government Procurement Platform.
- Unknowns: whether payment execution is definitional or optional; whether the requisition is an invariant or an implementation; how deep direct-materials support goes; how the newer "intake orchestration" posture fits.

## Research Questions

1. What are the core objects (requisition, PO, receipt, invoice, payment, supplier, catalog, contract) and how do they link?
2. What does the end-to-end flow look like, and where do humans intervene?
3. What approval/control structure does the platform enforce, and whose rules are they?
4. How does invoice matching work (2-way vs 3-way), and what happens on mismatch?
5. How do non-PO invoices, blanket POs, auto-POs, and services spend fit the chain?
6. Where does the platform end and the ERP begin (posting, payment execution)?
7. How do suppliers participate (portal, network, punch-out)?
8. What differs by segment (mid-market vs enterprise vs AP-led entry) and by vertical (manufacturing direct materials, public sector, higher ed)?
9. Where is the boundary against AP automation, PO management, sourcing, and ERP?

## Representative Products

| Product | Why selected | Evidence tier reached |
|---|---|---|
| SAP Ariba (SAP Spend Management / Ariba Buying & Invoicing) | Enterprise suite leader; source-to-pay breadth; supplier network; ERP-adjacent | Tier 2 (official product pages incl. dedicated P2P page with capability blocks + FAQ); help.sap.com JS shell unreachable |
| Basware | AP/invoice-led P2P philosophy ("start with AP"); global SSC / multi-ERP posture; e-invoicing network | Tier 2 (official P2P + e-Procurement pages with operational FAQs) |
| JAGGAER (JAGGAER One) | Enterprise S2P with direct-materials depth and vertical configurations (manufacturing, public sector, higher ed) | Tier 2 (official S2P page incl. P2P solution list + S2C/P2P boundary FAQ) |
| Procurify | Mid-market purchasing-first posture; requisition-centric; full KB reachable | Tier 1 (official Knowledge Base: PO/receiving/vendor/catalog articles) + Tier 2 product pages |
| Coupa | Major market player (frequent named competitor of Ariba/Jaggaer) | Unreachable — coupa.com 403 ×2, help.coupa.com transport error; market anchor only, no claims drawn |

## Sources

- SAP — Spend Management overview: https://www.sap.com/products/spend-management.html (fetched 2026-09-06)
- SAP — Ariba Procure-to-Pay software: https://www.sap.com/products/spend-management/procure-to-pay-software.html (fetched 2026-09-06; includes "What is the procure-to-pay process?" FAQ)
- SAP Help Portal (ARIBA_BUYING): https://help.sap.com/docs/ARIBA_BUYING — JS shell, no content (1 attempt, abandoned)
- Basware — Procure-to-Pay Automation: https://www.basware.com/en/solutions/procure-to-pay/ (fetched 2026-09-06; includes P2P definition FAQ)
- Basware — e-Procurement: https://www.basware.com/en/solutions/e-procurement/ (fetched 2026-09-06)
- JAGGAER — Source to Pay: https://www.jaggaer.com/solutions/source-to-pay/ (fetched 2026-09-06; includes S2C-vs-P2P FAQ)
- Procurify — product site: https://www.procurify.com/ (fetched 2026-09-06)
- Procurify Knowledge Base: https://success.procurify.com/en/ (fetched 2026-09-06) and Purchasing & Receiving collection: https://success.procurify.com/en/collections/8539162-purchasing-receiving-with-procurify (fetched 2026-09-06)
- Coupa — https://www.coupa.com/products/source-to-pay/procure-to-pay (403), https://www.coupa.com/ (403), https://help.coupa.com/... (transport error) — abandoned after 2 failures
- Ivalua — https://www.ivalua.com/products/ (403) — abandoned after 1 failure
- Internal cross-reference: research/enterprise-resource-planning-erp.md (procure-to-pay documented as a named ERP process: order-to-cash / procure-to-pay / record-to-report) and research/accounts-payable-automation.md (Boundary Findings #2 pre-defines the AP-automation vs P2P boundary)

## Product Observations

### SAP Ariba (SAP Spend Management)

Evidence layer: A (directly observed on official pages).

- Official FAQ defines the process: "The procure-to-pay process integrates purchasing and accounts payable systems… four key stages: selecting goods and services, enforcing compliance and ordering, receiving and reconciliation, and invoicing and payment."
- Named product: SAP Ariba Buying and Invoicing, with guided buying, catalogs, invoice management, network-based collaboration (SAP Business Network).
- Intake layer (newer posture): "AI-powered single front door for demand intake"; intake dashboard to submit and track procurement requests; "seamless procurement orchestration" across systems; no-code intake-to-procure process builder.
- Centralized procurement: unified requisitioning experience; central demand aggregation ("bundle requisitions for better pricing and create and publish central requests for quotes from external purchase requisitions"); enterprise contract orchestration ("distribute details to back-end ERPs for local execution"); single procurement command center for compliance/approvals/document output.
- Invoice management: capture from e-mail, networks, or AI; central worklist ("single view of all invoices across all channels… seamlessly integrated to SAP ERP"); touchless processing; handles non-PO invoices and recurring/complex services; workflow builder; preconfigured templates; monitoring by supplier/cost center/commodity code.
- Catalog management: collection, validation, enrichment, classification, approval; catalog APIs.
- Receiving: Receiving Assistant covers "goods receipt, service entry sheet, return, and quality tracking… enhance purchase order and contract compliance."
- Services procurement: collaborative digital workspace for services spend; operationalize contracts and SOWs (milestones, service quality, budget); built-in tax and labor compliance "across 180 countries and in 21 languages" (vendor figure — recorded, not generalized).
- Midsize edition (Ariba SNAP): "deploy in as few as 12 weeks… speed up purchase orders and improve cash flow" (vendor claim).
- e-invoicing mandates: compliance "in more than 40 countries" via SAP Business Network (vendor figure).
- ERP relationship: "track spend in real-time across multiple ERP systems"; invoice worklist "seamlessly integrated to SAP ERP" — the platform sits beside/above ERPs.

### Basware

Evidence layer: A (directly observed on official pages).

- Official FAQ defines P2P: "includes the whole process from point of order to payment, spanning the activities of requisitioning, purchasing, receiving, paying for, and accounting for goods and services."
- Philosophy: AP-first — "address your procure-to-pay transformation from the other end by starting with Accounts Payable"; e-procurement is the upstream add-on "natively integrated to our invoice automation solution."
- Interoperability stance: "Cover all purchase order sources by integrating into any existing procurement or ERP system… If you are using a different procurement solution to create POs or generating POs from your ERP – that's no problem at all. Our superior integration capabilities will pull that PO data into Basware and automatically match your invoice to it." Also: "An AP automation solution does not replace your ERP system(s) but complements them."
- Target profile: globally operating organizations, "more than 50,000 invoice transactions per year," finance shared service centers, multi-ERP environments (vendor positioning).
- e-Procurement capabilities: guided purchasing (preferred vendors/pricing compliance); simplified shopping (consumer-style experience, advanced catalog management, automated stock integration); advanced approvals — "automatically issues POs and places orders as each item on a requisition is approved without waiting for the other line items" (line-level partial approval); pricing compliance with "budget check matrices inform approvers of the impact of purchases on budgets… at the time of requisitioning"; operational sourcing (e.g., Price on Request); out-of-the-box analytics (spend by supplier/category/department, managed vs unmanaged spend).
- AP side: invoice ingestion (e-invoicing network), touchless AP (coding, routing, matching, exception handling), InvoiceAI for PO and non-PO invoices, invoice matching, compliance archive.
- KPI framing (vendor marketing, not asserted as fact): touchless rate, first-pass match on PO-based invoices, "invoices ready to pay before due-date" — the "ready to pay" endpoint framing is notable: the chain ends at a payment-ready payable.

### JAGGAER (JAGGAER One)

Evidence layer: A (directly observed on official pages).

- Official FAQ draws the S2C/P2P boundary: "Source-to-Contract covers everything from spend analysis through sourcing events, supplier selection and contract execution. Procure-to-Pay covers the buying, fulfillment, invoicing and payment side. Both run on the same JAGGAER One data layer, so decisions made in sourcing enforce automatically in purchasing."
- P2P solution list (directly observed): Purchase Requisitions, Purchase Order Management, Goods Receipts, Advance Shipping Notices, Invoice Management, Payments Management, Budget Management, Shopping Catalogs, Quality Management.
- P2P capability framing: "One-stop shopping with guided buying experience"; "Automate purchasing journey from Request to PO"; "Streamline inbound logistics and order accuracy" (ASN); "Automate the entire AP process with 3-way matching"; "Protect every payment with built-in intelligence."
- Direct materials: "Direct materials are a first-class workflow — BOM-driven sourcing, supplier quality (SCAR, APQP, PPAP), ASN and VMI"; manufacturing vertical with BOM management.
- Public sector vertical: "Solicitation management and bid publishing, cooperative purchasing and contract vehicles, supplier diversity and small-business tracking, audit trail and public-records compliance, multi-agency and consortium procurement."
- Higher education vertical: "Departmental catalog and punchout buying, grant-funded and project-based procurement… Integration with Banner, Workday, Oracle."
- Integration: pre-built connectors to SAP, Oracle, Workday, Infor, NetSuite, Banner, PeopleSoft and "1,000+ business applications"; REST API, EDI, cXML, OCI punchout standards; managed integration layer (JAGGAER Link).
- Security/governance: SSO/SAML/MFA for buyer and supplier identity; tenant isolation; "full audit trail on every transaction and approval"; role-based access controls.

### Procurify

Evidence layer: A (Tier 1 KB + official product pages).

- Product framing: "The agentic procurement platform that turns your spend data into faster workflows… acting across intake, approvals, purchase orders, invoice matching, and payment." Three named workflow segments: Intake-to-Approve ("Control starts at the request"), Purchase-to-Receive ("Procurify creates and sends POs in seconds, then closes the loop the moment items are received"), Invoice-to-Pay ("extracts invoices, matches them to POs, codes them against your context and routes only the exceptions").
- KB (Tier 1) — PO machinery: "Managing and Editing Purchase Orders (POs)… create, revise, and customize Purchase Orders… merge newly approved items, or remove line items back to your Procurement list using the Revise [function]"; "How to manually close a Purchase Order"; Auto PO ("What are Automatic Purchase Orders?", combining multiple Auto POs, custom PO numbering); Blanket Purchase Orders (create blanket PO request, blanket PO items); "What is PO Promise Date?"; "How to Link a PO to a Contract"; PO PDF labels/logo; procurement flags on PO items.
- KB (Tier 1) — Receiving: "How to Receive, Unreceive, and Manage Packing Slips — Record the arrival of goods, attach proof of delivery via web or mobile, and understand how receiving actions automatically update your Accounts Payable for invoice matching."
- KB (Tier 1) — Vendors: vendor records with internal vs external vendor IDs; add/update/decommission vendors; disable vendor creation (governed vendor master); default vendor tax rate; automatic remittance emails.
- KB (Tier 1) — Catalog: Product Catalog items with department tags, bundling, imports, pictures.
- KB (Tier 1) — Roles/permissions: Purchaser/Buyer role; "How to view a Purchase Order as an Accounts Payable user"; "Can I limit a Purchaser's ability to view Purchase Orders from certain locations/departments?" (permission scoping by location/department).
- Integrations: QuickBooks, NetSuite (bundle-based), Sage Intacct, Dynamics 365 Business Central; punch-outs (Amazon Business, Staples, ZAGENO); API; mobile apps (iOS/Android).
- Adjacent spend surfaces: Spending Card (prepaid company cards), Expense Reports, Budget Management, Spend Insights, Bill Payments.
- Positioning: mid-market ("Enterprise control, without the enterprise drag"; G2 "Leader for Mid-Market Procure-to-Pay Software" — vendor-cited award).

### Coupa (market anchor only)

- Unreachable (403 ×2 + transport error). No operational claims drawn. Its existence as a frequently named enterprise P2P/spend-management competitor is corroborated by the other vendors' own comparison/FAQ content (Procurify maintains a Coupa comparison page; JAGGAER FAQ names Ariba and Coupa).

## Cross-product Comparison

| Dimension | SAP Ariba | Basware | JAGGAER | Procurify |
|---|---|---|---|---|
| Self-positioning | enterprise source-to-pay suite ("Autonomous Spend Management") | AP-first P2P ("start with AP", add e-procurement) | enterprise S2P, direct+indirect on one data layer | mid-market "agentic procurement" platform |
| Demand capture | intake front door + guided buying + requisitions | e-procurement requisitions (upstream add-on) | purchase requisitions + guided buying | intake-to-approve requests (requisition-centric) |
| Catalogs | catalog management (collect/validate/enrich/classify/approve) + catalog APIs | consumer-style shopping, catalog management, stock integration | shopping catalogs | product catalog (items, bundles, tags) |
| Punch-out | network-based collaboration (SAP Business Network) | (not observed on fetched pages) | OCI punchout standard; higher-ed punchout buying | Amazon Business / Staples / ZAGENO punch-outs |
| PO machinery | POs auto-created; demand aggregation into RFQs | POs issued automatically per approved line item | purchase order management; request→PO automation | PO revise/merge/close, Auto PO, blanket POs, promise dates, PO↔contract link |
| Receiving | goods receipt, service entry sheet, return, quality tracking | receiving named in P2P definition | goods receipts + ASN + quality management | receive/unreceive, packing slips, proof of delivery; receiving updates AP matching |
| Invoice side | central worklist, touchless, non-PO + services invoices, workflow builder | touchless AP: coding/routing/matching/exceptions; InvoiceAI PO & non-PO | invoice management with 3-way matching; autonomous AP | invoice extraction, PO matching, coding, exception routing |
| Matching | automated invoice processing incl. reconciliation | first-pass match on PO-based invoices (KPI framing) | 3-way matching | matches invoices to POs (receiving feeds matching) |
| Budget | (not explicit on fetched pages) | budget check matrices at requisition time | budget management | budget management |
| Contract linkage | enterprise contract orchestration → ERPs | (not explicit) | contracts in S2C enforce in purchasing | link PO to contract; contract management |
| Payment | early-payment discounts via network; invoicing assistant covers "payment scheduling" | chain ends "ready to pay" (AP-centric) | payments management | bill payments |
| Supplier participation | SAP Business Network (supplier collaboration, onboarding) | e-invoicing network; supplier resources | supplier network (13M+ claim), onboarding, performance | vendor records; remittance emails; (portal not observed) |
| ERP relationship | multi-ERP real-time spend tracking; worklist integrated to SAP ERP | complements ERP; pulls POs from any source; 250+ ERPs (vendor claim) | 1,000+ connectors; managed integration layer | syncs to QuickBooks/NetSuite/Intacct/Dynamics BC |
| Verticals | services procurement (SOW/milestones), 40+ country e-invoicing mandates | global SSC, multi-ERP | manufacturing (BOM/ASN/VMI/quality), public sector, higher ed | education, healthcare, biotech, manufacturing, tech |
| Segment | enterprise (+ SNAP for midsize) | enterprise/global SSC (+ mid-market line) | enterprise | mid-market |

## Canonical Model (abstraction)

### L0 — Defining Invariant

The platform manages an organization's buying as a **linked chain of controlled transactional records**, executed by organizational actors under the organization's own approval structure, ending in a payment-ready payable:

```text
Supplier (external counterparty record)
└── Internal purchase demand, captured and approved before commitment
    └── Purchase order — the external commitment instrument to the supplier
        └── Confirmation of fulfillment against the order (receipt / acceptance)
            └── Supplier invoice validated against order + fulfillment (matching)
                └── Payment-ready payable (handed to payment / accounting)
```

Minimal elements — remove any one and the Type stops being recognizable:

1. **Supplier as external counterparty** — the party commitments are made to and invoices arrive from. Without it, the product is internal request workflow.
2. **Internal demand captured and approved before commitment** — the organization decides what to buy through a controlled request (requisition, guided-buying cart, intake request). Without it, the product is AP automation or order entry.
3. **Purchase order as external commitment** — an instrument sent to/against a supplier, with its own lifecycle. Without it, there is no procurement, only invoicing.
4. **Fulfillment confirmation against the order** — receiving/acceptance evidence that the supplier delivered. Without it, the chain has no delivery control.
5. **Invoice reconciled against order and fulfillment** — matching as the validation gate before payment. Without it, the product is uncontrolled bill pay.
6. **Organization's own approval structure governing transitions** — approvals are the org's rules, not the vendor's judgment. Without it, it is a shopping site, not a control platform.
7. **Chain linkage ending in a payment-ready payable** — each stage references its predecessors; the output is a validated payable. Without the linkage, the objects are disconnected tools.

Notes on minimality:
- Payment execution is **not** L0: the researched sample shows both native payment execution (JAGGAER Payments Management, Procurify Bill Payments) and handoff postures (Basware's chain ends at "ready to pay"; AP-side payment often executed by ERP/bank). The invariant endpoint is the *validated, payment-ready payable*.
- The requisition as a named document is **not** L0; the invariant is approved internal demand before commitment (implementations: requisition, guided-buying cart, intake request, direct PO under policy).
- Catalogs, budgets, contracts, supplier portals, AI extraction are **not** L0 (see L1/L2).

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- Catalogs and guided buying (consumer-style shopping; preferred suppliers; negotiated pricing compliance)
- Punch-out to external supplier stores (observed in 3 of 4 products; Basware equivalent not observed on fetched pages)
- Approval workflow engine (amount/department/vendor rules; delegation; mobile/email approval; line-level partial approval observed in Basware)
- Budget checking at request time (Basware budget check matrices; JAGGAER Budget Management; Procurify Budget Management)
- Contract linkage (PO↔contract; contract compliance; Ariba contract orchestration distributing terms to ERPs)
- Invoice capture and extraction (email/portal/network intake; AI extraction; central worklist)
- Matching automation with tolerance and exception queues (2-way/3-way; only exceptions routed to humans)
- Non-PO invoice path (coded and approved without a PO — explicit in Ariba, Basware, Procurify)
- Supplier master management and onboarding (governed vendor records; internal vs external IDs)
- Supplier collaboration surface (portal/network: PO transmission, ASN, invoice submission, status, remittance)
- ERP/accounting integration (posting approved payables; vendor/GL sync; multi-ERP support is a selling point in all four)
- PO lifecycle machinery (revise/merge/close; auto-PO; blanket POs; promise dates; PO↔contract links)
- Receiving mechanics (receive/unreceive, packing slips, proof of delivery; receiving feeds invoice matching)
- Payment execution (common but not universal — see L0 note)
- Audit trail, roles/permissions, segregation of duties (buyer vs AP vs admin; location/department scoping)
- Analytics/spend visibility (spend by supplier/category/department; managed vs unmanaged spend)
- Mobile apps for requesters/approvers/receivers
- Demand aggregation and intake orchestration (bundle requisitions; single front door; no-code intake workflows — newer but present in Ariba and Procurify)

### L2 — Variant / Optional Structure

- **Segment posture**: mid-market purchasing-first (Procurify) vs enterprise suite (Ariba, JAGGAER) vs AP-led entry that grows upstream (Basware)
- **Direct-materials depth**: BOM-driven sourcing, ASN, VMI, supplier quality (SCAR/APQP/PPAP) — JAGGAER manufacturing; absent from mid-market posture
- **Public-sector compliance pack**: solicitations/bid publishing, cooperative purchasing, contract vehicles, public-records audit trail, multi-agency procurement
- **Higher-education pack**: grant-funded/project-based procurement, punchout catalogs, ERP integrations (Banner/Workday)
- **Services procurement**: SOW/milestone-based services spend, service entry sheets, labor/tax compliance (Ariba services procurement)
- **Sourcing/supplier-risk extensions**: S2C integration (sourcing events enforce in purchasing), supplier risk/ESG intelligence
- **Payment depth**: native payment rails/networks vs handoff to ERP/bank; early-payment discount programs
- **e-invoicing mandate compliance**: country-specific structured-invoice compliance packs (Ariba 40+ countries claim; Basware compliance hub)
- **Deployment form**: standalone cloud platform vs ERP-embedded module (ERP-native P2P satisfies the same chain inside the ERP)
- **Intake-orchestration posture**: platform as the front door for all spend types (newer posture, Ariba/Procurify)
- **Adjacent spend surfaces**: expense reports, corporate/spending cards bundled alongside (Procurify)

### L3 — Vendor-specific (Research Notes only)

- SAP: SAP Business Network; Joule assistants (Buying/Receiving/Invoicing); Ariba SNAP (midsize edition); "180 countries / 21 languages" services compliance; 40+ country e-invoicing mandates; central demand aggregation → RFQ publishing.
- Basware: InvoiceAI / SmartCoding / SmartPDF; Basware Marketplace; AP Protect / AP Audit & Recovery / Statement Matching; "not a jealous provider" interoperability stance; 250+ ERP claim; 50,000+ invoices/year target profile; KPI marketing figures (89% touchless, 98% first-pass match, 93% ready to pay).
- JAGGAER: JAGGAER One platform; JAI (embedded AI); JAGGAER Link (managed integration layer, 1,000+ connectors claim); Research Material Management; Value Tracker; 13M+ supplier network claim; competitive FAQ naming Ariba/Coupa (marketing claim, not treated as fact).
- Procurify: "agentic procurement" AI framing; Spending Card; product-tour library; G2 mid-market award citations; specific punch-out partners (Amazon Business, Staples, ZAGENO).
- Coupa: no claims (unreachable).

## Vendor-specific / Rejected Findings

- **"Community benchmarking" / vendor-vs-vendor claims** (JAGGAER FAQ asserting Ariba/Coupa need "multiple products and integrations"): rejected as marketing; not used.
- **Vendor KPI figures** (Basware 89%/98%/93%; JAGGAER 60%/50%/95% etc.): vendor marketing; recorded in notes, never asserted as general facts.
- **"Autonomous/agentic spend management"** (SAP, Procurify): current positioning layer; the underlying capabilities (auto-PO, matching, exception routing) are L1; the AI framing is era-specific and excluded from the definition.
- **Payment execution as definitional**: rejected — evidence shows both execution and handoff postures.
- **Requisition as a mandatory named document**: rejected as too implementation-specific; abstracted to "approved internal demand before commitment."

## Boundary Findings

1. **vs Accounts Payable Automation (§08, processed)** — AP automation starts at the supplier invoice and consumes POs from any source (its research notes explicitly record that Basware matches invoices against POs generated in other systems). P2P owns the upstream chain: demand capture, PO creation, receiving. Test: remove requisition/PO-creation/receiving → AP automation remains; make them primary → P2P. Suite-creep is real from both directions (Basware AP-first growing upstream; AP vendors marketing P2P suites) — the boundary is center of gravity, not product packaging.
2. **vs Purchase Order Management (§10 sibling, unprocessed)** — PO management centers the single PO object's lifecycle (create/track/change/close); P2P centers the chain-wide flow including demand capture, receiving, and invoice reconciliation. Test: remove invoice matching + receiving + demand intake → PO management remains. Flag for joint review.
3. **vs Procurement Management Platform (§10 sibling, unprocessed)** — in market usage "procurement management" often denotes the broader source-to-pay scope (sourcing + supplier management + P2P); P2P is the transactional execution subset (request→pay). Probable superset/alias-adjacent relationship — flagged for joint review.
4. **vs Strategic Sourcing Platform / E-sourcing Platform (§10 siblings, unprocessed)** — upstream competitive events (RFx, auctions, supplier selection) ending at contract; JAGGAER's own FAQ draws the line: S2C = spend analysis through sourcing events, supplier selection, contract execution; P2P = buying, fulfillment, invoicing, payment. Test: remove sourcing events/award → P2P remains.
5. **vs Invoice Processing Platform (§08 sibling, unprocessed)** — capture/extraction-centric single-object processing; the front half of the AP pipeline. P2P's invoice stage presupposes the upstream chain. Test: remove PO/receipt context → invoice processing remains.
6. **vs ERP (§10, processed)** — the ERP records the same document chain as part of the books (its research notes name procure-to-pay as a unified ERP process); the P2P platform is the buyer-facing operational layer that hands postings to the ERP and explicitly does not replace it (Basware: "does not replace your ERP"; Ariba: multi-ERP tracking). Test: remove the general ledger/subledgers → P2P platform still functions; remove the operational buying layer → ERP remains.
7. **vs Expense Management Platform (§08 sibling, unprocessed)** — employee out-of-pocket spend (receipts, reimbursement, cards) has no supplier PO/matching; P2P platforms bundle expense/card surfaces as adjacent modules (Procurify). Test: remove supplier commitment chain → expense management remains.
8. **vs Supplier Portal (§10 sibling, unprocessed)** — supplier-facing slice (PO receipt, ASN, invoice submission, status) of the same chain; P2P includes a supplier collaboration surface as L1 but its center is the buyer organization. Test: remove the buyer-side chain → supplier portal remains.
9. **vs Spend Analysis Platform (§10 sibling, unprocessed)** — analytics layer over spend data; P2P includes spend visibility as L1 but does not center on analysis. Test: remove the transactional chain → spend analysis remains.
10. **vs Government Procurement Platform (§24 sibling, unprocessed)** — public-sector procurement shares the chain but adds solicitation/bid/publishing machinery and public-records obligations (observed in JAGGAER's public-sector vertical); likely a regulatory/sector variant or adjacent Type — flagged for joint review.
11. **ERP-native P2P modules** — the same chain inside an ERP (PR→PO→GR→IV→payment) satisfies the L0 loop; the standalone Type is the same chain as a dedicated layer beside the books. Recorded as an observation, consistent with the ERP research notes; no taxonomy change proposed.

## Historical / Market-Sample Check (§24)

- **ERP-native procure-to-pay** (SAP MM-era PR→PO→GR→invoice verification→payment run; corroborated by the repo's ERP research notes naming procure-to-pay as a canonical ERP process): satisfies L0 with none of the modern AI/intake/network machinery. ✓
- **2000s-era e-procurement** (catalog + requisition + PO + matching, no AI, no networks): satisfies L0. ✓ (reasoned from Basware's 40-year lineage and the stability of the documented chain; not directly fetched)
- **Public-sector e-procurement** (JAGGAER public-sector vertical, directly observed): same chain + solicitation/compliance overlays. ✓
- **AP-led P2P** (Basware: customers starting from invoice automation and adding e-procurement later): the full chain is the target state; the invoice-led entry is a deployment sequence, not a different structure. ✓
- **Regional check**: EU e-invoicing mandates and Latin-American fiscal invoicing add L2 compliance overlays; the L0 does not depend on mandates (Basware compliance hub and Ariba mandate pages observed as overlays). ✓
- **Small-organization check**: Procurify's mid-market customers satisfy the same chain with lighter configuration. ✓
- Conclusion: L0 does not over-fit the current AI/intake era; the chain formulation accommodates older, ERP-native, regional, and sector products.

## Uncertainties

- Exact per-product state vocabularies (requisition/PO/invoice status labels) were not fetched at field level for Ariba/Jaggaer/Basware; the final document describes lifecycle states conceptually only.
- Whether payment execution is majority-standard across the market is unverified; treated as common-but-not-universal.
- Coupa unreachable — no claims; it remains a named market anchor via other vendors' comparison content only.
- Ivalua unreachable — not sampled.
- Matching tolerance defaults, approval threshold mechanics, and per-product permission matrices were not researched; no precise values asserted anywhere.
- Punch-out prevalence: observed in 3 of 4 sampled products (Basware equivalent not observed on fetched pages) — treated as common, not universal.
- The newer "intake orchestration" posture (Ariba intake management, Procurify intake-to-approve) is documented from two products; its market breadth is unverified — kept as a common modern capability, not a definitional shift.

## Final Synthesis

A Procure-to-pay Platform is an organization-facing application that manages buying as a linked chain of controlled records — approved internal demand → purchase order to a supplier → confirmation of fulfillment → supplier invoice reconciled against order and fulfillment → payment-ready payable — with the organization's own approval structure governing each transition and the accounting system remaining the system of record. Around this chain, mature products add catalogs and guided buying, budget checks, contract linkage, invoice capture/extraction, matching automation with exception queues, supplier collaboration surfaces, ERP integration, payment execution, audit/permissions, and analytics. Segment posture (mid-market purchasing-first vs enterprise suite vs AP-led entry), direct-materials depth, sector compliance packs (public sector, higher ed, services), payment depth, and deployment form are variants. The defining boundary: AP automation starts at the invoice; sourcing ends at the contract; PO management centers one object; the ERP holds the books — the P2P platform is the chain between demand and payment that connects them all.
