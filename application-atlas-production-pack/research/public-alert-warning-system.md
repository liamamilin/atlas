# Research Notes — Public Alert & Warning System

## Research Goal

Understand what a Public Alert & Warning System actually is as an Application Type: what objects exist inside it, who operates it, how an alert moves from an authorized authority to the public, what rules constrain issuance, and where the boundary lies against mass notification systems, emergency management platforms, and broadcast/publishing systems.

## Initial Boundary

- Leaf: `Public Alert & Warning System` (DIRECTORY.md §24 Government, Public Sector & Civic, between Emergency Management Platform and Fire Department Records / EMS Operations Platform).
- Working hypothesis: software used by public authorities to compose, authorize, and disseminate emergency warnings to the public at large through public channels (cell broadcast, broadcast media, sirens, public web/social).
- Expected confusions: Mass Notification System (enterprise/campus), Emergency Management Platform (sibling leaf), Status Page Platform, Broadcast Management System, Government Service Portal.

## Research Questions

1. What is the unit of record — what does an "alert" consist of, and what fields/semantics does it carry?
2. Who may issue an alert, and how is that authorization enforced by the system?
3. How is the audience determined — subscription, roster, or geographic area?
4. Which dissemination channels exist, and are any of them definitional?
5. What is the alert lifecycle (issue → update → cancel → expire)?
6. How do test/exercise modes work?
7. What does the public see (device behavior, public archives, feeds)?
8. Where is the seam against enterprise/campus mass notification?
9. Do national aggregation gateways (IPAWS-class) and local origination tools form one Type or two?
10. Would older, analog-era warning systems (sirens, EBS, NOAA SAME) still fit the definition?

## Representative Products

| Product | Role in sample | Philosophy / position | Evidence tier |
|---|---|---|---|
| UK Emergency Alerts (GOV.UK) | Government-operated national cell-broadcast system | national infrastructure, no-opt-in cell broadcast, public archive | Tier-1 (official service pages: about, how-alerts-work, past-alerts, opting-out) |
| Everbridge Public Warning | Commercial vendor powering national deployments (25+ countries) | multi-channel population alerting (cell broadcast + LBS SMS + address SMS + legacy media), situational awareness | Tier-2 (official product page + FAQ) |
| Rave Alert (Motorola Solutions) | US state/local/campus origination tool | opt-in + geotargeted + FEMA IPAWS integration, 9-1-1 coordination | Tier-2 (official product page + FAQ, vendor-articulated boundary) |
| Genasys Protect | Zone-based + acoustic-hardware vendor | predefined zones, LRAD outdoor speakers, public site/app, dual public/enterprise market | Tier-2 (official root/product pages) |
| CAP v1.2 (OASIS Standard) | The interchange standard for the Type | structured alert message, lifecycle, authentication, geographic targeting | Tier-1 (normative standard text) |

Rejected/adjusted samples:
- FEMA IPAWS (US national aggregator) — fema.gov 403 ×2, Wayback timeout. Held as market context only, via Rave Alert's documented integration. No precise IPAWS operational claims made.
- CodeRED (OnSolve) — OnSolve acquired by Crisis24; the CodeRED product page no longer exists (redirects to Crisis24 mass notification). US local community-notification pole under-sampled first-hand; recorded as limitation.

## Sources

- UK Emergency Alerts — https://www.gov.uk/alerts , https://www.gov.uk/alerts/how-alerts-work , https://www.gov.uk/alerts/past-alerts , https://www.gov.uk/alerts/opting-out (fetched 2026-09-09)
- Everbridge Public Warning — https://www.everbridge.com/products/public-warning/ (fetched 2026-09-09)
- Motorola Solutions / Rave Alert — https://www.ravemobilesafety.com/products/rave-alert/ (redirects to Motorola mass-notification page) (fetched 2026-09-09)
- Genasys — https://www.genasys.com/ (fetched 2026-09-09)
- OASIS CAP v1.2 — https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html (fetched 2026-09-09)
- Unreachable: fema.gov (403 ×2), web.archive.org (timeout), alerts.weather.gov (transport error), gov.uk planner-guidance URL (404), onsolve.com (acquired → Crisis24)

## Product Observations

### UK Emergency Alerts (evidence layer A — direct observation)

- Self-description: "a UK government system that provides warning and advice in a life threatening emergency."
- Authorized origination: "Emergency alerts will only be sent by: the emergency services; government departments, agencies and public bodies that deal with emergencies."
- Dissemination mechanism: "mobile phone masts in the surrounding area will broadcast an alert. Every compatible mobile phone or tablet in range of a mast will receive the alert." Works on 4G/5G; not on 2G/3G/wifi-only; airplane mode may block.
- No-subscription audience model: "The government does not need to know your phone number or location to send you an alert." "You do not need to sign up for them or download an app." "Free."
- Location semantics: "You'll get alerts based on your current location - not where you live or work."
- Device behavior: loud siren-like sound even on silent, vibration, read aloud; sound/vibration lasts about 10 seconds; alert includes a phone number or GOV.UK link.
- Public alert record: "Current alerts" and "Past alerts" pages; each record shows issuing authority, target area, and full message text. Atom feed available.
- Multiple issuing authorities observed in the archive: UK Government, Environment Agency (flooding), Plymouth City Council (WWII bomb cordon) — national, agency, and city-level authorities.
- Area granularity observed: national (England+Wales), country (Wales), region (Cornwall), multi-county lists, hyper-local ("River Soar at caravan parks near Barrow upon Soar").
- Multilingual: English or Welsh (Welsh alerts in Wales).
- Test machinery: national test alerts (Apr 2023, Sep 2025), local tests (Reading 2021, East Suffolk 2021), operator tests page.
- Opt-out: recipients can turn off "severe alerts" and "extreme alerts" in device settings (device-side control, not system-side); page frames alerts as "life-saving information and should be kept switched on."
- Accessibility: audio and vibration attention signals for vision/hearing impairment.
- Explicit non-substitution: "Emergency Alerts will not replace local news, radio, television or social media."

### Everbridge Public Warning (evidence layer A for product; B for market position)

- Self-description: "a public warning system that helps governments and emergency authorities send urgent, location-aware alerts to people at risk during imminent or developing emergencies."
- Audience: "residents and visitors" — "citizens, tourists, commuters, and other transient populations." FAQ: cell broadcast and location-based alerting "can help authorities reach roaming visitors and tourists connected to local mobile networks without requiring prior opt-in."
- Channels: cell broadcast, location-based SMS, address-based SMS, "legacy media such as TV, radio, sirens, email, voice calls, and social media," digital signage, "opt-in address-based systems."
- FAQ defines the three mobile mechanisms: cell broadcast (to all compatible devices on specific towers, no phone numbers), location-based SMS (devices detected in a geographic area via network data), address-based SMS (predefined contact records associated with known addresses/subscriber databases).
- Targeting: Device-Based Geo-Fencing (DBGF) — "alerts delivered to mobile devices based on whether the device itself is located within a defined geographic area"; multi-language alerting.
- Situational awareness layer: visualize incident impact, crowd movement, device density, population patterns, devices by nationality.
- Compliance framing: GDPR, EECC Article 110 (the EU mandate for member states to operate public warning systems); "configurable governance controls, auditability."
- Market position: deployed by national governments in 25+ countries (UK, Germany, Norway, Sweden, Spain, Netherlands, Greece, Iceland, Estonia, Singapore, Peru, Australia, NZ, India coastal states); "protects more than 800 million people."
- Integrations: mobile network operators, public safety systems, GIS platforms, emergency management technologies, national alerting infrastructures.
- Privacy posture: "Passive data from mobile networks is used to identify devices in a specific area without tracking or storing individual locations"; "no PII is exposed or shared with third parties."
- Heritage: "Since 2002... first cell broadcast and location-based SMS solutions"; standardization activity in 3GPP, ATIS, ETSI, EMTEL.

### Rave Alert / Motorola Solutions (evidence layer A for product)

- Self-description: "Rave Alert helps you send critical, geotargeted emergency warnings across cities, states and first responder networks when it matters most."
- Coverage: "Reach residents and visitors across entire cities, states or campuses. Deliver critical warnings through SMS, FEMA IPAWS, emails, social media, landlines and public screens."
- Coordination: "Automatically sync alerts with 9-1-1 dispatch, first responders and local authorities to coordinate a fast, unified civic response." Cross-jurisdiction CAD data (via Link) "can trigger automated rules and dispatch emergency notifications."
- Infrastructure claims: "public-grade reliability tested in major crises. Send millions of geotargeted messages per minute without network bottlenecks to meet state and federal safety mandates."
- Named capabilities: FedRAMP Moderate certified; FEMA IPAWS integration; CAP outbound for digital signage; RSS feed integration.
- Targeting: "Send alerts based on your existing organizational structure — whether by site, floor, department or custom groups — or draw a precise geographic polygon on a map."
- **Vendor-articulated Type boundary (high value)**: the same page's FAQ distinguishes "Enterprise mass notification software (like Alert NXT) — internal workforce safety, operational continuity, facility closures, IT outages" from "Public safety emergency notification systems (like Rave Alert) — community-wide protection, geotargeted emergency alerts (IPAWS/WEA), 9-1-1 dispatch integration and high-volume messaging for state, local and campus environments."
- Page title is "Mass notification systems" — the market labels the category broadly; the vendor splits it into two product lines by audience model.

### Genasys (evidence layer A for product)

- Positioning: "Protective Communications... Go beyond traditional mass notifications with the modern evolution of emergency and non-emergency communications for private and public entities."
- Genasys Protect: "Zone-based communication software and multi-channel alerting for targeted, fast, and clear updates, from all hazard emergencies to daily community events."
- Zone model: "Multi-channel, targeted zone-based communication, alerting, and coordination"; "zone-based planning."
- Acoustic channel: Genasys Acoustics — "High-fidelity outdoor warning systems with clear voice messaging... solar power backup, and satellite backup"; LRAD devices "deliver live or recorded voice and tone messages."
- National Emergency Warning System offer: "No opt-in required for public safety warnings, notifications, and information to everyone in, or entering into, a crisis-affected area."
- Public-facing surfaces: Genasys Protect Public Site (protect.genasys.com) and public app — "Deliver targeted alerts and map-based updates to the public."
- Dual market: public safety (cities, counties, states, federal, military) AND enterprise/higher-ed (stadiums, campuses, facilities) — same platform.
- Use cases: wildfires, floods, hurricanes, active shooter, statewide alerting, seismic emergencies, non-emergency/daily communications.
- Scale claims: 155M+ people protected, 100+ countries, all 50 US states.

### CAP v1.2 OASIS Standard (evidence layer A for the standard; C for canonical inference)

- Self-description: "a simple but general format for exchanging all-hazard emergency alerts and public warnings over all kinds of networks"; "allows a consistent warning message to be disseminated simultaneously over many different warning systems."
- Alert message structure: `<alert>` (identifier, sender, sent, status, msgType, scope, references, incidents) containing one or more `<info>` (language, category, event, responseType, urgency, severity, certainty, effective/onset/expires, senderName, headline, description, instruction, web, contact) each with `<resource>` (images/audio) and `<area>` (polygon, circle, geocode, altitude).
- The urgency × severity × certainty triad: "collectively distinguish less emphatic from more emphatic messages."
- Event categories: Geo, Met, Safety, Security, Rescue, Fire, Health, Env, Transport, Infra, CBRNE, Other.
- Response types: Shelter, Evacuate, Prepare, Execute, Avoid, Monitor, Assess, AllClear, None.
- Message types (lifecycle): Alert / Update / Cancel / Ack / Error. Update "supercedes the earlier message(s)"; Cancel "cancels the earlier message(s) identified in <references>."
- Status codes: Actual / Exercise / System / Test / Draft — exercise/test separation is built into the format.
- Scope codes: Public / Restricted / Private.
- Authentication: "Support credible end-to-end authentication and validation of all messages"; digital signature capability; unique identifier per message and per originator ("sender... Guaranteed by assigner to be unique globally").
- Geographic targeting: "Flexible geographic targeting using latitude/longitude shapes and other geospatial representations in three dimensions."
- Design goal: "The primary use of the CAP Alert Message is to provide a single input to activate all kinds of alerting and public warning systems"; "a basis for a technology-independent national and international 'warning internet.'"
- Use scenarios (non-normative but structurally revealing):
  - Manual origination: Incident Commander uses "a portable computer and a web page (and a pop-up drawing tool to enter the polygon)" to issue an alert with evacuation + shelter-in-place areas.
  - Automated origination by sensor systems.
  - Aggregation/correlation on a real-time state map fed by all warning systems reporting activations as CAP messages.
  - Integrated public alerting: "all warning systems in a community can be activated simultaneously by the issuance, from an authorized authority, of a single CAP message"; each system converts it to its technology's form; "citizens also get corroboration of the alert through multiple channels."
  - Repudiating a false alarm: officials issue a cancellation referencing the erroneous alert; "Alerting systems that are still in the process of delivering the alert (e.g., telephone dialing systems) stop doing so."
- Compatibility with legacy: SAME (NOAA Weather Radio, EAS).

## Cross-product Comparison

| Dimension | UK Emergency Alerts | Everbridge Public Warning | Rave Alert | Genasys Protect | CAP standard |
|---|---|---|---|---|---|
| Operator | UK Government (national) | National governments (25+ countries) | US state/local/campus agencies | Cities/counties/states + enterprise | n/a (interchange format) |
| Unit of record | alert record (authority, area, text) publicly archived | location-aware alert | geotargeted emergency warning | zone-based alert/update | structured alert message (alert/info/area/resource) |
| Authorized origination | emergency services + gov departments/agencies only | governments and emergency authorities | public-safety agencies (FedRAMP-certified) | public-safety + enterprise operators | sender identifier + digital signature + status codes |
| Audience model | everyone in mast range; no opt-in, no phone number | residents + visitors; no opt-in for CB/LBS | residents + visitors + opt-in lists | everyone in/entering zone; no opt-in | scope: Public/Restricted/Private |
| Area targeting | mast/cell coverage | cell broadcast, DBGF, LBS, address-based | polygon on map + org groups | predefined zones | polygon/circle/geocode/altitude |
| Channels | cell broadcast + public web archive/feed | CB, LBS SMS, address SMS, TV/radio/sirens/email/voice/social, digital signage | SMS, IPAWS/WEA, email, social, landlines, public screens | multi-channel + LRAD acoustic + public site/app | any (format only) |
| Lifecycle evidence | issue → public archive | issue → update (implied) | issue → 911/CAD sync | alert/update | Alert/Update/Cancel/Ack/Error |
| Test machinery | national tests, operator tests, test status | n/a (not evidenced) | n/a (not evidenced) | n/a | status: Exercise/Test/Draft |
| Public-facing surface | current/past alerts pages + atom feed | n/a (not evidenced) | n/a | public site + public app | n/a |
| Standard alignment | n/a | 3GPP/ETSI/EMTEL activity | CAP outbound, IPAWS | n/a | the standard itself |
| Non-emergency use | no (life-threatening emergencies) | n/a | n/a | "daily community events" | n/a |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The alert as the unit of record.** A persistent, individually identified warning record carrying: what is happening (event type/category), how urgent/severe/certain (the CAP triad semantics), where (affected area), what to do (instructions/response types), until when (validity/expiry), and who is warning (issuing authority). The record is revisable (update) and retractable (cancel). Remove → a messaging/broadcast tool with no warning record; nothing for channels to consume or the public to archive.

2. **Authorized public origination.** Issuance is restricted to designated public-safety authorities operating under a public-warning mandate; the system enforces the authority chain — authenticated sender identity (CAP: globally unique sender + digital signatures; UK: only emergency services and designated government bodies), commonly approval workflow, and exercise/test separation (CAP status codes; UK national/operator tests). Remove → any organization's notification tool; the "public" trust posture collapses.

3. **Public area-based dissemination.** The alert is pushed to the public at large in the affected area through public-facing channels (cell broadcast, broadcast media, sirens, public web/social), with the audience defined by the alert's area rather than by subscription — reaching residents, visitors, commuters, and transients who never opted in (UK: "every compatible mobile phone or tablet in range"; Everbridge: "residents and visitors... without requiring prior opt-in"; Genasys: "everyone in, or entering into, a crisis-affected area"). Remove → opt-in mass notification system.

Jointly-held load-bearing:
- 1 alone = alert drafting/composition tool
- 2 without 1+3 = authorization paperwork
- 3 without 1+2 = mass notification / broadcast media
- 1+2 without 3 = internal alert workflow with no public warning
- 1+3 without 2 = open publishing (anyone can broadcast warnings)
- 2+3 without 1 = ad-hoc shouting through channels, no record, no update/cancel discipline

### L1 — Common Mature Structure

- Multi-channel dissemination from one alert (cell broadcast + SMS + email/voice + sirens + broadcast media + social/web + digital signage) — the CAP "single input to activate all kinds of alerting systems" pattern; UK's own page notes alerts complement (not replace) news/radio/TV/social.
- Geographic targeting tools: polygon drawing on a map (CAP scenario, Rave), predefined zones (Genasys), mast/cell selection (UK/Everbridge), geocodes (CAP).
- CAP-class structured alert format as the interchange layer (Rave documents CAP outbound; Everbridge active in 3GPP/ETSI/EMTEL; CAP itself).
- Templates for common event types (CAP "template support"; implied by event categories).
- Approval/authorization workflow (common; exact mechanics not directly observed — held at moderate strength).
- Test/exercise machinery: status separation (CAP), national tests, operator tests (UK).
- Public alert archive/feed: current + past alerts pages + atom feed (UK); public site/app (Genasys). Not evidenced for all products — common, not definitional.
- Multilingual alerts (UK English/Welsh; Everbridge multi-language).
- Accessibility (attention signals, read-aloud).
- Integration spine: national gateways (FEMA IPAWS per Rave), 9-1-1/CAD (Rave), GIS platforms, mobile network operators (Everbridge).
- Alert history/audit (CAP references/incidents; Everbridge auditability).
- Situational-awareness overlays: device density, crowd movement, population patterns (Everbridge; Genasys map-based updates).

### L2 — Variant / Optional Structure

- Channel posture: cell-broadcast-first national systems (UK, Everbridge deployments) vs opt-in-notification-first local systems (Rave) vs zone-acoustic-first (Genasys).
- Operator type: government-operated national infrastructure vs commercial vendor serving governments vs dual public/enterprise platform (Genasys).
- Opt-in subscriber lists as a supplementary channel (address-based SMS per Everbridge; Rave opt-in lists).
- Public-facing surfaces beyond the alert itself (public site/app with map-based updates — Genasys; UK archive).
- Situational-awareness depth (device density/crowd movement — Everbridge; absent from UK's public description).
- Regulatory regimes: EECC Article 110 (EU), IPAWS/WEA (US), national mandates elsewhere.
- Non-emergency community communications (Genasys "daily community events") — stretches the Type's edge; the warning core still present.
- Enterprise/campus dual-market packaging (Genasys; Motorola's Alert NXT sibling is the enterprise pole outside this Type).

### L3 — Vendor-specific (research notes only)

- Everbridge: Device-Based Geo-Fencing (DBGF) branding; "one provider, one solution, one support desk"; 800M-people and 25-country deployment claims; 16 patents.
- Genasys: LRAD hardware line; Protect Platform / Acoustics / Evertel product naming; "Ready when it matters" slogan; Forrester positioning.
- Motorola/Rave: Alert NXT sibling product; Link CAD-sharing product; FedRAMP Moderate; "millions of geotargeted messages per minute."
- UK: specific device behavior (~10-second sound), iOS 14.5+/Android 11+ thresholds, "severe alerts"/"extreme alerts" device setting names.
- CAP: exact element names (msgType, urgency/severity/certainty values, SAME compatibility).

## Vendor-specific Findings

- Motorola's own FAQ is the market's clearest self-articulation of the mass-notification vs public-safety-alerting seam (quoted above). It validates the audience-model seam (workforce/roster vs community/area) as the discriminator, from the vendor side.
- Everbridge's FAQ is the clearest articulation of the three mobile delivery mechanisms (cell broadcast / location-based SMS / address-based SMS) and of the no-PII privacy posture.
- Genasys extends the Type toward non-emergency community communications while keeping the no-opt-in zone-based warning core.

## Boundary Findings

1. **vs Mass Notification System (enterprise/campus)** — the sharpest seam. Discriminator: audience model. Public alert & warning defines its audience by the alert's area (public at large, including visitors/transients, no subscription); mass notification defines its audience by subscription/roster (employees, students, residents who signed up). Motorola's own product-line split (Alert NXT vs Rave Alert) documents the seam from the vendor side. Products straddle (Rave serves campuses; Genasys serves enterprises) — the Type boundary is real at the product-line/audience level, not the company level. Remove the public-area audience → mass notification territory.
2. **vs Emergency Management Platform** — EM platform is the emergency operations system of record (plans, incidents, resources, EOC coordination); public alert & warning is the warning-out function. Alerting appears as one capability inside EM suites; standalone alerting systems exist without EM machinery. Remove the warning-out focus → EM platform.
3. **vs Status Page Platform** — status pages inform users about a service's own status, operated by the service provider; public alert systems warn populations about physical-world threats, operated by public authorities. Different subject, different authority, different channels.
4. **vs Broadcast Management System / News Publishing Platform** — those produce editorial content for media consumption; alert systems issue standardized actionable warning records through regulated channels. The alert is a structured record with urgency/severity semantics and response instructions, not editorial content.
5. **vs Government Service Portal / Constituent CRM** — portals handle constituent transactions and service requests; alert systems push warnings out. Direction and purpose differ (pull/transaction vs push/warning).
6. **Internal seam: national gateway vs origination tool** — the Type realizes as (a) national aggregation/dissemination infrastructure (UK Emergency Alerts; IPAWS-class) and (b) origination software used by local authorities (Rave, Genasys, Everbridge deployments). Same core (alert record + authorized origination + public dissemination); different position in the chain. An origination tool that disseminates directly through its own channels (opt-in, sirens, social) without a national gateway is still in-type. The gateway adds channel breadth and national reach, not a different core.

## Historical / Market-Sample Check (per §24)

- Analog era: air-raid sirens operated from municipal control points by authorized operators; the US Emergency Broadcast System (1963) and its predecessor CONELRAD — government-designated authorities activating broadcast stations; NOAA Weather Radio SAME (1980s) — digitally geocoded warnings predating modern software; telephone fan-out trees; press releases. All three L0 legs satisfied with no modern software: alert message (scripted warning + area), authorized authority (designated officials/broadcasters), public dissemination (sirens/broadcast). ✓
- CAP's own history section documents the pre-standard era (NSTC 2000 report calling for "a standard method to collect and relay... all types of hazard warnings... for input into a wide variety of dissemination systems") — confirming the multi-channel dissemination goal predates the standard.
- Regional/national systems without US-style opt-in: J-Alert (Japan, satellite-based), NL-Alert (Netherlands, cell broadcast since 2012) — fit the three-leg core. (Held as conceptual lineage; not fetched this pass.)
- Conclusion: the definition does not over-fit the modern cell-broadcast era. Cell broadcast, DBGF, IPAWS, public web archives, and situational-awareness overlays are all era machinery, not invariants.

## Uncertainties

- FEMA IPAWS official documentation unreachable (403 ×2; Wayback timeout). The US national gateway is described only through Rave Alert's integration claims. No precise IPAWS operational details (message flow, authentication mechanics, channel list) asserted anywhere.
- CodeRED/OnSolve acquired by Crisis24; product page gone. The US local-government community-notification pole is under-sampled first-hand; Rave Alert carries that pole instead.
- Exact approval-workflow mechanics (single vs dual authorization, role names) not directly observed in fetched documents — held as common-mature at moderate strength only.
- Whether every national system publishes a public alert archive — UK does (verified); others unverified. Held common, not definitional.
- Alertus, Cooper Notification, Federal Signal, One2many, national systems (J-Alert, NL-Alert) not sampled first-hand.
- The "situational awareness" layer (device density, crowd movement) is evidenced for Everbridge and Genasys only; its prevalence across the market is unverified — held as optional.

## Final Synthesis

A Public Alert & Warning System is the public-authority warning-out system: authorized authorities compose structured alert records (what/where/how-bad/what-to-do/until-when) and push them to the public at large in the affected area through public-facing channels, without requiring the audience to have subscribed. The defining core is the joint hold of (1) the alert as unit of record, (2) authorized public origination, (3) public area-based dissemination. Everything else — channel breadth, CAP interchange, templates, approval workflows, test machinery, public archives, multilingual/accessibility layers, situational-awareness overlays, national gateways — is common mature structure or variant machinery. The Type's sharpest external seam is against Mass Notification System (audience by area vs audience by subscription); its sharpest internal seam is national gateway vs origination tool (same core, different chain position).
