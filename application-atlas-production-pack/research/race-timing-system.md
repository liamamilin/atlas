# Research Notes — Race Timing System

Research date: 2026-09-09
Directory leaf: Race Timing System (§28 Sports, Fitness & Recreation)
Slug: race-timing-system

## Research Goal

Understand what a Race Timing System actually is as an Application Type: what its world is built from (timing points, transponders/tags/cards, decoders/readers, reads, start references, splits, results), who operates it (the timer / timing company vs the club vs the organizer), how the race-day timing flow works (setup → capture → processing → official results), which structures are definitional vs merely common in today's market, and where its boundaries sit against Race Management Platform (adjacent leaf, already processed), Sports Registration, Sports Meet Management, tracking platforms, and generic RFID/telemetry systems.

## Initial Boundary

Working hypothesis at start:

- A Race Timing System is the **timekeeping machinery** for competitive events: capture hardware (transponder/chip systems, photo-finish, control stations) plus the software that turns raw captures into official participant times and results. It is typically operated by a **professional timer / timing company** — a structurally distinct role from the race organizer.
- Nearest directory neighbors:
  - **Race Management Platform** (§28, leaf above) — organizer-side system of record; already processed 2026-09-09. Its pass explicitly recorded the seam from the other side: "Timing systems center the timing stack (chips, decoders, photo-finish, scoring software) operated by/for timing companies, importing rosters; race platforms center the organizer's event operations and consume timing output. Remove the roster/registration/event operations → Race Timing System; remove the timing stack → race platform." This pass must **ratify that seam from the timing side**.
  - **Sports Registration Platform / Event Registration (§26)** — registration-first, no capture machinery.
  - **Sports Meet Management** (§28 sibling) — meet/season record-keeping (entries, schedule, standings) vs this leaf's capture-and-time focus.
  - **Tracking / telemetry platforms (§14/§18)** — position monitoring without competitive-time semantics.
  - **Industrial IoT / asset tracking** — same radio technology, no competition semantics.
- Prior pass note (race-management-platform, 2026-09-09): RunSignup's RaceDay Scoring was described as "a scoring layer *over* third-party chip systems, not a chip/hardware system"; Zone4 was described as "timing-anchored" (center-of-gravity straddle). Both noted as boundary poles to reconcile from this side.

## Research Questions

1. What is the core object model — timing point, capture device, tag/transponder/card, read record, start reference, split, lap, result — and how do they relate?
2. What does the end-to-end timing flow look like: event setup, roster/tag import, hardware deployment, live capture, processing, results production, publication/export?
3. Which rules govern the output: gun time vs net time, read selection from multiple captures, backup/redundancy, synchronization to the start signal, results validation before release?
4. Who operates the system, and how does the timer role relate to the organizer (roster ownership, data hand-off)?
5. How do the different capture technologies (passive/active RFID, photo-finish line-scan, contactless card stations, photocells, touchpads) realize the same model?
6. Which structures are vendor bundling (registration, tracking apps, check-in kiosks, results portals) rather than definitional?
7. Where exactly is the boundary against Race Management Platform, meet management, tracking/telemetry, and generic RFID?

## Representative Products

| Product | Geography / Segment | Why sampled |
|---|---|---|
| RACE RESULT | Germany + US; full-stack vendor (hardware + software + services) | Full-stack pole: transponders + decoders + RACE RESULT 14 software; the software page documents the entire timing workflow in one place |
| MYLAPS | Netherlands; global timing-technology incumbent ("since 1982") | Market giant pole; deepest hardware-system documentation (BibTag system: decoder, mats, tags, clocks, timing & scoring software) |
| ChronoTrack | US; timing-company ecosystem serving "Timing Partners" | Timer-services pole: hardware exclusive to timing companies; cloud scoring (ChronoTrack Live); remote device control (Fusion); demonstrates the timer-as-business structure |
| SPORTident | Germany; orienteering lineage, station/card model | Regional/technology pole: contact and contactless control-station capture, offline-first; proves the model without mats/decoders and without live connectivity |
| FinishLynx | US; photo-finish systems (track & field, rowing, horse racing) | Capture-technology pole: photo-finish line-scan + Fully Automatic Timing (FAT); proves the Type is not RFID-specific and documents the official-timing rules |

Rejected/avoided: MYLAPS help center (Salesforce portal, article depth not attempted after main pages sufficed), RACE RESULT knowledge-base article depth (portal reachable but article fetch budget spent on product/system pages), ChronoTrack support portal (not reached; root + hardware + scoring pages were sufficient), tracking-first and meet-management products (out of scope for this pass; recorded as boundary neighbors only).

## Sources

### Fetched directly (Layer A unless noted)

- RACE RESULT homepage — https://www.raceresult.com/ — fetched 2026-09-09
- RACE RESULT, "Timing-Software" (RACE RESULT 14) — https://www.raceresult.com/en-us/software/index — fetched 2026-09-09
- RACE RESULT, "Timing-Systems" (hardware systems overview + configurator) — https://www.raceresult.com/en-us/systems/index — fetched 2026-09-09
- RACE RESULT, "For Timers" — https://www.raceresult.com/en-us/solutions/timer — fetched 2026-09-09
- MYLAPS homepage — https://www.mylaps.com/ — fetched 2026-09-09
- MYLAPS, "BibTag System" — https://mylaps.com/active-sports/bibtag-system/ — fetched 2026-09-09
- ChronoTrack homepage — https://chronotrack.com/ — fetched 2026-09-09
- ChronoTrack, "Hardware" — https://chronotrack.com/hardware/ — fetched 2026-09-09
- ChronoTrack, "Scoring" — https://chronotrack.com/scoring/ — fetched 2026-09-09
- SPORTident homepage — https://www.sportident.com/ — fetched 2026-09-09
- FinishLynx homepage — https://www.finishlynx.com/ — fetched 2026-09-09
- FinishLynx, "What is Fully Automatic Timing (FAT)?" — https://www.finishlynx.com/about-us/what-is-fully-automatic-timing/ — fetched 2026-09-09

### Reused from the adjacent pass (Layer A, fetched 2026-09-09, recorded in research/race-management-platform.md)

- RunSignup RaceDay Real-Time product page — https://info.runsignup.com/products/raceday/ (RaceDay Scoring "Compatible with all major chip systems, including MYLAPS, Chronotrack, RFID, Race Result"; two-way sync with participant data; offline scoring)
- Zone4 product page — https://zone4.ca/about/products (GoChip chips, Timing Software, RapidCam photo-finish camera, Summit Timers, timing services)

### Source-access limitations

- Help-center **article depth** was not reached for RACE RESULT (help portal served, articles not fetched), MYLAPS (Salesforce help portal not fetched), and ChronoTrack (support portal not fetched). Internal scoring mechanics (exactly how duplicate reads are resolved, exact processing rules) are therefore **not verified at article level**; claims in this pass are calibrated to the product/system-page level, which is rich for structure but thin for precise internal rules.
- Vendor performance figures (detection rates >99.8%, timing resolution 0.01 s, max passing speeds 40 km/h, 40,000 fps camera rates, athlete/event counts) are **vendor specifications/marketing figures** and are used only as attributed vendor claims, never as independent facts.
- Meet-management software (e.g., track & field meet record systems) was not sampled; the boundary to that neighbor is drawn conceptually, not from product evidence.

---

## Product A — RACE RESULT (full-stack vendor)

### Key observations (all Layer A)

**Hardware systems layer (timing stack):**
- Two transponder technologies: **passive (UHF)** — low-cost, disposable bib-attached tags ("Bib with Transponder", "Transponder on roll") or reusable (HuTag) — and **active** — battery-powered, reusable, higher precision. Vendor's configurator states the trade-off explicitly: passive suits races not requiring accuracy beyond 0.2 seconds ("1.7 meters at 30 km/h"); active offers "up to 0.004 seconds (4 cm at 30 km/h)".
- Capture infrastructure: **Ubidium** system with ground antenna; **loop cable** ("a thin wire laid out as a rectangle at timing points", under/inside the track for motorsports); **Decoder** (System 5000S legacy); **Track Box** (active/passive) for tracking; USB Timing Box, Management Box, Loop Box; **Chip2Go**.
- **Configurator** (hardware setup wizard) asks: sport; accuracy required; ground-antenna restrictions; start/finish proximity; number of **split timing points** ("intermediate measuring points, not including the start and finish line"); live vs at-finish transmission of splits; start times live or at finish; net time vs gun time; disposable vs reusable transponders; participant count; motorsport specifics (surface, track width, top speed at timing point, loop cable under track, fixed transponder position by regulation).
- **Net time vs gun time defined by the vendor**: "Net Time: Every participant gets his individual start time — the moment when he crosses the start line. Gun Time: Every participant gets the same start time — the moment of the gun shot."
- Disposal/return economy: "Disposable transponders will not be collected after the race… Reusable transponders need to be collected from participants after the race." Rental pool exists ("Rental Equipment").

**Software layer (RACE RESULT 14 — "timing and event management software"):**
- Positioning: "covers everything from registration and bib assignment to live timing and results publishing" — a full-stack bundle whose center is the timing workflow.
- **Before the race:** create the event file (templates or custom; "manage multiple disciplines, complex wave starts, and flexible checkpoint configurations"); "Import registrations or link to registration tools"; "Configure timing points including start, splits, and finish lines. Set up age groups, team rankings, and custom result categories. Apply your own scoring rules."
- **On race day:** self-service check-in kiosk (check in, sign waivers, collect bibs, receive pre-assigned items); live results and tracking via my.raceresult.com, event screens, or embeds; announcer views; "Track timing data live from all points — start, split, and finish. Monitor device status, troubleshoot remotely, and adjust settings on the fly."
- **At the finish:** "Automatically calculate results using flexible templates. Generate age group rankings, team scores, or custom awards"; finisher certificates; "Organize the return of rental transponders and timing gear… Track what's been returned"; share race data via API.
- Advanced scoring: "Handle splits, penalties or multi-laps with ease. Customize your scoring…"
- Offline-first: "Works even if your internet doesn't. All functions continue seamlessly, with automatic syncing once connectivity is restored." Offline software is free; online hosting/results/registration is per-participant.
- **Manual backup capture as a first-class tool**: EventTools app — "Manual backups no longer need to be written on paper, simply key in the bib and record the time immediately"; BLE Reader app scans passive transponders at remote checkpoints "and send the time directly to your event file. All data is backed up to your device."
- **Aurora app**: remote access to timing hardware — "configure the decoder and track box, monitor the battery status and receive push notifications when there are important status changes."
- **Presenter** (live results dashboards for big screens) and **Checkin Kiosk** as ready-made output surfaces.
- "Supports any format: Run, cycle, triathlon, enduro, stage rally or backyard ultra."

**Timer-as-customer structure ("For Timers" page):**
- "Hundreds of companies worldwide specialized in time keeping rely on RACE RESULT technology… We provide the necessary technical infrastructure, trainings and extensive support to our timers worldwide."
- Volume/discount model for timers on passive tags; a signed "Contract for Using the RACE RESULT System" gates discount eligibility.
- "Race timers usually buy 2-5 systems which are sufficient for most of their events. For large events, they can flexibly rent additional systems."
- Manufacturing-as-a-service: race numbers, safety pins, transponders manufactured and shipped on the timer's behalf.

## Product B — MYLAPS (incumbent, hardware-system depth)

### Key observations (Layer A; performance figures are vendor specs)

- Positioning: "Since 1982, MYLAPS technology has been a global leader in sports timing… Serving 20,000+ events annually in 100+ countries" (vendor figures). Splits its business by **Motorsports** (X2 Timing System, X2 Pro, X2 Race Control, RC & Drone) and **Active Sports** (BibTag, ProChip, Horse Racing).
- **BibTag System** component structure (the clearest hardware decomposition in the sample):
  - **BibTag Smart Decoder** — "precise and accurate detection of participants in real time"; vendor spec: detection rate >99.8%, timing resolution 0.01 sec, max passing speed 40 km/h; "Recommended use: Start, finish, and intermediate timing points at any scale event."
  - **Mats as antennas** — "The modular mats serve as the system's antennas and detect the signals sent out by the ThinTags"; timing point length 1–8 m per decoder; EasyMat rollable variant "to setup your timelines within 1 minute and limit road closures."
  - **Tags** — ThinTag attached to the bib ("sends a unique UHF signal to identify the runner"); MultiSportsTag worn around the ankle under a wetsuit with "3 integrated timing tags"; BibTag Clip (reusable); SeatPost Tag for cycling detected by **SideAntennas** ("freeing the road from obstacles").
  - **Timing Clock** — electronic scoreboard ("Count up or down between 1 hundredth of a second to 99h59min59s") mounted at start/finish.
- **Timing & Scoring software**: "A complete and easy-to-use software package to set up and time a race and create and publish reliable results. Features: Multiple starts, splits, races, and courses in a single event. Extensive diagnostics."
- Services bundling (platform-side capabilities sold by a timing vendor — evidence that bundling crosses the seam): Cloud Timing, EventApp (live tracking, leaderboards, rankings), Registration ("all-in-one registration page"), Fundraising, Live Photos, results platform ("custom branded results page with good search functionality").
- **Find a Timer / MYLAPS Sports Service**: "Find a Timer" partner directory and staffed timing service — the timing-company role again; athletes own transponders with subscriptions ("Renew subscription", "Manage transponder") — a transponder-account model on the athlete side.
- Blog taxonomy evidences the domain's own teaching: "What's the difference between an active and passive timing system?", "6 Tips for BibTag equipment maintenance", "How do you time a running race?" (titles only; not fetched).

## Product C — ChronoTrack (US timer-company ecosystem)

### Key observations (Layer A)

- Positioning: "the only Timing Company in the world that can deliver… for Athletes, Timers, Race Directors and Spectators"; hardware "Exclusive to ChronoTrack Timing Partners" — hardware access is gated to partner timing companies. "Find a Timer" directory on site.
- **Hardware line** (all Layer A product descriptions):
  - **Kairos** — "next-generation timing system ecosystem"; modular; "Remote monitoring and management capabilities."
  - **AeroTrack** — "All-in-one UHF RFID tag reader and mobile device"; built-in WiFi/cellular; "Saves all of your off-line updates."
  - **PRO2 controller** — rugged case; touch screen; 8 antenna connections; "**NTP Time-Syncing**"; built-in WiFi and GPRS cellular modems; interchangeable batteries; AC power.
  - **MiniTrack** — smaller controller; "**Mechanical Gun Start Button**" (the start reference is a physical instrument on the controller).
  - **FlashPoint** — "original and most trusted side antenna"; "Use as a standalone timing line or as a **backup timing line** at your start/finish… Mat-less splits, anywhere on course."
  - **Timing Mats** ("nearly indestructible", ADA-compliant full-size) and **Timing Tags** ("Single-Use Bib Tags, Single-Use Triathlon Tags, Re-Usable Triathlon Tags, Bike Tags" — "we can time it" for run/walk/bike/tri/OCR/swim/kayak).
- **Scoring software**:
  - **ChronoTrack Live 2.0** — "Because ChronoTrack Live is cloud-based, your entire team can work on the same event at the same time, and should you lose connectivity on-course your data is saved. A NEW Scoring Engine… for any size event"; reporting; athlete search; product screenshot literally titled "ChronoTrack Tag Reads" — the read record is the software's central object.
  - **Fusion** — remote timing operation: "Remotely View: Battery Status, Antenna Status, Power Status, Reader Power. Remotely Control: Reader Channels, Markers, Acknowledge and View Alerts, Active Loop and Channels, Event and Point Names, Immediate Mode."
  - **Launch** — "intuitive race day solution for packet pickup and announcer kiosks"; offline bib & tag assignment and athlete check-in; announcer kiosk.
  - **Athlinks** — results/athlete side: tracking, live results, finisher certificates, SMS results.
  - **MobileTrack** — free mobile app "can time your athletes anywhere and in any conditions" (iOS/Android) — a phone-as-capture pole.
- "Our scoring and race results software takes timing to a new level of accuracy… complex timing for races of all distances including **lap and wave management**."

## Product D — SPORTident (station/card pole, orienteering lineage)

### Key observations (Layer A)

- Core model stated by the vendor ("How it works"): "The SPORTident system is comprised of two basic elements: **stations and cards**. Stations are placed on the race track. Each station has a unique control number. Every athlete carries a SPORTident card which **records the time and control number as he or she passes the stations** during the race. After the race, the SPORTident card holds the athlete's start-finish time, split times as well as all control numbers. This data is used to evaluate the race."
- Two timekeeping solutions: **SPORTident classic** (contact punching; "in use for almost 20 years and in more than 65 countries" — vendor figures) and **SPORTident AIR+** (contactless, active SIAC card worn by the athlete).
- Offline-first by design: "Our hardware will happily run unattended, timing your participants, and waiting for you to pick it up after the race"; stations run on battery for years (vendor claim); data lives in the card/station until read out.
- Product families: Cards, Stations, Radios, Sets, Software, Accessories; a documented **User Guide** (docs.sportident.com) and developer program.
- Services: equipment **hire**, **Online-Entry**, **Result Service** (SPORTident Center / All Results), **Timekeeping Service** ("a complete on-site timing service by our experienced Timing-Team").
- Sport scope: orienteering (leading position claimed), MTB enduro ("Set up the stages with your bike and a backpack. Get live results"), school sports, trail/ultra/triathlon/lap runs/adventure races.

## Product E — FinishLynx (photo-finish / FAT pole)

### Key observations (Layer A)

- Positioning: "certified, ultra-high-speed photo finish imaging and **Fully Automatic Timing (FAT)**"; certification references: "World Athletics / NCAA / USATF / NFHS Certified Results."
- **FAT definition (vendor's education page)**: "a widely used method of sports timing that produces digital race results accurate to at least 1/100th of a second (0.01), and often up to 1/1000th of a second (0.001). FAT systems rely on **precise synchronization between the start signal, running time, and capture device**… A true FAT system is **triggered automatically by the start signal**—unlike manual timing methods such as stopwatches—eliminating human reaction time… The finish is also captured electronically."
- **Core components** enumerated: **Photo-Finish Camera** ("aimed at the finish line captures 1,000 frames per second for accurate, time-stamped results images"), **FinishLynx Software** ("captures photo-finish results & integrates hardware like scoreboards, wind gauges, and additional cameras"), **Start Sensor** ("detects the start signal and instantly relays it… for accurate fully automatic timing").
- **Capture-technology breadth acknowledged**: "Common timing methods include photocells, full-frame video cameras, touchpads (used in swimming), and digital line-scan cameras."
- **Legitimacy rules** (vendor claim): "many governing bodies—including World Athletics—do not recognize [RFID systems, photocells, traditional video cameras] as valid FAT systems, since they cannot verify accuracy through standardized testing methods such as zero-control gun tests. For this reason, line-scan photo-finish technology remains the global standard for elite competition."
- Line-scan mechanics: the image is "a series of incredibly thin vertical image slices from the finish line… Each image slice is timestamped"; "Click on any competitor, and you can see the exact moment a torso, tire, ski, or skate crossed the finish line" — the evaluation loop: capture → timestamped image → operator clicks/positions lines → "Save & print results – accurate to 1/1000th of a second."
- Ecosystem breadth: RFID chip timing products also sold ("Cameras for Chip Timing"), false start detection, electronic start systems, scoreboards, broadcast overlays, live results; "Run It Yourself. Own your system." — the self-operated pole.
- Sports: track & field, cross country, cycling/BMX, motorsport, horse racing, rowing, speed skating, road racing.

## Boundary poles from the adjacent pass (reconciliation)

- **RunSignup RaceDay Scoring** (from race-management-platform research, Layer A, 2026-09-09): "Compatible with all major chip systems, including MYLAPS, Chronotrack, RFID, Race Result, and more"; two-way sync with RunSignup participant data; offline scoring; real-time scoring dashboard. **Reading from this side:** this is the **scoring end of the timing stack implemented without owned hardware** — reads come from third-party decoders, the roster comes from the registration platform. It satisfies this Type's model (points + reads + association + scoring) while its vendor is a race platform. Center-of-gravity, not contradiction: the product is a timing-stack component sold by a platform vendor.
- **Zone4** (same source): GoChip chips, Timing Software ("Live results, photos, racer tracking, Commentator system and TV results"), RapidCam photo-finish camera, Summit wireless timer, staffed **Race Timing Services**, plus registration. **Reading from this side:** timing stack is its center of gravity with registration bundled — the mirror image of the platform vendors bundling scoring.

---

## Cross-product Comparison

| Dimension | RACE RESULT | MYLAPS | ChronoTrack | SPORTident | FinishLynx |
|---|---|---|---|---|---|
| Capture technology | Passive UHF bib tags + active transponders; decoder + ground antenna/loop cable | Passive UHF tags on bib/ankle/seatpost; decoder + mats/side antennas | UHF RFID tags + controllers + mats/side antennas; phone app capture | Contact stations + athlete cards (classic) or contactless active cards (AIR+) | Line-scan photo-finish camera + start sensor (+ RFID accessories) |
| Timing points | Start, splits, finish ("intermediate measuring points") | "Start, finish, and intermediate timing points" | Standalone or backup lines; "mat-less splits anywhere on course" | Stations along the track, each with a control number; start-finish + splits | Finish line (+ start signal as the zero reference) |
| Identification substrate | Tag code on bib/ankle/vehicle | Tag code (bib/ankle/clip/seatpost) | Tag code (bib/tri/bike) | Athlete's personal card number | Lane/bib position in the photo-finish image (human-placed lines) |
| Start reference | Gun time vs net time (explicitly configurable) | Timing clock; start/finish points | "Mechanical Gun Start Button" on controller | Start station records start time on card | Start sensor triggered by the start signal (definitional for FAT) |
| Unit of record | Reads per tag per point → results | Tag reads at decoder points | "Tag Reads" (screenshot-named object) | Time + control number records stored in card | Timestamped image slices → placed lines per competitor |
| Offline capability | Offline software free; sync when connected | Cloud Timing available (variant) | Data saved on loss of connectivity; offline Launch | Unattended battery stations; data in card until read-out | Local capture/evaluation workflow |
| Device monitoring | Aurora app: battery, push alerts, remote config | "Extensive diagnostics" (software feature) | Fusion: remote view/control of battery/antenna/reader | Hardware runs unattended; pickup after race | Camera calibration guides; support/training |
| Scoring/results software | RACE RESULT 14 (templates, age groups, teams, penalties, laps) | "Timing & Scoring software… create and publish reliable results" | ChronoTrack Live (cloud scoring engine) | Data "used to evaluate the race"; Result Service | FinishLynx software; certified results |
| Results output | my.raceresult platform, presenter screens, API, certificates | Branded results page; Sporthive platform | Athlinks live results, SMS, certificates | SPORTident Center / All Results; printout sets | Certified results; scoreboards; print |
| Tag/credential economy | Disposable vs reusable; rental pool; return tracking | Disposable vs reusable tags; athlete-owned transponders with subscriptions | Single-use vs reusable tags | Athlete-owned cards (SIAC battery service) | Not tag-based (image-based identification) |
| Operator role | Professional timers (contract + volume discounts); organizer self-op possible | Timing companies (Find a Timer); staffed Sports Service; athlete transponder accounts | Exclusive to partner timing companies; Find a Timer | Clubs/organizers self-op (no computer needed); Timekeeping Service | "Run it yourself" self-op; professional timers; officials |
| Registration/organizer bundling | Registration import or link; check-in kiosk | Registration, fundraising, event app services | Launch packet-pickup kiosk; Event Dashboard mention | Online-Entry service | None observed (integrates with meet workflows via accessories) |

**Cross-product commonalities (Layer B):**
- Every sampled system measures the event at **defined timing points** — start and finish at minimum, intermediate split points common (RACE RESULT configurator, MYLAPS decoder "recommended use", ChronoTrack lines/splits, SPORTident stations, FinishLynx finish + start reference).
- Every sampled system's raw unit of work is an **identified time record**: tag ID + timestamp + point (three RFID vendors), control number + time in a card (SPORTident), timestamped image + competitor line (FinishLynx).
- Every sampled system binds captures to **participants** via a carried credential or an image/lane evaluation, over a participant list that comes from outside the timing system (import/integration — confirmed directly at RACE RESULT "Import registrations or link to registration tools" and RunSignup RaceDay Scoring's sync; structurally implied elsewhere).
- Every sampled system produces **times and results** as its output (scoring software, results platforms, certified print/export).
- Every sampled system has an **offline / continuity posture**: data survives connectivity loss (ChronoTrack, RACE RESULT) or never depends on connectivity at all (SPORTident); manual/backup capture paths exist (RACE RESULT EventTools manual key-in; ChronoTrack FlashPoint backup line; MobileTrack app as lightweight capture).
- The **timer / timing company** appears as a distinct operator role in four of five samples (RACE RESULT For-Timers program, MYLAPS Find-a-Timer + Sports Service, ChronoTrack Timing-Partners exclusivity, SPORTident Timekeeping Service); FinishLynx supports both self-operation and professional timers.
- **Redundancy** is a designed concern (backup lines, manual key-in backup, second tags in MultiSportsTag, start-signal synchronization).

---

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate)

A Race Timing System is recognizable as such only if all four hold:

1. **Timing points as the measured structure** — the event is measured at defined points on the course: a start reference and a finish point at minimum, with intermediate split points common. Remove → a stopwatch/photocell gadget with no course structure.
2. **Instrumented capture producing identified time records** — a dedicated capture apparatus (transponder read by decoder/antenna field, control station + carried card, photo-finish camera synchronized to the start signal) automatically produces records binding an identification to a precise timestamp at a timing point. The capture is instrumented — synchronized to the start reference and designed to remove human reaction time from official measurement — with manual capture relegated to backup. Remove → manual timekeeping / a results compiler working on hand-entered times.
3. **Participant association via a roster/credential binding** — captures are bound to specific participants through a mapping between the carried credential (bib tag, ankle band, card, vehicle transponder, lane/image position) and the participant list; that roster is imported or synced from the organizer/registration side — the timing system consumes the roster, it does not own registration. Remove → anonymous detection logging (traffic counting / asset tracking).
4. **Computation of official times and results** — raw records are processed into participant times (with the start-reference choice — gun time vs net time — made explicit) and competitive results (placings, divisions, laps), validated by the operator, and delivered as the event's official time output (publish/export to results surfaces or the organizer's platform). Remove → a capture logger whose data is never turned into official times.

Jointly-held load-bearing checks:
- 1 alone = timing gadget (photocell set, scoreboard clock)
- 2 without 1 = generic RFID reader / drone race lap counter with no event structure
- 1+2 without 3 = anonymous detection log (counts bodies, not competitors)
- 3 without 1+2 = results spreadsheet over hand-entered times (meet/results-compiler or organizer-side territory)
- 4 without 1+2 = results software with no capture story (platform-side scoring over foreign feeds remains in-type because it consumes 1+2 outputs from third-party decoders)
- 1+2+3 without 4 = data logger; 2+3 without 1 = lap counter with no course model

### L1 — Common Mature Structure (common in the sample, not definitional)

- Split points with live data transmission (or at-finish transmission where connectivity is absent)
- Device/hardware monitoring and remote control (battery, antenna, reader status; push alerts; remote configuration)
- Backup/redundancy machinery: backup timing lines, manual key-in of bib+time, phone-app capture, duplicate tags on one athlete
- Lap and wave management; penalties; multi-discipline/multi-course events in one file
- Scoring templates: age-group rankings, team scores, custom result categories
- Results publishing: vendor results platforms, presenter/announcer screens, scoreboards, certificates, API/export
- Tag/credential lifecycle: assignment (auto at registration / bulk / at packet pickup), distribution, collection of reusable tags, rental pools, loss prevention
- Check-in / packet-pickup kiosks with bib & tag assignment (bundled organizer-side work)
- Live participant tracking / leaderboards for spectators (apps and pages)
- Photo/video (non-measurement), participant communication (email/SMS)

### L2 — Variant / Optional Structure

- **Capture technology** per sport and scale: passive UHF bib tags ↔ active battery transponders ↔ contactless/station cards ↔ photo-finish line-scan ↔ photocells/video/touchpads ( FinishLynx enumerates the breadth)
- **Disposable vs reusable** credentials and the return/collection economy; athlete-owned transponders with subscriptions (MYLAPS model) vs event-supplied tags
- **Operator model**: professional timing company operated (ChronoTrack exclusivity; MYLAPS/RACE RESULT/SPORTident services) ↔ club/organizer self-operated (SPORTident "without even touching a computer", FinishLynx "run it yourself")
- **Connectivity posture**: cloud/live-first with offline fallback (ChronoTrack, RACE RESULT) ↔ fully offline-first (SPORTident)
- **Business model**: hardware purchase + supplies (timer discounts, contracts) ↔ per-participant software/hosting fee ↔ staffed timing service ↔ equipment hire
- **Sport packaging**: mass road races, triathlon, cycling, motorsports (lap timing), orienteering (point-to-point), track & field (FAT), horse racing, rowing
- **Results venue**: vendor-owned results portal ↔ organizer's platform (results feed exported/imported) ↔ print/scoreboard

### L3 — Vendor-specific Structure (stays here)

RACE RESULT: RACE RESULT 12/14, my.raceresult, Ubidium, Track Box, Chip2Go, EventTools/Aurora apps, Presenter/Kiosk, exact price tables and discount contracts. MYLAPS: BibTag/ProChip/X2 systems, ThinTag/MultiSportsTag/SeatPost Tag, EasyMat, Speedhive/Sporthive, EventApp, BrandScan, RunnerTag, "since 1982" and event-count figures. ChronoTrack: Kairos, AeroTrack, PRO2, MiniTrack, FlashPoint, Launch, Fusion, MobileTrack, ChronoTrack Live, Athlinks, Timing-Partner exclusivity, patent page. SPORTident: SI-Card/SIAC, AIR+, Printout Set BT, SPORTident Center, IOF approval claims, battery-service program. FinishLynx: EtherLynx/Vision PRO X, LuxBoost, 40,000 fps, zero-control gun test discourse, NFHS approvals. RunSignup RaceDay Scoring naming and chip-system compatibility list (from prior pass). Zone4 GoChip/RapidCam/Summit (from prior pass).

---

## Historical / Market-Sample Check

- **Paper-era lineage**: finish-line judges with stopwatches + a start gun + hand-recorded time sheets + a posted results board has the right *shape* (points, records, association, results) but fails the instrumented-capture leg as modern products realize it — the sampled vendors themselves define their value against "manual timing methods such as stopwatches" (FinishLynx FAT page). Hand timing is best held as the **conceptual ancestor**, not an in-type realization: the Type's distinguishing promise is that official times are produced by instrumented, start-synchronized capture.
- **Older technology generations still fit the L0**: film photo-finish cameras (capture instrument + start sync + identified image records) satisfy the model without any RFID; SPORTident classic (1990s-era contact punching, "in use for almost 20 years" per vendor) satisfies it without connectivity, decoders, or live results; the earliest chip-timing generation satisfies it with ankle-worn reusable tags and at-finish read-out. None of today's common machinery (cloud scoring, live tracking, apps, kiosks) is required by the definition.
- **Regional check**: German full-stack (RACE RESULT), Dutch incumbent (MYLAPS), US timer ecosystem (ChronoTrack), German orienteering specialist (SPORTident) all fit without US-specific machinery; sport packaging differs (motorsports lap timing vs orienteering control points vs road-race splits) but the four legs hold in each.
- **Anti-overfit**: RFID is NOT definitional (FinishLynx is in-type with zero transponders); live results are NOT definitional (SPORTident classic evaluates after the fact); cloud is NOT definitional (offline-first poles in-sample); the timer company is NOT definitional as a *business* (self-operated poles in-sample) even though the timer role is structurally near-universal; registration-in-the-same-product is NOT definitional (FinishLynx/SPORTident have no registration; RACE RESULT explicitly supports import-or-link).

---

## Vendor-specific Findings

- RACE RESULT: net-vs-gun configurator question; free-offline/per-participant-online pricing; timer volume-discount contracts; manufacturing-as-a-service for bibs/pins.
- MYLAPS: MultiSportsTag with three integrated tags (redundancy at the tag level); EasyMat 1-minute setup; athlete transponder subscriptions; "detection rate >99.8%" spec claim.
- ChronoTrack: hardware exclusive to Timing Partners; Mechanical Gun Start Button; Fusion remote control verbs (markers, immediate mode); Athlinks as the results/athlete platform.
- SPORTident: data-in-the-card storage model; card read-out after race; SIAC battery service; IOF certification claims; school-sports packaging.
- FinishLynx: FAT legitimacy discourse (World Athletics non-recognition of RFID/photocells as FAT; zero-control gun test); torso-crossing evaluation convention ("click on any competitor… torso, tire, ski, or skate"); equipment-ownership philosophy.
- From the prior pass: RunSignup RaceDay Scoring's named chip-system compatibility list; Zone4's commentator/TV output and staffed timing services.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (with removal test) |
|---|---|---|
| **Race Management Platform** (§28, processed) | deepest seam — RATIFIED from this side | The platform owns the **organizer-side event operations**: event pages, registration/roster, participant self-service, commerce, race-day logistics; it **consumes** timing output. The timing system owns the **timekeeping machinery**: capture apparatus, reads, time computation; it **imports** the roster. Remove the capture/timing stack from a platform → it stays a race platform; remove roster/registration/event operations from a timing stack → it stays a timing system. Cross-seal evidence: platform vendors bundle scoring (RunSignup RaceDay Scoring over third-party chips) and timing vendors bundle registration (MYLAPS Registration, RACE RESULT import-or-link, Zone4) — bundling crosses the seam in both directions without collapsing the Types. Zone4 and RunSignup are center-of-gravity calls already recorded by the platform pass; this pass concurs. |
| **Sports Meet Management / meet record systems** (§28 sibling) | record-vs-instrument neighbor | Meet management holds the meet's records (entries, event schedule, seeds, standings, records book) and compiles results; it does not measure anything itself. Timing systems measure. Results flow timing → meet record; entries flow meet record → timing. Not sampled at product depth — boundary drawn conceptually. |
| **Sports/Event Registration Platforms** (§28/§26) | upstream data neighbor | They create the roster the timing system imports; no capture, no times. Remove the roster-creation and keep scoring-over-imported-rosters → timing system. |
| **Tracking / spectator-tracking apps** (e.g., athlete map tracking services) | output-adjacent | Tracking consumes timing reads (and/or GPS) to show progress; its unit of record is position/progress, not official time. Position-first products are a different Type. |
| **Generic RFID / asset tracking / industrial IoT** (§14/§16) | same technology, different semantics | Same read machinery, but records bind things (assets, vehicles in logistics) without competitive time semantics or official results. Remove competition/results → asset tracking. (RACE RESULT itself ships a separate asset-tracking product — vendor-level confirmation of the split.) |
| **Sports video / broadcast tools** | adjacent media | Broadcast/video captures images for viewing; a photo-finish camera is a measurement instrument whose timestamped image is evidence for official times. Zone4's broadcast software (prior pass) is presentation, not measurement. |
| **Endurance Training Platform** (§28, processed) | opposite side of the event | Athlete-side plans/targets; no measurement of the event. No seam conflict. |

## Uncertainties

1. **Internal scoring mechanics are unverified at article depth** — how sampled products resolve duplicate reads per tag per line, exactly how gun/net offsets are applied per wave, and how missed-read corrections are workflowed. Stated only as capabilities ("advanced scoring logics", "flexible templates", "scoring engine"), never as precise rules.
2. **MYLAPS Cloud Timing and ChronoTrack Timer Portal internals** not reached; ChronoTrack's Event Dashboard (registration-side product) not explored — ChronoTrack's own bundling across the seam is therefore under-documented.
3. **Touchpads (swimming) and photocell-based systems** were acknowledged by FinishLynx as capture methods but no swimming-specific vendor was sampled; the FAT-recognition claim is a single-vendor (FinishLynx) statement about governing bodies — treated as vendor-attributed, not as established rule.
4. **Relative market weight** (MYLAPS vs RACE RESULT vs ChronoTrack share) unknown; vendor-count figures are marketing numbers.
5. **Historical anchor dates** (e.g., the 1982/1990s lineage claims) rest on vendor self-description; no independent history source was fetched, so no historical dates appear in the final document.

## Final Synthesis

A **Race Timing System** is the event's timekeeping machinery: it measures the competition at defined **timing points** through an **instrumented capture apparatus** (transponder + decoder/antenna field, control station + carried card, or photo-finish camera synchronized to the start signal), producing **identified time records** — credential ID + timestamp + point — which it binds to **participants imported from the organizer's roster** (bib/tag/card mapping) and processes into **official times and results** (gun vs net start reference, splits/laps, divisions), validated by the timer and delivered to the event's results surfaces or the organizer's platform. Its operator is most often a **professional timing company** (with self-operation common at club/school scale); its defining separateness from the Race Management Platform is that it **consumes the roster and produces the times**, while the platform **creates the roster and consumes the times** — a seam both passes have now ratified from their own sides. Around this core, mature products add device monitoring, backup capture, lap/wave handling, scoring templates, results platforms, tracking, kiosks, and tag-lifecycle machinery; capture technology (RFID vs photo-finish vs stations), connectivity posture (cloud vs offline-first), and the business model (hardware sales vs staffed service vs per-participant software) are the great variant axes. Remove the capture apparatus and it is a results compiler; remove the participant binding and it is an anonymous detection logger; remove the official-times computation and it is a data logger; remove the roster import and own the registration/event too — then it has crossed into Race Management Platform territory.
