# Dangerous Goods Transportation Management

## Overview

A **Dangerous Goods Transportation Management** application is the regulatory-compliance system of record for moving hazardous goods. It maintains each product's dangerous-goods classification in the vocabulary of the transport regulations, determines for every consignment what the applicable regulation permits and requires — packaging, marking and labeling, quantity limitations, forbidden-goods rules — and produces the legally required transport documentation and the data handoff through which a carrier accepts and carries the goods.

It solves a problem ordinary shipping software does not touch: a package of flammable liquid, lithium batteries, or compressed gas cannot be shipped by choosing a carrier and printing a label. Its hazard identity must be known in regulation terms, its transport must be judged legal under the regulation that governs the intended mode and region, and it must travel with specific documents and markings whose accuracy is legally the shipper's responsibility. Getting this wrong stops shipments at carrier acceptance, invites fines and audits, and creates safety incidents.

The boundary of the Type is the hazard-compliance spine of the consignment. It is not carriage execution (that belongs to transportation management and forwarding systems), not condition monitoring (cold-chain monitoring), not facility chemical inventory and safety-data-sheet management, and not customs or trade compliance — though it hands data to, and receives data from, all of those.

## Users & Context

Primary users are on the shipping side:

- **Dangerous goods / compliance specialists** at manufacturers and distributors — own the classification of products, answer "can we ship this, this way, to there", and sign off on determinations. Adjacent roles that share the work include product stewards and regulatory-affairs specialists, because classification decisions are made when products are formulated or re-formulated, not only when they ship.
- **Shipping and logistics staff** — execute compliant shipments: select the consignment's items, apply the determined packaging and labels, produce the transport documents, and hand the shipment to the carrier.
- **Freight forwarders' DG desks** — do the same work for customer consignments across modes, often at higher volume and multi-modal complexity.

Secondary users are on the acceptance side:

- **Airline and ground-handling acceptance staff** (and their road/sea equivalents) — validate that arriving dangerous-goods consignments carry correct, complete documentation and data before carriage; modern products automate much of this check and let staff work a digital checklist.

The work context is document- and deadline-driven: regulations are revised on fixed cycles, determinations must be auditable years later, and a refused shipment at acceptance is a direct cost. The user sitting in front of the software is usually working from an order, a product list, and a destination — and the software's job is to turn that into a legally shippable consignment.

## Core Model

### The Defining Core

Three structures, all required:

```text
Product / material
  └── Dangerous goods classification (per regulation)
        └── applied to a Consignment
              └── Compliance determination (mode × region × quantity)
                    └── Transport documents + carrier-acceptance data
                          └── Carriage (outside the Type)
```

**1. The dangerous goods classification record.** A maintained, per-product (or per-material/formulation) record that expresses the product's hazard identity in the vocabulary of transport regulation: the UN number, the proper shipping name, the hazard class or division, the packing group, and the regulation's per-regime specifics. Classification is *determined*, not looked up — a rule-driven act that weighs the product's composition against the regulation's criteria — and it is master data: it exists before any shipment and is maintained as regulations change. It is also not the same as the workplace safety data sheet: transport regulations and hazard-communication regimes use different rule sets, and the industry itself warns that safety data sheets frequently do not carry an accurate transport classification.

**2. The regulation-scoped compliance determination of a specific consignment.** Given a set of classified items, a mode (air, sea, road, rail), a destination and route, and the quantities and packaging involved, the application applies the governing regulation and produces a recorded determination: whether the consignment may be carried at all, under which quantity provisions, in which packaging, with which marks and labels, and which jurisdiction- or carrier-specific variations apply. The determination is attached to the shipment as its compliance state — it is what acceptance later checks against.

**3. The compliant transport documentation and carrier handoff.** The application produces the shipping paper that must travel with the goods — the shipper's declaration being the classic air-mode form — from the classification and consignment data, and delivers the required structured data to the carrier side that must accept and carry the consignment. In modern implementations the document is increasingly a data object exchanged electronically rather than only paper, and the validated data flows onward into the carrier's operational processes.

Remove the classification record and the product collapses into generic shipping software with a hazard checkbox. Remove the determination and it collapses into a classification reference database. Remove the documents and handoff and it collapses into a knowledge base — no longer transportation management.

### Standard Capabilities

What mature products add around that core:

- **Multi-regulation coverage** — classification and determination content keyed by mode and jurisdiction, so one product base can serve air, sea, road, and rail consignments under their respective regulation families.
- **Regulation content as a maintained service** — the rules change on published cycles (the air-mode standard is reissued annually, with addenda between editions), so products carry vendor-maintained regulatory datasets and feed changes back into re-determination.
- **Quantity-limit machinery** — limited-quantity and excepted-quantity regimes, packaging specification tiers, and forbidden or hidden-goods determinations.
- **Marking and labeling output** — the labels and marks that the determination requires, as printable or electronically transmitted outputs.
- **Acceptance checking** — validation of the consignment's documents and data against the regulation before carriage; on the air-mode ecosystem this is explicitly automated acceptance with digital checklists, and shipper-side products mirror it as pre-dispatch checking.
- **Downstream operational data flow** — validated dangerous-goods data feeding carriage operations: in air transport, the crew notification document (NOTOC) and unit-load-device build-up are the named consumers.
- **Variation handling** — jurisdiction- and carrier-specific deltas layered on the base regulation, maintained as data.
- **Emergency-response information** — information provision duties that travel with the shipment.
- **Audit trail and record retention** — determinations, documents, and their rule basis kept reconstructable; document retention is itself a regulatory duty.
- **Training and competency records** — regulation-imposed training duties realized as tracked records in many products.
- **Integration spine** — ERP and order systems (classification as product master data), transportation-management and multi-carrier systems (dangerous-goods flags and data consumed at booking), electronic declaration exchange, and regulatory-content APIs.

### Concept vs Implementation

```text
Concept:                 Common implementations:
Classification record     per-product master data; regulation-keyed datasets;
                          vendor-supplied content libraries and APIs
Determination             rule engines with explainable decision trees;
                          automated acceptance validation; manual expert review
Transport document        paper declaration; electronic declaration (data object);
                          document image + structured data exchanged together
Handoff                   paper at tender; e-declaration to carrier systems;
                          APIs into carriage operations (crew notification, load build)
```

## How It Works

### Maintain the classification

```text
Product created or re-formulated
→ composition/SDS data assembled
→ classification determined against the regulation's criteria
   (rule engine and/or expert, with recorded reasoning)
→ classification stored per applicable regulation as product master data
→ regulation content updates arrive
→ impacted classifications flagged and re-determined where needed
```

This loop runs continuously in the background of the business. An annual regulation revision can change packing instructions or quantity provisions, which can silently invalidate previously compliant setups — hence the impact-review step.

### Ship a consignment

```text
Order / delivery for a hazardous item
→ items pulled with their classifications
→ mode + route + destination + quantities assembled
→ determination run: permitted? which quantity provisions?
   which packaging? which marks/labels? which variations?
→ blocked if forbidden; corrected if data missing
→ transport documents produced; labels/marks output
→ declaration data handed to carrier (electronic or paper)
→ carrier acceptance check against the regulation
→ carried; validated data flows to carriage operations
```

The determination is the gate: a consignment that fails it does not ship until the conflict is resolved (different mode, different quantity, different packaging, or re-classification).

### Accept a consignment (carrier side)

```text
Consignment arrives with declaration / e-declaration data
→ acceptance check against the governing regulation
   (automated validation + staff checklist)
→ accepted, or rejected with reasons back to the shipper
→ validated DG data feeds operational processes
   (crew notification document, load planning, accounting)
```

On the air-mode ecosystem this acceptance step is a distinct, systematized surface shared across airlines, ground handlers, forwarders, and shippers through one validation layer — the clearest existing example of the industry moving the DG document from paper to data.

### Core vs Common vs Optional

- **Defining core** — classification record; consignment-level determination; document production and carrier handoff.
- **Standard capabilities** — multi-regulation libraries, maintained content service, quantity-limit machinery, labeling output, acceptance checking, downstream data flows, variations, audit/retention, training records, integrations.
- **Optional / variant** — AI-assisted classification with explainable reasoning, scenario simulation ("what if we change this formulation?"), special-cargo program depth (lithium batteries, infectious substances, radioactive material), packaging-side tooling, incident-reporting support, emergency-response service integration, storage-segregation extensions (which shade into facility-side hazmat management).

## Interfaces

Described conceptually; exact layouts vary by product.

### Classification workbench

The surface where a product's hazard identity is determined and maintained.

- Typical information: product/material identity, composition or formulation inputs, applicable regulations, the resulting UN number / proper shipping name / class / packing group per regime, the rule basis behind the result.
- Primary actions: run or review a classification, record reasoning, compare alternatives, simulate a change, mark classifications for review after regulation updates.

### Consignment / shipment determination view

The working surface for shipping staff and forwarder DG desks.

- Typical information: consignment items with classifications, mode and route, quantities against the applicable limits, required packaging, marks and labels, applicable variations, current compliance state.
- Primary actions: run the determination, resolve failures (split quantities, change mode or packaging), produce documents, print/transmit labels, release to the carrier.

### Document generation surface

Produces the shipping paper and its electronic equivalent from the same record.

- Typical information: declaration form populated from classification and consignment data, carrier and consignee details, supporting documents.
- Primary actions: generate, review, sign/authorize, transmit electronically or print, archive.

### Acceptance-check surface (carrier/operator side)

- Typical information: incoming declaration data, validation results per check against the regulation, exception details.
- Primary actions: run automated validation, work a digital checklist, accept or reject with reasons, pass validated data downstream.

### Regulation reference / content administration

- Typical information: the regulation libraries in force, their versions and effective dates, jurisdiction and carrier variations, update notices.
- Primary actions: browse/look up provisions, review content updates, manage which regulation set applies to which flows.

### Administration and integration consoles

- Typical information: product-master mappings, ERP/TMS/carrier connections, content subscriptions, user roles.
- Primary actions: configure integrations, manage roles and audit settings.

## Important Rules / Behaviors

### Classification is the shipper's responsibility

The transport regulations place correct classification on the shipper — the application operationalizes that responsibility but does not transfer it. This is why the classification record, with its recorded rule basis, is master data rather than a suggestion.

### The determination is mode- and region-specific

The same product can be shippable by sea and restricted by air, legal in one quantity regime and forbidden in another, permitted for one carrier and refused by another under its own stricter rules. Carriers may impose requirements beyond the regulation and may refuse even compliant shipments. Hence the determination is always scoped to mode × jurisdiction × carrier posture, and variation data is first-class content.

### Safety data sheets are not transport classification

Workplace hazard-communication documents (SDS/MSDS) are frequently inaccurate for transport purposes, and some products require none at all. Transport classification must be determined from transport criteria; products that also author SDSs keep the two determinations separate.

### Regulation content is perishable

Rules are reissued on fixed cycles and amended between cycles. A previously compliant consignment setup can become non-compliant without anyone acting — so content updates trigger re-determination impact reviews, and effective dating of regulation versions is built into determinations.

### Documents must match data

Acceptance checks validate the declaration against the regulation and against the physical consignment. A document that disagrees with the shipment's data is a rejection. In the electronic ecosystem, the declaration itself becomes validated data consumed downstream — which is why data quality (not just form filling) is the product's discipline.

### The compliance trail is a legal record

Determinations, documents, and their rule basis are retained and auditable for years; document retention is a regulatory duty, and explainability of a classification decision (which rules were applied and why) is a first-class requirement, not a nicety.

## Variants

- **Creation-side products** (shippers and forwarders): classification maintenance, determination, document production; depth in ERP/order integration.
- **Acceptance-side products** (carriers, ground handlers): automated validation and checklists, rejection handling, downstream operational data supply; depth in volume processing.
- **ERP- and suite-embedded DG management**: dangerous-goods assessment as a step inside broader product-compliance or supply-chain suites, fed by licensed regulatory content.
- **Classification-content and API supply**: the regulation logic sold as content/APIs embedded in other systems rather than as a standalone workflow.
- **Mode-specific depth**: air-acceptance ecosystems on one end; sea/road/rail regulation tooling and regional rule sets on the other.
- **Special-cargo tuning**: battery, infectious-substance, and radioactive programs with their own regulation publications and product tuning.

A variant remains a variant unless it changes the users, core objects, and rules enough that the model above no longer applies — for example, facility-side hazmat management without any consignment spine is a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Transportation Management System / TMS | adjacent, complementary | plans, tenders, executes and settles carriage; DG management determines *whether/how* hazmat may be carried and produces its papers; TMS consumes DG flags and data at booking |
| Freight Forwarding System | adjacent, complementary | the forwarder's multi-mode customer order and carriage coordination; DG compliance is a gate and document set inside that flow |
| Air Cargo Management | adjacent, complementary | air carriage itself — flight capacity, terminal handling, AWB lifecycle; DG acceptance and crew-notification data flow into it |
| Cold Chain Transportation Monitoring | sibling special-cargo type | hazard-class compliance (classification, documentation, packaging) vs condition preservation (measured environment vs requirement) |
| Hazardous Materials Management | adjacent (facility side) | chemical inventory, SDS, storage and worker safety at facilities; no consignment spine; different classification regime from transport |
| Global Trade Management | same pattern, different regulatory object | both hold product master classification → transaction-level determination → regulatory output; trade compliance answers tariff/origin/sanctions/customs, DG answers hazard/packaging/quantity limits for transport safety |
| Customs Compliance Platform | adjacent output boundary | customs declarations vs DG transport documents — different authorities, vocabularies, and outputs that may coexist on one shipment |

The TMS and forwarding boundaries are the load-bearing ones: dangerous-goods management does not book, route, or pay for carriage. It decides what may travel and with what paperwork, and hands that decision to the systems that do.

## Representative Products

- **IATA DG AutoCheck Solutions** (DG Digital for declaration creation; DG AutoCheck for automated acceptance; Connect API for downstream carriage operations) — the air-mode ecosystem realization.
- **3E** (3E Agent for Classification; 3E ERC+ dangerous-goods assessments within SAP Product Compliance; 3E Regulatory Intelligence API) — the classification-content and ERP-embedded realization.

Market anchors widely referenced by practitioners — standalone DG shipping software (e.g., the Labelmaster DGIS and DGOffice families) and ERP-embedded DG modules (e.g., SAP's dangerous-goods management) — could not be verified from official documentation during this pass and are recorded, without operational claims, in the Research Notes.

## Sources

Research date: **2026-09-07**

- IATA — Dangerous Goods (HAZMAT) program page: https://www.iata.org/en/programs/cargo/dangerous-goods/
- IATA — DG AutoCheck Solutions: https://www.iata.org/en/services/compliance/dg-autocheck/
- IATA — Dangerous Goods Regulations (DGR): https://www.iata.org/en/publications/dgr/
- 3E — 3E Agent for Classification: https://www.3eco.com/ai-solutions/3e-agent-classification/
- 3E — 3E ERC+ (Integrated Regulatory Content for SAP): https://www.3eco.com/3e-solutions/product-stewardship/3e-erc/
- Boundary context: VelocityEHS (EHS chemical management) — https://www.velocityehs.com/ ; Sphera (Hazardous Materials Management) — https://sphera.com/ ; AEB (trade compliance / TMS / multi-carrier, dangerous-goods data fields and carrier-service flags) — https://www.aeb.com/ and https://service.aeb.com/hc/en/search?query=dangerous+goods

> Sourcing limitation: the standalone shipper-side software pole (Labelmaster DGIS, DGOffice), the ERP-embedded DG module pole (SAP), carrier DG pages (FedEx/UPS), and the sea/road/rail regulator sites (IMO, UNECE, ICAO, PHMSA) were unreachable from the research environment on 2026-09-07 and were abandoned after repeated failures. Operational specifics are therefore anchored on the reachable official sources above (the air-mode standard and ecosystem, and the classification-content/ERP-embedded product line), and the document deliberately avoids precise numeric limits, exact document field lists, and named default settings for the unverified poles. Multi-mode and standalone-product mechanics are stated at correspondingly reduced strength. Detailed evidence, cross-product comparison, and the unreachable-source list are recorded in the paired Research Notes.
