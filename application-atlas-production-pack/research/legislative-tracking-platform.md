# Research Notes — Legislative Tracking Platform

Research date: 2026-09-08
Leaf: Legislative Tracking Platform (DIRECTORY.md §24 Government, Public Sector & Civic)
Slug: legislative-tracking-platform

---

## Research Goal

Understand, from real products, what a Legislative Tracking Platform actually is and how it works: what objects exist inside it, who uses it, what "tracking" means operationally, how data enters the system, what users do daily, and where its boundary lies — especially against the already-processed sibling leaf Legislative Management System (§24), whose STATUS entry explicitly reserved "external watcher = legislative tracking territory" and left a joint-review flag naming the operator-position discriminator.

## Initial Boundary (working hypothesis before research)

- A Legislative Tracking Platform is a watcher-side instrument: it monitors lawmaking activity (bills/measures) in legislatures on behalf of parties outside (or alongside) the legislature itself.
- Closest neighbors: Legislative Management System (the legislature's own system of record), official legislature bill-status websites / Government Transparency Portal, Regulatory Change Management (§11), Media Monitoring Platform, Advocacy Platform, Government Meeting / Agenda Management (§24).
- Suspected core: monitored bills + watch definitions + change detection/delivery. Suspected non-core: advocacy mobilization, stakeholder CRM, news, AI analysis, multi-jurisdiction breadth (test needed).

## Research Questions

1. What is the unit of monitoring? (bill/measure — with which attributes: jurisdiction, session, sponsor, stage/status, text, versions, actions?)
2. What does "tracking" mean in product terms — a saved query, a personal file, a team board?
3. How does change reach the user — alerts, digests, reports? Who configures them?
4. Where does the data come from? What is the relationship to official systems of record?
5. Is multi-jurisdiction aggregation definitional, or a market norm?
6. What do users do after receiving a change? (triage, annotate, log stance, brief stakeholders)
7. Which adjacent data classes (regulations, legislators/committees, hearings/transcripts, local proceedings) are core vs extension?
8. Boundary: what exactly distinguishes this Type from the Legislative Management System, official transparency portals, regulatory tracking, and media monitoring?
9. Historical check: does the definition survive without the web, AI, alerts-as-email?

## Representative Products

Selected for market representation + document reachability + different philosophies + different customer tiers:

| Product | Pole | Customer tier | Evidence depth reached |
|---|---|---|---|
| FiscalNote (flagship platform now branded PolicyNote) | enterprise AI-driven policy tracking; global coverage | enterprise GR teams | product page + data page (Tier 2) |
| Quorum | public-affairs workspace suite centered on bill tracking + stakeholder action | mid-market/enterprise policy teams, incl. legislature-internal caucus staff | homepage + legislative-tracking solution page (Tier 2) |
| State Net (LexisNexis) | legacy data-service pole; "pioneers in 50-state bill tracking" (customer testimonial: "since 1995") | compliance, government affairs, associations, law firms | product page incl. FAQ (Tier 2) |
| Plural (formerly Open States) | open-data-heritage pole (adopted the Open States project 2021; free tools + bulk open data + API) + paid AI bill tracking | advocacy orgs, chambers, corporations, law firms/lobbyists, libraries, journalists | homepage + product page (Tier 2) |

Rejected/adjusted samples:
- LegiScan — intended as the transparency/data-first free pole; root and API pages returned 403 twice → dropped per network-retry rule; recorded as limitation.
- congress.gov and state legislature sites — official systems of record; treated as boundary context (named by FiscalNote as its data sources) rather than sampled products.

Note: no sampled product's paid Help Center was reachable; all evidence is product-page/FAQ depth (Tier 2), not Tier-1 operational docs. Assertion strengths calibrated accordingly below.

## Sources

All fetched 2026-09-08:

- FiscalNote — https://fiscalnote.com/ ; https://fiscalnote.com/products/policynote ; https://fiscalnote.com/legislative-data
- Quorum — https://www.quorum.us/ ; https://www.quorum.us/solutions/legislative-tracking/
- LexisNexis State Net — https://www.lexisnexis.com/en-us/products/state-net.page
- Plural — https://pluralpolicy.com/ ; https://pluralpolicy.com/ai-powered-bill-tracking/ (openstates.org now redirects to pluralpolicy.com)
- LegiScan — https://legiscan.com/ and https://legiscan.com/legiscan-api — HTTP 403 both, unreachable (limitation recorded)
- Sibling context: STATUS.md entry for legislative-management-system (2026-09-08) and its research notes (Quorum previously sampled there as boundary counterpart)

---

## Product Observations

### FiscalNote / PolicyNote

Evidence layer A (directly observed on official pages). Vendor self-describes the flagship as "the #1 legislative and regulatory tracking software" whose job is to "track and shape policy."

- Problem framing (vendor's own words): "There's no shortage of policy information. The problem is knowing which bill actually moves, which hearing signals a real shift, and what it means for your organization specifically." — filtering to what matters is the stated product job.
- Automated tracking: "alert overviews, bill summaries, and curation ensure you never miss a policy development."
- Featured capabilities: Curated Alerts (vendor's analyst team "reviews your alerts first"); Bill Forecasts ("how likely a bill is to reach a floor vote and pass in each legislative chamber"); AI Impact Analysis (impact on "your organization's stored profile"); AI Assistant; Bill Summaries; Chat-Based Search; Reporting ("brief your leaders and prove your impact"); Custom Dashboard ("top priorities like new policies to review and tasks to complete"); Bill Comparison ("compare red lines between two versions of a bill").
- Coverage (data page): local (12,000+ municipalities, 4,000+ school districts — vendor-stated numbers), US (federal, 50 states, DC, Puerto Rico), global (100+ countries). Solutions packaged per tier: Federal Policy Tracker / State Legislative Tracking / US Local Policy Tracking / Global Policy Tracking.
- Data classes offered: Legislation ("bills, votes, hearings, sponsors, and pass-likelihood analytics... get alerted when one moves"); Regulations ("proposed and final rules... catch comment periods before they close"); People & Organizations ("officials, staffers, committees, and legislative districts"); Transcripts & Proceedings; Local Proceedings ("agendas, minutes, and meeting records").
- Collection mechanics (vendor FAQ): automated scrapers run continuously and re-scan all available records each pass "because most government websites don't announce what has changed"; vendor states new activity typically reaches users within about an hour of appearing.
- Source-of-record relationship (vendor's words, structurally decisive): "PolicyNote data comes straight from the systems of record: Congress.gov and the Federal Register, State legislative sites and regulatory registers, Local government websites, Official government sources worldwide. When you cite it, you're citing the source."
- User-side data layer (the watcher's own): "Access your Issues, Labels, and Actions in PolicyNote. Organize bills by Issue, log your advocacy, and filter every result by what your team is already tracking."
- Access modes: "One dataset three ways" — App (dashboards, alerts, reports, AI) / API / MCP (AI-agent access).
- Roles/audience: U.S. and global government affairs, advocacy, government agencies, congressional offices; testimonials from corporate and association GR staff.

### Quorum

Evidence layer A (homepage + legislative-tracking solution page).

- Solution page: "Track Every Bill Across All 50 States and Congress. Quorum's agentic AI ranks hundreds of thousands of state and federal bills so you act on what matters first." Page title: "Legislative Tracking Software | AI Bill Monitoring."
- Real-time alerts: "Get instant alerts when priority bills advance, amendments drop, or your keywords appear in hearing transcripts." — three trigger classes: stage advancement, new amendment text, keyword matches in transcripts.
- AI bill intelligence: "ranks bills by your issues, summarizes provisions, and flags what demands attention."
- Hearing transcripts: AI-indexed committee transcripts searchable by keyword with speaker identification.
- Cross-team tracking: "Assign bills, log stances, and share tracking boards so your team works from one source of truth." Platform counters: "Bill Alerts Opened / Active Bill Portfolios / Official Positions Logged" — the tracked-bill portfolio with assignments and stance logging is presented as the operating unit.
- AI assistant (Quincy) sample queries the vendor demos: new bills introduced last week mentioning given keywords; bills similar to a federal bill across states this session (text similarity); "Based on your tracked issues, here are 5 bills that moved this week"; enactment status of a policy across all 50 states; bill summaries.
- Products split by jurisdiction: Federal / State / Local & School Board / EU & International; separate solutions pages for Regulatory Tracking, Stakeholder Management, Grassroots Advocacy, PAC Management, News Monitoring, Government Contact Data (KnowWho) — tracking vs advocacy vs relationship management are distinct packaged modules.
- Case studies: Sierra Club "track hundreds of pieces of legislation across all 50 states each year"; US Air Force Office of Legislative Affairs uses it for institutional knowledge of tracked items; "State Legislatures" solution ("Track and triage legislation, align caucuses") — the same tracking product is also sold to legislature-internal users (caucus staff), used for triage/monitoring rather than operating the process.
- Audience: "2,000+ policy teams," "more than 50% of Fortune 100 companies" (vendor claims).

### State Net (LexisNexis)

Evidence layer A (product page + FAQ). Legacy enterprise data-service pole.

- Self-description: "State Net is a leading online legislative and regulatory tracking and intelligence service for the 50 States and Congress. State Net helps you monitor and manage pending legislative and regulatory activity, evaluate impact, influence proposals, prepare for changes, and deliver meaningful information to stakeholders."
- Scale (vendor-stated): "search and track more than 150,000 legislative and 50,000 regulatory measures annually" drawn from "350 legislative sources and over 12,000 regulatory agencies."
- Tracking workflow: "With the Track button, you can quickly add a measure to your private file, then easily add or create tags"; "Use the intuitive Tracking Console to access, filter, and sort all your tracked measures." — the tracked-measure file is the user's own portfolio.
- Search: type-ahead, pre/post-search filters, open-text search across 1,200+ prepopulated topics; custom topics; saved searches ("save searches so you can quickly return to them anytime").
- Alerts/delivery: email alerts; "automated delivery of reports. Customize recipients, message and frequency so your stakeholders are always up to date"; scheduled alerts; share via email or export for leadership briefings.
- Analysis: analyst-written summaries ("Robust analysis from dedicated professionals bridges the gap between raw data and useful knowledge"); what's added/deleted between versions; side-by-side version comparison; "Legislative Forecast and Timeline provide visualizations of a measure's status and speed"; predictive analytics for movement nationwide; session statistics; voter scorecard (support/opposition); calendars (hearing dates, session dates, elections).
- Delivery/integration surfaces: XML data feed "giving you control and customization within your own database"; iTrac — "customized, real-time legislative and regulatory updates to stakeholders through a secure, branded web portal"; API; Issue Screening (vendor experts build custom searches and auto-add results for review).
- Adjacent content: State Resources (session dates, elections); Representative Details (legislator profiles, committee assignments, agency contacts); Webcasts (live floor streams); Agency Documents; Local Ordinances ("more than 1,000 municipalities nationwide"); Code Navigator (from pending bill to statutes in Lexis+).
- Who it's for: compliance, government affairs, associations, law firms.
- FAQ: coverage "all 50 states, Congress, and key U.S. territories"; content includes "bills, rules, statutes, executive orders, legislative hearings, regulatory notices, and rulemaking activity"; updates "typically within 24 hours" (vendor-stated); local ordinances in select jurisdictions.
- Legacy evidence: customer testimonial — "I have been a State Net customer since 1995! They are pioneers in 50-state bill tracking."

### Plural (formerly Open States)

Evidence layer A (homepage + product page). Open-data-heritage pole.

- Product: "AI-Powered Bill Tracking & Intelligence — For policy teams who need premium data, real-time updates, and a competitive edge, Plural is the bill tracker of choice."
- Core loop in vendor's words: "Thousands of bills are introduced each session — with Plural, it's easy to find what you need. Use Plural's advanced search options to intelligently narrow down your results, and save your searches to get real-time updates on any new developments... without the need to constantly re-search."
- Search: filter by "keywords, bill status, sponsors, jurisdictions, and more."
- AI layer: AI-generated bill summaries including version-to-version summaries; AI-detected bill topics (auto-categorization); related/highly-similar-bill detection (omnibus bills, model bills) and a "Global Bill Search Tool" to see "whether similar bills have been introduced across multiple jurisdictions"; predictive signals ("which bills are likely to gain momentum and become law").
- Open-data heritage: "Plural is carrying that legacy forward from the Open States project, which we adopted in 2021. We continue to expand our open data and just launched improved democracy tools." Open data "available for bulk download and via our powerful API" with API keys via open.pluralpolicy.com (distinct free/community tier).
- Who it's for: advocacy organizations, chambers of commerce, corporations, law firms & lobbyists, libraries & universities, associations, journalists/news media; also a public "Find Your Legislators" lookup tool.
- Coverage: US-wide plus some African legislatures (footer "Africa" section, jurisdictions page) — international coverage beyond the US pole.
- Case study (blog link): a Georgia voting-rights coalition (Fair Fight) reduced time reviewing legislation by 75% with Plural.

---

## Cross-product Comparison

| Aspect | FiscalNote/PolicyNote | Quorum | State Net | Plural | Strength |
|---|---|---|---|---|---|
| Named activity: "bill / legislative tracking" | yes (#1 legislative and regulatory tracking) | yes (Bill & Legislative Tracking Software) | yes (legislative and regulatory tracking service) | yes (Bill Tracking & Intelligence) | 4/4 — core |
| Monitored measures as individually addressable records (jurisdiction, session, sponsor, status, text/versions, actions) | bills, votes, hearings, sponsors | every bill, tracked portfolios | tracked measures in private file, measure details | bills with status/sponsors/jurisdictions | 4/4 — core |
| User-configured watch (tracked measures + saved searches/topics/issues) | Issues, Labels, "what your team is already tracking" | tracked issues; tracking boards | Track button → private file + tags; saved searches; custom topics | saved searches; AI topics | 4/4 — core |
| Change detection → delivery (alerts/digests/reports) | alert overviews; continuous scan loop | instant alerts on advance/amendments/keyword-in-transcript | email alerts; scheduled reports w/ recipients+frequency | real-time updates on saved searches | 4/4 — core |
| Multi-jurisdiction aggregation | 50 states + Congress + local + 100+ countries | 50 states + Congress (+ local, EU products) | 50 states + Congress + territories (+ local add-on) | US-wide + some African legislatures | 4/4 — strong common; held common (see below) |
| Derives from official systems of record | explicit ("straight from the systems of record... When you cite it, you're citing the source") | implied (aggregates official activity) | implied (350 legislative sources = official bodies) | implied (open legislative data) | explicit 1/4; structurally certain for the Type |
| People/legislator layer | officials, staffers, committees, districts | KnowWho contacts (separate product) | Representative Details | Find Your Legislators | 4/4 — common |
| Regulations/rules as adjacent class | yes (federal+state rules, comment periods) | separate Regulatory Tracking solution | yes (50,000 regulatory measures; rulemaking) | yes ("legislation and regulations") | 4/4 — common extension |
| Stakeholder reporting/delivery | Reporting to "brief your leaders" | Impact Reports | automated reports w/ recipients; iTrac portal | weaker evidence (case-study level) | 3/4 — common |
| Version comparison | Bill Comparison (red lines) | via summaries | side-by-side compare | version-to-version summaries | 3/4 — common |
| Predictive analytics (pass likelihood) | Bill Forecasts | AI ranking/flags | Legislative Forecast; movement prediction | momentum prediction | 4/4 — era-current common (not definitional) |
| Team workflow (assign, stance/tag, share) | labels/actions, log advocacy | assign bills, log stances, shared boards | private file, tags, shareable alerts | thin evidence | common |
| Human analyst/curated services | Curated Alerts; PolicyNote+ | managed services | analysts; Issue Screening | — | 3/4 — optional |
| Open data / free tier | — | — | — | bulk download + API keys (Open States heritage) | 1/4 — variant |
| Suite adjacencies (advocacy, PAC, news, stakeholder CRM) | VoterVoice, CQ, stakeholder DB | grassroots, PAC, news, stakeholder | Lexis+ research link | — | vendor packaging, not Type |
| Branded AI assistant | AI Assistant | Quincy | — | AI summaries | era-current packaging |

### Synthesis of the comparison

1. Every sampled product, across 30 years of market history (State Net since at least 1995; Open States adopted 2021), realizes the same loop: aggregate official legislative activity into per-measure records → let the watcher define what to watch → detect change continuously → deliver it. This loop is the Type.
2. The relationship to official systems of record is structural: the platform holds mirrored, second-party records; only FiscalNote states it verbatim ("straight from the systems of record... you're citing the source"), but aggregation from official sources is the only coherent reading for all four.
3. Multi-jurisdiction breadth (federal + 50 states minimum in the US market) is universal in the sample and central to the value proposition — but the recognizability test does not exclude a single-body external watcher (a consultancy tracking one city council performs the same three-part loop). Held as strong common expectation, not definitional.
4. The watcher's own layer (private tracked files, tags/labels/issues, stances, assignments, saved searches) is what turns a public bill database into a personal/organizational monitoring workspace. Universal in sample.
5. Analysis layers (summaries, forecasts, comparisons) and stakeholder reporting are common mature capabilities; AI ranking/assistants are era-current (2024–2026 wave) and not definitional.
6. Customer segments are broad and heterogeneous (corporations, associations, law firms, advocacy orgs, libraries, journalists, government agencies, congressional offices, legislature-internal caucus staff) — segmentation is variant, not core.

---

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

An external-watcher monitoring instrument over lawmaking activity. Three jointly-held structures; the jointly-held property is load-bearing:

1. **The mirrored measure of record.** Bills/measures from lawmaking bodies held as persistent, individually identified watcher-side records — jurisdiction, session, sponsor, status/stage, official text/versions, and the accumulating action history — mirroring official records the platform's user neither authors nor advances. The watcher position is encoded here: the platform is a second party to the process; it observes and never operates. (Remove → an official bill database / transparency portal, or a news feed with no bill-shaped records.)

2. **The watch definition.** User-configured standing selections over the shared corpus — jurisdictions, sessions, topics/keywords/issues, tracked measures, sponsors, saved searches — held as the user's (or team's) private layer that scopes everything the platform surfaces. (Remove → a searchable public bill archive that requires manual re-querying.)

3. **The change-detection-and-delivery loop.** Continuous monitoring of official activity against the watch definitions, pushing what changed — stage advancement, new/introduced measures, new amendment text, new keyword matches — to the watcher through alerts, digests, dashboards, and stakeholder reports. The platform's defining act is to notice and deliver, never to operate. (Remove → a static searchable archive.)

Jointly-held decomposition tests:
- 1 alone = a bill database / open data portal (the official record itself).
- 2 alone = saved web searches — generic alerting with no legislative object model.
- 3 without 1+2 = a generic news/alert service.
- 1+2 without 3 = a searchable archive with saved queries; the user must check back manually — tracking without monitoring.
- 1+3 without 2 = a firehose of all activity, not personalized tracking.
- 2+3 without 1 = an alerts engine with nothing bill-shaped to alert about.

### L1 — Common Mature Structure

- Multi-jurisdiction aggregation and normalization (in the US market: Congress + all 50 states as the floor; local municipalities/school boards, EU/international as expansion tiers).
- Measure detail: full text, version history, action/vote history, sponsors, committee assignments.
- People/organizations layer: legislators, committees, staff; sometimes contact data and districts.
- Session/committee calendar layer: session dates, hearing schedules, calendars (legislative activity is session-bounded — the domain's own clock).
- Saved searches + tracked-measure portfolios: private files with tags/labels/issues, team assignment, stance logging, shareable tracking boards.
- Alerting with configurable delivery: email alerts, digests, scheduled reports with recipients and frequency; exports for stakeholder briefings.
- Stakeholder reporting: briefs/impact reports for leadership and members.
- Search across bill text with topic taxonomies; version comparison.
- Regulation/rulemaking as an adjacent data class.
- Historic archive depth (multi-decade at the enterprise pole; State Net customer since 1995; FiscalNote federal history to the 99th Congress, vendor-stated).

### L2 — Variant / Optional Structure

- Coverage scope packaging: federal-only ↔ state ↔ local ↔ EU/global (sold as separate products/solutions at FiscalNote, Quorum, State Net).
- Customer-segment packaging: corporate GR, associations, law firms/lobbyists, advocacy orgs, compliance, libraries/universities, journalists.
- Access mode: workspace app only ↔ open data + public API keys (Plural/Open States pole) ↔ enterprise data feeds (XML) ↔ agent/MCP access.
- Human-in-the-loop services: curated alerts, expert-built searches, custom research/briefs.
- Predictive analytics (pass likelihood, momentum), AI summaries/ranking/assistants — era-current.
- Suite adjacencies: advocacy mobilization, stakeholder CRM, PAC, news monitoring — bundled by suite vendors but separate Types.
- Free/open-data pole vs premium pole.
- Legislature-internal users (caucus staff triage) as an audience variant without changing the watcher stance.

### L3 — Vendor-specific (research notes only)

- FiscalNote: PolicyNote branding; MCP access; CQ/Roll Call news integration; VoterVoice advocacy; Curate local brand; EUIT; PolicyNote+ analyst services; vendor-stated collection cadence (~1 hour) and coverage counts (12,000+ municipalities, 4,000+ school districts, 100+ countries).
- Quorum: Quincy AI; KnowWho contact data; "50% of Fortune 100" claim; Sierra Club / USAF case studies; counters (alerts opened / portfolios / positions logged).
- State Net: iTrac branded stakeholder portal; XML feed; Code Navigator → Lexis+; Capitol Journal; webcasts; vendor-stated scale (150k legislative + 50k regulatory measures/year; 350 sources; 12,000 agencies; ~24h update).
- Plural: Open States heritage and open.pluralpolicy.com API keys; bulk download; AI topic/similarity machinery; Africa coverage.

---

## Vendor-specific Findings

- Curated-alert human review (FiscalNote) and expert issue-screening (State Net) show that the detection loop can include human analysts, not just automated scanning — a service wrapper around the same loop, not a different Type.
- iTrac (State Net) re-delivers tracked updates through a branded portal to the watcher's own stakeholders — the delivery leg extended one hop outward.
- Quorum's "State Legislatures" solution demonstrates the watcher position is about function, not employer: even legislature-internal users (caucus staff) use the tracking Type to monitor/triage the process they do not operate.
- Plural's Open States pole proves the open-data + API distribution model satisfies the same core without a paid workspace.

## Boundary Findings

1. **vs Legislative Management System (§24 sibling, processed 2026-09-08).** Discriminator confirmed from this side: the operator position. The LMS is the legislature's own system of record operated by its secretariat/clerk — intake, numbering, stage advancement, chamber business instrument, publication. The tracking platform holds mirrors of measures it cannot create, number, or advance; its defining acts are watch → detect → deliver. The two are upstream/downstream: the LMS (and peer official systems like congress.gov) are the sources of record the tracker derives from. Quorum was sampled in the sibling pass as boundary counterpart and appears here as a full tracking product — consistent. The joint-review flag is DISCHARGED with keep-both ratified.
2. **vs official legislature websites / Government Transparency Portal (§24).** Official bill-status systems publish the authoritative record for their own body; a tracking platform is (a) a third-party instrument, (b) aggregating across many bodies, (c) monitoring-oriented (watch portfolio → push). FiscalNote's own data page names congress.gov, state legislative sites, and local government websites as its inputs — evidence of the seam from the vendor itself. Remove the external aggregation and watch loop → transparency portal.
3. **vs Regulatory Change Management (§11).** Different instrument class (agency rulemaking vs legislature bills) and different center (obligations-driven compliance loop vs lawmaking monitoring). But all four sampled products carry regulations as a data class, and Quorum/FiscalNote market "legislative and regulatory tracking" together — the convergence is real and documented as a common extension, with the legislative instrument remaining the Type's center. Keep-both; the Regulatory Change Management pass should expect legislative trackers at its edge as adjacent tools, not the same Type.
4. **vs Media Monitoring Platform (§06).** Subject and source class differ: published media about the organization vs official lawmaking activity. Suite vendors bundle news monitoring as separate modules (Quorum News Monitoring; FiscalNote CQ), confirming the separation.
5. **vs Advocacy Platform / grassroots (§25/§06).** Advocacy mobilizes supporter action toward lawmakers; tracking informs the watcher. FiscalNote ships VoterVoice as a distinct product; Quorum splits Grassroots from tracking solutions. The watcher may "log advocacy" (FiscalNote "Actions") as annotation, which stays inside this Type.
6. **vs Government Meeting / Agenda Management (§24).** Local meeting agendas/minutes appear inside tracking products as a data class (FiscalNote Local Proceedings; Quorum Local & School Board), but the meeting-cycle instrument (agenda assembly, notice, minutes, run-the-meeting) is the clerk-side sibling Type. Ingesting local activity as monitored content is tracking territory.
7. **vs Legal Research Platform / Case Law Research (§11).** Prospective monitoring of pending measures vs retrospective research of enacted law. State Net's Code Navigator (pending bill → statutes) explicitly bridges the two — the seam is at enactment.
8. **vs generic monitoring/alerting (saved web searches, news feeds).** The bill-shaped object model (jurisdiction/session/stage/sponsor/versions) and the legislative-status semantics are what make this a distinct Type; generic alerting has no such model.

"去掉什么就变成另一个 Type" tests:
- Remove the watcher position (user operates the process) → Legislative Management System.
- Remove the external aggregation (single official body publishing its own record) → Government Transparency Portal / official bill-status site.
- Remove the legislative instrument (monitor agency rules only) → regulatory change tracking (§11 territory).
- Remove the watch definition and delivery loop → a bill database / open data portal.
- Remove the bill-shaped object model → generic media/news monitoring or a saved-search alert service.

## Historical / Market-Sample Check (§24)

Paper-era equivalent: a trade association's or law firm's legislative clerk maintaining a **bill watch** — a card file where each tracked bill is a card (number, title, sponsor, committee, current stage, hand-updated from journals, calendars, and daily papers), a **watch list** defining the association's issues and jurisdictions, and a periodic **mimeographed bulletin** circulated to members reporting what moved. All three legs hold: mirrored measure records (cards, not the chamber's own file), watch definition (the association's list), detection-and-delivery (a human engine producing a member bulletin). No web, email, AI, or multi-state vendor required.

Pre-AI era: State Net's 1995 customer confirms the 50-state electronic tracking service predates modern AI/mobile. The Open States open-data pole shows the core survives without a commercial workspace. Conclusion: the definition is era-robust; AI ranking, forecasts, and chat search are era-current capability layers.

## Uncertainties

1. No Tier-1 help-center documentation was reachable for any sampled product; operational details (alert configuration granularity, status-vocabulary normalization across jurisdictions, data-retention behavior) are inferred at product-page depth. Assertions kept at moderate strength accordingly.
2. LegiScan — a significant free/data-first market player — was unreachable (403 ×2); the free/transparency pole is evidenced only through Plural's Open States heritage.
3. Update-latency claims (FiscalNote "about an hour"; State Net "typically within 24 hours") are vendor-stated marketing figures, not independently verified; kept out of the final document as precise facts, retained here as vendor claims.
4. Exact coverage-count claims (12,000+ municipalities; 150,000+ measures/year) are vendor-stated; retained as claims, not facts.
5. Whether a genuinely single-jurisdiction commercial tracking product exists as a stable market pole could not be verified from the sample; the multi-jurisdiction norm is documented as strong-common rather than definitional to stay safe on this point.
6. Stakeholder-facing portals (iTrac) and delivery granularity documented for one product only — held product-specific/optional.

## Final Synthesis

A Legislative Tracking Platform is the external watcher's monitoring instrument over lawmaking. Its defining core is the joint holding of (1) mirrored, individually identified measure records derived from official systems of record — never authored or advanced by the user, (2) user-configured watch definitions that scope the corpus into a private/organizational portfolio, and (3) a change-detection-and-delivery loop that continuously notices official movement and pushes it to the watcher. Everything else — multi-jurisdiction breadth, legislator/committee data, session calendars, version comparison, forecasts and AI ranking, stakeholder reporting, regulations as adjacent class, advocacy and CRM adjacencies, open-data vs premium distribution — is common, optional, or vendor-specific structure layered on that loop. The Type sits on the watcher's side of the operator/watcher seam with the Legislative Management System, and is bounded against transparency portals (no watch loop, single body), regulatory tracking (different instrument class), media monitoring (different source class), and advocacy (different function).
