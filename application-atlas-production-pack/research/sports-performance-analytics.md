# Research Notes — Sports Performance Analytics

Research date: 2026-09-09
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1 (internal; not referenced in the final document)

## Research Goal

Understand what "Sports Performance Analytics" is as an Application Type: what the software's world is made of, who operates it, what the defining workflow is, and where its boundaries sit against the neighboring sports-software leaves (Athlete Management System, Fitness Assessment Application, Sports Video Analysis, Tactical Analysis Platform, Sports Scouting Platform, Race Timing System, Wearable Fitness Platform).

This leaf sits in DIRECTORY §28 between "Athlete Management System" and "Sports Video Analysis". Two sibling passes already pointed at it:

- Athlete Management System (processed 2026-09-06): "when it shifts to insight dashboards over data collected elsewhere, it is drifting toward Sports Performance Analytics"; Related-Types table: "insight layer over performance data; does not own program delivery or the managed roster. AMS products embed reporting and often sell analytics separately." The AMS pass also classified Catapult Athlete Monitoring as a monitoring-first boundary data point adjacent to both Types.
- Fitness Assessment Application (processed 2026-09-07): "Sports Performance Analytics | centers analysis of performance data (dashboards, models); here the structured testing event that produces the data is the center."

This pass must ratify or refine those seams from the analytics side.

## Initial Boundary (hypothesis before research)

- Core hypothesis: the Type is the analysis/insight application over measured sports performance data — athlete/team performance measurements are collected (from wearables, tests, matches, manual entry), turned into sport-native metrics, compared across athletes/sessions/time, and surfaced to coaching/performance staff for decisions.
- Likely confusions:
  1. vs Athlete Management System (AMS) — both hold athlete data; AMS owns the programming loop, analytics owns the insight loop.
  2. vs Dashboard Platform / BI — both produce dashboards; analytics has sport-native semantics (athletes, sessions, load, positions, matches).
  3. vs Tactical Analysis Platform / Sports Scouting — match-event analytics products drift toward opposition analysis and recruitment.
  4. vs Sports Video Analysis — data-to-video linkage exists but video editing/review is a different center.
  5. vs Race Timing System — competition timing results are a different object.
  6. vs Wearable Fitness Platform — consumer self-tracking vs staff-facing organizational analysis.

## Research Questions

1. What objects exist inside such a system (athletes, teams, sessions, matches, metrics, dashboards, reports)?
2. Where does the data come from — does the analytics product own collection (devices) or ingest from elsewhere?
3. What does the analysis layer actually compute (load, testing, wellness, match/event metrics) and how are comparisons made (benchmarks, norms, trends, drill-downs)?
4. Who consumes the output, on what surfaces, for which decisions?
5. What is the relationship to the AMS programming loop — do analytics products plan/assign training?
6. How does the match/event-data pole (football analytics) relate — same Type, variant, or neighbor?
7. What rules matter (data quality, role-based visibility, medical privacy walls)?
8. Historical check: do pre-wearable, spreadsheet-era, and regional products satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Pole | Customer tier | Evidence level |
|---|---|---|---|---|
| Vector / OpenField (Athlete Monitoring) | Catapult | wearable-first load analytics (own hardware) | elite pro → high school (Vector Core, Catapult One) | Tier 1 (help center) + Tier 2 (product pages) |
| Signal | Hudl | wearable monitoring analytics, automation + video integration | pro clubs, universities | Tier 2 (product pages) |
| Sonra (Apex 2.0 suite) | STATSports | wearable-first live + post-session analytics | elite/pro teams; individuals (Academy) | Tier 2 (product pages only) |
| My iP (Reporting & Visualizations) | Kitman Labs | enterprise aggregation/analytics layer inside a suite | elite clubs, collegiate, leagues, defense | Tier 2 (product pages) |
| Hudl Statsbomb (IQ platform) | Hudl | match event-data analytics | pro clubs, analysts, data community | Tier 2 (product pages) |

Boundary data points (not primary samples):

- CoachMePlus — self-labels "customizable athlete management system" with a "Data Analysis Suite" (Reports, Dashboards, Leaderboards) module; homepage-level evidence. Demonstrates AMS-embeds-analytics.
- Firstbeat Sports — intended sample (physiology-first team analytics); site is a JavaScript-only SPA, unreachable after two attempts; dropped per source-access rules.

## Sources

Fetched 2026-09-09:

- Catapult — Athlete Monitoring solution page: https://www.catapult.com/solutions/athlete-monitoring
- Catapult Support (help center home): https://support.catapultsports.com/hc/en-us
- Catapult — Vector OpenField Software category: https://support.catapultsports.com/hc/en-us/categories/9489215059983-Vector-OpenField-Software
- Catapult — Console Dashboards & Visual Analytics section: https://support.catapultsports.com/hc/en-us/sections/5857852861967-Console-Dashboards-Visual-Analytics
- Catapult — Console Dashboards article: https://support.catapultsports.com/hc/en-us/articles/360000421735-Console-Dashboards
- Catapult — Athlete Monitoring section (fundamentals): https://support.catapultsports.com/hc/en-us/sections/6084467760271-Athlete-Monitoring
- Hudl Signal product page: https://www.hudl.com/en_gb/products/signal
- Hudl Statsbomb product page: https://www.hudl.com/en_gb/products/statsbomb
- Hudl Statsbomb Analysis & Video Platform page: https://www.hudl.com/en_gb/products/statsbomb/platform
- Kitman Labs iP platform page: https://www.kitmanlabs.com/platform/
- Kitman Labs My iP page: https://www.kitmanlabs.com/platform/sports-analytics-reporting/
- STATSports Sonra page: https://statsports.com/sonra (homepage: https://statsports.com/)
- CoachMePlus homepage: https://coachmeplus.com/

Not reachable: firstbeatsports.com (JS-only SPA, two attempts). STATSports help center not fetched (product-page evidence only). CoachMePlus help center (help.coachmeplus.com) exists but was not fetched; homepage-level evidence only.

## Product Observations

### Catapult — Vector / OpenField (Athlete Monitoring) [Evidence layer A for its own product]

From the help center (Tier 1):

- The software's section structure describes the operational pipeline: Device Management → Running a Live Session (Vector Live) → Data Transfer & Management → Cloud Editor → Console Dashboards & Visual Analytics → Cloud Reporting / Timeline Reporting → Share Centre → Exporting Data; plus Video & Data Import, Parameters, Settings, Multi-User, Catapult Athlete (athlete-facing app), Working Remotely with Individual Athletes.
- Console Dashboards are "a user-determined collection of Console Widgets"; users create, rename, move, delete dashboards and load default or previously created ones. Widget types documented: Table, Line Graph, Bar Chart, Pie Chart, Table of Efforts/Events, Tactical Widget. Interval reports and data graphing are documented operations. Venue mapping (GPS and ClearSky/LPS) is a setup step for positional data.
- "Parameters" is a first-class concept — the metric vocabulary the system computes and reports on.
- The Athlete Monitoring education section frames the domain model: internal vs external load, "What to Measure", "What Can Player Load Tell Me About Athlete Work", "Building a High Performance Model", "Evaluating the Quality of Performance Data". Player Load is a named vendor metric.
- Multi-User and role/permission surfaces exist; Catapult Athlete gives athletes a view (app).
- Catapult sells Athlete Management as a separate product line with a separate support portal (ams.catapultsports.com) — monitoring/analytics and athlete management are distinct products at this vendor.

From product pages (Tier 2):

- Positioning: "Athlete Monitoring and Coaching solutions to optimize performance, reduce risk of injury & improve recovery"; platform promises: manage athlete data with tailored access (individual athletes to entire teams), centralize training sessions/matches/performance data in one hub, track injuries and recovery, evaluate performance and monitor training loads.
- Tier ladder: Vector Pro (elite, indoor/outdoor, LPS, live), Vector Core (smaller organizations), Catapult One (high school/youth, cloud platform for key insights).

### Hudl Signal [Evidence layer A for its own product, product-page level]

- Self-description: "the cloud-based data management and data curation platform that allows you to extract critical insights from athlete monitoring data, faster than ever before."
- Workflow framing: WIMU wearable tracker → Signal (data curation and data analysis) → Sportscode (video analysis integration with physical data); SVIVO provides live tracking insights (real-time metrics, session control, dynamic maps).
- Automation pitch: "fully-automated data uploads, processing, and reporting" replacing manual per-session data processing.
- Dashboard examples published by the vendor: Daily Report, Microcycle Analysis, Drill Analysis, Individual Profile, Longitudinal Analysis — "bespoke and dynamic dashboards that fit the specific performance needs of your team", "smart widgets".
- "Dedicated Club Entity — centralized control of club-wide data"; "Data Management — whether it's a single session or multiple seasons, manage your club data history within one single platform."
- Browser-based, SSO; positions itself as uniting sports-science and video-analysis departments.

### STATSports — Sonra / Apex 2.0 [Evidence layer A for its own product, product-page level only]

- Positioning: "athlete monitoring solution for elite and professional teams"; "Performance powered by data".
- Suite: Apex 2.0 tracker (wearable), Smart Beacon/Dock (data transfer hardware), Sonra software ("performance analysis software"), Sonra Live iPad and Watch apps (real-time monitoring of group and individual loads "to ensure players progress at an optimal effort"), Sonra Cloud (automated uploads, access from tablet/laptop/desktop anywhere).
- Live + post-session data presented as correlated; multi-sport (soccer, American football, rugby, baseball, hockey, GAA); individuals tier (Academy) beside teams tier.

### Kitman Labs — My iP (Reporting & Visualizations) [Evidence layer A for its own product, product-page level]

- Self-description: "personalized reporting and visualization workspace… turns structured data into clear, actionable insights"; "built on the data you already trust" — powered by data flowing through the iP platform (150+ third-party integrations claimed on the platform page — vendor claim).
- Role-based dashboard families documented:
  - Medical: Medical Overview (availability, injuries/illnesses, time-loss, trends), Injury Review (incidence, burden, exposure-adjusted rates), Availability & Time-Loss Trends, Current Injury & Illness Visibility, Medical Patterns in Context (by activity, contact type, surface, competition, weather, athlete group, body area…).
  - Performance: workload breakdown "across sessions, drills, athletes, and groups", training load in game context, team-to-individual drill-down, daily readiness & load response, early risk & imbalance detection.
  - Data Health: athlete record quality (duplicates, missing DOB), game data integrity (duplicate games, calendar integrity), injury data quality, metrics and integration coverage (missing data, outliers).
- User model: "day-to-day users" get ready-to-use dashboards; "advanced users" copy, personalize, and build dashboards; outputs can be explored, compared, personalized, shared, printed, exported.
- Kitman positions the analytics layer as one module of a suite whose other solutions (Performance Medicine, Performance Optimization, Coaching & Development, League Operations) own the operational loops; a separate "Custom Analytics" service sells bespoke data-science projects.

### Hudl Statsbomb (IQ platform) [Evidence layer A for its own product, product-page level]

- Pole: match event-data analytics for football. Data product (event data with player-location data; vendor claims 3,400+ events/match, 190+ competitions) + analysis platform.
- Platform capabilities documented: customizable data visualisations (radars), filters across players/teams/seasons/leagues with event types, in-match timeframes, date ranges; saved/reusable templates; comparison tables; player searches/shortlists; opposition analysis ("160+ insight metrics" — vendor claim); Tactics module (pitch zones, xG customization); player evaluation with proprietary models (xG, OBV, HOPS, Phases of Play, Defensive Responsibility, xPass — vendor-named models); integrated video (Wyscout) linking data insights to clips; AI player summaries (era-current feature).
- Delivery modes: analytics platform, APIs for internal integration, file formats (JSON/XML/CSV) for third-party tools.
- Use cases named by the vendor: player recruitment, opposition scouting, match analysis, performance evaluation.

### CoachMePlus [boundary data point, homepage level]

- Self-labels "a completely customizable athlete management system"; coach side: Coaching Toolkit, Workout Builder, Dashboards, Wellness Questionnaires, Testing, Scheduling; "Data Analysis Suite — customizable Reports, Dashboards, and Leaderboards".
- Confirms the market pattern: AMS products embed analytics as a module; the analytics module is not the product's center.

## Cross-product Comparison

| Dimension | Catapult Vector/OpenField | Hudl Signal | STATSports Sonra | Kitman My iP | Hudl Statsbomb |
|---|---|---|---|---|---|
| Analyzed subject | athletes, groups, sessions | athletes, sessions, drills, club | players, groups, sessions | athletes, teams, games (whole org) | players, teams, matches, leagues |
| Data origin | own wearables (GPS/LPS/HR/inertial) + imports | own wearable (WIMU) + integrations | own wearable (Apex) | ingested from platform solutions + 3rd-party integrations | vendor-collected match event/tracking data |
| Metric layer | Parameters (metric vocabulary), Player Load-class metrics, high-performance models | vendor metrics + widgets | 70+ real-time metrics claim, AI-enhanced | workload, readiness, injury burden, exposure-adjusted rates | xG/OBV/HOPS-class possession-value models |
| Comparison axes | athlete vs group vs session; interval reports | daily → microcycle → longitudinal | live vs post-session; group vs individual | team→individual drill-down; across seasons | player vs player, team vs team, across leagues/seasons |
| Insight surfaces | Console dashboards (widgets), Cloud/Timeline reporting, athlete app | dynamic dashboards (daily/microcycle/drill/profile/longitudinal) | live apps (iPad/watch), cloud analysis | role-based dashboards, share/print/export | analysis platform (radars, filters, templates), video-linked views |
| Live analysis | Vector Live | SVIVO live tracking | Sonra Live apps | real-time snapshots | live data product (separate) |
| Programming loop (plan/assign training) | not the center (separate Athlete Management product) | absent | absent | absent (Performance Optimization solution owns it) | absent |
| Video linkage | Video & Data Import; integrates with its video platform | Sportscode integration | not observed | not observed | integrated Wyscout video |
| Export/integration | Exporting Data, Share Centre | integrations emphasized | cloud access, API-era claims | API, exports | API, JSON/XML/CSV files |

Stable commonalities across all five (Evidence layer B):

1. An analyzed population of identified athletes (plus teams/sessions/competitions as analysis contexts).
2. A corpus of quantified performance measurements bound to that population, accumulating over time.
3. A metric layer: the system computes sport-native metrics/indicators (load, physical outputs, possession-value models, injury burden) rather than only storing raw data.
4. Comparison as the core analytic act: across athletes, groups, sessions/matches, and time (trends, benchmarks, drill-downs).
5. Insight surfaces consumed by staff: dashboards, reports, profiles — role-differentiated, exportable/shareable.
6. The purpose is decision support for coaching/performance staff (training, load, availability, tactics, recruitment) — not data storage and not program delivery.
7. None of the five owns the AMS programming loop (plan → assign → track → adjust as managed work). Where a vendor sells both, they are separate products or separate solutions.

## Canonical Model (synthesis)

```text
L0 — Defining Invariant (all three jointly held)
1. The analyzed performance population
   (identified athletes; teams/sessions/competitions as analysis contexts)
2. The performance measurement corpus
   (quantified performance data bound to that population, accumulating over time;
    device-derived, test-derived, match/event-derived, or manually entered)
3. The analysis → insight loop
   (sport-native metrics computed from the corpus; comparison across athletes,
    groups, sessions/matches, and time; surfaced as dashboards/reports/profiles
    consumed by staff for performance decisions)

Remove 1 → generic BI/dashboard platform over anonymous data
Remove 2 → empty dashboards / a roster with nothing to analyze
Remove 3 → a data archive or device data store; the "analytics" dies
1+2 without 3 → sports data warehouse
1+3 without 2 → dashboards over nothing
2+3 without 1 → device/vendor data store with no analyzed subject
```

L1 — Common Mature Structure (cross-product commonality, not definitional):

- Configurable dashboards with widget libraries (tables, line/bar/pie charts, event tables, pitch/tactical views)
- Role-based views (coach vs sport scientist vs medical vs analyst; day-to-day vs advanced builder users)
- Team → group → individual drill-down; individual performance profiles
- Longitudinal analysis (microcycle → season → multi-season trends)
- Benchmarks/norms and threshold flags; readiness/load-response views
- Export/share/print of reports; scheduled reporting
- Live session monitoring beside post-session analysis
- Multi-source ingestion (device feeds, imports, third-party integrations, APIs)
- Data-quality surfaces (duplicate records, missing data, coverage checks) where aggregation is deep
- Athlete-facing read views (apps) in some products
- Video linkage (data insights attached to clips)

L2 — Variant / Optional Structure:

- Data-source posture: own-hardware wearable pole (Catapult, STATSports, Hudl WIMU) vs platform-agnostic aggregation pole (Kitman My iP) vs match-event-data pole (Statsbomb)
- Customer tier: elite/pro → collegiate → high-school/youth (Catapult One) → tactical/defense (Kitman Defense, CoachMePlus first-responders)
- Sport breadth: multi-sport platforms vs football-specific data products
- Delivery: SaaS analysis platform vs API/file delivery of data + models vs embedded analytics layer inside a suite
- Live monitoring depth: full live session control vs none
- AI/ML layers: injury-risk models, AI player summaries, on-board metric processing (era-current; optional)
- Consumer/individual tier products beside team products (Catapult One, STATSports Academy)

L3 — Vendor-specific (research notes only):

- Catapult: Vector Pro/Core/One tier ladder; ClearSky LPS; venue mapping for GPS/LPS; "Player Load" metric name; Console/OpenField desktop + cloud split; separate Athlete Management product portal.
- Hudl Signal: WIMU/SVIVO/Sportscode integration chain; published dashboard exemplars (Daily Report, Microcycle, Drill, Individual Profile, Longitudinal); "Dedicated Club Entity".
- STATSports: Apex 2.0 hardware suite (Smart Beacon/Dock, conductive vest); Sonra Live iPad/Watch apps; vendor claims (70+ real-time metrics, 1200+ teams, 20+ sports).
- Kitman Labs: iP solution packaging (PM/PO/CD/LO); My iP role-based dashboard families; Data Health dashboards; Risk Advisor add-on; Custom Analytics services; "150+ integrations" claim.
- Hudl Statsbomb: named models (xG, OBV, HOPS, Phases of Play, Defensive Responsibility, xPass); Tactics module; IQ platform; Wyscout video integration; AI Player Summaries; vendor claims (3,400+ events/match, 160+ insight metrics, 190+ competitions).

## Vendor-specific Findings

See L3 above. Additionally:

- The same vendor (Hudl) ships products in two different poles (Signal = athlete monitoring analytics; Statsbomb = match event-data analytics) plus video analysis (Sportscode) — evidence that the market treats these as distinct product categories even inside one vendor.
- Catapult's separate Athlete Monitoring vs Athlete Management support portals are direct vendor-drawn evidence for the analytics/AMS seam.

## Boundary Findings

1. **vs Athlete Management System (AMS)** — ratified from this side. The AMS owns the programming loop (plan → assign → deliver → track → adjust) and the longitudinal preparation record as managed work; the analytics Type owns the measurement corpus and the insight loop and does not assign work. Vendor-drawn seams: Catapult (separate products/portals), Kitman (Performance Optimization solution vs My iP layer), CoachMePlus (AMS with an embedded "Data Analysis Suite"). Remove the programming loop from an AMS and the remainder drifts to this Type; add a programming loop to this Type and it becomes an AMS.
2. **vs Fitness Assessment Application** — ratified. The assessment app owns the structured testing event (protocol → administration → record → interpretation); analytics consumes test results as one input stream among many. A testing-device cloud (e.g., force-plate platforms) sits at the seam: when standardized test administration is the center it is the assessment Type; when the results are one more stream in squad-wide analysis it is this Type.
3. **vs Sports Video Analysis** — video editing/tagging/review is the center there; here video is a linked context for data insights (Signal→Sportscode, Statsbomb→Wyscout). Remove the measurement corpus and analysis loop → video analysis territory.
4. **vs Tactical Analysis Platform** — the match-event pole (Statsbomb's Tactics module, opposition analysis) drifts toward tactical analysis when the center of gravity becomes opposition/tactical content of matches. The seam proposed: tactical analysis centers on match/opposition content; performance analytics centers on athlete/team performance measurement (load, testing, wellness, match output) as one decision picture. Flagged for the Tactical Analysis pass; not resolved unilaterally here.
5. **vs Sports Scouting Platform** — recruitment evaluation of external players (Statsbomb recruitment module, shortlists) drifts toward scouting. Same flag for the Scouting pass.
6. **vs Dashboard Platform / BI (§13)** — generic BI lacks sport-native semantics: the analyzed subjects are athletes/sessions/matches, the metrics are sport-native (load, exposure-adjusted injury rates, possession-value), and the consumers are coaching/performance staff. A BI tool could technically render sports data; the Type is defined by the sport-native data model and decision loop, not by charting.
7. **vs Race Timing System** — competition timing produces official results for events; analytics consumes performance measurements for preparation decisions. Different objects and owners.
8. **vs Wearable Fitness Platform** — consumer self-tracking surfaces center the individual's own data; this Type is staff-facing organizational analysis over a population. Boundary flagged for the Wearable Fitness Platform pass (unprocessed).
9. **vs Athlete Injury / Availability Management** — injury/availability records may feed analytics (injury-burden dashboards in My iP), but the medical episode record and clearance decisions belong to the injury-management Type; analytics only reads them.

## Historical / Market-Sample Check

- Spreadsheet-era load monitoring (a performance staff member's workbook: squad list, per-session GPS/HR numbers, computed weekly ratios, printed comparison charts for coaches) satisfies all three L0 structures with no cloud, no AI, no vendor hardware.
- Early desktop GPS-analysis software of the 2000s (download device → session reports → squad comparison) satisfies the same core.
- Notational/match-statistics analysis predating tracking data satisfies the match pole.
- Conclusion: the definition does not depend on wearables, cloud, AI, or any current data-source fashion. The corpus's origin (device/test/match/manual) is a variant axis, not part of the invariant.

## Uncertainties

1. Firstbeat Sports (physiology-first team analytics) could not be fetched (JS-only SPA); the wearable/physiology monitoring pole is evidenced by Catapult (Tier 1) + Hudl Signal + STATSports (Tier 2), but a fourth independent confirmation is missing.
2. STATSports evidence is product-page level only; its help center was not fetched, so Sonra's operational mechanics (session processing, dashboard building) are unverified and were not asserted.
3. Exact metric vocabularies (named load metrics, specific readiness formulas) were not verified at article level for most products; the final document deliberately describes the metric layer generically.
4. The exact placement of the match-event-data pole relative to Tactical Analysis Platform and Sports Scouting Platform needs the sibling passes; this pass documents the seam and flags it.
5. Whether any pure "analytics-only, no-device, no-suite" vendor (e.g., dashboard specialists for pro clubs) would add a fourth posture — plausible but not verified; Rockdaisy-class vendors have thin official documentation and were not sampled.
6. Athlete-facing views: observed at Catapult (Catapult Athlete app) and implied elsewhere; not confirmed as a cross-product commonality, so held as common-not-definitional with moderate confidence.

## Final Synthesis

Sports Performance Analytics is the staff-facing analysis application over measured sports performance. Its defining core is three jointly-held structures: an analyzed population of identified athletes (with teams/sessions/competitions as analysis contexts), a performance measurement corpus bound to that population and accumulating over time, and an analysis→insight loop that computes sport-native metrics, compares across athletes/groups/sessions/time, and surfaces dashboards/reports/profiles that staff consume to make performance decisions. It is distinguished from the AMS by not owning the programming loop, from the Fitness Assessment Application by not owning the testing event, from video analysis by not owning the video surface, and from generic BI by its sport-native data model and decision loop. The market realizes the Type in three postures — own-hardware wearable analytics, platform-agnostic aggregation layers, and match-event-data analytics — which are variants of one Type, with drift seams toward Tactical Analysis and Sports Scouting flagged for those passes.
