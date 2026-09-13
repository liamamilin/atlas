# Debugger

## Overview

A **Debugger** is a tool that takes a running program under its control so a developer can stop that program at chosen points, examine what it is actually doing at those moments, and advance it step by step to find the cause of incorrect behavior.

It answers questions no other development tool answers directly: *Where exactly is the program right now? How did execution get here? What values did the variables actually hold?* Rather than reading code or scanning logs, the developer observes the program's real state while it is frozen and drives it forward one statement at a time.

The defining core is small — three structures that must all be present:

```text
Program under debug
└── taken under the debugger's control
    (launch under supervision · attach to a running program · open a captured snapshot)
    └── The declared pause
        (execution stopped at chosen points or on chosen events)
        └── Inspection of the stopped state
            in the program's own execution terms
            (current position · call stack · variables · expression evaluation)
```

Everything else commonly associated with debugging — stepping buttons, watch windows, conditional breakpoints, logpoints, thread panels, remote debugging — is standard capability layered on this core, and is not what makes a tool a debugger. A tool that only aggregates error reports, only measures performance, or only writes log lines is a different kind of application, however much it helps with defects.

## Users & Context

The primary user is a **software developer** investigating why a program behaves incorrectly or unexpectedly — a crash, a wrong value, a stalled request, a test that fails. Typical working context:

- writing or maintaining code in an editor or IDE, with the debugger one keystroke away
- running the program under the debugger from the start, or attaching to it when a problem reproduces
- debugging a unit test or small script, a local server, a compiled binary, or — via remote or post-mortem modes — software running on another machine or an already-captured snapshot

Secondary users and modes: QA engineers stepping through failing scenarios; engineers debugging code on other machines or devices (remote debugging) or on captured snapshots of crashed processes (post-mortem analysis); tool builders integrating debugger engines into editing tools through adapter protocols.

The debugger is a moment-in-time tool: it is opened when a specific defect needs a specific explanation, used intensively for a focused period, and closed when the cause is understood.

## Core Model

### The Defining Core

**1. Control relationship with the program under debug.** The debugger does not watch from outside; it holds the program's execution. There are three standard ways to establish this relationship, and a mature tool usually offers more than one:

- **Launch** — the debugger starts the program itself, in debug mode, so control exists from the first instruction. The debugger typically manages the program's arguments, environment, and working directory.
- **Attach** — the debugger connects to a program that is already running. The user started the program; the debugger joins it mid-flight. On detach, the program normally continues without the debugger.
- **Captured snapshot (post-mortem)** — the debugger opens a file holding a captured execution state of a process (a core dump in native environments). Nothing can be resumed, but everything can be inspected. This is a long-standing, fully recognized mode of debugging.

**2. The declared pause.** The debugger's central event is the stop: execution is frozen at a point the user declared in advance (a **breakpoint**), or on an event the program hit (an exception, a crash), or on demand (a manual pause). Breakpoints attach to the program's own locations — a line of source, a function, an instruction — optionally qualified with conditions. When a stop happens, the debugger surfaces it with its reason and location; this stop is what everything else in the tool exists to serve.

**3. Inspection of the stopped state in the program's own terms.** While stopped, the debugger answers, in the vocabulary of the program itself:

- *Where am I?* — the current execution position, mapped back to the code the developer wrote (the highlighted source line; or, at the machine level, the current instruction).
- *How did I get here?* — the **call stack**: the chain of function calls (stack frames) that led to this point, each frame selectable so its own context can be examined.
- *What are the values?* — the variables and their values in each frame's scope, browsable structurally (an object's fields, an array's elements).
- *What else can I ask?* — evaluation of arbitrary expressions in the program's own language and current context, including calling the program's own functions.

The phrase "in the program's own terms" carries the Type's real breadth. For a **source-level debugger** the terms are source names — variables, functions, lines. For a **machine-level debugger** the terms are registers, memory, and disassembly. For a **managed-runtime debugger** the terms are VM objects and the heap. What is invariant is that inspection happens at the program's own semantic level, not through external artifacts.

### Standard Capabilities

Mature debuggers across the researched sample share a stable capability set on top of the core:

- **Execution control** — continue, pause, **step over** (run the next call without entering it), **step into** (enter it line by line), **step out** (finish the current function and stop on return), run to a chosen location, restart the session. In native debuggers, instruction-level stepping alongside statement-level.
- **Breakpoint family** — function breakpoints (by name, useful when source is unavailable), conditional breakpoints (an expression that must hold, or a hit count), triggered breakpoints (armed by another breakpoint first), **logpoints** (breakpoint machinery that logs a message instead of interrupting), stops on exceptions, and **data watchpoints** that stop when a variable's value changes or is read.
- **Watch expressions** — user-pinned expressions re-evaluated at every stop.
- **State modification** — change a variable's value, rewrite a register, force an early return from a frame, or call a function mid-session to test behavior under conditions that are hard to stage externally.
- **Threads** — list threads, select one, view each thread's own call stack; stop semantics across threads are visible and product-specific.
- **Multiple sessions** — debugging several programs at once (for example a client and its server), with each session's stacks and control kept separate.
- **Launch configurations** — persistent definitions of how to launch or attach (program, arguments, environment, working directory), so a debug session is reproducible.
- **Breakpoint lifecycle** — a requested breakpoint may be unverified or moved if the debugger cannot bind it exactly where asked; this state is shown to the user.
- **Symbol and debug-information machinery** — source-level inspection depends on debug information compiled into or alongside the program; mature native debuggers include symbol lookup, separate debug files, and source-path remapping.
- **Remote debugging** — the controlled program runs on another machine, device, or runtime, with the debugger's UI on the developer's machine, connected through a debug server or agent.
- **Engine/front-end separation** — the debugging engine and the UI are commonly separate components joined by a protocol, so one engine serves many editing tools and one editor serves many engines.

### One Core, Many Substrates

The core is written in conceptual terms; the substrate determines what "state" concretely means:

```text
Concept:            what inspection reads
Native binary:      source lines (via debug info) · machine registers · memory · disassembly
Managed runtime:    objects on the heap · threads managed by the VM · loaded classes
Hosted runtime:     the program's interpreted context · its environment objects

Concept:            how control is established
Implementations:    same-machine process control · attach by process id ·
                    debug-server stubs for remote targets ·
                    runtime-provided debug agents · captured snapshot files
```

## How It Works

### Starting a session

```text
Prepare the program (built with debug information, where applicable)
→ define how to run or attach (launch configuration)
→ the debugger launches the program under supervision
  — or attaches to a running process —
→ register the breakpoints declared in the code
→ the program runs normally until a declared stop fires
```

Debugging a captured snapshot skips the launch step: the debugger opens the snapshot and lands in a permanently stopped state.

### The stop–inspect–advance loop

This is the interaction loop that defines daily use:

```text
The program stops (breakpoint / exception / crash / manual pause)
→ the debugger shows WHERE: the current position, highlighted in the source
→ the developer reads HOW: the call stack, frame by frame
→ the developer reads WHAT: variables in the selected frame,
  drill into structures, hover values in the editor
→ the developer asks MORE: evaluate expressions in the program's context,
  watch a value change across stops, alter a variable to test a hypothesis
→ the developer advances: continue to the next stop,
  or step over / into / out to follow execution statement by statement
→ repeat until the cause is understood
```

The loop is inherently interactive: each stop is an opportunity to ask a new question that no pre-written logging could have anticipated. The developer's mental work — comparing observed values against expected behavior — is the part no tool automates; the debugger's job is to make every step of that observation cheap and exact.

### Ending a session

- A **launched** program is terminated, or the session is detached and the program killed.
- An **attached** program is detached and keeps running without the debugger — attach is non-destructive by design.
- A **post-mortem** session simply ends; the snapshot remains on disk for later re-examination.

## Interfaces

Debugger interfaces fall into distinct shapes; a single product may offer several.

### Command-line session (engine pole)

The classic form, still primary for standalone engines:

- a prompt accepting commands: set breakpoints, run, step, print expressions, inspect frames, threads, memory, registers
- plain-text output as the inspection surface
- configuration through command-line flags and in-session settings

### Embedded debug UI (editor/IDE pole)

The dominant modern form, hosted in an editor or IDE:

- **Editor gutter** — click to set/clear line breakpoints; markers distinguish enabled, disabled, and unverified breakpoints; the current execution line is highlighted during a stop, with values often shown inline or on hover.
- **Debug sidebar/panel** — the inspection home: a **Variables** view scoped to the selected stack frame, a **Watch** section for pinned expressions, the **Call Stack** with one entry per frame, and a **Breakpoints** list managing every breakpoint with its conditions.
- **Debug toolbar** — continue/pause, step over/into/out, restart, stop.
- **Debug console** — a REPL over the stopped (or running) program: evaluate expressions, call functions, view program output. Typically requires an active session.
- **Configuration surface** — launch/attach configurations as files or structured settings.

### Protocol surfaces (integration pole)

For tool builders: a machine interface or adapter protocol through which an editing tool drives the engine — session lifecycle, breakpoint configuration, stop events, and the threads → stack → scopes → variables inspection hierarchy are all protocol operations. This separation is why a modern editor can offer a uniform debugging UI across many languages and runtimes.

## Important Rules / Behaviors

### Debug information is the substrate of source-level debugging

Source-level inspection — source names, line mapping, rich types — depends on debug information carried with the program. Build without it and the debugger falls back to lower-level views or degraded detail. This dependency is structural, not an edge case: it is why "compile for debugging" is a documented build concern.

### The source↔execution correspondence can break

Compilation and optimization relocate code: statements may be reordered, functions inlined, tail calls collapsed. Debuggers compensate where they can, but breakpoints can land on adjusted addresses, and some variables can be unobservable in optimized builds. Minified or transpiled front-end code raises the same correspondence problem at the source level.

### Breakpoints have a lifecycle

A breakpoint is a request. It can be verified (bound to an actual location), unverified (not currently bindable — shown as a hollow or gray marker), or adjusted (bound to a nearby address). Its state can change over the life of a session, and mature tools surface those changes to the user.

### The debugger interferes with the program

Debugging is not passive observation: the program runs under the debugger's control, stops at breakpoints, and may execute developer-supplied expressions — including function calls that can themselves stop at breakpoints or crash the target. Timing and behavior under the debugger can differ from the undisturbed run; timing-sensitive defects sometimes behave differently in a debug session. Products offer varying stop modes (for example, pausing one thread versus the whole process), and these semantics are user-visible.

### Attach and detach are asymmetric with launch

An attached program outlives the debugging session: detach, and it continues. A launched program's life is the session's life. This asymmetry shapes how each mode is used — attach for problems that only reproduce in the real running process, launch for controlled reproduction.

### Post-mortem inspection is read-only

In a captured snapshot nothing can be resumed, stepped, or modified; the debugger's value is complete, repeatable inspection of a state that no longer exists anywhere else. Live modification of program state (set variable, early return, calling functions) belongs to live sessions.

## Variants

- **Standalone engine vs embedded capability** — the same core ships as an independent command-line engine (native development, servers, embedded targets) and as a capability embedded in editors and IDEs (the dominant packaging today). The two poles are joined by adapter protocols; they are one Type, not two.
- **Native vs managed-runtime vs hosted-runtime substrate** — machine-level state (registers, memory) for compiled binaries; VM-level state (heap objects, VM threads) for managed runtimes; interpreted-context state for hosted runtimes. The core model is identical; what the variables view shows differs.
- **Remote debugging** — program and debugger UI on different machines; the standard answer for servers, devices, mobile hardware, and cloud workloads.
- **Post-mortem analysis** — working from captured snapshots of crashed or killed processes; the standard answer for "it died at 3 a.m. on a machine we can no longer reproduce on".
- **Embedded/hardware targets** — debugging code on other processors through debug stubs and probes.
- **Time-travel debugging** — record execution and step backward, or replay a recorded run; a rare, engine-specific capability rather than a standard one.
- **Non-intrusive collection** — breakpoint-like probes that record data without stopping the program (tracepoints); a specialized capability, documented in native engines, for cases where a stop would break the system being diagnosed.
- **AI-assisted debugging** — current-generation editors add AI help for generating debug configurations and reasoning about failures; it sits on top of the core loop, not in place of it.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Code Editor | manipulates program *text*; the debugger manipulates program *execution*. An editor can show code; only a debugger can stop the program and ask it questions. Embedding one in the other is packaging, not merger. |
| Integrated Development Environment / IDE | the integrated whole (editing, building, navigation, testing, debugging). The debugger remains a distinct Type because it exists independently (standalone engines, protocol adapters) and has its own core model. |
| Profiler | nearest neighbor. Aggregates timing and samples over whole runs to answer "where is time spent". It does not stop the program at declared points or inspect a single frozen state. Strip the pause and the program-term inspection from a debugger and you approach the profiler. |
| Error Tracking Platform | consumes *reported artifacts* — error events and stack traces arriving from deployed software — aggregated over many occurrences. No control over any live program, no declared stops, no ability to ask new questions of a stopped state. |
| Log Management / APM / Distributed Tracing | passive, continuous records of running systems, examined after the fact. Logging is what you do instead of debugging when you cannot stop the program; a logpoint is the debugger borrowing the log's shape while keeping breakpoint machinery. |
| Unit / Integration Test Runner | its object is the *outcome* of executing test suites (pass/fail, reports). Debugging a test is a debugger attached to an executable; running the suite is the runner's job. The two interlock when a failing test becomes a debugging target. |

The sharpest seams: against the **Profiler** (stop-and-inspect-one-state vs aggregate-measure-many-runs) and against **Error Tracking** (live control of one program vs reported artifacts from many runs).

## Representative Products

- **GDB (GNU Debugger)** — the canonical standalone command-line debugger for native code; spans launch/attach, remote debugging via debug servers, embedded targets, post-mortem core files, and machine interfaces for front ends.
- **LLDB (LLVM)** — the modern standalone engine pole; documents its full command surface as a direct counterpart map to GDB, and ships its own protocol adapter for tool integration.
- **Visual Studio Code (debugging)** — the editor-hosted pole: a generic debugging UI over per-language debug adapters, with built-in support for the JavaScript/TypeScript/Node.js family and a marketplace of debugger extensions.
- **IntelliJ IDEA (debugger)** — the managed-runtime pole: a JVM debugger embedded in an IDE, whose documented workflow (breakpoints → suspend → examine variables/threads/heap → step → fix without terminating) mirrors the canonical loop.

Together these four cover both product philosophies (standalone engine vs embedded capability), both major substrates (machine-level vs VM-level), and both modes (live vs post-mortem).

## Sources

Research date: **2026-09-07**

- GDB — *Debugging with GDB* (official manual, Tenth Edition): https://sourceware.org/gdb/current/onlinedocs/gdb.html/
- LLDB — GDB to LLDB command map (official documentation): https://lldb.llvm.org/use/map.html
- Visual Studio Code — *Debug code with Visual Studio Code* (official documentation): https://code.visualstudio.com/docs/editor/debugging
- IntelliJ IDEA — *Debug code* (official documentation): https://www.jetbrains.com/help/idea/debugging-code.html
- Microsoft — *Debug Adapter Protocol* — landing page and overview: https://microsoft.github.io/debug-adapter-protocol/ , https://microsoft.github.io/debug-adapter-protocol/overview

> Sourcing limitation: browser developer-tools documentation (the hosted-runtime pole) was unreachable during research (repeated fetch timeouts on 2026-09-07). No browser-specific debugging behaviors are asserted in this document. All capability claims above are grounded in the five reachable official sources; capability availability that varies by engine (logpoints, exception stops, data breakpoints) is stated as common rather than universal, consistent with the capability-negotiation model documented in the Debug Adapter Protocol.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
