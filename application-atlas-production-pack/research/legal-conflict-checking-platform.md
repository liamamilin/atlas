# Research Notes — Legal Conflict Checking Platform

## Research Goal

Understand what a Legal Conflict Checking Platform actually is as an Application Type: what objects it holds, what its defining workflow is, who operates it, and where its boundaries lie against Legal Intake & Client Onboarding, Law Practice Management Systems, sanctions/AML screening, and ethical-wall (information barrier) tooling.

## Initial Boundary

- Directory leaf: "Legal Conflict Checking Platform" (§11 Legal, Risk, Compliance & Governance).
- Hypothesis at start: software used by law firms (and professional-services firms) to detect conflicts of interest before accepting a client or matter — a searchable database of the organization's own relationships (clients, adverse parties, related parties), a screening search of prospective names against it, and a review/clearance/waiver decision loop.
- Prior passes already pointed here:
  - `legal-intake-client-onboarding` research: "the deep conflicts machinery (firmwide full-text search, ethical walls, clearance workflows) is a separate directory Type (Legal Conflict Checking Platform); intake only requires that a screening step can be performed and recorded."
  - `law-practice-management-system` research: conflict-check search over the firm's own records kept "common-not-universal" — a capability inside LPM, with a capability-vs-Type note deferred to this leaf.
- Adjacent suspects: Legal Intake & Client Onboarding (conversion-centered gate), LPM (embedded search capability), Sanctions Screening Platform (structurally similar name-matching, different data universe), ethical walls / information barriers (access enforcement, often triggered by conflicts results).

## Research Questions

1. What is the unit of record — the party database, the check, the clearance decision?
2. What feeds the searchable universe (clients, adverse parties, related parties, corporate families, employee interests)?
3. What matching techniques are used (exact, fuzzy/flex, synonyms, aliases, corporate-tree expansion)?
4. What happens after hits — who reviews, what dispositions exist (clear / conflict / waive / decline), how are they recorded?
5. Are ethical walls / information barriers part of this Type or a separate one?
6. Is there ongoing monitoring / re-screening (delta re-runs, continuous monitoring, recurring independence checks)?
7. What records are retained and why (audit trail, defensibility, regulator-readiness)?
8. Who uses it and on what surfaces?
9. How does it gate intake and matter opening?
10. Where is the boundary vs intake, LPM conflict search, and sanctions screening?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Intapp Conflicts | Enterprise deep-search platform (large firms + accounting/consulting/IB) | Market-leading dedicated conflicts product; ships alongside separate Intake/Walls products |
| iManage Conflicts & Intake (Conflicts Manager lineage) | Enterprise modular platform (Checks / Clearance / Intake tiers) | Explicitly tiered modules; rich official ebooks and customer stories |
| Aderant Conflicts (Expert Conflicts lineage) | Mid-market PM-suite module + new standalone cloud product | Shows both suite-embedded and standalone packaging |
| Clio (Manage/Grow conflict checks) | SMB LPM-embedded capability — upper capability pole | Public help docs; structured check with status + report, but no clearance machinery |
| PracticePanther (conflict check) | SMB LPM-embedded capability — floor | Public help doc; bare full-text search, no retained check record |

Market context (Tier 3): Gartner maintains a "Conflict Check Software" review category; comparison sites list Aderant, Intapp, iManage, Clio, MyCase, CosmoLex, Smokeball, Actionstep, PracticePanther, Rocket Matter, AbacusLaw, Bill4Time, Amicus Attorney, CARE T Legal, HoudiniEsq. One Tier-3 article claims ~89% of 50–99-lawyer firms use conflict checking software — not promoted (unverified statistic).

## Sources

Tier A (official, directly fetched):

- Intapp Conflicts product page — https://www.intapp.com/conflicts/ (fetched 2026-09-10)
- Intapp legal conflicts solution page — https://www.intapp.com/legal/conflicts/ (via search index, 2026-09-10)
- iManage Conflicts & Intake product page — https://imanage.com/imanage-products/risk-compliance/conflicts-intake/ (fetched 2026-09-10)
- iManage ebook "5 ways to enhance your law firm conflicts search" — https://imanage.com/media/ecelybke/5-ways-to-enhance-your-law-firm-conflicts-search-ebook.pdf (via search index)
- iManage ebook "Connect the Dots" (conflicts → information barriers) — https://imanage.com/media/j0anynk1/spm-conflicts-ebook-23.pdf (via search index)
- iManage customer story (global law firm) — https://imanage.com/resources/customer-stories/global-risk-compliance-customer/ (via search index)
- Clio Help Center — "Run Conflict Checks in Clio Manage and Clio Grow" — https://help.clio.com/hc/en-150/articles/41182681954331 (fetched 2026-09-10)
- Clio Help Center — "Customize Conflict Check Search Settings" — https://help.clio.com/hc/en-us/articles/43953875528731 (via search index)
- Clio Help Center — "Create Matters" / "Global Search" (via search index)
- PracticePanther Help Center — "Running conflict checks" — https://support.practicepanther.com/en/articles/479862-running-conflict-checks (fetched 2026-09-10)
- Aderant — conflicts.aderant.com (official description via search index; page itself is a JS app, not fetchable)
- Aderant — "Update Your Conflicts Process..." on-demand recording page — https://www.aderant.com/on-demand-recording/update-your-expert-conflicts-process-recording/ (via search index)
- Aderant — Expert Sierra solutions page (feature list incl. "Conflicts Check, File Opening") — https://www.aderant.com/solutions-expert-sierra/ (via search index)
- Aderant — Brach Eichler news release (Expert Conflicts description) — https://www.aderant.com/news-pr/brach-eichler-live-aderant-expert/ (via search index)

Tier 3 (market structure only, not promoted to definitional evidence):

- Gartner Peer Insights "Conflict Check Software" category — https://www.gartner.com/reviews/market/conflict-check-software
- wifitalents.com / gitnux.org / zipdo.co comparison pages (2026)
- regtechpost.com article (2025)

Source-access limitations:

- Intapp support/documentation (support.intapp.com) is behind SSO — operational detail (exact statuses, workflow configuration) not verifiable from official docs; assertions about Intapp internals held at product-page strength.
- Aderant's standalone Conflicts site (conflicts.aderant.com) requires JavaScript — description taken from the official site text as surfaced in the search index; internal mechanics not verified.
- Thomson Reuters Elite/3E Conflicts not sampled (documentation not reached within budget); heritage "conflicts embedded in finance system" pattern is evidenced instead by the iManage customer story.

## Product Observations

### Intapp Conflicts (evidence layer A unless noted)

From the official product page and FAQ:

- Positioning: "Manage conflict detection, analysis, and governance with one unified system" for professional firms (legal, accounting, consulting, financial services, private capital).
- **Centralized data management**: "Unify client, engagement, and relationship data in a searchable system." FAQ: integrates with the firm's existing systems that track "client entities, corporate structures, and associated engagements"; data can be enriched "with corporate trees and industry codes from trusted third-party sources"; employee financial interests arrive by integrating Intapp Employee Compliance (separate product).
- **Search**: "Use unified, real-time data from multiple sources in every conflicts check"; "Screen opportunities before they advance to formal review"; "Prevent staffing conflicts and misalignments by analyzing current and historical work"; "Surface employee conflicts by integrating outside business interest data."
- **AI (Celeste)**: builds the search strategy, "triage[s] high-risk hits for expert review," drafts "clearance summaries … for each analysis," and "continuously monitors integrated data sources and surfaces potential issues."
- **Initiation**: "Initiate conflicts checks directly from Intapp Intake or Intapp DealCloud" (separate products).
- **Recordkeeping**: "Create an auditable record of all analyses and decisions"; "Access the history of every conflicts search and outcome"; "Maintain a defensible record of every conflicts check and decision"; "Maintain a regulator-ready record of every analysis and decision" (financial-services framing).
- **Collaboration/resolution**: "Allow decision-makers to review details, add notes, and document resolutions in shared documents."
- **Reports**: "Generate reports that automatically filter confidential information using Intapp Walls policies" (Intapp Walls = separate product for ethical walls).
- Industry framings: accounting = independence ("Build an inspection-ready system of record for independence management"); consulting = "competitive and commercial conflicts"; financial services = "regulatory conflicts and information barrier requirements"; private capital = deal conflicts.
- Blog title evidences the workflow's weight: "What happens to conflicts clearance when law firms merge?" — mergers create "an immediate conflicts clearance crisis."
- Case study (BDO Australia): "systemize a rigorous closed-loop conflicts process."
- Tier 3 descriptions add: "configurable clearance workflows, repeatable conflict status decisions, and reporting artifacts that support search audit trail needs"; "party searching and adverse-party review flows with configurable matching logic for names and aliases"; "conflict status, waiver handling, and clearance decisions during new matter opening" (wifitalents/gitnux/zipdo — moderate confidence, consistent with official page).

### iManage Conflicts & Intake / Conflicts Manager (evidence layer A)

From the official product page, ebooks, and customer story:

- Positioning: "streamlines conflicts checks, conflicts clearance, and business intake … A scalable, modular solution."
- **Modular tiers** (FAQ): "start with the Conflicts Checks module and scale up to Conflicts Clearance and New Business Intake at a later stage" — the market itself sells the check, the clearance, and the intake as separable layers.
- **Conflicts Checking module**: "iManage streamlines searches by connecting siloed data to highlight organizational relationships. Along with inclusion on compliance or sanctions lists, this increases visibility into potential conflicts."
- **Conflicts Clearance module**: "stakeholders must be apprised of the results and given details of any ethical or compliance issues … multiple methods for distributing, clearing, and auditing the resolution."
- **Advanced search**: "Advanced features like synonym creation and application eliminate complex queries and conflict analysis, providing relevant results in one query."
- **Corporate intelligence**: "Seamless connection to Dun & Bradstreet, World-Check One, and Bureau van Dijk reveals corporate affiliations and third-party risks." Ebook: "search terms that cover an entire corporate tree or any portion thereof"; a sister application "pulls company and corporate family tree data from external data service providers and automatically refreshes the data."
- **Interactive clearance** (ebook): the conflicts team selects hits "on one screen and click[s] a single email button to send a message to each matter attorney that contains the request, along with the matter number and related details … Conflicts Manager maintains their replies, keeping a clear audit trail"; "Conflicts attorneys can also work through the dashboard to clear their own conflicts." Heritage alternative documented: firms that "forward PDF reports to the requesting attorney — with hundreds of hits to be cleared before they can open the matter."
- **Information barriers**: with iManage Security Policy Manager (separate product), search results show "an icon indicating any clients or matters having an applicable information barrier"; "as the need for new barriers [is] identified … policy updates [can be accomplished] without leaving the application." Ebook title: "Using conflicts results to drive the creation of information barriers that protect clients."
- **Re-screening / delta** (customer story): "Conflicts Manager automatically tells me what's changed since the last time I ran the search — so, for example, I can focus on 3 new entries rather than all 10,000 hits"; "I have a conflicts search that I'm required to do on a bi-monthly basis for a particular client to adhere to our obligations of independence for that client."
- **Heritage** (customer story): the firm's "existing conflicts system, which was embedded in their finance system, was not powerful enough"; information "once 'scattered' across various text fields … has become fully rationalized"; "the management of corporate affiliations and the firm's relationships within those corporate families has gone from manual to highly automated."
- **Intake integration**: "When a request comes to the conflicts team, the conflicts application is right there inside the intake form."
- Product-page feature bullets: "Comply with jurisdictional regulations by adapting checks to the type of work requested"; "Set up process workflows for information barriers, business acceptance, conflicts checks, and sanctions monitoring."
- Brochure phrase: "a sophisticated conflicts check solution that provides firms with a 360-degree view of all types of conflicts, automated issue spotting, interactive multi-device clearance options, and comprehensive audit history."
- Users (FAQ): "professionals responsible for new client onboarding that involves conflict of interest searches, clearances, and business intake."

### Aderant Conflicts / Expert Conflicts (evidence layer A for positioning; B for mechanics)

- Standalone product (official site text via search index): "Aderant's easy-to-use cloud native risk management solution providing comprehensive conflicts review and clearance capabilities."
- Official on-demand recording page: "Aderant Conflicts has been rewritten to become a modern, simple-to-use solution with enhanced functionality … improved search request methods, hit analysis, effective decisions, and workflows to support auditable records of considered searches across Aderant Expert considerable data sets."
- Expert Sierra feature list (official): "Conflicts Check, File Opening" listed alongside client/matter management and billing — suite-embedded packaging.
- News release (official): "Expert Conflicts minimizes the risk firms' face when taking on new business by thoroughly searching for any potential conflict of interest. Its powerful search engine, robust inquires, and comprehensive reporting enables professionals to quickly and accurately determine which engagements to accept and which to decline."
- Tier 3 mechanics (wifitalents/gitnux/zipdo — moderate confidence): "links pre-opening searches directly with the firm's Aderant Expert client and matter records"; "party and entity search with normalization for names, aliases, and variations"; "conflict clearance workflow ties screening results to opening decisions with an audit trail of search activity"; "role-based conflict rules"; "lateral conflict checks"; "Name normalization and alias matching help reduce variation issues like nicknames and common corporate suffix patterns."

### Clio Manage / Grow conflict checks (evidence layer A — official help articles)

- Definition (help article): "you can run a conflict check against your existing contacts and matters as you take on new work. A conflict check searches the names, contact details, and other identifying information you provide, and lets you mark each result with a conflict status. Closing the check generates a report that your firm can share, download, and associate with a matter, providing a record of the diligence you performed."
- Entry routes: global search bar; Contacts > Conflict checks subtab; matter dashboard; during matter creation ("Save and run conflict check"); during lead intake (Clio Grow).
- Search construction: subject type (Person / Company / Keyword); Flex search (variation-tolerant) vs Exact search; name variations for first/middle/last/company; search categories (calendar events, notes, document names, communication logs); up to ten individual searches per check (e.g., known adverse parties).
- Results handling: per-result "Mark conflict status" dropdown + "Add note"; then "Close and generate report" with overall conflict status and comments; PDF report; CSV export.
- Check history: Contacts > Conflict checks lists "information about each check, the associated matter, if any, the firm user who ran it, when they ran it, and the status they assigned"; reports re-downloadable; checks can be linked/unlinked to matters.
- Gating semantics: next-step guidance — "Create Contacts: Add the contact once the conflict check comes back clear. Create Matters: Open the matter you ran the conflict check for."
- Administration: search preferences set by firm users with Administrator/General Access permission, applying firm-wide.
- What is absent: no dedicated party/relationship database beyond the firm's own contacts/matters; no clearance workflow routing; no corporate-tree expansion; no walls; no monitoring.

### PracticePanther conflict check (evidence layer A — official help article)

- "You can run conflict checks from anywhere in the software to avoid any sticky situations!"
- Mechanics: "Use the top left search bar and search for any name or keyword … Click 'Run Full Search'. This will search through the entire software in one click. You can search through all your internal notes, tasks, events, emails, contacts, matters, and even custom fields!"
- That is the entire documented feature: a full-text search over the firm's records. No status marking, no report, no retained check record, no clearance workflow.

## Cross-product Comparison

| Dimension | Intapp Conflicts | iManage Conflicts & Intake | Aderant Conflicts | Clio | PracticePanther |
|---|---|---|---|---|---|
| Searchable universe | Unified client/engagement/relationship data, enriched (corporate trees, industry codes, employee interests) | Siloed firm data connected; own Conflicts Manager database + Corporate Intelligence refresh | Aderant Expert client/matter data sets | Firm's existing contacts and matters | Entire software (notes, tasks, events, emails, contacts, matters, custom fields) |
| Name-variation handling | normalization + matching logic (Tier 3) | synonym creation/application | normalization, aliases, variations (Tier 3) | Flex vs Exact search, name variations | none documented |
| Corporate-tree expansion | yes (third-party corporate trees) | yes (entire tree or any portion; D&B/BvD/World-Check feeds) | not evidenced | no | no |
| Check as retained record | "history of every conflicts search and outcome"; auditable record | audit trail; re-run deltas vs last search | "auditable records of considered searches" | check record + PDF report + CSV; history list with who/when/status | no retained check documented |
| Hit disposition | status decisions; notes; documented resolutions; clearance summaries (AI-drafted) | interactive clearance; email distribution to matter attorneys; replies tracked; dashboard clearing | "hit analysis, effective decisions"; clearance workflow (Tier 3) | per-result status dropdown + note; overall report status | none |
| Waiver/consent machinery | "waiver handling" (Tier 3 only) | clearance distribution incl. "ethical or compliance issues" details | not evidenced | status options (unspecified) | no |
| Intake/matter gating | initiate from Intapp Intake/DealCloud | conflicts application "right there inside the intake form"; Business Intake module tier | pre-opening searches tied to matter opening; "File Opening" pairing | "Save and run conflict check" at matter creation; create contact/matter once clear | none |
| Re-screening / monitoring | Celeste continuous monitoring | delta re-runs ("what's changed since last time"); bi-monthly independence re-screen | not evidenced | no | no |
| Ethical walls | reports filtered by Intapp Walls policies (Walls = separate product) | barrier icons in results; policy updates in-app (SPM = separate product) | not evidenced | no | no |
| Sanctions/compliance lists | not on product page | included in search scope | not evidenced | no | no |
| Employee/personal conflicts | via Employee Compliance integration | not evidenced | not evidenced | no | no |
| Industry scope | legal, accounting, consulting, financial services, private capital | law firms, accounting, consulting, financial services, government | law firms | law firms | law firms |
| Packaging | standalone product in a suite | tiered modules (Checks / Clearance / Intake) | suite module + standalone cloud product | capability inside LPM | capability inside LPM |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures over one binding:

1. **The relationship universe of record** — the organization's own accumulated records of clients, adverse parties, and related parties (its professional relationships, however held: a dedicated enriched conflicts database, or the firm's contact/matter records) that constitutes the searchable universe of "who this organization is or has been involved with." Remove → generic enterprise search / contact database.
2. **The conflict check as a structured, retained screening event** — a prospective party/matter's identifying details (names, and commonly emails/phones/addresses/keywords) searched against that universe with name-variation handling, producing match hits for review, and retained as a check record with a report/audit trail. Remove → one-off lookup, or a search with no memory.
3. **The recorded disposition** — hits and/or the check receive an explicit recorded status/decision (cleared / conflict found / waived-with-consent / declined — exact vocabularies vary) that gates acceptance of the new work and constitutes the diligence record. Remove → a search engine over firm records (the PracticePanther pole — a capability, not the platform).

Binding: professional-conflict-of-interest semantics — the universe is the organization's OWN relationship records, and the check gates the acceptance of new work under the organization's professional-responsibility/conflict rules. Remove the binding → sanctions screening (external lists) or generic entity resolution.

Jointly-held load-bearing:

- 1 alone = contact database / enterprise search
- 2 without 1 = search over nothing (or over external lists = sanctions screening)
- 3 without 1+2 = a decision log with nothing behind it
- 1+2 without 3 = search capability (LPM territory, not the platform Type)
- 1+3 without 2 = a database with decisions but no screening event
- 2+3 without 1 = screening over external lists (sanctions/AML territory)

### L1 — Common Mature Structure

- Clearance workflow: routing hits to matter attorneys/analysts for review, distribution (email/dashboard), replies tracked, audit trail of who decided what (iManage interactive clearance; Intapp decision documentation; Aderant clearance workflow [Tier 3]).
- Corporate-tree / corporate-family expansion of search terms (Intapp, iManage).
- Synonym/alias management and name normalization (iManage synonym creation; Clio Flex search; Aderant normalization [Tier 3]; Intapp matching logic [Tier 3]).
- Audit trails and defensibility reporting (all four dedicated products).
- Delta re-runs / re-screening against the last search (iManage "what's changed"; Intapp continuous monitoring at the AI pole).
- Integration with intake and matter opening (initiate from intake; gate matter creation) — all sampled products with a check record.
- Shareable reports (PDF; confidential-information filtering at Intapp).

### L2 — Variant / Optional Structure

- Third-party data enrichment (D&B, World-Check One, Bureau van Dijk; corporate trees, industry codes).
- Sanctions/compliance-list inclusion in the same search (iManage only in sample — variant).
- Employee/personal-interest conflicts via outside-business-interest data (Intapp + Employee Compliance).
- Lateral-hire screening (Intapp Celeste lateral search; Aderant lateral checks [Tier 3]).
- Ethical walls integration — the walls themselves are separate products (Intapp Walls, iManage Security Policy Manager); conflicts results can trigger wall creation.
- Industry variants: accounting independence, consulting competitive/commercial conflicts, investment-banking deal conflicts, private capital — same product family, different regulatory frames.
- AI assistance: search-strategy building, hit triage, clearance summaries, continuous monitoring (Intapp Celeste; iManage Ask-iManage extraction).
- Joint client representation handling (Intapp Intake+Conflicts feature).

### L3 — Vendor-specific (research notes only)

- Intapp Celeste (agentic AI), Intapp Walls/Intake/Terms/Employee Compliance packaging, DealCloud initiation, "50% faster" claim (marketing).
- iManage Corporate Intelligence sister app, Conflicts Matter Description field, tiered module purchasing, multi-device clearance, Security Policy Manager icon integration.
- Aderant Conflicts standalone cloud product (JS site, details unverified); Expert Sierra bundling.
- Clio Grow lead-intake route; Flex/Exact naming; ten-search limit; CSV export; firm-wide preference administration.
- PracticePanther "Run Full Search" naming.

## Historical / Market-Sample Check (§24)

- **Pre-software form**: the firm's card/index file of clients and adverse parties (the relationship universe), the manual search of a new name through the file (the screening event), and the responsible lawyer's recorded judgment before opening the file (the disposition). Satisfies all three L0 legs with zero software — the definition is not software-era-bound.
- **Heritage software form**: conflicts embedded in finance/time-billing systems (iManage customer story: "existing conflicts system, which was embedded in their finance system, was not powerful enough"). Satisfies the core — packaging, not identity.
- **Capability floor**: PracticePanther's bare full-text search fails leg 3 (no retained disposition) — correctly excluded from the Type proper; it is the capability inside an LPM. Clio passes all three legs minimally (retained check + status + report) — the in-type lower bound.
- **Modern enterprise form** (AI agents, continuous monitoring, corporate-tree feeds) adds nothing definitional — all L1/L2.
- Conclusion: the L0 survives the historical check; no re-abstraction needed.

## Vendor-specific Findings

See L3 above. Notable packaging facts: Intapp ships Conflicts, Intake, Walls, Employee Compliance as separate products; iManage sells Checks/Clearance/Intake as purchasable tiers; Aderant ships both a suite module and a standalone cloud product. This packaging structure is itself evidence for the Type's independence from intake and from walls.

## Boundary Findings

1. **vs Legal Intake & Client Onboarding** — keep-both. Intake is the conversion system (prospective-client record → screening gate → engagement decision → onboarding closure); the conflicts platform is the screening machinery itself (universe + check + clearance). Intapp ships Intake and Conflicts as separate products; iManage sells Business Intake as a separate tier; the intake pass explicitly deferred "deep conflicts machinery" here. Seam: intake *requires* that a screening step can be performed and recorded; the conflicts platform *is* that step's machinery at depth.
2. **vs Law Practice Management System** — capability-vs-Type seam. LPM conflict checks are search capabilities over the firm's records (PracticePanther: bare search; Clio: structured check with status + report — the capability ceiling). The Type proper is the dedicated platform where the check is the center of gravity with clearance machinery, party-database depth, and defensibility reporting. Clio straddles: it passes the L0 legs but has none of the L1 clearance machinery. Disposition: keep-both; document Clio-class products as the embedded-capability realization of the same function.
3. **vs Sanctions Screening Platform / AML screening** — structurally similar name-matching, different universe and semantics: sanctions screens against EXTERNAL regulatory lists with no waiver semantics; conflicts screens against the organization's OWN relationship records with waiver/consent semantics and professional-responsibility purpose. iManage bridges (includes sanctions-list checking in the same product) — packaging convergence noted, not a merger of Types.
4. **vs Ethical walls / information barriers** — walls are access-enforcement structures over sensitive matters (Intapp Walls, iManage Security Policy Manager — both separate products). Conflicts results commonly *trigger* wall creation (iManage ebook: "Using conflicts results to drive the creation of information barriers"), and conflicts reports are filtered by wall policies — integration seam, not identity. No dedicated "ethical wall" leaf exists in the directory; the enforcement function belongs to security/access-governance territory. Recorded as a taxonomy observation, not a change.
5. **vs Legal Matter Management** — the conflicts platform consumes client/matter data as its universe but does not manage matters (no matter lifecycle, no documents, no money).
6. **Generalization note** — the same product family (Intapp, iManage) sells conflicts management to accounting (independence), consulting, investment banking (deal conflicts), and private capital. The legal instance is the canonical realization (professional-responsibility rules are the sharpest frame); the directory placement under Legal is sound, but the Type generalizes to professional-services conflicts management. No directory change made.

## Uncertainties

- Exact disposition vocabularies per product (status names, waiver states) — not article-verified for Intapp/iManage/Aderant (gated or JS-only docs); held at the conceptual level ("recorded status/decision; exact labels vary by product").
- Depth of waiver/consent machinery — moderate evidence only (Tier 3 for Intapp "waiver handling"; iManage clearance distribution documented but waiver specifics not).
- Whether continuous monitoring is now standard at the enterprise tier — observed at Intapp (Celeste) and as delta re-runs at iManage; universality not claimed.
- Aderant standalone Conflicts internal mechanics — unverified (JS app).
- Adoption statistics (e.g., "89% of 50–99-lawyer firms") — Tier 3, not promoted.
- Thomson Reuters Elite/3E Conflicts — not sampled; the heritage "conflicts in the finance system" pattern is evidenced via the iManage customer story instead.

## Final Synthesis

A Legal Conflict Checking Platform is the professional organization's conflict-of-interest screening system of record. Its defining core is three jointly-held structures: the relationship universe of record (the organization's own accumulated records of clients, adverse parties, and related parties — the searchable universe of who the organization is or has been involved with), the conflict check as a structured retained screening event (a prospective party/matter's identifying details searched against that universe with name-variation handling, producing hits for review, retained with a report/audit trail), and the recorded disposition (explicit status/decision on hits and the check — cleared / conflict / waived / declined — that gates acceptance of the new work and constitutes the diligence record). Around this core, mature products standardize clearance workflow routing, corporate-tree expansion, synonym management, delta re-screening, intake/matter-opening integration, and defensibility reporting; enrichment, sanctions-list inclusion, employee-interest conflicts, lateral-hire screening, walls integration, industry frames, and AI assistance are variants. The market realizes the Type across a packaging spectrum — dedicated enterprise platforms (Intapp, iManage), suite modules and standalone products (Aderant), and embedded LPM capabilities (Clio at the ceiling, PracticePanther below the platform floor) — while intake, walls, and matter management remain separate Types that this one feeds and gates.
