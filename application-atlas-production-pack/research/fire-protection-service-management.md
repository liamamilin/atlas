# Research Notes — Fire Protection Service Management

Research date: 2026-09-07
Leaf: Fire Protection Service Management (DIRECTORY.md §29 Home, Family, Personal & Local Services)
Slug: fire-protection-service-management

## Research Goal

Understand what "Fire Protection Service Management" software actually is in the real market: what objects it manages, how fire protection work flows through it, what is fire-protection-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings like HVAC/plumbing/electrical/elevator, fire-department government systems, CMMS/EAM, construction project management, AHJ-side compliance platforms).

This pass also discharges the cross-reference left by the electrical-service-management pass ("vs Fire Protection Service Management / Elevator Service Management — trade siblings, expected same family pattern; cross-reference when processed").

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of a fire protection / fire & life safety service contractor (inspection, testing, maintenance, service, repair, and sometimes installation of fire protection systems: alarms, sprinklers, extinguishers, special-hazard suppression, fire doors, backflow preventers).
- Core objects likely: customer + service location, job/work order with lifecycle, technician, invoice/payment — the field-service family spine shared with the electrical pass.
- Fire-specific candidates: recurring code-mandated inspection programs, inspection forms/question sets tied to standards (NFPA/ULC etc.), deficiency tracking, compliance reporting to AHJs (authorities having jurisdiction), device/asset registries, technician certifications.
- Closest neighbors: Small Business Field Service Management (generic FSM spine), trade siblings (HVAC/plumbing/electrical/elevator), Fire Department Records / Operations System (§24 — government emergency response, totally different operator despite the shared word "fire"), CMMS/EAM (asset ownership line), Construction Project Management (installation projects), AHJ-side compliance platforms (The Compliance Engine / LivSafe / IROL — companions, not this Type).
- Key open question: does the fire trade carry a *structurally distinct* object (the way the electrical pass found none), or is "fire protection" purely a content/packaging layer over generic FSM?

## Research Questions

1. What objects make up the system (customer, site/building, system/device/asset, inspection, deficiency, work order, proposal, invoice, payment)?
2. How does the recurring inspection program work (series, frequencies, auto-scheduling, overdue visibility)?
3. How is an inspection executed and recorded (question sets, code libraries, offline mobile, photos)?
4. What is the deficiency lifecycle (creation, persistence across visits, status, conversion to proposals/work orders, resolution, reporting)?
5. How does compliance reporting work (customer reports, AHJ submission, third-party compliance platforms)?
6. How do service/repair/installation work and billing flow (work orders, price books, proposals, invoices, payments, accounting/ERP sync)?
7. How do the poles differ: fire pure-play vs commercial multi-trade suite vs multi-industry inspection platform vs FM-embedded module; US NFPA regime vs UK fire-safety regime?
8. Historical check: would older, regional, paper-era fire protection operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| Inspect Point | fire & life safety pure-play; inspection-first platform covering the full inspection-to-collection cycle; multi-trade within fire (alarm, sprinkler, extinguisher, special hazard, doors/dampers, backflow, suppression) | Tier 2 (product pages with operational FAQs) |
| BuildOps | commercial multi-trade contractor suite with a dedicated Fire & Life Safety vertical; service + projects + financials; integrates Inspect Point as its inspection engine | Tier 2 (site + rich fire FAQ) |
| InspectAll | multi-industry inspection platform (cranes, EHS, utilities, manufacturing; fire extinguisher inspections among types) — the "generic inspection platform used by fire protection companies" pole | Tier 1 (support docs) + Tier 2 (site) |
| Mobiess | UK/FM-pole mobile data-capture platform with a Fire Safety Compliance module (fire doors, fire risk assessments, compartmentation) — regional/regulatory variant and FM-operator pole | Tier 2 (site + module pages) |

Attempted and abandoned per source-access rules:

- ServiceTrade (a major fire-protection-focused service contractor platform): HTTP 403 on three attempts (www root, /fire-protection-software/, no-www root). Market-coverage gap acknowledged.
- ZenFire: two empty responses (zenfire.io, getzenfire.com transport error). Abandoned.
- Simpro (AU/UK multi-trade field service with fire vertical): HTTP 403 twice. Abandoned.
- FieldPulse fire page: 404.

## Sources

Fetched 2026-09-07:

- Inspect Point (Tier 2): https://www.inspectpoint.com/ — positioning, feature map, trades, stats; https://www.inspectpoint.com/features/inspections/ — inspection engine, code library list, FAQs; https://www.inspectpoint.com/features/deficiencies/ — deficiency lifecycle FAQs; https://www.inspectpoint.com/features/scheduling/ — inspection series, dispatch, FAQs
- BuildOps (Tier 2): https://buildops.com/ — platform map, Fire & Life Safety vertical link; https://buildops.com/industries/fire-safety — fire page with problem/solution framing and extensive FAQ (AHJ submissions, NFPA frequencies, certification dispatch, Inspect Point integration, Certified Fire story)
- InspectAll (Tier 1 docs): http://docs.inspectall.com/ — category map (Accounts, Assets, Barcodes/QR/RFID, Calendar, Folders, Form Building, Form Entry, Priorities, Portal, Reporting, Teams, Time); http://docs.inspectall.com/category/57-folders — folder articles; http://docs.inspectall.com/category/59-priorities — priority/deficiency articles; https://www.inspectall.com/ — positioning
- Mobiess (Tier 2): https://www.mobiess.com/ — platform modules; https://www.mobiess.com/modules/fire-safety-software — fire safety module (fire door registers, PAS 79 fire risk assessments, compartmentation surveys, actions/remedials)

Failed: https://www.servicetrade.com/ (403 ×3), https://zenfire.io/ (empty ×2), https://getzenfire.com/ (transport error), https://www.simprogroup.com/ (403 ×2), https://www.fieldpulse.com/industries/fire-protection-software (404), https://buildops.com/industries/fire-life-safety/ (404 — correct path is /industries/fire-safety)

## Product A — Inspect Point

### Key observations (evidence layer A unless noted)

- Positioning: "Purpose-Built Platform For Fire Protection Professionals"; "dedicated to the fire & life safety industry"; "Our platform … helps you run your ITM operations" — ITM (Inspection, Testing, and Maintenance) is the trade's core vocabulary. Scale claims: 15,000–16,000 users; 4.5M inspections completed; 20M systems & assets in service.
- Feature spine (site navigation): Scheduling → Inspections → Deficiencies → Proposals → Service (work orders) → Invoices → Payments, plus an AI Suite. The homepage frames the whole product as "the entire inspection, testing, and maintenance cycle from start to finish" and "inspection-to-collection."
- Trades served (fire-internal segmentation): Fire Alarm & Security, Fire Sprinkler, Fire Extinguisher, Special Hazard, Doors & Dampers, Backflow Prevention, Chemical Suppression, Facilities, Campus.
- **Inspection series engine (recurring program)**: "Inspect Point's innovative 'inspection series' engine simplifies managing, scheduling, and dispatching inspections, with full visibility into what's upcoming or overdue." "If a visit is missed, you can reschedule in seconds, and future visits automatically shift to stay aligned." AI can build series in bulk ("build out next quarter's monthly extinguisher inspections across every building on an account"). Recurring inspections "based on frequency and compliance needs."
- **Asset-based inspection engine + code library**: "the industry's most complete fire & life safety code library, an asset-based inspection engine." Question sets chosen "based on system type, building code year, and reporting requirements." Library includes NFPA 72 (fire alarm), NFPA 25 (water-based systems ITM), NFPA 10 (extinguishers), NFPA 17/17A, NFPA 2001, NFPA 101, NFPA 12, NFPA 770, NFPA 2010, NFPA 80 (fire doors); ULC 536/537/561/268 (Canada); California Title 19 AES; Joint Commission, DNV, HFAP (healthcare accreditation); backflow forms; "hundreds of city and town jurisdictions." Custom inspection builder and custom questions supported.
- **Deficiency lifecycle**: "When a technician answers a question indicating that a device or system is deficient, a deficiency will automatically be created for that device or system. This deficiency will be present on future inspections in that series until resolved." Deficiencies carry internal notes (back office only) vs public notes (on the report); photos auto-linked to deficiency/system/inspection, annotatable; deficiencies have statuses; a "filterable, sortable deficiency database" plus a deficiency dashboard with trends. Proposals are "built on detailed deficiency notes" (photos, notes, code references); work orders generated from deficiencies "linked back to the original inspection."
- **Compliance reporting & AHJ/third-party delivery**: branded one-click reports with flexible output (filter by system type, deficiencies-only, NFPA vs Joint Commission formats, service summaries); Customer Portal centralizes inspection and service reports; integrations with third-party compliance platforms TCE (The Compliance Engine), IROL, LivSafe with "batch submissions and one-click report delivery"; "Deficiencies are flagged to AHJs upon report submission and can be auto-resolved in platforms like BRYCER and IROL when resolved in Inspect Point."
- **Mobile field execution**: offline capable ("answer inspection questions and document deficiencies even if they are not connected to Wi-Fi"); quick and bulk inspect; extinguisher swap and loaner tracking; real-time pump curve capture; multi-tech support.
- **Service work**: service module "bridges the gap between your inspection and service teams"; convert inspection to service work; emergency service dispatch; time and materials tracking; customizable Price Book; service reports.
- **Money**: invoices generated from proposals, inspections, or work orders (syncing time, materials, price-book items); card/ACH payments incl. back-office charging; customer portal with 1-click payment; QuickBooks and ERP integrations; open API.
- **Other**: map-based scheduling + dispatch board; GPS fleet tracking (Inspect Point Fleet, powered by Azuga); AI suite (Inspection Assistant pre-fills fields, catches missing/mismatched fields, pre-publish checks; Inspect Point Assistant plain-language bulk actions and queries e.g. "show me every open critical deficiency past 60 days").
- Integrations named: BuildOps, simpro, QuickBooks, TCE, IROL, LivSafe, payments, fleet.

## Product B — BuildOps (Fire & Life Safety vertical)

### Key observations

- Positioning: commercial multi-trade contractor platform (HVAC, electrical, plumbing, **Fire & Life Safety**, refrigeration); fire page headline: "Where inspections, service, and compliance finally work as one." Homepage fire teaser: "NFPA 25, NFPA 72, ITM, deficiency tracking. For the teams who keep buildings safe."
- **Deficiency → quote → invoice pipeline**: "BuildOps keeps your fire protection operations connected from deficiency to quote to invoice. With Inspect Point built in, inspection findings flow straight into scheduling and billing. No re-entry. No dropped follow-ups." "Deficiencies sync from Inspect Point to BuildOps instantly. Quote, schedule, and bill the repair without re-entry."
- **Inspection agreements with auto-scheduling**: "Build inspection agreements with auto-scheduled visits by property, asset type, and NFPA frequency. Set it and let it run."
- **Compliance tied to work**: "Inspection reports attach to the job automatically. Compliance stays tied to the work. No chasing paperwork." FAQ: "You are required to submit AHJ reports and follow NFPA frequency requirements. Set up automated inspections on a recurring schedule… Build forms for your field techs to work through step-by-step to check off every single requirement of fire industry compliance."
- **One platform for inspections + service + installs**: "Inspections, service, and new construction all run in a single platform. The system you install becomes the system you inspect — and the data never breaks as you continue through service agreements, future work, and future inspections." "The same board that dispatches your techs to the jobsite talks to the dashboard that covers your recurring maintenance contracts. The boots on the ground tech that's flagging fire system deficiencies can instantly pull up the full service history for that location."
- **Inspection job type + dynamic asset/inspection-type population**: "You can create your job in BuildOps, mark it as an inspection, and it automatically syncs with Inspect Point. Assets and inspection types populate dynamically based on NFPA codes and system types (NFPA 25 for sprinklers, NFPA 72 for alarms, etc.). Techs complete inspections in the field, capture system deficiencies, and send signed reports, all in the same mobile flow. Back in the office, team members see flagged deficiencies instantly, and can build quotes in one click."
- **Certification-aware dispatch**: "Smart Dispatch By Field Tech Certification — With fire & life safety, you need different techs to go to different jobsites based on their certifications and skillset."
- Platform modules: Service Management (Work Order Closeout, Asset Management, Preventative Maintenance, Schedule & Dispatch, Purchasing & Inventory), Project Management, Financials, Sales & CRM; OpsAI; ERP integrations (Sage, Viewpoint, NetSuite, QuickBooks); role-based permissions; SOC 2 claim.
- Customer story: Certified Fire (fire protection services company, Utah/Nevada) — service billing tracking, billable time, profit margin improvements.

## Product C — InspectAll (multi-industry inspection pole)

### Key observations (Tier 1 docs)

- Positioning: "Mobile Inspection Software for EHS, Healthcare, OSHA Compliance"; "best practices for EHS, NFPA, NIH, and OSHA standards for companies that specialize in providing services to highly regulated industries." Industries pages: overhead cranes, EHS, site inspections, utilities, manufacturing — fire extinguisher inspections appear as one inspection type among many (fire extinguishers, exit routes, eyewash, ladders, forklifts, fall protection, confined space…).
- **Accounts** = "All of your facilities, customers, and locations in one place" — the customer/site container.
- **Folders** = the scheduled work unit: "Folders help you organize, schedule, and report on your forms." Folder types with default forms and default reports; schedule a folder; copy and reschedule; close/open a folder; folder notes (internal job notes); move folders/assets between accounts; merge.
- **Forms** = the inspection instrument: form building (44 articles), form entry ("Answer questions, snap photos, and prioritize your findings").
- **Assets** = "Manage your assets and equipment to keep them compliant" (50 articles); barcodes, QR codes, RFID for asset identification.
- **Priorities** = the deficiency analog: "Track priorities, assign tasks, and resolve problems found." Articles include: Prioritize Your Findings; Priority Resolution (website); Manage Follow Ups to Priorities in three options (Mobile Priority Resolution / Folder Workflow / One Form Option); **Priority Roll-Over Feature** (unresolved priorities roll into the next folder/visit); Summary/Deficiency Reports; Team Priorities; Resolve All Priorities; Show Resolved on Reports.
- **Portal** = "share your inspections with your clients through a convenient portal"; Reporting (42 articles); Teams; Time (job costing/timecards).
- Nothing fire-specific in the docs — the same structure serves many regulated-inspection trades. [Layer B: this is the generic pole of the same structure Inspect Point implements fire-specifically.]

## Product D — Mobiess (UK/FM pole)

### Key observations

- Positioning: UK "independent mobile data capture solution" for facilities management; modules: Audits and Inspections (Insight), Asset Data Capture (Asset Inspector), Mobile Work Orders, **Fire Safety Compliance**. Customers are FM providers (VINCI Facilities, Skanska UK, Mitie, Equans, BGIS, G4S, Transport for London…) — the operator is often the FM provider rather than a specialized fire contractor.
- **Fire Safety module templates**: Fire Door Inspections ("Create and maintain an efficient asset register for fire doors across multiple projects and sites"); Fire Risk Assessments ("full PAS 79-based Fire Risk Assessments" — the UK regime's assessment standard; "legally required inspections"); Fire Compartmentation Surveys (passive fire protection auditing).
- **Fire door asset register**: "Treating each individual door as a unique asset record, with a unique reference per door… QR codes / barcodes onto your fire doors… retrieve the assets attribute data upon re-inspection (such as client, building, floor, glazing, height, width, finish to frame, and finish to leaf)… assigning an inspection to a door… view its history on our web-portal, building up an audit trail and creating an accurate fixed asset register."
- **Actions and remedials** (the deficiency analog): "Log, assign, categorise and manage actions"; "Configure prepopulated options for defect and corrective action logging, down to a per-question basis"; logic can make an action compulsory based on question answers.
- **Evidence & reporting**: photo evidence with annotation against inspections/actions/assets/work orders; branded PDF reports; per-door and building/project reports; Excel/CSV exports; CAFM/IWMS/CRM integrations and data-lake/BI gateways.
- The fire module is one module of a broader FM inspection platform — fire safety compliance as a template family inside a generic mobile inspection/work-order engine. [Layer A for this product; regional regime variant: UK fire-safety regulation (PAS 79 FRAs, fire door registers) instead of US NFPA ITM.]

## Cross-product Comparison

| Structure / capability | Inspect Point | BuildOps (FLS) | InspectAll | Mobiess (Fire module) | Assessment |
|---|---|---|---|---|---|
| Customer with service location / site | ✓ (customer, building, system hierarchy in deficiency linkage) | ✓ (property, location, service history per location) | ✓ (Accounts = facilities/customers/locations) | ✓ (client, building, floor per door asset) | Universal — core |
| Recurring inspection program (series/agreements by frequency) | ✓ (inspection series engine; upcoming/overdue visibility; auto-shift on reschedule) | ✓ (inspection agreements, auto-scheduled visits by property/asset type/NFPA frequency) | ✓ (copy & reschedule folders; scheduled inspection services) | ✓ (recurring inspections implied via templates + portal history; scheduled inspections) | Universal — core (fire's organizing rhythm) |
| Inspection executed against standard/jurisdictional question sets | ✓ (NFPA/ULC/Title 19/Joint Commission/DNV/HFAP/city forms; question sets by system type + code year) | ✓ (NFPA 25/72 mapping; compliance checklists; custom workflows) | ✓ (forms per folder type; NFPA among standards; custom form builder) | ✓ (PAS 79 FRA template; fire door checklists; configurable templates) | Universal — core |
| Inspection report as formal deliverable | ✓ (branded one-click reports; NFPA vs Joint Commission formats; deficiencies-only; customer portal) | ✓ (reports attach to job automatically; AHJ submissions) | ✓ (folder reports with cover pages; summary/deficiency reports; customer portal) | ✓ (branded PDF reports; per-door/building reports) | Universal — core |
| Deficiency/finding as persistent tracked object until resolved | ✓ (auto-created per device/system; persists across the series until resolved; statuses; database + dashboard) | ✓ (deficiencies sync instantly; flagged deficiencies visible to office; quote in one click) | ✓ (priorities with roll-over to next folder; resolution tracking; show-resolved-on-reports) | ✓ (actions/remedials logged, assigned, managed) | Universal — core (the fire signature) |
| Deficiency → corrective work conversion | ✓ (proposals from deficiencies; work orders linked back to inspection) | ✓ (deficiency → quote → schedule → bill without re-entry) | ✓ (follow-up management options; one-form option for service calls + inspections) | ✓ (actions assignable; work-order module exists) | Universal — core |
| Technician coordination (schedule/dispatch/mobile) | ✓ (calendar/map/dispatch board; mobile app; offline) | ✓ (schedule & dispatch; mobile app; certification-aware smart dispatch) | ✓ (calendar; team scheduling; mobile app offline) | ✓ (mobile work-order module; offline implied) | Universal — core |
| Billing of completed work | ✓ (invoices from proposals/inspections/work orders; payments; QuickBooks/ERP) | ✓ (invoicing; financials; ERP sync) | ✓ (time/job costing; reporting; portal) — billing machinery lighter in fetched docs | ✓ (not in fetched fire-module docs; work-order module exists) | Universal — core (depth varies) |
| Asset/device registry with per-unit history | ✓ ("asset-based inspection engine"; 20M systems & assets; extinguisher swap/loaner) | ✓ (asset management; "system you install becomes the system you inspect") | ✓ (assets kept compliant; barcode/QR/RFID) | ✓ (fire door asset register with QR/barcodes, per-door history) | Universal — common (stronger here than in electrical pass; still not definitional) |
| Code/standards library as maintained content | ✓ (largest-library claim; maintained by in-house experts; updated to code-year) | ✓ (NFPA code mapping dynamic) | partial (NFPA among standards; forms are user-built) | partial (PAS 79 template; user-configurable) | Common; depth varies by product philosophy |
| AHJ / third-party compliance-platform delivery | ✓ (TCE, IROL, LivSafe integrations; batch submissions; auto-resolve in BRYCER/IROL) | ✓ (AHJ submissions named) | — (not observed) | — (UK regime: reports to clients/audits; no AHJ-platform layer observed) | Common (US pole); regional variant elsewhere |
| Certification-aware dispatch | — | ✓ (smart dispatch by tech certification) | — | — | Product-specific (BuildOps) — same finding as electrical pass |
| Offline mobile inspection | ✓ (explicit) | ✓ (mobile flow; offline implied) | ✓ (explicit) | ✓ (mobile-first; offline common in category) | Common — standard |
| Photo evidence with annotation | ✓ | ✓ (photos/videos on deficiencies) | ✓ (annotate, caption) | ✓ (annotate, markup) | Universal — standard |
| Customer portal | ✓ | — (not on fetched page) | ✓ | ✓ (web portal) | Common — standard |
| Price book / proposals / payments | ✓ | ✓ | partial (time/job costing; no price book observed) | — (not in fire module) | Common — standard (depth varies) |
| AI assistance | ✓ (Inspection Assistant; Assistant queries) | ✓ (OpsAI) | — | — | Optional; era-typical |
| Fleet/GPS | ✓ (Azuga-powered) | ✓ (Fleet+ add-on) | — | — | Optional |
| Operator type | fire protection contractors | commercial fire & life safety contractors | inspection service companies (multi-industry) | FM providers (fire safety as compliance duty) | Variant axis |

### What is actually fire-protection-specific (across sample)

1. **The recurring inspection program as the organizing rhythm** — inspections are scheduled as frequency-driven series/agreements per site/system (Inspect Point "inspection series"; BuildOps "inspection agreements… by NFPA frequency"; InspectAll folder copy/reschedule; Mobiess re-inspection cycles). In the electrical pass, recurring work existed as optional memberships; here the recurring inspection is the backbone of the service business and is code- or contract-mandated. [Layer A ×2 + Layer B ×2]
2. **The inspection record against standard/jurisdictional question sets** — inspections are executed against maintained code frameworks (NFPA, ULC, Title 19, healthcare accreditation, PAS 79, city forms) selected by system type and code year, producing a formal report. [Layer A ×2 + Layer B ×2]
3. **The deficiency as a persistent tracked object** — findings auto-created from inspection answers, tied to device/system, persisting across the inspection series until resolved, with statuses, and converting into proposals/work orders. The generic pole (InspectAll priorities with roll-over; Mobiess actions) shows the same structure without fire branding. [Layer A ×2 + Layer B ×2]
4. **Compliance reporting outward** — reports delivered to customers and to AHJs/third-party compliance platforms (TCE/Brycer, IROL, LivSafe), with deficiency status sync. [Layer A ×2; US-pole]
5. **Device/asset registries with per-unit inspection history** — stronger and more universal here than in the electrical sample (extinguishers, fire doors as individually tagged assets; "the system you install becomes the system you inspect"). [Layer B ×4]

No sampled product showed a structurally distinct object *beyond* this loop (no hydraulic-calculation object, no code-compliance engine that auto-derives requirements). The fire-specificity is the inspection–deficiency–compliance loop plus code content — not a different data model from field service.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

Held jointly — the fire protection service management system of record:

1. **Customer sites with protected systems** — work is performed at the customer's premises (buildings, facilities, campuses) where fire protection systems and devices live; jobs and inspections bind to those sites. (Remove → generic CRM/task tracking.)
2. **The recurring inspection program** — periodic inspections of those systems scheduled as a frequency-driven series or agreement per site/system, with visibility into upcoming/overdue work; this is the organizing rhythm of the fire protection service business. (Remove → generic field service management; the inspection backbone is what makes the business model recognizable.)
3. **The recorded inspection with persistent deficiencies** — an inspection executed against standard or jurisdictional question sets, producing a formal report; findings captured as deficiency records tied to the system/device, persisting across the series until resolved. (Remove → work-order-only FSM or a bare checklist tool; remove the persistence → a one-off inspection log.)
4. **Corrective work and billing** — deficiencies and service needs convert into proposals/work orders that are scheduled, assigned to technicians, performed, and billed (invoice/payment), with accounting sync at the mature pole. (Remove → an inspection log with no business operation.)

Remove the fire protection content (protected systems, code-driven inspections, life-safety semantics) → the generic Small Business Field Service Management Type. Remove the recurring program but keep one-off inspections → inspection software, not service management.

Historical check: a paper-era fire protection contractor (inspection contracts on a card file, clipboard question forms, hangtags on extinguishers, a deficiency list carried to the next visit, typed reports mailed to the owner and the fire marshal, invoices for inspection and repair) satisfies all four properties. UK fire-safety practice under a different regime (PAS 79 fire risk assessments, fire door registers) satisfies the same structure. The check passes; none of the modern machinery (code libraries as maintained content, offline apps, AHJ-platform integrations, AI, GPS) is definitional.

### Level 1 — Common Mature Structure

- Code/standards libraries and question sets maintained as content (NFPA/ULC/accreditation/jurisdictional; selected by system type and code year)
- Compliance report generation (branded, flexible formats incl. deficiencies-only) and delivery to customers via portal
- AHJ / third-party compliance-platform integrations (US pole: TCE/Brycer, IROL, LivSafe; batch submission, deficiency status sync/auto-resolve)
- Mobile inspection app: offline execution, quick/bulk inspect, photo capture with annotation, signatures
- Asset/device registry with per-unit inspection history; barcode/QR identification
- Proposals built from deficiencies (photos, notes, code references) with approval tracking
- Work orders with lifecycle (schedule → dispatch → perform → close out) and price books
- Customer notifications; customer portal with reports and payment
- Reporting/dashboards (inspections completed, deficiencies open/resolved, revenue)
- Accounting/ERP integration (QuickBooks at SMB pole; Sage/Viewpoint/NetSuite at commercial pole)

### Level 2 — Variant / Optional Structure

- Product packaging: fire pure-play vs commercial multi-trade suite vs multi-industry inspection platform vs FM-embedded module
- Regulatory regime: US NFPA ITM regime vs Canadian ULC vs UK fire-safety regime (PAS 79 FRAs, fire door registers, compartmentation) vs healthcare accreditation reporting (Joint Commission/DNV/HFAP)
- Certification-aware dispatch (single-product today — BuildOps; suspected trade practice)
- Extinguisher swap/loaner tracking; pump-curve capture; bulk inspection (field-efficiency specializations)
- Installation/project machinery at the commercial pole (the system you install becomes the system you inspect; project financials, WIP)
- Fleet/GPS tracking; payroll/time tracking; AI assistants (era-typical)
- Operator type: specialized fire contractor vs FM provider carrying fire-safety compliance duty

### Level 3 — Vendor-specific (kept out of the canonical document)

- Inspect Point: "inspection series" engine naming; Inspection Assistant / Inspect Point Assistant; extinguisher swap & loaner tracking; pump curve capture; Inspect Point Fleet (Azuga); stats (4.5M inspections, 20M assets); "largest inspection library" claim
- BuildOps: OpsAI; Inspect Point integration as the inspection engine; "system of action vs system of record" framing; Certified Fire customer metrics
- InspectAll: "Folders" as the work-unit name; "Priorities" as the deficiency name; Priority Roll-Over; three follow-up management options; Zapier integrations
- Mobiess: Insight/Asset Inspector module names; PAS 79 template packaging; Bellrock group context

## Vendor-specific Findings

See Level 3. Notable pattern: BuildOps — a commercial multi-trade suite — does not build its own fire inspection engine; it integrates Inspect Point and treats deficiencies as the sync currency between inspection and service/billing. This confirms that the inspection engine and the business-management spine are separable layers that the market also sells combined.

## Boundary Findings

1. **vs Small Business Field Service Management / trade siblings (HVAC, plumbing, electrical, elevator)** — the field-service spine (customer+site → job lifecycle → technician coordination → billing) is shared and verified. The durable difference: fire protection carries a *structurally distinct* trade object — the code-mandated recurring inspection program with persistent deficiencies and outward compliance reporting. The electrical pass explicitly found no such object for electrical (trade difference there is configuration/content); fire protection does have one. This makes the fire leaf more defensible as an independent Type within the family than a pure trade-tuning case — while the probable trade-Variant relationship to Small Business FSM (flagged in the electrical and cleaning passes) still deserves joint review.
2. **vs Elevator Service Management (§29 sibling, unprocessed)** — expected same pattern (code-mandated periodic inspections, certificates, deficiencies); cross-reference when processed.
3. **vs Fire Department Records / Operations System (§24)** — naming trap: both say "fire." Fire department systems serve government emergency-response agencies (incidents, apparatus, personnel); this Type serves private fire protection contractors maintaining prevention systems in customer buildings. Different operator, different objects, different money flow entirely.
4. **vs CMMS / Enterprise Asset Management** — CMMS/EAM manages assets owned by the software operator; here the protected systems are customer-owned; the contractor holds inspection/service history *about* them. The device registry is a record about customer property, not an owned-asset registry.
5. **vs Construction Project Management** — fire protection installation (new sprinkler/alarm fit-outs) is project work; commercial-pole products bundle project machinery ("the system you install becomes the system you inspect"). The service-management center (inspection loop + dispatched service) remains the Type's center; installation projects belong to the construction side.
6. **vs Property Inspection Application** — home/property inspections are one-off real-estate transaction reports; here inspections are recurring compliance events against maintained systems with deficiency follow-through. Different object, different lifecycle.
7. **vs AHJ-side compliance platforms (The Compliance Engine/Brycer, LivSafe, IROL)** — those platforms aggregate inspection reports for authorities having jurisdiction; they are delivery targets/companions of this Type, not the Type itself.
8. **vs Environmental Compliance Management / EHS Platform** — different regulated domain; InspectAll demonstrates the shared generic inspection structure across domains, but the fire Type's objects (protected systems, deficiencies, AHJ reporting) are fire-specific.
9. **vs Appointment Scheduling Application** — scheduling is one fragment; this Type is the whole business operation.
10. **vs Field Inspection Software (generic)** — InspectAll/Mobiess show the generic inspection structure; fire protection service management = that structure bound to the fire trade's code frameworks, deficiency semantics, and the contractor's full business operation (billing, customers, technicians).

## Uncertainties

1. **ServiceTrade** — a major fire-protection-focused platform — unreachable (403 ×3). Market-coverage gap; assertions calibrated to the four researched products. ServiceTrade's known positioning (commercial service contractors incl. fire protection) could not be verified from primary sources this pass.
2. **ZenFire, Simpro** unreachable (empty/403) — SMB and AU/UK regional poles under-sampled; the UK pole is represented only by Mobiess (an FM-side module, not a contractor pure-play).
3. **No Tier-1 help-center docs fetched for Inspect Point or BuildOps** — claims rest on product pages with operational FAQs (rich but marketing-adjacent). InspectAll provides the Tier-1 anchor for the generic structure.
4. **Exact code frequencies** (which systems require monthly/quarterly/annual inspection) — products reference "NFPA frequency" generically; no precise frequency table was documented in fetched sources; deliberately not stated.
5. **Recurring billing machinery for inspection agreements** — strongly implied (inspection series + invoicing + "recurring maintenance contracts" dashboard) but not directly documented as agreement-to-invoice automation in fetched sources; kept as standard capability without specifics.
6. **Certification/licensing tracking of technicians** — BuildOps documents certification-aware dispatch; whether products track license expiry/renewal as records was not observed; not claimed.
7. **Regional markets beyond US/UK** (e.g., AU after-simpro, EU regimes) — not verified; canonical document avoids region-specific claims beyond the US/UK contrast observed.

## Final Synthesis

Fire Protection Service Management is the business-management system of a fire protection / fire & life safety service contractor. Its defining core is the field-service spine (customer sites with protected systems → work orders carried through a lifecycle by coordinated technicians → billing) bound together with the trade's signature loop: a recurring, frequency-driven inspection program over those systems; inspections executed against standard or jurisdictional question sets and recorded as formal reports; deficiencies captured as persistent records tied to systems/devices that survive across inspection cycles until resolved; and deficiencies converting into corrective work that is scheduled, performed, and billed — with reports delivered outward to customers and, in the US regime, to AHJs and third-party compliance platforms. Everything else commonly associated with these products (code libraries as maintained content, offline mobile inspection apps, device registries with per-unit history, portals, price books, certification-aware dispatch, AI, GPS) is standard or optional capability layered on this structure. The leaf is the fire-trade instantiation of the field-service-management family — distinguishable from its siblings by a genuinely structural trade object (the inspection–deficiency–compliance loop), not merely by content tuning.
