# Research Notes — Clinical Documentation Platform

## Research Goal

Understand what a **Clinical Documentation Platform** actually is as an Application Type, from real products' official documentation — in particular:

- What is the managed object? (the clinical note / documentation record?)
- How is documentation produced, refined, finalized, and stored?
- How does the "capture/generation" pole (dictation, ambient AI) relate to the "documentation integrity/review" pole (CDI)? Are they one Type or two?
- Where are the boundaries vs EHR, Medical Coding Platform, Clinical Communication Platform, Clinical Decision Support System, and general dictation/meeting-transcription tools?
- Would older documentation products (dictation → transcription → sign workflows) still fit the definition?

## Initial Boundary

Leaf: `Clinical Documentation Platform` (§22 Healthcare & Life Sciences).

Hypothesis at start: the Type centers on the **clinical note** — the authored, clinician-attributed documentation of patient care — as the managed object. The EHR (processed sibling) holds documentation as one L1 capability among orders/results/meds/scheduling; this leaf should be the Type where documentation itself is the product's center of gravity. Adjacent markets that must be reconciled: Clinical Documentation Integrity (CDI) software (documentation review/query for completeness and revenue), front-end speech recognition / dictation, and ambient AI scribes. Risk: the Type could fragment into two unrelated poles — capture vs integrity. If they share the L0 (note as managed record + lifecycle to signed/final state), keep one Type with two poles; if not, flag.

Directory neighbors: Electronic Health Record / EHR, Practice Management System, Clinical Communication Platform (processed), Clinical Decision Support System (processed), CPOE, Nursing Information System, Care Plan Management, Medical Coding Platform, Healthcare Revenue Cycle Management, Patient Registration & Intake, Meeting Recording & Transcription Application (§03.10, structurally analogous capture→summary loop).

## Research Questions

1. What is the core object the software manages — a note, a document, a draft, a query, a chart?
2. What binds documentation to a patient and a care event (encounter/visit)?
3. What authoring/capture styles exist (typing, dictation, ambient conversation capture, template composition)?
4. What is the note's lifecycle (draft → review/edit → sign/attest → amend) and who owns each step?
5. Where does the finalized documentation live — native storage or the EHR's chart? What does integration look like?
6. What does the CDI (integrity) pole do mechanically — gap detection, prioritization, physician queries, amend loop?
7. What downstream outputs come from documentation (coding suggestions, charge capture, quality measures)?
8. What rules matter: attribution, attestation, AI-draft review, amendment/audit, privacy?
9. Who are the users (physicians, nurses, radiologists, CDI specialists, coders, HIM)?
10. Where is the boundary vs EHR (which documents as L1) and vs generic dictation/meeting transcription?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers, covering both market poles:

| Product | Pole | Posture | Customer tier |
|---|---|---|---|
| **Waystar Clinical Documentation Integrity** (ex-Iodine Software) | integrity/review (CDI) | AI-prioritized documentation gap/coding-opportunity review + physician query workflow, inside a revenue-cycle platform | enterprise health systems |
| **Abridge** | capture/generation (ambient AI) | ambient conversation capture → draft notes, pre-visit prep, post-visit outputs; clinician + revenue cycle + nursing experiences | enterprise health systems (300+ claimed) |
| **Microsoft Dragon Copilot** (ex-Nuance DAX Copilot) | capture/generation (dictation + ambient) | role-based AI clinical assistant: ambient capture → specialty notes, Q&A, task automation; browser/mobile/desktop/EHR-embedded | enterprise + EHR-partner installed base |
| **Microsoft Dragon Medical One** | capture (dictation heritage, still current) | speech-driven documentation: select-and-say, AutoText, voice skills, EHR embedding (Epic, Oracle Cerner, MEDITECH) | broad clinical installed base |
| **Suki** | capture/generation (AI assistant) | ambient documentation + dictation + coding/reasoning; clinician app + developer/partner toolkit | clinicians, groups, 400+ systems/partners claimed |
| **Ambience Healthcare** | capture/generation + point-of-care integrity | ambient notes/orders/instructions + record reconciliation + CDI-gap closure + coding with clinician attestation; outcome-priced | large, complex health systems |

Solventum 360 Encompass (CDI/HIM incumbent) was attempted twice (404 ×2) and abandoned per the network-failure rule; the CDI pole is covered by Waystar's CDI product page. All evidence below is from official vendor product/solution pages (Tier 2). No vendor help centers or product operational documentation were reached in this pass (see Sources & Limitations).

## Sources

Research date: **2026-09-07**. All official vendor pages.

- Waystar (Iodine Software acquired by Waystar; iodinesoftware.com redirects to waystar.com) — Clinical Documentation Integrity product page: https://www.waystar.com/our-platform/clinical-integrity-revenue-capture/clinical-documentation-integrity/ ; platform nav (Clinical Integrity + Revenue Capture: Utilization Management, Prebill Anomaly Detection, Charge Integrity, DRG Anomaly Detection) — https://www.waystar.com/our-platform/
- Abridge — home + platform nav (Clinicians / Revenue Cycle / Nursing; CDS; Care Signals): https://www.abridge.com/ (plus linked /platform/* pages reachable from nav)
- Microsoft Dragon Copilot: https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot
- Microsoft Dragon Medical One: https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-medical-one
- Suki: https://www.suki.ai/ (+ nav: /clinicians/, /partners/, /ehr-integrations/, help.suki.ai)
- Ambience Healthcare: https://www.ambiencehealthcare.com/ (+ /products, /ambulatory, /inpatient, /ed, /clinicians, /business, /informatics)

Unreachable: solventum.com (360 Encompass) — 404 ×2, abandoned. No regulator pages attempted (documentation requirements were not the research focus; if needed they would be cited from vendor pages only).

**Sourcing limitation (applies to all products):** evidence is Tier-2 official product/solution pages. No help-center / user-guide article was fetched. Assertions are therefore kept at the structure/workflow level; precise operational facts (numeric limits, timing windows, default settings, per-plan capabilities) are NOT asserted in the final document, and vendor performance metrics are treated as claims recorded here only.

## Product Observations

### Waystar Clinical Documentation Integrity (ex-Iodine) — Evidence layer: A

Positioning: "AI-powered CDI software… helps capture the complete patient story — resulting in stronger and more accurate revenue capture, better quality metric tracking, and enhanced team productivity." Framed inside "Clinical Integrity + Revenue Capture" alongside Utilization Management, Prebill Anomaly Detection, Charge Integrity, DRG Anomaly Detection.

- **Problem definition**: "Incomplete or inconsistent clinical records can lead to missed diagnoses, compliance risk, and lost revenue." "Every overlooked detail in clinical notes can translate to missed revenue and extra administrative work."
- **Gap detection + prioritization**: "Focus CDI efforts where they matter most, using the power of AltitudeAI to highlight documentation opportunities that should be addressed first." "Spot missing details and coding opportunities early, addressing issues before billing and preventing denials."
- **Physician query loop**: "Make it easy for physicians to respond quickly with Interact — Waystar's mobile query tool — that includes a new generative AI-powered QueryAgent to draft post-discharge queries."
- **Analytics**: "advanced analytics — including DRG and GMLOS predictions — to support smarter decisions and accurate financial forecasting."
- **Integration**: "Seamless integration with your EHR and existing workflows drives stronger compliance, prevents denials, and enhances reimbursement."
- **The loop in summary**: identify documentation gaps in the record → prioritize cases → query the physician → physician responds (amends/clarifies documentation) → record becomes complete/specific → coding/billing proceeds without denial.
- Metrics (vendor claims, recorded not asserted): 98% physician response rate; <$24h provider query response; $2M incremental revenue per 10K admissions; query-rate increase claims tied to named customers.

Observation: this pole does NOT author notes. It reviews existing documentation in the record and drives an amend/clarify loop through queries to the physician. Its managed object is the documentation state of a case (gaps, specificity, coding opportunity), plus the query conversation.

### Abridge — Evidence layer: A

Positioning: "Generative AI for Clinical Conversations… Enterprise-Grade AI… One platform, three tailored experiences": Clinicians ("AI-powered clinical documentation, built for accuracy"), Revenue Cycle ("Billable documentation, automated from the start"), Nursing ("Natural conversations, turned into draft documentation"). Capabilities: Clinical Decision Support (context-aware evidence), Care Signals.

- **Care workflow framing**: pre-visit (pulls together patient history, prior visits, context "so clinicians walk in informed"); encounter ("captures the conversation in real time while surfacing clinical decision support, identifying care gaps, and supporting orders"); post-visit ("Finalized notes, coding specificity, orders, and patient summaries—ready for review, billing, and follow-up").
- **Draft note + review**: notes are generated from the captured conversation and finalized for review — the clinician reviews and finalizes; outputs "ready for review, billing, and follow-up."
- **Revenue-cycle coupling**: "coding specificity" and "billable documentation, automated from the start" — documentation produced with coding-relevant structure; a Riverside Health case claims documentation clarity supported HCC diagnoses documented per encounter.
- **Scale**: 100M+ conversations/year claimed; 300+ health systems; multi-language (AltaMed: 28 languages).
- **AI evaluation machinery**: published whitepapers on confabulation ("hallucination") elimination and clinician-in-the-loop evaluation — accuracy/evaluation as a first-class product surface.
- **Nursing pole**: conversations → draft documentation for nurses (TIME Best Inventions listing "Abridge for Nurses").

Observation: capture pole. The note is produced from the clinical conversation; the clinician remains the reviewer/finalizer; outputs extend beyond the note (patient summaries, orders support, coding specificity).

### Microsoft Dragon Copilot (ex-Nuance DAX Copilot) — Evidence layer: A

Positioning: "Your AI clinical assistant… an extensible AI workspace that scales across specialties, care settings, and devices." Three verbs: streamline documentation, surface information, automate tasks.

- **Ambient capture**: "Ambiently capture multi-party, multilingual conversations and orders at the point of care, or through on-demand recordings any time. Automatically convert them into specialty-specific, customizable notes."
- **Surface information**: Q&A "drawn from transcripts, notes, and trusted third-party medical references with clear citations."
- **Automate tasks**: "accurate coding suggestions, clinical evidence summaries, referral letters, and after-visit summaries."
- **Role-based experiences** (physicians / nurses / radiologists): nurses — "Capture realtime observations ambiently, converting them into structured flowsheet documentation for quick nurse review and approval and seamless EHR transfer"; radiologists — reporting companion to PowerScribe One (report acceleration, impressions drafting, prior synthesis).
- **Access surfaces**: web browser, mobile app, desktop application, "embedded within supported EHRs such as Epic" (physicians); embedded EHR mobile (Epic Rover) + desktop (nurses); desktop companion with PowerScribe One (radiologists). Region availability listed per role.
- **Migration path**: Dragon Medical One → Dragon Copilot ("Take your Dragon Medical One experience to the next level").

Observation: capture pole with dictation heritage. Notes are "specialty-specific, customizable" — template/structure layer is explicit. Review-and-approve is the clinician step (nurses' flowsheet wording makes it explicit).

### Microsoft Dragon Medical One — Evidence layer: A (the historical pattern, still current)

Positioning: "number one clinical documentation companion… speech-driven clinical documentation with secure, comprehensive support from pre-charting to post-encounter."

- **Dictation core**: "Dictate notes immediately with best-in-class speech recognition — no voice profile training required"; accent detection, audio calibration; auto-punctuation.
- **Editing/voice control**: "Select-and-say with built-in voice control — Format, correct, and navigate notes quickly using natural-language commands."
- **Dictation box / anchor dictation**: dictate into any application, transfer text between apps.
- **AutoText**: automated insertion of commonly used content; shortcuts shared across users/departments/organizations (template/boilerplate layer).
- **Voice skills**: automate routines like moving through patient charts, placing orders, signing notes.
- **EHR embedding**: Epic Haiku/Canto, Epic Rover (nurses' voice-enabled flowsheets), Oracle Cerner PowerChart Touch, MEDITECH Expanse/MConnect — speech-to-text into the EHR's documentation fields; PowerMic Mobile smartphone microphone.
- Best in KLAS 2021–2026 claim (6 consecutive years).

Observation: this is the pre-ambient (and still sold) pattern: the clinician authors the note by dictation into the EHR's note fields; the product accelerates authoring but the note structure, storage, and lifecycle live in the EHR. It defines the lower bound of the Type: capture + clinician authorship + record, no AI drafting, no ambient.

### Suki — Evidence layer: A

Positioning: "Ambient Clinical Intelligence engineered to transform your workflow… AI infrastructure that gets documentation, coding, and revenue right. Manage charting, dictation, patient instructions, orders, and more with a platform that integrates with the top EHRs."

- **Ambient Documentation**: "capturing the entire patient conversation to generate complete, high-quality notes, patient instructions, and orders"; "voice-enabled editing and problem-based charting"; notes "sync directly into the EHR."
- **Dictation product line**: "Dictation enters a new era… industry-first flexible solution" — dictation as a separate mode alongside ambient.
- **Assisted Revenue Cycle** + **Clinical Reasoning** as sibling capability blocks.
- **EHR integration**: "deep, real-time integrations with the four leading EHRs — Epic, Oracle Health, athenahealth, and MEDITECH."
- **Surfaces**: iOS/Android + desktop; 100+ specialties claim; care-setting adaptability.
- **Two delivery poles**: Suki for Clinicians (first-party assistant spanning pre-charting → documentation → reasoning) and Suki for Partners (developer toolkit embedding AI capabilities into other healthtech applications).
- Governance posture: SOC 2 Type 2, HIPAA compliance (trust portal).

Observation: capture pole, clinician-tier + partner-embed pole. Explicitly spans multiple documentation outputs (notes, patient instructions, orders) and multiple authoring modes (ambient, dictation, voice-edited).

### Ambience Healthcare — Evidence layer: A

Positioning: "The AI partner built for clinicians… Turn frontier intelligence into measurable clinical, quality, and financial outcomes… trusted enterprise-wide at the most complex health systems."

- **Documentation**: "Write the documentation — Specialty-accurate notes, orders, and instructions written as care happens, from prep through discharge." Settings: Ambulatory, Inpatient, Emergency Department; 200+ specialties claimed.
- **Point-of-care integrity (CDI hybrid)**: "Closes documentation gaps — Surfaces patient complexity and resolves CDI gaps at the point of care."
- **Coding with attestation**: "Codes the care — ICD-10, HCC/MCC/CC classifications, and E&M levels as care is delivered, with the clinician there to attest."
- **Record reconciliation**: "Conflicting med lists, stale problem lists, and scanned faxes resolved into one trusted picture of the patient."
- **Chart Q&A and task follow-through**: "Answers the chart… with sources cited"; "Tracks and completes to-dos."
- **Platform**: "system of context" (Chorus: extracted, reconciled chart data feeding every AI use case) + "system of action" (writes decisions back into systems of record; "Every action clinician-reviewed, every action audited") + governance/telemetry layer.
- **Commercials**: fees tied to outcomes; ROI claims (3x, AAPC-verified 95% coding compliance — vendor claims).

Observation: capture pole that internally merges the integrity loop ("resolves CDI gaps at the point of care") and coding output "with the clinician there to attest" — attestation again the clinician-owned finalization step. Also notable: the platform reconciles the record (context layer) before documentation.

## Cross-product Comparison

| Dimension | Waystar CDI (Iodine) | Abridge | Dragon Copilot | Dragon Medical One | Suki | Ambience |
|---|---|---|---|---|---|---|
| Note as managed object | yes — documentation state of the case (gaps/specificity) | yes — generated draft note | yes — generated/customizable note | yes — dictated note into EHR fields | yes — notes/instructions/orders | yes — notes/orders/instructions |
| Patient + encounter binding | yes (cases, admissions; post-discharge queries) | yes (pre-visit/encounter/post-visit) | yes (point of care, encounter capture) | yes (in-EHR documentation, patient context) | yes (encounter capture, problem-based charting) | yes (prep→discharge, per setting) |
| Authoring machinery | no authoring — review/query/amend | ambient conversation → draft | ambient + on-demand recording → draft | dictation + voice editing | ambient + dictation + voice edit | ambient + reconciliation + Q&A |
| Clinician attribution/finalization | physician query response amends the record | clinician review/finalize | clinician review; nurse "review and approval" | clinician authors & signs in EHR | clinician edits/syncs | "clinician there to attest"; every action clinician-reviewed |
| Finalization machinery | query → response loop | draft → review → finalized note | draft → customize → finalize | author → sign (in EHR) | draft → edit → sync | draft → attest → write-back |
| EHR relationship | integrates with EHR; works on EHR-resident documentation | syncs into EHR; embedded | browser/mobile/desktop/EHR-embedded (Epic) | speech-to-text inside EHR (Epic/Oracle Cerner/MEDITECH) | deep sync with Epic/Oracle Health/athenahealth/MEDITECH | writes back into systems of record; reduces EHR transaction load (claim) |
| Downstream coding/revenue outputs | core purpose (coding opportunities, DRG/GMLOS analytics, denial prevention) | coding specificity, billable documentation | coding suggestions, referral letters, after-visit summaries | none observed (documentation only) | assisted revenue cycle module | ICD-10/HCC/E&M with attestation |
| AI drafting | AI prioritization + AI-drafted queries (not note drafting) | core | core | none (speech recognition only) | core | core |
| Roles | CDI specialists, physicians (responders), coders/HIM context | clinicians, nurses, revenue cycle | physicians, nurses, radiologists | any clinician (dictation) | clinicians + partner developers | clinicians (ambulatory/inpatient/ED), business, informatics |
| Multi-language/multi-party capture | — | yes (28-language claim) | yes (multi-party, multilingual) | accent detection | yes (implied) | — |

Reading of the comparison:

- All six products manage **clinical documentation bound to an identified patient and care event** and end their loop at **documentation finalized under clinician responsibility and living in the patient's record**.
- The sample splits into three postures rather than two: **review-and-query** (Waystar), **generate-then-review** (Abridge, Dragon Copilot, Suki, Ambience), and **author-in-place** (Dragon Medical One). The three postures are points on one lifecycle: produce → refine → finalize → record.
- Coding/revenue coupling is nearly universal in the current market (5 of 6) but structurally absent in Dragon Medical One — it is Common Mature Structure, not defining.
- AI drafting is era-common, not defining (Dragon Medical One proves the Type stands without it; Waystar proves the Type stands with review-only machinery).
- Nurse and radiologist documentation (flowsheets, reports) is a role-axis variant, not a separate Type.

## L0 / L1 / L2 / L3

### L0 — Defining Invariant (minimal)

```text
Clinical Documentation Record (the note)
  bound to an identified patient + a care event (encounter/visit)
    └── attributed authorship (a responsible clinician)
        └── documentation lifecycle machinery
            (produce and/or refine → draft → clinician finalize/attest)
            └── finalized documentation persists in the patient's longitudinal record
                (native or via integration with the EHR)
```

Four properties; remove any one and the product stops being this Type:

1. **The clinical note as managed object** — authored documentation of patient care (progress note, procedure note, discharge summary, report, flowsheet entry), not messages, orders, or claims. Without it: communication, coding, or billing software.
2. **Patient + encounter binding** — every document is about an identified person and, in the dominant pattern, a specific care event. Without it: generic dictation or meeting transcription.
3. **Attributed clinician finalization** — documentation reaches its record-ready state through a named clinician's review/attestation/signature; the medico-legal record requires a responsible human author. Without it: unattributed transcription or meeting notes.
4. **Lifecycle to a persistent record** — machinery that moves documentation from produced/unrefined to finalized, and the finalized result joins the patient's longitudinal record. Without persistence: an ephemeral text tool, not documentation.

### L1 — Common Mature Structure

- Authoring/capture styles: typing/keyboard, direct dictation with speech recognition, ambient conversation capture, template/boilerplate composition (AutoText-style shortcuts)
- Draft → review/edit → sign/attest → amend (addendum/correction) lifecycle surfaces
- Specialty-specific note structures and customizable note styles/templates
- Patient-context insertion (demographics, problems, meds, results pulled into the note or the AI's context)
- EHR integration — push the finalized note into the chart; increasingly bidirectional context
- AI-generated draft notes with mandatory clinician review (dominant modern capture pattern)
- Coding/revenue coupling: coding suggestions, documentation specificity for billing, denial prevention
- Structured outputs beyond prose: orders/instruction drafts, patient summaries, referral letters
- Multi-role coverage (physicians, nurses, radiologists/other specialists) in enterprise products
- Analytics on documentation work (query response, note completion, adoption)
- Security/compliance posture (HIPAA-class; audit trails; in one product a governance/telemetry layer)

### L2 — Variant / Optional

- Posture: standalone capture app vs EHR-embedded module vs CDI/review suite vs point-of-care hybrid (capture + integrity)
- Documentation scope: office/ambulatory visits, inpatient progress & discharge, emergency notes, procedure notes, radiology reports, nursing flowsheets/notes
- Revenue-cycle coupling depth: none → coding suggestions → full CDI query workflow → coding with attestation
- Authoring-mode mix (ambient / dictation / typing / template-only), multi-party and multilingual capture
- CDI analytics depth (case prioritization, predicted severity/class metrics — names and metrics vary by product)
- Regional availability and language coverage
- Commercial shape: clinician subscriptions, enterprise contracts, outcome-tied fees, developer/partner toolkits
- Quality machinery for AI drafts: evaluation programs, confabulation controls, cited answers

### L3 — Vendor-specific (research notes only)

- Waystar: Interact (mobile query tool), QueryAgent (AI-drafted post-discharge queries), DRG/GMLOS predictions, AltitudeAI branding; ex-Iodine lineage; metric claims (98% response rate, <$24h response, $2M/10K admissions).
- Abridge: three tailored experiences (Clinicians/Revenue Cycle/Nursing), Care Signals, confabulation-elimination whitepaper program, 100M+ conversations and 300+ systems claims, Best in KLAS 2025/2026 claims.
- Microsoft: Dragon Copilot role-based experiences (incl. radiologist companion to PowerScribe One), Epic Haiku/Canto/Rover/Oracle Cerner PowerChart Touch/MEDITECH Expanse integrations, PowerMic Mobile, AutoText, anchor dictation, dictation box, region-by-role availability tables, Best in KLAS 2021–2026 claim, DMO→Copilot migration path.
- Suki: Partner/developer toolkit, four-EHR deep-integration claim, 100+ specialties claim, dictation-as-flexible-solution positioning, trust portal.
- Ambience: Chorus "system of context," governance/telemetry layer, outcome-tied fees, AAPC-verified coding compliance claim, 3x ROI claim, 200+ specialties claim.
- Iodine Software brand absorbed into Waystar (iodinesoftware.com redirect) — market-consolidation evidence only.

## Vendor-specific Findings

- The physician **query** machinery with mobile query delivery and AI-drafted queries is documented only at Waystar in this sample (structurally implied at Ambience as "resolves CDI gaps at the point of care"). Treat detailed query mechanics as CDI-pole/product-specific, not canonical.
- **Record reconciliation** (conflicting med lists, stale problem lists, faxes) as a documentation-adjacent capability is documented at Ambience only → product-specific.
- **Developer/partner toolkit** for embedding documentation AI into other applications: Suki only → product-specific.
- **Radiology reporting companion** (drafting impressions, prior synthesis, PowerScribe One pairing): Microsoft only → product-specific (radiology reporting arguably borders a separate documentation niche).
- Numeric performance/compliance claims (98% query response, 95% AAPC-verified coding, 3x ROI, 100M+ conversations, 300+/400+ systems, Best in KLAS years) — vendor marketing claims, recorded here, never asserted in the final document.

## Rejected Findings

- "Clinical Documentation Platform = ambient AI scribe" — rejected: Dragon Medical One (no ambient) and Waystar CDI (no capture) both satisfy the minimal core; ambient is an era-common authoring implementation.
- "CDI is a separate Application Type from documentation capture" — rejected at L0: both poles manage the same object (patient-bound, attributed clinical documentation) and both end at finalized documentation in the record. They are lifecycle postures (refine-existing vs produce-new) over one Type. Recorded as a boundary consideration, not merged into another leaf.
- "Coding outputs are definitional" — rejected: Dragon Medical One documents without coding coupling; the revenue coupling is market-common, not defining.
- "Multi-role (nurse/radiologist) documentation is a different Type" — rejected: same core model with role-scoped note types (flowsheets, reports).
- "The platform owns the longitudinal chart" — rejected: the EHR sibling owns the chart; this Type's finalized output joins the chart natively or via integration. Ownership of the whole chart would make it an EHR.
- Precise operational facts (query response windows, note turnaround times, draft-retention durations, language counts as requirements) — rejected for lack of Tier-1 operational documentation; no numeric limits asserted in the final document.

## Boundary Findings

**vs Electronic Health Record / EHR (processed sibling)** — the sharpest seam. The EHR's documentation capability is L1 inside the EHR's patient/encounter system of record; here documentation IS the system's center of gravity. Tests: remove the note and only orders/results/meds/scheduling remain → EHR; keep only the note machinery (capture, refine, finalize, hand to the record) → this Type. The historical Dragon Medical One pattern (dictate into the EHR's note fields) shows the two can interlock without the platform owning the chart.

**vs Medical Coding Platform** — coding consumes the finalized record and assigns codes; this Type produces/refines/finalizes the record. Overlap zone: documentation specificity for coding (CDI) and coding suggestions at documentation time (Ambience, Dragon Copilot). Test: remove code assignment and the product can still exist (documentation); remove documentation production/refinement and only code assignment remains (coding). Products pair rather than collapse.

**vs Clinical Communication Platform (processed sibling)** — communication is messaging between care team members (secure chat, alerts, calls); documentation is the attributed record of care. No note lifecycle in communication; no conversation thread in documentation.

**vs Clinical Decision Support System (processed sibling)** — CDS is advice at decision points; documentation platforms may surface context-aware evidence (Abridge CDS, Dragon "surface information") as an adjacent capability. Test: remove advice and the documentation Type stands; remove documentation machinery and only advice remains (CDS).

**vs Meeting Recording & Transcription Application (§03.10)** — structurally nearest non-medical Type (capture conversation → structured summary → review). Distinctions: patient/encounter binding, clinical note conventions, clinician attestation, EHR record persistence, regulated privacy posture. Remove the patient/record frame and a clinical scribe degrades toward a meeting assistant.

**vs Practice Management System / specialty EMR** — those are business-operated systems (scheduling, billing, front office) that contain documentation as a module; this Type is the documentation machinery itself, usually alongside an EHR.

**vs Speech Recognition / general dictation (non-clinical)** — no patient binding, no note structure, no attestation, no record. Dragon Medical One sits inside this Type precisely because it is clinical-documentation-shaped (dictate into clinical note fields within the record context).

**"Remove what, and it becomes another Type" summary**: remove the note as managed object → coding/billing/communication; remove patient+encounter binding → generic dictation/meeting transcription; remove clinician attribution/finalization → unattributed transcription service; remove persistence into the record → an editor, not documentation; add the whole chart (orders, results, meds, scheduling) → EHR.

## Historical / Market-Sample Check

- **Dictation → transcription → review → sign** workflow systems (tape/digital dictation routed to transcriptionists, returning a draft for clinician signature): satisfies L0 exactly — note as managed object, patient/encounter binding, attributed finalization, persistence in the record. Authoring machinery = human transcription instead of AI.
- **Dragon Medical One (current, pre-ambient)**: satisfies L0 with the EHR owning storage — proves the Type does not require native storage.
- **Paper-era / early EHR-era CDI programs** (chart review for completeness before coding): the review posture's ancestor; the software implementations digitize the same query/amend loop.
- **Non-US / regional markets**: the sampled products are US-centric (coding references ICD-10/HCC/E&M; regional availability lists). The L0 does not depend on the US coding regime — documentation machinery (produce/refine/finalize/record) is regime-neutral; coding coupling is L2. Regional products (e.g., documentation inside non-US hospital systems) fit the minimal core.
- The ambient AI wave is an implementation era, not the definition: the definition must keep standing when (and before) ambient drafting exists — it does.

## Uncertainties

- **Tier-1 operational documentation was not reached for any sampled product** (help centers / user guides). Lifecycle details (exact draft states, edit windows, retention rules, signature mechanics) are inferred at structure level from product pages. If Tier-1 docs were reachable, some L1 details might sharpen.
- **Waystar/Iodine CDI internal mechanics** (worklists, case states, query statuses) come from one marketing-grade product page; the CDI pole's workflow detail is thinner than the capture pole's.
- **Where the boundary with Medical Coding Platform blurs commercially**: products like Ambience advertise coding output "with clinician attestation" inside the documentation product. Whether the market eventually collapses CDI/coding/documentation into one suite-leaf is a joint-review question for the coding leaf.
- **Solventum 360 Encompass** (the classic CDI+HIM incumbent) unreachable — the CDI pole rests on Waystar's page plus the capture pole's "CDI gap" language (Ambience). No structural claims about 360 Encompass are made anywhere.
- **Non-US documentation products** were not sampled; the historical check covers them by inference, not observation.
- The directory has no separate leaf for ambient scribes or CDI; this leaf absorbs both. If a future pass splits them, the L0 here is written so both would inherit it.

## Final Synthesis

A Clinical Documentation Platform is the software whose managed object is **clinical documentation itself**: the authored, clinician-attributed record of patient care, bound to an identified patient and a care event. The market realizes the Type through three postures over one lifecycle — **produce** the documentation from the care conversation or dictation (ambient AI assistants, speech-driven dictation), **refine** it for completeness and specificity (CDI review, gap detection, physician queries), and **finalize** it under clinician review/attestation so it joins the patient's longitudinal record (natively or inside the EHR). Coding and revenue coupling, multi-role coverage, specialty note structures, patient-context integration, and AI drafting are standard mature capabilities; ambient capture is era-common, not defining; the EHR remains the owner of the wider chart. Older dictation/transcription products and CDI review programs satisfy the same minimal core, which keeps the definition from over-fitting to the current AI implementation.
