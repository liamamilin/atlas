# Research Notes — Infection Prevention Platform

## Research Goal

Understand what an Infection Prevention Platform actually is as an Application Type: the system a healthcare facility's infection prevention and control (IPC) program uses day to day — what objects it maintains, what its detection→review→record→report loop looks like, who operates it, and where its boundaries sit against Clinical Decision Support Systems, Healthcare Quality Management, Public Health Surveillance Platforms, LIS, and the EHR.

## Initial Boundary (hypothesis before research)

- Hypothesis: hospital-side surveillance and case-management software for IPC teams; continuously watches patient data (labs, meds, vitals, notes) against surveillance definitions (e.g., HAI definitions), surfaces candidate infection events for infection-preventionist (IP) review, tracks isolation/precautions and outbreaks, and produces regulatory reports (e.g., US NHSN).
- Likely confusions: Clinical Decision Support System (surveillance variant), Healthcare Quality Management, Public Health Surveillance Platform, LIS, EHR-embedded modules, hand-hygiene monitoring products.
- Unknowns: exact module structure; whether antimicrobial stewardship is bundled; whether EHR-embedded modules are the same Type; how far employee-health/exposure tracking extends.

## Research Questions

1. What is the core object of record — alert, case, event, line-list entry?
2. How do surveillance definitions/criteria work as maintained content?
3. What is the detection → review → adjudication → record loop?
4. What data does the platform consume, and from where (EHR/LIS interfaces)?
5. What do infection preventionists actually do in the product day to day?
6. How are isolation/precautions and outbreak/cluster management represented?
7. How does regulatory reporting (NHSN etc.) work?
8. Which adjacent capabilities (stewardship, antibiogram, hand hygiene, ICRA/environmental, employee health) are core vs optional?
9. Is the EHR-embedded module the same Type as the standalone specialist?
10. What roles and multi-facility structures exist?

## Representative Products

| Product | Vendor | Pole | Tier | Evidence access |
|---|---|---|---|---|
| VigiLanz Infection Prevention (a.k.a. "Infection Surveillance Software") | Inovalon (VigiLanz acquired by Inovalon; product line continues) | standalone specialist, acute + post-acute tiers | enterprise health systems, community hospitals, post-acute | product page + official blog fetched (rich) |
| MEDITECH Expanse Surveillance | MEDITECH | EHR-embedded surveillance module | community/regional hospitals, international | Surveillance + CDS solution pages fetched (rich) |
| Vitalacy | Vitalacy Inc | prevention-behavior monitoring (hand hygiene sensors) — variant/adjacent pole | hospitals | site fetched (moderate) |

Context sources: APIC (professional association for infection preventionists) — fetched; CDC NHSN — blocked (see limitations).

Selection rationale: one standalone specialist (the pure Type), one EHR-embedded module (the delivery-posture pole), one sensor-based prevention-behavior product (the adjacent-capability pole that shares the buyer but not the core). Sentri7 and Premier SafetySurveillor — the other two classic standalone specialists in the KLAS "Infection Control and Monitoring" category — were unreachable (see Source-access Limitations).

## Sources

Fetched 2026-09-08:

- Inovalon — "Infection Surveillance Software / VigiLanz Infection Prevention" product page — https://www.inovalon.com/products/provider-cloud/care-quality-management/infection-prevention/ (vigilanz.com redirects here)
- Inovalon — Care Management suite page — https://www.inovalon.com/products/provider-cloud/care-management/ (via vigilanz.com redirect)
- Inovalon — blog "Inovalon and the EHR – A Powerful Synergy for Patient Safety" — https://www.inovalon.com/blog/vigilanz-and-the-ehr-a-powerful-synergy-for-patient-safety/
- MEDITECH — "MEDITECH Surveillance" solution page — https://ehr.meditech.com/ehr-solutions/meditech-surveillance
- MEDITECH — "Expanse Clinical Decision Support" page — https://ehr.meditech.com/ehr-solutions/clinical-decision-support
- Vitalacy — https://vitalacy.ai/
- APIC (Association for Professionals in Infection Control and Epidemiology) — https://apic.org/

Unreachable (1–2 attempts each, then abandoned per network rule):

- Wolters Kluwer Sentri7 — wolterskluwer.com 403; sentri7.com timeout
- Premier SafetySurveillor — premierinc.com 404 on guessed URL; safetysurveillor.com transport error
- CDC NHSN — cdc.gov 403 (both URL forms)
- Epic — epic.com 403
- VigiLanz product-sheet PDFs — fetched as binary, not readable by the tool
- icnet.com — different company (Japanese self-publisher); Baxter/ICNet public product page not located

## Product A — VigiLanz Infection Prevention (Inovalon)

### Key observations (evidence layer A unless noted)

Positioning and naming:

- Page title: "Infection Surveillance Software"; product name "VigiLanz Infection Prevention"; tagline "near real-time infection prevention software"; "Prevent harm, improve safety, and enhance patient care with the help of insights from near real-time infection prevention software."
- Suite context: one of several "Care Management" products (Pharmacy Surveillance, Safety Management, Quality Management, Audit Management, MDS Intelligence, UB Submission, PBJ) — infection prevention is a distinct product with its own page, sold alongside a pharmacy-surveillance sibling.
- Market-category naming: Inovalon news headline cites KLAS ranking "in Pharmacy Surveillance and Infection Control and Monitoring" — the analyst category name is "Infection Control and Monitoring".
- Blog: "Our products have been at the forefront of near real-time clinical surveillance for more than twenty years" — vendor category term "clinical surveillance".

Product tiers (three):

- **Infection Prevention Starter** — "For Post-Acute Facilities": "Simplify compliance and boost visibility into antibiotic use with easy-to-use surveillance designed for CMS readiness and post-acute needs."
- **VigiLanz Infection Prevention** — "For Acute Care Facilities": "Turn up-to-the-minute data into action with adaptive surveillance and rule-based alerts."
- **VigiLanz Infection Prevention Pro** — "For Acute Care Facilities": "advanced tools for high-risk environments and complex infection control needs."

Starter features (post-acute):

- "Smart Outbreak Monitoring: Track alerts, reports, and infection trends in a user-friendly dashboard"
- "Targeted Tracking Tools: Monitor HAIs, CAIs, and 'present on admission' infections"
- "Timely, Configurable Alerts: Receive near real-time notifications when new cases arise, thresholds are met, or risks emerge"
- "Visual Infection Mapping: See when and where infections happen to identify clusters"

Base features (acute):

- "Streamline Daily Workflows: Spot cases sooner, intervene earlier, and prioritize tasks with tools built for fast-paced care environments"
- "Strengthen Prevention Strategies: Uncover performance gaps and opportunities using deep, data-driven insights"
- "Automate NHSN Reporting: Eliminate manual uploads; reports go directly to NHSN with no extra handling required"
- "Access Robust Analytics: Track progress and identify trends with always-current metrics and reports, available on demand"

Pro features (acute, advanced):

- "Cluster Surveillance Tools: Identify and manage emerging outbreaks faster by tracking event clusters in real time"
- "Hand Hygiene Monitoring: Simplify documentation and oversight of hygiene protocols"
- "Construction Risk Tracking: Streamline ICRA management" (Infection Control Risk Assessment during construction)
- "Advanced Antibiograms: on-demand and trending antibiogram data"

"How It Works" (vendor's own description):

- "Our infection surveillance software works behind the scenes 24/7 to monitor clinical data, detect early warning signs, and alert your team the moment action is needed."
- "It pulls from multiple data sources: labs, vitals, medications, notes, and more, and applies intelligent, rule-based logic to surface actionable insights in near real-time."
- "Whether you're tracking HAIs, MDROs, or construction-related risks, your staff gets a clear, prioritized view of what needs attention – no manual data pulling required."
- "With intuitive worklists, automated NHSN reporting, and customizable dashboards, you can reduce documentation burden and stay survey-ready."
- "Quickly detect sentinel events, evaluate when McGeer criteria are met, and identify early signs of potential outbreaks – all while reducing manual tracking." (McGeer criteria = the long-term-care infection surveillance definition set — signals criteria-based evaluation as the review step.)

Customer testimonials (vendor-published; use as workflow signals, not verified outcomes):

- "We're identifying patients who may require isolation sooner, which is enabling us to act sooner. The new processes are also saving time, which enables our infection preventionists to spend more time rounding on units" (Director, System Accreditation) — isolation identification is part of the daily loop; IPs round on units.
- "The rules we created enable us to be proactive rather than reactive" (Infection Preventionist) — locally authored rules.
- "VigiLanz provides a ton of insight and confidence with infection surveillance. With the ability to develop a variety of reports and to share data more quickly, we have developed system-wide awareness that has allowed us to meet organizational infection prevention goals" (Infection Prevention Practitioner).
- "The time saved in tracking, monitoring and reporting infections is now better spent caring for patients. We had an Infection Control Survey in our facilities and were deficiency-free thanks to Infection Prevention" (Senior Clinical Director, post-acute) — survey/regulatory readiness posture.
- "Automated event detection saves us a significant amount of time, and gives us more peace of mind that more events are captured. As a result, we can now spend more time analyzing events and identifying improvement opportunities" (medication-safety director, on the surveillance pattern generally).

EHR integration (official blog):

- "Our clinical surveillance and patient safety solutions all integrate seamlessly with the EHR."
- Autodetection pattern: "using EHR data to automatically identify safety incidents that may otherwise have been missed."
- Cross-module trigger: "when an event is identified in VigiLanz Pharmacy Surveillance, it can trigger the creation of a safety event which is then documented and investigated in VigiLanz Safety Management" — events created by one module become records worked in another; the event-of-record pattern is explicit.

## Product B — MEDITECH Expanse Surveillance

### Key observations (evidence layer A)

Positioning:

- Dedicated EHR solution named "Surveillance" (top-level nav item alongside Pharmacy, Pathology, Population Health).
- "MEDITECH Surveillance analyzes data in real time and identifies patients who need attention, whether they qualify for a potential hospital-acquired condition or a clinical quality measure."
- "Intervene faster with predictive analytics… Catch patients before they fall through the cracks."

Detection mechanics:

- "Evidence-based rules search clinical and demographic data for patients who meet the criteria for CLABSI, CAUTI, and other potential HACs, automatically populating tracking boards."
- "Clinicians can order, document, or message the care team from these boards, right on the spot."
- "Our integrated solution sends notifications to status boards and trackers throughout MEDITECH Expanse, reducing communication delays and expediting interventions."

Communicable-disease tracking structure (named objects):

- **Profiles** "identify patients: who are at risk / with ordered tests / who tested positive."
- **Watchlists** "indicate all patients who are at risk and their status. Can be used by: Infection control staff, Nurse managers."
- **Special indicators**: "Alert clinicians to at-risk patients. Are accessed in clinician's workflows. Guide clinicians to take appropriate precautions."

Content library:

- "Twenty-eight standard surveillance boards and eight evidence-based EHR Excellence Toolkits."
- Board families: Quality Measures (AMI, pneumonia, VTE, newborn, SCIP…), Conditions (CLABSI, pressure ulcers, positive microbiology results…), Consults (respiratory therapy, PT, dietitian…), Preventive measures/other (readmissions, genotype poor metabolizer, unsigned admit orders…).
- Toolkits: Antimicrobial Stewardship, CAUTI Prevention, Depression Screening, Fall Risk, Heart Failure, OB Hemorrhage, Opioid Stewardship, Telemetry Appropriateness.
- CDS page: "Preloaded content includes standard displays, rules, and algorithms to help you monitor and manage common conditions, hospital-acquired infections, and quality measures. Use it as is, tailor it to meet your patients' needs, or create your own." Surveillance "identifies at-risk patients, monitors their care, and guides the care team" with "action lists, including orders, documentation, and notifications."

Customer evidence (vendor-published):

- Case-study titles: "Southern Ohio Medical Center Lowers Hospital-Acquired C. Difficile Rates by 30% With MEDITECH"; "NMC Health Decreases Antibiotic Use Through MEDITECH's Antimicrobial Stewardship Toolkit."
- Quote (Quality Outcomes Coordinator): "Surveillance allows us to zero in on the cases that we need to review, instead of reviewing a ton of normal charts and then finally getting to something that we need to actually have eyes on." — the case-review funnel is the core daily work.
- Quote (Senior Medical Infectious Disease Director): used CDS/analytics to "decrease and monitor treatment of asymptomatic bacteriuria" for a Joint Commission requirement — infection-related quality work runs through the same surveillance machinery.

Scope note: MEDITECH Surveillance is broader than infection — quality measures, conditions, consults, preventive measures. Infection (CLABSI/CAUTI/HACs, positive microbiology, communicable disease) is one family inside it, and "infection control staff" are named users of the infection watchlists.

## Product C — Vitalacy (variant/adjacent pole)

### Key observations (evidence layer A)

- Products: Hand Hygiene Monitoring ("automated hand hygiene compliance monitoring with low IT impact, three wearable options and strong dashboard reporting"), Dispenser Sensor, Virtual Sitter, Staff Productivity, Staff Rounding Monitoring, Contact Tracing.
- Hardware+software shape: wearable badges and dispenser sensors feeding compliance dashboards — a behavior-monitoring product, not a case-management product.
- Buyer/user alignment: testimonials from Infection Preventionists (GA, MN, VA) and a VP of Quality; "hand hygiene is the number one way to prevent transmission of infections" (Infection Preventionist testimonial); vendor funds an APIC scholarship — sells into the same IP community.
- Interpretation: hand-hygiene compliance monitoring exists both as a module inside surveillance platforms (VigiLanz Pro) and as standalone sensor products (Vitalacy). It shares the buyer but has a different core (behavior compliance events, not infection cases).

## Context — APIC (professional layer)

- APIC = "Association for Professionals in Infection Control and Epidemiology… the nation's leading association for infection preventionists, advancing science, education, and practice to reduce healthcare-associated infections and improve patient safety." 15,000+ members.
- The professional role is the **infection preventionist (IP)**; certifications: a-IPC, CIC (Certification in Infection Control), LTC-CIP (long-term care variant).
- Practice infrastructure: APIC Text ("the most comprehensive… reference for infection prevention and control (IPC)"), PolicyPro (adopt/customize/manage evidence-based IPC policies), toolkits (hand hygiene, C. diff, antimicrobial stewardship, environmental services), Emerging Infectious Diseases Playbooks.
- Interpretation: the software Type serves a defined profession with its own certification ladder, reference corpus, and program vocabulary (IPC, HAI, surveillance). LTC is a recognized sub-domain with its own certification (LTC-CIP) — consistent with VigiLanz's dedicated post-acute tier and McGeer criteria.

## Cross-product Comparison

| Dimension | VigiLanz Infection Prevention (standalone) | MEDITECH Expanse Surveillance (EHR-embedded) | Vitalacy (sensor pole) |
|---|---|---|---|
| Continuous data surveillance | ✔ "works behind the scenes 24/7… pulls from multiple data sources: labs, vitals, medications, notes" | ✔ "analyzes data in real time"; "rules search clinical and demographic data" | ✘ (sensor events only) |
| Criteria/definition-based detection | ✔ "rule-based logic"; "evaluate when McGeer criteria are met"; custom rules | ✔ "evidence-based rules… criteria for CLABSI, CAUTI, and other potential HACs"; "use as is, tailor, or create your own" | ✘ (compliance thresholds, not infection definitions) |
| Candidate queue / worklist for review | ✔ "intuitive worklists… spot cases sooner, intervene earlier, prioritize tasks" | ✔ "zero in on the cases that we need to review, instead of reviewing a ton of normal charts" | ✘ |
| Infection event as record | ✔ events tracked; cross-module event creation pattern documented | ✔ watchlists/profiles with patient status (at risk / tested / positive) | ✘ |
| Isolation / precautions | ✔ "identifying patients who may require isolation sooner" (testimonial) | ✔ indicators "guide clinicians to take appropriate precautions" | ✘ |
| Outbreak / cluster | ✔ Starter "outbreak monitoring"; Pro "cluster surveillance tools"; "visual infection mapping" | ✔ communicable-disease profiles/watchlists (COVID-19 named) | ✘ (contact tracing adjacency) |
| Regulatory reporting | ✔ "Automate NHSN Reporting… reports go directly to NHSN" | not stated on fetched pages (quality measures yes; NHSN submission not evidenced) | ✘ |
| Analytics / trends | ✔ dashboards, "always-current metrics and reports" | ✔ surveillance boards, analytics | ✔ compliance dashboards |
| Antimicrobial stewardship adjacency | ✔ "enhance antibiotic stewardship"; antibiograms; Pharmacy Surveillance sibling | ✔ Antimicrobial Stewardship Toolkit; NMC Health story | ✘ |
| Hand hygiene | ✔ Pro module ("documentation and oversight") | ✘ (not surfaced) | ✔ core product (sensors) |
| Post-acute/LTC variant | ✔ dedicated Starter tier; McGeer criteria; CMS readiness | not surfaced | not surfaced |
| Delivery posture | standalone, EHR-integrated | native EHR module | standalone, sensor-integrated |
| Broader-than-infection scope | suite siblings (safety, quality, pharmacy) are separate products | surveillance spans quality measures/conditions/consults — infection is one family | patient-safety operations (sitter, rounding) |

### Evidence layers

- **A (directly observed)**: all product-page observations above.
- **B (cross-product commonality)**: continuous data surveillance + criteria-based detection + review queue + alerts + EHR/LIS data substrate (both core products); stewardship adjacency (both); isolation/precaution surfacing (both); hand-hygiene monitoring existing in the ecosystem (module + standalone).
- **C (canonical inference)**: the Type is the IPC program's system of record — surveillance criteria → detected infection events → IP adjudication → facility infection registry → prevention action + mandatory reporting.

## Canonical Model (working)

```text
Surveillance criteria/definitions (maintained content)
        │ evaluated continuously against
        ▼
Patient clinical data (labs, meds, vitals, notes, demographics — from EHR/LIS)
        │ rule evaluation
        ▼
Detected candidate → Infection event of record (per patient, with evidence)
        │ worked by the infection preventionist
        ▼
Review / adjudication (criteria evaluation, classification, dispositions)
        │ confirmed events accumulate into
        ▼
Facility infection registry / line list (unit, organism, time, procedure views)
        │
        ├──► prevention action (isolation, rounding, improvement work)
        └──► reporting (internal + regulatory, e.g., NHSN in the US)
```

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. **Surveillance criteria as maintained content** — the facility's codified infection surveillance definitions (standard sets adopted/tailored/locally authored) that the system evaluates patient data against. Remove → generic clinical alerting/analytics with no surveillance program.
2. **The infection event of record** — a persistent, individually managed record per suspected/confirmed infection event, linked to an identified patient, carrying the supporting evidence. Remove → an alert feed with no case memory.
3. **The IPC review loop** — the infection preventionist works the queue of detected candidates, evaluates the criteria against evidence, and the classification outcome becomes the facility's infection record. Remove → unreviewed auto-detection, not an IPC program tool.
4. **The facility infection registry** — confirmed events aggregate into the facility's line list / registry with time/unit/organism views, feeding prevention action and external reporting. Remove → per-patient case tool with no program picture.

Jointly-held is load-bearing: 1 alone = a rules engine; 2 without 3 = auto-detected log; 3 without 1+2 = generic chart-review task list; 1+2+3 without 4 = case tool with no program view; 4 without 1–3 = a spreadsheet of counts with no case-level basis.

### L1 — Common Mature Structure (not definitional)

- Continuous automated detection engine over EHR/LIS feeds (paper-era equivalent: manual chart review of micro results)
- Alert/notification delivery and prioritized worklists
- Isolation/precaution identification and status surfacing
- Outbreak/cluster detection and mapping
- Dashboards, trends, rate views by unit/organism
- Regulatory reporting support (in the US, direct NHSN submission — documented in one sampled product; treat cross-market as common-but-not-universal)
- Multi-facility / system roll-up
- Standard content libraries maintained by the vendor (boards, rules, toolkits)

### L2 — Variant / Optional Structure

- Delivery posture: standalone specialist vs EHR-embedded module
- Care-setting variant: acute vs post-acute/LTC (different criteria sets — e.g., McGeer; different regulatory posture — CMS surveys)
- Antimicrobial stewardship adjacency (antibiograms, pharmacy surveillance sibling, stewardship toolkits)
- Hand-hygiene compliance monitoring (module or standalone sensor products)
- Construction risk / ICRA, environmental rounds
- Communicable-disease/emerging-infection profiles (pandemic-driven)
- Employee exposure/occupational-health follow-up — NOT observed in the fetched sample; unverified, do not assert
- Regional/regime differences in reporting targets and definition sets

### L3 — Vendor-specific (research notes only)

- Inovalon tier packaging (Starter/base/Pro), VigiLanz brand naming, KLAS ranking claims, "20+ years" heritage claim, cross-module trigger from Pharmacy Surveillance to Safety Management, MEDITECH's 28-board count and toolkit names, Vitalacy wearable/dispenser hardware options and APIC scholarship.

## Historical / Market-Sample Check

- Paper-era IPC: IPs manually reviewed microbiology results, kept hand-maintained line lists of infections, met as an infection committee, and reported periodically to regulators (US: NNIS, then NHSN from 2005). Criteria + case finding + review + line list + report all exist without software automation → L0 holds; automation, real-time engines, dashboards, NHSN auto-submission are era-current implementations (L1).
- Regional: UK/EU IPC programs run the same structure against national surveillance protocols rather than NHSN; the definition must say "surveillance criteria/definitions," not "NHSN definitions." NHSN automation is a regime implementation (L1/L2).
- EHR-embedded modules (MEDITECH) and standalone specialists (VigiLanz) both satisfy L0 → delivery posture is a variant, not a Type split.
- Older standalone surveillance products (e.g., pre-acquisition specialist vendors in the same KLAS category) were not directly fetchable; the historical check therefore leans on the paper-era structural argument plus the two fetched poles. Confidence: adequate for L0, moderate for L1 breadth.

## Vendor-specific Findings

- Inovalon: three-tier packaging; post-acute Starter with McGeer criteria and CMS-survey framing; Pro adds cluster tools, hand hygiene, ICRA, advanced antibiograms; NHSN direct submission; suite siblings (Pharmacy Surveillance, Safety Management, Quality Management, Audit Management, MDS, PBJ, UB); "clinical surveillance" category term; KLAS #1 claims.
- MEDITECH: Surveillance as a top-level EHR solution spanning quality/conditions/consults; named objects Profiles / Watchlists / Special indicators; 28 standard boards; 8 Excellence Toolkits; infection control staff + nurse managers as watchlist users; boards are also clinician action surfaces (order/document/message on the spot).
- Vitalacy: wearable + dispenser-sensor hand-hygiene monitoring; virtual sitter; contact tracing; APIC scholarship.

## Boundary Findings

1. **vs Clinical Decision Support System** — CDSS delivers person-specific advice to the treating clinician at a decision point; the clinician retains the decision. The Infection Prevention Platform is the IPC program's own system of record: the user is the infection preventionist, the object is the infection event, the output is the facility's HAI record and reports. The seam is visible in MEDITECH: its Surveillance module both populates IPC watchlists and pushes action lists into clinician workflows — the same installation serves both Types. Remove the IPC program/registry/reporting frame and only the CDS advice engine remains; remove the clinician-facing advice delivery and only the IPC platform remains.
2. **vs Healthcare Quality Management** — quality management spans the whole quality program (event reporting, audits, measures, accreditation readiness); infection surveillance is one specialized domain. Evidence: Inovalon sells Infection Prevention and Quality Management as separate products in the same suite.
3. **vs Public Health Surveillance Platform** — population/regional scale operated by public-health agencies (e.g., NHSN itself); the hospital platform is a data source and reporting constituent, not the agency system.
4. **vs LIS** — the LIS owns specimen/test workflow and produces micro results; the IPC platform consumes those results as surveillance input. Antibiogram analytics appear in both worlds (VigiLanz antibiograms) but the LIS's core is the lab operation, not case adjudication.
5. **vs EHR** — EHR-embedded surveillance is a delivery posture of this Type (MEDITECH), not a separate Type; the standalone specialist exists precisely because facilities want deeper surveillance content and cross-EHR analytics than the EHR ships.
6. **vs hand-hygiene / prevention-behavior monitoring products** — sensor-based compliance monitoring (Vitalacy; VigiLanz Pro module) shares the buyer but its core objects are behavior-compliance events, not infection cases. Adjacent capability, sometimes bundled.
7. **vs antimicrobial stewardship** — pharmacy-side program with distinct users (pharmacists) and objects (drug regimens); commonly bundled/sold alongside (both core products show adjacency) but a different Type.

"Remove what to become the other Type" tests:
- Remove the IPC review loop and registry, keep advice at the point of care → CDSS.
- Remove the infection-specific criteria/cases, keep generic event/audit/measure machinery → Healthcare Quality Management.
- Remove the single-facility program frame, operate at agency/population scale → Public Health Surveillance Platform.
- Remove case adjudication, keep specimen/test workflow → LIS.

## Uncertainties

- Case-adjudication state models (exact dispositions, e.g., confirmed/probable/ruled-out labels) were not directly observed in fetched pages; the review loop itself is well evidenced (criteria evaluation, "cases we need to review"), but precise state vocabularies are not asserted.
- NHSN reporting is directly evidenced for one product only; cross-market prevalence of direct submission vs manual upload is not established.
- Employee-health/exposure modules, environmental-rounds modules beyond ICRA, and public-health case-reporting handoff (communicable disease to health departments) were not observed in the sample; left unasserted.
- Denominator/device-day mechanics (how rates are computed) were not surfaced in fetched pages; not asserted.
- The two unreachable standalone specialists (Sentri7, SafetySurveillor) limit the standalone-pole breadth; their category membership is known from the sampled vendor's KLAS reference, not from their own documentation.

## Final Synthesis

An Infection Prevention Platform is the healthcare facility's IPC-program system of record. Its defining structure is small: maintained surveillance criteria; persistent infection-event records linked to identified patients; an infection-preventionist review loop that turns detected candidates into classified facility records; and a facility infection registry whose rate/trend views drive prevention action and mandatory reporting. Everything else commonly associated with the category — real-time detection engines, alerts and worklists, isolation status, outbreak/cluster tools, NHSN automation, antibiograms, stewardship adjacency, hand-hygiene modules, multi-facility roll-ups — is mature market structure or optional extension, not definition. The Type is realized both as standalone specialists integrated with the EHR and as EHR-embedded surveillance modules; both satisfy the same core. The closest boundary is with Clinical Decision Support Systems: surveillance output may feed clinician-facing action lists, but ownership of the infection record and the program/reporting frame belongs to this Type.
