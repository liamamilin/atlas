# Research Notes — Utility GIS

## Research Goal

Understand what a Utility GIS is as an Application Type: the core object model of a GIS as operated by a utility (electric, gas, water/wastewater), what makes the utility domain a distinct specialization of the generic GIS engine, who uses it, what the main workflows are (maintain the connected network model → trace → map → serve the model to consumers), and where its boundaries lie against the sibling GIS leaves (Government GIS, Agricultural GIS) and the utility/telecom/design siblings that prior passes have already seamed (Utility Asset Management, OMS, ADMS, Grid Operations Platform, Gas Pipeline Management, Fiber Network Management, Telecom Network Design, Civil/Site Design, Utility Field Service Management, SCADA).

Context carried in (from STATUS.md Boundary Issues and prior passes):

- **agricultural-gis (§20) / government-gis (§24) joint-review flag**: "all three are domain specializations of the same generic GIS engine (create/manage/analyze/map spatial data); the directory has no generic GIS leaf; shared framing, joint review when Government GIS and Utility GIS are processed." The government-gis pass adopted the shared framing (generic engine + jurisdictional authoritative-geography stewardship invariant) and left the utility-gis side pending. This pass must discharge the flag from the utility side.
- **utility-asset-management (§19) forward flag**: "the seam is network-model-of-record vs asset-lifecycle-of-record" — the GIS holds the georeferenced network model (layers, connectivity, LRS); asset management holds asset records and their lifecycle, consuming GIS as location/connectivity substrate. This pass must ratify or reject that seam.
- **OMS / ADMS / grid-operations-platform passes**: all three held "Utility GIS = model source" seams (the GIS holds as-built geographic asset records; operational systems derive working copies and run real-time loops). This pass sits upstream and should ratify from the source side.
- **gas-pipeline-management pass**: "a product that stops at the connected model + governance + tracing is the GIS layer (Esri pole demonstrates this shape); remove the lifecycle → Utility GIS territory."
- **fiber-network-management pass**: "fiber products may be built on a GIS platform (3-GIS on Esri) — substrate, not identity."
- **telecom-network-planning / telecom-network-design passes**: "GIS platforms supply the substrate and data models; the planning/design act sits on top."
- **civil-site-design pass**: "GIS records existing assets and their attributes; civil/site design authors proposed works against terrain."
- **gas-utility-management pass**: "the pipe network is not this Type's object set; network data enters only as the delivery context of served premises."

## Initial Boundary

- Hypothesis: a Utility GIS is a geographic information system operated by a utility to maintain the authoritative georeferenced model of its physical network — the plant and how it connects — and to turn that model into maps, tracing, and analysis for the utility's engineering, field, and operations work, and for the systems that consume the network model.
- Nearest neighbors: Government GIS and Agricultural GIS (same engine, different domain data model); Utility Asset Management (network model vs asset lifecycle); OMS/ADMS/Grid Operations (model source vs operational loop); SCADA (as-built model vs real-time telemetry); Gas Pipeline Management (model vs managed integrity lifecycle); Fiber Network Management (substrate vs fiber estate lifecycle); Telecom Network Design (substrate vs design act); Civil/Site Design (record vs proposed works); Utility Field Service Management (model vs field work execution); Land Records/Cadastre (landbase consumed as context vs stewarded as record).
- Unknowns at start: is connectivity/topology definitional or merely common? Is the as-built system-of-record role definitional? Does the model-distribution duty (feeding OMS/ADMS/asset management) belong in the definition? Do the water/gas/streetlight/telecom flavors change the core?

## Research Questions

1. What is the core object model of a utility GIS (network features, connectivity, topology, domain networks, subnetworks, structures, devices, assemblies)?
2. What does the utility specialization add beyond the generic GIS engine (georeferenced layers + map canvas + spatial operations)?
3. What are the defining workflows: model construction and maintenance, connectivity editing and validation, tracing, cartographic production, model distribution to consumers, design-to-as-built updates?
4. Who uses it and through which interfaces (desktop editing, web viewers, trace tools, schematics, field apps)?
5. What rules matter: connectivity rules, edit validation, topology currency, versioning, coordinate reference systems, flow physics by commodity?
6. Where are the boundaries vs the sibling and adjacent Types listed above — and does the joint-review flag resolve as keep-all-three?

## Representative Products

Selection rationale: market representation + different product philosophies + different customer tiers + documentation quality.

| Product | Pole | Evidence tier reached |
|---|---|---|
| Esri ArcGIS Utility Network | dominant platform engine (the GIS engine itself, with a purpose-built utility network data model) | Tier 1 (official ArcGIS Pro help: "What is a utility network?" + "Utility network vocabulary") |
| GE Vernova Smallworld GNM (Geo Network Management) | heritage enterprise network-model pole (electric/gas/water/telecom; large utilities) | Tier 2 (official product page + FAQ) |
| Schneider Electric ArcFM Solution | Esri-based utility solution suite (editing/design/web/mobile applications on the ArcGIS platform) | Tier 2 (official product-range pages, myArcFM portal, Esri partner listing) |
| Milsoft WindMilMap | small-utility integrated suite pole (co-ops/munis; GIS + OMS + engineering analysis + billing) | Tier 2 (official product page) |
| IQGeo Network Manager Electric | modern cloud-native "geospatial work execution" pole (municipal/co-op to Tier 1) | Tier 2 (official product page + FAQ) |

Rejected/abandoned: Hexagon G/Technology (major enterprise pole; docs.hexagongeospatial.com unreachable — 403/transport errors, consistent with prior passes), Autodesk/Innovyze water-network GIS (403/404 in prior passes), 3-GIS (fiber pole — belongs to Fiber Network Management territory per that pass), QGIS (generic engine, already sampled by the government-gis pass; no utility-specific layer).

## Sources

Fetched 2026-09-10 (all live):

- Esri — "What is a utility network?" (ArcGIS Pro help) — https://pro.arcgis.com/en/pro-app/latest/help/data/utility-network/what-is-a-utility-network-.htm
- Esri — "Utility network vocabulary" (ArcGIS Pro help) — https://pro.arcgis.com/en/pro-app/latest/help/data/utility-network/utility-network-vocabulary.htm
- GE Vernova — Smallworld GNM product page (incl. FAQs) — https://www.gevernova.com/software/products/geospatial-network-management-smallworld-gis
- Schneider Electric — ArcFM for Utilities product range — https://www.se.com/us/en/product-range/61765-arcfm-for-utilities
- Schneider Electric — myArcFM ArcFM overview — https://myarcfm.schneider-electric.com/s/arcfm
- Schneider Electric — EcoStruxure ArcFM Web / ArcFM Viewer product pages — https://www.se.com/us/en/product-range/61755-ecostruxure-arcfm-web , https://www.se.com/us/en/product-range/61756-arcfm-viewer
- Esri partner listing — "ArcFM by Schneider Electric" — https://www.esri.com/partners/schneider-electric-a2T70000000TNg7EAG/arcfm-a2d70000000VGqyAAG
- Esri Canada — ArcFM Solution page — https://www.esri.ca/en-ca/products/specialized-applications/arcfm-solution
- Milsoft — GIS (WindMilMap) product page — https://www.milsoft.com/engineering-operations/gis-field-engineering/
- IQGeo — homepage (incl. FAQ) — https://www.iqgeo.com/
- IQGeo — Network Manager Electric product page (incl. FAQs) — https://www.iqgeo.com/products/network-manager-electric

Known-unreachable / limitations (recorded; no content asserted from them):

- https://doc.arcgis.com/en/utility-network/ (404; pro.arcgis.com help used instead — still Tier 1)
- GE Vernova Smallworld Core product page (404; GNM product page used instead)
- Hexagon G/Technology documentation (unreachable, consistent with prior passes)
- No Tier 1 operational user guides were reachable for Smallworld GNM, ArcFM, Milsoft, or IQGeo — their structural claims below are vendor self-description (product pages/FAQs), treated as layer A for the product and layer B for the Type.

## Product Observations

### Product A — Esri ArcGIS Utility Network (evidence layer A — official help, directly observed)

- Definition (verbatim): "A utility network is the main component users work with when managing utility and telecom networks in ArcGIS, providing a comprehensive framework of functionality for the modeling of utility systems such as electric, gas, water, stormwater, wastewater, and telecommunications. It is designed to model all components that make up your system—such as wires, pipes, valves, devices, circuits, and zones—and allows you to build real-world behavior into the network features you model."
- Stated capabilities: "Create and edit features and objects that model every type of utility equipment. Discover how features and objects in the network are connected. Trace how resources, such as gas, water, and electricity, flow through the network. Provide an operational view of how the dynamic devices of your utility are currently configured. Analyze how the network is affected by real-world events such as storms, outages, or equipment failure."
- Deployment models: enterprise (services-based, multiuser, web/mobile/desktop) vs single-user (file/mobile geodatabase, desktop only).
- Visualization: thematic cartographic maps per use case (customer service, field collection/inspection, distribution management); **network diagrams** ("logical views... simplified, symbolic representation"); viewing inside complex assemblies; display filters for pressure zones/circuits.
- Analysis: post-storm network inspection; load summary reports ("the number of customers being supplied by a specific subnetwork in an electric network"); upstream/downstream tracing ("water utilities can determine which valves to shut off when a pipe bursts to isolate the area"); cross-system tracing (an electric outage affecting gas/water delivery).
- Editing: templates ("creating a power pole with transformers already attached"); multiuser concurrent editing; "Editing rules and validation in the network ensure data quality by preventing the entry of logically invalid data and associations. For example, a reducer must be connected to pipes of the correct diameter on either end."
- Vocabulary (Tier 1, the deepest structural evidence in this pass):
  - **Associations** model relationships of three kinds: **connectivity**, **containment**, **structural attachment**.
  - **Connectivity**: implicit (geometric coincidence — shared endpoint/vertex x,y,z) vs explicit (connectivity associations between non-coincident features).
  - **Connectivity rules**: "govern the types of network features that can connect or associate... defined based on business practices... enforced by snapping and the Validate Topology tool."
  - **Domain networks**: "industry-specific collection of feature classes... to represent the assets of industries—such as electric distribution, gas transmission, or telecommunications"; a utility network can have one or more; e.g., transmission and distribution tiers.
  - **Feature classes**: **Device** ("operational domain features with active properties that can impact the flow of resources... a valve controls the flow of water; a transformer changes electrical power...; a meter measures..."), **Junction** ("connectivity properties, but do not have an effect on the resource... taps, pipe tees"), **Line** ("linear operational features such as wires and pipes... conduct or deliver a utility resource"), **Assembly** (containers such as switchgears, transformer banks, pump assemblies), plus **structure network** features (poles, trenches, duct banks) held via structural attachment, and nonspatial junction/edge objects for dense inside-plant modeling.
  - **Network topology**: "the arrangement of how point, line, and polygon features share geometry and connectivity. The network topology (or network index) enables tracing analysis and rapid retrieval of network features based on logical connectivity." Edits create **dirty areas** ("mark modified features... out of date in the network topology... cleared when the network topology is validated").
  - **Subnetworks**: e.g., feeders, pressure zones; **subnetwork controllers** define them; traces support **condition barriers** ("stop at all closed devices in a water network"), **function barriers**, upstream/downstream/isolation/loops/connected trace types; **named trace configurations** shareable to web and field apps.
  - **Network attributes** (e.g., electric phases, pipe diameters) propagate through traces; **attribute rules** auto-populate attributes, restrict invalid edits, run QA checks.
  - **Network diagrams**: "symbolic representation of network features... simplified schematic view... often also referred to as schematic representations... A one-line diagram for electric utilities is an example."

### Product B — GE Vernova Smallworld GNM (evidence layer A for product claims; marketing discount applied)

- Positioning (verbatim): "Smallworld Geo Network Management (GNM) creates a detailed digital representation of a utility's electric, gas, water, or telecom networks. Proven, scalable, and providing an enterprise-wide network view with data quality and integrity enforced, GNM supports a fully connected network model that forms a solid foundation for asset infrastructure modernization."
- "Not just another GIS": "GE Vernova's GNM solutions are purpose-built to help utilities and telecoms manage their physical asset network model information, both geospatially and schematically... Generic GIS solutions stop at basic mapping. GNM goes above and beyond."
- Model distribution: "It shares the network model data across the enterprise for a consistent view – from the back office to the field." "It provides the as-built, geo-connected network model and relevant asset data that fuels key use cases like disruption planning and response, simulations, vegetation management, DER optimization, and more." Interoperable with GE Vernova's grid software (GridOS; ADMS/FLISR/DERMS named).
- FAQ (vendor's own GIS definition): "Geographic information system (GIS) refers to a system designed to capture, store, manipulate, analyze, manage, and present spatial or geographic data. The utilities industry leverages GIS technology to create as-built network models of their assets. This network model forms the backbone for numerous other grid applications, such as DERMS, ADMS, AEMS, and more."
- FAQ (difference GIS vs GNM): generic GIS solutions have "shortcomings that make it difficult to ensure their network model is complete, accurate, and available at all times"; GNM "enables unique, utility-specific use cases... network reliability assessments, connectivity analysis, load balancing, flow optimization."
- Field model updates: "With GNM's Network Update application, teams can update the network model in real time, while out in the field."
- Benefits named: reduced costs (streamlining design, data capture workflows), better planning, increased accuracy ("automated fault location, and isolation and restoration mechanisms"), scalability, field collaboration, integration.
- Vendor-cited Gartner quote: "Utilities are moving away from viewing GIS as a static system of record — essentially, passive digital maps — to using GIS to manage dynamic network models." (Gartner, How Utility CIOs Can Unlock the Business Value of Geospatial Information Systems, 2022 — recorded as vendor-cited analyst framing, not independently verified.)
- Blog (GNM 6.0): "the network model remains foundational"; "strengthening the role and integrity of the connected network model across planning, design, build, and operations."

### Product C — Schneider Electric ArcFM Solution (evidence layer A for product claims)

- myArcFM overview (verbatim): "A comprehensive enterprise GIS platform built specifically for utilities to better plan, design and operate their GIS infrastructure. ArcFM is a highly resilient, consolidated work management solution that includes spatial asset management, network planning and analysis, operational awareness, field mobility and seamless integration with key enterprise systems."
- Esri partner listing: "The ArcFM Solution XI Series is the next generation of ArcFM that maximizes a utility's investment in Esri's Utility Network... ArcFM Editor XI provides new ways for ensuring the highest quality data and delivers new editing tools for keeping asset and network data at its best... Built on the new foundation of the ArcGIS Utility Network Management Extension." "ArcFM Designer XI, ArcFM Web XI and ArcFM Mobile XI fill out the rest of the ecosystem and offer the most comprehensive utility GIS solution available today." Industries: "Electric & Gas, Water, Wastewater & Stormwater."
- Esri Canada page: "Developed by Schneider Electric, the ArcFM Solution is a powerful extension to the ArcGIS platform. It provides a complete out-of-the-box enterprise GIS solution for facilities management designed to meet the needs of electric, gas and water/wastewater utilities, and telecommunications service providers." "ArcFM consists of a family of models and a set of sophisticated tools for editing, modelling, maintenance and management of facility information." Suite benefits include "Greater access to spatial data for improved outage management, customer service and dispatch."
- Companion surfaces: ArcFM Web ("GIS data visualization and reporting... expands the capabilities of GIS across the organization"), ArcFM Viewer ("Enterprise query and display tool. Makes facility and asset database information available, efficiently, to users across the utility"), ArcFM Mobile ("Extend the value of your GIS investment into the field. With ArcFM Mobile XI, connected and disconnected field crews..."), ArcFM Designer ("Graphic Work Design... for designers and engineers").
- ArcFM Solution Maps and Apps: configurable maps/apps for electric, gas & water, communications networks through the ArcGIS platform; examples include Electric Facilities map ("utility staff, from field technicians to customer service representatives, access to basic geographic utility information"), Mobile Map Services (online/offline field viewing), Responder OMS reliability maps (integration with Schneider's own OMS).
- Interpretation: the Esri-based solution-suite pole — the GIS engine is Esri's; ArcFM adds utility-domain data models, editing/design tooling, and enterprise distribution surfaces on top.

### Product D — Milsoft WindMilMap (evidence layer A for product claims)

- Positioning (verbatim): "Say goodbye to paper maps or outdated versions of your service grid. With Milsoft Geographic System (GIS) - WindMilMap®, you can have a single, integrated system for all your engineering and operations applications."
- Engineers tab: "A complete, detailed electric circuit connectivity model is essential for planning and operating your system grid. The ability to easily maintain the connectivity model is a cornerstone of the Milsoft Geographic Information System (GIS). Designed to take the power of the Milsoft Engineering Analysis logic and embed it in the ESRI® environment, Milsoft GIS provides a single data source for the electrical connectivity model. This capability in our GIS is unique in the industry. The Milsoft GIS also includes project management tools to enable each user to create his or her versions of the model as necessary to do their job."
- "More Than a Pretty Picture": "A complete, detailed electric circuit connectivity model is essential for planning and operating the electric network, yet several GIS systems available only provides a 'representation' of your model. With Milsoft GIS, you get much more than a pretty picture. True electrical connectivity ensures attributes such as phasing, feeder, and substation are automatically updated when feeds change. Dynamic editors for complex objects like transformer banks and switchgear make modeling them easy."
- "Single Point of Entry": "Milsoft GIS (WindMilMap) is the cornerstone of the Milsoft product suite, allowing for a true single point of entry for electrical model data. Whether edits are performed in the field using Milsoft Electric Projects, or in the office using an ESRI editor, the changes seamlessly appear in the Milsoft Outage Management and Engineering Analysis systems."
- Staking integration: "Our staking software, Milsoft Electric Projects, automates manual processes, streamlines workflows, and integrates seamlessly with GIS platforms."
- Billing integration: "Integrate your Customer Billing system and Milsoft GIS with real time exchange of service location and the customer billing connectivity, service status, coordinates, transformer bank location information and polygon district information."
- Customer testimonial (Randolph EMC, CEO): "Milsoft's Windmil Maps seamless integration with map viewing, staking and outage management has transformed our daily business and has a positive affect on every department it touches."
- Interpretation: the small-utility integrated pole — the GIS is the connectivity model of record and the hub from which OMS, engineering analysis, staking, and billing all feed; built inside the Esri environment.

### Product E — IQGeo Network Manager Electric (evidence layer A for product claims)

- Positioning (verbatim): "IQGeo gives telecom and utility operators a single, end-to-end platform to plan, design, build, and operate their physical network infrastructure." "IQGeo's AI-powered geospatial network management software unifies the entire network lifecycle for telecom and utility networks... With native mobility at its core, IQGeo delivers an always-accurate, always-accessible view of complex network assets."
- FAQ: "Is IQGeo a GIS? IQGeo goes far beyond GIS. As an AI-first network intelligence platform, it can act as the system-of-record or integrate with existing ones, continuously maintaining a live digital twin..." — the work-execution-layer posture: augment/replace the GIS of record while still holding the network model.
- Network Manager Electric: "It supports the full range of electric infrastructure: substations, transformers, poles, underground and overhead lines, switches, and distributed assets, along with full hierarchy and connectivity details." "Network Manager Electric provides spatially precise outage details for field teams and integrates fault tracing, switching scenarios, and schematic views to speed outage restoration." "It models distributed energy resources (DERs), EV charging, and renewable connections."
- Integration: "Network Manager Electric connects with GIS, CAD, ADMS, OMS, EAM, ERP and other enterprise platforms." "It doesn't replace your GIS or work management systems, it connects them, making your network data actionable in real time."
- Field: "Crews can access the spatial network model and workflows to be performed in the field—even offline—along with AI to guide their work, update records in real time, and sync changes back automatically." "Flexibly build, maintain and update the network model as it exists in the real world, while connecting every utility task (design, as-builts, inspections, outage restoration, compliance) directly to the live network model with precise geospatial context."
- Deployment: "cloud (AWS by default), hybrid, or on-premises." Customer tiers: "trusted by municipal, cooperative, and Tier 1 utilities" (Stedin, TEPCO Power Grid, WAPA, LG&E-KU, PGE named).
- Utility use-case menu: Field Design, Digital As-Builts, Meter Installation, Asset Inspection, GIS Field Mobility, Outage Mobility.

## Cross-product Comparison

| Dimension | Esri ArcGIS Utility Network | GE Vernova Smallworld GNM | Schneider ArcFM | Milsoft WindMilMap | IQGeo Network Manager Electric |
|---|---|---|---|---|---|
| Form | platform engine + purpose-built network data model (enterprise or single-user deployment) | purpose-built enterprise network-model platform ("not just another GIS") | solution suite layered on the Esri platform (Editor/Designer/Web/Mobile XI) | integrated small-utility suite (GIS + OMS + engineering analysis + billing), built in the Esri environment | cloud-native platform ("geospatial work execution"; can act as system-of-record or integrate with existing GIS) |
| Network model | explicit: features modeling "wires, pipes, valves, devices, circuits, and zones"; connectivity + containment + structural attachment; domain networks/tiers | "fully connected network model"; "as-built, geo-connected network model"; geospatial AND schematic | "family of models... for editing, modelling, maintenance and management of facility information"; built on the Utility Network | "complete, detailed electric circuit connectivity model"; "true electrical connectivity" (phasing/feeder/substation auto-update) | "full hierarchy and connectivity details" over substations/transformers/poles/lines/switches/DERs |
| Tracing | upstream/downstream/isolation/loops/connected; condition/function barriers; named shared trace configurations | connectivity analysis; "automated fault location, and isolation and restoration mechanisms" | network planning and analysis (suite-level naming) | feeds Milsoft OMS + Engineering Analysis (tracing executed by consumers) | "fault tracing, switching scenarios, and schematic views" |
| Schematics | network diagrams (one-line diagrams named) | "both geospatially and schematically" | via ArcFM Web/suite surfaces | via Engineering Analysis consumers | "schematic views" |
| Model distribution | hosted services; web/field apps; named trace configurations shared to web/field | "shares the network model data across the enterprise"; fuels ADMS/FLISR/DERMS/vegetation/DER | ArcFM Web/Viewer/Mobile; Maps and Apps; Responder OMS integration | "single point of entry"; changes "seamlessly appear in the Milsoft Outage Management and Engineering Analysis systems"; billing integration | "connects with GIS, CAD, ADMS, OMS, EAM, ERP" |
| Editing governance | connectivity rules + validation ("a reducer must be connected to pipes of the correct diameter"); dirty areas; attribute rules; versioning | "data quality and integrity enforced" | "new ways for ensuring the highest quality data"; version controls | "increases quality while minimizing an accidental mapping error"; per-user model versions | AI validation of field work ("validating change as work is performed") |
| Field | field apps consume shared traces; mobile editing via enterprise deployment | Network Update application ("update the network model in real time, while out in the field") | ArcFM Mobile XI (connected/disconnected crews) | field edits via Electric Projects (staking) appear in OMS/engineering | native mobile-first; offline; AI guidance |
| Cartographic output | thematic maps per use case; display filters | enterprise-wide network view | ArcFM Web visualization/reporting; Maps and Apps | map viewing integrated with staking/OMS | always-accurate network view; web/mobile |
| Deployment | enterprise geodatabase / single-user file | enterprise (heritage on-prem; cloud evolution "VMDS Cloud") | on the ArcGIS platform (per Esri deployment) | Esri environment; suite | cloud (AWS default) / hybrid / on-prem |
| Customer tier | all tiers (platform) | large utilities + telecom (heritage enterprise) | electric/gas/water utilities; telecom providers | co-ops/munis (US co-op association memberships) | municipal/co-op to Tier 1 (Stedin, TEPCO, WAPA) |
| Commodity breadth | electric, gas, water, stormwater, wastewater, telecom | electric, gas, water, telecom | electric, gas, water/wastewater/stormwater, telecom | electric (co-op focus) | electric + gas + telecom/fiber |

Reading: all five products implement one recognizable structure — a georeferenced, connected network model of record worked on through a map canvas, traced and analyzed, and distributed to the utility's consumers. The poles differ in where the engine sits (generic platform vs purpose-built model vs suite vs integrated suite vs work-execution layer), not in the structure. Connectivity is named by every product as the dividing line between a utility GIS and "just mapping" (Esri: "discover how features... are connected"; Smallworld: "fully connected network model"; Milsoft: "several GIS systems... only provides a 'representation'"; IQGeo: "full hierarchy and connectivity details"; ArcFM: built on the Utility Network's connectivity foundation).

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant

A Utility GIS is the utility-domain specialization of a GIS: a system whose world is the **utility's connected network model of record**. The minimal structure without which the Type collapses:

1. **Persistent georeferenced spatial data store** — features (geometry + attributes) organized as layers under defined coordinate reference systems; the store persists across sessions. Remove → a drawing/CAD tool, not a GIS.
2. **Map canvas** — the store visualized as composited, interactive layers on a map. Remove → a tabular database or spreadsheet.
3. **Spatial operations** — query/select by location and attribute, measure, overlay/proximity-type analysis over the layers. Remove → a static map image or image viewer.
4. **The connected utility network model of record** — the system holds the utility's physical network (plant: conductors/wires, pipes, poles, transformers, valves, devices, meters, structures) as georeferenced features **held with connectivity** — the model records how the plant joins into a traversable network, not merely where it sits — and maintains that model as the as-built system of record that the utility's engineering, field, and operational work consumes. Remove → items 1–3 alone are a generic GIS (Government/Agricultural GIS territory, or a generic GIS used ad hoc); a located-asset map without connectivity is utility asset mapping, not the Utility GIS category.

Items 1–3 are the generic GIS engine (shared with Government GIS and Agricultural GIS, per the joint-review framing). Item 4 is the utility specialization and the reason the directory leaf exists. L0 deliberately excludes: industry data-model templates, connectivity-rule engines, trace toolkits, schematic diagrams, subnetwork management, design/staking workflows, mobile field apps, model-distribution integrations, AI validation, cloud deployment — none is required to recognize the Type.

### L1 — Common Mature Structure

Present across the sample (multi-product) but not definitional:

- **Industry data models (domain networks)** — packaged plant taxonomies for electric/gas/water/telecom; transmission/distribution (or pressure-tier) organization; asset classification hierarchies (asset group/type-class structures).
- **Connectivity rules and validation** — rules governing which feature classes may connect/associate; edit-time enforcement; validation passes; error inspection; dirty-area-style topology currency tracking.
- **Tracing toolkits** — upstream/downstream/isolation/connected trace types; condition barriers (e.g., stop at closed devices); named/reusable trace configurations shared to web and field apps.
- **Network diagrams** — schematic/one-line views derived from the same model (geospatial AND schematic representation).
- **Subnetwork management** — feeders, pressure zones, circuits; controllers defining them; customer/load summaries per subnetwork.
- **Model distribution to consumers** — services/exports/integrations feeding outage management, distribution/grid management, asset management, field apps, and billing/CIS (service locations, transformer/feeder bindings).
- **Design-to-as-built loop** — proposed designs/staking, per-user or named versions, as-built reconciliation back into the model.
- **Field/mobile model access** — view/collect/update the model in the field, commonly offline with sync.
- **Cartographic production** — circuit/feeder maps, thematic maps per audience, print/export, web maps.
- **Multiuser editing governance** — versions, conflict resolution, permissions, audit-grade edit trails.
- **Landbase/basemap context** — parcels, addresses, imagery, streets consumed as reference context.
- **Service-point/premises binding** — linking network features (transformers, mains, service locations) to customers for operations and billing.

### L2 — Variant / Optional Structure

- **Commodity flavor**: electric (radial, source-based flow) vs gas/water (pressurized, looped, sink-based) vs streetlight vs telecom extension — different plant taxonomies, flow physics, and trace semantics; the same core serves all.
- **Product philosophy**: platform engine (configure your own network model on a generic GIS platform) vs purpose-built network model (vendor's mature industry data model) vs solution suite on a platform vs integrated small-utility suite vs work-execution layer over/alongside existing GIS.
- **Deployment**: enterprise geodatabase/cloud/hybrid/on-premises/single-user desktop.
- **AI/automation layer**: AI validation of field work, automated error detection, agent-style guidance — era-current at some poles, absent in others.
- **Grid-orchestration positioning**: the network model marketed as the backbone for ADMS/DERMS/FLISR-class platforms (vendor-pole framing).
- **Customer tier**: Tier 1 investor-owned utilities vs co-ops/munis — different scale, same structure.

### L3 — Vendor-specific (kept out of the final document except as named examples)

- Esri: utility network feature classes (device/junction/line/assembly/junction object/edge object), association types (connectivity/containment/structural attachment), domain networks/tiers/subnetwork controllers, dirty areas, named trace configurations, asset packages, branch versioning, ArcGIS Pro/Enterprise deployment split.
- GE Vernova: Smallworld GNM naming, VMDS/cloud evolution, Network Update application, GridOS interoperability framing, Gartner quote.
- Schneider: ArcFM Editor/Designer/Web/Mobile/Viewer XI product split, Responder OMS integration, ArcFM Solution Maps and Apps, myArcFM portal.
- Milsoft: WindMilMap naming, Electric Projects (staking), Engineering Analysis embedding ("unique in the industry" claim), phasing/feeder/substation auto-update mechanics, MultiSpeak-certified integrations.
- IQGeo: Network Manager Electric/Telecom/Gas naming, "geospatial work execution" category framing, network twin, Visual Agent Studio/agents, Comsof Fiber, AWS-default cloud.

## Vendor-specific Findings

- The Gartner quote cited by GE Vernova ("moving away from viewing GIS as a static system of record... to using GIS to manage dynamic network models") is vendor-cited analyst framing — useful as market-direction evidence, not definitional, and not independently verified.
- Milsoft's "This capability in our GIS is unique in the industry" (embedding engineering-analysis logic in the GIS) is a vendor claim; the underlying pattern (GIS as the connectivity model feeding engineering/OMS consumers) is cross-product.
- IQGeo's "goes far beyond GIS" positioning is a boundary-relevant vendor claim: the work-execution layer still holds the network model ("can act as the system-of-record or integrate with existing ones"), so it remains inside this Type as a variant posture rather than a different Type.
- ArcFM's identity as "a powerful extension to the ArcGIS platform" documents the suite-on-platform pole; its XI series is explicitly "built on the new foundation of the ArcGIS Utility Network Management Extension" — evidence that the platform engine and the solution suite are distinct market roles over one shared structure.
- Esri's single-user vs enterprise deployment split shows the same structure served at personal and organizational scale — deployment is not definitional.

## Boundary Findings

1. **vs Government GIS (§24) — joint-review flag DISCHARGED from this side.** Same engine, different domain data model. Utility GIS centers the connected utility network (plant + connectivity serving engineering/field/operations); Government GIS centers the jurisdiction's administrative geography (parcels/addresses/boundaries/streets serving many departments + public). Removal tests: strip the connected network model → the government GIS core remains a Government GIS; strip the jurisdictional administrative base → a Utility GIS remains. The two coexist in one organization (a municipal utility and its city parent may even share a platform). **Keep-all-three RATIFIED**: the directory has no generic GIS leaf; the three domain leaves (Government/Utility/Agricultural) share the engine and are carried by their domain data models, users, and duties. This pass's evidence confirms the shared framing both prior passes adopted.
2. **vs Agricultural GIS (§20)** — same engine; farm fields & agronomic layers vs the connected utility network; growers/agronomists vs utility GIS staff/engineers/crews. Consistent with the agricultural-gis pass's framing; no conflict.
3. **vs Utility Asset Management (§19) — forward flag RATIFIED.** The seam is network-model-of-record vs asset-lifecycle-of-record. The GIS holds the georeferenced connected model (geometry + connectivity + cartography); asset management holds asset records and their lifecycle (condition, work, cost, whole-life governance), consuming the GIS as location/connectivity substrate. Both hold asset-ish records; what is primary differs. In embedded deployments (e.g., a GIS-centric asset platform) the two live in one product family — adjacency, not identity. Remove the connected network model → asset management remains; remove the asset lifecycle/care/governance → the Utility GIS remains.
4. **vs OMS / ADMS / Grid Operations Platform (§19) — model-source seams RATIFIED from the source side.** The GIS holds the as-built model; operational systems derive working copies and run real-time loops (outage prediction, switching, state estimation). Corroborated verbatim: Smallworld positions GNM as fueling ADMS/FLISR/DERMS use cases; Milsoft positions WindMilMap as the single point of entry whose changes "seamlessly appear in the Milsoft Outage Management and Engineering Analysis systems"; Esri's utility network provides "an operational view" but the operational loop lives in the consuming systems. Remove the real-time operational loop → the Utility GIS remains; remove the maintained as-built model → the operational system has nothing to derive.
5. **vs SCADA (§16)** — as-built model vs real-time telemetry/control. The GIS records what exists and how it connects; SCADA senses and controls the live state. No telemetry or control in the GIS core.
6. **vs Gas Pipeline Management (§19)** — RATIFIES that pass's test: the connected model + governance + tracing is the GIS layer; pipeline management adds the network-bound managed lifecycle (integrity, risk, hydraulic analysis, compliance programs). Remove the lifecycle → Utility GIS territory.
7. **vs Fiber Network Management / Telecom Network Design (§19)** — substrate vs fiber-estate lifecycle / design act. Fiber products are commonly built on GIS platforms; the fiber estate with connectivity + worked lifecycle is the managed object there. Note: telecom network GIS exists as a market (Esri's utility network explicitly covers telecommunications; Smallworld ships a telecom network inventory) — the same engine extends to telecom, but the directory assigns telecom estates to the telecom leaves; this leaf's core domain is the utility network (electric/gas/water), with telecom documented as a recognized extension of the same structure.
8. **vs Civil/Site Design (§17) / Telecom Network Design (§19)** — record vs design act. The GIS records the as-built network; design applications author proposed works against terrain/context. The design-to-as-built handoff is the seam: designs land in the GIS as as-built updates (Milsoft staking → GIS; ArcFM Designer → network data; IQGeo digital as-builts).
9. **vs Utility Field Service Management (§19)** — model vs field work execution. The GIS provides the map/model context crews consume; FSM holds work orders and crew capacity. Field model updates (as-builts captured in the field) flow back into the GIS. Remove the work-order/crew machinery → the Utility GIS remains.
10. **vs Utility Vegetation Management (§19)** — the GIS provides the network context (circuits, spans, feeders) vegetation programs work against; the work discipline lives in the vegetation Type (Smallworld explicitly names vegetation management as a downstream use case of the network model).
11. **vs Land Records / Cadastre System (§24)** — the landbase (parcels, addresses, streets) is context the utility GIS consumes as reference layers, not stewards as record; stewardship of the jurisdictional base is the Government GIS's role.
12. **Taxonomy observation (carried from agricultural-gis and government-gis, addressed from this side)**: the directory has no generic "GIS" leaf; Government/Utility/Agricultural GIS are the three domain specializations present. Keep-all-three ratified. The generic GIS engine also serves other buyers (telecom, transportation, environmental) — the Utility GIS leaf is justified by the utility domain's distinctive data model (the connected network), its users (utility GIS staff, engineers, crews), and its duties (as-built model custody + model distribution to operations), not by vendor category vocabulary.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit? The L0 requires only: persistent georeferenced layers + map canvas + spatial operations + the connected network model of record. The 1990s–2000s desktop utility GIS (connected features in a desktop geodatabase or CAD-derived environment, printed circuit/feeder maps, manual or tool-assisted tracing) satisfies this fully — no cloud, no web services, no mobile apps, no AI required. The paper-era practice it digitized — the utility's map room holding circuit and wall maps that recorded connected plant, updated by drafters as the as-built record — satisfies the stewardship role conceptually (the engine items are software-specific, exactly as in the sibling GIS passes). Non-US utilities (European DSOs, Asian utilities — Smallworld's and IQGeo's named customer bases) satisfy without any US-specific regime. Conversely: a generic GIS holding utility asset points without a connectivity model is utility mapping (the substrate posture), not the Utility GIS category; an OMS with a map view is not a Utility GIS. The definition does not over-fit to the current cloud/AI era.

## Uncertainties

- No Tier 1 operational user guides were reachable for Smallworld GNM, ArcFM, Milsoft, or IQGeo; their structural claims are vendor self-description (product pages/FAQs) — layer A for the product, layer B for the Type. The final document calibrates wording accordingly ("purpose-built", "commonly", "documented as").
- Hexagon G/Technology (a major enterprise pole) could not be sampled; the enterprise-suite pole rests on Smallworld + ArcFM evidence.
- Water-network specialist products (Innovyze/Bentley class) were unreachable in prior passes; water evidence rests on multi-utility products (Esri's water examples, Smallworld's water networks, ArcFM's water/wastewater industries).
- Whether every deployed utility GIS holds connectivity natively (vs simple located-asset layers) is uncertain at the market's low end — Milsoft's own remark that "several GIS systems available only provides a 'representation' of your model" implies mapping-only postures exist in the wild. This pass treats the connected model as the category's structure (all five sampled products center it) and records the mapping-only posture as outside the category (substrate/asset-mapping territory).
- Numeric facts (feature-class counts, schema limits, version counts, performance figures) were not collected and are not asserted anywhere.
- The Gartner quote is vendor-cited and not independently verified.

## Final Synthesis

A Utility GIS is the utility-domain specialization of a GIS: a system whose world is the **utility's connected network model of record** — georeferenced layers (geometry + attributes under coordinate reference systems) holding the utility's physical network (wires/conductors, pipes, poles, transformers, valves, devices, meters, structures) **held with connectivity** (how the plant joins into a traversable network), worked on through a **map canvas** with **spatial operations**, maintained as the as-built system of record by the utility's GIS/mapping staff, and consumed by the utility's engineering, field, and operational work — with the model distributed outward (as services, derived copies, and integrations) to outage management, distribution/grid management, asset management, field apps, and billing. The generic GIS engine is shared with Government GIS and Agricultural GIS; what makes this leaf distinct is the domain data model (the connected utility network — connectivity is the signature no other domain GIS carries as its center), the operator (a utility acting as the network model's custodian), and the consumption pattern (operational systems derive working copies from the maintained model). Everything else commonly bundled — industry data-model templates, connectivity-rule engines, trace toolkits, schematic diagrams, subnetwork management, design/staking workflows, mobile field apps, AI validation, cloud deployment — is common mature structure or variant, not definition.
