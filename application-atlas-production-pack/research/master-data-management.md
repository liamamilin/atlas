# Research Notes — Master Data Management

Research date: 2026-09-08
Slug: master-data-management (§13 Data, Analytics & AI Systems)

## Research Goal

Understand what a Master Data Management (MDM) product actually is as an Application Type: what objects exist inside it (master/golden records, source records/crosswalks, match rules, survivorship, stewardship tasks, hierarchies), how the ingest → match → merge → govern → serve loop works, which structures are defining vs merely common, and where its boundaries lie against the neighboring Types flagged by earlier passes (Data Quality Platform, Data Governance Platform, Data Catalog, PIM) and against operational systems of record (CRM/ERP/HRIS) and the Customer Data Platform.

## Initial Boundary

- Hypothesis: MDM is the system of record for the organization's shared core entity identities — it consolidates records from multiple source systems into one authoritative record per real-world entity and serves that record back to consuming systems.
- Nearest neighbors: Data Quality Platform (evaluator, not system of record — seam already held by that pass), Data Governance Platform (program/policy layer; CDE-management seam flagged for joint review), Data Catalog (metadata about assets vs master records), PIM (product-domain record store with channel syndication), CDP (marketing behavior profiles), CRM/ERP (single-domain operational systems of record).
- Easy confusions: "MDM" is also used in IT/endpoint contexts ("mobile device management") — different Type entirely (§14 endpoint family); ignore that reading.
- Open unknowns at start: are the classic implementation styles (registry/consolidation/coexistence/centralized) definitional or variant? Is multi-domain breadth definitional? Is stewardship workflow definitional or a common implementation?

## Research Questions

1. What is the world made of: what is a master/golden record, what is a source record/crosswalk, how do they relate?
2. How does a record become authoritative: matching (who decides "same entity"?), merging, survivorship (who wins each attribute)?
3. What do stewards actually do day to day? What states does a master record pass through?
4. How do consuming systems get the master data (publish/sync/API/event streams)?
5. Which implementation postures exist (where authoring lives; consolidation-only vs coexistence vs centralized)?
6. Is single-domain MDM (customer only, product only) still MDM?
7. What quality/governance machinery is embedded vs left to sibling platforms?
8. Boundaries: vs DQ (evaluator), vs governance platform (program), vs catalog (inventory), vs PIM (product domain), vs CRM/ERP (single-system master), vs CDP (marketing profiles).

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different customer tiers:

1. **Reltio** — cloud-native SaaS, real-time "connected data" philosophy. Documentation Portal (docs.reltio.com) reachable; several deep pages.
2. **Ataccama (ONE MDM)** — unified data-management suite where MDM is a standalone product line beside DQ&C/RDM; deep Tier-1 docs (docs.ataccama.com/mdm).
3. **Profisee** — Microsoft-native SaaS/PaaS/hybrid MDM, quality-led positioning; product-site capability pages + FAQs (docs subdomain unreachable — transport error ×2).
4. **Stibo Systems STEP** — enterprise heritage vendor, multi-domain strength, product-domain packaging; product-site platform page.
5. **Semarchy** — model-driven, declarative-design pole (xDM heritage, now "Semarchy Data Platform"); docs hub + concepts pages.
6. **Informatica** — category-defining enterprise vendor; docs.informatica.com returned 403 (this pass and prior passes). Used only as a category anchor with NO product-specific claims.

## Sources

- Reltio Documentation Portal: /en/reltio/what-does-reltio-do/what-reltio-does-at-a-glance (MDM vs data unification definitions, unification steps); …/data-unification-and-mdm-in-detail/reltio-configuration-data-types/the-source-type (crosswalk, survivorship → Operational Value); …/the-graph-type (hierarchies, multi-parent, entity singularity across graphs); roles listing (fetched 2026-09-08)
- Ataccama docs: /mdm/latest/overview.html; /mdm/latest/product-overview/introduction-to-mdm.html (business role, business cases, solution scope, implementation styles); full MDM user-guide + configuration navigation tree (fetched 2026-09-08)
- Profisee: profisee.com/platform/; /platform/golden-record-management/ (golden-record FAQ, match→merge→survive, survivorship definition, steward review); /platform/stewardship/ (steward definition, FastApps, record states imagery) (fetched 2026-09-08)
- Stibo Systems: stibosystems.com/platform (capability set, resolution/survivorship/approval language, semantic graph, domain packaging) (fetched 2026-09-08)
- Semarchy: docs.semarchy.com (+ /saas, /saas/get-started/concepts); stale xDM doc redirect noted (fetched 2026-09-08)
- Sibling-pass research: research/data-quality-platform.md (MDM seam), research/data-governance-platform.md (CDE seam), research/data-catalog.md (MDM seam), STATUS.md entries for PIM

## Product Observations

### Reltio (evidence layer A unless noted)

Key observations:

- Definition from own docs: "MDM focuses on governing an organization's core or master data, which often includes critical entities like customers, products, employees, and other core business elements, to create a single, consistent, and authoritative source of truth across all systems and processes in an organization." MDM described as "a specific type of data unification" — more specialized, centered on key entities.
- Data unification steps named in docs: Consolidate (ingest from internal/external sources, multiple formats/qualities) → Cleanse ("data is standardized and redundant entries are merged into newly authoritative entities") → Store (repository) → Integrate ("trusted interoperable data needs to be shared across the enterprise").
- Source-contribution model (config data types): "Data, relationships, and interactions each come from one or more sources." "multiple source systems can contribute to the attributes of the object. At the time a request for the object is made, survivorship rules at the attribute level within the object will produce an Operational Value (OV) for each attribute." "Each source system is represented in the object by a crosswalk which contains the name of the source and a unique key from that source." → source records never discarded; the authoritative value is computed at read time from contributions.
- Hierarchy/graph: a Graph type "defines a hierarchical structure you can use to model a tree of entities"; "entities are not duplicated across the hierarchies. Instead each entity is singular but can be a member of multiple graphs"; multi-parent branches supported. Healthcare examples use HCO (healthcare organization) / HCP (healthcare professional) party types.
- Documented user roles: Business User, Data Product Owner, Data Steward, Developer, Reltio Configurator, Solution Architect, System Administrator — steward as a first-class role.
- Marketing-layer vocabulary ("360 view", "Context Intelligence Platform") recorded but not load-bearing.

### Ataccama ONE MDM (evidence layer A)

Key observations:

- "Ataccama Master Data Management (MDM) is a standalone application consisting of a powerful MDM engine and a web interface… fully metadata-driven application." Metadata model drives functionality.
- Business role (near-verbatim): "Serves as a system of reference (ideally in the role of the central MDM hub), delivers the single version of the truth for all mastered data." "Prevents duplicates and low quality data from entering it into any connected source system or the MDM hub itself." "Centralizes cleansing, standardizing, matching, and merging rules across the data processing line (from source to master)." "Processes data in both full and incremental modes." "Provides data on demand in both full and incremental modes via online and/or batch interfaces."
- Business cases (verbatim list): Customer Data Integration (single domain), Address Data Integration (single domain), Vehicle Data Integration (single domain), Blocklist Data Integration (multiple domain), Group-wide Customer and Product Data Consolidation (multi-domain), Regulatory Compliance Data Integration and Reporting (multi-domain), Analytical and Operational CRM Support (multi-domain). → single-domain MDM explicitly a product-supported form.
- Solution scope: single domain / multi-domain (domains "processed together with their mutual relationships") / multiple domain (unrelated domains).
- Implementation styles (vendor-documented): **Consolidation** (consolidates systems, identifies duplicates, provides consolidated master records downstream); **Coexistence** (consolidation + "upstream propagation of consolidated master data back to the source systems, with data authoring remaining in the originating (source) systems"); **Mixed** ("master data exists both in the MDM hub (R/W) and source systems (R/W)"); **Centralized** ("Master data exists in MDM data hub only (R/W)").
- Web app user guide (operational loop): exploring master data (search, view entry details, browse master record hierarchies, compare records, export); "Reviewing and performing corrections on automatically constructed master records"; authoring (create/delete records, edit values); "manual merge and split operations"; matching proposals; publishing workflow; resolving tasks; creating tasks for other data stewards (manual or automatic task configuration); working with drafts; activating/deactivating records (record lifecycle states).
- Project configuration: logical models with an **instance layer model** and a **master data layer model**, "Configuring Record and Override Lifecycles"; reference data; external entities. Matching configured separately at instance layer and master layer; matching plans/steps; AI matching as an advanced option.
- Input/output interfaces: connecting a system; initial load / full load / complex delta load; exports (full instance / full master); stream consumers; native services (REST read-write/override services); streaming event handlers and publishers.
- Sits inside a platform family: ONE DQ&C (catalog+quality+observability), ONE MDM, ONE RDM (reference data management), ONE Desktop, runtime server. "MDM and RDM connection" exists as a source type in DQ&C. → MDM/RDM as sibling products; DQ native inside MDM ("MDM provides Master Data Management functions in combination with a strong emphasis on Data Quality as a core part").

### Profisee (evidence layer A for product pages; docs subdomain unreachable)

Key observations:

- Positioning: "Unify customer, product, supplier or any data. Deduplicate, apply rules and publish clean records in real time." Multi-domain by default ("any data").
- Golden record (own FAQ): "the process of creating and maintaining a single, accurate, and consistent version of essential data about an entity—often referred to as the 'single source of truth.'" "a golden record combines verified, deduplicated data from multiple systems."
- Match → Merge → Survive pipeline (own capability naming): Match ("Identify and group sets of duplicate records using fuzzy matching logic"), Merge ("Logically combine duplicate records, and update source systems with that same logical merge"), Survive ("Automatically create and populate golden records with the best information available across source systems").
- Survivorship definition (own FAQ): "determining which data values should be retained or 'survive' when conflicting or duplicate data records are merged or resolved… which values should be considered authoritative and retained."
- Steward-in-the-loop (own FAQ): ML-powered matching proposes matches; "Matching records are then displayed side-by-side in a match group for data stewards to review, where they are also given the option to merge records… choose 'winners' from the information in candidate records to survive the merge… Data stewards have a chance to review merge criteria before making any changes… Full audit trails."
- Stewardship surface: web-based stewardship UI ("Explore" search/browse; "Manage" author and edit; "Correct" fix issues surfaced by DQ rules and ML anomalies), task management, role/task-based "FastApp" experiences, embedded analytics, record states shown (Rejected / Proposed / Approved imagery).
- Capability menu: Entity Resolution, Automated Workflows, Data Stewardship, Integration ("Real-time integration with REST APIs and webhooks"), Quality & Governance, Relationship Management, Matching & Survivorship, Address Matching & Verification, Reference Data Management (as an initiative), Data Governance.
- Deployment: "SaaS, PaaS, IaaS, hybrid or on-prem." Microsoft-stack integrations (Fabric, Purview, Power Platform, Azure OpenAI), MCP server for AI agents (vendor-specific, era-current).

### Stibo Systems STEP (evidence layer A for product pages)

Key observations:

- "STEP pulls data in from across your ecosystem and resolves and governs it into trusted master records. From there, it serves that intelligence downstream." → the full arc in one sentence: sources → resolve/govern → serve.
- "entity resolution and survivorship" named as the verified-identity machinery; "No record reaches the master store without passing defined validation, approval and enrichment steps, whether the trigger is a human steward or an automated agent" → approval gate on the master store.
- "A single, resolved master record across multiple domains" and "STEP manages master data across the full enterprise rather than a single domain."
- Capability taxonomy: Data Sourcing (bring data together), Data Modeling (flexible data model), Data Integration ("Consolidate, synchronize and manage master data and reference data from various sources in a centralized and trusted repository"), Data Quality, Data Governance, Data Compliance, Data Sharing ("syndicate trustworthy data to customers, vendors, stakeholders, suppliers and value chain partners"), Data Delivery ("Distribute high volumes of master data across various systems, applications and teams for real-time data consumption").
- Data model: "Every entity exists as nodes in graph structure with typed, directional relationships, configurable hierarchies and attribute inheritance"; ontologies/classification schemes across domains.
- 100+ prebuilt connectors (ERP incl. SAP, CRM incl. Salesforce, D&B/Experian/Loqate enrichment).
- Domain packaging: Product Experience / Customer Experience (B2C) / Business Partner (B2B) / Supplier / Location / Sustainability "Data Clouds" — same platform, domain-scoped packages. → domain packaging is a variant, not separate Types.

### Semarchy (evidence layer A but light — docs hub + concepts)

Key observations:

- Platform names master data management as a core capability: "Master data management: create and maintain accurate, consistent, and governed master data." Sits beside data integration and data governance in one platform.
- Declarative, metadata-driven design (file-based design, VS Code-based IDE, no-code forms; SemQL declarative language for validation/enrichment/transformation business rules) → model-driven philosophy pole.
- Docs mention "certification processes" and "data products" (Semarchy's positioning has shifted from xDM to a broader "Data Platform"; legacy xDM docs redirect is stale — deep MDM object docs not reachable this pass). Evidence kept at platform level; no precise operational claims made.

### Informatica — Source-access Limitation

- docs.informatica.com returned 403 on this pass (and 403 ×2 in the data-quality and data-governance passes). No direct evidence. The vendor is used in this research ONLY as the category's enterprise anchor; NO Informatica-specific operational claims are made anywhere. Enterprise-pole behavior is triangulated via the sampled products and sibling-pass observations.

## Cross-product Comparison

| Structure | Reltio | Ataccama | Profisee | Stibo | Semarchy | Strength |
|---|---|---|---|---|---|---|
| Authoritative master/golden record per real entity | ✓ (entity objects, OV) | ✓ ("single version of the truth", master data layer) | ✓ (golden record) | ✓ ("trusted master records") | ✓ ("governed master data") | Universal — 5/5 |
| Records contributed by multiple source systems | ✓ (crosswalks, sources) | ✓ (instance layer, loads, connecting systems) | ✓ ("data from any source", match groups of duplicates) | ✓ ("pulls data in from across your ecosystem", connectors) | ✓ (integration as sibling capability) | Universal — 5/5 |
| Matching (deterministic/fuzzy/ML) + merge | ✓ (merge into trustworthy entities) | ✓ (matching plans, instance+master layers, AI matching) | ✓ (match groups, ML matching) | ✓ (entity resolution) | ✓ (validation/rules; depth unverified) | Common core — 5/5 |
| Survivorship of attribute values | ✓ (attribute-level survivorship → OV) | ✓ (override/master layer semantics) | ✓ (survivorship named) | ✓ (survivorship named) | n/v (unverified depth) | Common core — 4/5 direct |
| Source linkage retained on the record | ✓ (crosswalk = source + key) | ✓ (source records under master) | ✓ (candidate records shown side-by-side) | n/v | n/v | Common — 3/5 direct |
| Stewardship review loop (proposals, merge approval, tasks) | ✓ (steward role) | ✓ (matching proposals, tasks, publish workflow, drafts) | ✓ (side-by-side review, choose winners, audit) | ✓ (approval steps, human or agent trigger) | ✓ (steward role in docs) | Common core — 5/5 |
| Serve back to consuming systems | ✓ (Integrate step) | ✓ (exports, streams, native services; coexistence propagation) | ✓ ("update source systems with that same logical merge", REST/webhooks) | ✓ (data sharing/delivery, syndication) | ✓ (platform APIs) | Common core — 5/5 |
| Hierarchies/relationships between master records | ✓ (graph type, multi-parent) | ✓ (master record hierarchies) | ✓ (relationship management) | ✓ (typed relationships, hierarchies, inheritance) | n/v | Common — 4/5 |
| Embedded data quality (validation/cleansing) | ✓ (cleanse step) | ✓ (DQ native core) | ✓ (quality & governance) | ✓ (data quality capability) | ✓ (SemQL rules) | Common — 5/5 |
| Audit trail / history | n/v (not directly observed) | ✓ (history plugin, audit) | ✓ (full audit trails) | ✓ (auditable change history) | n/v | Common — 3/5 direct |
| Duplicate prevention at entry | n/v | ✓ (verbatim) | ✓ ("prevent issues before they spread") | ✓ (validation/approval gate) | n/v | Common — 3/5 direct |
| Reference data handled beside master data | n/v | ✓ (ONE RDM sibling; reference data in models) | ✓ (RDM initiative) | ✓ (master + reference in one repository) | n/v | Common — 3/5 |
| Implementation styles (consolidation/coexistence/centralized/mixed) | partial (real-time hub posture) | ✓ verbatim four styles | n/v | n/v | n/v | Variant — vendor-documented at 1 product; industry vocabulary |
| Single-domain MDM legitimacy | partial (MDM framed general) | ✓ verbatim business cases | partial ("customer, product, supplier or any") | partial (domain "clouds") | n/v | Variant — but 1-product explicit + 2 partial |
| Metadata-driven configurable data model | ✓ (tenant configuration) | ✓ ("fully metadata-driven") | ✓ (modeling via AI/config) | ✓ (data modeling capability) | ✓ (declarative design, SemQL) | Common core — 5/5 |
| AI-era additions (AI matching, AI assistants, MCP/agent consumption) | ✓ (platform framing) | ✓ (AI matching, MCP) | ✓ (Aisey, MCP) | ✓ (agentic platform framing, MCP) | ✓ (AI agents in docs) | Era-current, optional |

Reading notes: "n/v" = not verified from the fetched pages, not necessarily absent. Universal rows are the L0/L1 candidates; the cross-system consolidation + serving-back rows are what separate MDM from siblings.

## Canonical Model (abstraction result)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The master record of record for designated shared entities.** Persistent, individually identified, authoritative records for entity types the organization designates as master data (customer, product, supplier, location, employee, material…), held as the reference identity — the "single version of truth" — for those entities across the organization. Remove → the product becomes an evaluator (DQ), an inventory (catalog), or a transactional system (CRM/ERP).
2. **Cross-system identity consolidation.** The authoritative record is built and kept current by consolidating records contributed from multiple source systems: matching records that denote the same real entity and merging their content under survivorship rules, with source contributions retained/traceable on the record. The system is the standing authority on entity identity across systems — not a single-system master file, not a one-off dedup job. Remove → single-system master file (ERP/CRM internal master), or a data-quality dedup tool.
3. **Governed maintenance in service of the estate.** Golden records are kept current through a governed change loop — stewardship review of match proposals and conflicts, approval-gated publication, attributable changes — and made available to the consuming operational systems (publish/sync/API/stream), so downstream systems act on the shared identity. Remove → one-off consolidation/migration project, or a static shared dataset.

Jointly load-bearing: 1 alone = entity-shaped database; 2 without 1 = dedup/matching tool (DQ territory); 3 without 2 = shared database/sync layer; 1+2 without 3 = one-off consolidation project; 1+3 without 2 = manually-maintained shared register (no consolidation); 2+3 without 1 = integration machinery without held records.

### L1 — Common Mature Structure (standard, not definitional)

- Configurable matching machinery (deterministic/fuzzy; ML/AI-assisted matching in current products); separate configuration for source-record (instance) matching and master-record matching.
- Survivorship/trust rules per attribute; "best value wins" policies.
- Stewardship work surfaces: match-proposal queues, side-by-side record comparison, merge/unmerge/split operations, tasks assigned to stewards, draft states, publish workflow.
- Master record search/browse/compare/detail pages; hierarchical navigation.
- Hierarchies and typed relationships among master records (account/customer hierarchies, product hierarchies); graph-style multi-parent structures in some products.
- Metadata-driven, configurable data model (entity types, attributes, lifecycles) — every sampled product describes its model as configurable/metadata-driven.
- Input/output integration machinery: initial/full/delta loads, exports, REST APIs, streaming/event publication, connectors (ERP/CRM/enrichment).
- Embedded data-quality machinery: validation, cleansing, standardization, enrichment, duplicate prevention at entry.
- Audit trails/history, roles/permissions, activation/deactivation record states.
- Reference data handled beside master data (bundled or sibling product).

### L2 — Variant / Optional Structure

- **Implementation style** (where authoring lives, what is propagated): consolidation (downstream-only golden records), coexistence (golden records propagated back to sources; authoring stays in sources), centralized (hub is the only R/W master store), mixed (R/W in both) — vendor-documented at Ataccama; matches the industry's classic four-style vocabulary; treat as variant, not definition.
- **Domain scope**: single-domain MDM (customer/CDI, address, vehicle — Ataccama business cases) vs multi-domain suites (universal at the enterprise pole). Multi-domain breadth NOT definitional.
- **Domain packaging**: product / customer / business-partner (B2B) / supplier / location packages of the same platform (Stibo domain clouds).
- **Industry shapes**: healthcare party modeling (HCO/HCP), regulatory-compliance consolidation, CRM support (Ataccama business cases).
- **Deployment**: SaaS / self-hosted / hybrid / on-prem (Profisee full spectrum; Ataccama cloud/self-managed; Semarchy SaaS+self-hosted).
- **Suite position**: standalone MDM product vs one product line in a broader data-management platform (Ataccama ONE family; Semarchy Data Platform; Reltio platform) — packaging variant.
- **Model richness**: golden-record store vs graph/semantic model with typed relationships and attribute inheritance (Stibo, Reltio).
- **AI-era additions**: AI matching, AI stewardship assistants, MCP servers / agent consumption of master data — era-current, optional.
- **Authoring experiences**: role/task-specific "apps" over the master data (Profisee FastApps; Semarchy applications).

### L3 — Vendor-specific (research notes only)

- Reltio: crosswalk, "Operational Value (OV)", tenant configuration, HCO/HCP abbreviations, Context Intelligence Platform naming.
- Ataccama: ONE product-family decomposition (DQ&C / MDM / RDM / Desktop / Runtime), instance vs master layer naming, plans/steps, DPE/DPM infrastructure terms, Mixed Style page.
- Profisee: Aisey AI assistant, FastApps, MDS migration path, "Matching & Survivorship" as the capability name, SaaS/PaaS/IaaS/hybrid/on-prem five-way deployment claim.
- Stibo: STEP product name, "Trusted Intelligence Platform" framing, Data Clouds packaging, 100+ connectors claim, Loqate/D&B/Experian connector specifics.
- Semarchy: SemQL, xDM→Data Platform renaming, VS Code file-based design.
- Analyst badges (Gartner MQ/Forrester Wave/G2) across vendor pages — positioning only.

## Boundary Findings

- **vs Data Quality Platform** (discharges that pass's flag from this side): DQ platforms author rules and evaluate data the platform does NOT own as system of record, recording pass/fail results; MDM IS the system of record for master data — it holds the golden records. Removal test (DQ pass): "make the platform the system of record for the data → MDM." Interlock is tight and bidirectional: MDM products embed DQ machinery (Ataccama: "strong emphasis on Data Quality as a core part"; validation/approval gates at Stibo; Profisee quality capability), and DQ platforms connect to MDM as just another source (Ataccama DQ&C has an "MDM and RDM connection" source type). Boundary held: evaluator vs record-holder.
- **vs Data Governance Platform** (discharges that pass's CDE-management seam flag from this side): the governance platform governs the estate programmatically — policies, stewardship programs, CDE definitions, compliance processes — over data it does not hold; MDM manages the master data records themselves. The seam: "Customer ID" as a governed critical data element (a definition, an owner, a policy) belongs to governance; the consolidated customer record that gives the ID substance belongs to MDM. MDM products ship governance features (approval workflows, RBAC, policies — Stibo "Data Governance" capability) but the center of work is the record, not the program. Boundary held, documented both directions.
- **vs Data Catalog**: the catalog holds metadata ABOUT data assets (inventory + discovery); MDM holds the master data records themselves. Ataccama ships both as sibling products (ONE DQ&C beside ONE MDM) — packaging convergence, distinct centers. Consistent with the catalog pass's recorded seam.
- **vs PIM** (ratifies the PIM pass): PIM centers on product records structured for selling/marketing channels with outbound channel renditions; MDM centers on enterprise entity identity across systems, domain-general. A PIM can act as the product-domain master where the organization designates it so, but the Types differ in center of gravity (channel-ready content vs cross-system identity). Domain packaging ("product master data" inside MDM products, Stibo Product Data Cloud) shows the overlap is real but does not merge the Types.
- **vs CRM / ERP / HRIS**: operational systems of record own their transactions and their own domain records; MDM consolidates identity ACROSS such systems (the same customer in CRM + billing + ERP shipping = one master record). A single-system master file is not MDM — this is exactly why L0 leg 2 requires cross-system consolidation.
- **vs Customer Data Platform**: CDP collects behavior/event data and builds marketing-oriented profiles for activation; MDM builds governed operational master records for enterprise-wide use. Distinction kept conceptual this pass (no CDP product fetched); Reltio's own "unification vs MDM" framing supports "MDM = key entities + authoritative source of truth" as the narrower, governed discipline.
- **vs Data Warehouse / Lakehouse**: analytical copies for querying vs operational authoritative records served back to source systems (Ataccama's coexistence style propagates master data upstream — a warehouse never does that).
- **vs Reference Data Management**: reference data = code/value lists (countries, statuses), not entity instances; commonly bundled in MDM platforms (Stibo, Profisee) or shipped as a sibling product (Ataccama ONE RDM). Not a separate directory leaf.
- **vs endpoint "MDM" (mobile device management)**: name collision only — entirely different Type (§14 endpoint family). No relationship.
- **Registry-style MDM note**: the industry's classic "registry" style (central identity index without held golden-record content) was NOT directly evidenced this pass (Ataccama's four documented styles hold data in the hub in all variants). L0 leg 1 ("master record of record") is written to require held records; a pure registry index would strain leg 1 — recorded as an uncertainty rather than forcing the definition.

## Historical / Market-Sample Check

- Mainframe/ERP-era analog: the company "customer master file" — a central authoritative file maintained by clerks (matching "J. Smith" and "John Smith" as one customer), fed by branch paperwork, and distributed on tape to the applications that needed it. Satisfies all three legs at analog level (held authoritative record; cross-application identity consolidation; governed maintenance + serving). 
- Single-system item masters inside 1980s–90s ERP fail leg 2 (no cross-system consolidation) — correctly excluded; MDM as a named category emerged mid-2000s precisely when multi-system estates made cross-system identity the problem.
- The definition names no cloud, graph database, probabilistic-matching specifics, AI, MCP, or SaaS — all era machinery. Registry/consolidation/coexistence/centralized/mixed styles, single-domain vs multi-domain, SaaS vs on-prem are all variants.

## Uncertainties

1. Informatica (category anchor) unreachable (403 ×2 this pass + prior passes) — no Informatica claims made; enterprise pole triangulated via sampled products.
2. Profisee operational docs (docs.profisee.com) unreachable (transport error ×2) — Profisee evidence is product-site level (Tier 2); no Profisee-specific operational parameters asserted.
3. Semarchy deep MDM object docs unreachable (stale redirects; docs repositioned to "Data Platform") — evidence kept at platform level; Semarchy survivorship/matching depth not verified.
4. Registry-style MDM (identity index without held records) not directly evidenced; L0 written around held master records — flagged in Boundary Findings.
5. Reltio docs portal is a staging mirror ("temporary environment" footer) with real content but possibly not the final production docs — evidence treated as valid vendor documentation; no version-sensitive claims made.
6. Exact numeric limits, thresholds, retention windows not researched (and per evidence rules not asserted anywhere).
7. CDP comparison kept conceptual — no CDP product fetched this pass.

## Final Synthesis

A Master Data Management product is the organization's system of record for the identity of its shared core entities. Its defining work: hold authoritative, individually identified master records for entity types the organization designates as master data; build and keep those records current by consolidating the records contributed by multiple source systems — matching records that denote the same real entity, merging them, and deciding per attribute which value survives; and run a governed maintenance loop in which stewards review matches and conflicts, approve changes, and the authoritative records are published back to the operational systems that consume them. Everything else commonly seen — graph models, hierarchies, embedded data quality, reference data, AI matching, agentic access — is standard or optional capability layered on that spine. The Type's boundaries are clean: it is the record-holder (vs DQ the evaluator, vs governance the program layer, vs catalog the inventory), it is cross-system (vs CRM/ERP single-domain operational masters), it is operational and identity-centered (vs CDP marketing profiles, vs warehouse analytical copies), and it is entity-general even when packaged per domain (vs PIM).
