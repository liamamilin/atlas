# Research Notes — Equipment Administration Platform

Leaf: Equipment Administration Platform (DIRECTORY §10 Enterprise Operations & Administration)
Slug: equipment-administration-platform
Research date: 2026-09-06
Methodology: WORKFLOW v1.1 (10-step process; evidence layers A/B/C; abstraction levels L0–L3)

## Research Goal

Understand what "equipment administration" software actually is in the market: what object structure it centers on, what the daily operational loop is, how it differs from the neighboring registry / maintenance / IT-asset / inventory / rental types, and which capabilities are defining vs common vs variant.

## Initial Boundary (working hypotheses before research)

- Hypothesis A: a platform for administering an organization's physical equipment — laptops, cameras, tools, machines, radios, medical devices — as individually identified items with custody (who has it / where), state (available / in use / maintenance / retired) and lifecycle (acquire → use → maintain → dispose).
- Hypothesis B: nearest neighbors are Enterprise Asset Registry (§10 sibling, processed 2026-09-06), CMMS/EAM (§16), Tool Management (§16), IT Asset Management (§14), Inventory Management System (§10), Fleet Management System (§18), equipment rental software (EZRentOut-class), Durable Medical Equipment Management (§22).
- Hypothesis C (risk): the leaf may be near-duplicate of Enterprise Asset Registry — that pass explicitly flagged expected heavy overlap and left a test: "if the sibling pass finds circulation workflow without a durable per-item record system at the center, the two remain separable Types."
- Hypothesis D: the market label for this cluster is likely "equipment management / equipment tracking / asset tracking software", not the literal leaf name (same phenomenon the registry pass recorded).

## Research Questions

1. What is the central record, and what identity does an item carry (serial, QR/barcode, RFID)?
2. What custody/handover operations exist (checkout, check-in, assignment, transfer, reservation)?
3. What per-item state does the system track and how does it advance?
4. How does maintenance attach to the circulation loop (flag on return, block availability, work orders)?
5. How are availability and conflicts handled (no double-booking)?
6. What self-service surfaces exist for equipment users (portal, booking, requests)?
7. What administrative machinery surrounds the loop (audits/stocktaking, roles, notifications, reports, custom fields, locations, kits)?
8. Where do financials (depreciation, procurement), sensors (GPS/RFID/telematics) and rentals sit — core or variant?
9. What is the honest boundary against the Enterprise Asset Registry sibling (answering its joint-review flag)?
10. Do older / pre-digital / regional implementations still fit the abstraction?

## Representative Products

| Product | Why sampled | Tier | Evidence |
|---|---|---|---|
| Cheqroom | "Equipment Operations Platform"; circulation-first philosophy (bookings/checkouts/custody); media/AV/education/corporate; strong help center | mid-market → enterprise | A (product site + help center, fetched) |
| EZO / EZOfficeInventory | asset-operations posture with full custody chain + maintenance; product family explicitly splits ITAM (AssetSonar), CMMS (EZO CMMS), rental (EZRentOut) — boundary evidence | mid-market → enterprise | A (product pages, fetched) |
| Sortly | inventory-first philosophy; equipment tracking as a use case inside an inventory app; SMB tier; straddle test | SMB | A (product site + equipment-tracking page, fetched) |
| Timly | European (DACH) equipment/inventory administration; trades/construction/public-sector mix; assignment/return/transfer emphasis | SMB → mid-market | A (product site, fetched) |

Coverage check: 4 products, 4 philosophies (circulation-first / asset-operations / inventory-first / administrative assignment), 3 customer tiers, 2 regions (US-market + DACH). Two products (EZO, Sortly) overlap with the registry pass's sample — useful for the joint-review answer. Stop condition reached: new products would repeat existing evidence (the cluster is well-covered by these four plus the registry pass's Snipe-IT / Asset Panda).

## Sources

All fetched 2026-09-06, evidence layer A (official vendor surfaces):

- Cheqroom — https://www.cheqroom.com/ (homepage; positioning, capabilities, custody language)
- Cheqroom Help Center — https://help.cheqroom.com/ and https://knowledge.cheqroom.com/helpcenter/managing-equipment (section taxonomy: Item Statuses, Kits & Bulk Items, Labels/Barcodes/Scanning, Maintenance & Work Orders, RFID, Spotchecks, Bookings & Scheduling [Booking Portal / Booking Rules & Availability / Check-outs & Check-ins / Custody & Long-term Loans / Reservations], Users & Access, Reporting & Documents)
- EZO — https://ezo.io/ (family page: EZO vs AssetSonar vs EZO CMMS vs EZRentOut) and https://ezo.io/ezofficeinventory/ (Track/Move/Maintain/Control pillars, modules, FAQ)
- Sortly — https://www.sortly.com/ and https://www.sortly.com/solutions/asset-tracking-software/equipment-tracking/ (features list incl. Check-in/Check-out, Jobs, alerts, labels)
- Timly — https://timly.com/en/ (solutions: Asset Tracking, Tool Management, Maintenance & Servicing, Stocktaking, Live Tracking, Internal Ordering, Resource Scheduling; features: Assignment-Return-Transfer, Digital Signature, Custom Roles, Barcode Scanner, Direct-Access Labels)

No source failed; no evidence degradation required. Note: vendor numeric claims on homepages (45% fewer lost assets, 75% fewer failures, 500% ROI) are marketing figures and were not carried into the canonical document.

## Product A — Cheqroom (evidence layer A)

### Key observations

- Positioning: "The Equipment Operations Platform for Teams that Deliver"; "From procurement to disposal and everything in between"; self-description as "the equipment management platform built for teams where gear moves, gets shared, needs maintenance – and has to come back ready to work."
- Problem framing is custody-shaped: "Do you know who's using your assets? When it's due back? Who had it last?"
- Full Chain of Custody: "Digital check-in/out with signatures, QR scanning, automatic audit trails, and GPS tracking."
- Reservations: "Instantly see what's available; reserve gear or spaces in advance; ensure no one else takes what you reserved; configure user access, permissions, and booking rules." Plus "no double bookings."
- Maintenance: "Flag issues on return or on site, schedule repairs, block broken items from booking, create tickets, and manage work orders."
- Lifecycle: Acquire and Dispose capability ("procurement to disposal"); Lifecycle Management from "procurement and onboarding to maintenance, audits, and disposal."
- Help center structure (Tier 1): Managing Equipment (Adding & Organizing Items — item types, categories, custom fields, locations & sublocations, item statuses; Kits & Bulk Items — kits, locked kits, bulk vs individual, consumables; Labels, Barcodes & Scanning — QR generation, DYMO/Zebra printers, USB/Bluetooth scanners, RFID, geo position; Maintenance & Work Orders — preventive maintenance work orders, operations requests for maintenance/procurement/logistics/event-prep/calibration, flags for equipment state, warranty dates; RFID; Spotchecks for audits) + Bookings & Scheduling (Booking Portal, Booking Rules & Availability, Check-outs & Check-ins, Custody & Long-term Loans, Reservations) + Users & Access (roles & permissions, equipment access & field visibility, SSO & user sync) + Reporting & Documents (PDF documents & templates).
- Inventory duality: tracks "stock levels and consumables" alongside individually identified assets (bulk items vs individual items distinction; consuming bulk items within kits).
- Industries: broadcast, entertainment, production, higher education, worship, device manufacturers, corporate, sports, government, industrial. Education use case includes student self-serve booking.
- Vendor-branded (L3): Intelligent Resource Orchestration (IRO), predictive availability forecasting, Spotchecks, ATA Carnet generation, workspaces.

## Product B — EZO / EZOfficeInventory (evidence layer A)

### Key observations

- Family structure is itself boundary evidence: EZO (physical asset management) vs AssetSonar (ITAM) vs EZO CMMS (maintenance operations) vs EZRentOut (equipment rental). Same vendor draws the ITAM / CMMS / rental lines as separate products.
- EZO positioning: "Enterprise Asset Management Software & CMMS"; "Every Asset. Right Hands. Right Time. Right State."
- Status vocabulary directly observed: "See every asset across every site – checked out, in transit, under maintenance, or available."
- Four pillars: TRACK (fetch asset details; checked out/in transit/under maintenance/available), MOVE ("Request, approve, dispatch, and confirm receipt with a full custody chain. Give employees a self serve equipment portal. Route multi-tier approvals"), MAINTAIN ("Schedule preventive maintenance, enforce checklists, and convert field reports into work orders"), CONTROL ("Every checkout, return, transfer, and repair tied to the asset record. Flag damage, track condition, and pull the complete history of any item").
- Modules: Asset Tagging (GPS + telematics + barcode/QR/RFID scans), Equipment Booking (requests, availability check, reservations, approvals, "without double-booking"), Full Chain of Custody ("Move assets through checkout, handoff, return, and recovery… who received it, when it moved, where it is expected to be returned, and what action was taken"), Maintenance/CMMS (PM schedules, work orders, technicians, "hold back equipment that is unsafe, damaged, or due for service before it goes back into the field"), Inventory Control (bulk items, consumables, low-stock alerts), Workflow engine ("route approvals, escalate overdue check-ins, update asset statuses, trigger work orders for flagged returns, and send low-stock alerts"), Access Controls ("who can view, request, check out, move, or manage items by role, location, or responsibility").
- FAQ confirms: structured check-in/check-out across warehouses/departments/campuses/job sites; depreciation and asset value over time; full lifecycle "procurement, assignment, maintenance, audits, retirement, and disposal"; asset records hold "custody history, maintenance activity, condition updates, documents, depreciation, and service records"; deeper ITAM stays in the AssetSonar sibling.
- Integrations observed: service desks (Zendesk, Jira), SSO (Okta, OneLogin, SAML, Azure AD), GPS/telematics (Samsara, Trackunit, John Deere, Hapn).
- Vendor-branded (L3): Zoe AI copilot, Catalog Optimizer, Quick Action Center.

## Product C — Sortly (evidence layer A)

### Key observations

- Inventory-first positioning: "Simple Inventory Management Software… to manage their physical inventory, including supplies, materials, tools, and equipment." Equipment tracking is a use-case page under Asset Tracking, which is itself a solution inside the inventory app.
- Equipment page promises: "Know exactly where your equipment is, even if it frequently changes locations or hands"; "Scan equipment in and out with the in-app barcode and QR code scanner"; photos to "document its condition"; custom fields (manufacturer, serial number); attach manuals.
- Alerts: date-based (warranty end, maintenance/repair scheduling) and quantity thresholds; in-app + email notifications.
- Feature list (observed): Check-in/Check-out ("ensure they're returned to the correct locations"), Jobs ("track the parts, tools, equipment, supplies, and materials tied to each job, project, work order, ticket, or request"), Pick Lists, custom folders, custom fields, activity history ("who did what, and when"), customizable user access, label generation, barcode/QR scanning, reports (activity, move summary, item flow, transaction, inventory summary, low stock), purchase orders, QuickBooks integration, offline mobile, SSO, API.
- Straddle evidence: reservations/approval machinery not prominent; check-in/check-out present but the product's center is the visual inventory (folders, photos, quantities). Confirms the record-mode vs circulation-mode spectrum.
- SMB tier; consumer-grade simplicity ("no trainings or manuals required"); industries: construction, medical, warehouse, education, events, government, aviation, etc.

## Product D — Timly (evidence layer A)

### Key observations

- Positioning: "Inventory Management Software" / "asset management software" with a dedicated Equipment Management / Tool Management solution line; cloud, web + mobile app; DACH/European market (GDPR, EU hosting emphasized).
- "Track and Inventory Everything: From a paperclip to a construction crane, everything is managed centrally" — flexible categories, modular setup.
- Assignment model: "inventory is assigned directly to resources such as employees, locations, containers, projects, and other areas" — "Assignment, Return, Transfer: Assign inventory individually or in larger quantities using a barcode scanner, hand it over directly, or take it back with just a few steps." Digital signature on movements ("Document every signature and store it without gaps").
- Maintenance: "Report defects via app and automatically delegate them as tickets"; "Centrally plan recurring maintenance and trigger deadlines, intervals, and inspections on time"; integrated ticketing; audit-proof documentation; repair-vs-replace decision support.
- Additional solution lines: Stocktaking (digital inventory counts, on a date or continuous), Live Tracking (GPS/Bluetooth trackers), Internal Ordering (internal inventory orders, reservations, delivery notes/transport slips), Resource Scheduling & Deployment ("Reserve items in advance and assign them to projects or employees"), Warehouse Management (consumables/stock levels).
- Identification: QR/barcode scanning without extra hardware; RFID/Bluetooth; "Direct-Access Labels" let third parties (service partners, customers) report damage/tickets via QR scan without login (vendor-specific).
- Access: custom roles with granular permissions over inventory, staff, tickets; multi-client/multi-location capability.
- Industries: trades & services, construction, public administration, education, healthcare, hospitality. Customer stories describe replacing paper/magnetic-board inventory ("From Paper to Digital", "No More Magnets"), yearly stocktakes of furniture and keys.
- Vendor-branded (L3): Direct-Access Labels, Timly AI, DAT integration, switching service.

## Cross-product Comparison

| Structure / capability | Cheqroom | EZO | Sortly | Timly | Reading |
|---|---|---|---|---|---|
| Individually identified item records (serial/asset ID) | ✓ | ✓ | ✓ | ✓ | defining-core candidate |
| Physical identification: QR/barcode labels + scanning | ✓ (QR gen, printers, scanners, RFID) | ✓ (barcode/QR/RFID gen or import) | ✓ (label gen + in-app scanner) | ✓ (QR/RFID/BT, no extra hardware) | defining-core candidate (identification mechanism; form varies) |
| Custody/handover events (checkout/check-in, assignment, transfer, return) | ✓ (checkouts, custody & long-term loans, signatures) | ✓ (full custody chain; "tied to the asset record") | ✓ (check-in/check-out) | ✓ (assignment/return/transfer + digital signature) | defining-core candidate |
| Per-item state incl. availability (available / checked out / maintenance / retired) | ✓ (Item Statuses; flags; block booking) | ✓ ("checked out, in transit, under maintenance, or available") | ✓ (implicit; condition via photos; date alerts) | ✓ (condition + availability + readiness) | defining-core candidate (conceptual states; labels vary) |
| Reservations / advance booking with availability rules | ✓ (reservations, booking rules, no double bookings) | ✓ (request portal, reservations, approvals) | — (not prominent) | ✓ (resource scheduling, internal ordering reservations) | common mature structure, not universal → not defining |
| Self-service portal for equipment users | ✓ (booking portal, student self-serve) | ✓ (employee self-serve equipment portal) | — (user access levels only) | ✓ (internal ordering; third-party QR reporting) | common, varies |
| Maintenance attached to items (schedules, service records, work orders/tickets) | ✓ (PM work orders, operations requests, flags) | ✓ (PM, work orders, hold-back) | ◐ (date-based alerts only) | ✓ (ticketing, intervals, inspections) | common; depth is a spectrum (L1, depth varies) |
| Locations & sub-locations | ✓ | ✓ | ✓ (folders by location) | ✓ (multi-client, locations) | common |
| Custom fields & categories | ✓ | ✓ | ✓ | ✓ ("flexible category structures") | common |
| Kits / grouping / containers | ✓ (kits, locked kits) | ◐ (not directly observed in fetched pages) | ◐ (pick lists, jobs as grouping) | ◐ (containers) | common pattern, forms vary → L1/L2 boundary; keep qualified |
| Audits / stocktaking / counts | ✓ (Spotchecks, RFID spotchecks) | ✓ (audits in FAQ) | ✓ (inventory lists, move/transaction reports) | ✓ (Stocktaking line) | common |
| Consumables/bulk alongside equipment | ✓ (bulk items, consumables) | ✓ (inventory control, low stock) | ✓ (quantities native) | ✓ (warehouse/consumables) | common dual record-mode |
| Roles & permissions | ✓ | ✓ (view/request/checkout/move/manage by role/location) | ✓ (customizable access) | ✓ (custom roles) | common |
| Notifications (overdue, service due, low stock) | ✓ | ✓ (escalate overdue check-ins) | ✓ | ✓ | common |
| Documents/attachments per item | ✓ (files to equipment/bookings/contacts) | ✓ (documents on record) | ✓ (manuals) | ✓ (documents on items) | common |
| Reporting / activity history | ✓ | ✓ | ✓ (activity/flow reports) | ✓ (usage data) | common |
| Financial layer (depreciation, POs, cost) | ✓ (acquire & dispose) | ✓ (depreciation) | ◐ (purchase orders; cost fields) | ◐ (not prominent) | optional/variant |
| GPS / telematics / live tracking | ✓ (GPS) | ✓ (Samsara/Trackunit/John Deere) | — | ✓ (GPS/BT trackers) | optional |
| Approvals / request workflows | ✓ (operation requests) | ✓ (multi-tier approvals) | — | ✓ (internal ordering flow) | optional |
| Calibration / certification | ✓ (calibration workflow) | ✓ (calibration alerts) | — | ✓ (deadlines, inspections, training mgmt) | optional |
| External rental / invoicing | ◐ (invoicing workflow) | separated into EZRentOut | — | — | variant; rental business is a different type |
| AI assistance | ✓ (IRO, predictive availability) | ✓ (Zoe) | — | ✓ (Timly AI) | optional |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant (minimal)

An Equipment Administration Platform is recognizable when all of the following hold:

1. **Individually identified equipment records** — the organization's movable/durable equipment exists in the system as discrete, addressable item records (each with its own identity), not merely as stock quantities.
2. **Tracked custody and availability per item, advanced by recorded handovers** — for each item the system holds where it is / who holds it / whether it can be handed out next, and that state changes through recorded events (assign/checkout/hand over, return/transfer/receive), not through silent edits.
3. **Lifecycle state across the item's service life** — the record persists and its state advances from entry into service through use (including out-of-service states such as under maintenance / unavailable) to eventual retirement/disposal, so the pool stays findable, accountable and reusable.

Nothing else is required. Minimal test: a paper sign-out sheet over a numbered equipment list satisfies all three (identified items, handover lines, availability implied by who holds it) — which is exactly the predecessor artifact the sampled vendors name ("replace the spreadsheets, sign-out sheets"; "From Paper to Digital"; "manual Access database"). Conversely: remove per-item identity → stock inventory; remove handover/availability tracking → a static fixed-asset register; remove lifecycle/state → a label spreadsheet. Each removal lands in a different Type.

### L1 — Common Mature Structure (very common, not defining)

- reservation/booking with availability rules and no-double-booking conflict handling
- self-service request/booking portal for equipment users (employees, students, crews)
- maintenance attached to the item: schedules, service records, defect flags on return, work orders/tickets, hold-back from availability (depth varies from alerts to full work orders)
- physical identification machinery: QR/barcode generation and label printing, mobile scanning, optionally RFID
- locations and sub-locations (rooms, sites, trucks, containers)
- custom fields, categories/item types, per-item documents (manuals, warranties)
- consumables/bulk items tracked alongside individually identified equipment (dual record mode)
- audits/stocktaking and reconciliation of records vs physical reality
- roles & permissions (who can view/request/checkout/move/manage), scoped by location/team
- notifications: overdue returns, due service/warranty dates, low stock
- reporting and per-item/per-user activity history

### L2 — Variant / Optional Structure

- financial layer: acquisition cost, depreciation, purchase orders, disposal records (depth varies; plan- and segment-dependent)
- sensors & automation: GPS position capture, telematics feeds, Bluetooth/RFID live tracking
- request/approval workflows for checkout or allocation (multi-tier approvals)
- calibration / inspection / certification tracking (regulated tools & instruments)
- regional/regulatory posture: e.g. EU hosting/GDPR emphasis; public-sector accountability framing
- industry overlays: AV/media & broadcast, education media centers, construction tools, healthcare, government
- AI assistance (predictive availability, copilots)
- external-facing extensions: rental-style invoicing, third-party reporting via public QR access — adjacent to the rental Type
- deployment: multi-tenant cloud (dominant) vs on-prem/self-hosted; per-item vs per-user licensing

### L3 — Vendor-specific Structure (research notes only)

- Cheqroom: Spotchecks, Intelligent Resource Orchestration (IRO), predictive availability forecasting, ATA Carnet generation, workspaces, locked kits
- EZO: Zoe AI copilot, Catalog Optimizer, Quick Action Center, hardware signature-pad integration
- Sortly: photos-first visual inventory, Pick Lists, Jobs object, offline-first mobile
- Timly: Direct-Access Labels (loginless third-party QR access), DAT integration, switching service

## Rejected Findings (considered and rejected as defining)

- **Reservations/booking** — present in 3 of 4 sampled products, but absent/dim in the inventory-first sample member; historically sign-out without reservation was the norm. Kept L1.
- **QR-code identification specifically** — historically labels/barcodes/serials preceded QR; the invariant is per-item identification, QR is the current dominant implementation.
- **Mobile app** — the loop works desk-side (historically did); mobile is the current dominant surface, L1.
- **Maintenance machinery** — full work orders are product-dependent (Sortly has date alerts only); only the out-of-service *state* is invariant, not the maintenance program depth.
- **Depreciation/financials** — plan- and segment-dependent; the registry record layer carries finance in some products, not others.
- **"Asset operations platform" / "asset intelligence" marketing category** — vendor positioning language, not structure.
- **Multi-site scale** — single-closet deployments (a school media desk) fit L0 fully.

## Boundary Findings

1. **vs Enterprise Asset Registry (§10 sibling; answering its joint-review flag).** Overlap confirmed and substantial: all four sampled products carry a durable per-item record system *and* circulation machinery; market labels are shared ("asset tracking", "equipment management software"). The registry pass's test is answered as follows: circulation workflow in this cluster is never observed *without* a durable per-item record system underneath — the record is always the backbone. The honest distinction is therefore one of **center of gravity**, not of presence/absence: the registry Type centers on the enterprise's record of holdings (audit, verification, financial fields; custody flows bind to the record), while Equipment Administration centers on running the circulation/readiness loop as the primary job (reserve → hand out → use → return → service → re-circulate; availability and accountability are the product's reason to exist). Products straddle (EZO leans record+custody; Cheqroom leans circulation; Sortly leans record/inventory). Two separable Types remain defensible only under this center-of-gravity reading; the joint-review flag stands and should be resolved by the taxonomy owner (merge, or keep as emphasis-pair). Recorded in STATUS.md.
2. **vs CMMS / Maintenance Management and EAM (§16).** Here maintenance is a readiness constraint on circulation (flag on return, block booking, service before re-loan); in CMMS/EAM maintenance programs and work orders are the primary job for asset uptime. Directly observed vendor-family split: EZO ships EZO CMMS as a separate product line; Cheqroom markets a CMMS use-case page but frames itself as equipment operations. Gradient, not wall.
3. **vs IT Asset Management (§14).** ITAM scopes to the IT estate (hardware + software licenses + discovery agents + ITSM integration); equipment administration is cross-domain physical gear. Directly observed vendor-family split (EZO vs AssetSonar); EZO's own FAQ routes deeper ITAM to AssetSonar.
4. **vs Inventory Management System (§10).** Record mode: quantities of stock vs identity of items. All sampled products support both modes (consumables alongside equipment); what makes this Type is the individually identified item with custody. Sortly sits nearest the inventory pole in the sample.
5. **vs Equipment rental (EZRentOut-class; not a leaf in this section).** Rental centers on external customers, quotes/orders/invoicing/rental revenue; equipment administration centers on internal circulation without commercial order machinery. Vendor-family split directly observed (EZO vs EZRentOut).
6. **vs Fleet Management System (§18).** Fleet centers on vehicles as operated units (drivers, telematics, compliance/HOS, routes); equipment administration covers general gear, where telematics/GPS are optional attachments rather than the core record.
7. **vs Tool Management (§16).** Tool management is the manufacturing/trades overlay of the same structure (tool cribs, calibration, machine-adjacent tooling). Timly spans both vocabularies on one site ("Tool Management" solution line under equipment management). Likely best treated as a segment overlay / near-variant; flagged lightly.
8. **vs Enterprise Request Management / Resource Scheduling.** The request/approval flow is one stage inside the circulation loop here; those Types center on the request or the schedule itself across resource kinds.

## Historical / Market-Sample Check

Would older, regional, platform-native or differently positioned products still fit the L0?

- **Paper/card predecessors** — sign-out binders, card systems, magnetic tool boards, whiteboards, Access databases, spreadsheets: all satisfy L0 (numbered identified items, handover lines naming person+date, implicit availability from who holds it). The sampled vendors themselves name these artifacts as what they replace ("replace the spreadsheets, sign-out sheets, and siloed tools"; "From Paper to Digital"; "No More Magnets"; "manual Access database bottleneck").
- **University equipment desks / media centers** (long-standing institutional users) — fit without reservations machinery, without financial modules.
- **Factory tool cribs** — fit with the tool-management overlay; identity + handover + condition remain the core.
- **Regional products** (Timly as DACH sample) — fit without any US-specific compliance or financial machinery.

Conclusion: L0 is not over-fitted to the modern QR + cloud + mobile implementation. The definition holds for pre-digital practice, which is the correct historical anchor for this Type.

## Uncertainties

- Sortly's checkout/reservation depth (plan-gated) was not verified against its help center; Sortly's placement near the inventory pole is based on product-site evidence only.
- Kits/containers grouping was directly observed as first-class only in Cheqroom; for EZO/Timly the observation is partial (containers, pick lists) — kept qualified in L1.
- Exact per-product status vocabularies (e.g. Cheqroom's item status list) were not fetched item-by-item; canonical states are written conceptually, product labels differ.
- Financial depth (depreciation UX) asserted qualitatively from EZO FAQ; not exercised.
- The Enterprise Asset Registry joint review remains open — this pass provides the sibling answer but the merge/keep decision belongs to the taxonomy owner.

## Final Synthesis

An Equipment Administration Platform is the operational system for an organization's shared physical equipment: individually identified items, each with tracked custody and availability advanced by recorded handovers (reserve/assign → use → return/transfer), maintained in a serviceable state and eventually retired, so the equipment pool stays findable, accountable, and reusable. The durable per-item record is the substrate (shared with the Enterprise Asset Registry Type); what defines this Type is the circulation-and-readiness loop run on top of it as the primary job. Around that loop, mature products add reservations with conflict rules, self-service portals, scan-based identification, maintenance attached to returns, audits, roles, notifications and dual record modes for consumables; financials, sensors, approvals, calibration and AI are variants; rental-style commerce, maintenance-program depth and IT-estate scoping cross into neighboring Types.
