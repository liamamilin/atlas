# Jury Management System

## Overview

A **Jury Management System** is the court-operated system of record for administering jury service: it maintains lists of citizens eligible to be called, randomly draws and summons them, determines who is legally qualified to serve, adjudicates requests to postpone or be excused, assembles qualified citizens into pools and random panels for real trials, and tracks attendance and service through to discharge, proof, and payment.

It solves a problem no other court software owns: converting a jurisdiction's general population — via civic registers such as voter rolls or the electoral register — into the specific, legally defensible groups of people who sit in courtrooms as juries. The work is bound by statute at every step: randomness of selection, who must respond to a summons, who can be excused, and what happens to those who ignore the summons.

The defining core is small: a summoned citizen held as a record, a legally binding summons with mandatory response, qualification-and-relief decisions on that call, and random selection into panels for actual proceedings with service tracked to completion. Everything commonly associated with modern implementations — online juror portals, text reminders, electronic lottery systems, centralized national bureaus — is a current-market realization, not part of the definition. A clerk drawing names from a rotating drum, mailing typed summonses, and keeping handwritten attendance registers runs the same system.

When the center of gravity shifts to the case itself (parties, dockets, hearings, filings), the product is a Court Case Management System — jury management commonly ships as a module inside such suites, but its object of record is the summoned citizen, not the case.

## Users & Context

**Primary operators — the court's jury office staff** (jury commissioner's office, clerk's office, or a centralized summoning bureau): build and refresh source lists, generate and send summons batches, process responses, decide postponement and excusal requests, manage the daily pool of reporting jurors, assemble and deliver panels to courtrooms, record attendance, produce proof-of-service documents, and handle juror payments or expense claims. Their work is deadline-driven and calendar-driven: each trial date requires a panel of a certain size; each summons carries a response deadline.

**Requesting consumers — judges and courtroom clerks**: they consume panels sized to upcoming trials; the jury system's output (a randomly drawn group of reporting jurors) is their input to the trial process.

**Served population — summoned citizens (jurors)**: they receive a summons, must respond by a deadline, complete a qualification questionnaire, may request a change of date or an excusal, check reporting instructions before attending, attend and check in, possibly serve on a trial, and receive payment or claim expenses. Most interact with the system only a few times in their lives, under a legal obligation they did not choose.

The context is public-sector and jurisdiction-bound: a federal district, a state county court, or — in centralized models — a national bureau serving many courts. Physical courthouse operations (check-in desks, assembly rooms) surround the software.

## Core Model

The system's world is organized around **the summoned citizen**, moving through one lifecycle under court authority:

```text
Civic source list (voter/electoral/driver registers)
   ↓ random draw
Prospective juror record  ── carries ──→  summoning identifier (participant/juror number)
   ↓
Summons (legal order: when/where or qualification duty, response deadline)
   ↓ response (mandatory, by deadline)
Qualification determination (statutory criteria questionnaire)
   ↓ discretionary relief decisions
Postponement / Excusal  (or: remain qualified)
   ↓
Qualified pool for a bounded service term
   ↓ reporting instructions (checked day by day)
Appearance → attendance recorded
   ↓ random selection
Panel delivered to a real proceeding (trial or grand jury)
   ↓ voir dire is the court's process, not the system's
Served / released → service completed
   ↓
Proof of service + payment/expenses + retained service history
```

**The source list (jury wheel)** — the substrate. A merged, periodically refreshed list drawn from civic registers: voter lists, supplemented where needed by driver or ID-card lists to ensure a representative cross section; in England and Wales, the electoral register alone. In US practice the merged list is called the *master jury wheel*, with counties represented in proportion to their registered voters. Its defining property is not the medium (a rotating drum historically, a database today) but that names enter it from civic registers and leave it only by random draw.

**The prospective juror record** — a person record created when a name is drawn, carrying identity and contact data (correctable by the citizen), the summoning identifier used to log into self-service, the summons and its status, qualification outcome, relief decisions, and — across repeated calls — accumulated service history (which itself feeds later relief rules, such as recent-service excusals).

**The summons** — the system's central artifact: a legally binding official order telling a citizen to qualify and/or appear on a date, carrying the response deadline and the warning of penalties. Summonses are generated in batches against upcoming service terms and delivered by post in all researched systems, with online response as the modern channel.

**Qualification and relief decisions** — the adjudication layer. Qualification is determination against statutory criteria (age, residence, citizenship, language, criminal-history and capacity disqualifications) via a questionnaire. Relief is discretionary and bounded: *postponement* moves service to an agreed later window (typically once, within a statutory ceiling, sometimes requiring suggested alternative dates); *excusal* removes the obligation entirely (hardship, caregiving, occupational or recent-service grounds), sometimes only grantable by a judge. Every decision is recorded against the person and communicated back by letter or portal status.

**The pool and the service term** — qualified, available citizens are held as a pool for a bounded term: an on-call window during which they check reporting instructions daily and appear only if needed; a fixed term during which they may be assigned to several short trials; or a single appearance ("one appearance or one trial" is a common US county policy). The term model is jurisdictional policy, not the system's invariant.

**The panel** — the system's output event: a randomly selected group drawn from the reporting pool and delivered to a specific courtroom for a specific proceeding. Voir dire questioning, challenges, and the swearing of the jury belong to the court process the system feeds; the system's responsibility ends at producing the defensible random panel and recording what its members did.

**Attendance, proof, and payment** — check-in records each appearance day; proof-of-service documents (attendance letters, certificates) are produced for employers; fees and mileage or expense claims are processed; the completed service is written to the person's history.

## How It Works

### The summons lifecycle (the defining loop)

```text
Refresh source lists from civic registers
→ merge and de-duplicate into the master list (jury wheel)
→ randomly draw names for an upcoming service term
→ create juror records; generate and mail summonses
→ citizen responds by the deadline (online or paper):
     confirm availability
     or request postponement (suggesting acceptable later dates)
     or request excusal (with supporting evidence)
     or request accommodations
→ follow up non-responders (second notices; penalties loom)
→ adjudicate qualification questionnaire against statutory criteria
→ adjudicate relief requests (some categories reserved to a judge)
→ qualified + available citizens enter the pool for the term
```

### Pool operations (the daily loop)

```text
Juror checks reporting instructions the day before (portal or phone line)
→ either told to appear, or told to remain on call, or told service is over
→ on appearance: check-in, orientation, attendance recorded
→ panels randomly assembled from the reporting pool, sized to the day's trials
→ panel delivered to the courtroom; voir dire; some members seated, others released
→ if not seated: back to the pool or discharged, per the term policy
→ daily attendance accumulates until the term ends and service is discharged
```

### Completion

```text
Service ends (term expired, one appearance done, trial finished, or excused)
→ proof documents issued (attendance letter / certificate for employers)
→ payment processed (fee + mileage) or expenses claimed and reimbursed
→ service history retained; recent service feeds future relief eligibility
```

Two loops run continuously and asynchronously: the summons lifecycle advances in month-scale batches against future terms, while pool operations turn over daily. The system's skill is keeping both supplied: enough qualified jurors in the pool to feed the trial calendar, without summoning more citizens than necessary.

## Interfaces

### Staff back-office (jury office)

- **Source list management** — importing register extracts, merging and de-duplicating lists, refreshing the wheel. Vendors treat list hygiene as a distinct capability ("defensible jury lists"), and list data services exist as a market in itself.
- **Summons generation and response processing** — batch creation against upcoming terms, delivery tracking, queues of responses awaiting adjudication, second-notice handling.
- **Qualification and relief adjudication** — questionnaire outcomes, postponement and excusal decision screens with statutory reasons and evidence attachments; decision letters.
- **Pool and panel management** — today's reporting pool, panel assembly with randomness controls, panel lists delivered to courtrooms.
- **Attendance and payment** — check-in records, attendance registers, fee/mileage computation or expense claim processing.
- **Correspondence and reporting** — summons, notice, and decision letters across mail and portal channels; operational statistics for the court.

### Juror self-service portal

The citizen's entry point, typically requiring no account: the summoning identifier from the summons (a participant or juror number) plus identity attributes (name as printed, date of birth). Capabilities common to researched systems:

- complete the qualification questionnaire, correcting contact details along the way
- request postponement or excusal, with reasons and evidence
- check current status and reporting instructions (repeatedly, across an on-call period)
- download proof documents and confirmation of answers
- update personal information

The portal coexists with paper and telephone channels — paper questionnaires and reply forms remain available, and phone lines deliver reporting instructions to jurors who cannot or do not go online. Assisted-digital support (a help desk for those without internet access) appears in the national-service model.

### Mail and phone as first-class channels

The summons itself, decision letters, and proof documents are physical artifacts by default; postal reply with a stamped envelope, and call-in numbers for reporting instructions, remain structural parts of the operation rather than legacy leftovers.

## Important Rules / Behaviors

**Randomness is a statutory requirement, not a feature.** Selection must be random from a fair cross section of the community (the US Jury Selection and Service Act makes this explicit); systems document their randomness machinery — proportional composition of the wheel, randomized draws, "pure randomness, equal chance" — because defense of the process is a legal exposure. This shapes the core more than any other rule: panel assembly is a lottery with an audit trail, not an assignment optimization.

**Response to a summons is mandatory and enforceable.** Non-response or false response is itself an offense: fines (a £1,000 cap in England and Wales), contempt proceedings with fines, brief imprisonment, or community service (in one researched federal court). The system therefore tracks response status aggressively and generates escalation artifacts (second notices, orders to show cause).

**Relief is discretionary, bounded, and recorded.** Postponement is typically limited to once per summons within a statutory ceiling (researched examples: up to six months in one US court, within 12 months in England and Wales, with required suggested dates and advance notice). Excusal requires statutory grounds and evidence; certain categories (notably financial hardship) may be grantable only by a judge. Decisions can be appealed (in England and Wales, to the head of the summoning bureau). Disqualified citizens must still respond to the summons — the response duty is independent of eligibility.

**Disqualification is statutory and specific.** Criteria lists (age bands, residence duration, citizenship, language ability, criminal history, mental-health and capacity grounds; occupational exemptions such as active-duty military and professional police/fire) come from statute and differ per jurisdiction — the system encodes them as questionnaire logic, never invents them.

**Service terms are policy, and policies differ.** One appearance/one trial, on-call windows, and fixed terms coexist across jurisdictions; the system must be configurable to the local model. Exact limits (window lengths, deferral ceilings, distance rules, age thresholds) are jurisdictional parameters, not industry constants.

**The service record is a legal record.** Attendance must be provable (certificates, attendance letters) because jurors rely on them for employment protection (statutes in the US prohibit employer retaliation for jury service); records are retained and service history feeds later excusal rules. Payment handling (fees, mileage, expense claims, fee waivers where employers require forfeiting the fee) rides on the attendance record.

**Jurors are not staff.** Despite superficial resemblance to shift scheduling, no labor relationship exists; the population is compelled, selection must be blind, and "scheduling" is really randomized marshalling under court authority.

## Variants

- **Suite module vs standalone product vs government-built** — jury management commonly ships as a module of a court case management suite; dedicated standalone vendors also serve the category; and in the US federal judiciary and England and Wales the systems are built and run by the courts themselves.
- **Per-court vs centralized bureau** — US districts and counties typically run their own jury offices over their own lists; England and Wales runs a national Jury Central Summoning Bureau that summons for courts across the jurisdiction and can even relocate a citizen's service.
- **Service-term model** — one appearance/one trial (common in US county courts), on-call windows with day-by-day reporting instructions, or fixed terms with reassignment across several short trials.
- **Payment model** — per-day attendance fee plus mileage (US pattern) versus no pay with reimbursed expenses (England and Wales pattern).
- **Panel types** — the same machinery typically serves both petit (trial) juries and grand juries where both exist.
- **Jurisdictional scope** — the Type exists only where jury trials exist; jurisdictions using lay judges or bench trials have no counterpart system.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Court Case Management System | owns the case (parties, docket, hearings, filings, outcomes); jury management binds to proceedings but its object of record is the summoned citizen, not the case; the two are often sold together, and jury machinery ships as a CMS module |
| Court E-filing Platform | filers and documents entering the court's case record; no summoned population, no selection duty |
| Voter Registration System | maintains the citizen's registration — a *source list* this Type consumes; remove summoning from either and the other stands |
| Election Management System | also draws on citizen lists for a civic process, but manages ballots, contests, precincts, and results — no summons, qualification, or trial service |
| Government Service Portal | the juror portal is one surface of this Type; a service portal is a generic channel, not the operational system of record |
| Public Sector Case Management | a juror's failure to appear may escalate into an enforcement matter handled there; this Type records the failure and informs the escalation |
| Workforce / Employee Scheduling | shares pool/assignment/attendance mechanics, but governs willing staff under a labor relationship; jury service is compelled, randomly selected, and adjudicated |

The most important boundary is with the Court Case Management System. Both are court software and both touch trials, so they are frequently bought together; the structural test is the object of record — summoned citizen and service event versus case and docket.

## Representative Products

- **Federal judiciary jury machinery (US)** — the Jury Selection and Service Act process operated by the 94 district courts with the national eJuror self-service component (Administrative Office of the U.S. Courts); documented here via USCourts.gov and the U.S. District Court for the Northern District of California's jury office.
- **HMCTS Jury Central Summoning Bureau + "Reply to a jury summons" (England & Wales)** — the national centralized bureau and its citizen-facing digital service.
- **Jury Systems Incorporated (JSI)** — long-standing standalone vendor of jury management software and jury-list data services serving courts "across the country and beyond".

Court-software suites from major court-vendor ecosystems (e.g., the large court CMS vendors) commonly package jury management as a named module; this packaging pole is described from category structure rather than from reachable vendor documentation.

## Sources

Research date: **2026-09-08**

- US Courts (Administrative Office of the U.S. Courts) — Jury Service: https://www.uscourts.gov/court-programs/jury-service (incl. Juror Selection Process; Juror Qualifications, Exemptions and Excuses; Summoned for Federal Jury Service?)
- U.S. District Court, Northern District of California — Jurors: https://www.cand.uscourts.gov/jury/
- GOV.UK — Jury service guide: https://www.gov.uk/jury-service (incl. Who can be on a jury; Ask to change the date or be excused; Respond to the summons)
- GOV.UK — Reply to a jury summons: https://www.gov.uk/reply-jury-summons
- Jury Systems Incorporated: https://jurysystems.com/
- Journal Technologies (eCourt, suite context): https://www.journaltech.com/ecourt
- 28 U.S.C. §1861 (Jury Selection and Service Act) and §1875 (employment protection), as referenced by the official sources above

> Sourcing limitation: vendor product documentation for major court-software vendors was not reachable from the research environment (one vendor's site returned access errors; the dedicated jury-vendor's site is a redesign placeholder). Staff-facing interface structure is therefore documented at the level the systems' own official outputs (summonses, decision letters, attendance letters, fee rules, selection plans) make certain, with assertions kept correspondingly moderate. Jurisdiction-specific numbers quoted (deadlines, fee amounts, fine caps, deferral ceilings) are direct observations from the researched systems and are presented as examples of jurisdictional variation, not industry constants.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical (paper-era) check are recorded in the paired Research Notes.
