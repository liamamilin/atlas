# Research Notes — Building Access & Visitor Management

Research date: 2026-09-06
Leaf: Building Access & Visitor Management (DIRECTORY §17 Construction, Real Estate & Facilities)
Slug: building-access-visitor-management
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Understand what software in this category actually does: how buildings control who crosses their boundary, and how the temporary-visitor path through that boundary is managed — from real products, not from marketing abstraction.

## Initial Boundary

Initial hypothesis (Step 1):

- **What is it**: software that (a) decides and records who may physically enter a building or its controlled zones — via doors, gates, turnstiles, elevators, lobbies — and (b) manages the arrival, admission, hosting and departure of temporary visitors.
- **Who**: property/facility managers, security teams, office managers, front-desk/reception staff, tenants/residents, hosts; the visitor themselves as an end user.
- **Nearest Types**: Building Management System / BMS (plant automation), Space & Occupancy Management, Campus Card Management, Time & Attendance, Hotel PMS/front desk, Workplace Management platforms, IT IAM, video surveillance suites, Package & Mailroom Management, Amenity Booking.
- **Suspected risk**: the market actually contains TWO product families — physical access control systems (ACS/PACS) and visitor management systems (VMS) — sold both separately and combined. The directory has one combined leaf. This needs explicit treatment.
- **Unknowns**: how combined products unify the two poles; how visitor-first products relate to door hardware; regional compliance overlays.

## Research Questions

1. What are the core objects? (entry point, person, credential, group/level, schedule, event, visitor record)
2. How does an occupant get authorized and enter? (provision → assign → credential → verify → record)
3. How does a visitor move through the boundary? (pre-register/invite → check-in → screening → badge/credential → host notification → sign-out)
4. What rules gate the decision? (groups, schedules, watchlists, approvals, time bounds)
5. What does live operation look like? (event monitoring, remote unlock, lockdown, incident response)
6. What surfaces exist? (admin console, kiosk/tablet, mobile app, visitor form, integrations)
7. What exceptions matter? (lost credentials, forced/hold-open door, offline devices, visitor no-show, denied check-in)
8. How do the access pole and visitor pole relate in combined products (visitor → temporary credential)?
9. Boundary vs BMS, Time & Attendance, Campus Card, Hotel PMS, IT IAM, Space Management.
10. Would older/simpler products (card+logbook era, intercom+fob multifamily, iPad digital logbook era) still fit the definition?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophy + different customer tiers.

| Product | Pole | Segment | Evidence level reached |
|---|---|---|---|
| Kisi | access-first with integrated visitor module (beta) | SMB/mid-market commercial office | A — full operational docs (docs.kisi.io) |
| Swiftlane | combined access + video intercom + visitor passes | multifamily residential + small commercial | A — operational help center (support.swiftlane.com) |
| Envoy | visitor-first enterprise workplace platform | enterprise workplace, multi-location | A — help center (envoy.help) for visitor pole; product pages for platform; door access via integrations |
| Verkada | access-first enterprise, hybrid-cloud | enterprise, multi-site security | B/positioning — official product page (docs 403) |
| Brivo | access-first cloud ACS, unified security suite | commercial real estate / multifamily / enterprise | positioning — official product page (help KB unreachable ×2) |

Note: Brivo was originally sampled for its knowledge base (answers.brivo.com); after repeated transport errors it was demoted to positioning-level evidence. Verkada docs.verkada.com returned 403; the official access-control product page was used instead. Neither product's operational details are asserted anywhere in the outputs.

## Sources

Tier 1 (operational docs, fetched 2026-09-06):

- Kisi Product Documentation — https://docs.kisi.io/ (root), /access_control/, /visitor_management/, /visitor_management/share_access_with_visitors, /visitor_management/visitor_registration_point, /access_control/doors/, /quick_start/admins/
- Swiftlane Help Center — https://support.swiftlane.com/en/collections/10329490-i-m-an-admin (collection index), /articles/9810805-access-group-overview, /articles/9810829-how-do-i-create-a-visitors-pass
- Envoy Help Center — https://envoy.help/en/ (root), /collections/1930712-visitors (Visitors collection index), /articles/3330129-about-envoy-visitors

Tier 2 (official product pages, fetched 2026-09-06):

- Verkada Access Control — https://www.verkada.com/access-control/
- Brivo — https://www.brivo.com/
- Envoy platform — https://www.envoy.com/products (module architecture, ACS integrations list)

Unreachable (recorded per source-access limitation rule):

- answers.brivo.com — transport error ×2 → Brivo operational detail NOT asserted
- docs.verkada.com — 403 → Verkada operational detail NOT asserted
- support.kisi.io Zendesk portal — transport error (superseded by docs.kisi.io, which succeeded)
- www.envoy.com/products/protect — timeout; replaced by /products platform page (which does not name Protect; no Protect-specific claims made)

## Product Observations

### Kisi (evidence layer A)

Architecture and concepts:

- Hierarchy: Organization → Places (physical location with address) → Doors → Groups → Users.
- **Door** = entry point represented in software: "Doors in the Kisi system represent entry points into a facility… Each door corresponds to a physical door and is connected to up to four relays on the Kisi Controller." Doors can also represent elevators, gates, turnstiles. A door is associated with controller relay + reader in the dashboard.
- Lock hardware taxonomy: electric strike (fail safe / fail secure), magnetic lock (fail safe), wireless smart locks; door = reader + controller + lock.
- **Group** = the authorization unit: "Groups define which Doors Users can unlock." Users are invited by email; access granted by assigning user to group linked to a door ("Share Access").
- **Credentials**: digital (access links, QR codes, Apple passes, mobile credentials) and physical (cards, fobs); temporary digital credential with *Valid From* / *Valid Until* dates.
- Door controls: door restrictions, door access schedules, unlock schedules, "first to arrive" schedules, door lockdown; floors/elevators as access-controlled points; capacity management per place.
- Monitoring: event history, reports, incident policies (automated responses to incidents); hardware connectivity/offline support docs; live + audit surfaces.
- Org machinery: teams, SSO, SCIM provisioning, admin roles, door quotas (licensed per door).
- Mobile member app: unlock doors; members quick start.

Visitor management (feature in beta per docs):

- Visitor = temporary member added to a **group** with a **validity date** (pre-added by admin/host: "Select the group the user should be added to… Set a validity date for the access").
- Two paths: (1) dashboard add visitor → access link emailed to visitor; (2) **visitor registration point** — self-service check-in on a dedicated kiosk/tablet/QR form: visitor fills registration form (name, host selected from a host Team, visit reason e.g. "Interview"/"Delivery", optional photo), host notified by email/Slack, visitor is added to the selected group with an **access duration (hours after check-in)**.
- Registration point config: multiple per organization; hosts from Teams (syncable via SCIM); visit reasons; branding/logo; access method (QR code / access link / both); NDA acceptance via uploaded agreement PDFs with version history — "the visitor management log tracks which agreement version each visitor accepted"; badge printing at check-in (kiosk bundle or connected label printer); badges include name, date, reason.
- Visitor log: *Future visitors* and *Past visitors* tabs; entries show name, email, who issued access, group, validity period; CSV export; "Visitor logs are stored indefinitely for record-keeping and audit purposes."
- Delegation: admins can delegate visitor management to non-admin users; cancel/deactivate visitor access; adjustments of visit times.

### Swiftlane (evidence layer A)

Architecture and concepts:

- Hierarchy: Workspace → Sites → **Access Points** (doors equipped with SwiftReader devices/intercoms, controllers, relays) → **Access Groups** → Users (residents/tenants/employees).
- "Under the 'Access Groups' menu screen, you can 'Add Groups', 'Add User to Group', edit and delete Groups." Access groups bind users to access points; admin can check which access group has access to which access point.
- Credentials: PIN codes (self-service or admin-issued; users without smartphone/email get PINs), key fobs/keycards/vehicle tags, mobile app (face unlock), visitor passes.
- **Intercom**: SwiftReader as video intercom; intercom directory (residents), call routing to multiple people, front-desk assignment, calls to browser/cell/landline; "Call Front Desk" option on the door device.
- Schedules: access point schedules per access group, door unlock schedules, holidays, date-range schedules, schedule overrides.
- Monitoring: activity feed (exportable), audit logs, health check for devices, remote reboot, kiosk mode for door devices; remote access grant/revoke.
- Integrations: property management platforms (AppFolio, Entrata, RealPage, Yardi, Buildium), identity (Okta), Brivo sync, smart locks (August/Yale, Igloo), video (Eagle Eye).

Visitor handling:

- **Visitor PINs screen**: create single-use and multi-use visitor passes. Single-use pass deactivates after PIN entry (docs state after 5 minutes — product-specific detail). Multi-use pass bounded by activation date/time and deactivation date/time.
- Visitor passes can be restricted to certain access groups; passes can be deactivated.
- Delivery access: dedicated delivery PINs handed to carriers (Amazon, UPS, USPS, FedEx) — a standing visitor-like access for delivery personnel.
- Invite expiry exists ("Does a Swiftlane invite expire?").

### Envoy (evidence layer A for visitor pole; positioning for platform)

Positioning: "Envoy unifies visitors, spaces, and communications into one enterprise-ready workplace management platform." Products are **modules** on a required platform: visitor management, resource booking, mailroom, critical event management, digital signage. Presence signals include HRIS, MDM, WiFi, **ACS** (access control systems), SSO, geo. Envoy integrates with third-party access control systems (Brivo, Avigilon Alta, LenelS2, Honeywell ProWatch, Genetec, Cisco Meraki) — i.e., visitor-first product that connects to the door layer via integrations.

Visitor machinery (help center, 138-article Visitors collection):

- **Visitor entry** = the central record: "When a visitor signs in, Envoy creates a visitor entry… the record of their visit: all of the visitor's information, including sign-in and out times, their photo, signed legal documents and more." Entries appear on the dashboard in real time.
- **Sign-in flows**: customizable per **visitor type** (e.g. interview, contractor, event); sign-in fields configurable; flow rules with response-dependent actions; returning-visitor memory; touchless sign-in via mobile; static QR code sign-in; walk-in visitors; offline mode for the iPad kiosk.
- **Invites / registration (pre-registration)**: invite emails, invite log, group invites, bulk invites, multi-location invites, multiple hosts, calendar add-in (Outlook), visitor completes registration before arrival; QR code pass for sign-in; invite approvals queue (global); automatic approval permissions.
- **Screening & compliance**: block list ("prevent unwanted guests"), watch list, ID check, ID scanning (verify ID validity), visitor photos, facial recognition sign-in, legal documents (NDA/waiver e-sign at sign-in or pre-arrival, with storage), visitor assessments, pre-registration document uploads, evacuation support ("who's in the building"), walk-up visitor approvals, Advanced Visitor Approvals (policies, decision tables, risk intel, compliance screening), Martyn's Law (UK Terrorism Protection of Premises Act 2025) setup guide.
- **Notifications**: host notifications (email/SMS/Slack/Teams) when guests arrive; assistant notifications; fallback notifications when no host; sign-out reminders to hosts.
- **Badges**: automatic badge printing at check-in; badge printer hardware; badge settings.
- **Visitor log & data**: visitor log with blocklist action; visitor directory with profile matching rules; entry history log; editing/deleting entries; exports; analytics dashboard; global overview across locations; global invite log.
- **Kiosk**: iPad sign-in app (or Neat Frame device); virtual front desk (remote receptionist via kiosk video call).
- Sign-out: manual/automatic host sign-out; benefits documented.

### Verkada (evidence layer B/positioning — product page only)

- "Hybrid cloud access control": controllers + door readers + credentials (mobile NFC in Apple Wallet, encrypted keycards, Bluetooth, license-plate-recognition unlock) + wireless locks + Access Station (video intercom device).
- Command platform: web + mobile (Verkada Pass app) management; door events with natively integrated video ("see video of door events"), tailgating alerts, live door events, remote control.
- Edge processing: "Maintain door operations even in the event of network outages."
- User management automation: SCIM and SSO, bulk user management, APIs.
- **Verkada Guest**: "Provide guests with mobile or physical credentials and easily track visitor movement" — visitor management as companion module.
- Intercoms "with a door controller and badge reader built in"; intrusion alarm arm/disarm via badge swipe.

### Brivo (evidence layer: positioning only)

- "Brivo Security Suite: Centralize access control, video surveillance, visitor management, alarms, and sensors into a single, cloud-native platform."
- Access control: "Easily control who can access your buildings and while tracking all activity within a secure cloud-based platform." Hardware lines: credentials, readers, control panels, commercial door locks, intercoms.
- Visitor management: "Monitor all guest and vendor traffic at every entry point to ensure total visibility over who is on site."
- Industries: multifamily, commercial real estate, coworking, retail, warehouse, education, government, healthcare, etc.
- Integrations via open API: Azure AD/Okta provisioning, workspace/visitor tools (Envoy), property management (Entrata).
- Marketing stats (78K customers, 87 countries, 5M mobile credentials, 15M credentialed users) — vendor-claimed, not used.

## Cross-product Comparison

| Structure | Kisi | Swiftlane | Envoy | Verkada | Brivo | Judgment |
|---|---|---|---|---|---|---|
| Entry point as managed software object (door/access point bound to hardware) | Door | Access Point | (via ACS integrations; kiosk admits at lobby) | controllers/readers (product page) | access control line (product page) | **L0 — universal** |
| Person identified at the boundary | User + credential | User + PIN/fob/app | visitor entry + photo/ID | users + credentials (product page) | credentialed users (product page) | **L0 — universal** |
| Grant/deny decision under configured rules | group × door × schedule | access group × access point × schedule | check-in flow + approvals/blocklist/watchlist | badge decision w/ edge rules (product page) | "who can access and when" (product page) | **L0 — universal** |
| Recorded entry/visit events (audit + live) | event history, incident policies | activity feed, audit logs | visitor entry real-time on dashboard, entry history | door events with video (product page) | "tracking all activity" (product page) | **L0 — universal** |
| Visitor as distinct person class with bounded authorization + host linkage | visitor added to group w/ validity; duration after check-in | visitor passes w/ activation/deactivation; restricted to groups; deactivate | visitor entry, invite lifecycle, host notifications, sign-out | Guest: mobile/physical credentials for guests | visitor management module ("guest and vendor traffic") | **L0 (for this leaf) — universal across sample** |
| Access groups/levels binding people→doors | Groups | Access Groups | n/a (integration) | user groups (product page, generic) | (not observed) | **L1** |
| Schedules / time windows | door access schedules, unlock schedules, first-to-arrive | schedules, holidays, overrides | (visit dates/validity) | (product page implies; not detailed) | "modify schedules" (FAQ-level) | **L1** |
| Multi-form credentials (card/fob/PIN/mobile/QR/biometric) | digital+physical credentials, Apple passes | PIN/fob/keycard/vehicle tag/app/face | QR pass, facial recognition sign-in | Apple Wallet NFC, keycards, BT, LPR | mobile credentials, readers | **L1** |
| Visitor check-in machinery (kiosk/form, host notification, badge, sign-out) | registration point, Slack/email host notif, badge printing | (pass issuance; intercom admits) | full machinery: flows, invites, badges, photos, NDA, sign-out | Guest module | visitor mgmt module | **L1** (depth varies) |
| Visitor screening (blocklist/watchlist/ID/approvals) | (agreements only observed) | (not observed) | full: blocklist, watchlist, ID scan, approvals, risk intel | (not observed) | (not observed) | **L2 — compliance depth varies** |
| Live monitoring + response (remote unlock, lockdown, incident policies) | lockdown, incident policies, event history | remote unlock/reboot, health check, lockdown app (kiosk mode) | evacuation, iPad status alerts, walk-up approvals | live door events + video, tailgating alerts | 24/7 monitoring, lockdown (use case) | **L1** (response depth varies) |
| Self-service by end users (invite guests, manage PINs) | member app unlock | users create PINs; tenants manage | employees invite via calendar; touchless sign-in | Verkada Pass app | mobile credentials | **L1** |
| Directory/identity integration (SCIM/SSO/HRIS) | SSO, SCIM, Teams | Okta | HRIS/MDM/WiFi/ACS/SSO presence signals | SCIM/SSO | Azure AD/Okta | **L1** |
| Intercom / video intercom as entry surface | (not observed) | SwiftReader intercom, call routing | virtual front desk | Access Station/intercoms | intercoms | **L2 — market/segment variant** |
| Adjacent modules bundled (video, intrusion, alarm, desks, deliveries) | video surveillance, intrusion, bookings | Eagle Eye video, property-mgmt integrations | resource booking, mailroom, CEM, screens | video security, alarms, workplace | video, intrusion, sensors, POS integration | **L2 — bundling philosophy** |
| Property-management / residential tilt | (commercial) | AppFolio/Entrata/RealPage/Yardi, delivery PINs | (workplace) | (enterprise) | multifamily industry pages | **L2 — segment variant** |
| Cloud/hybrid/edge architecture posture | cloud controller | cloud + device health | cloud SaaS platform | hybrid cloud w/ edge processing | cloud-native suite | **L2 — deployment variant** |

## Canonical Model (Step 5)

The system's world:

```text
Building boundary
└── Entry points (doors, gates, turnstiles, elevators, lobby) — managed objects bound to hardware
    └── Person attempting to cross
        ├── Occupant (persistent authorization)
        │   └── credential (card/fob/PIN/mobile/QR/biometric)
        └── Visitor (bounded authorization)
            └── registration/invitation + check-in record
    └── Access rule set (who × where × when)
    └── Decision: grant / deny (automated verification, or admission at check-in)
    └── Entry/visit event record (live monitoring + persistent audit)
```

Visitor sub-model:

```text
Visitor
└── Pre-arrival: invite / pre-registration (host, purpose, validity)
└── Arrival: check-in (form fields, photo, ID, agreement e-sign, screening)
    └── Host notification
    └── Badge and/or temporary credential (door access for the visit duration)
└── Departure: sign-out / pass deactivation
└── Visit log retained (audit, compliance, evacuation)
```

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

1. **Managed entry points** — the building's controlled crossings (doors/gates/lobbies; optionally elevators, turnstiles) exist as configured software objects bound to physical control hardware or an admission surface.
2. **Identified person at the boundary** — whoever crosses is bound to a person record: occupants via credentials, visitors via registration/check-in.
3. **Grant/deny decision per crossing under configured rules** — automated credential verification for occupants; admission decision (possibly human/approval-mediated) for visitors.
4. **Recorded crossing events** — every entry (and, where supported, exit) becomes a persistent record feeding live monitoring and audit.
5. **Visitor as a distinct person class with bounded, host-linked authorization** — temporary validity, explicit ending (sign-out/deactivation/expiry), and a visit record.

Items 1–4 alone = access control; item 5 + the admission/check-in flow = visitor management. The leaf names both, and every sampled product carries both (as native modules or companion modules), so the combined Type is documented as one boundary-control Type with two person-poles. Historical check: a 2000s card-access panel with a visitors logbook has properties 1–4 mechanically and property 5 on paper; an iPad-era digital visitor logbook has 2–5 at the lobby with the door decision delegated to reception. The definition does not require mobile credentials, cloud, or biometrics — no era/vendor overfit.

### L1 — Common Mature Structure

- Access groups/levels binding persons to sets of entry points
- Schedules: time windows per door/group, holiday calendars, unlock schedules, overrides
- Credential management across multiple form factors (card/fob, PIN, mobile app, QR link/pass, wallet pass, biometric/face, license plate)
- Visitor check-in machinery: kiosk/tablet/QR self-service or assisted sign-in; configurable check-in forms/fields per visitor type; host notification (email/SMS/chat); badge printing; visitor photos; agreement/NDA e-signature; sign-out
- Visitor log: past/upcoming views, issuance attribution, exports, long retention for audit
- Live event monitoring and response: event feed, remote unlock, lockdown, device health/offline status, incident policies/alerts
- Role model: org/site admins, security operators, front desk/reception, delegated hosts, occupants (employees/residents/tenants)
- Self-service: occupants unlock doors, manage PINs, invite their own guests; hosts see and sign out guests
- Identity/directory integration: SSO, SCIM/HRIS sync of the person population
- Reporting/analytics: entry history, occupancy, visitor traffic
- Calendar-based invites (visitor expected via calendar/meeting integration)
- Capacity/occupancy surfaces ("who is in the building")

### L2 — Variant / Optional Structure

- **Pole of gravity**: access-first (Kisi, Verkada, Brivo — visitor module added) vs visitor-first (Envoy — door layer via third-party ACS integrations) vs combined-native (Swiftlane)
- **Market segment**: commercial office (Kisi, Envoy), enterprise multi-site (Verkada, Brivo), multifamily residential (Swiftlane, Brivo — intercom, delivery PINs, property-mgmt integrations), institutional (schools, government — Brivo industry pages)
- **Entry surface**: reader+controller standard doors; video intercom with call routing; kiosk-admitted lobby; turnstiles/elevators/parking (LPR) extensions
- **Deployment architecture**: cloud-native ACaaS, hybrid-cloud with edge processing (offline door decisions), on-prem legacy panels behind modern software
- **Compliance depth**: basic digital logbook → ID scanning, watchlists, blocklists, approval workflows, regional regimes (e.g. UK Martyn's Law setup guides, EU data residency)
- **Adjacent bundling**: video surveillance, intrusion alarms, mailroom, desks/rooms booking, digital signage, emergency notification (suite philosophy varies: unified suite vs module platform vs standalone)
- **Residential extensions**: carrier/delivery standing access, self-guided tours, tenant self-service PINs
- **Visitor depth**: simple pass issuance → multi-step approvals with decision tables and risk screening

### L3 — Vendor-specific (kept out of final document)

- Kisi: door-license quotas; max 250 groups per door; Kisi Kiosk Pro + Brother label printer bundle; visitor management in beta; registration-point Teams/SCIM host sync; agreement version tracking; magic-link admin auth; "first to arrive" schedules
- Swiftlane: single-use pass deactivates 5 minutes after PIN entry; single/multi visitor pass types with activation/deactivation datetimes; delivery PINs for named carriers (Amazon/UPS/USPS/FedEx); SwiftReader kiosk mode; Brivo sync; named property-mgmt integrations
- Envoy: "visitor entry" object and entry history log; global invite log; Advanced Approvals (policies/decision tables/Visual Compliance risk intel); Martyn's Law setup guide; Neat Frame kiosk; Virtual Front Desk; plus-one sign-in; facial-recognition sign-in; platform-tier + module pricing
- Verkada: hybrid-cloud edge claims; Verkada Pass app; tailgating alerts; LPR unlock; Apple Wallet NFC credentials; badge-swipe alarm arm/disarm; 10-year warranty marketing
- Brivo: unified-suite stats (customers/countries/credential counts — vendor-claimed); Eagle Eye video editions; voice-activated lockdown marketing; named integration marketplace

## Vendor-specific Findings → rejected from canonical core

- Visitor management "beta" status (Kisi) — implementation maturity detail.
- 5-minute single-use pass expiry (Swiftlane), 250-group door cap (Kisi), indefinite visitor-log retention (Kisi) — precise numeric claims, single-source, excluded from final doc per precision rule.
- Envoy platform modules (desks, rooms, deliveries, screens, CEM) — belong to Workplace Management platform, not this Type.
- Verkada/Brivo operational claims — evidence never reached operational docs; nothing asserted.

## Boundary Findings

- **vs Building Management System / BMS**: BMS automates building plant (HVAC, lighting, energy, plant monitoring); this Type controls *people* crossing the boundary and records it. Remove people-decisions → BMS. Remove plant → this Type. They co-exist in building stacks; some suites bundle access control into broader building/security platforms (module-of-suite flag).
- **vs Time & Attendance**: door events can feed attendance, but attendance owns work-time semantics (shifts, breaks, payroll, leave). Remove the entry-permission decision, keep hours worked → Time & Attendance. Badge-clock overlap is a data handoff, not a Type identity.
- **vs Campus Card Management**: campus card is person-centered across many institutional services (dining, print, door access, events); this Type is boundary-centered on the building. Door access is one downstream consumer of a campus credential. A campus-card product without boundary decisions is not this Type; a building access product without multi-service entitlements is not Campus Card.
- **vs Hotel PMS / Hotel Front Desk**: hospitality guest registration is folio/stay-economics-centric; room-lock integration is downstream. This Type has no stay/folio economics. Remove payment/stay objects → this Type; add them → Hotel PMS.
- **vs IT IAM / SSO / MFA**: digital-resource authentication vs physical-boundary authorization. Convergence exists (same directory, SCIM provisioning, mobile credentials, some vendors marketing "identity convergence"), but the managed object differs: doors and visits vs apps and sessions. Remove the physical boundary → IAM.
- **vs Space & Occupancy Management / Amenity Booking**: those manage *booking of space and time*; this Type manages *crossing a boundary*. A door decision is not a reservation. Occupancy analytics overlap is reporting only.
- **vs Video Surveillance / unified security suites**: video is evidence/monitoring; this Type is the decision surface for entry. Many vendors bundle both; bundling does not merge the Types.
- **vs Package & Mailroom Management**: visitors are people; packages are objects. Carrier standing-access PINs (Swiftlane) are an access-grant for delivery personnel — still people crossing, so in-scope; parcel logging itself is not.
- **vs Event/Attendee Management**: event check-in admits *event attendees* against a ticket/registration for an occasion; this Type admits people to a *building/zone* under standing or visit-based rules. Overlap appears for events hosted in buildings (Envoy markets event use); the center of gravity differs (occasion vs boundary).
- **"Remove X and it becomes another Type" criteria**:
  - remove entry-point decisioning, keep visitor logs → visitor sign-in tool drifting toward event/workplace check-in (Envoy's own platform drift is the example)
  - remove visitors → a pure physical access control system (no separate leaf exists in the directory — flagged below)
  - remove the physical boundary → IT IAM
  - remove people → BMS
  - keep space-time booking → Space Management / Amenity Booking

## Uncertainties

1. **Brivo operational behavior unknown** — help KB (answers.brivo.com) unreachable ×2; only positioning used. If Brivo docs become reachable, re-verify: access-level model, visitor module mechanics, event/monitoring surfaces.
2. **Verkada operational behavior unknown** — docs.verkada.com 403; product page used. Same caution for: group model, schedules, Guest module mechanics.
3. **Kisi visitor management is beta** — mechanics may change; used as evidence of the combined pattern, not of market-wide maturity.
4. **Pure-VMS without any door capability**: does it satisfy "managed entry points"? Resolved canonically: the lobby/admission surface acts as the entry point (decision at check-in), and Envoy's ACS integrations show the pattern of linking to the door layer. Noted as inference, not direct observation.
5. **Directory granularity**: the market sells pure ACS and pure VMS separately. Whether the atlas should hold a combined leaf or split into two leaves is a taxonomy decision — flagged in Boundary Issues, not resolved here.

## Final Synthesis

A Building Access & Visitor Management application is the operating system for a building's controlled boundary: it turns entry points into managed, rule-governed decision surfaces; it binds each crossing to an identified person — a persistently authorized occupant carrying a credential, or a temporarily authorized visitor moving through registration, check-in, hosting and sign-out; it makes and records a grant/deny decision for each crossing; and it keeps the resulting event/visit records for live operation, audit and compliance. Access groups, schedules, multi-form credentials, kiosk check-in machinery, host notifications, badges, monitoring/response, and directory integrations are the mature market's standard capabilities; visitor-first vs access-first posture, segment, compliance depth, deployment architecture and module bundling are variants. Its nearest neighbors — BMS (plant, not people), Time & Attendance (hours, not entry), Campus Card (person-services, not boundary), Hotel PMS (stay economics), IT IAM (digital resources), Space Management (booking, not crossing) — are separated by center of gravity, not by feature overlap.
