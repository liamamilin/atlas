# Public Alert & Warning System

## Overview

A **Public Alert & Warning System** is the system public authorities use to warn the population at large about imminent threats: authorized officials compose a structured alert — what is happening, where, how severe, what to do, until when — and the system pushes that alert to everyone in the affected area through public-facing channels, without requiring anyone to have subscribed.

Its defining structure is small:

```text
Authorized Alerting Authority
└── Alert record (event · area · urgency/severity · instructions · validity · issuer)
    └── Public area-based dissemination
        └── Everyone in the affected area — residents, visitors, transients — no subscription required
```

Three properties held together make the Type. Remove the alert record and only channels remain; remove authorized origination and any organization could broadcast warnings; remove the public area-based audience and the product becomes an opt-in notification tool.

The Type spans two positions in the warning chain: national aggregation-and-dissemination infrastructure operated by governments, and the origination software local authorities use to compose and issue alerts — including, in some deployments, both in one platform.

## Users & Context

The operating user is a public-safety official acting under a public-warning mandate:

- **Emergency management agencies** (national, state/provincial, county, municipal) issuing all-hazard warnings — severe weather, flooding, wildfire, hazardous materials.
- **Specialized authorities** issuing hazard-specific warnings — meteorological services, flood agencies, geological surveys.
- **Police, fire, and emergency services** issuing public-safety threats, evacuation orders, and missing-person alerts.
- **Local government** issuing localized public-safety notices (cordons, utility failures, public health measures).

The served population is the public at large in the affected area — explicitly including people with no relationship to the issuing authority: tourists, commuters, travelers passing through. This is the structural difference from every subscription-based notification product: the system must reach people who never signed up and cannot be addressed by name.

Typical context is time-critical operations: an emergency operations center or duty officer desk, often outside business hours, where minutes matter and errors are public. The system is exercised regularly through scheduled tests so that both operators and the public stay familiar with it.

## Core Model

### The Defining Core

**The alert as the unit of record.** An alert is a persistent, individually identified warning record. Across the researched sample and the industry's interchange standard, an alert consistently carries:

- **what** — the event type and category (geophysical, meteorological, public safety, fire, health, infrastructure, security...);
- **how emphatic** — the urgency × severity × certainty semantics that distinguish an immediate, extreme, observed threat from a possible future one;
- **where** — the affected area, expressed geographically (polygons, circles, named geocodes, or in cell-broadcast systems, the coverage of selected masts/cells);
- **what to do** — response instructions (shelter, evacuate, prepare, avoid, monitor, all-clear) in plain language;
- **until when** — effective time and expiry;
- **who is warning** — the issuing authority, human-readable and machine-identifiable.

The record is revisable: an update supersedes an earlier alert, and a cancellation retracts one — with systems still delivering the original message able to stop.

**Authorized public origination.** Issuance is restricted to designated authorities. The system enforces this structurally: each alert carries a globally unique sender identifier, message authentication (digital signatures in the interchange standard), and separation between actual alerts, exercises, tests, and drafts. Only emergency services and designated government bodies may issue through a national system; origination tools are certified to government security standards. The authorization chain — not the software's feature set — is what makes a warning credible to the public.

**Public area-based dissemination.** The alert is pushed to the public at large in the affected area. The audience is defined by the alert's geography, not by a subscriber list. Delivery mechanisms are public-facing: cell broadcast to every compatible phone in range of a mast (no phone number needed, no app, no sign-up), broadcast media, outdoor sirens, public websites and social channels. The reach requirement is explicit in the market: residents *and visitors*, people "in, or entering into" the affected area, transients on foreign networks.

### Standard Capabilities

Mature products commonly add, without these being what makes the product a public warning system:

- **Multi-channel dissemination from one alert** — a single alert activates several channel families simultaneously: mobile (cell broadcast, location-based SMS), direct (SMS/email/voice to address-based lists), physical (sirens, digital signage), media (TV/radio interrupt, social media, web publication). Channel corroboration increases the chance the warning is acted upon.
- **Geographic targeting tools** — drawing a polygon on a map, selecting predefined zones, or choosing mast/cell coverage areas.
- **A structured interchange format** — the industry's Common Alerting Protocol (CAP) lets one alert message feed many dissemination systems and lets activations be aggregated for situational awareness.
- **Templates for common event types** and pre-approved message patterns.
- **Approval workflow** — alerts commonly pass an authorization step before release (exact mechanics vary by jurisdiction and product).
- **Test and exercise machinery** — distinct test/exercise status, scheduled national tests, operator-level tests.
- **Public alert archive** — current and past alerts published on a public page, sometimes with a machine-readable feed.
- **Multilingual alerts** — the same alert issued in multiple languages, commonly including regional-language variants.
- **Accessibility** — attention signals (sound/vibration) that override silent mode, read-aloud rendering.
- **Integration spine** — national alert gateways, 9-1-1/dispatch systems, GIS platforms, mobile network operators.
- **Situational-awareness overlays** — in some products, device density, crowd movement, and population patterns in the affected area, to inform the next alerting decision.

### One Structure, Many Implementations

The core is conceptual; implementations differ on every layer:

```text
Concept:   Alert record
Realized:  CAP-class structured message · web-form alert with map polygon · zone-based update

Concept:   Authorized origination
Realized:  national credentialing of alerting authorities · certified origination tools · approval workflows

Concept:   Public dissemination
Realized:  cell broadcast · location-based SMS · address-based SMS · sirens · broadcast media ·
           social/web publication · digital signage · public site/app
```

A reader who has only seen one implementation (e.g., a phone-based national alert service) should still recognize a siren-control console or a county polygon-drawing origination tool as the same Type.

## How It Works

### Compose and authorize the alert

```text
Threat identified
→ operator selects an event template (or starts blank)
→ defines the affected area (draw polygon / pick zone / select cells)
→ writes headline, description, and protective instructions
→ sets urgency/severity and validity window
→ submits for authorization (where the jurisdiction requires it)
→ alert is released
```

The alert is now a record: identified, attributed to its issuing authority, and immutable in the sense that any change is a new version (update) or a retraction (cancel), not a silent edit.

### Disseminate to the public

```text
Released alert
→ fanned out simultaneously to the configured channel set:
   cell broadcast to every compatible device in the area
   location-based SMS to devices detected in the area
   SMS/email/voice to address-based contact lists
   sirens activated with tone or voice message
   broadcast media / digital signage / social media / public website
→ each channel renders the alert in its own form
   (text banner, synthesized voice, siren tone, web page)
→ the public receives corroboration across channels
```

Delivery to mobile devices is location-driven: a phone receives an alert because it is *in the area now* — not because of where its owner lives. No recipient action, account, or app is required for the public channels.

### Update, cancel, and expire

```text
Situation changes
→ operator issues an update (supersedes the earlier alert, references it)
→ or issues a cancellation (referencing the earlier alert;
   systems still delivering it stop)
→ or the alert simply expires at its set expiry time
→ the alert remains in the public archive
```

### Test and exercise

```text
Scheduled test (national or operator-level)
→ alert issued with test status
→ public devices sound the attention signal
→ archived as a test record
```

Exercise/test separation is built into the alert format itself, so a test can never be mistaken for — or silently become — an actual warning.

## Interfaces

Described conceptually; exact layouts vary by product.

### Alert composition console

The operator's primary surface.

- template picker, event type/category fields
- map with area-drawing tools (polygon, circle, zone selection, cell selection)
- urgency/severity/certainty selectors, headline and instruction editors
- validity window, language selection
- primary actions: save draft, submit for approval, issue, update, cancel

### Approval / authorization view

Where required, the reviewing official sees the composed alert with its target area and semantics, and approves, amends, or rejects it.

### Dissemination dashboard

The operational picture during an event.

- active alerts with their areas on a map
- per-channel delivery state
- primary actions: issue follow-up, update, cancel, escalate

### Public alert surface

What the population sees.

- device-level alert presentation: attention signal, message text, link/number for more information
- public web pages: current alerts, past alerts, per-alert detail with issuing authority and target area
- in some products: a public site/app with map-based alert views

### Archive and audit

The system of record view: every alert ever issued, with authority, area, text, timestamps, and update/cancel chains — publicly browsable in some deployments, internally auditable in all.

## Important Rules / Behaviors

### The audience is the area, not a list

The defining behavioral rule. An alert reaches everyone in the affected area — including people who never enrolled, visitors on roaming networks, and phones whose owners' details are unknown to the system. Conversely, the system cannot address "everyone who subscribed" as a first-class audience; subscriber lists, where they exist, are a supplementary channel.

### Only authorized authorities may issue

Issuance is gated by the authority chain: authenticated sender identity, jurisdiction-scoped credentials, and commonly an approval step. A test, exercise, or draft can never be released as an actual alert — status separation is enforced by the format.

### Alerts are versioned, never silently edited

A change to a live alert is an update that supersedes the original; a retraction is a cancellation that references the original and instructs in-flight deliveries to stop. The public archive preserves the chain.

### The alert outlives its delivery

Alerts persist as records after delivery — publicly archived in some systems, internally retained in all — so that the population can verify an alert was genuine and authorities can audit what was warned, when, to where.

### Device-side control is the recipient's, not the system's

In cell-broadcast systems, the recipient's device controls attention behavior (and, in some jurisdictions, allows opting out of lower-severity tiers) — the system broadcasts to all compatible devices regardless. The system's own posture is that alerts should stay switched on; the opt-out is a device setting, not a system feature.

### Public channels complement, not replace, other warning paths

Systems explicitly position themselves alongside news, radio, television, and social media — channel corroboration is a design goal, and devices that cannot receive the alert (older networks, incompatible devices) are expected to be reached through the other paths.

## Variants

- **National cell-broadcast infrastructure** — government-operated system broadcasting to all compatible phones nationwide; no opt-in; public archive; national and operator tests.
- **Multi-channel national platform (vendor-operated)** — commercial platform deployed by national governments, combining cell broadcast, location-based SMS, and address-based SMS with legacy media, often under regional regulatory mandates (e.g., the EU requirement to operate public warning systems).
- **Local origination tool with opt-in base** — county/city/campus systems composing geotargeted alerts, integrating with the national gateway, and supplementing with opt-in resident lists, sirens, and social channels.
- **Zone-based protective communications** — predefined geographic zones (neighborhoods, districts) as the targeting unit, often paired with outdoor acoustic hardware and a public site/app; extends into non-emergency community communications.
- **Hazard-specific warning networks** — flood, weather, or seismic warning systems issuing alerts through the same structure within one hazard domain.
- **Dual-market platforms** — the same product family serving public authorities and enterprises/campuses; the public-safety line stays in this Type, the enterprise line is mass notification territory.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Mass Notification System (enterprise/campus) | audience defined by subscription/roster (employees, students, enrollees); operational-continuity and workforce-safety purpose; no public-area mandate. The same vendor may sell both as separate product lines — the seam is the audience model |
| Emergency Management Platform | the emergency operations system of record (plans, incidents, resources, EOC coordination); alerting is one warning-out capability inside it, and standalone alerting systems exist without EM machinery |
| Status Page Platform | informs users about a service's own status, operated by the service provider; subject is service health, not public safety; authority is commercial, not public |
| Broadcast Management System / News Publishing Platform | produce editorial content for media consumption; the alert is a structured actionable warning record issued through regulated channels, not editorial content |
| Government Service Portal / Constituent Relationship Management | pull/transaction surfaces for constituents; the alert system pushes warnings out to whoever is in the area |
| Incident Management / On-call Management | internal operational alerting to named responders; the public alert system addresses the general population in an area |

The boundary against Mass Notification System is the most important one, because products and vendors straddle it. The structural test: **who is the audience?** If the audience is everyone in a geographic area — including people who never signed up — it is a public alert & warning system. If the audience is a managed list of enrolled people, it is mass notification, even when the message is an emergency warning.

## Representative Products

- **UK Emergency Alerts** — government-operated national cell-broadcast system with public alert archive (researched via official service documentation)
- **Everbridge Public Warning** — commercial multi-channel population-alerting platform deployed by national governments in 25+ countries
- **Rave Alert (Motorola Solutions)** — US state/local/campus origination tool with FEMA IPAWS integration and 9-1-1 coordination
- **Genasys Protect** — zone-based alerting with outdoor acoustic hardware and a public site/app
- **CAP (Common Alerting Protocol, OASIS standard)** — the industry's structured alert interchange format, used to anchor the alert record's semantics

## Sources

Research date: **2026-09-09**

- UK Emergency Alerts — https://www.gov.uk/alerts , https://www.gov.uk/alerts/how-alerts-work , https://www.gov.uk/alerts/past-alerts , https://www.gov.uk/alerts/opting-out
- Everbridge Public Warning — https://www.everbridge.com/products/public-warning/
- Motorola Solutions (Rave Alert) — https://www.ravemobilesafety.com/products/rave-alert/ (redirects to the vendor's mass-notification page)
- Genasys — https://www.genasys.com/
- OASIS Common Alerting Protocol v1.2 — https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html

> Sourcing limitation: the US national alert gateway's own official documentation (fema.gov) was not reachable from the research environment (blocked on repeated attempts). The US gateway is therefore described only through the origination vendor's documented integration with it, and no precise operational details of that gateway are stated in this document. One US community-notification vendor (CodeRED/OnSolve) was acquired mid-research and its product page no longer exists; the local-origination pole is carried by the sampled products above. Precise numeric limits, timing values, and jurisdiction-specific approval mechanics are intentionally not stated; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/analog-era check are recorded in the paired Research Notes.
