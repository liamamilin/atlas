# Research Notes — Profiler

Research date: 2026-09-09

## Research Goal

Understand the **Profiler** Application Type (DIRECTORY §12 Software Development & Product Engineering): what a profiler fundamentally is, what structures every profiler must have, what mature profilers commonly add, where the type's boundaries lie (vs Debugger, APM, Performance Testing, Observability, Static Analysis), and how the modern continuous-profiling variant relates to the classic development-time profiler.

## Initial Boundary (pre-research hypothesis)

- A profiler observes a program **while it executes** and attributes runtime cost (time, memory, other resources) to **code-level units** (functions, call paths, lines, allocation sites), producing an explorable record used to find performance problems.
- Neighbors: Debugger (controls execution vs measures cost), APM / Observability (service health vs code-level attribution), Performance/Load Testing (generates load vs observes one program), Static Analysis (no execution), Distributed Tracing (request-level across services vs function-level within a process).
- Risk: modern "continuous profiling" products might look like an observability sub-type; need to decide whether they are a variant of Profiler or a separate Type.

## Research Questions

1. What is the minimal structure without which a tool stops being a profiler?
2. How does a profiling session begin? (launch under the profiler / attach to a running process / continuous background collection)
3. What is collected? (stack samples, events/markers, allocation records, interval events)
4. What collection methods exist and what are their documented trade-offs? (sampling vs instrumentation vs line-level)
5. What analysis views are standard? (hot spots, call tree, flame graph, timeline, thread view, allocation/heap views, comparison)
6. What resource dimensions do profilers cover? (CPU, wall time, memory, GC, I/O, GPU, async, thread states)
7. What interface shapes exist? (standalone GUI, IDE-integrated, CLI, browser UI, server/web UI)
8. What rules/behaviors materially shape usage? (overhead, statistical nature of sampling, build type, symbol files, snapshot persistence)
9. Where exactly are the boundaries vs Debugger / APM / Load Testing / Observability / Static Analysis?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Slot | Philosophy / tier |
|---|---|---|
| JetBrains dotTrace | language-ecosystem (.NET) profiler, IDE vendor | commercial; sampling-first guidance; standalone + CLI + VS + Rider |
| Microsoft Visual Studio profiling tools | platform IDE profiler (Windows/.NET/C++) | free with IDE; debugger-integrated + post-mortem; broad tool set |
| Grafana Pyroscope | continuous profiling (production) | open-source infra; always-on, low-overhead, server-aggregated |
| Firefox Profiler | browser/web profiler | free, platform-native to the browser; client-side web UI; share-by-link culture |

Rejected/aborted candidates (source-access failures, not product judgments): Chrome DevTools Performance panel (timeouts ×2), Apple Xcode Instruments (JS-gated help pages ×2), Intel VTune Profiler (403 ×2), Android Studio Profiler (timeouts ×2), async-profiler (timeouts ×2). Their absence is recorded as a sourcing limitation; no details were filled from memory.

## Sources

Tier 1 (official operational documentation), fetched 2026-09-09:

- JetBrains dotTrace Help:
  - Introduction — https://www.jetbrains.com/help/profiler/Introduction.html
  - Basics. Profiling Types — https://www.jetbrains.com/help/profiler/Basic_Concepts.html
  - Start Profiling Session — https://www.jetbrains.com/help/profiler/Starting_Local_Profiling_Session.html
  - Analyze Profiling Results in Performance Viewer (Deprecated) — https://www.jetbrains.com/help/profiler/Studying_Profiling_Results__Index.html
  - Compare Snapshots — https://www.jetbrains.com/help/profiler/Comparison.html
- Microsoft Learn, Visual Studio profiling:
  - Overview of the profiling tools — https://learn.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2022
- Grafana Pyroscope documentation:
  - Main — https://grafana.com/docs/pyroscope/latest/
  - Introduction — https://grafana.com/docs/pyroscope/latest/introduction/
  - View and analyze profile data — https://grafana.com/docs/pyroscope/latest/view-and-analyze-profile-data/
  - Configure the client to send profiles — https://grafana.com/docs/pyroscope/latest/configure-client/
- Firefox Profiler (official project repository, end-user docs):
  - README — https://github.com/firefox-devtools/profiler (raw README fetched)
  - Profiler Fundamentals — https://raw.githubusercontent.com/firefox-devtools/profiler/main/docs-user/guide-profiler-fundamentals.md
  - Getting Started — https://raw.githubusercontent.com/firefox-devtools/profiler/main/docs-user/guide-getting-started.md

Unreachable (attempted, abandoned per network rules): developer.chrome.com (timeout ×2), help.apple.com + developer.apple.com Instruments pages (JS-gated ×2), intel.com VTune docs (403 ×2), developer.android.com (timeout ×2), github raw async-profiler README (timeout ×2), profiler.firefox.com/docs (JS app, no static content), firefox-source-docs performance page (pointer only).

## Product Observations

### JetBrains dotTrace (.NET profiler) — evidence layer A

- **Positioning**: "find performance bottlenecks in a variety of .NET applications" (.NET Framework, .NET Core, .NET, Mono, Unity).
- **Forms**: standalone application, console (command-line) tool, integrated in Visual Studio, integrated in Rider. (A)
- **Profiling types** (each a documented collection method with pros/cons): (A)
  - **Sampling** — periodically takes call-stack samples; "accurate measurement of function execution time", small snapshot, lightweight; does NOT measure call counts; not all stacks captured; recommended default ("If you are not sure which profiling type to choose, always start with Sampling").
  - **Tracing** — CLR notifies the profiler on function entry/exit; exact call counts, all non-inlined functions captured; timing distorted proportionally to call counts (documented example: a trivial function called millions of times); heavyweight.
  - **Line-by-line** — measures execution time per statement; requires PDB files; Windows only; "extremely heavyweight"; for narrow deep-dives.
  - **Timeline** — event-based (ETW); call stacks distributed in time plus memory allocation, GC, file I/O events, thread states, await/continuation blocks; used for UI freezes, excessive GC, lock contention, serialized execution.
- **Session start**: Home window → choose run configuration (what to profile) → choose profiling options (how) → Start. **Attach** to running processes (Windows; version-gated). Drag-and-drop attach icon onto the target window. (A)
- **Snapshot model**: profiling produces a **performance snapshot**; snapshots can be saved/opened (`.dtp` files); "getting performance snapshot, detaching the profiler" as session controls; API for automated control. (A)
- **Analysis views**: **Call Tree** (merged calls from all threads; system-call folding; scoping to a method), **Hotspots** ("the top five methods in Hotspots are what you're looking for"), **Threads** (as filter), **Subsystems** (filter dimension), source code preview, navigation/search, labeling. OLAP-style: "every view not only shows you some data but also works as a filter for other views". (A)
- **Comparison**: compare two snapshots; per-function Delta = A − B; green = improvement, red = deterioration; filters keep working in comparison mode. (A)
- **Bottleneck workflow**: start with Hotspots/Call Tree → scope to suspicious method → drill down. (A)

### Microsoft Visual Studio profiling tools — evidence layer A

- **Positioning**: "Application performance measuring tools … diagnose memory and CPU usage and other application-level issues … accumulate performance data while you run your application … visual depiction of execution times and CPU usage". (A)
- **Two modes**: **Performance Profiler** (Alt+F2; post-mortem analysis; intended for **Release** builds) and **Diagnostic Tools window** (during a debugging session; CPU, memory, .NET counters, events). (A)
- **Tool set** (per-language pivots): CPU Usage, Memory Usage, .NET Object Allocation, Instrumentation, .NET Async Tool, File I/O, .NET Counters, Database tool, GPU Usage, Application Timeline (XAML), Events viewer. (A)
- **CPU Usage view**: **Top Functions** (ordered by longest running), **Hot Path** (call stack of most CPU-consuming functions), **Call tree** with **Total CPU** (inclusive) vs **Self CPU** (exclusive) columns. (A)
- **Memory Usage**: take **memory snapshots**; recommended pattern = two snapshots (before/after suspected issue) then **diff** the heaps (object count diff, heap size diff). (A)
- **Instrumentation tool**: "exact call counts and wall clock time instead of CPU utilization"; "requires more overhead than the CPU Usage tool". (A)
- **PerfTips**: duration shown in-editor while stepping (debug-time measurement). (A)
- **Attach**: attach to running process (incl. Docker/Linux/WSL scenarios). **Command-line profiler** exists. (A)
- **Trace interoperability**: the profiler can view traces collected by other tools (e.g., dotnet-trace, sampling-based). (A)
- **AI**: Copilot recommends profiling tools and analyzes findings (2026-era feature). (A, single-product)
- **Legacy**: Performance Explorer/Performance Wizard folded into Performance Profiler (VS2019). (A)

### Grafana Pyroscope (continuous profiling) — evidence layer A

- **Positioning**: "multi-tenant, continuous profiling aggregation system"; continuous profiling is "an observability signal that allows you to understand your workload's resources usage **down to the source code line number**". (A)
- **Purpose**: "profile applications in production with minimal overhead"; "Starting with system-wide observability and drilling down to actionable code-level insights". (A)
- **Client paths**: (a) auto-instrumentation via a collector (Grafana Alloy; eBPF CPU profiling for compiled languages + agents for JVM/.NET/Python/Ruby/PHP/Node.js/Perl; pull mode; no source-code change), (b) SDK instrumentation (install language SDK, app pushes profiles periodically), (c) SDK → collector → server. (A)
- **Server**: ingestion, storage, querying of profiles; horizontally scalable; multi-tenant; object storage; integrates with Grafana for correlation with metrics/logs/traces. (A)
- **Analysis**: **flame graphs** ("visualize call relationships and identify hotspots"), **tables** ("detailed statistics for specific functions or time periods"), **charts/graphs** ("trends and compare performance across different metrics"); comparison across labels and time intervals; high-cardinality tag/label handling. (A)
- **Export/interchange**: pprof (and gzip-compressed pprof), JSON; CLI and HTTP API. (A)
- **Tags**: profiles enriched with labels (version, region, environment, request types) for correlation. (A)

### Firefox Profiler (browser profiler) — evidence layer A (project docs) / B (positioning)

- **Positioning**: "visualizes performance data recorded from web browsers … designed to consume performance profiles from the Gecko Profiler but can visualize data from any profiler able to output in JSON"; client-side web app. (A)
- **Collection model (fundamentals doc)**: two primary sources of information — **samples** and **markers**. (A)
  - **Samples**: "the profiler stops the execution of the profiled code at a fixed rate, for example, every 1ms and records … the current stack"; aggregated → "a statistical look into the execution"; no guarantee all code is sampled; sampling interval is a user-tunable knob (about:profiling); trade-off documented: higher rate → more overhead → can skew results; alternative = run the scenario more times.
  - **Markers**: "small pieces of data that are collected every time a specific event happens" — hand-instrumented, complete (do not miss events), but must be written/maintained by domain experts; over-instrumentation → gigabytes of data, skewed results. Markers can be cross-referenced with samples.
- **Workflow (getting-started doc)**: enable popup or devtools panel → choose preset (e.g., full browser vs web site) → **Start Recording** → **Capture** → profiler UI opens with captured data → **upload and share** (anyone with the link can access; current view + filters encoded in URL; permalink) → or **save to file** and reload by drag-and-drop. Data stays local until uploaded. (A)
- **Overhead culture**: docs recommend the popup over the devtools panel to avoid overhead from other panels. (A)

## Cross-product Comparison

| Dimension | dotTrace | Visual Studio | Pyroscope | Firefox Profiler |
|---|---|---|---|---|
| Target binding | launch via run config; attach (Windows) | launch (Performance Profiler); during debug session; attach (incl. Docker/Linux/WSL) | continuous: collector (eBPF/agents) or SDK push from running services | in-browser recording of browser/site; presets |
| Collection methods | sampling; tracing (entry/exit); line-by-line; timeline (ETW events) | sampling-based CPU Usage; instrumentation (exact counts); memory snapshots; event tools | continuous sampling via eBPF/agents/SDKs | fixed-rate stack sampling + hand-instrumented markers |
| Resource dimensions | time, call counts, memory alloc, GC, file I/O, thread states, await | CPU, wall clock, memory/heap, .NET counters, GPU, file I/O, DB queries, async ops | CPU (eBPF), workload resource usage "down to the source code line" | time (samples), event markers |
| Primary analysis views | Hotspots, Call Tree (folding, scoping), Threads, Subsystems, source preview | Top Functions, Hot Path, Call Tree (Total/Self), heap diff, timeline graphs, event lists | flame graphs, tables, charts; comparison across labels/time | call tree, timeline, marker charts (per docs index) |
| Record persistence | snapshot files (.dtp), save/reopen | reports/sessions; can open foreign traces (dotnet-trace) | server-side storage, historical, object-store backed | local until upload; shareable URL; save to file |
| Comparison | two-snapshot diff with delta coloring | two-snapshot heap diff | compare across labels/time intervals | (not evidenced in fetched docs) |
| Source navigation | source preview from profile | click function → call tree/source | "down to the source code line number" | (symbolicated stacks; not detailed in fetched docs) |
| Interface shapes | standalone GUI, CLI, VS, Rider | IDE panels (debug-time + post-mortem), CLI | server + web UI (Grafana), CLI, HTTP API | browser popup/devtools + web-based viewer |
| Production suitability | dev-time (attach possible) | dev-time (Release-build post-mortem) | production-first, minimal overhead | dev-time (browser) |
| Sharing | snapshot files | reports; foreign traces | Grafana dashboards, pprof/JSON export | upload → permalink; URL encodes view+filters |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately minimal)

A Profiler is recognizable as such only with **all four** of:

1. **A target program under observation during execution** — the profiler observes a program as it runs: launched under the profiler, attached to a running process, or continuously observed in the background. (Remove → static analyzer.)
2. **Runtime cost measurement** — the tool measures what execution costs in resources: time (CPU or wall-clock), memory allocated/retained, or other recorded events. (Remove → a launcher/logger.)
3. **Attribution of cost to program structure** — measured cost is attributed to code-level units of the target: functions/methods, call paths/stacks, statements/lines, allocation sites. This is the property that separates a profiler from a generic resource monitor. (Remove → system monitor / metrics dashboard.)
4. **The profile as a persistent explorable record** — collected data is captured into a record (snapshot / profile / report / trace) that survives the session and can be navigated, filtered, queried, and compared. (Remove → transient readout; every sampled product has this: dotTrace snapshots, VS reports, Pyroscope server storage, Firefox local-then-upload profiles.)

Jointly load-bearing:

- 1 alone = process launcher / logger
- 2 without 3 = resource monitor / dashboard
- 3 without 1+2 = static call-graph/complexity analysis (no measured cost)
- 4 without 1–3 = generic data viewer
- 1+2 without 3 = monitoring, not profiling
- 1+3 without 2 = static call graph, not measurement
- 2+3 without 1 = arithmetic over no real execution

### L1 — Common Mature Structure (cross-product, evidence layer B)

- **Multiple collection methods with documented trade-offs**: sampling (statistical, low overhead, may miss fast/rare code, no call counts) vs instrumentation (complete, exact counts, timing distortion grows with call frequency, heavier) — both explicitly documented with pros/cons in dotTrace and VS; line-level as a deeper instrumentation tier (dotTrace line-by-line; VS has no line tool in fetched docs — keep line-level as common-not-universal).
- **Multiple resource dimensions**: CPU time, wall time, memory allocation/heap, GC, file I/O, thread/lock states, async operations, GPU (VS, dotTrace timeline; Pyroscope resource usage).
- **Standard analysis views**: hot spot list (Top Functions / Hotspots), call tree with self/total time (Total/Self CPU; merged call tree), flame graph (Pyroscope; widely known elsewhere), timeline (dotTrace timeline, VS timeline graphs, Firefox timeline), thread view.
- **Snapshot/profile lifecycle**: collect → save → reopen → (optionally) compare. Two-profile comparison with per-function deltas (dotTrace, VS heap diff, Pyroscope label/time comparison).
- **Source navigation**: from a profile entry to source code (dotTrace source preview, VS call tree/source, Pyroscope line-number claims).
- **Multiple interface shapes from one engine**: standalone GUI + CLI + IDE integration (dotTrace explicitly; VS IDE + CLI; Pyroscope server + CLI + API; Firefox popup/devtools + web viewer).
- **Interchange/export**: open traces from other tools (VS/dotnet-trace), export pprof/JSON (Pyroscope), save/reload files (Firefox, dotTrace .dtp).
- **Symbol resolution dependency**: line-by-line requires PDB files (dotTrace); native functions require symbol files (dotTrace timeline). Symbols as an enabling input for readable profiles.

### L2 — Variant / Optional Structure

- **Continuous/production profiling**: always-on collection with minimal overhead, profiles shipped to an aggregation server, multi-tenant storage, correlation with other observability signals, comparison across labels/time. (Pyroscope; the variant that blurs into observability but keeps code-level attribution.)
- **Auto-instrumentation collectors** (eBPF, agent-based pull): profiling without source modification. (Pyroscope/Alloy.)
- **Hand-instrumented domain events (markers)**: complete-but-maintained event stream cross-referenced with statistical samples. (Firefox fundamentals; conceptually same family as dotTrace timeline ETW events / VS custom timeline marks.)
- **Debug-time measurement**: durations shown while stepping (VS PerfTips); profiling inside a debug session (VS Diagnostic Tools).
- **Remote/device targets**: attach into Docker/Linux/WSL (VS); on-device Android profiling guides exist in the Firefox project (file listing only — not fetched).
- **AI assistance**: tool recommendation and result analysis by an integrated AI assistant. (VS Copilot — single-product in-sample; optional.)
- **Sharing culture**: upload profile → share permalink with encoded view state (Firefox); server-side sharing via dashboards (Pyroscope). Local-file-only products (dotTrace, VS) do not center sharing.

### L3 — Vendor-specific (kept out of the final document)

- dotTrace: profiling-type names (Sampling/Tracing/Line-by-Line/Timeline), ETW basis, .dtp format, Home window run configurations, Subsystems filter, performance forecasting, OLAP viewer framing.
- Visual Studio: PerfTips, Diagnostic Tools window, per-language tool pivots, Copilot integration, BenchmarkDotNet data viewing, Application Timeline (XAML), legacy Performance Explorer.
- Pyroscope: Grafana Alloy, Profiles Drilldown, multi-tenancy, Mimir/Loki/Tempo architecture alignment, tag regex.
- Firefox: about:profiling, presets (Firefox / Web Developer), popup vs devtools entry points, markers terminology, uploaded-recordings management.

## Boundary Findings

- **vs Debugger**: the debugger's primary output is program **state at a controlled point** (pause/step/inspect); the profiler's primary output is **cost attributed to code**. Overlap is real and documented: VS profiles *during* debug sessions and shows durations while stepping (PerfTips); modern IDEs bundle both. The seam: does the tool control execution, or measure it? A tool that only controls is a debugger; a tool that measures cost and attributes it is a profiler; bundling does not merge the Types.
- **vs APM / Observability Platform**: APM/observability monitor **services in production for operators** — request rates, error rates, resource graphs — without attributing cost to code units. The profiler attributes cost to code for developers. **Continuous profiling** (Pyroscope) is production-deployed like observability but its defining output is code-level attribution — so it remains a **Profiler variant**, not an observability Type. Test: if the product's deepest answer is "which function/line/allocation site", it is profiling; if it stops at "which service/endpoint is unhealthy", it is monitoring.
- **vs Performance Testing / Load Testing**: load testing **generates load** and measures system response under it; the profiler **observes one program's internal cost**. Complementary: a load test can be the scenario during which a profiler runs. Remove load generation → profiler; remove code attribution and add virtual users → performance testing.
- **vs Distributed Tracing**: traces follow **requests across services** (spans); profilers attribute cost **within a process to functions**. Different unit of analysis; different primary user question.
- **vs Static Code Analysis**: static analysis reasons about code **without executing it**; a profiler's findings are grounded in **measured execution**. A static call graph without measured cost is not a profile.
- **vs Metrics Monitoring**: resource graphs without code-level attribution = monitoring. The attribution property is the single sharpest boundary: **remove code-level attribution and the product becomes a monitoring/metrics tool; remove execution observation and it becomes static analysis; remove measurement and keep control and it becomes a debugger.**

## Historical / Market-Sample Check

- Would older, regional, platform-native products still fit the L0? **gprof** (early 1980s Unix): runs the program under observation, produces a flat profile + call graph attributing time to functions — satisfies all four invariants with no GUI, no flame graph, no IDE, no cloud. **perf** (Linux): sampling + events, CLI collection + report viewing — satisfies. 1990s Java profilers (instrumentation-based, flat views) — satisfy. Platform-native profilers (Visual Studio legacy Performance Wizard lineage, browser profilers) — satisfy.
- Therefore the L0 must NOT include: flame graphs, IDE integration, cloud/continuous backends, share links, AI assistance, or any specific collection method (sampling vs instrumentation are both just implementations of "runtime cost measurement").
- Note: gprof/perf/1990s profilers are used here as conceptual-lineage checks from general knowledge; their details were not fetched in this pass (low confidence on specifics, high confidence on the structural point).

## Uncertainties

1. **Hardware-counter-based profiling** (e.g., processor PMU sampling in native profilers): widely known technique but **not directly evidenced in the fetched sample** (Intel VTune unreachable). Kept out of the final document's claims; recorded here as unverified-in-sample.
2. **Apple Instruments / Chrome DevTools / Android Studio Profiler**: official docs unreachable in this environment; the platform-native and browser slots are covered by Visual Studio (Windows) and Firefox Profiler respectively. Assertions about those specific products are avoided entirely.
3. **Memory-profiling depth**: VS documents snapshot+diff; dotTrace documents allocation/GC events in timeline mode; Pyroscope documents resource usage to line level. Whether a dedicated "heap walker"-class object browser is common-mature could not be confirmed across the sample (JProfiler/YourKit unreachable) — kept as common-not-confirmed.
4. **Flame graph universality**: directly evidenced at Pyroscope; widely associated with profiling generally, but only one in-sample product documents it in fetched pages. Written as "common" with moderate strength, not definitional.
5. **Sharing/upload**: evidenced in Firefox + Pyroscope; absent from dotTrace/VS fetched pages → variant, not core.
6. **Exact sampling rates/intervals**: Firefox docs give an example (1ms) and dotTrace gives a pause range (5–11 ms) — these are product-specific numbers and are kept in Research Notes only, not in the final document.

## Final Synthesis

The Profiler is best modeled as: **observe a running program → measure its runtime cost → attribute that cost to code-level units → capture the result as a persistent explorable profile → navigate from hot spots down to code → fix → re-profile and compare.**

The defining core is the four-part joint structure (observed target + cost measurement + code-level attribution + explorable profile record). Collection method (sampling/instrumentation/line-level/events), resource dimension (CPU/memory/I/O/GPU), interface shape (IDE/standalone/CLI/web), and deployment context (dev-time vs continuous production) are all axes of variation, not definition. The continuous-profiling pole proves the type survives deployment-context change because the defining output — cost attributed to code — is unchanged.
