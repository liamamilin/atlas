# 311 / Citizen Service Request Platform

## Overview

A **311 / Citizen Service Request Platform** is a government-operated system that receives non-emergency service requests from residents, categorizes and locates each request against a government-defined service catalog, routes it to the government unit responsible for fulfilling it, tracks it through a lifecycle to resolution, and reports status back to the person who made the request.

The name comes from the North American "311" non-emergency phone number, but the defining structure is not the phone number or the call center. The same Type appears worldwide under different names and channels: city reporting websites, mobile reporting apps, council issue reporters, and regional smart-city programs. What makes them all the same Type is the request record itself: a resident describes a civic problem or service need (a pothole, a missed trash collection, a broken streetlight, graffiti), the system determines what kind of request it is and where it is, sends it to whoever in government is responsible, and keeps both the government and the resident informed until it is resolved.

The boundary is equally clear: this is the **non-emergency** side of citizen contact. Life-threatening situations belong to emergency dispatch systems, and the Type is defined against them — some implementations screen for emergency situations at intake and divert them to emergency numbers instead of accepting the request.

## Users & Context

**Primary users:**

- **Residents** — report a problem or service need, provide location and details (often a photo), and follow the status of their request. They are usually not account-heavy users; many submit once and return only to check status.
- **311 / contact center agents** — take requests by phone or in person and enter them into the system on the resident's behalf; answer status questions; handle requests from people who cannot use digital channels.
- **Department staff** — receive routed requests in their department's queue, triage them, set priority, correct mistakes (wrong category, wrong location), and record progress and outcomes.

**Secondary users:**

- **Field crews / inspectors** — consume the work that results from requests (usually through an integrated work order system, sometimes directly in the platform).
- **Administrators** — configure the service catalog, routing destinations, response templates, staff roles, and public-facing settings.
- **Management / leadership** — consume volume, timeliness, and workload reporting; in transparency-oriented jurisdictions, the public itself is also a reader of request data.

The operating context is a city, county, or similar local government running a non-emergency contact program. Volume is high and individual requests are short-lived — the opposite profile of benefits or licensing casework.

## Core Model

### The Defining Core

```text
Resident (or agent acting on their behalf)
└── Service request — a non-emergency civic need or issue
    └── Categorized against the government's service catalog
    └── Located (address / geographic position)
        └── Routed to the responsible government unit
            └── Tracked lifecycle → resolution
                └── Status feedback to the requester
```

Six structures. Remove any one and the product stops being this Type:

- **Service request record** — the central object. One record = one reported issue or service need, with a description, submission time, requester contact, usually photos, and a unique tracking identifier the requester can reference.
- **Service catalog** — the government's own list of request types ("pothole", "missed collection", "streetlight out", "graffiti", "abandoned vehicle"). The catalog is jurisdiction-specific: each type carries its description, the extra questions it asks, and — critically — where requests of that type go. Requesters choose from this catalog; they do not invent free-form tickets.
- **Location** — a service request is tied to a place: an address, a map point, or both. Location is what allows the system to know which jurisdiction, which department, and often which physical asset (a specific streetlight, a specific catch basin) the request concerns. Requests without a location generally cannot be routed at all.
- **Responsible unit (routing)** — every request is directed to the agency, department, or crew that fulfills it. Routing is computed from the request's category and location — the two facts the catalog and the map jointly provide. When a request is re-categorized or moved, it may be re-routed to a different authority.
- **Tracked lifecycle** — the request moves through states from submission to resolution. The most minimal implementations use just two states beyond creation — open and closed — while richer implementations add states such as in progress or no further action. Closure carries a reason or note, and "duplicate of an existing request" is a normal, expected outcome.
- **Status feedback to the requester** — the requester can see where their request stands: a tracking identifier, status notifications, visible updates, and often an expected-resolution indication derived from service-level commitments for that request type. This is what distinguishes the Type from internal work management: the citizen is a participant in the lifecycle, not just a source of inbound calls.

### Standard Capabilities

Mature products commonly add the following around the core. They make the Type practical at municipal scale but do not define it:

- **Multi-channel intake** — a branded web portal and/or mobile app for residents; agent-created requests for phone and in-person contact; in some products SMS, chatbots, or social channels as additional inlets.
- **Requester contact and notifications** — confirmation that the request was accepted, and notifications when its status changes.
- **Photo/media attachments** — residents photograph the issue; staff may also attach photos (for example, after inspection).
- **Duplicate handling** — detecting that the same issue at the same place is already reported, pointing the new reporter to the existing request, or closing a new request as a duplicate.
- **Service-level expectations** — per-request-type response or resolution targets surfaced to the requester as an expected date.
- **Staff console** — queues filtered by department, category, or state; search; assignment to specific staff; priority setting; template responses for common replies.
- **Internal vs public communication** — internal notes for staff coordination, separate from updates visible to the requester and (in some jurisdictions) the public.
- **Reporting** — request volume by type, resolution timelines, department workload, and geographic concentration; used for staffing and service decisions.
- **Fulfillment integration** — handoff of approved requests to work order or asset management systems so field crews execute the work, with completion flowing back to update the request.
- **Moderation and privacy protection** — removing or redacting personal information and inappropriate content from publicly visible material.

### Concept vs Implementation

The core is deliberately written in conceptual terms; products realize each concept differently:

```text
Concept:            Service catalog
Implementations:    curated request-type list with codes and per-type forms;
                    category trees with per-category routing destinations;
                    low-code designed services/forms

Concept:            Location
Implementations:    map pin + address lookup; address-master IDs;
                    administrative-boundary lookup that resolves the responsible body

Concept:            Routing
Implementations:    category + boundary → department inbox or system;
                    automatic assignment by type and geographic area;
                    workflow-based task assignment

Concept:            Status feedback
Implementations:    tracking number + status page; email notifications;
                    public updates on the request; open-data feeds
```

## How It Works

### The main flow: from report to resolution

```text
Resident contacts the government (web portal, app, phone, in person)
→ request is created: type chosen from the service catalog,
  location pinned or captured, description and photos attached,
  requester contact recorded
→ system validates the request (location resolves to a jurisdiction/asset;
  required questions answered)
→ request is routed to the responsible department or unit
→ staff triage: verify, correct category/location if needed,
  set priority, assign
→ work is performed (directly, or via a handoff to a work order system)
→ staff record progress and outcome as status updates
→ request is closed with a resolution note
→ requester is notified / can see the final status
```

Two facts drive everything between intake and fulfillment: **what** the request is (catalog category) and **where** it is (location). Together they determine the responsible unit. This is why category and location errors are the most common things staff correct — and why correcting them can re-route a request to a different authority, with the request's open status preserved for the requester.

### The agent flow: requests created on behalf of residents

Phone and in-person contact remains a first-class channel. An agent taking a call creates the same request record the resident would have created — category, location, description, contact — and submits it into the same lifecycle. The request is attributed to the resident (whose details staff can see internally) while the public-facing attribution may be the government itself. Agents also answer "where is my request?" questions by looking the request up by tracking identifier or requester.

### The duplicate path

Because many residents report the same visible problem, intake in some products checks whether a similar request already exists for that category and location. If so, the new reporter is pointed to the existing request — in some products, invited to subscribe to it for updates — instead of creating a competing record. Requests that slip through may later be closed as duplicates with a note linking them to the original.

### The fulfillment handoff

For physical work (repairs, collections, cleanups), the request typically becomes an assignment in a work order or asset management system. The 311 platform's own job ends at handoff and resumes at completion: when the field system reports the work done, the request's status updates and the requester is informed. Products differ in whether execution is integrated, bundled in the same suite, or handled by email-style dispatch — but the request record remains the citizen-facing thread throughout.

### The measurement loop

Closed requests accumulate into the system's reporting: volumes by type and area, resolution times against service-level targets, workload per department. Jurisdictions use this to staff departments, adjust the catalog, and publish performance. Transparency-oriented jurisdictions go further and publish request data itself.

## Interfaces

### Resident portal / mobile app

The citizen-facing intake and tracking surface.

- catalog of request types with guidance (photos, descriptions of what belongs in each type)
- map/address location capture; photo upload; per-type questions
- "my requests" view: tracking identifiers, current status, updates, expected resolution
- primary actions: submit a request, track status, add an update, subscribe to notifications

### Public request map (transparency variant)

In transparency-oriented deployments, a public map of all reported issues.

- pins or clusters of requests by category and state
- anyone can view reports, add updates, or subscribe to area alerts
- primary actions: explore, subscribe, avoid duplicating an existing report

### Agent / contact center console

The staff surface for phone and in-person intake and inquiry handling.

- search by tracking identifier, requester, address, or content
- create a request on behalf of a caller (with internal attribution of the real requester)
- status lookup for "where is my request?" calls
- template responses for common replies

### Department queue / request workspace

The operational surface for the staff who fulfill requests.

- filtered queues (department, category, state, priority)
- request detail: description, photos, location map, requester contact, history
- primary actions: triage, correct category/location, set priority, assign, record updates, close with resolution note

### Administration / configuration

The setup surface that defines how the platform behaves.

- service catalog management: request types, descriptions, per-type questions, routing destinations
- routing rules and jurisdiction/boundary configuration
- staff roles and permissions; response templates; public-facing notices
- reporting dashboards

## Important Rules / Behaviors

### Routing is computed, not chosen

The responsible unit is derived from category + location. Staff normally cannot "pick" an arbitrary destination without changing the request's category or location — and changing those re-computes the route, possibly sending the request to a different authority while keeping it open for the requester.

### Location is load-bearing

A request without a usable location generally cannot be routed or fulfilled. Intake therefore pushes for a precise point or address, and staff can correct the pin (including setting it to their current position during field inspection).

### Non-emergency boundary is enforced in-product

Emergency situations are out of scope. Some implementations screen for them at intake — for example, a per-category question whose answer stops submission and directs the person to an emergency number.

### Status is requester-visible by design

The requester can follow their request from submission to closure. What the wider public can see varies by jurisdiction: some expose all requests on a public map; others restrict visibility to the requester. Internal notes are not requester-visible in either model.

### Duplicates are a normal outcome

Because the same physical problem generates many reports, closing a request as a duplicate of another (or merging attention into the original) is standard behavior, not an error state.

### Staff authority is scoped

Staff typically act only on requests belonging to their own department, body, or assigned categories; administrators control the catalog, routing, templates, and accounts. Moderation powers (editing or hiding public content, redacting photos) are permission-gated because publicly visible content carries legal and privacy exposure.

### Requests carry expectations

Service-level targets per request type are commonly surfaced as an expected resolution indication. Missing them is measurable — which is precisely why jurisdictions adopt these platforms.

## Variants

- **Call-center-centric 311 program** — a branded non-emergency number with staffed agents as the primary channel; the platform is the system of record behind the program (common in North American large cities).
- **Web/app-first reporting** — digital self-service as the primary channel with agents as fallback; typical of smaller jurisdictions and of the European council-reporting pattern.
- **Civic-suite module** — service requests embedded in a broader government platform alongside permitting, licensing, and asset management, sharing one resident account and one record system.
- **Open-transparency deployment** — all requests publicly mapped and subscribable; open-data feeds and open APIs for third-party apps.
- **Regional / multi-jurisdiction systems** — one platform serving several municipalities, with routing resolving which jurisdiction and which body is responsible at a given point.
- **Standalone citizen-reporting product** — lightweight, quickly deployed reporting sites, sometimes run by civic organizations rather than the government itself, forwarding reports to authorities.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Government Service Portal | access/transaction surface for many services (payments, permits, information); may embed request forms but does not own the fulfillment lifecycle |
| Public Sector Case Management | long-lived, caseworker-owned, eligibility-driven cases (benefits, social services) rather than high-volume short-cycle located requests |
| Help Desk / Ticketing System | same record→route→work→close shape, but private-sector catalog, customer framing, and no jurisdiction/location routing or public accountability |
| Code Enforcement Management | departmental violation workflow (inspection → notice → citation); a 311 request may spawn such a case but is not one |
| Public Works Management / Work Order Systems | field execution of work; the 311 platform hands requests off and tracks citizen-facing status, it does not schedule crews or manage assets |
| Computer-aided Dispatch / CAD | emergency response dispatch at seconds scale; the 311 platform explicitly diverts emergencies away |
| Constituent Relationship Management | centers the ongoing relationship and interaction history with a person; the 311 platform centers the request lifecycle (some vendors market the two together) |
| Government Contact Center | channel and agent infrastructure; the 311 platform is the request management system operating behind it |
| Civic Engagement / Petition Platform | collects opinions, ideas, and petitions without a fulfillment obligation or status lifecycle |

The closest neighbor is the work order system: the two meet at the fulfillment handoff, and some suites merge them. The structural test is the object and its audience — the 311 platform's object is a citizen-visible request whose lifecycle exists to keep the requester informed; the work order's object is internal work whose lifecycle exists to organize crews.

## Representative Products

- **Accela Service Request Management** — service requests as part of an end-to-end civic platform (permitting, licensing, asset management) for larger cities and counties
- **Granicus Service Request Management (govService)** — forms-and-workflow-centered request management with resident portal, staff portal, and contact-center hub for local government
- **FixMyStreet / FixMyStreet Pro (mySociety)** — open-source, citizen-first public issue reporting; UK-origin pattern deployed worldwide under many names
- **Open311 (GeoReport v2)** — not a product but the vendor-neutral open standard for civic issue reporting, implemented by many platforms and written into major city procurements; useful as a cross-vendor picture of the core data model

Other well-known products in this market (for example SeeClickFix, Tyler's 311 offerings, Cityworks) could not be directly documented from official sources during research; see Sources.

## Sources

Research date: **2026-09-06**

- Open311 — https://www.open311.org/ and GeoReport v2 specification — http://wiki.open311.org/GeoReport_v2
- Accela — Service Request Management — https://www.accela.com/solutions/service-request/ (plus platform overview at https://www.accela.com/)
- Granicus — Service Request Management (govService) — https://granicus.com/product/service-request-management-govservice/
- FixMyStreet Platform (mySociety) — https://www.fixmystreet.org.uk/ , including "How it works", the glossary, and the staff-user documentation

> Sourcing limitation: official pages for several additional market products (Tyler Technologies, Cityworks/Trimble, SeeClickFix, Salesforce public-sector 311) were not reachable from the research environment on 2026-09-06. Claims in this document are therefore grounded in the four sources above; product-specific details from unreachable vendors were deliberately not reconstructed. Precise numeric limits and defaults observed in single products were kept out of this document and remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the regional/historical breadth check are recorded in the paired Research Notes.
