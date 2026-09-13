# Research Notes — Deal Management for Private Equity / VC

## Research Goal

Understand what "Deal Management for Private Equity / VC" software actually is as an Application Type: what objects exist inside it, who uses it, how a deal moves through it, and where its boundaries lie against CRM, fund administration, investor portals, data rooms, and investment research platforms.

## Initial Boundary

Initial hypothesis: this is the investment firm's (GP-side) front-office system of record for sourcing, tracking, and executing investment deals — a CRM-shaped product whose "customer" is a company/investment target rather than a buyer, and whose pipeline ends in an investment decision rather than a sale.

Neighboring Types to watch:
- Customer Relationship Management / CRM (sales pipeline)
- Private Market Investment Platform (investor-side allocation)
- Investor Portal (LP-facing delivery surface)
- Cap Table Management (company ownership ledger)
- Virtual Data Room / Due Diligence Platform (deal-time document exchange)
- Investment Research Platform (market data)
- Fund Administration Platform (books of record)
- Real Estate Investment Management (sibling, property deals)

## Research Questions

1. What is the central record? (Deal / Opportunity / Company?)
2. What does a pipeline look like — who defines stages, what are typical stage vocabularies?
3. How do people/companies relate to deals?
4. How does activity/relationship data enter the system (manual vs auto-capture)?
5. What happens after "closed" — does the record become a portfolio record?
6. What roles exist (analyst, partner, IC, IR)?
7. What is relationship intelligence and is it definitional or common?
8. Where does the boundary with generic CRM break?

## Representative Products

- **Affinity** — relationship-intelligence CRM for dealmakers (VC/PE/IB); strongest Tier-1 documentation (public help center + tutorial library)
- **Intapp DealCloud** — enterprise "more than a CRM" for private capital, IB, legal; Tier-2 product pages (help center gated)
- **4Degrees** — relationship-intelligence CRM built by ex-investors for PE/VC/M&A; Tier-2 product pages
- **Dynamo (Backstop heritage)** — end-to-end alternative-investments platform with a CRM & Deal Management module; Tier-2 product pages (suite context)

Selection rationale: market representation (VC-native vs enterprise private-capital vs suite module), different product philosophies (relationship-intelligence-first vs configurable enterprise vs suite), different customer tiers (boutique VC to global PE).

## Sources

- Affinity Help Center: https://support.affinity.co/hc/en-us , llms.txt index, Tutorial 5 (Pipeline Basics), Tutorial 9 (Building Your Pipeline), Tutorial 6 (Relationship Intelligence), Lists/Profiles/Opportunities articles — fetched 2026-09-10 (Tier 1)
- Intapp DealCloud: https://www.intapp.com/dealcloud/ , /dealcloud/pipeline-deal-management/ , /private-capital/ — fetched 2026-09-10 (Tier 2)
- 4Degrees: https://www.4degrees.ai/ , /crm , /relationship-intelligence — fetched 2026-09-10 (Tier 2)
- Dynamo Software: https://www.dynamosoftware.com/ , /products/crm-deal-management/ — fetched 2026-09-10 (Tier 2; /products/backstop/ returned 404)

## Product A — Affinity

### Key observations (Evidence layer A — directly observed in official help center)

- Core objects: **Organizations** (companies), **People** (contacts), **Lists** (curated collections of entities), **Opportunities** (separate record type for complex deals), **Notes**, **Reminders**.
- A pipeline is "a list with a Status field that defines the stages a deal moves through"; Board view renders Status as Kanban columns; dragging a card updates the Status.
- Opportunities vs list entries: list entries for simple tracking; Opportunities for deals "with multiple parties and financial terms" — fields include Name, Stage, Owner, Expected Close Date, Amount; linked to multiple people + companies.
- Stages are firm-configurable; documented example VC pipeline: Sourced → Initial Review → Partner Meeting → Due Diligence → Term Sheet → Closed Won → Passed; example PE pipeline: Identified → Initial Screen → Management Meeting → Diligence → IC Approval → Closed → Declined. Each list has its own Status field/stages.
- **Relationship Intelligence**: email + calendar sync (Gmail/Outlook) auto-captures interactions; connection strength scoring; warm-intro path finding ("find the strongest path to a target through your team's network"); inferred connections; interaction timeline on profiles.
- Data enrichment: third-party data (Crunchbase, Dealroom) integrated into lists; enriched/global/list-specific fields.
- Pipeline analytics: funnel analysis, stage velocity, days-in-stage via Analytics, win ratios, probability-adjusted forecasting, deal health scoring.
- Automation: status triggers, opportunity triggers, reminders, required fields, list movement automations.
- Access control: **Restricted Opportunities** — "keep sensitive deals in your shared pipeline while limiting who can see them"; list sharing permissions; admin controls.
- Use-case recipes span deal sourcing, deal management, fundraising/IR (LP tracking), portfolio operations — the same product serves the whole front office.
- Data quality: duplicate merge, auto-created contacts from email sync.

## Product B — Intapp DealCloud

### Key observations (Evidence layer A on product pages / B for structure)

- Positioned "More than a CRM" for private capital (PE, VC, private credit, fund of funds, family offices, LPs), investment banking, legal, accounting.
- Pipeline and deal management module: "comprehensive views of every deal moving through the pipeline", "central hub for pipeline and deal execution", "visualize and prioritize the pipeline in real time".
- Tracks "sourcing, progress, and staffing details" across "the entire deal and client lifecycle"; automated task workflows, notifications, AI-generated signals; configurable reporting; ad hoc and templated reports.
- Relationship management (CRM) module is a sibling capability; relationship intelligence, Microsoft 365 add-ins, mobile app, integrations with market-data providers (Preqin, PitchBook, FactSet, S&P, SourceScrub, etc.).
- Fundraising and investor relations is a separate module — confirms IR/LP management is adjacent, not the deal core.
- Compliance modules (conflicts, intake, walls) sold separately — deal conflicts of interest is a private-capital-specific adjacent product.
- Highly configurable per firm ("configure DealCloud to meet your specific requirements and processes").

## Product C — 4Degrees

### Key observations (Evidence layer A on product pages / B for structure)

- "AI-powered CRM for private-market deals and the relationships that drive them"; built by ex-investors; industries: PE, VC, IB/M&A, corp dev, CRE, consulting.
- CRM: deal pipeline management; email/calendar/third-party sync (Crunchbase, PitchBook) auto-populates deal and contact records; "eliminate manual CRM entry".
- Relationship intelligence: relationship strength scoring, warm-intro finding, alerts on job changes/news, stale-relationship reminders.
- Reporting: business development analytics, sourcing data, portfolio KPIs.
- Extensions: Gmail/Outlook, LinkedIn, Chrome; Salesforce overlay product.
- Marketing claim "80%+ of VC and PE deals are sourced from firm networks" — vendor claim, not adopted as fact.

## Product D — Dynamo

### Key observations (Evidence layer A on product pages / B for structure)

- End-to-end alternative-investments platform: CRM & Deal Management is one module among investor relations, fundraising, portfolio monitoring & valuation, fund accounting, fund administration, research management.
- CRM & Deal Management: "drive deals toward the finish line"; consolidates deal and contact information (client testimonial); configurable modules and dashboards.
- Serves GPs (PE/VC), LPs/allocators, funds of funds, service providers — the deal-management core is the GP-side CRM module; the rest of the suite is adjacent Types.
- Confirms the pattern: deal management is the front-office CRM layer of a broader private-capital stack.

## Cross-product Comparison

| Dimension | Affinity | DealCloud | 4Degrees | Dynamo |
|---|---|---|---|---|
| Central record | Organization/Person entities + Opportunity | Deal/company/contact objects (configurable) | Deal + contact records | Deal + contact (CRM module) |
| Pipeline | List + Status field, Board view, firm-defined stages | Configurable pipeline views, real-time | Deal pipeline with stages | Configurable pipeline |
| Stage vocabulary | Firm-configurable; documented VC & PE examples | Firm-configurable | Configurable | Configurable |
| Activity capture | Auto email/calendar sync (defining feature) | Automated data entry, integrations | Auto email/calendar/third-party sync | Data automation module |
| Relationship intelligence | Core differentiator (warm intros, connection strength) | Relationship intelligence capability | Core differentiator | Present (AI auto-tagging contacts) |
| Market data integration | Crunchbase, Dealroom | Preqin, PitchBook, FactSet, S&P, etc. | Crunchbase, PitchBook | Data automation |
| Post-close | Portfolio operations recipes | Portfolio/financial systems integration | Portfolio KPI reporting | Portfolio monitoring module |
| IR/fundraising | Same product, separate recipes | Separate module | Same product | Separate module |
| Access control | Restricted opportunities, list sharing | Enterprise compliance-grade | Security posture page | Enterprise |
| Packaging | Standalone CRM | Suite ("more than a CRM") | Standalone CRM | Suite module |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The investment firm's deal-flow system of record. Minimal structure:

1. **Deal/opportunity record** — a persistent identified record for a prospective investment (company, round, asset, or transaction), owned by a firm member, carrying firm-defined attributes (stage, owner, amounts/dates where relevant).
2. **Firm-defined pipeline stages** — the deal moves through a stage sequence the firm configures, ending in an invested/passed disposition; the stage state is the primary workflow driver.
3. **Counterparty records** — companies and people held as first-class records, associated with deals; the firm's cumulative network of counterparties persists across deals.
4. **Persistent deal history** — activities, notes, documents, and stage transitions accumulate on the deal and counterparty records.

Remove the deal record + pipeline → generic contact manager. Remove counterparty records → bare task tracker. Remove persistence → meeting notes. Remove the investment-firm framing (stages ending in invest/pass, counterparties as investment targets) → generic sales CRM.

### L1 — Common Mature Structure

- **Relationship intelligence** — auto-captured email/calendar interactions, connection strength, warm-introduction paths across the team's network (all four sampled products; Affinity/4Degrees make it the headline)
- **Activity auto-capture** — email/calendar/third-party sync populating records without manual entry
- **Board/Kanban pipeline views, saved views, filtering**
- **Pipeline analytics** — funnel, stage velocity/dwell time, win ratios, forecasting
- **Notes, reminders, tasks, document attachments**
- **Data enrichment** from market-data providers
- **Team collaboration** — shared lists, mentions, assignment
- **Access control on sensitive deals**

### L2 — Variant / Optional

- Asset-class tuning (VC round-based vs PE buyout vs growth vs fund-of-funds manager tracking vs private credit)
- IC/approval workflow formalization (stage-gated, task workflows)
- Post-close portfolio tracking depth (from light KPIs to full portfolio monitoring modules)
- Fundraising/IR and LP relationship management (same product or separate module)
- Deal conflicts/compliance (separate products in the enterprise tier)
- AI capabilities (deal summaries, AI chat, agents)
- Mobile, browser extensions, Outlook/Gmail add-ins
- Deployment: SaaS standard; configurability depth varies (boutique out-of-box vs enterprise configured)

### L3 — Vendor-specific

- Affinity: Lists/Opportunities duality, connection-strength scoring, Ascend agents, Notetaker, Restricted Opportunities mechanics, Crunchbase/Dealroom field enrichment
- DealCloud: DataCortex, Intapp Data, Dispatch, Celeste AI, experience management, conflicts/walls suite
- 4Degrees: 4,000+ signals claim, Salesforce overlay, Chrome X-ray extension
- Dynamo: Backstop heritage, HoldingsInsight, DynamoAI, fund accounting integration

## Vendor-specific Findings

See L3 above; none promoted to the canonical core.

## Boundary Findings

- **vs CRM (sales)**: same skeleton (accounts/contacts/opportunities/pipeline), but the operator, object of pursuit, and pipeline semantics differ: a firm investing capital into companies vs a vendor selling to customers; stage vocabularies end in invest/pass, not won/lost revenue; relationship intelligence is oriented to sourcing and diligence, not quota. Remove the investment framing → CRM.
- **vs Private Market Investment Platform**: that Type is investor/LP-side (allocating into funds/deals); this Type is GP/deal-team-side (running the firm's own deal flow). Record owner flips.
- **vs Investor Portal**: external LP-facing delivery surface vs internal deal-team workbench.
- **vs Cap Table Management**: one company's ownership ledger vs the investor firm's deal pipeline.
- **vs Virtual Data Room / Due Diligence Platform**: deal-time document exchange/assessment vs the standing pipeline system; a deal-management record may reference a data room but does not host it.
- **vs Investment Research Platform / market data**: third-party data is integrated as enrichment; the market database itself is a different Type.
- **vs Fund Administration Platform**: books of record for the fund vs front-office deal flow.
- **vs Real Estate Investment Management**: sibling; property deals that mature into held-asset records with property-anchored value/returns content; this Type centers company/security deals in investment-firm terms.
- **Historical check**: pre-relationship-intelligence era (spreadsheets, early deal CRMs, Backstop-style contact+deal databases) satisfies L0 without auto-capture or warm-intro scoring — relationship intelligence is L1, not definitional. Regional/smaller funds using generic CRMs configured for deals sit on the boundary; the defining difference is the investment-firm object world, not the vendor.

## Uncertainties

- DealCloud and Dynamo help centers are gated; their internal object models are asserted at structure level only (Tier-2 evidence).
- Exact stage vocabularies are firm-configurable everywhere; no industry-standard stage set is asserted.
- "80%+ of deals sourced from networks" is a vendor marketing claim (4Degrees), not adopted.
- Packaging boundary is blurry in market practice: suite vendors bundle deal management with IR, portfolio, and accounting; the Type boundary is drawn on the deal-flow core, not the bundle.

## Final Synthesis

Deal Management for Private Equity / VC is the private-capital investment firm's front-office deal-flow system of record: deal/opportunity records moving through firm-defined pipeline stages toward an invest/pass decision, bound to persistent company and people records that constitute the firm's counterparty network, with accumulating activity history. Mature products add relationship intelligence (auto-captured interactions, warm-intro paths), pipeline analytics, enrichment, collaboration, and access control; suites extend the same core with IR, portfolio, and compliance modules. The defining core is deliberately smaller than any modern product's feature set: a spreadsheet-era deal list with contacts and stage columns satisfies it.
