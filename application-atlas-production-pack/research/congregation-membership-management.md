# Research Notes — Congregation Membership Management

Research date: 2026-09-07
Slug: congregation-membership-management
Directory leaf: Congregation Membership Management (§25 Nonprofit, Membership & Religious Organizations)

## Research Goal

Resolve the joint-review flag left by the church-management-system-chms pass: is "Congregation Membership Management" a distinct Application Type, or merely the membership slice of a ChMS? If distinct, establish its defining core, standard capabilities, variants, and boundaries against ChMS, generic Membership Management System, Member Directory, and the processed §25 siblings (church-giving-platform, church-communication-platform).

## Initial Boundary

Core guess: the membership-roll slice of church software — people records organized into households, a recorded membership status per person, directories/lists/reports derived from the roll — which exists both as standalone products/modules and as the record core of full ChMS products.

Likely nearest neighbors:

- Church Management System / ChMS (§25, processed) — closest; flagged this leaf as probable partial-overlap and requested joint review
- Membership Management System (§25 sibling, unprocessed) — generic-membership sibling
- Member Directory (§25 sibling, unprocessed) — possible capability slice
- Church Giving Platform (§25, processed) — meets at the giver record
- Church Communication Platform (§25, processed) — meets at the audience substrate
- Nonprofit CRM / Donor Management System (§25) — structurally similar record grammar
- Association Management System / AMS (§25, processed) — adjacent market

Prior sibling findings to respect:

- church-management-system-chms: "membership records, households, and directories are one slice of the ChMS record core… candidate outcomes are consolidation (membership as the record-core slice of ChMS) or a distinct narrow Type if standalone membership-only products with no participation machinery surface."
- church-giving-platform: ChMS owns people/membership/ministry life; the giving platform owns collection channels + contribution records; they meet at the giver record.
- church-communication-platform: the comms loop runs on the church's people records as audience substrate; remove the sending loop → ChMS/records side.

## Research Questions

1. Do standalone membership-only products or modules exist — roll without participation machinery (check-in, giving collection, groups, events)?
2. What is the roll's structure: person record, household/family, membership status?
3. What membership lifecycle events exist (join, transfer, removal; Catholic registration and sacramental milestones)?
4. What outputs does the roll feed (directories, labels, lists, reports, diocesan/denominational reporting)?
5. What is the member-facing surface (portal, directory opt-in, self-update)?
6. Where does attendance fit — machinery (check-in) vs light signal recording?
7. Where do giving, check-in, groups sit — inside this Type or in neighboring Types?
8. Historical check: parish registers, paper membership rolls, letters of transfer, 1990s office membership databases.
9. Boundary vs generic Membership Management System and vs Member Directory.

## Representative Products

| Product | Position in market | Why sampled | Evidence tier |
|---|---|---|---|
| Planning Center People | Standalone free membership database of a modular suite; explicitly usable on its own | The cleanest standalone "roll without participation machinery" realization; strongest documentation | Tier 2 product page + Tier 1 help article (custom fields, fetched in ChMS pass) |
| Church Windows (Membership module) | Desktop-heritage suite; modules purchasable individually | Purchasable standalone membership module — the module-level realization | Tier 2 (homepage + dedicated Membership module page) |
| ParishSOFT Families | Catholic parish/diocese heritage; census/family-directory module of the Family Suite | Denominational census/sacramental pole; family-as-registration-unit | Tier 2 (Families page; homepage from ChMS pass) |
| Breeze ChMS (Tithe.ly) | Lightweight people-centric all-in-one | The blurred pole: roll at the center but check-in/giving bundled | Tier 2 homepage |
| Servant Keeper, Churchteams | Full ChMS suites | Boundary anchors showing where the roll dissolves into ChMS | Tier 2 homepages |

Sample rationale: three standalone realizations (product, purchasable module, suite module) across three customer philosophies (modern modular SaaS, desktop heritage, Catholic denominational), plus two boundary anchors at the blurred pole. Customer tiers span small traditional churches to dioceses.

## Sources

All fetched 2026-09-07 unless noted:

- Planning Center People — https://planning.center/people (Tier 2)
- Planning Center People help: Manage custom fields — https://pcopeople.zendesk.com/hc/en-us/articles/204263134 (Tier 1; fetched in the ChMS pass, 2026-09-07)
- Church Windows — https://www.churchwindows.com/ (Tier 2)
- Church Windows Membership module — https://www.churchwindows.com/membership/ (Tier 2)
- ParishSOFT Families — https://www.parishsoft.com/families/ (Tier 2; /family-directory/ 404'd first, recovered via /families/)
- ParishSOFT homepage — https://www.parishsoft.com/ (Tier 2; fetched in the ChMS pass)
- Breeze ChMS — https://www.breezechms.com/ (Tier 2)
- Servant Keeper — https://www.servantpc.com/ (Tier 2)
- Churchteams — https://www.churchteams.com/ (Tier 2)

Unreachable this pass (recorded per source-access limitation rules):

- pcopeople.zendesk.com search and category listings — JS-rendered, no article content returned (1 attempt)
- pcochurchcenter.zendesk.com (Church Center help) — root rendered only featured sections, no directory/profile article content (1 attempt)
- https://www.breezechms.com/help — 404 (1 attempt); Breeze evidence stays homepage-tier

Sibling research reused for boundary context (not for product claims): research/church-management-system-chms.md, research/church-giving-platform.md, research/church-communication-platform.md.

## Product A — Planning Center People

### Key observations (evidence layer A unless noted)

**Positioning:** "People is the free membership database of the Planning Center platform—where you can centralize information from across your ministries." FAQ: "People is completely free. You can use it all on its own, or combine it with other Planning Center products." — a standalone membership-database realization, free, with no check-in/giving/groups/events inside the product (those are separate Planning Center products).

**Roll structure:**
- Person profiles with default fields (name, birth date, gender, contact details — Tier-1 help article) plus custom fields/tabs (text, paragraph, date, yes/no, dropdown, checkboxes, number, file) usable in list rules, forms, and the congregant's Church Center profile (Tier 1)
- "Ministry activity — see all the ways someone engages with your church—attendance, giving, volunteering, and more" (synced from the other products when the church uses them)
- Notes: "prayer requests, counseling notes, and health conditions"
- Background checks: "order and monitor background check completion and expiration dates"
- Automations "automatically update profile details like age, membership status, or primary campus" — **membership status is an explicit profile field**
- Workflows: "multi-step workflows to track peoples' progress toward specific goals like becoming a member or serving in a ministry"
- Lists: rule-based queries ("attended Sunday Services at any location, ever"), auto-refresh, organized by campus/category; contact a list via text/email/Church Center announcement
- Duplicate merge ("Merge duplicate profiles and keep your data clean"); CSV import/export
- Church Center (member-facing): "Invite people to your church-wide directory where they update their profile, view other members, and make connections"
- Communication history tracked "for up to three months"

**What People does NOT contain:** check-in stations, giving collection, groups module, events/registrations, service planning — all separate products in the suite. People alone = roll + fields + lists + workflows + forms + notes + light comms.

## Product B — Church Windows (Membership module)

### Key observations (evidence layer A)

**Positioning:** desktop-heritage suite (copyright 1987–; "more than 30 years' experience"), "available either via remote web access or desktop installation… includes the main modules: Membership, Scheduler, Donations, Accounting, and Payroll." Pricing: "Choose your desired Modules… Available in a Full Package or Individual Parts -- 'Modules'." — **the Membership module is purchasable standalone** (Scheduler included with it).

**Membership module page:**
- "The Membership module contains a wealth of family and individual information available in a straightforward view… all components are quickly accessed due to the customer-focused layout through our interactive dashboard."
- Family and individual records: view family and individual records simultaneously; track family and individual alternate addresses; view all family names (with option to display ages); "accommodate non-traditional and traditional family structures effortlessly"; customize fields; view giving and pledging data (from the Donations module); school grade, group, skills, and interest tracking
- Connect with people: individual emails with minimal clicks; email a group or committee; "track personal attendance of events and worship"; "enter personal visitation, and make notations, including follow-up date"
- Reporting: attendance and visitation in summary or detail; birthdays, anniversaries, group/skills/interests fields; custom reports by criteria; "prepare reports and labels based on multiple criteria"; export to spreadsheet/word-processor merge; "print a church directory in multiple, flexible formats — preformatted or custom"; export PDF/Text/CSV/Excel

**What the module does NOT contain:** contribution collection and record-keeping (Donations module), fund accounting (Accounting), payroll (Payroll) — separate purchasable modules. Attendance here is light personal-attendance tracking, not check-in machinery.

## Product C — ParishSOFT Families

### Key observations (evidence layer A)

**Positioning:** "Families — Trusted Sacramental Records Software for Churches… A trusted, secure system designed to help your parish thrive… keeping sacramental records at your fingertips." Part of Ministry Brands. Families = "Manage records online with streamlining census, records, and communication."

**Roll structure:**
- "A Complete Family Directory: Easily track every family, individual, and sacramental detail with intuitive workflows designed specifically for Catholic parishes and schools." — the family is the directory/census unit
- "Sacramental Records Tracking: Keep a lifelong record of each parishioner's journey through the sacraments, with built-in templates for certificates and notification letters." — lifecycle milestones as records with document outputs
- "'My Own Church' Parishioner Portal: …parishioners and staff can access their user-friendly portal… a secure parishioner portal and mobile directory that improves accuracy while easing the administration of member records" — members register for classes, volunteer for ministries, review giving history, update contact information
- "Efficient Data Management: Instantly search, filter, export, or generate reports with powerful tools that simplify parish office workflows."

**Suite context:** Offering (contribution record-keeping) and Giving (online collection) are separate modules; Faith Formation (classes/attendance), Ministry Scheduler, Safe Environment, Tuition are separate modules. Diocese side: **Census module** — "Complete data for families, sacraments, staff, and volunteers in your diocese, along with tools to manage roles" — the hierarchical multi-org realization of the same roll.

## Product D — Breeze ChMS (Tithe.ly) — blurred pole

### Key observations (evidence layer A)

- "PEOPLE — A powerful people database built for churches, making it easy to manage member information, track engagement, and support your congregation."
- Core features list: Unlimited Contacts; Free Data Export/Import; Online & Text Giving; Text Messaging; Unlimited Emails; Event Management; **Member Directories**; Mobile App; **Check-in & Name Tags**; Service Planning; Worship Tools; **Attendance & Giving Reporting**
- Tags: "customizable Tags… small groups, volunteers, or event attendees"
- Rebranded: "Breeze ChMS has been rebranded as Tithely Church Management. Same simple, powerful church database you love"; flat $72/mo; bundle $119/mo
- Interpretation: the roll is the product's center ("people database"), but check-in, giving, and events are bundled — a lightweight ChMS, i.e., the roll embedded in participation machinery. Included as the boundary case showing where this Type dissolves into ChMS.

## Product E — Servant Keeper & Churchteams — boundary anchors

### Key observations (evidence layer A)

- **Servant Keeper:** platform pillars = Church Management, Communications, Child Check-In, Online Giving, Sites/Apps/Livestream. "Let members connect and self serve with an online church directory." Role-framed pages (Administration, Pastors, Treasurer, Children's Ministry, IT). "30,000+ churches" claim. Full ChMS.
- **Churchteams:** features = People & App, Groups, Communication, Giving, Volunteers, Registration, Check-in, Automation, Websites, Text-to-Church. FAQ: "track progress, and add benchmarks to member records through automation." Full ChMS.

Both demonstrate the dominant market pattern: the roll lives inside a full ChMS. Neither is a standalone membership product.

## Cross-product Comparison

| Structure | Planning Center People | Church Windows Membership | ParishSOFT Families | Breeze | Servant Keeper / Churchteams |
|---|---|---|---|---|---|
| People roll (identified individuals) | A | A | A | A | A |
| Household/family as first-class unit | B (households in Church Center; family structures) | A (family + individual simultaneous view; traditional + non-traditional structures) | A (family directory/census unit) | B (families) | B |
| Membership status recorded per person | A ("membership status" profile field + automations) | B (implied by the membership module framing) | B (census/registration of parishioners) | B ("member information") | B (member records) |
| Lifecycle events / milestones | B (workflows "toward… becoming a member") | B (visitation notations with follow-up dates) | A (sacramental lifelong records; certificates + notification letters) | — | — |
| Directories (print and/or member-facing) | A (Church Center church-wide directory) | A (print directory, multiple formats) | A (My Parish mobile directory) | A (Member Directories) | A (online church directory) |
| Lists / labels / reports from the roll | A (rule-based auto-refreshing lists) | A (labels by criteria, custom reports, exports) | A (search/filter/export/reports) | B | B |
| Attendance | — (synced from Check-Ins product) | A (personal attendance of events and worship — light) | — (Faith Formation module) | A (bundled) | A (bundled) |
| Contribution records | — (Giving product) | — (Donations module; giving data viewable from Membership) | — (Offering module) | A (bundled) | A (bundled) |
| Member self-service | A (Church Center profile + directory) | — (not surfaced) | A ("My Own Church" portal) | B (Church App) | A (member profiles) |
| Custom fields | A (Tier-1 typed fields/tabs) | A ("customize fields") | B | B (tags) | B |
| Duplicate merge / data hygiene | A | — | — | — | — |
| Sensitive notes | A (prayer/counseling/health) | A (visitation notations) | B | — | — |
| Import/export/migration | A (CSV) | A (exports; spreadsheet/word merge) | A (export) | A (free import service) | A (vendor import) |
| Standalone realization | A (free product, "use it all on its own") | A (module purchasable individually) | A (module of Family Suite; diocese Census) | full product (blurred) | full product (blurred) |
| Multi-org hierarchy | B (campuses) | — | A (diocese Census over parishes) | — | — |

Reading of the table: the roll (people + households + status + outputs) is present everywhere; participation machinery (check-in, giving, groups, events) is present only where the roll is embedded in a ChMS. The standalone realizations (columns 1–3) carry the roll without the machinery — this is the evidence that answers the ChMS pass's joint-review question.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as congregation membership management:

1. **Congregation people roll** — identified individuals held as the church's maintained records (its census of who its people are and how to reach them). (Remove → nothing remains of the Type.)
2. **Recorded membership status per person** — the roll distinguishes who belongs (member) from who is connected but not enrolled (visitor/attender) and who has left (inactive, transferred, removed); status is recorded by the church, not self-declared by the member. (Remove → a contact database / address book, not membership management.)
3. **Church-side administration** — staff and lay leaders maintain and govern the roll; members are its subjects, with scoped self-service at most. (Remove → a member-owned community app.)

Historical check (§24): a parish register (baptism/marriage/death records), a paper membership roll with letters of transfer between congregations, a denomination's annual statistical reporting built from such rolls, and a 1990s single-desktop office membership database (families + attendance + contributions in one file) all satisfy the three properties without portals, workflows, kiosks, or apps. The roll + status + household + pastoral milestones is the timeless core; modern machinery stays out of L0.

Households: deliberately NOT in L0. A roll of individuals with status would still be a membership roll. Households are, however, near-universal in the sample (layer B) and are the registration unit in the Catholic pole — the strongest L1 item.

### L1 — Common Mature Structure

Present across the sample (layer B) and documented per-product (layer A):

- **Household/family organization** as first-class units (address/contact often held at household level; children under guardians; Catholic variants register the family, with individuals as family members)
- **Custom fields** extending the person record (typed fields/tabs)
- **Directories** — printable (multiple formats) and/or member-facing (with privacy controls)
- **Lists, labels, and reports derived from the roll** — mailing labels, email lists, class/group rosters, demographic and anniversary/birthday reports, custom criteria reports, exports (CSV/PDF/spreadsheet/word-processor merge)
- **Light attendance recording as a membership signal** — personal attendance of events and worship tracked on the person (distinct from check-in machinery, which belongs to ChMS)
- **Lifecycle/milestone records** — joining (membership class, baptism, profession, transfer in), removal (transfer out, death, removal); Catholic pole: sacramental milestones as lifelong records with certificate and letter templates
- **Member self-service portal** — profile self-update, directory opt-in/visibility, giving-history view, class/volunteer signup (depth varies)
- **Duplicate merge / data hygiene** — duplicates are a known hazard of congregation data
- **Sensitive notes** — visitation, pastoral care, counseling, health — under restricted visibility
- **Communication from the roll** — email individuals/groups/committees; labels; (deeper sending loops belong to the comms Type)
- **Import/export/migration** — CSV and vendor-assisted migration

### L2 — Variant / Optional Structure

- **Denominational/heritage poles**: Catholic parish census + sacramental records (family as registration unit; certificates; diocesan Census over parishes) vs mainline membership-roll pole (rolls, transfers) vs evangelical engagement-led pole (membership classes, next-step tracking — blurs into ChMS)
- **Packaging**: standalone free product (Planning Center People) vs purchasable standalone module (Church Windows Membership) vs suite module (ParishSOFT Families) vs lightweight all-in-one (Breeze) vs record core of a full ChMS (dominant pattern)
- **Deployment**: desktop installation vs remote web hosting (Church Windows offers both) vs SaaS
- **Background checks** (Planning Center), **workflows/automations** (Planning Center, Churchteams), **forms feeding the roll**, **giving-history view** in the portal, **multi-campus**, **multi-org hierarchy** (diocese)
- **Scale posture**: single congregation roll → diocesan census (hierarchical multi-org)

### L3 — Vendor-specific Structure (research notes only)

- Planning Center: People free with per-product paid modules; Church Center member app; communication history retained ~3 months; Checkr background-check integration; "[hidden content]" masking for non-collaborators; grade promotion ("Promotes To"); named-competitor FAQ (F1, Tithe.ly, Breeze, CCB/PushPay, Shelby)
- Church Windows: Scheduler bundled with Membership purchase; desktop vs hosted-web choice; Aatrix payroll partner; module-by-module pricing; "Hot Product" marketing claims
- ParishSOFT: Ministry Brands ownership; "My Own Church" portal naming; diocese Census module; Offering vs Giving module split; Tuition for schools; "patent pending" footer
- Breeze: $72/mo flat; Tithe.ly rebrand and $119 All Access bundle; TrustPilot/Capterra rating claims; 50,000-churches claim
- Servant Keeper: 30,000+ churches claim; role-based marketing pages; Bullpen design credit
- Churchteams: Text-to-Church keyword mechanics; 25+ years / 70M emails claims; named competitors (CCB, Church Trac, Planning Center)

## Vendor-specific Findings

See L3. Additionally: only Planning Center documents field-level privacy masking, duplicate merge, and the explicit "membership status" field at Tier-1/Tier-2 depth; only ParishSOFT documents sacramental certificates/notification letters and the diocesan census; only Church Windows documents module-level standalone purchase. None of these are promoted to the canonical model.

## Boundary Findings

1. **vs Church Management System / ChMS (§25, processed) — the joint-review flag, now discharged.** Outcome: **keep-both with a center-of-gravity seam.** Standalone membership-only realizations are documented at three vendors: Planning Center People ("free membership database… use it all on its own" — no check-in/giving/groups/events inside the product), Church Windows Membership (purchasable standalone module; Donations/Accounting/Payroll are separate modules), ParishSOFT Families (census/records module; Offering and Faith Formation are separate modules). These carry the roll — people + households + status + directories/lists/reports — without the participation machinery. ChMS = the roll **plus** participation machinery (attendance/check-in, giving records, groups, events, workflows) operated as one ministry system. Seam test: strip the participation machinery → still this Type; make the machinery the product's center → ChMS. Market-structure note: the dominant realization of the roll is inside ChMS products (Breeze, Servant Keeper, Churchteams all bundle it), so this Type's market position resembles case-law-research-platform inside legal-research-platform — a real, separately-sold core that mostly ships embedded. Removal tests: remove people records → giving/comms/scheduling tools; remove membership status → contact database; remove participation machinery → this Type.
2. **vs Membership Management System (§25 sibling, unprocessed).** Probable domain-sibling pair (congregation vs generic). Generic membership systems (associations, clubs) center dues, renewals, benefits, and self-governing member bodies; congregation membership centers status, households, and pastoral records, with no dues machinery (giving is separate and voluntary). Flag for joint review when that leaf is processed.
3. **vs Member Directory (§25 sibling, unprocessed).** The directory is one output of the roll (print and/or member-facing, privacy-controlled). Watch-item: the directory leaf may be a capability slice of this Type (or of ChMS) rather than an independent Type.
4. **vs Church Giving Platform (§25, processed).** Meet at the giver record: the roll holds the person; the giving platform holds collection channels and gift records. Structural confirmation: Church Windows splits Membership vs Donations; ParishSOFT splits Families vs Offering; Planning Center splits People vs Giving.
5. **vs Church Communication Platform (§25, processed).** The roll is the audience substrate; the comms Type owns the sending loop (compose, schedule, replies, opt-outs). Labels and simple email from the roll are standard here; the managed messaging loop is not.
6. **vs Nonprofit CRM / Donor Management System (§25).** Same record grammar, different center: donor-centric (gifts, campaigns, appeals) vs membership-centric (status, households, pastoral records).
7. **"Remove what to become another Type" tests:** remove membership status → contact database/CRM; remove the congregation domain (generic members + dues/renewals) → Membership Management System; keep only the outputs (drop the maintained roll) → Member Directory; add participation machinery as the center → ChMS.

## Uncertainties

- Membership status vocabularies (member/regular attender/visitor/inactive etc.) are conceptually present and explicitly named at Planning Center ("membership status" field), but exact value sets per product were not verified at Tier 1 — kept conceptual in the final document.
- Church Windows evidence is Tier-2 (module page); its help files were not fetched this pass.
- ParishSOFT evidence is Tier-2; its support/knowledge base was not fetched.
- Breeze help center 404; Breeze evidence is homepage-tier.
- Planning Center help-center search and Church Center help sections are JS-rendered and returned no article content; People observations rest on the Tier-2 product page plus the Tier-1 custom-fields article from the ChMS pass.
- Mainline-Protestant specifics (letters of transfer, congregational voting rolls) are reasoned from domain/history for the historical check, not directly evidenced from product docs this pass — kept as variant framing, not asserted as product fact.
- Open-source membership products (ChurchInfo/ChurchCRM class) were not fetched; noted as probable additional standalone realizations, unverified.

## Final Synthesis

A Congregation Membership Management application is the church-side system that maintains the congregation's roll: identified people organized into households, each carrying a church-governed membership status, administered by staff and lay leaders, and rendered into the outputs church administration runs on — directories, lists, labels, reports, and member self-service. The joint-review flag from the ChMS pass is discharged as keep-both: standalone roll-only realizations exist and are documented (free standalone product, purchasable module, suite module), while the dominant market pattern embeds the roll inside full ChMS products. The seam is the participation machinery: this Type is the roll without it; ChMS is the roll with it, operated as one ministry system. The definition survives the historical check: parish registers, paper rolls with transfer letters, and 1990s office membership databases satisfy the core without any modern machinery.
