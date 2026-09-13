# Research Notes — Smart Home Platform

Leaf: Smart Home Platform (DIRECTORY.md §29 Home, Family, Personal & Local Services — home/family cluster, after Home Improvement Planner, before Home Security Application)
Slug: smart-home-platform
Research date: 2026-09-09
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "Smart Home Platform" software actually is in the real market: what the platform binds and holds as its system of record (the home? devices? rooms? people?), how devices enter the system, what the core control model is, what automation machinery exists and how users program it, which surfaces users operate through, and where the exact seams lie — especially against the already-processed §29 siblings (Home Security Application, Home Management Application, Home Maintenance Application, Home Improvement Planner, Family Organizer), device-class companion apps, and the industrial/commercial IoT side of the taxonomy (BMS, Industrial IoT, Smart City).

Forward notes inherited from sibling passes:

- home-security-application (2026-09-08): "forward seam for unprocessed §29 sibling smart-home-platform: the discriminator is the arming posture + alarm-response protocol (device events evaluated against a security posture, with a defined response path) vs broad device control/automation; sampled products (Ring, Wyze) commercially span both categories, so the seam is center-of-gravity, not Type identity — recommend the smart-home pass hold the same seam from its side." → Held from this side (see Boundary Findings).
- home-management-application (2026-09-08): "Smart Home Platform = device control/automation; home management = the home's information and operating record. The seam is control vs record."
- home-maintenance-application (2026-09-08): "device control and automation vs upkeep planning."

## Initial Boundary

Working hypothesis going in (sharpened by sibling notes): a household-side application platform whose subject is the home's connected devices — a population of heterogeneous devices (lights, thermostats, plugs, locks, cameras, sensors, appliances) bound into one system per residence, operated through direct control and through user-defined automation, with the mobile app (plus voice and other surfaces) as the household's operating surface.

Nearest types identified up front:

- Home Security Application (§29, processed) — arming posture + alarm lifecycle over security devices.
- Home Management Application (§29, processed) — the home's information/operating record, not its devices.
- Home Maintenance Application (§29, processed) — upkeep planning, not device control.
- Family Location / Safety Application (§29, processed) — people in motion, not premises devices.
- Single-device companion apps (bulb/camera/thermostat vendor apps) — one device class, no cross-device system.
- Building Management System / Building Energy Management (§17) — commercial facilities, professional operators.
- Industrial IoT Platform / SCADA (§16) — industrial estate, not a household.
- Smart City Operations Platform (§24) — municipal scale.
- Personal Automation Platforms (§03.16) — cloud automation across services; no home device system of record.
- Voice assistants (Alexa, Google Assistant, Siri, Bixby) — one interface into the platform, arguably not a Type by themselves in this directory.

Open questions for this pass:

1. Is the home itself an explicit object (locations/rooms/floors) or just context?
2. Is automation definitional or merely common? (The word "smart" and every product's own framing suggest the former, but this must survive the historical check.)
3. Is multi-brand/multi-class device breadth definitional (platform vs device app)?
4. Are cloud connectivity and remote access definitional, or variants (local-first products exist)?

## Research Questions

1. What is the unit of record — the home, the device, the room, the account?
2. How do devices enter the system (pairing, discovery, certification, integrations), and what gates what can join?
3. What is the control model: what can users do to a device, and how is device state represented/kept in sync (including changes made outside the platform)?
4. What is the automation model (triggers/conditions/actions, schedules, scenes, presence, AI suggestions), and how deep does user programming go?
5. What surfaces exist (mobile app, web, voice, dedicated panels) and what is each for?
6. How does remote access work — cloud-dependent, local, hybrid — and what happens offline?
7. How do household members get access (owner/invite/permissions), and how are multiple homes handled?
8. Where are the seams vs Home Security Application, Home Management, device companion apps, BMS/Industrial IoT/Smart City, and generic personal automation?
9. What varies across the market: protocol substrate, cloud vs local, ecosystem lock-in, AI layer, energy, subscriptions?
10. Historical/market-sample check: would X10-era powerline home automation (controller + scheduled lamp/appliance modules, no app/cloud/accounts/rooms) still fit the definition?

## Representative Products

Sample (4 products with reachable official documentation + 1 unreachable ecosystem anchor; different product philosophies and customer tiers):

1. **Home Assistant** — open-source, self-hosted, local-first platform ("no servers in the cloud and no hidden subscriptions... runs on your own hardware, in your own home"). Represents the maker/DIY, privacy/local pole and the maximal-programmability end of the Type. Official documentation (home-assistant.io) is extensive Tier-1.
2. **Apple Home** (the Home app / Apple Home ecosystem) — platform-native consumer platform; "secure way to control and automate lights, locks, thermostats, window shades, smart plugs, and other accessories." Official Home User Guide (support.apple.com) is Tier-1. Represents the OS-integrated, privacy-marketed, certification-gated pole.
3. **Amazon Alexa** (the Alexa app / Echo ecosystem) — voice-first cloud ecosystem platform; controls compatible smart home devices via skills and direct hub connections. Amazon's own Alexa & Alexa Device FAQs (amazon.com) with a dedicated "Alexa Smart Home FAQs" section is Tier-1. Represents the voice-ecosystem pole.
4. **Samsung SmartThings** — hub-based multi-protocol ecosystem ("connect, control and automate your smart home from one app. Compatible with hundreds of devices and brands"), oldest independent platform lineage (now Samsung-owned). Samsung's SmartThings product pages (samsung.com) are Tier-2 official product documentation; the consumer help center was unreachable. Represents the multi-brand hub ecosystem pole.
5. **Google Home** — ecosystem anchor named for market coverage; every fetch attempt failed in this environment (recorded under Sources; no product-specific claims made).

Rejected as primary samples (recorded per network rule / sampling principles):

- **Ring / Wyze** — already consumed as Home Security Application samples; commercially span the security seam. Not re-sampled here.
- **Control4 / Savant** — professional-install channel; no Tier-1 documentation reachable this pass; not claimed.
- **Google Home** — unreachable (see Sources).

## Sources

All fetched 2026-09-09. Evidence layer recorded per observation: A = directly observed on an official source for that product; B = cross-product commonality; C = canonical inference.

- Home Assistant (Tier-1, home-assistant.io):
  - Getting started — https://www.home-assistant.io/getting-started/
  - Concepts and terminology — https://www.home-assistant.io/getting-started/concepts-terminology/
  - Automating Home Assistant (visual automation tutorial) — https://www.home-assistant.io/getting-started/automation/
  - Setting up presence detection — https://www.home-assistant.io/getting-started/presence-detection/
  - Onboarding Home Assistant — https://www.home-assistant.io/getting-started/onboarding/
- Apple Home (Tier-1, support.apple.com Home User Guide for Mac, macOS Tahoe 26):
  - Welcome / Control your home — https://support.apple.com/guide/home/welcome/mac
  - Add accessories — https://support.apple.com/guide/home/add-accessories-hmead877ec9c/mac
  - Automate scenes and accessories — https://support.apple.com/guide/home/automations-hme33ae10cb7/mac
  - Share control of Home accessories — https://support.apple.com/guide/home/share-control-hmeecfab3012/mac
- Amazon Alexa (Tier-1, amazon.com Customer Service):
  - Alexa and Alexa Device FAQs, incl. "Alexa Smart Home FAQs" — https://www.amazon.com/gp/help/customer/display.html?nodeId=201602230
- Samsung SmartThings (Tier-2, samsung.com official product pages):
  - SmartThings overview — https://www.samsung.com/us/smartthings/
  - SmartThings app page (referenced) — https://www.samsung.com/us/apps/smartthings/
- Unreachable (recorded per network rule; no claims made about these):
  - Google Home Help Center — https://support.google.com/googlehome/ (timeout ×2)
  - Google Home product pages — https://home.google.com/get-started/ (timeout), https://home.google.com/ (timeout), Google Play listing (timeout)
  - SmartThings consumer help center — https://support.smartthings.com/hc/en-us (transport error); SmartThings developer docs index (JS shell / 404)

## Product Observations

### Home Assistant — open-source, self-hosted, local-first pole

Key observations (all A unless noted):

- Positioning: "There are no servers in the cloud and no hidden subscriptions: Home Assistant runs on your own hardware, in your own home, and your data stays with you." Journey framing: "from a fresh install to a working smart home."
- Onboarding: install on own hardware → create owner account ("an administrator account. It will always be able to change everything") → enter home location ("used to configure the time zone, unit system, and currency... also used to create the home zone, which designates the area of your home") → default dashboard.
- Concept set (official concepts page): **Integrations** (connect to devices/services/platforms, e.g. Philips Hue integration → Hue Bridge → its devices appear), **Devices** ("a model representing a physical or logical unit that contains entities"), **Entities** ("represents a sensor, actor, or function... used to monitor physical properties or to control other entities"; each has exactly one state plus attributes, e.g. motion detected/clear, light on/off, brightness/color), **Areas** (grouping matching physical rooms; floors above areas; "target actions at an entire group of devices... turning off all the lights in the living room"), **Automations** ("a set of repeatable actions that can be set up to run automatically", three components: triggers, conditions [optional], actions), **Scripts** (actions without triggers; run from dashboards or automations), **Scenes** ("create predefined settings for your devices... saved as a scene and used without having to set individual devices every time"), **Apps** (add-ons, resource cost warnings).
- Automation tutorial (visual editor, no code): sun-set trigger with time offset → action "light turn on" targeting the living room **Area**; time trigger (21:45) + entity-state condition (workday sensor on) + if-then action gating on light state → light turn on with brightness/temperature/color. Automations are named and described ("Turn on living room table light at sunset"). Testing is explicit ("test your automation").
- Presence detection: "tells Home Assistant who is at home and where they are... lets your automations react to people arriving and leaving" (examples: notify when child arrives at school; turn on AC when leaving work). Phone companion app location → `device_tracker` entity; router-based detection alternative; **Zones** (home zone created at onboarding; custom zones e.g. "Office" as trigger or condition); **People** (Settings > People) bind device trackers to persons.
- Remote access: optional; easiest via the vendor-operated cloud service (Home Assistant Cloud / Nabu Casa). Local operation is the default posture; cloud is an add-on. (A)
- Reading: the platform is a self-hosted system of record for a household's devices and entities, organized by areas, driven by user-authored automations; the home (location/zone) is an explicit onboarding object; device state is a first-class observable (states + attributes + history).

### Apple Home — platform-native, certification-gated pole

Key observations (all A):

- Positioning (Home User Guide): "Home provides a secure way to control and automate lights, locks, thermostats, window shades, smart plugs, and other accessories with an Apple device... you can control any 'Works with Apple Home' accessory."
- Guide structure (TOC): rooms (add/arrange/group rooms), add accessories, control accessories (overview, cameras, lights, HomePod, home screen, scenes, automations, widgets, activity history), Grid Forecast, electricity usage and rates, access away from home, set notifications, share control, configure a router.
- Automations page: "Automations can run scenes and control accessories automatically based on the time of day, your location, a sensor being activated, or the action of an accessory. As you work with accessory settings, automations are suggested." Documented automation types: **People Arrive**, **People Leave**, **A Time of Day Occurs** (with "whether somebody is home or not"), **An Accessory is Controlled** (react to a device being turned on/off, with time-of-day and somebody-home qualifiers). Auto-off duration configurable for accessories turned on by an automation. Location automations require Location Services / Share My Location on the primary iPhone or iPad.
- Home hub requirement: automations on Mac require an Apple TV (4th gen+), HomePod/HomePod mini, or (on the older architecture) an iPad left at home — a vendor-specific local-bridge implementation. Sharing control likewise "will require a home hub on the new Home architecture."
- Share control page: owner invites others by Apple Account email; "After the invitation is accepted, the user can control your Home accessories." Per-person camera video sharing setting. Speakers/TV access policy options: everyone / anyone on the same network / only invited people / password-protected.
- Add accessories: must use the Home app on iPhone/iPad/iPod touch (Mac cannot add); Apple Account sign-in required; compatibility governed by the "Works with Apple Home" certification program (accessories website).
- Reading: the home is an explicit object (the "Home" with rooms); accessories join through a certification-gated flow; control, scenes, and automations are the operating verbs; household sharing is invitation-based per account; camera and energy surfaces sit inside the same app.

### Amazon Alexa — voice-first cloud ecosystem pole

Key observations (all A; from the vendor's own FAQ, incl. the "Alexa Smart Home FAQs" section):

- Device scope: "Alexa enables you to control and check the status of a variety of smart home devices, such as compatible lights, switches, plugs, thermostats, cameras, locks, televisions, printers, kitchen appliances, and robot vacuums."
- Connection paths: smart home skills; direct connection to compatible Echo devices (built-in Zigbee hub, e.g. Echo Show 10); Bluetooth or Wi-Fi; in-app setup; "Frustration-Free Setup" (automatic connection); voice discovery ("Alexa, discover my devices"). Firmware updates may be pushed on behalf of manufacturers.
- Two-way state: "We may receive information about those devices, such as device type, name, features, and status and usage history. We may receive this information even when you don't use Alexa to change the state of your device" — e.g., a manually adjusted thermostat's new setting is reflected when asked and in the app and on Echo screens. Device status/usage history feeds personalization and recommendations.
- Device History: reviewable history of smart home device status/usage (30-day window stated by the vendor) — the platform keeps device-state history as a user-visible record.
- Device Discovery: proactive notifications when a compatible device on the Wi-Fi network signals Alexa compatibility; user connects or dismisses; can disable.
- Hunches: "Alexa can alert you by voice or through the Alexa app with suggestions... If Automatic Actions are enabled, Alexa can automatically take action on your behalf for certain types of hunches, such as turning off connected smart lights when you're away." Uses device state + interactions + location. Some Hunches/Automatic Actions enabled by default.
- Routines: automated action sets; documented realization "Routines with sound detection" (device detects selected sounds — snoring, coughing — and triggers actions at chosen times).
- Map View: scan rooms with phone camera → generated floor plan → devices placed on it; deletable.
- Offline: "Local Voice Control allows Alexa to fulfill a limited set of requests on select Echo devices when the device is not connected to the internet, such as requests to control supported lights, plugs, and switches" — cloud platform with a documented local fallback for a narrow request class.
- Security-adjacent service: Alexa Emergency Assist (subscription; sound detection of smoke/CO alarms; agent helpline; explicitly "not a replacement for an alarm system") — documents how the voice-ecosystem platform stops short of the security Type.
- Reading: an account-bound, cloud-operated device population with voice as the primary command path; control + status check is the explicit pairing; automation exists as Routines plus an AI suggestion/auto-action layer; the home appears as a scannable floor plan (Map View).

### Samsung SmartThings — multi-brand hub ecosystem pole

Key observations (all A, Tier-2 official product pages; consumer help center unreachable):

- Positioning: "SmartThings lets you easily connect, control and automate your smart home from one app. Compatible with hundreds of devices and brands, SmartThings brings your entire smart home together."
- Device onboarding (official "How to register your devices"): auto pop-up in the app when a device powers on; manual add via "+" button; scan the SmartThings QR code sticker on the product.
- Device classes sold/managed: hubs ("the heartbeat of your smart home—connect, automate, and control everything"), smart lighting, sensors ("automate lights and appliances based on movement detection"), smart plugs, cameras, thermostats, doorbells; plus Samsung appliances/TVs ("Samsung TV includes a built-in SmartThings Hub" supporting Matter, Thread, Zigbee).
- Account structure (vendor-stated footnote): "All devices must be connected to Wi-Fi or other wireless network, and registered with a single Samsung Account." Structural limits stated by the vendor: max 300 devices per location, up to 10 locations per account, up to 20 rooms per location, up to 20 members invited per account by the location's administrator. (Precise numbers are vendor claims; they document the Location → Rooms → Devices → Members structure.)
- Feature surfaces: Home Insight ("bird's eye view summary of your home"), Home Routine ("create new routines easily with devices you already have"), Device Control ("turn your phone into a remote for all your favorite devices"), 3D Map View ("see your home at a glance... monitor and control your home"), AI Energy Mode (device energy optimization), Family Care / Pet Care, voice control via Bixby.
- Reading: a hub-plus-app multi-brand ecosystem; the location/room/member hierarchy is explicit; "control and automate" is the vendor's own verb pairing; TV/appliance firmware doubles as hub infrastructure (vendor-specific).

### Google Home — unreachable ecosystem anchor

- Market anchor for the voice-ecosystem pole alongside Alexa. All fetch attempts failed (Help Center timeout ×2; product pages timeout; Play listing timeout). No product-specific claims are made anywhere in this pass. Its inclusion in the sample is for market-structure completeness only.

## Cross-product Comparison

| Dimension | Home Assistant | Apple Home | Amazon Alexa | SmartThings |
|---|---|---|---|---|
| Subject of record | household devices/entities on self-hosted instance; home location/zone at onboarding | the "Home" with rooms; certified accessories | account-bound device population; floor-plan Map View | location → rooms → devices per Samsung account |
| Device entry | integrations (bridges, clouds, protocols) | certification-gated pairing via iPhone/iPad | skills / built-in Zigbee hub / Wi-Fi / BT / auto setup | auto pop-up, "+" add, QR scan |
| Device classes observed | lights, motion sensors, climate, TV, sun/workday info entities, vacuum (example) | lights, locks, thermostats, shades, plugs, cameras, speakers | lights, switches, plugs, thermostats, cameras, locks, TVs, appliances, robot vacuums | hubs, lighting, sensors, plugs, cameras, thermostats, doorbells, appliances |
| Control pairing | "monitor physical properties or to control other entities" | "control and automate" | "control and check the status" | "connect, control and automate" |
| Two-way state | states + attributes + history are first-class | activity history page | status/usage received even without commands; manual changes reflected | Device Status Check; Home Insight summary |
| Automation machinery | triggers + conditions + actions; scripts; visual editor; test tooling | time / people-arrive / people-leave / accessory-controlled; suggestions | Routines (incl. sound detection); Hunches with Automatic Actions | Home Routine; AI Energy Mode automation |
| Scenes | scenes = predefined device settings | scenes (dedicated section) | (routines serve the preset role) | (routines serve the preset role) |
| Presence/location | device_tracker + zones + people | People Arrive/Leave automations (Location Services) | location feeds Hunches | (not evidenced this pass) |
| Household access | owner admin account; People objects | invite by Apple Account; per-person camera scope; speaker/TV policy | (household machinery not evidenced this pass) | location admin invites up to 20 members (vendor-stated) |
| Remote access | optional cloud; local-first default | home hub + account ("access away from home") | cloud by default; limited offline Local Voice Control | cloud by default (hub bridges local protocols) |
| Voice | (community options; not shipped core) | HomePod / Siri surface | voice is the primary path | Bixby |
| Energy | (integrations exist; not core pages) | Grid Forecast; electricity usage and rates | (not evidenced) | AI Energy Mode |
| Openness | arbitrary integrations incl. custom | certification gate ("Works with Apple Home") | skills + certified ecosystem | "hundreds of devices and brands"; Matter/Thread/Zigbee |

Cross-product commonalities (B layer) with 3–4/4 support:

1. The home's devices are held as one system organized under the household (home/location object, rooms in most).
2. Control and status are paired verbs everywhere — the platform both operates devices and reports their state, including changes made outside the platform.
3. Automation is the second verb everywhere — "control and automate" appears verbatim in vendor copy (SmartThings, Apple) and as the platform's structure (HA triggers/conditions/actions; Alexa Routines; Apple automation types).
4. Mobile app as the primary surface; voice and other devices as command paths (3/4 evidenced; HA ships none).
5. Household sharing exists where evidenced (Apple, SmartThings; HA People/owner) — owner plus invited members.
6. Heterogeneous device populations spanning many classes — no sampled product is single-class.

## Canonical Model

Four abstraction levels.

### L0 — Defining Invariant

1. **The household device system.** The connected devices of one residence — heterogeneous, spanning more than one device class — are bound together as one addressable system held in the user's platform (account/home/instance). Remove → a pile of single-device companion apps; not a platform.
2. **Device state read + state control.** Each device is exposed as stateful: the platform reads current state (on/off, level, mode, activity) and the user commands state changes through the platform. Remove read → blind control; remove write → monitoring dashboard; remove both → no platform.
3. **Automation.** The user programs home behavior that executes device actions without a manual command each time — on schedules, on device/sensor events, on presence, or on other conditions. Remove → a remote control for devices; the "smart" in smart home disappears.

Conjunction test: 1+2 without 3 = a multi-device remote/status app (not "smart"). 1+3 without 2 = blind automation with no feedback. 2+3 without 1 = disconnected device apps with schedulers. All three jointly = the Type.

### L1 — Common Mature Structure

- Rooms/areas (and sometimes floors or a floor-plan/map view) as the spatial organization of devices; rooms as targets for grouped actions.
- Device onboarding flows: discovery notifications, pairing/pairing-code flows, QR stickers, bridges/hubs, certified-device directories.
- Scenes: saved multi-device presets invoked manually.
- Presence/location as an automation input (people arrive/leave, zones).
- Household member access: owner account + invited members, per-member or per-device scoping.
- Voice control through assistant speakers/devices.
- Device notifications/alerts (motion, door, appliance status) — distinct from alarm machinery.
- Cameras/doorbells as a device class with live view inside the same app.
- Device health/status (offline, battery) and activity/event history.
- Energy surfaces (usage, rates, optimization) — increasingly common, not yet universal.

### L2 — Variant / Optional Structure

- Connectivity substrate: cloud-operated vs local-hub vs local-first self-hosted; protocols (Wi-Fi, Zigbee, Z-Wave, Thread, Bluetooth, historically powerline); Matter as a cross-ecosystem standard.
- Ecosystem identity: bound to a platform vendor account (Amazon/Google/Apple/Samsung) vs self-hosted owner account (Home Assistant).
- Openness: certification-gated device population vs arbitrary integrations/custom code.
- AI suggestion/auto-action layers (Hunches-style) and their default-on posture.
- Map/floor-plan interaction (room scanning, 3D map views).
- Subscription services layered on the platform (cloud video, emergency helplines).
- Multiple homes/locations per user.
- Professional-install channel variants (under-evidenced this pass).

### L3 — Vendor-specific (Research Notes only)

- Apple: home hub requirement (Apple TV 4th gen+/HomePod, iPad on old architecture); Mac cannot add accessories; new Home architecture upgrade; speakers/TV access policy options; Grid Forecast.
- Amazon: Hunches naming/default-on; Map View room scanning; Frustration-Free Setup; built-in Zigbee hub in some Echo devices; Local Voice Control request class; Sidewalk; Smart Home Device History 30-day vendor-stated window; Emergency Assist positioning.
- SmartThings: vendor-stated limits (300 devices/location, 10 locations, 20 rooms/location, 20 members); Samsung TV built-in hub; single Samsung Account requirement; AI Energy Mode percentages (internal tests).
- Home Assistant: entities/integrations/add-on architecture; YAML configuration layer; integration card iconography; Nabu Casa cloud; zone radius default (100 m, vendor-stated).

## Rejected Findings

1. **"Remote access is definitional"** — rejected. Home Assistant's default posture is local; X10-era automation had no remote access at all. Remote/cloud is the dominant modern realization, not the invariant.
2. **"Voice control is definitional"** — rejected. Voice is one command path; Home Assistant ships none, older platforms predate it.
3. **"Rooms/floor plans are definitional"** — rejected as L0; the spatial organization is common mature structure, not the invariant (an X10 controller or a studio apartment installation has no rooms object).
4. **"Multi-brand breadth is definitional"** — rejected as stated; the refined invariant is *heterogeneous device population* (more than one device class). Single-brand ecosystems (e.g., a lighting vendor's suite) remain platforms under this definition if they bind multiple device classes; single-class device apps do not qualify. Vendor lock vs openness is a variant axis.
5. **"AI/ML intelligence is definitional"** — rejected; era-current layer (Hunches, AI Energy Mode).
6. **"Energy management is definitional"** — rejected; optional/segment surface.
7. **"A smart home platform includes security"** — rejected as a Type property; devices (locks, cameras, sensors) are common device classes, but the arming/alarm organizing structure belongs to the Home Security Application Type.

## Boundary Findings

1. **vs Home Security Application (§29, processed)** — the seam the sibling pass asked this pass to hold. Discriminator: the **arming posture + alarm-response protocol**. A smart home platform may contain locks, cameras, sensors, and notify on their events, but device events are not evaluated against a system-wide armed state and there is no alarm lifecycle with a response path (cancel/verify/dispatch). Removal test: strip the arming/alarm semantics from a security product → a smart home platform; strip broad comfort/lighting/energy device control → a security system. Center-of-gravity seam (commercially, Ring/Wyze-class products span both) — held from this side, matching the sibling's framing. Alexa's Emergency Assist copy itself acknowledges the line ("not a replacement for an alarm system").
2. **vs Home Management Application (§29, processed)** — control vs record. The smart home platform operates the home's devices; the home management app keeps the home's information (documents, appliances, maintenance, value). No binder/upkeep machinery observed in any sampled smart home product; no device-control machinery in the sibling's samples. Bundling in the market is conceivable but unverified; seam = the centered object.
3. **vs Home Maintenance Application (§29, processed)** — device control/automation vs upkeep planning. A smart home platform may *execute* device behavior; it does not plan or record maintenance work.
4. **vs Family Location / Safety Application (§29, processed)** — premises devices vs people in motion. Presence in a smart home platform is an automation input about household members, not a safety service over their locations.
5. **vs single-device companion apps** — one device class, no cross-device system, no cross-device automation → not this Type (capability/thin pole).
6. **vs Building Management System / Building Energy Management (§17)** — commercial facilities operated by facility professionals (zones, schedules, compliance, BAS machinery) vs a household-owned consumer platform. Same conceptual ancestry (the sibling seam "occupant vs operator" also appeared in the BMS-adjacent passes), different subject scale and user.
7. **vs Industrial IoT Platform / SCADA (§16)** — industrial estates and machine control vs residential device control; different objects (tags/PLCs vs household devices), different users.
8. **vs Smart City Operations Platform (§24)** — municipal infrastructure operations vs one residence.
9. **vs Personal Automation Platforms (§03.16)** — generic service-to-service automation without a home device system of record; a personal automation tool can *drive* smart home devices but does not hold the household device system.
10. **vs voice assistant products** — the assistant is a command path into the platform (one interface), not the platform; the platform persists the device system.

## Uncertainties

1. Google Home's operational documentation was unreachable; the voice-ecosystem pole rests on Alexa's evidence alone. No Google-specific claims are made.
2. SmartThings evidence is Tier-2 (official product pages); its consumer help center and developer docs were unreachable, so no SmartThings operational flows (automation editor behavior, offline behavior) are claimed.
3. Professionally installed whole-home platforms (Control4/Savant class) were not evidenced this pass; the professional-install channel is recorded as a variant pole with no operational claims.
4. Whether market packaging (vendor suites bundling security + smart home) is eroding the security seam is a commercial observation, not settled by evidence; the center-of-gravity framing is retained.
5. Device-class floor: "more than one device class" as the heterogeneity threshold is a canonical inference (C layer), supported by every sampled product listing 4+ classes; the exact threshold is a judgment, flagged as such.

## Final Synthesis

A Smart Home Platform is the household-side platform for a home's connected devices. Its defining core is three jointly-held structures: (1) the household device system — the home's heterogeneous connected devices bound as one addressable system under the user's platform; (2) two-way device state — the platform reads each device's state and the user commands state changes through it; (3) automation — user-programmed home behavior that acts on schedules, device/sensor events, presence, and other conditions without a manual command each time. Rooms, scenes, member sharing, voice, presence, cameras, notifications, energy, and AI suggestions are the common mature add-ons that make the platform practical; cloud vs local operation, protocol substrate, ecosystem identity, and openness are the variant axes. The Type is bounded from Home Security by the absence of the arming/alarm organizing structure, from Home Management by control-vs-record, and from single-device apps by the cross-class device system. The historical check passes: X10-era scheduled home automation satisfies the core with no app, cloud, accounts, rooms, or voice.
