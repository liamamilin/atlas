# Research Notes — Telecom Network Planning

## Research Goal

Understand what a **Telecom Network Planning** application is as an Application Type: what a "plan" is inside these products, what objects and workflows constitute the planning act, how planning relates to demand, to the existing network, to investment decisions, and to downstream design/construction — and where the Type's boundary sits against Telecom Network Design (the closest sibling, which pre-held a seam for this pass), Fiber Network Management, Telecom Inventory Management, Network Construction Management, Telecom Provisioning Platform, Mobile Network Management, and generic analytics/GIS tools.

## Initial Boundary (hypothesis before research)

Working hypothesis: Telecom Network Planning is the **decision layer** of telecom network engineering — it turns demand into costed, prioritized deployment intent (where/what to build, with which architecture, at what cost and return, in what order) **before** detailed design begins. The design pass (telecom-network-design, 2026-09-10) pre-held this seam from its side: "the vendors themselves draw intent-vs-buildable-artifact… but the straddle is heavy (products market 'planning & design' as one solution; the wireless pole's leading tool self-labels 'planning and optimisation' while doing detailed design), so the planning pass should hold the same center-of-gravity approach rather than exclusion." The fiber pass (fiber-network-management, 2026-09-08) additionally pre-held: planning/design tools center the act; the plant record centers the record; and Netadmin verbatim ("takes over after the network planning has been made") shows fulfillment is a neighboring layer.

Nearest neighbors going in: Telecom Network Design (intent vs buildable artifact), Fiber Network Management (plant of record), Telecom Inventory Management (estate of record), Network Construction Management (build execution), Telecom Provisioning Platform (service activation), Mobile Network Management (live RAN operation), Site Selection Platform (real-estate lens on one planning subtask), Utility GIS (substrate), Capacity Management (IT-side analog).

Unknowns going in: whether the fixed-line pole (demand/route/cost) and the wireless pole (coverage/capacity/site) share one Type structure; whether planning is a standalone product category or always a workflow inside a platform; how far investment/business-case machinery is definitional; whether OSS-side capacity planning (core/transport traffic forecasting) belongs to this Type.

## Research Questions

1. What is the unit of planning work (plan/scenario/study)? What granularity does it carry (decision-grade vs build-grade)?
2. What does planning ground itself in (demand data, traffic, coverage/capacity gaps, existing network)?
3. What are the alternatives being compared (routes, topologies/architectures, site placements, technology choices)?
4. What quantification does planning produce (cost estimates, BOM, revenue/ROI, coverage/capacity outcomes)?
5. What is the terminal output (prioritized deployment intent? business case? design handoff?) and how does it flow downstream?
6. How does the wireless pole differ (propagation, site selection, frequency planning, interference)?
7. Who performs planning (operator planning teams, sales engineering, engineering firms) and how does that shape the product?
8. Where exactly is the seam vs Telecom Network Design, and how heavy is the product-level straddle?
9. What is NOT planning (inventory, design, construction, provisioning, live-network operation)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers — deliberately avoiding re-sampling the design pass's products (3-GIS Web, IQGeo Network Manager, VETRO, Atoll, iBwave) as primary samples; those are used only as cross-references:

| Product | Vendor | Pole | Customer tier |
|---|---|---|---|
| Comsof Fiber | IQGeo (acquired Comsof NV 2022) | Automated FTTx planning & estimating — business case, deployment-area selection, topology/cost comparison | Fiber operators + engineering design firms (Deutsche Telekom, Proximus, Brightspeed, Zayo class) |
| Optimized Planning (use case) | IQGeo | High-level fiber planning & feasibility for investment decisions, explicit planning-vs-design split | Tier-1 fiber operators (Deutsche Telekom) |
| 3-GIS \| Prospector | 3-GIS | Demand→routes→cost→prioritization "before detailed design begins", as an extension of the plant-record platform | Mid-size operators + sales engineering (FiberLight) |
| VistaPlan / Planet | Infovista | RF planning & investment optimization — dimensioning, site selection, coverage prediction, what-if scenarios, CAPEX/ROI | Tier-1 MNOs (KDDI, Ooredoo, Zain, Ericsson; "400+ MNOs" claim) |
| HTZ Communications (ex ICS telecom) | ATDI | Technology-neutral radio network planning & modelling — prospective planning, coverage studies, traffic analysis, AFP | Civil operators, public safety, defence, broadcast, regulators |

Pole coverage: fixed-line fiber planning (3 products, three philosophies: automation-first, platform use-case, plant-record extension) + wireless RAN planning (2 products, two philosophies: tier-1 RF suite, spectrum-centric neutral tool). Backhaul/transport planning appears as one product line (Ellipse) — single-source, held as variant evidence. OSS-side capacity planning (core/transport traffic forecasting) not sampled — scope note in Uncertainties.

## Sources

All fetched 2026-09-10 (Tier 2 official product/solution/FAQ pages; no Tier-1 help centers reachable — see Uncertainties):

- Comsof Fiber product page: https://www.iqgeo.com/products/comsof-fiber (comsof.com redirects here)
- Comsof Fiber FAQ: https://www.iqgeo.com/product/comsof-fiber/faq
- IQGeo Optimized Planning use case: https://www.iqgeo.com/telecom-use-cases/optimized-planning
- 3-GIS | Prospector: https://www.3-gis.com/software/3-gis-prospector
- Infovista VistaPlan: https://www.infovista.com/products/planet-suite/network-planning-optimization
- Infovista Planet: https://www.infovista.com/products/planet/rf-planning-software
- ATDI Radio Network Planning: https://atdi.com/products-and-solutions/radio-network-planning/

Cross-referenced (fetched by sibling passes, cited from their research files):
- Forsk Atoll — research/telecom-network-design.md (fetched 2026-09-10)
- VETRO FiberMap — research/telecom-network-design.md (fetched 2026-09-10)
- 3-GIS planning-vs-design FAQ — research/telecom-network-design.md (fetched 2026-09-10)
- Netadmin scope statement — research/fiber-network-management.md (fetched 2026-09-08)

Unreachable (abandoned per network rules): TEOCO (root + ASSET product page, timeouts ×2), Ranplan (525), InfoVista /products/planet direct URL (404; reached via suite page).

## Product Observations

### Product A — Comsof Fiber (IQGeo)

Evidence layer: A (directly observed on official pages).

- Self-description: "The leading automated fiber planning and design software for telecom operators and engineering firms who want to quickly and cost-effectively scale their fiber-optic networks."
- Planning act (verbatim): "Automate fiber planning and estimating — Your engineers can quickly compare area costs, scenarios, and architectures to understand the best returns for network designs." "Quickly compare multiple scenarios and architectures."
- FAQ (load-bearing for the Type): "Comsof Fiber is a GIS-based design automation software that helps users plan and design their FTTx networks faster and better. Typically, our clients use our software to **build a better FTTx business case and select the deployment areas**. Then, they will leverage the power of Comsof Fiber to create the FTTx designs that will be used to build their network." — the vendor's own planning→design sequence.
- FAQ (boundary vs inventory): "Is Comsof Fiber an inventory tool? No. Comsof Fiber is an FTTx planning and design software. An inventory management software primarily stores information such as company network assets in a GIS-based repository."
- FAQ (prioritization + outputs): "You will be able to see **which areas should have a fiber deployment first based on your business case parameters**. You can also use the detailed bill-of-material to order your supplies faster and even send out tenders to construction partners."
- FAQ (alternatives): "rules configurator, which can help you **compare different topologies and see the impact it has on cost**. You can also **run different routing options and find out which is more cost effective**, make design changes quickly based on field survey information."
- FAQ (existing network): "Comsof Fiber is a powerful tool that can utilize existing networks and infrastructure, so it can be used for both **greenfield and brownfield** deployments."
- FAQ (scope): not only FTTH — "single dwelling units, multi-dwelling units, commercial buildings like banks, schools, hospitals, and 5G sites."
- FAQ (inputs): "GIS input data such as street centrelines, homes, and existing infrastructure are an important part of the success of your designs."
- Marketing figures (90% time reduction, 10% cost saving, "150 million homes" designed) — excluded from canonical claims.

### Product B — IQGeo Optimized Planning (use case)

Evidence layer: A.

- Positioning (verbatim): "Optimized fiber network planning — Automated high-level fiber planning for **faster, more confident investment decisions**."
- "Optimized planning automates **high-level fiber planning and feasibility**, enabling you to quickly compare scenarios, estimate costs and make confident investment decisions. By automating scenario modelling, you can… create a strong foundation for **downstream design and rollout**."
- Where planning breaks down (vendor's own framing): "Slow, manual feasibility and planning processes"; "Limited early visibility into cost and build trade-offs"; "Planning outputs that don't flow cleanly into downstream processes."
- Old way vs best practice (verbatim pairs): "Manual, spreadsheet-based feasibility analysis" → "Automated, rules-based high-level planning"; "Static GIS views with limited network insight" → "Fully connected planning model showing how assets connect"; "Limited or no scenario comparison" → "Fast, side-by-side scenario comparison and optimization"; "Uncertain, inconsistent cost assumptions" → "Early, data-driven BOM and cost estimates"; "Planning results disconnected from design workflows" → "**Seamless planning-to-design continuity**."
- What it delivers: "Automated planning and feasibility — Generate optimized high-level fiber plans automatically"; "Scenario comparison and optimization — Evaluate alternative build strategies and routes"; "Early cost and BOM estimation — Produce **order-of-magnitude cost estimates**"; "Connected network planning model — Understand how proposed assets connect"; "Infrastructure reuse and capacity planning — Identify reuse opportunities and plan for growth"; "Scalable planning workflows — Support aggressive rollout targets with small teams."
- Vendor taxonomy: "Optimized Planning" and "Rapid Design" are separate telecom use cases under "Plan & Design" — the planning/design seam is explicit in the vendor's own navigation.

### Product C — 3-GIS | Prospector

Evidence layer: A.

- Positioning (verbatim): "**Turn demand into routes**. 3-GIS | Prospector gives teams a faster way to evaluate fiber opportunities **before detailed design begins**. Use GIS-based routing and cost modeling to compare build scenarios, understand feasibility, and move from demand to direction with confidence."
- "Prospector accelerates fiber opportunity evaluation with GIS data, cost inputs, and routing logic. As an extension of 3-GIS | Web, Prospector generates **route options and budgetary cost estimates** for single-site, multi-site, and large-scale planning scenarios."
- "Know what to build next — Prospector translates raw demand into informed build decisions. Evaluate routes, costs, constraints, and opportunities before committing time and resources to detailed design."
- Capabilities: "Compare build paths — Generate route options based on existing infrastructure, geography, cost inputs, and constraints so teams can compare viable paths earlier"; "Estimate build impact — Produce budgetary cost estimates that help sales, planning, and engineering teams evaluate feasibility before detailed design begins"; "Evaluate at scale — Analyze large opportunities, multi-site requests, and thousands of demand points without manually routing each location one by one"; "Prioritize with confidence — Use route and cost outputs to compare opportunities, focus planning resources, and **decide which builds deserve the next level of attention**."
- Routing intelligence: "Configurable routing inputs — …edge-of-pavement, existing fiber routes, network records, and map-based constraints"; "Cost-aware routing — Factor in cost regions, barriers, and construction constraints to guide routes around higher-cost areas"; "Opportunity intelligence — Apply market, demand, and business data to surface revenue opportunities near planned routes while evaluating paths to priority demand points."
- FAQ (lifecycle position): "Prospector is an extension of 3-GIS | Web that supports the **earliest stage of the network lifecycle**. Once an opportunity moves forward, related planning and design work can continue into the broader 3-GIS environment."
- FAQ (when to use): "when your team needs to evaluate a potential fiber build **before investing deeper planning or engineering effort**. It is especially useful for early feasibility work, competitive bids, multi-location requests, and expansion planning."
- FAQ (audience): "gives sales and sales engineering teams faster access to the planning intelligence needed to qualify opportunities, respond to build requests, and understand whether a location or group of locations is worth pursuing."
- Case study (FiberLight): "machine-prescribed routes and cost estimates in minutes, helping them move viable builds toward the next stage faster"; CTO: "leveraged to drive new revenue and help our sales team leverage existing and upcoming assets."
- Spec sheet: "uses rules-based modeling to generate prescribed fiber routes, estimate costs, compare alternatives, and identify revenue opportunities faster."

### Product D — Infovista VistaPlan / Planet

Evidence layer: A.

- VistaPlan positioning (verbatim): "AI-powered network planning and **investment optimization**"; "Plan smarter investments and design high-performance networks."
- "VistaPlan is Infovista's portfolio for network planning and investment optimization… Whether you're planning 6G, 5G, a combination of multiple technologies, or **optimizing existing infrastructure**, VistaPlan delivers AI-enhanced solutions for RF planning, backhaul design, and geodata management… to help you make **smarter investment decisions** and deliver high-performance networks at optimal cost."
- Why VistaPlan: "CAPEX optimization: Maximize ROI by **incorporating revenue and cost metrics into network design decisions**"; "Backhaul optimization: **Dimension backhaul with least-cost routing, capacity assessments, and fiber vs. microwave analysis**"; "Real-world data integration: Connect plans with reality using crowdsourced data and external insights"; "Precision geodata: Build on an accurate foundation with geodata designed and validated for RF planning."
- Planet (planning engineers, verbatim): "With Planet, planning engineers can deliver higher quality radio network designs within the ever-tighter budgets and shorter deadlines demanded by the business… While comprehensive **what-if scenario planning ensures maximum return on CAPEX investments** and automation of planning tasks increases engineering efficiency, reducing the time-to-market of new designs."
- Planet benefits: "Accelerate your 5G roll-out — With **automatic site selection**, advanced AI-driven propagation modeling, native 3D planning"; "Optimize your network CAPEX return on investment — Determine your optimal network design based on network performance and quality targets as well as **revenue and cost metrics** with Planet ACP."
- Planet use cases: "5G network planning — Make the right design and optimization decisions and transition to 5G faster"; "Network planning in 3D — …3D traffic maps, 3D beamforming analysis and **3D site-selection**"; "Data-driven network planning — combine live network measurements including crowdsourced data, and call traces with predictions, to **connect your plans with reality**"; "ROI focused network planning — Quickly create and evaluate **network upgrade scenarios such as 5G overlay or 4G capacity expansion**. It includes **automated site placement capabilities to perform dimensioning and initial planning of new wireless networks, geographical expansions, or technology overlays like 5G rollout scenarios**. In addition to performance KPIs, Planet ACP can consider **revenue, time-to-market, and total cost of ownership models for a plan that balances ROI and performance**."
- Modules: Planet ACP ("Automate design optimization and 5G site selection"), Planet Crowdsource ("Base planning decisions on real-world data"), Planet AIM (ML propagation), Planet Call Analytics; Ellipse ("Backhaul planning for optimal topology, capacity, and latency"); Geodata ("High-precision digital maps validated for RF planning accuracy"); Smart CAPEX solution ("ROI-enabled ACP workflows supporting time to market and TCO metrics").
- Customer quotes: Ooredoo — "supports Ooredoo Kuwait across our 5G planning and deployment phase allowing us to reduce time to market along with **optimizing our 5G site investment**"; Zain KSA — "Leveraging crowdsourced data… for **traffic map creation**, Infovista Planet helped Zain KSA successfully introduce 5G in new cities"; KDDI — "5G network planning and automation capabilities… complete 3D feature set."
- "Trusted by 400+ MNOs worldwide" — marketing count, excluded from canonical claims.

### Product E — ATDI HTZ Communications (ex ICS telecom)

Evidence layer: A.

- Solution page header: "Radio Network Planning — Network planning & design; Network modelling; Optimisation; Automatic frequency planning; Prospective planning; Propagation model tuning."
- Planning rationale (verbatim): "Radio network operators are passionate about efficiency – getting the maximum return for the minimum outlay. **Planning a network with as few base stations is one way to achieve that.**"
- "Part of radio network planning is modelling. Modelling answers questions like whether a proposed new service can be slotted into a spectrum space without causing interference. Radio network modelling provides answers **before the operator incurs outlay costs** or services suffer as a result of interference."
- "At this stage of network development, it is important to ensure the network is **rolled out faster, performs better and costs are kept to a minimum**."
- "HTZ is a technology-neutral radio propagation software… This powerful RF engineering solution allows planners to **plan, design and optimise** their network."
- Feature list (verbatim): "**Prospective planning** - to identify the best locations for new sites for greenfield and densification scenarios"; "**Coverage studies** - including network coverage, composite coverage, overlapping, best-server and network densification"; "**Traffic analysis** - for ground occupancy, target areas or mesh blocks to cover"; "**Population analysis** - from points, areas by vector polygon imports or raster files"; "**Propagation model tuning** - analyses the correlation between prediction and measurement"; "**Automated frequency assignment and optimisation** - to minimise interference and maximise frequency allocation"; "Migration analysis - from analogue to digital communications"; "Analysis of outdoor to indoor coverage"; "Point to Point network analysis - including path profiles, reliability analysis…".
- Vendor scope note: ICS telecom rebranded to HTZ communications (civil) alongside HTZ Warfare (defence); the ICS prefix remains on spectrum-management products (ICS Manager, ICS RF allocations, ICS monitoring) — spectrum management is a sibling product family, not this sample's center.

### Cross-referenced evidence (from sibling research files)

- **Forsk Atoll** (design pass, 2026-09-10): "a multi-technology wireless network design and optimisation platform… from initial design to densification and optimisation"; also marketed as "radio planning and optimisation software"; ACP/AFP automation; CW/drive-test data and live-network KPIs feeding planning and optimisation. — the wireless pole's planning/design straddle, vendor-labeled.
- **VETRO FiberMap** (design pass): "Generate precise **cost and revenue estimates to invest with confidence**"; Z-Manager demand publishing; roles include Planning ("Design optimal, cost-effective fiber networks"). — demand/investment evidence on the fiber pole.
- **3-GIS FAQ** (design pass, verbatim): "Fiber network planning determines **where fiber should be deployed, what conditions shape the build, and how projects should be prioritized before detailed design begins**." / "Fiber network design **turns deployment plans into constructible, connected network data**." — the canonical vendor-drawn seam.
- **Netadmin** (fiber pass, verbatim): "Netadmin takes over **after the network planning has been made** and hands over to an invoicing platform when it is time for invoicing." — fulfillment is downstream of planning.

## Cross-product Comparison

| Structure | Comsof Fiber | IQGeo Optimized Planning | 3-GIS Prospector | Infovista VistaPlan/Planet | ATDI HTZ | Layer |
|---|---|---|---|---|---|---|
| Demand/coverage grounding (where service is needed vs what exists) | ✔ business case parameters, deployment-area selection, homes/street data | ✔ feasibility against demand; reuse of existing infrastructure | ✔ "turn demand into routes"; thousands of demand points; opportunity intelligence | ✔ traffic maps (crowdsourced), coverage prediction, capacity expansion | ✔ traffic analysis, population analysis, coverage studies | B |
| Existing network as planning context (brownfield/reuse) | ✔ greenfield + brownfield; existing infrastructure | ✔ "Infrastructure reuse… identify reuse opportunities" | ✔ routing inputs include existing fiber routes, network records | ✔ "optimizing existing infrastructure"; 4G capacity expansion | ◐ densification scenarios (existing-network implied) | B |
| Build alternatives generated & compared as scenarios | ✔ scenarios, architectures, topologies, routing options | ✔ side-by-side scenario comparison and optimization | ✔ route options, viable paths compared | ✔ what-if scenarios; upgrade scenarios (5G overlay, capacity expansion) | ✔ prospective planning; best-server/coverage alternatives; AFP | B |
| Quantified outcomes attached to alternatives | ✔ area costs, cost impact of topology/routing choices, BOM | ✔ early BOM and cost estimates; order-of-magnitude costs | ✔ budgetary cost estimates per route | ✔ revenue/cost metrics, CAPEX/ROI/TCO, performance KPIs | ✔ minimum base stations / minimum outlay rationale; interference answers before outlay | B |
| Prioritization / deployment decision as terminal act | ✔ "which areas should have a fiber deployment first" | ✔ "confident investment decisions"; foundation for rollout | ✔ "decide which builds deserve the next level of attention" | ✔ plan that "balances ROI and performance"; site investment optimization | ✔ site location decisions (prospective planning) | B |
| Handoff toward design/construction | ✔ explicit: business case → designs "used to build their network"; BOM for tenders | ✔ "Seamless planning-to-design continuity" | ✔ "before detailed design begins"; continues into 3-GIS environment | ✔ plans feed design/rollout (less explicit wording) | ◐ plan/design/optimise in one tool (straddle) | B (A for IQGeo/3-GIS/Comsof) |
| Geographic/physical working context | ✔ GIS-based (street centrelines, homes) | ✔ (GIS implied; "static GIS views" named as old way) | ✔ GIS-based routing | ✔ geodata, 3D city models, propagation environments | ✔ propagation environment, clutter/buildings models | B |
| High-level network model (how proposed assets connect) | ✔ topologies compared | ✔ "Fully connected planning model showing how assets connect" | ◐ route options (connectivity implied) | ◐ (network design output implied) | ✖ (coverage/interference focus) | B (variant depth) |
| Automation of planning | ✔ design automation, rules configurator | ✔ automated high-level planning | ✔ rules-based route generation | ✔ ACP automated site placement; AFP-class automation | ✔ AFP automatic frequency assignment | B |
| Real-world data feeding plans | ✔ field survey information | ✔ (downstream design correction named) | ◐ (network records as inputs) | ✔ crowdsourced data, call traces | ✔ propagation model tuning vs measurements | B |
| Investment/business-case framing | ✔ "build a better FTTx business case" | ✔ "investment decisions" | ✔ opportunity/revenue intelligence; competitive bids | ✔ investment optimization, Smart CAPEX | ✔ "maximum return for the minimum outlay" | B |
| Sales-engineering / opportunity-qualification audience | ◐ (engineering firms) | ✖ | ✔ explicit (sales + sales engineering) | ✖ | ✖ | A (product-specific pole) |
| Backhaul/transport dimensioning | ✖ | ✖ | ✖ | ✔ Ellipse (topology, capacity, latency; fiber vs microwave) | ◐ P2P link analysis | A (single-product; variant) |
| Spectrum/interference planning face | ✖ | ✖ | ✖ | ◐ (interference via propagation) | ✔ explicit (spectrum space, frequency assignment) | A (pole-defining for HTZ) |

Reading: both poles realize the same three-part structure — **demand/coverage grounding → compared build alternatives with quantified outcomes → prioritized deployment intent feeding design/build** — with **different decision physics**: fiber planning decides on cost/revenue/routing grounds; RF planning decides on coverage/capacity/interference grounds (plus cost). Both converge on investment-grade outputs and a forward handoff. The straddle with design is real and vendor-labeled on both poles.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The demand-and-existing-network picture as the grounding of planning** — the application holds/derives where service is needed (demand points, traffic, coverage/capacity gaps) against the existing network and geography, and planning proposals are justified against this picture.
   - Remove → a cost calculator or scenario tooling with no demand basis; a design tool that engineers whatever it is given.
2. **The evaluated build alternative as the unit of planning work** — deployment options (route/path options, topology/architecture variants, site placements, technology choices) are generated as **comparable scenarios**, each carrying quantified outcomes (order-of-magnitude cost/BOM, revenue/ROI, coverage/capacity gained).
   - Remove → a single-answer sketch (design territory) or an unquantified study; the comparison that justifies the decision disappears.
3. **The investment decision and deployment intent as the terminal output** — alternatives are compared and prioritized into a decision (which areas/sites/builds to pursue, in what order, at what cost and expected return), producing deployment intent that downstream design and construction consume.
   - Remove → analysis with no deployment consequence; "feasibility studies nobody funds."

Jointly-held is load-bearing: 1 alone = a demand/market map (GIS/market analytics); 2 without 1 = generic scenario/optimization machinery; 3 without 1+2 = a budgeting spreadsheet; 1+2 without 3 = studies nobody funds; 1+3 without 2 = decisions without compared alternatives; 2+3 without 1 = costing machinery over no demand.

### L1 — Common Mature Structure

Present in most mature products, not required for recognition:

- geographic/physical working context (map-based routes/sites/demand layers for fiber; terrain/clutter/3D propagation environments for RF)
- a high-level (connected) network model showing how proposed assets connect (fiber pole; RF pole often works through coverage/capacity predictions instead)
- automation of planning: rules-based route generation, automated site placement, automated frequency planning, automated BOM/cost rollups
- real-world data feeding plans: field surveys, crowdsourced data, call traces, drive tests, propagation model tuning against measurements
- infrastructure reuse / brownfield planning alongside greenfield
- scenario libraries, workflow templates, configurable rules/cost inputs
- collaboration across sales/planning/engineering (opportunity qualification pole)
- integration outward: design tools, inventory/plant records, construction/tendering, business systems
- reporting and visualization (maps, coverage plots, cost/BOM reports, business-case outputs)

### L2 — Variant / Optional Structure

- **Domain scope**: fixed-line fiber/copper (demand-routing pole) vs wireless RAN (coverage-site pole) vs backhaul/transport dimensioning (topology, capacity, latency; fiber vs microwave) vs broadcast/public-safety/defence radio — the same Type realized over different network media.
- **Decision physics**: cost/revenue/routing-driven (fiber) vs coverage/capacity/interference-driven (RF) — the deepest structural variant, mirroring the design pass's "two validation physics, one Type."
- **Automation depth**: manual feasibility studies → rules-based generation → automated optimization (site placement, frequency assignment).
- **Who plans**: operator planning teams vs engineering firms/consultancies vs sales engineering (opportunity qualification).
- **Deployment situation**: greenfield vs brownfield/expansion vs densification vs technology overlay (e.g., 5G rollout on 4G).
- **Hosting**: standalone tool vs extension of a plant-record platform vs suite product vs SaaS.
- **Customer tier**: tier-1 MNO / regional ISP / altnet / engineering firm / public safety / defence / regulator.

### L3 — Vendor-specific (research notes only)

- Comsof/IQGeo: "rules configurator"; 90%/10% marketing figures; "150 million homes" claim; acquisition note (Comsof NV acquired by IQGeo, Aug 2022); "Optimized Planning"/"Rapid Design" use-case naming; NetLux AI.
- 3-GIS: Prospector product name; "edge-of-pavement" routing input; FiberLight case study; spec-sheet phrasing; "earliest stage of the network lifecycle" FAQ.
- Infovista: VistaPlan/Planet/VistaPlan Go/Ellipse/Geodata product names; Planet AIM/ACP/Crowdsource/Call Analytics modules; Google propagation API partnership; Smart CAPEX solution name; "400+ MNOs" and "1,000 customers across 130+ countries" marketing counts; "70-80% indoor traffic" vendor claim.
- ATDI: HTZ family naming and ICS→HTZ rebrand; 10KHz–350GHz technology-neutral range; ITU model references; defence/public-safety/broadcast customer set; ICS Manager spectrum-management sibling family.

## Rejected Findings

- **"Planning = GIS."** Rejected: GIS is the common substrate for the fiber pole, but RF planning works in propagation environments, and paper-era planning worked on paper maps. The invariant is the demand-grounded, compared, quantified deployment decision — not a GIS engine.
- **"Planning = design."** Rejected as identity: the vendors themselves draw the seam (Prospector "before detailed design begins"; 3-GIS FAQ planning-vs-design; Comsof FAQ business-case-then-designs; IQGeo separate Optimized Planning vs Rapid Design use cases). But the straddle is heavy and vendor-labeled ("planning & design" solution naming; Atoll self-labels "planning and optimisation"; Planet ACP "automate design optimization"). Held as center-of-gravity, not exclusion.
- **"Planning requires automation/AI."** Rejected: automation depth is a variant axis; manual feasibility studies, paper coverage curves, and spreadsheet business cases satisfy the core (the vendors' own "old way" columns describe exactly this).
- **"Planning is fiber-only."** Rejected: the wireless pole (Planet, HTZ, Atoll) is half the market and structurally identical at the abstracted level.
- **"Planning includes construction management."** Rejected as definitional: tender/BOM outputs touch construction (Comsof "send out tenders"), but the terminal act is the decision and the intent, not the build project.
- **"Planning = live-network capacity management."** Rejected as identity: capacity *expansion* planning is in-scope (Planet "4G capacity expansion"; IQGeo "plan for growth"), but operating live-network capacity (OSS capacity products) was not sampled and is a different lifecycle stage. Scope note recorded.
- Precise numeric claims (90%, 10%, 150M homes, 400+ MNOs, 70-80% indoor, 10KHz–350GHz) — rejected from the final document: marketing figures or vendor specs without operational documentation.

## Boundary Findings

- **vs Telecom Network Design** (pre-held seam, DISCHARGED from this side): the seam is **decision-grade intent vs build-grade artifact**. Vendor-verbatim on both sides: planning "determines where fiber should be deployed, what conditions shape the build, and how projects should be prioritized **before detailed design begins**" (3-GIS FAQ); design "turns deployment plans into **constructible, connected network data**" (same FAQ); Comsof FAQ sequences "build a better FTTx business case and select the deployment areas. Then… create the FTTx designs that will be used to build their network"; IQGeo ships "Optimized Planning" and "Rapid Design" as separate use cases and names the handoff "Seamless planning-to-design continuity"; Prospector "supports the earliest stage of the network lifecycle." The straddle is heavy and product-labeled (Comsof self-labels "planning and design software" and produces detailed BOMs; Planet ACP "automate design optimization"; Atoll self-labels "planning and optimisation" while doing detailed design) — center-of-gravity seam, not exclusion, exactly as the design pass pre-held. Removal tests: remove the decision/comparison layer and keep constructible authoring → design; remove the buildable artifact and keep demand→options→investment → planning.
- **vs Fiber Network Management** (pre-held seam, confirmed): the plant record centers the persistent, connected, geospatial record of the built network; planning centers the act of deciding what to add to it. Planning *consumes* the record as context (Prospector routing inputs include "existing fiber routes, network records"; Comsof "existing infrastructure") and produces proposals that flow into it. Netadmin's scope statement ("takes over after the network planning has been made") locates fulfillment downstream of planning.
- **vs Telecom Inventory Management**: inventory holds the estate of record (equipment/services); planning reads it as context and proposes changes to it. Comsof FAQ draws this boundary explicitly ("Is Comsof Fiber an inventory tool? No.").
- **vs Network Construction Management**: planning output reaches construction as costed intent (BOM, budgetary estimates, tenders); construction centers the build project (schedules, contractors, progress). The tender/BOM surface is the overlap edge.
- **vs Telecom Provisioning Platform**: provisioning activates services on the built network; planning decides what network to build. Downstream neighbor (Netadmin verbatim).
- **vs Mobile Network Management**: live RAN operation (NMS/OSS) vs future RAN planning. Live data flows INTO planning (Planet crowdsourced/call traces; Atoll live KPIs; HTZ measurement tuning) — but operation of the live network is a different Type.
- **vs Telecom Service Assurance**: same data-flow direction (monitoring feeds planning); assurance operates the live network.
- **vs Site Selection Platform (§17)**: cell-site selection is a planning subtask (Planet "3D site-selection"; HTZ "prospective planning… best locations for new sites"), but this Type is the whole deployment decision (demand, alternatives, investment, prioritization), not real-estate site search.
- **vs Utility GIS / Government GIS**: substrate and data models; the planning act sits on top.
- **vs Capacity Management (§14, IT)**: IT capacity management plans IT infrastructure supply; telecom network planning covers the full deployment decision including greenfield and technology choice. Capacity expansion is one scenario class within planning, not the Type.
- **vs Diagramming / CAD / generic analytics**: no demand grounding, no compared alternatives, no investment output → not this Type.

## Historical / Market-Sample Check (§24)

Paper-era telecom planning satisfies the core: demand studies and traffic forecasts; coverage curves plotted on paper maps; route studies with cost estimates; five-year capital plans and build/buy decisions; site search files for new base stations. All three legs hold with no software machinery — demand grounding (studies/forecasts), compared alternatives (route studies, option papers), investment decision output (capital plans, prioritized programs). The vendors' own "old way" columns (IQGeo: "manual, spreadsheet-based feasibility analysis"; "static GIS views") name this pre-digital state. Conversely, a modern AI planning tool with no demand grounding, no compared alternatives, and no investment output fails the core. The definition is not over-fitted to the current GIS/cloud/AI implementation.

## Uncertainties

- No Tier-1 help-center documentation reached for any sampled product; all evidence is official product/solution/FAQ pages (same limitation as the sibling telecom passes). Operational specifics (exact object schemas, state vocabularies, cost-model details, numeric limits) are deliberately not asserted in the final document.
- TEOCO (major RAN planning/capacity platform) unreachable (timeouts ×2) — not sampled; the wireless pole rests on Infovista + ATDI primary evidence plus the Atoll cross-reference.
- Ranplan unreachable (525) — indoor wireless planning not directly sampled.
- OSS-side capacity planning (core/transport traffic forecasting, e.g., NetCracker/TEOCO capacity products) not sampled; the documented Type is grounded in access-network deployment planning (fiber + RAN) with backhaul dimensioning as single-product (Ellipse) evidence. Scope note recorded; no claim made about core/transport capacity products.
- Spectrum-management products (ICS Manager family) sit adjacent; only the radio-network-planning face of ATDI was sampled.
- The exact boundary between "planning" and "capacity management of live networks" inside operator OSS suites is recorded as a scope note, not resolved.
- Whether Esri's Telecom Domain Network should read as platform-native variant or competing substrate remains unresolved (carried from the fiber/design passes; same evidence base).

## Final Synthesis

Telecom Network Planning is the operator-side decision application that turns demand into costed, prioritized deployment intent. Its defining core is three jointly-held structures: (1) the **demand-and-existing-network picture** — where service is needed (demand points, traffic, coverage/capacity gaps) against the network that already exists, grounding every proposal; (2) the **evaluated build alternative** — deployment options (routes, topologies/architectures, site placements, technology choices) generated as comparable scenarios, each carrying quantified outcomes (order-of-magnitude cost/BOM, revenue/ROI, coverage/capacity gained); (3) the **investment decision and deployment intent** — alternatives compared and prioritized into a decision that downstream design and construction consume. The Type spans two structural poles — fixed-line planning (cost/revenue/routing physics) and wireless planning (coverage/capacity/interference physics) — that realize the same core with different decision physics. The seam vs Telecom Network Design is decision-grade intent vs build-grade artifact (vendor-verbatim on both sides, heavy product-level straddle held as center of gravity); the seam vs Fiber Network Management is planning-act vs plant-of-record.
