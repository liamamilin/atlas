# Research Notes — Field Management (Agriculture, §20)

## Research Goal

Understand what a "Field Management" application is as an Application Type in the agriculture family (directory §20, listed between Crop Management and Agronomy Management): what the "field" is as a managed object, what a product centered on it holds and does, who uses it, and where its boundary sits against the surrounding capability-slice Types (Farm Management Platform, Crop Management, Agronomy Management, Soil Management, Irrigation Management, Precision Agriculture Platform, Agricultural GIS) and against the unrelated construction Type with the same name (Construction Field Management, §17, processed 2026-09-07).

## Initial Boundary

Hypothesis before research: in agriculture, a "field" is a demarcated parcel of farmland (also called paddock, block, plot, bed). A Field Management application centers the field itself as a persistent managed asset — the register of fields, their definition (boundaries/area/characteristics), and the history attached to them — in contrast to:

- Farm Management Platform (processed 2026-09-08): centers the whole operation (business, inputs, labor, money, production subjects).
- Crop Management (processed 2026-09-07): centers the crop-season grown on a field.
- Agricultural GIS (processed): centers the georeferenced land base.
- Soil / Irrigation / Nutrient / Crop Protection Management: center single agronomic domains.
- Construction Field Management (§17): name collision only — a construction site-execution system; unrelated.

Two prior passes independently described this leaf's expected center: crop-management's flag — "field management centers the land unit as a persistent asset (boundaries, soil, infrastructure)"; farm-management-platform — directory siblings "center a single subject class (the crop's agronomy, the field's lifecycle)". This pass tests that hypothesis against real products.

## Research Questions

1. How is a field identified and defined in real products (name, boundary, area, hierarchy)?
2. What standing characteristics are held on the field record itself (soil, land class, infrastructure)?
3. Does field identity persist across seasons/years, and how is per-field history accumulated and retrieved?
4. What field-lifecycle operations exist (create, edit boundaries, split/merge, rename, retire/delete)?
5. How do fields relate to the operation (farm/client containers) and to crop seasons/rotations?
6. Which surfaces do users work in (map-first, list-first, record-first)?
7. Who uses these products (operator, agronomist/consultant, dealer, team)?
8. Where is the boundary vs Farm Management, Crop Management, Agricultural GIS, Soil Management, Precision Agriculture?

## Representative Products

Selected for market diversity (different product philosophy, customer level, region, and production system), all with reachable official documentation:

| Product | Philosophy / pole | Customer level & region | Production system |
|---|---|---|---|
| farmOS | open-source record-keeping; explicit data model (assets/logs) | self-hosted / small-to-diverse; global | mixed (land, plants, animals, structures) |
| Climate FieldView | field-centric data platform (boundaries as substrate for data) | row-crop, mid/large; US + international | row crops |
| AgriWebb | grazing/paddock management on a farm map | commercial grazing; AU/NZ/UK/US/ZA | livestock (paddocks) |
| OneSoil | satellite-first field platform, freemium | farmer + agri-service; Europe/global | row crops / arable |
| Agworld | collaborative records & planning with agronomists/retailers | growers + advisors; US/AU/NZ/SA/UK/EU/CA | mixed cropping |

## Sources

Research date: 2026-09-08. All observations below are from directly fetched official pages (Tier 1 help/user documentation where available, Tier 2 product pages otherwise).

- farmOS User Guide — https://farmos.org/guide , https://farmos.org/guide/assets [A]
- Climate FieldView — https://climate.com/ , https://climate.com/en-us/resources/getting-started.html , …/fieldview-101-overview/map-your-fields.html [A]
- AgriWebb — https://www.agriwebb.com/ , https://www.agriwebb.com/solutions/farm-mapping/ , https://help.agriwebb.com/en/ , …/collections/3870497-mapping [A/B]
- OneSoil — https://onesoil.ai/en , https://help.onesoil.ai/en/ , …/collections/2950325-apps-features , …/articles/5235093-how-to-add-fields… , …/articles/5237448-how-to-edit-field-information-and-boundaries [A]
- Agworld — https://www.agworld.com/ [B — product page only; help center not fetched]

Sourcing limitations: Agworld evidence is product-page depth only (marketing-adjacent; behavioral claims below use cross-product support). FieldView's Knowledge Center (support.climate.com) is a JS application and was not article-fetched; FieldView claims rely on the getting-started guide pages. No claims about numeric limits, pricing tiers, or unretrieved modules.

## Product Observations

### farmOS [A — user guide]

- "All the important and valuable things on your farm are represented as 'Assets'… the 'management units' of farmOS… the things of value that you are managing."
- **Land Assets**: "represent the fields, properties, beds, paddocks, etc that are being managed. They can be mapped and arranged hierarchically to make navigation easier, and they can be referenced by Logs to record events, activities, inputs, observations, etc. If you perform soil tests, these can be stored as 'Lab test' Logs associated with land Assets."
- Land assets can be designated as locations; other assets (plants, animals) can be "moved to" them; the location hierarchy is built from parent relationships. Mapping is optional ("can be mapped") — a land asset exists as a record even without geometry.
- Assets can be archived (hidden from lists, retrievable via filters); cloned without their logs; assigned owners.
- Plant Assets are separate from land; seeding/transplanting logs track where plants have been. So the land unit and the crop are distinct records — the field is the standing thing, the crop comes and goes.
- Logs are the events; quantities attach to logs; records are "connected and related" and navigable from the map or from the asset.

### Climate FieldView [A — getting-started guide]

- Onboarding order: Set Up Your Account → **Map Your Fields** → Upload Historical Data → collect/visualize data → prescriptions. "Once you map your field boundaries, you're on your way getting all your data in FieldView."
- Adding a field: click "Add a Field" in the Fields List pane; search by address, zip code, latitude/longitude, or by **CLUs (common land units)** "that will appear as outlined grids of land"; "Provide a Field Name, Client Name, Farm Name and Approximate Area of the field"; select the field, adjust boundaries, save.
- So the field record = named land unit inside a Client → Farm → Field hierarchy, with boundary geometry and area; every subsequent data layer (yield, imagery, scripts, scouting) lands on that field.

### AgriWebb [A/B]

- Positioning: livestock management software; "track your animals, paddocks, and records – all in one place."
- Farm map is the organizing surface ("It all starts with your farm map"); paddocks are clickable map objects: "Click on any map paddock to drill into key insights like grazing days remaining, current mob locations, and **a full history of records related to that paddock**."
- Infrastructure and landmarks are map records: "Track and locate hazards, fences, gates, water tanks and more."
- Paddock usage color-coding with preset categories (Cropping, Hay, Grazing, Withholding); per-paddock layers: feed on offer (kg DM/ha), pasture growth rate, stocking rate, grazing days remaining, days empty, days since last grazed.
- Mob movement by drag-and-drop on the map "automatically re-calculate[s] your stocking rate, animal load and grazing days remaining."
- Farm Map Editor ("Build your farm map on the go"), measurement tool, import/export/print maps; DIY mapping on phone/desktop with import of existing maps. Help-centre structure: "Mapping — Add infrastructure and landmarks to your digital farm map (8 articles)"; "Paddock Records and Grazing Management (21 articles)."
- Offline record keeping documented ("even when you're out of service").

### OneSoil [A — help articles]

- Four ways to add fields: select on map (fields auto-delineated from satellite imagery), draw boundaries point-by-point, upload files with field boundaries, import from John Deere Operations Center. Mobile: draw or select pre-delineated fields; on save, "enter the field name, and specify the crop, variety, and hybrid."
- Field card: rename; **edit field information and boundaries** — move contour points; cut out parts of a field (trees, water); "adjust field boundaries using up-to-date satellite images or index layers like NDVI… to more accurately define the working area."
- Season versioning of geometry: "Field boundaries can only be edited for a single season. If you change the boundaries in the 2024 season, the boundaries will remain the way they were for the 2023 season."
- Field carries crop-rotation history: "'Crop Rotation' section… We recommend adding crops for at least the past two years to improve the calculation accuracy of our tools."
- Upload "a file with field boundaries **and history**" (crops, planting dates, harvest dates, yields). Delete a field exists; compare/sort/group/share fields exists.
- Beyond the field layer the product centers satellite monitoring (NDVI indexes), VRA maps, soil sampling, weather, AI agronomist — the precision/monitoring pole.

### Agworld [B — product page]

- Records are organized per field: the field snapshot shows activities, costs, observations, notes, map directions for "East Field"; "analyze your agronomic and financial performance by crop, farm and field"; field-level multi-year view ("Field 012 Corn — 7 years of records", nitrogen/phosphorus/irrigation per year).
- Agronomists turn "season's plans into individual recommendations", which "become compliant digital records" — advisor-authored plans executed and recorded at field level.
- "Create field plans from a simple rotation all the way up to detailed, field by field, production plans." Standardized data, audit-ready reporting, offline apps, cloud storage.

## Cross-product Comparison

| Dimension | farmOS | FieldView | AgriWebb | OneSoil | Agworld | Evidence |
|---|---|---|---|---|---|---|
| Field as persistent individually identified land record | Land Asset | Field (named) | Paddock | Field | Field | B — all 5 |
| Survives across seasons/years (identity outlasts crops) | yes (land asset stands; plants move) | yes (historical data lands on fields) | yes (paddock history) | yes (season layers on persistent field; rotation history) | yes (7 years of records per field) | B — all 5 |
| Extent/area held on the record | optional mapping (geometry optional) | boundary + approximate area | drawn paddocks on map | boundary geometry + area | field on map/directions | B; drawn geometry 4/5, area near-universal |
| Container above the field | location hierarchy (parent) | Client → Farm → Field | farm → paddocks | flat field list per account (+seasons) | farm → field (operation context) | B — container varies, not uniform |
| Standing land characterization beyond extent | soil tests as logs on land asset; structures/water as assets | (data layers on field, not attribute register) | infrastructure/landmarks (fences, gates, water, hazards); usage categories | soil nutrient/EC data uploadable onto fields | (observations/notes per field) | B — soil/infrastructure common, form varies |
| History attached to the field and retrievable | logs referenced by land asset | per-field data layers incl. historical upload | "full history of records related to that paddock" | rotation history + boundaries-and-history upload | per-field multi-year records | B — all 5 |
| Map as organizing surface | dashboard map, optional | fields list + map | map-first | map-first + fields list | record-first with map | B — common, not universal posture |
| Field lifecycle ops | create, archive, clone, owner | create (CLU/search/draw/adjust), save | map editor, import/export, measure | create (4 ways), rename, edit/cut boundaries, delete | field plans, records | B |
| Season/rotation machinery | plants as time-bounded assets; logs dated | historical data upload | grazing cycles via mob movements | explicit seasons; season-scoped boundary versions | rotation plans; per-year records | B — explicit seasons 1/5, year-dimension all |
| Production-system realization | any (land/beds/paddocks) | row-crop | grazing paddocks | arable | mixed cropping | B — variant axis |
| Advisor/dealer participation | users of the instance | (partner sharing documented elsewhere) | team/advisors (user roles) | agri-service partners | agronomists/retailers first-class | B |
| Per-field financials | no (community modules exist) | (analysis surfaces) | cost of production (livestock) | (not observed) | cost per acre, field totals | C — not definitional |

## Canonical Model

### Level 0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as agricultural field management:

1. **The field register of record** — the operation's agricultural land units (fields, paddocks, blocks, plots, beds) held as persistent, individually identified records whose identity outlasts any season, crop, or year. The field is the standing subject; crops, animals, and activities pass over it. Remove → season-scoped crop records or a monitoring dashboard with no standing land asset (Crop Management / Precision Agriculture territory), or a bare map.
2. **The field's definition and standing characterization** — each field record defines the land unit as a distinct piece of land with an extent (measured area and/or boundary geometry — drawn, imported, auto-delineated, or referenced to cadastral/common land units) and, where kept, standing land characteristics (soil, land class, infrastructure). The conceptual requirement is a defined, distinguishable land unit; the drawn map is the dominant implementation, not the definition. Remove extent/definition → fields degenerate into location tags on generic records (a notes/lists app), not land management.
3. **Field-anchored history accumulation** — records of what happened on and to each field (activities, inputs, observations, outcomes, condition, boundary/attribute changes) attach to the field record and accumulate across seasons as the field's retained history, retrievable per field. Remove → a static digital farm map / land registry — a tool, not management (this is the subtraction the farm-management pass already named: "1 alone = digital farm map/asset register").

Jointly-held is load-bearing:
- 1 alone = a digital farm map / list of field names.
- 1+2 without 3 = a farm-mapping tool (adjacent to Agricultural GIS capabilities).
- 2+3 without 1 = per-season data layers with no persistent land identity (crop-season substrate view).
- 1+3 without 2 = a labeled ledger of location-tagged records.

### Level 1 — Common Mature Structure

- Interactive farm/field map as (usually the) organizing surface; click a field for detail.
- Standing land characteristics: soil data/tests, land class/usage categories.
- Infrastructure/landmark records placed on the map (fences, gates, water points, buildings, hazards).
- Container hierarchy above the field (client/farm → field; parent land hierarchy).
- Field lifecycle operations: create (draw / select pre-delineated / import file / reference CLU), rename, edit boundaries, archive/delete.
- Per-field record families: activities/inputs, observations/scouting, soil tests, harvest/yield outcomes.
- Multi-year per-field view; comparison/sorting/grouping across fields.
- Mobile capture with offline sync; import/export of boundaries and history; sharing with advisors/team.

### Level 2 — Variant / Optional Structure

- Production-system realization: row-crop fields vs grazing paddocks (stocking rate, feed on offer, grazing days) vs horticultural beds.
- Product pole: record-keeping-first (Agworld, farmOS), data-platform-first (FieldView), map/grazing-first (AgriWebb), satellite/monitoring-first (OneSoil) — the last drifts toward Precision Agriculture.
- Boundary acquisition: manual drawing, satellite auto-delineation, cadastral/CLU selection, file import, machinery-platform import.
- Season machinery: explicit season objects and season-scoped boundary versions (one product) vs year-filtered records (most).
- Regional vocabulary and identity substrate: CLU (US), paddock (AU/NZ/UK), parcel/bed; field naming local.
- Advisor/dealer-managed accounts; free vs subscription tiers.

### Level 3 — Vendor-specific (research notes only)

- FieldView Drive hardware, seed/fertility scripts, partner network, bu/ac marketing claims.
- AgriWebb mob-management vs individual-animal-management platforms, Sustainability Program Hub.
- OneSoil AI Agronomist, Global Analytics data products, Planet Labs imagery, QGIS troubleshooting.
- Agworld's Semios Group affiliation, budgeting module, contractor solutions.
- farmOS hosting (Farmier), log/quantity data-model internals, plan modules.

## Historical / Market-Sample Check

Asked: would older, regional, platform-native products still fit the L0?

- The paper-era farm field record book + farm plan/map (numbered fields with acreages, soil notes; per-field yearly entries of crops, manure, lime, drainage work) satisfies all three legs: persistent named land units, defined extent, accumulated per-field history. No GIS, satellites, sensors, cloud, or apps required.
- Regional/traditional practice: UK field-numbering and Australian/NZ paddock maps satisfy the core under local vocabulary; the L0 does not assume any particular terminology.
- A cadastral/LPIS-style parcel register (name + boundary + area, no operator history) satisfies legs 1–2 but not 3 — correctly excluded: that is the land-base pole (Agricultural GIS / government land records), not field management by an operator.
- Conclusion: the L0 does not over-fit the modern satellite/mapping implementation. Drawn boundaries, soil attributes, infrastructure layers, season objects, and cloud sync are deliberately held at L1/L2.

## Vendor-specific Findings

See Level 3 above; none of these entered the canonical model. Additionally: OneSoil's season-scoped boundary versioning is a directly observed but single-product rule; FieldView's CLU-based field selection is US-specific; AgriWebb's auto-recalculation of stocking rate on mob moves is grazing-specific.

## Rejected Findings

- **Soil as definitional**: soil appears in 4/5 samples but in different forms (tests as logs; uploadable layers; none on the record in one) and Soil Management is its own leaf. → L1 characterization, not L0.
- **Drawn boundary/geometry as definitional**: farmOS explicitly makes mapping optional while remaining a land-record system; CLU-selection and area-only realizations exist. → abstracted to "defined land unit with extent", geometry as dominant implementation.
- **Farm/client hierarchy as definitional**: container shapes differ across all five (hierarchy, client-farm-field, flat+seasons). → L1.
- **Infrastructure mapping as definitional**: prominent only in the grazing pole. → L1/L2.
- **Season objects as definitional**: only OneSoil documents explicit seasons; others use years/dated records. → L2.
- **Per-field financials as definitional**: present in Agworld (and grazing cost tools), absent in farmOS core. → Optional.
- **The whole-operation scope (inputs inventory, labor, money, multi-enterprise)**: that is the Farm Management Platform L0; its presence demotes a product to the sibling Type.

## Boundary Findings

1. **vs Farm Management Platform (§20, processed 2026-09-08)** — FMS centers the whole operation (the operation as managed entity: land structure + production subjects + business record loop). Field Management centers the land units themselves. Subtraction: remove the whole-operation business scope (input inventory, labor, finances, multi-enterprise) while keeping the field register + characterization + land history → Field Management remains. Addition: add the operation-as-entity and business loops → FMS. Consistent with the FMS pass: siblings "center a single subject class (… the field's lifecycle)". In practice the field register is the land substrate inside nearly every FMS — the Types differ by center of gravity, not by feature lists.
2. **vs Crop Management (§20, processed 2026-09-07)** — crop-season center vs land-asset center. In Crop Management the field appears as substrate ("an identified field/plot/block for one defined season"); here the field is the subject and its standing characterization (extent, soil, infrastructure) and cross-season land history are the point; crop seasons/rotations appear as one record family among several (or as rotation entries on the field). **This discharges the crop-management pass's joint-review flag from this side: keep-both ratified** with the recorded gradient (remove crop-cycle records → Field Management remains; remove whole-farm business ops → Crop Management remains).
3. **vs Agricultural GIS (§20, processed)** — ag GIS centers the georeferenced land base (spatial layers, analysis); here field geometry is an attribute of the operator's record, not the product's center. Consistent with the ag-GIS pass's row ("Field Management / Agronomy Management | adjacent | center field-level records … their data commonly appears as layers inside an Agricultural GIS"). "Farm mapping" as marketed by sampled vendors is a capability of this Type's map surface, not a separate directory Type.
4. **vs Soil Management (§20, unprocessed)** — soil as the managed subject (tests, amendments, programs) vs the field as subject with soil as one characterization. Soil-test records attach to fields in sampled products (farmOS lab-test logs; OneSoil soil uploads). Joint review flagged for that leaf's pass.
5. **vs Precision Agriculture Platform / Crop Remote Sensing (§20, unprocessed)** — drift zone demonstrated by OneSoil/FieldView: a product whose center is satellite monitoring, indexes, or VRA belongs to those Types even though fields are its substrate. Field Management's center is the register + characterization + history. Flagged for those passes.
6. **vs Agronomy Management (§20, unprocessed)** — recommendations/decision center vs land-asset center; Agworld shows advisors authoring recommendations at field level (collaboration), which is not the same center. Flagged for joint review.
7. **vs Construction Field Management (§17, processed)** — name collision only; a construction site-execution system (day record + field work items). No relationship beyond the word "field".
8. **Taxonomy observation** — Field Management is a thin standalone Type in the market: the L0 structure (field register + characterization + history) ships most often as the land substrate inside Farm Management / Crop Management / Precision products, and mapping-first standalone tools sit close to Agricultural GIS. The leaf is kept (distinct center, confirmed by two prior passes and this one), but this pass records that standalone realization is rare; see Boundary Issues.

## Uncertainties

- Agworld evidence is product-page depth; per-field record mechanics (e.g., how boundary changes are handled) were not directly observed.
- FieldView's Knowledge Center articles were not fetched (JS app); claims limited to the getting-started guide.
- Field split/merge operations are widely expected in the category but were not directly observed in fetched pages (OneSoil's cut-out excision was); no claim made in the final document beyond boundary editing.
- Standalone "field management"-labeled products (e.g., dealer-side tools) were not sampled; the sample intentionally spans product poles that embed the Type's center.
- Whether the taxonomy should eventually subordinate this leaf as the shared land substrate of §20 is a catalog-level question, recorded in Boundary Issues, not decided here.

## Final Synthesis

A Field Management application (agriculture) is the **land-unit system of record for a farming operation**: it holds the operation's fields — paddocks, blocks, plots, beds — as a persistent, individually identified register whose entries outlast every season; it defines each unit as a distinct piece of land with an extent (area and/or boundary, drawn, imported, auto-delineated, or referenced to land units) and, where kept, standing characteristics such as soil and infrastructure; and it accumulates, attached to each field, the history of what happened on and to that land — activities, inputs, observations, outcomes, condition, and changes to the field itself — retrievable per field across years. Mature products wrap this core with an interactive farm map as the organizing surface, soil and land-class data, mapped infrastructure, a farm→field hierarchy, field lifecycle operations (create by draw/select/import, rename, edit boundaries, archive), per-field record families, multi-year and cross-field views, mobile offline capture, and sharing with agronomists and teams. The market realizes the Type in poles — record-keeping-first, data-platform-first, grazing/map-first, satellite/monitoring-first — and the boundary logic is subtraction: remove the whole-operation business scope and Farm Management collapses to this Type; remove the crop-season loop and Crop Management collapses to it; remove the operator history and only the land base (Agricultural GIS) remains; remove the persistent land register and the remaining season/monitoring machinery belongs to Crop Management or Precision Agriculture. The paper farm field book and farm plan satisfy the core unchanged, which is why the definition depends on none of the modern implementation machinery.
