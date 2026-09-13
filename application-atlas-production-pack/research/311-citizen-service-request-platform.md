# Research Notes — 311 / Citizen Service Request Platform

Research date: 2026-09-06
Slug: `311-citizen-service-request-platform`
Directory leaf: "311 / Citizen Service Request Platform" (§24 Government, Public Sector & Civic)

## Research Goal

Understand what a 311 / citizen service request platform actually is as an Application Type: what objects exist inside it, how a resident report becomes a fulfilled government service action, which channels and roles participate, which rules govern the lifecycle, and where the boundary lies against neighboring government and ticketing Types.

## Initial Boundary (hypothesis before research)

- Core hypothesis: a government-operated system that receives non-emergency service requests from residents (potholes, missed trash, streetlights, graffiti), categorizes them against a government-defined service catalog, routes them to the responsible department, tracks them to resolution, and reports status back to the requester.
- "311" refers to the North American non-emergency phone number; the software behind 311 programs is multi-channel intake + request lifecycle management, not a phone system.
- Likely confusions: Government Service Portal, Public Sector Case Management, Help Desk/Ticketing, Code Enforcement Management, Public Works/work-order systems, Computer-aided Dispatch (911), Constituent Relationship Management, Government Contact Center.

## Research Questions

1. What is the core record (service request) and what does it contain?
2. What is the service catalog and who defines it? How do request types drive routing?
3. How does location/GIS participate (address validation, jurisdiction/authority resolution, asset lookup)?
4. Which intake channels exist (phone/agent, web, mobile, SMS, chatbot)? How does agent-created-on-behalf work?
5. What is the request lifecycle (states, SLA/expected dates, closure reasons such as duplicate)?
6. How does the requester learn status (tracking number, notifications, public map, updates)?
7. How do agents/department staff work (queues, assignment, priority, templates, internal vs public notes)?
8. How does fulfillment hand off to field work (work order / asset management integration)?
9. What reporting/analytics exist (volume by type, timelines, workload, geography, open data)?
10. How do duplicate reports, abuse/moderation, privacy (PII) get handled?
11. What varies by region (311 number vs council reporting), scale (city vs regional), and product philosophy?

## Representative Products

Selected for market representativeness, documentation accessibility, and different product philosophies / customer tiers:

| Product | Philosophy | Tier | Evidence access |
|---|---|---|---|
| Open311 GeoReport v2 (open standard) | vendor-neutral data model for civic issue reporting | cross-vendor | full spec fetched (Layer A) |
| Accela Service Request Management (SRM/CRM) | service requests embedded in an end-to-end civic platform (permitting/licensing/asset) | large cities/counties | product pages fetched (Layer A) |
| Granicus Service Request Management (govService) | digital-services/forms-first, portal + staff portal + customer service hub | mid/large local government | product page fetched (Layer A) |
| FixMyStreet / FixMyStreet Platform (mySociety) | citizen-first public issue reporting; open source; regional (UK-origin, deployed worldwide) | any size, incl. citizen-run | full docs fetched (Layer A) |

Rejected/abandoned samples (source-access limitation): Tyler Technologies (Enterprise 311) — tylertech.com 403; Cityworks (Trimble) — cityworks.com redirects to generic Trimble site, help/docs subdomains unreachable; SeeClickFix — seeclickfix.com and help subdomain 403; Salesforce public-sector 311 URL — 404. SeeClickFix is still referenced where the Open311 site itself describes it (third-party, Layer B).

## Sources

Fetched 2026-09-06:

- Open311 — https://www.open311.org/ (blog/ecosystem context)
- Open311 GeoReport v2 spec — http://wiki.open311.org/GeoReport_v2 (full API spec)
- Accela — https://www.accela.com/ (platform overview)
- Accela Service Request Management — https://www.accela.com/solutions/service-request/ (solution page)
- Granicus Service Request Management (govService) — https://granicus.com/product/service-request-management-govservice/ (product page)
- FixMyStreet Platform — https://www.fixmystreet.org.uk/ (overview)
- FixMyStreet Platform — https://www.fixmystreet.org.uk/how-it-works/ (workflow)
- FixMyStreet Platform glossary — https://www.fixmystreet.org.uk/glossary/ (object definitions)
- FixMyStreet Pro staff documentation — https://www.fixmystreet.org.uk/running/staff/ (staff-side workflow, permissions, categories, duplicates)

Not reachable (recorded limitation): tylertech.com, help.cityworks.com, docs.cityworks.com, seeclickfix.com, help.seeclickfix.com, salesforce.com public-sector 311 URL.

## Product Observations

### Open311 GeoReport v2 (standard) — Evidence Layer A

- Purpose statement: API to "view and report issues which government entities like cities are responsible for addressing"; interactions "often referred to as 'service requests' or 'calls for service'"; "traditionally handled by custom web forms or phone based call centers (sometimes using the 311 phone number or other short-code)".
- Scope: "location-based non-emergency issues such as graffiti, potholes, and street cleaning".
- Two main resources: **services** (request types) and **service requests**; plus a token resource for batch servers.
- Service list (GET services): `service_code` (unique id of request type), `service_name`, `description`, `metadata` (whether extra form fields exist), `type` (realtime / batch / blackbox), `keywords`, `group` (category grouping, e.g. "sanitation", "street"). Request types "can be unique to the city/jurisdiction".
- Service definition (GET service definition): per-type attributes with datatypes (string, number, datetime, text, singlevaluelist, multivaluelist), required flags, ordering — i.e., per-type dynamic intake forms.
- POST service request requires: `service_code` + a full location parameter (one of `lat`&`long`, `address_string`, or `address_id` from the jurisdiction's master address repository) + attributes per definition. Optional: `email`, `phone`, `first/last name`, `device_id`, `account_id`, `description` (free text), `media_url` (photo).
- Response: `service_request_id` (the tracking id), optional `service_notice` ("information about the action expected to fulfill the request").
- GET request(s): `status` with canonical values **open** ("it has been reported") and **closed** ("it has been resolved"), `status_notes` (example value: "Duplicate request."), `service_name/code`, `description`, `agency_responsible` ("the agency responsible for fulfilling or otherwise addressing the service request"), `requested_datetime`, `updated_datetime`, `expected_datetime` ("may be based on a service-specific service level agreement"), address fields (`address`, `address_id`, `zipcode`, `lat`, `long`), `media_url`.
- `jurisdiction_id` distinguishes multiple jurisdictions behind one endpoint — multi-jurisdiction is in the standard's data model.
- Ecosystem context (open311.org blog): began as an API for Washington D.C.'s 311 system; adopted by Chicago, Toronto, San Francisco, NYC-area, Helsinki/Bonn/Lamia (CitySDK), Bloomington (open-source uReport CRM); commercial supporters included SeeClickFix, Connected Bits, Motorola, Lagan; cities wrote Open311 into procurement (Boston/Commonwealth Connect, SF, Chicago, NYC 311 CSMS replacement RFP). NYC implemented the Inquiry v1 draft for information requests.

### Accela Service Request Management (SRM/CRM) — Evidence Layer A (product pages)

- Positioning: part of Accela's end-to-end civic platform (building, planning, licensing, asset management, fire, environmental health). SRM page headline: "Give residents a clear, convenient way to report issues and track progress, while giving agencies the tools to receive, route, and resolve every request."
- Resident side: "fully branded, mobile-ready portal … submit requests, upload photos, and track status from first report to final resolution"; real-time updates.
- Cost framing: "Reduce the cost of non-emergency requests"; shifting interactions online to "reduce duplicate requests" and eliminate manual routing/follow-up.
- Routing: "routes each request to the right team automatically based on request type and geographic boundaries, with two-way synchronization so every department has a current, accurate view".
- Fulfillment: "Integrate directly with your work order management system so field crews receive actionable assignments the moment a request is approved. No manual re-entry."
- GIS: "Residents and staff can pinpoint the exact location of an issue directly on a map. Location data speeds triage, improves routing accuracy, and gives agencies geographic visibility."
- Staff side: "search requests, track cases, configure processes, and manage their queue from intake to resolution. Priority setting, task assignment, and status tracking all live in one place."
- Automation: "pre-configured workflows that identify request types, route tasks to the right team, send internal communications, and push status notifications to residents."
- Reporting: "request volume by type, resolution timelines, department workload, and geographic patterns".
- AI intake (current-generation): photos analyzed to suggest request type; digital assistant validates plain-language descriptions with clarifying questions; automatic PII detection/redaction in photos (e.g., license plates).
- Privacy: automatic redaction of common PII in resident-submitted photos.
- Product naming note: Accela itself titles the module "Service Request Management (SRM/CRM)" — vendor evidence that service request management and constituent CRM are adjacent/merged in market framing.

### Granicus Service Request Management (govService) — Evidence Layer A (product page)

- Positioning: "combined online forms, workflow, and case management features that manage the requests important to your community"; "one system of record".
- Outcomes claimed: reduce service costs (fewer call center/in-person interactions), encourage resident interaction online, end-to-end citizen request management, empower non-technical staff.
- Functionality:
  - Digitize any form or process (low-code).
  - Customer portal: "fully brandable … highly configurable and device agnostic" self-service for all online services.
  - Staff Portal: "assign and track case work … log internal requests, audit and report cases".
  - Customer Service Hub: "centralized hub for front office/customer service operations, including support for phone, email, and in-person interactions that integrates with many phone systems" — the agent/call-center surface.
  - Service Designer: drag-and-drop creation of process flows.
  - Integration Manager: two-way third-party integration, "remove the need to re-enter data".
  - Realtime Reporting: "report on outcomes and service volumes using near real-time data", plus BI connectivity.
- Success stories referenced: Auburn AL (customized app for public service requests), Escondido CA (graffiti reporting), Coral Gables FL, Oakville (permitting).
- Granicus also ships a second SRM product line (OneView) — same vendor, two SRM products (market-structure observation).

### FixMyStreet Platform / FixMyStreet Pro (mySociety) — Evidence Layer A (full docs)

- Purpose: "sends problem reports to the people who can fix them"; user "can report a problem without worrying about the correct authority"; routing uses "the problem's location and category, and sends a report, by email or using a web service such as Open311, to the department or body responsible".
- Transparency: "makes the reports visible to everyone. Anyone can see what's already been reported, leave updates, or subscribe to alerts. We help prevent duplicate reports."
- Object model (glossary):
  - **problem report** — sent to the responsible body; unpublished until user confirms; may include a photo; anonymous display option (name hidden from public but still sent to the body).
  - **category** — problem type ("Pothole", "Graffiti"); "category, together with the area, determines which contact will be sent the report".
  - **body** — "the authority responsible for a problem. Bodies can be councils, local government departments … or even private companies that are paid to fix particular problems."
  - **contact** — per body/category destination (email address, or Open311 service code when integrated).
  - **area (admin boundary)** — polygons determining which bodies cover a location (via MapIt).
  - **state** — "typically start as unconfirmed, then open, then fixed. There are other states, including those that can only be allocated by a staff user or an administrator."
  - **update** — anyone can add; "message, a picture, and even change the report's state".
  - **staff user** — works for a body; powers only over that body's reports (hide reports, set states beyond fixed/not fixed, view dashboard).
  - **administrator** — back-end admin (bodies, categories, users).
  - **alert** — subscribe to reports/updates within an area.
  - **survey/questionnaire** — sent to reporters (default four weeks after reporting) asking whether the problem was fixed; feeds performance data.
  - **send method** — email by default; Open311 as integration alternative.
  - **integration levels** — (1) reports injected into back end, (2) back-end updates passed back, (3) back-end-created reports passed into FixMyStreet.
  - **partial report** — a report without location is not shown until completed; "a partial report (having no location) effectively has no body responsible for it" — location is structurally required.
- Staff-side workflow (FixMyStreet Pro docs):
  - Phone/in-person intake: staff "can add it to FixMyStreet on their behalf" ("contact centre staff making reports on behalf of someone who cannot access digital services"); "Report As" selector (council / anonymous / another user).
  - Private reports (not publicly visible) for sensitive content.
  - Moderation: edit title/body, remove names, redact photos (draw black rectangles), hide reports; abuse list/banning; flagged queue.
  - Category correction: changing category can re-send the report to another authority ("from the other authority's point of view, and for the person who made the report, the status is still open").
  - Location correction: drag pin; "set to my current location" for field inspection.
  - Status updates: template responses ("Repairs are now underway", "This issue is now closed"); states such as "in progress", "no further action"; updates can be public or direct.
  - Priority setting; shortlists for inspectors; assignment of reports to inspectors; offline inspection workflow.
  - Duplicate handling: "can suggest potential duplicate reports to users when it looks as though a report is being made in the same category and location as an existing report … encourages the user to subscribe to the existing report instead of creating a new one"; duplicate-suggestion radius configurable per category.
  - Category configuration: per-category email/Open311 destination, parent categories, extra questions/notices ("Extra data"), emergency diversion (a "dangerous?" question can disable submission and display "call an emergency number instead"), staff-only categories, update-close timeframes (Pro default: six months — product-specific), best practice ≤20 broad categories in resident language plus an "Other" category (product-specific guidance).
  - Permissions: granular per-permission checkboxes grouped into roles; category-scoped visibility for staff; 2FA available.
- Regional breadth: deployed as Züri wie neu (Zürich), Fixa min gata (Sweden), AduanKu (Malaysia), UK councils, etc. — no 311 phone number involved.

### SeeClickFix (via Open311 site only) — Evidence Layer B (third-party description)

- Described by the Open311 ecosystem blog as an early commercial supporter of GeoReport v2, offering Open311 endpoints for many cities and its own proprietary API; several Open311 endpoints "leverage a common SeeClickFix solution". Positioned as a citizen-facing reporting platform. (Direct vendor documentation was not reachable; no product-specific claims beyond this.)

## Cross-product Comparison

| Aspect | Open311 GeoReport v2 | Accela SRM | Granicus govService | FixMyStreet |
|---|---|---|---|---|
| Core record | service request (`service_request_id`) | service request | request/case in one system of record | problem report |
| Catalog | services list; `service_code`, group, per-type attributes | request types (drive routing) | online forms + Service Designer flows | categories (+contacts per body) |
| Location | required (lat/long, address_string, or address_id) | map pinpoint; GIS speeds triage/routing; routing by geographic boundaries | not detailed on fetched page | required (map pin); area→body routing; partial reports unusable without location |
| Requester identity | optional email/phone/name; device/account ids | resident portal account | portal account | email-based account; anonymous public display possible |
| Routing | `agency_responsible` field; jurisdiction_id | automatic by type + geographic boundaries | workflow assignment to staff | category + area → contact; re-send on category change |
| Lifecycle | open / closed (+status_notes) | intake → route → resolve; status notifications | assign/track/audit cases | unconfirmed → open → fixed; staff states (in progress, no further action, closed, hidden) |
| Requester feedback | GET status; service_notice; expected_datetime (SLA) | real-time updates; track to final resolution | "keep residents up to date" | public updates, alerts, 4-week survey |
| Fulfillment handoff | out of scope (API) | work order management integration | Integration Manager (two-way) | email/Open311 send; 3 integration levels |
| Duplicate handling | status_notes "Duplicate request." | reduce duplicate requests (online shift) | — | duplicate suggestion radius; subscribe to existing report |
| Channels | any client via API | web portal + mobile app (+AI intake) | web forms + customer service hub (phone/email/in-person, phone-system integration) | web + mobile + SMS; staff create on behalf (phone/in-person) |
| Transparency posture | public GET requests | resident's own status | resident's own status | fully public map of all reports; anyone can update/subscribe |
| Moderation/PII | — | auto PII redaction in photos | — | moderation, hide, redact, ban, private reports |
| Reporting | query API | volume by type, timelines, workload, geography | realtime reporting + BI | per-body dashboard; survey data |
| Jurisdiction model | jurisdiction_id (multi-jurisdiction) | city/county/state agencies | local government focus | bodies + areas; multiple bodies per area |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Resident-initiated request (or created by staff on the resident's behalf)
└── Service request record for a non-emergency civic service need/issue
    └── Categorized against the government-defined service catalog
        └── Located (address / geographic position)
            └── Routed to the responsible government unit/body
                └── Tracked lifecycle from submission to resolution
                    └── Status feedback to the requester
```

Six properties, each supported across the sample:

1. **Resident-initiated request record** — the unit of work is a request created by a resident (Open311 POST; Accela resident portal; Granicus portal; FixMyStreet report) or by staff on a resident's behalf (FixMyStreet Pro "Report As"; Granicus customer service hub phone/in-person intake). Without a citizen-originated request object, the system is internal work management, not a 311 platform.
2. **Non-emergency civic scope** — Open311: "location-based non-emergency issues"; Accela: "reduce the cost of non-emergency requests"; FixMyStreet actively diverts emergencies out of the system. This is what separates the Type from 911/CAD.
3. **Government-defined service catalog** — every sampled system first defines request types (Open311 `services`/`service_code`; FixMyStreet categories+contacts; Accela request types; Granicus designed services/forms). The catalog is jurisdiction-specific and drives everything downstream.
4. **Located request** — location is required at submission in Open311 (one of three location forms), structurally required in FixMyStreet (partial reports without location have no responsible body), and central to Accela's GIS triage/routing. Routing by category + location is the shared mechanism (Open311 agency_responsible; FixMyStreet category+area→contact; Accela type+geographic boundaries).
5. **Routed to a responsible government unit** — the request names/implies the agency responsible for fulfilling it (Open311 `agency_responsible`; FixMyStreet body/contact; Accela "right team"; Granicus staff assignment).
6. **Tracked lifecycle with status feedback to the requester** — every sample exposes status to the requester (Open311 GET status + expected_datetime; Accela "track status from first report to final resolution"; Granicus "keep residents up to date"; FixMyStreet updates/alerts/surveys). Without requester-visible tracking, the product is internal work order management.

Historical/regional check (§24-style): pre-smartphone 311 call centers captured the same structure by phone (agent records category + address + contact, creates a tracked request). FixMyStreet (UK), CitySDK cities (Helsinki, Bonn, Lamia, Zaragoza, Lisbon), AduanKu (Malaysia), Züri wie neu (Zürich) satisfy the definition with no 311 number and no call center. Therefore the defining core must not include the 311 phone number, a call center, a mobile app, or a public map.

### L1 — Common Mature Structure

Present in most mature modern products, not required for the definition:

- Multi-channel intake: web portal, mobile app, phone/agent-created, (in some products) SMS, chatbot, social.
- Requester contact/account and notifications (email confirmations, status notifications).
- Photo/media attachments on requests.
- Duplicate detection/merging (Open311 status_notes example; Accela duplicate reduction; FixMyStreet duplicate suggestion radius).
- Expected-resolution / SLA datetime per request type (Open311 `expected_datetime` "based on a service-specific service level agreement").
- Staff/agent console: queues, search, assignment, priority, template responses.
- Richer status vocabularies beyond open/closed (in progress, no further action, etc.) — exact labels vary by product.
- Internal notes vs public updates separation.
- Reporting/analytics: volume by type, resolution timelines, department workload, geographic patterns.
- Integration with work order / asset management systems for field fulfillment (handoff pattern; some suites bundle it).
- Moderation and PII protection (redaction, hiding, private reports).
- Knowledge/template responses for consistent replies.

### L2 — Variant / Optional Structure

Depends on region, segment, posture, scale:

- **311 call-center program wrapper** (North America): dedicated non-emergency number, agent staffing, phone-system integration (Granicus hub "integrates with many phone systems"). Regional, not defining.
- **Public transparency posture**: fully public map of all reports with subscribe/alerts (FixMyStreet; Open311 public GET) vs resident-private status only (Accela/Granicus emphasis). A policy choice of the jurisdiction.
- **Open-data / open-standard posture**: Open311 endpoints, open data portals, procurement mandates (NYC/Chicago/SF RFPs).
- **Suite embedding**: SRM as a module of a broader civic platform (Accela permitting/licensing/asset; Granicus forms/website/communications) vs standalone reporting product (FixMyStreet, SeeClickFix).
- **Deployment**: SaaS vs self-hosted open source (FixMyStreet Platform, uReport, Mark-a-Spot).
- **Scale/jurisdiction**: single city; county; multi-jurisdiction regional systems (Open311 `jurisdiction_id`; FixMyStreet multiple bodies per area).
- **AI intake assistance** (current generation): photo-based type suggestion, clarifying-question assistants, auto-redaction (Accela).
- **Emergency diversion rules** (category questions that disable submission and point to emergency numbers — FixMyStreet).
- **Post-resolution surveys** (FixMyStreet 4-week questionnaire).
- **Information requests** (non-location inquiries, e.g., "how do I get a driver's license") handled by the same platforms — NYC Inquiry API exists for this; common extension, not the defining object.

### L3 — Vendor-specific (research notes only)

- Accela: CivicAI branding; license-plate auto-redaction; two-way department synchronization; SRM/CRM dual naming.
- Granicus: Service Designer, Integration Manager, Customer Service Hub, Staff Portal as named modules; second SRM product line (OneView).
- FixMyStreet: MapIt boundary service; cobrand system; Message Manager (SMS gateway); shortlists/inspector assignment; offline inspection; "Report As" permission set; Pro default six-month update-close window; ≤20-category best practice; 4-week survey default.
- Open311: jurisdiction_id convention (jurisdiction's domain as id); realtime/batch/blackbox submission types; 90-day/1000-request query window; token resource.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model.

## Rejected Findings

- "311 phone number / call center is the defining structure" — rejected: regional (North America); FixMyStreet/CitySDK deployments satisfy the Type without either. The call center is one intake channel and one program wrapper.
- "Public map of all requests is defining" — rejected: Accela and Granicus center requester-private status; public transparency is a jurisdiction posture (L2).
- "Mobile app is defining" — rejected: phone/agent and web intake predate and outlast app-only patterns; SMS exists (FixMyStreet).
- "Work order management is part of the Type" — rejected as structure: the common pattern is integration/handoff; some suites bundle execution, but the 311 platform's own object is the request, not the work order.
- "AI intake is defining" — rejected: single-vendor, current-generation feature (L2).
- "Surveys/questionnaires are defining" — rejected: FixMyStreet-specific in this sample (L2).
- "Duplicate merging is defining" — rejected: common (L1), not required to recognize the Type.

## Boundary Findings

- **vs Government Service Portal**: a portal is the access/transaction surface for many government services (payments, permits, information); the 311 platform is the request intake + routing + fulfillment-tracking system. Portals may embed request forms; 311 platforms may expose a portal as one channel. Test: remove routing/lifecycle/status-feedback → only a form/portal remains; remove payments/permits/content → the 311 platform remains.
- **vs Public Sector Case Management**: case management handles long-lived, caseworker-owned, eligibility-driven cases (benefits, social services); 311 handles high-volume, short-cycle, location-based service requests fulfilled by operational departments. Test: caseworker ownership + eligibility determination + weeks/months duration → case management; minutes-to-days intake + location routing → 311.
- **vs Help Desk / Ticketing System (private sector)**: same ticket shape (record → route → work → close → notify), but the 311 platform's catalog is government services, routing is location/jurisdiction-aware, the requester is a resident (not a customer), and public accountability/transparency is structurally present. Test: replace the civic catalog + location routing + resident framing → generic ticketing.
- **vs Code Enforcement Management**: enforcement is a departmental violation workflow (inspection → notice → citation → re-inspection); 311 requests may spawn enforcement cases. Test: object is a citizen request vs a regulatory violation.
- **vs Public Works Management / work order systems**: 311 creates and tracks requests; work order systems execute field work. The handoff (request → work order → completion → status back) is the integration seam. Products like Cityworks merge both on a GIS/asset backbone — a suite-embedding variant, not evidence that execution is part of the 311 core. Test: remove field execution → 311 platform remains; remove citizen intake/status → work order system remains.
- **vs Computer-aided Dispatch (911/CAD)**: emergency vs non-emergency; CAD dispatches seconds-scale response units; 311 routes days-scale service fulfillment. FixMyStreet's emergency-diversion pattern shows the boundary is actively enforced in products.
- **vs Constituent Relationship Management**: CRM centers the ongoing relationship/history with a person across all interactions; 311 centers the request lifecycle. Market evidence of adjacency: Accela names the module "Service Request Management (SRM/CRM)". Test: remove the relationship profile/history → 311 remains; remove request fulfillment → CRM remains.
- **vs Government Contact Center**: the contact center is the channel/agent infrastructure; the 311 platform is the request management system behind it (Granicus hub integrates with phone systems; FixMyStreet Pro supports agent-created reports). Test: remove request lifecycle → contact center remains.
- **vs Civic Engagement Platform / Petition Platform**: engagement collects opinions/ideas/petitions without fulfillment obligations; 311 requests carry an expectation of government action and status feedback.

Taxonomy observation: the leaf name embeds "311", a regional program brand. The researched Type is broader (global citizen service request reporting). No conflicting leaf exists in the directory; no rename proposed unilaterally.

## Uncertainties

- Granicus govService's location/GIS handling was not detailed on the fetched page (forms-first framing); location routing for that product is inferred from the product family and kept at weak assertion strength.
- Exact status vocabularies for Accela and Granicus were not documented on fetched pages; only Open311 (open/closed) and FixMyStreet (unconfirmed/open/fixed/in progress/no further action/closed/hidden) have documented states.
- Tyler Enterprise 311, Cityworks, SeeClickFix, and Salesforce public-sector pages were unreachable (403/404/redirect); claims about them are limited to third-party descriptions (SeeClickFix via Open311 site) or omitted entirely.
- Numeric limits and defaults (SLA durations, category counts, duplicate radii) are product-specific where documented (FixMyStreet Pro) and were not generalized.
- The relative market weight of call-center-centric vs web-first deployments could not be quantified from accessible sources.

## Final Synthesis

A 311 / citizen service request platform is a government-operated request management system. Its unit of work is a resident-initiated (or agent-created-on-behalf) service request for a non-emergency civic need, categorized against a jurisdiction-defined service catalog and located by address/geography; the platform routes it to the responsible government unit, tracks it through a lifecycle to resolution, and feeds status back to the requester. Around this core, mature products add multi-channel intake (portal, app, phone/agent), requester notifications, media, duplicate handling, SLA expectations, staff consoles, reporting, and integration to work order/asset systems for field fulfillment. The 311 phone number, the call center, public maps, mobile apps, and AI intake are regional, programmatic, or generational wrappers — not the defining structure. The Type sits between the Government Service Portal (access surface), Public Sector Case Management (long-cycle casework), work order systems (field execution), and CAD (emergency dispatch), and is distinguished from each by the citizen-originated, catalog-categorized, located, routed, tracked, status-fed-back request record.
