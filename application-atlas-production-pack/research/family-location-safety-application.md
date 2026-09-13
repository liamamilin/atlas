# Research Notes — Family Location / Safety Application

Research date: 2026-09-07

## Research Goal

Understand what a Family Location / Safety Application actually is as an Application Type: what objects exist inside it, how members join and share location, what safety machinery is built around that sharing, what rules govern visibility, and where the Type ends relative to neighboring Types (home security, parental control, item trackers, family organizers, fleet tracking, social check-in).

## Initial Boundary (hypothesis before research)

- Core hypothesis: a private group of known family members ("circle") in which each member's location is visible to the group (or to guardians), wrapped in safety-oriented machinery (place alerts, check-ins, SOS, driving safety).
- Likely users: parents/guardians watching dependents; adult members sharing mutually (couples, adult children with elderly parents).
- Likely confusion set: Home Security Application (property vs people), Family Organizer (household logistics), parental-control suites (device management vs people safety), item/device trackers (things vs people), friend-location sharing (social graph vs family), fleet/telematics (commercial vehicles vs family members).
- Unknowns at start: consent model details; whether platform-native sharing products fit the same model; how much safety machinery is definitional vs common; identity substrate variability.

## Research Questions

1. What is the group object? (name, membership mechanics, roles, invitation flow, consent)
2. How is member location shared and refreshed? (continuous vs on-demand, background operation, pause, last-known behavior, failure states)
3. What safety machinery is built on top? (place/geofence alerts, check-ins, SOS/emergency alerts, crash detection, driving analysis, dispatch)
4. What surfaces do users operate? (map, member list, places manager, alert settings, notifications)
5. What rules govern visibility? (member consent, guardian authority over minors, pause/privacy modes, history retention)
6. What are the important exceptions? (phone off / battery dead / no signal; false geofence triggers; consent withdrawal; members without the app)
7. What identity substrates exist? (phone number vs platform account)
8. How do the dedicated-app pole and the platform-native pole differ in philosophy?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Life360 | Dedicated family-safety platform, market leader, freemium + paid tiers | Deepest safety machinery (dispatch, crash detection, driving analysis), circle model, multi-circle |
| Apple Find My (People) | Platform-native, privacy-first, free, bundled | Consent-first pairwise sharing, no history retention, contrasts sharply with dedicated-app philosophy |
| GeoZilla | Smaller dedicated family locator app + GPS tracker hardware | Independent implementation of the same core; consent via SMS; tracker-device pole |

Rejected sample candidates: Google Maps location sharing / Google Find Hub (support pages unreachable — see Sources); carrier-era family locator services (no reachable official documentation; used only as an abstract historical check, no factual detail drawn from them); kids' GPS-watch vendors (no official docs fetched — treated as a known variant, not evidence).

## Sources

All fetched 2026-09-07 (Tier 1 official documentation unless noted).

**Life360**
- Help Center root — https://support.life360.com/ (topics: Circles, Location, Bubbles; categories: App / Hardware / Memberships & Orders)
- App category — https://support.life360.com/hc/en-us/categories/29911467485207-App
- "Use the App" section — https://support.life360.com/hc/en-us/sections/30594687351063-Use-the-App (article titles observed: Crash Detection; Digital Safety Features; Circles; Drive Detection & Analysis; Family Safety Assist; SOS with 24/7 Emergency Dispatch (Europe); Place Suggestions; Daily History; Background Restrictions for Android; Flight Detection & Landing Notifications; Emoji Quick Notes & In-App Messaging; Notification Center; Life360 App Data Usage; Movement Icons; Movement Accuracy; Life360 Bubbles Feature; Establishing a New Home Address; Share My Location; Map View)
- "Share My Location" article — https://support.life360.com/hc/en-us/articles/23053695148823-Share-My-Location (full body read)
- life360.com root — 403 (not fetched)

**Apple (Find My — People sharing)**
- Find My product page — https://www.apple.com/icloud/find-my/ (full body read: Live Locations, arrive/leave notifications, opt-in, satellite sharing, privacy/24-hour retention)
- iPhone User Guide: "Share your location in Find My on iPhone" — https://support.apple.com/guide/iphone/share-your-location-iph01954dc44/18.0/ios/18.0 (full body read)
- iPhone User Guide Find My section structure observed (Share your location; Meet up with a friend; Send your location via satellite; Add or remove a friend; Locate a friend; Get notified when friends change their location; Notify a friend when your location changes)

**GeoZilla**
- Product site — https://geozilla.com/ (full body read: consent flow, crash detection, driver coaching, tracker devices, premium)
- Help Center — https://support.geozilla.com/hc/en-us
- User Guide section — https://support.geozilla.com/hc/en-us/sections/360002872994-User-Guide (article titles observed: How to send an invite; How to join the Circle; remove a person; member photo frame colors; widgets; battery optimization; cannot update location (Android/iOS); Emergency Alert; Places; edit/delete a Place; location accuracy; wrong location; 'Unknown address'; 'Couldn't locate'; battery usage)
- "How does Emergency Alert work?" — https://support.geozilla.com/hc/en-us/articles/360011558500-How-does-Emergency-Alert-work (full body read)
- "What are Places & how do I set them up?" — https://support.geozilla.com/hc/en-us/articles/360023861773-What-are-Places-how-do-I-set-them-up (full body read)

**Unreachable / limitations**
- Google Maps location sharing help (https://support.google.com/maps/answer/3118687): timed out twice on 2026-09-07; source abandoned per research rules. The maps-app feature pole (a share-my-location capability inside a general-purpose app) is therefore NOT directly evidenced in this pass and is described only as a positioning hypothesis, without operational detail.
- life360.com root returned 403; evidence taken from the official help center instead.
- No official documentation fetched for carrier-era family locator services or kids' GPS watches; historical/variant reasoning stays abstract.

## Product Observations

### Life360 — Key observations (Evidence layer: A = directly observed on official help center)

- **Circle as group object.** The help center is organized around "Circles" (a top help topic; section Circles under Use-the-App family of topics; popular article "Add a New Member to My Circle"). A user can be in multiple Circles ("If you are in multiple Circles, repeat the steps above in each Circle you're in"). (A)
- **Location sharing toggle per Circle.** Settings → Location Sharing → toggle. Turning it off shows "Location Sharing Paused" under the member's name to other members of that Circle. (A)
- **Check In.** "Tapping Check In shares a nearby location or one you choose to name." Works even while Location Sharing is off. (A)
- **SOS.** "Sending an SOS alert will share your location in every Circle you're in." For paid members in US/CA/UK/AU/NZ the location is also shared with Life360's 24/7 Emergency Dispatch Center. (A)
- **Crash Detection.** If enabled and a collision is detected, shares location with the Circle and emergency contacts; dispatch/emergency-services sharing for paid members in listed countries. (A)
- **History.** Turning off Location Sharing "stops future updates, but it doesn't delete the location history Life360 has already collected"; joining a new Circle may expose that history. "Daily History" is a documented feature; "Drive and Location History" referenced. (A)
- **Feature surface (from documented article titles).** Place Suggestions; Notification Center; Movement Icons / Movement Accuracy (member motion representation on the map); Flight Detection & Landing Notifications; Emoji Quick Notes & In-App Messaging (in-app messaging exists); Establishing a New Home Address; Map View; Bubbles feature; Drive Detection & Analysis; Digital Safety Features; Family Safety Assist; SOS with 24/7 Emergency Dispatch. (A, titles)
- **Hardware.** Help center has a Hardware category and a Tile App section (Tile trackers integrated). (A, structure)
- **Monetization.** Memberships & Orders category; paid-member dispatch/region claims imply a freemium tier structure. (A, structure)

### Apple Find My (People) — Key observations (Evidence layer: A)

- **Pairwise, consent-first sharing, no circle object.** Sharing is set up person-by-person: People tab → Add → Share My Location → pick a contact → choose a duration. Recipients respond to a location-sharing request by tapping Share (accept) or Cancel. Users can stop receiving requests (Allow Friend Requests off). (A)
- **Me / Share My Location toggle.** Master switch; "hide your location from everyone". The shared location comes "From" a chosen device (another device can be the source; Apple Watch may share when iPhone is out of range). (A)
- **Duration options.** "Tap Send and choose how long you want to share your location"; product page: Live Locations "for an hour, a day, or indefinitely". (A)
- **Location change notifications.** "Get notified when friends change their location" and "Notify a friend when your location changes" are documented articles; product page: notifications when "your child arrives at school or a family member leaves work... each person gets the choice to opt in." (A)
- **Location labels.** Home / Work / custom label for one's location. (A)
- **Safety-oriented usage on product page.** "keep in touch with one another, easily find your friends in a crowd, or know when a family member has arrived home safely"; satellite location sharing when off-grid (iPhone 15+). (A)
- **Privacy posture.** "Apple receives location information only when you actively locate your device, mark it as lost, or enable Send Last Location. Location data is encrypted on Apple's servers and only retained for 24 hours." Find My network finding is anonymous and encrypted "even from Apple." (A)
- **Boundary-relevant structure.** Find My is one app with three domains: People, Devices, Items (AirTags/third-party finders). People sharing is one tab of a broader finder app. Family Sharing groups have a separate "Share your location with family members" flow. (A)
- **No user-visible location history.** Nothing in the documentation describes a member location history/timeline; the 24-hour retention statement directly contradicts a history model. (A)

### GeoZilla — Key observations (Evidence layer: A for help center; A for product site claims)

- **Circle with invite/join/remove.** Documented articles: "How to send an invite in Geozilla?", "How to join the Circle?", "How do I delete the invite to join the Circle?", "How to remove a person from Circle?" Member presence states exist (green/grey/yellow frames next to member photos — semantics not read in detail). (A)
- **Consent flow (product site).** "1. Verify the number... 2. Send a location request — The recipient receives an SMS to give consent to their location. Location-sharing is opt-in... 3. Receive the location... in real time." (A, marketing-page wording — mechanism claim, not precise operational detail)
- **Continuous background updating + failure states.** Troubleshooting articles: "I cannot update the location" (Android/iOS), disable battery optimization, improve location accuracy, "Why is the app showing wrong location?", "What does 'Couldn't locate' mean?", "Why do I see 'Unknown address'?" — evidence of a continuously refreshed shared-location model with last-known/unknown states. (A)
- **Places (geofencing).** "Places are areas you can assign geofence zones for, so you are alerted when a family member enters or leaves a location." Setup: Home / Work / School / Other; pick location by name/address, set radius, choose which events to be informed about. (A)
- **Emergency Alert.** Configure Emergency Contacts (select contacts, confirm phone numbers). Sending: open Emergency Alert section, "Wait for 10 seconds for the alert to be sent. This helps prevent false emergency alerts." Contacts with the app get a push notification; contacts without the app get a text message; alert includes location information. (A)
- **Driving safety.** Product site: Crash Detection alerts Emergency Contacts; Driver Safety reports on phone use, speeding, distracted driving; Driver Coaching from motion sensors. (A, product-page wording)
- **Hardware trackers.** App pairs with GPS tracker devices (wearable/attachable for kids, pets, cars); "Find your tracker... on the same map as your family." (A, product site)
- **Monetization.** Premium membership sold on product site; subscription-cancellation help section. (A)

## Cross-product Comparison

| Dimension | Life360 | Apple Find My (People) | GeoZilla | Assessment |
|---|---|---|---|---|
| Group object | Circle (durable named group; user can be in multiple) | No circle object — pairwise shares (+ separate Family Sharing group flow) | Circle (durable named group) | Circle/group is common but pairwise sharing also satisfies the Type → the invariant is "a governed set of known people", not "a named circle object" (C) |
| Joining | Invite to Circle (documented article) | Send location-sharing request; recipient accepts/declines | Invite + SMS consent to share location | Membership/visibility always passes through an invitation or consent step (B) |
| Who can pause/stop sharing | Member toggle per Circle; visible as "Location Sharing Paused" | Master toggle; per-person stop; can refuse requests | Opt-in at join; permission settings exist | The located person controls visibility; product-specific visibility consequences vary (B) |
| Shared location view | Map view with member markers, movement icons | Map with people; direction/speed when moving; Precision Finding | Map with member markers (+ paired trackers) | Map as primary surface across the sample (B) |
| Member status details | Movement icons/accuracy, location history, daily history | Last update, direction/speed, labels; no history | Presence frames, battery/optimization states, last update | Rich member-status info is common; exact fields vary (B) |
| Place alerts (geofence) | Place Suggestions article; arrival/leave framing on market pages generally | "Get notified when friends change their location"; arrive/leave notifications with opt-in | Places with radius + enter/leave alerts | Cross-product commonality (B) — mature-standard, not definitional |
| Check-in | Check In feature (explicit) | Not as named feature (share current location manually) | Not observed | Product-common, not universal (single-product direct evidence → keep qualified) |
| SOS / emergency alert | SOS shares to all Circles + optional dispatch | Not in Find My People (system-level Emergency SOS is separate) | Emergency Alert to emergency contacts (app + SMS) | Common in dedicated products (B), absent in platform-native pole → common-not-core |
| Crash detection / driving analysis | Crash Detection, Drive Detection & Analysis | Absent | Crash Detection, Driver Safety reports, Driver Coaching | Common in dedicated pole (B); optional for the Type |
| Location history | Daily History; retained even after sharing off | Explicitly not retained (24h) | Not directly observed | Divergent by privacy philosophy → variant (L2) |
| In-app messaging / notes | Emoji Quick Notes & In-App Messaging | Absent (separate Messages app) | Not observed | Product-specific here (single product) → keep out of core |
| Hardware trackers on same map | Tile section (items) | Items tab (AirTag etc.) | GPS trackers for kids/pets/cars | Common optional extension: the family map extends to things (B) |
| Identity substrate | Phone-number-based (verify number articles) | Apple Account / platform identity | Phone number verification | Implementation varies → concept-level identity, substrate is variant (B→C) |
| Business model | Freemium + paid tiers (dispatch/regions) | Free, platform-bundled | Freemium/premium | Business model is not definitional (B) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three properties. Remove any one and the product stops being a Family Location / Safety Application:

1. **The family circle** — a persistent, private, membership-governed set of specific known people (typically a household/family), joined by invitation or consent, with at least implicit roles (the people being located; the people doing the locating; guardian authority over dependents is the common realization).
2. **Member location as the shared object** — each member's current or last-known location is visible inside that governed set (usually on a shared map), with visibility governed by membership plus consent/authority, controllable by the located person.
3. **The safety/reassurance purpose** — the location visibility exists to answer "where are my people, are they where they should be, are they okay" and to enable response: contact them, go to them, or get them help.

Remove tests:
- Remove the circle → generic public check-in / broadcast location → social/different Type.
- Remove member-location sharing → household logistics app (organizer/chat) → different Type.
- Remove the safety purpose → a bare location-sharing capability inside another app, not an Application Type of this kind.

Historical check: carrier-operated family locator services (SMS/web era), kids' GPS watch platforms, and platform-native people sharing all satisfy these three properties without any modern machinery (no geofences, no crash detection, no dispatch, no history). Continuous background background-sharing, phone-number identity, and the freemium model are market-current implementations, not invariants.

### L1 — Common Mature Structure

Present in most mature products across the sample:

- **Shared map as the primary surface** with a marker per member.
- **Member status details**: last update time, address/place naming, movement/driving indicators; battery/optimization troubleshooting states (continuous background operation).
- **Arrival/departure place alerts (geofencing)** over named places (home, school, work) with radius and enter/leave notification choice.
- **Pause/stop controls** for the located member, with user-visible sharing state to the rest of the circle ("Location Sharing Paused" in Life360; master toggle in Apple; refusal of requests).
- **Emergency alert path** in dedicated products: a help request that pushes the member's location to circle members and/or configured emergency contacts, with false-trigger prevention and an SMS fallback for contacts without the app.
- **Hardware extension**: the same map also locates tracker devices/items (Tile in Life360; Items tab in Apple; kids/pet/car trackers in GeoZilla).

### L2 — Variant / Optional Structure

Depends on philosophy, segment, geography, business model:

- **Packaging**: dedicated family-safety app (Life360, GeoZilla) vs platform-native sharing inside OS/map apps (Apple Find My People; Google's in-app sharing — not directly evidenced) vs carrier-provided family locator (historical/regional) vs kids'-watch hardware platforms.
- **Group shape**: durable named circle with multi-circle membership (Life360) vs pairwise consent shares optionally grouped by Family Sharing (Apple) vs named circle (GeoZilla).
- **Identity substrate**: phone number (Life360, GeoZilla) vs platform account (Apple).
- **Privacy posture**: retained location/driving history (Life360) vs explicitly no history (Apple). Both are coherent implementations; history is NOT definitional.
- **Safety depth**: crash detection, driving analysis, driver coaching (dedicated pole only); 24/7 human dispatch (paid tiers, region-limited — Life360).
- **Check-in** as a named gesture (Life360).
- **In-app messaging/quick notes** (Life360; single-product evidence).
- **Satellite / off-grid location transmission** (Apple, hardware-dependent).
- **Monetization**: freemium tiers vs free bundled.

### L3 — Vendor-specific (stays out of the final document)

- Life360: Bubbles (feature name observed; semantics not read in detail), Family Safety Assist, Flight Detection & Landing Notifications, Emergency Dispatch region matrix, membership tier names, Tile integration specifics.
- Apple: Precision Finding (UWB), Find My network of >1B devices, Activation Lock, Lost Mode — device-finder machinery adjacent to the People model.
- GeoZilla: 10-second send-hold on Emergency Alert, green/grey/yellow presence frames, "Couldn't locate"/"Unknown address" exact semantics, specific tracker device lineup.

## Rejected Findings (not promoted)

- "Circle" as a named object is NOT definitional — Apple implements pairwise shares; the invariant is the governed set, not the object name.
- Phone-number identity is NOT definitional (Apple uses platform account; historical/platform-native products differ).
- Continuous background sharing is NOT definitional — on-demand/request-based sharing (Apple model) still satisfies the Type; continuous updating is the dedicated-product norm.
- Location history is NOT definitional (directly contradicted by Apple's design).
- SOS/dispatch machinery is NOT definitional (absent in the platform-native pole).
- Freemium tiers, crash detection, driver coaching — business/segment features, not definitional.
- Google's in-app sharing pattern (feature inside a maps app) — could not be evidenced; NOT used in the definition.

## Boundary Findings

| Neighboring Type | Distinction | Remove-test |
|---|---|---|
| Home Security Application | Property/premises (sensors, cameras, arming) vs people-in-motion (circle member locations). Both "safety" but different objects. | Remove member locations, keep premises monitoring → Home Security |
| Family Organizer | Household logistics (calendars, chores, lists, messaging) vs people-location safety. Products can bundle both (Life360 has messaging). | Remove member-location sharing, keep household management → Family Organizer |
| Parental-control suites (adjacent category, not a directory leaf here) | Device/screen-time/content management vs people location & emergency response; overlap in kid-safety bundles. | Remove location, keep screen rules → parental control, not this Type |
| Item/device finder (Find My Devices/Items, Tile-class) | Things vs people as the located entity; the family-location Type's unit is a person. Tracker extension is optional (L1). | Remove people, keep items → device finder |
| Friend-location / social check-in | Social-graph discovery vs family/household governance and safety intent. | Replace family governance with open social graph → social location sharing, different user model |
| Fleet Management / Vehicle Telematics | Commercial vehicles and drivers as operational assets vs family members as persons; driving reports here are member-safety, not fleet ops. | Remove family members, keep vehicle assets → Fleet Management |
| School Transportation / Childcare systems | Institutional responsibility over a roster vs private family self-organization. | Remove private circle, institutionalize the roster → institutional Type |
| Emergency / personal-SOS apps | Circle-of-known-people model vs individual safety network; SOS is one feature here, not the whole model. | Remove the always-on circle view → standalone SOS app |

## Uncertainties

- Google's location-sharing/Find Hub surfaces could not be fetched (two timeouts). The "sharing feature inside a general app" packaging pole is therefore hypothesized, not evidenced; no operational claims about it are made.
- Life360 Bubbles semantics read only as a feature title; not characterized.
- GeoZilla presence-frame colors and exact failure-state semantics not read in detail.
- Carrier-era family locator services: no official documentation reachable; used only as an abstract historical-check argument.
- Kids' GPS-watch platforms treated as a known variant without direct documentation.
- Exact refresh intervals, accuracy radii, and dispatch SLAs deliberately not stated; no sampled source stated them precisely in a way that generalizes.

## Final Synthesis

The Family Location / Safety Application is a consumer application organized around a private, membership-governed circle of known people in which each member's current or last-known location is visible, so that the circle can confirm people are safe and where they should be, and respond when they are not. The defining core is exactly three things — the governed circle, member-location sharing within it, and the safety/reassurance purpose. Everything else — the map surface, place alerts, check-ins, SOS paths, driving machinery, history, trackers, dispatch — is common mature structure or variant machinery layered on that core, and varies sharply by product philosophy: dedicated freemium platforms maximize safety machinery and retention, while platform-native implementations minimize data (consent-first, no history) while preserving the same core.
