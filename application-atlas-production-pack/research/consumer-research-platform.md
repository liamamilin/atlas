# Research Notes — Consumer Research Platform

Research date: 2026-09-07
Leaf: Consumer Research Platform (DIRECTORY.md §06 Marketing, Advertising & Growth)
Slug: consumer-research-platform

## Research Goal

Understand what a Consumer Research Platform actually is as an Application Type: its core objects, its canonical workflow, who uses it, how results are produced and consumed, and where its boundaries lie against the neighboring Types in §06 (Market Research Platform, Research Panel Platform, Competitive Intelligence Platform, Social Listening Platform) and against Survey Platform (§03.11) and Voice of Customer Platform (§07).

## Initial Boundary (hypothesis before research)

- Core use: brand-side teams self-serve research about consumers — attitudes, behaviors, preferences, brand/category/product perceptions — by fielding structured questions to consumer audiences and turning answers into decision-ready insight.
- Likely neighbors: Market Research Platform (study-lifecycle tooling), Research Panel Platform (manages a standing member population), Survey Platform (instrument authoring/fielding without supplied audience), Social Listening (passive observation), Voice of Customer (feedback from existing customers).
- Open questions going in: does the platform have to own the audience? How does a syndicated-data product (query pre-fielded studies) fit the "field a study" model? Is this leaf distinguishable from Market Research Platform at all?

## Research Questions

1. What are the core objects? (study/survey, audience, question, result/insight)
2. Where does the audience come from, and is audience access part of the product?
3. What is the canonical workflow from research question to decision?
4. What methods exist beyond plain surveys?
5. How are results analyzed, visualized, shared?
6. Who uses it (roles), and in what context?
7. Where are the boundaries vs panel platforms, MR platforms, survey tools, VoC, listening, CI?
8. How does the syndicated-data model (pre-fielded studies you query) relate to custom fielding?

## Representative Products

Selected for market representativeness, documentation quality, differing product philosophies, and differing customer tiers:

| Product | Self-labeling (from official site) | Philosophy pole | Customer tier |
|---|---|---|---|
| Attest | "AI Consumer Insights Engine for B2C Brands" | self-serve DIY research with integrated panels + human research support | brand/insights teams, mid-market→enterprise |
| GWI | "Global Consumer Insights / human insights platform" | syndicated consumer dataset queried in-platform (+ custom research services) | brands & agencies, enterprise |
| Appinio | "Insights for everyone — global market research powered by AI" | proprietary mobile-first consumer panel + speed | SMB→mid-market teams |
| quantilope | "Consumer Intelligence Platform for Automated, AI-Powered Research" | automated advanced-method toolkit (conjoint, MaxDiff, TURF…) | enterprise insights teams |
| Suzy | "Suzy Decision Engine — AI-Powered Consumer Insights" | all-in-one decision engine (signals + insight query + deliverables) | enterprise brands |

## Sources

Tier 1 (official operational documentation — reached):

- Attest Help Center — https://help.askattest.com/en/ (collections: Getting Started; Building surveys ×28; Audience and targeting ×10; Analysing results ×26; Managing surveys ×13; Data Quality and methodology ×5; Account and collaboration ×13; APIs and MCPs)
  - "Getting started with your first survey" — https://help.askattest.com/en/articles/3494059
  - "Selecting demographics for your survey" — https://help.askattest.com/en/articles/3185429
  - "Sending surveys to your own audience" — https://help.askattest.com/en/articles/1273473
  - Collection indexes for Building surveys / Analysing results / Audience and targeting / Data Quality and methodology
- GWI Help Center — https://help.globalwebindex.com/en/ (collections: Our products ×23; Our data ×70; Metrics and interpretation ×15; Releases ×63)
  - "Using GWI data sets" — https://help.globalwebindex.com/en/articles/5880937

Tier 2 (official product pages — positioning, module boundaries):

- Attest — https://www.attest.com/ (redirects to askattest.com) — platform overview: Attest Measure / Attest Explore / Compass; use cases (brand tracking, campaign tracking, concept testing, consumer profiling, creative testing); teams (insights/marketing/brand/product)
- GWI — https://www.gwi.com/ , https://www.gwi.com/platform , https://www.gwi.com/data — Audiences (250K+ profiling points), Charts, Dashboards, Crosstabs, Agent Spark, Canvas, custom research, API; data: 50+ markets, 2M+ interviews annually, 4 waves/year, panel partners
- Appinio — https://www.appinio.com/en , /en/how-it-works/survey-platform , /en/how-it-works/panel-app — AI survey platform, Boards, proprietary panel app (gamification, Data Shield quality machinery), expert guidance, Conversations
- quantilope — https://www.quantilope.com/en — CI Advanced / CI Tracking / quinn; 16 automated methods; solutions (ad/brand/concept/pricing/packaging/segmentation + tracking); panel network
- Suzy — https://www.suzy.com/ , /intelligence , /insight — Decision Engine: Intelligence (Signals feed), Insight (unified data/docs + query), Impact (deliverables)

Source-access limitations:

- Suzy operational documentation could not be reached: help.suzy.com failed (transport error); suzy.com pages are marketing-only; Suzy Academy requires login. Suzy observations are therefore positioning-level (Tier 2) and all Suzy-specific claims in the final document are kept weak/qualified.
- Panel ownership/sourcing for Attest ("Attest panels") and quantilope ("trusted panel network") is not publicly documented in operational detail; treated as "platform-supplied audience" without asserting ownership structure.
- Vendor marketing numbers (150M+ consumers, 38M+ panelists, 300M+ network, 2M+ interviews, 35BN data points, 8.5k attributes, 190+ markets, 50+ markets) are recorded here as vendor claims only; none are asserted as operational facts in the final document.

## Product Observations

### Attest (evidence layer: A — direct, Tier-1 help center)

Platform composition (site): Attest Measure (quantitative surveys), Attest Explore (AI-moderated interviews, Beta), Compass (conversational AI co-pilot for creation/analysis). Positioning: "AI consumer insights engine for global B2C brands"; use cases: brand tracking, campaign tracking, concept testing, consumer profiling, creative testing; teams: insights, marketing, brand, product.

Canonical survey workflow (help center, "Getting started with your first survey"):

```text
Create new survey (editor)
→ Draft: name (public/internal), research type, questions + text cards,
  media (image/audio/video), qualifying questions at start,
  groups + randomisation, routing (map view) + display logic (list view),
  preview, shareable draft link, comments, Compass AI first draft
→ Audience tab: country + language; source = Attest panels | own audience | hybrid;
  pre-set audiences (e.g. Working Age Nat Rep) or custom;
  demographic filters; quotas (percentage per group); sample size; live pricing
→ Review tab: launch now or schedule; Confirm and purchase
→ (after purchase surveys cannot be edited)
→ Results: live dashboard as responses arrive
```

Audience model (help center):

- Audience page is a first-class step; three sourcing modes: Attest panels / own audience / hybrid.
- Demographic targeting: country + language + filters (age incl. specific ages, gender, region, household income, home ownership/housing type, parental status incl. children's age/gender, pets, education, relationship status, employment type/sector, professional experience; US-only: DMA, ethnicity, Hispanic/Latino origin). Availability varies by country.
- Real-time "Available sample" (feasibility) updates as filters are applied.
- Demographic quotas: set percentage per demographic group.
- Qualifying questions: screen in/out at survey start when an attribute is not available as a demographic filter; affect feasibility and fill speed.
- Multiple audiences per survey (multi-market research); preset audiences savable/reusable; sample size calculator; excluding previous respondents; survey fill speed surfaced.
- Own audience mode: customer distributes link (email/CRM), pseudonymised respondent IDs link responses to uploaded CSV/JSON audience data; no demographic targeting in this mode; max responses per audience; one-or-many responses per device; close/extend; privacy notice shown; optional logo; credits deducted per response.
- Hybrid: combine panel audiences with own audience in one survey.

Analysis model (help center collection index + article titles):

- Charts (create/edit), visualisation choices, filtering, crosstabs, segments, merging answer options, grid/ranked/open-text analysis, sentiment analysis, AI summaries for qualitative data, AI key insights, AI story generation, Boards (data stories, funnel charts), uploading own segmentations, multi-wave result analysis, qualitative video response analysis, statistical significance calculator, Key Findings, exports (Excel incl. multi-tab, PowerPoint, CSV), copy/paste from dashboard.

Quality machinery (Data Quality and methodology collection): Attention Checker, audience + automated quality checks, manual quality checks, duplicate-participant prevention, respondent NDA.

Other: APIs and MCPs collection (data into customer toolstack); Customer Research Team / Customer Research Manager (human support); credits-based purchasing.

### GWI (evidence layer: A for data-set/platform mechanics via help center; B for positioning)

Positioning (site): "Global Consumer Insights"; platform = "human insights platform"; FAQ self-describes as a "consumer research platform" distinct from generic "market research tools". Users: marketing, sales, product, research teams; agencies; media; sports; gaming; finance.

Data model (help center, "Using GWI data sets"):

- Syndicated datasets produced by GWI's own continuously fielded surveys: primary data sets (GWI Core — global internet users; GWI USA; GWI Kids) and add-ons (recontact studies of Core: Pulse, Core Plus, Travel, Luxury, Moments, Alcohol, Automotive, Sports, Work, Gaming, Consumer Tech).
- Comparability rules: Core + add-ons combinable; primary↔primary and add-on↔add-on not directly comparable (different samples/audiences).
- Recruitment via "trusted panel partners"; respondents answer in native language; expert translators; globally harmonized data for cross-market comparison.
- Vendor-claimed scale (marketing): 50+ markets, 2M+ interviews annually, 4 waves/year, 15+ years trended, 35BN data points.

Platform model (site + help center):

- Audiences: build target audiences from 250K+ profiling points (interests, attitudes, buying habits, demographics); pre-built GWI audiences; shared team audiences.
- Charts: custom charts comparing audiences/markets; Dashboards: shareable insight collections; Crosstabs: multi-dataset cross-analysis with rebase-to-audience-size mechanics; Canvas: presentation-ready slide generation.
- Agent Spark: conversational AI analyst over the datasets (configure data sets in chat; Core required when add-on active); also available inside customer LLMs.
- Custom research service: experts design and run bespoke studies ("GWI custom research extends the platform").
- API / integrations; respondent-level data (RLD); audience activation; data partnerships (fusions).

Key structural insight: in GWI the "study" is pre-fielded by the vendor continuously; the user's unit of work is the audience definition + query, not the questionnaire. Custom fielding exists but as a service layer. This is the syndicated pole of the Type.

### Appinio (evidence layer: A for product mechanics via detailed product pages; no public help center reached)

Positioning: "Insights for everyone"; "global market research powered by AI"; 3,000+ clients; industries CPG/fashion; roles page for teams.

Composition: Platform (AI-driven survey platform), Research excellence (advanced method toolkit), Appinio Boards (visual insight stories), Panel (proprietary consumer panel app), Expert guidance (research experts), Appinio Conversations (custom personas).

Platform page: AI generates/refines survey questions from a prompt (accept/reject/customize); dashboard shows results live as data is collected; splits, filters, open-text theme extraction; Boards turn data into stories.

Panel page: proprietary mobile-first panel app; gamification, daily polls, push notifications, activity bonuses; recruitment via referral/app-store/search/social ads; quality machinery "Data Shield" (Quality Score, geo-check, consistency tests, control questions, suspicious-behaviour detection, MFA; AI + human review); vendor-claimed scale: 190+ markets, 8.5k attributes, 2B+ opinions, 38M+ consumers.

Use cases: brand tracking, (psychographic) target group analysis, visual testing, pricing analysis.

### quantilope (evidence layer: A for method catalog via official site; B for workflow)

Positioning: "Consumer Intelligence Platform for Automated, AI-Powered Research"; "#1 market research technology" (Greenbook GRIT claim — vendor claim).

Composition: CI Advanced (automated advanced methods), CI Tracking (brand/ad/product-launch/satisfaction/trend tracking), quinn (AI co-pilot); quantilabs (client innovation hub); CEP generator (AI category entry points).

Method catalog (official Methods pages): A/B Test, A/B Pre-Roll, Conjoint (choice-based), inColor, NPS, Key Driver Analysis, MaxDiff, Mental Advantage, Mental Availability, Implicit (MAT/SIAT), Penalty Reward, Price Sensitivity Meter, Segmentation, TURF — 16 automated methods.

Solutions: advertising, branding, category exploration, claims, concepts, competitive landscape, consumer segmentation, packaging, pricing, product portfolio, shelf optimization + tracking family.

Audience: "300M+ consumers worldwide through quantilope's trusted panel network" (vendor claim); insights "<1 second after a survey response" (vendor claim). Client testimonials indicate enterprise insights teams replacing agency-commissioned studies (conjoint, ad testing) with the platform.

### Suzy (evidence layer: B — positioning only; operational docs unreachable)

Positioning: "Suzy Decision Engine — AI-Powered Consumer Insights". Three products:

- Intelligence: personalized "Signals" feed of consumer trends/cultural shifts/competitive moves; chat to dive deeper; attach signals to projects.
- Insight: unified workspace — store and query all project information (docs, PDFs, CSVs, Suzy Signals, chats) around a business objective; "customers always one click away" (validate with consumers).
- Impact: instant deliverable building for stakeholders.

Teams: marketing & brand, product, sales, insights. Testimonials indicate survey/creative evaluation/tracking use. Operational mechanics (survey builder, panel, analysis surfaces) not publicly documented — recorded as a source limitation.

## Cross-product Comparison

| Dimension | Attest | GWI | Appinio | quantilope | Suzy |
|---|---|---|---|---|---|
| Studied subject | consumers (B2C brand questions) | consumers/internet users globally | consumers | consumers | consumers + market signals |
| Audience substrate | own panels; own-audience mode; hybrid | panel partners + own continuous surveys | proprietary mobile panel app | trusted panel network | panel (not publicly documented) |
| Study model | user fields custom surveys (draft→audience→launch) | vendor pre-fields syndicated datasets; user queries; custom research as service | user fields custom surveys | user fields studies with automated method templates | user runs research + signals feed (docs thin) |
| Instrument | survey editor: question types, logic, media, qualifying, multi-wave | (pre-fielded questionnaire; user defines audiences/attributes) | AI-assisted survey builder | method-templated studies (conjoint, MaxDiff…) | not documented |
| Analysis surface | dashboard, crosstabs, segments, significance, AI summaries, Boards | audiences, charts, dashboards, crosstabs (rebase), Agent Spark | live dashboard, splits/filters, open-text themes, Boards | real-time dashboards, method outputs | Insight query layer; Impact deliverables |
| AI layer | Compass (draft/analyze), AI summaries, Explore interviews | Agent Spark analyst | AI question gen + analysis + Boards | quinn + automated methods | Ask Suzy / Signals |
| Quality machinery | attention checker, manual checks, dedup | harmonization, native-language, translators | Data Shield (geo/consistency/MFA…) | panel network quality (not detailed) | not documented |
| Storytelling/deliverables | Boards, PPT/Excel/CSV exports | Canvas slides, dashboards | Boards | dashboards/reports | Impact |
| Ongoing research | multi-wave surveys, brand/campaign tracking | trended syndicated waves (4/year) | brand tracking use case | CI Tracking products | tracking testimonials |
| Human support | Customer Research Team/Manager | analyst services, custom research | expert guidance | research experts (testimonials) | CSM (testimonials) |
| Data out | Excel/PPT/CSV, APIs/MCPs | API, RLD, audience activation, fusions | (not detailed) | (not detailed) | (not detailed) |

Stable across all five (Layer B): consumer as subject; structured questions answered by real consumers; platform-supplied consumer reach; analysis surface turning answers into decision-ready insight; AI assistance (era-typical); ongoing/tracking use; brand-side (non-agency-first) users.

Varies (Layer C → variants): who supplies the audience (owned panel vs partner network vs syndicated dataset vs customer's own list); whether the study is user-fielded or vendor-fielded-and-queried; method depth (plain surveys vs 16 automated advanced methods); qualitative extensions; signals/intelligence layers; deliverable generation; data activation.

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. **The consumer as the studied subject** — research questions are about people in their consumer role (attitudes, behaviors, preferences, brand/category/product perception). Remove → generic survey tooling or non-consumer research tooling.
2. **Structured studies fielded to real consumers** — the platform turns a research question into a structured instrument answered by sampled humans (not scraped/observed data). Remove → social listening / passive analytics.
3. **Platform-supplied access to consumers** — reaching the consumers is part of the product (owned panel, panel network/partners, or a continuously fielded syndicated dataset); the user does not recruit respondents. Remove → pure survey authoring tool (Survey Platform).
4. **Decision-oriented insight outputs** — answers come back as analyzed, shareable insight (dashboards, crosstabs, charts, reports, AI answers) for brand-side decisions, not as raw transcripts or a raw data pipe. Remove → sample marketplace / raw feed.

Historical/market-sample check (§24): older and differently positioned products — online panel companies with DIY survey tools (Toluna-class), YouGov-class syndicated+panel hybrids, SurveyMonkey Audience-class audience add-ons — all satisfy these four properties without any modern AI layer, without proprietary mobile panels, and without advanced-method toolkits. The definition does not depend on the current AI-era implementation. Passed.

### L1 — Common Mature Structure

- Audience targeting machinery: demographic filters, quotas, screening/qualifying questions, feasibility/available-sample feedback, sample-size calculation, representative presets (e.g., national-representative), multi-market/multi-audience studies, saved audiences.
- Study instrument: question types (single/multiple choice, grid, ranked, open text, scales), media in questions, routing/display logic, randomisation, templates, question libraries, translation/multi-language, multi-wave structure.
- Analysis surface: live results as data arrives; charts; crosstabs; segments/splits; filters; statistical significance; open-text analysis (themes/sentiment); AI summaries.
- Storytelling & delivery: boards/stories, dashboards, exports (spreadsheet/slides/CSV), presentation-ready output.
- Data-quality machinery: bot/fraud detection, attention/consistency checks, duplicate prevention, human review.
- AI assistance (era-typical): survey drafting, analysis summarization, conversational insight Q&A.
- Human research support: research experts / customer research managers alongside the tool.
- Ongoing research: brand/campaign tracking, multi-wave studies.

### L2 — Variant / Optional Structure

- Audience substrate: proprietary panel (Appinio) vs panel network/partners (quantilope, GWI) vs syndicated continuously-fielded dataset (GWI) vs customer's own audience distribution (Attest own-audience mode) vs hybrid.
- Syndicated vs custom: query pre-fielded harmonized datasets (GWI Core/add-ons with comparability rules) vs field your own study.
- Method depth: plain survey toolkit vs automated advanced methods (conjoint, MaxDiff, TURF, implicit association, PSM, key driver, segmentation).
- Qualitative extensions: AI-moderated interviews, video responses, research communities.
- Market-intelligence layer: trend/signal feeds adjacent to the study core (Suzy Intelligence).
- Deliverable generation: slide/story builders (Canvas, Boards, Impact).
- Data activation & supply outward: audience activation to ad platforms, respondent-level data, API/MCP access.
- Commercial model: credits per response, subscription/seat, per-study, service layers.
- Industry/segment tuning: CPG, media & entertainment, finance, retail; regional markets (US DMA/ethnicity demographics; DACH origin of Appinio; UK origin of Attest).

### L3 — Vendor-specific (kept out of the final document)

- Attest: Compass co-pilot; Attest Explore AI interviews; "Working Age Nat Rep" preset; credits deducted per response; one-year own-audience survey window; pseudonymised respondent-ID rule; US-only DMA/ethnicity demographics; flat cross-market pricing claim; Customer Research Manager role.
- GWI: Core/USA/Kids primary sets + recontact add-on model; 4 waves/year; rebase-to-audience-size mechanics in crosstabs; Agent Spark data-set configuration; Canvas; RLD; fusions.
- Appinio: Data Shield named machinery; panel-app gamification (daily polls, bonuses); Conversations personas; 8.5k attributes claim.
- quantilope: quinn; CI Advanced/CI Tracking product split; the specific 16-method catalog; quantilabs; CEP generator; BBHT (Better Brand Health Tracking).
- Suzy: Signals feed; Insight unified-query workspace; Impact deliverable builder; Suzy Academy.

## Rejected Findings

- "A consumer research platform must own its panel" — rejected. GWI recruits through panel partners; Attest supports own-audience and hybrid modes; the invariant is platform-supplied access, not ownership. (Also the §24 check: partner-supplied and syndicated models satisfy the Type.)
- "A consumer research platform is a survey tool with a panel attached" — rejected as under-abstraction: the analysis/insight layer (crosstabs, significance, segments, AI synthesis, storytelling) is as structural as the instrument; without it the product is a survey tool, not this Type.
- "Consumer research = qualitative communities" — rejected. Communities/qualitative extensions are variant layers in the sampled set, not the core; the sampled core is structured questions → quantified insight.
- "AI is definitional" — rejected. All five sampled products lead with AI in 2026, but the pre-AI generation of this Type (panel + DIY survey + dashboards) satisfies L0; AI is era-typical L1.
- "Consumer research platform = market research platform" — rejected as collapse: the sampled products are consistently consumer-subject-scoped with audience supply bundled; the MR-platform category (per the panel-platform pass) centers the study lifecycle and sample buying across subjects. Overlap is real and recorded as a boundary issue, not silently merged.
- Vendor scale numbers (panel sizes, market counts, data-point counts) — rejected for the final document: marketing claims, not operational evidence.

## Boundary Findings

1. **vs Research Panel Platform (§06, processed)** — the panel platform's managed object is the standing member population (recruit → profile → sample → field → record → reward → maintain); the consumer research platform's managed object is the study and its insight output, with the population as supply infrastructure. Test: remove the standing managed population → a consumer research platform still stands (GWI uses partners; Attest offers own-audience mode); remove the study tooling → a panel platform remains. This discharges the joint-review flag recorded by research/research-panel-platform.md §Boundary Findings #3 from this side; the panel side's characterization ("methods and analysis surfaces") is refined here into the four-property L0.
2. **vs Market Research Platform (§06 sibling, unprocessed)** — sharpest open seam. Working discriminator from this sample: consumer research platforms are consumer-subject-scoped and bundle audience access as product for brand-side teams; market research platforms (category usage per the panel pass) center the study lifecycle (design → field → analyze → report) and sample buying as a marketplace function, subject-agnostic, for research professionals. Several sampled products self-label with both vocabularies (Appinio: "global market research powered by AI"; quantilope: "market research technology" in GRIT framing), so the seam is commercially fuzzy. Flagged for joint review when market-research-platform is processed.
3. **vs Survey Platform (§03.11, unprocessed)** — survey platforms author/field instruments to arbitrary, non-persistent respondents and do not supply a consumer audience or a consumer-insight analysis frame. Test: remove platform-supplied consumer audience → survey platform. Attest's own-audience mode is the bridge case (instrument + analysis without supplied audience) — a variant, not the core.
4. **vs Voice of Customer Platform (§07)** — VoC manages feedback from an existing customer relationship (owned customers, feedback programs, closed loop); consumer research platforms study market consumers via sampled audiences, who need not be customers. Own-audience surveys of customers sit between the two; the study/insight frame (not the relationship) is what this Type manages.
5. **vs Social Listening Platform (§06)** — listening observes unsolicited public expression; this Type asks structured questions of sampled consumers. Different data nature (asked vs observed); complementary in practice.
6. **vs Competitive Intelligence Platform (§06)** — CI centers competitor/market tracking; here competitors appear only as brands inside consumer studies. Suzy's Signals feed drifts toward intelligence — recorded as a variant layer, not the core.
7. **vs Marketing Analytics Platform / BI (§06/§13)** — analysis here is over the platform's own survey data with survey-statistics machinery (significance, weighting/rebase, crosstabs), not over arbitrary business data sources.

## Uncertainties

- Suzy's operational model (survey builder, panel, analysis surfaces) is undocumented publicly; Suzy is retained in the sample for its positioning pole (decision-engine/signal layer) but contributes no operational evidence. All Suzy-derived claims in the final document are positioning-level.
- Exact panel sourcing/ownership for Attest and quantilope is not publicly documented; the final document says "platform-supplied audience" without asserting ownership.
- Whether the future market-research-platform leaf will be defined subject-agnostic (my working assumption from the panel pass) — joint review recommended; recorded in STATUS.md.
- The precise split between "consumer research platform" and "consumer intelligence platform" naming (quantilope uses the latter) — treated as naming variance over one Type, not two Types; no evidence of a structural discriminator.

## Final Synthesis

A Consumer Research Platform is a brand-side research platform whose defining core is four properties: the consumer as the studied subject; structured studies (question instruments) fielded to real consumers; platform-supplied access to consumer audiences (owned panel, panel network, or continuously fielded syndicated dataset); and decision-oriented insight outputs (dashboards, crosstabs, reports, AI answers) rather than raw instruments or raw data pipes.

Around that core, mature products add: audience targeting machinery (demographics, quotas, screening, feasibility), a study instrument (question types, logic, media, multi-wave), a live analysis surface (charts, crosstabs, segments, significance, AI summaries), storytelling/delivery (boards, exports), data-quality machinery, AI assistance, human research support, and tracking/ongoing-research modes.

The Type's main variant axis is the audience-and-data substrate: proprietary panel (field-your-own pole) vs syndicated dataset (query-pre-fielded pole), with own-audience and hybrid modes as bridges. Method depth, qualitative extensions, intelligence/signal layers, deliverable generation, and data activation are further variant layers.

Boundaries: the panel platform manages the population; the survey platform manages the instrument without supplying the audience; the MR platform (pending its own pass) centers the subject-agnostic study lifecycle and sample buying; VoC manages the customer relationship's feedback; listening observes rather than asks; CI tracks competitors rather than studying consumers.
