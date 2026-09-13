# Research Notes — Robotics Engineering Platform

## Research Goal

Understand what a "Robotics Engineering Platform" is as an Application Type: what the engineering subject is (the robot? the cell? the application?), what artifact engineers author, how behavior is verified before it reaches hardware, how it is carried to real robots, who does this work, and where the Type's boundary sits — especially against the processed sibling **Robot Fleet Management** (§16), which left a forward flag expecting the seam "build/program/simulate robots vs operate deployed fleets".

## Initial Boundary

Initial hypothesis: this is the *engineering* side of robotics software — modeling robots/workcells, authoring robot behavior (programs, applications, configurations), verifying it in software (simulation), and deploying it to real robot controllers. Neighbors to check: Robot Fleet Management (run side), Mechanical CAD (geometry without behavior), CAE/Engineering Simulation (physics analysis without deployment), PLC Programming Environment (fixed logic vs motion/task behavior), Digital Twin Platform (operations mirror vs engineering substrate), Machine Vision Platform, MBSE/System Simulation, Game Engines (§04), Machine Learning Platform (§13), Embedded/Firmware Development IDE (§12).

Scope note: "robotics engineering" in the market means engineering robot *applications and behavior*, not designing robot hardware — hardware design lives in Mechanical CAD, and the platforms researched here *consume* CAD as input. This was checked against the sample and held.

## Research Questions

1. What is the central artifact engineers author — program, application, configuration?
2. What is modeled (robot kinematics, cell geometry, components, sensors), and is a model required?
3. How is behavior authored (graphical teaching, code, post-processing, SDKs)?
4. How is it verified in software (simulation, virtual controller, mock components)?
5. How does the artifact reach real robots (download, post-processor, deploy, stack validation)?
6. Who uses it (robot programmer, manufacturing engineer, integrator, developer, researcher)?
7. What is the vendor-lock axis (OEM-locked vs vendor-agnostic) and does it change the core?
8. Where does this Type end and Robot Fleet Management begin?
9. What modern overlays (AI training, synthetic data, fleet spans) are common but not definitional?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

1. **FANUC ROBOGUIDE** — robot-OEM offline programming & simulation (industrial arms; OEM-locked; large manufacturers/integrators)
2. **RoboDK** — vendor-agnostic offline programming & simulation (80+ robot brands; startups to global industry)
3. **NVIDIA Isaac Sim** — simulation-first developer platform (open source; AI/robotics developers and researchers)
4. **Viam** — modern cloud robotics platform (component model + SDKs + registry; robotics product builders; spans build and fleet)
5. **Universal Robots (PolyScope / URScript / UR+ Developer Suite / UR Studio)** — cobot OEM pole (pendant-first authoring; SME tier)

## Sources

- FANUC America — ROBOGUIDE product page: https://www.fanucamerica.com/products/software/robot/roboguide (fetched 2026-09-09)
- FANUC America — robots landing page (ROBOGUIDE positioning): https://www.fanucamerica.com/products/robots (fetched 2026-09-09)
- RoboDK — home: https://robodk.com/ (fetched 2026-09-09)
- RoboDK — Offline Programming: https://robodk.com/offline-programming (fetched 2026-09-09)
- NVIDIA — Isaac Sim documentation "What Is Isaac Sim?": https://docs.isaacsim.omniverse.nvidia.com/latest/index.html (fetched 2026-09-09)
- Viam — platform overview: https://www.viam.com/product (fetched 2026-09-09)
- Viam — docs "What is Viam?": https://docs.viam.com/what-is-viam/ (fetched 2026-09-09)
- Viam — docs "Try Viam" overview (TOC incl. Gazebo Simulation Setup, fake components): https://docs.viam.com/try/overview/ (fetched 2026-09-09)
- Universal Robots — Developer Suite: https://developer.universal-robots.com/ (fetched 2026-09-09)
- Universal Robots — UR Studio: https://www.universal-robots.com/products/ur-studio/ (fetched 2026-09-09)
- Prior sibling pass: research/robot-fleet-management.md (§Boundary Findings #5 forward flag; §16 context)

Unreachable (recorded as limitations): ABB RobotStudio (new.abb.com 403, two URL attempts), Visual Components (visualcomponents.com 403; learn.visualcomponents.com transport error), UR URSim article (404 on two guessed paths), FANUC ROBOGUIDE deep manuals (not attempted beyond product page), KUKA.Sim (404 on guessed path, not retried).

## Product A — FANUC ROBOGUIDE

### Key observations (evidence layer A unless noted)

- Positioning: "offline robot programming and simulation software… creates programs and simulates robotic workcells in 3D – eliminating the need for physical prototypes" (product page).
- Workcell modeling: 64-bit app replicating "larger and more complex workcells"; CAD import/export "in greater detail"; drag-and-drop robot setup; browsers for "robots, workcell objects, parts, programs, and profiles".
- Virtual controllers/pendants: "Virtual pendants can be displayed simultaneously for each controller"; immediate visualization of motion types "without running the program".
- Application modules: iRPickPRO (pick systems: layouts, part rates, conveyor configurations, load balancing), HandlingPRO (material handling: "CAD to Path programming, conveyor line tracking, machine modeling and programming"), PaintPRO ("graphical offline programming solution… automatically generates robot programs by graphically selecting the area of the part"), PalletPRO ("completely build, debug and test a palletizing application offline… workcell layout, infeed and pallet stations… built-in library of industry standard patterns"), WeldPRO ("simulates robotic arc welding… CAD to Path… auto generation of multiple robot group coordinated motion programs").
- Deployment leg: "The data created in PalletPRO can be downloaded to a real robot controller containing PalletTool software"; WeldPRO: "Programs and settings from the virtual workcell can be transferred to the real robot to decrease installation time."
- VR playback of simulation recordings (Oculus/Steam VR) — era-current overlay.
- OEM-locked: the tool simulates and programs FANUC robots (product family context; the whole page is FANUC-robot-scoped).

## Product B — RoboDK

### Key observations (evidence layer A unless noted)

- Positioning: "a complete solution to simulate and program robot arms offline for robot manufacturing and automation" (home).
- OLP definition (offline-programming page): "Offline Programming means programming robots outside the production environment. Offline Programming eliminates production downtime caused by shopfloor programming." "Simulation and Offline Programming allows studying multiple scenarios of a robot work cell before setting up the production cell. Mistakes commonly made in designing a work cell can be predicted in time."
- Vendor-agnostic: "over 100 post processors to generate programs for more than 1400 robots and 80 robot manufacturers"; named post processors: ABB RAPID (mod/prg), Fanuc (LS/TP), KUKA KRC (SRC), Motoman Inform (JBI), Universal Robots (URP/script). Page shows a generated ABB RAPID program listing — the artifact is a controller program file.
- "You don't need to learn vendor-specific programming anymore" (feature: Robot Programs).
- Modeling: import STL/STEP/IGES; "create your Digital Twin"; external axes; "prevent the robot from going through singularities, axis limits and collisions"; robot calibration ("improve accuracy up to 0.100 mm" — vendor claim, product-specific).
- Programming layers: GUI ("no programming skills"), RoboDK API (Python, C#/.NET, C++, Matlab) with example script driving MoveJ/MoveL against targets, CAD/CAM integration (convert G-Code/APT-CLS for robot controllers).
- Extensibility: Add-in Marketplace; RoboDK for Web; TwinTrack/TwinTool/TwinBox (physical digital-twin products); robot library of 1400+ robots.
- Applications: welding, machining, dispensing, polishing, cutting, palletizing (documentation examples).

## Product C — NVIDIA Isaac Sim

### Key observations (evidence layer A)

- Positioning (docs "What Is Isaac Sim?"): "Import robots and scenes from URDF, MJCF, Onshape CAD, or USD. Simulate with PhysX or Newton, add RTX and physics-based sensors, generate synthetic data, prepare robots for Isaac Lab, and validate robot stacks with ROS 2."
- Workflow (docs): 01 Import (scenes, robots, sensors, CAD/USD) → 02 Configure (materials, sensors, scenarios, semantics, robot physics, communication graphs) → 03 Simulate (physics stepping, sensor output, control loop, stack behavior) → 04 Connect/Deploy ("Export datasets to training pipelines or connect external robot stacks for pre-hardware validation"). "Shared Isaac Sim Scene: USD scene, physics state, sensors, semantics, and graphs in one runtime."
- Ecosystem framing: Isaac Sim (simulator) + Isaac Lab (RL/IL training) + Replicator (synthetic data generation) + ROS 2 bridge; SIL testing = "validate the external robot stack before hardware".
- Robot setup tooling: URDF importer, robot assembler, gain tuner, self-collision detector, joint inspector; motion generation (cuRobo/cuMotion, RMPflow); sensors (RTX Lidar, cameras, IMU, contact…).
- Open source (Apache 2.0), USD-native, pip/conda/container/cloud install paths.
- Note: Isaac Sim itself does not flash robot controllers; its "deploy" leg is exporting datasets to training pipelines and connecting external robot stacks for pre-hardware validation — the terminus (behavior on real robots) is reached through the connected stack. This shapes the canonical phrasing of the deployment leg (see L0).

## Product D — Viam

### Key observations (evidence layer A)

- Positioning (docs "What is Viam?"): "a software platform for building, deploying, and managing robotics applications." "You declare the hardware and services you need in a JSON config. Viam installs the drivers and any additional software modules required… Application code versioning, deployment, and rollback are native… It's the development workflow you're used to, applied to physical devices."
- Object world: **machine** (the configured robot), **components** (arm, base, board, camera, motor, sensor, gantry, gripper, encoder, servo, input controller, switch, power sensor…), **services** (motion, vision, data management, frame system, discovery…), **modules** (packaged drivers/logic from the Registry), **fragments** (reusable configuration across machines), **Registry** (versioned modules/ML models/training scripts).
- Runtime: viam-agent installs viam-server; viam-server pulls machine config from the cloud, fetches modules, launches processes.
- Software verification leg: built-in **fake** component models for every component type (arm/fake, base/fake, camera/fake, motor/fake…); a **Gazebo Simulation Setup** tutorial pathway ("simulated canning line", no hardware required); motion planning docs include "Verify a plan before running it" (verify a motion plan without executing it).
- Deployment leg: deploy modules and configs to machines; version pinning, staged rollouts, rollback; OTA updates; fleet-wide fragments.
- Span: the same platform carries fleet deployment + monitoring + teleop + RBAC + billing — the build side (config/modules/code) is this Type's subject; the manage side overlaps Robot Fleet Management.
- SDKs: Python, Go, TypeScript, C++, Flutter; "Write code on your laptop and run it against machine hardware over the network."

## Product E — Universal Robots (PolyScope / URScript / UR+ / UR Studio)

### Key observations (evidence layer A unless noted)

- Developer Suite (developer.universal-robots.com): "a collection of all the tools needed to build an entire solution, including developing URCaps, adapting end-effectors, and integrating hardware." URCap Tools: "Develop a URCap to extend the functionality of PolyScope, create custom user interfaces and integrate third party devices." URScript: "program language [that] allows you to do almost anything with your cobot." Hardware & Motion: CAD files, wire diagrams, user manuals, DH parameters, mounting guides. Communication protocols: Ethernet/IP, Modbus TCP, Profinet, ROS/ROS2.
- UR Studio (product page): "Simulate and evaluate your robotics solutions before deployment. Your one click online simulation tool for studying reach, speed and placement optimization in a digital work cell." "Design, simulate, deploy": build a 1:1 virtual work cell in the browser (robots, modules, components, conveyors, grippers), "Simulate the complete setup, test your program and calculate cycle time"; cell optimization: "test robot reach, check for collisions, evaluate speeds and plan around real-world constraints".
- Parity principle (UR Studio page): "UR Studio is designed to work hand-in-hand with PolyScope X… the program you create in the simulation environment will behave the same way when deployed on the robot… PolyScope X is built to support simulation from the ground up, so you can create and validate solutions in a virtual space before committing to the floor."
- OEM-locked: UR robots only; extensibility via URCaps.
- URSim (UR's offline virtual controller) is known to exist but was not directly fetched (404s on guessed article paths) — no specific claims made; the simulation leg for UR rests on the UR Studio / PolyScope X evidence (Tier 2).

## Cross-product Comparison

| Dimension | ROBOGUIDE | RoboDK | Isaac Sim | Viam | UR (PolyScope/UR Studio) |
|---|---|---|---|---|---|
| Engineering subject | FANUC workcell (3D) | any-brand workcell ("digital twin") | USD scene with robots+sensors | machine (component config + frames) | UR work cell (browser) / cobot program |
| Behavior artifact | robot programs + application-module data | controller program files via post-processors | control logic, policies, SDG pipelines, ROS 2 stacks | machine config + modules + control code | URScript programs / program tree + URCaps |
| Software verification | 3D simulation, virtual pendants | simulation, collision/singularity checks | physics sim (PhysX/Newton), sensors, SIL | fake components, Gazebo sim, plan verification | UR Studio sim (reach/collision/cycle time), PolyScope X sim |
| Path to real robots | download to real controller (PalletPRO→PalletTool; WeldPRO transfer) | post-processors → 80+ brands' controllers | external robot stack (ROS 2), pre-hardware validation | viam-server runs config+modules on machines | program deploys to cobot; PolyScope X parity |
| Extensibility | application modules | add-in marketplace, API | extensions, Python API, open source | module Registry, SDKs | URCaps SDK, URScript |
| Vendor lock | FANUC-only | none (80+ brands) | none (URDF/MJCF/USD) | none (driver modules per device) | UR-only |
| Deployment shape | desktop app | desktop app (+web) | workstation/container/cloud | cloud + edge runtime | browser tool + pendant software |
| Customer tier | large manufacturers/integrators | startups→global industry | AI/robotics developers, researchers | robotics product builders | SME manufacturers, education |
| AI/ML overlay | (FANUC Physical AI is a separate solution line) | (Physical AI page exists) | core-adjacent (SDG, Isaac Lab) | built-in (data→train→deploy) | (Physical AI product line) |

### Cross-product commonalities (evidence layer B)

- All five author a **behavior artifact** destined for robots (programs / applications / configurations).
- All five maintain a **digital model of the robot(s) and its environment** against which engineering happens — 3D workcell (ROBOGUIDE, RoboDK, UR Studio), USD scene (Isaac Sim), component/frame configuration (Viam).
- All five **verify behavior in software** before/alongside hardware — simulation is universal; its form varies (physics-based, kinematic, virtual controller, mock components).
- All five own a **bridge from the virtual artifact to real robot execution** — download (ROBOGUIDE), post-processing (RoboDK), stack validation (Isaac Sim), runtime deployment (Viam), parity-guaranteed deployment (UR Studio/PolyScope X).
- All five carry an **extensibility mechanism** (modules/add-ins/URCaps/extensions/Registry) — common mature structure, not definitional (historical OLP systems predate rich extensibility).
- All five integrate **CAD/geometry import** — CAD is an input, not the artifact.
- Modern overlays present in the current market: AI/ML training loops (Isaac Lab, Viam train/deploy, vendor "Physical AI" lines), synthetic data generation, VR playback, cloud dashboards — era-current, not definitional.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The robot behavior artifact** — a persistent, iteratively authored definition of what a robot does: a program, application, or configuration (motion paths, task logic, component wiring, control code). Remove → a CAD model or simulation viewer with nothing authored.
2. **The robot/cell model as the engineering subject** — a digital representation of the robot(s) and its working environment (geometry, kinematics, components, sensors) against which behavior is authored and verified. Remove → a generic IDE/programming tool with no robot semantics.
3. **The virtual-to-real bridge** — authored behavior is verified in software against the model (simulation, virtual controller, mock components) and carried to running behavior on real robot hardware (download, post-processing, deployment, or validation of the stack that runs on the robot). Remove the software verification → shop-floor teach-pendant programming (below the platform bar); remove the hardware terminus → a pure simulation environment / game engine.

Jointly-held load-bearing:
- 1 alone = behavior code with no robot context (generic programming)
- 2 alone = CAD/3D model viewer
- 3 without 1+2 = fleet operations over robots it never authored (Robot Fleet Management territory)
- 1+2 without 3 = simulation-only sandbox (game-engine / digital-twin-viewer territory)
- 1+3 without 2 = direct-to-hardware teaching with no model (teach-pendant class)
- 2+3 without 1 = an operations mirror with nothing authored (digital-twin monitoring territory)

### L1 — Common Mature Structure

- 3D workcell/cell modeling with CAD import (dominant form of the model leg)
- Collision detection, reach checking, singularity/axis-limit avoidance
- Cycle-time estimation
- Virtual controllers / virtual pendants / offline program testing
- A programming-language layer above the GUI (vendor languages, Python/C#/C++ APIs, SDKs)
- Extensibility ecosystems (modules, add-ins, URCaps, extensions, registries)
- Application-specific tooling (welding, painting, palletizing, handling, picking)
- Motion planning services
- Sensor simulation
- Robot calibration tooling
- Versioning of the engineering artifact (program files; config versioning/rollouts)
- AI/ML integration loops (synthetic data, policy training, model deployment) — current-market common

### L2 — Variant / Optional Structure

- Vendor lock axis: OEM-locked (ROBOGUIDE, UR) vs vendor-agnostic (RoboDK, Isaac Sim, Viam)
- Robot population: fixed arms vs cobots vs mobile bases vs mixed cells
- Deployment shape: desktop app vs browser vs cloud+edge vs open-source container
- Simulation fidelity: kinematic vs physics-based vs photoreal rendering
- AI training pipelines as first-class workflows (RL/IL, SDG)
- Fleet-management span (build+manage in one platform)
- Business model: license vs free/open-source vs subscription/cloud
- Education/training use of virtual cells

### L3 — Vendor-specific (Research Notes only)

- ROBOGUIDE: HandlingPRO/PaintPRO/WeldPRO/PalletPRO/iRPickPRO module names; PalletTool download pairing; VR playback (Oculus/Steam); ribbon UI.
- RoboDK: TwinTrack/TwinTool/TwinBox; "accuracy up to 0.100 mm" claim; "2 clicks" program generation; RoboDK for Web.
- Isaac Sim: OpenUSD scene format; Replicator; Isaac Lab; cuRobo/cuMotion; Newton physics backend; Nova Carter; MCP server.
- Viam: viam-server/viam-agent; fragments; Registry; white-label auth/billing; Micro-RDK (ESP32); Viam Rover rental.
- UR: URCaps; PolyScope/PolyScope X; URScript; UR Studio; DH parameters documentation; forum/Discord/beta program.

## Vendor-specific Findings

- RoboDK's OLP page is the clearest articulation of the Type's economic rationale: move programming off the production floor to eliminate downtime; "the time for the adoption of new programs can be cut from weeks to a single day" (vendor claim, product-specific).
- UR Studio/PolyScope X states the virtual-real parity principle explicitly ("the program you create in the simulation environment will behave the same way when deployed on the robot") — the strongest direct statement of the bridge's guarantee; other products imply parity (virtual controllers) without stating it as strongly (single-source, treat as product-stated principle, generalized cautiously).
- Isaac Sim's deployment leg is indirect by design (validate stacks before hardware) — evidence that the L0 bridge must be phrased to include stack-validation, not only direct download/deploy.
- Viam demonstrates the build+manage span inside one product — the engineering core (config/modules) and the fleet layer (deployment/monitoring) are separable surfaces, supporting the seam with Robot Fleet Management.
- ROBOGUIDE's application modules show the artifact can be module-scoped data (pallet patterns, weld paths), not only a monolithic program.

## Boundary Findings

1. **vs Robot Fleet Management (§16 sibling — DISCHARGES the forward flag from research/robot-fleet-management.md §Boundary Findings #5)**: the expected seam "build/program/simulate robots vs operate deployed fleets" is CONFIRMED from this side. The engineering platform authors and verifies the behavior robots run; the fleet manager operates deployed robots (register + directed missions + oversight loop). Evidence: ROBOGUIDE's output is programs downloaded to controllers (production then runs them); RoboDK frames OLP as engineering outside the production environment; Viam explicitly separates build surfaces (config/modules/code) from manage surfaces (fleet deployment/monitoring); UR Studio's entire pitch is "before deployment". The sibling's evidence (OTTO ships simulation as a separate service; Formant positions as operations infrastructure; Orbit consumes rather than builds robots) is consistent. Removal tests: remove authoring, keep register+missions+oversight → Robot Fleet Management; add the fleet register/oversight loop to this Type → Robot Fleet Management. **Verdict: keep-both — distinct Types sharing a robot-subject family; the seam is author-vs-operate.**
2. **vs Mechanical CAD (§16)**: geometry authoring without behavior. All sampled platforms import CAD (ROBOGUIDE CAD import/export; RoboDK STL/STEP/IGES; Isaac Sim CAD converter/Onshape; UR CAD files) — CAD is input. Remove behavior authoring + the bridge → Mechanical CAD.
3. **vs CAE / Engineering Simulation (§16)**: CAE validates *designs* against physics (stress, flow) producing engineering verdicts; this Type simulates *behavior* to produce runnable robot artifacts. Isaac Sim's physics serves behavior/stack validation, not design analysis. Different artifact, different terminus.
4. **vs PLC Programming Environment (§16, unprocessed — forward note)**: both program industrial machines, but the subject differs — PLC tools author fixed-logic control sequences; this Type authors motion/task behavior of articulated/mobile robots against kinematic/cell models (the model leg is absent in PLC tooling). Left as a forward note for the PLC pass; no taxonomy claim.
5. **vs Digital Twin Platform (§16)**: digital-twin platforms mirror operating assets for monitoring/analysis in the operate phase; here the model is an engineering substrate for authoring and verification. RoboDK markets "digital twin" (of the cell, for programming) and Isaac Sim has a Digital Twin docs section — in both, the twin serves the engineering loop, not operations mirroring. Seam: authoring-and-deployment vs operate-phase mirroring.
6. **vs Game Engine / 3D creation (§04)**: simulation without robot semantics (kinematics, controllers, sensors-for-robots) and without a real-robot destination is a game engine. Isaac Sim is built on a rendering engine but its object world and output are robot-shaped.
7. **vs Machine Learning Platform (§13)**: Isaac Sim's SDG/Isaac Lab and Viam's train/deploy loops touch ML, but the ML platform's world (datasets/experiments/registries/serving as the center) is not this Type's center; here ML is an input/output around the behavior loop.
8. **vs Embedded/Firmware Development IDE (§12)**: firmware IDEs target generic embedded hardware without robot/cell semantics; Viam's microcontroller support (Micro-RDK/ESP32) is a variant inside a robot-subject platform.
9. **vs MBSE / System Simulation Platform (§16)**: system-level multi-domain modeling vs robot behavior engineering with deployment to robot controllers; light seam, noted only.
10. **去掉什么就变成另一个 Type 判据**: remove the robot/cell model → generic IDE; remove behavior authoring → simulation viewer/digital-twin monitor; remove the virtual-to-real bridge → game engine or pure simulation sandbox; add the fleet register+oversight loop → Robot Fleet Management; replace robots with fixed logic → PLC territory; keep geometry only → Mechanical CAD.

## Historical / Market-Sample Check (§24)

- **1980s–1990s offline programming systems** (GRASP/PLACE/IGRIP/RoboCAD class — Tier 3, reasoned, not fetched): workcell models + robot programming + simulation + download to controllers satisfy all three L0 legs with no cloud, no AI, no USD, no ROS. RoboDK's own OLP definition ("programming robots outside the production environment") describes a decades-old practice.
- **Teach-pendant-only programming** lacks the model and software-verification legs — it is the robot's own interface, below the "platform" bar; the Type's center has always included the virtual model. This is the boundary that makes "platform" meaningful.
- The definition names no rendering technology, no file format (USD/URDF), no protocol (ROS 2), no deployment shape (desktop/cloud/browser), no AI machinery — all era or variant.
- Regional check: sample is US/Europe/Japan-weighted (FANUC, UR, RoboDK, NVIDIA, Viam). Other regional OLP/simulation ecosystems were not fetched; the L0 is domain-neutral and should accommodate them, unverified.

## Uncertainties

1. **ABB RobotStudio unreachable** (403 on two URLs) — the other major OEM-OLP anchor unverified; the OEM pole rests on FANUC (Tier 2) + UR (Tier 2). No claims made about RobotStudio specifics.
2. **ROBOGUIDE evidence is product-page strength** (Tier 2); detailed workflow rules (virtual-controller parity guarantees, calibration workflows) not confirmed from manuals.
3. **UR URSim not directly fetched** (404s); UR's simulation leg rests on UR Studio / PolyScope X statements (Tier 2). No specific URSim claims made.
4. **Viam's Gazebo simulation depth** is tutorial-level — held as an optional capability, not core.
5. **Isaac Sim's deployment leg is indirect** (via ROS 2 stacks); the L0 bridge phrasing calibrated to include stack validation.
6. **Visual Components unreachable** — the vendor-agnostic manufacturing-simulation pole is evidenced via RoboDK instead.
7. **Mobile-robot coverage in arm-centric OLP tools** (RoboDK is arm-focused) — the Type spans arm-centric and mobile-centric products; population breadth reasoned at canonical-inference strength.

## Final Synthesis

A Robotics Engineering Platform is the engineering-side system for robot behavior: it holds a digital model of the robot(s) and their working environment as the engineering subject, hosts the authored behavior artifact (program/application/configuration) that defines what the robot does, verifies that behavior in software against the model (simulation, virtual controllers, mock components), and carries it to running behavior on real robot hardware (download, post-processing, deployment, or validation of the stack that runs on the robot). Around that core, mature products add 3D workcell modeling with CAD import, collision/reach/singularity checking, cycle-time estimation, virtual controllers and pendants, programming-language layers and SDKs, extensibility ecosystems, application-specific tooling, motion planning, sensor simulation, calibration, versioning, and — in the current market — AI/ML training loops. The market realizes the Type across a vendor-lock axis (OEM-locked vs vendor-agnostic), a robot-population axis (arms vs cobots vs mobile bases), a deployment axis (desktop vs browser vs cloud+edge vs open source), and a fidelity axis (kinematic vs physics vs photoreal). The Type is bounded against Robot Fleet Management (author vs operate — forward flag discharged), Mechanical CAD (geometry without behavior), CAE (design verdicts vs robot artifacts), PLC programming (fixed logic vs motion/task behavior), digital-twin platforms (engineering substrate vs operations mirror), game engines (no robot destination), and ML platforms (model-world vs behavior-world).
