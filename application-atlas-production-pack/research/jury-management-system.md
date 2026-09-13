# Research Notes — Jury Management System

Research date: 2026-09-08
Leaf: Jury Management System (DIRECTORY.md §24 Government, Public Sector & Civic)
Slug: jury-management-system

---

## Research Goal

Understand how real jury management systems work: what objects they maintain, how the summons-to-service lifecycle flows, what rules govern selection and relief decisions, what surfaces jurors and court staff use, and where this Type ends and neighboring Types (Court Case Management, Voter Registration, Election Management, Government Service Portal) begin.

## Initial Boundary (hypothesis before research)

- Core use: court-side administration of jury service — source list → summon → qualify → excuse/defer → pool → panel → service tracked → payment/proof.
- Users: jury office staff (jury commissioner / clerk of court); judges and courtroom staff requesting panels; jurors via self-service.
- Neighbors: Court Case Management System (case = object of record; jury often ships as a module), Voter Registration System (source list supplier), Government Service Portal (juror self-service is a surface of this Type), Election Management System (also draws on citizen lists for a civic process, but no ballots/precincts).
- Unknowns: whether standalone products exist vs module-only; how random selection is implemented and documented; service-term models; payment handling; panel-to-trial assignment mechanics.

## Research Questions

1. What is the object of record — juror, summons, panel? How do they relate?
2. How is the source/master list built and refreshed (voter rolls, driver lists, electoral register)?
3. What is the full summons lifecycle, including response duty and deadlines?
4. How does qualification work (statutory criteria, questionnaire)?
5. How do postponement/deferral and excusal work (limits, discretion, appeal)?
6. How does random selection work, and how is it made defensible?
7. How are panels matched to trials and how is service completed/tracked (term models, on-call, attendance, proof)?
8. What payment/expense machinery exists?
9. What self-service surfaces do jurors get?
10. Deployment shapes: CMS module vs standalone vs government-built vs national service?

## Representative Products

| Product | Operator / Vendor | Shape | Why chosen |
|---|---|---|---|
| Federal judiciary jury system (Jury Selection & Service Act machinery; eJuror; court jury offices) | Administrative Office of the U.S. Courts + 94 district courts | government-built, national | deep official process documentation (selection, qualification, eJuror) |
| U.S. District Court, Northern District of California jury office (CAND) | Federal district court | court-operated instance of the federal machinery | richest operational detail: on-call model, postponement/excusal rules, attendance/proof, pay, sanctions |
| HMCTS Jury Central Summoning Bureau + "Reply to a jury summons" service | UK Ministry of Justice / HM Courts & Tribunals Service | national central bureau + citizen digital service | international breadth; centralized bureau model; strong citizen-side documentation |
| Jury Systems Incorporated (JSI) | Independent vendor (Simi Valley, CA) | standalone dedicated jury management software + jury-list data services | proves the standalone-product pole of the market |

Considered and dropped: Tyler Technologies (tylertech.com returned 403 twice — unreachable, limitation recorded; market reports identify it as the largest court-software vendor, and court CMS suites commonly ship jury modules); Journal Technologies eCourt (site reachable but no jury-specific detail surfaced at product-page level — used only as suite-context evidence); juryplus.com (dead/unrelated site); NY State courts (403).

## Sources

Tier 1 (official operational documentation):

- US Courts (AO) — Jury Service hub: https://www.uscourts.gov/court-programs/jury-service (and sub-pages Juror Selection Process; Juror Qualifications, Exemptions and Excuses; Summoned for Federal Jury Service; Juror Pay listed but pay page not separately fetched)
- US District Court N.D. Cal. — Jurors: https://www.cand.uscourts.gov/jury/ (questionnaire, eJuror login, status/attendance, on-call model, postponement, excusal grounds, pay, sanctions, selection plan)
- GOV.UK — Jury service guide: https://www.gov.uk/jury-service (+ who-can-be-on-jury; delaying-or-being-excused; respond-to-the-summons; how-to-claim expenses pages linked in guide structure)
- GOV.UK — Reply to a jury summons service: https://www.gov.uk/reply-jury-summons (service run at https://reply-jury-summons.service.gov.uk)

Tier 2 (official vendor positioning):

- Jury Systems Incorporated: https://jurysystems.com/ (placeholder site: positioning + data-services description only; no product docs reachable)
- Journal Technologies eCourt: https://www.journaltech.com/ecourt (suite context only)

Unreachable: tylertech.com (403 ×2), nycourts.gov (403 ×1), jsijury.com (transport error; correct domain jurysystems.com reached instead), uscourts.gov ejuror subpage (404; eJuror documented via "Summoned for Federal Jury Service?" page instead).

---

## Product Observations

### 1. Federal judiciary jury machinery (USCourts.gov, AO) — evidence layer A

- **Jury wheel**: "A jury wheel is the database containing a specified number of names of district residents, with each county in the district represented in the jury wheel in proportion to its number of registered voters." Randomly drawn from the wheel "for possible qualification and summoning ... if they are deemed qualified and necessary for the court's trial schedule."
- **Source lists**: all courts use state voter lists; "if voter lists alone fail to provide ... a representative cross section", courts supplement with licensed drivers lists (28 U.S.C. §1861, Jury Selection and Service Act).
- **Qualification questionnaire**: randomly selected persons "are mailed a qualification questionnaire to complete and return to the court within 10 days or instructed to complete the questionnaire online on the court's eJuror page."
- **Qualification criteria** (federal): US citizen; 18+; resided in district ≥1 year; English ability; no disqualifying mental/physical condition (absent accommodation); not currently facing felony charges (>1yr); never convicted of a felony unless rights restored.
- **Exemptions** (bar service entirely): active-duty armed forces; professional fire/police; public officers.
- **Excuses**: permanent group excuses on request (e.g., over 70; served on a federal jury within past two years; volunteer firefighter/rescue/ambulance); temporary deferrals at summons time for "undue hardship or extreme inconvenience"; granted at court's discretion, not appealable; each of the 94 districts maintains its own procedures.
- **eJuror capabilities** (official list): complete the Juror Qualification Questionnaire online; update personal information; check when they need to report for service; submit a request for an excuse or deferral; select an alternate time to serve if deferral is granted.
- **Summoning**: each district court summons eligible citizens from counties in the district or its jury divisions.
- **Pool → panel**: qualified jurors who reported "is taken to the courtroom where the trial will take place"; voir dire questioning by judge/attorneys; some excused for cause; peremptory challenges.
- **Trial schedule linkage**: drawn for qualification and summoning "if they are deemed qualified and necessary for the court's trial schedule."

### 2. U.S. District Court N.D. Cal. jury office (CAND) — evidence layer A

- **Selection plan (court-documented)**: master jury wheel created from names drawn randomly from registered-voter lists (CA Secretary of State) and driver's license/ID lists (CA DMV); names then randomly drawn and sent summonses with eJuror instructions; qualified individuals "entered into a pool from which jurors are randomly selected for grand juries and trials"; "All selections are performed through an electronic data processing system designed to ensure pure randomness, giving each person an equal chance of being selected." One-step randomized process. (District maintains a published Jury Plan general order.)
- **eJuror login model**: 9-digit participant number from summons + first three letters of last name (as printed; corrections possible after login) + date of birth. No account creation.
- **Questionnaire flow**: verify/correct name, address, contact info → complete questionnaire (text boxes mandatory; "n/a" convention) → review → confirm → confirmation screen. Paper questionnaire still offered (2nd Notice includes paper version; online described as "most efficient").
- **Postponement**: "You may postpone your jury service one time for up to six months. Your request must be submitted at least two weeks before the start of your on-call period ... please be prepared to identify a two-week period within the next six months to which your service can be rescheduled." Online request possible after submitting the online questionnaire; email channel also available.
- **Excusal grounds (court-specific list)**: age 75+; reported for jury service in past 12 months (must have been present in court; certificate of attendance from the other court required); sole caregiver of preschool child or aged/infirm person (not employed outside home); volunteer firefighter / rescue squad / ambulance crew; resides >80 miles from courthouse (one-way mileage, requested on questionnaire); severe hardship with evidence (medical hardship requires provider letter). "Many requests for excuse – and any excuses related to financial hardship – may only be granted by a judge."
- **Service-term model**: "one appearance, or one trial" court; on-call period = 10 consecutive court days; check reporting instructions the day before the first scheduled date (via eJuror "Current Status" or 1-800 phone line); "You must continue calling for instructions until the message says your service is over." If not selected at the one appearance, service ends when jury selection completes; if selected, serve the length of the trial.
- **Attendance & proof**: "Attendance Letter" printable from eJuror showing dates appeared in person (updated the following month); jury office provides certificates of attendance on a daily basis; used as employer proof. On-call-only jurors cannot print attendance letters.
- **Pay**: attendance fee $50/day; round-trip mileage at IRS-authorized rate; parking validation at listed lots; bridge tolls; hotel reimbursement for distant jurors with prior authorization; Fee Waiver form if employer requires forfeiting the fee.
- **Sanctions**: failure to report may trigger an order to show cause; contempt under the Jury Selection Act; "penalty can be a fine of up to $1,000, up to three days imprisonment, a term of community service, or any combination."
- **Employment protection**: 28 U.S.C. §1875 (no discharge/intimidation for jury service) surfaced directly in juror FAQ.
- **Supplemental pre-screen**: court staff may send an additional SurveyMonkey questionnaire "to pre-screen qualified jurors before they appear at the courthouse."
- **Extra surfaces**: jury-office chat during business hours; scam warnings (juror scams targeting summoned citizens).

### 3. UK — HMCTS Jury Central Summoning Bureau + Reply to a jury summons (GOV.UK) — evidence layer A

- **Source & draw**: "Your name was chosen randomly from the electoral register."
- **Summons**: letter in the post; "you must respond within 7 days and confirm if you can attend." Fine up to £1,000 for not returning the form or not turning up; also for lying to avoid service.
- **Response channels**: online service (reply-jury-summons.service.gov.uk) or post (form + stamped envelope). Online requires juror number (on the letter) + name and address exactly as printed (corrections allowed); can reply for someone else with their permission; answers downloadable at the end.
- **Response options**: confirm attendance; ask to change the date; ask to be excused; request reasonable adjustments or other help at court.
- **Deferral**: "change the date ... to another date within the next 12 months ... You can only ask to change the date once"; suggest 3 possible dates; reasons examples (operation, exam, employer won't release, holiday, new parent, living abroad).
- **Excusal**: "exceptional circumstances" (serious illness/disability; full-time carer; new parent unable to serve any time in 12 months; living abroad); also if service done in last 2 years; proof may be requested (e.g., doctor's letter); if refused, deferral still possible.
- **Appeal**: write to the Head of the Jury Central Summoning Bureau with reasons + juror number + court + dates.
- **Eligibility**: 18–75 on start day; lived in UK/Channel Islands/Isle of Man ≥5 years since age 13; registered to vote. Disqualifications: on bail; custodial/community sentence in last 10 years; ever sentenced ≥5 years; sectioned under Mental Health Act; lacking capacity. "Even if you're disqualified, you must still respond to the summons within 7 days."
- **Bureau decides & confirms**: Jury Central Summoning Bureau sends confirmation letter with when/where; letter states whether deferral/excusal requests accepted; Bureau can change service location (e.g., moved house, at university).
- **Service shape**: jury of 12 for a criminal trial; "usually lasts up to 10 working days"; if trial shorter, "you may be asked to be a juror on other trials"; if likely longer, jury staff notify; first-day earlier arrival.
- **Expenses**: not paid for service itself; claim loss of earnings + travel (pages for employees / self-employed / not working); England & Wales travel only; no accommodation.
- **Support surfaces**: webchat, phone, email; assisted-digital support via a third-party group ("We Are Group") for those without internet access.

### 4. Jury Systems Incorporated (JSI) — evidence layer A (positioning only)

- Self-description: "the nation's leading provider of jury management software, serving courts across the country and beyond ... purpose-built technology. For decades, JSI has helped courts streamline juror administration, improve operational efficiency, and maintain accurate, defensible jury lists through advanced data processing and proprietary tools." Separate **Data Services** offer: "merge, scrub, and optimize your jury lists."
- Confirms: standalone dedicated jury management software is a real market category; jury-list data hygiene is a distinct service need; "defensible jury lists" echoes the randomness/audit requirement.
- No product feature documentation reachable (site is a redesign placeholder) — no feature claims drawn from JSI.

### 5. Journal Technologies eCourt — suite context only

- Court case management suite (appellate/superior/municipal/traffic/probate/drug courts; US/Canada/Australia). Product page does not surface jury functionality; used only to evidence that court software suites exist into which jury management commonly packages as a module. No jury claims drawn from it.

---

## Cross-product Comparison

| Dimension | US federal machinery (AO + CAND) | UK HMCTS bureau | JSI (vendor) | Evidence |
|---|---|---|---|---|
| Object of record | summoned citizen per service event (participant number) | summoned citizen per summons (juror number) | "juror administration" / jury lists | B |
| Source list | voter lists (+ driver/ID lists as needed), merged into "master jury wheel"; counties proportional to registered voters | electoral register | vendor data services "merge, scrub, optimize" lists | B |
| Random selection | random draw from wheel; pool → random selection for grand juries/trials; "electronic data processing system designed to ensure pure randomness, equal chance" | random from electoral register | "accurate, defensible jury lists" | B |
| Summons as legal order | yes; contempt/§ sanctions for failure | yes; up to £1,000 fine | — | B |
| Mandatory response with deadline | questionnaire within 10 days (or online) | reply within 7 days | — | B |
| Qualification determination | statutory criteria + questionnaire | statutory eligibility + must respond even if disqualified | — | B |
| Discretionary relief | postponement (once, ≤6 months, ≥2 weeks notice, choose window) + excusal grounds, some judge-only | deferral (once, within 12 months, suggest 3 dates) + excusal (exceptional; proof; appeal) | — | B |
| Pool / service term | on-call 10 court days; one appearance or one trial | up to 10 working days; multiple shorter trials | — | B (both bounded terms; models differ) |
| Reporting instructions | check status day before (portal or phone line), repeat until service over | confirmation letter states when/where | — | A each; B jointly |
| Attendance & proof | attendance letter (eJuror); daily certificates; employer fee waiver | confirmation letter brought to court | — | B |
| Pay/expenses | $50/day + IRS mileage + parking (fee-based) | no pay; expense claims (earnings, travel) | — | B |
| Relief decision-maker | court/jury office; some categories judge-only | Jury Central Summoning Bureau; appeal to its head | — | B |
| Self-service portal | eJuror (questionnaire, status, requests, info updates, proof docs) | Reply to a jury summons service (confirm/defer/excuse/adjustments) | — | B |
| Penalty scale | up to $1,000 / 3 days / community service (contempt) | up to £1,000 fine | — | B |
| Standalone vs module | government-built national system + per-court offices | national bureau + digital service | standalone vendor product | B |

Stable across the whole researched sample (the structure of the Type):

```text
Civic source list  →  random draw  →  summons (legal order, mandatory response)
   →  qualification determination  →  discretionary relief (deferral / excusal)
   →  qualified pool for a bounded service term  →  reporting instructions
   →  appearance / attendance tracked  →  panel drawn for a real proceeding
   →  service completed  →  proof of service + payment/expenses
   →  service history retained (feeds future relief rules)
```

---

## Canonical Model

### Level 0 — Defining Invariant

Four jointly-held structures. Removing any one stops the system from being a jury management system:

1. **The summoned civic participant of record** — a person record drawn from a civic source population (voter/electoral/driver registers), maintained per summoned service event with identity/contact data and a summoning identifier (participant/juror number). *Remove → a mailing list / generic notification system.*
2. **The summons as a legally binding call with mandatory response** — an official order naming when/where (or the qualification duty), carrying a response deadline and statutory penalties for non-response or false response. *Remove → volunteer recruitment or survey sampling.*
3. **Qualification and relief adjudication** — determination against statutory eligibility criteria, plus discretionary, bounded decisions to postpone (deferral to an agreed later window) or excuse entirely (hardship/eligibility grounds), recorded against the person. *Remove → pure notification; no eligibility work, "management" gone.*
4. **Random selection into panels bound to real proceedings, with service tracked to completion** — qualified available persons are randomly assembled into panels delivered to actual court proceedings, and attendance/service is recorded and discharged with proof. *Remove random selection → assignment system; remove proceedings-binding → survey panel; remove tracking → summons blaster.*

Jointly-held is load-bearing: (1) alone = mailing list; (2) without 1 = process serving; (3) without 1+2 = eligibility questionnaire; (4) without 1–3 = a raffle.

Historical check (paper era): a clerk drawing names from a rotating drum ("wheel"), typing summonses, receiving questionnaires by post, card files of jurors, typed panel lists, handwritten attendance registers, check payments — all four invariants hold. Online portals, text reminders, and electronic randomness are implementations, not the invariant. Jurisdictions without jury trials (much of the world, lay-judge systems) genuinely lack this Type — the Type exists where the jury summons exists.

### Level 1 — Common Mature Structure

- Master jury wheel assembled from multiple source lists, with proportional composition across counties/districts and periodic refresh; list merge/scrub/data services as a distinct task.
- Response-deadline enforcement and second-notice handling for non-responders.
- Juror self-service portal: login by summons identifier + identity attributes (no account), questionnaire completion with info correction, relief requests, status/reporting instructions, downloadable proof documents.
- On-call / reporting-instructions management (night-before check, repeat until discharged; phone IVR line as parallel channel).
- Attendance check-in and proof-of-service documents (attendance letters / certificates) for employers.
- Juror payment or expense machinery (fees, mileage, parking; or expense claims) and fee-waiver handling.
- Correspondence generation (summons, notices, confirmation/decision letters) across mail + online + phone channels.
- Statistics and operational reporting for the court.
- Supplemental pre-screening questionnaires before appearance (some courts).

### Level 2 — Variant / Optional Structure

- Service-term model: one appearance/one trial; on-call window (e.g., 10 court days in one court); fixed term (e.g., up to 10 working days with reassignment to shorter trials) — jurisdictional policy, not invariant.
- Payment model: daily attendance fee + mileage (US pattern) vs no-pay expense reimbursement (UK pattern).
- Organizational shape: module of a court CMS suite vs standalone product vs government-built national system vs centralized national bureau serving many courts (UK) vs per-court/per-county offices (US).
- Panel types: petit juries vs grand juries handled by the same machinery.
- Location transfer rules, reasonable-adjustment/accommodation requests, assisted-digital support, multilingual provision.
- Penalty specifics (fines, contempt, imprisonment windows) — statutory per jurisdiction.
- Deferral/excusal numeric limits (once-per-period, advance-notice windows, suggested-date counts) — policy parameters that vary.

### Level 3 — Vendor-specific (Research Notes only)

- JSI's proprietary jury-list data processing tools and "merge/scrub/optimize" service packaging.
- Tyler Technologies' jury module packaging inside its court suite (unreachable — no detail recorded).
- CAND's SurveyMonkey pre-screening step (court-specific practice built atop the federal machinery).
- Vendor portal naming, exact login schemas, internal workflow labels — not sampled (docs unreachable).

---

## Vendor-specific Findings

- All observed concrete parameter values (10-day questionnaire window, 7-day UK reply window, $50/day, £1,000 cap, 6-month/12-month deferral ceilings, 80-mile rule, 10-day on-call, 75+/70+ age thresholds, 2-year/12-month recent-service excusals) are single-jurisdiction facts — kept product/jurisdiction-specific here and in the final document as clearly attributed examples of "varies by jurisdiction".
- No vendor feature documentation was reachable; nothing in the final document depends on vendor-internal claims.

## Boundary Findings

1. **vs Court Case Management System (CCMS)** — the most important boundary. CMS object of record = the case (parties, docket, hearings, filings, outcomes). Jury system object of record = the summoned citizen and their service event. Jury machinery binds to proceedings (panels requested for trials) and may ship as a module inside a CMS — same packaging pattern as leave-absence inside HRIS and injury-tracking inside athlete management. Remove jury machinery → CMS remains a CMS; keep jury loop without case handling → still this Type (UK bureau and standalone JSI prove the module-independent pole). The leaf remains a definable Type, not a mere capability.
2. **vs Voter Registration System** — the register is a *source list input*. Registration systems maintain the voter's registration; jury systems consume lists and manage summoned service. Directional test: remove summoning from a registration system → still a registration system.
3. **vs Election Management System** — both draw citizen lists into civic processes. Elections manage ballots/contests/precincts/results; jury manages summons/qualification/trial service. The existing election-management-system document already cross-references this leaf as "civic-process neighbor ... involves no ballots or election geography" — consistent.
4. **vs Government Service Portal** — the juror portal is one surface of this Type; the service portal is a generic channel across many services. The operational system of record (lists, summonses, pools, panels, attendance) belongs here.
5. **vs Public Sector Case Management** — failure-to-appear may escalate into an enforcement matter (order to show cause), but that lives in case-management territory; this Type ends at recording the failure and informing the escalation.
6. **vs Workforce/Employee Scheduling** — false friend: pools, assignments, attendance, stand-in notices resemble shift scheduling, but the governed population is summoned citizens under statutory authority, selection must be random, and relief is discretionary adjudication — not a labor relationship.

## Uncertainties

- Vendor-side staff interfaces (panel assembly screens, pool management UIs, payment processing) could not be directly documented — no vendor help centers reachable (Tyler 403, JSI placeholder). Staff-side structure is inferred from the juror-visible artifacts each system must produce (summonses, decision letters, attendance letters, certificates, fee payments) plus vendor positioning. Assertion strength kept moderate for staff-facing detail.
- Whether large court-CMS vendors (Tyler-class) package jury management as a named module is market knowledge not directly verified here; the final document states suite-module packaging as "common" based on the category's existence and court-software structure, not on a specific vendor page.
- Jury payment processing depth (treasury integration, 1099-class reporting) unverified — kept out of the final document beyond fee/expense existence.
- Non-US/non-UK jury jurisdictions (Canada, Australia, Ireland, NZ) not sampled; the two sampled regimes anchor the Type but regional variation (e.g., Scotland's separate rules per GOV.UK pointer) is noted, not detailed.

## Final Synthesis

A Jury Management System is the court's operational system of record for jury service. Its world is organized around summoned citizens: a civic source list is randomly drawn into a master wheel/list; summonses issue as legally binding orders with mandatory response; responses trigger qualification determination and bounded discretionary relief (deferral/excusal); qualified available citizens form pools for bounded service terms; reporting instructions marshal them day by day; panels are randomly assembled for real proceedings; attendance and service are tracked to discharge, producing proof-of-service documents and payment/expense handling; service history is retained and feeds future relief rules. Randomness and defensibility are statutory requirements that shape the whole system, and the citizen-facing portal plus the staff back-office plus the mail/phone channels together form one operational loop. It is distinct from the case management system (which owns the case, not the summoned citizen), from voter registration (source-list supplier), and from election systems (different civic process). The Type survives paper-era and digital-era implementations unchanged in structure; it exists only where the jury summons exists.
