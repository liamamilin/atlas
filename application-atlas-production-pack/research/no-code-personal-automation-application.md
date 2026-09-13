# Research Notes — No-code Personal Automation Application

## Research Goal

Understand what a **No-code Personal Automation Application** is as an Application Type: what a user builds in it, how automations are triggered and executed, what they act on, and — critically for this directory node — how the Type is separated from its two §03.16 siblings (Personal Workflow Automation Platform, unprocessed; Desktop Automation Application, processed) and from the surrounding automation family (RPA, workflow platforms, agents, app builders).

The desktop-automation pass recorded a pre-hung hypothesis for this leaf (see STATUS Boundary Issues): the seam is **what the artifact acts on, and where it executes** — local desktop apps/windows/input via a local engine (Desktop Automation) vs orchestrating cloud services/app events (the sibling family) — and flagged joint review when the two unprocessed siblings are processed. This pass tests that hypothesis and records the seam from this side.

## Initial Boundary Hypotheses (pre-research)

1. The §03.16 family splits by automation surface: Desktop Automation (local desktop) / cloud workflow platforms (external services) / **personal device-centered automation (this leaf)**.
2. "No-code" is a real structural property (block/palette authoring, no programming required), not just marketing.
3. "Personal" means owned by one person for their own life; no organizational management layer.
4. Risk: the leaf name is close to a synonym of "Personal Workflow Automation Platform" — alias/variant problem must be honestly evaluated rather than forced into a fake distinction.

## Research Questions

1. What is the unit the user builds (recipe/shortcut/profile/applet/flow)? What are its parts?
2. What triggers invocation — personal-context events (time, place, device state, app use) or external service events?
3. What do the actions act on — the user's own device, personal content, connected services?
4. Where does the recipe execute — on-device or in a vendor cloud?
5. What does "no-code" mean operationally in these products (authoring model, escape hatches)?
6. Is there any organizational layer (teams, admin, deployment machinery)?
7. What is the automation's lifecycle (create → enable → run → log → edit → disable/delete/share)?
8. Where are the boundaries: desktop automation, cloud workflow platforms, RPA, agents, home automation, app builders?

## Representative Products

| Product | Pole | Access |
|---|---|---|
| Apple Shortcuts (iOS/iPadOS) | platform-native, consumer, on-device | User Guide fetched (4 pages) |
| Tasker (Android, third-party app) | power-user, on-device, maximal depth | Site + userguide index fetched |
| Microsoft Power Automate (cloud flows) | cloud platform pole (boundary sample) | Microsoft Learn overview fetched |
| Zapier | cloud platform pole (boundary sample) | Help center root fetched |
| IFTTT | consumer connection service | **unreachable** (timeout + 404) — no claims made |
| Samsung Modes and Routines | platform-native Android | **unreachable** (404 ×2) — no claims made |

Apple Shortcuts and Tasker are the Type-core samples; Power Automate and Zapier are sampled primarily as boundary evidence for the workflow-platform seam.

## Sources

- Apple — Shortcuts User Guide (iOS 26): welcome, Intro to Shortcuts, Intro to personal automation, Event triggers — https://support.apple.com/guide/shortcuts/welcome/ios , …/intro-to-shortcuts-apdf22b0444c/ios , …/intro-to-personal-automation-apd690170742/ios , …/event-triggers-apd932ff833f/ios (fetched 2026-09-08)
- Tasker — site root https://tasker.joaoapps.com/ and Userguide index https://tasker.joaoapps.com/userguide/en/index.html (fetched 2026-09-08)
- Microsoft — "What is Power Automate?" / flow types — https://learn.microsoft.com/en-us/power-automate/flow-types (fetched 2026-09-08)
- Zapier — Help Center root — https://help.zapier.com/hc/en-us (fetched 2026-09-08)
- IFTTT — https://help.ifttt.com/hc/en-us (timeout), https://ifttt.com/explore/what_is_ifttt (404) — abandoned per retry rule
- Samsung — https://www.samsung.com/uk/support/mobile-devices/what-are-modes-and-routines-and-how-do-i-use-them/ (404), https://www.samsung.com/us/support/answer/ANS00087296/ (404) — abandoned

Evidence layers: **A** = directly observed on fetched official pages (all per-product observations below); **B** = cross-product commonality; **C** = canonical inference.

## Product A — Apple Shortcuts (iOS/iPadOS)

### Key observations (evidence layer A)

- Definition: "A *shortcut* provides a quick way to get things done with your apps, with just a tap or by asking Siri." The app "lets you combine multiple steps across multiple apps to create powerful task automations."
- **Action** = "the building block of a shortcut… a single step that performs a particular function"; "hundreds of actions"; "Actions represent the best features of the apps on your Apple devices, broken out into smaller parts." Actions interact with "apps and content on your Apple devices, as well as with content and services on the Internet."
- Storage/organization: collections (All Shortcuts, My Shortcuts, Share Sheet, Apple Watch, App Shortcuts); grid of titled/iconed colored tiles; "Tap a shortcut once to run it."
- Run surfaces enumerated: app, Home Screen, widget, Apple Watch, share sheet of another app, Siri, Control Center, Action button, Apple Pencil Pro, Search screen, back-tap of the phone, launched from other apps. (Very wide manual-invocation surface.)
- **Personal automation**: "Personal automation provides a way to run actions based on events such as time of day, arrival at a location, or the opening of an app. A normal shortcut requires you to run it from the Shortcuts app, the Shortcuts widget, or the share sheet, whereas personal automation actions use event triggers, travel triggers, communication triggers, or setting triggers to run."
- Confirmation behavior: "when an event occurs you'll receive a notification asking you to run the automation. You can also edit a personal automation to run without asking."
- **Device-binding rule**: "Personal automation is specific to a device. The automation will be backed up to iCloud but will not sync to other devices." (Shortcuts themselves sync via iCloud per the Edit section; triggered automations do not.)
- Trigger families (guide sections): Event triggers, Travel triggers, Communication triggers, Transaction trigger, Setting triggers. Event-trigger page enumerates: Time of Day (sunrise/sunset with offsets; specific time; daily/weekly/monthly repeat), Alarm (snoozed/stopped/any/existing/wake-up), Sleep (wind down/bedtime/waking — requires Health sleep schedule), Apple Watch Workout (type; start/end — requires paired Watch), Sound Recognition (requires enabling in Settings).
- **Home automation is a separate guide section** with its own triggers (Home app context) — Apple's own taxonomy separates the person's personal automation from the home's device automation.
- Advanced structure: variables (types, adjustment), list actions, Choose from Menu, If, Repeat, Find/Filter, prompts (Ask for Input, Ask Each Time, Show Alert/Show Notification), input types, Receive onscreen items (share-sheet input), Run JavaScript on Webpage action, URL schemes, Web APIs + JSON handling.
- Lifecycle/editing: create, organize in folders, rename, icons, duplicate, delete, sync, share (with import questions for shared shortcuts).
- AI-era: "Based on how you use your Apple devices—your app usage and your browser, email, and messaging history—Siri suggests simple, useful shortcuts that you can quickly tap to run."
- Gallery: curated collection; add with a tap and customize.

## Product B — Tasker (Android)

### Key observations (evidence layer A)

- Definition: "Tasker is an application for Android which performs *tasks* (sets of actions) based on *contexts* (application, time, date, location, event, gesture) in user-defined profiles or in clickable or timer home screen widgets." Tagline: "Total Automation for Android."
- "…extends your control of your Android device and its capabilities, without the need for 'root'."
- Object model (userguide index): **Profiles** (Main Screen) built from **Contexts** — Application / Time / Day / Location / State / Event; **Tasks** (General, Task Edit, **Flow Control**) composed of **Actions** (Action Edit, Settings, A–Z index); **Task Widgets / Shortcuts** (manual/timer invocation on the home screen); **Scenes** (user-built custom UI: buttons, menus, sliders, text, web views, etc.); **Variables**.
- Miscellaneous docs confirm depth and OS coupling: Android System Power Management, App Creation (export automations as apps), CPU Control, Gestures, Icons, Intents, Java, JavaScript, MIDI, Pattern Matching, Run Log.
- Sharing ecosystem: TaskerNet (share), pre-made projects on the forum, community wiki ("Step-throughs, Recipes"), plugin list (ecosystem of plugins).
- Usage examples (vendor page): change settings by application/time/location (screen timeout in a book reader, brightness in the evening, ringer volume at the office, keyguard off at home); TTS read-outs (incoming SMS, battery low, appointments); launch music app when headphones connect; widgets toggling wifi/bluetooth; emergency SMS with GPS location; backups; location tracking via SMS; night airplane mode; scheduled birthday SMS.

## Product C — Microsoft Power Automate (cloud flows) — boundary sample

### Key observations (evidence layer A)

- Positioning: "helps you streamline your business processes and automate repetitive tasks… many connectors allow you to create workflows with little to no knowledge of coding." (Business-process framing; no-code-adjacent authoring.)
- **Access requires a Microsoft work or school email address** — organizational identity, not personal-consumer.
- Three flow types: **Cloud flows** ("triggered either automatically, instantly, or via a schedule"), **Desktop flows** ("automate tasks on the web or the desktop"), **Generative actions (preview)** ("specify only the *intent*… have the AI choose the right set of actions in the right order").
- Confirms the desktop-automation pass's observation: one vendor ships desktop flows and cloud flows as distinct artifact types in one product family — the seam is artifact-level, not vendor-level.

## Product D — Zapier — boundary sample

### Key observations (evidence layer A)

- Help center: "Zap workflows — Create workflows that connect your apps to automate repetitive tasks."
- Connector catalog as the defining structure: "With over 8,000 apps on Zapier, from Airtable to Zendesk."
- Surrounding machinery: Zapier tools (transform data, control how automations run), custom logic (code steps, direct API calls, webhooks), Forms, Tables ("no-code data storage"), Canvas (diagramming), Lead Router, Zapier AI (chatbots, agents, MCP), **Enterprise** tier, Templates.
- Zapier is the no-code *service-orchestration* pole: recipes act on external SaaS apps through a connector catalog, execute in the vendor cloud, and the product family scales into team/enterprise usage.

## Cross-product Comparison

| Aspect | Apple Shortcuts | Tasker | Power Automate (cloud) | Zapier |
|---|---|---|---|---|
| Unit of automation | Shortcut / personal automation | Profile (contexts) → Task (actions) | Cloud flow | Zap |
| Authoring | visual step list over an action library | visual pickers (contexts, actions) + flow control | drag/drop + connectors | visual editor + 8,000-app catalog |
| Trigger source | personal context: time, sunrise/sunset, location, app open, alarm, sleep, workout, sound, communication, transaction, device setting | personal context: application, time, day, location, state, event, gesture | service events / instant / schedule | external service events |
| Execution locus | on-device; triggered automations device-local | on-device | vendor cloud | vendor cloud |
| Acts on | device apps/settings/content + internet services | device settings/apps/content + plugins (incl. home automation area) | external SaaS via connectors | external SaaS via connectors |
| Identity | personal platform account | none (app on device) | work/school account | personal account; enterprise tier |
| Org layer | none | none | organizational (work/school) | enterprise tier |
| Sharing | Gallery + share with import questions | TaskerNet, projects, wiki, plugins | templates | templates |
| Escape hatches | JS on webpage, URL schemes, web APIs | Java, JavaScript, Intents, app creation | code steps | code steps, API, webhooks |
| Run confirmation | notification prompt, or run-without-asking | silent by design (documented posture) | — | — |

### What is stable across the Type-core sample (evidence layer B)

- **Trigger/context + action-step recipe**: every product composes a persistent named recipe from (1) an invocation condition and (2) an ordered sequence of prebuilt action steps. (Apple: trigger → actions; Tasker: contexts → task.)
- **No-code authoring**: steps are chosen from libraries and configured with forms/pickers; programming is never required to build or modify a recipe. Both core products additionally offer optional script/code escape hatches — the authoring model stays no-code.
- **Personal-context trigger catalogs**: trigger sources are the person's own life and device — time/day, location, app use, device state/events, communication/transaction events, sensors.
- **Actions act on the person's own device and digital life**: settings, apps, content, notifications, plus internet services.
- **On-device execution** of the recipe logic for the device-centered products.
- **Wide manual-invocation surfaces beside triggers**: app grids, home screen icons, widgets, voice, share sheet, hardware buttons.
- **Lifecycle machinery**: enable/disable/delete, run feedback/history, folders/organization, gallery/template + community sharing.
- **No organizational layer** in the core products (no roles, fleets, central deployment, admin consoles).

### Common but not defining (L1 candidates)

- variables and step-to-step content flow (both core products; depth varies)
- control flow: conditions, repetition, menus/branching
- run-time prompts and notifications (Ask for Input / Show Notification; confirmation prompts)
- run log / completion feedback
- curated galleries and community sharing (with import-safety questions)
- account sync of recipes (with the notable Apple exception that triggered automations stay device-local)

### Variant, era, or positioning dependent (L2 candidates)

- OS-native (bundled, free) vs third-party app (paid/free-trial)
- consumer-simple vs power-user depth (scenes, pattern matching, app export, CPU control)
- code escape hatches (JS/URL schemes/web APIs/Java/Intents)
- plugin ecosystems
- home-automation extension areas inside the same app
- voice-assistant invocation depth; watch/wearable invocation
- AI-era authoring aids (usage-based suggestions; intent-to-flow composition in the platform pole)
- pricing/limits (not deeply evidenced — kept generic)

### Vendor-specific (L3 — kept out of the final document)

- Apple: "Personal automation" as a feature name; Content Graph engine; iCloud backup-without-sync of automations; Action button/Pencil/back-tap triggers; exact trigger option sets (sunrise offsets, alarm states, Health/Watch dependencies); Sound Recognition.
- Tasker: Profile/Context/Task/Scene terminology; TaskerNet; AutoApps; no-root positioning; 7-day trial; app-creation export.
- Power Automate: work/school sign-up requirement; flow-type triad; generative actions preview.
- Zapier: 8,000+ app catalog; Tables/Canvas/Forms/Lead Router; MCP integration; ZapConnect.

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

A No-code Personal Automation Application is recognizable by three jointly-held properties:

1. **No-code recipe authoring** — the user assembles persistent, named automations — an invocation condition (trigger or single gesture) plus an ordered sequence of action steps — by selecting and configuring prebuilt blocks; programming is never required to build or change an automation.
2. **Personal ownership and scale** — automations belong to one person and serve that person's own digital life; there is no organizational machinery (teams, roles, device fleets, central deployment, admin governance) in the structure.
3. **The person's own device and life as the automation hub** — trigger sources come from the person's own context (time, place, activity, device state, app use, personal events); action steps act on the person's own device (apps, settings, content) and the personal services connected to it; the recipe's logic executes on that device, running on the user's behalf.

Jointly-held is load-bearing: (1 alone + 2 + cloud orchestration of external services) = the Personal Workflow Automation Platform pole; (1 alone + org layer + fleets) = RPA; (programming required) = scripting/desktop-automation territory; (2 + 3 without no-code authoring) = device scripting; (3 without 1+2, acting on local desktop app windows via a local engine) = Desktop Automation Application.

Negative-space discriminators (same mechanism family, different Type when removed):
- Remove the personal device hub — triggers from external service events, actions on external services via a connector catalog, execution in the vendor cloud → **Personal Workflow Automation Platform** (sibling).
- Remove the personal surface — automation acts on local desktop apps/windows/input via a local engine → **Desktop Automation Application** (processed sibling).
- Remove personal scale — centrally managed bot fleets as organizational assets → **Robotic Process Automation Platform**.
- Remove human-designed determinism — a model decides each action at runtime from live observations → **Agent Tool / Computer-use Platform**.
- Remove the "automate my own life" job — building software/apps for others → **No-code Application Builder / Low-code Application Platform**.

### L1 — Common Mature Structure

- trigger/context catalog (time, location, device state, app events, communication/transaction events, sensors)
- action library spanning device functions, apps, content, and internet services
- ordered step editor with per-step parameter forms
- content flow between steps; variables
- control flow (conditions, repetition, menus)
- run-time prompts, notifications, and confirmation behavior
- wide manual-invocation surfaces (app grid, home screen, widgets, voice, share sheet, hardware buttons)
- enable/disable/delete per automation; run history/completion feedback
- galleries/templates and community sharing with import-safety questions
- account sync of recipes (triggered automations often device-bound)

### L2 — Variant / Optional Structure

- OS-native vs third-party; consumer vs power-user depth
- code escape hatches; plugin ecosystems
- home-automation extensions; voice-assistant invocation; wearable surfaces
- AI-era authoring aids (suggestions from usage; intent-based composition)
- export as standalone app; cross-device/watch extension
- pricing/limits postures

### L3 — Vendor-specific

See vendor-specific list; stays in Research Notes.

## Vendor-specific Findings

- Apple's guide itself maintains a two-way split inside one app — **personal automation** (device/personal-context triggers) vs **home automation** (Home-app device triggers) — strong vendor-articulated evidence that personal automation is a distinct surface from home/household automation.
- Power Automate documents the same product family as three artifact types (cloud / desktop / generative) — corroborates the artifact-level seam recorded by the desktop-automation pass.
- Tasker's docs show OS-coupling depth (power management, CPU control, intents) — the device is the platform; OS background-execution policy is a first-class reliability topic.
- Apple's Siri suggestions (from app/browser/email/messaging history) are an AI-era authoring aid: the recipe remains user-visible and user-owned.

## Rejected Findings

- "Personal automation = consumer IFTTT-style service-to-service applets" — rejected as the definition: the Type-core products center the person's own device and life context; service-to-service orchestration is the sibling platform territory. (IFTTT unreachable this pass; no claims made about it.)
- "No-code means no code anywhere in the product" — rejected: mature products ship optional script/code actions as escape hatches; the invariant is that authoring never requires programming.
- "The Type is defined by the smartphone" — rejected as an invariant: the defining structure is the person's own personal computing context as hub; thin ancestors (scheduled feature-phone profiles; personal email filter rules) and platform-native desktop instances fit the same shape. The phone is the dominant current realization.
- "Automatic triggering is what separates this from desktop automation" — rejected: desktop automation also has triggers (hotkey/schedule/event, per that pass's notes). The seam is the act-on surface and execution locus, exactly the hypothesis recorded by the desktop-automation pass.
- "AI runtime behavior is part of this Type" — rejected: AI appears as authoring aids (suggestions) or, in the platform pole, as intent-to-flow composition at authoring time; runtime decisions remain the user-authored recipe. Model-decides-at-runtime is the neighboring agent Type.

## Boundary Findings

1. **vs Personal Workflow Automation Platform (§03.16 sibling, unprocessed) — the central seam.** Working seam recorded from this side: this Type's recipe lives on and acts through the person's own device and personal life context (personal-context triggers; device/content/personal-service actions; on-device execution); the platform leaf orchestrates external services through a connector catalog, executes in the vendor cloud, and commonly carries team/organizational usage (work/school identity at one sampled vendor; enterprise tier at another). Straddle evidence is real and bidirectional: the platform pole serves individuals (no-code personal use), and this Type's products reach internet services. The seam is center-of-gravity, not mutual exclusion. **Joint review recommended when personal-workflow-automation-platform is processed; alias-risk between the two leaf names is acknowledged.**
2. **vs Desktop Automation Application (§03.16, processed).** The recorded surface-level hypothesis is confirmed from this side for the device-personal pole: this Type's artifact acts on the person's own device contexts and life events (settings, apps, content, personal services) rather than driving local desktop app windows/input via a local engine. Same-vendor evidence (one vendor ships desktop flows and cloud flows as two artifact types) supports an artifact-surface-level seam. **This discharges the desktop-automation pass's flag from this side for this leaf**; the personal-workflow-automation-platform half remains open until that leaf is processed.
3. **vs Home automation / smart-home surfaces.** Apple's own guide separates personal automation from home automation inside one product. Where the automation's subject is the household's device network (hubs, sensors, home devices), that is home-automation territory; personal-automation products touch home devices as an extension area. No directory rewrite proposed; noted as adjacency.
4. **vs Agent Tool / Computer-use Platform (§13, processed).** Consistent with the desktop-automation pass's discharge: runtime decisions here are the user-authored deterministic recipe; AI is an authoring aid. No merge.
5. **vs No-code Application Builder / Low-code Application Platform (§12).** Different job: those build software/applications for others; this composes automations for one's own life. Both no-code; boundary is the artifact and the beneficiary.
6. **vs Robotic Process Automation Platform (§10, unprocessed).** Same mechanism family at organizational scale with central fleet management; personal scale here. Consistent with the desktop-automation pass's recorded ownership/scale discriminator.

## Historical / Market-Sample Check (§24 check)

- Would older/regional/platform-native products fit? Feature-phone scheduled profiles and mode switching (time/location-triggered device behavior changes, configured through menus — no code) satisfy the three L0 properties as a thin ancestor. Personal email filter rules (user-composed condition → action over one's own mail flow, form-based authoring) satisfy the recipe shape as a capability-level ancestor. The iOS automation app that became Apple Shortcuts and Tasker's long Android lineage represent the modern product generation; the fetched Apple guide's own version selector documents a multi-version, multi-OS-release history (versions labeled for iOS 12 through iOS 26).
- Cloud-mashup-era no-code tools (visual personal data pipelines) sit closer to the sibling platform pole (cloud execution, service-to-service) — they are claimed nowhere for this Type.
- Check conclusion: the definition does not overfit to the modern smartphone/cloud/AI packaging. The abstractable core — a person composing no-code trigger→action recipes for their own device and life — spans the thin ancestors and the current market. The one historical skew to abstract away: invocation is sometimes gesture-first (shortcuts) and sometimes trigger-first (automations); both are the same recipe shape.

## Uncertainties

1. IFTTT unreachable (timeout + 404) — the consumer service-connection pole is unverified this pass; no IFTTT claims made anywhere. If the sibling platform pass samples it, the seam statement should be revisited.
2. Samsung Modes and Routines unreachable — the platform-native Android pole is evidenced only through Tasker (third-party).
3. Power Automate and Zapier were sampled at overview/help-root level: the org-identity and enterprise-tier claims are directly evidenced, but their deeper org machinery was not researched; the seam is stated as center-of-gravity, not exhaustive.
4. Apple's macOS/watchOS personal-automation story was not fetched (guide is iOS/iPadOS); no cross-OS claims made beyond the guide's own watch-related trigger mentions.
5. Whether the market would classify Zapier-class *personal* usage under this leaf remains genuinely unresolved — recorded as the joint-review item with personal-workflow-automation-platform.
6. Monetization tiers, run limits, and quota machinery were not researched; no numeric claims made.

## Final Synthesis

A No-code Personal Automation Application is a personal tool for automating one's own digital life without programming. Its defining core is small and jointly-held: no-code assembly of persistent trigger→action recipes; personal ownership at personal scale (no organizational machinery); and the person's own device and life context as the automation hub — personal-context triggers in, device/personal-content/personal-service actions out, executed on the device on the user's behalf. Everything that makes modern products feel different — OS-native bundling vs third-party power tools, variables and control flow, galleries and community sharing, code escape hatches, voice/wearable invocation, AI suggestions, home-automation extensions — is standard capability or variant, not definition. The mechanism family is shared with the cloud workflow platforms (different hub: connector-cataloged external services in the vendor cloud — the central sibling seam, flagged for joint review), with desktop automation (different surface: local desktop apps/windows/input via a local engine — hypothesis confirmed from this side), with RPA (different ownership scale), with computer-use agents (opposite runtime decision-maker), and with app builders (different job). The Type's shape predates the smartphone era in thin-ancestor form and is stable at its core while its edges converge with the platform and agent families.
