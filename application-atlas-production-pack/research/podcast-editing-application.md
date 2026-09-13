# Research Notes — Podcast Editing Application

Research date: 2026-09-08
Leaf: Podcast Editing Application (DIRECTORY 04.09 Audio)
Slug: podcast-editing-application
Evidence layers used below: A = directly observed on an official source for a named product; B = cross-product commonality across the sample; C = canonical inference from comparison + Type-boundary reasoning.

---

## Research Goal

Understand the Application Type **Podcast Editing Application** (04.09 Audio) from real products: what its world consists of, what users do, how production work flows, which rules constrain it, and where its boundaries sit against the three sibling leaves of 04.09 (Audio Editor, DAW, Audio Restoration Application) and adjacent Types (Podcast Platform §27, Meeting Recording & Transcription §03.10, AI Video Editing §04.21, AI Voice Generator §04.22).

This pass must discharge three joint-review flags held by sibling passes:

- audio-editor pass (research/audio-editor.md Boundary Findings): "A podcast-first product restructures around the podcast pipeline (episodes as units, text/transcript surfaces, music beds, chapters, publication) — that is a domain variant built on this Type's core. Whether it deserves independent-Type status is a taxonomy question."
- DAW pass (research/digital-audio-workstation-daw.md Boundary Finding 6): "DAWs are widely used for podcast production, but the podcast Type reorganizes around the domain pipeline (episodes, transcripts, publication). Same editing substrate, different center. Flagged for the sibling pass."
- audio-restoration pass (research/audio-restoration-application.md Boundary Findings): "Podcast-first products restructure around episodes/transcripts/publication. Restoration products have no pipeline objects; podcast cleanup is a use case performed inside this Type."
- Secondary: ai-video-editing pass (research/ai-video-editing-application.md Boundary Finding 5): "Descript serves both; boundary is the primary medium (audio program vs video)."

## Initial Boundary

Initial hypothesis: the Type is the audio-editing substrate reorganized around the **podcast production pipeline** — the episode as the unit of work, spoken-word capture and editing, and a publication-facing finish. Nearest neighbors: Audio Editor (same substrate, file-shaped work), DAW (composition), Audio Restoration (repair loop), Podcast Platform (distribution/listening side), Meeting Recording & Transcription (record-of-record).

## Research Questions

1. What is the unit of work — file, project, session, or episode? Is there a show/series container?
2. What does the recording step look like (local mic, remote guests, call capture, imports)?
3. What are the editing surfaces (waveform, multitrack, transcript/text)? Is transcript-based editing definitional or generational?
4. Where does cleanup/processing sit (manual tools vs one-click AI voice enhancement)?
5. What exactly is the end of the workflow — export, or publication? Does publication imply in-product hosting?
6. What episode-level artifacts does the pipeline produce (show notes, chapters, transcripts, music reports)?
7. Who uses it (solo creators, journalists, producers, teams) and what roles exist?
8. Where are the boundaries vs Audio Editor / DAW / Audio Restoration / Podcast Platform / Meeting tools?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers.

1. **Hindenburg PRO (Hindenburg Systems)** — dedicated spoken-word editor for radio journalists and podcasters; professional/broadcaster pole; desktop-native; publication as export with loudness/format targets, no hosting. Danish company, product line born 2008 for radio journalists.
2. **Descript** — transcript-first editing philosophy ("edit by text"); prosumer/creator pole with enterprise tier; cloud; recording (Rooms), editing, AI cleanup, publishing to hosting services; also does video.
3. **Riverside** — remote-recording-studio-first platform for interview shows; browser-based; local per-speaker recording, text-based editing, hosting and distribution attached; business tier for marketing/production teams.
4. **Alitu** — simplest end-to-end "episode maker" for non-technical indie podcasters; web; automatic cleanup, transcript editing, hosting and distribution attached; consumer pole.

Excluded: Podcastle — the fetch returned an unrelated site (domain redirect in this environment); abandoned after one attempt per the network-restriction rule, not filled from memory.

## Sources

Fetched 2026-09-08 (all official vendor surfaces):

- Hindenburg — product page: https://hindenburg.com/products/hindenburg-pro ; Radio & Podcast (PRO 2) page: https://hindenburg.com/products/radio-podcast/ (Tier 2: positioning, workflow verb chain, capture/transcription/clipboard/editing/publishing sections, feature matrix)
- Descript — homepage: https://www.descript.com/ ; Podcasting page: https://www.descript.com/podcasting (Tier 2: product workflow, Rooms, text-based editing, AI features, FAQ incl. formats and publish-to-hosting, pricing tiers)
- Riverside — homepage: https://riverside.fm/ (Tier 2: Record→Edit→Repurpose→Stream→Publish flow, local per-speaker recording, text-based editor, hosting, AI features, business tier)
- Alitu — homepage: https://www.alitu.com/ (Tier 2: four-step workflow, features, hosting details, FAQ, audience framing)

Not attempted (time budget; product pages already provided rich direct evidence): help.descript.com, support.riverside.com, help.alitu.com, hindenburg.com/academy. Assertion strength is therefore calibrated to official product-page level; no help-center-only operational detail is asserted.

Previous environment failures observed by sibling passes (Adobe helpx, Steinberg) were avoided rather than re-attempted.

---

## Product A — Hindenburg PRO

### Key observations

- Positioning (A): "Hindenburg PRO is spoken-word audio editing software built for journalists and audio storytellers… While most DAWs are designed for engineers and musicians, Hindenburg PRO is purpose-built for professional spoken-word production — for broadcasters, journalists and podcasters." Self-distinguishes from DAW on both material (spoken word vs music) and audience.
- The page header gives the product's own workflow verb chain (A): "record - set broadcast levels - transcribe - organise tape - edit - montage - report - publish". The "publish" verb is at the end of a production chain, not a hosting act (see Publishing below).
- User framing (A): "the professional audio storyteller — You do it all: interview, edit, mix, publish. Hours of: interviews, selects, ambi, music. Endless revisions: 'Can you swap out that bite?' Broadcast-ready deliverables - before deadline." Deliverable is a finished program item; material classes are voice-centered with ambience and music supporting.
- Capture (A): import BWF/WAV/MP3/MP4/PolyWav — "Hindenburg converts everything to high-quality WAV, sets broadcast-ready levels, and keeps full headroom with 64-bit floating point processing"; multitrack recording "for debates and roundtables"; record call recordings "Zoom, Google Meet and more".
- Transcription (A): offline transcription, 99 languages, "Search across hours of material", "Rough-cut in text / audio". PRO 2 adds "editing-by-transcript" (Podnews quote: "the ideal coming-together of the original Hindenburg plus the power of editing-by-transcript") — i.e., the original product generation predates transcript editing. The Manuscript feature: "Edit audio like a Word Processor". Transcription quotas differ by edition (Standard: none shown; Plus: 20 hrs/month; Premium: 50 hrs/month — L3 detail).
- Material organization (A): "Clipboards for interviews, ambience and music. Add Groups & Subgroups. Favorites… When you're working with long-form material, organisation is creative control. With clipboards and favorites, organise even the largest projects, from features to documentaries."
- Editing (A): "Fully non-destructive workflow… Every tool is built for spoken word."
- Publishing (A): "Music Report gives you all the details on your music usage. Broadcast-Ready Loudness Levels. Multiple Publish Targets — Publish to various audio formats and Loudness Levels - when you have multiple targets. Set it once. Deliver everywhere." Publication = export machinery toward multiple delivery targets; no hosting product offered. This is the key evidence that the pipeline terminus does not require in-product hosting.
- Feature matrix (A): story-focused workspace, Clipboard, Video Track ("audio post production sound for your video"), Manuscript, Soundly sound library, Transcription. Editions Standard/Plus/Premium; personal/business/education sectors.
- Heritage (A): "Created for radio journalists by radio journalists. Born in 2008…" — the radio-journalist tape workflow is the digitized ancestor.

## Product B — Descript

### Key observations

- Positioning (A): homepage currently leads with video ("AI Video Editor") but the Podcasting product page is dedicated: "Podcast Editing Software | Record, Edit, Publish" — "Seamlessly record, transcribe, edit, make clips, and publish, all in Descript."
- Text-based editing philosophy (A): "Descript automatically transcribes your files, so you can edit your podcast like a doc. Make cuts with your backspace key. Copy-paste to lock down your narrative; rearrange and revert easily. Words are just so much easier than waveforms." Timeline kept as secondary: "The timeline's there if you need it"; "a complete set of professional editing tools" underneath.
- Recording (A): Descript Rooms — "high-quality audio and 4K video, recorded locally, so internet glitches can't hurt you. Producers can manage sessions from off-screen." FAQ: remote interviews recorded "in crystal-clear audio and video". Customer quote: "What sold me on Descript was the ease of having a recording solution and an editing solution in the same platform."
- AI voice work (A): Studio Sound ("AI-powered background-noise removal and voice enhancement. One click."); Remove Filler Words; Remove Retakes; Regenerate ("Mispronounce a name or say 'gods' when you meant 'horses'? Fix it by typing, with Regenerate." — voice-cloning-based correction of spoken words); AI Speech/voice clones.
- Episode artifacts (A): "Generate episode titles and show notes"; "writes YouTube descriptions and creates chapters as well as will give me the start to a blog post" (user quote); AI Show Notes nav item.
- Repurposing (A): Create Clips ("turn your long-form video or podcast into clips"); translation into 20+ languages.
- Publication (A): FAQ — "You can even publish your podcasts directly to your favorite hosting service. If you've created a video podcast, you can publish it directly to YouTube from Descript." Formats: "WAV, MP3, AAC, AIFF, M4A, and FLAC."
- Collaboration (A): "free collaboration tools allow you to share your content with other editors; they can add comments just like in a Google doc, and even make edits. Because it's all in the cloud, you'll be able to view different versions and restore them."
- Pricing (A, L3 detail): Free (1 media hour/month), Hobbyist ($16–24, 10 media hours), Creator ($24–35, 30 media hours), AI credits per tier. Enterprise tier: SOC 2 Type II, SAML SSO/SCIM, GDPR.

## Product C — Riverside

### Key observations

- Positioning (A): "Riverside is the AI-powered platform that lets you record, edit, repurpose, and distribute studio-quality content as easily as if you had a crew behind you." Products list: Recording, Editing ("AI, text-based video editor"), Live Streaming, Webinars, Hosting ("Podcast publishing and analytics"), Newsletters.
- The product's own flow (A): "Record (Record solo or with guests, in top quality) → Edit (Use the text-based editor, and AI when you want it) → Repurpose (Turn one recording into clips and more with AI) → Stream (Stream in HD to multiple destinations at once) → Publish (Publish straight to Youtube, Spotify and Apple)."
- Recording (A): "Local recording for sharp video & audio — Capture up to 4K video and uncompressed audio in separate tracks, unaffected by internet connection." Per-speaker file cards: each speaker "Ready — 3840 x 2160 — WAV / MP4" plus "All Speakers" mixed download. The double-ender principle: every participant recorded locally, per-track delivery.
- Editing (A): "Edit recordings like a doc — Just search, cut, copy, and paste right in the transcript to edit your videos with our text-based editor." "Multi-track editing — With separate track recording, you can easily remove crosstalk, change layouts, and more." Branding applied once (logo, colors, intro/outro).
- AI (A): "Your episode's ready — Riverside's AI turns your session into a polished cut complete with transcripts, show notes, and more. Edit further if you'd like, or share as is." Magic Audio ("AI polishes your sound, removes noise, and makes any mic sound like it's professional-grade"); Correct speech ("fix the transcript. AI syncs your voice and lips"); Remove filler words; auto-layouts; translation/dubbing 30+ languages; AI Co-Creator (clips, posts, thumbnails, headlines); AI Twin.
- Hosting (A): "Podcast hosting built right in — In just a few clicks you can get listed on Spotify, Apple, Youtube and more… Automatically generate transcriptions, titles, descriptions, chapters, and takeaways."
- Audience (A): use cases — podcasts, interviews, webinars, live streams, social clips; for podcasters/producers/marketers; "Riverside for business — Give your teams the ability to collaborate and produce content at scale."

## Product D — Alitu

### Key observations

- Positioning (A): "Alitu: Edit Your Next Podcast Episode in 20 Minutes" — "Podcasting is hard enough. So Alitu keeps the tech simple, and all in one place." "Zero editing skills required." Audience: "passionate creators who want to focus on their content, not the technical details"; "Made with ❤️ for all indie podcasters."
- The product's own four-step pipeline (A): "1. Record or upload — Record audio and video calls with Alitu, or upload any format. 2. Let Alitu clean up — Straight away Alitu will start removing noise, and polishing your voice. 3. Review and edit — Search and edit your recording like a doc. You already know how! 4. Get it out there! — Get your episode on Apple Podcasts and Spotify with one click."
- Features (A): Recording ("Your own shareable studio"), Audio Editor ("One that's made for podcasting"), Audio Clean-up ("Sound your best, out of the box"), Podcast Music Library, Podcast Hosting, Audio Transcription, Podcast Website.
- Editing surface (A): "Edit using a transcript. You already know how." "Nothing gets lost — Undo edits, even after you publish." "Built for speed — Edit, literally, at 2x speed." (Waveform presence not evidenced on the fetched page; not asserted.)
- Publication (A): "Publish to the world with a click — Apple Podcasts, Spotify, your own Alitu website!" "Connect your favorite host — Link your hosting account and send episodes to your host without waiting for uploads and downloads." "Schedule and forget — Pre-recording your episodes? Smart. Schedule your release date…" Shownotes editor; AI transcription "for your show notes or personal blog".
- Hosting details (A, L3): "completely free up to 1,000 downloads per month… $10 for up to 10,000"; episode scheduling; analytics. Trial: 7 days; pause up to 3 months.

---

## Cross-product Comparison

| Dimension | Hindenburg PRO | Descript | Riverside | Alitu | Pattern |
|---|---|---|---|---|---|
| Unit of work | story/production → program item ("broadcast-ready deliverables"); clipboards organize per-story material | project (recording + transcript + edit) | session → episode | episode (the product's spine) | B: episode-shaped work in all four |
| Capture | mic + call recording (Zoom/Meet) + format import | Rooms (local per-participant) + Zoom import + screen recorder | browser studio, local per-speaker tracks | in-app calls + upload any format | B: local-first multi-participant capture + import path in all four |
| Editing surface | waveform + transcript/Manuscript (PRO 2) | transcript-first, timeline secondary | transcript-first, multitrack underneath | transcript ("edit like a doc") | B: transcript surfaces in 4/4 current-generation; waveform-first in the professional pole |
| Cleanup | auto-levels at import; noise reduction (journalist quote) | Studio Sound one-click | Magic Audio; filler-word removal | automatic cleanup on upload | B: voice-oriented one-click cleanup in 4/4 |
| Material organization | clipboards (interviews/ambi/music), favorites | media library, drive | recordings library | "organise and reuse everything" | B: long-form material organization in 4/4 |
| Episode artifacts | Music Report (licensing), loudness targets | show notes, titles, chapters, transcript (deliverable) | auto titles/descriptions/chapters/takeaways, transcripts | show notes editor, transcripts, scheduling | B: publication-context artifacts in 4/4 |
| Repurposing | — (video track for audio post) | Create Clips, translation | Magic Clips, AI Co-Creator, social scheduling | — | partial (2/4 strong, 1/4 light) |
| Publication terminus | export to multiple formats/loudness targets ("deliver everywhere") | publish to external hosting service / YouTube | in-product hosting → Spotify/Apple/YouTube | in-product hosting + connect external host | B: pipeline terminus in 4/4; hosting in-product 2/4, push-to-host 1/4, export-only 1/4 |
| Video | video track for audio post | video podcasts, 4K | 4K video native | video calls recorded (audio podcast focus) | variant |
| Delivery form | desktop app (Mac/Win), perpetual + subscription editions | desktop + web, subscription | browser (+ Mac/mobile apps), subscription | web, subscription | variant |
| Tier | professional broadcasters/journalists | prosumer creators → enterprise | creators → business teams | non-technical indie beginners | B: full market spread |

### What repeats everywhere (candidate common structure)

1. Episode-shaped work: all four organize the world around producing a finished program item ("episode"), not around editing a loose file.
2. Voice-first material: spoken word is the center; music/ambience support it (Hindenburg: "Every tool is built for spoken word"; Alitu: cleanup/voice polish; Descript/Riverside: speech cleanup and transcript).
3. Capture + editing in one place: every product either records in-product (sessions/rooms/calls) or ingests recordings, then edits — "having a recording solution and an editing solution in the same platform" (Descript customer quote).
4. The pipeline terminus is publication: every product's own verb chain ends in publish/distribute (Hindenburg "publish", Descript "Record, Edit, Publish", Riverside "Publish straight to…", Alitu "Get it out there!").
5. One-click voice cleanup as the default path (4/4).
6. Transcript as a working surface in the current generation (4/4) — see historical check for why this is NOT definitional.
7. Episode publication context (notes/titles/chapters) machinery (4/4, different depth).

---

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

**1. The episode as the unit of work.** The managed object is an episode — a persistent, identified production bound to a show/series (or a standalone project equivalent), accumulating recordings, edits, and publication context. Work is episode-shaped, not file-shaped: the user opens an episode, works on it across sessions, and finishes it toward release. Remove → the product becomes an Audio Editor / DAW (file- or composition-shaped work).

**2. Voice-first capture-and-edit core.** The material is spoken-word audio: captured (local mic, remote multi-participant sessions, call capture) or ingested from recordings, then edited on the shared audio-editing substrate — with the waveform and the transcript as alternative surfaces — using voice-oriented processing and organization (takes/selects/ambience/music as supporting material classes). Remove → the product is not an audio production application at all.

**3. Publication-oriented completion.** The workflow terminates in a **publish-ready episode** for episodic distribution: a deliverable rendered for its delivery target(s) — formats and loudness expectations included — plus episode context (title, description/show notes, commonly chapters/transcript). Publication may be executed in-product (hosting, push to directories), pushed to an external host, or exported as deliverables; the orientation, not the hosting act, is definitional. Remove → the product is an editor with no pipeline, or drifts to the distribution platform.

Jointly-held is load-bearing:
- 1 alone = an episode/show tracker (no production)
- 2 alone = Audio Editor / DAW (the sibling Types)
- 3 alone = a hosting/distribution platform (Podcast Platform territory)
- 1+3 without 2 = planning/publishing workflow tooling
- 2+3 without 1 = a domain-tinted audio editor (file editor with podcast loudness presets) — the audio-editor pass's "domain packs" variant
- 1+2 without 3 = recording+editing with no pipeline endpoint = editor/DAW-shaped work

### L1 — Common Mature Structure

- **Transcript as a working surface** — automatic transcription, search across material, text-based editing ("edit like a doc"), speaker handling. 4/4 current-generation sample. NOT L0 — see historical check.
- **One-click AI voice cleanup** — background-noise removal, voice polish, leveling as an automatic first-class step (4/4).
- **Recording machinery** — in-product capture: local-first per-participant recording insulated from connection quality (Riverside per-speaker WAV/MP4; Descript Rooms "recorded locally, so internet glitches can't hurt you"; Alitu calls; Hindenburg Zoom/Meet capture), plus an import path for externally recorded material (4/4).
- **Long-form material organization** — libraries/clipboards of takes, selects, ambience, music with search (4/4).
- **Speech-convenience editing operations** — filler-word/silence removal, retake removal, speed editing (3–4/4).
- **Multitrack arrangement/mixing** — per-speaker tracks, crosstalk handling, montage/mix depth varying widely (4/4, depth varies).
- **Episode publication context** — titles, descriptions/show notes, chapters, transcripts; often AI-generated (4/4).
- **Repurposing** — social clips and promotional assets derived from the episode (2/4 strong — Descript, Riverside; era-current feature).
- **Distribution connection** — in-product hosting or push-to-host (3/4: Riverside, Alitu, Descript; Hindenburg export-only).
- **Collaboration/review** — comments, versions, producer roles in cloud products (Descript doc-style; Riverside producers off-screen; Descript enterprise).

### L2 — Variant / Optional Structure

- Publication form: export-only (Hindenburg) vs in-product hosting (Riverside, Alitu) vs push-to-external-host (Descript, Alitu "connect your favorite host").
- Video podcasts: native video capture/edit (Descript, Riverside) vs audio-only with a video track for post (Hindenburg) vs audio-focused (Alitu).
- Live streaming/webinars attached (Riverside).
- Desktop native vs browser/cloud vs mobile capture apps.
- Script/teleprompter and manuscript surfaces (Hindenburg Manuscript; Riverside teleprompter).
- Music libraries and licensing artifacts (Alitu library; Hindenburg Soundly + Music Report; Riverside free music).
- Language reach: translation/dubbing (Riverside 30+, Descript 20+).
- AI agents/co-editors (Descript Underlord; Riverside AI Co-Creator); voice cloning for correction (Descript Regenerate).
- Audience/business sectors: personal/business/education licensing (Hindenburg); enterprise controls (Descript SOC2/SSO/SCIM; Riverside business).

### L3 — Vendor-specific (research notes only)

- Hindenburg: clipboard metaphor; "organise tape" vocabulary; Manuscript ("edit audio like a Word Processor"); Music Report; BWF/PolyWav import; 64-bit float processing; broadcast-levels automation; Soundly library; 99-language offline transcription; transcription hour quotas (Plus 20 / Premium 50 per month); Standard/Plus/Premium editions; personal/business/education sector gating; born-2008 radio-journalist heritage narrative; Narrator (audiobooks) and Field Recorder (iPhone) as sibling products.
- Descript: Underlord AI co-editor; Rooms; Studio Sound; Regenerate (fix speech by typing); Remove Retakes; media-hour pricing (1/10/30 per month); AI credits; 720p/1080p/4K export gating; free-plan watermark-free 720p; SOC 2 Type II / SAML SSO / SCIM / GDPR claims; G2 rating claims; "Publish directly to YouTube" for video podcasts.
- Riverside: per-speaker WAV/MP4 download cards; 3840×2160 local capture; Magic Clips/Magic Audio; AI Co-Creator; AI Twin; correct-speech lip sync; auto-layouts; async recording; teleprompter; webinars with HubSpot sync; social content planner; newsletters product; MCP; SOC certification; G2 4.8/1,582 reviews claims.
- Alitu: "20 minutes" edit promise; automatic cleanup on upload; "undo edits even after you publish"; 2x-speed editing; hosting free to 1,000 downloads/month then $10/10,000; 7-day trial; 30-day refund; 3-month pause; podcast website; planner sub-product; WWDC25 feature claim; user testimonials.

## Vendor-specific Findings

- "Publish" means different concrete acts across the sample: export with loudness/format targets (Hindenburg), push to external hosting service (Descript), in-product hosting + directory listing (Riverside, Alitu). The common denominator is the publish-ready episode, not a specific distribution mechanism — this is the load-bearing abstraction for the L0's third leg.
- Transcript-based editing is philosophically central in Descript/Riverside/Alitu ("words are just so much easier than waveforms") but is positioned as an addition in Hindenburg ("the original Hindenburg plus the power of editing-by-transcript") — direct evidence that the transcript surface is generational, not definitional.
- The professional pole (Hindenburg) ships no hosting, no clip generation, no AI-agent layer; the consumer pole (Alitu) ships no deep manual toolset. Both remain the same Type — evidence that hosting/AI/clips are common-or-optional, not core.
- Domain-adjacent products from the same vendor confirm the center: Hindenburg Narrator (audiobooks) is a separate product for a separate spoken-word pipeline; Hindenburg Field Recorder is capture-only.

## Boundary Findings

1. **vs Audio Editor (04.09 sibling — JOINT REVIEW DISCHARGED from this side)**: the audio-editor pass asked whether podcast-first products are an independent Type or a "domain variant built on this Type's core". Resolution from this pass: **keep-both as substrate/center-of-gravity siblings**. All four sampled podcast products are organized around the episode + pipeline (their own verb chains end in publish; episode/show-shaped work objects), while the audio-editor sample (Audacity, ocenaudio, TwistedWave, WavePad — sibling pass evidence) has no episode object, no transcript surface, no publication targets — only "domain packs"/loudness presets as tinting. Directional tests: remove episode + pipeline from a podcast product → a (waveform/transcript) audio editor remains; add episode + pipeline to an editor's file-shaped world → a podcast editing application. This matches the DAW pass's framing ("same editing substrate, different center") and the restoration pass ("podcast cleanup is a use case performed inside this Type [restoration], not a pipeline structure"). The audio-editing substrate remains shared and documented on both sides.
2. **vs Digital Audio Workstation / DAW (04.09 sibling — JOINT REVIEW DISCHARGED from this side)**: the DAW is a general-purpose multitrack production environment (composition: recording + authored notes/patterns, instruments, mixing console); the podcast Type is spoken-word-episode-first with no instruments/MIDI as center. Hindenburg self-distinguishes: "While most DAWs are designed for engineers and musicians, Hindenburg PRO is purpose-built for professional spoken-word production". Convergence surfaces noted by the DAW pass (DAWs used for podcast production) are use-case overlap, not Type identity. Consistent with research/digital-audio-workstation-daw.md Boundary Finding 6.
3. **vs Audio Restoration Application (04.09 sibling — JOINT REVIEW DISCHARGED from this side)**: restoration is impairment-centric (diagnose → treat → verify over named degradation classes); the podcast Type embeds cleanup as an automatic pipeline step (one-click noise/voice polish in 4/4) with no impairment taxonomy and no repair-first discipline. Podcast cleanup is a use case inside both Types; the organizing structures differ. Consistent with research/audio-restoration-application.md.
4. **vs Podcast Platform (§27, unprocessed) — NEW FLAG for that leaf's pass**: this Type's center is production; distribution/listening (hosting, feeds, players, analytics) is the Podcast Platform's center. Three of four sampled products attach hosting/distribution as an extension (Riverside, Alitu in-product; Descript push-to-host), which risks boundary blur on the other leaf. Recommended joint review when Podcast Platform is processed: the seam proposal from this side is "episode production vs episode distribution/listening" — remove production tools → host; remove hosting/distribution → this Type.
5. **vs Meeting Recording & Transcription Application (§03.10, processed)**: consistent with that pass's own note ("Production-oriented vs record-of-record"). Meetings produce an internal record of what happened; podcast episodes are produced publications with a pipeline terminus. Recording machinery and transcripts are shared surfaces.
6. **vs AI Video Editing Application (§04.21 sibling — discharge from this side)**: the ai-video-editing pass flagged Descript as serving both with the boundary "primary medium". Confirmed: Descript's podcasting center is the audio program (multitrack audio editing, publish to podcast hosting); its video podcast support carries the same episode pipeline into video. The medium test holds: audio-program-first → this Type; video-first → AI/normal video editing.
7. **vs AI Voice Generator / AI Speech (§04.22)**: voice cloning appears inside this Type as in-episode repair/correction (Descript Regenerate: fix a spoken word by typing) — repair-side usage of a generative capability, not generation-centered. Consistent with the generative-audio passes' material-source framing.
8. **vs Radio Station Management / Broadcast Management System (§27)**: station-side continuous operations (scheduling, playout, logs) vs per-episode production. Hindenburg's "broadcast-ready" language describes deliverable compliance, not station operations.

## Historical / Market-Sample Check

- **Pre-digital ancestor**: the radio journalist's tape workflow — record the interview, select bites, splice and assemble the program item, deliver at broadcast spec — satisfies all three L0 structures at analog level (the "episode" is the program item; editing is physical; completion is delivery-ready). Hindenburg's own verb chain ("organise tape") names this ancestry explicitly.
- **Early dedicated podcast tools (2008–2010s generation, pre-transcript)**: waveform editing + material clipboards + loudness/format delivery targets (the original Hindenburg generation). Fits L0 without transcripts — confirming transcript editing must NOT be definitional.
- **Podcast production done in general audio editors (Audacity/GarageBand era)**: correctly excluded — that is the use case performed inside the Audio Editor Type, not the Type; the dedicated Type exists where products restructure the workflow around episode + pipeline.
- **Current web all-in-one generation**: fits without core change (hosting, AI, clips are extensions).
- Definition names no era pattern: no transcript requirement, no AI requirement, no hosting requirement, no desktop/browser requirement.

## Uncertainties

- Podcastle could not be sampled (fetch returned an unrelated site in this environment; abandoned after one attempt). The fifth (web all-in-one) pole is covered by Alitu and Riverside instead; no claim depends on Podcastle.
- Help-center depth was not fetched for any sample (assertions rest on official product pages/FAQs). Operational specifics below the product-page level (exact export formats per product beyond what pages state, exact hosting limits, exact transcription quotas semantics) are not asserted in the final document.
- Hindenburg's "publish" concrete act (whether it pushes directly to podcast hosts/directories vs export only) is not fully specified on the fetched page; the final document states only the evidenced part (multiple publish targets as formats/loudness levels, "deliver everywhere").
- Whether Alitu offers a waveform/timeline editing surface beyond the transcript editor is not evidenced; not asserted.
- Episode metadata handling in Hindenburg (artwork, show notes) is not evidenced on the fetched page; the metadata-machinery claim is generalized only from Descript/Riverside/Alitu and kept out of Hindenburg-specific assertions.
- The show/series container is explicit in Alitu (show + episodes) and implicit in Riverside/Descript project structures; its universality could not be tested against a strictly show-less pole, so "show/series (or equivalent project)" phrasing is used.

## Final Synthesis

The Podcast Editing Application is the **episode-pipeline production application for spoken audio**: its world is organized around the episode as the unit of work; its material is voice-first (captured locally, remotely, or ingested) edited on the shared audio-editing substrate — waveform and transcript as alternative surfaces; and its workflow terminates in a publish-ready episode prepared for episodic distribution, whether publication is executed in-product, pushed to a host, or exported as compliant deliverables. Around this core, mature products add the transcript-first editing surface, one-click AI voice cleanup, local-first multi-participant recording machinery, long-form material organization, filler-word/speech-convenience operations, multitrack mixing, AI-generated publication context (notes, titles, chapters), clip repurposing, and hosting/distribution connections. The market realizes one Type across poles: the professional narrative/radio editor (desktop, export-only), the transcript-first creator editor (cloud, text-native, video-capable), the recording-studio-first platform (browser, remote interviews, hosting attached), and the consumer end-to-end episode maker (web, automated cleanup, hosting attached). The Type's edges: against the Audio Editor (same substrate; episode+pipeline vs file-shaped work — jointly reviewed, keep-both), against the DAW (spoken-word episodes vs composition — jointly reviewed), against Audio Restoration (pipeline step vs impairment-centric repair — jointly reviewed), against the Podcast Platform (production vs distribution/listening — flagged for that pass), against meeting tools (publication vs record-of-record), and against video AI editing (medium of the program).
