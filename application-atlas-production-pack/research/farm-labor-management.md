# Research Notes — Farm Labor Management

Research date: 2026-09-08
Methodology: WORKFLOW.md (production pack) — 10-step process; evidence tiers A = direct observation of official product documentation fetched this pass, B = cross-product pattern observed in ≥2 sampled products, C = inferred / positioning-level only.

## Research Goal

Understand what a **Farm Labor Management** application is as an Application Type: what objects exist in its world, who operates it, how farm work is planned, recorded, measured, paid, and reported, and where its boundary lies against generic workforce software (time & attendance, employee scheduling, payroll) and against agriculture-side siblings (farm management, harvest management, agribusiness ERP).

## Initial Boundary Hypothesis

- Core use: manage the workforce that performs farm work — especially the seasonal harvest workforce — as records that can be organized into crews, assigned to fields/blocks and crop tasks, and tracked while working (hours and/or piece counts), with payroll-grade output and agricultural compliance reporting.
- Nearest neighbors: Time & Attendance System, Employee Scheduling Platform, Payroll System (generic §09 machinery); Construction Labor Management (parallel domain-specific labor Type); Harvest Management / Farm Management Platform / Agribusiness ERP (agriculture-side record systems); Driver Management (machines/vehicles); Farm Equipment Telematics (equipment).
- Suspected definitional agriculture anchors: production-unit anchoring (ranch / block / field / row / house), crop tasks, crew + crew-leader operating unit, seasonal workforce lifecycle, and piece/production measurement for harvest work.
- Known confusables: "Harvest Time Tracking" (getharvest.com) is an unrelated generic time tracker — name collision only. AgCode is the second dedicated vendor in the named "ag labor management" category but its site was unreachable this pass.

## Research Questions

1. What objects make up the system's world (worker, crew, job, block, ticket, piece type, wage program…)?
2. How is labor planned and assigned — against what anchors (fields/blocks, crops, tasks, crews)?
3. How is work recorded in the field — who captures it (crew leader device, worker self-service, kiosk), and what is captured (hours, breaks, NPT, pieces, weight)?
4. How does piece-rate / production-based pay work, and what compliance machinery surrounds it (minimum wage top-ups, break pay, OT rules)?
5. What does payroll handoff look like (batches, exports, code mapping, ag payroll providers)?
6. What agricultural-specific compliance surfaces exist (H-2A, farm labor contractors, worker safety, audit trails)?
7. What surfaces do workers themselves see (transparency, portals, pay statements)?
8. Which capabilities are definitional vs common vs optional, and does the definition survive pre-digital / regional practice (historical check)?

## Representative Products (sample)

| Product | Pole | Customer tier / geography | Why sampled |
|---|---|---|---|
| PickTrace | dedicated ag labor tracking platform (hire → track → pay) | large US specialty-crop growers/packers | market-leading dedicated product; richest field+kiosk+pay machinery |
| FieldClock | farm-first labor tracking app family | family → enterprise farms + farm labor contractors (US PNW) | different philosophy (QR BYOD vs biometrics); Tier-1 knowledge base; FLC + H-2A surfaces |
| Croptracker | labor module inside a crop/farm management platform | Canadian specialty-crop growers/packers | module-packaging pole; traceability-centric orientation; spray/harvest linkage |

Rejected as samples: AgCode (agcode.com / www.agcode.com — transport errors ×2, abandoned per network rule); FarmERP (farm-erp.com — parked domain). "Harvest" (getharvest.com) excluded as a name-collision generic time tracker.

## Sources

- PickTrace — https://picktrace.com/ (home), https://picktrace.com/time-productivity/, https://picktrace.com/onboarding/ [A, tier-2 product pages]
- FieldClock — https://www.fieldclock.com/ (home), https://www.fieldclock.com/features/labor-tracking [A, tier-2]; Knowledge Base: https://support.fieldclock.com/ root, /fieldclock-app, /admin-site [A, tier-1 operational documentation]
- Croptracker — https://www.croptracker.com/ (home), /product/farm-management-software.html, /product/farm-management-software/farm-labor-tracking.html [A, tier-2]

Source-access limitations:

- PickTrace Help Center (picktraceinc.zendesk.com) — timeout + transport error ×2, abandoned. PickTrace mechanics rest on its three product pages; no claim drawn from its help articles.
- AgCode — transport error ×2 (agcode.com, www.agcode.com); abandoned. The dedicated "ag labor management" vendor category is therefore evidenced by product self-description (PickTrace "labor tracking for growers", FieldClock "farm labor tracking") and not corroborated by a second dedicated vendor's docs.
- FarmERP — parked domain; the international estate/plantation pole could not be sampled. Regional (non-North-America) products are not directly evidenced this pass; the historical check partially covers them at the pre-digital level.
- No vendor numeric limits, exact state-law configurations, or pricing figures are asserted from memory; nothing below relies on model-recalled product details.

## Product Observations

### PickTrace (pole: dedicated ag labor platform)

Evidence tier A (product pages fetched 2026-09-08).

- Positioning: "Digital Workforce Management … for Ag Operations" — Hire (Onboarding), Track (Labor Management), Pay (PayCard); "Track production from field to warehouse"; solutions named Onboarding / Time & Productivity / PayCard / Receiving.
- Onboarding [A]: hire/rehire "in 90 seconds", automatic I-9 and W-4 creation, document scanning + digital storage, employee self-hire via SMS or WhatsApp links, bulk pre-fill "hundreds of applications" via spreadsheet upload, biometric rehire matching faces to the employee database to prevent duplicates, export of employees directly into payroll systems, Spanish & English hiring, "Ping" broadcast messaging to the workforce.
- Field capture [A]: field application "designed to keep up with your crew leaders" — seconds to check in employees, "milliseconds to record pieces", works online & offline, edit and audit from the field, break & lunch alerts, "move the entire crew in one action".
- Warehouse kiosk [A]: high-speed check-in kiosk; biometric facial verification ("eliminate ghost employees"); jobs assigned in advance for faster check-in; enforcement of mandatory break & lunch durations; "every action is backed by a geo-located, timestamped audit log".
- Wage engine [A]: "piece paid breaks", NPT (non-productive time) bulk insert, automatic minimum wage adjustments, regular rate of pay calculations, OT/DT, 7th-day OT — generating "accurate gross payroll calculations".
- Payroll handoff [A]: integrates with "popular agriculture payroll providers like Famous and Datatech" and "most other major payroll providers"; payroll code mapping; bulk employee import; error alerting; bulk timecard and piece auditing.
- Reporting/insight [A]: customizable reports; daily production and cost reports; minimum-wage adjustment reports; unit cost analysis; "compare contractors, H-2A"; Insights mobile app with live gross payroll calculations and "production stats by crew, ranch, and block".
- Pay (PayCard) [A]: payroll card program eliminating paper checks (bank-issued Mastercard program).
- Receiving [A]: a module for production "from field to warehouse" (packhouse receiving) — adjacent to harvest/receiving territory, not the labor core.

### FieldClock (pole: farm-first labor tracking app family)

Evidence tier A (tier-1 KB fetched 2026-09-08; richest operational detail of the sample).

- Product family [A]: FieldClock app (crew & operations management), Agent (individuals track their own activity and record compliance logs), Kiosk (self-service time clock "in your office, warehouse, packhouse or cold storage"), Admin Site (web management + stakeholder reporting), Employee Portal ("employees can view their own hours, production, and payouts"), API.
- Identity & capture philosophy [A]: core interface is a "color-coded QR scanner"; employees identified by scanned QR badges (with photo, badge PIN, temporary badge printing, bluetooth badge printer). Biometrics explicitly rejected: gloves make fingerprints impractical, external readers are fragile, and biometric legal requirements change frequently. Captures clock-in/out, breaks, piecework quantities; weight streamed from bluetooth scales per scan; QC reports associable with an employee or a box of fruit.
- Jobs [A]: Jobs are created as **Hourly** or **Piecework**; Jobs List with filters; job details tabs in Admin — Map (pins per job), Employees, Breaks, Payouts, Photos, Timeline, Equipment, Notes, Finalize; "Jobs to Finalize" list; finalize/unfinalize workflow; copy job; overnight jobs; multiple jobs for roamers; "fast pieces" alerts (suspiciously high piece counts); set/change an employee's piecework quantity on mobile or admin; tickets vs pieces distinction documented; **Ticketer** role (a person who counts/records production and issues tickets) with "Production by Ticketer" report; **Shared and Team picking** (group production split across workers).
- Farm anchoring [A]: Ranches and Blocks as managed records with geo-fenced boundaries (mobile + admin); restricting job access at ranches; limiting tasks and varieties per ranch/block; Varieties and Tasks as importable reference lists; Equipment and Equipment Categories tracked against jobs.
- Crews & people [A]: Crew Boss role; "Associated Crew Bosses" configuration; move an entire crew from one job/ranch/block to another on mobile; clock an employee in/out without a badge; employee merge, deactivate, bulk edit, import; group numbers; payroll codes distinct from badge display numbers; granular roles: Company Administrator, Account Administrator, Employee Administrator, Kiosk Administrator, Payroll Administrator, Report Viewer, Production Viewer, Quality Controller, Manager, Crew Boss, Ticketer, Roamer.
- Wage machinery [A]: Wage Programs configuring Overtime/Doubletime, Piecework Break Pay, Minimum-Wage settings; Pay Templates; payouts calculation ("What types of payouts can FieldClock generate?", "How are payouts calculated?"); Minimum-Wage Adjustments (MWAs) setup article; Regular Rate of Pay (RRoP) calculation article; Non-Productive Time Categories (breaks, travel, training) and Break Templates; Note Templates/Fields; Payroll Batches (preview, generate, download, add note, fix issues) with per-system export setup for ~20 payroll providers — ag-specific ones documented (Famous, The Farmer's Office, Spokane Software, Delp Farm Accounting, Blue Skies, Compu-Tech, Agknowledge, Agstar, Greux, Paymate Clarity, NRS) plus generic (ADP, Paychex, Paylocity, Kronos, QuickBooks, MAS90, CenterPoint, Asure, BBSI); hours-count semantics in payroll CSVs; payroll code mapping; Payroll Entities; payroll groups.
- Compliance & transparency [A]: H-2A solution — "Track Hours Offered and progress toward your Three-Quarters Guarantees while producing wage statements that are compliant with H-2A requirements"; KB article "How do 'hours offered' work for H2-A requirements"; FLC solution — "keep track of labor expenses to invoice your clients while providing them with direct access to reporting"; Employee Portal transparency ("treat your employees with respect"); Worker (agent) compliance logs; device lockdown/pinning support; location fixes recorded; audit-ready posture ("protect yourself from future investigations").
- Field conditions [A]: offline mode ("remote fields with no cellular coverage"; data saved to device then synced); BYOD commodity iOS/Android; bilingual English/Spanish ("no tech experience required"); usage-based pricing following seasonal labor-force size.
- Reports [A]: Overtime, Daily Activity, Daily Pay, Labor Costs by Field, Non-Productive Time, Production by Ticketer / by Field / by Employee, Job Summary, ranch reports, QC Notes Summary, custom reports, CSV export.

### Croptracker (pole: labor module inside crop/farm management platform)

Evidence tier A (tier-2 product pages fetched 2026-09-08).

- Positioning [A]: "farm management software that connects the full operation — spray, harvest, labor, packing, shipping — on one platform built specifically for fruit and vegetable growers"; "coordinate crews across multiple harvest windows"; traceability "right down to the block and employee responsible".
- Labor module ("Work Crew Activity and Labor Tracking" / "Punch Clock") [A]: "a complete employee management and time keeping solution built for fruit and vegetable growers"; track hourly and piecemeal pay rates; make schedules; organize work crews and assign crew leaders; employee badges + kiosk mode punch-in; record time on the go and offline (customer testimonial stresses offline sync for unreliable rural cell coverage); "track employee time on location and easily shift employees to different tasks and areas on the go"; automate piece-rate calculations "including minimum wage top-ups and performance bonuses"; hourly payouts; export payroll reports in a variety of formats for payroll systems; email employees their work-log summaries ("fair and transparent payroll management"); maintain employee records season over season; kiosk / admin / hourly / piecerates workflow pages.
- Cross-module linkages [A]: "Pair Punch Clock with Harvest and record time against inventory to accurately assess individual and team performance"; "Keep workers safe — link Spray records and worker locations"; spray records "alert workers of safe re-entry and pre-harvest intervals before they enter an area"; production practice records (pruning, mowing, thinning, cleaning…) "link to employee performance records" and "log tasks down to the row"; harvest yield records "link location and picker information to harvested inventory"; track labor and equipment costs and analyze profitability.

## Cross-product Comparison

| Structure / capability | PickTrace | FieldClock | Croptracker | Tier |
|---|---|---|---|---|
| Identified worker records (photo, badge/credential, seasonal records) | yes (biometric identity, employee DB) | yes (QR badges, photos, PINs) | yes (badges, season-over-season records) | B — definitional |
| Crews with crew leaders as operating unit | yes (field app "keeps up with your crew leaders"; move entire crew in one action) | yes (Crew Boss role; move entire crew job→job) | yes (work crews + crew leaders) | B — definitional |
| Assignment anchored on farm production units | yes (production stats by crew, ranch, block) | yes (Ranches/Blocks, geo-fence, per-ranch job access) | yes (block/row-level records, traceability to block) | B — definitional |
| Work organized as jobs/tasks with crop-task semantics | jobs assigned in advance (kiosk), crew-level | Jobs (hourly/piecework), Tasks, Varieties per ranch/block | tasks down to the row; production practices | B — definitional |
| Hours + breaks + non-productive time capture | yes (break/lunch alerts, NPT bulk insert) | yes (breaks, NPT categories, Break Templates) | yes (hours and break times) | B — definitional (recorded form) |
| Piece/production counts per worker | yes ("milliseconds to record pieces"; piece auditing) | yes (pieces, tickets, ticketer, shared/team picking, weight) | yes (piecemeal rates; time against harvested inventory) | B — signature recorded form |
| Piece-rate payout computation with minimum-wage top-ups | yes (MWA, piece paid breaks, RRoP, OT/DT, 7th-day OT) | yes (Wage Programs, MWA, piecework break pay, payouts, RRoP) | yes (piece-rate calc, MWA, bonuses) | B — common, strongly characteristic; NOT definitional (pieces can be tracked while paying hourly — FieldClock states this) |
| Supervisory capture (crew-leader device records the crew) | yes | yes | yes | B |
| Worker self-service / transparency | partial (self-hire, messages) | yes (Agent app, Kiosk, Employee Portal) | yes (emailed work-log summaries) | B — common |
| Offline-first field capture + sync | yes | yes | yes | B |
| Payroll handoff via batches/exports with code mapping to ag payroll providers | yes (Famous, Datatech) | yes (~20 documented providers incl. ag-specific) | yes (multi-format exports) | B — common |
| H-2A machinery (hours offered, three-quarters guarantee, contractor comparison) | yes (report "compare contractors, H-2A") | yes (explicit H-2A solution + KB) | not observed | product-specific ×2, common in US specialty-crop segment |
| Farm labor contractor (FLC) support | yes (contractor comparison reports) | yes (FLC invoicing + client reporting) | not observed | common (US) |
| Worker-safety linkage to crop-protection records | not observed | not observed | yes (spray REI/PHI alerts linked to worker locations) | product-specific (crop-platform pole) |
| Harvest/production-inventory linkage | yes (field-to-warehouse; Receiving module) | partial (weight per scan; QC per box) | yes (time against inventory) | common, package-dependent |
| Identity hardware philosophy | biometric facial verification (kiosk; anti-ghost-employee rationale) | QR scan; biometrics explicitly rejected (gloves, legal churn) | badges + kiosk (method not emphasized) | vendor-specific contrast |
| Hiring/onboarding forms (I-9/W-4, self-hire, bilingual) | yes (deep) | partial (employee import) | partial (employee records; not observed as hiring) | common, depth varies |
| Payment card program for workers | yes (PayCard) | no (payroll via ADP partnership) | no | vendor-specific |
| Labor as module vs standalone product | standalone suite (hire+track+pay) | standalone app family | named module inside crop platform | packaging variant |

## Canonical Model (abstraction)

Two jointly-held structures carry the Type; remove either and the product stops being farm labor management.

**1. The farm workforce as managed records.** Identified individual workers — the farm's own employees, seasonal and returning workers, and (in US practice) workers belonging to farm labor contractors / H-2A crews — each record carrying farm-work attributes: identity and contact, crew membership, task capability, availability, pay identifiers (badge number vs payroll code), and status across seasons. Anonymous headcount is an input to reports, never the record.

**2. Tracked placement of that labor against farm work over time.** The anchors are the farm's production units — ranches/farms, blocks, fields, orchard/vineyard blocks, rows, greenhouses/houses — and the crop tasks performed on them (planting, pruning, thinning, irrigation, crop protection, harvest…). Tracking takes two complementary forms, either of which alone keeps a product inside the Type:

- *planned form*: crews and individuals assigned to jobs (job = crew/task × block × date), jobs prepared in advance, crews moved between blocks/jobs as the day unfolds;
- *recorded form*: presence and time (clock in/out, breaks, non-productive time) and/or production (pieces, tickets, weights) attributed per worker against the job/block.

The agricultural anchoring is load-bearing: remove production units, crop tasks, crew semantics and seasonal workforce shape, and the same machinery is generic time & attendance / employee scheduling — that genericness is exactly the boundary.

**Signature capability (common, not definitional):** agricultural work measurement and its pay translation — piece/production counts per worker per block per task, computed into payouts under piece rates with minimum-wage top-ups/adjustments, piecework break pay, regular-rate-of-pay and overtime rules. Products can track pieces while paying hourly; a hours-only deployment still satisfies the core.

**Historical check (older / regional / pre-digital practice):** a grower's labor ledger naming seasonal workers; a farm labor contractor's crew roster; the daily assignment of crews to orchard blocks for picking; tally sheets of boxes or buckets picked per worker; time books of hours; settlement of the contractor's invoice — all satisfy both structures without mobile apps, GPS, cloud, or biometrics. Plantation/estate registers (per-worker daily attendance with output weights) satisfy the same shape regionally. The definition is not fitted to the modern mobile implementation.

## Vendor-specific Findings (research notes only)

- PickTrace: biometric facial verification as identity spine (anti-"ghost employee" rationale); proprietary "Wage Engine"; PayCard payroll-card program; Ping workforce messaging; SMS/WhatsApp self-hire; Receiving module (packhouse receiving — outside this Type).
- FieldClock: QR-scan-first identity with an explicit documented rejection of biometrics; patented Employee Portal; Agent app for individual self-tracking + compliance logs; ticket/ticketer production mechanics; shared/team picking; bluetooth scale weight streaming; FLC client-invoicing mode; ~20 documented payroll export configurations; usage-based seasonal pricing.
- Croptracker: labor realized as a named module ("Punch Clock") of a crop-management platform; spray REI/PHI worker-safety linkage; harvest-inventory linkage ("record time against inventory"); traceability-to-block-and-employee orientation.

## Boundary Findings

- **vs Time & Attendance System (§09):** generic T&A owns the punch→timesheet→approval→payroll machinery for any employer. Farm labor management holds the farm-workforce record and its placement against production units and crop tasks; punches are one recorded form. A farm running generic T&A gets hours but not blocks/crews/pieces; a farm hours-only tracker (FieldClock-style minimal deployment) sits at the family edge toward T&A.
- **vs Employee Scheduling Platform (§09):** scheduling products plan shifts against demand patterns for any industry; farm labor management's allocation anchors are ranches/blocks and crop tasks with crew semantics and harvest-window seasonality.
- **vs Payroll System (§09):** payroll executes pay (checks, taxes, filings). This Type produces the labor record and payout-grade computation (pieces→gross, MWAs, OT) and hands off via payroll batches/exports to payroll systems — including agriculture-specialized payroll providers (Famous, Datatech, The Farmer's Office…). Ag payroll providers that also brand "labor management" are packaging over this seam.
- **vs Construction Labor Management (§17):** parallel domain-specific sibling with the same two-leg shape. The worlds differ: projects/jobsites/work orders and craft certifications vs ranches/blocks and crop tasks; prevailing-wage/certified-payroll machinery vs piece-rate machinery; the seasonal H-2A/FLC population has no construction analogue. Keep both as sibling Types.
- **vs Harvest Management (§20 sibling, unprocessed):** harvest management's center is the harvest operation and its product (what was picked, maturity, yield, inventory, quality). This Type's center is the workforce (who, in what crew, how long, how many pieces, owed what). They meet where production records link pickers and hours to bins (Croptracker pairing; PickTrace field-to-warehouse) — a handoff seam, not a merged Type.
- **vs Farm Management Platform (§20 sibling, unprocessed):** farm platforms hold crop/production records and may include a labor module (Croptracker proves the packaging); the workforce as the managed population is the labor Type's center.
- **vs Agribusiness ERP:** labor is one module among many in estate/agri ERP; standalone dedicated products prove the Type stands alone.
- **vs Driver Management / Farm Equipment Telematics (§18/§20):** machines and their operators' machine-hours vs field labor crews and their productive work; equipment tracking appears as a capability here (FieldClock Equipment records) but is not the center.
- **vs Farm labor contractor services / H-2A recruitment services:** licensing, recruitment, and agency services are services, not this software Type; the software supports FLCs (invoicing, contractor comparison) and H-2A recordkeeping (hours offered, three-quarters guarantee) without performing recruitment.

## Uncertainties

- AgCode's product detail unverified (site unreachable) — the dedicated-vendor category is evidenced by self-description of two products, not a third vendor's docs.
- The international / estate-plantation pole (tea, rubber, palm estates; EU vineyard labor) was not directly sampled; its inclusion rests on the historical check and on the model's abstraction, not on a fetched modern non-North-American product.
- Exact legal scopes (H-2A program rules, state overtime/doubletime variants, biometric law specifics) are referenced by vendors but not independently verified; all compliance statements above are held at the level vendors state them.
- Crew leader as formal system role vs informal crew selection varies; both patterns observed, no claim of uniformity made.
- Whether scheduling (planned form) is present in every product: Croptracker mentions schedules; PickTrace mentions jobs assigned in advance; depth of planning (multi-week crew planning vs same-day movement) is not fully documented in reachable sources.

## Final Synthesis

Farm Labor Management is the farm's workforce system of record: it holds the people who perform farm work — disproportionately seasonal, crew-organized, and partly contractor-supplied — and tracks their placement on farm work across the season. The world is workers → crews (crew leaders) → jobs/tasks → ranches/blocks/rows → recorded time, breaks, non-productive time, and piece/production counts → payout computation under piece rates and wage rules → payroll batches and compliance reporting (H-2A, contractor comparisons, audit logs). Its defining delta against generic workforce software is the agricultural anchoring of every leg; its signature capability is piece/production measurement translated into compliant pay; its packaging ranges from dedicated labor platforms to a module of a crop-management platform.
