# Research Notes — Nutrition Coaching Platform

Directory location: §28 Sports, Fitness & Recreation (siblings: Personal Training Management, Online Fitness Coaching, Meal Planning Application [processed 2026-09-08], Food / Calorie Tracking Application [processed 2026-09-08], Corporate Wellness Platform [processed], AI Fitness Coach [processed], Wearable Fitness Platform; distant family: Coaching Commerce Platform §27 [processed], Practice Management System / Telehealth Platform §22, Employee Wellbeing Platform §09)

Research date: 2026-09-08

## Research Goal

Understand what a Nutrition Coaching Platform actually is as an Application Type: what objects exist inside it, what the practitioner and the client each do, how nutrition guidance is composed, delivered, executed, and reviewed, which machinery is common across the market, and where the Type's boundaries sit — especially against the already-processed Meal Planning Application (which hung a forward flag for this pass), Food / Calorie Tracking Application, Coaching Commerce Platform, and AI Fitness Coach.

## Initial Boundary

Initial hypothesis before research:

1. Core use: software for nutrition professionals (dietitians, nutritionists, health coaches, trainers) to deliver nutrition coaching to clients — plans, logging, communication, progress.
2. Primary users: the professional (manages many clients); the client (executes the plan).
3. Nearest neighbors: Meal Planning Application, Food / Calorie Tracking Application, Personal Training Management / Online Fitness Coaching, Coaching Commerce Platform, generic Telehealth / Practice Management.
4. Likely boundary: the meal-planning pass flagged that professional plan-building tiers sit on the planner↔coaching seam — plan-building machinery in-type there, coach-client relationship machinery in-type here.
5. Unknowns: whether meal-plan building is definitional; whether telehealth is definitional; whether practice-management machinery (billing, charting) belongs in the core; how the gym/trainer pole differs from the dietitian pole.

## Research Questions

1. Who holds the roster — what is a client record here, and how does it relate to the professional?
2. What forms does the nutrition prescription take (meal plan / macros / protocol / care plan / habits)? Is any one form definitional?
3. How does the client-side execution loop work (logging, check-ins), and how does data flow back to the professional?
4. What review/feedback machinery does the professional have between sessions?
5. Where do sessions, scheduling, and communication sit — core or common?
6. How much practice/business machinery (billing, forms, charting) appears, and is any of it definitional?
7. What distinguishes this Type from a professional meal-plan builder (plan artifact without a relationship loop)?
8. What distinguishes it from a personal tracking app (self-serve loop without a professional)?
9. What distinguishes it from coaching commerce (selling the engagement) and from fitness-coaching Types (different managed subject)?
10. Would older / paper-era / regional nutrition counseling practice still fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Healthie | practice-management + client-engagement platform, EHR-grade, scaled practices & organizations (US) | market-leading "nutrition/wellness practice platform"; Tier-1 help center; shows the business/engagement depth pole |
| Practice Better | all-in-one EHR & practice management for wellness practitioners incl. nutritionists/dietitians (Canada) | second practice-management pole; explicit client-portal + journaling machinery; Tier-1 help TOC |
| Nutrium | dietitian-clinical nutrition software, international (6 UI languages) | nutrition-first clinical pole (meal plans, measurements, BIA devices); non-US regional evidence |
| Macrostax (Team) | macro-prescription platform through the gym/trainer channel (US) | fitness-channel pole; prescription can be software-computed; client app-first |
| That Clean Life | nutrition planning for health professionals (Canada) | boundary probe — professional plan-builder with no client-relationship machinery; expected to fall outside the Type |

## Sources

Tier 1 (official operational documentation):

- Healthie Software Support (Help Scout) — https://help.gethealthie.com/ — categories: Platform, Scheduling, EHR & Billing, Data & Reporting, Engagement (Chat, Video Calls, Programs, Journal Entries, Goals, Metrics, Documents, Care Plans, Meal Plans), Marketplace, Organizations. Articles read in full: "Meal Planning and Healthie" (article/614), "Getting Started: Journal Entries" (article/100). Category TOCs read: Journal Entries (17 articles), Meal Plans, Client Management, Goals, Metrics, Client Packages, Payments, Insurance, Superbills, Electronic Forms, Charting, Automations, Branding, Organizations.
- Practice Better Help Center (Zendesk) — https://help.practicebetter.io/hc/en-us/ — categories: Getting Started, Using Practice Better, Client Portal, Practice Better Payments; featured articles list read (services, packages, booking/availability, adding/inviting clients, forms & waivers, session notes, payments/invoices, telehealth, programs, documents, insurance billing, automations, "Setting Up Client Journals and Reviewing Entries", team members, That Clean Life integration, DrFirst ePrescribe, Fullscript).
- Nutrium Help Center (Intercom) — https://help.nutrium.com/en/ — collections read: Practice Management Features (21 articles, titles), Meal Planning and Recipes (13 article titles), Nutrium Mobile App for Patients (5 article titles), plus root TOC (Basic Features, Nutritional Analysis, Payment System, Nutrium Care).
- Macrostax Help (StaxHelp, Intercom) — https://help.macrostax.com/ — root TOC read; collection "Macrostax Team" (2 articles); article read in full: "What is Macrostax Team?" (article/2845050).
- That Clean Life Help Center — https://help.thatcleanlife.com/ — root TOC read (category list).

Tier 2 (official product pages):

- Practice Better — https://practicebetter.io/ — feature navigation (Protocols, Templates, Billing & Insurance, Payments, Reporting, Branding, ePrescribe, Automations, Charting, Secure Messaging, Telehealth, Scheduling, Group Sessions, Journaling, Programs & Courses, Mobile App, Client Portal), "who we serve" (nutritionists, dietitians, health coaches, personal trainers, …), That Clean Life integration page copy.
- That Clean Life — https://thatcleanlife.com/ — positioning "Nutrition planning for health professionals"; feature copy (flexible planning, filters, automation from calories/macros/diet type, templates, recipes, secure share links, branded PDF export "to upload to your practice management software", nutrition analysis, grocery lists, grocery delivery integration, stats for shares); practitioner testimonials.

Source-access limitations:

- help.practicebetter.io root and /en/ failed (transport error, then 404) before the product page revealed the working Zendesk path /hc/en-us/; only the category/featured-article TOC level was read, no article bodies. Practice Better claims are therefore held at TOC/product-page strength.
- Macrostax Team's professional-side documentation is thin (2 help articles); Team feature depth (scheduling, messaging, plan editing) is unverified — no claims made about it.
- Nutrium article bodies were not fetched; evidence is at collection/article-title level, which nonetheless names concrete objects (meal plan sections, supplements in plans, measurements, assessment forms).
- No numeric limits, prices, or defaults are asserted anywhere from these sources.

## Product A — Healthie (Tier 1)

### Key observations

- Help center organized as: Platform / Scheduling / EHR & Billing / Data & Reporting / Engagement / Marketplace / Organizations — practice management and client engagement as the two big halves.
- **Client management**: "Organize and manage client accounts, tags, groups, and relationships"; clients are added as accounts (Account Management category), orgs have team member management and permissions.
- **Engagement layer** (the nutrition-coaching substance): Chat (secure messaging), Video Calls (telehealth + Zoom), Phone Sessions, Programs ("build courses and distribute/sell to clients"), Journal Entries, Goals ("build goal regiments for clients and track progress"), Metrics ("log metrics… create custom metrics"), Documents, Care Plans ("share recommendations with your clients with care plan templates"), Meal Plans.
- **Journal Entries article (read in full)**: "Healthie's Journaling feature enables clients to log key nutrition and lifestyle information into their platform. As a provider, you are able to customize this experience for your clients, as well as view, comment, and react to client entries as part of providing longitudinal engagement with your clients to augment care."
  - Clients log: food (meal photos, hunger levels, perceived healthiness, moods, comments, reflection), nutrients (via an external food-database integration), metrics (weight, BMR, waist circumference; custom metrics), stool, symptoms, water (with provider-set target), notes, selfies, activity; wearable integrations pull data in.
  - Provider review surfaces: Journal tab on the provider dashboard (all clients' recent activity, filterable by entry type and client group), per-client Journal tab, activity reports.
  - Provider feedback: comments and "quick reactions" on individual entries; clients get notifications (default on).
  - Provider controls: journaling can be turned on/off globally, per group, per client, and per feature; special settings exist for eating-disorder populations; journaling can be disabled entirely.
- **Meal plans**: the native Meal Plans category holds only 2 articles — Healthie's own meal planning is light and it "offers an integration with Living Plate Rx to offer meal planning services to clients." Deep plan-building is delegated to an integration. This is direct evidence that a deep native meal-plan builder is NOT definitional.
- **Practice/business machinery**: scheduling (calendar, availability, bookings, rooms), payments (packages to "charge for sessions, products, programs, and services"), insurance claims (CMS-1500), superbills, electronic forms (intake + e-signature), charting (notes, templates, e-fax), e-prescribing (via integration), e-labs, inventory, marketing tools, automations & workflows, branding/white-label, organizations (teams, providers, admin, billers), API.
- Positioning evidence: HIPAA/PIPEDA/GDPR/PCI compliance categories; specialty-population setup guides.

## Product B — Practice Better (Tier 1 TOC + Tier 2)

### Key observations

- Self-describes as "All-In-One EHR & Practice Management Software" for wellness practitioners; "who we serve" lists Nutritionists and Dietitians alongside health coaches, naturopathic doctors, personal trainers, mental health professionals, etc.
- Feature set splits the same way as Healthie: **Practice Management** (Protocols, Templates, Billing & Insurance, Payments, Reporting, Branding, ePrescribe, Automations, Charting, Integrations) and **Client Engagement** (Secure Messaging, Telehealth, Scheduling, Group Sessions, Journaling, Programs & Courses, Mobile App, Client Portal).
- **Journaling** feature copy: "Lower the barriers to food and lifestyle tracking for an accurate window into clients' daily habits." Help article: "Setting Up Client Journals and Reviewing Entries" — the review loop is named at TOC level.
- **Protocols** as a first-class feature; a customer quote (nutritionist) describes usage: "build protocols, give nutrient and hydration targets, foods to include or reduce, and provide supplement recommendations."
- Help TOC confirms client-relationship machinery: Adding New and Prospective Clients, Sending a Client Invitation, forms & waivers sent to clients, session notes, packages, invoices, booking & cancellation settings, availability, client portal navigation, team members.
- **That Clean Life integration** (both companies document it): "Effortlessly plan and deliver personalized nutrition care" — access recipes, track client preferences, create personalized nutrition plans, "make food journaling a breeze," add meal plans to programs and protocols. Confirms: plan-building can be delegated; the platform's own center is the client relationship + care machinery.
- Payments machinery (own payment product, invoices, bank debits, buy-now-pay-later) — business layer present.

## Product C — Nutrium (Tier 1)

### Key observations

- Help center in 6 languages (EN, PT-BR, FR, DE, IT, ES) — international/regional evidence.
- Top-level collections: Get Started, Basic Features, **Practice Management Features**, Subscription Management, Mobile Apps, **Nutritional Analysis**, **Meal Planning and Recipes**, Payment System, Nutrium Care.
- **Meal Planning and Recipes** article titles show the professional-authored prescription: create weekly meal plans, add recipes to the plan, food portions/equivalents, dietary supplements as plan items, multi-week plans "for my clients," print/PDF, share recipes with clients and on websites, plan sections configurable (lunch/dinner).
- **Practice Management Features** article titles: in-house video calls + Zoom integration, online scheduling/bookings, appointment requests, nutrition assessment forms sent to the client (customizable), anthropometric and clinical measurements configured per appointment, blood analysis registration, client file attachments, measurements reports (download/print), client reports, assistant access to the software, BIA device integrations (InBody, AKERN), Google Calendar sync, AI Notes.
- **Client side**: a dedicated help collection "Nutrium Mobile App for Patients" — "Guide for clients/patients who have access to the Nutrium mobile app from their nutrition expert": food diary logging (add new foods while logging, how the diary page works), joining video calls with the nutrition professional. The client app exists *because* the professional granted access — access is relationship-derived.
- Nutritional Analysis is its own collection; Nutrium Care (1 article) suggests a corporate/care program extension (not researched further).

## Product D — Macrostax (Tier 1)

### Key observations

- Two-sided structure: a consumer macro-tracking app (client side; rich help: getting started, tools & features, progress & goals, community, challenges, medical/dietary needs) and **Macrostax Team** for professionals.
- "What is Macrostax Team?" (read in full): "a hands-off software built for gym owners and trainers to offer custom nutrition plans to their clients in minutes." Gym owners/trainers use it because: (1) "They can trust us to provide a proven, scientifically-backed program if they don't have the right nutrition expertise"; (2) "their clients get everything they need through our mobile app"; (3) "keep tabs on and easily manage all their clients' progress on one synced platform." Unlimited client invites on trial.
- Structure reading: the professional holds the client roster and monitors progress; the nutrition prescription can be **software-computed** (macro targets/plan from client data) or provided as the vendor's program — the professional does not need to author the plan content themselves. Prescription authority and roster/progress management remain the professional's; authorship is delegated.
- No evidence found in Team docs of scheduling, video calls, or charting — the fitness pole is prescription+tracking+roster, without the clinical/practice layer. (No claims made about absent features beyond "no evidence found".)

## Product E — That Clean Life (Tier 1 TOC + Tier 2) — boundary probe

### Key observations

- Positioning: "Nutrition planning for health professionals" / "provide beautiful nutrition guidance to your clients." Users are the same professionals as the coaching Type (nutritionists, dietitians, naturopaths, gym owners).
- Feature structure (help TOC + homepage): Meal Planning, Recipes, Planner, Lists, Templates, Collections, Recipe Box, Nutrition, Sharing, Exports, Subscriptions/Pricing. Automation "generate meal plans in seconds based on calories, macros, and diet type"; 150+ condition templates; nutrition analysis on plans; smart grocery lists; grocery delivery integration; branded PDF export — explicitly "to upload to your practice management software."
- Client delivery: "Send clients everything they need through a secure unique link" + share/view statistics. Crucially, no client-management category exists in the help center; a testimonial praises that "it doesn't require clients to opt in to any type of membership." Client preferences exist only inside the planning workflow (and via the Practice Better integration's "track client preferences").
- Judgment: this is the professional plan-builder pole — the plan artifact is the product's center. The coach-client relationship machinery (standing client records under the professional's care, adherence loop, review between sessions) is absent. Per the meal-planning pass's recorded seam, plan-building machinery is in-type in Meal Planning Application; That Clean Life belongs there (professional tier), not here. Used in this pass as the boundary probe, not as an in-type sample.

## Cross-product Comparison

| Structure | Healthie | Practice Better | Nutrium | Macrostax Team | That Clean Life |
|---|---|---|---|---|---|
| Practitioner's client roster (identified client records, invites, archive) | ✓ (accounts, tags, groups) | ✓ (add/invite clients) | ✓ (client profiles, assistant access) | ✓ (unlimited client invites) | ✗ (share links only) |
| Nutrition prescription bound to a client (plans/targets/protocols) | ✓ care plans + meal plans (meal planning largely via integration) | ✓ protocols + nutrient/hydration targets; meal plans via TCL | ✓ weekly/multi-week meal plans + supplements | ✓ custom nutrition plans / macro programs (computable) | plan artifact ✓ but not bound to a client record |
| Client-side execution capture (logging against their plan/record) | ✓ journal entries (food/nutrients/metrics/symptoms/water/notes/selfies/activity) | ✓ journaling ("window into clients' daily habits") | ✓ food diary in client app | ✓ client app macro tracking | ✗ |
| Practitioner review & feedback on client data | ✓ view/comment/react per entry; activity reports | ✓ "Setting Up Client Journals and Reviewing Entries" | (review implied via professional's software view; not article-verified) | ✓ "keep tabs on… progress" | ✗ (view stats only) |
| Secure messaging | ✓ chat | ✓ secure messaging | (present via professional software; not TOC-verified) | no evidence | ✗ |
| Scheduled sessions / video consultations | ✓ scheduling + telehealth/Zoom | ✓ scheduling + telehealth + group sessions | ✓ bookings + in-house/Zoom video | no evidence | ✗ |
| Goals / metrics / measurements tracking | ✓ goals + custom metrics | ✓ reporting | ✓ anthropometric + clinical measurements, blood analysis | ✓ progress & goals (client side) | nutrition analysis of plans only |
| Intake forms / documents | ✓ electronic forms + e-signature + documents | ✓ forms & waivers, documents | ✓ assessment forms, file attachments | no evidence | ✗ |
| Payments / packages for services | ✓ packages, payments, insurance, superbills | ✓ packages, invoices, payments, insurance | ✓ payment system collection | no evidence | n/a (own subscription) |
| Practice/EHR depth (charting, e-rx, labs, e-fax) | ✓ deepest | ✓ (charting, ePrescribe via DrFirst, labs via Fullscript) | partial (notes/AI notes, reports) | ✗ | ✗ |
| Native deep meal-plan builder | ✗ (integration) | ✗ (integration) | ✓ | ✓ (computed macros) | ✓ (but no client loop) |
| White-label / branding of client surfaces | ✓ | ✓ branding | partial (PDF/branding at plan level unverified) | no evidence | ✓ branded PDFs |
| Programs / courses / group delivery | ✓ programs | ✓ programs & courses + group sessions | no evidence | challenges (consumer side) | collections/templates |
| Wearables / devices | ✓ integrations | ✓ integrations | ✓ BIA devices (InBody, AKERN) | no evidence | ✗ |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The client as a managed record under a nutrition professional.** The platform's organizing container is the professional's roster: each client is an identified person-record in that professional's care (profile, history, plan, data), added/invited by the professional, distinct from an anonymous app user. The relationship is the unit around which everything else hangs.
   - Remove → a personal tracking application (self-serve loop) or a plan tool with no care relationship.
2. **The nutrition prescription bound to the client.** Nutrition guidance composed by — or issued under the authority of — the professional, attached to a specific client's record, and delivered into the client's hands. The FORM is deliberately not fixed: a meal plan, macro/nutrient/hydration targets, a protocol or care plan, supplement and habit recommendations, a structured program. What is invariant is that a nutrition-specific prescription exists as a client-bound deliverable of the professional.
   - Remove → generic telehealth/CRM/practice software with no nutrition substance.
3. **The adherence-and-review loop.** The client's real-world execution — food logging, habit/metric check-ins, measurements, messages — is captured against their record and surfaced to the professional, who reviews and responds (feedback, encouragement, plan adjustment). The loop runs between and across sessions; it is what makes the engagement coaching rather than one-way plan delivery.
   - Remove → a plan generator / PDF deliverer (the coaching loop is gone).

Jointly-held load-bearing checks:

- 1 alone → client CRM
- 2 alone → professional meal-plan/protocol generator (Meal Planning Application territory)
- 3 without 1+2 → generic habit tracker
- 1+2 without 3 → plan delivery with no coaching loop
- 1+3 without 2 → communication/telehealth with no nutrition substance
- 2+3 without 1 → an ephemeral plan+tracking pair with no standing relationship record

### L1 — Common Mature Structure

- Client management: profiles, invitations, groups/tags, archival; team/assistant access at the practice pole.
- Client-facing portal / mobile app: dashboard, plan access, logging surfaces — access granted through the relationship.
- Food & lifestyle logging depth: food diary with nutrient composition, custom foods, saved meals, barcode scanning, water, activity, symptoms, notes, photos/selfies, wearable sync.
- Practitioner review surface: cross-roster journal feed (filter by client/entry type), per-client history, comments/reactions on entries, activity/engagement reports.
- Goals & metrics: provider-set targets (calories, macros, water, weight), custom metrics, progress views; anthropometric/clinical measurements at the clinical pole.
- Secure messaging between professional and client.
- Scheduled sessions & video consultations: booking pages, availability, reminders; group sessions.
- Intake forms & documents: assessment forms, waivers, e-signature, file exchange.
- Plan/protocol sharing & export (PDF/print/secure link).
- Payments & packages for services (light commerce inside the practice platform).

### L2 — Variant / Optional Structure

- Practice-management depth: charting/session notes, billing & insurance claims, superbills, e-prescribing, lab ordering, e-fax, inventory (EHR-grade pole vs. light prescriptions+tracking pole).
- Prescription authorship mode: hand-built meal plans; auto-generated plans from targets (calories/macros/diet type); vendor-supplied standard program (professional without nutrition expertise); delegated to a meal-planning integration.
- Customer channel: private-practice dietitians/nutritionists/health coaches; gyms/trainers; multi-provider organizations/teams; corporate care programs.
- Group delivery: cohort programs, courses, challenges, communities.
- Device/lab ecosystems: wearables, body-composition devices, lab ordering, supplement dispensary integrations.
- White-label/branding of client-facing surfaces.
- AI assistance: charting/notes drafting, plan generation, client-facing insights.
- Regulatory posture: HIPAA/PIPEDA/GDPR-class compliance; population-specific configurations (e.g., eating-disorder-sensitive settings); jurisdiction/language scope.
- Meal-planning depth: native builder vs. delegated integration — proven variable in BOTH directions across the sample.

### L3 — Vendor-specific (research notes only; not in the final document)

- Healthie: CMS-1500 insurance claims, superbills with ICD-10/CPT lookup, e-fax, e-prescribing via a named partner, e-labs, inventory; "Bridge / Data / Visualize" reporting products; AI Charting suite; Marketplace integrations (Edamam food database, Living Plate Rx meal planning, Apple Health/Google Fit/Fitbit); eating-disorder special settings; organizations with provider/admin/biller roles; client activity report.
- Practice Better: DrFirst ePrescribe, Fullscript labs/supplements, Practice Better Payments (own payment rails incl. bank debits, BNPL), "50,000+ practitioners" claim, compare pages vs SimplePractice/Jane/Healthie, Protocols/Templates as named features, migration tooling.
- Nutrium: 6 UI languages; InBody/AKERN BIA integrations; blood-analysis registration; Nutrium Care (corporate/care extension, 1 article, not researched); AI Notes; food-equivalent suggestions; supplements as plan items; assistant access.
- Macrostax: "StaxHelp" center; 30-day free trial / unlimited client invites claims; consumer-side challenges & community; "Macrostax Team for Business" naming; gym-owner positioning ("what should I eat" as the #1 fitness-business question).
- That Clean Life: 8,000+ recipes / 150+ templates / "100+ filters" claims; Automation, Airdrop, Assessment Tool, snippets, PDF themes, unit systems, stats for shares; © 2014–2025.

## Vendor-specific Findings

See L3 above. Additional observations kept out of the final document:

- Healthie's own meal-plan machinery is shallow (2-article category) and explicitly complemented by the Living Plate Rx integration — the strongest single piece of anti-overfit evidence that "deep native meal-plan builder" is not definitional.
- Practice Better and That Clean Life jointly market an integration ("add meal plans to programs and protocols… make food journaling a breeze") — the market itself pairs plan-builders (meal-planning Type) with coaching platforms (this Type) rather than requiring one product to do both natively.
- Macrostax Team shows prescription authorship can be delegated to the vendor's computed program — mirroring the ai-fitness-coach pass's "who adapts the plan" seam, but with a human professional still holding the roster and review loop.

## Boundary Findings

1. **vs Meal Planning Application (§28, processed)** — sharpest seam, flagged forward from that pass and now discharged from this side. Plan-building machinery (recipes, auto-generation, grocery lists, PDF artifacts) is in-type THERE; the coach-client relationship machinery (standing client records under care, adherence-review loop, communication between sessions) is in-type HERE. That Clean Life — professional nutrition planning with share links but no client records or review loop — is the meal-planning pole ("no client membership" praised in its own testimonials). Healthie — deep client engagement with meal planning delegated to an integration — is the coaching pole. Products blend at the middle (Nutrium has a real builder AND the loop); the center of gravity (plan artifact vs. managed relationship) is the discriminator. Keep both Types.
2. **vs Food / Calorie Tracking Application (§28, processed)** — the tracker centers the person's self-serve daily loop; here the center is the professional-managed loop (client records belong to the practice; the professional is an acting party with authority over the prescription). The tracker pass already recorded "professional companions (dietitian consoles over the same diaries)" as a variant — those consoles are this Type's review surface when the relationship machinery is present. Seam holds.
3. **vs Coaching Commerce Platform (§27, processed)** — commerce centers productized offers → checkout → tracked engagement (session credits/program access); here the center is the nutrition care process itself (prescribe → execute → review → adjust). Both ship scheduling, payments, client portals, even programs — feature overlap is real; the seam is the managed center. The coaching-commerce pass noted the delivery-first↔commerce-first emphasis spectrum for generic coaching with no separate leaf; nutrition is different: the domain machinery (food logging, nutrition prescription) is substantial enough that the market splits delivery-first platforms (this Type) from commerce-first platforms (that Type).
4. **vs Personal Training Management / Online Fitness Coaching (§28, unprocessed)** — domain seam: the managed prescription subject is nutrition here vs. training/exercise there. Both Types embed each other as modules (fitness platforms add nutrition features; nutrition platforms log activity), mirroring the endurance-training pass's adjacent-module finding. Forward flag recorded for those passes: apply the "which prescription is the managed center" test.
5. **vs AI Fitness Coach (§28, processed)** — the processed seam test ("who adapts the plan") holds: here a human professional holds the adapting authority; software may compute plan drafts (Macrostax pole) but the professional manages the relationship and the review loop. Fully software-adaptive nutrition coaching without a professional in the loop drifts toward the AI-coach/tracking territory. Gradient, not wall.
6. **vs Telehealth Platform / Practice Management System (§22)** — those Types are discipline-generic (clinical scheduling, notes, billing for any specialty); here the nutrition care substance (plans/targets/protocols + food/adherence data) is the managed center. Nutrition platforms style themselves "EHR" at the clinical pole (Healthie, Practice Better), so the boundary is center-of-gravity, not vocabulary.
7. **vs Corporate Wellness Platform (§28, processed)** — employer-sponsored program with an organizational view is that Type; here the roster belongs to the practitioner/practice and care is personal. Vendor extensions toward employer care exist (Nutrium Care) — packaging variant.
8. **vs Sports Coaching Platform / Athlete Management System (§28)** — nutrition appears there as a module within athlete preparation; here the nutrition process is the center (the endurance-training and AMS passes recorded nutrition as adjacent modules from their sides — consistent).

### "Remove what to become another Type" summary

- Remove the client relationship (roster/records/care context) → meal-plan builder (Meal Planning) or personal tracker (Food/Calorie Tracking).
- Remove the nutrition prescription substance → generic telehealth/CRM/practice management.
- Remove the adherence-review loop → one-way plan delivery (still meal-planning territory).
- Swap the prescription domain to exercise → personal-training / online-coaching territory.

## Historical / Market-Sample Check (§24)

Paper-era nutrition counseling practice: an index card or file per client (diet history, weight, notes), a handwritten diet sheet or meal plan handed to the client, the client keeping a written food record, follow-up visits where the professional reviews the record and weight and adjusts the plan, correspondence by letter/phone. This satisfies all three L0 legs (client records under the professional; professional-authored nutrition prescription; adherence-review loop) with no app, telehealth, billing, macro calculator, or AI. Early-desktop-era dietitian software (plan composition + print + client records) also satisfies. The definition therefore names no specific medium, channel, app form, payment machinery, or regulation. Regional check: the sample includes a non-US, multi-language product (Nutrium) with the same core; nothing in the definition assumes US insurance/billing machinery.

## Uncertainties

1. Practice Better evidence is TOC-level (article bodies not fetched); capabilities are named by the vendor's own help center but operational details are not verified. Claims about it kept at feature-name strength.
2. Macrostax Team's professional-side depth (messaging, scheduling, plan editing) is undocumented in reachable sources; no claims made. Its consumer-app evidence (tracking, goals, challenges) is strong but belongs to the client side.
3. Nutrium article bodies not fetched; collection/article titles used as evidence of object structure (meal plan sections, supplements in plans, measurement configuration) — safe at that level; deeper workflow details unverified.
4. Whether "Nutrium Care" is an employer-facing program is unverified (1 article, not read) — mentioned only as an extension hint in research notes.
5. The exact market share/ordering of poles (practice-management-first vs prescription-first vs channel products) is not measured; the sample shows at least three poles exist.
6. Adjacent products not sampled: dietetics-clinic management outside wellness framing, hospital dietetics modules (belong to clinical EHR/institutional foodservice per those passes), nutrition marketplace apps.

## Final Synthesis

A Nutrition Coaching Platform is the practitioner-side system of record for delivering nutrition coaching: the professional holds a roster of client records, composes and delivers a nutrition prescription bound to each client (the form varying from meal plans to macro targets to protocols), and runs a continuous adherence-and-review loop in which the client's logged execution flows back for professional review and response. Client relationship, prescription, and loop are jointly load-bearing: remove the relationship and the product is a plan builder or tracking app; remove the prescription and it is generic practice software; remove the loop and it is one-way plan delivery. Everything else the market expects — portals, messaging, video sessions, forms, payments, goals, devices, AI — is standard capability layered on that spine, with practice-management depth, prescription authorship mode, and customer channel as the major variant axes.
