# Research Notes — Proof of Delivery Platform

## Research Goal

Understand what a Proof of Delivery (POD) Platform actually is as an Application Type: its unit of record, who uses it, how delivery evidence is captured and managed, what rules govern capture, and where its boundary sits against neighboring delivery/logistics Application Types.

## Initial Boundary

Initial hypothesis: the center of gravity is the **delivery-evidence record** — driver-side capture at the stop (signature / photo / scan / geostamp) plus back-office management of that evidence (storage, search, sharing, dispute response) — not dispatch, not route planning, not shipment tracking.

Neighboring Types suspected at start:
- Last-mile Delivery Platform / Courier Management Platform (dispatch & job orchestration)
- On-demand Delivery Platform (consumer-side ordering)
- Delivery Scheduling Platform (when, not whether)
- Shipment Visibility Platform (tracking status, not evidentiary record)
- Delivery Experience Platform (consignee-facing experience layer)

## Research Questions

1. What is the unit of record — the delivery stop, the job, the POD document?
2. What forms of proof are captured, and which are definitional vs optional?
3. What does the driver flow look like (stop list → arrival → capture → exception → next)?
4. How are failed / partial / refused deliveries documented?
5. What does the back office do with captured evidence (search, retrieve, share, dispute)?
6. How do capture requirements get configured (mandatory fields, verification codes)?
7. Is POD a standalone Type or a capability inside delivery-management platforms?
8. Do older / regional / embedded implementations (paper-POD replacements, telematics-embedded forms) fit the same core?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy | Tier / Segment | Evidence quality |
|---|---|---|---|
| Detrack | POD-first delivery management (delivery + collection jobs) | SMB–mid, global (SG/AU origin) | Strong — root, ePOD page, Help Centre (Tier 1) |
| Track-POD | All-in-one delivery management with configurable ePOD workflow | SMB–mid, EU/US | Strong — root, ePOD article (Tier 2) |
| Shipday | Restaurant/local delivery ops with POD as flagship feature | SMB, US/global | Moderate — root + POD feature page (Tier 2) |
| Samsara | Telematics/fleet suite where POD = route-stop digital forms | Enterprise fleets, US | Moderate — KB search results confirm POD framing (Tier 1, partial) |

Rejected/abandoned: Onfleet (help center + docs unreachable — 404/403/timeout), Bringg (403 twice). Market context from search results: Upper, JumpTrack, EasyDrop, Greenlight, SuiteFleet, Infor Proof of Delivery (distributor ERP module), a 2014-era Windows POD app — confirms a broad POD-branded market including standalone and embedded poles.

## Sources

- Detrack — https://www.detrack.com/ (root), https://www.detrack.com/electronic-proof-of-delivery/ (ePOD page), https://help.detrack.com/en/ + Driver App collection (Tier 1)
- Track-POD — https://track-pod.com/ (root), https://track-pod.com/blog/what-is-proof-of-delivery/ (ePOD article)
- Shipday — https://www.shipday.com/ (root), https://www.shipday.com/features/proof-of-delivery (POD feature page)
- Samsara — https://kb.samsara.com/hc/en-us/search?query=proof+of+delivery (KB search results: "Complete a Digital Form for a Route Stop — forms specific to your route-based workflow, such as proof of delivery (POD), bill of lading (BOL)"; "Submit and View Documents — to capture documents such as receipts, invoices, and proof of delivery")
- Market context (Tier 3): Upper POD feature pages (upperinc.com), app-store listings (Detrack, Track-POD, JumpTrack, EasyDrop, Infor POD, Greenlight), Onfleet POD product page title/snippet via search

Research date: 2026-09-10

## Product Observations

### Detrack (evidence layer A — direct observation, Tier 1 + Tier 2)

- Positioning: "Delivery Software — ePOD, Tracking & Route Optimization"; ePOD is the first-listed feature; app-store name literally "Detrack Proof Of Delivery POD".
- ePOD page: "Your permanent record that can't be disputed" — photo evidence (up to 10 photos per job), electronic signature (customer signs on driver's phone), GPS verification and timestamps ("Every delivery is pinned to an exact time and location. If your driver was there, you can prove it"), searchable ePOD storage "for up to 5 years", real-time receipt of confirmations.
- Configurable driver workflow: "Make photos, signatures, or recipient names mandatory, and require data inputs like temperature or payment amount. Lock POD completion behind milestones such as 'heading to' or 'arrived at', so nothing gets skipped."
- Driver app with offline mode; three main buttons; POD info can be overlaid onto photos.
- Help Centre Driver App collection (88 articles) — operational depth:
  - Completing delivery jobs: scan to pick up packages, capture signature, capture photo proof, submit delivered status, submit failed delivery status, reject/un-reject delivery item, change quantity for delivery item, enter payment amount for COD, write note, call recipient, GPS navigation, scan barcode to search for a specific delivery, transfer jobs to another driver, reattempt failed jobs, force resubmit jobs, resend a wrongly sent/failed POD status, mass POD (batch completion), mass arrived-at.
  - Symmetric "Completing Collection Jobs" collection — pickups/collections get the same POD machinery (photo, signature, note, failed status, reject, quantity).
  - Settings: POD submission settings customization; make signature mandatory / photo mandatory / signature-or-photo mandatory / receiver's name mandatory / note-for-photo mandatory; verification code enforcement before completing or failing a job; geofence prompt when driver too far from address; customize non-delivery reasons; capture signature for specific failed-delivery reasons; max photos; photo resolution; photos from device gallery allowed; continuous photo taking; contactless delivery with recipient signature; mandatory COD payment amount; mandatory temperature values for POD submissions (cold chain); pre-delivery SMS; hide completed jobs.
- Pricing: per-driver; POD (signature, 10 photos, location, timestamps) in the base plan; secure storage & search up to 5 years.
- Customer quotes confirm the back-office loop: "if a customer queries any deliveries we can just download the POD and send it to the customer"; "went from a paper based pod system… reduced scanning PODs and shredding".

### Track-POD (evidence layer A — direct observation, Tier 2)

- Positioning: delivery management software with "electronic proof of delivery app" as flagship; name itself is POD-anchored.
- ePOD article defines the ePOD document's essential elements: (1) electronic signature (customer's or driver's, or both), (2) photos ("must include at least one photo to confirm successful contactless delivery"; also documents partial and failed deliveries), (3) location coordinates (geotag automatic or manual entry), (4) goods quantity (partial delivery and overdelivery scenarios), (5) COD amount, (6) PIN code (security measure for high-value deliveries; can replace signature+photo).
- Explicitly frames ePOD as documenting "successful, unsuccessful, partial, or over-deliveries".
- ePOD workflow: load check (scan packages at loading; rejected status if not loaded) → in transit → on-site scanning (confirm right packages at right address) → proof of delivery (e-signature and/or photos) → close route.
- Seven configurable ePOD types: customer e-signature + name; signature AND photo; signature OR photo; photo only; driver's e-signature; driver's + customer's signatures; PIN code.
- Root page: app works offline and syncs when connection restored; geotags & timestamps captured; barcode scanning for load control; delivery notification with digital PDF (signature, geotag, timestamp, shipment details) emailed to customer; signed POD "works as a delivery note or bill of lading to automatically create a credit invoice in your ERP or accounting system".
- Customizable POD template; branded notifications; COD collection in driver app.

### Shipday (evidence layer A — direct observation, Tier 2)

- Positioning: AI delivery management for restaurants/local businesses; POD is a named feature: "Capture proof with photos, signatures, and accurate delivery timestamps."
- POD feature page: "automatically captures delivery photos, timestamps, and customer signatures—providing clear, verifiable proof that orders were received. This protects your business, builds trust with customers, and reduces disputes."
- Delivery history surface: "Instantly view past deliveries with full details"; "Clear records help resolve issues before they escalate."
- Customer quote: "Having proof of delivery photos and invoices is huge for us—especially for audits. We used to scramble for paperwork; now it's all digital."
- Driver app includes proof-of-delivery; delivery confirmation sent via text and email; branded tracking pages.
- Segment evidence: restaurants/pizzerias/florists/liquor/grocery — POD embedded in a dispatch/tracking/review product, not standalone.

### Samsara (evidence layer A — partial, Tier 1 KB search results)

- Telematics/fleet suite; POD appears inside "Driver Workflows and App":
  - "Complete a Digital Form for a Route Stop — forms specific to your route-based workflow, such as proof of delivery (POD), bill of lading (BOL), and other common transportation [forms]".
  - "Submit and View Documents — to capture documents such as receipts, invoices, and proof of delivery" (document scanning capability).
- Interpretation: in a telematics-native implementation, POD is realized as driver-completed digital forms/documents bound to route stops, alongside BOL — i.e., POD as one instance of a stop-workflow document pattern, not a standalone product.
- Evidence is partial (search-result snippets only); treat detailed Samsara workflow claims as unverified beyond this framing.

### Market context (evidence layer B — cross-product commonality, Tier 3)

- Upper (route planner with POD): photo + signature in one tap, GPS & timestamp auto-attached, searchable delivery history, custom proof requirements ("drivers can't skip required proof"), failed-delivery documentation ("drivers log exceptions with photos and notes — closed business, wrong address, refused"), POD connected to routes/tracking ("POD that isn't standalone").
- App-store ecosystem shows both poles: standalone POD apps (EasyDrop — "collect proof of delivery for each job… photo… signature… location details") and POD inside suites (Bringg Driver App, Greenlight Driver, JumpTrack).
- Infor Proof of Delivery Driver (distributor ERP companion): "helps distributors manage order deliveries, capture a customer's signature, as well as the time and location" — ERP-embedded pole, older pattern.

## Cross-product Comparison

| Dimension | Detrack | Track-POD | Shipday | Samsara |
|---|---|---|---|---|
| Unit of record | delivery/collection job | delivery/collection (order) | delivery order | route stop (form-bound) |
| Signature capture | yes (mandatory-configurable) | yes (7 ePOD types) | yes | via digital form |
| Photo capture | yes (up to 10, configurable) | yes (contactless proof) | yes | via form/document scan |
| Barcode scan | yes (pickup, item, search) | yes (load check + on-site) | not evidenced | document scanning |
| Time + location stamp | yes (GPS verification) | yes (geotag + timestamp) | yes (timestamps) | route-stop context |
| Failure documentation | failed status, non-delivery reasons, reject item, reattempt | unsuccessful/partial/over-delivery | not detailed | not evidenced |
| Configurable requirements | mandatory signature/photo/name/temp/COD, verification code, geofence | 7 ePOD type configurations | not detailed | form templates |
| Back-office evidence mgmt | searchable 5-year storage, download & send POD | PDF POD document, ERP handoff | delivery history, audit use | dashboard documents |
| Distribution to stakeholders | automatic emails with POD info, tracking links | emailed PDF confirmation | text/email confirmation | not evidenced |
| Offline mode | yes | yes | not evidenced | not evidenced |
| Packaging | POD-first suite | all-in-one with POD flagship | feature inside delivery ops | capability inside telematics suite |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The delivery event of record** — a persistent, identified record per delivery attempt/stop (bound to consignee/address and the goods involved), carrying the outcome (delivered / failed / partial), retained after completion. Remove → a status tracker or task list with no evidentiary memory.
2. **Point-of-delivery evidence capture** — the person performing the delivery captures evidentiary artifacts at the stop, bound to that event: at minimum one evidentiary form (signature, photo, or scan) with time and location context attached. Remove → back-office data entry or a bare checklist.
3. **The evidence record as managed, shareable artifact** — captured proofs are stored, searchable, retrievable, and distributable to stakeholders (customer, shipper, auditor) as the record that the delivery did or did not happen as claimed. Remove → capture utility with no archive, or a document folder.

Binding: delivery semantics. The record is about a delivery/collection event — remove delivery semantics and it becomes a generic form/signature capture tool.

Jointly-held load-bearing:
- 1 alone = delivery status tracker
- 2 without 1 = camera + signature pad
- 3 without 1+2 = document folder
- 1+2 without 3 = capture with no archive
- 1+3 without 2 = records entered after the fact (paper-POD scanning office — the predecessor artifact, not the digital Type)
- 2+3 without 1 = orphaned photos/signatures not bound to delivery events

### L1 — Common Mature Structure

- Driver mobile app with stop/job list, navigation handoff, arrival/heading states
- GPS driver tracking and live location
- Customer notifications with POD attached (email/SMS/tracking link, PDF POD document)
- Barcode/QR scanning for load check and item verification
- Offline capture with later sync
- Configurable capture requirements (mandatory fields, verification codes/PIN, geofence checks)
- Non-delivery reason lists (customizable)
- COD payment amount capture
- API/webhooks and ERP/e-commerce integrations
- Searchable POD archive with multi-year retention

### L2 — Variant / Optional Structure

- Packaging pole: standalone POD-first product vs POD inside delivery-management suite vs POD inside telematics/ERP suite
- Contactless delivery posture (photo instead of signature)
- Collections/pickups as symmetric job type (Detrack, Track-POD)
- Mass/batch POD for multi-item stops
- Temperature values for cold chain
- ID/age verification scanning
- Marketplace driver grab / third-party driver dispatch
- 3PL rate cards and contractor commissions
- POD data feeding invoicing (credit invoice generation)

### L3 — Vendor-specific (Research Notes only)

- Detrack: 10-photo limit, 5-year retention, MCP server (AI), scanner app for warehouse staff
- Track-POD: the specific 7 ePOD type list; SOC 2 / HIPAA compliance posture
- Shipday: review management, refund collection, AI receptionist
- Samsara: POD as one form type among route-stop digital forms within the telematics suite

## Historical / Market-Sample Check

- Paper-POD heritage: the signed paper delivery note + office scanning is the predecessor artifact. Digital POD platforms explicitly market against it ("went from a paper based pod system"; "reduced scanning PODs and shredding"). The digital Type's core (capture at the stop + retained record) is satisfied by early/minimal implementations: signature + timestamp + location only, no photos, no GPS map, no notifications (e.g., the 2014-era Windows POD app; Infor POD for distributors).
- Therefore L0 must NOT require: photos, GPS map verification, customer notifications, barcode scanning, offline mode, or multi-year retention guarantees. Signature-only capture with time/location satisfies the core.
- Regional/platform-native check: distributor-ERP-embedded POD (Infor), telematics-embedded POD (Samsara), restaurant-ops-embedded POD (Shipday) all satisfy the three-part core — the core is packaging-neutral.

## Vendor-specific Findings

See L3 above. Also: Detrack's "mass POD" batch completion and marketplace job-grabbing are product-specific; Track-POD's load-check scanning workflow is more elaborate than peers; Shipday's POD is thinner (photos + signature + timestamp only, per public docs).

## Boundary Findings

- **vs Last-mile Delivery Platform / Courier Management Platform**: those center on dispatch, job orchestration, route optimization, driver management. POD platform centers on the evidence record. The sampled POD-first products all bundle dispatch/tracking — POD is frequently a flagship capability of delivery-management platforms rather than a fully standalone market. The standalone Type is defensible (POD-branded standalone products exist: Detrack's ePOD identity, Track-POD's name, JumpTrack, EasyDrop, Infor POD), but the seam is real: remove dispatch/route machinery and keep capture+archive → still a POD platform; remove capture/archive and keep dispatch → delivery management. Recorded as a boundary issue for the taxonomy.
- **vs Shipment Visibility Platform**: visibility = where is my shipment now (status/location across the journey, consignee-facing tracking). POD = the evidentiary record of the delivery event itself. Tracking links often surface POD images, but the visibility platform's unit is the shipment's journey; the POD platform's unit is the delivery event's proof.
- **vs Delivery Scheduling Platform**: scheduling decides when the delivery happens; POD records whether it happened and with what evidence.
- **vs On-demand Delivery Platform**: consumer-side ordering/matching marketplace; POD is operator-side evidence.
- **vs Delivery Experience Platform**: consignee-facing experience layer (tracking pages, notifications); POD may feed it but the record-of-record is the evidence, not the experience.
- **vs generic e-signature / form tools**: no delivery-event binding, no outcome states, no delivery semantics.
- Decisive test: remove the delivery-event binding and outcome semantics → generic signature/photo capture; remove evidence capture/archive and keep the delivery event → dispatch/tracking product.

## Uncertainties

- Onfleet and Bringg documentation was unreachable (403/404/timeout); their POD implementations could not be directly observed. Onfleet's POD product page snippet (via search) confirms photo/barcode POD in its driver app, but no operational detail was verified.
- Samsara evidence is limited to KB search snippets; the exact shape of its route-stop POD forms (fields, requirements, storage) is unverified.
- Whether the market sustains truly standalone POD platforms long-term, or whether POD consolidates as a capability of delivery-management suites, is an open market question. Both poles exist today.
- Exact retention periods, photo limits, and notification defaults vary by product and plan; no cross-product numeric standard is asserted.

## Final Synthesis

A Proof of Delivery Platform is the delivery-side evidence system of record. Its defining core is three jointly-held structures: (1) the delivery event of record — a persistent identified record per delivery attempt carrying the outcome, retained after completion; (2) point-of-delivery evidence capture — the person performing the delivery captures evidentiary artifacts at the stop (signature, photo, or scan, with time and location context), bound to that event, under configurable capture requirements; (3) the evidence record as managed, shareable archive — stored, searchable, retrievable, and distributable to stakeholders for dispute resolution, audits, and invoicing handoff. The driver mobile app is the characteristic capture surface; the web dashboard is the characteristic management surface. Failure documentation (non-delivery reasons, partial/over-delivery quantities) is part of the evidence semantics, not an add-on. Mature products add tracking, notifications, scanning, offline mode, and integrations; packaging ranges from POD-first standalone products to POD as flagship capability inside delivery-management and telematics suites.
