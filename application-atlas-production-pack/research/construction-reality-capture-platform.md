# Research Notes — Construction Reality Capture Platform

Research date: 2026-09-07
Slug: construction-reality-capture-platform (DIRECTORY §17 Construction, Real Estate & Facilities)

## Research Goal

Understand how real products turn the physical state of a construction site into a structured, dated, spatially organized visual record, and what separates this Application Type from Construction Field Management, Construction Project Management, BIM tools, general photogrammetry applications, and building condition assessment.

## Initial Boundary

Initial hypothesis (before research): these platforms capture the site (360° photo/video, drone imagery, laser scan), auto-organize captures against plans/models/maps, accumulate them as a dated progress record, and let remote stakeholders navigate and compare — distinct from field work-item systems (punch lists/day logs) and from PM systems (schedule/cost/RFI).

Risk of confusion noted up front: the phrase "reality capture" is also used by laser-scanner ecosystems (scan-registration software) and by general photogrammetry tools; fixed construction cameras are a live-monitoring neighbor.

## Research Questions

1. What is the unit of capture (walk / flight / survey / scan session) and what metadata does it carry (project, date, location)?
2. How is capture data spatially organized — floor plans, BIM models, orthomosaics, georeferenced terrain?
3. How does the time dimension work — capture series, date comparison, progress vs plan/schedule?
4. What can users do with captures: navigate, measure, annotate, report, export, share?
5. Who captures, with what hardware; what is the upload→processing→viewable pipeline?
6. How do captures connect to issues/observations and to PM platforms?
7. What access/permission rules, roles, and sharing models exist?
8. Boundary: what makes this not field management / not BIM authoring / not photogrammetry / not construction cameras?

## Representative Products

Selected for market representation, documentation depth, different capture philosophies, and different customer tiers:

| Product | Philosophy | Capture emphasis | Customer tier |
|---|---|---|---|
| OpenSpace | capture-first 360° documentation, "Visual Intelligence Platform" (Capture / Coordinate / Act) | 360° video walks + phone + drone + laser scan; outsourced Walk Services | GCs/trades/owners; SMB→enterprise |
| Reconstruct | multi-modal reality mapping fused with design + schedule ("remote quality control, progress monitoring") | any-device photo/video → measurable 2D/3D; 4D BIM | enterprise; owners/GCs; infrastructure/hospitals/airports |
| Buildots | AI progress intelligence ("construction intelligence platform") | 360 cameras/drones/laser scans; fully managed Capture Services | enterprise GCs/owners/CM (data centers, commercial) |
| DroneDeploy | aerial-first unified reality capture + robotics + AI | drone mapping + ground 360 walks + mobile 3D scan | enterprise multi-industry (construction, energy, mining) |
| Propeller | survey-grade map-based earthworks command center | drone photogrammetry/LiDAR/PPK, GNSS rover, total station, TIN upload | contractors/surveyors/mining/aggregates |

## Sources

- OpenSpace — product page https://www.openspace.ai/products/capture/ (fetched 2026-09-07); Help Center https://support.openspace.ai/hc/en-us + "Using OpenSpace" category https://support.openspace.ai/hc/en-us/categories/35805776511891 (fetched 2026-09-07). Evidence Layer A.
- Reconstruct — main site https://www.reconstructinc.com/ (fetched 2026-09-07), product/solutions pages linked from it (Visual Command Center, Reality Mapping, Design Integration, Schedule Integration/4D, Progress Monitoring, Online As-Builts). Evidence Layer A (Tier-2 product pages). NOTE: Knowledge Center https://help.reconstructinc.com/hc/en-us failed twice (transport error) — abandoned per source-access rule; operational mechanics below are limited to marketed behavior.
- Buildots — home https://buildots.com/ + product page https://buildots.com/product/ (fetched 2026-09-07). Evidence Layer A (Tier-2 product pages incl. FAQ).
- DroneDeploy — home https://www.dronedeploy.com/ (fetched 2026-09-07); Help Center https://support.dronedeploy.com/ (fetched 2026-09-07) incl. Ground category https://help.dronedeploy.com/hc/en-us/categories/16533264928407-Ground. Evidence Layer A.
- Propeller — home https://www.propelleraero.com/ (fetched 2026-09-07); Help Center https://help.propelleraero.com/hc/en-us (fetched 2026-09-07) incl. "Getting Started with the Propeller Platform" https://help.propelleraero.com/hc/en-us/articles/39648495685015. Evidence Layer A.

## Product Observations

### OpenSpace (Evidence Layer A — Tier-1 help center + Tier-2 product/FAQ)

- Platform framing: "Visual Intelligence Platform" organized as Capture / Coordinate / Act (Progress Tracking, AI Agents & APIs).
- Capture: attach a 360° camera to a hard hat, tap record in the mobile app, walk the site; the "Spatial AI engine automatically timestamps and maps images to plans". Frames of the 360° video become 360° images pinned to the floor plan. Marketing numbers (image every half second, ~15-min processing, 25K sq ft in 10 min, 2 fps recording) are vendor claims — research notes only.
- Capture modalities: 360° cameras (supported-camera list incl. Insta360, Ricoh Theta), smartphones, drones (OpenSpace Air: drone images → point clouds, 3D meshes, orthomosaics), laser scanners, LiDAR iPhone/iPad "3D Scan". Also outsourced "Walk Services".
- QuickCodes: QR codes placed at capture start points; scanning auto-starts a capture with the correct project, floor plan, and location preselected.
- Viewing/navigation: click images mapped to the floor plan; view by time and date; "Capture Paths" (walked-path visualization in the pano viewer); "Sheet View" to verify capture coverage and spot gaps; Playback Mode (watch a capture as video); AI Image Enhance.
- Time comparison: "Split View — compare any captured area from two dates side by side"; "Reveal Mode — slider comparing now vs was, revealing what's covered up or built over"; Timelapse videos generated from 360° images; "Offline Deliverable" zip of all captured stages viewable without internet ("see what was installed when").
- BIM: optional BIM upload; "BIM Compare" aligns the model to captures so users navigate the model as easily as the 360° images; sheet overlay; self-serve BIM-to-sheet alignment; multiple models; Autodesk Build/BIM 360 model import; mobile BIM viewer with offline mode.
- Field Notes: photos/notes taken while walking auto-pin to the location where made; "Worklist" sends Field Notes to trade partners to respond; Field Notes convert to Procore Observations / Procore Punch List; two-way integrations with Procore and Autodesk (punch, observation, issue workflows); embedded experience inside Procore; Revizto integration.
- Roles: viewer, editor, site administrator, organization administrator (permission matrix in help articles).
- Project setup: upload floor plans (required substrate), optional BIM; unlimited captures and unlimited team members; multi-organization access ("add as many people... from any organization"); customers own content; exports PDF/JPG/PowerPoint reports.
- Overhead captures document spaces above normal line of sight during a walk.

### Reconstruct (Evidence Layer A — Tier-2 product pages; help center unreachable)

- Positioning: "remote quality control, progress monitoring, and facilities assessment"; "brings the project site to decision-makers"; claims to be the only solution combining reality capture, design, and construction schedule.
- Reality Mapping: generates "precise, measurable 2D floor plans and 3D models" from site footage captured on virtually any device (smartphones, 360 cameras, drones); "virtually anyone on site can perform a reality capture walk."
- Reality mapping engine "combines all forms of photo and video and automatically positions that footage in space and over time", producing an "immersive digital twin of your job site as it stands today and as it appeared in the past."
- Design Integration: patented overlay of 2D & 3D designs against reality — clarity into "what's been installed versus what was initially planned."
- Collaboration & Reporting: identify issues remotely, "drop a pin directly where problems are visualized"; on-demand progress reports.
- Schedule Integration & 4D: integrate project timeline; 4D BIM visualization sequencing next steps (Oracle partnership named).
- Online As-Builts: "rewind construction with the click of a button"; "see through sealed walls by turning back the clock" — renovations, tenant questions, liability claims; "view an asset's digital twin at any date or time."
- Project Snapshot: share surveys/captures with anyone.
- Solutions per industry: commercial, industrial, infrastructure, retail multi-site, higher ed, hospitals, airports; facility assessment / infrastructure inspection use cases.
- Marketing percentage claims (travel reduction, on-time improvement) not usable as evidence.

### Buildots (Evidence Layer A — Tier-2 product pages incl. FAQ)

- Positioning: "construction intelligence platform"; Know / Act / Outperform framing (data → insight → action).
- How it works (stated): 1. Capture — "capture footage of your site using 360 cameras, drones or laser scans. Do it yourself or use Buildots' fully managed service (Capture Services)". 2. Analysis — "AI compares the captures to your BIM and schedule to unlock accurate progress and installation data over time." 3. Intelligence — actionable insights.
- Progress at element level, "even for unmodeled areas"; "verified, objective data from multiple sources"; framed as eliminating "he said, she said".
- Capabilities: at-a-glance progress Timeline; Delay Forecast (AI delay prediction — vendor claim); Explorer ("explore your site from anywhere — detailed records of what was built when"); Trades progress (granular per-trade data; contractor/trade management on objective data).
- Complete site documentation: "a true record of what was built and when... defensible documentation in the event of questions or disputes."
- Phase coverage stated: underground utilities (drone captures vs 3D model + schedule), superstructure (drone + 360), interiors/fit-out (360 mapped to BIM + schedule; MEP, walls, finishes).
- Integrations: BIM models, project schedules, captures; "Buildots Data Connector" consolidates progress with financial/scheduling/operational data.
- FAQ (direct): captures processed within 24–36 hours, expedited option via success manager; setup "a few weeks" with dedicated implementation team; no project-count limit; stakeholders incl. owners and consultants; SOC 2 Type 2, ISO 27001, GDPR, MFA, SSO.
- Buildots Field (separate product): workforce intelligence, safety, logistics — workforce visibility ("which trades are on site, where they're working"), automatic records replacing manual logs.
- Use cases incl. payment applications (progress data for pay apps).

### DroneDeploy (Evidence Layer A — Tier-1 help center + Tier-2 product pages)

- Positioning: "unified reality capture platform combining drone mapping and photo documentation" (structured-data description); "See and measure your sites from every angle with 360 cameras, robots and drones — and AI agents proactively surfacing schedule or safety risks."
- Value pillars: Progress ("accurate earthworks analysis and automated schedule tracking and quantification"), Quality ("instant visual defect detection... ranked by severity"), Safety ("automated safety risk identification, from missing toe boards to tripping hazards").
- Help-center taxonomy (direct evidence of pipeline structure): Getting Started / Flight / Ground ("on-site data capture and immersive walks") / Upload & Process ("process your captured data into actionable maps, models, exports, and reports") / Analysis ("inspection tools, analysis, exports") / Reports & Sharing ("deliver roof reports, stockpile data, inspections, and progress... email an export, invite a user to collaborate, or provide them view-only access") / Accuracy & Ground Control ("GCPs, checkpoints, RTK/PPK") / App Market & Integrations (Procore, BIM) / Enterprise ("Flight Services, Single-Sign-On, DroneOps, user management").
- Ground product specifics: 3D Walks capture best practices; Mobile 3D Scan (measurable interiors with a phone); 3D Mobile Scanning with RTK; interior explore experience; media sortable by date; movable media markers; Field Notes on mobile; 3D scan tools and annotations.
- Customer-quoted uses (testimonial layer): progress verification for payments ("If they claim 100% of the work is done but it's actually 80%, we can prove it with a specific 360 scan" — Kier); OAC meeting alignment; trade coordination without climbing; earthworks week-over-week tracking; "Digital Dig Board" for undergrounding (DPR).
- Progress AI product (named) for automated progress tracking; Robotics product for automated inspections.

### Propeller (Evidence Layer A — Tier-1 help center + Tier-2 product pages)

- Positioning: "a single, cloud-powered map that brings your plans, data, and team together"; "map-based command center with analytics tools and reporting"; "it's more than just drone mapping."
- Data capture posture: hardware-agnostic — "upload surface data from the capture or survey tool that best matches your accuracy needs... drone mapping, GNSS rover, total station, or other conventional methods... one unified map"; survey-grade positioning (PPK), photogrammetry and LiDAR processing pipeline; AeroPoints smart ground control; accepts pre-processed data (design files, TIN surfaces, LAS/LAZ point clouds, CSV point data).
- Platform mechanics (help center): create a site (name, location, industry); organization settings; SSO; user access and permissions management; share/manage access to a site per site; upload data; "check the status of a survey submitted for processing"; Survey Explorer; Composite Surveys (crop/duplicate — merging surveys); measurement tools (surface comparisons, volume measurements, stockpiles, cross-sections, smart/custom surface comparison); exports (custom outputs, bulk export, PDF map).
- Capabilities: site checks + analytics; volume calculations; progress tracking; machine telematics (DirtMate GNSS receivers — machines on the map, cycle times, utilization); daily reporting; field collaboration (annotations/markups, "raising issues, and walking projects like we're right there on site"); data management ("your map-based SharePoint" — geospatial docs in one hub with permissions); design conformance (overlay CAD/PDF design files onto the map); Propeller CAD (AI earthworks design on real survey terrain).
- Teams served: project managers, foremen/superintendents, site engineers, VPs/owners, surveyors/GIS, estimators/bidders, quarry managers. Industries: construction, mining, aggregates, waste, transportation, survey+engineering, data centers.
- Software integrations: Trimble Connect, Procore, Autodesk BIM 360, Aconex, OneDrive, Autodesk Build, HCSS. 14-day free trial.

## Cross-product Comparison

| Dimension | OpenSpace | Reconstruct | Buildots | DroneDeploy | Propeller |
|---|---|---|---|---|---|
| Unit of capture | 360° video walk → dated capture pinned to plans; also stills, drone captures, 3D scans | capture walk (any device) → reality-mapped record | 360/drone/scan capture session | flight / 3D walk / mobile 3D scan | survey (dated, processable dataset) |
| Spatial reference | floor plans (+ optional aligned BIM) | auto-generated 2D plans + 3D models | BIM + schedule | maps/models/orthomosaics | georeferenced site map/terrain |
| Time model | capture series by date; Split View; timelapse; offline archive | "in space and over time"; rewind to any date | Timeline; element-level progress over time | media/flights by date; week-over-week analysis | surveys by date; composite surveys; volume over time |
| Plan comparison | BIM Compare overlay, sheet overlay | 2D/3D design overlay ("installed vs planned") | AI vs BIM + schedule | design overlays, schedule tracking | design conformance overlay, site checks |
| Measurement | 3D scan measurement (phone LiDAR) | measurable 2D/3D | element-level progress % | earthworks/stockpile analysis | volumes, stockpiles, cross-sections (survey-grade) |
| Issues | Field Notes pinned to location → Procore punch/observation | pin issues on visualized spots | deviation detection, trade management | AI defect/safety detection | markups, issues, field collaboration |
| Outputs | links, JPG/PDF/PPT, shared folders, timelapse, offline zip | reports, Project Snapshot sharing | progress reports, delay forecast, portfolio views | maps/models/reports, exports | reports, PDF maps, measurements export |
| Processing | fast automated processing (vendor-stated minutes) | automated reality mapping | 24–36 h stated in FAQ | cloud processing pipeline | survey processing pipeline with status |
| Roles/access | viewer/editor/site/org admin; unlimited members, multi-org | enterprise; Project Snapshot for outsiders | SSO/MFA; owners/CM access | enterprise SSO, user management, view-only invites | per-site access sharing, roles, SSO |
| Capture services | Walk Services | (self-capture posture) | Capture Services (managed) | Flight Services (enterprise) | (surveyor self-capture) |
| PM integrations | Procore, Autodesk, Revizto (two-way) | Oracle (named partnership) | Data Connector | Procore, BIM 360, app market | Procore, BIM 360, Aconex, HCSS, Trimble Connect |
| Adjacent extensions | Progress Tracking product; AI agents/APIs | 4D scheduling; facilities assessment | Buildots Field (workforce/safety) | safety/quality AI, robotics | machine telematics (DirtMate), Propeller CAD, daily reporting |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (minimal)

1. **Dated site capture record** — a defined project/site accumulates captures of its real, physical state (photographic, panoramic, video, or scan data), each bound to a date. Remove → nothing remains (no content to view or compare).
2. **Spatial anchoring of captures** — captures are organized against a spatial reference of the project (floor plan, model, map, or georeferenced terrain) so users can locate and navigate them. Remove → an ordinary photo/video library or cloud drive.
3. **Chronological accumulation as the record of work** — captures form a date-ordered series across the project's life, so the site can be compared over time ("what was built when"). Remove → a one-shot capture/scanning service (general photogrammetry or a single survey), not a platform.
4. **Remote navigable access for project stakeholders** — the record is hosted and viewed by people beyond the capturer, without visiting the site. Remove → a field capture tool that hands off files; the platform dimension disappears.

### L1 — Common Mature Structure (cross-product, Layer B evidence)

- Multi-modality in one system: 360° imagery, drone data, phone capture, laser scan ingestion side by side (all five sampled products, at least two modalities each).
- Plan/model overlay: design or model layered against the captured reality (installed vs planned) — OpenSpace BIM Compare/sheet overlay, Reconstruct design integration, Buildots BIM+schedule analysis, DroneDeploy design overlays, Propeller design conformance.
- Progress tracking: progress read from captures against plan/schedule — manual visual comparison at minimum; AI-derived element-level or activity-level progress at the modern pole (OpenSpace Track, Buildots, DroneDeploy Progress AI, Reconstruct progress monitoring, Propeller progress tracking).
- Measurement and quantification: distances/areas, earthworks volumes, stockpiles (aerial pole strongest: Propeller, DroneDeploy; interiors via scan: OpenSpace, DroneDeploy; measurable models: Reconstruct).
- Capture processing pipeline: upload → processing → viewable record (all five; the survey/capture as a processable object with status is explicit at Propeller and DroneDeploy).
- Location-pinned field annotations/issues: notes/photos/markups pinned to capture locations, handoff to field/PM systems (OpenSpace Field Notes→Procore, Reconstruct pins, DroneDeploy annotations/Field Notes, Propeller markups/issues; Buildots deviations).
- Sharing and outward reporting: links, exports (PDF/image/report), view-only stakeholders, timelapse-style outputs, shareable snapshots (all five).
- Mobile capture app + web viewing console (all five).
- Access control: roles/permissions, per-project/per-site sharing, enterprise SSO at the upper tier (all five).
- Integrations with construction PM ecosystems (Procore/Autodesk-class, all five).

### L2 — Variant / Optional Structure

- Capture-modality emphasis as product pole: walk-first 360° (OpenSpace), multi-modal mapping (Reconstruct), AI-analysis-first (Buildots), aerial-first (DroneDeploy), survey-grade earthworks (Propeller).
- Accuracy posture: consumer-grade visual documentation vs survey-grade positioning (PPK/GCP/RTK, accuracy tooling — DroneDeploy Accuracy & Ground Control category, Propeller PPK/AeroPoints).
- Schedule analytics depth: delay forecasting / 4D visualization / trade performance vs schedule (Buildots, Reconstruct) vs visual progress only.
- Outsourced/managed capture services (OpenSpace Walk Services, Buildots Capture Services, DroneDeploy Flight Services).
- Quantified earthworks machinery: composite surveys, surface comparison, cross-sections (Propeller deepest).
- Machine telematics / machine guidance overlay (Propeller DirtMate).
- Workforce/safety/logistics modules (Buildots Field), AI safety/quality detection (DroneDeploy).
- Interior 3D scanning via phone LiDAR (OpenSpace, DroneDeploy).
- Owner/CM-side operation and portfolio multi-project dashboards (Buildots, Reconstruct).
- Payment-application verification use of capture evidence (Buildots use case; Kier testimonial at DroneDeploy).
- Offline deliverable/archival packaging (OpenSpace explicit; others export-based).
- Live fixed-camera monitoring adjacency (not in the sampled five; TrueLook-class) — live streaming vs discrete dated captures.

### L3 — Vendor-specific (research notes only)

- OpenSpace: QuickCodes, Reveal Mode, Capture Paths, Sheet View, Playback Mode, Overhead Captures, AI Image Enhance, "Visual Intelligence Platform" naming, OpenSpace Air naming, offline deliverable zip packaging, hard-hat camera mount kit, viewer/editor/site/org admin role names.
- Reconstruct: "Visual Command Center", patented overlay claim, 4D Scheduling product name, Project Snapshot, Oracle partnership positioning.
- Buildots: "Construction Intelligence Platform" naming, Delay Forecast, Explorer, Data Connector, Buildots Field, Capture Services, 24–36 h processing (FAQ), "reduce delays by up to 50%" marketing claim.
- DroneDeploy: Progress AI, Robotics, DroneOps, Flight Services, roof reports, Stand Count (agriculture), App Market.
- Propeller: DirtMate, AeroPoints, Propeller CAD, MapLabs early-access program, "map-based SharePoint" framing, Survey Explorer, Composite Surveys naming, PropellerU training.
- Vendor-stated figures (processing minutes/hours, area-per-minute, fps, accuracy inches, delay-reduction %) recorded here and excluded from the final document.

## Evidence → Assertion Calibration

- Layer A (direct observation): product behaviors above, each traceable to a fetched official page. Facts like "OpenSpace supports multiple 360 camera models with a published list" or "Propeller surveys are processed with a checkable status" are A.
- Layer B (cross-product commonality): L1 list — observed in all or nearly all sampled products; final document may say "mature products commonly / across the researched sample".
- Layer C (canonical inference): the four-part defining structure — derived from comparison and removal tests; final document states it as the defining structure, more abstract than any implementation.
- Single-source items (e.g., offline deliverable zip, machine telematics as native capability, payment-application framing) stay product-specific/optional and are not promoted.

## Historical / Market-Sample Check

- Pre-360-era construction photo documentation services (companies photographing sites on schedules, delivering plan-organized photo sets via web portal): satisfy L0 (capture + plan anchoring + dated series + remote access) — the Type predates the current 360/drone/AI form. ✔
- Fixed jobsite webcams (live streams for monitoring/security): have capture + time but lack plan/map anchoring and navigable spatial organization → adjacent live-monitoring products, not this Type. ✔ (boundary useful)
- One-off laser-scan/photogrammetry jobs delivered as files: capture + spatial but no accumulation or platform audience → a service/tool, not the platform Type. ✔
- General photogrammetry applications (§04.13): create 3D content from photos of anything; no project container, no dated series, no stakeholder viewership semantics → different Type; construction platforms may *use* photogrammetry as one processing mechanism. ✔
- Pre-digital practice (dated progress photos keyed to floor plans in a binder): satisfies capture+date+spatial idea but not remote hosted access — the paper analog, useful to show the remote-access invariant is what the digital Type adds. Noted honestly; the Type as an Application Type is the digital platform.

## Boundary Findings

1. **vs Construction Field Management** (§17 sibling): field management's objects are day records and field work items (defects raised, routed, verified). Reality capture's object is the visual-spatial record of site state. The seam is a designed handoff: capture-pinned notes convert into the other system's punch/observation/issue records (OpenSpace→Procore direct). Remove the capture record and the Type collapses into field management; remove work-item routing and it collapses into this Type.
2. **vs Construction Project Management** (§17 sibling, processed): PM owns the project container, schedule, cost, contracts, coordination records; the capture platform supplies dated visual ground truth into that container via integrations and (at the analysis pole) progress data. The capture platform has no project-container semantics of its own beyond the site/project reference used to organize captures.
3. **vs BIM Authoring / BIM Coordination** (§17 siblings): models are consumed references here (upload, align, overlay) — never authored or clash-coordinated. A capture platform with BIM viewer is a viewer/alignment consumer.
4. **vs Photogrammetry Application** (§04.13): general 3D-from-photos creation for arbitrary subjects and deliverables vs construction-scoped record systems whose center is the dated project record. Photogrammetry appears inside this Type as one processing mechanism (Reconstruct, Propeller, OpenSpace Air, DroneDeploy).
5. **vs Building Condition Assessment** (§17, processed): condition assessment is a portfolio-condition survey system for existing buildings (element ratings/deficiencies); reality capture is construction-phase visual record accumulation. Adjacent at the facilities-assessment pole (Reconstruct facilities assessment) but no condition-rating machinery in this Type's core.
6. **vs construction camera / live monitoring products** (no directory leaf in §17): continuous live video vs curated, dated, spatially organized capture sessions; cameras feed security/monitoring, capture platforms build the project record. Some products bridge (ingesting fixed-camera feeds) — recorded as adjacency, not identity.
7. **vs Digital Twin Platform** (§16, manufacturing/operations flavor): the phrase "digital twin" appears in vendor language here (Reconstruct), meaning a visual as-built record of a structure — not the operations/maintenance twin machinery of §16. Flag for joint review only if that leaf's pass treats construction twins as core.
8. **vs laser-scanner ecosystem software** (Faro/Leica-class registration tooling): scan registration/processing-centric software is a sibling tooling category; construction capture platforms ingest scan data but their center is the project record, not scan registration.

## Uncertainties

- Reconstruct's operational mechanics (capture→processing→view flow, roles) are evidenced only by product pages (help center unreachable); assertion strength for that product is reduced accordingly.
- Exact processing times, accuracy figures, and capture rates are vendor-stated and were deliberately kept out of the final document (precision not independently verifiable).
- Whether AI-derived progress tracking is becoming definitional: present in four of five sampled products at some depth, but visual comparison products still function without it → kept in L1/L2, not L0.
- Drone-flight planning/operations tooling sits inside two sampled products (DroneDeploy, Propeller) and outside the others (which ingest drone data) → treated as modality machinery (L2), not definitional.
- Market label scope: "reality capture" in AEC marketing covers this Type plus scan-registration ecosystems and camera services; no canonical market term boundary exists — taxonomy note recorded.

## Final Synthesis

A Construction Reality Capture Platform is the project-side system of record for the site's visual history: it accumulates dated captures of the physical work (360° imagery, drone data, phone capture, scans), organizes them against the project's spatial references (plans, models, maps, terrain), and hosts them for remote stakeholder navigation, comparison over time, and comparison against plan/schedule — with issues, measurements, reports, and integrations built on that record. Its capture modalities, accuracy posture, and analysis depth are variant axes; its center of gravity — the dated, spatially anchored, remotely navigable record of what was built when — is invariant.
