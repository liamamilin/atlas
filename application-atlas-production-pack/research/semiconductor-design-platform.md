# Research Notes — Semiconductor Design Platform

Research date: 2026-09-09

## Research Goal

Understand what the software used to design integrated circuits actually is: what objects it holds, what flows move a chip design from description to manufacturing, what verification disciplines gate progress, what role the silicon manufacturing process plays, and where the boundary with neighboring Types (board-level ECAD/EDA, PCB design, software development tools, FPGA toolchains, CAE simulation) lies. Output: a vendor-neutral Application Document for the directory leaf "Semiconductor Design Platform" (§16 Engineering, Manufacturing & Industrial).

## Initial Boundary

Working hypothesis before research:

- The leaf is the chip-level (IC) side of the industry domain the market calls electronic design automation (EDA) — the Cadence/Synopsys/Siemens-EDA class of tools — as distinct from the board/system-level electrical design already documented under `ecad-eda` (processed 2026-09-07). That pass deliberately did NOT sample IC-level vendors and left the boundary "asserted from directory structure + one vendor's own product-family categorization (not from sampling IC-EDA vendors)" — this pass discharges that flag from this side with fresh IC-vendor evidence.
- Likely confusions: ECAD/EDA (board), PCB Design, software IDE/VCS (HDL is code-like), FPGA implementation toolchains, CAE/system simulation (chip tools simulate too), TCAD (device physics), fab-side manufacturing software (MES/CIM — a different world).
- The word "platform" suggests the full-flow integrated posture of the big vendors, but point tools (standalone simulators, layout viewers) exist as fragments of the same flow — expected to be recorded as a variant/posture, not a separate Type.

## Research Questions

1. What are the core objects? (design database, abstraction levels, libraries, process data, verification artifacts)
2. What is the flow? (front end → implementation → verification → signoff → manufacturing hand-off)
3. How do the digital and custom analog/mixed-signal flows differ, and what is shared?
4. What exactly does "verification" mean here, and what gates it (signoff)?
5. What role does the silicon manufacturing process / foundry play in the tooling?
6. What interfaces do users actually work in? (editors, waveforms, dashboards, batch/compute)
7. What rules genuinely constrain behavior? (process-specific design rules, LVS/equivalence correspondence, timing closure, certification)
8. What are the market variants (digital/analog/RF poles, platform vs point tools, regional ecosystems, open-source pole, FPGA adjacency, 3D-IC extension)?
9. Boundary verdict vs ECAD/EDA and other neighbors — keep separate, merge, or fold?

## Representative Products

| Product | Vendor | Why sampled | Notes |
|---|---|---|---|
| Chip Design platform (Fusion Design Platform / Custom Design Platform / Synplify) | Synopsys | digital IC design leader; full-flow platform posture | product pages + official IC-design glossary fetched |
| Digital Design and Signoff + Virtuoso Studio | Cadence | full-flow + the dominant custom/analog pole | product pages fetched |
| IC design, verification & manufacturing (Calibre, Questa, Tessent, Veloce) | Siemens EDA | signoff/physical-verification standard; vendor straddling IC and PCB families | corporate + IC portfolio pages fetched |
| Aether/ALPS/Argus AMS + Digital SoC + Foundry solutions | Empyrean Technology (华大九天) | regional (China) pole; covers analog/PMIC, RF, digital, foundry enablement | English site fetched |
| KLayout | open source (Matthias Köfferlein) | open-source/low-tier witness; mask layout viewer/editor with DRC/LVS scripting | project site fetched |

Not sampled (with reasons):
- Keysight EDA (RF/microwave pole, ADS) — keysight.com returned HTTP 403 on first fetch; abandoned per network rule. The RF pole is covered indirectly via Cadence's RF/RFIC material and Empyrean's RF products. Recorded as a sourcing limitation.
- Silvaco, Tanner, Altium (board-side), Ansys (pre-acquisition) — marginal after core evidence saturated.
- Berkeley Magic (historical 1980s VLSI layout editor) — fetch failed twice (tool rendering error on opencircuitdesign.com); historical check therefore conducted at class level.

## Sources

Tier 1/2 official surfaces fetched 2026-09-09:

1. Synopsys — Chip Design (https://www.synopsys.com/implementation-and-signoff.html)
2. Synopsys — Glossary: "What is Integrated Circuit (IC) Design?" (https://www.synopsys.com/glossary/what-is-ic-design.html)
3. Cadence — Digital Design and Signoff (https://www.cadence.com/en_US/home/tools/digital-design-and-signoff.html)
4. Cadence — Virtuoso Studio (https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/virtuoso-studio.html)
5. Siemens — EDA Software, Hardware & Tools (https://www.siemens.com/en-us/company/electronic-design-automation/; eda.sw.siemens.com root redirects here)
6. Siemens — IC Tool Portfolio (https://www.siemens.com/en-us/products/ic/)
7. Empyrean — corporate English site (https://www.empyrean-tech.com/)
8. KLayout — project site (https://www.klayout.de/)

Failed / limited:
- Keysight EDA — HTTP 403 (1 attempt, abandoned).
- Siemens eda.sw.siemens.com/en-US/ic-design/ — HTTP 404 (1 attempt; recovered via siemens.com equivalents).
- opencircuitdesign.com/magic — fetch/render error ×2 (abandoned; historical check downgraded to class level).
- Deep operational manuals of the big three (Synopsys SolvNetPlus, Cadence Online Support, Siemens Support Center) are license-gated; no step-by-step user manuals were reachable. Flow descriptions in this pass derive from official product/glossary pages, not tool manuals — precise operational defaults, time windows, and numeric limits are therefore NOT asserted.

## Product Observations

Evidence layers: **A** = directly observed on a fetched official page of that product; **B** = cross-product commonality across the sampled set; **C** = canonical inference (used only in the synthesis).

### Synopsys

Key observations (A unless noted):

- Positioning: "Chip Design — Optimize Designs for Power, Performance, Area, and Yield"; "One unified, AI-driven platform spans digital, custom analog/mixed-signal, and FPGA flows". Claim: "The Technology Behind 90% of FinFET Designs" (marketing claim, not structurally load-bearing).
- Official definition: "IC design is the engineering discipline that turns a chip's specification into manufacturable silicon — spanning RTL synthesis, physical implementation, signoff, and verification across digital, custom, and FPGA flows."
- Three design families: **Digital Design Family** ("across the entire RTL-to-GDSII flow"), **Custom Design Family** ("Visually-assisted layout, fast SPICE simulation, and unified verification for analog, mixed-signal, RF, and memory"), **FPGA-based Design** (Synplify). FAQ: "Choose the Digital Design Family for RTL-to-GDSII work on SoCs, processors... Choose the Custom Design Family for analog, mixed-signal, RF, or memory blocks where SPICE accuracy and **hand-driven layout** matter... all three share a unified data model so designs flow between them without rework."
- Function-level taxonomy (nav): Analog Design, Digital Design, Design for Test, Verification, Virtual Prototyping, Hardware Assisted Verification, Signoff, Silicon Lifecycle Management, Manufacturing, SoC Integration (IP).
- Named products: Fusion Compiler ("Synthesis & Implementation"; "An innovative RTL-to-GDSII product"), IC Compiler II ("industry-leading place-and-route solution"), Design Compiler NXT (RTL synthesis), VCS ("Logic Simulation"), PrimeSim SPICE/HSPICE/XA (circuit simulation; HSPICE "gold standard for accurate on-chip simulation"), PrimeWave ("graphical waveform viewer and simulation post-processing tool"), IC Validator ("signoff physical verification solution"), PrimeTime ("static timing analysis... design signoff"), StarRC ("parasitic extraction... gold standard"), PrimePower, Formality ("Equivalence Checking"), SiliconSmart ("library characterization... generate the models required for digital signoff tools such as PrimeTime"), TestMAX ("IC Test"), RedHawk-SC ("Digital Power Integrity Signoff"), 3DIC Compiler (multi-die), Lynx (flow automation), ZeBu/HAPS (emulation/prototyping).
- Official glossary defines the flow steps: Architectural Design → Logic/Circuit Design → Physical Design → Physical Verification → Signoff:
  - "IC design consists of two distinct processes. First, circuit elements are assembled to perform the objective function... typically called logic, or circuit, design and the second process is called physical design."
  - Logic/Circuit Design: "decomposed into the required low-level circuit elements. This process is automated by software called logic synthesis. The collection of devices is simulated to verify the functionality of the design."
  - Physical Design: "begins with a chip 'floor plan'... The final circuit elements are then placed and routed in preparation for manufacturing. If the macro-level building blocks need to be modified... custom layout techniques, employing an IC layout editor tool, are used."
  - Physical Verification: "many design rules regarding how the circuit must be physically laid out on the silicon wafer to ensure it will be manufacturable. These design rules are checked at this step as well"; wiring resistance, crosstalk, process variability modeled.
  - Signoff: "the final step before the design is sent to manufacturing... verified against the results of 'golden signoff' quality tools. Design rules are fully verified... along with design for manufacturability rules. The timing, power consumption, and signal integrity of the design are also verified and 'closed'... accurate parasitic extraction is performed."
  - Shift-left: test and power "modeled and refined at each step of the process".
- Tool documentation lives behind SolvNetPlus support portal (evidence of gated operational docs).

### Cadence

Key observations (A):

- Digital Design and Signoff page: "accelerate convergence from RTL through implementation and signoff"; "Cadence digital design and signoff flows support advanced-node, low-power, mixed-signal, 3D-IC, chiplet, test, ECO, and signoff requirements... move from design intent to high-quality silicon".
- Key benefit: "Integrated RTL-to-Signoff Flow — Connect RTL, synthesis, implementation, test, ECO, and signoff in a unified path to predictable closure"; "Superior Signoff — Reach predictable closure with trusted timing, power, and physical signoff across advanced nodes".
- Flow stages as marketed: **Design Creation** (Constraints and CDC Signoff; Functional ECO; Logic Equivalence Checking via Conformal; Low-Power Validation; RTL Power Analysis; Synthesis — Genus, Innovus+, Stratus High-Level Synthesis, Virtuoso Digital Implementation; Test Automation — Modus DFT; RTL Prototyping), **Design Implementation** (Cerebrus AI Studio; Innovus+ — "Accelerating chip design with seamless RTL to GDS integration"; Integrity 3D-IC Platform), **Superior Signoff** (Tempus Timing Solution; Quantus Extraction; Voltus IC Power Integrity; Pegasus — "Cloud-ready physical signoff solution"; MaskCompose "Reticle and Wafer Synthesis Suite"; Pegasus DFM incl. CMP Predictor; Liberate — "cell library characterization solution for standard cells and complex I/Os").
- Virtuoso Studio (custom/analog pole): "Analog and custom IC design"; "an ideal balance of automation and custom-crafting, including managing **design intent that flows naturally from the schematic throughout all phases of the design**"; "the analysis environment facilitates real-time knowledge of circuit status compared to specifications, with both pre- and post-layout parasitics considered"; "The layout tools are designed with productivity features to facilitate connectivity-*right* designs regardless of rule complexity"; "Integrated verification methods, both in the **front-end and back-end** spaces"; advanced-node custom flow enables "rapid layout prototyping, **in-design signoff**, and close collaboration between **schematic and layout designers**".
- RF/RFIC: "RF analyses built on silicon-proven simulation engines in both the time and frequency domains... verification of broad RFIC types, including mixers, transceivers, power amplifiers..."; "RFIC, RF module, and package co-design".
- Photonics (EPDA): "schematic capture, circuit simulation, and schematic-driven layout implementation... complex photonic SKILL PCells and advanced photonic layout generators".
- Foundry coupling: news releases — certified flows/collaborations with TSMC, Samsung Foundry (2nm, 3D-IC), Intel 16 FinFET process ("Cadence Digital, Custom/Analog Design Flows Certified... for Intel 16"); Virtuoso migration page: "the world's foundries have teamed up with Cadence to produce new techniques in moving schematic and layouts efficiently to new nodes".
- Family separation (vendor's own taxonomy): nav "IC Design & Verification" (Virtuoso, Spectre — "Analog and mixed-signal SoC verification", Innovus+, Xcelium — "Logic Simulation — IP and SoC design verification", Palladium/Protium emulation) vs "System Design & Analysis" (Allegro X "System and PCB design platform", Sigrity, AWR RF, CFD...). PCB products are a separate family from digital/custom IC design.

### Siemens EDA

Key observations (A):

- Positioning: "Siemens EDA provides a comprehensive portfolio of electronic design automation (EDA) software, hardware, and services for the **design, verification and manufacturing of integrated circuits (ICs) and electronic systems**."
- Vendor's own family split: "IC design, verification and manufacturing — A comprehensive portfolio of tools for the design, verification and manufacturing of integrated circuits" vs "Electronic Systems design and manufacturing — ...mechanical, electrical, PCB design, simulation, verification and manufacturing". (Same IC-vs-board seam as Cadence's taxonomy.)
- IC portfolio page: "Siemens EDA is a leader in IC design, verification, and manufacturing"; "Every new IC process node introduces a new set of design complexities. To ensure you can meet performance, power, and area requirements... requires a comprehensive tool flow that spans from C-level, high-level synthesis, all the way to signoff verification."
- Verification-effort claim: "IC verification can account for up to seventy percent of the IC design cycle." (vendor page; single-source claim)
- Solution areas: Custom IC, MEMS & photonic design ("custom IC design flow... supporting analog, analog mixed-signal, MEMS, and integrated photonic designs"); Design for test (Tessent — "silicon test and yield analysis... manufacturing test, debug, and yield ramp"); FPGA design ("from C/RTL design, FPGA synthesis, functional verification, logic equivalence checking to PCB design"); High-level synthesis & verification; Place and route ("top-level hierarchical IC design and block-level physical implementation for complex digital ICs"); Power analysis & optimization.
- Verification: Custom IC verification ("world-class circuit simulation, mixed-signal verification, and variation-aware design"); Digital verification (Questa One — "efficiently reaching coverage, debug and design quality goals"; press release frames Questa as "smart verification software portfolio... for faster RTL sign-off").
- Featured platforms: Veloce/Innexis (hardware-assisted verification — emulation/prototyping); Tessent Silicon Lifecycle; **Calibre** Design Solutions — "a complete IC verification and DFM optimization platform that speeds designs from creation to manufacturing, addressing all sign-off requirements"; Calibre manufacturing named in advanced-node readiness ("3nm, 2nm and future nodes").
- Foundry coupling: "Siemens & Intel Foundry certify tools for 2D/3D design... Intel Foundry's latest silicon processes"; Excellicon acquisition (timing-constraint development/verification/management software).
- Cloud: "EDA cloud offerings — market-leading... EDA tools and managed services for use in your cloud environment."

### Empyrean (regional pole)

Key observations (A):

- Positioning: "providing innovative, high-quality, market leading EDA solutions to the global semiconductor industry." (China-based; English + Chinese sites.)
- Solution families: **AMS and PMIC Design and Verification Platform**; **RF IC Design Solution**; **Digital SoC Design Solution**; **Foundry EDA Solution**; Advanced Packaging Design Solution; Flat Panel Display Design Solution; plus a Foundry Design Enablement Service.
- Product mapping (same functional anatomy as the big three): Aether ("Schematic and Layout Design Environment"), ALPS ("SPICE Simulator"; ALPS RF), Patron ("Transistor-level Power Integrity Analysis"), Argus ("Physical Verification"), RCExplorer ("Parasitic RC Extraction"), Ada ("Layout Parasitic Analysis"), Polas ("Power IC Analysis" / reliability), Liberal ("Std. Cell, Mem, IP Characterization"), Qualib ("Standard Cell Library and IP Validation"), ICExplorer-XTop ("Timing and Power Optimization"), XTime ("Timing Simulation and Analysis"), Skipper ("Layout Integration and Analysis"), XModel RF ("RF model extraction"), ClockExplorer (per testimonial).
- Customer testimonials (evidence of real flows): MPS — Polas used to "analyze and build the required reliability into the design **prior to tape out**"; Diodes — Skipper used "during chip finishing time... to locate and pinpoint the shorts on the layout" of mixed-signal designs ("flatten the digital blocks into transistor-level"); Renesas — ClockExplorer "report[s] Clock KPI in various design stages such as pre-Place, pre-CTS, and post-CTS"; O2Micro — "a smooth mixed-signal IC design flow with a one-stop platform... with the help of TowerJazz's **iPDK** and Empyrean's AMS flow".
- Confirms the Type's structures exist identically in a regional ecosystem, including the foundry/PDK coupling and characterization for digital signoff.

### KLayout (open-source witness)

Key observations (A):

- "KLayout — Your Mask Layout Friend": View / Edit / Generate / Analyze modes.
- "It can read GDS2, OASIS, DXF, CIF, Gerber, LEF/DEF and other formats" — mask layout data formats confirmed at the low/free tier.
- "Develop and run **design rule check (DRC) and layout vs. schematic (LVS)** scripts"; "Trace nets with the integrated net tracing tool"; XOR/diff layout comparison; parametrized cells (PCells); Ruby/Python scripting with an integrated IDE.
- Demonstrates that even a free single-purpose tool is organized around the mask-layout object, rules-based checking, and layout↔net correspondence — the fragments of the same flow.

## Cross-product Comparison

| Structure | Synopsys | Cadence | Siemens EDA | Empyrean | KLayout | Layer |
|---|---|---|---|---|---|---|
| Design held at multiple abstraction levels (description → netlist → layout) with correspondence | yes ("logic, or circuit, design" + "physical design"; RTL-to-GDSII) | yes (RTL-to-signoff; schematic→layout intent flow; LEC/ECO) | yes (C-level/HLS → implementation → signoff) | yes (Aether schematic/layout; digital SoC family) | partial (layout ↔ net tracing, LVS scripts) | B |
| Functional description entry: RTL (digital) / schematic (custom) / C-level | yes (RTL synthesis; Custom Compiler design entry) | yes (Genus/Innovus+ RTL; Virtuoso schematic; Stratus HLS) | yes (C-level/HLS; custom IC flow) | yes (digital SoC; Aether schematic) | no (layout only) | B |
| Simulation of electrical/logical behavior | yes (VCS logic; PrimeSim SPICE/HSPICE; PrimeTime STA) | yes (Xcelium; Spectre; Tempus timing) | yes (circuit simulation; Questa digital; Veloce emulation) | yes (ALPS; XTime timing) | no | B |
| Physical verification against process rules (DRC-class) | yes (IC Validator "signoff physical verification") | yes (Pegasus "physical signoff") | yes (Calibre — the named standard) | yes (Argus) | yes (DRC scripts) | B |
| Layout-vs-schematic correspondence checking (LVS-class) | yes (assumed inside PV suite; Formality LEC at logic level — A for LEC) | yes (front-end/back-end verification; LEC via Conformal) | yes (Calibre family) | yes (Qualib validation; PV) | yes (LVS scripts) | B |
| Parasitic extraction feeding electrical re-check | yes (StarRC "gold standard") | yes (Quantus) | yes (Calibre) | yes (RCExplorer) | no | B |
| Signoff as the manufacturing gate ("golden" tools) | yes ("golden signoff quality tools"; Signoff category) | yes ("trusted timing, power, and physical signoff") | yes ("all sign-off requirements"; "RTL sign-off") | yes (pre-tape-out reliability; characterization "required for digital signoff") | no | B |
| Transformation flow ending in fabrication/mask data | yes (RTL-to-GDSII) | yes ("seamless RTL to GDS"; MaskCompose reticle/wafer) | yes ("from creation to manufacturing") | yes (tape-out testimonials) | yes (mask layout files GDS2/OASIS/CIF) | B |
| Process/foundry data as first-class input (PDK-class; device models, design rules, certification) | yes (foundry-node support, signoff models) | yes (foundry-certified flows; "foundries have teamed up") | yes (Intel Foundry certification) | yes (Foundry EDA solution; TowerJazz iPDK) | implicit (rule decks as scripts) | B |
| Library/IP foundation (standard cells characterized, IP blocks) | yes (SiliconSmart; DesignWare IP) | yes (Liberate; Tensilica IP) | yes (MEMS/photonics flows; Excellicon constraints) | yes (Liberal, Qualib, memory compiler) | no | B |
| Design for test (DFT) | yes (TestMAX) | yes (Modus) | yes (Tessent) | not observed on fetched pages | no | B (common, not definitional) |
| Hardware-assisted verification (emulation/prototyping) | yes (ZeBu, HAPS) | yes (Palladium, Protium) | yes (Veloce) | not observed | no | B (common, optional) |
| Waveform viewer as simulation debug surface | yes (PrimeWave named) | implied in analysis environment | implied ("debug") | implied (simulation post-processing in flow) | no | B (common; one named anchor) |
| Timing signoff as named discipline | yes (PrimeTime) | yes (Tempus) | yes (Excellicon acquisition rationale) | yes (XTime/XTop) | no | B |
| Power integrity / analysis | yes (PrimePower, RedHawk-SC) | yes (Voltus) | yes (power analysis & optimization) | yes (Patron, Polas) | no | B |
| Design data model unification across families | yes ("share a unified data model") | yes ("unified path") | yes (one portfolio) | yes ("one-stop platform") | n/a | B |
| 3D-IC / multi-die / advanced packaging | yes (3DIC Compiler) | yes (Integrity 3D-IC) | yes (3D IC implementation) | yes (Advanced Packaging solution) | no | B (era-current, common) |
| AI-assisted design/verification | yes (Synopsys.ai) | yes (Cerebrus, Verisium, agentic AI) | yes (Fuse agent, Questa One agentic toolkit) | not observed | no | B (era-current) |
| Cloud delivery | yes (cloud-ready) | yes (OnCloud) | yes (cloud offerings) | not observed | n/a (desktop) | B (variant) |
| Regional/sovereign ecosystem packaging | n/a | n/a | n/a | yes (domestic China EDA) | n/a (open source) | variant |
| Analog/mixed-signal as first-class pole alongside digital | yes | yes | yes | yes (AMSID the founding family) | no | B |
| RF pole with EM/frequency-domain analysis | partial (HSPICE SI framing) | yes (RFIC suite; AWR in system family) | partial (MEMS/photonics) | yes (ALPS RF/XModel RF) | no | B |
| Non-silicon-substrate reuse of the pattern | — | photonics | MEMS, photonics | flat-panel display | — | variant |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

The Type is recognizable only when **all three** of these structures are jointly held:

1. **The chip design as multi-level connected data of record.** One integrated circuit is held as corresponding representations at distinct abstraction levels — a functional/logical description (RTL, schematic, or C-level model), a circuit realization (netlist of cells/transistors), and a physical layout (geometry on silicon) — with the correspondence between levels maintained and checkable. Remove → a code editor or a drawing CAD tool.
2. **Verification against electrical behavior and manufacturing reality.** The design is simulated for electrical/functional behavior (circuit-, logic-, and timing-level), and the physical implementation is checked against the target manufacturing process's own rules and models (design rules, device models, parasitics), which arrive as process-specific data inputs from the silicon supplier; findings gate progress. Remove → freehand drawing with no engineering semantics, or a generic simulator disconnected from any manufacturing target.
3. **The transformation flow to fabrication-ready manufacturing data.** The abstract description is progressively transformed into the physical implementation — by automatic synthesis/place-and-route and/or hand-crafted layout — and finished as fabrication hand-off data (mask-layout data) a wafer fab can build. The flow's terminus is manufacturing data, not a running device and not a board. Remove → a simulation sandbox with no producible artifact; or FPGA-implementation territory (terminates at device programming); or board-level ECAD (different terminus and object).

Jointly-held load-bearing checks:

- 1 alone = drawing/CAD (or code editing)
- 2 alone = a standalone circuit simulator
- 3 without 1+2 = a file-format converter
- 1+2 without 3 = a simulation environment / academic playground (no producible artifact)
- 1+3 without 2 = layout tooling with no verification (the KLayout-viewer floor)
- 2+3 without 1 = a point-tool collection, not a design platform
- all three = the Type

### L1 — Common Mature Structure (very common, not definitional)

- Library/IP foundation: standard-cell libraries characterized into timing/power models consumed by signoff tools; pre-designed IP blocks integrated into the design (SiliconSmart/Liberate/Liberal; IP product families at Synopsys/Cadence).
- Design-for-test (DFT): test-logic insertion, ATPG, yield/test analysis (TestMAX, Modus, Tessent).
- Hardware-assisted verification: emulation and FPGA-based prototyping platforms (ZeBu/HAPS, Palladium/Protium, Veloce).
- Power analysis and integrity (PrimePower/RedHawk, Voltus, Patron/Polas) and signal-integrity analysis.
- Timing-constraint development/management as a discipline of its own (Excellicon acquisition; Timing Constraints Manager).
- Unified design data model / shared database across the flow; design data and library management.
- Flow automation around the point tools (script-driven, job-based — Lynx; agentic/AI automation is the era-current extension).
- Waveform viewers and simulation management environments as the debug surface.
- Formal verification (equivalence checking, CDC, low-power intent validation — Formality, Conformal, Questa).

### L2 — Variant / Optional Structure

- Flow pole: digital (RTL→synthesis→P&R) vs custom analog/mixed-signal (schematic→hand layout→post-layout verification) vs RF (frequency-domain, EM co-analysis) vs FPGA (front-end shared, terminus differs).
- Customer type: fabless design houses vs IDM internal teams vs systems companies building own silicon vs foundries' design-enablement groups.
- Node position: leading-edge (FinFET/GAA, advanced-node readiness marketing) vs mature/analog nodes; migration tooling across nodes.
- Ecosystem: commercial big-three platforms vs regional domestic ecosystems (China) vs open-source/low-cost toolchains (KLayout; Tanner-class — not sampled) vs academic flows.
- Packaging of adjacent domains reusing the same anatomy: MEMS, photonics (EPDA), flat-panel display (Empyrean FPD solution).
- 3D-IC/multi-die/chiplet and advanced packaging as an extending layer; multiphysics (thermal/EM) co-analysis arriving via acquisitions (Ansys/Synopsys; Cadence Sigrity/MSC).
- Delivery: on-premise license-managed desktop/server tools vs cloud-managed flows.
- AI-assisted optimization/verification/agentic workflows (era-current).

### L3 — Vendor-specific (research notes only)

- Named products and families: Fusion Compiler/IC Compiler II/PrimeTime/StarRC/IC Validator; Innovus+/Genus/Conformal/Tempus/Quantus/Voltus/Pegasus/MaskCompose/Liberate; Calibre/Questa/Tessent/Veloce; Aether/ALPS/Argus/Liberal/Qualib/Skipper.
- Marketing claims: Synopsys "technology behind 90% of FinFET designs"; Siemens' "verification up to seventy percent of the IC design cycle" (vendor-page claim); IBS-cited cost/complexity figures on Siemens' page ($245M→$539M advanced design cost; ~10,000→~24,000 engineering-months).
- Cadence's "Cerebrus/InnoStack agentic AI" and Synopsys' "DSO.ai" reinforcement-learning positioning.
- Empyrean's flat-panel-display and foundry-enablement service packaging.

## Rejected Findings (anti-overfit)

- **"RTL" is not definitional.** The custom/analog pole (Virtuoso, Custom Compiler, Aether) designs from schematics at transistor level with no RTL; Siemens' flow starts at C-level. The invariant is "functional/logical description," realized variously.
- **"Place-and-route automation" is not definitional.** Analog layout is explicitly "hand-driven" (Synopsys FAQ) and custom-crafted (Virtuoso "automation and custom-crafting"). The invariant is reaching a physically implemented layout consistent with the logical design, by whatever mixture of automation and craft.
- **"Digital SoC" is not the center.** Every sampled vendor runs a first-class analog/mixed-signal business; Empyrean's founding family is AMS/PMIC.
- **Specific formats are not definitional.** GDSII is the dominant hand-off format (RTL-to-GDSII marketing; KLayout reads GDS2/OASIS), with OASIS as successor and CIF/Gerber/LEF/DEF in the same family — the invariant is "fabrication-ready mask data," not a format name.
- **"Platform = suite" is a posture, not the definition.** Point tools (standalone simulator, layout viewer with DRC scripts) are fragments of the same flow; the market's center of gravity is the integrated flow, but the L0 holds for any tool set that jointly carries the three structures.
- **Verification-effort percentages, node numbers, cost figures** — single-vendor or third-party-attributed claims; kept out of the canonical definition.
- **AI/cloud/agentic features** — era-current; fail the historical check by construction; recorded as L2.

## Boundary Findings

1. **vs ECAD/EDA (§16 sibling, processed 2026-09-07)** — keep both; the flag that pass hung is discharged here with fresh IC-vendor evidence. The seam:
   - Unit of design: die/chip vs board/system/machine (electrical connectivity of equipment).
   - Binding to a silicon manufacturing process: this Type consumes process-specific rules/models (PDK-class) and is certified per foundry process; ECAD consumes component catalogs, not a foundry process.
   - Flow terminus: fabrication/mask hand-off data for a wafer process vs board fabrication outputs (netlists/BOM/panel drawings) for PCB manufacture.
   - Vendors themselves separate the families: Cadence nav "IC Design & Verification" vs "System Design & Analysis"/PCB; Siemens "/products/ic/" vs "/products/pcb/". The umbrella term "EDA" spans both — a naming fact, not a merge argument.
2. **vs PCB Design** — same seam as (1); PCB design is the board-layout-centered realization of the ECAD/EDA family (per that pass's recorded working position).
3. **vs Software development tools (IDE, Version Control, Code Editor)** — front-end HDL/RTL editing is code-like and some verification tooling resembles software test infrastructure, but the platform's object of record is the circuit and its manufacturing data; the terminus differs (silicon vs running software). Mature IC platforms also integrate with software stacks (virtual prototyping, HW/SW co-design) without becoming software IDEs.
4. **vs FPGA implementation toolchains** — share the front-end (HDL, synthesis, functional simulation, equivalence checking) but terminate at a programming image for a prefabricated device, with no process-rule/physical-verification/mask-data tail. Vendors treat FPGA design as a separate family (Synopsys "FPGA-based Design"; Siemens lists it inside IC but with a flow ending "to PCB design"). Adjacent; boundary held.
5. **vs CAE / Engineering Simulation and System Simulation Platform / MBSE** — chip tools simulate the artifact being designed as an integral design step (SPICE/logic/timing), not physics studies of an external system model; system-level and multiphysics analysis enters only as era-current extensions. SPICE-class circuit simulation is design-embedded verification, not CAE study management.
6. **vs TCAD (device/process simulation)** — upstream discipline simulating the fabrication physics itself to derive device models; separate product families; adjacent, not part of the L0 (Empyrean's device-model extraction for foundries is the closest approach — recorded as foundry-enablement variant).
7. **vs fab-side manufacturing software (MES, fab CIM/yield)** — the design platform ends at manufacturing hand-off; "IC design, verification and manufacturing" in vendor naming means design-for-manufacturing readiness (DFM), not fab execution. Different object world (lots/wafers/fabs vs designs).
8. **Internal variant caution** — flat-panel display design (Empyrean) reuses the whole anatomy on a display substrate; MEMS/photonics likewise. Recorded as domain variants of one tooling pattern; no directory action requested.

## Uncertainties

- RF pole under-documented: Keysight (the archetypal RF-EDA vendor) was unreachable; RF structure documented via Cadence's RFIC material and Empyrean's RF products only. Claims about RF-specific mechanics (EM-circuit co-simulation details) kept generic.
- No step-by-step operational manuals reachable for any big-three vendor (all license-gated). Consequently the final document describes flows at the level vendors' own product/glossary pages support, and deliberately avoids precise defaults, limits, and tool-vocabulary minutiae.
- The "verification ≈ 70% of design cycle" figure is a single-vendor page claim; kept attributed and qualitative in the final document.
- Historical check is class-level (Magic fetch failed twice): SPICE (1970s Berkeley circuit simulation), 1980s VLSI layout editors with integrated design-rule checking and netlist extraction, and mask-data formats of the GDSII generation (1970s Calma; KLayout still reads GDS2/OASIS/CIF today — indirect A-layer lineage evidence). A 1980s environment of schematic/netlist entry + SPICE + layout + DRC + mask-data output satisfies all three L0 legs with none of the modern machinery (AI, cloud, 3D-IC); Empyrean (regional) also satisfies fully. Historical check: passed at class level.
- License-management mechanics (license servers, per-seat concurrency) are industry-common but were not evidenced on fetched pages; omitted from the final document rather than asserted.
- Whether "Semiconductor Design Platform" should eventually fold into or be renamed under the EDA umbrella is a taxonomy-owner question; this pass records the keep-both verdict and the naming fact without changing the directory.

## Final Synthesis

A Semiconductor Design Platform is the software environment in which an integrated circuit is carried from functional description to fabrication-ready manufacturing data. Its defining structure is the joint holding of: (1) the chip design as corresponding representations at multiple abstraction levels (description → circuit → layout); (2) verification against electrical behavior and against the target silicon process's own rules and models, with findings gating progress; (3) a transformation flow — automatic synthesis/place-and-route, or hand-crafted layout, or both — that terminates in mask/fabrication hand-off data. Around this core, mature platforms add library/IP foundations, DFT, power/integrity analysis, hardware-assisted verification, formal verification, and flow automation; regional, open-source, RF, analog, and FPGA-adjacent implementations vary the packaging while preserving the core. The Type's cleanest separations: from board-level ECAD/EDA (object + process binding + terminus), from software toolchains (terminus), from FPGA toolchains (no manufacturing tail), and from fab-side manufacturing software (different object world).
