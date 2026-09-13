# Research Notes — Integrated Development Environment / IDE

Leaf: `Integrated Development Environment / IDE` (Section 12 — Software Development & Product Engineering)
Slug: `integrated-development-environment-ide`
Research date: 2026-09-08

---

## Research Goal

Understand what makes an Integrated Development Environment a distinct Application Type — not a bigger text editor, not a build tool, not a debugger — by studying how real products organize the edit→build→run→debug work of software development inside a single application, and how that organization differs from neighboring Types already processed in this directory (Code Editor, Cloud IDE, Debugger, AI Coding Assistant, AI Coding Agent, Embedded / Firmware Development IDE, Database IDE, Dev Container Workspace Platform).

## Initial Boundary

Working hypothesis before research:

- Core purpose: software developers write, build, run and debug programs inside one application, organized around a project that defines the code being developed.
- Likely users: professional and student software developers.
- Nearest neighbors: Code Editor (editing without a first-class project/build model), Cloud IDE (same loop, remote-managed compute), Debugger / Build Automation System / Profiler (component Types the IDE integrates), Embedded / Firmware Development IDE (the same loop bound to non-host hardware), AI Coding Assistant / Agent (capability overlays).
- Key unknowns: (1) is the project container a defining invariant or merely the dominant modern implementation? (2) is integrated debugging required for Type membership, given historical/debugger-less poles? (3) how does the boundary hold against modern code editors that host build tasks and debuggers via extensions?

## Research Questions

1. What is the core object model? What exactly is a "project" in each product, and what attaches to it?
2. Which capabilities are integrated (editor, build, run, debug, test, VCS, terminal, profiler) and how do they interoperate?
3. What is the canonical interaction loop (create/open project → edit → build → run → debug → repeat)?
4. How do IDEs handle build tools they don't own (Gradle/Maven/MSBuild) — replace, wrap, or delegate?
5. What is the debugging experience and how does runtime state map back to source?
6. What distinguishes an IDE from a code editor that hosts build tasks + debugger extensions?
7. What varies by language family, platform, licensing, extensibility model?
8. How do older products (1990s–2000s generation) fit the definition?

## Representative Products

| Product | Why sampled | Evidence layer |
|---|---|---|
| IntelliJ IDEA | Market-leading commercial JVM-family IDE; project-model-centric philosophy; deep help docs | A |
| Visual Studio (Windows) | Canonical full IDE; solution/project model; Microsoft's own IDE-vs-editor boundary statement | A |
| Eclipse IDE | Open-source platform IDE; workspace/project model; the extensible-platform pole; lineage still shipped | A (product-level) |
| Xcode | Platform-native IDE bound to Apple SDKs/hardware; different customer pole | A (product-level) |
| Visual Studio Code | Boundary witness — sampled by the code-editor pass; official docs used here only to draw the IDE/editor seam | A (boundary) |

Coverage check: commercial vs open source, language-family vs platform-native vs polyglot, project-model-rich vs folder-mode, three different vendors + a foundation-hosted project, plus one deliberate out-of-Type witness. Stop condition satisfied after 5 products: new evidence repeated existing patterns.

## Sources

Tier 1 (official operational documentation, fetched 2026-09-08):

- IntelliJ IDEA Help — "IntelliJ IDEA overview" — https://www.jetbrains.com/help/idea/discover-intellij-idea.html
- IntelliJ IDEA Help — "Projects" — https://www.jetbrains.com/help/idea/creating-and-managing-projects.html
- Microsoft Learn — "What Is Visual Studio?" (Visual Studio IDE overview) — https://learn.microsoft.com/en-us/visualstudio/get-started/visual-studio-ide?view=vs-2022
- Microsoft Learn — "What Are Visual Studio Solutions and Projects?" — https://learn.microsoft.com/en-us/visualstudio/ide/solutions-and-projects-in-visual-studio?view=vs-2022
- VS Code Docs — "Debug code with Visual Studio Code" — https://code.visualstudio.com/docs/debugtest/debugging (boundary witness)
- VS Code Docs — documentation index (section map) — https://code.visualstudio.com/docs

Tier 2 (official product pages, fetched 2026-09-08):

- Eclipse IDE and platform — https://eclipseide.org/ ; Eclipse Foundation IDE topic page — https://www.eclipse.org/ide/
- Xcode — Apple Developer — https://developer.apple.com/xcode/

Source-access limitations:

- Eclipse help.eclipse.org topic-level documentation (workbench/workspace/project concepts) was not fetched; Eclipse observations rest on the official IDE/platform product pages and release notes surfaced there. Eclipse-specific claims are therefore held at product-page strength.
- A historical sample fetch (Wikipedia, Turbo Pascal) timed out and was abandoned per the retry rule; the historical check is kept conceptual (see Historical / Market-Sample Check) with no precise version-level claims.

---

## Product Observations

### IntelliJ IDEA (JetBrains)

Evidence layer A unless noted.

- Self-description: "an Integrated Development Environment (IDE) for professional development in Java and Kotlin"; cross-platform; plugins extend it to polyglot; it is a "superset" of the JetBrains sibling IDEs (PyCharm, WebStorm, PhpStorm, GoLand, CLion, DataGrip functionality available via bundled language plugins).
- **Project definition (key evidence)**: "a project is the top-level container for everything you work on: source code, tests, libraries and SDKs, build instructions, and your personal settings. A project defines the scope of your work. It tells the IDE which files belong together, how they are built and run, and which settings apply to them." A project groups one or more **modules** (e.g. backend service + frontend app sharing one SDK). Two storage formats: file-based (.ipr/.iws/.iml — outdated) and directory-based (.idea directory + .iml — default, VCS-friendly).
- Editor-centric UI; "follows your context and brings up the necessary tools automatically"; tool windows; configurable layout/colors/keymaps.
- Navigation/search across the whole project: Search Everywhere, go to file/class/symbol/declaration, recent files/locations, file-structure popup.
- Coding assistance: context-aware completion (basic; type-matching "smart"; ML-based full-line), automated **refactorings with project-wide effect** ("when you rename a class, the IDE will update all references to this class throughout your project"), inspections (built-in static analysis) with quick fixes, intention actions, code generation from templates.
- **Debugger**: "built-in JVM debugger" — suspend execution via breakpoints (multiple types, conditions, filters), step through execution, examine variable values, call stacks, thread states, modify values, evaluate expressions.
- **Build tools**: "fully functional Gradle and Maven integration" — opening/creating such a project auto-detects and downloads required repositories/plugins; build files edited in the IDE with automatic sync of configuration changes. (IDE wraps external build systems rather than replacing them.)
- Version control: Git, Mercurial, Perforce, Subversion — history, compare, branches, GitHub pull requests in-IDE. Local History: private revision tracking even without VCS.
- Other integrated tools: profiler (Java Flight Recorder + Async Profiler), built-in terminal.
- Extensibility: JetBrains Marketplace plugins.

### Visual Studio (Microsoft, Windows)

Evidence layer A unless noted.

- Self-description: "a powerful integrated development environment (IDE) for Windows where you can **develop, build, debug, test, and deploy your apps, all in one place**." Overview diagram: develop → build → debug → test → deploy cycle. "Visual Studio includes compilers, code completion tools, source control, extensions."
- **Boundary statement (key evidence)**: "Visual Studio is available for Windows. For a lightweight, cross-platform **code editor**, see Visual Studio Code." Microsoft's own docs separate the IDE from the code editor.
- **Solution/project model (key evidence)**: "When you create an app or website in Visual Studio, you start with a *project*. A project contains all files that are compiled into an executable project, library, or website… A project also contains compiler settings and other configuration files." Project file is an MSBuild XML document (.csproj/.vbproj/.dbproj…) containing "all the information and instructions that MSBuild needs to build your project." A **solution** is "a container for one or more related projects, along with build information, Visual Studio window settings, and any miscellaneous files" (.sln + hidden .suo). Solution Explorer is the primary management surface (build project, manage packages, add reference, run tests from context menus).
- **Counter-case recorded**: "You don't have to use solutions or projects in Visual Studio to edit, build, and debug code. You can simply open the folder that contains your source files" (Develop code without projects or solutions — an official alternative mode).
- Workload-based installer (install only needed components); editions Community (free, students/OSS/individuals), Professional, Enterprise.
- Develop: editor with light-bulb quick fixes, outlining; Solution Explorer / Class View navigation; AI assistance (GitHub Copilot completions/chat, IntelliCode) throughout.
- Build: "compile and build your applications to create builds right away and test them in a debugger"; multiprocessor builds; custom/built-in build configurations; warning/output configuration.
- Debug: "integrated debugging… step through your code and look at the values stored in variables, set watches on variables to see when values change, and examine the execution path."
- Test: unit testing tools, code-coverage-style analysis claims at overview level.
- Version control: integrated Git — clone, branch, commit, push, resolve conflicts, review pull requests.
- Deploy: publish to web/Azure, network share, or local folder.

### Eclipse IDE (Eclipse Foundation)

Evidence layer A at product-page strength; deep help topics not fetched (see limitations).

- Official pages position "Eclipse IDE and platform" as "Open, industry-backed, and community driven"; free and open source under EPL 2.0; released on a simultaneous-release train (2026-06 observed; next 2026-09).
- "Support for Latest Java — Supports Java 26 and provides the necessary tooling for development" → the IDE bundles language tooling for its family language.
- "Improved Java Development Tooling — Better **debugging** through statement-level step filtering and byte code instruction highlighting, improved **watch expression** creation with correct evaluation context from **variables view**…" → integrated debugging as core JDT function.
- "Proven Extensibility — Features a huge variety of platform plugins… check the marketplace." Marketplace is a first-class distribution surface.
- **Platform-as-base evidence**: testimonials — Renesas has "been using the Eclipse IDE platform and C/C++ Development Toolkit for many years as the basis of our own IDE product"; Sigasi "built our flagship Sigasi Studio IDE on the Eclipse platform"; VMware/Broadcom ships Spring Tools as extensions for Eclipse. → the IDE as an extensible platform that downstream products build on.
- Ecosystem context from the Foundation page: Eclipse Platform, Theia (cloud/desktop framework), Open VSX registry; separate working groups for the IDE and cloud devtools.

### Xcode (Apple)

Evidence layer A at product-page strength; Xcode docs topics not fetched.

- Self-description: "Xcode offers the tools you need to **develop, test, and distribute apps for Apple platforms**, including predictive code completion… advanced profiling and debugging tools, and simulators for Apple devices."
- Platform-native binding: predictive completion "powered by Apple silicon — uses an on-device machine learning model trained for Swift and Apple SDKs"; Simulator for prototyping across Apple devices/OS versions; Instruments profiler (CPU/disk/memory/GPU tracks); Organizer for managing the app "from start to finish — including testing, debugging, building, and deploying."
- **Debugger (key evidence)**: "The Xcode debugger provides a clear look into your app's behaviors. You can **pause execution at specified breakpoints, inspect memory**… and **monitor variables** to identify when their values change."
- Previews: visualize SwiftUI/UIKit/AppKit views in a preview canvas; selecting a control highlights the corresponding source line (bidirectional UI↔code correspondence).
- Distribution/CI: Xcode Cloud — "continuous integration and delivery service built into Xcode" (an adjacent cloud service reached from the IDE).
- AI posture: coding intelligence with "the large language model of your choice, including… Anthropic and OpenAI" plus coding agents (Xcode 26.3/27 era).

### Visual Studio Code (boundary witness — not a sample member)

Evidence layer A. Sampled by the code-editor pass (2026-09-07); used here only to draw the seam.

- Microsoft Learn classifies it: "a lightweight, cross-platform **code editor**" (on the Visual Studio IDE page).
- Debugging doc: VS Code "has built-in support for JavaScript, TypeScript, and Node.js debugging"; other languages/runtimes require **debugger extensions** from the marketplace (PHP, Ruby, Go, C#, Python, C++, PowerShell listed); debug behavior is defined by the debug extension ("Remote debugging is a feature of the debug extension you are using").
- Debug configuration is a per-project JSON file (`launch.json`); "For simple applications, VS Code tries to run and debug the currently active file." Tasks (`tasks.json`) run external build tools (Gulp, Grunt, Jake named) and surface errors/warnings.
- Full debug-session UI exists (breakpoints incl. conditional/triggered/inline/function/data/logpoints, call stack, variables, watch, debug console REPL, multi-target) — i.e., the editor hosts a complete debugger *front end*, with the engine contributed per-language by extensions.
- Interpretation: the working set remains file/folder-centric ("lightweight human-readable wrapper over folders" per the code-editor pass); build/run/debug plumbing is generic and delegated (tasks + debug-adapter extensions), not a first-class project model with native tool integration. This is the documented IDE-adjacent variant of the Code Editor Type, not the IDE Type.

---

## Cross-product Comparison

| Aspect | IntelliJ IDEA | Visual Studio | Eclipse IDE | Xcode | VS Code (witness) |
|---|---|---|---|---|---|
| Self-label | IDE (Java/Kotlin) | IDE (Windows) | IDE / platform | "tools to develop… Apple platforms" | code editor (per MS) |
| Project container | Project → modules; .idea/.iml; scope + build/run + settings | Solution → projects; MSBuild project file; folder-mode alternative | Workspace → projects (platform model; product-page strength) | Project (+ platform binding) | Folder/workspace = lightweight wrapper |
| Build | Gradle/Maven fully integrated, auto-sync from build files | MSBuild under IDE control; build configurations | JDT language tooling | build for Apple platforms; Simulator run | external tools via tasks |
| Run | run configurations | run/deploy targets | run configurations | Simulator/device run | F5 / launch.json |
| Debug | built-in JVM debugger (breakpoints/conditions, stepping, variables, call stacks, threads, evaluate) | integrated debugger (step, variables, watches, execution path) | JDT debugging (step filtering, watch expressions, variables view) | integrated debugger (breakpoints, memory, variable monitoring) | built-in JS/TS/Node only; else per-language extensions |
| Language intelligence | completion (incl. ML full-line), project-wide rename, inspections+quick fixes, intentions | quick fixes, outlining, Copilot/IntelliCode | JDT tooling | predictive completion trained for Swift/SDKs | IntelliSense, refactoring |
| VCS integrated | Git/Hg/Perforce/SVN + PRs | Git + PRs | via platform/team tooling | platform-level | built-in |
| Extensibility | Marketplace plugins; superset packaging | Extensions + Marketplace; workload installer | Marketplace; platform reused by downstream IDEs | closed platform; model choice for AI | extension marketplace |
| Extra integrated | profiler, terminal, local history | test tools, deploy/publish | — | Simulator, Instruments, Organizer, Previews, Xcode Cloud tie-in | terminal, browser, port forwarding |

Findings:

- **The project is the organizing unit in every IDE sample** and is described by vendors as the thing that tells the environment "which files belong together, how they are built and run" (IntelliJ's own definition; Visual Studio's project = "all files that are compiled into an executable… plus compiler settings"; Eclipse workspace/project; Xcode project). Evidence layer B.
- **Build/run/debug are integrated in every IDE sample** and are the activities the vendors name first (Visual Studio: "develop, build, debug, test, and deploy… all in one place"; IntelliJ: "integrates the essential developer tools and lets you debug, analyze, and version… from within the IDE"; Xcode debugger described in its overview). Evidence layer B.
- **Build machinery is often external but operated from within** (Gradle/Maven/MSBuild). Integration ≠ ownership; the invariant is operation-from-within against the project, not a proprietary compiler. Evidence layer B.
- **Debugging is universally present in mature IDEs** across the sample and across the 2000s generation (Eclipse lineage). No counter-case inside this sample. The only debugger-less poles on record are outside this Type's center: early compiler-only environments (historical, weak evidence) and maker-tier embedded IDEs (recorded in the embedded-firmware pass). Evidence layer B with boundary qualification.
- **The IDE/editor seam is vendor-acknowledged**: Microsoft separates Visual Studio (IDE) from VS Code (code editor) in its own documentation; the code-editor pass independently holds "build tasks + debugger integration" as an IDE-adjacent variant. Two independent lines agree. Evidence layer B.
- Extensibility, VCS integration, integrated terminal, testing, profiling are common but not uniform in depth — common mature structure, not defining. Evidence layer B (extensibility)/A-B (others).

---

## Canonical Model

### L0 — Defining Invariant (deliberately small)

An IDE is one application in which editing, building/running and debugging a program happen **together, bound to a shared project scope**. Four jointly-held structures:

1. **The project as first-class organizing context** — a persistent working context that defines which code belongs together and how it is built and run; the unit to which build/run/debug configurations and language services attach. Realized as project/solution/workspace structures; in degenerate historical form, the single loaded program file served as the scope.
   Remove → the working set is files/folders with no first-class project semantics → Code Editor territory.
2. **Scope-bound integrated editing** — a code editing environment whose assistance is computed against the project's model: project-wide navigation, cross-file operations (e.g. rename following references), project-scoped diagnostics.
   Remove → editing is file-local → plain editor.
3. **Integrated build/run from within** — the application compiles and/or launches the program it edits from inside the same application, with results/diagnostics mapped back to code; where the toolchain is external (build tools, SDK compilers), it is integrated and operated from within, not replaced.
   Remove → editor + separately operated toolchain → Build Automation System / external tools.
4. **Integrated debugging with source correspondence** — the application launches or attaches the program under debugger control from within, mapping runtime state (breakpoints, stepping, variables, call stack) back to the edited source in the same environment.
   Remove → editor + build/run without debugging, or a separate debugger tool → Debugger (standalone Type).

Jointly-held is load-bearing:

- 1 alone = project/build file formats with no environment.
- 2 alone = code editor.
- 3 alone = build automation.
- 4 alone = standalone debugger.
- 1+2 without 3+4 = an editor with a project file (code editor with project support).
- 2+3 without 1 = folder + tasks editor (the documented IDE-adjacent code-editor variant).
- 1+3 without 2+4 = headless project/build configuration.
- 2+4 without 1+3 = editor hosting a debugger front end (the boundary-witness pattern).

Honest qualification on leg 4: every sampled IDE and the whole mature generation of the Type integrate debugging; however, historically and at the maker tier, debugger-less environments have still been recognized as IDEs (see Historical check). Leg 4 is therefore held inside L0 as the canonical loop's third stage while the counter-case class is explicitly recorded; if a future pass finds debugger-less generic IDEs to be a substantial population, leg 4 should be demoted to the top of L1.

### L1 — Common Mature Structure

Present across the sample; expected by the market; not required for recognition:

- language intelligence: completion (including ML-assisted in the current era), go-to file/symbol/declaration, project-wide search
- automated refactorings with project-wide effect (rename, extract, inline)
- static analysis in the loop: inspections/errors surfaced as problems with quick fixes
- project explorer/tree as the primary structural view; editor-centric layout with tool windows (problems/output, terminal)
- run/debug **configurations**: named, per-project setups for launching
- version control integration (status, commit, branches, history; pull requests in two samples)
- integrated terminal
- testing integration (run tests from within the IDE; Visual Studio and Xcode name test tooling on their overview surfaces)
- extension/plugin ecosystem with a marketplace (3 of 4 samples; Xcode is the closed-platform pole)
- profiler integration (IntelliJ, Xcode)

### L2 — Variant / Optional Structure

- **Language-family specialization** (Java/Kotlin, .NET, Swift/Apple SDKs) vs polyglot general IDEs; sibling IDEs sharing one platform (IntelliJ "superset" packaging; Eclipse CDT/C/C++ toolkits).
- **Platform-native binding**: the IDE as the only first-class gateway to a platform's SDKs, simulators, signing and distribution (Xcode; Android Studio-class equivalents).
- **Open platform posture**: the IDE (Eclipse) reused as the base for third-party commercial IDEs and toolkits — an IDE-of-IDEs variant.
- **Loop breadth**: test tooling, GUI/UI designers, previews, profiling, database tools, deployment/publish, cloud CI tie-ins — which of these are integrated varies widely.
- **AI posture**: embedded completion/chat/agents (era-common; capability overlays governed by the AI Coding Assistant / AI Coding Agent Types).
- **Remote/cloud posture**: remote development front ends and cloud-hosted compute — when compute becomes a managed remote workspace, the Cloud IDE Type takes over.
- **Hardware-target loops**: when the build/run/flash loop targets non-host hardware, the Embedded / Firmware Development IDE Type takes over.
- Licensing shape: free/open source, freemium editions, subscription, platform-bundled.

### L3 — Vendor-specific Detail (research notes only)

- IntelliJ: .idea/.iml directory format vs .ipr file format; Local History; intention actions; Search Everywhere; on-device ML full-line completion; "superset of sibling IDEs" edition unification (2025.3).
- Visual Studio: .sln/.suo file split; MSBuild project file schema; Solution Explorer context-menu surface; workload-based installer; default repos location; light-bulb quick fixes; IntelliCode.
- Eclipse: workspace↔project two-level container; simultaneous release train; EPP packages; JDT statement-level step filtering/byte-code highlighting (2026-06); Theia/Open VSX ecosystem; downstream platform users (Renesas, Sigasi, Spring Tools).
- Xcode: Simulator; Instruments; Organizer; Previews with code↔canvas selection correspondence; Device Hub; Xcode Cloud; on-device predictive completion; coding agents with model choice (26.3/27-era).
- VS Code (witness): launch.json/tasks.json machinery; Debug Adapter-based per-language debugger extensions; built-in debugger limited to JS/TS/Node; multi-root workspaces; Workspace Trust.

---

## Vendor-specific Findings

See L3. None promoted to the canonical model. Notably: project *file formats* (.idea/.iml, .sln/.csproj, Eclipse metadata) are implementation, not invariant — Microsoft's own folder-mode counter-case ("you don't have to use solutions or projects to edit, build, and debug") proves the project *semantics* survives even where the project *file* disappears; the invariant is the defined scope with build/run configuration, not any file format.

## Rejected Findings

- "An IDE is defined by a proprietary project file format" — rejected; folder-mode counter-case + directory-based formats + Eclipse workspace semantics vary too much. Abstracted to project-as-scope.
- "An IDE must own its compiler" — rejected; Gradle/Maven/MSBuild delegation is the norm. Abstracted to integrated operation-from-within.
- "An IDE is defined by AI assistance / ML completion" — rejected; era-common capability, absent in the mature generation and uneven today.
- "An IDE is defined by marketplace extensibility" — rejected; Xcode's closed platform satisfies the Type without it; Eclipse's platform-reuse is a variant, not the definition.
- "Integrated debugging is a mere feature" — rejected as a *merely-optional* reading: it is universal in the mature sample and canonical to the loop; but its strict-invariant status is qualified by the historical/maker counter-case class (recorded, watched).

---

## Boundary Findings

1. **vs Code Editor** (processed 2026-09-07) — the central seam. Code editor: file-centric working set ("lightweight human-readable wrapper over folders"), no proprietary project/build artifact required, build tasks + debugger integration held as IDE-adjacent variant. IDE: first-class project with native build/run/debug loop. Corroborated by Microsoft's own product split (Visual Studio = IDE; VS Code = code editor). Convergence pressure is real and bidirectional (editors host debuggers via adapters; IDEs add lightweight folder modes) — the seam is "who owns the build/run/debug loop and what the working set is," not any single feature checkbox. Keep both Types.
2. **vs Cloud IDE** (processed 2026-09-07) — same development loop; seam = locus of compute. Cloud IDE's defining core is a managed remote workspace + client-delivered editing surface + remote execution. The local IDE runs tools and program on the developer's machine. Remote-development front ends and hosted-straddle products noted in the cloud pass; keep separate Types.
3. **vs Debugger / Build Automation System / Profiler / Test Runner** — component Types. The IDE *integrates* these capabilities into the loop; those Types remain where the capability is the whole product (standalone engine/tooling). The debugger pass already resolved IDE-embedded packaging via adapter-protocol separation — consistent.
4. **vs Embedded / Firmware Development IDE** (processed 2026-09-08) — seam = host↔target bridge. That Type's loop is bound to declared target hardware (declare device + cross-build to a target image + flash to target). The generic IDE's loop targets the host (or a general runtime). Embedded IDEs historically share this Type's platform (Eclipse CDT) — platform reuse does not merge the Types.
5. **vs AI Coding Assistant / AI Coding Agent** (processed 2026-09-06) — AI assistance is a capability overlay (plugin or native) inside the IDE loop; the assistant (human-held step loop) and agent (autonomous task loop) are separate Types. All four IDE samples now ship AI features; none are defined by them.
6. **vs Database IDE / SQL Client** (processed 2026-09-07) — a domain-specific development environment whose subject is database connections/schemas/data, not program build/run/debug. Same word "IDE," different Type.
7. **vs Dev Container / Workspace Platform, Developer Environment Manager** (processed 2026-09-08) — environment *provisioning/definition* vs the in-environment *development loop*. An IDE can attach to a provisioned environment (cloud-IDE pass documents this attach layer); provisioning is not the IDE's defining core.
8. **vs Web Development IDE** (sibling leaf, unprocessed) — likely a domain variant of this Type (browser/frontend-targeted tooling over the same project→edit→build→run→debug model). Recommend that pass check its defining structures against this L0 before claiming an independent Type. Recorded as Boundary Issue.
9. **vs Game Engine / Mobile App Development Platform** — broader platform Types whose subject includes runtime content (scenes/assets) or platform delivery; the IDE model is one component inside them. Out of scope here.

---

## Historical / Market-Sample Check

- **Eclipse (2001 lineage, still shipped)**: workspace/projects + language tooling + integrated debugger + plugin marketplace — satisfies all four legs with zero modern machinery (no AI, no cloud, no ML completion). Evidence: official Eclipse IDE pages (product-level strength). ✓
- **1990s–2000s cross-development environments**: the processed embedded-firmware pass recorded that device selection + cross toolchain + device programming (+ emulator debugging) satisfied its core — evidence that the integrated-environment pattern predates all modern packaging. ✓ (cross-referenced, second-hand)
- **1980s integrated compiler environments (Borland-era class)**: full-screen editor + compiler + run command in one program, with interactive debugging appearing across later releases and some eras shipping debugging as a separate product. Kept **conceptual and weak** (the historical fetch timed out; no precise version-level claims made). What this check contributes: (a) the project scope has a degenerate form (the single loaded program file), which is why the invariant is phrased as scope, not file format; (b) a debugger-less pole exists in the Type's lineage — the reason leg 4's strict-invariant status carries an explicit qualification rather than silent confidence. ✓-with-qualification
- **Platform-native + open-platform + commercial poles all satisfy** (Xcode, Eclipse, IntelliJ/Visual Studio) — no era, region or vendor overfit. ✓

---

## Uncertainties

1. Eclipse topic-level documentation (workbench/project concepts in the official help) was not fetched; Eclipse project-model details rest on product-page + platform-reputation strength. Risk: low (Eclipse's workspace/project model is corroborated by the platform-reuse testimonials), but noted.
2. The precise historical boundary of the Type (which 1980s products had integrated debugging and which shipped it separately) is unverified this pass; only the class-level qualification is asserted.
3. The size of the debugger-less generic-IDE population today is unknown; leg 4's status (strict vs demoted-to-L1) is held under watch rather than settled.
4. Xcode documentation was sampled at product-page strength; scheme-level run/debug configuration semantics were not fetched and are therefore absent from all levels (deliberately).
5. Web Development IDE (sibling leaf) is unprocessed; the recommended joint-review question is recorded, not resolved.

---

## Final Synthesis

The IDE is the application form of the edit→build→run→debug loop: a single, editor-centric environment organized around a **project** — a first-class scope that defines which code belongs together and how it is built and run — to which the environment natively binds building/running and debugging, with runtime state mapped back to the edited source. Language intelligence, refactorings, problems/quick fixes, VCS, terminal, testing, profiling and extensibility are the standard capabilities that make the loop productive; they are common mature structure, not the definition. The identity of the Type rests on the joint hold of project scope + scope-bound editing + integrated build/run + integrated debugging: remove any one and the residue is a recognizable neighboring Type (code editor, build system, standalone debugger) rather than an IDE. Vendors converge on this self-understanding ("develop, build, debug… all in one place"; "integrates the essential developer tools… from within the IDE"), and Microsoft's own documentation draws the IDE/code-editor line the same way the cross-product evidence does. Domain- and platform-bound loops (embedded firmware, cloud-hosted compute, databases) are separate Types whose seams are now ratified with the processed siblings.
