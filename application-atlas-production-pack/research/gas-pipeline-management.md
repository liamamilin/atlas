# Research Notes — Gas Pipeline Management

Research date: 2026-09-08

## Research Goal

Understand what "Gas Pipeline Management" software actually is from real products: what objects it manages (the pipeline network itself? integrity? flow? customers?), who uses it, what its core model is, and where its boundaries run against neighboring Types (Gas Utility Management, Utility GIS, Utility Asset Management / EAM, SCADA, Water Network Monitoring, Energy Trading).

## Initial Boundary

Hypothesis before research:

- The leaf sits in §19 Energy, Utilities & Telecommunications next to "Gas Utility Management".
- Working hypothesis: Gas Utility Management = the gas utility's customer/business operation (customers, billing, rates, service orders). Gas Pipeline Management = the physical pipeline network itself — the network as a modeled asset, its integrity/maintenance lifecycle, operational analysis (pressure/flow), and pipeline-safety compliance.
- Adjacent types suspected: Utility GIS (network model layer), SCADA (real-time telemetry/control), CMMS/EAM (maintenance records without network semantics), Energy Trading / scheduling (commercial transactions on pipeline capacity).

## Research Questions

1. What is the central object of record: the network model, the asset register, integrity events, or something else?
2. How is the pipeline network represented (topology, segments, nodes, equipment)?
3. What lifecycle machinery is bound to the network: inspection, integrity/risk, maintenance, leak/anomaly response, compliance?
4. Does operational/physical analysis (pressure, flow, hydraulic simulation) belong to the Type's core or to a sibling engineering tool?
5. Where does the commercial side of gas pipelines (nominations, scheduling, capacity transactions) belong?
6. What roles use the system and through what interfaces?
7. What rules matter (data governance, audit trail, regulatory anchoring)?
8. How does this Type differ from Utility GIS, EAM, SCADA, and the electric/water sibling types?

## Representative Products

Chosen for market representation + documentation accessibility, acknowledging the market splits into three functional poles:

| Product | Vendor | Pole | Evidence |
|---|---|---|---|
| Synergi Pipeline | DNV | pipeline integrity & risk management (gathering/transmission/distribution/offshore) | A |
| Synergi Gas | DNV | network analysis / hydraulic modelling (distribution/transmission/gathering) | A (same vendor as above — marked) |
| ArcGIS Utility Network | Esri | the network-model-of-record layer as a platform (cross-utility; used by gas utilities) | A |

Attempted but unreachable (recorded as research limitation, no claims drawn from them):

- Quorum Business Solutions / IFS (pipeline commercial/measurement products — quorumsolutions.com timed out twice; ifsguessed-path 404)
- GE Vernova Smallworld Gas Distribution Office (gevernova.com 404 ×2, ge.com 404 ×1)
- Hexagon Safety, Infrastructure & Geospatial (hxgncontent.com 403)
- ArcFM Solutions (arcfmsolutions.com transport error)

Consequence: the midstream **commercial/transaction** pole and the **GIS-vendor distribution** pole could not be directly verified this pass. All claims about those areas are kept at canonical-inference strength (Layer C) with qualified wording, and no vendor-specific facts from them appear anywhere.

## Sources

- DNV — Synergi Pipeline product page: https://www.dnv.com/services/synergi-pipeline/ (fetched 2026-09-08)
- DNV — Synergi Gas product page: https://www.dnv.com/services/synergi-gas/ (fetched 2026-09-08)
- DNV — software products overview: https://www.dnv.com/software/products/ and pipeline category: https://www.dnv.com/services/?types=2688 (fetched 2026-09-08)
- Esri — ArcGIS Utility Network overview: https://www.esri.com/en-us/arcgis/products/arcgis-utility-network/overview (fetched 2026-09-08)
- Unreachable: quorumsolutions.com, www.ifs.com/products/quorum-pipeline, gevernova.com / ge.com Smallworld pages, hxgncontent.com, arcfmsolutions.com

## Product A — DNV Synergi Pipeline

### Key observations (Layer A — directly observed)

Positioning: "Pipeline integrity and risk management software … maximize pipeline performance, ensure compliance, minimize risk". Explicitly an **enterprise platform for risk and integrity needs**.

- **Asset scope**: "across assets: pipelines, valves, pressure regulator stations, storage, etc."; "across segments: gathering, transmission, distribution, offshore"; "for both liquid and gas pipelines" — i.e., the product family is pipeline-segment-agnostic and names the network equipment classes.
- **Data foundation**: integrates multiple data sources into a single repository; Esri ArcGIS can be the **master data source** via a published map service; alternatively tabular import / REST API / data managed **within the software** ("Many users use Synergi Pipeline without a GIS"). Supports industry data models (vendor names UPDM / PODS) or custom models; "data model neutral".
- **Risk machinery**: comprehensive risk assessments and analytics; what-if scenarios; open "whitebox" modeling — users can create and edit their own risk models without coding.
- **Managed lifecycle**: "manage pipeline inspection, repair, and maintenance activities"; "track inspections, threats, and consequences"; "manage the full anomaly lifecycle"; prioritize and schedule activities across the entire Integrity Management Plan.
- **Compliance machinery**: "monitor compliance requirements and status"; HCA/MCA and Class Location identification/assessment; "production of data for annual audits and reporting"; activity compliance tracking; "comprehensive audit trails and versioning" for Management of Change.
- **Modules** (vendor naming): Activity Planning and Monitoring; Integrity Management; Quantitative Risk Management; In-line Inspection (ILI) Analysis; HCA/MCA and Class Location Assessment; Qualitative Risk Assessment.
- **Interfaces**: web-based enterprise platform; interactive dashboards; "GIS-based maps"; data viewer across sources; drill-down from enterprise view to individual assets.
- **Deployment**: SaaS (vendor-hosted) or on-premises; GIS server optional.
- Customer quote (Samarco PIMS project manager): integrity team "gets clearly designated tasks and responsibilities from the system … transparent and easily auditable".

Related same-family products listed by the vendor: Synergi Mains Replacement Planner (distribution repair/replacement/modernization planning), Synergi Gas, Synergi Liquid, Synergi Pipeline Simulator (surge analysis).

## Product B — DNV Synergi Gas

### Key observations (Layer A — directly observed; same vendor as Product A, marked)

Positioning: "Advanced network analysis and hydraulic modelling software" for gas networks; "trusted by pipeline engineers worldwide for 50+ years" (vendor claim — record, do not generalize).

- **Network model as digital twin**: "create digital twins of your physical infrastructure with precise component representation"; multi-asset analysis of "closed conduit networks of pipes, regulators, valves, compressors, storage fields, and production wells"; network scale from small systems to "1,000,000+ nodes" (vendor claim).
- **Hydraulic analysis**: pressure drops, flow rates, velocity profiles; steady-state and transient (unsteady-state) analysis; thermal modeling; equations of state (vendor names AGA, GERG-2008, Peng-Robinson); scenario comparison with differential analysis.
- **Operational decision support**:
  - Load approval assessment — "determine system capacity for new customer connections".
  - Regulator and compressor optimization (fuel/energy consumption).
  - Isolation impact analysis — "evaluate consequences of planned or emergency shutdowns"; Area Isolation module "shows the required valves for closure to isolate any pipe or zone", and with the Customer Management module "generate a list of the affected customers".
  - Over-pressurization prevention "through detailed pressure analysis".
  - Model calibration — "compare simulation results with SCADA measurements for continual model refinement".
- **Model lifecycle**: build by hand or from GIS/CAD; Model Builder module automates GIS import (points→linear facilities, attribute mapping); Facilities Management module synchronizes model with GIS updates without full rebuild; Version Management (parent/child model versions, permissions, change tracking).
- **Customer/billing touchpoint**: Customer Management module integrates with the Customer Information System to compute load factors, assign loads to the model, display customer info — i.e., customer data enters as *load* on the network, not as managed objects.
- **Compliance touchpoint**: vendor FAQ describes annual compliance studies on safety relief valves under "DOT Part 192" supported by the Regulator Station module (MAOP/MOP pressure levels); reporting templates "aligned with regional regulatory formats".
- **Integration**: imports data from SCADA, GIS, CIS, enterprise systems.
- **Energy-transition content**: hydrogen blending (up to 100% per vendor), biogas, CO₂, ammonia; composition tracking; calorific-value management; sectorization analysis.

## Product C — Esri ArcGIS Utility Network

### Key observations (Layer A — directly observed; platform-layer contrast)

Positioning: "Manage your infrastructure with an advanced network information model"; "an enterprise geographic information system (GIS) for modern utilities"; extends ArcGIS Enterprise / ArcGIS Pro.

- **Single unified model of a connected network**: "manage a connected network with a single unified model"; "digital twin of your connected network"; "advanced network modeling … view inside complex assemblies of devices and lines, and management of how assets are connected within them".
- **Data governance**: "ensure data integrity through rules and logic"; "secure, role-based access to network data" with viewing/editing capabilities per role.
- **Analysis**: "advanced analytics and tracing capabilities … aggregate and report dynamically based on event conditions … for both current, historic, and future states".
- **Surfaces**: desktop, mobile, web (field maps imagery shows a gas pipeline being traced on a mobile device).
- This page documents the **network-model layer as its own market layer** (cross-utility, any media). It contains no integrity, risk, hydraulic or compliance machinery of its own — that is exactly the contrast this sample was chosen for.

## Cross-product Comparison

| Dimension | Synergi Pipeline (DNV) | Synergi Gas (DNV) | ArcGIS Utility Network (Esri) |
|---|---|---|---|
| Central object | network assets + integrity/risk records bound to them | connected network model (digital twin) + scenarios | connected network information model |
| Network model of record | yes — imports/manages network asset data; GIS optional | yes — explicit "digital twin", node/segment/equipment model | yes — the product IS this layer |
| Managed lifecycle on the network | inspection/repair/maintenance + anomaly lifecycle + compliance | analysis/scenario lifecycle; model versioning | no (governance/tracing only) |
| Integrity / risk machinery | core (risk models, threats, ILI, HCA/class) | not present | not present |
| Hydraulic / pressure analysis | not present | core (steady/transient, overpressure) | not present |
| Compliance records | core (audit trail, MOC, annual reporting) | present as touchpoint (MAOP/MOP studies, regional report formats) | not present |
| Customer data | not observed | enters as load via CIS integration | not present |
| SCADA | not observed | consumed for model calibration | not present |
| Primary interface | web platform, dashboards, GIS maps | model editor + analysis surfaces | map-centric GIS (desktop/web/mobile) |
| Role center of gravity | integrity manager / compliance | network planning engineer | GIS/records steward |

Reading: the market realizes the Type in poles. The **network model of record** appears in all three. The **pipeline-specific managed lifecycle** (integrity/risk/inspection/compliance at Synergi Pipeline; hydraulic/operational analysis at Synergi Gas) is what turns the model into "management". A product holding only the model is the GIS layer (Esri sample).

## Canonical Model

### Level 0 — Defining Invariant (deliberately small)

Two jointly-held structures:

1. **The pipeline network model of record** — a persistent, identified, connected model of the physical pipeline system: pipe segments joined, regulated, compressed and limited by network equipment (valves, regulator stations, compressor stations, storage, supply/meter points), carrying attributes. The model authoritatively answers "what exists, where, with what attributes, connected how". It may live in an external GIS as master data or inside the product.
2. **A pipeline-specific managed lifecycle bound to that network** — the operator's analysis and activity records tied to network locations: integrity/risk assessment, inspection and maintenance/repair activity, anomaly/leak handling, pressure/hydraulic studies, and the compliance records these generate. The network record accumulates the managed history.

Jointly-held is load-bearing:
- (1) alone = a utility GIS / network-model platform (the Esri pole);
- (2) without (1) = a task tracker / document store with no network semantics;
- both together = Gas Pipeline Management.

Historical check: the analog-era gas utility (paper system maps + leak/inspection/pressure-test ledgers + desk hydraulic calculations for load growth) satisfies both legs; 1990s-era GIS + integrity databases satisfy both. The definition names no modern implementation pattern.

### Level 1 — Common Mature Structure

Present across the sampled poles (Layers A/B):

- GIS integration (often GIS-as-master) — and symmetrically, the ability to hold the model internally
- risk assessment machinery with editable models; what-if/scenario analysis
- integrity planning: inspection programs (incl. in-line inspection data), anomaly lifecycle, prioritized mitigation/mitigation-plan scheduling
- maintenance/repair activity planning and monitoring
- audit trail / versioning / change management on records
- compliance support anchored to locations (consequence-area/class-location assessment; annual reporting; pressure-protection studies) — realization differs by jurisdiction
- hydraulic analysis (steady-state; transient in mature products); model calibration against SCADA
- isolation/trace reasoning over the topology (which valves isolate a zone; affected customers)
- load-growth / capacity assessment for new connections (customer data entering as load)
- dashboards and map-based visualizations; role-based access on the model

### Level 2 — Variant / Optional

- segment focus: distribution vs transmission vs gathering vs offshore
- fluid family: gas core; liquid and multiphase siblings exist in the same product families (recorded as adjacent siblings)
- packaging pole: integrity-led vs simulation-led vs network-model-platform-led (the sampled products are literally one per pole)
- deployment: SaaS vs on-premises
- regulatory regime: jurisdiction-specific programs and report formats (US federal pipeline-safety code named by one vendor's FAQ only — keep generic)
- energy-transition modeling: hydrogen blending, biogas, composition tracking (vendor-marked capability, modern-era)
- mains replacement / modernization planning as a dedicated extension
- commercial/transaction machinery on pipeline capacity (nominations/scheduling): NOT VERIFIED this pass — treated as adjacent territory (see Boundary Findings), no claims drawn

### Level 3 — Vendor-specific (kept out of the final document)

- Module names: Area Isolation, Regulator Station, Model Builder, Facilities Management, Customer Management, Time-Varying, Automated Design, Optimization (Synergi Gas); Integrity Management, Quantitative Risk Management, ILI Analysis, HCA/MCA & Class Location Assessment (Synergi Pipeline)
- Industry data-model names (UPDM, PODS), equations of state (AGA, GERG-2008, Peng-Robinson, Redlich-Kwong)
- Numeric claims: "1,000,000+ nodes", "50+ years", "100% hydrogen"
- Deployment specifics: MS Azure hosting, MS SQL Server, browser list

## Vendor-specific Findings

- DNV markets Synergi Pipeline and Synergi Gas as separate products for the two poles (integrity vs simulation) with cross-links (GIS integration, shared data). Whether integrity and simulation live in one product or two is vendor packaging, not Type structure.
- Esri positions the network model as a horizontal platform layer across utilities — confirming that the network-model leg alone is its own market layer rather than the whole Type.
- DNV's FAQ naming "DOT Part 192" shows regulation anchoring but is vendor-specific evidence for one jurisdiction; other regimes exist and were not directly documented this pass.

## Boundary Findings

- **vs Gas Utility Management** (sibling leaf): the customer/business operation (customers, billing, rates, service orders) vs the pipeline network itself. Evidence: Synergi Gas integrates with the CIS but customer records enter only as *load* on the network — the managed object remains the network. Remove the network as managed object → you are in the sibling leaf. Conversely the pipeline system stops caring about individual customers beyond service points.
- **vs Utility GIS / network-model platform**: a product that stops at the connected model + governance + tracing is the GIS layer (Esri pole demonstrates this shape). "Management" is added by the network-bound lifecycle leg. Remove the lifecycle → Utility GIS territory.
- **vs Utility Asset Management / EAM**: EAM holds maintainable asset records without connected-network semantics (segment/valve topology, trace, isolation). Remove the connectivity/topology semantics → generic asset management.
- **vs SCADA**: SCADA is live telemetry and control of field instrumentation. Pipeline Management *consumes* SCADA measurements (calibration — directly observed) but its defining record is the network model + lifecycle, not real-time process state.
- **vs CMMS / maintenance management**: maintenance execution is a capability inside the lifecycle leg; a product that is only work orders is CMMS territory.
- **vs Energy Trading / gas scheduling (commercial pole)**: transmission pipelines also carry commercial machinery (capacity transactions, nominations, scheduling, allocations). That machinery is transaction-shaped on capacity rights rather than network-shaped; it could not be verified this pass (Quorum/IFS unreachable). Recorded as a likely distinct/adjacent Type — flagged for the taxonomy owner rather than merged.
- **vs electric/water sibling types** (Grid Operations Platform / DMS, Water Network Monitoring): same pattern over a different medium and physics. The medium and the failure semantics (pressure, gas release, integrity threats) are what keep this leaf distinct.
- **"Remove what to become another Type" summary**: remove the managed lifecycle → network-model platform; remove the network model → integrity/inspection task tracker; remove gas/pressure semantics → generic EAM/GIS; move to customer/business objects → Gas Utility Management.

## Uncertainties

1. The commercial/nomination/scheduling side of gas transmission (Quorum-family products) is unverified — all statements about it are boundary-level inference only.
2. Distribution-GIS-vendor pole (Smallworld Gas Distribution Office, ArcFM, Hexagon) unverified; the claim "GIS is commonly the master data source for the network model" rests on one vendor's FAQ + the Esri platform's existence. Kept at moderate wording in the final document.
3. Regulatory program specifics (which assessments, which reports) vary by jurisdiction; only one vendor-FAQ jurisdiction mention was observed. Final document keeps compliance discussion generic.
4. Whether all mature products include hydraulic analysis (vs integrity-led products) is not established; treated as common-pole capability, not defining.
5. Same-vendor limitation: two of three samples share one vendor; cross-product commonality claims are therefore weaker than a 3-vendor sample would support. Mitigated by choosing opposite poles, but flagged.

## Final Synthesis

Gas Pipeline Management is the pipeline operator's network system of record: a connected, attribute-carrying model of the pipeline system (segments + valves/regulators/compressors/stations), plus the pipeline-specific lifecycle managed against that model — integrity and risk, inspection and maintenance, anomaly/leak handling, pressure/hydraulic analysis, and location-anchored compliance records. The market realizes one Type in three poles (integrity-led, simulation-led, model-platform-led), each pole documenting a different half of the core; no single pole is the whole Type. Adjacent territories: the utility's customer/business system (sibling leaf), the network-model platform layer (GIS), SCADA (live telemetry), EAM (assets without topology), and the commercial transaction layer on pipeline capacity (unverified this pass; likely distinct).
