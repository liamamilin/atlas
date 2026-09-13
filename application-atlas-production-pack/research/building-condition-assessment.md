# Research Notes — Building Condition Assessment

## Research Goal

Understand what "Building Condition Assessment" software actually is as an Application Type: what objects it manages, what workflow it drives, who uses it, and where its boundary lies against neighboring facility/construction Types (Building Asset Management, Property Inspection Application, Building Commissioning Platform, CMMS/Building Maintenance Management, Capital Improvement Planning, IWMS, Property Assessment System).

## Initial Boundary

- Directory leaf: §17 Construction, Real Estate & Facilities — "Building Condition Assessment" (between "Building Access & Visitor Management" and "Building Asset Management").
- Working hypothesis: this is the software side of the Facility Condition Assessment (FCA) practice — structured surveys of building systems/components producing condition ratings, deficiencies, photos, repair/replacement cost estimates, and condition indices (FCI-type) that feed capital planning and deferred-maintenance decisions.
- Nearest neighbors flagged up front:
  - Building Asset Management (processed sibling) — continuous care loop vs periodic condition data production.
  - Property Inspection Application (§17, unprocessed) — transaction-driven single-property inspection vs portfolio condition survey.
  - Building Commissioning Platform (processed sibling) — performance verification vs condition survey.
  - Capital Improvement Planning (§24, processed) — downstream consumer of condition/FCI data.
  - Property Assessment System (§24) — tax valuation; "assessment" word overlap only (false friend).

## Research Questions

1. What are the assessed objects? (portfolio → buildings → systems/components; how granular?)
2. What does a condition survey record? (ratings, deficiencies, photos, notes, location, remaining useful life, recommended action)
3. How does field capture work? (mobile/tablet, offline, floor-plan guidance, checklists)
4. How is condition translated into money? (cost data libraries, repair-vs-replace, unit costs)
5. What aggregated outputs exist? (FCI-type indices, deferred-maintenance backlog, multi-year capital plans, funding scenarios, reports)
6. Who are the users and roles? (field assessors, facility managers, capital planners, executives/boards; assessor firms vs owner/operators)
7. How does assessment data stay current? (one-time snapshot vs "living" updates fed by maintenance systems)
8. What delivery models exist? (software-only, service-led, tiered)
9. Where are the boundaries vs neighbors?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| AkitaBox FCA | mid-market FM suite module; dual audience (AEC/facilities-services assessors + owner/operators); "living FCA" philosophy | market representative; strong product-page documentation |
| Intellis FOUNDATION | pure-play FCA + capital planning platform; public-sector/enterprise (K-12, higher ed, government, housing) | pure-play philosophy; module decomposition documented |
| Gordian (Assessments and Capital Planning) | assessment service tiers + RSMeans cost data + cloud platform; the cost-data incumbent | different philosophy: assessment depth as tiered offering; cost-data ownership |
| Brightly Assetic | boundary anchor: Assessments module inside a public-infrastructure asset management suite (AU/regional) | shows the assessment function embedded in the asset-management family; regional variant |

Boundary context reused from prior sibling passes (already documented with their own sources): Brightly Predictor (capital planning companion), AkitaBox Platform/Capital Management (continuous asset record), Building Commissioning Platform research.

## Sources

All fetched 2026-09-06 (Tier 1 — official vendor product/resource pages):

- AkitaBox — FCA Software product page: https://home.akitabox.com/software/akitabox-fca/
- Intellis — homepage: https://www.intellis.io/
- Intellis — FOUNDATION product page: https://www.intellis.io/foundation/
- Gordian — "The Facility Condition Assessment: Gordian's Options for Data Collection": https://www.gordian.com/solutions/facility-condition-assessment/
- Gordian — Assessments and Capital Planning product page: https://www.gordian.com/products/assessment-and-planning/
- Brightly (Siemens) — Assetic product page: https://www.brightlysoftware.com/products/assetic
- Accruent — Products index (market observation): https://www.accruent.com/products

Unreachable / not used:
- Accruent VFA product URLs (404 ×3: /products/vfa-capital-planning, /products/vfa, /products/facility-capital-planning). VFA is absent from Accruent's current product index; Gordian's site login menu links to a "VFA Support Portal" (facility.vfafacility.com). Consolidation observed; corporate details not asserted.
- No vendor help-center / in-product documentation was fetched in this pass (product and resource pages only).

## Product Observations

### AkitaBox FCA (evidence A)

- Positioning: "Fully digital, streamlined facility condition assessment capture"; "the ultimate FCA software for creating and maintaining a living FCA"; "manage the entire FCA process from start to finish" in one tool.
- Four main components: **Capture** (simplifies/standardizes/speeds data collection), **Cost Estimation** (own rates or industry-standard cost data), **Insights** (raw data → live dashboards), **Report Builder** (professional client deliverable, drag-drop, export).
- Field capture: tablet/smartphone app (iOS/Android), **offline capability** ("basements or remote locations"), digital floor plans with asset pins as "step-by-step guide through the facility", location-based notes and photos pinned to floor-plan spots and associated to assets, text recognition from manufacturer tags into data fields, custom data fields.
- Cost estimation: "connected directly to a cost database"; pull cost data while in the platform and associate with the asset; flexible adjustment for building location/complexities; RSMeans database named for the owner/operator DIY path.
- Insights: BI-style dashboards ("how many assets are past their expected life spans", "which equipment will be most expensive to replace"); FCI, renewal costs, condition status "at a glance" (owner framing).
- Two audiences: **AEC & Facilities Services firms** (produce FCA as client deliverable; pricing per seat and by square foot) and **Building Owners & Operators** (in-house or partner-conducted; "living FCA").
- "Living FCA": FCA data connected to AkitaBox Platform (asset & maintenance management) and Capital Management; work orders/inspection results feed back into the data; "no need to start over from scratch re-collecting data for a new FCA"; "quickly resolve issues uncovered in your FCA by scheduling maintenance right from AkitaBox".
- Report Builder: drag-drop data/graphs → professional final report, export; sample FCA report published (observed remaining life chart).
- Industries: healthcare, higher ed, K-12, government, commercial real estate, AEC/facilities services. SOC2 badge.

### Intellis FOUNDATION (evidence A)

- Positioning: "facility condition assessment software and capital planning system"; "Turn facility condition data into a defensible capital plan"; "Assess. Prioritize. Model. Plan. Defend."
- Pipeline framing: "FIELD DATA → CONDITION & RISK → PRIORITIES → FUNDING SCENARIOS → CAPITAL PLAN → EXECUTIVE DECISION"; "from a list of deficiencies to a clear, defensible investment strategy".
- Four modules:
  - **FOUNDATION.Conditions** — standardized field data collection and condition assessments; mobile-enabled inspections "with or without a wi-fi connection"; identify and document deficiencies with digital checklists; real-time reporting; understand "the cause of deferred maintenance and slow backlog accumulation".
  - **FOUNDATION.Needs** — "a living repository of needs for all physical assets"; predict asset lifecycle by extrapolating needs from older condition assessment reports; **automatically estimate cost** of component/equipment repair vs replacement; benchmark with "proven unit cost libraries".
  - **FOUNDATION.Projects** — scoping, prioritizing, forecasting; "automatically scopes, estimates, and schedules projects"; configurable rules (facility priority, component priority, urgency of individual actions); "applies phase duration and cost rules to generate cash flow requirements for each potential project".
  - **FOUNDATION.Plans** — long-range data-driven capital plans "with traceability"; quick generation of repair and renewal plans; integration with enterprise financial systems; documentation "at various detail levels" for stakeholders.
- Benefits list: mobile app for data collection; configurable business rules at each step; useful-life and **deterioration modeling**; traceability from investment to underlying needs; dashboards/reporting "configured for different roles"; cloud-based.
- Key features: capture condition data in the field with mobile-first tools; connect assessment findings directly to capital planning priorities; evaluate "risk, urgency, cost, and impact with transparent business rules"; forecast future capital needs across portfolios/campuses/business units; defensible capital plans for "executive and stakeholder alignment".
- Marketing stats (L3): 110k facilities inspections supported; 300M sq ft inspected annually; $50B in capital planning; 4,600+ sites.
- Clients include engineering firms (WSP, AECOM) and public owners (NYC Health, NYC DDC, NYC DOE) — both assessor-side and owner-side usage. Case studies: "Facilities Condition Assessment System", "City-wide school structural inspection and budget assessment", "Public school asset survey and analysis system".
- Industries: K-12, higher ed, corporate RE, housing, government, engineering, healthcare.

### Gordian — Assessments and Capital Planning (evidence A)

- FCA definition (FAQ): "A Facility Condition Assessment (FCA) is a structured evaluation of a building's components and systems to determine their condition, remaining useful life and estimated cost to repair or replace them. FCAs are commonly used to support budgeting, capital planning and deferred maintenance analysis."
- Four assessment tiers (need-based framing):
  - **FCA+** — project-level detail "to drive execution of work"; documents non-renewal needs: code compliance, life/safety, modernization, resilience; assessors "catalog every building component from the foundation to the roof".
  - **FCA** — building-level detail "to drive capital planning decision"; qualified professionals (engineers/practiced assessors) evaluate major systems for age and condition; systems replacement timing and capital expenditure needs.
  - **Modeled Assessment** — "fast, high level funding decisions across your portfolio"; statistical models, "comprehensive square foot costing and detailed lifecycle models", no site visit; estimates to justify funding and to locate where detailed assessment is needed.
  - **Self-Assessment** — on Gordian Cloud Platform; in-house, for "mature capital planning organizations"; proprietary **Asset Capture** mobile application; built on RSMeans Data; connected to planning/strategy tools.
- Data gathered in an assessment (resource article): functional use; location; number and type of systems (HVAC, gas, flooring); actual age; renovation age; improvement needs; recommended actions (repair or replacement); costs (RSMeans Data); energy use.
- FAQ: data typically collected — building systems, asset age, observed deficiencies, condition ratings, remaining useful life, estimated repair/replacement costs; "often stored in a centralized system for analysis and reporting".
- FAQ: who uses — "public agencies, educational institutions, healthcare organizations and commercial property owners to manage buildings, justify funding requests and make long-term investment decisions".
- RSMeans Data: construction cost database used "to develop cost estimates for facilities, systems, assets and requirements" (marketing figures L3: 92,000+ line items; 30,000+ hours/year validation).
- Asset Capture app: "create a digital record of any facility asset while in the field... capture photos, asset information and link RSMeans Data in a single step"; platform = "single source of truth for all asset data gathered".
- Capital planning: "understand what assets you have and what condition they are in... analyze and prioritize those assets for replacement"; multi-year capital plans; "Building Portfolios" stakeholder process; "Strategic Assessment Insights" — "brings the concepts of financial investment and portfolio-based wealth management to the facilities world".
- FCI: "The Facilities Condition Index (FCI) is an investment compass. It is an unbiased, universally-accepted measure of performance..." (free FCI calculator offered). Formula not stated on fetched pages.
- Add-on assessment services: Life Cycle Assessment, Five-Year Needs Assessment, Due Diligence, Energy Assessment (ASHRAE Level One), Green Assessment, Site Linear Assessments, Accessibility, OSHA, Non-Structural Seismic, Equipment Tagging & Inventory, Data Validation.
- Gordian Cloud Platform: integrates capital planning, estimating, construction procurement; workflows across the building lifecycle.
- Industries: federal, state & local, K-12, higher ed, healthcare, commercial, A/E/C, Canada/UK public sector.
- Login menu includes "VFA Support Portal" (facility.vfafacility.com) — the VFA facility-capital-planning product is still supported in the Gordian ecosystem (market observation; both vendors' careers links point to fortive.com).

### Brightly Assetic (boundary anchor) (evidence A)

- Positioning: cloud-based, end-to-end **asset management** system (public infrastructure focus; AU/NZ lineage; Siemens-owned).
- Intelligent asset register "pre-configured for more than 100 asset classes"; flexible asset hierarchy (group/complex/component/simple).
- **Assessments module**: "capture asset data, as well as photos and other attachments, with permission controls and printing capability. Easily raise work orders if issues are identified during assessments."
- Mobility module: optimized Assets/Maintenance/Assessments for field crews.
- Accounting module: component-level depreciation, written-down value, remaining asset life.
- FAQ: "Assetic provides advanced tools for predictive maintenance, capital planning and detailed asset condition assessments."
- Work management (reactive/proactive/strategic), dashboards, GIS integration.
- Confirms: condition assessment exists as a module inside the asset-management family; the center of gravity there is the asset register + work management, not the assessment deliverable.

### Market observation — Accruent VFA (evidence A, negative)

- Accruent's current product index (fetched 2026-09-06) lists 13 products (EMS, FAMIS 360, Accruent Field, Lucernex, Maintain, Maintenance Connection, Meridian, Observe, RedEye, Siterra, Space Intelligence, Sustain, TMS) — **VFA is not among them**; three VFA URL guesses 404'd.
- Gordian's site links a "VFA Support Portal". Both vendors' career links resolve under fortive.com.
- Interpretation (kept out of the final document): the historical FCA software incumbent has been consolidated/retired from marketing; the category nonetheless remains active via the sampled products. No claims about dates or mechanics.

## Cross-product Comparison

| Finding | AkitaBox FCA | Intellis FOUNDATION | Gordian | Assetic | Layer |
|---|---|---|---|---|---|
| Assessed objects = identified building systems/components records | ✓ (assets pinned to floor plans) | ✓ (physical assets/components) | ✓ (components & systems) | ✓ (asset register, 100+ classes) | B |
| Structured field capture (mobile/tablet, offline-capable) | ✓✓ (Capture app, offline, floor-plan guided) | ✓ (mobile, with/without wi-fi) | ✓ (Asset Capture app) | ✓ (Mobility module) | B |
| Deficiency documentation with photos/notes/location | ✓ (location-pinned notes+photos) | ✓ (digital checklists) | ✓ (observed deficiencies, photos) | ✓ (photos/attachments) | B |
| Condition + remaining useful life per element | ✓ (observed remaining life in reports) | ✓ (useful-life & deterioration modeling) | ✓ (condition, RUL) | ✓ (condition assessments) | B |
| Recommended action: repair vs replace | ✓ | ✓ (auto estimate repair vs replacement) | ✓ (recommended actions) | ✓ (issues → work orders) | B |
| Cost estimation tied to cost-data library | ✓ (integrated cost estimation; RSMeans named) | ✓ (unit cost libraries) | ✓✓ (RSMeans) | – (not observed) | B |
| Aggregated condition index (FCI named) | ✓ (FCI at a glance) | – ("condition & risk" wording) | ✓✓ (FCI calculator, "universally-accepted") | – | B |
| Deferred-maintenance backlog / needs repository | ✓ | ✓✓ (Needs = "living repository") | ✓ (needs baseline) | – | B |
| Multi-year capital plan / funding scenarios | ✓ (capital planning from FCA data) | ✓✓ (Projects+Plans, cash-flow rules, funding scenarios) | ✓✓ (multi-year plans, Building Portfolios) | via companion (not on page) | B |
| Report generation as deliverable | ✓✓ (Report Builder, client deliverable) | ✓ (documentation at detail levels) | ✓ (assessment reports) | ✓ (printing) | B |
| "Living"/continuously refreshed assessment data | ✓✓ ("living FCA" fed by WOs/inspections) | ✓ ("living repository of needs") | ✓ (single source of truth; keep data current) | ✓ (assessments ↔ work orders) | B |
| Assessor-firm audience (consultant deliverable) | ✓✓ (AEC & facilities-services pole, per-seat/per-sq-ft pricing) | ✓ (engineering firms among clients) | ✓ (assessor teams; also self) | – | B |
| Owner/operator audience | ✓ (owner/operator pole) | ✓✓ (facility teams, executives) | ✓✓ (owners) | ✓ (public agencies) | B |
| Assessment-depth tiers (modeled / building / project level) | – | – | ✓✓ (4 named tiers) | – | A (product-specific) |
| Configurable prioritization rules (facility/component priority, urgency) | – | ✓✓ | – (prioritization present, rules depth not observed) | – | A (product-specific) |
| Deterioration/lifecycle prediction modeling | via Capital Management companion | ✓ | ✓ (lifecycle models in Modeled tier) | via Predictor companion | B |
| Raise work orders from assessment findings | ✓ (schedule maintenance from AkitaBox) | – (not observed) | – | ✓✓ | B |
| Energy assessment as scope extension | – | – | ✓ (ASHRAE Level One add-on) | – | A (product-specific) |
| Suite-embedded vs standalone | module of FM suite (Pulse) | standalone platform | platform + services | module of asset-management suite | B |

## Canonical Model (C-layer synthesis)

```text
Building Portfolio (sites → buildings → assessable systems/components)
└── Assessed Element (identified record: system/trade, location, age/renovation age,
│   functional use, expected life)
│   ├── Condition observation (rating, deficiency, photos, notes, location pin,
│   │   remaining useful life, recommended action: repair vs replace)
│   └── Cost translation (repair/replacement estimate from cost data)
└── Quantified condition outcome
    ├── Deferred-maintenance backlog / needs repository
    ├── Condition indices (FCI-style) per building / portfolio
    └── Multi-year capital plan (priorities, funding scenarios, cash flow)
        → reports / funding cases → executive decision
```

### L0 — Defining Invariant (deliberately small)

1. **Assessed building elements** — the portfolio's buildings decomposed into identified, assessable systems/components records.
2. **Structured condition observations** — per-element observed condition captured through a structured survey: ratings/deficiencies with evidence (photos, notes, location) and a recommended action.
3. **Condition-to-cost translation** — observed condition expressed in financial terms (repair/replacement estimates) and aggregated into condition indices / needs backlog that drive capital renewal decisions.

Fails-the-type tests:
- Remove (3) → an inspection/checklist tool (property-inspection territory), not a condition assessment system.
- Remove (2) → a static asset register with condition fields (Building Asset Management territory).
- Remove (1) → a generic survey/audit form tool.

### L1 — Common Mature Structure

- Survey machinery: standardized component taxonomies, checklists/templates, survey project setup, baseline data import.
- Mobile/tablet field capture, offline-capable, photos + notes pinned to locations; floor-plan guidance through the walk-down.
- Cost estimation from industry-standard unit-cost libraries, with location/complexity adjustments.
- Deficiency/needs repository; repair-vs-replace recommendations; remaining-useful-life tracking.
- Aggregated dashboards: condition indices (FCI named by two products), backlog, renewal costs.
- Multi-year capital plans, funding scenarios, prioritization (risk/urgency/cost/impact), cash-flow projection.
- Report generation (executive/board-ready deliverables, export).
- Role separation: field assessor vs planner vs executive; role-configured dashboards/reporting.
- Integration with FM/CMMS/asset-management/financial systems (living data loop).
- Deterioration modeling / lifecycle prediction.

### L2 — Variant / Optional Structure

- Delivery pole: software-only (self-assessment) vs service-led (vendor conducts) vs tiered hybrid (Gordian's four tiers).
- Assessment depth: modeled (no site visit) vs building-level vs project-level (incl. code compliance, life/safety, modernization, resilience).
- Audience pole: assessor firms (FCA as client deliverable) vs owner/operators (in-house program).
- Segment tuning: K-12/higher ed, government (federal/state/local, incl. UK/Canada public sector), healthcare, commercial real estate, public infrastructure.
- Regional vocabulary: US FCI/RSMeans-flavored vs AU/NZ ISO-55000-flavored public-asset vocabulary (Assetic pole); UK "stock condition survey" naming exists in the market (not sampled directly).
- Scope extensions: energy audits (ASHRAE-style), accessibility, seismic, OSHA, due diligence, equipment tagging/inventory, data validation.
- Data currency posture: one-time snapshot survey vs "living" continuously updated assessment.
- Packaging: standalone platform vs module of FM/asset-management suite.
- AI assistance (estimating, insights) — emerging, single-product observations.

### L3 — Vendor-specific (keep out of final doc)

- AkitaBox: module names (Pulse, Capture, FCA, Insights, Report Builder, Platform, Capital Management, Inspections, Connect), text recognition from manufacturer tags, per-seat + per-square-foot pricing, SOC2 badge, McKinstry/Impact DM quotes.
- Intellis: FOUNDATION.Conditions/Needs/Projects/Plans module names, VQS (vendor qualification), marketing stats (110k inspections, 300M sq ft, $50B, 4,600+ sites), client logos (WSP, AECOM, NYC agencies).
- Gordian: tier names (FCA+, Modeled Assessment, Self-Assessment), RSMeans Data (92,000+ line items, 30,000+ hours/year), Asset Capture app name, Building Portfolios, Strategic Assessment Insights, Sightlines, Flash AI Estimating, FCI calculator, add-on service list, VFA Support Portal link.
- Assetic: module names (Assessments, Mobility, Accounting), 100+ asset classes, AU case studies (Victor Harbor, Tasmanian DECYP, Gunnedah).
- Accruent VFA absence from product index; Gordian VFA Support Portal (consolidation observation).

## Vendor-specific Findings

- Gordian's four-tier assessment-depth model (modeled → self → building-level → project-level) — only in-sample instance of depth-as-product-framing; others imply depth choices but don't productize tiers.
- Intellis's configurable business rules at each step (facility priority, component priority, urgency; phase duration/cost rules → cash flow) — deepest prioritization machinery observed; product-specific depth.
- AkitaBox's text recognition from manufacturer tags and per-seat/per-sq-ft pricing — product-specific.
- AkitaBox and Assetic both raise work orders from assessment findings; Intellis/Gordian pages don't show it (likely exists elsewhere; not generalized beyond "common in suite-integrated deployments" — actually keep as observed-in-two, B-layer with caution).
- Gordian's add-on assessment catalog (energy/accessibility/seismic/OSHA/due diligence) — product-specific packaging of adjacent survey scopes.

## Boundary Findings

- **vs Building Asset Management (§17, processed)** — sharpest structural seam. Assessment is periodic data production (condition surveys → indices/needs); asset management maintains the continuous care loop the assessment feeds. AkitaBox literally ships FCA and Platform/Capital Management as separate modules; Assetic embeds Assessments inside the asset-register suite. Test: remove the cost-quantified capital outcome and the survey deliverable → asset register with condition fields; remove the continuous care loop from the asset product → assessment tool.
- **vs Property Inspection Application (§17, unprocessed sibling)** — transaction-driven single-property inspection (buyer/lender due diligence, point-in-time report for a real-estate transaction) vs portfolio condition survey for capital renewal planning. Gordian offers "Due Diligence" as an add-on service — evidence of adjacency. Joint-review flag: the two leaves likely split on purpose (transaction vs capital planning), but the sibling must confirm its own center of gravity.
- **vs Building Commissioning Platform (§17, processed)** — condition assessment surveys what state existing facilities are in; commissioning verifies performance through tests against requirements (sibling research records the same seam from its side: "condition assessment surveys existing condition/facility condition (FCA); retro-Cx verifies performance against requirements through tests").
- **vs CMMS / Building Maintenance Management (§16/§17)** — no work execution here. Assessment findings may raise work orders (AkitaBox, Assetic) but the care loop lives in the maintenance system.
- **vs Capital Improvement Planning (§24, processed)** — CIP is the public-sector capital-program planning/approval process; it consumes this Type's condition indices/needs as input (sibling doc names condition assessments as a planning driver). Downstream consumer, not the same object.
- **vs Facility Management System / IWMS (§17)** — suite whose center is the real-estate/space/lease estate; condition assessment is one feed/module at most.
- **vs Property Assessment System (§24)** — tax valuation of property; "assessment" word overlap only. False friend.
- **vs Construction Quality Management (§17)** — during-construction work compliance vs existing-building condition.
- **vs Building Energy Management (§17) / energy audits** — energy assessment measures consumption/performance; condition assessment measures physical deterioration. Gordian sells energy assessment as an add-on — adjacent scope, different object.
- **vs Environmental Site Assessment (§21)** — contamination due diligence vs physical condition. Different object, both "assessment" words.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products fit the L0? Yes:
- Pre-software FCA practice (paper walk-down surveys with FCI spreadsheets, common in US public facility capital planning since the 1980s–90s) exhibits all three L0 properties: element records, structured condition observations, cost-quantified outcomes.
- UK "stock condition surveys" (regional naming) and Australian public-asset condition surveys (Assetic lineage) fit without US FCI vocabulary — the cost-quantified condition outcome is the invariant, not the FCI label.
- None of the modern implements (mobile offline apps, floor-plan pins, cost-data integrations, dashboards, AI, deterioration modeling) are required by the definition.
No era/vendor over-fit detected. The one caution: don't define the Type by today's "living FCA" posture — the snapshot survey is the older and still-common form.

## Uncertainties

- No help-center/in-product documentation fetched; no field-level record schemas, exact rating scales (e.g., 5-point scales), numeric limits, or default values asserted anywhere.
- FCI formula not verified from fetched sources (Gordian names FCI and calls it "universally-accepted" but doesn't state the formula on fetched pages); final doc mentions FCI as a named index without asserting its formula.
- Exact relationship between VFA and Gordian/Accruent (consolidation mechanics, dates) unverified — kept as market observation only.
- Property Inspection Application sibling unprocessed — boundary flagged for joint review.
- Whether "raising work orders from findings" is universal across the Type: observed in 2 of 4 samples; phrased cautiously in final doc.
- Regional naming breadth (UK "stock condition survey", "property condition assessment" for due diligence) not directly sampled; noted as market vocabulary only.

## Final Synthesis

Building Condition Assessment software is the system of record for **quantified building condition**: it turns walk-down observations of a portfolio's building systems/components into evidence-backed condition records, translates those into repair/replacement costs, aggregates them into condition indices and a deferred-maintenance/needs backlog, and assembles them into defensible, multi-year capital renewal plans and reports. Its center of gravity is the assessment deliverable and the capital decision it supports — not the continuous care loop (Building Asset Management), not work execution (CMMS), not transaction inspection (Property Inspection), and not performance verification (Commissioning). The defining core is small: assessed element records + structured condition observations + condition-to-cost translation. Everything else — mobile capture, cost libraries, dashboards, funding scenarios, living updates, service tiers — is mature structure around that core.
