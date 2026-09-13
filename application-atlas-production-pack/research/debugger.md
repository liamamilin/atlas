# Research Notes — Debugger

Research date: 2026-09-07

## Research Goal

Understand the Debugger as an Application Type: what the defining core is (and only is), what the standard interaction loop is, which capabilities are common vs optional, where the boundary runs against profilers, error trackers, editors/IDEs, and logging/tracing tools, and how the Type survives historical checks (command-line era, machine-level debuggers, post-mortem analysis).

## Initial Boundary (hypothesis before research)

- Core use: run a program under controlled conditions, stop it at points of interest, inspect the live program state, step through execution to locate the cause of incorrect behavior.
- Users: software developers (also QA debugging failing tests, engineers debugging deployed systems via remote/post-mortem modes).
- Nearest neighbors: Code Editor / IDE (debugger commonly embedded), Profiler (performance vs correctness), Error Tracking Platform (production error artifacts vs live control), Logging / APM / Distributed Tracing (passive records vs interactive stopping), Unit Test Runner.
- Initial uncertainty: is "source-level" inspection definitional, or is it only the common modern realization? (Machine-level and VM-level debuggers exist.)
- Initial uncertainty: does post-mortem (core dump) analysis belong to the Type if live resume is impossible?

## Research Questions

1. How does a debug session start? (launch vs attach vs captured snapshot)
2. What is the breakpoint model? (kinds, conditions, lifecycle, non-stopping variants)
3. What does "stepping" mean canonically? (over/into/out, instruction-level, run-to)
4. What state is inspectable, and in whose terms? (position, call stack, variables/scopes, expression evaluation, memory/registers)
5. How do threads and multi-session scenarios appear?
6. What rules constrain the tool? (debug info/symbols, optimized code, breakpoint verification, evaluation side effects)
7. How is the Type realized as product packaging? (standalone CLI engines, IDE-embedded UIs, protocol-separated engine/front-end)
8. Where exactly do the neighboring Types end and this one begin?

## Representative Products

Selected for market representativeness, documentation quality, and deliberately different product philosophies:

| Product | Pole | Why selected |
|---|---|---|
| GDB (GNU Debugger) | standalone CLI engine, native/machine substrate | canonical pure debugger; decades-old lineage; covers native + remote + embedded + post-mortem |
| LLDB (LLVM) | standalone CLI engine, modern native | second engine philosophy; published GDB-to-LLDB command map is direct cross-product evidence of a stable command canon |
| Visual Studio Code debugging | editor-embedded generic front end over protocol adapters | dominant modern editor packaging; generic UI over per-language debug adapters |
| IntelliJ IDEA debugger | IDE-embedded debugger, managed-runtime (JVM) substrate | managed-runtime state model (objects/heap) instead of machine state; rich official procedure documentation |
| Debug Adapter Protocol (DAP) | protocol specification, not a product | abstracts "a debugger" into named concepts/requests — the strongest available canonical-model evidence |

## Sources

All fetched 2026-09-07.

- GDB manual (Tenth Edition, GDB 19), https://sourceware.org/gdb/current/onlinedocs/gdb.html/ — table of contents and chapter structure (Running, Stopping and Continuing, Breakpoints/Watchpoints/Catchpoints, Stack, Data, Altering, Symbols, Remote Debugging, Tracepoints, Optimized Code, TUI, GDB/MI, Debugger Adapter Protocol, core files, debuginfod). [Evidence layer A]
- LLDB — GDB to LLDB command map, https://lldb.llvm.org/use/map.html — full command correspondence table (execution, breakpoints, watchpoints, variables, expressions, thread state, memory, disassembly, symbolication, source mapping, save-core). [A]
- Visual Studio Code — "Debug code with Visual Studio Code", https://code.visualstudio.com/docs/editor/debugging — debug UI components, session start, debug actions table, breakpoint types, data inspection, multi-target, remote debugging, extensions. [A]
- Debug Adapter Protocol — landing page and Overview, https://microsoft.github.io/debug-adapter-protocol/ , https://microsoft.github.io/debug-adapter-protocol/overview — session lifecycle, launch/attach, breakpoint configuration requests, stopped events, threads→stackTrace→scopes→variables waterfall, terminate/disconnect semantics. [A]
- IntelliJ IDEA — "Debug code", https://www.jetbrains.com/help/idea/debugging-code.html — debugger purpose, general debugging procedure, suspended program, examining state, stepping, HotSwap, attach/remote as separate topics. [A]
- Chrome DevTools (browser-hosted debugger) — https://developer.chrome.com/docs/devtools/javascript/breakpoints — **unreachable**: WebFetch timed out twice on 2026-09-07. Source abandoned per retry discipline. No browser-devtools claims are made from memory; the browser-hosted pole is mentioned only as an unverified realization in Uncertainties. [limitation recorded]

## Product Observations

### GDB (GNU Debugger) — Evidence layer A unless noted

From the official manual structure and chapter organization:

- **Control relationship**: "Running programs under GDB" — start your program, program arguments/environment/working-directory, "Debugging an already-running process" (attach), multiple inferiors (several programs/connections at once). Remote debugging via `gdbserver` and the GDB Remote Serial Protocol. Embedded processors chapter (ARM, MIPS, PowerPC, RISC-V, …) — the controlled program can be on other hardware.
- **Pause machinery**: chapter "Stopping and continuing" with sections for breakpoints (set by linespec/function/address; conditions; breakpoint command lists; save breakpoints to file; static probe points), watchpoints (stop on data change), catchpoints (stop on events such as signals/exceptions), disabling breakpoints, "Cannot insert breakpoints" failure section, "Breakpoint address adjusted…" warning — i.e., a breakpoint lifecycle beyond set-and-hold.
- **Non-stopping variant**: "Dynamic printf" — breakpoint-like instrumentation that prints instead of stopping (logpoint analog). Tracepoints chapter: non-intrusive data collection on remote targets.
- **Execution control**: "Continuing and stepping" (continue, step, next, finish, until line), skipping over functions/files, instruction-level steps exist alongside source-level steps (stepi/nexti per the LLDB correspondence), signals handling, all-stop vs non-stop multi-thread modes, thread-specific breakpoints, observer mode.
- **Post-mortem**: core file generation ("How to produce a core file from your program"); core files appear throughout (e.g., tasking support when debugging core files) — captured-execution-snapshot inspection is a native mode.
- **Inspection**: Stack chapter (frames, backtraces, frame selection, frame info), Source chapter (printing/listing source, location specifications, source directories, mixed source and machine code), Data chapter (expressions in the program's language, program variables, memory examination, registers, automatic display, pretty printing, value history, convenience variables).
- **Altering execution**: assignment to variables, continuing at a different address (jump), returning from a function, calling program functions in the target, patching, code injection via `compile`.
- **Substrate nuance**: dedicated chapter "Debugging optimized code" (inline functions, tail call frames) — the source↔machine correspondence is a first-class concern, and it can degrade.
- **Interfaces**: CLI prompt commands; TUI (text user interface); GDB/MI "Machine Interface" for front ends; a "Debugger Adapter Protocol" chapter (DAP support); Python/Guile scripting APIs; interpreters.
- **Symbols infrastructure**: Symbols chapter, separate debug files, index files, debuginfod (downloading debugging resources) — source-level debugging depends on external debug information.

### LLDB — Evidence layer A

From the official GDB-to-LLDB command map (which is itself cross-product evidence: two independent engines expose the *same conceptual surface*):

- **Control**: `process launch` / `run` (with args, env vars, tty), `process attach` by pid/name/waitfor, `gdb-remote` / `kdp-remote` (remote targets, kernel), `process save-core` (capture snapshot).
- **Pause machinery**: `breakpoint set` by name/file+line/method/selector/func-regex/source-pattern, conditions (`--condition`), list/delete/disable/enable; `watchpoint set variable/expression` with conditions.
- **Execution control**: `thread step-in` / `step-over` / `step-out` / `step-inst` / `step-inst-over`, `thread return` (early return), `thread until <line>`, stop hooks (commands run on every stop).
- **Inspection**: `frame variable` (args/locals per frame), `target variable` (globals), `print`/`expr` evaluation including calling functions in the target (e.g., calling `printf`), registers (`register read/write`), memory (`memory read`), disassembly (mixed source+disassembly), `image lookup` / symbolication, source-map remapping for relocated sources.
- **Threads**: `thread list`, `thread select`, `thread backtrace [all]`, frame select/up/down.
- **Interfaces**: CLI command interpreter with unique-short-form commands; `lldb-dap` (DAP adapter); Python API incl. scripted breakpoints/thread plans; stop hooks. Side nav confirms "IDE & Tool Integration" as an official concern.

### Visual Studio Code debugging — Evidence layer A

From the official debugging documentation:

- **Packaging**: a generic debugger UI with built-in support for JavaScript/TypeScript/Node.js and per-language debugger extensions from a marketplace — the editor hosts, the engine comes from elsewhere.
- **UI surfaces** (documented as the five main components): Run and Debug view (configuration + management), debug toolbar (session control), debug console (view/interact with program output + REPL), debug sidebar (call stack, breakpoints, variables, watch), Run menu. Breakpoints are set in the editor gutter; session status shown in the status bar.
- **Session start**: F5 / Run and Debug; a `launch.json` debug configuration defines more complex scenarios (arguments, attach to a running process). Copilot can generate configurations (current-generation AI assistance).
- **Debug actions** (documented as the canonical toolbar): Continue/Pause, Step Over ("execute the next method as a single command without inspecting its component steps"), Step Into, Step Out, Restart, Stop.
- **Breakpoint types** (documented): line breakpoints (gutter click), conditional breakpoints (expression condition, hit count, or combination), triggered breakpoints (activated when another breakpoint is hit), inline breakpoints (column-precise, for minified code), function breakpoints (by name when source is unavailable), data breakpoints (Break on Value Change/Read/Access, set from the VARIABLES view), logpoints (log a message with `{expression}` interpolation instead of interrupting). Availability of some types depends on the debugger extension (capability flags).
- **Breakpoint lifecycle**: breakpoints that can't be registered with the debugger turn into a gray hollow circle — unverified state is user-visible.
- **Data inspection**: VARIABLES view scoped to the selected call-stack frame; hover over source for values; Set Value to change a variable; WATCH section for expressions; filter variables; Debug Console REPL ("You must be in an active debugging session to use the Debug Console REPL").
- **Multi-target**: multiple debug sessions (e.g., client and server) shown as top-level elements in the call stack view; toolbar actions apply to the active session; switching sessions.
- **Remote debugging**: not built-in universally — a feature of each debug extension (Node.js debugger supports it directly).
- **Launch vs attach** both exist ("For more complex debugging scenarios like attaching to a running process, you need a `launch.json`").

### IntelliJ IDEA debugger — Evidence layer A

From the official "Debug code" documentation:

- **Purpose statement** (vendor's own definition): "The purpose of the debugger is to interfere with the program execution and provide you with the information on what's happening under the hood. This facilitates the process of detecting and fixing bugs in your program."
- **Session modes**: launch the program with the debugger attached (run/debug configuration); attach to a process; debug a remote application — separate documented topics. Multiple debug sessions can run at the same time.
- **General procedure** (vendor-documented canonical loop): 1) define where to stop with breakpoints ("special markers … places and conditions when the debugger needs to step in and freeze the program state"; the frozen program is called *suspended*); alternative: manual suspension at an arbitrary moment (with limitations); 2) run the program in debug mode (a regular application, a unit test, or any other executable code); 3) examine the suspended program state — variable values, thread states, heap breakdown of objects — and test behavior by throwing exceptions or running arbitrary code mid-execution; stepping gives control over step-by-step execution; 4) fix without terminating (reload modified classes / HotSwap).
- **Substrate**: JVM — state is variables, threads, and objects in the heap (not registers/memory). "Generate debugging info" compiler option noted as feeding debugger functionality.
- **Stepping/watches/evaluation**: Debugger Essentials topics list line breakpoints, stepping, session control, watches, expression evaluation, breakpoint conditions; Advanced topics include remote debug, renderers, breakpoint types/settings.

### Debug Adapter Protocol — Evidence layer A (as cross-tool canonical evidence)

From the official overview:

- Framing: DAP "defines the abstract protocol used between a development tool (e.g. IDE or editor) and a debugger" via an intermediary *debug adapter* that adapts "an existing debugger or runtime" — direct evidence that the industry models "a debugger" as a distinct, protocol-able component.
- **Feature list the protocol exists to standardize**: source-, function-, conditional-, and inline breakpoints; variable values in hovers or inlined in source; multi-process and multi-thread support; navigating complex data structures; watch expressions; debug console REPL; logpoints. This list is effectively a vendor-neutral enumeration of the standard debugger feature set.
- **Session lifecycle**: initialize (capability exchange) → launch ("the debug adapter launches the program — the *debuggee* — in debug mode") or attach ("connects to an already running program"; end user responsible for launching/terminating) → configuration (setBreakpoints per source, setFunctionBreakpoints, setExceptionBreakpoints, configurationDone) → run.
- **Stop model**: "Whenever the program stops (on program entry, because a breakpoint was hit, an exception occurred, or the user requested execution to be paused), the debug adapter sends a `stopped` event with the appropriate reason and thread id." The tool then requests: threads → stackTrace (stack frames) → scopes per frame → variables per scope → nested variables — the documented *request waterfall* mirrors the inspection hierarchy exactly.
- **Verification**: breakpoints that cannot be applied are marked `verified: false`; state changes are pushed via breakpoint events.
- **Session end**: launched debuggees are terminated (terminate → disconnect as fallback); attached debuggees are *detached* and allowed to continue — attach is non-destructive by design.
- **Capabilities negotiation**: features are optional and flagged — direct evidence that many debugger capabilities (conditional breakpoints, data breakpoints, logpoints, …) are per-engine options, not universal.

## Cross-product Comparison

| Structure | GDB | LLDB | VS Code | IntelliJ | DAP | Assessment |
|---|---|---|---|---|---|---|
| Program under debug, launched by the tool | run (+args/env/cwd) | process launch | launch config (launch.json) | run/debug configuration | `launch` request | **All 5 — defining** |
| Attach to an already-running program | attach | process attach (pid/name/waitfor) | launch.json attach scenarios; per-extension | separate "attach to process" topic | `attach` request | **All 5 — defining leg of control** |
| Captured-execution-snapshot (post-mortem) | core files; gcore | process save-core | — (per-extension) | — | — | native-debugger realization; 2 products; keeps live-resume out of the definition |
| Breakpoint at source location | break file:line / function / address | breakpoint set -f -l / -n / regex / source-pattern | gutter line breakpoints; inline (column) breakpoints | breakpoints as "special markers" | `setBreakpoints` (per source) | **All 5 — defining** |
| Function breakpoints (by name, no source) | break <function> | breakpoint set --name | documented type | — (not on fetched page) | `setFunctionBreakpoints`; listed feature | cross-product; standard |
| Conditional breakpoints | break … if <expr> | --condition | expression + hit count + triggered | breakpoint conditions (topic list) | conditional breakpoints listed | **All 5 — common mature structure** |
| Non-stopping logging breakpoint | dynamic printf | — (not in map) | logpoints with {expr} interpolation | — (not on fetched page) | logpoints listed | 3/5 + protocol — common, not universal |
| Exception/event catch stops | catchpoints | — | — | — (not on fetched page) | `setExceptionBreakpoints` | 2–3/5 — common, per-runtime |
| Data watchpoints (stop on data change/read) | watch / watch -location | watchpoint set variable/expression + conditions | Break on Value Change/Read/Access | — (not on fetched page) | — (capability-flagged) | 3/5 — common in native; optional elsewhere |
| Manual pause of a running program | interrupt (implied by stopping chapter; observer/non-stop modes) | — | Pause toolbar action | manual suspension (documented) | `pause` request | cross-product — standard |
| Continue / resume | continue | — (process continue exists; map focuses elsewhere) | Continue/Pause toolbar | implied by procedure | `continue` request | **All 5 — standard live loop** |
| Step over / into / out | next / step / finish | thread step-over / step-in / step-out | toolbar table (identical trio) | stepping (topic) | `next` / `stepIn` / `stepOut` | **All 5 — canonical stepping** |
| Instruction-level stepping | stepi/nexti | thread step-inst(-over) | — | — | — | native-substrate realization |
| Run to location | until <line> | thread until | — | — | — | 2/5 — common |
| Current position mapped to source | source chapter; list; mixed source/disassembly | frame info; source-map | editor highlights current line (gutter markers; inline values) | suspended-program examination | stackTrace request returns source refs | **All 5 — defining leg of inspection** |
| Call stack / frames / backtrace | backtrace, frame select, up/down | thread backtrace, frame select | CALL STACK section (frame-scoped evaluation) | thread states + suspended examination | stackTrace → stack frames | **All 5 — defining leg of inspection** |
| Variables/scopes per frame | info locals/args; print | frame variable | VARIABLES view scoped to selected frame; hover; filter | variable values in suspended state | scopes → variables waterfall | **All 5 — defining leg of inspection** |
| Expression evaluation in program context | print/call expressions | expr (incl. calling functions) | Debug Console REPL (session-gated) | "running arbitrary code right in the middle of the program execution"; expression evaluation | `evaluate` | **All 5 — defining leg of inspection (evaluation)** |
| Modify program state mid-session | set variable; jump; return; patching | register write; thread return; expr assignment | Set Value (variables) | throw exceptions; reload modified classes | `setVariable` | 4–5/5 — common mature (not definitional) |
| Threads | info threads; all-stop/non-stop; thread-specific breakpoints | thread list/select/backtrace | call stack per session; multi-session | thread states | `threads` request + stopped event thread id | 4–5/5 — common mature |
| Multiple simultaneous sessions/targets | multiple inferiors | multiple targets (SB API) | multi-target debugging (client+server, active session) | multiple debug sessions at once | multi-process listed | 4/5 — common mature |
| Launch configuration (args/env/cwd) | set args / set env | settings target.run-args / env-vars | launch.json | run/debug configuration | launch/attach arguments (per-adapter) | **All 5 — common mature** |
| Debug info/symbols dependency | "Compiling for Debugging"; separate debug files; debuginfod | symbolication docs | gray hollow circle when unresolvable (breakpoint binding) | "Generate debugging info" option | — | **All 4 products — structural rule** |
| Optimized-code correspondence breaks | dedicated chapter (inline, tail calls; breakpoint address adjusted) | — | minified-code inline breakpoints (analog for transpiled code) | — | — | native/analog evidence — structural rule, qualified |
| Breakpoint verification lifecycle | "Cannot insert breakpoints"; address adjusted warnings | breakpoint list (resolved state) | gray hollow circle for unregistered | — | verified: false + breakpoint events | 3–4/5 — common mature |
| Remote debugging | gdbserver; remote protocol chapter | gdb-remote; remote docs | per-extension; Node.js built-in | separate remote topic | adapter-mediated | **All 4 products — common mature** |
| Engine/front-end separation | GDB/MI; DAP chapter; TUI; Emacs | lldb-dap; Python API; IDE integration docs | generic UI + marketplace debug adapters | plugins for other languages | the protocol itself | 4/5 + protocol — common mature (packaging) |
| Extensibility/scripting | Python/Guile; command files | Python API; scripted breakpoints | debugger extensions | plugins/renderers | adapter SDKs | 4/5 — common mature |
| Formatters/pretty printers | pretty printing chapter | data formatters/variable formatting | — | renderers (topic list) | string-based presentation in protocol | 3–4/5 — common mature |
| Reverse execution / record-replay | dedicated chapters (reverse execution; process record and replay; checkpoints) | Intel PT tracing (trace cursor) | — | — | — | 1–2/5 — optional/advanced |
| Tracepoints (non-intrusive remote collection) | dedicated chapter | tracing docs | — | — | — | 1–2/5 — optional/advanced |
| HotSwap / live code reload | — | — | — | reload modified classes | — | 1/5 — product-specific |
| AI-assisted debugging | — | — | Copilot config generation; debug-with-AI guides | — | — | current-generation, 1/5 — optional |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures. Removing any one makes the tool a different kind of thing:

1. **Control relationship with the program under debug.** The tool does not observe from outside: it takes a specific program's execution under its control — launching it under supervision, attaching to it while it runs, or opening a captured execution snapshot of it (post-mortem). *Remove →* profiler, log viewer, error-tracking platform, crash-artifact analyzer.
2. **The declared pause.** Execution is stopped at points or conditions the user (or the event itself) chooses — location/function/conditional breakpoints, manual suspension, stops on exceptions, crashes, or data changes — and the stop is surfaced as the tool's central event (with a reason and location). *Remove →* logging, tracing, printf-debugging (continuous passive output, no stop).
3. **Inspection of the stopped state in the program's own execution terms.** While stopped, the tool answers: *where am I* (current position mapped to the program's code), *how did I get here* (the call stack of frames leading to this point), *what are the values* (variables/scopes per frame), and lets the user *ask new questions* (evaluate expressions in the program's own language/context). The "terms" are the program's semantic level: source names (variables, functions, lines) in source-level debuggers; machine names (registers, memory, instructions) in low-level debuggers; VM object names in managed-runtime debuggers. *Remove →* hex dumper or a static stack-trace artifact (you can look, but not ask anything new).

Deliberately **not** in L0:

- **Resume/stepping.** Continue/step is the standard interaction loop of live debugging, but a post-mortem debugger working on a captured snapshot cannot resume, and is still a debugger (GDB's core-file mode; the capture commands in both native engines). Making live-resume definitional would fail the historical check.
- **Source-level inspection.** Requiring source names would exclude machine-level and post-mortem debuggers; the invariant is inspection *at the program's own semantic level*, of which source-level is the common modern realization (and it depends on external debug information).
- Breakpoint *kinds* beyond location-based stops, threads, watch expressions, variable modification, remote debugging, any UI form.

### L1 — Common Mature Structure (very common, not definitional)

- Execution control: continue/pause, step over/into/out (the trio is identical across all five sources), run-to-location, restart/relaunch, instruction-level stepping in native engines.
- Breakpoint family: function breakpoints, conditional breakpoints (expression and/or hit count), enable/disable/delete management, non-stopping logpoints, exception/catch stops, data watchpoints (change/read/access).
- Watch expressions and persistent value display; automatic display on each stop.
- Expression evaluation / REPL in the program's context, including calling functions in the target; modifying program state mid-session (set variable, register write, early return).
- Threads: list/select/per-thread stacks; stop semantics across threads (with product-specific modes).
- Multiple simultaneous sessions/targets (client+server debugging; several inferiors).
- Launch configuration as a persistent artifact (arguments, environment, working directory).
- Breakpoint lifecycle: requested → verified/unverified/moved, pushed to the user.
- Debug-information dependency: symbols/symbolication, separate debug files, source-path remapping.
- Remote debugging (debug-server stubs, adapter-mediated, IDE topics).
- Engine/front-end separation: machine interfaces (GDB/MI), protocol adapters (DAP, lldb-dap), marketplace/extensibility models; scripting APIs; pretty printers/formatters/renderers.
- IDE/editor integration surfaces: gutter markers, current-line highlighting, hover/inline values, debug console, variables/call-stack/breakpoints panels.

### L2 — Variant / Optional Structure

- State substrate: machine registers/memory/disassembly (native engines) vs VM objects/heap (managed runtimes) vs hosted-runtime contexts (browser page; unverified this pass) — substrate-specific inspection surfaces (e.g., heap breakdown vs memory dumps).
- Reverse debugging / record-replay / process checkpoints (documented in GDB; tracing in LLDB).
- Tracepoints: non-intrusive remote data collection instead of stopping.
- Live code replacement (HotSwap-class; documented in IntelliJ).
- Post-mortem snapshot generation from a live process (gcore/process save-core).
- Embedded/hardware target debugging (other architectures, debug stubs).
- Non-stop/observer stopping modes (whole-process vs per-thread pause semantics vary).
- AI-assisted debugging (configuration generation, guided investigation) — current-generation add-on.
- Historical: machine-level debuggers with assembly-only views satisfy L0 at the machine semantic level; command-line-era debuggers satisfy L0 with CLI interfaces alone.

### L3 — Vendor-specific (research notes only)

- GDB: convenience variables/value history, checkpoint/restart of inferiors, static probe points, breakpoint command lists, debuginfod, overlay debugging, Ada tasking support, observer-mode semantics, non-stop mode specifics.
- LLDB: stop hooks, unique-short-form command rules, scripted breakpoint resolvers/thread plans, `target.prefer-dynamic-value`, macOS heap-analysis helpers, Intel PT trace cursor.
- VS Code: `launch.json` schema and variable substitution, debug.breakpointsView settings, middle-click gutter action, Copilot-generated configurations, overview-ruler breakpoint display.
- IntelliJ: run/debug configuration machinery, reload-modified-classes (HotSwap) UX, debug labels, asynchronous stack traces, decompiled-code debugging, debugger settings tree.
- DAP: object-reference lifetime bound to the suspended state, capability flags vocabulary, single-dummy-thread requirement for single-threaded engines, runInTerminal reverse request, terminate-vs-disconnect semantics.

## Vendor-specific Findings

- Reverse execution, record-replay, and checkpoints are documented GDB capabilities; LLDB documents hardware-trace tooling rather than the same reverse-stepping surface. Treat "time-travel debugging" as optional/rare, not standard.
- HotSwap-class live class replacement is documented in the JVM-pole product; no sampled native engine documents it.
- AI-assisted configuration/investigation appears only in the current-generation editor sample.

## Rejected Findings

- **"A debugger is part of an IDE"** — rejected as definitional. Standalone engines (GDB, LLDB) and the protocol-separated adapter architecture (DAP; GDB/MI; lldb-dap) demonstrate the Type exists independently of any editing surface. Embedding is the dominant *packaging*, not the definition.
- **"Source-level" as the defining term** — rejected. Machine-level debuggers (assembly-only inspection) and post-mortem core-dump analysis are recognized members of the Type; the invariant was abstracted to "inspection at the program's own semantic level."
- **"Live resume/stepping is definitional"** — rejected. Post-mortem snapshot inspection satisfies the Type; resume/step is the standard live-mode loop.
- **"A stack trace artifact is inspection"** — rejected. A reported stack trace answers one fixed question; the defining leg requires asking new questions (frame selection, variable drill-down, expression evaluation) against the stopped state.
- **"Debuggers measure performance"** — rejected (profiler territory). Sampling/timing aggregation without stopping is a different Type; occasional overlap features (GDB tracepoints) remain optional.
- **"Logpoints are a logging capability"** — partially rejected as a boundary worry: logpoints are breakpoint machinery that chooses not to stop; they inherit breakpoint binding/conditions and remain inside the Type.

## Boundary Findings

| Neighbor | Relationship | Remove-test (what turns it into the other Type) |
|---|---|---|
| Code Editor | adjacent; debugger often embedded in it | Editing is static text manipulation; the debugger's object is a *program's execution*. Strip editing from an IDE debugger → still a debugger; strip debugging → editor. The embedded realization is packaging, not definition. |
| Integrated Development Environment / IDE | containing surface for the debugger capability | The IDE leaf covers the integrated whole (editing, building, navigation, debugging). The debugger stands as its own Type via standalone engines + protocol-separated adapters. Capability-vs-Type question recorded below. |
| Profiler | nearest tool-family neighbor | Profiler aggregates timing/sampling over whole runs to answer "where is time spent" and does not stop the program at declared points or inspect one stopped state; strip the pause + program-term inspection → profiler. |
| Error Tracking Platform | artifact-oriented neighbor | It aggregates externally reported error events from deployed software (stack traces, occurrences) — no control relationship, no declared stops, no live inspection; strip the control relationship → error tracking. |
| Log Management / APM / Distributed Tracing | passive-record neighbors | Continuous records of running systems, viewed after the fact; no stopping, no declared breakpoints; strip the declared pause → logging/tracing. |
| Unit / Integration Test Runner | workflow neighbor | The runner's object is the *outcome* of executing test suites (pass/fail, reports). The debugger's object is one program's execution state. The sampled IDE documents debugging a unit test as a valid target — the debugger attaches to whatever executable; the runner reports results. |
| REPL / notebook-style interactive runtime | superficial similarity | A REPL evaluates expressions in its own session; it does not take a separate program's execution under control at declared points. (Debug consoles expose REPLs *over* the controlled program — the control relationship is what makes them debugger surfaces.) |

Sharpest seams recorded: **vs Profiler** (stop-and-inspect vs aggregate-and-measure) and **vs Error Tracking** (live control vs reported artifacts). Both hold under the remove-test.

Capability-vs-Type note: in the current market the Debugger is realized *dominantly* as a capability embedded in IDEs/editors, with standalone engines (GDB, LLDB) and protocol adapters as the other poles. The Type stands (distinct core model, standalone products, protocol-level independence); packaging should be documented as a variant, not a taxonomy split.

## Uncertainties

- **Browser-hosted debuggers** (developer tools in web browsers): the intended sample member for the hosted-runtime pole was unreachable (two fetch timeouts on 2026-09-07). From the remaining evidence (DAP's tool/runtime framing; VS Code's marketplace including browser-family debug adapters), such debuggers clearly exist as realizations of this Type, but no browser-specific breakpoint behaviors (e.g., DOM/network-event stops) are asserted anywhere in the outputs.
- **Exception-breakpoint prevalence**: directly observed in the native engines (catchpoints) and in the protocol (`setExceptionBreakpoints`); not on the fetched pages of the JVM-pole product — asserted as common, not universal.
- **Stop-scope semantics** (whether a pause stops one thread or all threads): product-specific modes are documented (GDB all-stop/non-stop); the canonical document therefore states only that semantics vary and are user-visible.
- **Market-share claims** (which engine dominates which segment): not researched; no share numbers appear in the outputs.
- **GDB observer mode / non-stop mode details**: only chapter/section titles were consumed; no operational specifics asserted.

## Final Synthesis

A Debugger is defined by a three-part core, held jointly: **(1) a control relationship** with a specific program's execution — the tool launches the program under supervision, attaches to it while it runs, or opens a captured execution snapshot; **(2) the declared pause** — execution stopped at chosen points or on chosen events, surfaced as the tool's central event with reason and location; **(3) inspection of the stopped state in the program's own execution terms** — position, call stack, variable values in scope, and expression evaluation in the program's context, at whatever semantic level the program itself lives (source, VM, or machine).

Around that core, mature products add a stable standard capability set: the continue/step-over/step-into/step-out control trio, a breakpoint family (conditional, function, logpoint, exception, data watchpoints), watch expressions, state modification, thread handling, multi-session operation, persistent launch configurations, remote debugging, symbol/symbolication machinery, and a packaging split between debugging engines and interchangeable front ends (protocol adapters). Variant structure depends on the substrate (machine vs VM vs hosted runtime) and the mode (live vs post-mortem), plus rare capabilities (reverse execution, tracepoints, live code replacement, AI assistance) that remain optional.

The Type holds its ground on every boundary: without control it is a profiler or error tracker; without the pause it is logging; without program-term inspection it is an artifact dumper; without the program it is an editor.
