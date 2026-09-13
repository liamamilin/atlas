# Museum Visitor Experience Platform

## Overview

A **Museum Visitor Experience Platform** is the museum-operated interpretation layer of a visit: the institution's own team assembles digital guides — sets of stops bound to the museum's exhibits, objects, spaces, and points of interest, each carrying narrated or otherwise interpretive media — and publishes them through a surface the platform operates, which visitors use on their own phones, on museum-issued devices, or on screens inside the galleries.

The defining structure is deliberately small:

```text
Institution-authored guide
└── Stop bound to an exhibit / object / space
    └── Interpretive content (narration first, text/image/video as companions)
        └── Reached by the visitor on an operated surface
            (own phone, museum device, or on-site screen)
```

Selling admission, validating entry, managing members, cataloguing objects, and publishing the collection for remote discovery are all real museum software needs — but they belong to neighboring application types. A visitor experience platform makes the visit itself more intelligible: it is the digital layer that stands between the visitor and what is on display.

## Users & Context

Primary users on the institutional side:

- **Interpretation, curatorial, and digital media staff** — write scripts, record or commission narration, select images and video, and structure tours; this is the group the platform's authoring surface is built for.
- **Education and public programs staff** — build family, school, or access-oriented tours alongside the main offer.
- **Marketing and visitor-services staff** — promote the guide on site, monitor how visitors use it, and handle the practicalities of loaned devices.
- **Administrators** — manage languages, accessibility settings, user permissions, and (where devices are issued) the device fleet.

Primary users on the visitor side: anyone in the venue or planning/preparing/following up a visit — general visitors, school groups, tourists, accessibility-needs visitors, and remote audiences who never enter the building. Visitors typically need no account and no training; the interaction is deliberately as light as entering a number, scanning a code, or pointing a phone at an object.

The work context is a physical venue with a live audience: content is authored at desk pace but consumed in gallery conditions — standing, crowds, noise, poor connectivity — which shapes the emphasis on headphones, short stop lengths, offline use, and accessibility.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as this type:

- **The institution-authored guide.** A persistent tour or guide assembled by the museum's own staff. It is composed of discrete **stops** (also called stories, tracks, or points of interest), each bound to an exhibit, an object, a room, an outdoor feature, or another point of interest in or around the venue. The guide — not the individual media file — is the unit the institution maintains and the unit visitors follow.
- **The interpretive content carried by each stop.** Narration is the dominant and historically founding medium; text, images, video, and interactive material routinely accompany it. The content does the interpretation: context, stories, expert voices, close looks at details — the layer a wall label cannot carry.
- **The operated visitor consumption surface with per-stop access.** A surface the platform itself operates — the visitor's own phone (app or web), a museum-issued device, or an on-site touchscreen — through which the visitor reaches the right stop for what is in front of them, by entering a code, scanning a code or object, using location, searching, or browsing the tour. Without an operated surface the content is just an archive; without per-stop access it is a brochure.

### What Mature Products Add

These capabilities are widespread across current products and are what make the platform practical at museum scale. They do not define the type:

- **Web-based authoring** — the institution edits guides in a browser-based content manager, with multiple staff working on content and updates publishing to visitor surfaces without app-store delays or gallery downtime.
- **Multiple tours and collections** — permanent-collection tours, temporary-exhibition tours, family trails, behind-the-scenes guides, outdoor trails, each maintained and categorized separately.
- **Multilingual delivery** — guides offered in many languages, with translation tooling and increasingly synthesized narration lowering the cost of language coverage.
- **Accessibility features** — audio description, image descriptions, captions and transcripts, sign-language video, adjustable text; often a decisive reason museums adopt the platform.
- **Maps and location awareness** — floorplans and indoor maps, outdoor map integration, the visitor's position with nearby stops.
- **Rich media and interaction** — video, image zoom, 360° views, augmented reality, quizzes and games for younger audiences.
- **Visitor analytics** — which stops are played, which routes are taken, where visitors linger; feedback loops into curation and exhibition design.
- **Device-fleet machinery** — where devices are issued: provisioning, locking down settings, charging and storage, real-time device status.
- **Engagement and relationship features** — push notifications, surveys, messaging that connects the visit to a longer audience relationship.

### One Structure, Many Implementations

```text
Concept:      Guide / tour
Realizations: audio tour, exhibition guide, family trail, outdoor trail,
              building/campus tour, collection highlight tour

Concept:      Stop binding
Realizations: number codes at labels, QR codes, AI object recognition,
              search, GPS/beacon proximity, plain browsing

Concept:      Consumption surface
Realizations: visitor's own phone (app / web app), museum-issued
              audio device, on-site touchscreen / kiosk
```

A reader who has only seen one realization — say, a rented keypad audio-guide device — should still be able to recognize a phone-based AR trail or an in-gallery touchscreen as the same type from this model.

## How It Works

### Author the guide

```text
Plan the tour (route, stops, audiences, languages)
→ write scripts for each stop
→ produce narration (recorded, or synthesized/edited in the platform)
→ attach images, video, transcripts, alt text
→ bind each stop to its exhibit/object/location reference
→ preview and publish to the visitor surfaces
```

Authoring is a standing loop, not a one-off project: temporary exhibitions rotate, objects move, and tours are revised as visitor data and curatorial thinking evolve. Products update visitor surfaces in real time from the same content base.

### Visit with the guide

```text
Visitor starts the surface (own phone via app/web, picks up a device, or walks to a screen)
→ selects a tour and language
→ moves through the venue
→ reaches a stop by entering/scanning its code, pointing at the object,
   arriving at its location, or browsing the list
→ listens to / views the interpretive content
→ continues to the next stop (route guidance where offered)
```

The consumption loop is deliberately lightweight: one action per stop, no account required in most products, headphones on the visitor's own phone or built into device hardware. Remote use of the same guides — exploring a museum from home before or after a physical visit — is a standard posture, not an exception.

### Operate the experience

```text
Monitor visitor usage (stops played, routes, dwell, device status)
→ identify what resonates and what is missed
→ revise tours and narration
→ for issued devices: charge, sanitize, restock, track status
```

### Core vs Common vs Optional

**Defining core** — without these, not this type:

- institution-authored guide composed of stops bound to exhibits/spaces
- interpretive content carried by each stop (narration-first)
- operated visitor surface with per-stop access

**Common mature structure** — present in most current products:

- web-based authoring with real-time updates
- multiple tours/collections; multilingual; accessibility features
- maps (indoor/outdoor), location awareness
- rich media (video, 360, AR) and interactive elements
- visitor analytics; device-fleet machinery where devices are issued

**Optional / variant** — depends on institution and product:

- premium or paid content, sponsorship, in-app purchases
- built-in surveys and messaging
- AI object recognition and personalized recommendations
- companion collection-publishing products; monetized tour marketplaces
- dedicated hardware accessories and content-production services

## Interfaces

### Authoring console (staff)

The institution's content workspace.

- tour lists and stop editors; media and narration tools; language and translation panels
- binding controls linking each stop to its exhibit, object record reference, or map position
- primary actions: create/edit tours and stops, upload media, publish, manage staff access

### Visitor's own phone (app or web)

The dominant consumption surface.

- tour selection by exhibition/theme; language and accessibility pickers
- stop list, route/map view, the stop player (listen, read, view, zoom)
- primary actions: choose tour, reach a stop (scan/code/search/location), play, save, share

### Museum-issued device

The venue-loan surface, traditionally the audio-guide handset.

- simplified stop access (code entry or single-movement triggers), narration playback
- operational side: charging/storage logistics, device status and lockdown managed from the platform
- primary actions: start tour, enter code / trigger stop, adjust volume

### On-site touchscreen / kiosk

The in-gallery surface.

- digital labels and interactive storytelling stations next to displays
- themed layouts, hotspot images, multimedia, same accessibility features
- primary actions: explore a display's content, play narration, browse related items

### Analytics / reporting (staff)

- stop-level and route-level usage, language and device activity, feedback responses where offered
- primary actions: view dashboards, export reports, feed revisions back into authoring

## Important Rules / Behaviors

- **The stop is bound to what the visitor encounters.** Whether by number, code, recognition, or location, the access mechanism exists to connect one specific stop to one specific thing in the venue; guides are consumed stop-by-stop in physical context, not primarily as linear media.
- **Content updates must not disturb the visit.** Publishing from the authoring console reaches visitor surfaces without gallery downtime; products emphasize real-time or near-real-time propagation because exhibitions rotate on working schedules.
- **Accessibility is structural, not cosmetic.** Narration plus captions, transcripts, image descriptions, and sign-language options are treated as first-class content channels — the same stop serves multiple sensory modes.
- **The visitor's own phone is both the cheapest and the least controlled surface.** Products therefore typically offer the same guide across phone, device, and screen realizations from one content base, letting the institution choose per venue what to operate.
- **Interpretation is institution-voiced.** Content carries the museum's curatorial voice and credits; the platform operates the surface, but the institution owns what is said.
- **Remote use does not change the model.** The same guides served on site also serve remote audiences; on-site use remains the primary posture, and the stop-in-front-of-an-object pattern degrades gracefully to browsing off site.

## Variants

Common shapes of the same type:

- **Shared multi-museum app** — one free app carries many institutions' guides side by side; the museum authors its guide into a common network.
- **White-label institution app** — each institution runs its own branded app on its own surface.
- **Dedicated device posture** — venue-issued, screen-free audio devices as the primary surface, with a mobile/web companion for accessibility.
- **On-site interactive posture** — gallery touchscreens and digital labels as the primary surface, with the phone as companion.
- **Destination/heritage extension** — the same platform serves historic sites, gardens, cities, and campus tours; the museum is the anchor segment, not the boundary.
- **Services-heavy posture** — institutions buy content production, translation, and narration services alongside the platform.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Attraction Management System | the admission business: operator-defined admission products, sale → transaction → entitlements, entry validation producing attendance; this type carries no admission machinery — the two are complementary layers of the same venue |
| Attraction Ticketing / Event Ticketing Platform | selling and validating entry or seats; no interpretive layer; museums commonly run these alongside a visitor experience platform |
| Digital Collection Portal | public publishing of collection-item records for remote discovery; records-first, catalog orientation — this type is experience-first and aligned to the physical encounter; the two feed each other |
| Museum Collections Management (and its workflow siblings) | custody and documentation of objects — accession, location, loans, condition; this type holds no collection records of its own and consumes imagery/stories at most |
| Exhibition Planning / Installation Management | staff-side display-occasion workflows; this type addresses the visitor during and around the display |
| Event Mobile App | serves an event's attendees (agenda, logistics); this type serves a venue's standing interpretive layer |
| Website Builder / CMS | generic content publishing lacks the guide/tour object, the stop↔exhibit binding, venue devices, and spatial triggers |
| Virtual Tour / 3D Experience Builders | primarily render a remote/3D experience; this type's center is the in-venue interpretive layer (which may include 360/AR content) |

The sharpest boundary is with the **Attraction Management System**: the same museums buy both, vendors' target markets overlap, and the two are easily conflated because both are "the visitor app." The test is what the system is for — selling and validating entry (admission) versus interpreting what the visitor is looking at (experience). Removing interpretation leaves the admission system intact; removing admission leaves the experience platform intact.

## Representative Products

- **Bloomberg Connects** — free shared app carrying many institutions' guides; institution-authored in a common CMS
- **STQRY** — white-label platform family: visitor-phone apps, on-site kiosks, venue device fleets from one builder
- **Smartify** — "digital experience platform" combining apps, devices, AI object recognition, surveys, and revenue services
- **Guide-ID (Podcatcher)** — dedicated screen-free audio-guide device with a Tour Editor platform and accessible mobile companion

The defining core was checked against the device-era audio-guide lineage (keypad handsets, number-entry stops) to avoid over-fitting to the smartphone era, and against the admission-business boundary to keep entry-validation machinery out of the core.

## Sources

Research date: **2026-09-08**

- Bloomberg Connects — homepage, FAQ, and For Partners pages — https://www.bloombergconnects.org/ , https://www.bloombergconnects.org/faq/ , https://www.bloombergconnects.org/for-partners/
- STQRY — homepage, STQRY Apps, STQRY Kiosk, STQRY Fleet product pages — https://stqry.com/ , https://stqry.com/products/stqry-apps , https://stqry.com/products/stqry-kiosk , https://stqry.com/products/stqry-fleet
- Smartify — homepage and Partners page — https://www.smartify.org/ , https://www.smartify.org/partners/
- Guide-ID — homepage and Platform page — https://www.guide-id.com/ , https://www.guide-id.com/products/platform/

> Sourcing limitations: izi.TRAVEL (a free self-service guide platform selected as a fifth sample) was unreachable from the research environment (repeated timeouts) and is held at market-anchor level only; no claims depend on it. Smartify's deeper product and documentation pages were not reachable (404s); its claims rest on official partner-page material. No pricing, numeric limits, or default settings observed on vendor pages are asserted in this document; vendor-specific details remain in the paired Research Notes.
