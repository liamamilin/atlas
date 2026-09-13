# Research Notes — Fiber Network Management

## Research Goal

Understand what "Fiber Network Management" software actually is in the market: what objects it manages, what users do with it, how work flows through it, and where its boundary sits against neighboring directory leaves (Telecom Network Planning / Design, Utility GIS, Telecom Inventory Management, Telecom Provisioning Platform, Telecom Service Assurance, Network Construction Management, Mobile Network Management).

## Initial Boundary (hypothesis before research)

- Guess: the fiber operator's system of record for its physical fiber plant (routes, cables, fibers, splices, splitters) plus operations on it.
- Likely confusions: (a) generic GIS / Utility GIS; (b) network design tools; (c) telecom equipment inventory; (d) service provisioning/activation; (e) service assurance/monitoring; (f) construction project management.
- Open question: does the leaf center the *physical plant record* or the *service fulfillment loop*? The directory already has separate leaves for provisioning, assurance, and order management, which suggests the plant-record reading.

## Research Questions

1. What objects make up the fiber plant record? (routes, cables, strands, ducts, closures, splitters, ports, equipment…)
2. How is connectivity modeled? (splicing, termination, patching, splitter ports, path/circuit tracing)
3. How do customers/services attach to the plant? (serviceable addresses, port assignment, reservations, availability)
4. What is the lifecycle? (design → build/as-built → operate → grow)
5. What interfaces do users actually work in? (map canvas, schematics/SLDs, splice views, forms, mobile field app)
6. How do faults get located? (tracing, OTDR ingestion, affected-service identification)
7. Where is the boundary vs GIS, design tools, inventory, provisioning, assurance?

## Representative Products

Selected for market coverage, documentation quality, and different product philosophies / customer tiers:

| Product | Pole | Customer tier | Evidence depth this pass |
|---|---|---|---|
| VETRO FiberMap | cloud-native fiber design/management for broadband operators | regional ISPs / altnets / engineering firms / public sector | product + operator-edition pages (Tier 2) |
| 3-GIS (3-GIS \| Web/Mobile/Admin) | Esri-platform enterprise network management, fiber + copper | enterprise carriers, wholesale, municipalities, also electric/gas utilities | solution + product + FAQ pages (Tier 2, FAQ fairly operational) |
| IQGeo Network Manager Telecom | global geospatial network management platform (absorbed OSPInsight) | Tier-1 operators + regional ISPs + utilities | product page with capability matrix + FAQ (Tier 2) |
| Netadmin Nine | Nordic-style fiber OSS: fulfillment/assurance around the network record | national telcos, wholesale/open-access, altnets | homepage + Resource Management module page (Tier 2) |
| OSPInsight (heritage) | 30-year standalone OSP fiber management, now IQGeo-owned | small/mid OSP operators | IQGeo acquisition/landing page only (Tier 2, thin) |

## Sources

All fetched 2026-09-08:

- VETRO — https://vetrofibermap.com/ ; https://vetrofibermap.com/products/fibermap-network-operators/
- 3-GIS — https://www.3-gis.com/ ; https://www.3-gis.com/telecom/telecom-asset-inventory-management ; https://www.3-gis.com/telecom/network-operations-maintenance
- IQGeo — https://www.iqgeo.com/ ; https://www.iqgeo.com/products/network-manager-telecom ; https://www.iqgeo.com/ospinsight (via www.ospinsight.com redirect)
- Netadmin — https://www.netadminsystems.com/ ; https://www.netadminsystems.com/platform/product-modules/resource-management

Unreachable / abandoned (per source-access limitation rules):

- VETRO help center (vetrofibermaphelp.zendesk.com) — auth-walled + transport error ×1 → abandoned; no Tier-1 VETRO claims.
- OSPInsight docs (docs.ospinsight.com) — transport error ×1 → abandoned; OSPInsight evidenced only via IQGeo pages.
- IQGeo /products/geo-comms path — 404 (superseded by Network Manager Telecom page).

Consequence: **no Tier-1 help-center articles were reached for any sampled product.** All evidence is official product/solution/FAQ pages (Tier 2). Assertion strength calibrated accordingly: no precise numeric limits, defaults, or state vocabularies are asserted in the final document; vendor marketing figures stay in these notes only.

## Product Observations

### VETRO FiberMap (evidence layer A unless noted)

- Self-positioning: "Fiber network design and management platform"; "Manage your network from design to monetization." Audiences: network operators, engineering firms, middle mile, public sector; roles: executives, GTM (go-to-market), planning, operations.
- Operator edition capabilities (directly observed):
  - "Effortless Design & Editing — rapidly generate fiber paths and link elements"
  - "Intelligent Fiber Management & Tracing — quickly find network issues to minimize downtime. Straight Line Diagrams (SLDs) instantly visualize fiber paths… multi-point tracing, alternate routes, and assess impact. Custom fields and quick filters… inherited fields"
  - "Data-Driven Network Dashboard — pinpoint specific network elements and circuits"
  - "Network Data Change Management — manage and document network changes… complete record of all user actions and system events for accountability"
  - "Automated Materials & Costing — automatically create Bills of Materials, including fiber cables, splice closures, equipment, conduits, ducts, and clamps, along with quantities and estimated costs"
- Companion products: VETRO Mobile (field crews, offline capture, "directly submit drawings to editors for immediate review and placement… streamlining our provisioning"); AddressBook (address validation, MDU handling, "single source of truth… from sales to billing"); Z-Manager (publish network plans for demand generation / pre-registrations).
- Customer quotes (marketing, but structurally informative): "VETRO became the source of truth for the splicing of fiber circuits and physical fiber assets"; "validating connections in a network design… catches errors before they become problems"; "visibility into our contractor progress and 'ready for sales' stages"; "real-time availability information" for customer signup.

### 3-GIS (evidence layer A)

- Self-positioning: "purpose-built software for telecom and utility networks, turning spatial, asset, and operational data into a more accurate view of critical infrastructure. Plan, build, inspect, manage, and operate."
- Telecom framing: "a connected network record for planning, designing, building, documenting, and managing fiber and copper networks."
- Asset & inventory solution page (directly observed):
  - Physical infrastructure: "fiber, copper, conduits, poles, cabinets, splice enclosures, handholes, structures, and equipment"
  - Logical relationships: "splicing, splitters, circuits, and service paths"; "connectivity at the individual fiber strand level, including how paths continue through splitters and downstream infrastructure"
  - Asset-level detail: "ownership and manufacturer to specifications, installation dates, and custom fields"
  - Geographic visibility: "map where the network exists today, including infrastructure not yet in service"
  - Serviceability context: "what is built, where capacity exists, and which assets are positioned to support new service opportunities"
  - Operational history: "installation details, field changes, maintenance history, asset condition"
  - "Authoritative network record — centralized system of record for telecom infrastructure, inventory, connectivity, and operational network data"
  - "Physical + logical network modeling — model both assets and the relationships that show how those assets support services, customers, and network activity"
  - Lifecycle continuity: "carry network data from planning and construction into operations, maintenance, troubleshooting, activation, and future expansion"
  - FAQ: telecom inventory management = "documenting, organizing, and maintaining records for the physical and logical components… fiber, copper, conduits, poles, cabinets, splice enclosures, handholes, equipment, circuits, and service paths"; replaces "spreadsheets, CAD drawings, paper maps, static GIS layers, legacy systems, and institutional knowledge"
- Network operations & maintenance page (directly observed):
  - "connect asset, connectivity, capacity, and field data so teams can respond faster"
  - Connectivity context: "which paths are involved, and what downstream services, areas, or customers may be affected"
  - Service impact: "identify outage areas, affected assets, and potential service impact using connected network records"
  - **OTDR detail (product-specific, directly observed):** "3-GIS | Web and 3-GIS | Mobile ingest OTDR results, taking into account slack loops, sag, and sequential values, and provide the physical address and coordinates of the break. For reports of multiple outages, 3-GIS | Web pinpoints the common assets between each downed equipment."
  - NOC teams: "assess outage location, affected paths, service areas, recent changes, and network impact"
  - Interoperability: "connect network records with active monitoring tools, OSS/BSS platforms, CRMs, field operations"
  - 3-GIS | Admin: "user access, permissions, tools, data visibility, QA/QC rules"
  - Windstream Wholesale case: remote fiber monitoring + GIS "to detect faults earlier, locate affected assets, and coordinate response before customer-reported issues drive the process" ("Before the trouble ticket")
- Products: 3-GIS | Web ("core network system of record… telecom network data, GIS editing, signal tracing, project tracking, enterprise collaboration in one browser-based system"), Mobile (redlines, inspections, outage tracing, offline), Admin, Diagramming, Prospector, Enterprise APIs (connect to "serviceability, OSS/BSS, CRM, construction").
- Also serves electric/gas utilities (Esri Utility Network workflows) — same vendor, different domain packaging.
- Marketing scale claims (L3, not asserted in final doc): 500M+ network records, 50M+ monthly transactions, 170K+ miles of fiber in one customer network, thousands of users.

### IQGeo Network Manager Telecom (evidence layer A)

- Self-positioning: "AI-powered geospatial network management software… plan, build, and operate fiber and coax networks"; "single, end-to-end platform to plan, design, build, and operate their physical network infrastructure."
- Capability matrix (directly observed):
  - "Outside and Inside plant inventory — flexible network model supports both outside and inside plant inventory requirements"
  - "Fiber planning and design — manual fiber network design and route planning"
  - "Fiber management — end-to-end fiber management including splicing, termination, patching, utilization, reservations, fault tracing, and location"
  - "Field mobility — online, responsive browser-based mobility that takes the full network model to the field on tablets" (+ offline per FAQ)
  - "Dynamic network schematics — automatically-generated schematic view that visually displays network connectivity down to the fiber level"
  - Search and reporting; embedded Google Maps/Street View; data import/export; BOM and labor cost management
  - Administration: user/group roles and access, custom attributes, configurable data forms, feature creation, API integration tiers
- FAQ (directly observed):
  - "model down to splice closures, patch panels, and strand-level detail"
  - "trace fiber and coax networks down to individual strands, splices, and connections"
  - "FTTH, PON, point-to-point, metro, and transport" + hybrid copper/coax
  - Fault management: "built-in tracing and schematic views, operators can quickly locate issues and restore service faster"
  - As-builts: "crews capture photos and redlines in the mobile app, and real-time visual AI automatically validates construction to automatically update the network model"
  - Migration from other fiber network management systems; flexible data model (custom attributes, rules, equipment catalogs)
  - "Is IQGeo a GIS?" — "goes far beyond GIS… can act as the system-of-record or integrate with existing ones, continuously maintaining a live digital twin"
- AI layer (era-current): visual AI validation of field photos, automated error detection for network records, AI agents (Visual Agent Studio: Asset Inventory / Drop Installation / Service Activation agents).
- Marketing ROI claims (L3): 50–90% design-time reduction, 33% engineering-cost reduction, etc.
- OSPInsight heritage page: "plan, design, build, analyze, and maintain fiber networks for more than 30 years"; now folded into IQGeo; Network Manager Telecom positioned as the successor for "fiber optic network management."

### Netadmin Nine (evidence layer A)

- Self-positioning: "Vertical Market Software purposely built for the fiber journey — network operators starting, transitioning to, or operating a fiber network business"; "We help fiber operators streamline every stage of the customer journey."
- **Boundary-revealing scope statement (directly observed):** "Netadmin takes care of your whole fiber business. Our platform offers the needed functionality for the fulfillment and assurance processes… Netadmin takes over after the network planning has been made and hands over to an invoicing platform when it is time for invoicing."
- Modules: Order Management, Service Provisioning, Resource Controlling ("communicates with your devices directly"), Resource Management (network inventory), Service Monitoring ("support service assurance processes"), Ticket Management, CRM capabilities, Address Management ("easy management of fiber delivery locations"), Work Order Management add-on ("scheduling and managing fiber installations"), Service Provider Portal (wholesale).
- Resource Management module (directly observed):
  - "stores all your devices and other resources… spanning from passive equipment like fiber panels to core routers and datacenter entities"
  - Device classes: active P2P (access/distribution switches, routers, CPE/RGW), PON (OLT, ONT), coax (CMTS, modems), passive (ODF/MDF panels), server infrastructure, wireless
  - Manages: "active or passive devices with cards and ports; software versions, hardware versions and configuration backups; network topology with routes/connections and connection types between devices; IP networks, MAC addresses, VLAN's; sites/POP's with coordinates"
  - "pre-integrated with Provisioning, Ticket Management, and Monitoring capabilities"
- Customer cases: Telia ("manage subscribers, services, and devices in their fiber networks", 1M+ households), Telenor Open Universe (wholesale L2 bitstream), JT (copper→fiber conversion OSS).
- Operations-manager framing: "It is crucial to understand which customers and addresses are affected by a failure."

### OSPInsight (heritage evidence, layer A but thin)

- "Fiber network management software… easily plan, design, analyze, and maintain their networks" for 30+ years; acquired by IQGeo; existing customers continue, new customers directed to Network Manager Telecom. Confirms the longevity and naming of the category ("fiber network management software" as a market label).

## Cross-product Comparison

| Dimension | VETRO | 3-GIS | IQGeo NMT | Netadmin | OSPInsight (heritage) |
|---|---|---|---|---|---|
| Plant of record (routes/cables/strands/closures/splitters/ports) | ✓ (fiber paths, splice circuits, physical assets) | ✓ (fiber, conduits, poles, cabinets, splice enclosures, handholes) | ✓ (OSP+ISP, splice closures, patch panels, strands) | ✓ (devices, panels, ODF/MDF, topology) | ✓ (OSP fiber) |
| Strand/fiber-level connectivity | ✓ (splicing of fiber circuits) | ✓ (individual fiber strand level) | ✓ (down to strands, splices) | partial (routes/connections between devices; port level) | ✓ (OSP heritage) |
| Geospatial map as primary surface | ✓ | ✓ (Esri-based) | ✓ (Google Maps/Street View embedded) | weaker (sites/POPs with coordinates; not map-first) | ✓ |
| Path/circuit tracing | ✓ (multi-point tracing, alternate routes, impact) | ✓ (signal tracing, trace circuits) | ✓ (fault tracing down to strands) | ✓ (topology; affected customers/addresses on failure) | ✓ (analyze) |
| Service/customer attachment | ✓ (availability, "ready for sales", AddressBook) | ✓ (serviceability, service paths, circuits) | ✓ (utilization, reservations) | ✓ (subscribers, services, delivery addresses) | ✓ (assignments) |
| Design + BOM/cost | ✓ (paths, BOM with cables/closures/conduits/ducts/clamps + costs) | ✓ (plan routes, OSP design) | ✓ (planning/design, BOM + labor cost) | ✗ (explicitly takes over AFTER planning) | ✓ (plan/design) |
| Field/as-built capture | ✓ (VETRO Mobile, offline, drawings→editors) | ✓ (Mobile: redlines, photos, inspections) | ✓ (offline tablets, photos+redlines, AI validation) | partial (Work Order Management for installations) | ✓ (OSP surveys) |
| Fault localization | ✓ (find network issues, minimize downtime) | ✓ (OTDR ingestion → address/coordinates; common-asset pinpointing) | ✓ (fault tracing + schematics) | ✓ (service monitoring + affected-customer view) | ✓ |
| Change governance / audit | ✓ (change management, full action record) | ✓ (Admin: QA/QC rules, permissions) | ✓ (roles/access; AI-audited ops) | ✓ (permissions by role) | ? |
| Schematics/diagrams | ✓ (SLDs) | ✓ (Diagramming module) | ✓ (dynamic schematics) | ? | ✓ |
| Fulfillment (orders/provisioning) | ✗ | integration-level (APIs to OSS/BSS) | add-on agents (Service Activation Agent) | ✓ core (Order Mgmt, Provisioning, Resource Controller) | ✗ |
| Monitoring/assurance | ✗ | integration-level (monitoring tools; OTDR feeds) | ✗ (tracing only) | ✓ core (Service Monitoring) | ✗ |
| Non-fiber domains | ✗ (fiber-focused) | copper + electric/gas utilities | coax/copper + electric/gas | coax devices, wireless, servers | ✗ |
| Platform substrate | standalone cloud | Esri ArcGIS | standalone + Google Maps, SaaS/private cloud | standalone suite | standalone (now IQGeo) |

Reading of the comparison:

- The **plant-of-record + connectivity + lifecycle** triad is present in every fiber-specific product (B layer: cross-product commonality).
- The **fulfillment/assurance machinery** (orders, device provisioning, monitoring) is present as a *core* only in the OSS-suite pole (Netadmin) and as *integrations/add-ons* elsewhere — it is not what the fiber-plant products are.
- The **map canvas** is near-universal in the plant-record pole but weaker in the fulfillment pole (Netadmin is coordinate/site-based, not map-first) — supporting "location-anchored records" as the invariant and "map-first canvas" as common implementation.
- Design/BOM and field/as-built are common but one sampled product explicitly excludes design (Netadmin) — so design is common-not-definitional for the Type as a whole; it is definitional only for the plant-record pole's design-heavy packaging.

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The fiber plant of record** — the operator's physical fiber infrastructure held as persistent, individually identified records: routes/paths, cables, fibers/strands, ducts/conduits, structures (poles, handholes, cabinets), splice closures/enclosures, patch panels/ODFs, splitters, ports, and active equipment — each located in the real world and carrying its attributes (ownership, specifications, installation data).
   - Remove → a generic GIS layer or asset spreadsheet; the fiber network as an ownable, queryable estate disappears.
2. **The connectivity model** — the plant records bound into a traversable topology (splices, terminations, patching, splitter ports) so that end-to-end paths through the network can be represented and traced.
   - Remove → map drawings and asset lists with no network semantics; "what connects to what" and "what does this path serve" become unanswerable.
3. **The managed plant lifecycle** — the record is actively worked and kept current: designed/extended, captured as-built from field work, and operated (paths traced, faults located, maintenance recorded) with every change written back to the record.
   - Remove → a static map archive; the "management" disappears.

Jointly-held is load-bearing: 1 alone = asset registry/GIS layers; 2 alone = abstract topology tool with no physical estate; 3 without 1+2 = work orders about nothing; 1+2 without 3 = a map archive, not management.

### L1 — Common Mature Structure

Present in most mature products, not required for recognition:

- interactive map canvas as the primary working surface (with base maps, street-level context)
- strand-level detail (individual fibers within cables)
- service paths / circuits assigned to customers or services; serviceability ("what can be sold where"); capacity/utilization and reservations
- straight-line diagrams / auto-generated schematics alongside the map
- mobile field app with offline capture (redlines, photos) feeding as-built updates
- BOM / materials and cost estimation generated from designs
- change management with user-action audit trail; QA/QC rules; role-based permissions
- fault localization support, including ingestion of OTDR/monitoring results (one product documents slack-loop/sag-aware OTDR placement — product-specific depth)
- search, reporting, dashboards
- integration surfaces to OSS/BSS, CRM, monitoring, construction systems

### L2 — Variant / Optional Structure

- plant scope: fiber-only vs fiber+copper/coax; OSP-only vs OSP+ISP
- architecture support: FTTH/PON vs point-to-point vs metro/transport vs middle-mile/backbone
- operator type: altnet/regional ISP vs tier-1 carrier vs wholesale/open-access vs municipal/public vs utility-with-fiber
- platform substrate: standalone cloud vs Esri/ArcGIS-embedded vs suite module
- center of gravity: design-heavy (engineering firms) vs operations-heavy (NOC/field) vs fulfillment-heavy (OSS suite pole)
- fulfillment/assurance extension: orders, device provisioning, service monitoring as built-in modules (suite pole) vs API handoff (plant-record pole)
- era-current additions: AI visual validation of field work, automated error detection, AI agents, public availability/demand portals
- deployment: SaaS vs private cloud vs on-premises

### L3 — Vendor-specific (research notes only)

- VETRO: Z-Manager (demand/pre-registration publishing), AddressBook product, "ready for sales" stage label
- 3-GIS: Prospector, Diagramming, Admin module names; Telecom Domain Network (Esri) positioning; OTDR slack-loop/sag/sequential-value handling; marketing scale figures (500M+ records, 170K+ miles, 50M+ monthly transactions)
- IQGeo: NetLux AI, Visual Agent Studio + named agents, Comsof Fiber (acquired design tool), editions/deployment matrix, ROI percentages (50–90% design time, 33% engineering cost, 6× QC, 100% AI-audited)
- Netadmin: Nine/Nine.2/Nine.3 versioning, module names (Resource Controller, One Touch Switch, Service Provider Portal), Telia 1M+ households case
- OSPInsight: 30-year heritage, acquisition by IQGeo

## Rejected Findings

- "Fiber network management = GIS." Rejected: GIS is a common substrate (3-GIS is Esri-based; IQGeo explicitly answers "beyond GIS"), and the fulfillment pole (Netadmin) is not map-first. The invariant is location-anchored plant records + connectivity, not a GIS engine.
- "Fiber network management = telecom inventory management." Rejected as identity: the market does call the plant record "telecom asset & inventory management" (3-GIS's own solution naming), but the directory separates the leaves; the defensible seam is the connected, geospatial, lifecycle-worked plant vs the equipment/services estate record. Flagged for joint review.
- "Fiber network management includes service activation/provisioning." Rejected as definitional: only the OSS-suite pole carries it as core; plant-record products hand off via APIs. Netadmin's own scope statement ("takes over after the network planning has been made") shows fulfillment is a neighboring layer.
- "Design tools are a different Type entirely, so design is out of scope." Rejected as too strong: in the plant-record pole, design happens *inside* the plant record (design → validate → as-built on one record). The seam vs Telecom Network Design is center-of-gravity, not exclusion.
- Precise numeric claims (records managed, miles of fiber, % time savings, household counts) — rejected from the final document: marketing figures without operational documentation.

## Boundary Findings

- **vs Utility GIS**: Utility GIS = generic geospatial engine + jurisdictional/utility data model stewardship; Fiber Network Management = the operator's own fiber estate with connectivity semantics and a worked lifecycle. Fiber products may be *built on* a GIS platform (3-GIS on Esri) — substrate, not identity. Remove connectivity + lifecycle → Utility GIS territory.
- **vs Telecom Network Planning / Telecom Network Design**: planning/design tools center the design act (route selection, cost modeling, scenario comparison); this Type centers the persistent plant record that designs flow into and out of. In sampled products design is a phase of the record's life (VETRO "design to monetization"; 3-GIS "from planning and construction into operations"). Straddle is real (engineering-firm packaging); recommend the design leaves hold the "design act vs plant of record" seam.
- **vs Telecom Provisioning Platform**: provisioning activates services on network elements (device configuration, service turn-up); this Type holds the physical plant and paths that activation consumes. Netadmin demonstrates the fulfillment pole as its own product family; 3-GIS/IQGeo expose activation only via APIs/add-on agents.
- **vs Telecom Service Assurance**: assurance monitors live network/service state and raises alarms; this Type holds the physical record that alarm localization is resolved against (3-GIS: monitoring integration, "before the trouble ticket"; Netadmin: Service Monitoring module beside Resource Management). Remove the physical plant record → pure assurance.
- **vs Telecom Inventory Management**: sharpest naming overlap — 3-GIS markets this exact space as "telecom asset & inventory management." Proposed seam: inventory management centers the equipment/services estate (devices, cards, ports, services, often datacenter/enterprise-centric, not necessarily geospatial); this Type centers the geospatial outside plant with strand-level connectivity and field/as-built operations. JOINT REVIEW RECOMMENDED when telecom-inventory-management is processed.
- **vs Network Construction Management**: construction management centers build projects (schedules, contractors, budgets); this Type receives construction outcomes as as-built updates to the plant record. Field-capture modules blur at the seam.
- **vs Mobile Network Management**: mobile centers RAN/radio access networks; this Type centers fixed fiber plant. Different object worlds despite the shared word "network management."
- **vs Enterprise Asset Registry / EAM**: asset registries hold equipment without network connectivity semantics or path tracing; remove connectivity → EAM/registry territory.
- **vs Telecom OSS (umbrella)**: "OSS" spans inventory, fulfillment, assurance; this Type is the network-resource-management slice specialized to fiber plant.

## Historical / Market-Sample Check (§24)

Paper-era fiber plant records satisfy the core: route maps and cable schedules (identified plant records located in the world), splice books and assignment sheets (connectivity), redlined as-builts and maintenance logs (worked lifecycle). No GIS, cloud, mobile, or AI is required. Conversely, a modern interactive map with no connectivity model (pretty fiber layers) fails the core — supporting connectivity as invariant rather than map polish. The definition is not over-fitted to the current cloud/GIS/AI implementation.

## Uncertainties

- No Tier-1 help-center documentation reached for any sampled product; all evidence is product/solution/FAQ pages. Operational specifics (exact object schemas, state names, validation rules, numeric limits) are deliberately not asserted.
- Netadmin's inventory depth at strand/splice level is unclear from the fetched page (it lists panels/ODF and "routes/connections" but not explicit strand-level splicing) — the fulfillment pole's plant record may be coarser than the GIS pole's. Kept as uncertainty; the final document does not claim strand-level detail is universal.
- OSPInsight's own operational documentation was unreachable; its inclusion rests on IQGeo's heritage pages.
- The exact market share / prevalence of the fulfillment-suite pole vs the plant-record pole was not measured; the two-pole reading is structural, not quantitative.
- Whether Esri's Telecom Domain Network (ArcGIS Utility Network extension) should eventually be treated as a platform-native variant or a competing substrate was noted but not resolved (3-GIS webinar evidence only).

## Final Synthesis

Fiber Network Management is the fiber operator's system of record for its physical fiber network, worked as a living record. Its defining core is the triad: (1) the fiber plant held as persistent, identified, location-anchored records; (2) those records bound into a traversable connectivity model (splices, terminations, splitter ports) supporting end-to-end path tracing; (3) a managed lifecycle that keeps the record current — design/extension, field-captured as-builts, and operations (fault localization, affected-service identification, maintenance history) all written back to the same record. Around that core, mature products add the map canvas, strand-level detail, serviceability/capacity, schematics, mobile field capture, BOM/costing, change governance, and monitoring/OTDR integrations; suites in the fulfillment pole wrap the record with orders, provisioning, and assurance. The Type is bounded against GIS (substrate), design tools (the design act), provisioning/assurance (the fulfillment loop), and equipment inventory (the estate without the connected plant).
