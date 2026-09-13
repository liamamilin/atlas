# Research Notes — Grain Management (§20 Agriculture, Food & Natural Resources)

Research date: 2026-09-08
Slug: grain-management
Methodology: v1.1 (WORKFLOW_v1.1.md, WRITING_GUIDE_v1.1.md)

---

## Research Goal

Understand what "Grain Management" is as an Application Type: what the managed subject is, what the system senses and records, what protective actions it drives, what interfaces users face, and how it differs from the two adjacent §20 leaves — Grain Elevator Management (processed 2026-09-08) and Grain Origination Platform (unprocessed).

Special duty from the grain-elevator-management pass (STATUS.md, Boundary Issues): that pass adopted the working seam "bin/storage monitoring = the physical condition of grain (temperature, moisture, aeration) vs elevator management = bushels as commercial inventory and money" and asked this pass to confirm the seam from this side. It also recorded that GrainChain's Silosys product ("silo inventory") shows a naming collision to be resolved here.

## Initial Boundary

Hypothesis before research:

- Grain Management = software (typically sensor-attached) that watches and protects the physical condition of grain held in storage — temperature, moisture, spoilage risk — and drives conditioning actions (aeration fans, heat).
- Nearest neighbors: Grain Elevator Management (commercial bushels, tickets, settlement, grower money), Grain Origination Platform (grower acquisition / contracting front end), Farm Management Platform (whole-operation record), Agricultural IoT Platform (sensing backbone), Precision Agriculture (field side).
- Expected definitional content: sensed grain condition + spoilage-risk watch + conditioning action loop. Expected NON-definitional: contracts, settlement, tickets (elevator), field/crop-cycle records (farm/crop), generic sensor plumbing (IoT).

## Research Questions

1. What is the core "thing" the system manages — the grain mass, the bin, the inventory, or the money?
2. What physical quantities are sensed, where are sensors located, and how are readings bound to storage units?
3. Is there an action loop (fan/heat control)? Manual, remote, automated — which forms exist?
4. Do these products carry grain-commerce functions (contracts, tickets, settlement, cash bids)? (boundary vs Grain Elevator Management)
5. Do they carry crop-cycle / field functions? (boundary vs Farm/Crop Management)
6. What interfaces exist (web dashboard, mobile app, 3D views, handheld readers, alert channels)?
7. What is the site structure (yard → bin → cable → sensor depth)?
8. What did the analog pre-history look like (probe + chart + manual fan)? (historical check)
9. How is the word "grain management" used by the market — does it also name elevator commerce systems? (naming collision)

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

1. **OPI Systems** (Calgary, Canada; independent specialist, 40+ years, self-described "global leader in grain storage management") — pole: full-automation specialist spanning grower → commercial → dealer channels. Products: BLUE Lite (handheld), EPIQ (remote monitoring), BLUE (smart conditioning / full automation), OMNI cable (3-in-1), temperature cables, CO2 monitoring, ManageGrain.com platform.
2. **Bin-Sense** (Calian Agriculture, Regina, Canada) — pole: wireless-first challenger, farm-focused, tiered lineup Direct (handheld) → Solo (daily) → Live (hourly + remote fan) → Plus (automatic conditioning); cellular; works with existing third-party cables.
3. **AgroLog** (Supertech Agroline ApS, Denmark) — pole: European/industrial silo monitoring (TMS6000/TMS Link/TMS2000/2500, Wireless Sensor Spear), AgroLog Manager software with 3D facility view, aeration control as an add-on, REST API integration.
4. **GSI GrainVue** (GSI / Grain & Protein Technologies) — pole: the world's largest bin manufacturer's own "Grain Management" category (with GSI Connect); strategy-button philosophy (Dry Down / Cool Off / Rehydrate / Maintain); on-farm storage focus.

Rejected / unreachable candidates:

- grainviz.com — redirects to GSI (brand evidently absorbed); not sampled as an independent product.
- intellifarms.com — transport error ×1; abandoned per network rule.
- TSGC (tsgc.com) — not fetched; sample already saturated (stop conditions met).
- GrainChain Silosys — not fetched this pass; referenced via the elevator pass's note (naming collision: "silo inventory" naming).

## Sources

All fetched 2026-09-08 (direct fetches, Tier-1 product/official pages):

- OPI Systems — homepage https://opisystems.com (claims, product lineup, "Inventory Management" feature)
- OPI Systems — "Grain Management" https://opisystems.com/grain-management/ (proactive vs reactive framing; automated fan control; alarms & automated alerts; advanced sensors: temperature, moisture, inventory level, CO2)
- OPI Systems — BLUE Smart Conditioning https://opisystems.com/opi-blue-full-automation/ (EMC science, modes Manual Control / Aeration / Natural Air Drying / Natural Air Drying with Heat, ManageGrain.com dashboard, manual override, fan run-time reduction, multi-site coordination, FAQ)
- Bin-Sense — homepage https://www.binsense.com (lineup framing, testimonial: hot spot a canola bin "couldn't have caught using an old thermometer")
- Bin-Sense — Products https://www.binsense.com/products/ (per-tier features; grain level indicator by yard/bin/grain type; fan controller; installation FAQ: site map, cables anchored to bin floor, dealer training; compatibility with OPI StorMax cables; approximate volume estimation; subscription plan prices)
- AgroLog — homepage https://www.agrolog.com (company framing, product tree incl. Inventory Monitoring / Crop Level Measurement / Weather Station / Aeration Control)
- AgroLog — Software https://www.agrolog.com/agrolog-software (real-time temp/moisture/CO2, 3D visualisation, email alerts, historical charts, multi-facility, REST API, RS485)
- AgroLog — Aeration Control https://www.agrolog.com/aeration-control (weather station + cables + level monitoring integration; target thresholds; single parameter EMC, 29 crops; avoid or add moisture; aeration relays; manual + automated fan control)
- GSI — homepage https://www.grainsystems.com (via grainviz.com redirect; "Grain Management" category = GrainVue + GSI Connect)
- GSI — GrainVue https://www.grainsystems.com/na/en/products/grain-management/grainvue/ (monitors temperature, moisture, inventory; automates fan operation to cool/dry/store/rehydrate; CO2 detection optional with fan control module; strategy modes Dry Down / Cool Off / Rehydrate / Maintain incl. "within 10 degrees" claim; tutorial series listing: Dashboard, Bins List, Bin Details, Settings, How to Read Bin Cables, Alerts, Fan Control Basics, Custom Mode, Drying, Rehydration; 3D bin view; weather station)

Not reached (recorded per source-access limitation rule): vendor help-center/manual PDFs (GSI manuals index, OPI ManageGrain platform page, BinSense support center). No precise operational numbers asserted in the final document beyond fetched marketing/product statements.

---

## Product Observations

### OPI Systems — Key observations (evidence layer A unless noted)

- Self-positioning: "The Global Leader in Grain Storage Management"; tagline "The next level of Grain Management"; 40+ years; 50K+ bins monitored (marketing figures — layer A for the claim's existence, not its accuracy).
- Its "What is Grain Management?" page defines the category as proactive vs "classical reactive grain monitoring": grain temperature + moisture monitoring + automated control; rationale framed as market value ("carrying in-condition grain until the market is profitable").
- Three named pillars on that page: Automated Fan Control (automate conditioning systems; electrical/fumigation/labor savings), Alarms & Automated Alerts (audio, visual, text message or e-mail to internet-connected device), Advanced Sensors (temperature, moisture, inventory level, and CO2; control humidity, aeration and temperature from wireless device/desktop).
- Homepage feature list: Moisture Sensing; Temperature Monitoring ("real-time temperature readings across multiple zones to prevent spoilage and hotspots"); Inventory Management ("know exactly how much grain is in every bin with precise inventory level measurement technology"); Remote Access (cloud-connected mobile); Rugged Design; Grain Conditioning ("automate fans and heaters based on real-time conditions").
- BLUE tier (top): "While monitoring tells you there is a problem, BLUE solves it" — "full autonomous conditioning, acting as a 24/7 grain management operator"; calculates "the exact atmospheric conditions needed to condition grain, preventing over-drying"; user defines a conditioning target, system executes.
- Operational modes documented: Manual Control, Aeration, Natural Air Drying, Natural Air Drying with Heat.
- Automation mechanism: real-time weather data + Equilibrium Moisture Content (EMC) science; fans run "only when ambient conditions are scientifically optimal"; claims of energy savings and shrink reduction by avoiding over-drying.
- Manual override always available; strategy adjustable through the ManageGrain.com dashboard.
- Commercial-scale posture: "coordinate conditioning across massive storage footprints", "multiple sites and high-capacity bins from one central interface"; CO2 monitoring part of "High-Volume Risk Management".
- Channels: For Growers / For Commercial / For Dealers; dealer portal exists; hardware (cables) is part of the system.

### Bin-Sense — Key observations (evidence layer A unless noted)

- Positioning: "Wireless connectivity between you and your stored grain conditions – wherever you are"; "Secure Your Harvest".
- Tiered lineup (one family, ascending capability):
  - Direct: on-site handheld reader, plug into bin cables, Bluetooth to smartphone — the digitized probe.
  - Solo: daily readings, up to 4 temp/moisture cables per bin, battery powered.
  - Live: hourly readings, remote fan control from app/desktop, solar+battery.
  - Plus: automatic aeration fan control ("automatic grain conditioning"), ambient air temp/humidity readings, AC power.
- Sensing: temperature and/or moisture in-grain via cables; moisture cables "also have temperature sensors, performing dual duty"; relative humidity of ambient air at the fan (fan controller has RH sensor).
- Alerts: custom text or email grain condition alerts.
- Site structure: installation creates "your site on our Bin-Sense platform, including a site map"; cables installed at bin roof, anchored to bin floor; devices associated with cables "so that if your grain conditions become a problem, you'll know exactly where to look"; dealer training included. Grain level indicator "by yard, bin, and grain type".
- Volume: FAQ states the system can generate an approximate grain-volume estimate (sensors 4 ft apart vertically indicate contact with grain); explicitly "not precise".
- Connectivity: cellular (per-site Master Unit with SIM); deliberately no Wi-Fi (privacy settings + power constraints); weatherproof to −40 C (vendor claim).
- Ecosystem compatibility: "compatible with OPI StorMax, provided that the OPI cables are not analog" — hardware cross-compatibility between competing vendors' cables.
- Testimonial (layer B signal about the job): spoilage loss motivated adoption; system "caught a canola bin that had a hot spot right in the middle, which we couldn't have caught using an old thermometer."
- Subscription plans exist (Solo $48/yr per device; Live $375/yr per master unit; Plus $600/yr per automation hub — vendor-published prices, kept in research notes only).

### AgroLog — Key observations (evidence layer A unless noted)

- Positioning: "Protecting the World's Harvest"; measures/monitors "temperature, moisture, and CO2 in a variety of crops, including grain and seeds" — from field to storage; company stats (332,000 sensors installed; 9.5M tons monitored — marketing figures).
- AgroLog Manager software: "the core of our Grain Bin Monitoring systems"; real-time monitoring and control of temperature, moisture, and CO2; benefits: intuitive UI; real-time telemetry/monitoring/control 24/7; real-time 3D visualisations "quickly illustrate where problems occur in the silo"; REST interface for third-party integration; email alerts on critical issues; full historical charts; multiple facilities in one dashboard; PC/tablet/phone.
- Companion AgroLog App for farmers; Wireless Sensor Spear — GSM-enabled, moveable, per-spear data on the app (farm-scale, relocatable sensing).
- Hardware catalog: temperature sensor cables, moisture sensor cables, headspace + CO2 sensor, Inventory Monitoring, Crop Level Measurement, Weather Station, hand terminals, handheld TMS2000/2500 readers.
- Aeration Control (software add-on): harnesses data from weather station + temperature & moisture cables + level monitoring; target thresholds for temperature and moisture; controlled with a single parameter EMC; "EMC support for 29 crops"; reacts to temperature changes; can avoid or add moisture; aeration relays enable "both manual and automated control of aeration fans and/or external alarm signals"; customizable threshold alerts.
- Integration: REST API (cloud or on-site), RS485 for sensor lines.

### GSI GrainVue — Key observations (evidence layer A unless noted)

- Context: GSI sells bins/dryers/handling equipment; "Grain Management" is one of its product categories (with Storage, Conditioning, Material Handling) — the software layer over its own storage hardware. Category contents: GSI Connect and GrainVue.
- GrainVue highlights: "Monitors temperature, moisture and inventory"; "Automates fan operation to cool, dry, store or rehydrate"; "Get alerts when potential signs of spoilage are detected."
- Monitoring: up-to-date moisture and temperature data + inventory levels; 24/7; alerts about grain condition "alongside the information they need to correctly set their heaters and fans."
- CO2 detection: elevated CO2 as "an early warning sign of spoilage"; alert on heightened CO2; option requires the fan control module.
- Aeration Management — four named strategy modes:
  - Dry Down: run fans only when outside conditions favorable (natural-air drying; energy saving).
  - Cool Off: automatic night cooling vs manual on/off habit; weather station + parameters.
  - Rehydrate: pull moist air into the bin when outside RH reaches a set point until soybeans reach desired moisture (vendor's worked example: 40,000-bu bin from 10% to 13% target = weight/money gain — vendor math, research notes only).
  - Maintain: slowly warm grain with automated aeration to keep grain temperature within 10 degrees of outside temperature, preventing condensation when storing into summer (vendor-precise number — kept out of final doc).
- Web app structure (from tutorial series): Dashboard; Bins List; Bin Details; Settings; How to Read Bin Cables; Alerts; Fan Control Basics; Custom Mode; Drying; Rehydration. 3D bin view exists.
- Weather station integration; cloud login (connect.grainsystems.com); brochure + selection guide PDFs exist (not fetched).

---

## Cross-product Comparison

| Dimension | OPI | Bin-Sense | AgroLog | GSI GrainVue |
|---|---|---|---|---|
| Managed subject | stored grain condition (temp, moisture) + spoilage risk | same | same | same |
| In-grain sensing | temp/moisture cables, zones | temp/moisture cables (dual-duty moisture cable) | temp + moisture cables, spears | temp/moisture cables |
| Extended sensing | CO2, inventory level, ambient | ambient RH at fan; grain level indicator | CO2 (headspace), level monitoring, weather station | CO2 (optional w/ fan module), inventory levels, weather station |
| Site structure | bins; multi-site commercial | site map; yard → bin → grain type | facilities → silos; multiple facilities per dashboard | bins list; 3D bin view |
| Spoilage-risk watch | alarms: audio/visual/text/email; hotspot prevention ("multiple zones") | custom text/email alerts; hot-spot testimonial | threshold alerts by email; real-time 3D problem location | alerts on potential spoilage signs; CO2 early warning |
| Conditioning response | remote fan on/off (BLUE), automated fans+heaters, EMC + weather | remote fan (Live), automatic conditioning (Plus) | aeration relays; manual + automated; EMC single-parameter | automated strategies: Dry Down / Cool Off / Rehydrate / Maintain; fan control basics + custom mode |
| Explicit theory | EMC + real-time weather; target moisture; anti-over-dry | parameters; "conditions are right" framing | EMC (29 crops); avoid-or-add moisture | weather/RH set points; maintain-temp-near-ambient logic |
| Handheld pole | BLUE Lite | Direct | TMS2000/2500 | — (not observed) |
| History/trends | — (not observed on fetched pages) | — (not observed) | full historical charts | bin detail views (implied; not observed explicitly) |
| Multi-facility | multi-site coordination | multiple sites via master units | multiple facilities in one dashboard | — (not observed) |
| Business-model surface | dealer channel, subscriptions/support | dealer install + annual subscriptions | direct/partner, demo-led | dealer network, bundled with bins |
| Grain-commerce machinery | none observed (marketing references to market value of in-condition grain only) | none | none | none |
| Field/crop-cycle machinery | none | none | "from field to storage" framing only; field sensing = grain analyzers/spears | none |

Layer-B cross-product commonalities (observed in 3–4/4):

1. In-grain temperature + moisture sensing bound to identified bins — 4/4.
2. Ambient/environment sensing (weather station or ambient RH/temp) feeding conditioning decisions — 4/4 (BinSense ambient at fan; OPI weather data; AgroLog weather station; GrainVue weather station).
3. Alerting on out-of-condition grain (threshold-based notifications) — 4/4.
4. Fan/aeration control as the conditioning actuator — 4/4 (tiered: absent in lowest tiers, remote in mid, automated in top).
5. EMC-class decision logic (run fans only when air will improve/maintain condition) — 3/4 explicit (OPI, AgroLog, GrainVue's favorable-conditions framing); BinSense documents parameter-based automatic control without naming EMC.
6. Level/inventory sensing of physical fill — 4/4 offer it (OPI, BinSense level indicator, AgroLog inventory/crop-level, GrainVue inventory) — always physical level, never ownership/settlement.
7. Web dashboard + mobile app + cloud — 4/4.
8. Dealer/installer onboarding and site configuration — 3/4 documented (BinSense installation FAQ; OPI dealer channel; GSI dealer network); AgroLog sells through partners (1169 partners claim).
9. CO2 sensing as spoilage early-warning — 3/4 (OPI, AgroLog, GrainVue-optional).
10. 3D visualization of bin/silo interior — 2/4 (AgroLog, GrainVue) — optional presentation layer.

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small; three jointly-held structures)

1. **Sensed grain condition in identified storage.** The system measures the physical condition of the stored grain mass itself — temperature and moisture at minimum — at points inside the grain, with readings bound to identified storage units (bins/silos) for the purpose of early spoilage detection. Remove → generic facility/weather monitoring, bin-fill inventory tool, or a sensing backbone (Agricultural IoT pattern); the grain as a perishable subject disappears.
2. **The out-of-condition watch.** The system interprets the condition against safe-storage limits and surfaces out-of-condition grain to the user — threshold alerts/notifications are the standard form. Remove → a raw sensor readout (thermometer with a display); the "watch" that justifies the product disappears.
3. **The conditioning response loop over the storage environment.** The system actuates (or directs the actuation of) the storage's conditioning equipment — aeration fans, heat — to bring the grain to and hold it at target condition; realizations range from manual on-site, to remote switch, to automated EMC-class control. Remove → passive monitoring; the "management" in the Type name disappears.

Jointly-held is load-bearing:

- 1+2 without 3 = a passive monitor with alarms (entry tier of real families; below the full Type — the human still does all management).
- 1+3 without 2 = blind fan automation that never looks at the grain.
- 2+3 without 1 = a weather-driven fan timer; no stored-grain subject.
- 1 alone = a thermometer network. 3 alone = fan control hardware. 2 alone = a rules engine with no eyes.

Historical check (per §24): the analog pre-history — perforated temperature cables probed with a thermometer, handheld moisture testers, aeration decision charts, night-time manual fan switching, bin walks — satisfies all three legs at analog level: sensing (probe/meter), watch (chart + judgment + inspection routine), response (hand-switched fans). The handheld readers sold today (BinSense Direct, OPI BLUE Lite, AgroLog TMS2000) are the direct digitization of the probe. EMC, CO2, cellular, 3D views, subscriptions, and AI are era machinery and are NOT in the definition. Regional check: the European industrial-silo pole (AgroLog) and the North American farm pole (BinSense/GSI) satisfy the same three legs; nothing in the definition is region- or crop-specific (AgroLog's 29-crop EMC table is an implementation detail).

Note on monitoring-only products: real families sell monitoring-only tiers (Solo, Direct, EPIQ, TMS without aeration add-on). These are entry tiers of the Type's families — the documented upgrade path (BinSense "Upgradeable to Solo/Live at any time"; OPI "monitoring tells you there is a problem, BLUE solves it"; AgroLog aeration as add-on; GrainVue ships monitoring+automation together) shows the market itself treats the response loop as the completing element. They are recorded as a variant standing between this Type and the pure-sensing IoT pole.

### L1 — Common Mature Structure (very common in current products; not definitional)

- Ambient/external sensing layer: weather station or ambient temp/RH at the fan, feeding conditioning decisions.
- CO2 sensing (headspace or in-bin) as early spoilage indicator.
- Physical grain-level / inventory sensing ("how full is this bin"), including approximate volume estimation.
- Historical trends/charts per bin.
- 3D visualization of the bin/silo and sensor locations.
- Multi-bin/multi-site dashboards (one pane of glass over the whole storage estate).
- Mobile apps (iOS/Android) + cloud web dashboards.
- Custom alert configuration (text/email; thresholds per bin).
- Manual override of automation.
- Third-party cable/hardware compatibility and dealer-installed site configuration.

### L2 — Variant / Optional Structure

- Tiering within one family: handheld → daily wireless → hourly + remote control → full automation (BinSense pattern; OPI BLUE Lite→EPIQ→BLUE mirrors it).
- Automation posture: remote-only control vs strategy-mode automation (dry/cool/rehydrate/maintain) vs single-parameter EMC automation.
- Audience packaging: grower/farm vs commercial facility vs dealer channel; industrial silo plants (elevator storage side) vs on-farm bins.
- OEM-attached (bin manufacturer's own layer: GSI) vs independent specialist (OPI, BinSense, AgroLog).
- Connectivity: cellular vs on-site controller; solar/battery vs AC power.
- Subscription billing per device/hub (BinSense) vs hardware-plus-service (OPI/GSI) — pricing models are vendor-territory.
- Rehydration (adding moisture deliberately for weight/value) as an explicit supported strategy — documented at 2/4 (OPI rehydration trend-search term; GrainVue) — probably common in soybean-growing markets but held as variant.
- Companion moisture meters/analyzers (AgroLog sells standalone meters as a separate line).

### L3 — Vendor-specific (kept out of the final document)

- OPI: brand names BLUE/BLUE Lite/EPIQ/OMNI/ManageGrain.com; "50K+ bins" and "40+ years" claims; StorMax cable line (referenced by BinSense).
- Bin-Sense: Calian ownership; Master Unit/SIM architecture; specific subscription prices ($48 Solo / $375 Live / $600 Plus per year); "compatible with OPI StorMax, not analog"; −40 °C weatherproofing; 4-ft sensor spacing for volume estimation; "Secure Your Harvest" tagline.
- AgroLog: TMS6000/TMS Link/TMS2000/2500 product names; Wireless Sensor Spear; "29 crops" EMC table; RS485 integration; Supertech Agroline identity; 332,000 sensors / 9.5M tons / 1169 partners stats.
- GSI: GrainVue / GSI Connect names; "within 10 degrees" maintain logic; 40,000-bushel soybean worked example with $10.50/bu price; strategy-mode names Dry Down / Cool Off / Rehydrate / Maintain; CO2 requires fan control module; tutorial-series UI vocabulary.

---

## Vendor-specific Findings

- GrainVue's "Maintain" mode includes a precise thermal-delta rule (keep grain within 10 °F... vendor page says "10 degrees" — unit and exact behavior not verified beyond the page) — product-specific.
- BinSense publishes concrete subscription pricing per device class — product-specific, plan-specific.
- AgroLog quantifies EMC crop support (29 crops) — product-specific.
- OPI/GrainVue both sell "rehydration" as a value story (soybean moisture arbitrage) — strongest at GSI with a worked dollar example; treat the money framing as vendor marketing, not canonical.
- Cross-vendor hardware compatibility exists at least BinSense↔OPI (cables) — notable market fact, but ecosystem detail.

## Boundary Findings

1. **vs Grain Elevator Management (§20 sibling, processed)** — seam CONFIRMED from this side, both directions. Elevator L0 (per that pass): ticketed grain movements + settlement money loop with growers + storage-located grain inventory in bushels by commodity (commercial inventory and money). This pass's four samples carry NONE of that machinery: no tickets, no contracts, no grower settlement, no cash bids. Conversely the elevator products do not watch/condition grain condition. The one straddling capability is physical fill-level sensing: this Type's "inventory" = how full the bin is (OPI "inventory level"; GrainVue "inventory levels"; AgroLog Inventory Monitoring; BinSense level indicator) — a sensor reading; the elevator's "bin inventory" = whose bushels, what position, what value. The elevator pass's adopted seam ("physical condition of grain vs bushels as commercial inventory and money") is ratified; the Silosys naming collision noted there is consistent with this side: in this domain "silo/bin inventory" naming usually means level sensing (this Type), while "grain inventory" in elevator accounting means commercial position.
2. **vs Grain Origination Platform (§20 sibling, unprocessed)** — from this side: no offers, contracts, or grower-acquisition machinery in any sample. The only touchpoint is economic framing ("carrying in-condition grain until the market is profitable" — OPI): quality → market value is the *motivation*, not a function. Ratification of the keep-both split is supported from this side but must be ratified by that pass.
3. **vs Farm Management Platform (§20, processed)** — that pass listed Grain Management as a "side or downstream slice the platform consumes". Confirmed: no fields, crops in ground, operations records, or whole-operation scope here; the subject is grain in storage. Consistent with the farm pass's finding.
4. **vs Agricultural IoT Platform (§20, unprocessed)** — sensing hardware alone is not this Type: the defining posture is the protective mission (condition watch + conditioning response), which pure sensing backbones lack. Monitoring-only entry tiers of this Type's families sit exactly on that seam (recorded as variant, not merge).
5. **vs Precision Agriculture / Crop Management** — field-side, pre-harvest; this Type is post-harvest, in-storage. AgroLog's "from field to storage" framing and grain analyzers show vendors straddling, but the storage-condition core is separate.
6. **vs Building Management System (§17 BMS)** — structural analogy only (sense → alarm → actuate environment); different subject (building climate vs stored grain condition) — no product-level overlap observed.
7. **Naming collision (recorded, no directory change)** — market vocabulary "grain management" spans (a) storage-condition monitoring & conditioning systems (this leaf: OPI's and GSI's own category naming) and (b) elevator grain accounting/merchandising software (AGRIS-class, per the elevator pass's naming note). The directory's three-leaf split (Grain Management / Grain Elevator Management / Grain Origination Platform) disambiguates; leaf name retained.

## Uncertainties

- No vendor help-center/manual PDFs were fetched (GSI manuals index, OPI ManageGrain page, BinSense support). UI behaviors beyond tutorial titles and marketing pages are unverified; no precise thresholds, sensor counts, refresh rates, or alert limits asserted in the final document.
- The "within 10 degrees" maintain rule and all vendor dollar figures are vendor-published marketing math — not verified.
- Rehydration support breadth across the market is under-sampled (2/4 explicit) — held as variant.
- Monitoring-only as "entry tier below the full Type" is an inference from upgrade paths and vendor framing (layer B/C), not a documented category statement by any vendor.
- GrainViz (3D moisture mapping, if it still exists as an independent product) was not sampled — its apparent absorption into GSI could not be verified from the redirect alone.
- Whether commercial storage operators use this Type alongside elevator systems in the same facility is implied (OPI "For Commercial") but the co-existence workflow was not documented.

## Final Synthesis

Grain Management is the stored-grain protection system: it senses the condition of grain in identified storage units, watches that condition against safe-storage limits and alerts on out-of-condition grain, and drives the storage's conditioning equipment (aeration/heat) — manually, remotely, or automatically — to bring grain to and hold it at target temperature and moisture until it goes to market. Its L0 is the jointly-held trio: sensed condition (temp+moisture in-grain, bound to bins, for early spoilage detection) + out-of-condition watch + conditioning response loop. Everything else — CO2, level sensing, weather stations, EMC science, 3D views, multi-site dashboards, subscriptions, dealer channels — is common mature structure or variant. The elevator seam holds in both directions: condition (this leaf) vs commerce (elevator leaf); the physical-level sensor is the shared boundary object. The Type's name is confirmed by the market's own category vocabulary (OPI "Grain Management", GSI "Grain Management" category).
