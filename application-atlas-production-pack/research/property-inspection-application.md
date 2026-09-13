# Research Notes — Property Inspection Application

## Research Goal

Understand what a **Property Inspection Application** (DIRECTORY §17, Construction, Real Estate & Facilities) really is in the market: who operates it, what its core objects and workflows are, and how it differs from its three flagged neighbors — Home Inspection Application (§29), Building Condition Assessment (§17 sibling), and Government Inspection Management (§24).

This leaf arrives with **three carried joint-review flags** (recorded in STATUS.md by prior passes):

1. **home-inspection-application (§29, processed 2026-09-08)** proposed the operator/customer split: §17 = owner/property-manager-side recurring condition inspections over a standing portfolio (no per-job external client, no sold report); §29 = the home-inspection trade serving external clients per engagement. This pass must confirm or refute that split with fresh evidence.
2. **building-condition-assessment (§17, processed)** flagged adjacency and carried the line "transaction-driven single-property inspection (buyer/lender due-diligence report) belongs to the sibling" — which the home-inspection pass contradicted for the buyer-side pole. This pass must ratify the correction jointly.
3. **government-inspection-management (§24, processed 2026-09-07)** flagged name proximity: private-sector operator vs government authority. This pass must discharge or confirm.

## Initial Boundary (working hypothesis before research)

- The §17 center is **operator-side**: the inspecting party owns or manages the property portfolio; inspections are recurring/event-driven operations work, not sold engagements.
- Nearest neighbors: Home Inspection Application (§29 trade), Building Condition Assessment (capital-planning surveys), Government Inspection Management (regulatory authority), Property Maintenance Management (work execution), Residential/Commercial Property Management PMS (portfolio + business loop).
- Unknowns: whether the market's center really is property-manager-side; whether move-in/move-out deposit documentation is core or variant; how findings flow to maintenance; whether scoring/audits belong; regional (non-US) structure.

## Research Questions

1. Who operates the software (property manager, owner, maintenance/inspection staff, external inspector)?
2. What is the core object — the inspection event, the property/unit, the checklist template?
3. What inspection types recur across products (move-in, move-out, routine, turn/make-ready, safety, common-area, audit)?
4. How is an inspection structured (sections, items, ratings, photos, notes, signatures)?
5. How are inspections scheduled and assigned (recurring schedules, routes, team assignment)?
6. How do findings flow onward (work orders, deposit/damage documentation, compliance, owner reporting)?
7. What is the report's role — internal record, resident-facing document, owner-facing document? Is it ever a *sold* deliverable?
8. How does the product relate to the property management system (PMS) — integration, embedding, or separation?
9. What separates this Type from the home-inspection trade (§29), from capital-planning condition surveys (BCA), and from government inspection programs (§24)?
10. What regional/segment variants exist (multifamily, SFR, student, vacation rental, commercial, associations; AU/US)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Why sampled |
|---|---|---|
| **HappyCo** | Multifamily maintenance-operations platform whose Inspections module is the market reference (also embeds its inspection engine into Buildium and MRI) | Deepest documentation; enterprise multifamily; platform philosophy |
| **SnapInspect** | Pure-play property inspection app (SMB, multi-industry, NZ-rooted selling globally) | Independent pure-play; strongest scheduling/report detail; multi-industry breadth |
| **AppFolio Property Manager** | Full PM suite with Inspections inside its Maintenance module ("Inspections & Unit Turns" in the Core plan) | Suite pole; different packaging philosophy; large PM customer tier |
| **InspectRealEstate (IRE)** | Australian residential-PM inspection tool (now under Reapit ANZ) | Regional (AU) pole — **evidence thin, see Source-access Limitation** |

Deliberately not sampled: InspectAll/InspectPoint (service-company inspection tools — §29-adjacent per the government pass's boundary note), CityReporter/Cloudpermit (government side, already sampled by the §24 pass), Spectora/HomeGauge (§29 trade, already sampled by that pass).

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- HappyCo product site: https://www.happyco.com/ , https://happy.co/platform/maintenance-operations
- HappyCo Support (Zendesk help center): https://support.happy.co/hc/en-us (category/section index) and article: "Performing an Inspection: The Complete Guide to Sections, Items, Photos, Notes, and Ratings" https://support.happy.co/hc/en-us/articles/52935499171220
- SnapInspect: https://www.snapinspect.com/ , https://www.snapinspect.com/howitworks , https://www.snapinspect.com/property-maintenance-software
- AppFolio: https://www.appfolio.com/property-manager/ , https://www.appfolio.com/property-manager/maintenance
- InspectRealEstate: https://www.inspectrealestate.com.au/ (root only)

**Source-access Limitation**: InspectRealEstate's site returned only a minimal landing page (brand line, "enquiries processed" counter, agent login) under Reapit ANZ branding; two further URL attempts 404'd. Per the network rule the source was abandoned after two failures. IRE is retained in the sample as a **weak regional anchor only** — no structural claims rest on it, and nothing in the canonical model depends on it. AppFolio's public help center serves resident-portal documentation (not manager-side inspection detail); AppFolio observations rest on its product/marketing pages. Buildium's own help center (Salesforce site) failed to render; Buildium is covered indirectly through HappyCo's Buildium-embedded support category.

## Product A — HappyCo

### Key observations (evidence layer A unless noted)

**Positioning**: "Property Maintenance Management Software and AI Platform" for multifamily. Platform pillars: Maintenance Operations (Proactive Maintenance, Work Orders, Make Readies, **Inspections**, Reporting & AI Insights), Maintenance Services, Asset Management, Asset Evaluation (Due Diligence, Lease File Audits, Site Visits), Sourcing. Roles addressed: Owners/Principals/Acquisition Managers; Operators (PM leaders, maintenance leaders, property teams); Maintenance teams (VPs, supervisors, technicians).

**Inspections module** (maintenance-operations page):
- "Consistent, defensible inspections every time. Use configurable templates and mobile capture to document every detail—then convert findings into action instantly."
- "Standardize quality across move-ins, move-outs, safety, and more"
- "Capture photos, notes, and signatures in the field"
- "**Auto-create work orders from findings**"
- "Maintain compliant, audit-ready records"
- Inspections sit beside Work Orders and Make Readies in one maintenance hub that "syncs with your PMS".

**Support-center structure** (Tier-1 operational documentation):
- Category "Happy Property" → section **Inspections** (27 articles): Creating a New Inspection in Manage; Inspections in Manage; Editing Inspections in Manage; Bulk Delete Inspections and Work Orders; Workarounds for Inspection Duplication.
- Category "Happy Property Maintenance Mobile App" → Inspections: **Smart Inspections – Mobile**; Creating, Starting, and **Scheduling** Inspections in the app; **Performing an Inspection: The Complete Guide to Sections, Items, Photos, Notes, and Ratings**; Native camera; Capturing Video.
- Tasks section: "**Create Tasks or Work Orders From Inspection Ratings**"; "Managing Tasks in Happy Property: Scheduled Dates and Resident Signatures".
- Features/FAQs: Managing Templates in Manage; Customizing Templates in Manage; **Managing Report Workflows and Styles**; Bulk Importing Units; Property Provisioning Portal.
- Legacy app category "Inspections (Legacy app, older version)": Inspection **Schedules**; Assigning Inspections to Team Members; Copying a Previous Inspection; Business Wide Inspection Templates; Guest Inspections (send + require signatures); Live Inspections (live operator / guest inspector / inspector join a live session); Reports (presets, formatting, comparison reports).
- **Due Diligence category** (separate product line): Unit Walk (performing unit inspections, editing unit inspection templates, pre-filled values, common-area units), Lease File Audit, cost sheets, DD reporting — the acquisition-side inspection context is packaged as a *different product* from operations Inspections.
- **PMS Integrations**: AppFolio, Entrata, MRI, RealPage, ResMan, Yardi sections; FAQ "**MRI Inspections powered by HappyCo**"; a full **Buildium** category (Templates; Creating Inspections — Assigning Inspections to Team Members, Copying a Previous Inspection; Performing Inspections — Accessing Inspection Templates, Rating Items, Completing/Saving/Deleting; Reports) — i.e., HappyCo's inspection engine is embedded as Buildium's and MRI's inspections module.

**Inspection record structure** (from the "Performing an Inspection" article, A-layer):
- An inspection is built on an **Inspection Template** with three components: **Overview** (short text fields at top), **Sections** ("groupings of items… typically represent physical rooms or areas (e.g., Entry, Bedroom, Kitchen)"), **Summary** (longer text fields at bottom).
- **Items** carry **rating types**: checkboxes (multiple applicable ratings, e.g., "Good" and "Clean"), drop-down lists (exactly one), radio buttons (restricted options, e.g., Yes/No).
- Per-item **Notes** (typed or voice-to-text) and **Photos** (in-app camera or device library), with per-item photo-count badges.
- **Base templates vs one-off customizations**: base templates edited only by account administrators on the Manage page and apply to all future inspections; one-off customizations during an active inspection apply only to that inspection (and copies).
- **Move-out caution**: "Changing section names or altering their order during a Move Out inspection affects the layout of your final report… not recommended for Move Out flows" — record consistency across the tenancy is a stated concern.
- Internal-only "reference notes" on items visible to team members.

**Customer-story evidence** (B-layer, vendor-published outcomes):
- GoldOller/Timberlake: "resident disputes… dropped 82%. And we've increased damage charges collected by 17%" — move-in/move-out documentation feeding deposit/damage resolution.
- Maxus: "Before, turning a unit required multiple visits to assess requirements. With HappyCo, they log right in and see any inspection" — inspections feeding unit turns.
- Mark Taylor: "automatic daily report… portfolio inspections and top issues, essential for meeting company compliance goals and informing ongoing budget decisions."

## Product B — SnapInspect

### Key observations (A-layer)

**Positioning**: "Intuitive Property Inspection Software & App" for "property managers, real estate pros, and inspectors… multi-family units, commercial properties, or Associations". Also markets a "Home Inspections" industry page (straddles the §29 trade — boundary evidence, see Boundary Findings).

**Inspection types by industry** (both the home page and how-it-works enumerate them):
- Residential: Move in, Move out, Annual, Routine, Exterior, Unit inspections
- Commercial: same set
- Multifamily: Due diligence, Lease file audit, Unit inspections, Exterior & interior, Safety/regulatory, Pool/Gym inspections, Preventative maintenance
- Vacation Rental: Move in/out, Pre-arrival, On-boarding, Housekeeping, Inventory
- Student Housing: Tenant move in/out, Cleaning & maintenance, Damages inspections, Mid-lease inspections

**Workflow** (how-it-works):
- **Checklists**: "Select from our range of industry-proven inspection checklists or customize your very own… No checklist is too complex."
- **Scheduling**: "Set inspection dates & times, with the option to make inspections **recur in 'X' days/weeks/months**." "SnapInspect automatically organizes your schedule for you."
- **Field capture**: mobile app (iOS/Android/web), offline support with sync, in-app **video recording** attached to the report (served via branded web-page link), in-app **signatures**, auto-text comments, voice dictation.
- **Reports**: branded templates or in-house designer; "Collect signatures directly in-app and email your inspection report as soon as you are finished"; continue editing online after completion; export Microsoft Word, PDF, Excel.
- **Sync/security**: cloud sync, multi-location backup.
- **Integrations**: Dropbox, Google Drive, Zapier, robust API.

**Testimonial evidence** (B-layer): "Our customized checklists help guide inspectors so they know what to look for and the finished reports make **handling the security deposit** a breeze" (CGA Property Management).

**Maintenance companion page** (property-maintenance-software):
- "brings your inspections, work orders, and reporting into one smart platform"
- Work orders capture labour hours, material costs, completion status; time-stamped records
- "**Flag issues and create follow-up tasks instantly**"
- Geofencing clock-in; live in-app team chat; offline work
- Preventive maintenance scheduling; industry lists again name move-out damage assessments, fire safety/ADA inspections **and scoring**, unit turn inspections & make-ready tracking, "Deposit deduction & dispute documentation"

## Product C — AppFolio Property Manager

### Key observations (A-layer for existence and placement; depth limited)

- The PM platform's **Core plan** lists "**Inspections & Unit Turns**" among its headline capabilities (alongside Property Accounting, Marketing & Leasing, Work Order Management, Mobility, Portals).
- Maintenance module "Includes:" list: Online Maintenance Requests, Work Orders, Unit Turn Board, **Inspections**, Common Area Maintenance, Mobile Violations & Tracking, In-House Maintenance.
- "**Mobile Inspections**: Enable your team to manage on-site property inspections directly in AppFolio. This results in faster and more accurate workflows that get your units tuned more quickly." — inspections explicitly tied to unit turns.
- "**Mobile Violations & Tracking**: With real-time GPS tracking, navigate community maps to easily add new violations, follow up on existing violations, and close them out all from the field" — association/HOA violation machinery adjacent to inspections (community-association variant).
- Public help center serves the *resident* portal (payments, maintenance requests, leases) — manager-side inspection detail not publicly documented; depth of inspection workflow not directly observed.

## Product D — InspectRealEstate (IRE)

### Key observations (weak — sourcing limitation)

- Root page only: "Real estate agent Software - Australia — Inspect Real Estate", "225,403,616 enquiries processed!", agent login link; site now under **Reapit ANZ** branding (Facebook/LinkedIn links to reapit-anz).
- Confirms: AU regional market presence, agent/PM-facing login, high-volume operational use. No structural detail obtainable; two further URL attempts 404'd; abandoned per the network rule.
- No claim in the canonical model rests on IRE.

## Cross-product Comparison

| Dimension | HappyCo | SnapInspect | AppFolio | IRE |
|---|---|---|---|---|
| Operator | multifamily operator/PM (owner & operator roles) | property managers, PM companies, associations | property management companies | AU residential PM/agents (weak) |
| Standing portfolio substrate | properties/units, bulk unit import, PMS sync | properties/units per industry | properties/units in the PM suite | implied |
| Inspection event as unit of record | yes (create/start/schedule/complete; duplication handling; bulk delete) | yes (scheduled, recurring, copied) | yes (mobile inspections; tied to turns) | implied |
| Template/checklist structure | template = overview + sections (rooms/areas) + summary; items with rating types | industry-proven + custom checklists | not directly observed | n/a |
| Evidence capture | photos, notes (typed/voice), video, signatures | photos, video, notes, signatures | mobile capture (detail not observed) | n/a |
| Recurring scheduling | Inspection Schedules (legacy app documented); scheduling in current app | explicit recurrence "X days/weeks/months" | not directly observed | n/a |
| Findings → work | **auto-create work orders from findings**; "Create Tasks or Work Orders From Inspection Ratings" | "flag issues and create follow-up tasks instantly"; work orders in same platform | inspections inside the maintenance module beside work orders | n/a |
| Deposit/damage loop | damage chargebacks, dispute reduction (customer story) | security-deposit handling (testimonial); deposit deduction & dispute documentation | not directly observed | n/a |
| Report | report workflows/styles, presets, comparison reports, branding | branded reports, Word/PDF/Excel, emailed when finished | not directly observed | n/a |
| Packaging | standalone inspections app (legacy) → maintenance-operations platform; **embedded engine inside Buildium & MRI** | pure-play app + companion maintenance module | module inside full PM suite | standalone (AU) |
| Adjacent inspection contexts kept separate | Due Diligence / Unit Walk / Lease File Audit as a **separate product line** | markets due diligence & property-condition-assessment as industry pages | violations tracking (associations) as separate machinery | n/a |

**Cross-product commonalities (B-layer)**: standing property/unit portfolio; inspection event bound to a specific property/unit; template/checklist-driven examination; mobile field capture with photo evidence; report generation and sharing; findings feeding maintenance work; move-in/move-out as canonical inspection types; team assignment; audit-ready record posture.

**Structural placement observation**: in all three strongly-evidenced products, inspections live **beside or inside the maintenance/operations machinery** (HappyCo Maintenance Operations; SnapInspect inspections+work orders "one smart platform"; AppFolio Maintenance module), and integrate with the PMS rather than replacing it (HappyCo PMS integrations incl. embedding; SnapInspect API/Zapier; AppFolio *is* the PMS).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The standing property portfolio as the inspected population.** Properties, and the units/spaces within them, held as persistent records that accumulate inspection history over time. The portfolio pre-exists any single inspection and outlives it. *(Remove → a generic checklist/audit tool with no property memory, or a PMS database with no examination loop.)*
2. **The structured inspection event as the unit of record.** A dated, attributed examination of a specific property/unit/space, structured by a reusable examination template — sections (typically rooms/areas) containing checkable/rated items — producing a recorded result retained on the property's record. *(Remove → free-floating checklists, or a photo/notes app with no examination structure.)*
3. **The operator-side condition loop.** The inspecting party is the portfolio's own operator — an owner or property manager inspecting inventory it is responsible for — and the recorded findings are consumed by the operator's own processes: maintenance work, deposit/damage resolution, safety/compliance posture, owner reporting. **No per-job external paying client and no sold report.** *(Remove the operator-side structure → the §29 home-inspection trade; remove the consumption loop → an inspection archive nobody acts on.)*

Jointly-held load-bearing tests:
- 1 alone = property/unit database (PMS territory)
- 2 without 1 = generic checklist/audit tool or one-off §29-style engagements
- 3 without 1+2 = operations software with no inspection record
- 1+2 without 3 = inspection archive with no operational home (thin; the market's products all show the loop)
- 1+3 without 2 = maintenance/operations platform with no examination record

### L1 — Common Mature Structure (standard capabilities; not definitional)

- Mobile field capture: photos (in-app camera/library), notes (typed/voice), video, per-item attachment
- Recurring scheduling and assignment (schedules, recurrence intervals, team-member assignment, copying previous inspections)
- Report generation: branded/formatted reports, presets, comparison reports, PDF/Word export, email/share at completion
- Findings → work: auto-creating work orders/tasks from inspection ratings or flagged issues
- Move-in/move-out flows with resident signatures; deposit/damage documentation
- Unit turn / make-ready integration (inspections feeding turn boards/timelines)
- Team roles and permissions (administrators vs field staff; internal-only reference notes)
- PMS integration (unit/resident data sync; or being the PMS's own module)
- Portfolio-level dashboards/reporting over inspection activity and compliance goals
- Property/unit hierarchy management (bulk import, provisioning)

### L2 — Variant / Optional Structure

- **Segment packaging**: multifamily, single-family rental, student housing, vacation rental (pre-arrival/housekeeping/inventory types), commercial (repair-vs-replace, equipment audits), community associations (violations tracking), affordable housing
- **Inspection-type mix**: due-diligence/lease-file audits (acquisition context — packaged as a separate product line by the platform pole), safety/regulatory scoring (fire safety/ADA), common-area/site inspections
- **Delegated/remote inspection**: guest inspections sent to non-team persons with required signatures; live/remote collaborative inspection sessions (single-vendor observed — product-specific until corroborated)
- **AI assistance**: voice-to-text, auto summaries, photo analysis, AI workflow builders (era-current)
- **Geofencing/clock-in**, offline-first capture depth
- **Regional regimes**: deposit/dispute rules, compliance vocabularies (not directly researched across regions in this pass; kept weak)

### L3 — Vendor-specific (research notes only)

- HappyCo: Manage (desktop) + Happy Property Maintenance App (HPMA) naming; Smart Inspections; JoyAI; Happy Force; SiteVisit; Due Diligence product line; Continuous Lease Audits; Property Provisioning Portal; Guest/Live Inspections; embedded inspection engine for Buildium ("HappyCo Inspections" inside Buildium) and "MRI Inspections powered by HappyCo"; legacy standalone Inspections app generation documented in its own help center.
- SnapInspect: report-customization engine ("industry's most powerful report customization engine" — marketing claim), video-in-report via branded web link, auto-text comments, geofencing, AI workflow builder, "75% time savings"/"$10 per $1" marketing figures (unverified — rejected from canonical model).
- AppFolio: Realm-X Maintenance Performer (agentic AI), Unit Turn Board, Mobile Violations & Tracking, Auditing Center, plan packaging (Core/Plus/Max).
- IRE: Reapit ANZ ownership; "enquiries processed" counter (meaning unverified).

### Rejected Findings (not promoted)

- "Inspection apps are just checklist tools" — rejected: the standing property portfolio and the operator-side consumption loop are structural, not cosmetic.
- "Photos are definitional" — rejected: the paper-era pole (written condition sheets) satisfies the core without photo capture; photos are the dominant modern evidence layer, not the invariant.
- "Recurring schedules are definitional" — rejected: one-off move-in/move-out-only usage fits the Type; recurrence is the dominant operational pattern, not the invariant.
- "Deposit/damage chargebacks are definitional" — rejected: depth varies (customer-story evidence at the platform pole; testimonial at the pure-play); the documentation loop is the invariant, chargeback economics are segment depth.
- "Due-diligence unit walks belong here" — rejected as center: the sampled platform itself packages acquisition-side inspection (Due Diligence) as a separate product line from operations Inspections; adjacency recorded, not identity.
- Marketing figures (75%/80% time savings, $10:$1 ROI, 82%/17% outcomes): vendor-published, no verification path — kept out of the canonical model.

## Boundary Findings

1. **vs Home Inspection Application (§29, processed — joint review RATIFIED from this side).** The carried split is confirmed by this pass's evidence: all strongly-sampled products sell to property operators/managers; inspection types are operational (move-in, move-out, routine, turn, safety, common-area); reports are internal/counterparty records (residents, owners, staff), never a per-engagement sold deliverable; there is no external paying client per job. §29's center (client-commissioned, fee-per-engagement, report-as-product trade) is a different commercial structure. Corroborating nuances: (a) SnapInspect also markets a "Home Inspections" industry page — the same tool family can serve the §29 trade, so the boundary is the **operator/customer structure of use**, not tool capability; (b) HappyCo packages acquisition-side Due Diligence separately from operations Inspections — even within one vendor the contexts are separated. The home-inspection pass's proposed test is adopted: *external paying client + sold report → §29; standing inventory + operator-side loop → §17.*
2. **vs Building Condition Assessment (§17 sibling, processed — joint review RATIFIED with a correction).** Keep both. BCA's center is the portfolio-scale condition survey translated into cost-quantified capital renewal outcomes (condition indices, deferred-maintenance backlog, multi-year capital plan); this Type's center is operational, unit/room-grain, event-driven inspection feeding maintenance/deposit/compliance. **Correction to BCA's carried line**: "transaction-driven single-property inspection (buyer/lender due-diligence report) belongs to the sibling" is wrong for the buyer-side home-inspection pole — that pole belongs to **home-inspection-application (§29)** per that pass's evidence (the §17/§29 boundary is operator/customer structure, not transaction-vs-capital). Corrected statement: buyer/lender due-diligence inspection performed as a *sold engagement by the inspection trade* → §29; portfolio-scale acquisition condition assessment (capital context) → BCA; operator-side recurring operations inspection → this Type.
3. **vs Government Inspection Management (§24, processed — name-proximity flag DISCHARGED).** Confirmed: different operator (private owner/PM vs government authority), different purpose (operations & documentation vs regulatory oversight), different record semantics (no code/standard criteria layer, no violation/enforcement track here). The two Types share only the word "inspection" and the generic examination-event shape.
4. **vs Property Maintenance Management (§17).** The inspection is the examination event with its evidence; maintenance is work execution. Findings hand off at the seam (auto-created work orders carry the findings into the neighbor's object). In-suite the two are siblings under one operations roof; as Types their centers differ. Remove the examination record → maintenance management; remove the work loop → this Type thins toward a documentation archive.
5. **vs Residential/Commercial Property Management (PMS).** The PMS holds the portfolio, leases, residents, and the money loop; this Type examines condition. Integration/embedding is the seam (HappyCo syncs unit/resident data from PMSs and is embedded in Buildium/MRI; AppFolio ships inspections inside its own suite). Remove the examination loop → PMS.
6. **vs generic inspection/audit checklist tools (no directory leaf; MeazureUp/GoAudits class).** No property portfolio substrate; subject is any business/site; no property-shaped template grammar (rooms/areas/units). The portfolio + property-shaped sections is the differentiator.
7. **vs Construction Quality Management / punch lists (§17).** Project-delivery container vs standing-portfolio operations; construction inspections live inside a project's lifecycle, these inspections live on the portfolio's timeline.
8. **vs Security Deposit Management (§17 sibling leaf).** Move-out inspection documentation is the evidentiary input to deposit disposition; the deposit ledger/disposition machinery is the neighbor's center. Adjacent, interlocking, distinct.
9. **vs Tenant/Resident Portal.** Resident-side requests/payments vs operator-side examinations; the resident may *sign* an inspection record (move-in) but does not operate this Type.
10. **"Remove what to become another Type" tests**: remove the standing portfolio → generic checklist/audit tool; remove the template structure → photo/notes log; remove the operator-side loop (add external paying client + sold report) → Home Inspection Application (§29); add cost-quantified capital-renewal outcomes → Building Condition Assessment; add government authority + code criteria → Government Inspection Management; remove the examination event → PMS/maintenance software.

## Historical / Market-Sample Check (§24)

Paper-era practice: the property manager's per-unit condition checklist form (printed template: rooms as sections, items with check/rating boxes), completed at move-in with the tenant's signature, photos or written condition notes attached, filed per unit; annual walk-through list; findings phoned/memo'd to maintenance; the signed condition sheet produced at deposit disposition. This satisfies all three L0 structures — no cloud, no mobile app, no PMS, no AI. Regional check: the sampled set spans US multifamily/SMB and (weakly) AU residential PM; the core does not depend on US deposit law or US PMS embedding. Within-vendor history: HappyCo's own help center documents a legacy standalone "Inspections app" generation (schedules, templates, team roles, reports) preceding its current platform — the standalone-inspection-app generation is inside the Type. **Pass.**

## Uncertainties

- IRE structural detail unobtainable (sourcing limitation recorded above); the regional pole is asserted weakly.
- AppFolio's inspection workflow depth (templates, scheduling, report mechanics) not directly observed — its public help center documents the resident portal, not manager-side inspections; AppFolio claims are limited to existence and placement.
- Exact lifecycle state vocabularies per product not verified article-by-article (article titles observed only); states are described generically in the final document.
- Guest/Live inspections observed at one vendor only — held product-specific/optional.
- Scoring (fire safety/ADA) observed in one product's industry list — held variant, not common.
- Whether a *resident-facing* inspection surface (beyond signature capture) exists broadly was not researched.
- Regional deposit/notice regimes not researched; no claims made about them.

## Final Synthesis

A Property Inspection Application is the **property operator's inspection system of record**: it holds the operator's standing portfolio (properties and their units/spaces) as persistent records, structures recurring and event-driven **inspection events** (move-in, move-out, routine, turn/make-ready, safety, common-area) through reusable templates — sections shaped like rooms/areas containing rated/checkable items — captures field evidence (photos, notes, signatures) on mobile, retains the recorded result on the property's record, and converts findings into the operator's own follow-through: maintenance work orders, deposit/damage documentation, compliance posture, and owner reporting. The defining core is exactly three jointly-held structures — standing portfolio, structured inspection event, operator-side condition loop — with **no per-job external paying client and no sold report** (that commercial structure is the §29 home-inspection trade). Everything else — mobile capture, recurring schedules, branded reports, PMS integration/embedding, dashboards, AI, segment packaging — is mature structure around that core. The Type is realized across packaging poles (standalone app, maintenance-operations platform module, PM-suite module, embedded engine inside other suites) without its structure changing, and it passes the historical check: the paper condition-sheet system satisfies all three structures with no modern machinery.
