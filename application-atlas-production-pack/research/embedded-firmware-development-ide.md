# Research Notes — Embedded / Firmware Development IDE

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what an Embedded / Firmware Development IDE actually is as an Application Type: what objects exist in its world, what the edit→build→run loop looks like when the code runs on different hardware than the machine the developer sits at, which capabilities are definitional vs common vs optional, and where the boundary lies against the general IDE, code editors, PLC programming environments, and device-testing platforms.

## Initial Boundary (hypothesis before research)

- Core use: authoring, building, loading, and debugging software (firmware) that executes on embedded hardware — microcontrollers (MCUs), microcontrollers/SoCs, boards — where the development machine (host) is physically and architecturally distinct from the execution machine (target).
- Likely defining twist vs a general IDE: the host↔target split. A general IDE's run/debug loop executes on the host; an embedded IDE's loop must cross a hardware boundary (cross toolchain, image transfer, on-target inspection).
- Likely users: embedded firmware engineers, driver/bring-up engineers, IoT device developers, maker/hobbyist tier.
- Nearest neighbors: Integrated Development Environment / IDE (parent), Code Editor, Debugger, Build Automation System, PLC Programming Environment, Device Testing Platform, Mobile App Development Platform, Game Engine, ECAD/PCB Design.
- Open questions going in: how universal on-target interactive debugging is across market tiers; whether hardware-configuration/code-generation tooling is definitional or vendor-specific; how simulator-only flows fit.

## Research Questions

1. What are the core objects (project, target device, build configuration, image, debug session, probe/connection, peripheral/register views)?
2. How does the canonical edit → build → transfer → run → inspect loop work, step by step, in real products?
3. How is the target declared, and what does the build adapt (toolchain, flags, memory layout, startup code)?
4. How does the developer observe and control the running target (probe-based run control, serial console, RTOS awareness)?
5. Is hardware configuration / code generation (pins, clocks, peripherals) definitional or a common implementation?
6. What variants exist (chip-vendor IDE vs toolchain-vendor IDE vs ecosystem/plugin vs maker IDE; bare-metal vs RTOS vs embedded Linux)?
7. Where exactly is the boundary against the general IDE, the PLC environment, and device-testing platforms?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| PlatformIO IDE (for VS Code) | toolchain-agnostic ecosystem/plugin on a generic editor | professional + maker | Tier 1 (official docs, rich) |
| ESP-IDF Extension for VS Code | vendor framework + toolchain delivered through a generic editor | professional | Tier 1 (official docs, rich) |
| STM32CubeIDE | chip-vendor free IDE (ST), device-family-scoped | professional + maker | Tier 2 (official product page + feature list) |
| SEGGER Embedded Studio | independent toolchain-vendor commercial IDE, multi-architecture | professional | Tier 2 (official product page, detailed) |
| Renesas e² studio | chip-vendor IDE (Eclipse CDT-based), device-family-scoped | professional | Tier 2 (official product page, detailed) |
| Arduino IDE 2 | maker/education tier, maximal simplification | hobbyist/student | Tier 1 (official docs via source repo; docs site itself unfetchable) |

Rejected/abandoned samples: Keil MDK (keil.com and developer.arm.com both returned 403 — abandoned after 2 attempts), Microchip MPLAB X (microchip.com 403, developer site timeout — abandoned), NXP MCUXpresso (404). The commercial-toolchain-vendor pole is covered by SEGGER; the chip-vendor-IDE pole is covered twice (STM32CubeIDE, e² studio).

## Sources

Fetched 2026-09-08:

- PlatformIO — "PlatformIO IDE for VSCode" (official docs): https://docs.platformio.org/en/latest/integration/ide/vscode.html — Tier 1
- Espressif — "ESP-IDF Extension for VSCode" (official docs, index + flash + debug pages): https://docs.espressif.com/projects/vscode-esp-idf-extension/en/latest/index.html , .../flashdevice.html , .../debugproject.html — Tier 1
- Arduino — IDE 2 docs hub: https://docs.arduino.cc/software/ide/ (fetched; SPA content thin) + "How to upload a sketch with the Arduino IDE 2" (official docs source, GitHub-hosted markdown): https://raw.githubusercontent.com/arduino/docs-content/main/content/software/ide-v2/tutorials/getting-started/02.ide-v2-uploading-a-sketch/ide-v2-uploading-a-sketch.md + arduino-ide README: https://raw.githubusercontent.com/arduino/arduino-ide/main/README.md — Tier 1
- STMicroelectronics — STM32CubeIDE product page: https://www.st.com/en/development-tools/stm32cubeide.html — Tier 2
- SEGGER — Embedded Studio product page: https://www.segger.com/products/development-tools/embedded-studio/ — Tier 2
- Renesas — e² studio product page: https://www.renesas.com/e2studio — Tier 2

Unreachable (recorded per source-access limitation rules): keil.com / developer.arm.com (403), microchip.com (403/timeout), nxp.com (404), wiki.st.com (timeout ×2), docs.arduino.cc tutorial pages (empty SPA responses; recovered via the official docs-content source repository).

---

## Product Observations

### PlatformIO IDE for VS Code (evidence layer A)

From official docs (docs.platformio.org, "PlatformIO IDE for VSCode"):

- Project creation: "New Project" → **select a board** → project created. Board selection is the first-class step.
- Project configuration file `platformio.ini` carries the target declaration: `platform` (chip family/ecosystem), `framework` (e.g. arduino), `board` (specific board), plus `upload_port`, `build_flags`, `lib_deps` (library dependencies), monitor options (`monitor_port`, `monitor_speed`, `monitor_filters`).
- Toolbar: **Build / Upload / Clean / Serial Port Monitor / Terminal** + project-environment switcher (multiple `[env:...]` environments per project).
- Project Tasks: Build, Upload, Clean, Monitor per environment; custom tasks; multi-project workspaces.
- Debugging (requires PlatformIO account): variable explorer (local/global/static), conditional breakpoints, expressions and watchpoints, **generic registers**, **peripheral registers**, **memory viewer**, **disassembly**, multi-thread support, hot restart of a debug session. Debug uses a dedicated **debug build configuration** ("PIO Debug" runs a Pre-Debug task and builds with the debug configuration).
- Serial Port Monitor with configurable port/speed/parity/filters; auto-close monitor before upload/testing (setting `autoCloseSerialMonitor` default true).
- Library management, platforms, boards, frameworks as managed package concepts.
- Key bindings: Build, Upload, Debug, Serial Monitor.

### ESP-IDF Extension for VS Code (evidence layer A)

From official docs (docs.espressif.com). The documentation's own chapter sequence is the workflow: Prerequisites → Install ESP-IDF and Tools → **Start a Project → Connect Your Device → Configure Your Project → Build Your Project → Flash onto the Device → Monitor the Output → Debug Your Project**.

- Positioning: "develop, build, flash, monitor, debug, and manage projects targeting Espressif chips".
- Flash page: **select the serial port** → **flash the project** choosing method **UART, JTAG, or DFU**; JTAG requires selecting the **OpenOCD board configuration** for the hardware; flashing runs as a task with terminal output ("Flash Done").
- Debug page: debug session = **OpenOCD server** (GDB port 3333, Telnet 4444, TCL 6666) + **GDB debug adapter** connecting VS Code to the target; `launch.json` with `program` = built **ELF file**, toolchain GDB resolved per target chip; initial hardware breakpoint at app entry; **hardware-watchpoint limit resolved per target**.
- Debug instruments: navigate call stack and threads; set/clear breakpoints; halt target manually; step into/over/out; watch and set program variables; conditional breakpoints; **disassembly view**; watchpoints (data breakpoints); send GDB commands; **peripheral view populated from SVD files**; post-mortem debugging via **core dump or GDB stub**; image viewer for raw pixel buffers.
- Options: `buildFlashMonitor` (build + flash + launch monitor before debug), `verifyAppBinBeforeDebug` ("verify that current ESP-IDF project binary is the same as binary in chip").
- Other features: new project wizard, SDK configuration editor (menuconfig-style), **partition editor**, **eFuse viewer**, NVS partition editor, **size analysis of binaries**, serial port selection, multiple configurations per project, multiple projects per window, **QEMU emulation** of debug and monitor output, unit testing, application/system tracing, Docker/WSL support.

### Arduino IDE 2 (evidence layer A for upload flow; docs hub for the rest)

From official docs (upload tutorial + docs hub + README):

- Unit of work: the **sketch**, uploaded to an Arduino **board**.
- Two operations: **Verify** ("goes through your sketch, checks for errors and compiles it") and **Upload** ("does the same, but when it finishes compiling the code, it also uploads it to the board").
- Target declaration: toolbar **dropdown showing connected boards**; "Select other board and port…"; or **Tools > Board** and **Tools > Port**. Board Manager installs **board packages**; Library Manager installs libraries.
- Serial Monitor and Serial Plotter for observing the running board.
- Debugger exists for supported boards with debug probes (tutorial covers Zero board, J-Link, Atmel-ICE) — i.e., on-target interactive debugging is probe-gated, not universal across the tier.
- Architecture: IDE 2 based on Theia; "backend operations such as compilation and uploading are offloaded to an arduino-cli instance running in daemon mode". Cloud sketch sync (Remote Sketchbook) available.
- OS-level rule surfaced in docs: Linux serial-port permission (dialout group) needed for upload and Serial Monitor.

### STM32CubeIDE (evidence layer A for feature list; page is Tier 2)

From official product page (st.com):

- Positioning: "Integrated Development Environment for STM32"; "an environment for editing, compiling, and debugging"; multi-OS C/C++ IDE for STM32 code development.
- Two variants: Eclipse-based (2019) and **VS Code-based (2025)**; ST is focusing resources on the VS Code variant as primary IDE platform. Supports all STM32 MCUs and MPUs (Eclipse variant) / all STM32 MCUs (VS Code variant).
- Feature list: powerful C/C++ editor; **GCC and Clang toolchains**; **ST-LINK and J-Link debug probes**; debug features: **breakpoints, CPU core registers, memory view, live data, SFR registers, RTOS debug, fault analysis**.
- Ecosystem: used with **STM32CubeMX** ("graphical configuration tool") and STM32CubeProgrammer; compatible with vertical tools (TouchGFX Designer, motor control workbench, STM32Cube AI Studio).

### SEGGER Embedded Studio (evidence layer A for feature set; page is Tier 2)

From official product page (segger.com):

- Positioning: "The all-in-one IDE for **building and deploying** embedded applications"; editor, compiler, debugger, and simulator "all in a single application".
- How-it-works diagram: **Set up project → Write code → Build firmware → Debug application**.
- Built-in toolchains: SEGGER (Clang-based) and GCC; external toolchains (LLVM, IAR, ARM/Keil compiler) can be used. Multi-architecture: **Arm, RISC-V**.
- Tool set: **package manager** (libraries, tools, **board-support packages**), **project manager** (files, **build configurations**, dependencies), code editor, code analyzers (memory analysis, **static stack analysis**, static code analysis, trace and profile), embedded-optimized runtime library, **graphical debugger** ("seamless integration with J-Link"), **RTOS awareness plug-in** (task activity and stack use during debugging), **instruction-set simulator** (emSim — "writing and testing application programs with **no hardware present**").
- Licensing: commercial license; free for non-commercial/education; **silicon-vendor buyouts** — free commercial licenses tied to specific vendors' devices (Nordic, Renesas, GigaDevice, HPMicro, SemiDrive named).

### Renesas e² studio (evidence layer A for feature set; page is Tier 2)

From official product page (renesas.com):

- Positioning: "Eclipse-based integrated development environment (IDE) for Renesas MCUs… covers build (editor, compiler and linker control) as well as debug interface"; "covers all development processes, from the downloading of sample code to debugging".
- Project creation: wizard — **select the MCU and the compiler** → generates a project including basic sample code; "immediately start building or debugging".
- **Smart Configurator**: "easily set clocks, pins, and interrupts of the MCU… then automatically generate code which includes those settings"; middleware import.
- Build: compiler choice from Renesas or partner vendors; GUI toolchain setup "automatically generates a 'makefile'".
- Debug: standard GDB functions (register values, memory operations, breakpoints, execution control) plus "real-time memory display, real-time tracing, **peripheral register display**, and breaks by events in the hardware"; emulators E2, E2 Lite, E20, or J-Link.
- Debug views (video/documentation titles): Register view, Disassembly view, Memory view, **IO Registers (SFR) view**, Breakpoints view, Expressions view, Profile view (execution time/counts per function), **RTOS Resources view**, **Stack Analysis view**.
- Extensibility: Eclipse plug-in architecture; QE tools (capacitive touch tuning, display tuning); project import from other Renesas IDEs (CS+, HEW).
- Device families: RA, RZ, RL78, RX, RH850, RISC-V MCU.

---

## Cross-product Comparison

| Structure | PlatformIO | ESP-IDF ext | Arduino IDE 2 | STM32CubeIDE | SEGGER ES | e² studio |
|---|---|---|---|---|---|---|
| Device/board selection as first-class step | A (board in New Project + ini) | A (target chip; OpenOCD board config) | A (board dropdown / Board Manager) | A (STM32-scoped product) | A (device support list, board-support packages) | A (MCU selection in wizard) |
| Cross build → target image | A (Build task; toolchains per platform) | A (build; ELF program for debug) | A (verify/upload compile) | A (GCC/Clang toolchains) | A (build firmware; compiler+linker) | A (build; makefile generation) |
| Integrated transfer to target | A (Upload) | A (Flash: UART/JTAG/DFU) | A (Upload) | B (probes + ecosystem programmer; flash-and-run not stated on fetched page) | A ("building and deploying"; debugger+J-Link) | B (emulator-integrated debug; download implied, not stated on fetched page) |
| On-target interactive debugging | A (full instrument list) | A (full instrument list) | A-conditional (probe-gated, supported boards) | A (breakpoints, core registers, memory, SFR, RTOS debug, fault analysis) | A (graphical debugger + J-Link) | A (GDB + emulator views) |
| Serial console/monitor | A (Serial Port Monitor) | A (IDF Monitor) | A (Serial Monitor/Plotter) | not on fetched page | not on fetched page | not on fetched page |
| Hardware configuration / code generation | not native (framework-delegated) | A (SDK config editor, partition editor) | not native (board packages abstract it) | A via ecosystem (CubeMX companion) | not on fetched page | A (Smart Configurator: clocks/pins/interrupts → code) |
| Package/board/library management | A (platforms/frameworks/boards/libraries) | A (tools install, component registry) | A (Board + Library Manager) | B (ecosystem downloads) | A (package manager, BSPs) | A (FSP installer, plug-ins) |
| Simulator / emulation | not on fetched page | A (QEMU) | — | not on fetched page | A (instruction-set simulator) | not on fetched page |
| RTOS awareness | B (multi-thread debug) | B (threads in GDB) | — | A (RTOS debug) | A (RTOS plug-in) | A (RTOS Resources view) |
| Size/stack analysis | not on fetched page | A (size analysis) | — | not on fetched page | A (static stack analysis) | A (Stack Analysis view) |
| Multi-environment / multi-target builds | A (env switcher) | A (multiple configurations) | — | — | A (build configurations) | A (compiler choice) |
| Post-mortem (core dump) | — | A | — | — | — | — |
| CI/cloud integration | B (CI docs section) | B (Docker/WSL) | B (cloud sketch sync) | B (VS Code variant pitched for CI/CD) | — | — |

Legend: A = directly observed in official docs for that product; B = cross-product/common inference only (not directly observed for that product in this pass); — = not observed.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

An Embedded / Firmware Development IDE is a development environment whose edit→build→run loop is bound to **separate target hardware**, realized through three jointly-held structures:

1. **Declared target hardware** — the project names a specific embedded device/board (selected from a device or board catalog) that is physically distinct from the machine running the IDE. Remove → generic IDE/code editor with no embedded subject.
2. **Cross build producing a target image** — the environment drives a toolchain that compiles and links the source into an executable image for the target's architecture, constrained by the target's memory layout. Remove → editor with a host build, or a bare build-automation pipeline.
3. **Integrated transfer of the image onto the target** — a built-in operation (upload/flash/program/download) that loads the built image into the target device over a physical connection (serial/USB/debug probe), so the code executes on the device. Remove → a flash-programmer utility plus an editor, or an IDE that can never reach its own subject.

Jointly-held is load-bearing: 1 without 2+3 = device catalog browser; 2 without 1+3 = cross-compiler build setup (build automation, not an IDE); 3 without 1+2 = standalone programming tool; 1+2 without 3 = IDE whose workflow never reaches the device; 1+3 without 2 = flashing tool with an editor.

The IDE substrate itself (source editing, build management, run/debug management) is inherited from being an IDE; the three structures above are the delta that makes the Type "embedded/firmware".

### L1 — Common Mature Structure

Present in essentially all mature modern products; expected by the market but not required to recognize the Type:

- **On-target interactive debugging** through a debug probe/emulator: run control (run/halt/step/continue), breakpoints (with hardware-breakpoint limits surfaced on MCUs), call stack/threads, variables/watch, core registers, memory view, disassembly. Directly observed in 5/6 samples; in the maker tier it is probe-gated (Arduino IDE 2 debugs only supported boards with a probe). Historical check: Arduino IDE 1.x shipped without a standard debugger and was still universally recognized as an embedded development IDE → belongs here, not in L0.
- **Serial console/monitor** for observing (and interacting with) the running device — the minimal observation channel that needs no probe.
- **Package/board/library management** — installing toolchains, board definitions/board-support packages, frameworks, and libraries (Board Manager, package manager, platform/framework/board model, FSP/component installers).
- **Debug vs release build configurations** (optimization vs debuggability).
- **Size/stack analysis** — image-size and stack-usage inspection, a direct consequence of the constrained-memory reality of targets.

### L2 — Variant / Optional Structure

Depends on segment, vendor posture, or workflow:

- **Hardware configuration & code generation** (pin muxing, clock trees, interrupts, peripheral init code; SDK configuration stores; partition tables). Strong in chip-vendor IDEs (Smart Configurator, CubeMX companion, sdkconfig/partition editor); absent or framework-delegated in the ecosystem and maker poles. Common in one pole, optional overall — deliberately NOT definitional.
- **Instruction-set simulator / QEMU emulation** — develop and debug with no hardware present.
- **RTOS awareness** (task lists, stack usage, RTOS resource views).
- **Post-mortem debugging** (core dump analysis, GDB stub).
- **Multi-environment/multi-target builds** (same sources, several boards/toolchains).
- **Unit testing, tracing, profiling** integration.
- **CI/CD and cloud/remote development** postures (Docker/WSL, cloud sketchbooks, CI-oriented VS Code variant).
- **AI assistance** (era-current; e.g., Copilot integration named for the VS Code-based STM32CubeIDE variant).

### L3 — Vendor-specific Structure (research notes only)

- PlatformIO: `platformio.ini` environment model; PlatformIO account required for debugging; PIO Debug pre-build task.
- ESP-IDF: OpenOCD port layout (3333/4444/6666); `idf.*` settings; SVD-file-driven peripheral view; eFuse/NVS/partition editors; core-dump destination configuration; appimage offset handling.
- Arduino: sketch model; arduino-cli daemon backend; Theia base; Remote Sketchbook; Linux dialout-group procedure.
- ST: Eclipse vs VS Code dual-variant strategy (VS Code variant declared primary focus 2025); CubeMX/CubeProgrammer ecosystem split; TouchGFX/motor-control/AI Studio verticals.
- SEGGER: emRun runtime, emSim simulator, STOP stack-overflow prevention; silicon-vendor license buyouts (Nordic/Renesas/GigaDevice/HPMicro/SemiDrive named).
- Renesas: Smart Configurator, QE tool family, CS+/HEW project migration, family-scoped information pages.

## Vendor-specific Findings

(See L3; none of these enter the canonical document beyond neutral examples.)

## Boundary Findings

**vs Integrated Development Environment / IDE (general).** The general IDE's run/debug loop executes on the host machine (or a local runtime it controls). The embedded IDE's loop crosses a hardware boundary: the run target is separate hardware reached through a cross build and an image transfer. Remove-test: remove the declared target + cross build + on-device transfer → the product collapses into the general IDE Type. The directory carries both leaves; the seam is exactly the host↔target bridge. (Flagged for joint review with the IDE leaf.)

**vs Code Editor.** A code editor with extensions can edit C/C++ and even invoke a cross toolchain as an external task, but has no integrated device/board model, no transfer operation, no on-target debug session. Remove the bridge → code editor territory.

**vs Debugger (standalone) / probe tooling.** Debug probes and their host tools (and OpenOCD-class servers) are components the IDE orchestrates; the standalone Debugger Type lacks the authoring + build + transfer loop.

**vs Build Automation System / toolchain CLI.** The same pipeline exists as CLI (arduino-cli daemon, idf.py-class CLIs, makefile generation observed in e² studio). Remove the interactive editing/debugging environment → build automation, not an IDE.

**vs PLC Programming Environment.** PLC environments also build, download to hardware, and debug on-target — the superficial loop is similar. The distinction is the programming/runtime model: embedded/firmware IDEs center on C/C++ (increasingly Rust) source compiled to a bare-metal or RTOS image with register-level hardware access and a memory-map-bound image; PLC environments center on industrial control semantics (control-logic languages, scan-cycle runtime, field I/O configuration). Remove-test: replace C/C++ register-level firmware authoring with control-logic languages over a scan-cycle industrial runtime → PLC Programming Environment. (To be confirmed from the PLC leaf's own pass; flagged in Boundary Issues.)

**vs Device Testing Platform.** Device testing runs *completed applications* across a device catalog for QA (remote sessions, automated suites); the embedded IDE *authors the firmware itself* for one declared target. Different unit of work (test run vs firmware image), different direction (consume apps vs produce images).

**vs Mobile App Development Platform / Game Engine.** Both also target devices/emulators, but through a managed runtime (OS + app framework / platform SDK): the load step is app installation, not firmware imaging; no bare-metal memory map or register-level model. Remove the bare-metal image model → those Types.

**vs ECAD / PCB Design.** Adjacent inside vendor ecosystems (the IDE targets the chips the ECAD tools put on boards) but different objects: hardware design vs software for that hardware.

**Simulator-only development.** A thin pole: with simulators (instruction-set simulator, QEMU), a session may never touch hardware. The Type still holds because the transfer capability remains integral to the product (and the simulator stands in for the target). The bridge is to the *target environment*, whether physical or emulated.

## Historical / Market-Sample Check

- 1990s–2000s cross-development environments (Keil µVision for 8051/ARM, IAR Embedded Workbench, classic MPLAB, AVR Studio, CodeWarrior) all satisfy the core: device selection, cross toolchain, device programming, emulator/monitor-based debugging. No cloud, AI, code generation, or package managers in the core.
- Arduino IDE 1.x (no standard debugger) still recognizable → confirms on-target interactive debugging is common-mature, not defining.
- Thinnest ancestor: editor + cross-assembler/compiler + separate device programmer + in-circuit emulator — the *integration* into one environment is what makes it an IDE, but the host↔target bridge predates the IDE packaging.
- Embedded Linux targets (MPU-class boards running Linux) stretch the "firmware image" leg (bootloader/kernel/driver work vs application images); chip-vendor IDEs support them as device families (e² studio RZ, STM32CubeIDE MPUs). Held as a variant, not a boundary break.

## Uncertainties

1. **Integrated flash-and-run in STM32CubeIDE / e² studio**: the fetched pages evidence probe-integrated debugging and the build→debug loop but do not literally document the flash/download step (ST splits programming into STM32CubeProgrammer; Renesas ships separate flash-programmer products). Cross-product commonality (B-layer) makes the transfer leg safe as a Type-level claim; per-product detail left unstated.
2. **Keil MDK / IAR / MPLAB X**: unreachable this pass; the commercial-toolchain pole rests on SEGGER alone. Claims about that pole are calibrated accordingly.
3. **Serial monitor in professional IDEs**: directly observed in the ecosystem/maker poles; not on the fetched professional-IDE pages (likely present but unverified) — held as common-mature with maker-tier direct evidence, not claimed for specific professional products.
4. **Exact hardware-breakpoint limits, flash algorithms, port defaults**: product-specific (e.g., ESP32's two hardware breakpoints is documented for that chip family); deliberately not generalized.
5. **PLC boundary**: reasoned from this side only; the PLC Programming Environment leaf's own pass should confirm the seam.

## Final Synthesis

The Type is an IDE whose defining property is that its whole working loop is bound to hardware other than the machine it runs on. The defining core is the host↔target bridge in three jointly-held legs — declared target hardware, cross build to a memory-layout-bound image, integrated transfer of that image onto the device. Everything else the market associates with embedded IDEs — probe-based on-target debugging, serial consoles, package/board managers, hardware-configuration code generation, simulators, RTOS awareness, size/stack analysis — is standard mature capability or variant structure, not definition. The market realizes the Type in four stable poles (chip-vendor IDE, independent toolchain-vendor IDE, ecosystem/plugin on a generic editor, maker IDE) that differ in packaging and licensing but share the same bridge.
