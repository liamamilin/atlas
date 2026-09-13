# Research Notes — Food Cold Chain Management

## Research Goal

Understand "Food Cold Chain Management" (§20 Agriculture, Food & Natural Resources) as an Application Type: what the software's world consists of, who operates it, what the daily loop looks like, what rules/state matter, and where the boundary sits — especially against the processed sibling **cold-chain-transportation-monitoring** (§18, 2026-09-07), which pre-hung a scope flag for this leaf, and against Environmental Monitoring Platform, HACCP Management, Food Safety Management, Food Traceability Platform, and WMS.

## Initial Boundary (hypothesis before research)

- Hypothesis: the Type is the **food operator's own management of temperature integrity across its supply-chain presence** — fixed cold storage (warehouses, walk-ins, display cases), refrigerated equipment, and refrigerated transport legs it uses — with monitoring, excursion response, and food-safety compliance records.
- Expected nearest neighbors: Cold Chain Transportation Monitoring (§18), Environmental Monitoring Platform (§21), HACCP Management / Food Safety Management (§20), Food Traceability Platform (§20), WMS (§10), Industrial IoT Platform (§16).
- Pre-hung obligation from the §18 sibling pass: "food-cold-chain-management owns food-supply-chain-wide scope (production/storage/retail, food-industry semantics) while this Type is the transport leg and cargo-agnostic (pharma/chemicals/floral/organs) — apply the scope test." Discharged in Boundary Findings #1.

## Research Questions

1. What is the managed subject: shipments, fixed storage contexts, equipment, products, or all? How is the operator's "estate" structured (sites, zones, sensors, assets)?
2. What requirements are defined (ranges per zone/product, time-out-of-range rules), and what semantics do excursions have in food contexts?
3. What happens on excursion: alerting, escalation, corrective-action records, product safeguarding, equipment service?
4. What evidence/compliance functions exist (HACCP-style records, inspection readiness, audit trails, data export), and what is the analog ancestor?
5. How do transport legs appear, and how does the market itself draw the facility-vs-transport line?
6. Which capabilities are common but not definitional (multi-sensor arrays, dashboards, predictive maintenance, checklists, analytics)?
7. Where do the boundaries sit vs the neighbors above?

## Representative Products

Selected for market representativeness, documentation reachability, different product philosophies, and different customer levels. The pharma-pole platform vendors (Controlant) were deliberately excluded after root-page verification showed a pharma-only positioning; the §18 sibling pass already covers that pole deeply.

| Product | Pole | Customer level |
|---|---|---|
| Sensitech (Carrier) | incumbent cold-chain visibility vendor; food industry programs across restaurant chains, foodservice distribution, supermarkets, growers, c-stores, food manufacturers; ships **stationary** and **in-transit** monitoring as separate product lines | enterprise |
| Checkit | digital food-safety operations: sensors + mobile checklists + compliance reporting + predictive equipment failure (UK/EU foodservice, retail, care) | mid-market/enterprise sites |
| ComplianceMate (Ladle) | US foodservice chains: continuous temperature monitoring + automated HACCP workflow checklists + hierarchical multi-location views | chain/multi-site foodservice |
| Monnit | horizontal wireless-sensor platform with cold-chain/food-service/commercial-refrigeration application framings; self-serve kits | SMB / single-site up to multi-site |

## Sources

All fetched 2026-09-08:

- Sensitech: https://www.sensitech.com/en/ (root); https://www.sensitech.com/en/industries/food/ ; https://www.sensitech.com/en/industries/food/food-industry-solutions/ ; https://www.sensitech.com/en/products/stm/ (Stationary Temperature Monitoring / ColdStream Site)
- Checkit: https://www.checkit.net/ (root); https://www.checkit.net/solutions/food-safety
- ComplianceMate / Ladle: https://www.compliancemate.com/ (redirects to Ladle); https://ladle.com/solutions/continuous-temperature-monitoring/ ; https://ladle.com/solutions/operational-food-safety-checklists/
- Monnit: https://monnit.com/ (root); https://monnit.com/applications/ ; https://monnit.com/applications/cold-chain-monitoring/
- Sibling research for boundary alignment: research/cold-chain-transportation-monitoring.md (fetched 2026-09-07 by the sibling pass)

## Product Observations

### Sensitech (evidence layer A — direct, official pages)

- **Food industry framing is end-to-end**: "Ensure product quality and integrity from source to store"; segments served: Restaurants ("maintain high standards for food quality—both in-transit and in-store—while ensuring suppliers are performing to established service levels"), Food Service distributors, Supermarkets ("reduce labor and costs, and minimize food waste"), Growers ("field to the consumer"), Convenience Stores, Food Manufacturers ("from the production plant through to the customer and the consumer").
- **Facility vs transport is a product-line split**: "Stationary Temperature Monitoring" (ColdStream Site, SmartMonitor Site, Fridge-tag loggers) vs "In-Transit Monitoring Software" + TempTale GEO (real-time temp + location) + SensiWatch platform.
- **Stationary monitoring definition (own FAQ)**: "ensures that temperature and humidity of a storage facility falls in a specified range. Products, such as produce and medication, need to maintain a specific temperature range to ensure efficacy and safety."
- **ColdStream Site attributes**: real-time web-based monitoring which "alerts designated personnel when an issue has occurred"; "live data history for the duration of the initial contract"; "eliminates time consuming and inaccurate paper record keeping"; 24x7 browser access; sensors include Temperature, Humidity, Cryogenic, Door Ajar; compliance built (21 CFR Part 11 for pharma grade; separate **Food datasheet** exists).
- **Thermal mapping**: own FAQ recommends "a thermal mapping study … to identify risk areas, since temperature is never consistent in a warehouse or storage facility"; monitors placed at risk areas.
- **Rationale framing (own FAQ)**: "If food is not stored properly, it may reduce shelf life and quality or become dangerous for consumption."
- Professional Services team "harnesses real-time and historic temperature and location monitoring data to drive continuous improvement."

### Checkit (evidence layer A — direct, official pages)

- **Food-safety solution framing**: "Automate temperature monitoring of your critical freezers and fridges, digitize compliance reporting and safety workflows"; "Gain real-time visibility and control over critical assets and operational tasks."
- **Solution anatomy**: 🌡️ "Temperature monitoring with industrial-grade sensors (food checks, fridge/freezer temp automated logging)"; 📋 "Checklists & workflows get digitized and executed in native mobile apps (iOS & Android)"; 📈 "Reporting is simplified by providing one source of the truth, always."
- **Benefits enumerated**: "Automate temp logs — No more manual or paper-based process for logging fridge and freezer temps"; "Ensure compliance — See what has happened, by who, and when, at scale"; "Prevent operational waste — Reduce wasted time, energy, resources, money."
- **Challenge framing**: "managing critical control points, maintaining accurate records, and ensuring consistent team adherence becomes a daily challenge"; spoilage named as the cost.
- **Equipment prediction**: "Asset Intelligence™ provides advanced warnings of potential failures" of "freezers and fridges" for "proactive maintenance."
- **Conditions sensed**: temperature, humidity, O2/CO2, ambient, water leaks; "critical environments, such as freezers, cold rooms, and laboratories, stay within safe parameters."
- Industries: Food & Beverage, Coffee Shops & Cafes, Care Homes, Hospitality, Retail + medical/pharma poles (same platform, different verticals — vertical is packaging over one monitoring+checks platform).

### ComplianceMate / Ladle (evidence layer A — direct, official pages)

- **Product identity**: "ComplianceMate offers … automated HACCP workflows and real-time temperature monitoring"; suite: ComplianceMate + MeazureUp (audits) + Storewise (grocery pricing) + TrackAssure under the **Ladle** foodservice/retail platform.
- **CTM (Continuous Temperature Monitoring) page**: "Instant alerts when temperatures fluctuate out of required specifications"; "System visibility with hierarchical views of all locations"; "Ensure every location is maintaining product safety compliance, without having to physically visit"; "Ensure correct temperatures during transportation and delivery of the products"; "Control of Operational and FSQA workflows for complete compliance."
- **HACCP/SOP framing**: "designed to eliminate safety hazards, support your Hazard Analysis Critical Control Point (HACCP) program, and aid you in collecting data in accordance with your standard operating procedure (SOP) documentation."
- **Checklist solution page**: "replace paper logs with mobile-first, digital workflows"; "Ensure every HACCP and temperature-critical task is completed and recorded"; "Digital signatures, photo capture, and timestamps create transparent proof of task completion"; "All checklist data is stored securely … creating a permanent digital trail that simplifies inspections and compliance reviews"; dashboards "highlight missed tasks, incomplete checklists."
- Industries: restaurants, retail, foodservice, healthcare, education, hospitality, travel, corporate dining; grocery & supermarkets, convenience stores.

### Monnit (evidence layer A — direct, official pages)

- **Cold-chain application framing**: "Remotely monitor food and drug temperatures from production to pallets, reefers to retailers"; "A 2-degree change can ruin a shipment. Instant Monnit real-time alerts help you catch and prevent spoilage."
- **Sensor line for cold chain**: low temperature (−200 °C to 0 °C), digital temperature (thresholds "modify … to comply with federal regulations"), open/close (cooler/freezer doors), humidity, differential air pressure (freezer ventilation), water detection (melt), AC current meters ("a sharp spike in power draw might be a signal that your cold chain management equipment requires servicing").
- **Loop**: sensors → gateways → iMonnit cloud; "instant alert anytime conditions fall below or exceed predefined thresholds"; notifications via "text, email, or call"; "designate team members and users to receive alerts"; dashboards and mobile apps; data export/API ("get vital insights for prioritizing equipment maintenance").
- **Compliance artifacts**: temperature sensors with "up to 25-month NIST certification"; certified for "Europe's EN12830 cold chain traceability standard"; "deliver accurate reports for food safety monitoring compliance."
- **Positioning honesty**: root page is a *horizontal* remote-monitoring platform (water leak, HVAC, greenhouses, healthcare); cold chain/food service/commercial refrigeration/vaccine monitoring are named applications over the same substrate — strong evidence that the sensing substrate is generic and the Type's identity lives in the food domain framing.

## Cross-product Comparison

| Aspect | Sensitech | Checkit | ComplianceMate (Ladle) | Monnit |
|---|---|---|---|---|
| Monitored unit | storage facility / walk-in; DC; in-transit lines separate | "critical freezers and fridges", cold rooms at sites | coolers/freezers at restaurant/c-store/school sites | coolers, freezers, reefers, production areas (sensor per context) |
| Estate structure | facility + sensor network (network controller + sensors); mapping study | sites + sensors + mobile checklists | locations hierarchy + sensors | sensors/gateways in account; zones by placement |
| Defining condition | temperature (+humidity, door ajar, cryogenic) | temperature (+humidity, O2/CO2, ambient, leak) | temperature ("required specifications") | temperature (+door, humidity, pressure, power, water) |
| Requirement | "specified range" per environment/product | "safe parameters" | "required specifications" (FSQA workflows) | "predefined thresholds", configurable to regulations |
| Excursion handling | "alerts designated personnel when an issue has occurred" | "immediate alerts"; workflows; predictive alerts | "instant alerts"; missed-task dashboards | "text, email, or call"; team/user routing |
| Response/work loop | professional services improvement loop | digitized food-safety checks + workflows | automated HACCP checklists; corrective recording | equipment maintenance prioritization (from data) |
| Record/evidence | live data history; eliminates paper records; compliance built (pharma-grade; food datasheet) | "see what has happened, by who, and when, at scale"; compliance reports | "permanent digital trail"; audit-ready; HACCP records | reports "for food safety monitoring compliance"; NIST/EN12830 certified data |
| Equipment health | (services) | Asset Intelligence failure prediction | (via monitoring + hierarchy) | AC current meter → servicing; maintenance prioritization |
| Transport legs | separate in-transit product lines | not in evidence | "during transportation and delivery of the products" (application claim) | "reefers" monitoring (sensor in truck context) |
| Segment framing | restaurants, foodservice dist., supermarkets, growers, c-stores, food manufacturers | food & beverage, coffee shops, care homes, hospitality, retail | restaurants, retail, foodservice, education, healthcare, travel | cold chain, food service, grocery/c-store, commercial refrigeration |

### Cross-product commonalities (Layer B)

Present in **all four** (defining-core candidates):

1. A **standing set of identified temperature-controlled contexts** belonging to the food operation (storage equipment/rooms/zones; transport contexts where covered), monitored continuously or on schedule — not a one-journey object.
2. A **temperature requirement** (specified range / safe parameters / required specifications / predefined thresholds) configured per context, against which readings are evaluated.
3. **Excursion alerting routed to responsible people** (designated personnel / immediate alerts / instant alerts / text-email-call) when readings leave the requirement.
4. A **retained temperature record** presented as replacement for paper logs and serving food-safety compliance/audit needs (live history; "who did what when"; permanent digital trail; compliance reports).

Present in **three or four** (common mature structure):

- Digital food-safety checklists / workflow tasks (probe checks, line checks) alongside automated sensor logging (Checkit, Ladle; Sensitech's food programs emphasize workflow integration; Monnit exports data for such use).
- Equipment-health signals as early warning (Checkit Asset Intelligence; Monnit current meter; Sensitech services) — "what the machine shows about risk to the food."
- Multi-site / hierarchical views for chains (Ladle, Checkit, Monnit dashboards; Sensitech enterprise programs).
- Multi-sensor conditions beyond temperature: humidity, door events, power, water, pressure.
- Data export / API / integration (Monnit explicit; Sensitech enterprise integration; Ladle platform dashboards).
- Analytics over waste/spoilage/efficiency (Sensitech food pages, Checkit waste prevention, Ladle insights).
- Certification/calibration artifacts for data trust (Monnit NIST/EN12830; Sensitech pharma-grade qualification lines; Checkit ISO/UKAS certifications).

Present in **one or two** (variant/vendor-specific):

- Thermal mapping studies (Sensitech STM FAQ — service framing).
- Predictive failure analytics as a named module (Checkit Asset Intelligence).
- Handheld probe integration with checklists (Ladle ThermoPen imagery; Checkit "food checks").
- 24/7 managed monitoring services (Sensitech professional services).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

```text
The food operation's standing temperature-controlled estate
(storage contexts — cold rooms/walk-ins/fridges/freezers/warehouses —
 and the refrigerated transport contexts it uses)
└── Condition monitoring of each context against a defined temperature requirement
    └── Excursion detection → alert-driven response loop
    └── Retained temperature record serving food-safety compliance and quality decisions
```

Four properties. Remove any one and the product stops being recognizable as this Type:

1. **Standing temperature-controlled estate of a food operation** — the unit of management is the operator's persistent, identified cold contexts (a walk-in, a freezer bank, a distribution-center cold zone, the reefer a chain's products ride in), watched continuously/repeatedly, not a single one-way journey. Remove → asset registry of refrigeration equipment (or, if per-shipment only, §18's transport-monitoring Type).
2. **Monitoring against a defined temperature requirement** — a configured acceptable range per context/product that gives readings meaning. Remove → thermometers/data loggers producing numbers nobody evaluates.
3. **Excursion alerting with a response loop** — out-of-range readings trigger alerts to responsible people and recorded responses (corrective action, equipment service, product safeguarding). Remove → passive logging; the "management" in the Type name disappears.
4. **Retained temperature record as compliance/quality evidence** — the history persists as the operator's record for inspections, audits (HACCP-class programs), claims, and quality decisions, replacing the paper temperature log. Remove → live alerting with no trail; the food-safety function disappears.

**Historical / market-sample check (deliberately applied):** the analog food cold chain satisfies all four legs — a clipboard temperature log taped inside the walk-in (twice-daily readings vs the required range), corrective notes ("called service tech", "product moved to the backup cooler"), the binder kept ready for the health inspector. Mechanical strip-chart recorders in refrigerated warehouses (the Ryan line Sensitech still sells) satisfy. Standalone fridge data loggers with PDF graph reports satisfy. Therefore real-time connectivity, mobile apps, AI failure prediction, multi-sensor arrays, digital checklists, cloud dashboards, and multi-site hierarchies are all **excluded from L0** — they are how modern products realize the invariants, not what makes the Type. The scope test from the sibling pass also passes: the unit here is the food operation's standing estate with food-safety semantics; strip the estate framing down to per-shipment cargo and it becomes §18's Type.

### L1 — Common Mature Structure

Very common in current products; expected by the market; not definitional:

- Wireless sensor networks/gateways and sensor-fleet administration (installation, calibration certificates, battery/health).
- Multi-sensor conditions beyond temperature: humidity, door open/close, power draw, water/defrost, air pressure.
- Live dashboards, mobile apps, and multi-site/hierarchical views for chains and groups.
- Notification routing and escalation to named users/teams; acknowledgment.
- Digital food-safety checklists and task workflows (probe-temperature checks, line checks) integrated with sensor data, with timestamps/photos/signatures.
- Equipment-health alerting and failure prediction feeding maintenance.
- Compliance/audit reporting and exports (inspection-ready records; regulator- or standards-aligned data certification where sold).
- Data export/API and integrations (BMS, ERP, POS-adjacent, BI).
- Analytics: spoilage/waste trends, location comparison, energy signals.
- Managed services: monitoring-response desks, thermal mapping studies, professional services.

### L2 — Variant / Optional Structure

- **Segment pole**: foodservice/restaurant (checklist-heavy, probe temps, line checks) ↔ grocery/c-store (display cases, asset health, labor savings) ↔ food manufacturing/plant (HACCP/CCP depth, GxP-grade tooling reused) ↔ distribution/3PL cold storage (warehouse scale) ↔ grower/field. Same core loop, different weight of checklist vs sensor vs analytics.
- **Transport-leg coverage**: stationary-only vs integrated in-transit monitoring; the market itself splits these into separate product lines (Sensitech STM vs in-transit software), and many food operators buy both from the same vendor.
- **Hardware approach**: fixed wireless sensors vs handheld probe thermometers whose readings are digitized through checklist tasks vs data-logger PDF reports; several products mix all three.
- **Regulatory depth**: food-inspection readiness (restaurant/c-store regimes) vs GxP-grade machinery (21 CFR Part 11-class) sold to food plants sharing pharma tooling.
- **Operating model**: self-serve sensor kits (SMB) vs enterprise programs with professional/managed services.
- **Data ownership/deployment**: vendor cloud vs self-hosted/local; data-export guarantees as a sales point.
- **AI posture**: predictive equipment failure, anomaly detection — era-current layer, present in some products only.

### L3 — Vendor-specific (kept out of the final document)

- Sensitech: ColdStream Site, SmartMonitor Site L, Fridge-tag family, TempTale GEO, SensiWatch, SmartView, Lynx FacTOR (transport-side), thermal-mapping services, Ryan strip-chart heritage, Berlinger line.
- Checkit: Asset Intelligence™ naming; illuminate training; specific certification set (UKAS, ISO 17025/27001/9001).
- Ladle: suite packaging (ComplianceMate + MeazureUp + Storewise + TrackAssure); ThermoPen integration imagery; "FSQA workflows" phrasing.
- Monnit: ALTA / Next / PoE•X sensor lines, iMonnit software, 25-month NIST claim, EN12830 certification, "own your data" positioning.
- Controlant (excluded food-side): Saga devices, Zero-Touch Release — pharma pole, covered by the §18 sibling pass.

## Vendor-specific Findings

(Consolidated L3 — none entered the canonical model.)

- **"Predictive freezer/fridge failure"** (Checkit Asset Intelligence) is a vendor-named module; equipment-health alerting as a general capability is L1, the named predictive product is vendor-specific.
- **Power-draw-as-service-signal** (Monnit AC current meter) is one product's implementation of the equipment-health concern.
- **Suite packaging** (Ladle) and **vertical packaging over one platform** (Checkit food vs medical vs care) are packaging facts, not Type structure.
- **Certification specifics** (NIST 25-month, EN12830, ISO sets) are trust artifacts whose exact forms vary by vendor and region.

## Rejected Findings

- **"The Type is defined by IoT sensors"** — rejected. The analog clipboard log and PDF logger satisfy the defining loop; sensing mechanism is implementation (anti-overfitting, same pattern as the §18 sibling's strip-chart anchor).
- **"Food cold chain management = in-transit shipment monitoring with food flavor"** — rejected. The monitored unit in the food-side products is the standing estate; in-transit is a separate (adjacent) Type and, where the same vendor sells both, a separate product line. This pass discharges the §18 sibling's scope flag in that direction.
- **"The Type requires HACCP certification machinery"** — rejected as definitional. HACCP is the dominant *rationale* and record frame in foodservice products, but the defining loop (estate, requirement, excursion response, retained record) exists in products that never name HACCP (Monnit cold-chain application framing speaks of "federal regulations" and "food safety monitoring compliance" generically).
- **"Multi-sensor breadth (humidity/door/power) is defining"** — rejected. Temperature is the only condition present in every sampled product's core; the rest are common extensions.
- **"Cold chain management includes scheduling procurement/production"** — rejected for this Type. Demand/production/procurement for food operations belong to other Types (Foodservice Distribution, ERP/production planning); no sampled product centers them.

## Boundary Findings

| Neighboring Type | Relationship | Distinction | "Remove what → becomes the other" |
|---|---|---|---|
| Cold Chain Transportation Monitoring (§18, processed) | adjacent sibling; pre-hung scope flag discharged | That Type monitors a **shipment/trip** of temperature-sensitive cargo (cargo-agnostic: pharma/chemicals/floral) with delivery evidence as the payoff; this Type manages the **food operation's standing estate** (fixed cold contexts + the transport legs it uses) with food-safety compliance and daily operations as the payoff. Vendors sell them as separate lines; food operators use both. | Strip the standing-estate framing, keep per-shipment monitoring → §18 Type. Add the estate + food operations → this Type |
| Environmental Monitoring Platform (§21) | substrate cousin | Env-Mon watches fixed facilities generically (labs, data centers, buildings) against environmental tolerances; this Type's requirements, records, and workflow are **food-safety-shaped** (food products, shelf life/spoilage, health-inspector/HACCP records, food operations staff). Sensing hardware is shared territory. | Remove food-safety semantics & the food-estate subject → generic environmental/facility monitoring |
| HACCP Management (§20, unprocessed) | program vs estate | HACCP Management centers the **food-safety program machinery** (hazard analysis, CCP determination across all hazards, verification, audits); temperature is one hazard class (the dominant CCP family). This Type centers the **physical temperature-controlled estate** and its operations; products here *serve* HACCP programs. | Flag for joint review when that leaf processes; remove the program machinery → this Type; remove the estate/condition core → HACCP program software |
| Food Safety Management (§20, unprocessed) | program vs estate (broader) | Food-safety management spans sanitation, hygiene, supplier approval, prerequisite programs; this Type is the temperature-integrity slice operated on physical cold contexts. | Flag for joint review when that leaf processes |
| Food Traceability Platform (§20, unprocessed) | condition vs identity | Traceability follows **lot identity and movement** of products (one-up/one-back, recall); this Type follows **condition integrity** of the contexts/products. Some vendors bundle both in food programs. | Remove condition monitoring, keep lot genealogy → traceability; remove lot identity, keep condition → this Type |
| Warehouse Management System (§10) | co-tenant in the cold warehouse | WMS runs warehouse *operations* (receiving, putaway, picking, inventory); cold chain management watches *condition* of the storage environment and equipment. A refrigerated DC runs both. | Remove condition monitoring → WMS |
| Industrial IoT Platform (§16) / generic sensor monitoring | generic substrate | Monnit evidences the substrate: a horizontal sensor platform *sells* "cold chain monitoring" as an application. The Type is defined by the food-safety subject/loop, not by the sensing machinery. | Remove the food-safety estate/loop → horizontal IoT monitoring |
| CMMS / refrigeration equipment monitoring (equipment-health pole) | equipment vs food | Equipment telematics/compressor health alone watches the machine; the food-experience test (what the food/storage environment experiences vs what the machine experiences) decides. Equipment-health signals stay in this Type when framed as early warning for food risk. | Watch only machine health → CMMS/equipment monitoring |

Boundary verdict: the leaf is a legitimate distinct Type — the food operator's estate-level temperature-integrity management with a food-safety evidence function. No taxonomy conflict with the directory. The two pre-hung/likely seams (transport sibling; HACCP/food-safety program leaves) are recorded for joint review.

## Uncertainties

- **Copeland/Emerson unreachable (403, ×1; consistent with the §18 sibling pass's 403)** — the food-retail refrigeration-equipment pole (supermarket refrigeration racks/cases with connected monitoring) is therefore under-sampled; its shape is inferred from Sensitech's supermarket segment framing and is acknowledged as weaker evidence.
- **Help-center depth**: all four products were evidenced from official product/solution pages, not deep help-center articles (Checkit docs.checkit.net and Monnit support KB exist but were not article-crawled). Operational micro-details (exact alert latencies, retention periods, default thresholds) are deliberately not asserted.
- **Product-disposition depth**: how explicitly products record *food* outcomes of excursions (product moved/discarded vs equipment serviced) varies and was only partially observable (Ladle's checklists record task completion; Sensitech's food material speaks of waste reduction; none of the fetched pages documents a dedicated "product disposition" object). Held at L1 with qualified wording in the final document.
- **Transport-leg integration**: how stationary and in-transit data merge inside one vendor platform (Sensitech) was visible only at product-line level, not at data-model level.
- **Regional products** (UK/EU HACCP-monitoring vendors of the BluLog/Navitas class) were not sampled; their expected fit is through the same four-leg loop (paper-log digitization is their explicit pitch), but this remains unverified by direct fetch.

## Final Synthesis

A Food Cold Chain Management application is the food business's own system for keeping its cold chain cold and *proving* it: it holds the operation's temperature-controlled estate — cold rooms, walk-ins, freezers, display cases, warehouse zones, refrigerated transport it uses — as identified monitored contexts; it watches each against a defined temperature requirement; it turns excursions into alerts and recorded responses; and it retains the temperature history as the audit-ready record that replaces the paper log for inspections, HACCP-class programs, and quality/waste decisions. Everything else in modern products — sensor networks, humidity/door/power sensing, mobile checklists, multi-site dashboards, failure prediction, managed services — is mature implementation mass around that loop. The Type's center of gravity is the **standing food estate**, which separates it from the per-shipment transport-monitoring sibling (§18) and from generic facility monitoring (§21); its program-side neighbors (HACCP/Food Safety Management) own the food-safety machinery this Type feeds; its identity cousins (traceability) own lot genealogy, not condition.
