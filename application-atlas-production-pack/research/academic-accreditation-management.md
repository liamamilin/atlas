# Research Notes — Academic Accreditation Management (§23 Education, Research & Knowledge Institutions)

Research date: 2026-09-06

## Research Goal

Understand what "Academic Accreditation Management" means as an Application Type in the
directory's education context, how real products in this space actually work, and how it
differs from the adjacent leaves that share the accreditation vocabulary:

- §11 **Accreditation / Certification Management** — already documented; the *seeking
  organization's* compliance posture toward an external standard (generic/corporate:
  controls, policies, evidence, assessment event, credential maintenance). Its document
  lists this leaf as "probable variant … institutional/programmatic accreditation for
  education shares the core spine but lives in an education-data context".
- §25 **Accreditation Management** — already documented; the *accrediting body's* program
  management (operator side). Its boundary findings state: "the market itself ships
  separate products for the two seats (Weave Education institution-side vs Weave
  Accreditation accreditor-side; Watermark/Nuventive also institution-side); §23 should
  anchor the institution side when processed, otherwise the two leaves would collide."

Working hypothesis (inherited from both prior passes, tested against new evidence): §23's
leaf is the **institution side** — a college, university, school, or academic program
preparing for, undergoing, and maintaining academic accreditation (institutional/regional
and programmatic/specialized). This research tests that hypothesis against real products.

## Initial Boundary

- Academic accreditation is a relationship between an accrediting body (regional
  institutional accreditor, national accreditor, or programmatic/specialized accreditor)
  and an education institution or program. Three seats exist: the body operating the
  program (§25), the institution seeking/maintaining accreditation (this leaf), and —
  loosely — the corporate compliance analog (§11).
- The obvious confusion set:
  1. §25 accreditor-side program management — same relationship, opposite seat;
  2. §11 generic seeker-side compliance — same seat, different domain substrate;
  3. §23 sibling **Institutional Effectiveness Platform** — the same product family
     markets itself as both; accreditation is one driver of institutional-effectiveness
     work;
  4. §23 siblings **Curriculum Management** and **Assessment Platform** — curriculum
     mapping and outcomes assessment appear inside this Type as evidence machinery;
  5. §23 **Digital Credential Platform** — "credential" vocabulary collision (student
     credentials vs institutional accreditation status; also vendor "credentialing"
     modules that actually mean faculty qualifications).

## Research Questions

1. What does the institution-side system contain? (objects: accreditor standards,
   compliance responses, evidence, self-study/report, assessment/curriculum data,
   plans, faculty qualifications)
2. What is the end-to-end workflow across an accreditation cycle: standards setup →
   evidence mapping → gap analysis → authoring → internal review → submission →
   between-cycle readiness → reaffirmation?
3. How are accreditor standards represented (per-accreditor templates? vendor-maintained
   versions? mapped to evidence and assessment data)?
4. What education-specific machinery exists (curriculum mapping, program learning
   outcomes, assessment measures/results, faculty qualifications, program review)?
5. How do systems connect to LMS/SIS/other campus systems?
6. Who are the users (institutional effectiveness office, accreditation liaison, provost/
   deans, program chairs, faculty, non-academic unit leads)?
7. Where is the boundary vs §25 (accreditor side), §11 (generic seeker side), and the §23
   sibling Institutional Effectiveness Platform?
8. Does the historical (pre-software) and non-US-higher-ed reality still fit the model?

## Representative Products

Selected for: market representativeness in the institution-side accreditation market,
different product philosophies, different customer levels, and coverage of the
suite-vs-standalone and data-first-vs-document-first spectrum.

1. **Watermark Planning & Self-Study** (Watermark Insights) — enterprise higher-ed suite
   hub unifying planning, assessment, program review, and accreditation; per-accreditor
   use-case marketing (HLC, SACSCOC, MSCHE, WSCUC, NWCCU, NECHE); lineage of the classic
   accreditation products (Taskstream, LiveText, Tk20 confirmed as "heritage" help-center
   categories). Philosophy: one continuous-improvement hub; accreditation readiness as a
   year-round state fed by assessment data.
2. **Weave Education** — standalone, affordability-and-community positioned platform for
   institutions and programs ("3,200 members"; founded 2006); accreditation, assessment,
   curriculum mapping, program review, strategic planning in one system; vendor maintains
   standards versions. The vendor ships a *separate* product (Weave Accreditation) for the
   accreditor seat — the market's own seat split, useful for the boundary.
3. **SPOL (Strategic Planning Online)** — integrated planning/budgeting/assessment/
   credentialing/accreditation system for colleges and universities (~two decades).
   Philosophy: accreditation as "continuous readiness" embedded in everyday institutional
   work; self-study built from real institutional work rather than retroactive assembly.
4. **eLumen (Insights for Canvas Outcomes)** — LMS-embedded, data-first philosophy:
   outcomes/rubric management, curriculum mapping, assessment planning, juried
   assessments, longitudinal analytics inside Canvas; accreditation workflows evidenced
   downstream (case-study level). Represents the assessment-data substrate end of the
   spectrum.
5. **Nuventive Improvement Platform** — institution-side planning/improvement platform
   covering strategic planning, accreditation, learning outcomes, program review
   (evidence from the prior §25 pass, product-page level).

## Sources

All accessed 2026-09-06 unless noted.

- Watermark Insights — Accreditation use-case hub:
  https://www.watermarkinsights.com/explore/accreditation/
- Watermark Insights — Planning & Self-Study solution page (features, stats, FAQ,
  integrations, testimonials):
  https://www.watermarkinsights.com/solutions/self-study-planning-software/
- Watermark Help Center (product/suite structure; heritage products Taskstream, LiveText,
  Tk20, AMS, OAP): https://support.watermarkinsights.com/hc/en-us
- Weave Education — root: https://weaveeducation.com/
- Weave Education — solution page: https://weaveeducation.com/accreditation-assessment-management-software/
- Weave Education — accreditation software page:
  https://weaveeducation.com/accreditation-software-higher-ed/
- SPOL — root: https://spol.com/
- SPOL — Accreditation module page: https://spol.com/solutions/accreditation-software-higher-ed/
- eLumen — root (Insights for Canvas Outcomes): https://www.elumenconnect.com/
- Nuventive — root: https://nuventive.com/ (accessed in the prior §25 pass, 2026-09-06)
- Prior passes (context, not re-fetched): research/accreditation-management.md,
  research/accreditation-certification-management.md, and their application documents.

Evidence layers used below: **A** = directly observed on an official source of a named
product; **B** = cross-product commonality.

## Product Observations

### Watermark Planning & Self-Study (institution side; evidence layer A)

From the accreditation use-case hub, the P&SS solution page (incl. FAQ), and the Help Center:

- Positioning: "Accreditation Management Software for Higher Ed"; P&SS "unifies planning,
  assessment, program review, and accreditation, creating a hub"; "One hub for
  accreditation readiness and program review."
- Per-accreditor marketing with the accreditor's own requirement vocabulary: HLC
  ("Criteria and Assumed Practices", "assurance reviews and comprehensive evaluations"),
  SACSCOC ("Principles of Accreditation", "self-studies and QEP"), MSCHE ("Standards for
  Accreditation and Requirements of Affiliation", self-study), WSCUC/NWCCU/NECHE
  ("Standards of Accreditation" / "criteria for accreditation"). The product is sold from
  the institution's seat against specific accreditors' requirements.
- FAQ definition: "helps institutions manage assessment planning, program review, and
  accreditation self-study processes in a centralized system … collaborate on reports,
  identify and track continuous improvement actions, align performance to strategic goals
  and accreditation standards, and organize supporting evidence in a structured workflow."
- Accreditation-readiness hub: "Centralize your work in a single hub with access to a
  shared evidence library and pre-built templates"; "document longitudinal program
  performance and actions taken to improve"; "Confidently manage multi-stage reviews.
  Take advantage of collaborative authoring tools and progress tracking to ensure
  compliance and showcase institutional quality."
- Compliance-certificate authoring: testimonial — "share evidence items, and customize our
  compliance certificate" (reaffirmation context); another testimonial: "our accreditation
  report submission" inside P&SS.
- Assessment machinery feeding accreditation: curriculum mapping ("Automate curriculum
  mapping to align learning outcomes with course content"; 7,000+ programs have created
  curriculum maps; 301K+ outcomes assessed; 2,000+ self-studies created; 3,000+ program
  reviews completed — vendor stats); LMS integrations (Canvas, Blackboard, D2L Brightspace)
  pulling rubric/assignment results; direct + indirect measures (course evaluations);
  close-the-loop narrative ("student learning outcomes - measures - actions taken -
  curricular or operational changes - adapted outcomes"); longitudinal comparison across
  reporting periods; disaggregation by attributes (major, gender, race, Pell) and
  modality-parity analysis.
- Non-academic units: CAS standards operationalized by student affairs/admissions/
  facilities; "recurring self-studies for every corner of your campus."
- Faculty qualifications: Faculty Success suite product — "Manage and report on faculty
  credentials … demonstrate qualifications."
- Users (FAQ): "institutional effectiveness offices, academic leaders, accreditation
  teams, program chairs, and faculty committees"; stakeholder cards for provosts/deans,
  IE teams, program assessment leads.
- AI: "AI-assisted analysis and recommended action items" (Assessment Catalyst Toolpack).
- Help Center structure: P&SS is a distinct help-center category; heritage categories
  Taskstream / LiveText / Tk20 / AMS / OAP confirm the product lineage of the classic
  institution-side accreditation/assessment tools consolidated into Watermark.

### Weave Education (institution side; evidence layer A)

From the root, solution, and accreditation-software pages:

- Positioning: "Innovative Accreditation Software"; "empowering higher education to
  prepare for their institutional and programmatic accreditations"; "Compile and generate
  accreditation reports for multiple accreditors in one accreditation software platform."
- Standards handling: "House regional, other institutional, or programmatic standards all
  for one price"; "Leave the update and maintenance of standards to us. We make sure you
  have the version you need" (vendor-maintained standards versions); "Employing up-to-date
  standards and criteria as your accreditation process evolves."
- Response authoring: "Focus on Content — Easily manage teams, access, formatting, and
  files to focus on writing responses to standards"; "Assign teams that can write, revise,
  and edit together in one place in real-time"; "clear expectations on the screen."
- Evidence: "Submitting and storing all types of standards-related evidence in an
  easy-to-navigate, unlimited data repository"; "team management, formatting, evidence
  alignment" named as the tedious parts accreditation software removes.
- Reports: "Live Reports — You run any type of report any time you need it, including
  stable and reliable formats with links"; "dynamic reports that are adaptable,
  version-controlled, consistently formatted, and professionally presented."
- IE integration: "Tie Institutional Effectiveness Together — integrate assessment,
  planning, and credentials easily from other areas of the platform to eliminate
  redundancy in report preparation."
- Feature set: Assessment (institution, course, & program); Accreditation (program and
  institution); Program Review; Strategic Plan Tracking; Unlimited customizable templates;
  Faculty Roster; permissions and workflow management; dashboards.
- Market posture: affordability ("at a cost any size institution can afford", "no hidden
  costs"), community ("Weave Community", "hundreds of institutions and programs", "3,200
  members", "500+ institutions"), created by campus professionals (founded 2006).
- Seat split: the accreditor seat is a separate product on a separate site (Weave
  Accreditation, weaveaccreditation.com) — the vendor itself splits the two seats.
- Cycle framing: marketing guide "The Four-Year Countdown Guide to Successful
  Accreditation … the before, during and after of your accreditation visit" (marketing
  material; confirms visit-centered cycle framing, not an operational standard).

### SPOL (institution side; evidence layer A)

From the root and accreditation module pages:

- Positioning: "SPOL brings planning, budgeting, assessment, credentialing, and
  accreditation into one connected system"; accreditation module: "Coordinate accreditation
  from response through submission."
- Continuous readiness: "Move from Periodic Preparation to Continuous Readiness";
  "embedding accreditation into everyday processes, so when it's time to report, the work
  is already done."
- Standards-to-work linkage: "SPOL connects accreditation standards directly to: Planning
  objectives, Assessment outcomes, Supporting documentation. So your narrative reflects
  actual performance, not retroactive assembly."
- Process management: "From developing responses to connecting supporting evidence and
  aligning work to standards, every part of the process is structured and coordinated
  within SPOL. As progress is made, reporting takes shape automatically"; "Reports that
  are organized and ready for submission."
- Cross-institution coordination: contributors in a shared system with clear
  responsibilities — "What they're responsible for / Where their work fits / When the work
  is due / How it contributes to the final report."
- Gap visibility: "a clear picture of progress and coverage across standards. So issues
  are addressed early, not during final review."
- Report production: "SPOL compiles your narratives and supporting evidence into a
  structured, complete report."
- Credentialing module = faculty qualifications ("Ensure faculty qualifications are
  clearly documented and defensible") — a vocabulary note: "credentialing" here is faculty
  qualification evidence, not student credentials.
- Customer base: colleges and universities of all sizes; ~two decades in market.

### eLumen (institution side, data-first; evidence layer A at positioning level)

From the root site:

- Current flagship: "Insights for Canvas Outcomes" — "a powerful suite of tools within the
  Canvas LMS that enables higher education institutions to turn Canvas into a
  comprehensive assessment platform."
- Capability list: manage learning outcomes and rubrics; curriculum mapping; assessment
  planning; juried (multi-rater) & external assessments; real-time and longitudinal data
  analytics and reporting; Comprehensive Learner Record (CLR) and micro-credentialing
  support.
- Course Central: "a new hub for course review, coordinator workflows, and faculty
  reflection … a new Course Coordinator role, structured reflection workflows, course
  review cycles."
- Accreditation appears downstream: case study describes faculty-centered assessment that
  streamlines "accreditation workflows" (Community College of Philadelphia case study
  blurb). No accreditation-specific feature list on the reachable pages — accreditation
  depth is positioning-level evidence only.
- Philosophy: assessment data captured where teaching happens (inside the LMS), feeding
  reporting; contrast with document-first self-study authoring.

### Nuventive (institution side; evidence layer A, prior pass)

- "Delivers planning and improvement software that helps higher education institutions…
  from strategic planning to accreditation, learning outcomes, program review, and more."
- Institution-facing improvement platform; accreditation is one initiative type inside a
  planning/measurement system.

## Cross-product Comparison

| Dimension | Watermark P&SS | Weave Education | SPOL | eLumen | Nuventive |
|---|---|---|---|---|---|
| Whose workflow | the institution/program (seeker) | the institution/program | the institution | the institution (assessment layer) | the institution |
| Central container | continuous-improvement hub (planning + assessment + program review + accreditation) | one system: accreditation + assessment + curriculum mapping + program review + strategic planning | connected system: planning/budgeting/assessment/credentialing/accreditation | Canvas-embedded outcomes/assessment suite | improvement platform (planning + accreditation + outcomes + program review) |
| Standards representation | per-accreditor use cases; pre-built templates; align performance to accreditation standards | regional/institutional/programmatic standards housed in one platform; vendor maintains versions | standards connected to planning objectives, assessment outcomes, documentation | not detailed on reachable pages | accreditation as initiative type |
| Compliance responses | "compliance certificate" customization; accreditation report submission | "writing responses to standards"; team-based real-time authoring | "developing responses … aligning work to standards" | not detailed | not detailed |
| Evidence | shared evidence library; repository; evidence items shared across areas | unlimited standards-related evidence repository | supporting documentation connected to standards | assessment data as evidence | not detailed |
| Assessment/curriculum machinery | curriculum maps, outcomes assessed, LMS pulls, direct+indirect measures, close-the-loop | assessment (institution/course/program), curriculum mapping | assessment outcomes linked to standards | outcomes/rubrics/mapping/planning/juried assessments (core strength) | learning outcomes |
| Program review | yes (3,000+ completed, vendor stat) | yes (feature) | yes (module) | course review cycles (Course Central) | yes |
| Planning linkage | strategic goals alignment; action plans | strategic plan tracking | planning objectives; budgeting module | not detailed | strategic planning (core) |
| Faculty qualifications | Faculty Success suite product | Faculty Roster | Credentialing module (faculty qualifications) | not detailed | not detailed |
| Progress/gap visibility | real-time dashboards; spot gaps | dashboards; insights at a glance | progress and coverage across standards; gaps early | longitudinal analytics | dashboards (prior pass) |
| Report production | collaborative authoring; multi-stage reviews; self-studies (2,000+, vendor stat) | live reports; version-controlled; formatted | compiles narratives + evidence into structured report | reporting/analytics | reports (prior pass) |
| Multi-accreditor | per-accreditor pages (6 regional named) + programmatic (CAEP case study) | regional + institutional + programmatic in one platform | not enumerated | not detailed | not detailed |
| Integrations | LMS (Canvas/Blackboard/Brightspace), course evals, Lightcast, CAS | within-platform IE integration | within-platform modules | native to Canvas | Canvas data integration (prior pass) |
| Philosophy | enterprise continuous-improvement hub | affordable simplicity + community | planning/budget-first continuous readiness | LMS-embedded data-first | improvement platform |

Key observations:

- **(B)** All five products serve the *institution/program* seat. None operates the
  accreditor's program. The accreditor seat is a separate product even within one vendor
  (Weave Education vs Weave Accreditation).
- **(B)** The recurring spine across all products: accreditor standards/criteria →
  standard-by-standard responses → evidence linked to standards → compiled accreditation
  report/self-study → maintained readiness across the cycle.
- **(B)** Education-specific evidence machinery is universal in the sample: curriculum
  mapping, learning-outcomes assessment (often LMS-fed), program review, faculty
  qualifications. This is what distinguishes the substrate from generic corporate
  compliance (§11).
- **(B)** "Continuous readiness" is a shared positioning idea (Watermark "always ready";
  SPOL "continuous readiness"; Watermark FAQ "year-round institutional effectiveness") —
  accreditation management is a standing state, not a one-shot report project.
- **(A)** The external accreditor makes the decision; none of the institution-side
  products records an accreditation decision. The institution's system ends at submission
  and follow-up readiness.
- **(A→B)** Multi-accreditor operation (institutional + programmatic simultaneously,
  sharing one evidence base) is explicit in Weave and Watermark.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (institution side of academic accreditation)

The smallest structure without which the product is no longer recognizable as academic
accreditation management for the *seeking institution*:

1. **External accreditor standards as the organizing structure** — the accrediting body's
   published standards/criteria/requirements are configured in the system (per accreditor,
   per cycle) and structure everything else. Without this → generic document management.
2. **Standard-by-standard compliance responses** — the institution/program (the accredited
   subject) authors and maintains a response/narrative against each requirement. Without
   this → assessment platform or planning tool.
3. **Evidence linked to standards** — documents and data (including assessment/outcomes
   data) attached as support for the responses. Without this → word processor.
4. **Compiled accreditation report** — responses and evidence are assembled into the
   submittable self-study/report for the accreditor. Without this → compliance checklist.
5. **Standing cycle with longitudinal continuity** — accreditation is a recurring state
   the institution maintains between external events (ongoing evidence, interim
   reporting, reaffirmation preparation), with the institution's history retained across
   cycles. Without this → a one-shot report project tool.

Removal tests: remove external standards → document management; remove responses →
assessment platform; remove evidence linkage → text editor; remove report compilation →
checklist tool; remove the standing cycle → a one-off report project.

Note: the accreditation *decision* is made by the external accreditor and is not an
in-system object on this side; the institution's system covers preparation, submission,
and between-event maintenance. (The decision-recording structure belongs to §25.)

### L1 — Common Mature Structure

- Central evidence library/repository: documents and data stored once, linked to many
  standards and reused across accreditors and cycles
- Curriculum mapping: learning outcomes mapped to courses/programs; gap identification
- Outcomes assessment machinery: assessment plans, measures (direct and indirect),
  results capture (often pulled from the LMS), close-the-loop action tracking
- Program review as a recurring, structured workflow
- Strategic-planning linkage: institutional goals/objectives connected to standards and
  evidence; action plans with owners and due dates
- Progress/coverage dashboards across standards; gap identification before deadlines
- Multi-stage internal review of drafts: assignments, deadlines, version control,
  collaborative authoring
- Multi-accreditor support: institutional (regional) and programmatic standards side by
  side, sharing one evidence base
- Faculty qualification/credential records (faculty roster) as accreditation evidence
- Roles and permissions: IE/accreditation office, liaisons, contributors (faculty/program
  chairs), leadership viewers
- Standards templates (pre-built per accreditor; customizable); vendor-maintained
  standards updates observed in one product, template configuration in others
- Longitudinal data: year-over-year comparison, trends across reporting periods
- Non-academic unit assessment (student affairs and operational units against their own
  standards)
- Integrations: LMS (rubric/assignment results), course evaluations, other campus systems

### L2 — Variant / Optional Structure

- AI assistance (analysis of findings, recommended action items)
- Budgeting linkage (planning→budget alignment in one vendor)
- Labor-market data packs; Comprehensive Learner Record / micro-credentialing support
- Disaggregation analytics (demographics, modality parity)
- Community/services posture (training, best-practice sharing) vs pure software
- Suite packaging (part of a multi-product higher-ed suite) vs standalone single system
- LMS-embedded execution (assessment lives inside the LMS) vs standalone platform
- Segment breadth: higher education dominant in the sample; K-12 school accreditation and
  non-US contexts exist in the market but were not verified in reachable sources
- Deployment: SaaS across the sample; on-prem posture not observed

### L3 — Vendor-specific (research notes only)

- Watermark: vendor stats (7,000+ curriculum maps, 301K+ outcomes assessed, 2,000+
  self-studies, 3,000+ program reviews); per-accreditor partner-percentage claims (e.g.,
  "over 60% of SACSCOC institutions"); Assessment Catalyst Toolpack (AI); heritage
  products (Taskstream, LiveText, Tk20, AMS, OAP); CAS standards pack; Lightcast labor
  market data pack; named LMS integrations; CODiE finalist badge.
- Weave: founded 2006; "3,200 members" / "500+ institutions" claims; unlimited repository;
  vendor-maintained standards versions; "Live Reports"; TX RAMP / CSA Star Level 1 /
  CHEA-linkage badges; separate accreditor product (Weave Accreditation) with member-based
  pricing; "Four-Year Countdown" marketing guide.
- SPOL: five-module connected system (planning/budgeting/assessment/credentialing/
  accreditation); "Capture → Connect → Validate → Show" method framing; Cordance
  Operations ownership; named community-college customers.
- eLumen: Insights for Canvas Outcomes; Course Central; Course Coordinator role; CLR and
  micro-credentialing support; Instructure podcast/white-paper marketing.
- Nuventive: dual-panel plan+resource UI; Canvas data integration marketing (prior pass).
- All testimonial claims (e.g., "50% reduction in preparation time", "80-hour weeks")
  are vendor testimonials, not operational facts.

## Vendor-specific Findings

See L3. None promoted to the canonical model.

## Rejected Findings

- **"Academic accreditation management = the accreditor's program system."** Rejected for
  this leaf: that seat is §25 (already documented). The market ships separate products per
  seat; every product sampled here serves the institution seat.
- **"Same as §11 generic compliance management."** Rejected as a merge: the accreditation
  spine is shared, but the evidence substrate (curricula, learning outcomes, faculty
  qualifications, program review vs corporate controls/policies), the governance (faculty
  committees, IE offices, accreditation liaisons), the deliverable (self-study report),
  and the vendor market (education specialists) differ. Recorded as a boundary issue, not
  silently merged.
- **"Same as Institutional Effectiveness Platform."** Rejected as a merge for now: IE is
  the institution's own planning/assessment/improvement loop; accreditation management is
  organized around an *external* accreditor's standards and cycle. Products converge
  heavily (same vendors, same platforms) — flagged for joint review rather than merged.
- **"Accreditation decision workflow is part of this Type."** Rejected: no sampled
  institution-side product records the accreditor's decision; that is §25 structure.
- **"Site-visit management is core."** Not observed in reachable sources (only marketing
  references to "before, during and after of your accreditation visit"); left as
  uncertainty.
- **"Student credentialing is part of this Type."** Rejected: vocabulary collision —
  vendor "credentialing" modules here mean faculty qualifications; student credentials
  belong to Digital Credential Platform.

## Boundary Findings

1. **vs §25 Accreditation Management (accreditor side)** — settled empirically: opposite
   seats of one relationship. Structural test: whose workflow does the system run — if the
   user is the body receiving submissions, reviewing, deciding, and maintaining accredited
   members, it is §25; if the user is the institution preparing responses/evidence for
   someone else's standards and maintaining its own readiness, it is this leaf. The market
   itself splits the seats into separate products (Weave Education vs Weave Accreditation;
   Watermark/Nuventive/SPOL/eLumen are all institution-side).
2. **vs §11 Accreditation / Certification Management** — same seat (the seeking
   organization), different domain substrate. Shared spine: external standard → mapped
   compliance records → evidence → assessment event → status/renewal. Differences: the
   evidence substrate here is educational (curriculum maps, learning-outcomes assessment,
   program review, faculty qualifications) rather than controls/policies; governance is
   faculty/committee-based; the deliverable is a self-study report; the vendor market is
   education-specific. Probable Variant or closely-related Type — flagged for joint
   review; consistent with the §11 document, which lists this leaf as "probable variant".
3. **vs §23 Institutional Effectiveness Platform (sibling)** — the strongest internal
   tension. The same products (Watermark P&SS, Nuventive, SPOL, Weave) market themselves
   as both "accreditation management" and "institutional effectiveness"; accreditation is
   one driver of IE work. Working distinction: this leaf is organized around the
   *external* accreditor's standards and cycle (standards → responses → evidence → report
   → reaffirmation); an IE platform is organized around the institution's *own*
   planning/assessment/improvement loop even where no accreditor is involved. In practice
   one product usually serves both; the leaves likely need a shared framing or a joint
   review — flagged, not unilaterally resolved.
4. **vs §23 Curriculum Management (sibling)** — curriculum management runs the curriculum
   change process and catalog; here curriculum mapping appears as *evidence* for
   accreditation. A curriculum product may feed this Type; it is not this Type.
5. **vs §23 Assessment Platform (sibling)** — assessment measures student learning; here
   assessment results are consumed as accreditation evidence. Data flows in; the
   accreditation spine (standards/responses/report/cycle) is what makes this Type.
6. **vs §23 Digital Credential Platform / Transcript Management** — no structural
   relationship: those manage student-facing credentials and records; this manages the
   institution's accreditation standing. Vocabulary collision only (also with vendor
   "credentialing" = faculty qualifications).
7. **vs Government Licensing Management** — voluntary recognition by an accrediting body
   vs government-issued permission to operate; different authority and object (consistent
   with §11's framing).

## Historical / Market-Sample Check (§24-style)

Would older, regional, or differently positioned products still fit the L0? Academic
accreditation and the self-study cycle long predate this software: institutions ran
accreditation preparation with paper binders, committees, and narrative documents. The
defining structure (external standards → standard-by-standard responses → evidence →
compiled report → standing cycle) is era-independent — a paper-era institution or a
homegrown SharePoint/committee process satisfies the same shape. The software lineage
confirms continuity: Watermark's help center still documents Taskstream, LiveText, and
Tk20 — the 2000s-generation accreditation/assessment platforms — as heritage products
alongside the current P&SS. The L0 does not depend on LMS integrations, dashboards, AI,
or any specific accreditor's framework. One skew is acknowledged: the reachable sample is
US higher-ed heavy (regional accreditors named per product); K-12 school accreditation and
non-US quality-assurance contexts were not verified and are recorded as variants of
uncertain coverage, not as structure.

## Uncertainties

1. Site-visit / external-review logistics inside the system (team visit coordination,
   visit-day evidence rooms) — not observed in reachable sources; may be handled offline,
   by the accreditor (§25 side), or in vertical products.
2. Substantive-change / interim reporting as a distinct in-product workflow — not directly
   observed in reachable sources (only generic "interim/annual reporting" on the accreditor
   side); not asserted.
3. Cycle cadences (years between reaffirmations) — not documented in reachable sources;
   deliberately not asserted (Weave's "Four-Year Countdown" is a marketing guide title).
4. K-12 and international coverage of the sampled products — unverified; the sample is
   US-higher-ed heavy.
5. eLumen's accreditation-specific depth — current reachable pages evidence the
   assessment/outcomes layer only; accreditation workflows appear at case-study level.
   Claims about eLumen limited accordingly.
6. Whether institutions ever run *mock review* workflows with external consultants
   in-system — plausible but not evidenced; not asserted.
7. Exact template/standards-update mechanics per vendor (who maintains versions) —
   observed explicitly only in Weave ("leave the update and maintenance of standards to
   us"); others show pre-built templates without stating maintenance posture.

## Final Synthesis

"Academic Accreditation Management" in the directory's education context is best
understood as the **institution-side accreditation application**: a college, university,
school, or academic program uses it to organize its accreditation work around an external
accreditor's published standards — maintaining standard-by-standard compliance responses,
linking evidence (documents plus curriculum/outcomes assessment data) to each requirement,
collaboratively authoring and versioning the self-study or compliance report, and keeping
the institution in a state of readiness across the recurring accreditation cycle, with
longitudinal history retained between events. The accreditor's decision is made outside
the system; this Type covers preparation, submission, and between-event maintenance. Its
machinery overlaps with institutional-effectiveness platforms (same vendors, shared
assessment/curriculum/planning infrastructure) and with generic compliance management
(§11); what makes it this Type is the external-standards spine with educational evidence
substrate and the maintained multi-accreditor cycle. The accreditor seat is a separate
Type (§25), and the market ships separate products for the two seats.
