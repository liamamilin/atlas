# Research Notes — Industrial Laboratory Management

## Research Goal

Establish what "Industrial Laboratory Management" is as an Application Type: the software operated by quality-control / testing laboratories inside manufacturing and industrial organizations. Determine whether it is a distinct Type, an industry instance of LIMS, or something else; draw the seam against LIMS (processed), Environmental Laboratory Management (processed), Laboratory Information System / LIS (processed), Calibration Management (processed), and the unprocessed siblings Manufacturing QMS, Product Test Management, Stability Study Management, and SPC.

The LIMS pass (processed 2026-09-08) pre-recorded an expectation for this leaf: "expected same seam shape as environmental (manufacturing QC-lab instance, 'QC LIMS' market vocabulary)". This pass tests and discharges that expectation.

## Initial Boundary

Hypothesis before research:

- The Type is the information system of record for QC/testing laboratories inside manufacturing organizations: testing raw materials, in-process/intermediate materials, and finished products against specifications; supporting lot/batch disposition and release; producing certificates of analysis; connecting lab results to production and enterprise systems.
- Market vocabulary: "QC LIMS", "Manufacturing LIMS", "Quality Manufacturing LIMS/Informatics", 检验检测管理平台 (CN).
- Nearest neighbors: generic LIMS (§22, processed — closest sibling); Environmental Laboratory Management (§21, processed — sibling domain instance); LIS (§22, processed — clinical, expected clean); Calibration Management (§16, processed — instrument-fitness machinery that tends to be embedded here as modules); Manufacturing QMS / Product Test Management / Stability Study Management / SPC (§16/§22, unprocessed).
- Unknown points: whether the industrial instance has load-bearing legs beyond the generic LIMS substrate; whether the disposition/release loop is definitional (the LIMS pass held report/CoA generation at common-mature because generic LIMS results are often consumed downstream); whether a distinct product population answers to the leaf name itself.

## Research Questions

1. What is the unit of record in an industrial QC lab, and what is a sample anchored to (material, batch/lot, product, production stage)?
2. How do specifications work — material/product specs, customer- or market-specific levels, limits, grading?
3. What is the deliverable: CoA, lot release decision, results to ERP/MES? Is the disposition loop definitional for this instance?
4. How does the lab workflow run: task/login → assignment → bench/instrument work → review → release?
5. What roles exist (analyst, supervisor, QA release)?
6. How do instruments, calibration/performance checks, and analyst competency integrate?
7. Enterprise multi-site lab networks vs single-plant lab?
8. What compliance posture (ISO 17025, GMP/cGxP, FDA 21 CFR Part 11, data integrity)?
9. Does a distinct product population exist for industrial labs, and how does the market name it?
10. Historical/regional check: would paper-era QC labs and non-Western markets fit the same core?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

1. **LabWare** — enterprise LIMS leader with a dedicated SaaS edition ("QAQC") aimed at QA/QC testing labs (SaaS/rapid-deployment pole). Root + QAQC product page reachable.
2. **Thermo Scientific SampleManager LIMS** — enterprise manufacturing-QC flagship; dedicated manufacturing solution page and industries pages (CN site reachable; thermofisher.com geo-redirects to the CN site from this environment).
3. **STARLIMS** — enterprise suite with a named "Quality Manufacturing Informatics" platform (LIMS + SDMS + LES + ELN + Advanced Analytics) and an SMB edition ("QM Essentials"). Root reachable; deep pages 403 ×2 → source abandoned per the retry rule; only platform-family-level evidence.
4. **Autoscribe Informatics (Matrix Gemini LIMS)** — mid-market configurable pole; dedicated "Manufacturing LIMS" industry page reachable.

Regional breadth check (observational support, not a fifth full sample): **Sunway World / 三维天地** — Chinese enterprise/industrial LIMS vendor (petrochemical, metals smelting, manufacturing solution pages reachable).

## Sources

- https://www.labware.com/ (root: product suite, industries, customer logos)
- https://www.labware.com/lims/saas/qaqc (SaaS QAQC product page)
- https://www.thermofisher.cn/cn/zh/home/digital-solutions/lab-informatics/lab-information-management-systems-lims.html (LIMS overview)
- https://www.thermofisher.cn/cn/zh/home/digital-solutions/lab-informatics/lab-information-management-systems-lims/industries.html (industries)
- https://www.thermofisher.cn/cn/zh/home/digital-solutions/lab-informatics/lims-manufacturing.html (manufacturing solution page)
- https://www.starlims.com/ (root: platform families, QM Essentials, MODA; deep pages 403 ×2)
- https://www.autoscribeinformatics.com/ (root: product taxonomy, FAQ)
- https://www.autoscribeinformatics.com/industries/manufacturing-lims (Manufacturing LIMS industry page)
- https://www.sunwayworld.com/ (root: 检验检测管理平台, industry solution summaries)

Research date: **2026-09-08**.

Source-access limitations: no help-center / operator-manual-grade documentation was reachable for any sampled product (same limitation pattern as the LIMS, LIS, and environmental passes). Evidence level is official product/solution/industry pages. No numeric limits, defaults, or exhaustive state lists are asserted anywhere below; all cross-product claims are calibrated to that strength.

## Product Observations

Evidence marks: **A** = directly observed on an official page of that product; **B** = observed across multiple sampled products.

### LabWare

- **A** — Root positions a unified laboratory informatics platform (LIMS + ELN + Mobile + AI); industries list includes Food & Beverage, Mining & Metals, Oil & Gas, Process & Chemical, Pharmaceutical — industrial sectors alongside life-sciences ones; customer logos include ExxonMobil, Chevron, Caterpillar, Goodyear, Sasol, Tyson Foods, Hershey.
- **A** — Dedicated SaaS edition "LabWare QAQC — SaaS LIMS for QAQC Testing", "ideal for testing in the lab and in the field", positioned to "replace paper-based systems" and go live fast.
- **A** — QAQC feature blocks observed: **Sample Management** (manual sample logging plus "powerful schedulers designed to automate the process"; "chain of custody continuously updates the status and location of the sample throughout the lifecycle"); **Results Entry** (grouping via Samples, Folders and Batches; batch-level results and calculations via Batch Manager with instrument integration); **Lot Management & Release** ("Track the status of all batches/lots tested … from submission through to reporting. With built-in laboratory KPIs, data review functionality and **lot release functions** as well as **automatic COA report generation and report approvals for each lot**"); **Environmental Monitoring** (programmed sampling schedules and point monitoring); **Stability Study Management** (study coordination, storage locations, stability pulls, review, reporting).
- **A** — More features: COAs in multiple formats selected at creation; Inventory Manager (standards, reagents, samples, calibration weights — quantity, location, expiry, vendor); Instruments (recording performance checks "ensuring they are calibrated and appropriate for use", instrument result import via standard file format); data visualization with control charting and stability trending; ad-hoc queries with export; barcodes (1D/2D).
- **A** — FAQ: pharmaceutical customers regularly audited; data-integrity functionality claimed; customers "of all types, sizes & industries … to integrate & streamline their QA/QC processes".

### Thermo Scientific SampleManager LIMS

- **A** — LIMS family positioned for R&D, process development, quality control, and production ("工艺开发、质量控制和生产").
- **A** — Dedicated **manufacturing LIMS** solution page: "制造业实验室信息管理系统(LIMS)贯穿整个生产阶段的质量、合规性和可追溯性" (quality, compliance, traceability across all production stages). Testing happens "在原料、生产的各个阶段到成品发布前" (on raw materials, at production stages, and before finished-goods release). "SampleManager LIMS 软件能够管理原料、加工材料和最终产品之间的**批次关系**" (manages the batch relationships between raw materials, processed materials, and final products). Configurable for ISO 17025 and other industry regulations. "**多级规格**概述了不同客户可接受的质量水平，便于立即进行检查并快速发布产品" (multi-level specifications define different customers' acceptable quality levels, enabling immediate checking and fast product release).
- **A** — Manufacturing feature list observed: sample management and tracking with automatic scheduling of sampling points viewable by calendar; instrument management (status, scheduling, maintenance; instrument data connected to production data; tight integration with Chromeleon CDS); inventory and storage management incl. reagents with reorder reminders; lab management (queue/status overview, capacity); **LES** guiding analysts step-by-step through methods per SOP with complete process history; configurable workflows mapping to real lab processes; **integration with ERP (named example: SAP S4/HANA) and MES**, plus ELN and CDS; **multi-level specifications** (instant checking of raw materials or finished goods against agreed levels for different customers/markets); **recall and crisis management** (recalls, holds, long-term record retention, complete results traceability); SQC (statistical quality control) relations and metadata capture; mobile LIMS incl. GPS-tagged sampling and barcode scanning; cloud or on-premises; security/compliance (ISO 17025, GMP); dashboards and reporting.
- **A** — Industries page: Manufacturing ("从库存管理和流程优化到 QA/QC 检测，确保整个生产流程的一致性和标准化"), Metals & Mining ("确保材料符合客户规格" — ensure materials conform to customer specifications; standardized raw-material testing and process analysis across multiple labs), Chemical & Petrochemical, Oil & Gas, Food & Beverage, plus life-science/clinical verticals.
- **A** — Manufacturing QC case studies: Chr. Hansen (starter-culture production QC standardization), Müller (yogurt QC).

### STARLIMS

- **A (root level only)** — Platform families: "**Quality Manufacturing Informatics**" ("Get to market faster by integrating our LIMS with our SDMS, LES, ELN, and Advanced Analytics solutions into one unified lab informatics platform"), Clinical Informatics, Public Health Informatics. Under the quality-manufacturing family: Quality Manufacturing LIMS, Labstep R&D ELN, SDMS, LES, Advanced Analytics, **MODA Platform**, and "**QM Essentials for SMB**" (LIMS edition for smaller manufacturers). Vendor founded 1986; 2,000+ laboratories. Resource items: MODA-EM ("environmental monitoring informatics for QC microbiology"), MODA-ES (electronic batch record platform), "Breaking Lab Bottlenecks: How a LIMS Helps SMB Manufacturers Speed Time to Market".
- **Limitation** — deep product pages 403 twice; no QC workflow detail asserted for this product beyond the platform-family structure above.

### Autoscribe Informatics — Matrix Gemini LIMS (Manufacturing)

- **A** — Root FAQ gives the vendor's own lab-software taxonomy (LIMS vs ELN vs LES vs LIS vs SDMS vs laboratory instrument software); describes LIMS as managing "sample information through an analytical laboratory" with audit trails/e-signatures for 21 CFR Part 11, GxP, ISO 17025; notes "Products can be tested against specific **product limits** defined in the LIMS"; notes in-house and contract labs both served; LIS described as patient-centric/clinical vs LIMS "generally batch and sample-centric".
- **A** — Dedicated **Manufacturing LIMS** page: "Matrix Gemini Manufacturing LIMS is designed specifically for manufacturing industries. Manufacturing LIMS drives quality throughout the manufacturing flow by **managing and tracking the samples of raw materials, intermediate and final product**, ensuring they can be quickly **related to the relevant product and batch**."
- **A** — Key features observed: "**Batch and recipe management to link final products to raw materials and suppliers** — provides complete batch tracking, batch traceability and genealogy"; "**Manage tests performed at each stage of every batch** — allows validation of each production stage"; "**Defined specifications and workflows**"; "**Automated data approval for in specification results** — management by exception reduces turnaround time"; "**Test to manufacturing specifications** — track manufacturing quality"; "**Customer specific product grading** — maximize the value of manufactured material"; "Built-in instrument integration, calibration and maintenance and **analyst certification**"; "Integration with **ERP** and other corporate systems"; "Built in security, user by user specific access to workflow options and full audit trail" (FDA 21 CFR Part 11, ISO 17025, cGxP); staff competency; CAPA for quality lapses; optional environmental-monitoring module for production-environment hygiene testing; stability module for shelf-life statistics.
- **A** — Manufacturing case studies: Pixelle Specialty Solutions (paper products, manufacturing QA, configured in three months), FAR Chemical (specialty chemicals QC lab), Amway (R&D lab testing botanical ingredients).

### Sunway World / 三维天地 (regional observation)

- **A** — Chinese enterprise "检验检测管理平台" (inspection & testing management platform) vendor (listed company, founded 1995) with industry solutions for 石油化工 (petrochemical), 金属冶炼 (metals smelting), 生产制造 (manufacturing), among many others.
- **A** — Petrochemical solution summary: implement the inspection business flow for 生产原料、辅料、中控样、半成品、产成品 (production raw materials, auxiliary materials, in-process control samples, semi-finished products, finished products); flow described as 检验任务下达 → 采样 → 接收 → 数据录入 → 仪器自动采集 → 数据审核 → 报告发布 (task assignment → sampling → receipt → data entry → automatic instrument capture → data review → report publishing) with full-process traceability, under ISO/IEC 17025 and ISO 9001.
- **A** — Metals smelting: 原料/辅料/过程样/金属平衡样/产成品 flows including 品质交换 (quality settlement/exchange with trading counterparties); manufacturing framing: labs support production control with timely, accurate process and product-quality information so that products leaving the factory conform to standards.
- **A** — Also ships a cloud lab platform (云端·实验室信息管理平台) and quality-statistics tooling; an automotive/electronics page positions the lab platform as filling the quality gap between PLM/MES/ERP investments.

## Cross-product Comparison

| Structure | LabWare | Thermo SampleManager | STARLIMS | Autoscribe Matrix Gemini | Sunway World | Evidence |
|---|---|---|---|---|---|---|
| Sample anchored to production materials (raw/intermediate/finished) | QAQC sample mgmt + lot mgmt; industrial industry pages | explicit batch relationships raw→processed→final | QC-manufacturing platform family (family-level only) | explicit: raw materials, intermediate, final product related to product & batch | explicit: raw/auxiliary/in-process/semi-finished/finished | B (4/5 explicit at page level) |
| Batch/lot context with genealogy | Lot Management & Release; batch manager | batch relationships + recall/traceability | (family-level only) | batch & recipe management, genealogy linking final products to raw materials and suppliers | batch-level inspection flows incl. 金属平衡样 | B |
| Specification machinery (limits; customer/market levels) | product limits (implied by lot release + CoA) | multi-level specifications per customer/market | (unverified) | defined specifications; test to manufacturing specifications; customer-specific product grading | conformity to national standards/customer requirements | B |
| Managed testing workflow (login→assignment→bench→review) | sample logging→results entry→review→release; custody status/location | mapped-to-lab-process workflows; LES step-by-step; queue/status overview | (unverified) | sample testing automation; in-spec auto-approval management-by-exception | task→sampling→receipt→entry→auto-capture→review→report | B |
| Disposition/release of lots + CoA | lot release functions; automatic COA per lot; report approvals | fast product release; multi-level spec check | (unverified) | automated data approval for in-spec results; product grading | 报告发布; 品质交换 (metals) | B |
| Instrument integration + performance/calibration records | instrument performance checks; file import | instrument management; production-data linkage; Chromeleon CDS | SDMS pillar | instrument integration, calibration and maintenance | 仪器自动采集 | B |
| QC evaluation (controls/spec checks) | control charting; data review before release | spec checking; SQC relations | (unverified) | in-spec/out-of-spec evaluation driving approval | 数据审核 | B |
| ERP / enterprise integration | integration-first positioning | ERP (SAP S4/HANA example) + MES + ELN + CDS | unified platform incl. SDMS/LES/ELN | ERP and corporate systems | complements PLM/MES/ERP | B |
| Data-integrity posture (audit trail, e-signature, ISO 17025/GMP) | data integrity; audited pharma customers | ISO 17025/GMP; e-signatures; audit trail | ISO 9001/27001 vendor certs | 21 CFR Part 11, ISO 17025, cGxP | ISO/IEC 17025, ISO 9001 | B |
| Inventory/reagents, competency, stability, CAPA, environmental monitoring as modules | inventory; stability; environmental monitoring | inventory/reagents; (stability in LIMS family) | MODA-EM (QC microbiology EM) | all four as built-in modules | quality-statistics tooling | B |
| SMB / rapid-deployment edition | QAQC SaaS (fast deployment) | preconfigured editions by industry/workflow | QM Essentials for SMB | Matrix Gemini LIMS Express | cloud lab platform | B |
| Multi-site enterprise lab networks | global enterprise deployments | multi-lab standardization (metals & mining) | enterprise platform | global support; multi-national case study | 央企/group customers | B |

Reading: every sampled product realizes the same spine — production-anchored samples, specification-driven testing, and a disposition/deliverable step — on the generic LIMS substrate (sample of record, managed workflow, validated results, traceability). Differences are tier (SaaS/SMB vs enterprise), suite composition, and industry vocabulary.

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant

The industrial instance keeps the generic LIMS substrate (sample of record + managed analysis workflow + validated result of record, bound by a traceability posture) and adds the industrial binding. The smallest structure without which a product stops being recognizable as an industrial QC-lab management system:

```text
Production-anchored sample of record
  (sample of raw material / intermediate / finished product,
   identified and related to its product, batch/lot, production stage)
└── Specification-driven testing workflow
    (tests per material/product stage; results evaluated against
     defined specification limits under the lab's QC)
└── Disposition deliverable of record
    (validated results roll up to lot/product disposition — release,
     hold/reject, grading — and are issued onward as certificates /
     quality records into the production and commercial context)
```

Three jointly-held structures:

1. **Production-anchored sample of record** — samples exist as identified records bound to the production flow (material, batch/lot, stage, supplier where relevant). Remove the production anchor → generic LIMS territory (samples detached from manufacturing) or a batch inventory.
2. **Specification-driven testing workflow** — the material/product carries defined tests and specification limits; lab work moves samples through the testing process and evaluates results against those limits under QC. Remove the specifications → a generic task-tracker/workflow engine; remove the managed workflow → a spec calculator.
3. **Disposition deliverable of record** — validated results accumulate to the lot/product level and are acted on: release/hold/reject decisions, certificates of analysis or equivalent quality records, results passed onward to ERP/MES/clients; retained as the lab's quality evidence. Remove the disposition → testing tracker whose results never gate anything (the generic LIMS shape, where results are simply consumed downstream); remove everything else → paperwork generator.

Jointly-held is load-bearing: 1 alone = batch/material inventory; 2 without 1 = workflow engine / bare spec evaluation; 3 without 1+2 = disposition paperwork; 1+2 without 3 = tracker with no production consequence; 2+3 without 1 = spec calculator with anonymous data; 1+3 without 2 = release rubber stamp over unmanaged lab work.

Anti-overfitting notes: CoA is the *common* deliverable form, not the only one (product grading / quality-exchange records / ERP status writes are observed realizations of leg 3); exact workflow stage names and state labels vary by product; GMP/ISO-17025 regime names are the dominant but not exclusive compliance frame.

### L1 — Common Mature Structure

Present across essentially all mature products; makes the lab practical but does not define the Type:

- configured test/analysis catalog and method management (SOP-linked)
- instrument integration (result capture from instruments) plus instrument records: performance checks, calibration, maintenance
- QC samples (controls, standards, blanks, duplicates) evaluated alongside production results
- review chains with e-signatures; management-by-exception auto-approval for in-spec results
- CoA/report generation machinery with templates and approvals
- batch/lot genealogy views linking final products to raw materials and suppliers
- reagent/standard/consumable inventory with expiry and reorder
- analyst competency/certification linkage
- dashboards, TAT and workload views, KPIs; ad-hoc queries and export
- barcode/label identification; audit trails; role-based access
- results trending and control charting (SQC-class)

### L2 — Variant / Optional Structure

Depends on industry, scale, geography, deployment, business model:

- industry flavor: pharma GMP QC; food & beverage; petrochemical; metals & mining (with quality settlement/exchange); discrete manufacturing; cannabis/agrochemical etc.
- enterprise multi-site lab networks vs single-plant lab; corporate standardization programs
- suite composition: LIMS + LES + SDMS + ELN + analytics bundled vs standalone core
- LES depth (step-by-step SOP execution)
- stability study management, CAPA, environmental monitoring of production areas — usually modules or sibling products
- deployment: SaaS / cloud-hosted / self-hosted / on-premises; SMB preconfigured editions vs configurable enterprise platforms
- external-service posture: in-house labs offering testing to outside customers; contract-lab interaction
- regional regimes and vocabularies (ISO 17025/ISO 9001 in CN market summaries; GMP/21 CFR Part 11 in regulated-industry material)

### L3 — Vendor-specific Structure (Research Notes only)

- LabWare QAQC: 30-day deployment posture, 99.5% availability guarantee, twice-yearly validated upgrades, spreadsheet-based data onboarding.
- Thermo SampleManager: Chromeleon CDS tight integration branding; Integration Manager product; SAP S4/HANA example integration; Connect platform adjacency.
- STARLIMS: MODA platform (paperless QC microbiology EM; MODA-ES electronic batch records); Labstep ELN acquisition; QM Essentials SMB packaging.
- Autoscribe: concurrent-user licensing model; low-code configuration tools preserving a validated core; Matrix Gemini LIMS Express edition.
- Sunway World: 品质交换 (quality settlement) machinery for metals; S-tab statistics software; cloud lab platform; listed-vendor group/央企 customer base.

## Vendor-specific Findings

See L3 above; none of these belong in the final document.

## Rejected Findings

- **Instrument-local software** (titration/instrument suites of the LabX class): instrument-level data acquisition/processing, not the lab-wide operation — consistent with the CDS pass's instrument-vs-lab seam and with Autoscribe's own taxonomy page ("Laboratory Instrument Software" distinct from LIMS). Not sampled this pass; classification held at taxonomy level, not asserted as market research.
- **Facilities/booking reading of "laboratory management"**: no sampled industrial product centers on lab space/equipment booking; that pattern belongs to the Scientific Instrument Management / Research Core Facility Management leaves. In this Type, instrument and inventory management appear as modules serving the testing operation.
- **EHS/safety reading**: no sampled evidence links the leaf name to environmental-health-safety platforms; those are a separate family (§21). Environmental monitoring *of production areas* appears only as a module inside QC-lab products.

## Boundary Findings

1. **vs Laboratory Information Management System / LIMS (§22, processed)** — generic Type vs industrial-domain instance, ratified **keep-both** consistent with the environmental precedent: the generic pass holds report/CoA generation at common-mature because generic LIMS results are often consumed downstream, while this instance makes the **disposition/deliverable leg definitional** (release/hold/grading + certificates/records into ERP/MES/commerce is the lab's product). The three industrial legs are a strict specialization of the generic substrate that pass documented. If maintainers ever prefer one LIMS Type with industry variants, this leaf becomes the industrial variant (no directory change proposed from this side).
2. **vs Environmental Laboratory Management (§21, processed)** — sibling domain instances on the same substrate. Seam: sample anchor (production materials/batches vs environmental matrices/collection points), external driver (customer specifications and production schedule vs regulation/permit- and client-SLA-driven schedules), deliverable (CoA/release into commerce vs regulator-facing reports/EDD). Note: environmental monitoring of production areas is a module inside industrial QC products (observed in LabWare QAQC and Autoscribe) — packaging, not boundary failure.
3. **vs Laboratory Information System / LIS (§22, processed)** — clean seam held from this side: organizing subject is the production flow (material/batch/product), not the subject-of-care; result destination is the production/commercial context, not the care context. Autoscribe's own taxonomy page documents the split ("LIS are patient-centric… LIMS are generally batch and sample-centric").
4. **vs Calibration Management (§16, processed)** — measurement-fitness machinery vs laboratory testing operation. Calibration/performance records appear inside this Type as standard modules (observed in all sampled products where instrument management was described); the standalone Type owns the instrument register, due-state computation, as-found/as-left calibration events, and the reference-standard recursion. Removing calibration from this Type leaves the testing operation intact; removing the testing operation from Calibration Management's leaves its Type intact.
5. **vs Manufacturing QMS (§16, unprocessed)** — expected seam: quality *system* of record (document control, deviations, CAPA, audits, supplier quality) vs the laboratory *testing operation* of record. CAPA and quality modules appear inside this Type (observed in Autoscribe, LabWare-class suites) — module packaging, same pattern as calibration. Forward flag for that pass.
6. **vs Product Test Management (§16, unprocessed)** — expected seam: engineering/DV/PV product testing (test plans against requirements, design verification) vs QC analytical testing of production materials/batches against specifications. Forward flag for that pass.
7. **vs Stability Study Management (§22, unprocessed)** — observed in-market as a module inside this Type (LabWare QAQC stability study management; Autoscribe stability module; Thermo LIMS family positioning) — same packaging pattern the LIMS pass documented. Forward flag: that pass should treat the study-protocol-driven machinery as its core, with LIMS-side packaging noted.
8. **vs Chromatography Data System / CDS (§22, processed)** — instrument-local acquisition/processing vs lab-wide workflow; the sample-list-out/results-in interface and named CDS integrations (Chromeleon) are seam artifacts, consistent with the CDS pass.
9. **vs SPC (§16, unprocessed)** — control charting/trending of results appears as a capability here (observed in LabWare QAQC and Thermo's SQC note); the SPC leaf is expected to own production-process statistical control as its center. Forward flag for that pass.
10. **vs Research LIMS / ELN (§23/§22, processed)** — industrial R&D labs inside the same company drift toward ELN/Research LIMS territory; this leaf's center of gravity is the QC/testing operation on production materials. Suite vendors bundle R&D ELNs beside their QC LIMS (STARLIMS Labstep, LabWare ELN) — bundling evidence, not type merger.

## Historical / Market-Sample Check

- Paper-era QC lab: specification sheets per material/product + sample logbook keyed to batch/lot numbers + bench worksheets + results-vs-spec evaluation + supervisor sign-off + typed CoA + release stamp + retained files — satisfies all three L0 legs at analog level. The substrate traceability posture (the LIMS pass's binding condition) holds on paper.
- Older/regional products: STARLIMS (founded 1986) and Autoscribe (40+ years) grew up in exactly this market; the Chinese pole names the same loop in its own vocabulary (检验任务下达→采样→接收→录入→采集→审核→报告发布) and adds industry-specific settlement practices — same core, different labels.
- Single-plant small labs (SaaS/SMB editions) and multi-plant enterprise networks both fit; the definition names neither SaaS, nor cloud, nor specific compliance regimes, nor specific ERP systems.
- Conclusion: the L0 passes the historical/regional check; no era- or region-specific machinery is definitional.

## Uncertainties

- STARLIMS QC workflow detail is unverified (deep pages 403 ×2); its inclusion rests on root-level platform-family evidence only. All cross-product claims rest on the other three samples plus the regional pole.
- No help-center/manual-grade docs reachable for any sampled product — no numeric limits, defaults, or exhaustive state lists asserted; exact workflow-state names held at "vary by product".
- Whether a standalone product population self-describes as "industrial laboratory management" distinct from "QC LIMS" was not found; the market names this population QC/Manufacturing LIMS (or 检验检测管理平台). The leaf name describes the function; the market name describes the product category (same naming pattern as the environmental pass recorded).
- Dedicated SMB-only QC-lab SaaS products *outside* the enterprise vendors' SaaS editions were not sampled.
- The LIMS-family cluster question (one Type + industry variants vs several leaves) remains a maintainer-level taxonomy decision, consistent with the environmental and LIMS passes' notes.

## Final Synthesis

Industrial Laboratory Management is the industrial-domain instance of the laboratory-informatics family: the manufacturing organization's QC/testing laboratory system of record. Its defining core is three jointly-held structures on the generic LIMS substrate: the **production-anchored sample of record** (samples of raw materials, intermediates, and finished products, identified and related to product, batch/lot, and production stage, with batch genealogy), the **specification-driven testing workflow** (defined tests and specification limits per material/product — commonly at customer/market levels — with results evaluated under QC through a managed lab workflow), and the **disposition deliverable of record** (validated results rolled up to lot/product disposition — release, hold/reject, grading — issued as certificates/quality records and passed into ERP/MES/commercial context, retained as quality evidence). Keep-both with LIMS ratified (generic Type + domain instance, environmental precedent); boundaries drawn against LIS, Calibration Management, Environmental Laboratory Management, CDS, ELN/Research LIMS, with forward flags for Manufacturing QMS, Product Test Management, Stability Study Management, and SPC.
