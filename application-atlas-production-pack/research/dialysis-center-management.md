# Research Notes — Dialysis Center Management

## Research Goal

Understand what a Dialysis Center Management application actually is from real products: what its core objects are, who uses it, how a dialysis facility's daily work flows through it, which rules and states matter, and how it differs from adjacent Types (general EHR, practice management, machine data systems, remote patient monitoring).

## Initial Boundary

Initial hypothesis (before research): software that runs the daily clinical and administrative operation of an outpatient dialysis facility — a recurring, protocol-driven treatment delivered to a fixed patient panel on a fixed station/shift schedule, three times per week per patient, indefinitely. Expected neighbors: general EHR, Practice Management System, Patient Scheduling, dialysis-machine data systems, Home Health / remote monitoring.

Main confusion risk observed up front: the dialysis clinic software market is dominated by (a) the two largest dialysis providers running proprietary in-house systems with no public documentation, and (b) machine manufacturers whose clinical IT products are documented publicly. The "standalone dialysis clinic software for independent clinics" segment proved largely unreachable from this environment (see Sources — access limitations).

## Research Questions

1. What is the central object — the treatment session? the schedule slot? the patient record?
2. What does a dialysis treatment record contain (weights, fluid removal, machine parameters, observations)?
3. How does the recurring schedule (shift pattern × station) work, and is it definitional?
4. How are laboratory data and medication cycles handled (recurring renal panels, trends, interpretation)?
5. How does machine/device integration work (pre-setting, prescription transfer, auto-capture)?
6. What quality-assurance machinery is specific to dialysis (target values, key indicators, center vs patient views)?
7. What integration exists with hospital information systems / general EHRs / labs?
8. What role model does the interdisciplinary team imply?
9. What variants exist (in-center vs home, single clinic vs chain, machine-maker suite vs device-integrated cloud vs renal-unit EHR)?
10. Boundary: what would make this a general EHR, and what makes it not?

## Representative Products

Selection principles: market representativeness + documentation completeness + different product philosophies + different customer layers. The US big-chain proprietary systems (Fresenius Medical Data System, DaVita's system) have no public operational documentation and were not usable as evidence. Three products with public, fetchable official documentation were selected, deliberately spanning three philosophies:

1. **Fresenius Medical Care — Therapy Data Management System (TDMS)** (with Therapy Monitor (TMon), Therapy Support Suite (TSS), communication Data Link (cDL)) — the machine-and-clinic conglomerate's integrated dialysis-center IT suite (global/EU-facing documentation; in-center hemodialysis focus). Philosophy: clinic-side system of record bound to the machine-maker's ecosystem, modular (data acquisition / clinical data management / corporate data management).
2. **Outset Medical — Tablo Hemodialysis System + EMR Connect** (US; acute in-hospital, in-center unit, skilled nursing, home) — device-maker cloud platform. Philosophy: the machine itself generates and transmits structured treatment data into the general EMR's flowsheets; the clinic system of record may remain the hospital EHR.
3. **Renalware** (UK NHS renal units; open-source renal unit management application, Ruby on Rails; developed from King's College Hospital context, mirrored publicly) — renal-patient-pathway EHR covering dialysis inside a wider renal dataset. Philosophy: one renal-unit record across CKD/dialysis/transplant, with registry data sharing.

Context source (Tier 3): RenalWEB — long-running dialysis-industry portal (news, product directories, industry history), used for market-structure context only.

## Sources

### Reached (research date 2026-09-07)

- Fresenius Medical Care — corporate site (global EN): https://www.freseniusmedicalcare.com/en — company profile (≈3,600 dialysis centers, ≈292,000 patients worldwide, >44 M dialysis treatments; "the world's leading provider of products and services for individuals with renal diseases"), Healthcare Professionals > Digital Solutions menu.
- Fresenius Medical Care — Therapy Data Management System (TDMS): https://www.freseniusmedicalcare.com/en/healthcare-professionals/digital-solutions/therapy-data-management-system-tdms/
- Fresenius Medical Care — Clinical management: https://www.freseniusmedicalcare.com/en/healthcare-professionals/digital-solutions/clinical-management/ (covers TMon, TSS, cDL positioning)
- Outset Medical — root: https://www.outsetmedical.com/ (Tablo system; audiences: administrators/nurses/nephrologists/SNF; acute/home contexts; FDA indications text)
- Outset Medical — EMR Connect: https://www.outsetmedical.com/emr-connect/ (data options, connectivity, EMR vendor support)
- Renalware — GitHub org: https://github.com/renalware → canonical repo: https://github.com/airslie/renalware (public read-only mirror; README)
- Renalware — documentation site: https://airslie.github.io/renalware/ (sparse; topics list includes Reporting, Safety Alerts, Accessibility; TODO list names Charting, HD Diary, UKRDC, HL7/Mirth/stunnel, Pathology groups)
- RenalWEB — industry portal: https://renalweb.com/ (Dialysis Yellow Pages "120 categories" of products/services; industry history essay by editor: 1973 federal dialysis legislation, 1983 composite-rate reimbursement, rise of for-profit dialysis corporations, Kt/V as adequacy measure, ESRD Quality Incentive Program; showcase categories incl. renal laboratory services)

### Not reachable (access limitations — assertion strength reduced accordingly)

- Search engines: DuckDuckGo (html + lite, timeouts ×3), Bing (regional redirect, unusable ×3), Mojeek (captcha). No working general web search from this environment; discovery relied on direct URL attempts and link-following.
- Capterra / GetApp / G2 / SourceForge software categories: 403/404.
- pcdialysis.com (transport error), renaltracky.com (transport error), dialysispro.com (403), clinicalcomputing.com (timeout ×2), renalware.org (transport error), dialysisadvances.com Yellow Pages (transport error), cms.gov ESRD Quality Reporting System page (403).

### Consequence of limitations

- The **US independent-clinic standalone dialysis software segment** could not be documented from vendor-operational sources. Claims about that segment are NOT made in the final document beyond what context sources support.
- **US regulatory-reporting specifics** (EQRS/CROWNWeb mechanics, CMS forms) could not be verified; the final document uses only calibrated, generic wording for registry/regulatory submission.
- Precise operational facts (field counts, time-savings figures) observed on vendor marketing pages are recorded here as vendor claims (L3), not promoted to the canonical model.

## Product Observations

### Fresenius Medical Care — TDMS (+ TMon, TSS, cDL) [Evidence layer A]

Official product pages (freseniusmedicalcare.com, Digital Solutions, EN, accessed 2026-09-07):

- Positioning: "An integrated solution for professionals — Data Acquisition, Data Management, Quality Assurance"; "seamlessly integrated in existing working processes and supports the user in his or her daily tasks, such as ultra-filtration management, prescription transfer to dialysis devices or treatment documentation"; "the right tool for every professional in a dialysis center"; "flexible solution to support working processes for individual demands in dialysis centers and hospitals".
- **Monitoring area** (explicit list): recording the weight of a patient before and after dialysis; preparation and pre-setting of the dialysis devices; documenting the treatment process; documenting any additional laboratory tests during the dialysis; documenting any administration of medication; documenting results of the treatment; documenting predetermined working procedures; documenting any changes in the treatment procedures.
- **Clinical Data Management** (explicit list): creation and processing of instructions for dialysis treatment; creation and processing of medication instructions; maintenance of administration data; maintenance and interpretation of laboratory data; production of reports and writing doctors' letters; supporting internal and external quality assurance; multicenter management capability; advanced data analysis and reporting functionality; treatment and medication scheduling at patient or clinic level.
- **Corporate Data Management** (explicit list): communication with higher-level hospital information systems (HIS); supporting core business processes in hospitals, e.g. billing process and treatment documentation in electronic health records.
- Clinical management page: "Shared management of dialysis treatment data; Long-term treatment documentation; Managing prescriptions and pre-setting devices; Exchange of patient data with Hospital Information Systems."
- Quality assurance framing: "Quality assurance in dialysis means a continuous process of defining target values for key indicators: to measure outcomes, interpret results, and intervene. This is done for individuals and groups of patients in a center or network." Data must be contextual (gender, comorbidity, medical data, date), "aggregated and yet specific, so you can drill down in the same view from different perspectives (patient and clinic)."
- Therapy Monitor (TMon): "online documentation of various data collected before, during and after dialysis"; bedside monitoring; "overview of the status of current treatments according to the principle 'all information at a glance'"; part of TDMS. Vendor-cited study: ≈25 minutes / ≈40% nursing-time saving per dialysis treatment (vendor claim, unverified).
- Therapy Support Suite (TSS): "central clinical management software that carries out, creates and manages patient prescriptions, medication plans, documentation of treatment data, and patient-related laboratory data… enhanced reporting capabilities and allows the professional management of a group of dialysis centers. The Therapy Support Suite is part of the Therapy Data Management System."
- communication Data Link (cDL): "seamless integration of Therapy Data Management System as a sub-system in a higher-level hospital information system"; consistent essential patient data across wards; supports "billing processes or treatment documentation in electronic health records"; references lab information and admission-discharge-transfer (ADT) systems.
- Modular architecture statement; one-contact-partner installation/training/support model.
- Company scale (About page): ≈3,600 dialysis centers worldwide, ≈292,000 patients, >44 M dialysis treatments per year.

### Outset Medical — Tablo + EMR Connect [Evidence layer A]

Official pages (outsetmedical.com, accessed 2026-09-07):

- Tablo Hemodialysis System: dialysis device "designed from the inside out"; "covering 95% of dialysis treatments" (vendor claim); indications (FDA text on site): acute and/or chronic renal failure in acute or chronic care facilities, also home; treatment types IHD, SLED/SLEDD, PIRRT, isolated ultrafiltration; not for CRRT.
- Outset EMR Connect: "Two-way cloud communication for automated documentation and system management"; "Simplify dialysis workflows from charting to billing."
  - Automated: "Patient charting and documentation for Tablo to save staff time"
  - Accurate: "Flowsheets in patient chart designed to minimize documentation errors"
  - Eliminate: "Manual charting with data transfer from Tablo to your EMR platform"
  - Flow diagram: Patient treatment → secure cloud-based connection → automated patient charting in EMR.
  - Data options: "70+ treatment fields for charting"; "Data transmission timing defined by customer"; "Event-based data and alarms"; "One-way dialysis treatment data transmission".
  - Connectivity: "HL7v2 and API/JSON communication options"; "Support for HIPAA compliance".
  - EMR vendor support: "Major vendors such as Epic, Cerner/Oracle Health, Meditech and Gaia".
- Vendor claim surfaced on page: "Nurses spend up to 41% of their time on documentation."
- Audiences: administrators, nurses, nephrologists, skilled nursing facilities; deployment contexts requested in contact form: Acute, Home, ICU, In-Center Dialysis Unit, Inpatient Rehab Facility, LTACH, SNF.
- Trademarks on site: Tablo, TabloCart, MyTablo, TabloHub.
- Business context: "Nearly 1,000 hospitals and health systems have already insourced their acute dialysis" — i.e., hospitals running dialysis as an in-house service line.

### Renalware [Evidence layer A — code/docs; sparse documentation]

Official repo + docs site (github.com/airslie/renalware; airslie.github.io/renalware; accessed 2026-09-07):

- Self-description: "Renalware uses demographic, clinical, pathology, and nephrology datasets to improve patient care, undertake clinical and administrative audits and share data with external systems." "open-source Ruby on Rails application for **renal unit management**."
- Demo users ordered "in order of role permissiveness": superkch (super renal coordinator), kchdoc, kchnurse, kchguest — an interdisciplinary role ladder including a coordinator role and role-scoped access.
- Documentation site topics: Reporting; Testing; Nags (reminders); Safety Alerts; Accessibility. Explicit TODO list naming product areas: Charting, **HD Diary**, **UKRDC** (UK Renal Data Collaboration data sharing), HL7 / Mirth / stunnel integration stack, Pathology and configuring groups, Configuring Event Types, Azure architecture.
- "Hospital-specific deployment state is tracked through release documentation and container image tags" — per-unit deployment model.
- GitHub org topic tags: rails, renal, ruby.

### RenalWEB (industry context, Tier 3) [Evidence layer B/C for market context]

- Long-running industry portal ("Since January 1999") with a Dialysis Yellow Pages of ~120 product/service categories — evidence that dialysis facility software, laboratory services, water treatment, machines etc. form an established supplier industry.
- Editorial history (by portal editor, former Fresenius product manager): 1973 federal dialysis legislation (US Medicare ESRD coverage); 1983 composite-rate reimbursement driving dialysis "out of hospitals and into for-profit dialysis corporations"; Kt/V as the adequacy measure tied to reimbursement; ESRD Quality Incentive Program as a top-down quality mechanism. Used only as market/regulatory context, not as product-structure evidence.
- Showcase advertisers confirm adjacent supplier categories: renal laboratory services (Ascend Clinical), water treatment, digital patient engagement (Renal Care 360).

## Cross-product Comparison

| Aspect | Fresenius TDMS (machine-maker clinic suite) | Outset Tablo + EMR Connect (device-integrated cloud) | Renalware (renal-unit EHR, open source) |
|---|---|---|---|
| Primary setting | in-center dialysis centers + hospitals (EU-facing docs) | hospital acute units, in-center units, SNF, home (US) | NHS renal units (hospital-based specialty units) |
| Patient population | facility's dialysis patients; administration data maintained; multicenter capable | patient's treatments transmitted per session; census presumably lives in EMR | renal patient population across CKD/dialysis/transplant; demographics + clinical + pathology datasets |
| Central operational object | the dialysis treatment: documented before/during/after; weight pre/post; treatment results; changes documented | the dialysis treatment: 70+ treatment fields, event-based data, one-way transmission into EMR flowsheets | HD Diary (station/day diary) + charting within the renal pathway |
| Prescription | creation/processing of treatment instructions; prescription transfer to devices; medication instructions | machine is the treatment executor; prescription-level data among transmitted fields (not itemized publicly) | within renal clinical record (details not publicly itemized) |
| Schedule | treatment and medication scheduling at patient or clinic level | none documented (machine/EMR layer, not a scheduling system) | HD Diary (dialysis station diary) |
| Machine/device integration | pre-setting of devices; prescription transfer to dialysis devices | two-way cloud communication with the machine; automated capture from Tablo | not evidenced in reachable docs (UK units often separate; HL7/Mirth stack exists for integrations) |
| Laboratory | maintenance and interpretation of lab data; additional lab tests during dialysis documented | not documented on reachable pages | pathology datasets; pathology group configuration |
| Medication | medication instructions/plans documented | event-based alarms; medication fields not itemized publicly | clinical datasets (details not publicly itemized) |
| Quality assurance | defining target values for key indicators; measure → interpret → intervene; individuals and groups in a center or network | minimized documentation errors; (quality analytics for enterprise) | clinical and administrative audits; Nags (reminders); Safety Alerts |
| Reporting/letters | reports; doctors' letters; advanced data analysis and reporting | EMR flowsheets are the record; charts for enterprise | Reporting module; letters |
| Multicenter / network | multicenter management capability; TSS manages "a group of dialysis centers" | enterprise posture across ~1,000 hospitals (vendor claim) | per-renal-unit deployment |
| HIS / EHR integration | cDL sub-system integration with hospital information systems; ADT; lab info; billing; EHR treatment documentation | the product's purpose: HL7v2/API-JSON into Epic/Cerner/Meditech/Gaia flowsheets | "share data with external systems"; UKRDC; HL7/Mirth/stunnel |
| Patient-facing | (PD PatientOnLine and kinexus exist in FMC's digital portfolio; not part of TDMS pages fetched) | MyTablo (patient trademark); home program support | not evidenced in reachable docs |
| Roles | "every professional in a dialysis center" (nurses, physicians, technical staff) | administrators / nurses / nephrologists | coordinator / doc / nurse / guest permission ladder |

**Stable commonalities (visible across products):**

1. The dialysis **treatment session** is the unit of work: something is prescribed, executed on a machine, and documented before/during/after (weights, fluid removal, parameters, observations, results). All three products exist to make this record accurate and automatic.
2. A **persistent longitudinal treatment record** per patient ("long-term treatment documentation" — FMC; EMR flowsheets — Outset; datasets + audit — Renalware).
3. A **defined dialysis patient population** with administrative lifecycle (census/admission data — FMC; EMR census — Outset's model; renal patient datasets — Renalware).
4. **Integration outward** — hospital information systems/EHRs, labs, and (UK) national data-sharing (UKRDC). Every product's perimeter is defined by these handoffs.
5. **Quality/audit machinery** — indicator targets, audits, safety alerts (present in all three in different depths).

**Consistent but not universal (→ standard capabilities, not definition):**

- Recurring **schedule** (FMC: patient/clinic-level scheduling; Renalware: HD Diary; Outset: none — because Outset is a device-data layer, not a clinic system of record).
- **Machine pre-setting/prescription transfer** (FMC explicit; Outset realizes it inside the device; Renalware: not evidenced).
- **Labs and medication** management (FMC explicit; Renalware via pathology/clinical datasets; Outset: out of scope).

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the software stops being a dialysis-center management application:

1. **Dialysis patient population under active management** — a defined census of patients receiving maintenance dialysis care from the facility, carried with an administrative lifecycle (admission → active → discharge/transfer).
2. **The dialysis treatment session as a first-class, prescribed, documented object** — a clinician-authored prescription (what to run: modality, targets) that is executed at a treatment station/machine and documented as a structured per-session record spanning before/during/after the treatment (e.g., pre/post weights and fluid removal, machine/device parameters, patient observations, treatment result and deviations).
3. **Persistent longitudinal treatment history per patient** — sessions accumulate into the patient's continuing dialysis record, queryable over time (the digital successor of the paper flowsheet binder).

Remove #1 and the software is a generic treatment-charting tool. Remove #2 (no prescribed, machine-delivered, per-session record) and it is a generic EHR/scheduling product. Remove #3 and it is a session-terminal device app, not a center's system of record.

**Historical / regional check (§24):** a paper-era dialysis center (1960s–70s and still today in low-resource settings) satisfies this structure without any software: a patient roster, per-treatment paper flowsheets, and accumulating chart binders. A UK renal unit, a German machine-maker clinic, and a US device-cloud hospital program all satisfy it without sharing any vendor's terminology. The definition therefore does not depend on machines (manual machine setting possible), cloud delivery, or US regulatory machinery.

### Level 1 — Common Mature Structure (standard capabilities)

- **Recurring rotating schedule** — the shift-pattern grid (patient × weekday pattern × station/chair × shift) and its daily/weekly operations; realized as scheduling at patient/clinic level (FMC) and as an HD station diary (Renalware). Absent only in device-data-layer realizations.
- **Machine/device integration** — pre-setting devices from prescriptions, transferring prescriptions to machines, automatic capture of treatment parameters (FMC TDMS; Outset's whole design).
- **Laboratory data management** — recurring renal lab panels, results maintenance and interpretation, trend views (FMC; Renalware pathology datasets).
- **Medication management** — medication instructions/plans, administration documentation during treatment (FMC).
- **Quality assurance machinery** — target values for key indicators, measure → interpret → intervene loops, individual and group/center views, audit and reporting (all three, different depths).
- **Reporting and letters** — reports, doctor letters, dataset exports (FMC; Renalware).
- **Integration with hospital/external systems** — HIS/EHR sub-system integration, ADT feeds, lab feeds, billing support (FMC cDL; Outset EMR Connect — the product's core; Renalware UKRDC/HL7).
- **Role-scoped access for the interdisciplinary team** — nurses, physicians, coordinators, technical/admin staff (all three; Renalware's role ladder is explicit).

### Level 2 — Variant / Optional Structure

- **Multicenter/enterprise network operations** — managing a group of centers (FMC TSS; Outset enterprise posture; chain operators). Depends on operator scale.
- **Regional regulatory/registry submission** — where national ESRD programs exist, facilities submit census, treatment and quality data to registries/quality programs (UKRDC in the UK evidenced; US context evidenced only as reimbursement/quality-program history, mechanics unverified). Region-dependent.
- **Billing/revenue-cycle support** — US composite-rate-style reimbursement makes treatment-count billing a core process; often realized via HIS integration rather than in-product billing (FMC cDL mentions billing support). Region-dependent depth.
- **Home therapies support** — peritoneal dialysis and home hemodialysis with patient-side data capture and remote monitoring (FMC PatientOnLine/kinexus; Outset home program with MyTablo). Changes the venue but not the treatment-session model.
- **Acute/in-hospital dialysis support** — same treatment model delivered in hospital units (Outset's core market). Venue variant.
- **Patient-facing engagement** — portals/apps for patients (MyTablo; FMC's PD patient products). Optional.
- **Analytics dashboards/cockpits** — aggregated, drill-down center/network views (FMC describes patient-vs-clinic drill-down; vendor sells a named cockpit product). Optional depth.
- **Water treatment / biomedical / equipment maintenance logs, supplies inventory** — adjacent operational records; not evidenced in the fetched pages; treat as unverified-adjacent (common in the industry's supplier categories, not confirmed as in-product modules in this sample).

### Level 3 — Vendor-specific (Research Notes only)

- Fresenius: TDMS/TMon/TSS/cDL module names; "≈25 min / 40% nursing time saved per treatment" study claim; "all information at a glance" TMon framing; Nephrologic Cockpit / PatientOnLine / kinexus naming; FMC scale figures (3,600 centers / 292k patients / 44M treatments); modular architecture and single-contact installation model.
- Outset: TabloHub/MyTablo/TabloCart trademarks; "70+ treatment fields"; "Nurses spend up to 41% of time on documentation"; "covering 95% of dialysis treatments"; "nearly 1,000 hospitals" claim; FDA indications wording (IHD/SLED/PIRRT/isolated UF; not CRRT); Epic/Cerner-Oracle Health/Meditech/Gaia named EMR support.
- Renalware: kch demo-user naming; Ruby/Rails/PostgreSQL stack; Mirth/stunnel integration components; Azure architecture TODO; Nags module; per-unit release/container deployment.
- Market-structural: largest US providers run proprietary in-house systems (from industry knowledge/context; NOT verified from public operational docs — see Uncertainties).

## Vendor-specific Findings

- Outset's philosophy inverts the usual architecture: the machine is the charting front-end and the general EMR is the system of record; the dialysis-specific software is a data-and-documentation bridge. This is a valid realization of the Type's *data layer* but by itself it does not carry the census/schedule/quality machinery — it demonstrates where the Type's boundary with the general EHR sits.
- FMC's TDMS is the fullest single-vendor expression of the Type: it names all three layers (acquisition/clinical/corporate) that the canonical model abstracts.
- Renalware shows the *renal-pathway* philosophy: dialysis is one module inside a unit-wide renal record; the same vendor family also covers CKD clinics and transplantation. The dialysis-specific seam is the HD Diary + treatment charting + dialysis datasets.

## Boundary Findings

| Neighbor | Relationship | What removes the boundary confusion |
|---|---|---|
| Electronic Health Record (general) | adjacent / host | A general EHR holds the patient's overall chart; a dialysis center management system is the specialty system of record for the treatment operation (prescription → machine session → flowsheet; station/schedule; dialysis quality indicators). In integrated hospitals the general EHR is the *host* and the dialysis system feeds it (Outset EMR Connect; TDMS cDL). If the prescribed-machine-session model is removed, what remains is a general EHR. |
| Practice Management System | adjacent | PM handles generic appointments/billing; dialysis management embeds scheduling inside the treatment operation (shift × station × prescription) and its billing is treatment-count/regime-specific. |
| Patient Scheduling | capability overlap | Scheduling dialysis is constraint-based (chair/shift rotation, machine reuse, prescription cadence) — a capability of the Type, not the Type itself. |
| Dialysis machine data management (device-side tools) | upstream seam | Device tools capture/forward treatment data but do not manage the census, schedule, longitudinal per-patient record or quality program; they are the acquisition layer of the Type (or a boundary product like Outset's EMR Connect). |
| Remote Patient Monitoring | variant-blurred for home | RPM watches patients between encounters; home-dialysis program support includes remote treatment data but centers the dialysis session. In-center core is clearly distinct; home variants share telemetry plumbing. |
| Chronic Care Management | adjacent service model | CCM coordinates between-visit care for chronic conditions; dialysis management runs the recurring treatment itself as the facility's production process. |
| Home Health / Home Care Management | adjacent service model | Visit-based home services vs facility's recurring machine-delivered treatment; home-dialysis coordination overlaps partially (transport, visits) but the core object differs. |
| Organ Transplant Management | sibling within nephrology | Different pipeline (referral/evaluation/waitlist/organ match), though the same renal patient may move between them; Renalware covers both in one unit record — evidence they are distinct modules of one renal pathway, not one Type. |
| Renal Laboratory services | supplier seam | Renal labs (large dedicated labs serve dialysis providers) feed the lab-management layer; they are a service, not the application. |

**"Remove what → becomes another Type" tests:**
- Remove the per-treatment prescribed/machine-delivered session record → generic EHR + scheduling.
- Remove the longitudinal per-patient treatment history → device session app / point-of-care terminal.
- Remove the dialysis-specific semantics (weights/UF, machine parameters, dialysis quality indicators) and keep the generic structure → clinic practice-management product.
- Add general-patient populations, encounters, orders, problem lists as the primary model → EHR.

## Uncertainties

1. **US independent-clinic standalone software** (e.g., small vendors serving community dialysis clinics) could not be documented — vendor sites unreachable; review aggregators blocked. The canonical model rests on three products from other realizations; the standalone segment is assumed to share the core (paper-flowsheet successor) but this was not verified from its own documentation.
2. **US regulatory reporting mechanics** (EQRS/CROWNWeb field-level flows) unverified (cms.gov blocked). The final document deliberately uses generic wording ("national registry/quality-program submission where applicable").
3. **Renalware's dialysis module depth** (HD session flowsheet fields, machine integration) not verifiable from the sparse public docs; inferred only at the level of named modules (Charting, HD Diary).
4. **Big-chain proprietary systems** (Fresenius US FMDS, DaVita) — no public operational documentation; their existence/role is market context only and is not used as product-structure evidence.
5. **In-product billing depth** — evidence shows billing realized via HIS integration (FMC cDL); whether typical standalone products embed billing directly is unverified in this sample.
6. **Water treatment/maintenance/inventory as in-product modules** — industry supplier categories exist, but none of the three sampled products' fetched pages evidences these modules; left as adjacent/unverified.

## Final Synthesis

A Dialysis Center Management application is the specialty clinical-operations system of record for a facility that delivers recurring, machine-delivered, life-sustaining dialysis treatments on a fixed schedule. Its defining core is: (1) a managed dialysis patient census, (2) the prescribed treatment session as the central documented object spanning pre/during/post treatment, and (3) each patient's persistent longitudinal treatment history. Everything else — the rotating schedule grid, machine pre-setting and auto-capture, labs, medications, quality-indicator machinery, letters, HIS/EHR/registry integration, multicenter management, home-therapy and acute variants — is standard, regional, or optional structure layered onto that core. The Type is distinct from a general EHR by its treatment-session object model and its station/schedule/quality machinery; in integrated settings it typically coexists with a general EHR as the feeding sub-system.
