# Research Notes — Home Security Application

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 (10-step), abstraction per §22, evidence per §23, historical check per §24.

---

## Research Goal

Understand what a **Home Security Application** actually is as an Application Type: the software (overwhelmingly mobile) through which a household controls, monitors, and responds through a residential security system — as distinct from smart-home device control, family location sharing, camera viewing, and commercial alarm systems.

## Initial Boundary (hypothesis before research)

- Core guess: arming/disarming, sensor/camera events, alerts, alarm response (self or professional), household access management.
- Likely confusion set: Smart Home Platform (broad device control), Family Location/Safety (people vs property), standalone camera/doorbell apps, commercial intrusion & access-control systems, Emergency Management (government), Home Management Application (household binder).
- Unknowns: exact arming-state model across products; alarm-response flow detail; whether cameras are definitional; whether professional monitoring is definitional; self-monitoring variants.

## Research Questions

1. What is the core object model? (system/location, devices/sensors, cameras, events, alarms, arming state, users/access, monitoring service)
2. What does "arming" mean structurally, and what states/modes exist?
3. What happens when an alarm triggers — full lifecycle, who is contacted, how is it cancelled, what is dispatch?
4. How do cameras relate to sensors — definitional or common?
5. What user/access structures exist (owner, shared users, guest codes, emergency contacts, safe word, duress PIN)?
6. What are the monitoring variants (professional / self / none) and how does the app behave in each?
7. Where is the boundary with Smart Home Platform, camera apps, and commercial alarm systems?
8. What rules are jurisdictional (permits, false-alarm fees) vs structural?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| SimpliSafe | alarm-first DIY, monitoring-plan ladder | help center reachable (Tier 1); cleanest alarm-lifecycle documentation |
| Ring | camera+alarm consumer DIY, subscription ladder, pro monitoring optional | largest consumer footprint; permission model documented |
| Wyze | budget camera-first with add-on alarm system | different customer tier; third-party monitoring (Noonlight) |
| Vivint | pro-install, integrated smart-home security | JS-walled support site — unreachable (see Sources) |
| ADT | legacy pro-install incumbent | help surfaces 403/404 — unreachable (see Sources) |
| Abode | self-monitoring emphasis hub | support site timed out twice — unreachable (see Sources) |
| Alarm.com | white-label platform powering dealer apps | site timed out — unreachable (see Sources) |

Sample note: 3 products with direct official evidence (SimpliSafe Tier 1; Ring, Wyze Tier 2). The pro-install incumbent pole (ADT/Vivint) is under-evidenced; claims about it are kept weak or omitted.

## Sources

Fetched 2026-09-08:

- SimpliSafe Help Center (Tier 1, directly observed):
  - https://support.simplisafe.com/ (home)
  - https://support.simplisafe.com/articles/app-support/alarm-screen-within-the-simplisafe-app
  - https://support.simplisafe.com/articles/alarm-event-monitoring/what-are-the-service-plan-options
  - https://support.simplisafe.com/articles/alarm-events-monitoring/what-happens-during-an-alarm/6344794f013ba90af0bce6a5
- Ring (Tier 2, official product/support pages; help-center category pages are JS-rendered and returned only the home shell on 3 attempts):
  - https://ring.com/plans
  - https://ring.com/professional-monitoring
  - https://ring.com/support/articles/clv68/adding-and-managing-shared-and-guest-users
- Wyze (Tier 2, official product page; Zendesk category returned 403 once):
  - https://www.wyze.com/products/wyze-home-monitoring-core-starter-kit
  - https://support.wyze.com/hc/en-us (home only)
- Unreachable after 1–2 attempts each (abandoned per network rule): support.vivint.com (JS wall ×2), www.abode.com/pages/support (timeout), support.goabode.com (transport error), www.myadt.com/help (404), www.adt.com/customer-support (403), www.alarm.com (timeout).

---

## Product A — SimpliSafe (evidence layer A: official help center)

### Key observations

- **System composition**: Base Station (hub), Keypad, sensors (Entry, Motion, Glassbreak), Panic Button, Key Fob, Smoke & CO detectors, water/temperature sensors, cameras (indoor/outdoor/doorbell), Smart Lock. App + web account are the software surfaces.
- **Alarm categories** (documented): Burglary (Entry, Motion, Glassbreak, Panic Button, Duress); Active Guard Outdoor Protection alarms (specialist-observed video events); Life Safety (Fire/Smoke, CO); Environmental (Water, Temperature).
- **Alarm lifecycle (burglary)**: sensor triggers → immediate push notification + alarm text → user can cancel (Keypad, Key Fob, in-app Alarm Screen, or replying "C" to the alarm text within a false-alarm grace period) or request help (reply "H", silent panic button, duress PIN) → if no user action, monitoring center phones primary contacts → caller must give the correct **Safe Word** to cancel; wrong/unknown safe word → dispatch requested (user is not told it was wrong, to protect someone under duress) → if contacts unreachable → dispatch requested; secondary contacts then notified that police are on the way.
- **Cancel ≠ disarm**: cancelling via alarm text closes the alarm but the system stays armed; user must separately reply "Disarm now".
- **Per-alarm-type response rules differ structurally**:
  - Smoke: monitoring calls only the *first* primary contact (time-critical); no safe word needed to cancel by phone; cannot cancel via text; with eligible camera + plan, specialist attempts two-way audio through the camera before dispatch.
  - CO: automated call **and** immediate dispatch simultaneously; cannot be cancelled.
  - Environmental (water/temperature): automated voice message to primary contacts, then secondary; **never dispatches**; cancellation within the first minute suppresses the voice call.
- **Duress**: silent panic (held 2 seconds) or duress PIN at disarm → immediate dispatch request, and *no* push/text/call to the user, deliberately.
- **Contacts model**: Primary Contacts and Secondary Contacts are account-level roles in the alarm protocol.
- **Alarm Screen**: dedicated in-app alarm-handling surface; consolidates alarm info; buttons to Cancel Alarm or Send Help; cancel within grace period means no monitoring call; requires a monitoring subscription (plan-gated).
- **Monitoring plans ladder**: professional monitoring tiers (24/7 emergency dispatch police/fire/medical; top tiers add AI video observation "Active Guard"), "Self-Monitoring w/Camera Recordings" (no professional monitoring), and **Unmonitored** — with no plan the app still does live video and remote arm/disarm; dispatch, network backup, recordings etc. are lost.
- **Other app capabilities**: push notifications, SMS/text alerts, "Secret Alerts" (silent notifications from specific sensors), Scheduled Arming, arming via Google Assistant/Alexa, camera recordings/downloads, system timeline (history window plan-dependent), Test Mode (checks Base Station ↔ Monitoring Center connection), critical alarm notifications that bypass Do Not Disturb.
- **Post-alarm state**: Base Station light pulses red then solid red until the user sets Off Mode and clears the warning — an explicit alarm-event clearing step.

## Product B — Ring (evidence layer A/B: official product + support pages; help-center article bodies reachable via ring.com/support)

### Key observations

- **Location as container**: users and devices are organized per **location**; plans cover "all devices, 1 location"; a user can have devices at multiple addresses (separate plans). "Delete location" is an owner-level action.
- **User/permission model (documented matrix)**: Owner; shared users at three permission levels (**Advanced / Standard / Limited**) scoped per location and per device selection; **Professional installer** level (auto-expires after 48 hours); **Alarm Guest Users** who get a 4-digit access code and can arm/disarm on the Keypad and lock/unlock connected locks. Permission rows include: arm/disarm on keypad, device control, Live View, event history, mode controls, share recorded video, real-time notifications, adjust device settings, user management, add/remove devices, manage account/subscriptions, delete recordings, delete location.
- **Arming**: "Device Modes — Remotely Arm and Disarm your Ring Alarm, customize when your cameras record, and more, in the Ring app." Mode Controls is a distinct permission row. Footnote: a Ring subscription is required for *digital* (in-app) arming/disarming — keypad arming itself is not plan-gated.
- **Professional monitoring flow (documented)**: sensors trigger → real-time notification in Ring app → **video verification** (with permission, agents temporarily access live and recently recorded video) → **confirmation call** from the monitoring center → **emergency response requested** if the user asks or if there is no answer; for carbon monoxide, fire dispatch is requested on every event.
- **Monitoring scope**: intrusion, panic, duress, SOS; add devices for smoke, CO, water/flooding, cold temperatures, glass break. Monitoring center calls the user *and their emergency contacts*.
- **SOS Response**: an in-app SOS button to immediately request emergency services (plan-gated).
- **Enrollment**: professional monitoring is enrolled from app Settings → Monitoring; permit information emailed where jurisdictions require alarm permits; false-alarm fees and guard-response fees are jurisdiction-dependent; Ring states it does not own its monitoring center.
- **Resilience**: Alarm Cellular Backup keeps the system connected when home internet fails (subscription-gated).
- **Video layer**: recorded event history (plan-gated, cloud), Live View, smart alerts (person/package/vehicle), AI features (video descriptions, familiar faces, active warnings) — all camera-side, plan-gated.
- **Sharing**: unlimited phones/tablets can manage devices; shared users are free; subscription managed by owner.

## Product C — Wyze (evidence layer A: official product page; layer B for app behavior)

### Key observations

- **System composition**: Wyze Sense Hub (battery backup, built-in siren), Sense Keypad, Entry Sensors, Motion Sensor, plus add-on Leak and Climate sensors; cameras are a separate Wyze line that integrates.
- **Professional monitoring via third party (Noonlight)**: if an alarm triggers, monitoring "try[ies] to reach you within ~30 seconds, and dispatch[es] emergency services if you can't respond" (vendor-stated figure — treat as vendor claim).
- **Arm/disarm via keypad or Wyze app**; keypad uses a simple code.
- **Environmental monitoring**: leaks, temperature, humidity alerts.
- **Camera alert-trigger customization**: user chooses what designated cameras respond to (motion, person, CO/smoke-alarm audio) and how notifications are delivered — cameras behave as configurable sensors inside the security system.
- **Business model**: hardware + optional monitoring subscription ("no contracts"); monitoring is an add-on, not a precondition for app control.

---

## Cross-product Comparison

| Structure | SimpliSafe | Ring | Wyze | Reading |
|---|---|---|---|---|
| Premises system: hub + sensors at one location | ✔ (Base Station) | ✔ (Alarm base station; location container) | ✔ (Sense Hub) | Universal in sample |
| Arming state controlled from app | ✔ (remote arm/disarm, even unmonitored) | ✔ (Device Modes; in-app arming plan-gated, keypad not) | ✔ (app or keypad) | Universal; plan-gating varies |
| Multiple armed modes (not just on/off) | ✔ (Off Mode named; Home/Away arming referenced) | ✔ (Modes; mode controls permission) | weak evidence (arm/disarm named) | Common; exact mode sets vary |
| Sensor event → user alert (push/SMS) | ✔ | ✔ | ✔ | Universal |
| Alarm event with defined response path | ✔ (rich: safe word, contacts, dispatch) | ✔ (verification → call → dispatch) | ✔ (Noonlight reach → dispatch) | Universal; depth varies |
| Professional monitoring as optional subscription | ✔ (plan ladder incl. self-monitoring & unmonitored) | ✔ (plan-gated) | ✔ (add-on) | Universal in sample |
| Self-monitoring / unmonitored poles supported | ✔ (explicit plans) | ✔ (no plan = app control + live view) | ✔ (no subscription) | Universal in sample |
| Cameras integrated as security devices | ✔ (recordings, two-way audio in smoke alarm) | ✔ (video verification, live view) | ✔ (cameras as configurable triggers) | Common, not definitional (SimpliSafe core is sensors) |
| Life-safety + environmental sensors (smoke/CO/water/temp) | ✔ | ✔ (add devices) | ✔ (leak/climate) | Common |
| Household user/access management | ✔ (primary/secondary contacts, safe word, duress PIN) | ✔ (owner/Advanced/Standard/Limited/installer/guest codes) | weak evidence | Common; depth varies |
| Panic/duress/SOS paths | ✔ (panic button, duress PIN, text "H") | ✔ (panic, duress, SOS button) | not directly evidenced | Common |
| Event history / timeline in app | ✔ (plan-dependent window) | ✔ (event history permission row; recorded video plan-gated) | not directly evidenced | Common |
| Siren on hub | ✔ (Base Station siren) | ✔ (Alarm siren) | ✔ (88 dB, vendor-stated) | Common |
| Network/cellular backup | ✔ (plan-gated) | ✔ (cellular backup, plan-gated) | ✔ (hub battery backup) | Common |
| Scheduled arming | ✔ | not directly evidenced | not directly evidenced | Product-specific in sample |
| Voice-assistant arming | ✔ | not directly evidenced | not directly evidenced | Product-specific in sample |
| AI video features (descriptions, faces, warnings) | ✔ (top plan) | ✔ (top plans) | ✔ (camera AI alerts) | Common current-market, plan-gated |
| Specialist video observation (agents watching) | ✔ (Active Guard) | ✔ (Virtual Security Guard) | ✘ | Vendor-specific pole |
| Jurisdictional machinery (permits, false-alarm fees) | ✔ (implied by safe-word/dispatch protocol) | ✔ (explicit) | not evidenced | Common (US-centric) |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The premises security system of record** — a specific home's security devices (entry/motion-class sensors at minimum; cameras and life-safety/environmental sensors commonly) bound together as one addressable system at one location, held in the household's account.
2. **The arming posture** — a user-controlled system state (a disarmed state plus one or more armed states/modes) that changes how device events are interpreted: the same sensor reading is normal activity while disarmed and a security event while armed.
3. **The alarm event with a response path** — a qualifying event (sensor trigger under armed posture, or an explicit panic/duress/SOS act) raises an alarm event that demands a response: user-side (cancel / verify / request help) and/or professionally mediated (monitoring-center verification → emergency dispatch). The response path may be self-directed or professional; some response path must exist.

Jointly-held is load-bearing:
- 1 alone = device inventory / smart-home dashboard
- 2 without 1 = an abstract toggle with nothing to secure
- 3 without 1+2 = a standalone panic/SOS button app
- 1+2 without 3 = an armed box that never tells anyone anything — the application adds nothing
- 1+3 without 2 = a notification/camera app with no security posture (events can't be *alarms*)

### L1 — Common Mature Structure

- Cameras/doorbells as integrated security devices: live view, recorded clips, video used for verification
- Professional monitoring as an optional subscription tier; self-monitoring and unmonitored poles
- Multi-channel alerting (push, SMS, call), including critical-alarm delivery that bypasses silenced phones
- Household access management: owner + shared members with permission levels; guest/access codes; emergency contacts
- Alarm-protocol identity verification: safe word / duress PIN / access codes
- Panic / duress / SOS actuation paths
- Event history / timeline of system activity
- Device health & connectivity (battery, offline, test mode), hub siren, network/cellular backup
- Life-safety and environmental sensor integration (smoke/CO/water/temperature)
- Arming conveniences: scheduled arming, voice-assistant arming

### L2 — Variant / Optional Structure

- Install model: self-install DIY vs professional installation
- Monitoring posture: professional / self / none (plan ladders)
- Product philosophy: sensor-first alarm systems vs camera-first systems with add-on alarms
- Scope: security-only vs security bundled into a wider smart-home suite
- Distribution: direct-to-consumer vs white-label platform powering dealer-branded apps (market structure; not directly evidenced this pass)
- Platform-native security slices inside general smart-home apps (thin pole; arming semantics usually weak there)
- Jurisdictional overlay: alarm permits, false-alarm fees, verified-response rules (US-centric in sample)
- Small-business use of residential-class systems (documented at SimpliSafe/Ring as a secondary segment)

### L3 — Vendor-specific (research notes only)

- Ring: permission-level names (Advanced/Standard/Limited), 48-hour installer auto-expiry, 14-day invite validity, 4-digit guest codes, Virtual Security Guard (live agent video monitoring), Familiar Faces/Active Warnings/Video Descriptions, Amazon Sidewalk sensor connectivity, Ring Appstore, "Ring does not own its monitoring center" disclosure, in-app arming plan-gating.
- SimpliSafe: Safe Word protocol (wrong word → silent dispatch), "C"/"H"/"Disarm now" alarm-text commands, Alarm Screen, Secret Alerts, Active Guard Outdoor Protection, temporary smoke "disregard" (up to three days, specialist-set), Base Station red-light clearing procedure, Test Mode, primary-vs-secondary contact cascade, per-alarm-type dispatch rules (CO never cancellable; environmental never dispatches).
- Wyze: Noonlight partnership, ~30-second contact claim, 88 dB siren spec, camera-as-configurable-trigger model.

## Rejected Findings (considered, not promoted)

- **"Cameras are definitional"** — rejected: SimpliSafe's documented core is sensors; Ring alarm works without cameras; camera-first is a philosophy, not the Type.
- **"Professional monitoring is definitional"** — rejected: all three sampled products support unmonitored/self-monitored operation with the app still functioning (arm/disarm, live view, alerts).
- **"Smartphone app is definitional"** — rejected as a *structure*: the historical check shows keypad + central station satisfies the same core; the app is the current dominant surface, not the invariant. (The Type is however defined as the *application*, so the software surface is the object being documented; the invariant is what that software must do, not which device it runs on.)
- **"AI alerts / person detection are definitional"** — rejected: plan-gated add-ons across the sample.
- **"Geofence auto-arming"** — not directly evidenced in the sample; not claimed.
- **Exact entry/exit delay durations, exact contact time-frames** — not researched to precision; no numbers stated in the final document (Wyze's "~30 seconds" kept as a vendor claim in research notes only).

## Historical / Market-Sample Check (§24)

- **Pre-app era (keypad + central station over phone line)**: system of devices ✓, arming via keypad ✓, alarm event + monitoring-center call + dispatch ✓. Satisfies the core without app, cloud, cameras, or AI. → Core must not require app-only affordances.
- **SMS-era control (arm/disarm and cancel by text)**: satisfies the core; text commands are an implementation of the response path. ✓
- **Platform-native smart-home apps (Apple Home / Google Home with security devices)**: devices and notifications exist but arming posture and alarm-response protocol are weak/absent → correctly falls *outside* the Type (smart-home territory), confirming that arming + alarm semantics is the discriminator, not device control.
- **Regional products (e.g., monitored systems outside the US)**: core (system, arming, alarm, response) holds; permits/false-alarm machinery is jurisdictional overlay, not definitional. ✓

## Boundary Findings

| Neighboring Type | Boundary judgment | "Remove what → becomes the other" |
|---|---|---|
| Smart Home Platform | Closest and most commercially entangled boundary. Smart home = broad device control/automation with notifications; Home Security = events evaluated against an arming posture with an alarm-response protocol. | Remove arming posture + alarm/response semantics → Smart Home Platform. Remove broad comfort/lighting/energy control → Home Security. |
| Family Location / Safety Application | Property/premises (sensors, cameras, arming) vs people-in-motion (circle member locations). Both "safety". | Remove member locations, keep premises monitoring → Home Security. Remove premises, keep people → Family Location/Safety. |
| Camera / doorbell viewing app (consumer VMS pole) | Camera apps lack arming state and alarm-response protocol; in home security, cameras are one device class among several. | Remove sensors + arming, keep only camera feeds/clips → camera app. |
| Commercial intrusion / access-control systems | Residential premises with household users vs commercial facilities with zones, guard tours, compliance, professional operators. | Change the premises/user model to facilities+operators → commercial security management. |
| Emergency Management Platform (government) | Different actor entirely (public agencies), no household system of record. | — |
| Home Management Application | Household binder/inventory/maintenance vs live security event system. | Remove security event machinery → Home Management. |
| Personal Safety / SOS apps | A standalone panic button is L0-leg 3 without legs 1–2 — a thin pole, not this Type. | Add the premises system + arming → Home Security. |

Taxonomy note: no conflict found. The leaf is a legitimate distinct Type. The Smart Home Platform boundary is the one to watch commercially (products increasingly span both), but the core models remain distinct.

## Uncertainties

- Pro-install incumbent pole (ADT, Vivint) not directly evidenced this pass; their app behavior is inferred only weakly from market position — kept out of strong claims.
- Abode (self-monitoring emphasis) and Alarm.com (white-label platform) unreachable; the white-label dealer-app pole is described as market structure, not from direct evidence.
- Exact arming-mode sets, entry/exit delay behavior, and notification timing precision not researched to numeric precision — deliberately not stated.
- Wyze app-side alarm handling (beyond arm/disarm) under-evidenced (Zendesk 403).
- Geofencing/auto-arming prevalence unknown in sample.

## Final Synthesis

A Home Security Application is the household-side control surface of a residential security system. Its defining core is three jointly-held structures: (1) the premises security system of record — a specific home's security devices bound as one system in the household's account; (2) the arming posture — user-controlled system states that change how device events are interpreted; (3) the alarm event with a response path — qualifying events become alarms that demand a response, whether user-side (cancel/verify/request help) or professionally mediated (monitoring-center verification → emergency dispatch). Cameras, professional monitoring, AI alerts, permission hierarchies, and jurisdictional machinery are all common or variant structure, not definition. The Type is bounded from Smart Home Platforms by the arming/alarm semantics, from Family Location/Safety by property-vs-people, and from camera apps by the sensor-plus-posture model.
