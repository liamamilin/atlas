# Research Notes — Research Panel Platform

Research date: 2026-09-07

## Research Goal

Understand what a Research Panel Platform is as an Application Type: what objects it manages, who uses it, how a panel is built and operated (recruit → profile → sample → field → record → reward → maintain), and where its boundary lies against survey platforms, market/consumer research platforms, community platforms, and sample marketplaces.

## Initial Boundary

Hypothesis at start: a Research Panel Platform is software for building and operating a **standing, managed population of research participants** — as distinct from:

- Survey platforms (authoring/fielding instruments to arbitrary respondents)
- Market/Consumer Research Platforms (the study/insights workflow, with external sample buying)
- Community platforms (member conversation for its own sake)
- Sample exchanges/marketplaces (programmatic routing of respondents from many sources to buyers)

Adjacent-directory leaves flagged up front: `Market Research Platform`, `Consumer Research Platform`, `Competitive Intelligence Platform` (§06 siblings); `Survey Platform` / `Online Form Builder` (§03.11); `Community Platform` family (§01.06); `Customer Feedback Management` (§07); `Data Labeling Platform` (§13) as a structural cousin (managed contributor pool + tasks + payment).

## Research Questions

1. What is a "panel" and a "panelist/member" in these products — what is the object model (member record, profile attributes, membership states)?
2. How are members recruited and how does membership begin and end?
3. How is profiling done (baseline attributes, dynamic updates) and how does sampling/targeting of subgroups work?
4. What research activities get fielded to members (surveys, discussions, diaries, missions, product tests) and how are they delivered?
5. How do incentives/rewards work (points, redemption, thresholds)?
6. What panel-health machinery exists (engagement, fatigue, quality, fraud, refreshment)?
7. What are the member-facing vs operator-facing interfaces (portal vs channel-first)?
8. Where is the line vs survey platforms, community platforms, and sample marketplaces/exchanges?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| QuestionPro (Communities / Panel Management) | Self-serve suite, survey heritage, SMB-to-enterprise | Vendor with an explicit, named "Panel Management Software" product page + how-to steps |
| Alida (formerly Vision Critical) | Enterprise community-centered research, brand first-party panels | The reference "insight community / customer panel" vendor; Audience Management framing |
| Rival Technologies | Mobile-first conversational research; insight communities; proprietary closed panel | Counter-pole: deliberately **no member portal**; also demonstrates the vendor-operated panel-asset pole (Rival Audiences) |
| Forsta (Panel Management, within Research HX) | Enterprise/agency survey heritage (Decipher lineage) | Feature-level panel-management modules (panel database, sampling engine, incentive tracker) |
| Cint (Cint Engage / Cint Exchange) | **Boundary context only** — sample marketplace + panel-owner monetization | Documents the exchange/monetization pole against which the panel platform is bounded |

Qualtrics was planned as a CX-suite-module pole but its support site returned 404 twice; abandoned (see Sources / limitations).

## Sources

All fetched 2026-09-07.

- QuestionPro — Research Suite product page: https://www.questionpro.com/research-suite/
- QuestionPro — Online Research Community Platform: https://www.questionpro.com/communities/
- QuestionPro — Panel Management Software (incl. create-panel how-to steps): https://www.questionpro.com/communities/panel-management-software.html
- Alida — homepage: https://www.alida.com/
- Alida — Audience Management: https://www.alida.com/audience-management
- Rival Technologies — homepage: https://www.rivaltech.com/
- Rival — Insight Community Platform: https://www.rivaltech.com/rival-insight-communities
- Rival — Rival Audiences (proprietary panel): https://www.rivaltech.com/audience-research-panel
- Forsta — homepage: https://www.forsta.com/
- Forsta — Panel Management: https://www.forsta.com/platform/market-research/panel-management/
- Cint — homepage (marketplace positioning): https://www.cint.com/
- Cint — Manage Communities / Cint Engage: https://www.cint.com/solutions/manage-communities/

**Source-access limitations.** (1) Vendor help centers were not reachable in this pass: Alida help center (transport error), QuestionPro help article (empty response), Qualtrics support (404 ×2). (2) All successfully fetched sources are official product/positioning pages plus one operational how-to page (QuestionPro). (3) Consequently the evidence base is Tier-2-heavy with one Tier-1 surface; precise numeric limits, defaults, and internal admin mechanics observed only as vendor claims are recorded here and deliberately excluded from the final document. (4) Assertion strength in the final document is calibrated accordingly (no precise numbers, no admin-console internals).

## Product Observations

### QuestionPro (Communities / Panel Management) — evidence layer A on each point below unless noted

- Explicit product named "Panel Management Software": "Create and maintain a healthy Online Customer Panel."
- Defines panel management as managing "a research panel (a pre-qualified community)" contributing to ongoing quantitative or qualitative research; panel management software lets companies "recruit, segment, and maintain their panel or members," "create and manage a number of panels, build rich profiles, and target segments of the panelists."
- **Panel creation wizard**: create a branded community (name, logo, landing page content/background image, theme, selectable modules, default language) — panel and branded portal are one act.
- **Recruitment ingestion from surveys**: a survey question can be flagged as a "recruitment" option and assigned to a panel; responses are added to the panel automatically (email → panel assignment). Direct operational evidence that survey-run recruitment feeds the member database.
- **Recruitment channels** (advice layer): social media, niche online communities, offline methods, subscriber base; incentive attractiveness and transparency named as success factors.
- **Member portal / centralized community web portal**: built-in communication system, reminders, engagement tools, analytics, dashboards; members engage via a branded standalone community site.
- **Targeting**: "target segments of your panel to send surveys and other emails."
- **Rewards/gamification**: "Reward your local customers with interactive points, gamification badges, cash and donations."
- **Methods**: 50+ question types (vendor claim), logic/branching, qualitative solutions, mobile integration, multilingual (vendor claim), social sharing; reports incl. TURF/CHAID/weighting (vendor claim).
- **Vendor-documented panel vs MROC distinction** (layer A, vendor framing — treat as vendor's market vocabulary): MROCs = long-standing smaller online research communities (vendor says 250–500 participants, year or more active); panels = larger groups (vendor says usually thousands), often used once or twice per research project.
- Energizer case study: "Needed a long-term research panel to continuously generate product ideas, gather feedback, and track consumer loyalty" (customer-panel purpose example).
- Contradictory marketing number on the panel page ("a panel can constitute 100-150 members") conflicts with the same site's own MROC/panel FAQ — rejected (see Rejected Findings).

### Alida (Audience Management / community-centered research) — evidence layer A unless noted

- Positioning: "community-centered research platform"; "always-on access to opted-in sample"; "recruit, profile, segment, and incentivize with secure end-to-end audience management."
- **Recruit**: in-app, via URL, in-survey, or from existing internal data sources (CRM, user lists); screening out professional responders; inviting new members over time "to maintain desired size, response rates, and diverse feedback"; "built-in consent, privacy, and burden controls."
- **Segment & target**: "unlimited customizable profile variables and dynamic profile updates"; segmentation from self-reported, behavioral, product-usage, and operational data; "longitudinal access to members"; extension with third-party sample.
- **Engage & reward**: on-demand engagement of members "who have a vested interest"; intrinsic value (sharebacks, advance previews, exclusive content); "streamline delivery of monetary rewards with built-in incentive management."
- Panels members are long-lived: homepage metrics (layer A as *vendor claims*: 3.1 years average active participation, 40% average response rate, 38 activities per member) — marketing numbers, not structural claims; only used to confirm the standing-membership pattern.
- Platform modules: Audience Management / Feedback & Research ("build and execute activities") / Insights / Alida AI / Technology (privacy & governance).

### Rival Technologies (Insight Communities + Rival Audiences) — evidence layer A unless noted

- Insight community defined as "an always-on panel of real people, ready to engage when you need them."
- **Documented lifecycle** (six steps, layer A): 01 recruit custom community panel (define audience by demographics, behaviors, product usage, custom criteria) → 02 launch research in hours (concept tests, IHUTs, user research, journey mapping) → 03 collect human responses (unlimited video, open-ended) → 04 share insights (real-time reports, AI summaries, video reels) → 05 build intelligence over time ("360-degree segmentation you can't get from one-off studies") → 06 keep the community healthy ("manage engagement, quality, member refreshment, and incentives").
- **No-portal pole**: "No separate community apps to manage or member portals to maintain"; distribution via SMS, WhatsApp, QR codes, branded apps, or email. Member experience is channel-first (chat-style surveys), not portal-first.
- **Multi-segment communities**: "maintain one community while accessing different customer cohorts based on demographics, behaviors, product usage, or other custom attributes"; "advanced targeting and recontact capabilities."
- **Rival Audiences** (separate offer): "proprietary, closed research asset — never resold or sourced from open-access marketplaces"; recruitment standards, real-time fraud detection (branded "Survey Sentinel" — vendor name), video-verified respondents; "longitudinal profiling = better experience = better data"; sold as ad-hoc sample, platform subscription + panel retainer, or full-service.
- Scale claims (layer A as vendor claims): communities from a few hundred to 20,000+ members; 1,000+ engaged members in 4–8 weeks (recruitment phasing).
- Managed-service spectrum: DIY (platform + community health managed by vendor team) / assisted-serve (project execution: programming, QA, fieldwork, reporting) / full-service.

### Forsta (Panel Management within Research HX) — evidence layer A unless noted

- Positioning: "Build targeted, engaged panels quickly and at scale. Streamline everything from recruiting to rewards."
- Scale span claim (layer A, vendor claim): "whether you're managing 200 panelists or 2 million."
- **Named modules** (layer A — the clearest feature decomposition in the sample):
  - *Panel database* — "a scalable, panelist-centric system for storing and accessing all survey and profile data."
  - *Smart sampling engine* — "automates selection and recurring draws, while improving sample quality."
  - *Profile survey builder* — "customize profiling workflows to match your study goals and reduce fatigue."
  - *Incentive credit tracker* — "log and manage panelist rewards with complete visibility into point history and redemption."
  - *Alerts and automation* — "trigger actions based on profile changes, survey completions, or engagement thresholds."
- **Sampling detail**: representative samples "including concurrent and subsamples"; manage and filter panel data from within the survey workflow.
- **Profiling detail**: "continuously updated panelist profiles and monitor changes in demographics and behaviors over time"; "incremental profiling, smart filters, and custom rules" to reduce fatigue; rewards customizable by panelist profile or behavior.
- **Member portal pole**: "custom, on-brand portals" where panelists "update their profiles, track incentives, and view their survey history"; real-time sync of profiles/survey data; multilingual.
- **Workflow integration**: panel management part of Research HX — "from sampling to survey to insight and reporting without switching tools"; direct integration with Decipher (vendor product name); API sync of panel data to external systems.
- FAQ self-definition: "our solution for building, engaging, and rewarding research panels."

### Cint (Engage + Exchange) — boundary context only — evidence layer A unless noted

- Cint Exchange: "programmatic research marketplace" connecting sample buyers to a network of suppliers; buyers "source respondents" — no standing operator-owned member population.
- Cint Engage: "the only panel management tool connected to the world's largest research marketplace" — panel management **for panel owners** whose goal is monetization: set up/manage panels "of any size and in any market," match members to paid surveys by profile ("precise matching logic"), real-time tracking and on-the-fly adjustments, business-intelligence reports, gamified engagement, flexible/customizable reward schemes, unsubscribe-prevention controls.
- This demonstrates the **supply-side panel-management pole**: same machinery (member records, profiles, matching, rewards) but the panel exists to be monetized through survey routing rather than to serve the operator's own research program.
- Marketplace metrics are vendor claims (200M+ completed surveys annually, 800+ suppliers, 130 countries) — recorded, not reused structurally.

## Cross-product Comparison

| Dimension | QuestionPro | Alida | Rival | Forsta | Cint (Engage) |
|---|---|---|---|---|---|
| Panel/member record with profile attributes | ✔ (rich profiles, multiple panels) | ✔ (unlimited profile variables) | ✔ (longitudinal profiling) | ✔ (panel database, continuously updated profiles) | ✔ |
| Standing, consent-based membership | ✔ (opt-in community) | ✔ ("opted-in sample", consent controls) | ✔ (recruited, verified) | ✔ | ✔ (panel owners' members) |
| Recruitment machinery | ✔ wizard + in-survey recruitment question | ✔ in-app/URL/in-survey/CRM imports | ✔ vendor-run phased recruitment | ✔ recruiting to rewards loop | panel-owner side |
| Member portal | ✔ branded community portal | ✔ community experience | ✖ deliberately no portal (SMS/WhatsApp/QR/app/email) | ✔ on-brand self-serve portal | ✔ panelist experience |
| Incentive machinery | ✔ points/badges/cash/donations | ✔ built-in incentive management | ✔ managed incentives | ✔ incentive credit tracker (point history + redemption) | ✔ customizable reward schemes |
| Sampling/segmentation | ✔ target panel segments | ✔ segment & target, dynamic profiles | ✔ multi-segment + recontact | ✔ smart sampling engine, concurrent/subsamples | matching by profile (monetization) |
| Fielding/distribution | ✔ surveys/emails via portal | ✔ build & execute activities | ✔ SMS/WhatsApp/QR/app/email chat studies | ✔ survey workflow integration (Decipher) | paid-survey routing |
| Participation recorded per member | ✔ | ✔ (longitudinal access) | ✔ (recontact, engagement) | ✔ (survey + profile data per panelist) | ✔ (conversions) |
| Panel health/quality | ✔ engagement tools | ✔ burden controls, professional-responder screening | ✔ refreshment, fraud detection | ✔ fatigue rules, alerts/automation thresholds | unsubscribe-prevention, engagement |
| Methods beyond surveys | discussions/forums/qual solutions | activities (community methods) | video, IHUTs, missions, diaries | diaries, focus groups (suite) | surveys only (routing) |
| Panel ownership/purpose | operator's own panel | brand first-party panel | brand community + vendor proprietary panel | operator/agency panel | panel owners monetizing audiences |
| Third-party sample extension | ✔ (Audience product, separate) | ✔ explicit | explicitly closed (proprietary) | not stated | n/a (is the exchange) |

Reading: the first, second, third, seventh, and eighth rows hold across all five (including the boundary-context product); the portal row splits (Rival's no-portal pole); method breadth varies; ownership/purpose is the major strategic variant.

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the product is no longer a research panel platform:

```text
Panel member record (identified person, editable profile attributes)
└── standing, consent-based membership in an operator-managed panel
    (persists across studies; can end)
    ├── sampling / selection of member subgroups by profile attributes
    ├── research activities fielded to the selected members
    │   └── recorded participation per member
```

Five properties:

1. **Panel member record** — each participant is an individually held record with identity and profile attributes. Without it there is no panel, only a mailing list or ad-hoc respondents.
2. **Standing, consent-based membership** — members opted in and remain in scope across studies until they leave. Without standing membership, the product is a survey tool or sample exchange.
3. **Sampling/selection by profile attributes** — the operator chooses subgroups of the panel for each study. Without it, there is no profiling value and no panel discipline.
4. **Research activities fielded to members** — studies (surveys/tasks) are sent to selected members as the panel's purpose. Without it, it is a CRM or community app.
5. **Recorded participation per member** — completions/interactions are tracked against the member record (the basis of history, recontact, fatigue and quality management). Without it, the operator cannot operate a panel over time.

Historical/market-sample check: mid-20th-century mail panels and TV-meter household panels (paper rosters, profile questionnaires, mailed/recorded participation, prize incentives) satisfy all five without portals, points engines, or online surveys; a platform-native consumer research community satisfies all five too. The abstraction is not over-fit to the modern online implementation.

### Level 1 — Common Mature Structure

Present across the modern sample; expected in the market but not definitional:

- recruitment machinery (public join pages, in-survey recruitment, CRM/list imports, referral/ads; entry screening)
- member-facing portal or equivalent self-serve experience (profile updates, activity history, incentive balance)
- incentive machinery (points accrual, reward catalogs/redemption, thresholds; gamification in some products)
- profiling system (baseline profile survey + incremental/dynamic profile updates; demographic, behavioral, product-usage attributes)
- segmentation/targeting (attribute filters, quotas, recurring sample draws, recontact rules)
- distribution/fielding (email invitations and reminders; SMS/WhatsApp/push/QR/app variants)
- panel-health management (engagement monitoring, response rates, member refreshment, fatigue/burden controls, professional-responder screening, fraud detection)
- consent/privacy controls as built-in machinery
- reporting/dashboards (panel composition, engagement, activity/quota tracking)
- research-method integration (built-in survey engine or tight integration; qual methods in many products)

### Level 2 — Variant / Optional Structure

- panel ownership & purpose: brand first-party panel vs independent consumer panel vs professional/B2B panel vs vendor-operated proprietary panel asset (Rival Audiences) vs panel-owner monetization (Cint Engage)
- panel shape: large survey panel vs small always-on insight community (MROC) — vendors document both and the distinction between them
- member surface: branded web portal vs portal-less channel-first (chat/SMS/WhatsApp/app)
- method breadth: surveys only → discussions, diaries, mobile missions, IHUTs, video feedback
- sample posture: closed proprietary vs extended with third-party sample vs marketplace-connected
- service depth: DIY → assisted → fully managed (research ops outsourced)
- scale, language coverage, regional data residency
- business model: SaaS subscription vs agency/insights-as-a-service vs revenue share on monetization

### Level 3 — Vendor-specific (research notes only)

- QuestionPro: create-community wizard fields (name/logo/landing page/theme/modules/language); "recruitment question type" auto-adding respondents to a chosen panel; branded community site; TURF/CHAID/weighting report claims; "10 million users", "50+ question types", "50+ languages" claims; the 100–150-member panel claim (contradicted internally).
- Alida: Audience Management / Feedback & Research / Insights / Alida AI module framing; claims of 3.1 years average participation, 40% response rate, 24–72h response time, 38 activities/member, 25–60% response rates, 176M people reached.
- Rival: Survey Sentinel fraud-detection brand; Rival Audiences closed-panel claims (4% scrub vs "22% industry average", 82% lower fraud failure); 87% completion / 65% recontact / 40% within-an-hour claims; 1,000+ members in 4–8 weeks; communities to 20,000+; Angus Reid heritage.
- Forsta: module names (Panel database, Smart sampling engine, Profile survey builder, Incentive credit tracker, Alerts and automation); Decipher integration; "200 panelists to 2 million" span; "up to 2x engagement" claim; datasheet at library.forsta.com.
- Cint: Cint Exchange / Cint Engage product split; survey-to-qualification matching; filter paid surveys by duration/reward; 200M+ surveys / 800+ suppliers / 130 countries / 4,000+ buyers claims.

## Vendor-specific Findings

(See L3 above — none of these enter the final document.)

## Rejected Findings

- **"A panel is 100–150 members"** (QuestionPro panel page): contradicts the same vendor's own FAQ (panels "usually thousands") and every other sampled product; marketing error — rejected.
- **"Member portal is a defining structure"**: rejected — Rival explicitly markets having *no* portals or community apps while operating insight communities; the portal is a common (L1) realization of the member surface, not the Type.
- **"Incentives define the Type"**: rejected as definitional; universal in the sampled online products, but historical panels ran on prizes/lotteries/non-monetary recognition, and the *structure* that matters is recorded participation, of which reward accounting is one use. Incentive machinery stays L1.
- **"Panels and MROCs/insight communities are different Types"**: rejected as separate Types — the sampled vendors themselves sell both shapes on the same machinery (member records + sampling + fielding + health); they are Level-2 shapes of one Type. The vendor-stated numeric distinction (250–500 vs thousands) is a vendor framing, not asserted in the final document.
- **Precision claims (response rates, completion rates, panel sizes, scrub rates, member counts)**: all single-vendor marketing claims; none promoted to canonical structure.
- **"The survey engine is part of the Type"**: weakened — panel platforms either embed a survey engine (QuestionPro, Forsta) or integrate/distribute to one (Rival's conversational studies, Alida activities); what is invariant is *fielding activities to selected members*, not authoring surveys.

## Boundary Findings

1. **vs Market Research Platform (§06 sibling)**: the market-research platform centers the *study* lifecycle (design → field → analyze → report) and typically buys external sample; the panel platform centers the *standing member population* (its recruitment, profiling, health, and reuse). Convergence is real (panel platforms embed survey tooling; MR platforms resell sample), but the managed object differs. **Test: remove the standing managed population — what remains is a survey/MR platform; remove the study tooling — what remains is a panel platform.**
2. **vs Survey Platform (§03.11)**: survey platforms author and field instruments to arbitrary, non-persistent respondents. Panel platforms persist the *respondent population itself* as the asset. A panel platform may embed a survey engine; a survey platform does not thereby manage a panel.
3. **vs Consumer Research Platform (§06 sibling)**: consumer-research products emphasize methods and analysis surfaces (video feedback, in-the-moment, agile tests); the panel platform's distinguishing stewardship is the population (recruit/profile/health/incentives). Joint review recommended when the sibling leaf is processed.
4. **vs Community Platform (§01.06)**: community platforms center member-initiated conversation/content for the members' own sake; panel platforms center operator-structured research participation. Insight communities (MROCs) are the panel platform's community-shaped variant, and the boundary deserves a joint review when §01.06 leaves are processed.
5. **vs Sample exchange / marketplace (Cint Exchange, Dynata, Lucid-class)**: exchanges route respondents programmatically from many suppliers to buyers; they hold no operator-owned standing population and no member-stewardship loop. **Test: who holds the member relationship, and why do members exist — the operator's research program (panel platform) vs monetization supply (exchange).** Cint Engage is the hybrid: panel management machinery attached to a monetization outlet — recorded as a variant pole.
6. **vs CRM / contact management**: both hold people records; the panel platform adds the research relationship (consent, sampling, study fielding, participation history, incentives). A contact list without these is not a panel.
7. **vs Data Labeling Platform (§13)**: structurally similar (managed contributor pool, task routing, payment) but the work object differs (annotation/training data vs opinion/behavior research) and the record model differs (task/annotation records vs studies/participation history). Structural note only — not sampled.
8. **vs Customer Feedback Management (§07) / Employee Survey Platform (§09)**: audience-specialized feedback tools manage an existing relationship population (customers/employees) for feedback programs; the panel platform is population-agnostic (consumers, B2B professionals, customers, patients) and centers research participation as the product. Customer panels are a variant, not the Type's extent.

## Uncertainties

- No help-center/admin-console documentation was reachable for Alida, Forsta (beyond the product page), or Qualtrics; internal member-state models (e.g., pending/active/dormant/retired member states) could not be verified directly and are described only generically in the final document.
- Whether panel platforms commonly support *multiple distinct panels under one account* is confirmed at QuestionPro ("create and manage a number of panels") and implied by Rival's multi-segment framing, but not confirmed across the whole sample — kept qualified.
- The panel-vs-MROC size norms are vendor framings only; no scale norm is asserted.
- Incentive mechanics (points economics, redemption thresholds) were observed only at vendor-claim level; not asserted.

## Final Synthesis

A Research Panel Platform is operator-side software for building and running a **standing population of consented research participants**. Its world consists of: member records (identity + profile attributes), the panel (the managed membership container), profile data (baseline + dynamically updated), studies/activities fielded to profile-selected samples of the panel, per-member participation records, and the incentive and health machinery that keeps the population willing and usable over time. The operator loop is: recruit → profile → sample → field → record → reward → maintain (refresh/re-engage/prune). The member loop is: join → share profile → receive invitations → participate → accrue rewards → update profile → remain or leave. Mature products wrap this loop in portals or channel-first member experiences, rich targeting, quality/fraud controls, and reporting — none of which change the defining structure. The Type sits deliberately between the survey/MR platform (which centers studies and can rent sample) and the community platform (which centers member conversation), and is distinct from the sample exchange (which routes respondents it does not steward).
