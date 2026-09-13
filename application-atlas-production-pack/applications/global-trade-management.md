# Global Trade Management

## Overview

A **Global Trade Management** application is an importer/exporter-side system of record for the compliance and fiscal machinery of physically moving goods across customs territories. It binds products to the trade regulations that apply to them through classification, screens the parties involved in each cross-border transaction, determines whether export licenses or import permits are required, calculates the duties and taxes the goods will owe, and produces the declarations and trade documents that customs authorities, customs brokers, and trading partners require.

The application exists because a cross-border sale is not just a shipment — it is a legally regulated event. A machine part can be freely sold domestically and require an export license abroad; an apparel import's true cost is invisible without duties, tariffs, and taxes; a supplier's component decides whether a finished good qualifies for a free trade agreement. GTM software turns that regulatory layer into managed data and workflow.

Its boundary: it is not the system that plans and executes the carriage of the goods (a Transportation Management System), and not the ledger that owns the commercial order (ERP / order management). It sits between them as the compliance layer the order-and-shipment flow must pass through — and it is broader than a pure customs declaration tool, because it also owns export/import control decisions, origin qualification, and duty-reduction programs.

## Users & Context

Primary users:

- **trade compliance managers and analysts** — own the compliance determination of transactions; resolve screening hits and exception cases
- **customs managers / customs specialists** — own classification, declarations, entry processes, and relationships with customs authorities and brokers
- **export-control officers** — manage country controls, license determination, and license usage
- **trade operations / logistics coordinators** — prepare shipments with the right documents and data so goods release at the border
- **duty and origin analysts** — run free-trade-agreement qualification and duty program participation

Secondary users: finance teams (landed cost, duty savings), managers (compliance dashboards), IT integrators (connecting orders, shipments, and master data), and external collaborators — customs brokers, freight forwarders, and suppliers who exchange data and certificates through portals or integrations.

Typical context: manufacturing, distribution, and retail organizations with meaningful cross-border volume. The work is event-driven: an export order or shipment created in an upstream system triggers screening and document work; an inbound purchase triggers import documentation and entry preparation. Industry tilt varies — high-tech, semiconductor, aerospace, and pharmaceutical companies lean on export-control and licensing; retailers and consumer-goods importers lean on duty, origin, and landed-cost work.

## Core Model

The system is organized around four linked structures. Understanding them means understanding the type.

### The defining core

```text
Product trade master (classification + origin)
        ↓ applied to
Cross-border trade transaction (an import or export movement of goods)
        ↓ screened and determined
Compliance outcome (clear · hold for review · licensed · blocked)
        ↓ produces
Customs-facing output (declarations + trade documents)
        underpinned by duty / origin / valuation determination
```

- **Product classification.** Every traded product is classified against tariff and trade-control catalogs — harmonized-system-family tariff codes on the customs side, and export control classification lists on the control side. The classification is the join key between a product and the law: it drives the duty rate, whether a license is needed, what documents are required, and which programs the goods may enter. Classification is maintained as governed master data, not re-decided per shipment.

- **The cross-border trade transaction.** The unit the system evaluates and records is a specific import or export movement of goods — typically arriving as an order, shipment, or line-item stream from an ERP, order management, or transportation system. On it hang the parties, the classified lines, the countries of origin and destination, the values, and the determinations and documents produced for it.

- **The compliance determination.** Each transaction is checked against restricted-party and sanctions lists, against destination/embargo controls, and against export-control rules to determine whether a license or permit is required. The result is a recorded outcome on the transaction — cleared, held for review, licensed (often consuming tracked license capacity), or blocked. This gate, and the record it leaves, is what distinguishes trade management from document generation.

- **The customs-facing output.** From the transaction's invoice, shipment, and master data the system assembles customs declarations and trade documents — entry data for customs authorities (for direct filing) or pre-entry data packages (for a customs broker), plus certificates, licenses, and shipping documents. On the import side this rests on duty, tax, origin, and valuation determinations: what the goods owe and under what preference they enter.

### Standard capabilities layered on the core

Mature products across the researched sample commonly add:

- **Duty and landed-cost determination** — computing duties, taxes, tariffs, and often freight/handling/insurance to state the true landed cost of a purchase or sale, sometimes with scenario simulation.
- **Free trade agreement and origin management** — analyzing bills of material down to components, soliciting origin declarations and certificates from suppliers through campaigns or portals, and tracking certificates of origin against shipments.
- **Duty deferral and refund programs** — managing participation in foreign trade zones, bonded or customs warehouses, and duty drawback: deferring, reducing, or reclaiming duty, including reconciling inventory movements against program requirements.
- **Regulatory trade content** — continuously updated reference data (duty and tariff schedules, restricted-party lists, country rules, control lists) supplied by the vendor or its content partners; the application is, in practice, a consumer of this layer.
- **Trade document management** — generating, versioning, storing, and distributing trade documents, with archiving that supports later audit.
- **Partner collaboration** — exchanging declarations, entry data, and documents with customs brokers, freight forwarders, carriers, and customs authorities; soliciting data from suppliers.
- **Audit trail and reporting** — retaining the compliance determination and documents of each transaction as an inspectable record; reporting on screening hits, license usage, filing status, and duty savings.
- **Analytics** — dashboards over trade flows, compliance status, duty savings, and program utilization.

### One structure, several implementations

The core is conceptual; products implement each element differently:

```text
Concept:  classification
Impl.:    HS-family tariff codes · export control numbers · munitions/control lists

Concept:  screening
Impl.:    denied-party lists · sanctions and embargo regimes · internal watch lists

Concept:  customs output
Impl.:    self-filed electronic declarations · pre-entry data handed to a broker ·
          paper/electronic certificates and shipping documents

Concept:  duty determination
Impl.:    real-time per-transaction calculation · scenario landed-cost simulation ·
          program-based deferral/refund
```

## How It Works

### 1. Establish the trade master data

Before any transaction can flow, the system must know what the goods are and who the parties are: products are assigned tariff and export-control classifications and recorded countries of origin; trading partners (customers, suppliers, intermediaries) are registered and screened against restricted-party lists. This layer is maintained continuously — classifications are reviewed, screening runs against the partner base as lists change.

### 2. Gate each cross-border transaction

When an upstream system creates an export order or shipment (or an import arrives), the transaction enters the compliance gate:

```text
transaction received from ERP / order / TMS / WMS
→ screen all parties against restricted-party / sanctions lists
→ check destination and product controls (embargo, country control)
→ determine license / permit requirement
→ outcome recorded: clear | hold for review | licensed | blocked
→ if licensed: consume and record license usage
→ generate / collect required trade documents
```

Transactions that hit a control stop in an exception queue for a compliance analyst; clean transactions flow through automatically. On the import side, inbound shipment data is completed with supplier and broker documentation so entry data is ready when the goods arrive.

### 3. Build and submit the customs declaration

For each border crossing the system assembles the declaration from invoice data, shipment data, and the trade master data (classifications, origins, values) — either enriching it automatically from master data or prompting users for what is missing. The declaration is then either filed electronically by the importer itself (self-filing) or handed to a customs broker as structured pre-entry data; status flows back from customs authorities or the broker. Supporting documents — certificates of origin, licenses, and similar control paperwork — travel with the entry.

### 4. Run duty savings programs

In parallel with the transactional flow, trade teams work a program layer:

```text
identify candidate transactions / products
→ analyze bills of material for rules-of-origin qualification
→ solicit supplier declarations and certificates
→ enroll qualified flows in trade agreements or duty programs
  (FTA preference · foreign trade zone · bonded/customs warehouse · drawback)
→ reconcile program inventory and claims
→ realize and report the duty savings
```

This is program management, not a one-off calculation: qualification has to be maintained, certificates collected, program inventory reconciled against receipts and issues, and claims documented.

### 5. Audit and analyze

Every determination, document, and filing remains inspectable. Teams audit transactions, report to management and regulators, and analyze trade flows, screening outcomes, license usage, and duty savings. Landed-cost data feeds sourcing and pricing decisions elsewhere in the business.

## Interfaces

The main working surfaces, described conceptually:

- **Transaction compliance screens** — an order/shipment view showing the compliance status of each cross-border transaction: screening results, control flags, license requirement, documents, duties. Primary actions: inspect determinations, release or escalate, attach documents.
- **Exception / hold queue** — the compliance analyst's worklist of held transactions and screening hits, triaged by risk. Primary actions: review evidence, resolve false positives, apply or request a license, block.
- **Classification workbench** — product-by-product maintenance of tariff and export-control classifications, with catalog lookup and change tracking. Primary actions: search catalogs, assign codes, record rationale.
- **Screening workbench** — list management and hit resolution: which lists, who was screened, when, and what happened to each potential match.
- **License / permit management** — the inventory of held licenses and permits with their conditions and usage. Primary actions: model or register a license, assign it, track consumption.
- **Declaration editor / filing workspace** — country-shaped declaration assembly from transaction data, with validation prompts before submission to customs or a broker; filing status tracking afterward.
- **Program workspaces** — FTA qualification projects (component analysis, supplier campaigns, certificate collection) and duty-program views (zone/warehouse inventory reconciliation, claims).
- **Document management** — the trade document library: generation, revision, distribution, archive.
- **Partner portals** — supplier-facing solicitation (origin data, certificates) and broker/forwarder-facing document and entry-data exchange.
- **Dashboards and reports** — compliance metrics, duty savings, filing timeliness, program utilization.
- **Integration surfaces** — the event and data seams to ERP, order management, transportation and warehouse systems that feed transactions in, and return holds, classifications, documents, and costs.

## Important Rules / Behaviors

- **The gate is enforced in the flow.** When a transaction meets an applicable control, the transaction is stopped pending resolution — held for review, or blocked — so that restricted goods do not move without the license, permit, or documentation in place. The exact mechanism (hold status on the order, a review case, an approval step) varies by product; teams work by exception in all of them: clean transactions pass automatically, hits land in a queue.
- **Screening covers both master data and transactions.** Partners are screened as records and again as part of each transaction, because lists change between the two moments.
- **Licenses are finite, tracked resources.** A license or permit typically carries conditions and capacity; using it for a shipment consumes recorded usage against it.
- **Classification drives everything downstream.** A product's tariff and control classifications determine the license decision, the documents, and the duties — which is why classification is governed master data and why a classification change ripples through licensing, declarations, and costs.
- **The system is only as current as its content.** Duty schedules, control lists, and restricted-party lists are regulatory content that changes continuously; vendors (or their content partners) supply updates, and the application's correctness depends on consuming them.
- **Declarations are assembled, not retyped.** Entry data is built from invoice, shipment, and master data, with validation to catch missing or inconsistent fields before submission.
- **Program inventory must reconcile.** Participation in deferral/refund programs imposes record-keeping: inventory movements into and out of zones or bonded warehouses are reconciled against program requirements, and claims must be documented to survive audit.
- **The audit trail is the product's spine.** The determination, the documents, the filing, and the outcome of each transaction are retained — compliance in this domain is proven after the fact.

Common exceptions: screening false positives that must be resolved quickly so shipments do not stall; missing supplier certificates blocking FTA claims; broker queries or amendments to entry data; retroactive claims (such as duty drawback) filed after import; classification corrections that touch many historical transactions.

## Variants

- **Deployment posture** — embedded in an ERP suite; a sibling module in a supply-chain suite next to transportation management; a standalone SaaS suite; or a federated combination of point products (classification service, screening service, country declaration product) plus purchased trade content.
- **Trade-side emphasis** — export-control-centric deployments (licensing, screening, documents) vs import-duty-centric deployments (entries, landed cost, programs); many organizations run both.
- **Filing posture** — self-filing against customs systems vs preparing pre-entry data for a customs broker; customs brokers themselves run declaration tools as a service for many importers.
- **Geographic depth** — country-specific declaration and filing support (each customs authority has its own processes), plus pre-arrival security filings in some jurisdictions.
- **Industry tuning** — export-control-heavy industries (high-tech, semiconductor, aerospace, defense), regulated goods (pharma, chemicals), FTA-heavy manufacturing (automotive), and high-volume retail/apparel importing.
- **Adjacent extensions** — global e-invoicing compliance, forced-labor and supply-chain traceability checks, trade-data market intelligence (who imports what, where), AI assistance for screening resolution and classification.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Transportation Management System / TMS | adjacent, tightly coupled | TMS plans and executes carriage — rates, carriers, routing, tracking; GTM determines whether goods may legally cross, what they owe, and what customs requires. They share the shipment as data, often as paired products. |
| Customs Compliance Platform | sibling slice | Declaration preparation and filing for customs authorities — often country-specific and often broker-operated. GTM includes that slice plus transaction-level screening/licensing, origin programs, and duty-program management. The sharpest seam: does the product record the compliance determination of the transaction, or only prepare declarations? |
| Sanctions Screening Platform | same technology, different domain | Screens financial transactions, payments, and customer onboarding against sanctions/AML rules; GTM screening is a step inside physical-goods trade transactions, attached to licensing determination. |
| Freight Forwarding System | provider-side adjacent | The forwarder's own operational system (bookings, consolidation, shipment files). A forwarder may use declaration software on behalf of importers, but the importer's trade-compliance program is not the forwarder's system. |
| ERP / Order Management | upstream owner | Owns the commercial order, purchase order, and invoice; GTM consumes them as the transaction stream to screen and determine, and returns holds, documents, classifications, and costs. |
| Supply Chain Planning | consumer of outputs | May use landed-cost estimates for sourcing decisions; performs no regulatory determination and produces no customs output. |
| Inventory Management / WMS | adjacent | Executes the physical stock movements; in duty-program deployments the GTM-side reconciliation compares itself against these movements rather than performing them. |

## Representative Products

- Oracle Global Trade Management (Oracle Fusion Cloud Transportation & Global Trade Management)
- E2open Global Trade Application Suite
- Descartes (Global Trade Intelligence and Customs & Regulatory Compliance product families)
- SAP Global Trade Services (ERP-embedded market anchor; its help documentation was not directly accessible during research — see Sources)

## Sources

Research date: **2026-09-07**

- Oracle — Global Trade Management product page: https://www.oracle.com/scm/logistics/global-trade-management/
- Oracle — About Oracle Fusion Cloud Transportation and Global Trade Management (Integration Playbooks for SCM): https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faips/otm-about-oracle-fusion-cloud-transportation-and-global-trade-management.html
- Oracle — Transportation and Global Trade Management Cloud, Get Started: https://docs.oracle.com/pls/topic/lookup?ctx=otm-latest&id=otm-gs
- E2open — Global Trade Management suite: https://www.e2open.com/global-trade/
- E2open — Export Management: https://www.e2open.com/global-trade/export-management/
- E2open — Duty Management: https://www.e2open.com/global-trade/duty-management/
- Descartes — Customs Declarations: https://www.descartes.com/solutions/customs-and-regulatory-compliance/customs-declarations
- Descartes — solution catalog (Global Trade Intelligence / Customs & Regulatory Compliance): https://www.descartes.com/
- SAP — Help Portal entry for SAP Global Trade Services: https://help.sap.com/docs/SAP_GLOBAL_TRADE_SERVICES

> Sourcing limitation: vendor help-center and documentation portals for the ERP-embedded pole (SAP) returned JavaScript-gated or access-restricted surfaces, and direct documentation paths for one vendor's implementation guide were unavailable. The research therefore rests on official product pages and publicly reachable documentation for Oracle, E2open, and Descartes, with the SAP product present in the sample only as a category anchor cross-referenced by another vendor's official materials. Vendor-published scale figures (list counts, country counts, filings per year, savings claims) were observed but intentionally excluded from this document; no precise numeric limits or defaults are asserted. Detailed observations, the cross-product comparison, and the historical-sample check are recorded in the paired Research Notes.
