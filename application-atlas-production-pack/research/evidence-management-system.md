# Research Notes — Evidence Management System

Research date: 2026-09-07
Directory leaf: Evidence Management System (§24 Government, Public Sector & Civic, between Law Enforcement Case Management and Corrections Management System)
Slug: evidence-management-system

---

## Research Goal

Understand, from real products, what an Evidence Management System (EMS) in the public-safety/justice domain actually is: its core objects, its custody model, its lifecycle from intake to disposition, the rules that make it distinct from inventory/asset tracking, and where its boundary lies against neighboring Types (Law Enforcement Case Management, eDiscovery, Records Management, asset systems).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the leaf is the law-enforcement "property & evidence" custody system — the system of record for physical and digital items an agency holds because of their role in a case, with an unbroken recorded chain of custody and legally gated disposition.
- Likely confusions:
  - Law Enforcement Case Management (case records vs item custody)
  - eDiscovery / Legal Hold Management (corporate ESI preservation vs agency custody)
  - Enterprise Records Management (retention of documents vs custody of items)
  - Asset/inventory tracking (items for use vs items held as proof)
- Unknowns going in: how the digital-evidence-only pole (DEMS) structurally relates to physical property-room systems; whether RMS-embedded modules are structurally the same; lab-side evidence handling depth.

## Research Questions

1. What is the evidence item record — identity, attributes, categories, media?
2. How is chain of custody modeled (events, signatures, scan history, immutability)?
3. What is the circulation lifecycle: check-out / check-in / move / transfer, expected returns, verification?
4. How do items anchor to cases and persons (one item ↔ many cases)?
5. How is storage modeled (locations, containers, location-scoped permissions)?
6. How does disposition work (retention, review, authorization gates, methods, correction paths)?
7. How does the digital-evidence pole differ (hashing, access-event custody, ingestion, redaction, disclosure)?
8. Who uses the system (custodians, officers, investigators, prosecutors, admins, public) and on which surfaces?
9. What rules matter (append-only custody, prohibited-action triggers, audit/inventory discipline, access scoping)?
10. Where exactly is the edge vs inventory control, RMS case management, and records management?

## Representative Products

| Product | Vendor | Pole chosen | Evidence obtained |
|---|---|---|---|
| SAFE | Tracker Products | Dedicated property/evidence specialist, physical+digital, cloud (GovCloud) | Tier-1 support-guide structure + Tier-2 product/FAQ pages |
| EvidenceOnQ | FileOnQ | Dedicated property/evidence specialist, on-premises, configurable platform | Tier-2 feature-detailed product pages |
| Axon Evidence | Axon Enterprise | Digital-first cloud DEMS, camera-ecosystem ingestion | Tier-2 product page |
| Mark43 RMS | Mark43 | Suite-embedded (cloud RMS with evidence as a data domain) | Tier-2 root/RMS pages only — no operational detail |
| JusticeTrax | JusticeTrax | Lab-side evidence management (LIMS heritage) | UNREACHABLE (transport error ×2) — abandoned, no claims |

Selection rationale: two property-room specialists with different delivery philosophies (cloud vs on-prem; workflow-automation-led vs configurability-led), one digital-first platform pole, one suite-embedded pole; different customer tiers (specialists across local/state agencies; Axon enterprise-scale). JusticeTrax was to represent the lab-side pole; it failed twice and was dropped per source-abandonment rule.

## Sources

- https://www.trackerproducts.com/ (homepage, FAQ, feature comparison) — 2026-09-07
- https://guide.trackerproducts.com/home (SAFE Support Guide: full section tree; sub-pages embed linked documents whose bodies did not render) — 2026-09-07
- https://fileonq.com/ (homepage) — 2026-09-07
- https://fileonq.com/evidence-management-system/ (EvidenceOnQ product page, benefits/features, FAQ) — 2026-09-07
- https://www.axon.com/products/axon-evidence — 2026-09-07
- https://www.mark43.com/ and https://mark43.com/platform/mark43-rms/ — 2026-09-07
- https://www.justicetrax.com/ — transport error ×2 — 2026-09-07

Sourcing limitations:
- Tracker's individual help-article bodies are embedded Google Docs that did not render; evidence from that help center is structural (section/page titles + summaries) rather than procedural detail.
- FileOnQ support/training portals are login-gated; product pages are marketing-detailed but not operational manuals.
- Axon's help center not reached; product-page evidence only.
- Mark43's evidence module not documented at an accessible depth; representative name only.
- Consequently: no precise numeric limits, retention periods, fee schedules, or state-machine names are asserted anywhere from memory; anything not directly evidenced is kept generic or omitted.

---

## Product A — Tracker Products (SAFE)

### Key observations

Entity model (Evidence Layer A — direct observation of official support-guide structure):

- Top-level objects: **Case**, **Person**, **Item**; training sequence "Add Cases, People, Items", "Build a Complete Case".
- Case tabs: Basic Info, Persons, Items, Media, Notes, History. Case attributes include offense types, case number formatting, case officers (plural supported), required case forms.
- Item tabs: Cases (plural), Media, Notes, Tasks, **Chain of Custody**, **Scan History**, History. Item attributes include categories, "belongs to" person, custom data forms; items can be duplicated and **split** ("Item Splitting / Balancing" — implies quantity-bearing items).
- An item may belong to **multiple cases**, with a designated **primary case**; items can be removed from a case.
- **Containers** exist as objects (boxes); you can "scan and move containers" — container-level custody movement.
- **Storage Locations** are a first-class configured structure: adding/editing/creating/moving/printing labels for storage locations; a webinar states storage locations "only show what a User has access to" — location-scoped permissions.
- Media attaches to both cases and items, with media categories, shared media, mass downloads.

Transactions (Layer A):

- Item actions enumerated in the help center: **Check In, Check Out, Move, Transfer**, Check Out to Another Office, **Dispose**, **Undispose**.
- Transaction vocabularies are administrator-configured: **Checkout Reasons**, **Custody Reasons**, **Disposal Methods**, **Verification Settings**, **Expected Return Date Notifications**.
- Advanced search is organized **by transaction type**: searching for Disposals, Check-Ins, Check-Outs, Moves, Transfers — custody events are the query backbone of the system.
- Signature devices (Topaz pads) supported; scanning via handheld barcode scanners (Zebra/Socket) and mobile-app scanner; an article weighs "RFID v/s Barcoding (or both)" — identification technology is an implementation choice.
- Multi-organization operation: OrgID/ItemID numbering, switching offices, "Scanning Items from Another Office or Organization", **Org Item Sharing**.

Audit & verification (Layer A):

- Tools: **Inventory Reports**, **Random Audits**, **Discrepancy Reports** (dedicated webinar: "What are Discrepancy Reports, when and why should you use them, and how can you run them?"); manual inventory report buildable from any item search; mobile app supports inventory reports and random audits in the field.
- Item-level **Scan History** tab (scans as their own evidence layer distinct from custody actions).
- Every item carries History; complete audit trail is a headline homepage claim: "unbroken, court-admissible digital trail for every piece of evidence".

Disposition (Layer A structure; Layer A for mechanics at testimonial level):

- Settings pages: **Auto Disposition** and **Advanced Auto Disposition** (with dedicated training videos/webinar).
- Item action: Disposing of an Item; **Undispose an Item** exists (correction path — disposition is recorded but reversible through a controlled action, not silent).
- Searching for Disposals as a first-class query.
- Customer testimonial (homepage): "The auto-disposition feature allows us to purge items we no longer need with consistent reminders. After 90 days, officers and evidence custodians get notifications to review evidence with documentation to support the directive." (The 90-day figure is that agency's configuration — vendor/customer-specific, not canonical.)
- Homepage FAQ frames the category: "An effective EMS requires unbreakable chain of custody, communication between investigators and property room personnel, automated disposal approval, audits, and inventories." Also explicitly contrasts with "barcode-based inventory control" — a vendor-articulated boundary vs inventory systems.

Positioning & delivery (Layer A):

- "Evidence management software for Physical and Digital Evidence ... in one secure cloud platform built for court-defensible chain of custody and audit-ready reporting."
- Digital evidence handling: "SAFE captures, **hashes**, stores, and tracks digital files alongside physical evidence" — same chain of custody over both.
- Lifecycle statement: "collection and submission in the field, intake at the property room, internal transfers, secure storage of physical and digital items, and final disposition or release."
- AWS GovCloud hosting, SOC 2 Type II, CJIS-alignment claims; on-premise file servers supported for media; SAML SSO, MFA (Google Authenticator), IP whitelisting, time-out settings.
- Hardware ecosystem: Zebra printers, handheld scanners, signature pads; label/report builder (forms, labels, reports); custom data forms; widgets/dashboards; tasks with types/subtypes/escalation and supervisor control.
- Ecosystem breadth claim: agencies use it beyond law enforcement — "federal, state, and local government, plus military units, forensic labs, hospitals, museums, universities, and law firms that need defensible custody records" (Layer A as a claim; breadth not independently verified).
- RMS integrations documented (CentralSquare instances); **Evidence.com integration** (i.e., integration toward a digital-evidence platform is itself a supported seam).
- CALEA Data Storage Guidelines page exists — accreditation context is first-class.

---

## Product B — FileOnQ (EvidenceOnQ)

### Key observations

Stakeholder model (Layer A — vendor's own role enumeration):

- Patrol officers: "spend less time filling out bags and tags"; customized entry screens with **required fields** ensuring vital capture.
- Investigators: "easily organize the evidence in the case for presentation to the prosecutor."
- Evidence staff: "Barcode technology makes transactions fast, automated, and paperless. The **automated dispo process assigns a retention date** and sends out **automated requests for review**. Purge projects are efficient and streamlined..."
- Administration: "integrity ... protected with an **unalterable chain of custody**, and **random percentage audits** ensure policies and procedures are being followed"; accreditation standards explicitly referenced.
- **Prosecutors**: "can access evidence information as needed ... submit requests or **authorizations electronically**, such as requesting lab analysis or **approving the return of the item to the owner**" — external authorized parties act inside the system's workflow.
- **Victims/public** (via the vendor's separate Foundrop product): enter itemized stolen-property lists, report lost/found property — public-facing intake feeding the custody system.
- IT staff: ease of installation; the FAQ states the system is **on-premises** by default ("data is stored locally on a customer's server"; some customers host on VMware clouds).

Features (Layer A):

- "Unalterable Chain of Custody": "EvidenceOnQ makes the chain of custody automated and unalterable. A customized chain of custody report makes trial preparation accurate."
- Barcode technology as the transaction backbone; location barcodes; configurable barcode label design; reads most existing 1D and some 2D barcodes.
- Inventories and audits: "fast and accurate inventories using barcode technology. A detailed inventory report shows items **accounted for, missing, and in the wrong location**. **Random percentage audit** reports comply with accreditation standards."
- Automated notifications/triggers: "Specific criteria are built into 'triggers' that will take an action, such as an automated email to an officer if an item needs correction or **evidence has been checked out too long**. Triggers can also **stop a prohibited action**, such as **releasing drugs to an owner** or **destroying search warrant items without a court order**." — direct evidence of legally gated disposition and circulation rules.
- Single-screen transactions: "searching, scanning barcodes, transferring items, and obtaining signatures are made from one screen."
- User-group dashboards: officers see last cases + packaging instructions; evidence staff see "items in intake, evidence **pending destruction**, or the type of evidence being stored."
- User-configurable screens/fields/workflows/reports ("Every field is user-defined"); custom reports/statistics without IT assistance.
- Mobile PDA option, works **disconnected**: transfer items, transfer boxes, perform inventories, transfer items with a signature.
- RMS + digital evidence integration: "Our EvidenceOnQ and DigitalOnQ systems are integrated, keeping all types of evidence tightly connected"; integrations with RMS, lab systems, purchasing, towing/impound, court management ("integrate with ANY third-party software").

Positioning (Layer A claims):

- Pain list includes: duplicate paper documentation, difficulty determining item location, "time-consuming and inaccurate inventories", "**Overflowing inventory due to lack of purging**", "Dismissed cases due to **compromised chain of custody**", "Failure to meet accreditation requirements".
- Suite structure: EvidenceOnQ (physical evidence), DigitalOnQ (digital evidence), **Asset & Quartermaster Management System (separate product)**, SAMSONQ/TrackOnQ (sexual assault case/kit tracking), FoundropOnQ (public found property), forensic suite/crime scene management. — Asset management being a separate product supports the boundary between evidence custody and asset tracking.
- Marketing claim: "RMS evidence modules notoriously lack functionality and flexibility" (suite-vs-specialist pole conflict; treat as vendor rhetoric, but it evidences that the specialist-vs-module packaging axis exists).

---

## Product C — Axon Evidence

### Key observations (digital-first DEMS pole)

All Layer A (official product page):

- Positioning: "secure, cloud-based platform ... for capturing, search, review, redaction, and sharing" of **digital** evidence, "from call to closure".
- File integrity: "Each file uploaded to Axon Evidence is assigned a **unique digital fingerprint** that validates the file's authenticity and confirms it remains unchanged during upload or playback" — hashing is the digital analog of physical tamper-evidence.
- Chain of custody for digital items: "Every action on a file, whether **viewing, editing, or downloading**, is automatically recorded in a detailed **audit trail**, supporting its credibility and admissibility in court." — custody events generalize to access events for digital items.
- Ingestion: from Axon cameras, **public submissions**, and third-party systems; "Auto-Tagging" organizes files on arrival.
- Review surface: search, review, **redaction** (framed against FOIA/public-records requests), transcription.
- Sharing/disclosure: "prep disclosure early"; sharing with investigators/prosecution implied by user roles (Investigators, Officers, Admins & Staff, Command Staff).
- Security: CJIS requirements, encryption in transit and at rest.
- Access control: "Agency administrators can manage who has access to evidence and which features they can use. Permissions can be tailored by role or user type."
- Note: no physical-item custody language appears on the page — this pole evidences the digital realization of the same custody logic (identity, integrity, recorded access, controlled sharing) without physical storage semantics. Retention/deletion specifics for digital items were not documented on the fetched page — not asserted.

---

## Product D — Mark43 RMS (suite-embedded pole, weak evidence)

### Key observations (Layer A, product-page level only)

- Public-safety platform spanning CAD, RMS (reports/investigations), booking, data platform; evidence appears as one data domain: "brings together all your data from CAD events to reports, **evidence**, booking and more"; RMS headline "Connect evidence, cut duplication, and close cases faster"; hero imagery includes "Evidence storage solutions".
- No operational evidence-module documentation was reachable; no structural claims are made from this sample beyond "evidence custody exists as a module inside a cloud RMS suite."

---

## Cross-product Comparison

| Dimension | Tracker SAFE | FileOnQ EvidenceOnQ | Axon Evidence | Mark43 (weak) |
|---|---|---|---|---|
| Item of record | Item with ID, category, "belongs to", media, notes, tasks; splittable | Item with configurable fields, categories, media | Digital file with fingerprint/hash | not documented |
| Matter anchor | Case (plural officers; item ↔ multiple cases; primary case) | Case evidence organization for prosecution; RMS integration | Case/closure framing; camera-incident origin | RMS case domain |
| Custody events | Check-in/out, move, transfer, dispose/undispose; scan history; signatures | Transactions on one screen; signatures; check-out-too-long triggers | Access events (view/edit/download) auto-logged | not documented |
| Custody immutability | "unbroken, court-admissible digital trail" | "unalterable" | "files remain protected, unaltered, and fully auditable" | not documented |
| Storage model | Storage locations (hierarchical, labeled, permission-scoped) + containers | Location barcodes; boxes; wrong-location detection | Cloud storage (no physical semantics) | not documented |
| Identification tech | Barcode (RFID alternative discussed), Zebra hardware | Barcode 1D/2D, labels | Digital fingerprint (hash) | — |
| Verification discipline | Inventory reports, random audits, discrepancy reports | Inventories; missing/wrong-location reports; random percentage audits (accreditation) | Audit trail | not documented |
| Disposition | Auto Disposition (+Advanced), disposal methods, notifications to review, undispose | Retention date assignment, review requests, purge projects, pending-destruction views, triggers blocking illegal destruction | not documented (closure framing only) | not documented |
| Authorization gates | "automated disposal approval" (category FAQ) | Drug-release ban; court-order requirement for warrant-item destruction | permission model by role | not documented |
| External parties | Prosecutor via ecosystem; Evidence.com integration | Prosecutor access + electronic authorizations (lab requests, return approvals); public found-property intake | Public submissions; disclosure/redaction to public-records process | — |
| Digital evidence | Same custody chain; hashing | DigitalOnQ sibling, integrated | Native (primary object) | — |
| Deployment | Cloud GovCloud (+on-prem file servers for media) | On-premises default (VMware cloud possible) | Cloud | Cloud |
| Roles/access | Permission groups (office- and location-based), MFA/SAML | User-configurable; role dashboards | Role/user-type permissions | — |
| Integration spine | RMS (CentralSquare), Evidence.com, API, data import/export | RMS, labs, courts, towing, purchasing "ANY third-party" | Axon cameras, third-party systems, public submissions | CAD/RMS/data platform |
| Adjacent products by same vendor | — | Asset & Quartermaster (separate), SAK tracking, forensic suite | Camera fleet, AI plans | CAD, booking, data platform |

Stable commonalities (B layer, cross-product): identified item of record; case/legal-matter anchoring; recorded custody events forming an unbroken, effectively unalterable chain; controlled circulation (check-out with reason/expected return vs access grants for digital); verification machinery (inventory + audits + discrepancy handling); authorized, legally gated disposition with retention/review mechanics; role- and location-scoped access; chain-of-custody reporting for court; security/compliance posture (CJIS-class); integration outward to RMS/courts/prosecution.

Pole differences (variant layer): physical storage semantics (locations/containers/barcodes) vs digital access semantics (hash/audit/redaction); cloud vs on-prem; configurable-platform vs opinionated-workflow; specialist vs RMS-embedded module.

---

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable as an Evidence Management System:

1. **The evidence item of record** — a persistent, individually identified record of a specific physical or digital item held in an agency's custody because of its role in an investigation or legal matter (not held for use, consumption, or asset value). Remove it → generic property/asset inventory.
2. **The unbroken chain of custody** — every intake, transfer of possession or location, and (for digital items) access event is recorded as an attributed, time-stamped event; the accountability trail is append-only in effect and reconstructable at any time. Remove it → inventory control (the boundary a sampled vendor itself draws: "many evidence tracking systems are no more than barcode-based inventory control").
3. **Controlled entry and authorized exit** — items enter custody through recorded intake bound to the matter, and leave only through recorded, authorized disposition (release, return, destruction, transfer); custody is a bounded state, never silent or indefinite. Remove it → indefinite storage/archive.

Test against L0: a paper property book (numbered tags, ledger lines for each transfer, signature column, "released/destroyed" entries with authorizing signature) satisfies all three — deliberate, so the definition is not overfit to barcodes, cloud, or AI.

### L1 — Common Mature Structure

Present across the sampled mature products; expected in market but not definitional:

- Case/person anchoring: item ↔ case (commonly many-to-one with a primary case), persons of interest/owners, officer attribution.
- Item attributes: category taxonomies (property classes), descriptions, photos/media, notes, tasks, custom fields.
- Identification & labeling: unique IDs, printable barcode/QR labels, handheld scanners, mobile capture.
- Circulation mechanics: check-out with configured reasons and expected return dates, overdue notifications, moves between locations, transfers between custodians/offices, signature capture.
- Storage machinery: hierarchical storage locations with location barcodes, containers/boxes, location-scoped visibility.
- Verification machinery: inventory reports, random/percentage audits, discrepancy reports and their investigation.
- Disposition machinery: retention-date assignment, review notifications, approval workflows, configured disposal methods, purge/backlog programs, correction paths (e.g., reversing a disposition through a recorded action).
- Chain-of-custody reporting for trial preparation; production of custody documentation.
- Roles/permissions (role- and location-scoped), MFA/SSO, CJIS-class security posture, full audit logging.
- Reporting/analytics (counts, categories, storage, productivity); dashboards per role.
- Integration spine: RMS/CAD, courts, labs, digital-evidence platforms, towing/purchasing.
- Mobile surfaces for field capture and transactions; multi-office/multi-organization operation.

### L2 — Variant / Optional Structure

- Custody medium: physical-dominant, digital-only (DEMS pole), or unified physical+digital in one chain.
- Ingestion sources: station intake, field submission, public submissions, camera fleets, third-party systems.
- External collaboration depth: prosecutor/lab portals and electronic authorizations; public found-property reporting; FOIA/redaction surfaces.
- Automation depth: from manual workflows to auto-disposition engines and prohibited-action triggers.
- Deployment: government cloud vs on-premises vs hybrid; hardware ecosystems (printers, scanners, signature pads, RFID).
- Accreditation/regulatory tuning: CALEA-class standards, CJIS, jurisdictional retention rules; adjacent specializations (sexual-assault kit tracking, quartermaster/asset modules as separate products).
- Agency scale/tuning: local PD, sheriff, task forces/multi-agency sharing, state/federal.

### L3 — Vendor-specific Structure

- Tracker: Organization/Office model with OrgID/ItemID numbering; Scan History as a distinct tab; widget dashboards built from saved searches; Evidence.com integration; supported hardware list (Zebra/Socket/Topaz); license allocations; translation support.
- FileOnQ: Foundrop (public lost/found property), MobileOnQ (disconnected mobile), DigitalOnQ (digital sibling), 100% user-configurable screens/labels/workflows, on-premises-first delivery, "Seven Deadly Sins" property-room guide.
- Axon: camera-ecosystem ingestion, Auto-Tagging, Redaction Assistant, transcription, AI Era Plan packaging, unlimited-storage positioning.
- Mark43: evidence as one domain of a CAD/RMS/data-platform suite.

### Historical / Market-Sample Check

- Pre-digital property rooms ran on paper property books and tagged items with sign-out lines and disposition entries — satisfies L0 without barcodes, software, or cloud. ✔
- Non-US justice systems and adjacent custodial institutions (courts' exhibit custody, customs seizures, campus/federal agencies; vendor claims of labs/museums/hospitals/law firms using custody-record systems) fit the same invariant: identified items held for a matter, recorded custody, authorized exit. Regional retention statutes vary — kept out of the definition. ✔
- Digital-first systems express the same three invariants with access events instead of physical possession. ✔
- Therefore the definition is written over "recorded accountability for identified items held for a matter", not over any implementation era (barcode/cloud/AI).

---

## Vendor-specific Findings (kept out of the final document)

- Tracker testimonial numbers (2–3 FTE productivity, <30 min disposition batches, $450K avoided expansion, "100% audit pass rate"); Apple Valley PD's 90-day notification configuration.
- FileOnQ marketing statistics (unfilled %-figures on the page), "RMS evidence modules notoriously lack functionality" rhetoric, customer testimonials.
- Axon AI-era packaging and testimonial quotes.
- All vendor compliance badging (SOC 2 Type II, CJIS claims, FedRAMP) — compliance posture is summarized generically in the final document.

## Boundary Findings

- **vs Law Enforcement Case Management**: the case-management system of record is the case (narratives, offenses, persons, clearance); the EMS system of record is the **item under custody**. The two interlock (items attach to cases; RMS integrations documented at Tracker, FileOnQ; Mark43 ships both in one suite), but custody semantics — check-out, custody chain, storage location, disposition — do not exist in case management. Removing case-management features (narratives, clearance, NIBRS-class reporting) leaves an EMS intact; removing custody machinery leaves a case file system.
- **vs inventory / asset control** (Inventory Management, Enterprise Asset Registry, quartermaster/asset products): inventory exists to have things available and consume them; the EMS holds items as **proof** — items are preserved, not consumed; custody is personal and attributable; exit is legally gated. Direct evidence: Tracker's own FAQ draws this line; FileOnQ ships Asset & Quartermaster as a **separate product** from EvidenceOnQ.
- **vs eDiscovery / Legal Hold Management**: eDiscovery preserves and produces ESI for civil/legal process with preservation obligations and review/production workflows; the EMS is a custody system of record where the unit is an item (usually physical) whose possession must be attributable at all times. Custody chain ≠ preservation obligation. Digital evidence blurs the media type but not the custody semantics.
- **vs Enterprise Records Management / Government Records Management**: records management retains documents per retention schedules for organizational/statutory memory; the EMS holds items for their evidentiary role with person-attributed possession. Disposition exists in both, but EMS disposition is per-item, matter-linked, and often court-gated.
- **vs Archive Storage Management**: IT storage-tiering vs physical/digital custody chain — different objects, different accountability model.
- **vs Digital Evidence Management as a separate Type?**: within this research, the digital-only pole (Axon) reproduces all three defining invariants with digital semantics; the market sells DEMS both standalone (Axon) and integrated with physical evidence (Tracker, FileOnQ). Treated as a **variant within the Type**, consistent with the single directory leaf. Flagged in Boundary Issues for maintainers' awareness.
- **vs court exhibit management**: court-side exhibit custody was not sampled (no directory leaf processed); transfers to prosecutors/courts appear in the EMS as custody transfers/outbound transactions. Kept as adjacency, not a boundary claim.

## Uncertainties

- Lab-side evidence management (JusticeTrax pole) is unevidenced this pass — the lab/LIMS-adjacent realization is plausible but unverified; no claims made.
- Digital-evidence retention/deletion specifics (when files leave custody in the DEMS pole) were not documented on fetched pages; the final document keeps digital disposition generic.
- RMS-embedded module structure (Mark43) unverified below product-page level; suite-module realization stated without structural detail.
- Exact statutory retention regimes, fee schedules, auction mechanics, and state-machine names vary by jurisdiction/product and were deliberately not asserted.
- Tracker help-article bodies (procedural detail) did not render; transaction mechanics are evidenced at structure level, not click level.

## Final Synthesis

The Evidence Management System is the agency-side custody system of record for items held because of their role in investigations and legal matters. Its defining core is three properties: an identified evidence item of record (physical or digital), an unbroken recorded chain of custody (possession/location/access events, attributed and effectively unalterable), and controlled entry with authorized, recorded exit (disposition). Around that core, mature products add case/person anchoring, barcode-labeled identification, circulation mechanics (check-out with reasons and expected returns, moves, transfers, signatures), storage-location machinery, inventory/audit discipline (including random audits and discrepancy handling), legally gated disposition with retention/review automation, chain-of-custody reporting for court, role/location-scoped access with CJIS-class security, and integrations to RMS, courts, labs, and digital-evidence platforms. Two realizations dominate the market: the physical property-room system (often unified with digital items) and the digital-first evidence platform; they are variants of one custody model, differing in whether custody events are physical movements or access events. The Type is cleanly separated from inventory/asset control (items held as proof, not for use), from case management (item-custody vs case records), from eDiscovery (custody chain vs preservation/production), and from records management (per-item matter-linked custody vs document retention).
