# Research Notes — Desktop Automation Application

Research date: 2026-09-07
Directory leaf: Desktop Automation Application (§03.16 Personal Automation)
Slug: desktop-automation-application

---

## Research Goal

Understand what a Desktop Automation Application actually is as an Application Type: the core object of work (the user-authored automation), how automations are authored (recording / building / scripting), how they are triggered and executed on the local machine, what reliability machinery exists, how automations are shared and reused, and where the Type boundary sits against neighboring leaves — especially Robotic Process Automation Platform (§10), Agent Tool / Computer-use Platform (§13), the §03.16 siblings (Personal Workflow Automation Platform, No-code Personal Automation Application), Test Automation Platform (§12), and Code Editor / general scripting tools (§12).

## Initial Boundary Hypotheses (pre-research)

- Hypothesis 1: the core is a user-authored action sequence that runs locally on the user's own machine and acts on the local desktop environment.
- Hypothesis 2: recorder / GUI-builder / script are three authoring philosophies, not three Types.
- Hypothesis 3: the boundary vs RPA is organizational scale + central bot-fleet management; the boundary vs computer-use agents is who decides each action at runtime (this discriminator was established by the agent-tool-computer-use-platform pass: "RPA executes human-designed deterministic scripts on triggers, this Type has a model deciding each action from live observations").
- Hypothesis 4: the boundary vs cloud workflow automation (Zapier-class) is the target surface — cloud services vs the local machine.
- Known confusions: macro recorders, text expanders, test-automation recorders, OS-native schedulers/shells, IDE/scripting runtimes.

## Research Questions

1. What is the core artifact (macro / flow / workflow / script / shortcut) and its internal structure?
2. How are automations authored — recording, visual building, scripting — and how do these coexist?
3. What trigger types exist (manual, hotkey, schedule, app/file/system events, context conditions)?
4. What can automations act on (input simulation, app-specific actions, windows, files, clipboard, system, web)?
5. Where does execution happen (foreground user session, background, attended vs unattended)?
6. How is playback reliability handled (waits, targeting by element / image / coordinate, window state)?
7. How much of a programming model do products expose (variables, conditionals, loops, functions)?
8. How are automations saved, exported, shared, distributed?
9. What OS permission/elevation constraints shape the experience?
10. Where are the boundaries vs RPA, computer-use agents, cloud workflow automation, test automation, and code editors/scripting runtimes?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Platform | Philosophy | Customer tier | Role in sample |
|---|---|---|---|---|
| Microsoft Power Automate (desktop flows) | Windows | low-code designer + recorder; Microsoft ecosystem; self-described as broadening RPA | individual → enterprise | designer+recorder pole; RPA-convergence edge |
| AutoHotkey v2 | Windows | scripting language + runtime (GPL; heritage from AutoIt, 1999) | enthusiast / power user | script-first pole |
| Keyboard Maestro (Stairways Software) | macOS | GUI macro program; "design your own macros and trigger them at any time" | prosumer | GUI-macro pole, 30-year lineage |
| Apple Automator (with Shortcuts relationship) | macOS | OS-native visual automation; "no programming or scripting needed" | all Mac users | OS-native consumer pole |
| Macro Recorder (Bartels Media) | Windows + Mac | record → edit → replay, "No programming. Period." | consumer / small team | pure recorder pole |

## Sources

Tier 1 — official operational documentation (fetched 2026-09-07):

- Microsoft Learn — Power Automate desktop flows: Introduction; Trigger desktop flows from cloud flows; Configure actions and the actions pane; Record desktop flows; Run desktop flows via keyboard shortcuts. (learn.microsoft.com/en-us/power-automate/desktop-flows/…)
- AutoHotkey v2 documentation: Quick Reference index; Using the Program; Hotkeys; Hotstrings. (autohotkey.com/docs/v2/…)
- Apple Support — Automator User Guide (macOS Tahoe 26 tree): Welcome; Create workflows; Run a workflow; Use scripts. (support.apple.com/guide/automator/…)
- Macro Recorder (Bartels Media): product homepage + full documentation table of contents (v5 beta docs path; production docs pointer at /docs/04/). (macro-recorder.com)

Tier 2 — official product pages:

- Keyboard Maestro: keyboardmaestro.com product/documentation pages (Stairways Software).

Accessibility record:

- wiki.keyboardmaestro.com manual: 404 twice (manual/Start, Manual:Home) — abandoned per source-retry rule; Keyboard Maestro evidence downgraded to product-site claims only.
- learn.microsoft.com "actions-introduction" slug 404 — replaced by actions-pane + recording-flow pages found via the official TOC JSON.
- learn.microsoft.com desktop-flows root URL 404 (TOC only).
- Apple Shortcuts-for-Mac guide not fetched this pass (Automator guide sufficient for the OS-native pole); Shortcuts relationship evidenced via Automator's import-workflows-into-Shortcuts page.

---

## Product A — Microsoft Power Automate (desktop flows)

Evidence layer: A (5 official Learn pages).

### Key observations

- Positioning: "Desktop flows broaden the existing robotic process automation (RPA) capabilities in Power Automate and enable you to automate all repetitive desktop processes." Designed for "everyone who performs simple or complex rule-based tasks on their workstations" — home users, small businesses, enterprises. Targets: legacy applications (terminal emulators), modern web and desktop applications, Excel files, folders. Interaction "by using application UI elements, images, or coordinates."
- Core artifact: the desktop flow, authored in the flow designer.
- Authoring mechanism 1 — actions pane: left side of the designer lists all available desktop flow actions in modules; search; favorites; double-click/drag into workspace; action modal with input parameters (hardcoded values or variables, typed), produced variables (auto-generated outputs of the action), per-action error-handling configuration ("On error"); enable/disable actions without deleting (used for testing).
- Authoring mechanism 2 — recorder: "replicating the tasks you wish to automate"; recorder "keeps track of mouse and keyboard activity in relation to UI elements, and it records each action separately"; generates UI and browser automation actions; captured UI elements collected into a UI elements pane; capturing modes for two Windows accessibility frameworks (UIA recommended for modern apps; MSAA for legacy); special handling screens for drop-downs, date/color pickers, IME text entry; drag gestures can generate Resize/Move window actions; image-based recording mode uses image recognition + OCR (Tesseract) with text area + anchor area selection, for apps that don't expose accessibility APIs. Explicit guidance: "Use the recorder to create the backbone of your flow… most recorded tasks should be modified"; "Certain types of actions, like conditionals and loops, can't be recorded."
- Variables: variables pane, data types, %-notation embedding, scoped variables; input/output variables pass data between desktop and cloud flows.
- Triggers observed: keyboard shortcuts to run/pause/resume/stop flows (saved per user, per machine; input variables prompted at run); URL or desktop shortcuts; picture-in-picture runs; triggering from cloud flows (instant or automated cloud flows).
- Execution: on registered machines ("the physical or virtual devices you use to automate desktop processes"); attended vs unattended run modes (licensing attached); sequential/concurrent run modes; run history monitoring; video logs of the last 60s before an unattended failure.
- Enterprise layer (RPA structure, optional for the Type): machine groups, hosted machines, work queues, run-only user role, governance, premium accounts.
- Vendor-specific detail (L3): Copilot "suggested actions" panel (AI-suggested next actions; work/school accounts; region list); 2 MB desktop-flow input limit; "up to 70 desktop flow runs per minute per connection"; IME recording support; %localappdata% storage paths; console.config shortcut list.

## Product B — AutoHotkey v2

Evidence layer: A (4 official doc pages).

### Key observations

- Nature: "AutoHotkey doesn't do anything on its own; it needs a script to tell it what to do. A script is simply a plain text file with the .ahk filename extension… most scripts define a number of hotkeys, with each hotkey followed by one or more actions." Scripting language + resident runtime.
- Triggers: hotkeys (keyboard, mouse buttons, mouse wheel, game-controller buttons; modifier symbols; custom two-key combinations; key-up variants; wildcard/tilde/hook prefixes), hotstrings (typed abbreviations that auto-replace text or run actions), context-sensitive hotkeys/hotstrings via #HotIf conditions (e.g., fire only while a specific application window is active), hotkeys created dynamically at runtime. Suspend/pause of all hotkeys. Startup-folder autostart documented as the standard way to make a script load at login.
- Actions: Send keystrokes to the active/foremost window; window management (activate, move, maximize, wait); control-level targeting (ControlClick/ControlSend with ClassNN control identifiers); pixel color search; Run programs/URLs; DllCall; full language (functions, objects, expressions, regex).
- Targeting aid: bundled Window Spy utility displays window title/class/process/handle, mouse coordinates, focused control, status-bar text, visible text — "intended as a quick reference while writing automation scripts… obtain the exact values needed for common built-in functions."
- Runtime UX: per-script tray icon (open, reload, edit, suspend hotkeys, pause, exit); hidden main window with debugging views (recently executed lines, variables, hotkey list, key history); persistent scripts; quasi-multi-threading of hotkey handlers.
- Reuse/distribution: scripts are shareable text files (official AutoCorrect.ahk example — ~4700 common misspellings corrected on the fly); compile scripts into self-contained .exe; UI-Access builds to interact with elevated windows; v1/v2 launcher.
- Heritage evidence: "a special thanks to Jonathan Bennett, whose generosity in releasing AutoIt v2 as free software in 1999 served as an inspiration" — ties the product to a 25+ year automation-script lineage.
- Vendor-specific detail (L3): hotstring options (ending chars, case, B0, O, Z…), 40-char hotstring limit and ~5000-char replacement limit, Win+H hotstring helper, SendInput/SendPlay/SendEvent modes, Dash UI, launcher syntax detection.

## Product C — Keyboard Maestro (Stairways Software)

Evidence layer: A for the product-site claims themselves; source downgraded (manual wiki unreachable) — no structural claims beyond the site text.

### Key observations (as stated by vendor pages)

- "Keyboard Maestro is a powerful macro program for macOS. With Keyboard Maestro you can design your own macros and trigger them at any time, automating many tedious things on your Mac."
- "Keyboard Maestro can control almost anything on your Mac. If you can perform it manually, Keyboard Maestro can almost certainly automate it for you."
- Version-11 feature names: New Macro Wizard; new Security preference pane; keyboardmaestro command line tool; support for Apple Text Recognition; new actions such as Prompt For Snippet, Create Calendar Event, Send Pushover Notification, Select Menu by Name.
- macOS Accessibility permission requirement: "If you have any troubles with accessibility (eg typing keystrokes, selecting menus, copy/paste, etc), you need to toggle the accessibility permissions… for Keyboard Maestro and Keyboard Maestro Engine" — implies an editor/engine split (engine performs the automation).
- "history over the last thirty years" — the product (and category) is long-lived.
- Not verified this pass (wiki 404): trigger taxonomy, macro-group scoping, variable/palette systems, action library breadth. Kept out of all claims.

## Product D — Apple Automator (macOS)

Evidence layer: A (4 official guide pages).

### Key observations

- Positioning: "Let your Mac do repetitive tasks for you. With Automator, you don't need to know complicated programming or scripting languages to create automations—you can create a custom workflow and have your Mac do the work for you."
- Core artifact: the workflow. Creation: File > New → select workflow type (type menu with descriptions; Quick Action is one named type) → add actions from the Library (grouped by app or by type of file/data; searchable) → double-click to add; drag to reorder → save.
- Recording exists inside the visual model: "Record your own action: Click the Record button and complete the task you want to automate… it automatically appears in your workflow."
- Quick Action workflows surface in Finder windows, the Services menu, and the Quick Actions menu — OS-level invocation surfaces.
- Execution: "The workflow executes from the top, running each action in sequence"; Log area with status messages, warnings, errors; green checkmark per completed action; View Results utility action for inspection; per-action option "Show this action when the workflow runs" (runtime prompt).
- Variables action and loop action documented ("Use variables", "Use the loop action").
- Script escape hatch: Run Shell Script action (bash, selectable shell); Run AppleScript / Run JavaScript actions editable in place; Automator itself is scriptable (AppleScript/JXA dictionary). Shows the Type's mechanism range beyond input simulation: automations can act through app-provided actions and scripts.
- Platform convergence: Automator workflows import into the Shortcuts app ("automatically become a collection of shortcuts") — OS-native automation surfaces are consolidating.
- Not enumerated in fetched pages: the full list of workflow types; per-type trigger details (e.g., Folder Actions) — not claimed.

## Product E — Macro Recorder (Bartels Media)

Evidence layer: A (product page + complete documentation TOC; production-version doc pages not fetched — structural claims only).

### Key observations

- Positioning: "records your mouse and keyboard actions for infinite playback… Press Record. Perform the actions. Press Stop. Edit the macro. Press Play. Repeat the macro." Windows + Mac. "No programming. Period." — no-code positioning; "Macro scripts consist of easy-to-edit steps instead of cryptic macro code."
- Use cases listed by vendor: automate repetitive tasks, hand out recorded automations to a team, screencasts, auto-fill forms, system maintenance, auto-login, auto-click websites/programs, software test automation. (The test-automation mention is boundary evidence: same driving mechanism, different job.)
- SmartClick targeting: "uses visual context around the click location rather than fixed X/Y coordinates… scans the desktop for the captured visual area and clicks on it when found… pauses only until the click target is found… no static wait times needed." Window positions/sizes tracked at record time and restored at playback.
- Action catalog (from doc TOC): mouse (click, SmartClick, move, wheel, AI object search), keyboard (keypress, hotkey, text output, phrase insertion), wait functions (time, until time, hotkey press, text input, file event, pixel color change, change on desktop), find image on screen / OCR text on screen, capture (screenshot, OCR, barcode/QR, webpage scraping), AI (text processing, image analysis, image generation; OpenRouter/OpenAI/Anthropic/Ollama settings), variables (create, calculation, lists, save to file/clipboard), control functions (window focus, execute program, embed another macro, Goto, Repeat, If-Then-Else).
- Playback machinery: speed, repetitions, filter, mouse-path smoothing, post-playback actions; triggers via hotkey or text shortcut (via companion PhraseExpress) and scheduled playback (Windows Task Scheduler integration); popup menu launcher.
- Editing/debugging: action list with labels, comments, groups, search & replace, line numbers; overlays visualizing recorded mouse paths; debugging tools (notification, message box, beep, Variable Explorer, breakpoints, disabling actions).
- Files: load/save macros; export as macro file; export to CSV; export to PhraseExpress; command-line parameters.
- Sharing (with PhraseExpress): tree-structured macro organization, network sharing, popup launch, central licensing.
- macOS: "Important macOS settings / Troubleshooting macOS system permissions" sections — same accessibility-permission structural constraint.
- Vendor-specific detail (L3): ScreenGrasp/AI provider settings, game-optimization mode, mouse-delta recording settings, QR/barcode capture.

---

## Cross-product Comparison

| Dimension | Power Automate desktop flows | AutoHotkey | Keyboard Maestro | Apple Automator | Macro Recorder |
|---|---|---|---|---|---|
| Core artifact | desktop flow | script (.ahk) with hotkeys/hotstrings | macro | workflow | macro (recorded step list) |
| Authoring | visual action library + recorder | writing scripts (any editor) | GUI macro design (vendor claim; details unverified) | action library + record-action + script actions | record → edit step list (no code) |
| Scripting escape hatch | script actions; custom actions; expressions | the whole product is a language | unverified | Run Shell/AppleScript/JavaScript actions | none (no-code by design) |
| Manual invocation | console/designer run; URL/desktop shortcuts | running the script; hotkeys | "trigger them at any time" (claim) | Run button; Quick Action menus | Play button |
| Hotkey trigger | keyboard shortcuts per user/machine | primary mechanism (documented in depth) | implied by "trigger at any time"; unverified | not in fetched pages | hotkey trigger (via docs/companion) |
| Schedule | via cloud flows (enterprise layer) | not evidenced | unverified | not evidenced | Task Scheduler integration |
| Event/context triggers | cloud-flow events (enterprise layer) | #HotIf context conditions; dynamic hotkeys | unverified | not evidenced | in-flow waits (file, pixel, desktop change) |
| Input simulation | yes (recorder + Send-class actions) | yes (Send) | yes (implied by accessibility needs) | recording exists, but core is app actions | yes (core mechanism) |
| App/OS action mechanisms | UI-element actions (accessibility frameworks), Excel/folder actions | window/control functions, window messages, DllCall | Select Menu by Name, Create Calendar Event (named actions) | app-provided actions (Library grouped by app) | window focus, execute program, embed macro |
| Targeting machinery | UI elements pane, images, coordinates; UIA/MSAA modes | Window Spy (title/class/control), ClassNN, pixel | unverified | app-action parameters | visual-context SmartClick, image find, OCR, pixel color, anchors |
| Variables | yes (pane, types, % notation, scoped) | full language | unverified | variables + loop action | yes (calculation, lists) |
| Conditionals/loops | buildable actions (not recordable) | language-level | unverified | loop action | If-Then-Else, Repeat, Goto |
| Reliability waits | "wait for action" during recording; error handling per action | WinWait-class functions | unverified | per-action runtime prompts | dedicated wait-function family |
| Debugging | enable/disable actions; error handling; run history; video logs (unattended) | main window (lines, vars, hotkeys, key history) | unverified | Log area, checkmarks, View Results | breakpoints, Variable Explorer, disable actions |
| Share/distribute | share/export flow; custom actions; org accounts | script files; compile to .exe; community scripts | unverified | saved workflows; import into Shortcuts | macro files; CSV; companion-app sharing; network sharing |
| OS permission gating | elevation mode documented (TOC) | UI Access builds for elevated windows | Accessibility permission (named processes) | not in fetched pages | macOS permission troubleshooting |
| Execution locus | the local machine; attended/unattended modes; PiP runs | resident runtime in tray | local machine + engine | local machine (OS-native) | local machine foreground playback |
| AI assistance | Copilot suggested actions | none evidenced | Apple Text Recognition support | none evidenced | AI actions + AI settings |

### What is stable across the sample (evidence layer B)

1. The core artifact: a named, persistent, user-authored automation — a stored sequence of actions (recorded, assembled, or written) that can be run repeatedly. All five.
2. Local execution on the user's own machine, acting on that machine's desktop environment (apps, windows, input, files, OS). All five; every product's value proposition is "automate tedious things on your Mac / workstation / computer."
3. Triggered invocation, with direct manual invocation universal and the global hotkey as the signature trigger (documented in depth in three products; vendor-claimed in a fourth). Schedule and event triggers appear where products document them but are not universal in the sample.
4. A step/action granularity: automations decompose into individually addressable, editable, disable-able actions — in visual products as step lists and in the script product as statements/hotkey bodies.
5. Reliability machinery targeting a mutable GUI: element-based targeting (accessibility/selectors/control IDs), image/OCR/visual-context targeting, coordinate fallback, window-state restoration, and waits for conditions. Present in every product that documents execution (all five, in different mixes).
6. An editing/debugging loop: recorded/built automations are expected to be edited; every product provides inspection surfaces (logs, variable views, enable/disable, breakpoints).
7. Reuse and transfer of automations as artifacts: export/import, files, compiled executables, companion-app sharing. All five.
8. OS-level permission/elevation gates as a structural consequence of input-injection/control (macOS Accessibility, Windows UI Access/elevation). Documented in four of five (Automator's pages don't cover it; macOS gate evidenced by the other two macOS products).
9. Both authoring families coexist or cross-pollinate: visual products embed scripting (Automator, PAD) or recording (PAD, Automator, MR); the script product is context-conditioned and GUI-aware (AHK). No product is purely one mechanism.

### Common but not defining (L1 candidates)

- Recorder (3 of 5 document it directly; absent by design in the script pole).
- Scheduled execution (2 of 5 directly evidenced; likely more, not claimed).
- Web/browser automation inside the desktop tool (2 of 5 direct).
- Text expansion / typed-abbreviation automation (1 direct, AHK hotstrings; phrase insertion in MR; historically a sibling micro-category).
- AI assistance (2 of 5; era-common trend).
- Team/organizational sharing posture (2 of 5).

### Variant, era, or positioning dependent (L2 candidates)

- Authoring philosophy: script-first vs GUI-first vs recorder-first (audience/skill variant; the deepest split in the Type).
- Platform-native bundling (OS ships the automation app — Automator; convergence into Shortcuts).
- Attended vs unattended execution; machine registration; cloud-flow orchestration (the RPA-convergence edge — PAD).
- Cloud-service connectors mixed with desktop actions (PAD connector actions; MR web scraping).
- Depth of app-specific integration (named app actions vs generic input injection).

### Vendor-specific (L3 — kept out of the final document)

- PAD: UIA/MSAA capture modes, Copilot suggested actions, video logs, work queues, hosted machines, 2 MB input limit, 70 runs/min, % notation, PiP runs, IME handling.
- AHK: Window Spy, hotstring option grammar, launcher/version detection, UI Access builds, 40-char/~5000-char limits, AutoCorrect script.
- KM: Engine process split, command-line tool, Security preference pane, Pushover action, named feature set.
- Automator: Quick Action type, Services menu, Shortcuts import, Script Editor dictionary.
- MR: SmartClick, PhraseExpress integration, AI provider settings, game optimizations, QR/barcode capture.

---

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

A Desktop Automation Application is recognizable by four properties:

1. **User-authored automation artifact** — a named, persistent sequence of actions (or script) that the user defines through the application — recorded, assembled from an action library, or written — and that is reusable across runs.
2. **Local execution engine** — the application itself runs that artifact on the machine where it resides.
3. **Desktop as the object of automation** — the actions act on the local machine's environment: installed applications, windows, keyboard/mouse input, files, or OS functions (as opposed to only remote cloud services).
4. **Triggered invocation** — the artifact runs when invoked: the baseline is direct manual invocation, with hotkey/schedule/event/context triggers as the common mature extensions.

Negative-space discriminator (same family of mechanism, different Type when removed): the automation is owned and operated on the user's machine for the user's own work. Remove that (central bot-fleet management as an organizational asset) → Robotic Process Automation Platform. Remove human-designed determinism (a model decides each action at runtime from live observations) → Agent Tool / Computer-use Platform. Remove the local surface (automation binds cloud services together) → Personal Workflow Automation Platform. Remove the "do the user's work" job (assert expected behavior of software under test) → Test Automation Platform.

### L1 — Common Mature Structure

- recorder (capture user actions into the artifact)
- visual step/action editor with per-step parameters (where the philosophy allows)
- global hotkey triggering; manual run surfaces (console, menu items, tray)
- variables; conditionals and loops (depth varies from spreadsheets-of-values to a full language)
- targeting machinery: UI-element selectors, image/OCR matching, coordinates, window-state restoration, wait-for-condition
- standard action families: window management, keyboard/mouse, files/folders, clipboard, text, dialogs/notifications, program launch
- editing/debugging: enable/disable steps, logs/run history, variable inspection
- import/export/share of automations (files, exports, compiled executables, team sharing)
- OS permission/elevation gating surfaces (accessibility permissions, elevated-window workarounds)

### L2 — Variant / Optional Structure

- authoring philosophy as market segment: script-first (enthusiasts) / GUI-first (prosumers) / recorder-first (consumers) / OS-native visual (everyone)
- platform-native bundling and convergence (OS vendor ships it; older surfaces migrate into newer OS-native ones)
- web/browser automation; image/OCR-based automation for uncooperative apps
- text expansion (typed abbreviations → text or actions)
- AI assistance (suggested actions, AI processing steps)
- cloud-service connectors / hybrid cloud+desktop packaging
- attended/unattended posture, machine registration, organization accounts (RPA convergence edge)
- team sharing / network deployment / central administration

### L3 — Vendor-specific

See Vendor-specific list above; stays in Research Notes.

---

## Vendor-specific Findings

(See per-product L3 lists. Notable structural observations worth keeping for boundary work:)

- PAD self-describes as "broadening the existing RPA capabilities" — the vendor itself frames desktop flows as the personal/local layer of an RPA stack. This supports treating the enterprise orchestration layer (machines, groups, unattended licensing, work queues, governance) as an optional extension, not the Type's core.
- AHK's docs acknowledge AutoIt (1999) as direct ancestor — the Type has an unbroken 25+ year scripting lineage on Windows.
- Automator's Shortcuts import shows OS vendors consolidating legacy automation surfaces into platform-native ones — the Type persists under new names.
- MR lists "software test automation" as a use case of the same mechanism — mechanism overlap with Test Automation is real and acknowledged by vendors themselves; the Types are distinguished by job, not by mechanism.

## Rejected Findings

- "Desktop automation is a Windows category" — rejected: macOS-native products (Automator, Keyboard Maestro, Macro Recorder for Mac) satisfy the same model; so would any platform with resident automation tooling.
- "The Type is defined by record-and-replay" — rejected: the script-first product has no recorder in its core docs, and the OS-native product's primary mechanism is an action library; recording is one authoring mechanism among three.
- "The Type is defined by input simulation" — rejected: multiple products automate through app-provided actions, accessibility-element actions, and scripts without simulating raw input; input simulation is the most common mechanism, not the definition.
- "Cloud/event scheduling is definitional" — rejected: local-only products with manual/hotkey triggers remain full instances of the Type; scheduling evidence in the sample is product-specific.
- "AI-driven behavior is part of the Type" — rejected: AI appears as an authoring aid (suggested actions) or as callable processing steps; runtime decisions remain deterministic and human-designed. Model-decided runtime action is the neighboring computer-use Type.
- "This is just personal RPA" — rejected as a definition (RPA's organizational machinery is not required), accepted as a market-convergence observation at one product's edge.

## Boundary Findings

1. **vs Robotic Process Automation Platform (§10, unprocessed).** Same mechanism family (human-designed deterministic automations). Discriminators: organizational scale and central management — RPA adds bot-fleet orchestration (central deployment, unattended farms on servers/VMs, queues, licensing, governance) as the primary structure; desktop automation keeps the automation owned and operated on the user's machine. PAD is the bridge product: its local designer + local desktop runtime is this Type's core; machines/machine-groups/unattended/cloud orchestration is the RPA layer bolted on. **Flag for joint review when robotic-process-automation-platform is processed** (consistent with the flag raised by the agent-tool-computer-use-platform pass).
2. **vs Agent Tool / Computer-use Platform (§13, processed).** Boundary answered from this side: the discriminator is who decides each action at runtime — here, a human-designed deterministic sequence fixed at authoring time; there, a model deciding from live observations. Observed support: desktop-automation products embed AI only as an authoring aid or processing steps, never as the runtime decision-maker. Mechanism-level boundary holds; no merge.
3. **vs Personal Workflow Automation Platform / No-code Personal Automation Application (§03.16 siblings, unprocessed).** Hypothesis from this pass: the discriminator is the target surface — cloud-service-to-cloud-service orchestration vs acting on the local desktop. The same vendor (PAD) ships both surfaces as two flow types in one product, supporting a surface-level, not vendor-level, boundary. **Flag for joint review when the sibling leaves are processed.**
4. **vs Test Automation Platform (§12).** Same GUI-driving mechanisms (record, replay, element/image targeting); different job and artifact — doing the user's own work vs asserting expected behavior of software under test; test artifacts carry assertions/suites/CI semantics. MR's own "software test automation" use-case page confirms the overlap is real but intent-defined. Distinct Types; boundary is the job.
5. **vs Code Editor / scripting runtimes (§12).** The script-first product is a language + resident runtime whose *purpose* is desktop automation (hotkeys, hotstrings, window control, targeting inspector). What makes it an instance of this Type is the purpose + the resident automation runtime (tray, hooks, hotkey engine), not the existence of a language. General-purpose languages/shells without that purpose are not this Type. Conversely, visual products embed script actions without becoming code editors. Boundary holds; note the dual-membership risk for tool-shaped products.
6. **Pure recorder products and text expanders are in-Type variants, not separate Types** — recorder-first is an authoring-philosophy variant; text expansion appears as a capability (hotstrings, phrase insertion) inside desktop automation products, though a pure text expander with no other automation may be a narrower adjacent product. Noted for the record; no directory change proposed.

## Historical / Market-Sample Check (per §24 check)

- Would older products fit the definition? Keyboard-macro utilities of the 1980s–90s (resident macro programs with recorded or built action sequences fired by hotkeys), the DOS/Windows macro-recorder generation, and the AutoIt (1999) → AutoHotkey (2000s) script lineage all satisfy the L0 properties: user-authored action sequences, local execution, desktop targets, triggered invocation. Nothing in the definition requires cloud, AI, modern UI, or even a GUI builder.
- Platform-native: Automator (2005-era) and its Shortcuts successor satisfy it as OS-native instances; the Shortcuts-import evidence shows OS vendors converging older surfaces rather than the Type disappearing.
- Regional: regional macro/automation utilities (known to exist in several markets) fit the same structure; none were fetched this pass, so no region-specific claims are made.
- Check conclusion: the definition does not overfit to the modern low-code/cloud/AI implementation. The one historical skew to abstract away: older products were hotkey-centric — the invariant is "triggered invocation," with hotkeys as the common (not defining) trigger.

## Uncertainties

1. Keyboard Maestro structure (triggers, macro groups, variables, palettes) — manual wiki unreachable (404 ×2); only product-site claims available. KM-specific claims in the final document are limited accordingly.
2. Purely-local scheduling inside PAD (without the cloud layer) — not verified this pass; scheduling evidence is attributed specifically (PAD via cloud flows; MR via OS Task Scheduler integration).
3. AutoHotkey scheduling — not evidenced in fetched pages; not claimed.
4. Automator's full workflow-type list (beyond Quick Action) — not enumerated in fetched pages; not claimed.
5. Macro Recorder production-version docs differ from the beta TOC used; structural claims safe, version-specific details withheld.
6. Apple Shortcuts-for-Mac trigger model — not fetched; the OS-native trigger story rests on Automator's guide only.
7. Market-structure breadth (e.g., Linux equivalents, enterprise desktop-management suites with macro features) — not researched; the Type definition is expected to generalize but only the sampled five plus historical reasoning support it.

## Final Synthesis

A Desktop Automation Application is a personal-scale automation tool for one's own computer. Its defining core is small: a user-authored, persistent automation artifact (sequence of actions or script); a local execution engine; the local desktop environment as the object of automation; and triggered invocation (manual baseline; hotkey/schedule/event as common extensions). Everything else that makes modern products feel different — recorder vs visual builder vs script, waits and image targeting, variables and control flow, export and sharing, AI assistance, web automation, OS-native bundling, and the enterprise RPA layer — is standard capability or variant, not definition. The mechanism family is shared with RPA (same human-designed deterministic automations, different ownership/management scale), with computer-use agents (opposite runtime decision-maker), with cloud workflow automation (different target surface), and with test automation (different job) — all four boundaries are mechanism/surface/job-level and hold against the sampled products. The Type is old, stable, and converging at its edges (RPA suites, OS-native automation, AI assistance), but the personal-tool core has not moved in three decades.
