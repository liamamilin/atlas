# Computer-aided Dispatch / CAD

## Overview

A **Computer-aided Dispatch (CAD)** system is the real-time operational application used by emergency communication centers and other dispatch operations to receive requests for service, turn them into tracked incidents, and assign status-tracked response units to those incidents — all maintained as a live operational picture that shows, at any moment, what is happening and who is responding.

The defining structure is small:

```text
Service request (call for service)
└── Incident (tracked unit of response work: location, nature, priority, timeline)
    └── Assignment (unit(s) bound to the incident — recommended by the system, governed by a person)
        └── Response unit with real-time status
            └── Live operational picture (status board + map)
```

Everything else commonly associated with modern dispatch — 911/NG911 call integration, GIS mapping, vehicle location tracking, mobile field apps, multi-agency operation, records hand-off, cloud deployment — is widespread in current products but is not what makes a system a CAD. Older text-terminal dispatch systems without maps or automatic location, non-US emergency centers, and non-emergency dispatch operations all fit the same definition.

When the real-time dispatch of status-tracked units disappears, the product stops being a CAD: what remains is a call log or a records system. When the emergency semantics disappear and commercial settlement takes over, the product becomes a different type (taxi, towing, freight dispatch).

## Users & Context

Primary users sit in a communications center and work the same live picture from different roles:

- **Call-taker (telecommunicator)** — receives the request for service, verifies location and nature, creates or updates the incident. In emergency centers the request arrives from the emergency line already carrying caller number and location data; the call-taker confirms and classifies it.
- **Dispatcher** — watches the incident queue and the unit status board, evaluates system recommendations, and commits assignments; then tracks the response as units report their status back.
- **Shift supervisor** — monitors overall workload and coverage, handles reassignments, escalations, and incidents that outgrow their initial handling.

Field responders are secondary but essential users: through a mobile client they receive assignments, report status, exchange messages with the center, and see location and premise information. Administrators configure the system (status vocabularies, response rules, priorities, jurisdictions, users).

The work context is distinctive: operations run 24/7, every action is time-stamped, seconds matter, and the system is expected to keep working under stress — which is why availability and degraded-mode operation are first-class design concerns rather than afterthoughts. The same core also serves non-emergency dispatch contexts: ambulance transport operations, campus and port security, and other organizations that run a dispatch desk.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a CAD:

- **Incident** — a request for service held as a discrete, tracked record: where it is, what it is, how urgent it is, who is assigned, what has happened so far. The incident is the unit of work the whole system exists to move from intake to resolution. Multiple requests about the same event are recognized and merged into one incident.
- **Response unit** — a dispatchable resource (a patrol car, an apparatus, an ambulance crew, a responder) with a capability profile and a jurisdiction, whose current status and location the system maintains in real time. A unit is always in exactly one status at a time; the status vocabulary is configured per operation.
- **Assignment** — the binding of unit(s) to an incident: the dispatch act. The system recommends; a person (or a governed automation with explicit confirmation points) commits. The assignment is transmitted to the unit and starts the response.
- **Live operational picture** — incidents and unit states presented as current state, typically as a status board and a map side by side. The picture is the product's core output: everyone in the center works from the same real-time view, and it survives shift changes.

The real-time posture is itself definitional: a CAD is judged by how faithfully it reflects *now*. Every state change is recorded as it happens, with time stamps, forming the incident's timeline.

### Standard Capabilities of Mature Products

These are not required to recognize the type, but mature products carry most of them:

- **Emergency-line integration** — the request stream arrives from emergency call handling with caller number and location already attached; current-generation products also receive texts, images, and structured incident data from IP-based emergency networks. Call handling and CAD remain distinct systems: the call belongs to one, the incident and the units to the other.
- **GIS map as a primary surface** — addresses are geocoded onto the map; incidents, units, and jurisdiction boundaries live there. Map quality directly affects dispatch quality, and vendors treat mapping accuracy as a headline capability.
- **Priority and response logic** — the incident's severity drives its queue position and the response it receives. Operations encode their response policy as configurable rules (which units, how many, from where, for which incident types), and the system recommends or executes accordingly.
- **Unit recommendation** — the system ranks available units by proximity, capability, and availability; some products add live traffic and road-closure inputs, or model the coverage impact of rule changes before they take effect.
- **Automatic location for units** — vehicle location feeds keep the map and the recommendations current without manual reporting.
- **Mobile field client** — the responder's window into the incident: assignments in, status out, messaging, navigation, and location/premise context. It closes the loop between center and field and reduces voice traffic.
- **Incident timeline and audit trail** — every event, status change, and action is time-stamped and attributable; the record is both an operational tool and the raw material for downstream records.
- **Multi-agency and cross-jurisdiction operation** — consolidated centers serve many agencies on one picture; interoperability gateways connect separate CAD systems so neighboring jurisdictions can share incidents when response crosses boundaries.
- **Downstream records hand-off** — incident data flows automatically to records management, patient-care documentation, or billing systems, eliminating duplicate entry.
- **Reporting and analytics** — response times, unit utilization, incident trends; the same data that ran the response now measures it.
- **Resilience machinery** — redundancy, failover, and the ability to keep dispatching from alternate locations; cloud-delivered products make availability during disasters a central promise.

### One Structure, Many Implementations

The core model is conceptual. Realizations vary:

```text
Concept:  Service-request intake
Realized as:  emergency-line handoff, non-emergency lines, web/self-service
              requests, transport request queues

Concept:  Unit status
Realized as:  agency-configured status codes, automatic location updates,
              mobile-app updates, radio-reported changes entered by the dispatcher

Concept:  Recommendation
Realized as:  proximity ranking, rule-driven response plans, coverage
              impact modeling
```

A reader who has only seen a modern map-centric cloud CAD should still be able to recognize an older, plainer dispatch system — or a non-emergency one — from the core model alone.

## How It Works

### The response loop

The defining workflow is a loop from request to resolution:

```text
Request arrives (with caller location where available)
→ call-taker verifies location, classifies nature, sets priority
→ incident created (duplicates merged)
→ system recommends unit(s) per response rules
→ dispatcher confirms / changes / commits the assignment
→ assignment transmitted to the unit(s)
→ units update status as the response proceeds
→ dispatcher tracks, escalates, adds or reassigns units as needed
→ response completes, units clear and return to available
→ incident closed; data flows to records
```

Two properties make this loop distinctive:

- **The incident is the thread.** Everything that happens — every call, unit, status change, message, and time stamp — attaches to one incident record, so the response has a single, inspectable history from the first ring to closure.
- **Status is the currency.** The dispatcher's board is a live inventory of who is available, who is committed, and who is out of service. Assignments change statuses; statuses drive recommendations; clearing restores availability. The whole system breathes through status changes.

### The configuration loop

Alongside the live loop runs a slower one: administrators encode the operation's policy into the system — status vocabularies, incident types and priorities, response rules mapping incident types to required units, jurisdiction and agency boundaries, user roles. Because response policy differs by agency and is subject to negotiation and regulation, configurability is a core product dimension, and some products let supervisors preview how a rule change would alter staffing and coverage before it goes live.

### Exceptions that shape the design

- **Duplicate reports** — several callers report the same event; the system must recognize and merge them into one incident without losing any caller information.
- **Escalation** — an incident grows after dispatch (a minor collision becomes a multi-casualty event); additional units are added, priorities raised, and the timeline records the escalation.
- **Cross-boundary response** — the nearest unit belongs to a neighboring jurisdiction; mutual-aid arrangements and CAD-to-CAD links let the incident cross the boundary.
- **Unit unavailability** — units go out of service unexpectedly; recommendations must respect real availability, not roster plans.
- **Degraded operation** — when networks or sites fail, dispatch must continue; the system's resilience posture (redundancy, failover, remote operation) exists for this case.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Call-taking surface

The intake desk for requests.

- incoming request with caller number and location where available, location validation, incident-type and priority selection
- primary actions: create incident, update an existing incident, merge duplicates, transfer the call

### Dispatch console

The dispatcher's working surface, typically combining several panels.

- incident queue ordered by priority and age; unit status board; recommendation display; communication controls
- primary actions: commit or change an assignment, update unit status, add units to an incident, escalate, broadcast messages

### Map

The spatial surface shared by every role.

- incidents, units, jurisdiction boundaries, and points of interest on a GIS basemap
- primary actions: locate, route, inspect an incident or unit, measure coverage

### Mobile field client

The responder's surface in the vehicle or on foot.

- current assignment with location and premise context, status controls, messaging, navigation
- primary actions: acknowledge assignment, change status, exchange messages, view incident details

### Supervisor surface

Oversight of the center itself.

- live workload and coverage view, staffing state, incident list across dispatcher positions
- primary actions: reassign, escalate, intervene in an incident, adjust unit states

### Configuration / administration

The policy surface.

- status vocabularies, incident types and priorities, response rules, jurisdiction and agency data, users and roles
- primary actions: configure, preview impact, publish

### Reporting / analytics

The retrospective surface.

- response times, unit utilization, incident trends, exportable reports

## Important Rules / Behaviors

- **Human governance of the dispatch act.** Recommendations are advisory; a person commits the assignment. Products that push further into automated response execution pair it with explicit confirmation points rather than removing the person — the dispatch act remains human-governed across the type.
- **One status at a time.** A unit occupies exactly one status; assignments and clearances move it through the cycle. Exact status labels are configured per operation and vary widely — the conceptual cycle (available → committed → responding → on scene → clearing → available) is canonical, the vocabulary is not.
- **Priority governs order.** The incident queue is ordered by severity and time; priority drives both what the dispatcher sees first and what the response rules prescribe.
- **Jurisdiction bounds authority.** What a dispatcher can see and dispatch is bounded by agency and jurisdiction configuration; crossing boundaries requires mutual-aid arrangements or interoperability links.
- **Everything is recorded.** The public-safety context makes the audit trail non-negotiable: every action is time-stamped and attributable, and the incident record outlives the response.
- **The picture must be current.** Stale status is a hazard; the system is designed so that state changes propagate immediately to every position, and the shared live picture is what makes a consolidated multi-agency center possible.
- **Availability is a feature.** Dispatch cannot pause; products are engineered for redundancy, failover, and continued operation under degraded conditions.

## Variants

Common forms of the type:

- **Discipline scope** — law-enforcement-only, fire-only, EMS-only, or consolidated multi-discipline centers handling all disciplines on one picture. Consolidation is the current direction, but single-discipline deployments remain common.
- **Emergency vs non-emergency workload** — some operations run dedicated queues for non-emergency service requests or scheduled transport alongside emergency response; the same core model covers both, with the emergency queue carrying the priority machinery.
- **Deployment** — on-premises installations remain widespread in the installed base; cloud-native delivery is the current market direction, enabling remote dispatch and vendor-managed resilience.
- **Scale** — single-agency centers versus regional consolidated centers serving dozens of agencies on one system.
- **Adjacent-domain deployments** — campus, port and transportation, private ambulance and other non-governmental dispatch operations run the same core under different governance.
- **Automation depth** — from dispatcher-driven systems with simple proximity ranking to rule-driven products that execute response plans automatically with human checkpoints.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Police Records Management System | downstream | RMS owns the post-incident case record (investigation, arrests, evidence); CAD owns the live incident and the units. The seam is the automatic hand-off of closed incident data. |
| Emergency Management Platform | adjacent, confusable at scale | Emergency management coordinates multi-event, multi-agency, long-duration disaster response at an operations-center level; CAD is per-incident, real-time, unit-level dispatch. Large events stress CAD toward it, but the unit of work differs. |
| Fire Department Records / Operations System | downstream | Fire records systems consume CAD output; they do not dispatch units. |
| EMS Operations Platform | downstream | Patient-care documentation and billing consume dispatch data; the dispatch itself lives in the CAD. |
| Taxi Dispatch Platform | structural sibling, commercial | Same mechanics (jobs, units, status, assignment, map) but commercial ride orders with fare settlement and no emergency priority or public-safety semantics. |
| Towing Dispatch Platform | structural sibling, commercial | Same distinction as taxi dispatch, for towing service orders. |
| Dispatch Management (freight) | structural sibling, logistics | Load assignment over commercial logistics; no incident, priority, or response semantics. |
| On-call Management | adjacent | Schedules who is available; does not run incidents or dispatch units. |
| Contact Center Routing Platform | superficial resemblance | Routes customer contacts to agents; no field units, no incidents, no status cycle. |
| Public Alert & Warning System | adjacent | Outbound mass alerting to populations; not incident-level unit dispatch. |
| Mechanical CAD | name collision only | Engineering design software; shares only the acronym. |

The sharpest boundary is upstream: **emergency call handling owns the call; CAD owns the incident and the units.** Vendors sell these as distinct products that integrate at the call-to-incident handoff, and confusing the two is the most common category error around this type.

## Representative Products

- Mark43 CAD — cloud-native multi-discipline CAD (law, fire, EMS)
- Motorola Solutions CAD family (PremierOne, Flex, CommandCentral CAD) — enterprise incumbent, PSAP-centric
- ZOLL Dispatch — EMS/ambulance-specialist CAD
- CentralSquare Public Safety Suite CAD — public-sector suite with adjacent NG911 call handling and CAD-to-CAD interoperability

Other major vendors exist in this market (including Hexagon and Tyler Technologies) but could not be documented from official sources in this research pass; no claims are made about them.

## Sources

Research date: **2026-09-07**

- Mark43 — CAD product page: https://mark43.com/platform/cad/ ; corporate site: https://mark43.com/
- Motorola Solutions — Voice & computer-aided dispatch: https://www.motorolasolutions.com/en_us/products/command-center-software/public-safety-software/voice-and-computer-aided-dispatch.html ; NG911 software: https://www.rapiddeploy.com/ (redirects to Motorola NG911 page)
- ZOLL Data Systems — ZOLL Dispatch: https://www.zolldata.com/ems-fire/dispatch ; corporate site: https://www.zolldata.com/
- CentralSquare — Public Safety & Justice solutions: https://www.centralsquare.com/solutions/public-safety-software ; corporate site: https://www.centralsquare.com/

> Sourcing limitation: vendor help centers and detailed product manuals were not reachable from the research environment on 2026-09-07 (JavaScript-gated help center, binary PDFs, blocked or timed-out vendor sites for two additional major vendors). All claims above are calibrated to the reachable official product pages: conceptual structures are stated with confidence, while exact status vocabularies, numeric limits, timing windows, and uptime figures are deliberately not asserted. Detailed evidence, product-by-product observations, and the cross-product comparison are recorded in the paired Research Notes.
