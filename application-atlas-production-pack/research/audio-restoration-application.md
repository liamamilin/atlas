# Research Notes — Audio Restoration Application

Research date: 2026-09-06
Methodology: v1.1 (update-v1/WORKFLOW_v1.1.md, WRITING_GUIDE_v1.1.md)

---

## Research Goal

Understand the Application Type **Audio Restoration Application** (DIRECTORY 04.09 Audio) from real products: what its world consists of, what users do, how repair work flows, which rules constrain it, and where it borders the three sibling leaves of 04.09 — Audio Editor, Digital Audio Workstation / DAW, Podcast Editing Application — plus adjacent Types (noise-reduction plugin suites, media transfer/conversion utilities, forensic audio, AI voice enhancement).

This pass is also the **joint review from the restoration side** of the flag recorded in the audio-editor pass ("restoration looks like an emphasis variant of the same editing core").

## Initial Boundary

Temporary hypothesis before research:

- Core use: repairing **impaired recordings** — noise, clicks/crackle, hum, clipping distortion, reverb, speed errors, dropouts — rather than editing sound generally or composing music.
- Users: post-production dialogue/forensic engineers, remastering/archival engineers, restorers of vinyl/tape transfers, podcasters/creators cleaning voice.
- Nearest neighbors: Audio Editor (repair as capability inside an editor), DAW, Podcast Editing Application, noise-reduction plugin bundles, analog-media transfer utilities, forensic audio, AI voice enhancement services.
- Likely boundary: a restoration product is **organized around the impairment → repair loop**; an editor is organized around general operations (cut/split/trim/process) with repair as one capability.
- Unknowns: is the spectrogram/spectral editing definitional? Is the standalone editor form definitional (vs plugin-only suites)? Is "diagnosis" a real, product-visible structure or just folklore? Do consumer products (wizards) still fit? Did AI change the shape?

## Research Questions

1. What are the core objects — the audio material, the impairment, the repair processor, the profile/learn, the output?
2. Which impairment classes do products explicitly name and build processors for? Is there a stable taxonomy across products and eras?
3. What does the workflow look like: diagnose → treat → verify? Is processing order a real, documented rule?
4. How do "learn/profile/adaptive" noise models work as user-facing structures?
5. How is before/after verification exposed (preview, compare, residual monitoring)?
6. What product forms exist: standalone app, editor with integrated repair, plugin-only suite, archive system, consumer wizard?
7. Where do AI/ML features change the model (auto-detection assistants, neural separation, one-knob enhancement)?
8. What interfaces does the user face (spectrogram/waveform editor, module windows, assistants, batch, in-host plugin surfaces, wizards)?
9. What rules/constraints matter (processing order, artifact risk, program-material preservation, offline-vs-realtime limits, what is unrepairable)?
10. Where exactly do the boundaries to Audio Editor / DAW / Podcast Editing / plugins / transfer utilities / forensic tools lie ("remove/add what to become the other Type")?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Philosophy / Tier | Documentation used |
|---|---|---|
| iZotope RX 12 | the pro-market standard; standalone restoration suite + editor + plugin family; module-per-impairment; AI assistants | izotope.com product page (Tier 2) + docs.izotope.com RX 12 user guide incl. "Identifying Audio Problems" (Tier 1) |
| Acon Digital (Acoustica + Restoration Suite 2) | prosumer; restoration delivered both inside an editor and as a plugin-only suite; adaptive/profile noise modeling | acondigital.com product pages for Acoustica and Restoration Suite (Tier 2) |
| CEDAR Audio (CEDAR Cambridge / ICONS / Studio / Forensic lines) | high-end specialist; archives & national libraries, broadcast, remastering, forensics; real-time restoration pioneer | cedar-audio.com home, /applications/audiorestoration (Tier 2) + official "Audio Restoration Workflow" knowledge article (Tier 1-equivalent technical reference) |
| Diamond Cut Audio Restoration Tools (DCart) / Forensics | long-running dedicated restoration family; vintage-media restoration + forensics variant | diamondcut.com catalog + DCart 11.09 product page (Tier 2; operational detail limited) |
| NCH Golden Records | consumer tier; analog-to-digital transfer wizard with embedded restoration tools | nch.com.au/golden product page (Tier 2) |

Considered and **excluded due to source inaccessibility**:

- Adobe Audition (restoration-effects help page) — helpx.adobe.com timed out (1 attempt this pass; 2 attempts already failed in the audio-editor pass). Used only as a named boundary example already established by the sibling pass; no new claims made about it.
- Steinberg WaveLab — not attempted this pass; failed twice in the audio-editor pass; no claims made.

Consequence: claims below rest on the five accessible samples; the "editor with strong restoration" tier (Audition/WaveLab) is covered only indirectly (via Acoustica's self-description as editor+restoration+mastering platform, and via the editor pass's WavePad/Audacity evidence).

## Sources

- iZotope RX 12 product page: https://www.izotope.com/en/products/rx.html
- iZotope RX 12 user guide: https://docs.izotope.com/rx12/en/index-en.html
- iZotope RX 12 user guide — Identifying Audio Problems: https://docs.izotope.com/rx12/en/identifying-audio-problems.html
- Acon Digital Acoustica: https://acondigital.com/products/acoustica/
- Acon Digital Restoration Suite: https://acondigital.com/products/restoration-suite/
- CEDAR Audio home: https://www.cedar-audio.com/
- CEDAR Audio — Audio Restoration applications page: https://cedaraudio.com/applications/audiorestoration
- CEDAR Audio — "Audio Restoration Workflow" technical reference: https://cedaraudio.com/article/000001/audio-restoration-workflow
- Diamond Cut Productions catalog: https://diamondcut.com/ ; software category: https://diamondcut.com/product-category/software/ ; DCart 11.09 product page: https://diamondcut.com/product/diamond-cut-audio-restoration-tools-10-62/
- NCH Golden Records: https://www.nch.com.au/golden/index.html
- (attempted, inaccessible) https://helpx.adobe.com/audition/using/noise-reduction-restoration-effects.html — timeout
- (help.izotope.com 403 — RX docs reached instead at docs.izotope.com)

## Product Observations

### iZotope RX 12 (Evidence layer A — official product page + full user guide)

- Self-positioning: "audio restoration software to fix every flaw"; "Industry-standard audio repair and post production"; "50+ tool audio restoration software, the industry standard for post"; tagline context "rescue dialogue, avoid ADR, and save the scene". Editions: Elements / Standard / Advanced. Stated user domains: Post Production, Music Production, Content Creation.
- **Product form**: standalone editor application + "20+ plugins that can load in your DAW or NLE" (module-equivalents as plugins); host integration documented via AudioSuite (Pro Tools offline render + Learn), ARA (RX Spectral Editor in Logic), RX Connect (round-trip from Audition/Pro Tools/Cubase/Nuendo), external-editor hooks for Premiere/Logic/Resolve, RX Monitor.
- **Module = the organizing unit**, named after the impairment: De-click, De-crackle, De-clip, De-hum, De-plosive, De-reverb, De-rustle, De-wind, De-bleed, De-ess, Mouth De-click, Breath Control, Spectral De-noise, Voice De-noise, Guitar De-noise, Dialogue Isolate, Spectral Repair, Spectral Recovery, Interpolate, Ambience Match, EQ Match, Wow & Flutter, Azimuth, Deconstruct, Music Rebalance, Scene Rebalance, Leveler, Loudness Control/Optimize, Trim Silence, plus utility modules (Gain, Normalize, Fade, EQ, Time & Pitch, Resample, Dither, Phase, Markers, Signal Generator, Spectrum Analyzer, Waveform Statistics).
- **Diagnosis is a first-class documented structure** — user-guide chapter "Identifying Audio Problems" opens: "As with medical diagnostics, the key to successful audio restoration lies in your ability to correctly analyze the subject's condition." Provides an official **RX Processing Step Flowchart** (impairment → module decision tree) and a spectrogram-signature taxonomy:
  - Hum: electrical noise, low-frequency tone (50/60 Hz base) + harmonics → horizontal lines in spectrogram → De-hum.
  - Buzz: electrical noise extending to higher frequencies (>~400 Hz) → Spectral De-noise often more effective.
  - Hiss / broadband noise: spread across the spectrum → speckles surrounding program material → Spectral De-noise / Voice De-noise.
  - Clicks, pops, short impulses: vertical lines; sources include vinyl/shellac transfer, digital errors, buffer misconfig, bad edits, mouth noises → De-click / Mouth De-click.
  - Clipping: "squared-off" waveform tops (waveform display, not spectrogram) → De-clip ("intelligently redraw the waveform to where it might have naturally been").
  - Intermittent noises: coughs, sneezes, footsteps, car horns, ringing cell phones → Spectral Repair (attenuate/replace).
  - Gaps and drop outs: missing/corrupted sections → delete gap + Spectral Repair replace.
- **Module-level structures**: parameters with Preview and **Compare** (Common Module Controls: "Module Footer — Preview, Compare"); **Learn** (capture noise profile / reverb profile / hum fundamentals) and Adaptive modes (Spectral De-noise "Learn", "Adaptive Mode"; De-hum Static vs Dynamic Adaptive mode); Noise Spectrum Display; Artifact Control; per-module "Alternative Modules" pointers (cross-referenced repair paths); Instant Process tools (attenuate/de-click/fade/gain/replace directly on selections).
- **Repair Assistant**: "intelligently recognizes and proposes fixes for specific problems that you can tweak to your taste" — Voice Mode (Clean Up / Tone / De-Ess / De-Clip) and Music Mode (Clean Up / Tone / De-Harsh / De-Clip); available as module and as plugin.
- **Workflow infrastructure**: Module Chain; Batch Processor (Input files → Module Chain → Output naming/format); Undo History (resizable panel, exportable as XML); RX Documents (save editable state); Export file/selection/regions; Composite View for multi-file work; spectrogram/waveform display with clip-gain envelopes, markers & regions; text navigation (transcript, multiple-speaker detection).
- **Purpose statements**: De-clip "extremely useful for reducing distortion in recordings that were made in a single pass, such as live concerts, interviews, and any audio that cannot be re-recorded"; De-crackle for "vinyl recordings"; Azimuth repairs "improper tape head alignment" stereo/phase issues; Wow & Flutter for tape speed deviations; Spectral Recovery restores missing bandwidth (legacy/lossy sources); Ambience Match fills noise-floor beds under constructed dialogue/ADR.
- **ML posture**: "Powered by pioneering machine learning tech"; new/rebuilt neural nets for Dialogue Isolate, Music Rebalance, Breath Control, De-bleed; real-time plugin versions of some modules.

### Acon Digital (Evidence layer A — official product pages)

**Acoustica 7** (editor):
- Self-positioning: "a complete audio editing, restoration and mastering platform. Standalone application. Full plugin suite." Standard edition: "spectral and stereo clip editing, multitrack editing, restoration and mastering tools. Also features ARA support with compatible DAWs."
- Spectral editing marketed as: "Fix problems that traditional editing can't touch. See and remove unwanted noise — a cough, a creak, a rogue frequency — without affecting the audio around it." Selection tools: area/brush/freehand/magic wand; **Retouch tool** ("attenuates noise in time-frequency selections"); retouch in spectral domain.
- **Audio Restoration** feature block: "Turn problem recordings into usable ones. Whether it's background noise, clicks, crackle, clipping or a muddy live recording, Acoustica's integrated restoration tools help you recover audio that would otherwise be unusable."
- **Dialogue Cleaning Suite** (Premium): DeWind, DeRustle, DeBuzz, DePlosive, DeClick, DeEss, DeBird — "AI-trained suite tackles the noise problems that crop up most in real-world dialogue work — wind, lavalier rustle, buzz, hum, plosives, mouth clicks and even birdsong."
- **Extract:Dialogue 2** (Premium): "uses AI to automatically separate spoken voice from background noise and reverb" — one-knob AI speech cleaning.
- **Cleaning Wizard**: "simplifies LP or tape to CD transfers" — archival transfer workflow inside the editor.
- Restoration tools present in-app (Standard: Restoration Suite 2 tools incl. DeNoise *Light* "static noise profile only and fewer parameters"; Premium: full suite) — edition-tiered repair depth.
- General editing substrate: unlimited undo, Edit History pane, batch processing "files and complete folder structures", labels/regions, CD projects/burning, analysis (spectrum, spectrogram, wavelet, statistics, loudness EBU R-128), multitrack editor, VST/VST3/AU hosting, ARA2 clip editor + AAX Transfer plug-in for Pro Tools round-trip.

**Restoration Suite 2** (plugin-only product, four processors):
- Positioning: "Suite of four plug-ins for professional grade audio restoration… remove noise, distortions, and unwanted artifacts **without harming the sound you want to keep**."
- **DeNoise**: "reduces noise in adaptive mode or based on noise analysis" (noise-profile mode); v2 adds **dynamic noise profiles** "that capture the dynamic properties of the noise so that noise that fluctuates over time, such as wind noise, can be effectively reduced"; transient detection; temporal smoothing to reduce "musical noise" artifacts; **Solo Noise mode** to listen to the removed signal.
- **DeHum**: targets hum/buzz "from poorly grounded electrical equipment" + motor noise; **Scan button** "automatically fine tunes the fundamental hum frequency"; sinusoidal re-synthesis vs notch mode; adaptive mode for fluctuating fundamentals; harmonic count (up to 96); **Solo Hum mode**.
- **DeClick**: "impulsive noise such as clicks, crackle and thumps. Frequently encountered on LP and 78 RPM records, but also occur in digital recordings due to drop-outs or distorted data packets"; thump reduction covers vocal plosives; separate detection of clicks/crackle/thumps/plosives; **Residual signal mode** to audition what was removed.
- **DeClip**: "Reconstructs peaks distorted by analog or digital clipping"; upper/lower thresholds on level histograms.
- Stated use cases: vinyl/cassette/archival tape transfers; "Repair clipped or overloaded recordings **without re-recording the source**".
- Formats: VST/VST3/AAX/AU; surround up to 7.1.6.

### CEDAR Audio (Evidence layer A — official site + official technical reference article)

- Self-positioning: "The inventors of real-time audio restoration, digital dialogue noise suppression, adaptive limiting and spectral editing." Emmy/CASAR/AMPs awards displayed; product history page.
- **Market structure** (applications page "Software Solutions for Audio Restoration"): "small sound libraries and huge national archives… share a need to create clean copies of the sounds held on aged and decaying media."
  - **CEDAR Cambridge** — archive-scale system: "digitisation, metadata generation, single- and multi-user processing, file distribution and report generation"; integration with MAM systems "enabling restoration to be automated."
  - **ICONS plug-ins** — "eleven of the most important processes within CEDAR Cambridge": Declick, Manual Declick ("Repair long clicks, scratches, drop outs and extended digital errors"), Decrackle, Dethump, Declip 2, Debuzz, Auto Dehiss, Retouch ("The original, and best, spectral editor"), DNS One (dialogue noise suppression), VoicEX 2 (AI noise suppression), plus Blade EQ (analyser EQ).
  - Additional lines: Studio (Dethump/Manual Declick/Retouch), Forensic (Forensic Enhance), Live Broadcast hardware+real-time plugins (DNS 8S; Voxis "low-latency neural network voice isolator" for live), Film & TV, Music Production, Remastering.
- **Official "Audio Restoration Workflow" technical reference** — the richest cross-vendor workflow document found:
  - History: "Back at the birth of digital audio restoration in the late 1980s… the rule was **declick – decrackle – dehiss**, and it never varied" (spectral subtractive dehissers of the era destroyed the information declickers need).
  - **Degradation taxonomy tied to the recording's life story**: resonant coloration at capture; dust/groove deviations and coarse disc materials; groove wear and scratches from playback; tape hiss ("Even with suitable biasing, tape is hissy"); **azimuth errors** (inter-channel timing, smearing); **wow/flutter and speed aberrations** from tape machines; digital dropouts and clicks ("dropped samples and clocking errors"); lossy compression (MP3-class); one-off events ("somebody slammed a door… in the quietest and most emotive part of the song").
  - **Golden rule**: "Removing noise is simple… you have removed all of the problems, but with an unacceptable side effect… removing noise is easy, but doing so without introducing unwanted artefacts is hard… The golden rule here is to concentrate on the **quality of the wanted signal** in the output rather than concentrating solely on how much noise you can remove."
  - **Documented processing order** (guideline): 1) **Declipping** (first; "It's vital that the audio level is reduced at this point or the reintroduced peaks will be clipped again"; "you will be unable to correct a clipped voice or instrument within an otherwise unclipped mix"); 2) **Declicking and decrackling** (before anything that changes bandwidth or works in the frequency domain; "Don't be tempted to over-process… Remove the tiny impulses that comprise crackle… using a dedicated decrackler"); 3) **DC filtering**; 4) **Manual declicking and dethumping** (extended clicks; "Take care to retain the atmos… you will obtain holes in the ambient noise"); 5) **Debuzzing and speed correction** (order depends on when the buzz entered the signal; "Don't attempt to eliminate the fundamental and its harmonics using EQs… hollow sound"); 6) **Azimuth correction** (after debuzz, else detectors lock to the hum); 7) **Retouching** (spectral editing of discrete noises — coughs, dropped items, doors; "ensure that the background noise remains… consistent"); 8) **Broadband noise reduction** (last stage of the restoration chain; "this is where you are most likely to create artefacts"); 9) **Audio sweetening** (EQ/dynamics/loudness — subjective, applied with care).

### Diamond Cut Audio Restoration Tools / Forensics (Evidence layer A for positioning; operational detail limited)

- Company tagline: "Audio Restoration Tools and Archival Music"; sells music archives (historic recordings), books/videos, and **seven software products**.
- Product family: **Diamond Cut Audio Restoration Tools 11.09 ("DCart")** $59; **Diamond Cut Forensics 11.0 Audio Laboratory** $749; AFDF Automatic Forensic Adaptive Filter $399; VVA VST plugin; test-CD set. A free "Before and After" demo section; Knowledge Base; user forum.
- DCart 11.09 page (feature evidence):
  - "Three Step Easy Restoration Wizard in the Task Panes. Get professional results quickly"; Task Pane "steers the user to the correct solution based on their audio goal"; "Green Zones to guide filter slider settings"; 2,000+ descriptive factory presets.
  - Stated uses: "Clean up your old records and tapes"; "Clean up recorded conversations, speeches, concerts, etc."; make MP3s/CDs; transcription/time expansion; format conversions; audio & acoustical measurements.
  - Restoration-relevant tools named in changelog/features: **CNF (Continuous Noise Filter) presets re-done with "re-sampled noise fingerprints"** (noise-profile learning); **Harmonic Noise filter** with 100/120 Hz options ("less obtrusive line noise removal" — mains hum); **Wind Noise Filter**; **Change Speed system**; **Virtual Phono Preamp** incl. balance meter "for optimum restoration of Vertically recorded material" (hill-and-dale/78 rpm era); **Paste Interpolate** ("easy waveform interpolation"); spectrogram + histogram views; Make Wave generator; VST hosting.
- Forensics variant exists as a separate, higher-priced product (Audio Laboratory) + dedicated forensic adaptive filter.
- Limitation: no operational user manual reachable this pass; finer workflow details unverified.

### NCH Golden Records (Evidence layer A — official product page)

- Positioning: "Convert vinyl records & cassette tapes to digital audio" — an easy-to-use **wizard** guiding the conversion; Mac/Windows.
- Restoration tools listed: "Restoration tools automatically clean up damaged audio"; "Remove **hiss, clicks and pops** from old tapes or scratched records"; "Normalize the volume"; "Apply **dc offset correction** when converting analog to MP3"; RIAA phono EQ in software ("no pre-amplifier is required"); "Convert **78 RPM records** playing on a 45 RPM player" (speed correction); automatic silence-based track splitting; CD burning; encode MP3/WAV.
- Advanced editing explicitly delegated to the sibling product WavePad ("If you want to perform advanced editing… try WavePad").
- Structural read: a **transfer/conversion utility with embedded restoration** — the consumer, wizard-shaped minimal form of repair work; the restoration features are the same impairment classes (hiss/clicks/pops, DC offset, speed) with fixed "automatic" settings.

## Cross-product Comparison

| Structure / capability | iZotope RX | Acon (Acoustica + RS2) | CEDAR (Cambridge/ICONS) | Diamond Cut DCart | Golden Records | Assessment |
|---|---|---|---|---|---|---|
| Existing recording (often un-re-recordable) as working material | ✔ ("cannot be re-recorded") | ✔ ("without re-recording the source") | ✔ ("aged and decaying media") | ✔ ("old records and tapes") | ✔ (vinyl/cassette transfer) | **Defining** — all five |
| Named impairment classes organize the processing | ✔ (module-per-impairment; diagnosis chapter) | ✔ (De* naming; dialogue-cleaning suite) | ✔ (product-per-impairment; workflow article taxonomy) | ✔ (CNF/Harmonic Noise/Wind/Change Speed/Interpolate) | ✔ (hiss/clicks/pops/DC/speed) | **Defining** — all five |
| Dedicated repair processors matched to impairment classes | ✔ (50+ modules) | ✔ (4–11 processors) | ✔ (~15 across lines) | ✔ (dozens of filters) | ✔ (a few automatic tools) | **Defining** — all five |
| Restored audio as output; judged by program-material preservation | ✔ ("without artifacts") | ✔ ("without harming the sound you want to keep") | ✔ ("golden rule… quality of the wanted signal") | ✔ (restoration of usable audio) | ✔ (cleanup in service of the transfer) | **Defining** — all five |
| Diagnosis before treatment (identify impairment by listening/looking/analysis) | ✔ (official "Identifying Audio Problems" + flowchart) | ✔ (spectral views, analysis tools; wizard) | ✔ (workflow article; analysis-EQ lineage) | ✔ (spectrogram/histogram; Task Panes steer diagnosis) | ✔ (automatic detection inside wizard; minimal user diagnosis) | **Defining** (diagnosis step; may be automated) |
| Spectrogram view + time-frequency (spectral) editing/selection | ✔ (primary surface; Spectral Repair) | ✔ (spectral editor, retouch tool) | ✔ (Retouch — "original… spectral editor") | ✔ (spectrogram views; interpolate) | — (waveform screenshots only) | Common (absent in the consumer wizard → not defining) |
| Learn/profile/adaptive noise modeling | ✔ (Learn + Adaptive modes) | ✔ (profile mode, adaptive mode, dynamic profiles) | ✔ (Auto Dehiss; adaptive lineage) | ✔ (noise fingerprints; CNF presets) | — (fixed automatic) | Common |
| A/B verification (preview/compare; audition removed/residual signal) | ✔ (Preview + Compare in every module) | ✔ (Solo Noise/Hum/Residual modes) | ✔ (guidance to listen for artifacts) | (presets/live preview implied; not confirmed) | — | Common (3/5 confirmed; not defining) |
| Documented processing ORDER (impulses before broadband NR; sweetening last) | ✔ (Processing Step Flowchart) | (presets/order not fetched) | ✔ (full ordering doctrine) | (wizard encodes an order) | ✔ (wizard = fixed order) | Common-to-structural; strongly documented in 2, implicit in 2 |
| AI/ML assistance (auto-detect + propose fixes; neural separation) | ✔ (Repair Assistant; neural Dialogue Isolate/Music Rebalance/Breath Control/De-bleed) | ✔ (Extract:Dialogue 2; AI-trained dialogue suite) | ✔ (VoicEX 2, Voxis neural voice isolation) | — | — | Common in current pro tier (3/5); emerging |
| Module chains + recommended fix sequences | ✔ (Module Chain; Repair Assistant chain) | ✔ (processing chains) | ✔ (Restore bundles "tailored to the task") | ✔ (Task Panes/3-step wizard) | ✔ (wizard) | Common |
| Batch processing at file/folder scale | ✔ (Batch Processor) | ✔ (files + folder structures) | ✔ (archive throughput; automated restoration via MAM) | (likely; not confirmed) | ✔ (one file per pass; wizard) | Common |
| Repair delivered as plugins into DAW/NLE hosts | ✔ (20+ plugins; ARA/AudioSuite/Connect) | ✔ (Restoration Suite 2; ARA2; Transfer plug-in) | ✔ (ICONS/Studio/Forensic plugin lines) | ✔ (VVA VST; VST hosting) | — | Common product form |
| General editing substrate inside the product | ✔ (full editor) | ✔ (full editor) | (systems/plugins; Retouch is editing) | ✔ (full editor + recorder) | — (delegated to WavePad) | Common but **not defining** (plugin-only and wizard forms exist without it) |
| Media-transfer capture support (phono preamp/RIAA, speed correction) | ✔ (Wow & Flutter, Azimuth) | ✔ (Cleaning Wizard) | ✔ (speed correction in doctrine) | ✔ (VPP, vertical-cut balance, Change Speed) | ✔ (RIAA EQ, 78→45) | Common; strongest in the vintage-media segment |
| Archive-scale system features (multi-user, metadata, reports, MAM automation) | — | — | ✔ (CEDAR Cambridge) | — | — | Product-specific (single source) |
| Forensic-oriented products | (post-production emphasis) | — | ✔ (Forensic Enhance; Trinity) | ✔ (Forensics Audio Laboratory; AFDF) | — | Variant tier (2/5 confirmed) |
| Consumer wizard form | (Elements = entry edition, still editor) | — | — | (3-step wizard inside editor) | ✔ (whole product) | Variant surface (segment-dependent) |
| Real-time/live versions (broadcast) | (real-time plugins for some modules) | (real-time preview) | ✔ (DNS One/8S, Voxis — live sound/broadcast) | — | — | Variant (2/5; CEDAR strongest) |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

Four properties. Removing any one stops the product from being recognizable as an Audio Restoration Application:

1. **A degraded recording as the working material.** The input is sound that already exists and carries an impairment — noise, impulses, distortion, unwanted ambience, speed errors, dropouts, discrete events. Implicit in the Type: the material is often irreplaceable (aged media, single-pass live captures, location dialogue) — the reason repair, rather than re-recording, is the only option.
2. **An impairment model: named classes of problems.** The product's world is organized around a catalog of degradation classes (broadband noise/hiss; hum/buzz; clicks/crackle/pops/thumps; clipping/distortion; reverb; wind/rustle/plosives/mouth noise/breaths; speed errors (wow/flutter) and azimuth; dropouts/gaps; discrete intermittent noises). This catalog is what the product's processing, documentation, and workflow are structured around.
3. **Repair processors matched to those classes**, applied to diagnosed regions or to the whole material, with the explicit goal of **preserving the program material** while suppressing the impairment. (CEDAR's "golden rule", Acon's "without harming the sound you want to keep", RX's "without artifacts" — the preservation goal is the Type's quality contract.)
4. **Restored audio as output** — the repaired recording is rendered/exported (or delivered onward into a downstream pipeline).

Notes:
- The **diagnosis step** (identify what is wrong before treating) belongs to the Type's defining loop, but it may be performed by ear, by eye (waveform/spectrogram), by analysis tools, or automatically (assistants) — the *step* is defining, its *surface* is not.
- Historical check (§24-style): the L0 holds for late-1980s digital restoration (CEDAR's documented declick–decrackle–dehiss era), for hardware-era broadcast units, for classic desktop restoration tools (Diamond Cut), and for current ML-based products — all keep: degraded material, impairment classes, matched processors, program preservation, restored output. The spectrogram, learn-profiles, AI assistants, plugin forms, wizards are era/market accretions, not definition.

### L1 — Common Mature Structure

Present in most mature products; expected but not definitional:

- **Spectrogram + waveform diagnosis surfaces** — frequency-over-time display with impairment-specific visual signatures (horizontal harmonics = hum, vertical lines = clicks, speckle = broadband noise, flat tops = clipping); spectrum analysers, waveform statistics; time-frequency selection and "retouch" editing in pro tools.
- **Learn / profile / adaptive noise modeling** — capturing a noise profile/fingerprint from a sample; continuously adaptive tracking of changing noise; automatic detection of hum fundamentals and reverb profiles.
- **Before/after verification** — preview with bypass, compare multiple settings, audition of the removed/residual signal ("Solo Noise/Hum", residual modes); the removed-signal monitor is a distinctive user-facing behavior of this Type.
- **Ordered repair sequences** — impairment processors applied in a principled order (distortion → impulses → tonal/electrical → speed/azimuth → discrete spectral events → broadband noise → sweetening); shipped as flowcharts, wizards, task panes, module chains, assistant-proposed chains.
- **AI/ML assistance and neural processing** — automatic problem detection with proposed fixes; ML source separation (dialogue isolation, de-bleed, de-reverb); rebuilt "De*" modules as neural nets.
- **Batch processing** — applying a repair chain across many files/folders; archive-scale throughput; watch/folder processing.
- **Host integration** — the same processors as plugins (VST/AU/AAX/AudioSuite) and ARA clip-editors inside DAWs/NLEs; round-trip transfer utilities; external-editor hooks.
- **A general audio-editing substrate** — most standalone restoration products contain a real editor (files, selection, undo/history, markers, gain/fade/EQ utilities, export) because repair is region-oriented work; but plugin-only suites and consumer wizards prove the substrate is not the definition.
- **Media-transfer support for vintage sources** — phono preamp/RIAA EQ, speed correction (wrong-speed transfers, wow/flutter), azimuth correction, DC offset removal, silence-based track splitting.

### L2 — Variant / Optional Structure

Depends on segment, era, deployment:

- **Product form**: standalone desktop suite+editor (RX, Acoustica, DCart) ↔ plugin-only suite (Restoration Suite 2, CEDAR ICONS) ↔ archive-scale system (CEDAR Cambridge: multi-user, metadata, reports, MAM-integrated automated restoration) ↔ consumer transfer wizard (Golden Records) ↔ real-time broadcast processors (DNS line, Voxis).
- **Customer tier / domain emphasis**: consumer (LP/cassette rescue) → prosumer → post-production dialogue rescue (broadcast/film) → music remastering → archives/national libraries → forensics (separate forensic product lines with evidence-oriented tooling).
- **AI posture**: classical DSP vs neural nets; explicit per-impairment modules vs one-pass "enhance" operations (one-knob AI voice cleaning sits at this Type's edge — impairment model implicit in the model weights rather than user-selected).
- **Processing execution**: offline/offline-render (AudioSuite-style) vs real-time; some heavy processors are offline-only (high latency), others have real-time plugin versions.
- **Extended restorative-adjacent processing**: source/stem separation and rebalancing (dialogue/music/effects), spectral bandwidth recovery for band-limited/lossy sources, ambience matching, dialogue contour/pitch repair.
- **Forensic variant**: intelligibility enhancement and analysis for legal/security contexts (distinct products/lines).
- **Surface**: desktop-dominant; historical hardware; live-sound hardware+plugins; consumer wizards.

### L3 — Vendor-specific (kept out of the final document)

- iZotope RX: module names and the 50+ module count; "Repair Assistant" Voice/Music modes (Clean Up/Tone/De-Ess/De-Harsh/De-Clip); RX Processing Step Flowchart; RX Documents; Composite View; Stems View; export-history-as-XML; RX Connect/Monitor/ARA Spectral Editor; edition ladder (Elements/Standard/Advanced); pricing.
- Acon: dynamic noise profiles; DeHum Scan button + 96-harmonic bound; Solo Noise/Hum/Residual modes; Cleaning Wizard; De*Dialogue suite naming (DeWind/DeRustle/DeBird…); Extract:Dialogue 2; ARA2 clip editor; AAX Transfer plug-in; edition tiering (Standard/Premium/Post Production Suite); 7.1.6 surround support; pricing.
- CEDAR: CEDAR Cambridge system; Retouch trademark ("the original… spectral editor"); ICONS bundle; DNS One/8S; VoicEX 2; Voxis; Forensic Enhance; Trinity (surveillance); the official workflow article's ordering doctrine and "golden rule"; "inventors of real-time audio restoration" claim.
- Diamond Cut: DCart/Forensics split and pricing; CNF "noise fingerprints"; Harmonic Noise filter 100/120 Hz options; Virtual Phono Preamp with vertical-cut balance meter; Task Panes / 3-step wizard / Green Zones; Paste Interpolate; AFDF forensic adaptive filter; 2,000+ presets.
- NCH: Golden Records RIAA no-preamp hardware pairing; 78→45 RPM conversion; delegation to WavePad/MixPad siblings; wizard steps.

## Boundary Findings

**vs Audio Editor** (sibling leaf; the audio-editor pass flagged restoration as a possible emphasis variant):
- The editing substrate is nearly identical (waveform/spectrogram, selection, processing, render). The difference is the **organizing purpose**: a restoration product's world is the impairment catalog and the repair loop — its marketing, documentation, and workflow all name problems (De-click, De-hum…) and encode diagnosis/order doctrine (RX's diagnosis chapter + flowchart; CEDAR's workflow article; wizards that steer by problem). An editor's world is general operations on sound, with repair as one capability among many (editor-pass evidence: WavePad lists noise reduction beside echo/amplify; Audacity treats it as one effects area).
- Market test passes for distinctness: multiple products exist whose **entire product** is the repair loop (RX; CEDAR Cambridge/ICONS; DCart; Acon Restoration Suite as a suite-only product), and the market leader self-identifies as "audio restoration software", not an editor. Dedicated-Type status held.
- BUT the boundary is a **gradient, not a wall**: editors bundle increasingly strong repair (editor-pass finding), and editor-first products self-describe as "editing, restoration and mastering platform" (Acoustica). Judgment rule: remove the impairment catalog + diagnosis/order structure → what remains is an editor; demote repair to one effect among dozens → editor with repair capability.
- This resolves the audio-editor pass flag from the restoration side: same shared core, distinct Type on the organizing-purpose test. Podcast Editing Application flag remains for its own pass.

**vs Digital Audio Workstation / DAW**: restoration products do not compose — no MIDI, instruments, loop construction, or arrangement as primary surfaces. None of the five samples positions itself near music creation except remastering (working on finished mixes). Clear boundary on working material + absence of composition layer.

**vs Podcast Editing Application**: podcast-first products restructure around episodes/transcripts/publication. Restoration products have no pipeline objects; podcast cleanup is a use case performed inside this Type (CEDAR even publishes a podcast-cleanup guide for its processors). Domain use case, not the same Type.

**vs noise-reduction / restoration plugin bundles**: a single processor (or a 4-pack) is a capability; this Type is the application that organizes many such capabilities with diagnosis, ordering, verification, and delivery. When a vendor ships the suite as a standalone product form (Acon Restoration Suite 2), it is a product-shaped instance of this Type's processor layer; the organizing application frame (editor/host/assistant/batch) then lives in the host or a sibling editor.

**vs analog-media transfer/conversion utilities**: Golden Records shows restoration embedded in a transfer wizard. When the product's center of gravity is format/medium conversion with cleanup as an automatic step, it is a transfer utility (adjacent); restoration becomes the Type proper when impairment diagnosis and treatment are the product's purpose and depth.

**vs forensic audio**: forensic lines (CEDAR Forensic/Trinity, Diamond Cut Forensics) reuse this Type's processors for intelligibility enhancement, and add evidence handling, analysis, and investigative workflows beyond restoration. Restoration is the substrate capability of forensic audio work.

**vs AI voice/audio enhancement services (one-knob "enhance")**: automatic single-pass speech enhancement (Acon Extract:Dialogue 2 as an in-suite instance; CEDAR VoicEX/Voxis as processors; cloud services adjacent) keeps the repair goal but drops the user-facing impairment step. Treated here as an L2 posture of repair processors (AI posture variant), not a separate Type — but watch: if "enhance" products lose the impairment model entirely and reorganize around a subscription speech-quality service, they may deserve their own leaf (none exists in the current directory).

**"去掉什么就变成另一个 Type" 判据**:
- 去 impairment catalog + diagnosis/order 结构，留一般编辑操作 → Audio Editor。
- 加 composition 层（MIDI/instruments/arrangement）→ DAW。
- 加 episode/transcript/publishing pipeline → Podcast Editing Application。
- 把 repair 降为众多 effects 之一 → editor with repair capability; 把 repair 升为全部世界 → 本 Type。
- 把 input 从"已有录音"换成"prompt 生成" → AI Audio Generator（另一个 family 的 Type）。

## Uncertainties

- **Editor-with-strong-restoration tier unverified this pass**: Adobe Audition (timeout ×1 this pass; ×2 in the editor pass) and Steinberg WaveLab (not attempted) could not be fetched. Their structural fit (restoration toolchains inside editor/mastering products) is consistent with Acoustica's self-description and the editor-pass evidence, but no direct claims were made about either product in the final document.
- **CEDAR Cambridge operational detail** (exact workflow, batch semantics, report structure) rests on the applications page summary; no manual was reachable. Claims kept at positioning level.
- **Diamond Cut operational workflow** (exact wizard steps, filter semantics) rests on catalog + changelog evidence; fine workflow detail unverified. Claims kept at capability level.
- **A/B verification spread**: confirmed directly in 3/5 samples (RX, Acon, CEDAR guidance); kept as L1 common, not defining.
- **Order doctrine spread**: fully documented in CEDAR's official article; RX ships an official flowchart (image — text of individual steps not extractable this pass); wizards imply fixed orders in consumer products. The canonical ordering is stated in the final document at the level of "order matters, impulses before broadband noise reduction" rather than a precise universal sequence.
- **One-knob AI enhancement boundary**: whether cloud "enhance" services drift into a separate Type is unresolved; no directory leaf exists; recorded as a watch item.
- Numeric vendor facts (module counts, harmonic bounds, prices, edition splits) recorded only here, not in the final document.

## Final Synthesis

The Audio Restoration Application is an **impairment-centric repair application**: it takes a recording that already exists and is in some way damaged or compromised — often material that cannot be re-recorded — organizes its entire world around named classes of degradation (broadband noise, hum/buzz, clicks/crackle, clipping, reverb, wind/rustle/plosives, speed/azimuth errors, dropouts, discrete noises), and treats each with dedicated processors under a preservation contract: maximize the quality of the kept program material, not the amount of noise removed. The defining loop is diagnose → treat → verify: identify the impairment (by ear, eye, analysis, or AI assistant), apply the matched processor in a principled order, audition before/after (including the removed signal), iterate, and render repaired audio. Spectrogram diagnosis, learned/adaptive noise profiles, AI-assisted problem detection, batch chains, and host-plugin delivery are the standard capability set of mature products; the standalone editor, the plugin-only suite, the archive-scale system, and the consumer transfer wizard are the market's product forms. The Type's edge is against the Audio Editor (repair as the whole world vs repair as one capability), the DAW (no composition layer), Podcast Editing (no pipeline objects), and conversion utilities (repair as purpose vs repair as a step).
