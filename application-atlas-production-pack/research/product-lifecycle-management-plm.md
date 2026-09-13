# Research Notes — Product Lifecycle Management / PLM

## Research Goal

Understand what a Product Lifecycle Management (PLM) system actually is as an Application Type: what the central record is, what data it holds, how change is controlled, who uses it, how it hands off to manufacturing/ERP, and where its boundaries lie against BOM management, PDM/CAD, ERP, QMS, MBSE, product configuration management, and engineering document management.

This pass also discharges four pre-hung boundary flags from processed sibling passes:

1. **bill-of-materials-management** (§16, processed 2026-09-06) — joint review requested: "market gravitates to PLM-branded packaging (Duro self-labels PLM; OpenBOM lists a PLM capability; Aligni pairs PLM+MRP) while the BOM-management core remains extractable and independently sellable… boundary criterion = center of gravity (structural definition + controlled evolution as the managed world vs the full lifecycle estate of CAD vaulting/documents/requirements/quality); recommend joint review when the PLM leaf is processed."
2. **medical-device-lifecycle-management** (§22, processed 2026-09-08) — proposed seam: "generic product-data estate (CAD/PDM/BOM/change) vs device-regime record chain (design controls/risk file/submission evidence); enterprise PLM vendors serve device makers with medtech accelerators — packaging straddle to confirm from that pass's own sample."
3. **mbse-platform** (§16, processed 2026-09-09) — proposed seam: "product data estate (CAD/PDM/BOM/change/documents) vs system model; integration evidence exists (System Modeling Workbench for Teamcenter; Obeo Publication connecting to PLM/ALM repositories)."
4. **product-configuration-management** (§16, processed 2026-09-09) — proposed seam: "product-data estate (CAD/PDM/BOM/change/documents) vs the variant-space layer (PTC frames variant/configuration management as capabilities inside Windchill; a standalone configuration layer sits across PLM/ERP/CPQ without owning the estate)."

## Initial Boundary

Working hypothesis before research:

- PLM is the manufacturer's system of record for the product's definition — items/parts, product structure (BOM), documents/CAD files — with revision control and formal change management, spanning the product's life beyond the engineering design phase and serving functions beyond engineering.
- Nearest neighbors: Bill of Materials Management (structure-centered sibling), PDM (design-org data management — not a directory leaf; Engineering Document Management is the document-register sibling), Mechanical CAD (authors the model), ERP (consumes released definition), Manufacturing QMS (quality-event loop), MBSE (system model), Product Configuration Management (variant space), Engineering Change Management (unprocessed leaf — change process), Medical Device Lifecycle Management (device-regime record chain), PIM (commercial content).
- Main unknowns: Is the lifecycle span definitional or merely marketing? Is BOM part of the definition or just common? How deep does CAD integration go across the market? Where exactly does the estate end and the sibling Types begin?

## Research Questions

1. What is the central record in a PLM system, and what attaches to it?
2. How do revisions, lifecycle states, and change processes (ECR/ECO/ECN) actually work?
3. What is the relationship to CAD authoring tools (vaulting, check-in/out, visualization)?
4. Who uses the system, and what does each role do?
5. How does the released definition reach manufacturing/ERP?
6. Which capabilities are estate-defining vs modules vs industry packaging?
7. How do deployment models and customer tiers vary?
8. Where are the boundaries against the sibling Types listed above?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Pole |
|---|---|---|
| Teamcenter | Siemens | enterprise suite leader; broadest estate; on-prem/cloud/SaaS |
| Windchill | PTC | enterprise PDM-rooted PLM; packages + role apps; SaaS (Windchill+) |
| Aras Innovator | Aras | platform-based open PLM; low-code composable apps; Community Edition |
| Arena PLM | Arena (a PTC business) | cloud-native mid-market PLM; separate QMS product; multi-tenant SaaS |
| Centric PLM | Centric Software | industry-variant pole: fashion/retail/food/consumer-goods PLM |

Rejected/considered: Duro (startup-tier cloud PLM — unreachable, see Sources), Autodesk Fusion Manage (403), Dassault ENOVIA (same tier as Teamcenter/Windchill; skipped for breadth), OpenBOM/Aligni (already documented by the BOM pass as BOM-centered).

## Sources

Research date: **2026-09-09**. All fetches this pass.

| # | Source | Tier | Status |
|---|---|---|---|
| S1 | Siemens — Teamcenter product page (plm.automation.siemens.com/global/en/products/teamcenter/, served via siemens.com/en-us/products/teamcenter/) | 2 | OK |
| S2 | PTC — Windchill product page (ptc.com/en/products/windchill) | 2 | OK |
| S3 | PTC — Engineering Change Management technology page (ptc.com/en/technologies/plm/engineering-change-management) | 2 | OK |
| S4 | Aras — home page (aras.com) | 2 | OK |
| S5 | Aras — PLM Software capabilities page (aras.com/en/capabilities/product-lifecycle-management) | 2 | OK |
| S6 | Arena — PLM product page (arenasolutions.com/platform/plm/ → served at products/plm/) | 2 | OK |
| S7 | Arena — Engineering Change Management solution page | 2 | OK |
| S8 | Arena — Item & BOM Management solution page | 2 | OK |
| S9 | Arena — "What Is PLM?" education page (arenasolutions.com/what-is-plm/) | 2 | OK |
| S10 | Centric Software — home page (centricsoftware.com) | 2 | OK |
| S11 | PTC — Windchill Help Center (support.ptc.com/help/windchill/r13.0/wchelp/en/index.html) | 1 | 404 |
| S12 | Aras — Innovator product page (aras.com/products/aras-innovator) | 2 | 404 (root + capabilities pages used instead) |
| S13 | Duro — duroapps.com root and /plm-software | 2 | transport error ×2 → abandoned |
| S14 | Autodesk — Fusion Manage overview (autodesk.com/products/fusion-manage/overview) | 2 | 403 |
| S15 | Centric — /plm/ path | 2 | 404 (root used instead) |

**Source-access limitations:**

- No Tier-1 help centers were reachable this pass: PTC help center 404 (S11); Siemens documentation sits behind the gated support/docs portal (not attempted beyond the product page after the pattern seen in sibling passes); Aras docs portal not fetched (product/capability pages sufficient for the claims made); Arena publishes solution/education pages rather than a public help center.
- Duro abandoned after 2 transport errors (S13). The startup-tier cloud PLM pole is therefore under-sampled first-hand; the BOM pass's observation that Duro self-labels PLM is carried at cross-pass strength only.
- Autodesk Fusion Manage 403 (S14) — the CAD-vendor-adjacent mid-market pole is not sampled.
- Centric evidence is root-page strength only (S10) — industry-variant claims are kept weak accordingly.
- Consequently, **no precise operational mechanics are asserted anywhere** (exact lifecycle state names, revision-number schemes, workflow step sequences, numeric limits). All product observations below are at product/solution-page strength (Layer A for the named product; Layer B only where the same structure appears across products).

## Product Observations

### Siemens Teamcenter (S1)

Layer A observations (product page):

- Self-positioning: "Teamcenter PLM software — Plan, develop and deliver innovative products… a leading choice in product lifecycle management (PLM)."
- "Teamcenter provides a single source of product information for every stakeholder across the business." — the product-information system-of-record claim.
- Lifecycle framing: **Plan** ("set the strategic direction and product definition to guide downstream decisions") → **Develop** ("design and document the multi-discipline product") → **Deliver** ("weave the digital thread to connect product development with manufacturing, service and suppliers").
- "Leverage the digital twin: use digital twins to connect and optimize processes for designs, systems, software, simulation and visualization."
- Deployment variants: on premises (your IT team), on cloud (your provider, your IT team), Teamcenter X (SaaS operated by Siemens) — "Get Teamcenter delivered any way you want it."
- Audience span: "Start-ups to large enterprises – across industries."
- Estate breadth signals: PDM white papers, Product Cost Management (cost engineering), requirements ebook, GenAI (Teamcenter AI / Teamcenter Copilot).
- Analyst positioning: named in Gartner Magic Quadrant for PLM software; ABI Research "PLM for large discrete manufacturers"; Forrester Wave "PLM for Discrete Manufacturers".

### PTC Windchill (S2, S3)

Layer A observations (product page):

- Self-positioning: "Windchill is PTC's enterprise PLM software that connects product data, processes, and people across the entire product lifecycle."
- Key features enumerated by the vendor: BOM management ("align eBOM, mBOM, and software BOMs"); engineering change and configuration management ("automate and orchestrate change processes across mechanical, electrical, and software domains"); collaborative product and supplier development; manufacturing process management ("automated mBOM generation, process planning, and reusable work instructions"); parts classification; product variability management ("manage complex product configurations with scalable logic and rules-based modeling"); CAD integration, visualization, and PDM ("unify multi-CAD environments with centralized product data management, browser-based 3D visualization"); quality management ("closed-loop processes… support audits, CAPAs, and traceability"); supply chain collaboration.
- Application suite structure: Expert packages (base/advanced/premium "core PDM and PLM functionality"), role and industry add-ons, Non-expert packages (Windchill Navigate — "role and task-based apps for non-expert users to view and interact with product data"), visualization, enterprise system integrations (EAI to ERP), extensions.
- **PDM vs PLM (vendor's own FAQ)**: "PDM focuses on managing engineering data such as CAD files, versions, and design collaboration. PLM extends beyond engineering to manage the entire product lifecycle—from concept and design to manufacturing, service, and end-of-life."
- **ERP handoff (vendor's own FAQ)**: "Windchill acts as the system of record for product data—managing designs, configurations, and change processes—while ERP systems handle planning, procurement, and execution… only validated, released product data is transferred to ERP."
- Deployment: on-premises or PTC Cloud; Windchill+ (SaaS, FedRAMP authorized); PTC Jetstream (secure collaboration layer).
- Industry pages: Aerospace & Defense, Automotive, MedTech ("regulatory compliance and product quality with end-to-end traceability, document control, and closed-loop processes" — generic PLM machinery, no design-control/risk-file/submission semantics), Industrials, E&HT.
- Competitive FAQ: "Arena PLM is often used for cloud-based collaboration and mid-market product development, while Windchill is built for enterprise-scale lifecycle management."

Layer A observations (engineering change management technology page, S3):

- "Engineering change management is the process of creating, reviewing, and gaining formal approval for engineering change requests, engineering change orders, and engineering change notifications." (ECR / ECO / ECN vocabulary.)
- Process tiers: "full track (full CRB/CIB), fast track (change admin) or basic (lightweight CN only)" — change review board / change implementation board machinery.
- "Configurable change process: tailor a change process from simple and quick to deep traceability. Scale the process for different points in time such as prototype, new product introduction, and sustaining production."
- Problem report: "capture issues or opportunities for products and processes and determine next steps. Tie these to both change and quality processes."
- Deviation or waiver: "capture a 'temporary' change to a product or process as part of the standard change workflow."
- Engineering change notice: "create and execute the implementation plans for delivering the change to the enterprise. Allow for auditing and validation of the results prior to release of the data."
- Electronic signatures: "change records, including sign-offs, markups, and comments connected to product data with audit trails."
- Workflow: "repeatable, easy-to-use processes that deliver tasks automatically to users."
- "Automatic synchronization with manufacturing systems: publish updated information to downstream systems when changes are resolved."
- ECR vs ECO vs ECN distinctions spelled out in the FAQ (ECR = evaluate justification and plan; ECO = notify, seek approval, implement; ECN = implementation plan for delivering the change to the enterprise).

### Aras Innovator (S4, S5)

Layer A observations:

- Self-positioning: "Aras delivers a scalable platform for building open and adaptable PLM and digital thread solutions."
- Vendor's own PLM definition (FAQ): "PLM software is software used to manage product information, processes, and decisions across the entire product lifecycle, from requirements and design through manufacturing, delivery, service, and change. It provides a governed system for connecting product data, people, and workflows so organizations can maintain a single source of truth, improve traceability, and coordinate work across engineering and the broader enterprise. In the Aras view, PLM software is not just a database for product records; it is the foundation for a connected digital thread that links requirements, systems, BOMs, documents, quality, manufacturing, and service information."
- Lifecycle span: "from ideation to end-of-life" / "every stage of your product lifecycle, from ideation to end-of-life"; Forrester quote: "from as-designed to as-manufactured and as-maintained."
- Application library (composable apps over one platform): Requirements Engineering ("requirements in context with product configuration data"), Systems Architecture ("systems models as an integral part of your digital thread"), Product Engineering ("integrate BOM management, version control, and cross-functional workflows"), Program Management, Component Engineering ("single source of truth for part data, linked directly with supplier catalogs, compliance status, and lifecycle health"), Simulation Management, Variant Management ("product platform variability and reuse across all product representations"), Manufacturing Process Planning ("integrating EBOM and MBOM… extend your digital thread to the shop floor"), Technical Documentation, Quality Management System ("integrates CAPAs, audits, nonconformance reports, and risk data with baseline product definitions"), Digital Twin Core, Supplier Management.
- Platform philosophy: Product Data Platform ("extensible data model with shared services"), low-code development, composable app framework, Community Edition (downloadable), subscription.
- Interoperability pages: MCAD, ECAD, Simulation, Requirements, ALM, ERP connectors; open API.
- Industries: Aerospace & Defense, Automotive, Food & Beverage, High Tech, Industrial, Medical Devices.
- Customer stories: Technip Energies ("replacing an obsolete PDM system and bringing the management of As-Design and As-Built configurations, documents & geometries, engineering changes into Aras Innovator, and how the system provides interfaces with supply chain & manufacturing (ERP)"); Dräger (medical, cloud); Microsoft hardware (agile PLM platform); Kawasaki Robotics; Airbus; Toyota Motor Europe.

### Arena PLM (S6, S7, S8, S9)

Layer A observations:

- Self-positioning: "Cloud-native Product Lifecycle Management Software… Arena by PTC, the leading cloud-native product lifecycle management (PLM) software that helps manufacturers design, build, and deliver products"; "Arena invented Cloud PLM"; 1,500+ customers; multi-tenant SaaS.
- Vendor's own PLM definition ("What Is PLM?"): "Product lifecycle management is the management of all data and processes that are tied to the product record—from concept through design, development, and production."
- **PDM vs PLM (vendor's own education page)**: "PDM software provides a shared data repository for engineering workgroups to collaborate and manage design iterations. PLM software systems, however, extend beyond the design phase to manage all data and drive all processes associated with new product development and introduction (NPDI). Everyone on the team—not just engineering—can review the entire design and provide input before releasing the final product to production."
- **How PLM works (vendor's own education page)**: "provides a controlled and automated way to manage product and quality processes throughout the entire product lifecycle. It brings mechanical, electrical, and software designs into one shared platform—enabling dispersed teams to collaborate on the entire design before passing the released product to downstream systems."
- Product record: "brings all your critical product information—parts, assemblies, documents, requirements, quality processes, and change history—together in a single, secure, always accessible system"; "Manage the complete product record from concept through commercialization"; "Bring the Entire Product Record Together."
- Item & BOM management: "revision-controlled items and BOMs"; "engineering changes are linked to items, BOMs, and documents to create a solid, transparent product record foundation"; "links engineering changes (ECOs), manufacturers (AML), and vendors (AVL)"; BOM "includes the entire assembly and all associated components, files, drawings, and specifications required to build a shippable product… create, import, share, change, compare, and approve product designs throughout the entire lifecycle."
- Change management: "formal engineering change requests (ECR) and engineering change order (ECO) processes with automated approvals"; "changes connected to items, bill of materials (BOMs), drawings, and SOPs"; "automate approval routings based on specified criteria like change types, priorities, and product lines"; "review changes in context with all parts, BOMs, and documents linked to product and quality processes"; "proposal through implementation with email notifications and dashboards."
- Roles named: Design Teams, Engineering Teams, Component Engineers, Procurement Teams, Quality Teams, Supply Chain Partners, Executive Management, Cross-Functional Teams.
- PLM essentials enumerated: Item and BOM Management, Engineering Change Management, Document Management ("product specifications, assembly instructions, SOPs, quality policies, and training records… revision control and audit trails"), Regulatory and Compliance (FDA, ISO, RoHS, REACH, ITAR, EAR), Project Management, Requirements Management, Business Analytics, Enterprise Integrations (ERP — "ensures that manufacturing receives the latest released design"; MCAD/EDA design tools; component databases SiliconExpert/Octopart; CRM).
- Product structure: Arena PLM and Arena QMS are **separately named products** ("Arena Engineering Change Management is a foundational part of our PLM and QMS solutions"); QMS side carries Design Controls, Requirements Management, Issue Management, Training Management, Software Validation; compliance side carries Environmental, Cybersecurity & Export Controls, Medical Device Regulatory, QMS Compliance.
- Industries: high-tech electronics, medical device, consumer electronics, industrial, A&D, semiconductors, clean tech, IoT, EV; "small startup or Fortune 500 company."
- Government variant: Arena PLM for Government (GovCloud login).

### Centric PLM (S10)

Layer A observations (root page only — weak strength):

- Self-labels "Centric PLM… market-leading product lifecycle management" within an "End-to-End Product Platform From Concept to Commercialization" spanning "pre-season to in-season and end of season."
- Industries: Fashion & Apparel, Food & Beverage, Outdoor & Sports, Home & Furniture, Cosmetics & Personal Care, Consumer Electronics.
- Sibling product lines sold separately: Centric Planning, Centric Pricing & Inventory, Centric Market Intelligence, Centric Visual Boards, Centric PXM (PIM/DAM) — the PIM seam is vendor-drawn.
- Food case study: "Teway Food Achieves 100% Compliance Calculation Accuracy and Cuts Formula Updates to Minutes with Centric PLM" — formula/compliance content rather than parts/CAD.

## Cross-product Comparison

| Dimension | Teamcenter | Windchill | Aras Innovator | Arena PLM | Centric PLM |
|---|---|---|---|---|---|
| Central claim | single source of product information for every stakeholder | system of record for product data; connects data/processes/people across the lifecycle | governed system; single source of truth; "not just a database for product records" | management of all data and processes tied to the product record | end-to-end concept-to-commercialization platform |
| Product record | product information + digital twin | product data (designs, configurations, change processes) | product records + digital thread (requirements, BOMs, documents, quality, manufacturing, service) | product record (parts, assemblies, documents, requirements, quality processes, change history) | styles/products for consumer goods (weak evidence) |
| Definition data | multi-discipline product design & documentation | eBOM/mBOM/software BOMs; multi-CAD PDM; parts classification | BOM management, version control, part data (Product/Component Engineering) | revision-controlled items & BOMs + documents/drawings/SOPs | styles/BOMs/formulas (industry content; weak evidence) |
| Change control | in estate (change management across disciplines) | ECR/ECO/ECN; full/fast/basic tracks; CRB/CIB; e-signatures; audit trails; problem reports; deviations | change management capability page; engineering changes in customer stories | ECR/ECO with automated approvals; linked to items/BOMs/documents; approval routings | not observed at root-page strength |
| Lifecycle span | Plan → Develop → Deliver (manufacturing, service, suppliers) | concept → design → manufacturing → service → end-of-life | ideation → end-of-life; as-designed → as-manufactured → as-maintained | concept → design → development → production → commercialization | pre-season → in-season → end of season |
| Beyond engineering | every stakeholder across the business | manufacturing, quality, supply chain; non-expert role apps (Navigate) | engineering and the broader enterprise | everyone on the team, not just engineering; supply chain partners | merchandising/design/supply chain (consumer goods) |
| CAD relationship | PDM white papers; multi-discipline design | multi-CAD management, visualization, PDM as core feature | MCAD/ECAD connectors; simulation management | MCAD/EDA integration (integration-level, lighter) | none observed (fashion/food) |
| ERP relationship | digital thread to manufacturing | only validated, released product data transferred to ERP | ERP connectors; interfaces with supply chain & manufacturing (customer story) | ERP integration ensures manufacturing receives the latest released design | not observed |
| Quality | in estate | quality management feature (audits, CAPAs, traceability) | QMS app (CAPAs, audits, NCRs, risk) | Arena QMS = separate product | compliance calculations (food) |
| Requirements | ebook/strategy content | traceability via digital thread | Requirements Engineering app | Requirements Management essential | not observed |
| Variants/configuration | in estate | product variability management feature | Variant Management app | not prominent | colorways/sizes (industry; weak) |
| Manufacturing process | Deliver leg | mBOM generation, process planning, work instructions | Manufacturing Process Planning app (EBOM/MBOM) | DfM collaboration, ramp-up | not observed |
| Supplier collaboration | suppliers in Deliver leg | supply chain collaboration feature | Supplier Management app | supply chain partners review/approve in the same record | not observed |
| Deployment | on-prem / cloud / SaaS (Teamcenter X) | on-prem / PTC Cloud / SaaS (Windchill+, FedRAMP) | cloud or on-prem; Community Edition | multi-tenant SaaS; GovCloud variant | SaaS (implied) |
| Packaging philosophy | broad suite | packages + role/industry add-ons + non-expert apps | platform + composable apps + low-code | fixed cloud platform + separate QMS product | PLM + planning/pricing/PXM product lines |
| Tier | enterprise (start-ups via Teamcenter X) | mid-size to large enterprise | enterprise (largest manufacturers) + Community Edition | startup to Fortune 500, mid-market center of gravity | brands/retailers/manufacturers (consumer) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The manufacturer's system of record for the product's definition across its life. Four jointly-held structures:

1. **The product record as the unit of record** — a persistent identified record of the product to which the product's data attaches (items, structure, documents, changes, quality). All five sampled vendors name this center ("product record" — Arena; "system of record for product data" — Windchill; "single source of product information" — Teamcenter; "single source of truth… not just a database for product records" — Aras).
2. **The product's definition held as structured, revision-controlled data** — items/parts, the product structure (BOM), and associated documents/design files, maintained as the authoritative definition of what the product is, under revision control. (Universal in the discrete sample; industry variants hold the same leg with industry content — styles/BOMs, formulas.)
3. **Controlled evolution through formal change processes** — changes to the definition advance through request → review/approval → order/notice → release, producing new revisions with traceability and audit trails. (ECR/ECO/ECN machinery explicit at PTC and Arena; change management a named capability at Aras and inside Teamcenter's estate.)
4. **The whole-life, whole-organization span** — the record's governance extends beyond the engineering design phase: at minimum through release into production with handoff of the released definition to downstream systems (ERP/production); commonly through service and retirement; and the system serves functions beyond engineering (manufacturing, quality, procurement, supply chain, executives). This is the leg both PTC and Arena use to distinguish PLM from PDM.

Jointly-held load-bearing tests:

- 1 alone = a product registry / product database (or drifts toward PIM if content is commercial).
- 2 without 3 = an uncontrolled parts list / file share.
- 3 without 1+2 = change ticketing with nothing defined.
- 4 without 1+2+3 = project/portfolio or lifecycle-marketing tooling.
- 1+2 without 3 = static data dump, no controlled evolution.
- 1+3 without 2 = change process over an empty record.
- 2+3 without 4 = PDM / BOM-management territory (design-org scope, structure-centered world) — the sibling Types' seam.
- 1+4 without 2+3 = a portfolio view with no authoritative definition.

### L1 — Common Mature Structure

Present across the sampled estate leaders; expected in mature products but not required to recognize the Type:

- CAD/ECAD integration and visualization (multi-CAD management, file vaulting/check-in, 3D visualization/markup) — deep in Teamcenter/Windchill/Aras; integration-level in Arena; absent in fashion/food PLM.
- Manufacturing process planning / BOM transformation (eBOM → mBOM, process plans, work instructions).
- Parts classification & component engineering (duplicate detection, reuse, AVL/AML).
- Supplier / external collaboration (secure sharing and review with supply chain partners in the same record).
- Quality management (closed-loop quality, CAPA, NCR, audits) — as module or separate product.
- Requirements management (as module/app/add-on).
- Project / program management linked to the product record.
- Compliance content (environmental RoHS/REACH/conflict minerals; export controls ITAR/EAR; industry regulations).
- Cost management, simulation data management, analytics/reporting (estate leaders).
- Digital thread / digital twin framing and AI assistants (era-current layer over the estate).

### L2 — Variant / Optional Structure

- Deployment: on-premises / vendor cloud / multi-tenant SaaS / government cloud (Arena GovCloud; Windchill+ FedRAMP).
- Packaging philosophy: broad suite (Teamcenter) vs packages + role apps (Windchill) vs platform + composable apps + low-code (Aras) vs fixed cloud platform + separate QMS product (Arena) vs PLM + planning/pricing/PXM product lines (Centric).
- Industry packaging: discrete manufacturing (A&D, automotive, high-tech, medtech, industrial) vs consumer-goods/fashion/food (styles/seasons/colorways, formulas, compliance calculations) — same Type identity, different record content.
- QMS bundling posture: one platform (Arena PLM+QMS share the change machinery) vs separate products (Arena names them separately; Greenlight Guru pattern from the medical-device pass).
- Scope of "product": physical goods vs software-defined products (ALM integration, software BOMs).
- Customer tier: enterprise vs mid-market vs startup (Teamcenter X "even the smallest start-up"; Arena "small startup or Fortune 500").

### L3 — Vendor-specific (research notes only)

- Teamcenter X (Siemens-operated SaaS), Teamcenter AI / Copilot, Product Cost Management.
- Windchill Navigate (role/task apps for non-experts), PTC Jetstream (collaboration layer), Windchill+ FedRAMP authorization, expert packages base/advanced/premium, full-track CRB/CIB vs fast-track vs lightweight-CN change tiers, Onshape connection.
- Aras Innovator Edge (AI agents), Community Edition, low-code DevOps, Digital Twin Core app, federation services.
- Arena SCI (supply chain intelligence powered by Accuris), Arena Connect/iPaaS, Arena Analytics, app.bom.com login, AI item redlines.
- Centric Planning / Pricing & Inventory / Market Intelligence / Visual Boards / PXM.

## Vendor-specific Findings

See L3 above. None of these entered the canonical core.

## Boundary Findings

1. **vs Bill of Materials Management (§16 sibling — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED).** The BOM pass's center-of-gravity criterion is confirmed and sharpened from the PLM side: BOM management is the item/BOM/revision-structure-centered Type whose managed world is the structural definition + controlled evolution; PLM is the product-record estate whose managed world spans the definition data (of which BOM is one component), the change process over it, and the whole-life/whole-organization span. Evidence from this pass: the BOM core is extractable and independently sellable inside PLM-branded products — Arena names "Item & BOM Management" as one solution area inside its PLM platform; PTC publishes BOM management as one technology page inside Windchill's feature list; Aras ships BOM management inside its Product Engineering app. Conversely, the sampled PLM products all carry estate elements BOM-centered tools do not own as their center: CAD vaulting/visualization, quality, requirements, supplier collaboration, manufacturing process planning, ERP handoff. The packaging gradient the BOM pass recorded (Duro self-labels PLM; OpenBOM lists a PLM capability; Aligni pairs PLM+MRP) is consistent with this pass's finding that "PLM" is the market's umbrella label while the BOM core remains a separable layer. Removal test: remove the estate breadth + lifecycle span → BOM management; remove the structure-centered world → PLM.
2. **vs Medical Device Lifecycle Management (§22 sibling — keep-both CONFIRMED from this side).** The proposed seam (generic product-data estate vs device-regime record chain) holds: Windchill's own MedTech industry page sells generic PLM machinery ("end-to-end traceability, document control, and closed-loop processes") with no design-control/risk-file/submission semantics at the center; Aras serves Medical Devices as an industry page plus a QMS app and compliance webinars (QSR→QMSR); Arena serves device makers through a separately named Arena QMS product (Design Controls, Medical Device Regulatory compliance) beside Arena PLM. The device-regime record chain is either a separate product or industry packaging — never the PLM center. The medical-device pass's "packaging straddle to confirm" is hereby confirmed; its Windchill-at-generic-PLM-strength caveat is upgraded by this pass's direct fetch of the Windchill MedTech page.
3. **vs MBSE Platform (§16 sibling — keep-both CONFIRMED from this side).** Product data estate vs system model: Aras ships "Systems Architecture" as one app in its composable library ("systems models as an integral part of your digital thread") — the model is an app inside the estate, not the estate; the MBSE pass's integration evidence (System Modeling Workbench for Teamcenter) is consistent. Removal test: remove the estate → MBSE platform; remove the model-centric record world → PLM.
4. **vs Product Configuration Management (§16 sibling — keep-both CONFIRMED from this side).** Variant-space layer vs estate: PTC frames "product variability management" as one key feature among nine on the Windchill page; Aras ships "Variant Management" as one app ("product platform variability and reuse across all product representations"). The variant space is a capability inside the estate, not the estate. Consistent with that pass's own proposal.
5. **vs Mechanical CAD (§16 sibling — consistent with that pass's holding).** PLM manages product lifecycle data above the model (items, changes, releases across disciplines); MCAD authors and maintains the model itself. CAD integration depth in PLM varies from deep vaulting (Teamcenter/Windchill/Aras) to integration-level (Arena) to absent (Centric) — integration is L1, not identity.
6. **vs Engineering Document Management (§16 sibling — consistent with that pass's holding).** PLM's center is the product record; document management appears as a module (Arena Document Management essential; Aras Technical Documentation app). EDM's center is the document register for engineered assets/projects regardless of BOM presence.
7. **vs ERP / Manufacturing ERP.** Direction of truth-flow: PLM defines and releases the product definition; ERP consumes it for planning, procurement, and execution. PTC's own FAQ: "Windchill acts as the system of record for product data… while ERP systems handle planning, procurement, and execution… only validated, released product data is transferred to ERP." Arena: ERP integration "ensures that manufacturing receives the latest released design." Consistent with the BOM pass's direction-of-truth discriminator.
8. **vs Engineering Change Management (§16 leaf, UNPROCESSED — FORWARD FLAG).** Every sampled PLM embeds change management as a core process over the product record (ECR/ECO/ECN at PTC and Arena; change capability at Aras; change across disciplines inside Teamcenter's estate). The separate ECM leaf is defensible only for change-centered products whose managed objects span engineering objects broadly (documents, files, items across engineering) without owning the product-record estate. Alias risk flagged by the BOM pass is confirmed from this side: the change process is embedded machinery in PLM, not the center. The ECM pass should test whether its sampled products hold a change-process center independent of the product-record estate.
9. **vs PDM (not a directory leaf).** Both PTC and Arena publish the distinction: PDM = shared repository for engineering workgroups' design data (CAD files, versions, design collaboration); PLM = extends beyond the design phase to all data and processes of NPDI, for the whole team. PDM is the ancestor/adjacent concept; in the directory its territory is split between Mechanical CAD (companion PDM), Engineering Document Management (document register), and this Type. No directory change needed.
10. **vs Product Information Management / PIM (§05.04).** Different record world: PIM manages commercial/catalog content for selling channels; PLM manages the engineering/manufacturing definition. Vendor-drawn seam: Centric sells Centric PLM and Centric PXM (PIM/DAM) as separate product lines. Consistent with the BOM pass's "no confusion risk" finding.
11. **vs Digital Twin Platform (§16 sibling — consistent with that pass).** "Digital twin" is era-current vocabulary over the product record (Teamcenter "leverage the digital twin"; Aras Digital Twin Core app); the twin-platform Type centers the operational counterpart of a specific physical asset. Development-time record vs operational counterpart.
12. **vs Food PLM (§20 sibling, UNPROCESSED — FORWARD FLAG).** The food-formulation pass pre-hung "composition core vs lifecycle container" for the food-plm leaf. From this side: industry PLM variants (fashion/food/consumer goods) are realizations of this Type with industry-specific record content (Centric self-labels PLM across fashion/food; its food case study centers formula updates and compliance calculations). The food-plm pass should test whether its sampled products hold the four-leg core (product record + structured definition + controlled change + lifecycle span) with food content, or whether they are composition/specification-centered tools adjacent to this Type.

## Historical / Market-Sample Check (§24)

- **The Type's own history supports the L0 span leg.** The "PLM" label was coined in the early 2000s for what had been PDM expanding beyond engineering (reasoning from both vendors' own PDM-vs-PLM explanations; the label's history itself is held at reasoning strength, not fetched). Early-2000s PLM products (the Teamcenter/iMAN-Metaphase lineage, Windchill, ENOVIA, Agile) satisfy all four legs: product record + structured revisioned definition + formal change control + lifecycle span beyond engineering. The definition therefore does not depend on SaaS, AI, digital-thread vocabulary, or modern CAD integration.
- **PDM-era systems fail leg 4** (design-org scope) and are the ancestor craft, not the Type — consistent with both vendors' own explanations and with the engineering-document-management pass's PDM/PLM boundary note.
- **Paper-era lineage**: drawing registers, part lists, and change-order forms routed for approval satisfy legs 1–3 conceptually; the whole-life span existed as organizational practice (engineering → production handoff). Held as lineage at low strength; not fetched.
- **Industry-variant check**: Centric (fashion/food/consumer goods) self-labels PLM and spans concept-to-commercialization with industry record content — the definition holds without discrete-manufacturing machinery (no CAD, no parts-classification). The L0 does not over-fit to the discrete-manufacturing implementation.
- **Anti-overfit inventory** (all held NOT definitional): CAD vaulting depth, requirements management, quality management, manufacturing process planning, supplier collaboration, project management, compliance content, cost management, simulation data management, digital thread/digital twin vocabulary, AI, SaaS delivery, multi-tenant architecture, low-code extensibility, specific change-process tiers (full/fast track), specific state names.

## Uncertainties

- **Duro unreachable** (transport error ×2) — the startup-tier cloud PLM pole is under-sampled first-hand; its PLM self-label is carried from the BOM pass at cross-pass strength.
- **Autodesk Fusion Manage 403** — the CAD-vendor-adjacent mid-market pole is not sampled.
- **No Tier-1 help centers fetched** — all evidence is product/solution-page strength. Exact lifecycle state names, revision schemes, workflow step sequences, and numeric limits are deliberately not asserted in either file.
- **Centric evidence at root-page strength** — its change-control and structure machinery in fashion/food deployments is unverified; claims kept weak.
- **Teamcenter operational detail** — the product page confirms positioning and breadth but not internal mechanics; the product-configuration-management pass's note ("Siemens Teamcenter docs gated") remains true this pass.
- **Whether a PLM without any product structure exists** — not observed in the sample; the question is left open rather than resolved by definition (the structure's form varies: parts BOM / style BOM / recipe).

## Final Synthesis

PLM is the manufacturer's system of record for the product's definition across its life. Its defining core is four jointly-held structures: the product record as the unit of record; the product's definition held as structured, revision-controlled data (items/parts, product structure, documents/design files); controlled evolution of that definition through formal change processes; and the whole-life, whole-organization span — governance extending beyond engineering design through release into production (commonly service/retirement), serving functions beyond engineering, and handing the released definition to downstream systems. Everything else the market associates with PLM — CAD vaulting, requirements, quality, manufacturing process planning, supplier collaboration, compliance, cost, simulation data, digital thread, AI — is standard mature capability or industry/deployment variant, not definition. The Type's seams are held by center of gravity against BOM management (structure-centered world), PDM/Engineering Document Management (design-org data and document registers), MBSE (system model), Product Configuration Management (variant space), ERP (consumes the released definition), and the device-regime record chain of Medical Device Lifecycle Management. The leaf stands as an independent Type; no directory change required.
