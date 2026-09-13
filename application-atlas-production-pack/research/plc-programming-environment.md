# Research Notes — PLC Programming Environment

## Research Goal

Understand, from real products, what a PLC Programming Environment is: the engineering software used to author, configure, download, and debug the control programs that run on industrial controllers (PLCs / PACs / machine controllers / soft PLCs). Produce a vendor-neutral canonical model and a clean boundary against neighboring Types (SCADA/HMI, DCS engineering, embedded/firmware IDE, CNC programming, Industrial IoT).

## Initial Boundary (hypothesis before research)

- Core use: authoring the control program of an industrial controller; configuring that controller's hardware and I/O; transferring the program to the controller; monitoring/debugging it online.
- Users: controls/automation engineers, system integrators, machine builders, maintenance engineers.
- Likely confusions: SCADA/HMI (operator visualization), DCS (plant-wide control engineering), Embedded/Firmware IDE (general firmware), CNC programming (part programs).
- Unknowns: exact object model per product; how offline/online difference tracking works; role of simulation; how safety programming is packaged.

## Research Questions

1. What is the core object model? (project, device/hardware configuration, POUs, variables, tasks, libraries)
2. Which programming languages does the Type use, and how is the language set standardized?
3. What is the edit → compile → download → online-monitor → debug loop, exactly?
4. How is hardware configured and how do program variables bind to physical I/O?
5. What does "online mode" expose (monitoring, breakpoints, writing values, device diagnostics, offline/online difference tracking)?
6. What runs without hardware (simulation)?
7. How are safety programs, motion, and HMI authoring packaged relative to the core?
8. How do version control and team development work?
9. Who uses the tool and in which roles?
10. Where is the boundary vs SCADA/HMI, DCS, embedded IDE, CNC programming?

## Representative Products

Selected for market representativity, documentation completeness, different product philosophies, different geographies and customer tiers:

| Product | Vendor | Philosophy / pole | Official sources reachable |
|---|---|---|---|
| CODESYS Development System | CODESYS Group | vendor-independent IEC 61131-3 platform; IDE + runtime licensed to many device makers | Yes (site + online help, Tier 1) |
| TwinCAT 3 (TE1000 XAE) | Beckhoff | PC-based control; engineering inside Microsoft Visual Studio; IEC 61131-3 + C++/MATLAB/Simulink | Yes (Tier 2) |
| SIMATIC STEP 7 in TIA Portal | Siemens | integrated engineering framework (PLC + HMI + drives in one portal); SIMATIC-only | Yes (Tier 2) |
| Sysmac Studio | Omron | machine automation IDE (logic + motion + robotics + HMI + vision + safety + 3D simulation) | Yes (Tier 2) |
| Studio 5000 Logix Designer | Rockwell Automation | North-American ladder-centric pole | **No — rockwellautomation.com 404 ×3; abandoned per network rule** |

Schneider EcoStruxure Control Expert (se.com 403 ×2) and Mitsubishi GX Works3 (mitsubishielectric.com 404 ×2) were also attempted and abandoned; ia.omron.com 403 but industrial.omron.eu reachable.

## Sources

All fetched 2026-09-09.

- CODESYS — corporate site root: https://www.codesys.com/ (Tier 2)
- CODESYS — Development System product page: https://www.codesys.com/products/engineering/development-system/ (Tier 2)
- CODESYS — Online Help, Overview: https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_development_system.html (Tier 1)
- CODESYS — Online Help, Creating and Configuring a Project: https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_struct_project_creation.html (Tier 1)
- CODESYS — Online Help, Device Tree and Device Editor: https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_device_tree_device_editor.html (Tier 1)
- CODESYS — Online Help, Testing and Debugging: https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_struct_test_application.html (Tier 1)
- CODESYS — Online Help, Downloading an Application to the PLC: https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_struct_application_transfer_to_plc.html (Tier 1)
- Beckhoff — TwinCAT overview: https://www.beckhoff.com/en-en/products/automation/twincat/ (Tier 2)
- Beckhoff — TE1000 TwinCAT 3 Engineering: https://www.beckhoff.com/en-en/products/automation/twincat/texxxx-twincat-3-engineering/te1000.html (Tier 2)
- Siemens — TIA Portal: https://www.siemens.com/en-us/products/tia-portal/ (Tier 2)
- Siemens — STEP 7 (TIA Portal): https://www.siemens.com/en-us/products/tia-portal/step7/ (Tier 2)
- Omron — Sysmac Studio: https://industrial.omron.eu/en/products/sysmac-studio (Tier 2)
- PLCopen — Standards: https://www.plcopen.org/iec-61131-3 and https://www.plcopen.org/standards/logic/ (standard body)

Unreachable (1–2 attempts each, then abandoned): rockwellautomation.com (404 ×3), se.com (403 ×2), mitsubishielectric.com (404 ×2), ia.omron.com (403).

## Product Observations

### CODESYS Development System (evidence layer A unless noted)

- Self-description: "The CODESYS Development System is the IEC 61131-3 programming tool for controller and automation technology"; "the core of the software platform"; platform = development system + runtime ("PLC runtime system / SoftPLC / virtual PLC") for different device platforms.
- Positioning: "Use the leading programming software to efficiently program industrial controllers such as PLCs, PACs, ECUs, and building controllers."
- Editors: "All IEC 61131-3 editors (FBD, LD, IL*, ST, SFC)" plus CFC variants; IL marked obsolete by PLCopen and no longer maintained (can be enabled).
- Project model (help, Tier 1): "A project contains the objects which are necessary to create a controller program ('application')": pure POUs (programs, function blocks, functions, GVLs) plus objects required to run the application on a PLC (task configuration, Library Manager, symbol configuration, device configuration, visualizations, external files). Multiple applications and multiple controller devices per project. Device-specific POUs live in the Devices view ("device tree"); project-wide POUs in the POUs view.
- Device tree (help, Tier 1): "you organize applications according to target device… see the PLC hardware and fieldbus systems, configure the hardware communication, and assign applications." Device objects represent "a controller, fieldbus, bus coupler, drive, I/O module, or monitor." Devices come from a local device repository via device description files; hardware can be scanned from a live network ("scan the hardware for available devices"). Programmable devices get a "PLC Logic" node holding applications; "Below each application, you need to insert a task configuration and configure the respective program calls."
- Device editor: "configure device communication, parameters, and IO mappings."
- Compile/download (help, Tier 1): program must compile without errors; connection settings required; "the application is downloaded to the PLC at login." Encrypted/restricted communication requires certificates and permissions.
- Online mode (help, Tier 1): device-tree status symbols (connected/running, connected/STOP, bus error, trial mode, diagnosis pending…); connected devices highlighted; simulation-mode devices shown in italics. POU name colors encode offline/online state: gray = unused; blue = "changed as compared to the POU on the controller and will be included with the next download."
- Debugging (help, Tier 1): "start your application in simulation mode, even without connecting any hardware. Using breakpoints and stepping commands, you can examine specific parts of a program. By writing values to variables, you can influence the running program." Reset commands at varying degrees (non-persistent variables → factory settings). "Online Config Mode" allows referencing/testing I/O before an application is downloaded.
- Product page: "Extensive debugging and online features for troubleshooting, optimizing the application code, and speeding up testing and commissioning, such as breakpoints, variable monitoring, sequence control"; integrated compiler for many CPU platforms; comprehensive project comparison "also for graphical editors"; library concept for reuse; OOP per IEC 61131-3 3rd edition (optional, mixable with functional style); project exchange via PLCopen XML and proprietary formats; project archive; source control (SVN named in help); security (project protection, application encryption, device user management, certificates, dongles, passwords); integrated companion tools (Visualization, SoftMotion, Application Composer); packages/licenses extend the IDE.
- Runtime side: SoftPLC for many platforms; virtual controllers on IT hardware; free Development System download with a demo SoftPLC (Control Win SL).

### TwinCAT 3 / TE1000 XAE (Beckhoff)

- Engineering/runtime split: "TwinCAT XAE (eXtended Automation Engineering) allows hardware to be programmed and configured in a single engineering tool. In addition to the IEC 61131-3 programming languages, C/C++, MATLAB® and Simulink® are also available for programming. The tool even offers integrated debugging options for the program code and diagnostic functionalities for the control hardware." Runtime XAR executes the code in real time on PC-based control.
- TE1000 page: "the TwinCAT development environment for convenient configuration of control, drive control and I/Os. In addition, the tool includes the configuration and programming of TwinSAFE" (safety).
- "TwinCAT 3 Engineering is integrated in a Visual Studio version… Pure configurations or PLC programming can be performed in the free Visual Studio shell included. A connection to source code control tools is fully integrated. The programming of the PLC also takes place here. More than one PLC can be created and programmed. The inputs and outputs of the PLC can be linked to the inputs and outputs of the I/Os. The programs can be monitored and debugged online."
- Features: IEC 61131-3 (IL, ST, LD, FBD, SFC) and CFC editors; IEC 61131-3 compiler; "integrated system manager for the configuration of the target system"; instancing/parameterization of TwinCAT modules; C++ debugger; MATLAB/Simulink module parameterization UI; .NET projects in the same solution (e.g., HMI); Scope View charting for commissioning; Bode Plot for drive-axis optimization.
- Engineering area definition: "all components and products that can be used for configuring, programming, simulating, diagnosing and debugging user programs or applications. These components are mostly installed and used on the engineering PC."
- Overview page: Git source control, CI/CD in the engineering workflow; modular Functions (HMI, Measurement, Motion, Vision, Connectivity); engineering free of charge, runtime licensed.

### SIMATIC STEP 7 in TIA Portal (Siemens)

- TIA Portal: "One platform for efficient engineering… guides you through the entire engineering lifecycle – from intuitive hardware configuration and efficient engineering workflows to accelerated commissioning and machine optimization." "Integrated engineering: Automation components are integrated so that everything can be programmed." Simulation: "Use virtual representations of machines and systems to simulate and test every aspect before building the real thing."
- STEP 7: "The comprehensive engineering tool to configure, program, test, and diagnose all SIMATIC controllers intuitively and efficiently"; "the engineering software for configuring and programming SIMATIC controllers"; "STEP 7 Professional (TIA Portal) can be used to configure, program, test and diagnose all generations of SIMATIC controllers"; STEP 7 Basic is "the price-optimized subset."
- Engineering aids: drag & drop, copy & paste, Auto Complete, "project-wide cross-reference lists."
- Diagnostics: "System diagnostics does not require an additional license. In the engineering phase, diagnostics is activated with just one click. All user programs can be precisely diagnosed and optimized with a real-time trace function."
- Editors: "The editors in STEP 7 (TIA Portal) support graphical programming languages… fully graphical LAD and FBD editors."
- Safety: "All configuration and programming tools required for generating a safety-oriented program are integrated into the STEP 7 user interface."
- Portal companions: WinCC Unified (visualization), SINAMICS Startdrive (drives commissioning), multi-user engineering, MTP, security options.

### Sysmac Studio (Omron)

- "Sysmac Studio Integrated Development Environment… the 1st Industry IDE integrating Logic, Motion, Robotics, HMI, Vision, Sensing, Safety and 3D Simulation in one single platform." Targets NJ/NX controllers, NA HMI, NX I/O, servos, drives, vision systems, network components.
- "One software for motion, logic sequencing, safety, drives, vision and HMI."
- "Fully compliant with open standard IEC 61131-3… a state-of-the-art programming environment based on the ladder diagram, structured text programming languages and on program organization units which include programs, functions, and function blocks. Additionally, motion control instructions that are based on PLCopen standards…"
- "Supports Ladder, Structured text and In-Line ST programming with a rich instruction set"; CAM editor for motion profiles; "One simulation tool for sequence and motion in a 3D environment."
- Team Edition: Git-based distributed version control, project comparison, machine-version handling.
- Sysmac Library: "free online software library lets licensed Sysmac Studio users download rigorously tested Function/Function Blocks."
- Security: "confirmation of Controller names and serial ID's, administrator access rights and controller write protections… authentication of user program execution and password protection for project files."
- Editions: Full / Lite / HMI / Vision / Drives / I/O / Measurement / CNC; Team Development option; 3D Simulation option.

### PLCopen / IEC 61131 (standard body — evidence for the Type's standard substrate)

- "The PLCopen basis is provided by the world wide standard IEC 61131, and especially Part 3 - Programming Languages."
- IEC 61131-1 applies to "programmable controllers (PLC) and their associated peripherals such as programming and debugging tools (PADTs), human-machine interfaces (HMIs)" — the standard itself names the programming/debugging tool as an associated peripheral of the PLC.
- IEC 61131-3: "the only global standard for industrial control programming. It harmonizes the way people design and operate industrial controls by standardizing the programming interface." Languages: graphical Ladder Diagram (LD) and Function Block Diagram (FBD); textual Instruction List (IL) and Structured Text (ST); Sequential Function Chart (SFC) "used to structure the internal organization of a program." "Via decomposition into logical elements, modularization… each program is structured, increasing its re-usability." Current edition 4.0 (2025).
- IEC 61131-10 / PLCopen XML: standardized exchange format for IEC 61131-3 programs.
- PLCopen Safety: "integrates safety functionality into the IEC 61131-3 development environments."
- PLCopen Motion: "reusable, hardware independent Motion Control applications via IEC 61131-3 and PLCopen Function Blocks."

### Studio 5000 Logix Designer (Rockwell Automation) — SOURCING LIMITATION

Official product documentation was not reachable (rockwellautomation.com 404 ×3). No product-specific observations are recorded and no Rockwell-specific claims are made anywhere in this research or the final document. Rockwell's role in the sample is market-structural only: it marks the North-American ladder-centric pole that the reachable sample (CODESYS, TwinCAT, STEP 7, Sysmac Studio) under-represents. The canonical model was derived without it; the historical/market check below compensates conceptually.

## Cross-product Comparison

| Dimension | CODESYS | TwinCAT 3 | STEP 7 / TIA Portal | Sysmac Studio |
|---|---|---|---|---|
| Unit of work | Project (POUs + task config + device config + libraries) | TwinCAT solution in Visual Studio (PLC projects + system manager config) | TIA Portal project (STEP 7 PLC + WinCC + Startdrive) | Sysmac Studio project (logic/motion/HMI/vision/safety in one) |
| Language set | FBD, LD, IL(legacy), ST, SFC + CFC | IL, ST, LD, FBD, SFC + CFC (+ C++, MATLAB/Simulink) | LAD, FBD evidenced (graphical editors) | Ladder, ST, in-line ST |
| POU model | programs, function blocks, functions, GVLs | PLC programs (POU model per IEC) | blocks (implied; "block editor") | programs, functions, function blocks |
| Hardware config | device tree + device repository + network scan | integrated system manager for target system | "intuitive hardware configuration" in portal | integrated (NJ/NX, I/O, servos, vision) |
| I/O binding | "IO mappings" in device editor | "inputs and outputs of the PLC can be linked to the inputs and outputs of the I/Os" | hardware configuration in portal | integrated device targets |
| Tasks | task configuration with program calls | real-time runtime (XAR) executes | commissioning workflows | sequence/motion execution |
| Transfer | compile → download at login | download to runtime; online debug | configure, program, test, diagnose | download to controllers |
| Online | monitor, breakpoints, stepping, write values, device status symbols, offline/online POU colors | "monitored and debugged online" | diagnostics one click, real-time trace | (security + write protection) |
| Simulation | simulated device (Control Win SL), no hardware | "simulating" in engineering scope | virtual representations to simulate/test | 3D simulation of sequence + motion |
| Libraries | Library Manager, library concept | modules/Functions | reusable components | Sysmac Library (tested FBs) |
| Safety | CODESYS Safety products | TwinSAFE config/programming in TE1000 | safety tools integrated in STEP 7 UI | safety in the IDE |
| Version control | SVN named in help | Git fully integrated | multi-user engineering | Git (Team Edition) |
| Companion authoring | Visualization, SoftMotion | HMI, Vision, Measurement | WinCC, Startdrive | HMI, Vision, Robotics, CAM |
| Substrate | vendor-independent; runtime licensed to device makers | PC-based control on Windows | SIMATIC ecosystem portal | Omron machine automation platform |
| Business model | free IDE + licensed runtime/devices | free engineering + licensed runtime | licensed tiers (Basic/Professional) | licensed editions per discipline |

Reading of the table (evidence layer B — cross-product commonality):

- All four reachable products share: project-based engineering on an engineering PC; IEC 61131-3 language family; POU-style program organization; hardware/device configuration of controller + I/O; binding of program variables to physical I/O; compile → download to the controller; online monitoring/debugging/diagnostics against the running controller; libraries; safety authoring; simulation; companion authoring (HMI/motion) inside the same tool.
- They differ in: host shell (standalone IDE / Visual Studio / portal), ecosystem breadth (multi-vendor vs single-vendor), language emphasis, packaging (editions/tiers), and extra machinery (3D simulation, scope/trace tools, AI assistants).

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

A PLC Programming Environment is the engineering software in which a control program for an industrial controller is authored, bound to the controller's hardware and I/O, and transferred to and debugged on the running controller. Three jointly-held structures:

1. **Controller-program authoring in controller-oriented languages** — the control program is the unit of work, organized as reusable program units (POUs: programs, function blocks, functions) written in the controller language family standardized by IEC 61131-3 (LD/LAD, FBD, ST, SFC; IL legacy). Remove → a generic IDE/text editor, not a PLC tool.
2. **Binding of the program to the controller's hardware and I/O** — the project carries a configuration of the controller and its field devices (controller, fieldbus, couplers, drives, I/O modules) and maps program variables onto physical inputs/outputs. Remove → a programming toolchain with no contact with the machine's wiring.
3. **The transfer-and-online-debug loop against the controller** — the compiled program is downloaded to the controller; the engineer then works online against the running (or simulated) controller: monitoring live values, stepping/breakpoints, writing values, reading device diagnostics. Remove → an offline editor only; commissioning and troubleshooting — the tool's reason to exist — disappear.

Jointly load-bearing: (1) alone = generic code editor; (2) without (1) = electrical/fieldbus configuration tool (ECAD territory); (3) without (1)+(2) = a transfer utility with nothing to transfer; (1)+(2) without (3) = offline authoring with no commissioning path; (1)+(3) without (2) = embedded-style firmware tooling without the machine-wiring binding.

### L1 — Common Mature Structure

Present across the reachable sample; expected in mature products but not definitional:

- task configuration binding POUs to cyclic/event execution
- typed variable model (global/local scopes, derived data types)
- libraries of reusable blocks (vendor/system libraries; curated FB libraries)
- simulation without hardware (simulated device / virtual controller / 3D cell simulation)
- device/fieldbus diagnostics inside the tool; offline/online difference tracking (which POUs differ from the controller)
- project comparison (including graphical editors), archives, source-control integration (SVN/Git), multi-user/team development
- security machinery: project/application protection, user management on the device, encrypted/signed communication
- integrated companion authoring: HMI/visualization, motion (PLCopen-style motion FBs, CAM editors), safety programs (separate safety objects/runtimes)
- multi-application / multi-controller projects

### L2 — Variant / Optional Structure

- host shell: standalone IDE (CODESYS) vs general-purpose IDE shell (TwinCAT in Visual Studio) vs portal framework (TIA Portal)
- runtime substrate: dedicated controller hardware vs PC-based soft control vs virtual controller on IT hardware
- language emphasis: ladder-centric vs FBD/ST-centric (regional/tradition axis; sample shows both poles)
- ecosystem breadth: multi-vendor device support via device repositories (CODESYS) vs single-vendor ecosystem (STEP 7/SIMATIC, Sysmac/Omron)
- packaging: free engineering + licensed runtime (CODESYS, TwinCAT) vs licensed tiers/editions (STEP 7 Basic/Professional; Sysmac editions)
- era-current extras: AI coding assistants (CODESYS AI engineering, TwinCAT Chat, Siemens Eigen agent), 3D simulation/digital-twin workflows
- extended language substrates beside IEC 61131-3 (C++/MATLAB/Simulink modules in TwinCAT)

### L3 — Vendor-specific (research notes only)

- CODESYS: device repository/description files, Control Win SL demo runtime, Automation Server, Application Composer, packages/store model.
- Beckhoff: TE/TC/TF product-code modularization, TwinSAFE, Scope View, Bode Plot, platform levels.
- Siemens: TIA Portal companions (WinCC Unified, Startdrive), STEP 7 Basic/Professional split, SIMATIC-only scope, Eigen Engineering Agent.
- Omron: Sysmac Library, CAM editor, 3D Simulation option, edition matrix (Full/Lite/HMI/Vision/Drives/I/O/Measurement/CNC), NJ/NX/NA hardware family.

## Historical / Market-Sample Check

- The IEC 61131-1 definition (standard text, still current) treats "programming and debugging tools (PADTs)" as associated peripherals of programmable controllers — the Type predates modern IDEs and is defined by its relationship to the controller, not by any modern machinery.
- Conceptual test: a standalone ladder editor with a serial/network connection to a controller — no cloud, no Git, no AI, no integrated HMI, no simulation, no multi-language support — satisfies all three L0 structures (authoring in a controller language, I/O binding, download + online monitoring). Conversely, none of the modern extras (Git, AI, 3D simulation, portals) is required to recognize the Type.
- Platform breadth: CODESYS's own positioning spans "PLCs, PACs, ECUs, and building controllers" — the core holds beyond factory PLCs.
- Conclusion: the L0 is not over-fitted to the current integrated-engineering era. The North-American ladder-centric pole is under-evidenced in the reachable sample (Rockwell unreachable); the ladder language itself is standard-substrate (IEC 61131-3 LD), so the model does not depend on any single regional implementation.

## Vendor-specific Findings

See L3 above. Not promoted to the canonical model.

## Boundary Findings

- **vs SCADA/HMI**: SCADA/HMI is operator-facing supervision and visualization over running processes; the PLC programming environment is engineer-facing authoring of the control program. The suites themselves draw the seam by bundling: TIA Portal = STEP 7 (PLC) + WinCC (visualization); TwinCAT = XAE + HMI Functions; CODESYS = Development System + Visualization; Sysmac Studio = logic + HMI. Remove the program-authoring + I/O-binding core and keep operator screens → HMI/SCADA territory.
- **vs DCS engineering**: DCS engineering environments configure plant-wide distributed control (multiple controllers, operator stations, field devices, process control philosophy). Function-block authoring overlaps, but the unit of work differs: per-controller control program vs plant-wide control system configuration. Directory keeps both as separate Types; seam recorded.
- **vs Embedded/Firmware Development IDE**: embedded IDEs author general firmware (C/C++) for microcontrollers via debug probes; PLC environments author controller applications in the IEC 61131-3 family, configure industrial hardware catalogs, map variables to field I/O, and download over industrial networks. TwinCAT deliberately blurs the shell (Visual Studio, C++ modules) but its PLC core remains IEC 61131-3 + I/O binding + online PLC debugging. The invariant that keeps the Types separate is the controller-oriented language model plus machine-wiring binding, not the IDE shell.
- **vs CNC Programming Application**: CNC programming produces part programs (machine-tool machining semantics); the PLC environment produces control logic for automation controllers. TwinCAT/CODESYS ship CNC/motion as extensions of the PLC environment — the PLC environment is the substrate, CNC programming a specialized add-on surface.
- **vs Industrial IoT Platform**: IIoT platforms ingest/analyze data from device fleets; the PLC environment authors the control logic. OPC UA / cloud connectivity appear in PLC environments as communication extensions, not as the core.
- **"去掉什么就变成另一个 Type" 判据**: remove controller-program authoring → fieldbus/ECAD configuration tool; remove hardware/I-O binding → generic IDE; remove transfer/online-debug → offline editor; add operator-facing runtime screens as the primary surface → SCADA/HMI; change the target from industrial controllers to microcontroller firmware → embedded IDE.

## Uncertainties

- Rockwell Studio 5000 (North-American pole) unreachable — the ladder-centric regional implementation is evidenced only through the standard substrate (LD in IEC 61131-3), not through a North-American product's own documentation.
- STEP 7's full language set (SCL/STL/GRAPH) is not evidenced from fetched pages (only LAD/FBD named); no claim made.
- Online-change semantics (modifying a running program without stop) are evidenced for CODESYS only; treated as product-specific, phrased generically in the final document.
- "Force" semantics (permanently overriding I/O) not evidenced in fetched text; only "writing values to variables" (CODESYS) is used.
- Exact per-product task models (cyclic/event/interrupt taxonomies) not uniformly evidenced; described conceptually.
- DCS engineering environments were not sampled; the DCS boundary is reasoned from the directory structure and the PLC-side evidence, not from DCS product documents.

## Final Synthesis

The PLC Programming Environment is the engineer-facing authoring system for industrial control. Its world model: an engineering project that contains (a) a device/hardware configuration of the controller and its field devices with I/O mapping, (b) a control program organized as POUs in the IEC 61131-3 language family with typed variables, (c) a task configuration that binds programs to execution, and (d) commonly libraries, safety objects, and companion authoring (HMI/motion). Its defining loop: author → compile → download to the controller → go online → monitor/debug/diagnose against the running (or simulated) controller → modify and repeat, with offline/online difference tracking keeping project and controller comparable. Everything else — shells, portals, Git, AI, 3D simulation, editions — is implementation or era-current machinery.
