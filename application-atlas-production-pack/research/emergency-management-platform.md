# Research Notes — Emergency Management Platform

## Research Goal

Understand what an Emergency Management Platform actually is as an Application Type: the core objects, the coordination model, the workflows of emergency/disaster response, the interfaces EOC and field users face, the rules that govern behavior, and the boundaries against neighboring Types (CAD, Public Alert & Warning, IT Incident Management, Business Continuity, agency records systems).

## Initial Boundary Hypothesis (before research)

- Guess: software for emergency management agencies (EOC-centric) to prepare for, respond to, and recover from emergencies/disasters; organized around an incident/event; multi-agency; often ICS/NIMS-aligned (US).
- Likely confusions: Computer-aided Dispatch (unit-level dispatch), Public Alert & Warning (outbound mass alerting), IT Incident Management, Business Continuity Management (corporate continuity planning), Fire/EMS/Police records systems.
- Unknowns: is the "status board" a defining structure or a vendor implementation? How central are resource management, damage assessment, preparedness? How strong is ICS coupling (US-centric risk)?

## Research Questions

1. What is the central object (incident/event) and its lifecycle?
2. How is the shared operational picture implemented (boards, dashboards, maps)?
3. How are tasks, requests, and resources modeled and tracked?
4. How do roles/positions work during a response?
5. How does situation reporting work and what does it produce?
6. What preparedness machinery exists (plans, rosters, equipment, exercises)?
7. What recovery machinery exists (damage assessment, cost documentation, reimbursement)?
8. What interfaces do users face?
9. What rules matter (permissions, audit, doctrine alignment, configurability)?
10. What variants exist (government vs corporate vs campus; all-hazards vs specialist)?

## Representative Products

| Product | Vendor | Why sampled | Evidence tier reached |
|---|---|---|---|
| WebEOC Nexus | Juvare | Incumbent government EOC platform; deployed in all 50 US states (vendor claim); board-based architecture | Tier 1 (official user + admin help centers) |
| D4H Incident Management | D4H | Modern SaaS; readiness + response; government + corporate + volunteer; strong public help center | Tier 1 (official help center articles) |
| Veoci | Veoci Inc. | "Virtual EOC" all-in-one suite; no-code platform; government + aviation + higher-ed + healthcare | Tier 2 (official product pages) |
| Noggin | Noggin (a Motorola Solutions company) | Integrated resilience workspace; corporate + government CEM pole; international (AIIMS/JESIP/NIMS) | Tier 2 (official product/solution pages) |
| Crisis Track | Juvare | Recovery/damage-assessment specialist pole; FEMA grant documentation | Tier 1 (official help center) |

Deliberately not sampled (boundary references only): Everbridge/OnSolve (mass-notification-led CEM), DisasterLAN (DLAN), Mission Manager, Microsoft Teams EOC — named as competitors in D4H's own comparison pages but not directly researched; no claims made about them.

## Sources

Fetched 2026-09-07:

- Juvare — WebEOC Nexus User Help Center: https://docs.juvare.com/webeoc-onnexu/landing.htm (Get Started; Navigate the User View; Landing Pages; Use Boards; Standard Plug-Ins)
- Juvare — WebEOC Nexus Admin Help Center: https://docs.juvare.com/webeoc-onnexa/landing.htm (Get Started; WebEOC Nexus Key Concepts; Boards List and Downloads)
- Juvare — Help Center portal (product family descriptions): https://docs.juvare.com/help/landing.htm
- Juvare — WebEOC for Private / Business Continuity product page: https://www.juvare.com/webeoc/
- Juvare — Crisis Track Help Center: https://docs.juvare.com/crisis_track/landing.htm ; Incident Functions: https://docs.juvare.com/crisis_track/incident-functions/what-are-incidents.htm
- D4H — Incident Management product page: https://www.d4h.com/incident-management
- D4H — Help Center: https://help.d4h.com (collections index; Getting Started Guide; Situation Overview; Roles Module Overview; Status Board Module Overview)
- Veoci — corporate site + Emergency Management solution page: https://www.veoci.com/ ; https://www.veoci.com/emergency-management
- Noggin — corporate site + Emergency Management solution page: https://www.noggin.io/ ; https://www.noggin.io/solutions/emergency-management

## Product Observations

### WebEOC Nexus (Juvare) — Evidence layer A unless noted

Positioning (help center, Tier 1): "a cloud SaaS platform for emergency management that provides a common operating picture for critical events." "WebEOC Nexus can be used during the planning, mitigation, response, and recovery phases of any emergency. It can also be used by agencies and organizations during day-to-day activities to manage routine, nonemergency operations."

Key concepts (Admin Help Center, Tier 1 — near-verbatim):

- **Incidents**: "events, disasters, or disruptions that require a planned, coordinated response to resolve them to protect life or property. They can be natural or human-caused. In WebEOC Nexus, incidents are a fundamental mechanism for organizing emergency response data." Users "must select from a position and incident to view data." Incidents can be created, deactivated, deleted. Some boards are incident-dependent.
- **Boards**: "the heart of WebEOC Nexus… the mechanisms you use to manage and share real-time incident information with authorized users in your system and between linked systems… used as apps or workflows and are highly customizable." "In the context of a crisis information management system (CIMS), a WebEOC Nexus board is equal to a large, chronological or categorical paper-based status board that used to dominate EOCs and command centers around the country." Standard government forms (ICS forms, FEMA forms, situation reports, resource boards) are built as boards.
- **Views**: every board has Input views (data entry) and Display views (display). Multiple Display views allow sensitive data restriction (documented example: a Victims board with a hospital Display view showing victim names and a media Display view hiding them; views assigned to feature groups on a need-to-know basis).
- **Positions**: "Every user is assigned to at least one position… WebEOC Nexus is a role-based system, where each position can have different privileges." Documented example position names: "CMD EOC Director, FIN Staff, or DOT – LOG – Logistics Dept Lead" (ICS-style section prefixes).
- **Feature groups / organizational groups / process permissions**: positions are grouped; feature groups grant access to boards/maps/menus/plug-ins; organizational groups + process permissions "create the structure for process flow" (controller → reviewers → staff pattern documented). "There is no single way of developing the process for information flow in your agency… Process requires structure, and process permissions help to enforce that structure."
- **Master Views**: "Organizations can combine multiple incidents in a common master view… view the data from all sub-incidents together or filter the information to a single incident."
- **Dashboards**: view more than one board and/or map at a time.
- **Maps**: built on Esri ArcGIS; board data on maps; embed map in board; "dynamic, geographically-based common operating picture."
- **Notifications**: scheduled (admin), board-triggered, and user alerts.
- **Reporter**: "preformatted or ad hoc reports based on individual status boards… a comprehensive incident report consisting of individual or all status boards."
- **Audit Log**: automatic event tracking for compliance (logins, deletions, admin actions; date/time, user, position).
- **Simulator**: exercise scenario injects into status boards; MSEL (Master Scenario Events List) management; import an incident into a simulation for exercises.

Standard plug-ins (Tier 1): Checklists (steps with states Complete/Open/Previously Accomplished/Not Applicable), File Library, MapTac (image maps with markers/shapes, shared), Messages (internal + external email), NWS Weather Alerts, Reporter, Search Tool (across all boards), Sessions (who is logged in: username, position, assigned incident), Simulator.

Boards list (Admin Help Center, Tier 1) — the prebuilt board taxonomy:

- Standard: After Action Review, Call Center, Checklist, Crisis Track Integration (view-only tabs: Residential, Public, Commercial, Debris, Protective Measures), Distribution Sites, Event Calendar, Event Reporting, Facility Status, File Library, Incident Action Plan, Incident Creator, Incident Documentation, Press Releases, Requests and Tasks, Schedule, Sign In/Out, Situation Report.
- Premium (subscription): Contact Tracing, COOP Builder, Elections Management, National Qualification System, Personnel Staffing, Plan Builder, Project Management, Requests Inventory and Deployments (RID), Shelters with Registration, Situation Report with Community Lifelines.
- Add-on: Air and Cruise, Asset Tracking with FleetUp, Drone Tracking with AirSight, Facility Status with WeatherOptics, Maintenance Management, PowerOutage.com Integration, SimulationDeck, Wildfire Detection with SenseNet, Workforce Management.
- Industry sets: Airline, Airport, Business Continuity Management Program (Audit and Compliance, BCM, Plan Management, Runbooks, Training and Exercise Tracker), DOT (District Status), Education (Crime Reports, Damage Assessment, Event Reporting, Facility Status, Incident Creator, Requests Tasks, Special Events), Healthcare (AAR, EMTrack Integration, Event Reporting, Facility Status, Incident Creator, Requests Tasks), Healthcare Labs, Nuclear, State and Local (Damage Assessment, Road Closures, Shelters), Utilities (Infrastructure Status, Plan Management, Public Safety Outage, Support Services), Venue Management (Deliveries, Event Operations, Lost and Found).

User view (Tier 1): homepage configured by position; Essential Boards; tabs for open boards/maps/dashboards; Inbox; Quick Actions (open board, pinned notification template, external URL, map); profile menu shows "Your Position" and "The current Incident"; system-wide banner messages.

Product page (Tier 2): multi-channel alerts (text/email/Teams/Slack/voice), low-code/no-code DesignStudio (boards, drag-and-drop forms, public data-capture forms, offline forms), mobile app (field task completion), Juvare Exchange (secure external-partner communication), connectors to CAD/HR/GIS/maintenance, Juvare Intelligence (AI summaries), industries span state & local, federal, utilities, aviation, corporations, education, healthcare, financial, transportation, venues. Vendor claims: deployed in all 50 US states, 4,000+ organizations.

### D4H — Evidence layer A unless noted

Positioning (help center, Tier 1): "real-time incident management software that enables the coordination of an effective response to any situation. Easily create a common operating picture, communicate objectives, and collaborate on a resolution using forms, tasks, logs, maps, and status boards."

Structure (help center, Tier 1):

- **Channel** = the per-event/incident container. "Discover how to manage each event or incident within a channel." Channel lifecycle: start a channel (autofills Start Date; "the clock / timer in your channel is based on this time and date") → shutdown a channel (End Date; clock stops). Channel statuses configurable.
- **Situation module**: "provides the latest updates on an event / incident. Incident Summary, SITREP, and Incident Report are all common alternate names." Built-in fields: Event name, Status, Start Date, End Date, Location (pinned to map; weather recorded there). One situation template per account. Actions: snapshot, display on map, tag in log, print to PDF, share by email/public link, view audit trail.
- **Roles module**: "assign a role to a member during an event / incident." Teams + roles customizable to the org structure (documented example: team "Command Staff" with roles "Incident Commander, Response Manager, Technical Expert"). Roles can be pre-loaded from Collections (even pre-assigned); included in Plays; linked to tasks; org chart creation; tagged in log.
- **Status boards**: "a visualization of information… comprised of a set of rows, much like a spreadsheet, with a configurable form behind each row. You can add as many status boards as you like and there is no limit as to what you can represent in a status board." Rules change row colors (status expressions), update dashboard widgets and module headers. Documented board ideas: Shelters, Risks, Rivers, Road Closures, Bridges, Buildings, Damage Assessments, Schools, Infections, Crew, Passengers, Delays, Incidents. Pre-load via Collections; include in Plays; display on map; tag in log; PDF/spreadsheet export; audit trail.
- **Other channel modules**: Dashboard (overview of ongoing incident data, key metrics, log posts), Personnel (contact details; groups for alerting and incident response; filter/import personnel into a channel), Forms ("incident forms, like ICS forms"), Logs ("record and track important actions, decisions, and communications"), Task Boards ("track assigned tasks, progress, and completion status"), Map, Weather, Library (documents/guidelines), Templates, Plays ("standardized response procedures and quick activation… automatically include modules to your channel when you start it"), Extension Packs (sample template packs, e.g., HAZMAT ERG).
- **Control Room** exists as a navigation area (4 articles; not further fetched).
- **Multi-product family**: Operations Center (Incident Management + Alerting) and Team Manager (Personnel & Training: members, groups, qualifications, roles, calendar, exercises & events, on/off-call planner; Equipment Management: items, categories/kinds, inspections, repairs, supply levels, barcoding; Incident Reporting: reports, timestamps, hazmat, persons/vehicles involved, lost-person behavior). Two-way data sync between products.
- **Shared services**: Cost Recovery & Billing, Reports, Activities, API, Address Book, Health & Safety Reports, Real-Time Collaboration.
- **Alerting**: separate product; "send alerts to personnel during incidents."

Product page (Tier 2): features list (E-Signature Approvals, Document Library, Incident Summary, Pre-Plans, PDF Exports, Incident Audit Trail, Weather Feed, Organizational Charts, Incident Roles, Incident Dashboard, Communication Log, GIS Mapping, Tasks & Checklists, Share by Public Link, Digital Incident Forms, Status Boards). Sectors: EMAs, campus, corporate, healthcare, fire, EMS, SAR, maritime, utilities, aviation, law enforcement, etc. Customer stories: county EMAs (virtual EOC, common operating picture), healthcare all-hazards preparedness, New Zealand emergency management, corporate (Subsea 7, Alton Towers). Competitor comparison pages name: fact24, Everbridge, Mission Manager, Microsoft Teams EOC, emqnet, DisasterLAN, Veoci, WebEOC, Noggin.

### Veoci — Evidence layer B (product pages only; no operational help docs fetched)

Positioning: "Veoci - Virtual Emergency Operations Center Software" (site title). EM solution: "A virtual Emergency Operations Center (EOC) with every tool you need to plan, respond, and recover." "Activate your EOC in one click."

Documented structure (Tier 2):

- Three pillars: **Simplify Planning** (one home for all plans; easier revisions; "all plan edits are timestamped, logged, and available for any review"); **Centralize Your Response** ("one-click activation" launching notifications, checklists, tasks; communications hub — mass notifications + stakeholder collaboration; "Veoci automatically feeds live, incoming data into dashboards to build situational awareness in your EOC"); **Kickstart After-Action Reporting** ("all communications and actions taken are logged"; "immediately access timelines and transcripts after you scale back and close an activation"; corrective actions with automatic reminders to task owners).
- "A Complete EOC Solution" modules: Planning and ICS Forms; Activation & Response; Situational Awareness; After Action Reporting; Resource & Asset Management.
- Adjacent solutions sold alongside: Business Continuity (BIAs, plans, exercises), Crisis Management, Mass Notification, No-code Platform, Veoci VIA (AI).
- Industries: aviation (180+ airports claimed), government, education, healthcare, enterprise & finance, utilities.
- Customer quotes (Tier 2, vendor-published): "track everything from man-hours to resource hours for small-scale activations or on a daily basis" (county EM coordinator); "manage and track critical information during emergency and non-emergency situations… information tracking, mapping and notifications in real time" (town fire marshal).

### Noggin — Evidence layer B (product/solution pages only)

Positioning: "integrated resilience workspace that seamlessly integrates 10 core solutions" (Business Continuity, Operational Resilience, Crisis Communications, Operational Risk Management, Crisis & Incident Management, Third-Party Risk Management, Emergency Management, Safety Management, Investigations & Case Management, Security Management). A Motorola Solutions company.

EM solution page (Tier 2):

- "Noggin Emergency provides all the information and tools needed to manage any incident effectively through its entire lifecycle of mitigation, preparedness, response, and recovery… keeps your whole incident management team, from the emergency manager to untrained field staff, following the same plans, communicating on the same platform, and working from the same operating picture."
- Features: **All Hazards Incident Management** ("best practice all-hazard incident management standards from around the world, including AIIMS, NIMS / ICS, JESIP"); **Situational Awareness** ("common operating picture… via field personnel updates, GIS feeds, data import, email, and social media… comprehensive dashboards… external data feeds"); **Emergency Operation Center Management** ("Stand up EOCs at local, regional, state, and national levels. Wrap up multiple related local incidents into a single regional one, with interfaces fully tailored to each user's role and level"); **Team Activation, Roles, & Collaboration** ("team activation notifications, defined roles and responsibilities, and a centralized hub"); **Mapping** (Esri ArcGIS, WMS, KML, GeoJSON; update feature layers on your own ArcGIS server); **Emergency Messaging** (email, SMS, voice, push, in-app; "automated response links for assistance requests, with workflows that follow up automatically"); **Response Plans & Checklists** ("activate, and automate response plans and checklists so every team follows the same playbook… Each step is assignable and rolls up for easy progress tracking"); **Documentation & Forms** ("custom sitreps, briefings, objectives, incident action plans, or use built-in Incident Command System forms. Automatic field population").
- Four phases: Mitigation & Disaster Planning (GIS hazard analysis, notification workflows); Preparedness ("turning static documents into actionable, digital workflows… built-in exercise management"); Tactical Response ("Noggin serves as your digital Emergency Operations Center… swift team activation, resource assignments, and real-time situational updates"); Recovery ("capturing every action, decision, and communication for comprehensive after-action reviews… drive improvement activities").
- Common uses: public safety & disaster relief (capturing requests for assistance, dispatchers, resources, recovery ops), fire & rescue, retail & corporate security, law enforcement (major events, multi-agency), healthcare (patient tracking in MCI, daily dispatch), aviation SOCs, critical infrastructure, education.
- Platform: no-code customization (workflows, notifications, dashboards, forms, assets; "build your own modules from scratch"); Library ("275+ pre-configured modules", "25,000+ library objects" — vendor numbers); standards alignment (ISO 22320 Emergency Management, ISO 22301, ISO 31000, ISO 22308, ISO 45001, ISO 27001, NIMS, ICS); native iOS/Android apps.

### Crisis Track (Juvare) — Evidence layer A unless noted

Positioning (help center, Tier 1): "A real-time disaster management platform that helps local and state governments track, assess, and manage disaster impacts." Product page (Tier 2): "FEMA-ready damage assessment."

Incident Functions (Tier 1): "Crisis Track allows you to track disaster consequence data for several events through the Incidents feature. Each incident keeps data such as equipment, employees, tasks, and forms separate. Using Crisis Track for incident management helps an organization conduct damage assessments and process FEMA grant applications to get recovery dollars into your community more quickly and efficiently. Crisis Track can also track and manage resources more efficiently for non-emergency incidents like parades or festivals."

- **Tiers**: Damage Assessment (DA), Disaster Management (DM), All-Hazards Emergency Management (EM). "Equipment, Employee, and Resource management features are only available to the Disaster Management (DM) and All-Hazards Emergency Management (EM) tiers, not the Damage Assessment (DA) tier."
- **Roles**: "Incidents can only be created by people with Admin, Admin (No Payroll), or Commander user roles. Only users with an Admin role can edit an incident, deactivate, or delete old incidents."
- **Modules**: Teams, Tasks, Resources, Entries, Personnel Records, Equipment Records, Footprint Map (resource locations, Areas of Concern), Documents. Tasks: assign structures to a task; edit entries for a task.
- **Optional features**: "managing logins and gathering reports from residents and survivors" (public-facing data capture).
- Mobile app exists.
- WebEOC integration: a standard WebEOC "Crisis Track Integration" board shows Crisis Track data (Residential, Public, Commercial, Debris, Protective Measures tabs) in view-only mode.

## Cross-product Comparison

| Dimension | WebEOC Nexus | D4H | Veoci | Noggin | Crisis Track |
|---|---|---|---|---|---|
| Central object | Incident ("fundamental mechanism for organizing emergency response data") | Channel (per event/incident, with clock) | Activation (one-click EOC activation) | Incident (all-hazards, full lifecycle) | Incident (disaster consequence data; also non-emergency events) |
| Shared picture | Boards (Input/Display views) + dashboards + ArcGIS maps | "Common operating picture" via forms, tasks, logs, maps, status boards | Dashboards fed by live data | Common operating picture via dashboards, GIS feeds, field updates | Footprint map + modules |
| Roles | Positions (ICS-style naming documented) + feature groups + process permissions | Incident roles in teams; org chart; pre-loadable | ICS forms; role-based use implied | Team activation, defined roles; "interfaces fully tailored to each user's role and level" | Admin/Commander user roles |
| Tasks/requests | Requests and Tasks board; Incident Action Plan board | Task Boards; Plays | Tasks launched on activation | Response plans & checklists; assignable steps rolling up | Tasks module; assign structures to task |
| Resources | RID board (Requests, Inventory, Deployments); Personnel Staffing | Equipment Management product; personnel sync | Resource & Asset Management module | Resource assignments; asset tracking | Resources module (employee/equipment; tier-gated) |
| Situation reporting | Situation Report board; Reporter builds incident report from boards | Situation module (SITREP; snapshot/PDF/share) | Timelines/transcripts; AAR | Custom sitreps, briefings, IAPs, ICS forms | Forms; FEMA documentation |
| Damage assessment | State & Local board set (Damage Assessment board); Crisis Track integration | Status-board idea (Damage Assessments) | Not surfaced | Not surfaced | Core purpose (FEMA grant applications) |
| Preparedness | COOP Builder, Plan Builder, Event Calendar, Simulator (exercises/MSEL) | Personnel & Training (qualifications, exercises, on/off-call), Equipment inspections, Pre-Plans | Planning module (plan revisions, timestamped) | Mitigation/preparedness phases; exercise management | Not surfaced |
| Notification | Alerts landing page; scheduled + board-triggered notifications; Juvare Alerts add-on | D4H Alerting product | Mass Notification solution | Emergency messaging (email/SMS/voice/push) | Optional resident/survivor reporting |
| Multi-agency | Juvare Exchange; linked systems; Master Views (multi-incident roll-up) | Multi-agency collaboration (customer stories) | Stakeholder collaboration | "Wrap up multiple related local incidents into a single regional one" | Not surfaced |
| Configurability | DesignStudio low-code board builder; lists; menus; industry board sets | Templates, Extension Packs, Plays, Collections | No-code platform | No-code module designers; 275+ module library (vendor number) | Product tiers |
| Audit/record | Audit Log; Reporter | Incident audit trail; logs | Timestamped logs; transcripts | Capture for after-action reviews | Attributed records |
| Exercises | Simulator plug-in (scenario injects, MSEL) | Exercises & Events (Team Manager) | Veoci Exercise Series | Exercise management | Not surfaced |
| Deployment | Cloud SaaS (Nexus); hosted; federal variant (UCP, FedRAMP High claimed) | Cloud SaaS + mobile apps | Cloud SaaS | Cloud SaaS + native mobile | Cloud + mobile app |
| Audience | Government (state/local/federal) + private sector | Government + corporate + volunteer | Government + aviation + education + healthcare + utilities | Corporate + government, international | Local/state government (US) |

### What repeats across all five (candidate common structure)

1. An incident/event container that organizes the response data (all five; WebEOC and Crisis Track state it explicitly).
2. A shared operational picture: status boards / dashboards / maps showing current state to all authorized participants (all five).
3. Tracked coordination work: tasks, requests, resource assignments with owners and status (all five).
4. Roles/positions bound to people during the response (all five).
5. Situation reporting / documentation produced during and after the event (all five).
6. Notification/alerting to participants (all five, in different depths/products).
7. Configurable structure: admins build boards/templates/modules/workflows (all five).
8. Maps/GIS as a primary surface (all five).
9. Audit trail / timestamped record (all five).
10. Preparedness machinery in the same system (plans, rosters, equipment, exercises) — four of five (not Crisis Track's focus).
11. Recovery machinery (damage assessment, cost documentation) — three of five strongly (Crisis Track core; WebEOC board set + integration; D4H cost recovery shared service), Noggin at phase level.

### What differs (implementation, not Type)

- The unit of shared information: WebEOC's "board" (form-backed, input/display views) vs D4H's module set inside a channel vs Veoci's no-code workflows/forms vs Noggin's modules. The *concept* (configurable shared status surface) is common; the *implementation* is vendor-specific.
- Doctrine vocabulary: NIMS/ICS (US products), AIIMS (AU), JESIP (UK) — regional realizations of role-based coordination.
- Packaging: standalone EM (D4H, Crisis Track) vs suite member (Veoci, Noggin) vs platform family (Juvare: WebEOC + eICS + EMResource + EMTrack + Crisis Track + Juvare Alerts + UCP).
- Segment: government EOC vs corporate crisis vs campus/healthcare/aviation/utilities.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

An Emergency Management Platform is a coordination system of record for emergencies and significant events. Four structures; remove any one and the product stops being recognizable as this Type:

1. **The incident/event as the managed unit of coordination** — an emergency, disaster, disruption, or significant planned event held as a record that organizes the response data (participants, status, tasks, resources, documents). All-hazards by design; the same object serves a hurricane, a hazmat spill, a major sporting event, or a parade.
2. **A shared operational picture** — current status/situation information entered once and simultaneously visible to all authorized participants (status boards, dashboards, maps), replacing the paper status boards of physical EOCs.
3. **Managed coordination work** — tasks, requests, and resource assignments held as tracked records with owners and states, moved toward completion during the response.
4. **The operational record** — the event is documented as it happens: time-stamped logs, situation reports, and after-action material that outlive the event and feed reporting, reimbursement, and improvement.

Historical check: pre-digital EOCs ran on exactly these four — the incident file, the wall of paper status boards, the task/resource boards, and the message log/sitrep file. WebEOC's own documentation anchors the lineage ("a board is equal to a large, chronological or categorical paper-based status board that used to dominate EOCs and command centers"). Non-US doctrines (AIIMS, JESIP) and older products fit the same four structures. The definition does not depend on ICS, cloud, mobile, or any specific board implementation.

### L1 — Common Mature Structure (very common in modern products; not definitional)

- Situation reporting (SITREP) as a recurring, shareable product of the record
- Role/position assignment during response (org structure realized in software; ICS-style in US products)
- Resource management: requests, inventory, deployment tracking
- Maps/GIS as a primary surface (board data on maps)
- Dashboards aggregating boards/modules
- Notification/alerting to participants (multi-channel)
- Forms and document libraries (ICS forms, agency forms, pre-plans)
- Configurable structure: low-code/no-code board/template/module builders
- Audit trail / compliance logging
- Mobile field apps
- After-action reporting and corrective-action tracking
- Exercise/training support (simulators, MSEL, drills)

### L2 — Variant / Optional Structure

- Preparedness depth: plan builders (EOP/COOP), personnel qualification & training records, equipment inspection management, on-call planning
- Recovery depth: damage assessment with structure-level data, FEMA/public-assistance grant documentation, cost recovery/billing, payroll
- Mass-notification depth (dedicated products or add-ons)
- Multi-incident roll-up (master views; wrapping local incidents into regional ones)
- Public-facing data capture (public forms; resident/survivor damage reports)
- Integration spine: CAD, HR, GIS, weather, outage/detection feeds
- Deployment: cloud SaaS vs hosted vs federal secure clouds (FedRAMP-class)
- Regional doctrine: NIMS/ICS (US), AIIMS (AU), JESIP (UK)
- Customer segment: government EOC vs corporate crisis vs campus/healthcare/aviation/utilities/venues
- Product tiers (specialist packaging, e.g., damage-assessment-only)

### L3 — Vendor-specific (research notes only)

- WebEOC: "boards" as universal unit; DesignStudio; Juvare Exchange; JAI AI assistant; Simulator/MSEL; premium/add-on/industry board licensing; position+incident login selection; Juvare product family (eICS, EMResource, EMTrack, CORES, UCP, Juvare Alerts).
- D4H: channel/plays/collections/extension-packs model; Team Manager vs Operations Center split; two-way product sync; K9 & handlers module.
- Veoci: one-click activation; rooms/forms/workflows no-code model; Veoci VIA AI; exercise series.
- Noggin: 10-solution resilience workspace; 275+ module library (vendor number); ISO-standards framing; Motorola Solutions ownership.
- Crisis Track: DA/DM/EM tiers; footprint map with Areas of Concern; structures assigned to tasks; FEMA grant processing focus.

## Vendor-specific Findings

- WebEOC's position-based login (user must select position + incident) is a product design, not a Type requirement — D4H users join channels without position selection.
- D4H's channel clock (start/shutdown dates driving a timer) is product-specific; WebEOC incidents do not document an equivalent timer in fetched pages.
- Crisis Track's tier gating (resource management absent from DA tier) is product packaging.
- Noggin's "wrap up multiple related local incidents into a single regional one" is the clearest vendor articulation of multi-incident roll-up; WebEOC's Master Views is the operational equivalent. Treat roll-up as common-not-core (2 of 5 documented).
- Veoci's "one-click activation" phrasing is marketing; the underlying concept (activation launching notifications/checklists/tasks) is common.

## Boundary Findings

- **vs Computer-aided Dispatch / CAD**: CAD is per-incident, real-time, unit-level dispatch of status-tracked response units (per the CAD research pass). The EM platform is event-level coordination over hours-to-months: situation, resources, tasks, reporting across agencies and an EOC. The CAD pass already records the seam ("Large events stress CAD toward it, but the unit of work differs"). WebEOC lists CAD among its integration connectors — evidence that vendors treat them as distinct systems that interconnect.
- **vs Public Alert & Warning System**: PAWS is outbound mass alerting to populations. EM platforms notify *participants* (staff, responders, partners); public mass alerting appears as a separate product (Juvare Alerts, D4H Alerting is personnel alerting, Veoci Mass Notification as a separate solution). Boundary: audience (public vs response organization) and direction (warning vs coordination).
- **vs Incident Management (IT)**: different object world (tech incidents, on-call, service context). Name collision only.
- **vs Business Continuity Management Platform**: BC is plan-centric continuity of organizational functions (BIA, plans, exercises); EM is incident-centric coordination. Overlap is real and vendor-driven: WebEOC markets itself as "business continuity software" for the private sector; Veoci and Noggin sell BC solutions beside EM; WebEOC ships a COOP Builder board and a BCM industry board set. The seam: BC owns the plan-of-record for continuing functions; EM owns the event-of-record for coordinating response. Flag for joint review when Business Continuity Management Platform is processed.
- **vs Fire Department Records / EMS Operations / Police RMS**: agency-specific operations and records; the EM platform coordinates across agencies rather than running one agency's business.
- **vs Emergency Department Information System**: hospital clinical operations; no relationship beyond shared vocabulary ("emergency").
- **vs 311 / Citizen Service Request Platform**: routine service requests vs emergency coordination; Crisis Track's "non-emergency incidents like parades or festivals" shows the EM incident object can absorb event coordination, but 311 is a citizen-request workflow, not a response coordination system.
- **vs Government GIS**: GIS is a component surface (maps) inside EM platforms, built on Esri in the sampled products; Government GIS is a data/analysis system of record.
- **Corporate crisis management**: not a separate directory leaf; the corporate pole (Noggin, D4H crisis management, WebEOC private sector) is a segment variant of this Type.

## Uncertainties

- Veoci and Noggin were documented from official product/solution pages only; their operational help documentation was not fetched (Veoci help center not located in this pass; Noggin support pages not fetched). Claims about their internal object models (rooms, forms, module internals) are therefore not made; their *market-facing* structures are documented.
- Exact permission models beyond the documented examples (WebEOC view-level permissions; Crisis Track role gating) vary and were not exhaustively researched; no precise permission claims are made in the final document.
- Numeric claims (Noggin's 275+ modules, WebEOC's 50-state deployment, Veoci's 180+ airports) are vendor marketing figures, recorded here but not promoted to the final document.
- The relative market position of products not directly researched (Everbridge, OnSolve, DLAN, Mission Manager) is unknown from this pass; they are named only as boundary references.
- Whether "Emergency Management Platform" should also absorb the corporate "Critical Event Management" (CEM) label as an alias: the sampled evidence suggests CEM is a marketing label for the same structure in corporate clothing; recorded as a taxonomy observation, not resolved here.

## Final Synthesis

The Emergency Management Platform is the coordination system of record for emergencies and significant events. Its defining core is four structures: the incident/event as the managed unit of coordination; the shared operational picture that replaces the paper status boards of the physical EOC; tracked coordination work (tasks, requests, resources); and the time-anchored operational record that feeds situation reports and after-action documentation. Around this core, mature products add role/position machinery, resource management, maps, dashboards, notification, configurable board/module builders, mobile apps, exercises, and — with varying depth — preparedness (plans, rosters, equipment) and recovery (damage assessment, cost documentation) machinery. The Type is government-anchored (EOC, all-hazards doctrine) but extends to corporate, campus, healthcare, aviation, and utility deployments under the same structure. Doctrine alignment (NIMS/ICS, AIIMS, JESIP) is regional realization, not definition. The sharpest boundaries: CAD (unit dispatch vs event coordination), Public Alert & Warning (public warning vs participant coordination), and Business Continuity Management (plan-of-record vs event-of-record — flagged for joint review).
