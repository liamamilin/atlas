# Research Notes — Government Inspection Management

## Research Goal

Understand what "Government Inspection Management" software actually is as an Application Type: who operates it, what the central object of work is, how inspections are planned, scheduled, conducted, recorded, and reported, how the subject inventory (properties, establishments, facilities, assets, devices) is modeled, where violations/notices/citations fit, and where the boundary sits against Code Enforcement Management, Permit Management, Fire Department Records / Operations System, 311 / Citizen Service Request, Public Sector Case Management, Property Inspection Application (§17), and CMMS/Asset Management.

## Initial Boundary

- Working hypothesis: an agency-side system whose core object of work is the inspection itself — planned/scheduled, conducted in the field by an inspector, recorded with findings against defined criteria, and reported — as distinct from enforcement (violation case + directed instrument + compliance ladder) and from permitting (authorization before work).
- Nearest neighbors: Code Enforcement Management (§24, processed — counterparty), Permit Management (§24, unprocessed), Fire Department Records / Operations System (§24, processed — counterparty), 311 / Citizen Service Request Platform (§24, processed), Public Sector Case Management (§24, unprocessed), Property Inspection Application (§17, unprocessed), Inspection & Metrology Software (§16), CMMS / Maintenance Management (§16).
- Carried obligations from prior passes:
  - Code-enforcement pass joint-review note: "inspections-inside-enforcement must not be absorbed as evidence that generic inspection management owns the notice/citation/compliance track." Test recorded there: "if the output is an inspection report shared with an inspected party but no notice/citation/compliance track follows, it's inspection management."
  - Fire-RMS pass module-boundary flag: apply the core-object test (inspection as the agency's core object of work vs response records as the core with prevention as a module); treat research/fire-department-records-operations-system.md §Boundary Findings as counterparty.

## Research Questions

1. What is the central object — the inspection record — and what lifecycle does it carry (scheduled → assigned → conducted → recorded → re-inspection)?
2. What is the subject inventory (what gets inspected) and how does inspection history accumulate on it?
3. How are inspections driven: recurring/periodic programs, requested inspections (citizen/contractor), permit-driven, complaint/event-triggered?
4. What is the criteria layer (inspection types, checklists, code sets) and how is it configured per agency?
5. What does the field operation look like (mobile, offline, photos, notes, GPS/GIS routing)?
6. What outputs exist: inspection reports, results to inspected parties, notices, citations, work orders, fees?
7. Where do violations/notices/citations sit — inside this Type's core loop or as a handoff to enforcement?
8. How do the packaging poles differ (standalone inspection product vs suite module vs platform module vs fire-RMS product line)?
9. What roles exist (inspector, supervisor/coordinator, administrator, inspected party, third-party inspector)?
10. Historical check: would a paper-era inspection program (annual list, route book, clipboard checklist, filed report) satisfy the definition?

## Representative Products

| Product | Pole | Operator/customer | Tier |
|---|---|---|---|
| Cloudpermit Inspections | standalone Inspections product inside a local-government suite | municipalities/counties (US + Canada) | Tier 2 (product pages) |
| iWorQ Fire Inspections | fire-specific inspection product inside a municipal suite | cities/counties (US), fire marshals | Tier 2 (product page + FAQ) |
| CityReporter | inspection-first multi-department municipal software | municipalities across North America | Tier 2 (product site) |
| GovPilot GovInspect | inspection module of a government platform | municipalities (US) | Tier 2 (product page) |
| ESO Properties & Inspections | fire-department prevention product line | fire departments (US) | Tier 2 (product pages) |

Selection rationale: market representation (local government is the center of gravity), documentation completeness, different product philosophies (suite product vs inspection-first vs platform module vs fire-vertical), different customer levels (small towns → counties), US + Canada coverage. Note: CityReporter was acquired by Cloudpermit (both vendors' sites confirm); both remain distinct products and were sampled as such.

## Sources

Fetched 2026-09-07:

- Cloudpermit — Inspections product page: https://cloudpermit.com/products/inspections ; Mobile Inspections App page: https://cloudpermit.com/products/mobile-inspections
- iWorQ — home: https://iworq.com/ ; Fire Inspection Management Software: https://iworq.com/systems/fire-inspections/
- CityReporter — home: https://cityreporter.ca/ (serves https://www.cityreportersoftware.com/ ; cityreporter.com is a parked domain)
- GovPilot — GovInspect: https://www.govpilot.com/govinspect
- ESO — Community Risk and Prevention: https://www.eso.com/community-risk-prevention/ ; Properties and Inspections: https://www.eso.com/fire/properties-and-inspections-software/

Failed fetches (recorded per source-access limitation):

- HealthSpace (health-department pole): https://www.healthspace.com/ 404; https://healthspace.com/ transport error ×2 → abandoned.
- Decade Software (environmental-health pole): https://www.decadesoftware.com/ and https://decadesoftware.com/ transport errors ×2 → abandoned.
- iworq.com first attempt transport error; succeeded on retry with same URL.
- eso.com/products/eso-properties-inspections/ 404; succeeded via /fire/properties-and-inspections-software/.

Consequence: no authenticated help-center/knowledge-base article bodies were fetched in this pass; all observations rest on official product pages (rich but marketing-adjacent). Exact state names, field lists, numeric limits, and fee schedules are NOT asserted anywhere. The health/environmental-health agency family is covered by inference only (see Uncertainties).

## Product A — Cloudpermit Inspections

### Key observations (Layer A unless noted)

- Positioning: "Complete inspections of your municipality's properties and assets faster than ever with comprehensive software and a mobile app that works offline." Subject = properties AND assets.
- Shipped as a separate product from Building Permitting, Code Enforcement, Licensing, Planning & Zoning, Property Management, Work Orders (product-catalog structure).
- Inspection domains itemized on the page: Fire Inspections ("periodic, scheduled inspections"; "Mark violations and follow-ups"; "Track and route recurring inspections"), Park Inspections, Sports Facilities Inspections, Building Inspections (municipal facilities; "Create punch lists and verify completion of repairs"), Road & Highway Inspections, Asset Inspections.
- Dispatching: citizens schedule inspections online; "Schedule and require additional inspections"; "Dispatch and manage your team of inspectors"; "Confirm or reschedule inspections"; "Reassign inspections to another time or day"; "See the status of all inspections for a multi-permit or violation site"; "View past and upcoming inspections while in the field."
- Field: any mobile device; photos in notes; offline completion with automatic sync; "quick pass inspections to expedite simple visits."
- Re-inspections: "Manage re-inspections remotely."
- GIS: "Plan optimal inspection routes with local GIS integration"; find sites by address or property ID; filter by layers.
- Municipal portal: "Request and track inspections online; View inspection results and project status"; automated updates/notifications; "seamless digital trail of inspections results and decisions"; time-stamped messages.
- API: "Access all inspections data and get inspectors' work lists."
- ICC Code Connect integration: adopted building codes referenced in-product during inspections/reviews.
- Configuration: "Configure workflows to meet local needs."

## Product B — iWorQ Fire Inspections

### Key observations (Layer A)

- Audience named: "fire marshals, inspectors, municipal government officials, and fire department staff." Web-based; "updated in the office from your computer or in the field from your mobile phone."
- Subject model: locations + devices. "Track key devices like smoke detectors and fire extinguishers. Monitor condition and expiration dates, and pinpoint device locations." "Comprehensive Tracking: Monitor and manage all locations and devices."
- Conduct: "Schedule and conduct thorough inspections with clear pass/fail statuses"; annual inspections across property types.
- Criteria layer: "Fire Code Integration — Tie inspection items to integrated fire codes, listing failing/passing code values on inspection printouts."
- Files: "Attach compliance certificates and reference photos directly to locations."
- Financial: "Charge fees directly to locations and link them to specific inspection types"; invoicing and card payments online or in person.
- Contacts/property: "View all locations associated with a single contact and link locations to property details (e.g. parcel numbers)."
- Portal: inspectors in the field; "primary contacts to see results and process payments."
- Reporting: custom reports, Excel/PDF export, scheduled email delivery.
- Custom data fields on top of built-in fields.
- Pre-plans: "Accessible Emergency Pre-Plans — store blueprints… entry points and device locations, including power and water shut-offs"; Emergency Floor Plan Editor.
- FAQ: integrates with iWorQ Permit and Code applications via shared parcel numbers and GIS; automatic sharing of inspection results with other departments; contractor portal for third-party inspectors (sprinklers/alarms) to submit reports directly; notices/letters to property owners sent individually or in bulk, auto-populated with property-specific data.

## Product C — CityReporter

### Key observations (Layer A)

- Positioning: "dedicated software modules for every department"; "paperless inspections"; "One App for all your needs." Department modules: Planning & Development, Fire Prevention & Code Enforcement, Park & Playground, Sports Fields & Stadiums, Facilities, Public Works, Roads & Highways, School & Education.
- Solutions list separates: Asset Management, Inspection & Maintenance Management, GIS Mapping & Vehicle Tracking, E-Permitting, Timesheet Management, Workplace Safety Management, Work Order Management — inspection/maintenance is its own named solution beside work orders and asset management.
- Criteria layer: "stock forms that are both modular and scalable"; "custom form builder"; fire prevention: "an up-to-date library of fire inspection forms based on the current national fire code."
- Motives quoted from clients: standardization ("we needed to standardize the inspection process"), consistency ("ensure our inspection process was consistent, for accountability"), liability/risk reduction, replacing "multiple inspection binders with often illegible documentation."
- Scale example: one Ontario department of environmental services inspects 271 playground sites with 7 inspectors on iPads.
- Historical product naming: ParkReporter™ (module-era naming) — evidence of the inspection-first lineage.
- Now part of Cloudpermit (banner + footer "© Copyright - Cloudpermit 2026").

## Product D — GovPilot GovInspect

### Key observations (Layer A)

- Positioning: "The GovInspect App, when paired with GovPilot's platform, enables on-site inspections and real-time, cloud-based record keeping directly from mobile devices."
- Scope: "all building and construction related inspections - CCO Rental/Sale Inspections, and Code Enforcement Inspections, as well as the issuance of Violation Citations, and Work Orders." (The module spans into citation and work-order issuance — platform-module pole.)
- Scheduling: "Manage inspection assignments with automatic alerts and a custom dashboard configuration. Access records and make updates directly from your calendar. Group users by department or project."
- Cross-department: "assign, track, and complete inspections across relevant departments such as Building and Construction, Code Enforcement, and Planning and Zoning. Records are updated in real-time at the parcel level via GovPilot's GIS Map and Property Profile."
- Field: "one-click navigation feature, inspectors are provided instructions to get to their next assignment, eliminating the need to return to the office"; "Do away with paper forms and the need to update records back at the office."
- Output: "Inspection reports are generated in a digital form formatted to a local government's standards, and utilize drop down lists and typed comments"; "Inspection reports are saved in real-time and become instantly searchable by any employee or department with access to the GovPilot platform."

## Product E — ESO Properties & Inspections

### Key observations (Layer A)

- Suite context: ESO Community Risk and Prevention = "a single platform to track properties, run inspections, and manage permits"; two products: Properties and Inspections; Permits. "Prevention data doesn't stop at the station. When inspections, properties, and permits connect to fire and EMS reporting…" (linkage to the incident-response record — the fire-RMS counterparty).
- Properties side: "Properties tracks all pre-planning aspects of today's fire service"; "property, building and occupant hierarchy and history provide easy access to historical and NERIS incident data"; CAMEO chemical lookup; chemicals and tanks.
- Inspections side: "flexibility… to perform simple to large scale inspections by offering agency configurable checklists and unlimited code sets"; "From NFPA standards to ICC, you can access them easily"; "with the code search feature, you can quickly and easily add ad-hoc violations when doing your inspections."
- "Mobile-first inspections and hazard maps built for crews."

## Cross-product Comparison

| Structure | Cloudpermit | iWorQ Fire | CityReporter | GovPilot | ESO | Strength |
|---|---|---|---|---|---|---|
| Inspection as recorded unit with outcome | ✔ (status, results, digital trail) | ✔ (pass/fail statuses) | ✔ (inspection reports) | ✔ (inspection records/reports) | ✔ (inspections) | A, all 5 |
| Standing subject inventory (properties/establishments/facilities/assets/devices) | ✔ properties + assets | ✔ locations + devices | ✔ locations/assets per department | ✔ parcel/property profile | ✔ property/building/occupant hierarchy | A, all 5 |
| Inspection history accumulating on subject | ✔ (past inspections visible in field) | ✔ (locations carry records) | ✔ (records at fingertips; binders replaced) | ✔ (property history "instant") | ✔ (hierarchy and history) | A, all 5 |
| Agency-defined criteria layer (types/checklists/forms/codes) | ✔ configurable workflows; ICC codes | ✔ fire-code-tied items; custom fields | ✔ stock forms + custom builder + national fire code forms | ✔ digital forms to local standards | ✔ configurable checklists + unlimited code sets (NFPA/ICC) | A, all 5 |
| Scheduling/assignment/dispatch | ✔ (dispatch, reschedule, reassign) | ✔ (schedule + automated notifications) | ✔ (inspection programs; implied scheduling) | ✔ (assignments, calendar, alerts) | (not explicit on page) | A, 4 of 5 |
| Field/mobile capture | ✔ (offline app, photos/notes) | ✔ (field from mobile phone) | ✔ (iPad/tablet, paperless) | ✔ (real-time mobile) | ✔ (mobile-first) | A, all 5 |
| Findings against criteria (pass/fail/deficiency/violation marks) | ✔ (notes, fails, violations & follow-ups) | ✔ (failing/passing code values) | ✔ (forms/checklists) | ✔ (dropdowns + comments) | ✔ (checklists, ad-hoc violations) | A, all 5 |
| Re-inspection / follow-up | ✔ (manage re-inspections remotely) | ✔ (compliance-status notifications) | ✔ (deficiencies → work orders) | (implied) | (follow-ups implied) | A, 3 of 5; B elsewhere |
| Results/reports outward (portal, notices) | ✔ (portal results, auto updates) | ✔ (contacts see results; notices/letters) | ✔ (reports; accountability motive) | ✔ (reports formatted to local standards) | (not explicit) | A, 4 of 5 |
| GIS / routing / parcel linkage | ✔ (routes, property ID) | ✔ (shared parcel + GIS) | ✔ (GIS mapping) | ✔ (parcel-level, navigation) | (hazard maps) | A, 4 of 5 |
| Recurring/periodic programs | ✔ (fire: periodic/recurring, track & route) | ✔ (annual inspections) | ✔ (routine department inspections) | (not explicit) | (not explicit) | A, 3 of 5 |
| Fees/payments | (portal payments implied) | ✔ (fees to locations, invoicing, cards) | (not explicit) | (not explicit) | (not explicit) | A, 1 of 5; keep common-not-core |
| Work-order handoff | ✔ (separate Work Orders product) | (not in fire product) | ✔ (Work Order Management solution) | ✔ (issuance of work orders) | (not explicit) | A, 3 of 5 |
| Violations/citations/notices from findings | ✔ (mark violations & follow-ups) | ✔ (notices/letters; failing code values) | ✔ (fire prevention & code enforcement module) | ✔ (violation citations) | ✔ (ad-hoc violations) | A, all 5 — but as outputs/handoff, not a compliance ladder |
| Third-party/contractor submissions | (portal) | ✔ (contractor portal) | (not explicit) | (not explicit) | (not explicit) | A, 1 of 5; optional |
| Device/equipment-level detail | (assets) | ✔ (devices, condition, expiration) | ✔ (asset management) | (not explicit) | ✔ (chemicals/tanks) | A, 3 of 5 |
| Cross-department property spine | ✔ (separate products, shared spine) | ✔ (shared parcel numbers) | ✔ (modules per department) | ✔ (parcel-level across departments) | ✔ (properties ↔ incidents) | A, all 5 |
| Integration with permits | ✔ (separate permitting product) | ✔ (Permit app integration) | ✔ (E-Permitting solution) | ✔ (Building/Construction module) | ✔ (Permits product) | A, all 5 |
| Pre-plan / emergency data | (not explicit) | ✔ (pre-plans, floor plans, shut-offs) | (not explicit) | (not explicit) | ✔ (pre-planning, CAMEO) | A, 2 of 5; domain-flavored |

## Canonical Model

### L0 — Defining Invariant

Three structures, jointly held:

1. **The inspection as the agency's managed unit of record** — a dated, attributed examination of a specific subject, conducted against defined criteria, recorded with findings and an outcome (pass / deficiencies / violations noted), carried through a lifecycle of scheduling → assignment → conduct → recorded result → follow-up where required. Remove → a work-order or asset-maintenance tool, or a generic case log.
2. **The standing subject inventory** — the inspected things held as persistent records (properties, establishments, facilities, public assets, devices/equipment), each accumulating an inspection history that later inspections read and extend. Remove → one-off field forms with no program memory.
3. **The agency-defined criteria layer** — the inspection types, checklists/forms, and code/standard references that define what is examined and how findings are expressed, configured by the agency to match its own regulatory program. Remove → a generic site-visit log with no inspection semantics.

Operator framing (part of the Type's identity, not a fourth structure): the operator is a government authority running an inspection program under its oversight mandate — this is what separates the Type from private inspection tools.

### L1 — Common Mature Structure

- mobile/offline field capture (photos, notes, GPS) with automatic sync
- scheduling/dispatch consoles: calendars, assignment, reschedule/reassign, route planning over GIS
- re-inspection management and follow-up tracking
- result reporting: inspection reports/documents; portals where inspected parties view results, request inspections, pay fees
- notifications/status updates to requesters, owners, other departments
- recurring/periodic inspection programs (annual fire inspections, routine playground/park checks)
- reporting/analytics over the inspection population (counts, compliance status, trends)
- fees charged to inspections with payment processing (directly observed in one product; portal payments implied in another — keep common-not-core)
- deficiency → work-order handoff; cross-department property history on a shared parcel spine
- code-content access in-product (ICC Code Connect; fire-code-tied items; NFPA/ICC code sets)
- device/equipment-level tracking under a subject
- time-stamped, attributed records positioned as a defensible digital trail

### L2 — Variant / Optional Structure

- agency family: building/community development, fire prevention, parks & recreation, public works/roads/facilities, schools; health/environmental-health (inferred, not directly sampled)
- packaging: standalone Inspections product (Cloudpermit) / department product in a suite (iWorQ Fire) / inspection-first multi-department product (CityReporter) / platform module (GovPilot) / fire-RMS product line (ESO)
- inspection driver: recurring program vs requested (citizen/contractor scheduling) vs permit-linked vs complaint/violation-site-linked
- enforcement posture: findings-only vs notices/citations issued from findings (depth varies; the compliance ladder itself belongs to Code Enforcement Management)
- two-sided structures: third-party/contractor submission portals (AHJ receives external inspection reports)
- pre-plan/emergency-data depth (fire pole)
- regional regimes (US/Canada sampled; other jurisdictions not sampled)

### L3 — Vendor-specific (Research Notes only)

- Cloudpermit: NoVa AI assistant; "quick pass inspections"; DigEplan/Bluebeam plan-review integrations; ICC Code Connect API; marketing counters (1450 customers).
- iWorQ: XworQ AI; Emergency Floor Plan Editor; "Locate Me Safe"; FEMA reporting; AWS GovCloud hosting; NPS 82 marketing claim; "4-5 weeks" implementation claim.
- CityReporter: ParkReporter™ legacy module naming; loss-control/risk-management education offering; "reduces inefficiencies by at least 50%" marketing claim.
- GovPilot: GovAlert companion app; CCO Rental/Sale inspections (New Jersey certificate-of-occupancy practice); one-click navigation.
- ESO: CAMEO chemical lookup; NERIS incident-data linkage; hazard maps; D2i acquisition banner.

## Rejected Findings

- "Inspection management owns the notice/citation/compliance track": rejected. The compliance ladder (violation case → directed instrument → escalation → hearing/lien) is Code Enforcement Management's defining loop (counterparty pass). In the sampled inspection products, violations/notices/citations appear as outputs of findings or handoffs — GovPilot's citation issuance is the deepest direct observation, and it is a platform-module pole, not the standalone pole. This pass discharges the code-enforcement joint-review note by NOT claiming the track.
- "Inspections are just a module of a fire RMS / permitting suite, not a Type": rejected. Standalone inspection products exist and are marketed as products (Cloudpermit Inspections; iWorQ Fire Inspections; CityReporter's inspection-first identity; ESO Properties & Inspections as a named product line). The fire-RMS pass itself recorded that removing prevention leaves the RMS intact while removing the response record leaves a prevention tool — a different Type.
- "Inspection management = asset management / CMMS": rejected. CityReporter ships Asset Management and Inspection & Maintenance Management as separate named solutions; Cloudpermit ships Work Orders separately. The inspection event + criteria + regulatory record is the differentiator.
- "Inspection management = 311": rejected. A citizen-scheduled inspection request (Cloudpermit dispatching) creates an inspection record, not a service request; the terminal object differs (recorded result vs delivered service).
- "Building inspections belong to Permit Management only": rejected. Permit-linked inspections exist (Cloudpermit multi-permit sites), but the sampled standalone poles run inspections with no permit context at all (parks, playgrounds, roads, facilities, fire prevention).
- Precise numeric claims (Cloudpermit "1450 customers / 60 citizens / 32 inspections conducted" counters; iWorQ NPS 82; CityReporter "50% efficiency"): rejected from the canonical model — marketing figures, no verification path.

## Boundary Findings

1. **vs Code Enforcement Management (§24, processed — counterparty)** — sharpest seam. Inspection: an examination event recorded with findings and an outcome; terminal state = recorded result (+ re-inspection where required). Code enforcement: a violation case against a responsible party, driven by a directed instrument (notice/citation) through a compliance ladder to compliance or sanctioned escalation. The same field event can feed both: an inspector's findings may open a violation case — at that moment the record crosses into the enforcement Type. Vendors ship the two as separate products (Cloudpermit, iWorQ, GovPilot all list them separately). Test (confirmed from this side): if the output is an inspection report/result and no violation case with a directed instrument follows, it stays inspection management. Joint-review note DISCHARGED — this pass does not claim the notice/citation/compliance track.
2. **vs Fire Department Records / Operations System (§24, processed — counterparty)** — core-object test applied as instructed. In the fire RMS the incident response record is the core and inspections/permits are a module (direct module evidence in 3 of 5 of that pass's vendors). In this Type the inspection is the core object of work. ESO Properties & Inspections was sampled here as a named product line whose removal-of-response-record pole the fire pass itself called "a different (adjacent) Type." Ratified: the fire department as inspecting agency is an agency-family variant of this Type; the two Types interlock (prevention data connects to incident reporting — ESO's own framing). Counterparty boundary note honored.
3. **vs Permit Management (§24, unprocessed)** — permits authorize proposed work before it happens; inspections verify actual conditions and record results. They interlock (permit-driven inspection requests; inspection results visible on the permit workspace) and share the property spine, but the objects differ. Evidence that the inspection object stands alone: the standalone poles run entire inspection programs (parks, roads, fire prevention) with no permit context.
4. **vs 311 / Citizen Service Request Platform (§24, processed)** — a service request asks government to perform a service; an inspection examines and records a condition. Citizen inspection scheduling (Cloudpermit) is a request *for an inspection* and produces an inspection record. Consistent with the 311 pass's recorded seam.
5. **vs Public Sector Case Management (§24, unprocessed)** — inspection records are event-shaped (dated examination of a subject with criteria-based findings), not case-shaped containers; no generic case grammar. Adjacent, not identical.
6. **vs Property Inspection Application (§17, unprocessed)** — private-sector operator (property managers/inspection companies inspecting on behalf of owners or transactions) vs a government authority exercising regulatory oversight. Name proximity only; different operator, purpose, and record semantics. Flag recorded for that leaf's pass.
7. **vs private-sector field inspection tools (InspectAll/InspectPoint class — no directory leaf)** — service companies performing inspections for clients. Adjacent market; the two-sided AHJ/service-provider structure (iWorQ contractor portal) is where the two worlds meet. No directory restructuring proposed.
8. **vs CMMS / Maintenance Management & Asset Management (§16)** — inspections appear inside asset care (condition checks), but those Types center the asset lifecycle (maintenance, work orders); this Type centers the examination event and its regulatory record. CityReporter and Cloudpermit both ship them as separate solutions/products.
9. **vs Inspection & Metrology Software (§16)** — manufacturing product measurement vs regulatory field examination. Different object, operator, and output entirely.
10. **vs Construction Quality Management / Construction Field Management (§17)** — construction inspections (punch lists, quality checks) are project-delivery machinery inside a project container; this Type is an ongoing regulatory program over a standing subject inventory. Cloudpermit's municipal-facility "punch lists" sit on the facilities-maintenance side, not project delivery.

## Uncertainties

- **Health/environmental-health pole not directly sampled**: HealthSpace and Decade Software were unreachable (404/transport errors ×2 each). The model is inferred to cover health-department inspection programs (establishments as subjects, criteria as inspection types/score forms, field operation identical), but no direct product evidence was collected in this pass. Assertions about the health pole are kept weak in the final document.
- No authenticated help-center/knowledge-base articles were fetched; all observations rest on official product pages. Exact lifecycle state names, field lists, deadline rules, and fee schedules are not asserted anywhere.
- Scheduling depth at ESO and CityReporter was not explicit on the fetched pages (ESO page focuses on properties/checklists/codes; CityReporter's scheduling lives behind its solutions pages) — scheduling is kept as "common" with 4-of-5 direct evidence rather than definitional.
- Regional breadth: all five sampled products are North American. UK/AU/NZ and other regimes were not sampled; the historical check covers them by inference only.
- Whether state/provincial/federal inspection regimes (e.g., statewide inspection systems) use a materially different structure was not researched; the model is built from local-government evidence.
- CityReporter's post-acquisition roadmap (Cloudpermit ownership) may merge product lines; the two were sampled as distinct products as of the research date.

## Final Synthesis

Government Inspection Management is the government agency's inspection-program system of record. Its world model has three jointly-held structures: **the inspection as the agency's managed unit of record** (scheduled/assigned → conducted in the field → recorded with findings against criteria → outcome → re-inspection where required), **the standing subject inventory** (properties, establishments, facilities, public assets, devices — each accumulating inspection history), and **the agency-defined criteria layer** (inspection types, checklists/forms, code/standard references) that structures what is examined and how findings are expressed. Around this core, mature products add the field machinery (mobile/offline capture, photos, GIS routing), the program machinery (recurring schedules, requested inspections, dispatch boards), the outward surfaces (portals for results/requests/payments, notices), the follow-up machinery (re-inspections, work-order handoffs), and the oversight layer (reporting/analytics, fee collection, defensible time-stamped records). Violations, notices, and citations appear in sampled products as outputs of findings or handoffs toward enforcement machinery — the compliance ladder itself belongs to Code Enforcement Management, and this pass explicitly does not claim it. The Type is realized across packaging poles (standalone inspection product, department product in a suite, inspection-first multi-department product, platform module, fire-RMS product line) without its structure changing, and it passes the historical check: a paper-era program (annual list, route book, clipboard checklist, filed report) satisfies all three defining structures without any modern machinery.
