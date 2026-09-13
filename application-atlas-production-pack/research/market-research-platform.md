# Research Notes — Market Research Platform

Research date: 2026-09-10
Leaf: Market Research Platform (DIRECTORY.md §06 Marketing, Advertising & Growth)
Slug: market-research-platform

## Research Goal

Understand what a Market Research Platform is as an Application Type: its core objects, its canonical workflow (design → field → analyze → report), who uses it, how sample is sourced and operated, and where its boundaries lie against the neighboring Types — Survey Platform (§03.11, processed), Research Panel Platform (§06, processed), Consumer Research Platform (§06, processed), sample exchanges, Competitive Intelligence Platform (§06, processed), Social Listening Platform (§06, processed), Marketing Analytics Platform (§06, processed), and Voice of Customer (§07, processed).

This pass also carries TWO pending joint-review obligations recorded by sibling passes:
1. research-panel-platform (2026-09-07): "vs Market Research Platform … the market-research platform centers the *study* lifecycle (design → field → analyze → report) and typically buys external sample; the panel platform centers the *standing member population*. Test: remove the standing managed population — what remains is a survey/MR platform; remove the study tooling — what remains is a panel platform."
2. consumer-research-platform (2026-09-07): "vs Market Research Platform … sharpest open seam. Working discriminator: consumer research platforms are consumer-subject-scoped and bundle audience access as product for brand-side teams; market research platforms center the study lifecycle and sample buying as a marketplace function, subject-agnostic, for research professionals. The seam is commercially fuzzy (Appinio self-labels 'global market research powered by AI'; quantilope is framed as 'market research technology'). Flagged for joint review when market-research-platform is processed."

## Initial Boundary (hypothesis before research)

- Core use: the research professional's workbench for running studies end to end — design the instrument, source/operate sample, field, process data, produce deliverables.
- Likely distinct from: Survey Platform (instrument authoring/fielding without operated sample supply), Research Panel Platform (manages a standing member population), Consumer Research Platform (consumer-subject-scoped, brand-side, audience bundled), sample exchanges (route respondents, hold no study).
- Open questions going in: is sample supply definitional or common? Is the study-portfolio layer (templates, tracking, libraries) definitional? Where exactly does the survey platform end and the MR platform begin (Qualtrics is claimed by both categories in the market)? How fuzzy is the consumer-research seam in practice?

## Research Questions

1. What is the unit of work — the study/project — and what does its lifecycle look like?
2. What does "design" include (instrument authoring, method libraries, templates)?
3. How is sample sourced and operated (marketplace, panels, suppliers, bring-your-own; feasibility, quotas, redirects, quality, cost)?
4. What does fieldwork operations include (soft launch/QA, live monitoring, mid-field changes, wave deployment)?
5. What does "analyze" include (processing, tabulation, weighting, significance, method models)?
6. What does "report" include (dashboards, toplines, decks, client portals, exports)?
7. Who uses it (agency researchers, insights teams, self-serve researchers) and for what subjects?
8. Where are the boundaries vs survey platforms, panel platforms, consumer research platforms, sample exchanges, CI/listening/analytics?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers — deliberately avoiding the products already sampled by the sibling passes (QuestionPro/Alida/Rival/Forsta-panel-module/Cint by the panel pass; Attest/GWI/Appinio/quantilope/Suzy by the consumer pass):

| Product | Pole | Why selected |
|---|---|---|
| Forsta (Research HX / Decipher) | Enterprise agency-grade MR suite | The reference professional MR platform (Confirmit + Dapresy + FocusVision heritage); explicitly sells to research agencies and in-house teams; rich module decomposition |
| Qualtrics (Market Research / Research Hub) | Research core inside an XM suite | The largest name in the space; demonstrates the suite-embedded pole and the survey-platform/MR-platform fuzzy zone; human + synthetic panels |
| Conjointly | Self-serve method-depth + sample marketplace | SMB/prosumer pole; advanced methods packaged as tools; sample buying as a first-class self-serve function; excellent public workflow documentation |
| Zappi | Insight automation (templated, automated, benchmarked) | The automation pole; deliberately included to document the consumer-research seam — it self-labels "consumer insights platform" while the MR industry lists it under market research platforms |

Boundary context (not primary samples): Cint (sample exchange — documented first-hand in research/research-panel-platform.md, 2026-09-07), Dynata (sample/data supplier with a thin self-serve platform, fetched this pass).

## Sources

All fetched 2026-09-10 unless noted.

Tier 2 (official product pages — positioning, module boundaries, workflow claims):

- Forsta — Market research platform page: https://www.forsta.com/platform/market-research/
- Forsta — Advanced data collection (Decipher): https://www.forsta.com/platform/market-research/advanced-data-collection/
- Qualtrics — homepage: https://www.qualtrics.com/
- Qualtrics — Market Research Software: https://www.qualtrics.com/market-research/
- Conjointly — homepage: https://conjointly.com/
- Conjointly — How it works: https://conjointly.com/how-it-works/
- Zappi — homepage: https://www.zappi.io/
- Zappi — Platform page: https://www.zappi.io/web/platform
- Dynata — homepage (boundary context): https://www.dynata.com/

Prior-pass evidence reused (same repo, cited where used):

- Cint Exchange / Cint Engage observations — research/research-panel-platform.md (fetched 2026-09-07)

Source-access limitations:

- Qualtrics operational documentation (support/help center) was not reachable: /products/research-core/ returned 404 this pass; the panel pass also recorded qualtrics.com/support 404 ×2 on 2026-09-07. Qualtrics evidence is therefore product-page level (Tier 2); no operational internals asserted.
- Zappi's Knowledge Base (learn.zappi.io) was not fetched (login-gated product docs; marketing pages reachable). Zappi mechanics are positioning-level; all Zappi-specific operational claims kept weak.
- Forsta's library datasheets (library.forsta.com) referenced by product pages but not fetched this pass; Decipher observations rest on the two official product pages.
- No vendor help-center/admin-console documentation was reached for any sampled product this pass. All successfully fetched sources are official product/positioning pages. Consequently: no precise numeric limits, defaults, or admin-console internals are asserted anywhere; vendor-claimed figures are recorded here as vendor claims only.
- Assertion strength calibrated accordingly (no precise numbers in the final document; workflow claims stated at the level the product pages support).

## Product Observations

### Forsta — Research HX / Decipher (evidence layer A on each point unless noted)

- Positioning: "Your AI-powered solution for every market research study"; "a comprehensive suite of AI-powered tools built on advanced technology that unites market leaders Confirmit, Dapresy, and FocusVision under one roof"; "30+ years of experience working with the world's leading research agencies and in-house teams"; "8/10 of the world's largest market research agencies use Research HX" (vendor claim).
- Named module decomposition (the clearest in the sample): Advanced data collection (Decipher) / Multi-mode research / Data visualization / Digital diaries / Online focus groups / Focus group streaming / Panel management.
- Decipher (the survey engine) described as "the world's leading survey platform for researchers": dual interface (drag-and-drop or full-code XML + Python scripting); advanced logic (nested routing, complex quotas, loops); multilingual (vendor claim: 80+ languages); "85+ question types, including MaxDiff and conjoint" (vendor claim); rich media (video/audio/image).
- Setup acceleration: AI-import (Word docs → surveys), reusable templates ("build once, relaunch forever"), instant QA ("auto-check logic, links, and skip patterns, and flag quality issues instantly").
- **Built-in Sample Marketplace**: "Recruit 80% faster or bring your own sample" — sample supply is an in-platform function with an explicit bring-your-own-sample mode; "high data quality … with server-to-server (S2S) connections and partnerships with top-tier vendors"; open API to CRMs and panel providers.
- Live survey management: "Monitor and optimize survey quotas, logic, and deployment in real time"; "Wave deployment: run segmented fielding across markets"; "Client portals: give stakeholders secure, live views"; "Adapt on the fly … pivot fast when studies change mid-field."
- Processing/reporting: "automated data processing"; AI analysis (summarize open-ended feedback; AI computes; AI-powered QA flags PII, tags sentiment/topics on open-ends); "Auto reporting: generate dashboards and decks in minutes"; "Auto-generate detailed reports: create share-ready PowerPoint decks with native charts"; data visualization module ("transform survey data into engaging dashboards and reports").
- One-platform claim: "One platform for all your research needs: collecting, analyzing, panel management, and reporting. Configure a solution that suits you, and scale as needed"; "Go from survey to dashboard with Research HX."
- Users: research agencies (the named core constituency) and in-house/enterprise research teams; scale claims (vendor): 1B+ surveys completed annually, 40,000+ studies per year, "deliver projects 50% faster".

### Qualtrics — Market Research / Research Hub (evidence layer A for positioning; operational docs unreachable)

- Positioning: "Market Research Software Platform — Fast enough to matter. Rigorous enough to trust."; "Bring every market research need into one intelligent platform. From market trends to customer preferences."
- Scope statement: "Qualtrics unifies all your market, product & innovation, UX, and brand research in a single platform. Connect insights across every study."
- Research Hub (the workspace): AI-recommended conjoint analysis project surfaced from a market-trends query; MaxDiff workflow shown as steps — "Define features, Refine respondent targeting, Distribute via email, SMS, or panel."
- **Human and Synthetic Research Panels**: "Combine AI-powered synthetic respondents with human panels for faster, cost-effective insights with trusted methodology"; synthetic audiences for rapid directional validation, human panels where rigor is critical; three methodology options shown (synthetic / human / mixed).
- Sample supply: B2B decision-maker audience panel "4.2M across 18 countries" (vendor claim); "automated real-time quality checks confirming speeders, bots, and straight-lining are filtered."
- Study-portfolio layer: research library of searchable studies "auto-tagged by topic" (screenshot: 142 studies, 38 added this quarter — vendor UI claim); brand tracking study template "with best practice methodology locked and centralized approval permissions."
- FAQ self-definition against neighbors: "Most research tools solve one problem—a survey platform, a panel provider, a UX testing tool. Qualtrics brings every research need into a single AI-powered platform … your organizational knowledge compounds over time rather than living in disconnected project folders."
- Agentic research: "With AI guiding and accelerating every step — from study design to synthesis."
- Context: the research capability sits inside the broader XM (experience management) platform alongside CX/EX programs — the suite-embedded pole. Users: research teams/leaders; enterprises, governments, healthcare.

### Conjointly (evidence layer A — official site + how-it-works)

- Positioning: "All-in-one survey research platform with expert support"; "covering everything from simple surveys to advanced conjoint, product, and pricing research, as well as conversational and video surveys."
- Method toolkit packaged as named, self-serve tools: Generic Conjoint, Brand-Specific Conjoint, Brand-Price Trade-Off, MaxDiff, Gabor-Granger, Van Westendorp PSM, Kano Model, Feature Placement Matrix, TURF Analysis Simulator, Claims Test / Claims Combination Test, A/B Test, Monadic Test, Video Test, Five-Second Testing, ad pretesting (image/copy/print/out-of-home/dial), concept testing (product concept, variant selector, description, idea screener, package), brand testing (business/brand/product name, logo, domain, graphic design), Brand Tracker, implicit testing, segmentation typing tool, ranking surveys, Insights Explorer; plus a general Survey Tool (multiple question types, randomisation blocks, multilingual; free basic tier).
- Sample supply as a first-class commercial function: "Source real human respondents swiftly and at scale through Conjointly" — Predefined panels ("customisable sample solution hand checked by Conjointly's fieldwork team"), Self-serve sample A & B ("urgent access"), Self-serve sample C ("ID-verified experts and niche respondents"), Bring your own respondents, Send an email campaign, Data quality assurance. Vendor claims: "100+ million panellists across 150+ countries"; micro-targeting "from sub-regions, income and type of education to age of children".
- Documented five-step workflow (layer A): 1 choose a tool → 2 design the study (intuitive interface, wizard, minimum sample size, templates) → 3 choose participants (buy sample through Conjointly or invite existing customers; predefined panels for recurrent experiments) → 4 Conjointly collects answers (mobile/tablet/desktop; real-time analytics; "identify and remove responses that don't meet your target criteria or speed through your questions") → 5 automated reports (customise display, create respondent segments, pivot tables; interactive dashboard; "simulations to view preference shares and revenue projections"; automatic analysis; online and Excel reports; direct PowerPoint export).
- Users: consumer goods, MedTech/pharma, consultancies, marketing agencies, software/technology, social enterprise; testimonials from market research firms, economists, faculty researchers, and brand teams — the self-serve pole serves both professionals and non-specialists.
- Human support: "expert researchers on hand"; full-service research projects; hosts the Research Methods Knowledge Base (Trochim).

### Zappi (evidence layer A for positioning; mechanics positioning-level)

- Positioning: "The consumer insights platform that helps brands win"; "Powerful, automated, agile consumer insights platform"; "on-demand research, automated AI-generated reports and all your data in one user-friendly platform."
- Solution packaging = pre-built study types: advertising (TV ads, storyboards, early campaign ideas, digital ads), innovation (idea screening, concept testing, pack research, pricing research), brand tracking; AI Concept Creation Agents.
- Platform mechanics (as marketed): "Set & Forget" — "expertise seamlessly incorporated so you can quickly, easily & consistently run research"; "on average 12 hours from idea to insight" (vendor claim); "Simple pricing with no sizing or quotes needed" (sample bundled, not quoted); "automatically populated charts as data comes in"; "smart autocoding to get an instant view of the most relevant themes"; benchmarks ("country, category, brand & other relevant benchmarks"); company/brand-specific benchmarking; "ability to do your own analyses / data cuts on the fly"; easy export to share with the business.
- Learning loop: "Look across all your research quickly & easily to learn what works and what doesn't, creating a learning loop" — the cross-study knowledge layer.
- Users: brand insights teams (Reckitt, GSK Consumer Healthcare, McDonald's, PepsiCo); industries CPG, QSR, finance, telco.
- **Seam evidence**: Zappi self-labels "consumer insights platform" while the market-research industry lists it among market research/insight-automation platforms — direct documentation of the consumer-research/MR-platform commercial fuzziness.

### Boundary context — Dynata (fetched 2026-09-10)

- "World's Largest First Party Data Platform"; global panel with specialized audiences (B2B respondents, healthcare respondents); QualityScore ML model ("analyzes 175+ data points to identify survey fraud and inattention … removed and replaced live during fielding" — vendor claim).
- Dynata+ self-serve platform: "Define your audience, see real-time feasibility and pricing, and launch in minutes"; Dynata+ Sample and Dynata+ Brand Lift products; managed services (project management, survey scripting, reporting & visualizations).
- Reading: the sample supplier is building a thin self-serve platform (audience → feasibility → launch → report), but its center of gravity remains the panel/data asset it sells — the study-lifecycle machinery and method toolkit are thin or service-delivered. This is the exchange/supplier pole against which the MR platform is bounded.

### Boundary context — Cint (from research/research-panel-platform.md, 2026-09-07)

- Cint Exchange: "programmatic research marketplace" connecting sample buyers to a network of suppliers; buyers "source respondents" — no standing operator-owned member population, no study of record, no processing/deliverable layer.
- Cint Engage: panel management for panel owners monetizing audiences — the panel-platform machinery attached to a monetization outlet.

## Cross-product Comparison

| Dimension | Forsta (Research HX) | Qualtrics (Research Hub) | Conjointly | Zappi |
|---|---|---|---|---|
| Study as managed record | ✔ studies with waves, templates, live management, client portals | ✔ Research Hub library, auto-tagged studies, locked templates, approvals | ✔ projects managed in one place; experiments list | ✔ tests in a collaborative workspace; learning loop across tests |
| Instrument authoring | ✔ dual interface (drag-drop / XML+Python), advanced logic, quotas, loops, multilingual, media | ✔ survey engine inside the platform (MaxDiff workflow: define → target → distribute) | ✔ wizard-driven tool-specific setup + general survey tool | ✖ (authoring replaced by pre-built study templates — "Set & Forget") |
| Method depth | ✔ MaxDiff, conjoint among 85+ question types (vendor claim) | ✔ conjoint, MaxDiff (AI-recommended projects) | ✔ deep method catalog (conjoint family, MaxDiff, PSM, Gabor-Granger, Kano, TURF, monadic, implicit…) | ✔ method embedded in templates (ad pretest, concept test, pack, pricing) |
| Sample supply | ✔ built-in Sample Marketplace + bring-your-own + S2S supplier connections + panel-management module | ✔ human panels + synthetic respondents + distribute via email/SMS/panel | ✔ buy through platform (predefined/self-serve tiers) + bring-your-own + email campaigns | ✔ bundled ("no sizing or quotes needed") — sourcing details not public |
| Fieldwork operations | ✔ live quota monitoring, mid-field changes, wave deployment, QA auto-checks | ✔ real-time quality checks (speeders/bots/straight-lining filtered) | ✔ removes non-qualifying/speeding responses; data quality assurance | ✔ quality machinery marketed (ESOMAR/ISO standards claim) |
| Processing & analysis | ✔ automated data processing, AI computes, open-end summarization | ✔ AI synthesis; method outputs | ✔ automatic analysis, segments, pivot tables, preference-share simulations, revenue projections | ✔ auto-populated charts, autocoding, data cuts on the fly |
| Deliverables | ✔ dashboards, auto-generated PowerPoint decks, client portals | ✔ dashboards/reports (implied), connected insights | ✔ online + Excel reports, PowerPoint export | ✔ automated AI-generated reports, exports |
| Portfolio/knowledge layer | ✔ templates, one platform survey→dashboard | ✔ research library, locked methodology, approval permissions, connected insights across studies | ✔ predefined panels for recurrent experiments; Brand Tracker | ✔ benchmarks + learning loop across all research |
| Human research support | ✔ professional services, 24/7 support (vendor claim) | ✔ (expertise/playbooks; XM Institute) | ✔ expert researchers, full-service projects | ✔ professional services offering |
| Subject scope | subject-agnostic (agencies run any study) | subject-agnostic (market/product/UX/brand; B2B panels; gov/healthcare) | broad (consumer, MedTech/pharma, consultancies, agencies, software, social) | consumer-scoped (CPG/QSR/finance/telco brands) |
| Primary user | research agencies + in-house teams | research/insights teams | self-serve researchers + brand teams + agencies | brand insights teams |
| Self-labeling | "market research" explicitly | "Market Research Software Platform" | "survey research platform" | "consumer insights platform" |

Reading: rows 1, 5, 6, 7 hold across all four; sample supply is present in all four but with different postures (marketplace/panels/synthetic/bundled/bring-your-own); authoring depth varies from full-code scripting to fully templated automation; subject scope and user base split the sample — Zappi is the consumer-scoped automation pole sitting on the seam.

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the product is no longer a market research platform:

```text
The study as the managed unit of record
└── (instrument + sample plan + fielding state + data + deliverables,
    carried through design → field → analyze → report)
    ├── respondent supply operated as a platform function
    │   (sample sourced through the platform or brought by the user,
    │    flowing through feasibility/quota/quality/cost machinery)
    └── research-grade processing and deliverable production
        (cleaning, tabulation, weighting, significance, method models,
         client/stakeholder-ready outputs)
```

Three jointly-held structures:

1. **The study as the managed unit of record** — a persistent, identified research study that carries its instrument, its sample plan, its fielding state, its data, and its outputs through an explicit lifecycle (design → field → analyze → report), and is worked on over time (templates, waves, tracking, multi-country, research libraries). Remove it → a survey tool (instrument + fielding without a managed study) or a pile of ad-hoc analyses.
2. **Respondent supply operated as a platform function** — the people who answer are a managed fieldwork input: sourced through the platform (built-in sample marketplace, panels, synthetic respondents, configured suppliers) or brought by the user (client lists, own panel), always flowing through the platform's fieldwork machinery — feasibility, quotas, redirects, quality/fraud controls, live monitoring, cost. Remove it → the survey platform's publish-and-distribute fielding (respondent supply as an optional add-on, per the survey pass's own recording).
3. **Research-grade processing and deliverable production** — the study's data is processed into research outputs: cleaning/quality processing, tabulation and crosstabs, weighting, significance testing, method-specific models (e.g., preference simulators), and client/stakeholder-ready deliverables (dashboards, toplines, decks, exports). Remove it → a data-collection pipe or a sample exchange.

Binding: **subject-agnostic professional research** — the study's population is whatever the research question demands (consumers, B2B decision-makers, healthcare professionals, employees, citizens), and the platform serves research practitioners (agency researchers, insights teams, self-serve researchers) running studies as a discipline. Remove the subject-agnostic scope and the professional machinery, keep consumer subjects with bundled audiences for brand-side teams → the Consumer Research Platform. Remove the professional machinery and keep one relationship population → VoC / employee-survey territory.

Jointly-held load-bearing:

- 1 alone = a study tracker / project folder
- 2 alone = a sample marketplace / exchange
- 3 alone = a tabulation/stats tool
- 1+2 without 3 = a fieldwork-operations platform (data handed off for processing elsewhere)
- 1+3 without 2 = a research workbench without sample (the historical MR-software pole; today's survey platforms at their research pole)
- 2+3 without 1 = an exchange with analytics, no study of record

Historical/market-sample check (§24): the paper-era research agency (paper questionnaire + mail/phone/face-to-face fielding operated by the agency's field department + hand tabulation + typed report, with sample held by the agency or bought from field suppliers) satisfies all three structures and the binding. The 1990s–2000s MR software generation (authoring + data processing + tab books; CATI sample-management modules operating sample as a configured input) satisfies the same core without any modern layer. Regional MR software (European specialists) has the same shape. Thin platform-native forms (bundled-sample DIY survey products with auto analysis) satisfy the core in a reduced form. The abstraction is not over-fit to the current AI-era implementation. Passed.

### Level 1 — Common Mature Structure

Present across the modern sample; expected in the market but not definitional:

- instrument authoring with research-grade depth: broad question types, routing/branching, quotas, loops, randomization, multilingual support, media stimulus; dual authoring interfaces (visual + code) at the professional pole
- method libraries: advanced methods packaged as tools/templates (conjoint family, MaxDiff, TURF, pricing methods, Kano, monadic testing, concept/ad/pack/claims tests, brand tracking)
- sample sourcing options: built-in sample marketplace, panel supply (own, partner, or synthetic), supplier integrations (S2S/API), bring-your-own-sample, email campaigns; feasibility and pricing feedback
- fieldwork operations: pre-launch QA checks, soft launches, live quota monitoring, mid-field adjustments, wave deployment across markets, redirects, completion tracking
- data-quality machinery: fraud/bot detection, speeder/straight-liner filtering, attention/consistency checks, duplicate prevention, live replacement of bad respondents
- processing & analysis: automated data processing, cleaning, crosstabs/pivot tables, segments, weighting, significance testing, open-text coding/sentiment, method-specific models and simulators
- reporting & delivery: dashboards, toplines, auto-generated decks, client portals with live views, exports (spreadsheet, slides, statistical formats)
- study-portfolio layer: reusable templates, locked/best-practice methodology, research libraries, cross-study learning, benchmark databases, tracking waves, multi-country coordination
- human research support: expert researchers, professional services, full-service project options
- AI assistance (era-typical): survey drafting/import, AI analysis and summarization, AI agents at process stages, synthetic respondents

### Level 2 — Variant / Optional Structure

- customer pole: agency-grade professional suites vs brand-insights-team platforms vs self-serve SMB/prosumer tools
- automation depth: full-code professional scripting vs templated "set & forget" automation vs wizard-driven self-serve
- sample posture: built-in marketplace vs supplier integrations vs own/managed panel (panel-management module) vs synthetic respondents vs bring-your-own
- method breadth: quant-only vs multi-mode (CATI/phone/offline) vs qual extensions (digital diaries, online focus groups, communities, video responses)
- suite embedding: standalone MR platform vs research core inside a broader XM/CX suite
- service depth: DIY → assisted → full-service (vendor runs the study)
- industry/regional packaging; scale, language coverage, compliance posture (ISO 20252-class standards invoked by vendors)

### Level 3 — Vendor-specific (research notes only)

- Forsta: Research HX / Decipher / Dapresy / FocusVision lineage and module names; "80+ languages", "85+ question types", "1B+ surveys annually", "40,000+ studies per year", "8/10 of the world's largest market research agencies", "recruit 80% faster", "deliver projects 50% faster" — all vendor claims.
- Qualtrics: Research Hub; synthetic-audience methodology options; "4.2M B2B decision-makers across 18 countries"; "142 studies / 38 added this quarter" library screenshot; XM platform embedding; Forrester Wave "Experience Research Platforms" mention.
- Conjointly: the specific tool catalog (Generic Conjoint, BPTO, Gabor-Granger, Van Westendorp, Kano, FPM, TURF, dial testing…); Predefined panels / Self-serve sample A/B/C tiers; "100+ million panellists across 150+ countries"; run.conjoint.ly app; hosting of the Research Methods Knowledge Base.
- Zappi: "Set & Forget"; "12 hours from idea to insight"; connected-insights report; AI Concept Creation Agents; benchmark machinery; PepsiCo/McDonald's testimonials.
- Dynata: QualityScore ("175+ data points"); Dynata+ Sample / Brand Lift; panel book.

## Vendor-specific Findings

(See L3 above — none of these enter the final document.)

## Rejected Findings

- **"Sample supply means the platform owns the panel"** — rejected. Forsta explicitly offers "bring your own sample" alongside its built-in marketplace; Conjointly offers bring-your-own and email campaigns; Qualtrics distributes via email/SMS/panel. The invariant is respondent supply *operated as a platform function* (feasibility/quota/quality/cost machinery), not panel ownership.
- **"Advanced methods (conjoint, MaxDiff) are definitional"** — rejected as definitional; they are the method-library layer (L1). A market research platform without conjoint is still an MR platform; a product with conjoint but no study lifecycle/sample machinery is a method tool, not this Type.
- **"AI/synthetic respondents are definitional"** — rejected. Era-typical (L1). The paper-era and 2000s-era forms satisfy the core without them.
- **"The MR platform is just a survey platform with more features"** — rejected as collapse: the survey pass itself records respondent supply as an *optional commercial add-on* for survey platforms and analysis depth as a variant axis; the MR platform is defined by the study-of-record lifecycle + operated respondent supply + research-grade deliverable production *jointly*, plus the professional/subject-agnostic binding. The fuzzy zone (survey platforms at their research pole; Qualtrics claimed by both categories) is recorded as a boundary finding, not merged away.
- **"Insight automation (templated studies, benchmarks, learning loops) is a separate Type"** — rejected; it is the automation-depth variant of this Type (Zappi pole). Its consumer-subject scoping is what pulls it toward the consumer-research seam — recorded, not resolved by merge.
- **"Client portals / dashboards define the Type"** — rejected; deliverable machinery is L1.
- Vendor scale/precision claims (surveys per year, panel sizes, language counts, hour claims) — all marketing claims; none promoted to canonical structure.

## Boundary Findings

1. **vs Research Panel Platform (§06, processed) — JOINT REVIEW DISCHARGED from this side.** The panel pass's characterization is RATIFIED with first-hand MR-side evidence: the panel platform's managed object is the standing member population (recruit → profile → sample → field → record → reward → maintain); the MR platform's managed object is the study (design → field → analyze → report) with sample bought/routed as fieldwork procurement. Convergence is real and documented from this side: Forsta ships a Panel Management module inside the MR suite (the panel-platform machinery at module grain), and agencies operate panels beside the study tooling. Removal tests hold both directions: remove the standing managed population from a panel platform → an MR/survey platform remains; remove the study tooling from an MR platform → a panel platform (or sample asset) remains. Keep-both confirmed; no directory change.
2. **vs Consumer Research Platform (§06, processed) — JOINT REVIEW DISCHARGED from this side.** The consumer pass's working discriminator is RATIFIED: consumer research platforms are consumer-subject-scoped with audience access bundled as product for brand-side teams; the MR platform is subject-agnostic with sample procurement as an operated function for research practitioners. The fuzziness is confirmed first-hand: Zappi self-labels "consumer insights platform" while the MR industry lists it under market-research/insight-automation platforms; Appinio/quantilope self-label with both vocabularies (per the consumer pass). The two leaves are kept as separate Types on the recorded test (remove consumer-subject scoping + bundled audience supply → MR platform; conversely, strip the professional study machinery and scope to consumer subjects with bundled audiences → consumer research platform). The overlap zone (consumer-scoped automation platforms) is documented as the seam, not merged. No directory change.
3. **vs Survey Platform (§03.11, processed)** — the survey pass records its core as instrument + fielding + response + compiled results, with respondent supply as an optional commercial add-on and analysis depth as a variant axis. The MR platform is where (a) the study becomes a managed lifecycle record with a portfolio layer, (b) respondent supply becomes an operated platform function (feasibility/quotas/redirects/quality/cost), and (c) processing reaches research-grade deliverable production for clients/stakeholders. Test: remove the operated fieldwork/sample function and the study-of-record machinery → a survey platform remains. Fuzzy zone acknowledged: survey platforms at their research pole (weighting, significance, sample integrations) and suite products (Qualtrics) are claimed by both categories in the market; the seam is a gradient, recorded honestly.
4. **vs Sample exchange / marketplace (Cint, Dynata-class)** — exchanges route respondents programmatically from suppliers to buyers and hold no study of record and no processing/deliverable layer; Dynata+ shows the supplier building a thin self-serve platform (audience → feasibility → launch), but its center of gravity is the panel/data asset. Test: remove the study lifecycle + processing → an exchange remains. MR platforms integrate exchanges as sample sources (S2S/API supplier connections documented at Forsta).
5. **vs Competitive Intelligence Platform (§06, processed)** — CI runs a standing monitored loop over tracked entities from observed data; the MR platform fields structured studies to sampled populations. Competitors appear inside MR studies as stimulus, not as the tracked entity population. (Consistent with the CI pass's own recording.)
6. **vs Social Listening Platform (§06, processed)** — listening observes unsolicited public expression; the MR platform asks structured questions of sampled people. Asked vs observed. (Consistent with the listening pass's recording.)
7. **vs Marketing Analytics Platform (§06, processed)** — marketing analytics measures the organization's own campaign/channel performance from observed behavioral data; the MR platform generates attitudinal data by asking sampled populations and processes it with survey-statistics machinery. Complementary.
8. **vs Voice of Customer Platform (§07, processed)** — VoC manages feedback from an existing customer relationship as a standing program; the MR platform studies arbitrary populations via procured sample. Own-customer studies are the bridge case (a variant posture, not the core).
9. **vs Employee Survey Platform (§09, processed)** — employee surveys bind the same instrument machinery to the workforce population and employment lifecycle; the MR platform is population-agnostic. An MR platform can field an employee study as one study among many; the employee-survey Type is the workforce-bound specialization.
10. **vs A/B Testing Platform (§06, processed)** — experimentation measures revealed preference on live product traffic; the MR platform collects stated preference from sampled humans. Different evidence source.
11. **vs Investment Research Platform (§13-adjacent, processed)** — that Type's object world is investable subjects (securities, issuers); the MR platform's object world is market populations and their attitudes/behavior. (Consistent with the investment-research pass's recording.)

## Uncertainties

- No help-center/admin-console documentation was reachable for any sampled product this pass; internal study-state models (draft → in QA → live → closed → reported) are described generically and not asserted as uniform.
- Qualtrics operational internals (survey engine, Stats iQ-class tools, sample procurement mechanics) could not be verified; Qualtrics claims are positioning-level.
- Zappi's operational mechanics (sample sourcing, instrument internals) are not publicly documented; Zappi contributes seam evidence and the automation pole, not operational structure.
- Whether "multi-mode" (CATI/phone/offline) machinery is common across the category could not be verified beyond Forsta's multi-mode module; kept as a variant, not asserted as common.
- The exact market share of agency-grade vs brand-side vs self-serve poles is unknown; no scale claims made.

## Final Synthesis

A Market Research Platform is the research professional's end-to-end system for running studies: it manages each study as a record carried through design → field → analyze → report; it operates respondent supply as a platform function (sample sourced through marketplaces/panels/suppliers/synthetic or brought by the user, always flowing through feasibility, quota, quality, and cost machinery); and it processes the study's data into research-grade outputs and client-ready deliverables. Its scope is subject-agnostic — the population is whatever the research question demands — and its users are research practitioners, from agency researchers to insights teams to self-serve researchers.

Around that core, mature products add: research-grade instrument authoring (visual + code), method libraries (conjoint, MaxDiff, pricing, monadic testing), fieldwork operations (QA, live quota monitoring, wave deployment), data-quality machinery, weighting/significance/tabulation, dashboards/decks/client portals, study-portfolio layers (templates, locked methodology, research libraries, benchmarks, learning loops), human research support, and era-typical AI (drafting, analysis, agents, synthetic respondents).

The Type's main variant axes: customer pole (agency-grade ↔ brand insights ↔ self-serve), automation depth (full-code ↔ templated automation), sample posture (marketplace ↔ suppliers ↔ own panel ↔ synthetic ↔ bring-your-own), method breadth (quant ↔ multi-mode ↔ qual extensions), and suite embedding (standalone ↔ research core inside an XM suite).

Boundaries: the survey platform authors and fields instruments without operated sample supply; the panel platform stewards a standing member population; the consumer research platform scopes to consumer subjects with bundled audiences for brand-side teams; the sample exchange routes respondents without studies or deliverables; CI/listening observe rather than ask; marketing analytics measures behavior rather than eliciting attitudes; VoC and employee surveys bind the machinery to one relationship population.
