# Research Notes — Radio Station Management

Research date: 2026-09-09
Slug: radio-station-management
Directory leaf: Radio Station Management (§27 Media, Entertainment, Creator & Culture)

## Research Goal

Understand what a Radio Station Management application actually is as an Application Type: what objects exist inside it, who operates it, how a radio station's broadcast day is planned and aired, and where its boundary lies against neighboring Types — especially Broadcast Management System (which left a joint-review flag for this leaf), Internet Radio Platform, Newsroom Management System, Podcast Platform, Media Asset Management, and DJ Software.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the Type is the station-side on-air operations system: audio library + broadcast-day planning (music/program log) + automated playout + voice tracking. Commercial traffic/billing belongs to Broadcast Management System; news production belongs to Newsroom Management System; consumer listening belongs to Internet Radio Platform.
- Likely confusions: radio traffic/billing (BMS-shaped), playout automation as a separate capability vs the Type's center, music-scheduling-only products (companion discipline), internet-radio streaming suites, DJ performance software.

## Research Questions

1. What is the central managed record? (hypothesis: the station's daily log / playlist)
2. What objects exist: station, audio library, song/element metadata, clock, rotation, log event, voice track, split/local break, as-run?
3. What is the canonical pipeline: schedule → log → playout → aired output (+ record)?
4. What rules govern: separation rules, automation continuity, traffic-log merge, split rejoin, live-assist vs auto?
5. What interfaces: log editor, library, scheduler, voice-track editor, on-air/presenter screen, remote clients?
6. How do variants differ: terrestrial vs internet-only, single station vs group/network, suite vs standalone scheduler vs open-source, music vs talk formats?
7. Where is the boundary vs Broadcast Management System (joint review), Internet Radio Platform, NRCS, MAM, DJ Software?

## Representative Products

| Product | Vendor | Why selected | Evidence tier reached |
|---|---|---|---|
| Zetta + GSelector | RCS (Radio Computing Services) | Industry-standard suite; explicitly splits automation / music scheduling / traffic-billing into separate products | Tier 2 product pages (root, Zetta, GSelector) |
| WO Aurora | WideOrbit | Independent major; vendor literally markets a "radio station management solution"; pairs with WO Traffic (BMS seam evidence) | Tier 2 product pages (radio solutions, Aurora) |
| DAD | ENCO Systems | Full single-product expression of the station stack (ingest→library→scheduling→playout→voice tracking→logging); LPFM-to-global range | Tier 2 product page (DAD) |
| AzuraCast | AzuraCast (open source) | Internet-radio / self-hosted pole; Tier-1 documentation accessible | Tier 1 docs (about + feature docs) |
| StationPlaylist Creator + Studio | StationPlaylist | Budget terrestrial+internet pole; scheduler + playout split at small scale | Tier 2 product pages (home, product summaries) |

## Sources

- RCS — corporate root: https://www.rcsworks.com/ (fetched 2026-09-09)
- RCS — Zetta product page: https://www.rcsworks.com/zetta/ (fetched 2026-09-09)
- RCS — GSelector product page: https://www.rcsworks.com/gselector/ (fetched 2026-09-09)
- WideOrbit — Radio Solutions page: https://wideorbit.com/radio/ (fetched 2026-09-09)
- WideOrbit — WO Aurora product page: https://wideorbit.com/products/automation-radio/ (fetched 2026-09-09)
- ENCO — DAD product page: https://enco.com/products/dad (fetched 2026-09-09)
- ENCO — corporate root: https://enco.com/ (fetched 2026-09-09)
- AzuraCast — About / docs: https://www.azuracast.com/ and https://www.azuracast.com/docs/ (fetched 2026-09-09)
- StationPlaylist — home page with product summaries: https://www.stationplaylist.com/ (fetched 2026-09-09)
- Prior pass context: research/broadcast-management-system.md and applications/broadcast-management-system.md (joint-review flag)

Sourcing limitations:
- RCS product support/documentation (rcssupport.com) requires login; observations limited to public product pages.
- Marketron (radio traffic) was unreachable in the prior BMS pass (timeout ×2); not retried — the traffic seam is evidenced via WideOrbit/ENCO/StationPlaylist/RCS product pages instead.
- No Tier-1 help-center articles were fetched for the commercial vendors (marketing/product pages only); precise operational parameters (numeric limits, timings, defaults) are therefore not asserted.

## Product Observations

### RCS — Zetta (Radio Automation) + GSelector (Music Scheduling) [Layer A]

Corporate framing (root page): "RCS — Broadcast Software for Radio Automation, Music Scheduling & Streaming"; "the world's largest broadcast software provider"; portfolio described as "Zetta radio playout, GSelector music scheduling, and Aquira traffic and billing—solutions designed to power broadcast operations". Product menu: Zetta, ZettaCloud (cloud playout), GSelector, SelectorCloud (cloud music scheduling), Aquira ("CRM & Sales Proposal Solution"; described in About as "traffic and billing"), RCS News, RCS2GO, Disaster Recovery, Revma ("Professional Grade Streaming"), AudioDisplay.

Zetta ("Radio Automation"):

- Modular services: "the Audio Player service can run independently from the Sequencer, which can be controlled from your console and many other devices thanks to Zetta's GPIO service."
- Zetta2GO (browser client) module list — the clearest single enumeration of the automation surface: "Voice Tracker for recording jock tracks off-air, Segue Editor for dialing in transitions, Logs for station log management, Library for asset management, Hot Keys for local playback or full station control, On-Air for live playout, and more."
- "your audio files are readily available for playback at the right place and the right time" (Audio Engine; mixed sample rates/bit rates/formats).
- ZCast: "share Audio Assets, Logs, Voice Tracks with Heads/Tails, Segue Transitions and Splits between stations and databases."
- Zetta Splits: "Lets a master station send a signal to local stations to play their own local spots and links, then rejoin the master station after the break."
- Emergency On-Air Backup: "Go Local – allows the local computer use a copy of the main database that is saved and synchronized onto the local computer."
- Background Recorder: "record a Show or Satellite Feed for play at a later date or time on an On-Air station."
- Site Replication; ZettaCloud sync/backup/restore; Publish ("offloading of the rendering to separate computers, and also running separate external applications after the file(s) have been created").
- Real-time integration: "starting with Log changes, to Hot Keys updates, to new Media Imports in your Library – changes are instantly reflected everywhere... across the entire RCS suite."

GSelector ("Music Scheduling Reinvented"):

- "Create a station, design clocks, code your songs and GSelector will create a schedule using each song's natural demand." ("Goal Demand Scheduling"; "goal-driven demand-based scheduling engine")
- "Customizable Editor — Every programmer can massage their logs based on their music philosophy."
- "Enterprise Solution — Dial up as many stations as you want. No limits."
- Selector2GO: "continue to add music, schedule, send your logs to your automation and more – all remotely."
- "Data Exchange Job — ...share your database with a consultant"; "Mass Audio Analysis — song audio analysis... applied to more than one song simultaneously."

Interpretation: RCS itself splits the world into three products/disciplines — playout automation (Zetta), music scheduling (GSelector), traffic and billing (Aquira) — plus adjacent products (news, streaming, disaster recovery). The automation product's own module list (Logs, Library, Voice Tracker, Segue Editor, Hot Keys, On-Air) is a near-canonical inventory of the Type's surfaces.

### WideOrbit — WO Aurora [Layer A]

Radio Solutions page: "WideOrbit offers the most complete radio station management solution to keep your business moving and listeners engaged." The "Total Radio Solution" spans: Radio Station Automation (WO Aurora), Ad Traffic Management (WO Traffic), Digital Audio Monetization (WO Digital Hub), Business Insights (WO Data Bridge), A/R Management (WO Payments Suite). Users named: "Broadcast Engineers, Program Directors, and on-air talent" (automation) and "Ad Sales and Traffic Managers" (traffic).

WO Aurora ("Radio Automation Without Limits"; "cloud-powered radio automation"):

- Web Studio: "A browser-based automation interface that gives talent access to the tools they need from anywhere."
- Live Mic: "Broadcast live from virtually any location using just a laptop and a microphone, with no codec, no mixing console, and no on-site engineer required."
- Deployment: on-premises, hybrid, cloud-hosted (AWS-managed).
- "Radio Client — Talent in any market can manage any of your radio stations in real-time."
- "Remote Radio Station Management — Access via web browser, with support for macOS, Windows, and Linux." (the vendor applies the phrase "radio station management" to the automation product's remote access)
- "Multi-Market Voice Tracking — Record voice tracks remotely to leverage talent across markets."
- "Audio Finder — Remotely manage audio libraries from any device in your organization."
- "Customizable UI and User Rights — Show/hide widgets and control what features talent have access to."
- "Remote Content and Playlists — Record, import, edit, and convert content once for cross-market distribution."
- WO AFR Mobile (iOS): "modify programming instantly and on-air talent can control the station during remote broadcasts or sporting events, eliminating the need for a board operator."

Integration seams (the joint-review evidence):

- "WO Traffic for Radio — Comprehensive traffic and invoicing solution. The WO Traffic and WO Aurora integration enables live log editing, playlist delivery, real-time reconciliation, and auto run-date sync."
- "MusicMaster Scheduling — WO Aurora seamlessly integrates with the leading solution for intelligent song replacement, real-time reconciliation, music search, and song card creation."

Interpretation: the automation product is the station-operations center; traffic/invoicing is a separate product whose integration with automation is described as log delivery + reconciliation — exactly the BMS↔RSM seam. Note: the vendor's marketing applies "radio station management solution" to the whole business stack (automation + traffic + digital + payments + data), which is broader than the operational core; the product split remains the structural evidence.

### ENCO — DAD [Layer A]

Positioning: "Powerful Radio Automation"; "The flexible, customizable, and interoperable architecture and interface of DAD support numerous workflows. DAD is the audio playout and automation system trusted by thousands of broadcasters worldwide, from local LPFMs to global broadcasters and station groups."

- "Centralized Content, Regional Splits & Intuitive Control — Share content across multiple stations with localized playlists for each market, insert different content and ads for each OTA and Webstream feed, and easily break away for local commercials, liners, and jingles, then rejoin seamlessly. Fully automate your schedule, or jump-in using DAD's intuitive and customizable Presenter On-Air interfaces for live-assist."
- "All-in-One Solution — Automate content ingest, scheduling, logging, playout, programming, control and more."
- Library: "The media asset manager includes essentials like searchable groups, filtered views, cross-module drag and drop, and highly robust and customizable metadata fields to help you better schedule and log"; Gateway module: "rules-based multi-site file replication and backups across broad networks."
- Voice tracking: "the integrated FastTRAK module, enables voice track insertion into a playlist with just a few clicks. The DAD Editor lets you cut, paste, and add marker placements (segues, timers, etc.). MultiTrack seamlessly integrates between DAD and third-party digital audio workstations, such as Adobe Audition or Hindenburg Broadcaster."
- Scheduling: "The integrated Ensemble Music Scheduling System allows for quick and easy creation of playlists with detailed clocks and rules to prevent duplicates from being accidentally scheduled. Scheduling Wizard offers a toolset specialized for satellite radio programming. ListGen has the ability to interface with any music scheduling and traffic software such as MusicMaster, PowerGold, Marketron, Wedel, or Amily, allowing DAD to fit into your current workflow."
- Ingest: "Using ENCO's ENconveyor and Dropbox modules, you can automate the download of audio files and metadata from Web or FTP sites, or scan watch folders for content to ingest into your DAD libraries."
- Newsroom: "ENCO's MOS Interface allows users to manage audio embedded in stories generated in AP ENPS, AVID iNews, Octopus... automatically sync your rundowns to a DAD playlist. If a last-minute change is made within your newsroom system, the change is propagated to DAD instantly."
- Presenter On-Air Interface: "every feature of the presenter interface is designed to be as easy and quick-to-action as possible... optimized for touchscreen use... instant access to their library, playlists, and more."
- Playout engine: "DAD workstations include up to 16 playback modules, multi-channel audio outputs... Real-time log changes in any studio are instantaneously reflected in all other studios."
- Metadata: "With the included PADapult module, live or scheduled RDS and metadata can be automatically published from each playlist."
- Logging: SideCAR extension — "Radio Logging & Recording... powerful recording and logging capabilities. Web-based interface lets you keep an eye on your station."
- Remote: WebDAD / iDAD / iDAD-Remote / enDROID — "Record voice tracks, send control commands, manage your content, create playlists... whatever you need to run your station, wherever you are."
- AI voice tracking: aiTrack — "users can preschedule automated voice tracks (song intros, stations IDs, localized news and weather), by using generative AI and synthetic voice engines."
- Client case: Dash Radio — "delivers 65 radio stations to listeners worldwide, and automates its entire playout network using DAD... drive up to 12 stations from a single workstation... remote voice tracking."

Interpretation: DAD is the fullest single-product expression of the Type: ingest → library → scheduling (internal rotation engine or external schedulers/traffic via ListGen) → log → playout (automated or live-assist) → voice tracking → splits → logging/metadata → remote. It also names the external ecosystem explicitly: MusicMaster/PowerGold (music scheduling), Marketron/Wedel/Amily (traffic), newsroom systems (MOS), DAWs (editing).

### AzuraCast [Layer A — Tier 1 docs]

Positioning: "a self-hosted, all-in-one web radio management suite. Using its easy installer and powerful but intuitive web interface, you can start up a fully working web radio station in a few quick minutes." "AzuraCast works for web radio stations of all types and sizes."

Core features (for radio stations):

- "Rich Media Management: Upload songs, edit metadata, preview songs and organize music into folders from your browser."
- "Playlists: Add music to standard-rotation playlists (in sequential or shuffled playback order) or schedule a playlist to play at a scheduled time, or once per x songs/minutes/etc."
- "Live DJs: Set up individual DJ/streamer accounts and see who's currently streaming from your station's profile page."
- "Web DJ: Broadcast live directly from your browser, with no extra software needed."
- "Public Pages: ...embeddable public pages... powerful APIs... rich metadata support."
- "Listener Requests: Let your listeners request specific songs from your playlists."
- "Remote Relays: Broadcast your radio signal (including live DJs) to any remote server running Icecast or Shoutcast."
- "Web Hooks: Integrate your station with Slack, Discord, TuneIn, Twitter and more."
- "Detailed Analytics and Reports: Keep track of every aspect of your station's listeners over time. View reports of each song's impact on your listener count. You can also generate a report that's compatible with SoundExchange for US web radio royalties."

Administration: "Role-based User Management: Assign global and per-station permissions"; "Multi-Station Administration: Host multiple stations on a single installation" (from the marketing page). Included software: "Liquidsoap as the always-playing 'AutoDJ'"; "Icecast-KH... as a radio broadcasting frontend" (Shoutcast optional).

Interpretation: the internet-radio pole proves the core structure without terrestrial infrastructure: media library + scheduled/rotation playlists + always-playing automation (AutoDJ) + live DJ accounts + streaming output + analytics/royalty reporting. Voice tracking is absent (live DJs instead); music scheduling is simplified to rotation playlists rather than clock/rule engines. The SoundExchange-compatible royalty report is direct evidence of the aired-record/reporting capability.

### StationPlaylist — Creator + Studio [Layer A]

Positioning: "StationPlaylist Creator + Studio integrate to provide a very affordable and powerful radio broadcasting software solution for terrestrial radio and internet streaming / webcasting. Also suitable for party DJ's and in-store music automation." Used by "commercial and non-commercial AM & FM radio stations, internet streaming stations, clubs, restaurants, malls, and other stores."

- Studio ("on-air broadcast automation playout software"): "Plays all your media files with manual or intelligent / automatic crossfading. Play jingles, commercials, news, songs, live streams, live inputs from your sound card, satellite feeds etc. Includes an internet stream encoder, voice track / song ramp overlapping, many automation and live assist features such as 96 cart slots for instant jingles, timed events, time and temperature announcements while automated, compressor / limiter sound processing, website integration, and much more."
- Creator ("spot and music scheduler"): "Gain complete control over your station format using rotations of music categories and spot groups (jingles, advertisements, etc). Generate sophisticated daily or weekly playlists, with track separation rules for artist, song, genre, tempo, and much more. Also includes a Playlist Editor, Voice Track recording, traffic/billing log file importer, and much more..."
- Remote Voice Tracker: "enables your DJ's to record voice tracks within the scheduled playlist from home, to sound like a live show!"
- Remote Studio: "connects to Studio Pro at the station to enable live shows to be performed remotely via the internet."
- Streamer: stand-alone internet radio stream encoder.

Testimonial (Layer 3, but names the older generation): "I am a Master User on both Scott Studios WideOrbit and RCS NexGen, and find StationPlaylist radio broadcasting software to be most competitive with those two very sophisticated platforms." Another: "In my old job at a big radio station 1995-2001, I worked with the Dalet automation which cost around $150,000."

Interpretation: the budget pole reproduces the same structure at small scale: scheduler (rotations, separation rules) + playout automation (live assist, carts, timed events) + voice tracking + traffic-log import + streaming. The vendor itself documents adjacent reuse (clubs, stores, party DJs) — the same software serving non-station venues as an adjacent use, not the center.

## Cross-product Comparison

| Dimension | RCS Zetta+GSelector | WO Aurora | ENCO DAD | AzuraCast | StationPlaylist |
|---|---|---|---|---|---|
| Station as managed unit | yes (multi-station enterprise) | yes (multi-market, group) | yes (LPFM → global groups; 65-station case) | yes (multi-station per install) | yes (single station; clubs/stores adjacent) |
| Audio library with metadata | yes (Library; media imports) | yes (Audio Finder) | yes (media asset manager, custom metadata) | yes (media management, metadata, folders) | yes (media files) |
| Broadcast-day log / playlist | yes (Logs) | yes (playlists, content) | yes (playlists; real-time log changes across studios) | yes (playlists, scheduled) | yes (daily/weekly playlists) |
| Music scheduling (rotation) | yes (GSelector: clocks, coded songs, demand) | via MusicMaster integration | yes (Ensemble clocks/rules; ListGen to external) | simplified (rotation playlists) | yes (Creator: rotations, separation rules) |
| Automated playout | yes (Sequencer, On-Air) | yes (Web Studio) | yes ("fully automate your schedule") | yes (AutoDJ/Liquidsoap, always-playing) | yes (Studio automation, timed events) |
| Live assist | yes (Hot Keys, On-Air) | yes (Live Mic) | yes (Presenter interface) | yes (Web DJ, live DJ accounts) | yes (live assist, cart slots) |
| Voice tracking | yes (Voice Tracker) | yes (Multi-Market Voice Tracking) | yes (FastTRAK; aiTrack AI) | not observed (live DJs instead) | yes (Voice Track recording; Remote VT) |
| Multi-station / splits | yes (ZCast, Zetta Splits) | yes (any-market clients, cross-market content) | yes (regional splits, localized playlists, break away/rejoin) | yes (multi-station administration) | not observed |
| Traffic-log integration | suite sibling (Aquira traffic & billing) | yes (WO Traffic: live log editing, playlist delivery, reconciliation, run-date sync) | yes (ListGen: Marketron, PowerGold, MusicMaster, Wedel, Amily) | not observed | yes (traffic/billing log file importer) |
| Newsroom integration | RCS News (sibling product) | not observed | yes (MOS: rundown sync) | no | no |
| Ingest automation | media imports (instant reflection) | yes (record/import/edit/convert once, distribute) | yes (ENconveyor, watch folders, FTP) | upload/SFTP | not detailed |
| Aired record / logging | Background Recorder (show/satellite capture) | real-time reconciliation (with traffic) | SideCAR (logging & recording) | analytics; SoundExchange royalty report | not detailed |
| Now-playing / metadata out | not observed on page | not observed | yes (PADapult RDS/metadata) | public pages, APIs, web hooks | website integration |
| Streaming output | Revma (sibling); ZettaCloud | cloud-hosted | yes (OTA + Webstream feeds) | native (Icecast/Shoutcast, relays) | yes (encoder, hosting) |
| Remote operation | yes (Zetta2GO) | yes (web + iOS) | yes (WebDAD, iDAD) | web-native | yes (Remote Studio, Remote VT) |
| Deployment | on-prem + cloud (ZettaCloud) | on-prem / hybrid / cloud-hosted | on-prem workstations | self-hosted Docker | Windows desktop |

Layer B (cross-product commonality, ≥2 products): station as managed unit; audio library with scheduling metadata; the daily log/playlist as the operating artifact; rotation-based music scheduling; automated playout; live-assist mode; voice tracking (4/5); multi-station operation with content sharing/splits (4/5); traffic-log integration (4/5); remote operation (5/5); streaming output (4/5); aired-record/logging/reporting (3/5 explicit).

Layer C (canonical inference): the Type is the radio station's on-air operations system — it holds the station's audio library, plans the broadcast day as a time-ordered log assembled from music schedules, produced elements and commercial events, and executes that day through automated playout with live assist as the human-intervention mode.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **The station's broadcast day as a planned, time-ordered log** — the station's continuous output organized as a daily sequence of events (songs, IDs/jingles/liners, promos, programs/shows, commercial breaks) that will air, built and edited before and during air.
2. **The station's audio library** — the persistent catalog of audio elements (music with scheduling metadata, produced elements, commercials, recordings) from which the log is built and on which playout draws.
3. **Automated execution of the log (playout)** — the system itself plays the day out in real time, event after event, to the station's output (transmitter or stream); live assist is the human-intervention mode over the same log, not a separate model.

Jointly-held load-bearing:

- (1) alone = a schedule document / planning grid with nothing to play.
- (2) alone = an audio library / asset store.
- (3) alone = a media player.
- (1)+(2) without (3) = the companion music-scheduler shape (scheduling + library, no playout) — a real adjacent product family, not the Type's center.
- (2)+(3) without (1) = a playlist player, not a station.
- (1)+(3) without (2) = an automation shell with no content inventory.

Anti-overfit notes: music scheduling is NOT definitional (talk/news stations and automation-only products satisfy the core without it; AzuraCast reduces it to rotation playlists); voice tracking is NOT definitional (absent at AzuraCast, which uses live DJs instead); streaming output is NOT definitional (terrestrial playout satisfies); cloud/web delivery is NOT definitional (on-prem workstation products satisfy); multi-station scale is NOT definitional (single-station products satisfy).

### L1 — Common Mature Structure

- Rotation-based music scheduling: clocks/hour structures, music categories, song coding (artist/genre/tempo/energy-class attributes), separation rules preventing repeats; the music log feeds the station log. Integrated (Ensemble, Creator) or via companion scheduler (GSelector, MusicMaster, PowerGold).
- Voice tracking: pre-recording DJ talk segments into the log so automated hours sound live; remote voice tracking common.
- Live-assist surface: hot keys/cart decks for instant elements; presenter screens optimized for on-air speed.
- Multi-station operation: centralized/shared content stores, localized playlists per market, split/break-away for local spots and liners with rejoin, group-wide voice tracking.
- Traffic-log integration: import/merge the commercial log from the traffic/billing system; live log editing and run-date sync; as-run returned for reconciliation (the BMS seam).
- Newsroom integration: MOS-class rundown sync into the playlist (DAD evidence; RCS News as sibling product).
- Ingest automation: watch folders, FTP/web download, satellite/feed recording for later play.
- Aired record and reporting: logging/recording of what aired; royalty reports (SoundExchange-compatible at the internet pole); listener analytics.
- Now-playing/metadata publishing: RDS/now-playing feeds, public player pages, APIs, web hooks.
- Remote operation: browser/mobile clients for talent and engineering; remote live events.
- Streaming output: internet stream encoders/relays alongside (or instead of) over-air transmission.
- Roles and permissions: talent vs program director vs engineer; per-station permissions in multi-station installs.

### L2 — Variant / Optional Structure

- Output medium: terrestrial OTA, internet-only stream, satellite-fed, hybrid (OTA + webstream with different ad inserts).
- Scale: single station → station group → multi-station network (dozens of stations from few workstations).
- Format: music-heavy (scheduling central) vs talk/news (scheduling minimal, newsroom integration central).
- Business/deployment model: enterprise licensed suite, budget one-time-purchase desktop, open-source self-hosted, cloud-hosted subscription.
- AI-generated voice tracks (song intros, station IDs, localized news/weather) — emerging.
- Listener-facing extras: requests, public player pages, embeds — prominent at the internet pole.
- Adjacent reuse: clubs, restaurants, stores, party DJs (vendor-documented at StationPlaylist).

### L3 — Vendor-specific (kept out of final doc)

- Product/module names: Zetta, Zetta2GO, ZettaCloud, ZCast, Zetta Splits, GSelector, SelectorCloud, Selector2GO, Aquira, RCS News, RCS2GO, Revma, AudioDisplay (RCS); WO Aurora, Web Studio, Live Mic, Audio Finder, WO AFR Mobile, WO Traffic, WO Digital Hub, WO Data Bridge, WO Payments Suite (WideOrbit); DAD, Presenter, FastTRAK, Ensemble, ListGen, Scheduling Wizard, ENconveyor, Dropbox module, PADapult, SideCAR, WebDAD, iDAD, enDROID, Gateway, MultiTrack, aiTrack (ENCO); Creator, Studio, Streamer, Remote Voice Tracker, Remote Studio (StationPlaylist); Liquidsoap/AutoDJ, Icecast-KH, Shoutcast, AzuraRelay (AzuraCast).
- Marketing claims: "world's largest broadcast software provider" (RCS); "most complete radio station management solution" (WideOrbit); "thousands of broadcasters" (ENCO); "Over 15,000 licences sold" (StationPlaylist); Dash Radio 65 stations / 12 per workstation (ENCO case study).
- Named third-party ecosystem: MusicMaster, PowerGold, Marketron, Wedel, Amily, AP ENPS, AVID iNews, Octopus, Adobe Audition, Hindenburg Broadcaster, Scott Studios, Dalet, RCS NexGen.

## Vendor-specific Findings

- RCS uniquely (in sample) demonstrates the three-product split as corporate strategy (playout / music scheduling / traffic-billing as separately marketed products) and ships cloud variants of both playout and scheduling.
- WideOrbit uniquely (in sample) documents the traffic↔automation integration mechanics in detail ("live log editing, playlist delivery, real-time reconciliation, and auto run-date sync") and markets browser-native remote live broadcasting (Live Mic) with no studio hardware.
- ENCO uniquely (in sample) ships the widest single-product span (internal music scheduler + external scheduler/traffic interfaces + MOS newsroom + RDS publishing + logging extension + AI voice tracks) and documents the satellite-radio scheduling variant (Scheduling Wizard).
- AzuraCast uniquely (in sample) is open-source and self-hosted, exposes listener-facing public pages/APIs as first-class features, and generates a SoundExchange-compatible royalty report.
- StationPlaylist uniquely (in sample) documents the budget tier and the adjacent non-station reuse (clubs/stores/party DJs) in its own positioning.

## Boundary Findings

1. **vs Broadcast Management System** (joint review — DISCHARGES the BMS pass's flag from this side): radio traffic/billing systems are structurally BMS (order → inventory → log → as-run → reconciliation → billing). This side's independent evidence: RCS markets Aquira as "traffic and billing" separate from Zetta/GSelector; WideOrbit sells WO Traffic separately from WO Aurora and describes the integration as "live log editing, playlist delivery, real-time reconciliation, and auto run-date sync" — the traffic system produces the commercial log and delivers it to automation; automation returns the aired record for reconciliation; DAD's ListGen "interface[s] with any music scheduling and traffic software such as MusicMaster, PowerGold, Marketron, Wedel, or Amily"; StationPlaylist ships a "traffic/billing log file importer". **RATIFIED: keep both leaves.** BMS = the commercial management layer of a linear channel (any medium): orders, airtime inventory, spot placement, reconciliation, billing. RSM = the station's on-air operations: library, music/program scheduling, playout automation, voice tracking, live assist. The seam artifact is the commercial log (traffic → automation) and the as-run (automation → traffic). Refinement of the BMS pass's framing: the primary separator is the **layer** (commercial management vs on-air operations), not medium scope — a radio traffic/billing product belongs to BMS regardless of medium; a radio automation/scheduling product belongs to RSM. Medium (radio vs TV vs cross-medium) is secondary. Suites span both layers as separate products, which is itself market evidence that the two are distinct categories.
2. **vs Internet Radio Platform** (§27 sibling): consumer-facing listening (apps, directories, streams for listeners) vs operator-side station management. AzuraCast includes public player pages and TuneIn web hooks — a station-management product can expose listener-facing surfaces — but its center is operating the station (library, playlists, playout, DJ accounts). Remove the station-operations core → an internet radio platform remains; remove listener-facing discovery → RSM remains.
3. **vs Newsroom Management System**: news production (rundowns, scripts, wires) vs station operations. Seam evidenced: DAD's MOS interface "automatically sync your rundowns to a DAD playlist"; RCS News is a separate RCS product. The NRCS output appears in the station log as program events.
4. **vs Media Asset Management**: the station library is a core leg of RSM defined by its role in the broadcast day (scheduling metadata, playout readiness); MAM is the broader enterprise asset repository. DAD's vocabulary ("media asset manager") shows the overlap zone, but the RSM library exists to feed the log and playout.
5. **vs Podcast Platform** (processed sibling): episodic-show venue (shows → episodes → follows) vs continuous station day (log → playout). Some automation products render/publish content after air (Zetta Publish) — distribution of aired content is an extension, not the center.
6. **vs DJ Software** (§04.12): live performance tool (decks, beatmatching, crowd) vs station operations (log, automation, library). StationPlaylist's own "suitable for party DJ's" shows the adjacent reuse; the center differs.
7. **vs Audio Editor / DAW** (§04.09): editing exists inside RSM as a utility (DAD Editor; MultiTrack integration with Adobe Audition/Hindenburg) — the editing Types center on producing audio files, not airing a station's day.
8. **vs Music Streaming Platform**: consumer on-demand catalog vs operator-side station day. Different users, objects, and flows entirely.

**去掉什么就变成另一个 Type:**

- Remove automated execution of the log → a music-scheduling/planning tool (the companion-scheduler family) or a paper log.
- Remove the audio library → a schedule document or a hollow automation shell.
- Remove the broadcast-day log → a media player or an asset library.
- Make commercial orders/inventory/billing the center → Broadcast Management System.
- Flip to the listener side → Internet Radio Platform.

**Historical / market-sample check:** the 1990s-generation automation products (Dalet, Scott Studios, RCS NexGen — named in StationPlaylist's own testimonials) ran the same model: library + log + automation + voice tracking. The pre-automation paper era (record library + program log + board operator executing it) is conceptual lineage — the software Type begins with automation, and the L0 names no specific technology (no OS, no codec, no cloud, no stream format). Regional products fit (DAD documents European traffic/scheduling interfaces Wedel/Amily). Internet-only stations fit (AzuraCast). Talk/news formats fit (scheduling leg shrinks; newsroom integration grows). The L0 holds across eras, media, and scales.

## Uncertainties

- Voice tracking was not observed at AzuraCast (live DJ accounts instead) — held as common mature structure (4/5 products), not definitional.
- Compliance/regulatory logging (e.g., EAS, official station logs): SideCAR is described as "Radio Logging & Recording" (monitoring); no direct evidence on regulatory specifics — kept qualitative in the final doc.
- Music-scheduling depth varies widely: full rotation engines (GSelector, Ensemble, Creator) vs simple rotation playlists (AzuraCast). The discipline is common; its depth is a variant axis.
- Whether the directory's "Radio Station Management" should also cover station business administration (sales CRM, HR, payments): WideOrbit markets its whole stack (automation + traffic + digital + payments + data) as a "radio station management solution", but the operational evidence shows the automation core as the station-operations center, with business layers covered by BMS and CRM/sales leaves. Held: RSM = on-air operations; the marketing-broader usage noted as vocabulary overlap.
- RCS product documentation sits behind a login (rcssupport.com); all RCS observations are from public product pages — no operational parameters asserted beyond those pages.
- MusicMaster and PowerGold (companion music schedulers) were not fetched directly; they are evidenced through DAD's and WideOrbit's integration pages. Their classification as the companion-scheduler family (adjacent to this Type) rests on those integration descriptions plus GSelector's positioning.

## Taxonomy Flags (for STATUS.md Boundary Issues)

- Joint review with broadcast-management-system DISCHARGED from this side: keep-both ratified; seam = commercial management layer (BMS) vs on-air operations layer (RSM); the commercial log and as-run are the seam artifacts; radio traffic/billing products → BMS regardless of medium.
- Vocabulary note: "radio station management" is used by at least one vendor (WideOrbit) for the whole business stack; the directory leaf is held to the on-air operations core.

## Final Synthesis

A Radio Station Management application is the radio station's on-air operations system: it holds the station's audio library, plans the broadcast day as a time-ordered log assembled from music schedules, produced elements, and commercial events, and executes that day through automated playout — with live assist for DJs on air, voice tracking for pre-recorded hours, multi-station content sharing and splits for groups, traffic-log integration at the commercial seam, and logging/reporting after air. Music scheduling, voice tracking, streaming, remote operation, and analytics are the standard capabilities that make the system practical; the defining core is the station day: library → log → automated execution.
