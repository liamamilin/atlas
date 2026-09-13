# Research Notes — Relationship Discovery Application

## Research Goal

Resolve the status of the directory leaf **Relationship Discovery Application** (§01.07 Dating & Relationship Discovery): is it a distinct Application Type with its own structure, or an umbrella alias over the user-led candidate-discovery loop already documented as **Dating Application**?

Two joint-review flags were pre-hung on this leaf by sibling passes:

- dating-application (§01.07): "relationship-discovery-application reads as a probable umbrella alias of the same loop"
- matchmaking-platform (§01.07): "remaining open: (1) relationship-discovery-application umbrella-alias question (unprocessed sibling, joint review pending)"

This pass must discharge both flags: either define a distinct Type or record the alias determination. Per the workflow, an alias finding is recorded, not silently rewritten into the directory.

## Initial Boundary

- Family placement: §01.07, siblings all processed — Dating Application (user-led candidate loop, mediated contact gate), Matchmaking Platform (service-led selection + service-mediated activation), Dating Community Platform (community container with partner discovery integrated).
- Working hypotheses at start:
  1. **Distinct Type** — "relationship discovery" names a structure different from the dating loop (e.g., discovery of relationship *potential* rather than dating; long-term-relationship machinery; compatibility-first structures).
  2. **Umbrella alias** — the leaf is a label over the same user-led loop; "relationship" adds intent positioning, not structure.
  3. **Cross-family umbrella** — "relationship discovery" could plausibly cover platonic discovery too (friend discovery lives in §01.05 as Friend Discovery Application), making the leaf a wider umbrella than the dating family.
- Adjacent leaves to test against: Friend Discovery Application (§01.05), General Social Network (§01.05), Instant Messaging Application (§01.01).

## Research Questions

1. Does any real product self-identify as a "relationship discovery" application? Is "relationship discovery" a market category at all?
2. Do the products that lead most strongly with relationship intent differ structurally from the Dating Application defining core (profile → candidate discovery → interest expression → contact gate → two-person conversation with pairing lifecycle)?
3. Where relationship-oriented products use heavy curation (daily batches, type-learning algorithms), does that cross the ratified matchmaking seam (who-selects + who-activates), or does the user still comb and act unilaterally?
4. Is "relationship intent" a structural difference (new objects, new workflow, new rules) or a positioning/segmentation layer? The dating-application pass already registered "intent specialization (casual, relationship, marriage)" as a **Variants** entry of that Type.
5. Does "relationship discovery" plausibly cover platonic discovery (Friend Discovery Application), and does the directory placement (§01.07, inside the dating family) support or reject that reading?
6. Historical / market-sample check: did any era or region have a structurally distinct "relationship discovery" category (personals ads, matrimonial platforms, search-era subscription services, questionnaire services)?

## Representative Products

Selection principle: sample the products that lead most strongly with *relationship* positioning (they are the strongest candidates to instantiate a distinct Type if one exists), plus a mixed-intent questionnaire product and a mass-market general product as controls; attempt the curated-machinery pole and a personality-based dual-mode product.

- **Hinge** — the most explicit relationship-first positioning among mainstream products ("designed to be deleted"). Tier 1 evidence: official help center + product page. Fetched successfully.
- **Coffee Meets Bagel** — "the dating app for serious daters"; curated daily batches. Tier 2 evidence: product + about pages. Help center unreachable (transport error, then 403; abandoned).
- **OkCupid** — questionnaire/compatibility heritage, mixed intents. Evidence: help center root category structure only (deeper pages did not render; marketing site 403).
- **Plenty of Fish** — mass-market general product; control sample to show the loop is not intent-dependent. Tier 2 evidence: product home + features pages + help center root. Fetched successfully.
- Attempted and unreachable: **eHarmony** (main site and /help/ both 403 — consistent with the matchmaking-platform pass, which also found it unreachable), **Boo** (403), **Zoosk** (help timeout). All abandoned per source-access rules; none are characterized from memory.

## Sources

Research date: **2026-09-08**. All observations below are from same-day fetches unless noted.

- Hinge product page — https://hinge.co/ (positioning: "the dating app designed to be deleted"; mission copy)
- Hinge Help Center — https://help.hinge.co/hc/en-us (root categories) and "What is Hinge?" — https://help.hinge.co/hc/en-us/articles/26845979318803-What-is-Hinge (loop description)
- Coffee Meets Bagel — https://coffeemeetsbagel.com/ (positioning) and https://coffeemeetsbagel.com/AboutUs (the product's own loop description); help center https://coffeemeetsbagel.zendesk.com/hc/en-us/ UNREACHABLE (transport error + 403)
- OkCupid Help Center — https://help.okcupid.com/hc/en-us (root category structure only; category URLs returned the root page; marketing site https://www.okcupid.com/ returned 403)
- Plenty of Fish — https://www.pof.com/ (positioning), https://www.pof.com/features/ (Meet Me / Super Like loop), help center root https://www.pof.com/HelpCenter/helpcenter_faq (redirected to /hc/en-us root categories)
- eHarmony — https://www.eharmony.com/ and https://www.eharmony.com/help/ both 403 (abandoned)
- Boo — https://www.boo.world/ 403 (abandoned)
- Zoosk — https://help.zoosk.com/ timeout (abandoned)
- Sibling documents: applications/dating-application.md, applications/matchmaking-platform.md, applications/dating-community-platform.md (STATUS.md flags), applications/instant-messaging-application.md (gold standard)

> Source-access limitation: the two most intent-specialized products in the market beyond the sampled ones (eHarmony-class curated machinery, Boo-class personality duality) could not be reached from official documentation in this pass. They are held at market-context strength only; no operational claim about them is made anywhere in this research or in the final document.

## Product Observations

### Hinge (evidence layer A — direct observation, official help center + product page)

- Self-description: **"Hinge is the dating app designed to be deleted."** A dating app, positioned around getting members off the app and into in-person relationships. Product page: "succeed in getting you out on promising dates, not keeping you on the app"; careers pitch: "make dating effective, not addictive."
- Loop as the product itself describes it ("How We Get You Off Hinge"):
  - **Profiles**: "in-depth and personalized profiles"; "You'll get to know potential dates through their unique answers to prompts, and personal information like religion, height, and politics." Prompt answers are the personality carrier.
  - **Curation**: "We quickly learn your type. You'll only be introduced to the best people for you." The word "introduced" appears, but the agent is the product's own algorithm inside the user's loop — there is no third-party service selecting and standing behind introductions, and the user still evaluates and acts on presented candidates.
  - **Interest expression / contact gate**: "Every match begins by someone liking or commenting on a specific part of your profile." Interest is anchored to a specific profile element; a match is the gate that opens conversation.
  - **Offline exit + feedback**: "After exchanging phone numbers with a Match, we'll follow up to hear how your date went so we can make better recommendations in the future." The designed outcome is a date; feedback tunes future candidates. Deletion is the success state.
- Monetization: free to use; "Hinge+ or HingeX membership" for seeing everyone who liked you and advanced preferences.
- Help center structure: How Hinge Works (About Hinge, Community Guidelines, Availability, Age Checks, Research FAQ) / Managing My Profile / Connecting With Matches / Reporting & Appeals / Safe Dating / Support & Legal.
- Product page also references an in-house research group ("Hinge Labs — researchers, behavioral analysts, and matchmakers study daters and compatibility").

**Reading**: the relationship-first pole of the market is, structurally, a Dating Application with intent-forward profile content and an offline-exit design philosophy. No structure distinguishes it from the dating core.

### Coffee Meets Bagel (evidence layer A for positioning/loop copy; degraded below that — help center unreachable)

- Self-description: **"The dating app for serious daters."** Founded "because casual swiping apps just weren't going to cut it"; describes itself as "cultivating the dating app with the highest number of serious-relationship seekers." Vendor claims: "over 91% of CMB Daters looking for a committed relationship"; "over 150 million matches." (Claims recorded as vendor claims only.)
- Loop as the product describes it ("The CMB way"):
  - **Intent captured upfront**: "We ask upfront what you want and deliver daily batches of people picked just for you, so you can match with confidence." Curation delivery (daily batches) + user matching — the user still combs the batch and decides.
  - **Intent-forward profiles**: "Do they want kids? Are your values aligned? The important details like education, interests, and family plans are front and center."
  - **Conversation designed for meeting**: "We'll help you get the conversation rolling with icebreakers, then help you move the conversation to real life with chat limits." Friction (chat limits) deliberately pushes toward offline contact.
- Help center (coffeemeetsbagel.zendesk.com) unreachable: first transport error, then 403. Operational mechanics (exact batch sizes, chat-limit windows, any match expiry) are therefore **not characterized** and must not be asserted.

**Reading**: same loop as the dating core, with (a) serious-intent audience positioning, (b) curation inside the loop (daily batches — algorithmic, user still acts unilaterally → does NOT cross the matchmaking seam per the ratified who-selects + who-activates test), and (c) conversation friction oriented to moving offline. All three are positioning/design layers, not new objects or workflow.

### OkCupid (evidence layer A — root category structure only)

- Help center root categories: **Profile & Photos / Paid Features & Power-Ups / Account Settings / Member Communication / Technical Issues / Advice and Safety / Manage My Subscription / Find More Help / Legal**.
- Marketing site 403; deeper help pages returned the root page (did not render). Loop mechanics are NOT directly evidenced this pass.
- Market context (from the dating-application pass, which also had only root-structure evidence): questionnaire/compatibility heritage product; registered there as the questionnaire/compatibility variant of the Dating Application Type.

**Reading**: OkCupid serves a mixed-intent population (casual through serious) while carrying the same structural vocabulary (profile, member communication, subscriptions). A questionnaire-heavy product that does *not* specialize by intent is the control showing that "relationship" is not what organizes this market's products — the candidate loop is.

### Plenty of Fish (evidence layer A — product pages + help root)

- Self-description: **"Dating on POF — Date, chat and match for free"; "The most welcoming way to date";** "a community of singles where you can come exactly as you are"; "lots of options to make finding your person actually fun." General-audience positioning; intent is not the organizing axis.
- Loop (features page, "Meet Me"): "scroll through profiles of potential matches. Swipe left if you're not into it and right if you want to get to know them a little better. **If the love is mutual, we'll open up a chat** so the banter can begin." — unilateral interest expression, mutual-consent contact gate, chat. "Super Like": "an extra boost" on interest expression.
- Help center root categories: **Member Communication & Profile** ("message, search, and show off your best self") / Advice & Safety / Manage My Subscription / Account Settings / Safety, Tools & Resources.
- Home page copy also promises multiple connection options ("Whether you're into sending a good-old-fashioned DM…") — POF combines several discovery/contact surfaces (search, decks, messaging); the current contact-gate rules beyond Meet Me are not evidenced this pass and are not asserted.

**Reading**: the mass-market control. Identical loop skeleton (profile → deck/feed/search → like/pass → mutual gate → chat) with no relationship-intent specialization. Confirms the loop does not require the "relationship" framing — i.e., the framing is not structural.

## Cross-product Comparison

| Dimension | Hinge | Coffee Meets Bagel | OkCupid | Plenty of Fish |
|---|---|---|---|---|
| Self-description | "the dating app designed to be deleted" | "the dating app for serious daters" | dating product (help-center vocabulary; site unreachable) | "Dating on POF" |
| Discovery surface | algorithmic feed ("we quickly learn your type") | daily curated batches picked for you | questionnaire/compatibility heritage (market context; not directly evidenced this pass) | swipe deck (Meet Me) + search ("message, search") |
| Interest expression | like or comment anchored to a specific profile element; every match begins this way | match within the delivered batch | — (not evidenced) | swipe right; Super Like boost |
| Contact gate | match (mutual) | match ("so you can match with confidence") | — | "If the love is mutual, we'll open up a chat" |
| Conversation design | unique conversations from prompt answers | icebreakers; chat limits pushing to real life | — | chat opens on mutual interest |
| Offline exit | follow-up after phone-number exchange: "how did your date go"; deletion as success | "move the conversation to real life with chat limits" | — | — (not emphasized) |
| Curation agent | product's own algorithm | product's own algorithm | product's own machinery | deck + user search |
| Monetization | free + Hinge+/HingeX | subscriptions (help center unreachable; positioning page confirms paid app) | Paid Features & Power-Ups category | free core + Manage My Subscription category |
| Safety surfaces | Safe Dating, Reporting & Appeals, Age Checks categories | — (unreachable) | Advice and Safety category | Advice & Safety + Safety, Tools & Resources categories |
| Intent posture | relationship-first positioning | serious-only positioning | mixed | general |

**Findings across the sample:**

1. **No product uses "relationship discovery" as its category.** The two most relationship-forward products on the market both self-describe as *dating apps*. The leaf's own phrase does not appear in any fetched product vocabulary.
2. **The loop is the Dating Application core in every case.** Profile (intent-forward where positioning demands) → candidate discovery (feed / batches / deck / search) → unilateral interest expression → mutual-consent gate → private two-person chat → designed move offline. No sampled product adds an object, workflow, or rule that the Dating Application core lacks.
3. **Curation never crosses the matchmaking seam.** Hinge's type-learning and CMB's daily batches are algorithmic selection *inside* a user-led loop: the user still combs what is delivered and acts unilaterally; no service owns the introduction and no service mediates activation. Per the ratified who-selects + who-activates test (matchmaking-platform pass), these products remain in the Dating Application family.
4. **"Relationship intent" is a positioning/segmentation layer, not a structure.** It changes what profiles carry (upfront intent questions, family plans, values), what the pool is filtered to (serious-only vs mixed), and how conversation is pushed offline (chat limits, post-date follow-up). The dating-application pass had already registered exactly this as a Variants entry ("intent specialization (casual, relationship, marriage)").
5. **Structural vocabulary is shared even by mixed-intent products.** OkCupid and POF, neither of which specializes by relationship intent, use the same profile/communication/subscription/safety structure — the loop, not the intent, is what the market's products are built from.

## Abstraction

### L0 — Defining Invariant (of what this leaf covers)

The leaf covers exactly the **user-led romantic candidate loop** already defined as the Dating Application core:

```text
Evaluation-oriented dating profile
└── Candidate discovery over the application's own member pool
    └── Unilateral interest expression toward a specific candidate
        └── Mediated contact gate (mutual consent)
            └── Private two-person conversation, controllable pairing lifecycle
```

The leaf adds **no** invariant of its own. If the candidate loop is removed, nothing remains that any product recognizes; if the "relationship" framing is removed, every product still stands. That asymmetry is the alias determination: the only leaf-specific candidate for definitional content (relationship-intent framing) fails the remove-test in the defining direction — remove it and the products are unchanged.

### L1 — Common Mature Structure (inherited from the Dating Application Type)

Standard capabilities of the products this leaf covers, none of them leaf-specific:

- preference filters and "liked you" visibility
- match/conversation list with turn affordances
- verification machinery (age checks; photo/ID verification)
- unmatch / block / report; safety centers and advice surfaces
- paid subscriptions and power-ups (see-who-liked-you, advanced preferences)
- post-date feedback gathering (documented in one product's help center as a recommendation-tuning input; present as a designed loop stage in that product's own description)

### L2 — Variant / Optional Structure

Where the leaf's angle actually lives — the intent layer and its delivery styles:

- **Intent posture** — serious/committed-relationship-only pools (the leaf's core case), mixed-intent general pools, casual-oriented pools; intent captured upfront as profile fields and pool filters.
- **Curation delivery style** — daily batch delivery vs continuously learned feeds vs user-driven search vs questionnaire-driven ordering; curation depth varies with the relationship-first philosophy (products positioned for serious outcomes invest in compatibility machinery and post-date feedback).
- **Conversation-to-offline friction** — icebreakers, chat limits, post-date follow-ups, "designed to be deleted" positioning: design philosophies that push the loop's exit offline.
- **Profile content emphasis** — prompts and personality answers; structured values/lifestyle/family-plan fields; questionnaire batteries.
- **Platonic side-modes** — some consumer products embed friend-finding modes beside dating; these are multi-mode embeddings of a different Type (Friend Discovery Application, §01.05), not content of this leaf.

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Hinge: "designed to be deleted" brand philosophy; Hinge+ / HingeX tier names; Nobel-Prize-winning algorithm claim; Hinge Labs research group; post-phone-number-exchange date follow-up as a named mechanism.
- Coffee Meets Bagel: "bagels" product vocabulary; sister-founders origin story; "91% of CMB Daters" and "150 million matches" vendor claims; daily-batch delivery and chat-limit mechanics (positioning-page strength only — help center unreachable).
- Plenty of Fish: "Meet Me" deck name; "Super Like" boost; "most welcoming way to date" brand line.
- OkCupid: Paid Features & Power-Ups category naming.

## Vendor-specific Findings

(Consolidated from L3 above; none of these enter the final document's defining content.)

- Hinge's date follow-up ("we ask how your dates are going… so we can make better recommendations") is the clearest documented instance of the offline-exit feedback loop in the sample.
- CMB's chat limits (conversation friction toward real life) are documented only on the product's own marketing/about pages this pass — held at that strength.
- POF's Meet Me copy confirms the mutual-consent gate for that surface; other contact paths (e.g., messaging options advertised on the home page) are not evidenced in detail this pass.

## Rejected Findings

1. **"Relationship discovery" is a market category.** REJECTED — no sampled product uses the phrase; the market's own umbrella terms are "dating app," "dating site," "online dating." The leaf phrase has no product population answering to it that does not also answer to "dating application."
2. **Relationship-forward curation = matchmaking.** REJECTED — daily batches and type-learning feeds are algorithmic selection inside a user-led loop; the user still combs and acts unilaterally; no service owns introductions or mediates activation. The ratified matchmaking seam (who-selects + who-activates, jointly load-bearing) is not crossed.
3. **The leaf is a cross-family umbrella including platonic discovery.** REJECTED for this leaf's definition — the directory places it inside §01.07 (Dating family), both sibling flags read it as an alias of the *dating* loop, and no sampled relationship-first product centers platonic discovery. The naming tension is recorded below, but platonic discovery belongs to Friend Discovery Application (§01.05), which has its own leaf.
4. **"Relationship discovery" implies a distinct relationship-*potential* workflow (compatibility scoring, relationship-stage discovery).** REJECTED at this pass's evidence level — compatibility/questionnaire machinery is documented as a dating-application variant (OkCupid-class), and no product documents a relationship-stage object or workflow that the dating core lacks. If the unreachable eHarmony-class pole were shown to possess service-owned introduction or activation mediation, it would belong to matchmaking, not here.

## Boundary Findings

With remove-tests (the §-style discriminator for each neighbor):

- **vs Dating Application** — no structural boundary. The leaf's covered products realize the Dating Application defining core without addition or subtraction; the only differentiator is intent positioning, which the dating Type itself registers as a variant. *Remove the intent framing → the same products remain, still fully recognized as Dating Applications. Remove the candidate loop → nothing remains.* This is the alias signature.
- **vs Matchmaking Platform** — who-selects + who-activates. Service-led selection AND service-mediated activation = matchmaking (introductions the service stands behind, arranged meetings, identity withheld until the mediated point). Algorithmic curation inside a user-led loop (batches, feeds) does not cross. *Remove the user's unilateral action over the pool and substitute service-owned introductions → Matchmaking Platform.*
- **vs Dating Community Platform** — organizing structure. Community container (events, groups, content) with partner discovery integrated vs the 1:1 candidate loop as the organizing structure. *Remove the candidate loop and add a community container as the designed path to partners → Dating Community Platform.*
- **vs Friend Discovery Application (§01.05)** — intent and family. Friendship intent, typically weaker consent gating, separate leaf outside the dating family. *Remove romance → Friend Discovery territory.* The English word "relationship" can cover platonic bonds; the directory's family placement and the market's own usage (relationship-first products = serious *romantic* positioning) both confine this leaf to the romantic reading.
- **vs General Social Network / Instant Messaging** — no candidate loop, no consent gate, no pairing lifecycle; contact anchored to existing/follower graphs or personal contacts. Unchanged from the sibling passes' findings.

**Taxonomy determination**: the leaf is an **umbrella alias of Dating Application**, not an independent Type. Its only non-inherited content — the relationship-intent layer — is (a) already a registered variant of the Dating Application Type, (b) realized in products that self-describe as dating apps, and (c) fails the defining-direction remove-test. Both pre-hung sibling flags are discharged in the alias direction. Consolidation (merging the leaf into Dating Application) is a taxonomy-pass decision and is recommended; this pass documents the leaf honestly from its own angle without rewriting the directory.

## Uncertainties

1. **The curated-machinery pole remains unverified.** eHarmony-class products were unreachable in this pass (403 ×2) and in the matchmaking pass. If a product exists that delivers matches with NO user-facing candidate stream and NO service-owned introduction/activation, the who-selects test places it in the Dating Application questionnaire pole — but that needs direct evidence; it stays open. This pass neither ratifies nor refutes the matchmaking pass's open question.
2. **CMB operational mechanics unverified.** Chat-limit windows, batch sizes, any expiry rules: help center unreachable (transport error + 403). Only positioning-page copy stands; no numbers asserted anywhere.
3. **OkCupid loop mechanics not directly evidenced.** Help root categories only; the questionnaire loop is held at market-context strength inherited from the dating-application pass.
4. **POF contact paths beyond Meet Me not evidenced.** Home-page copy advertises multiple connection options; current rules not documented from reachable pages.
5. **Regional usage of "relationship discovery" as a term** was not researched beyond English-language sources. If a regional market uses the phrase as a live category with distinct structure, the alias determination would need revisiting.
6. **The platonic reading** ("relationship" ⊃ friendship) is a naming tension, not a resolved taxonomy question; recorded in Boundary Findings. If the taxonomy ever wants a cross-family "relationship discovery" umbrella (romantic + platonic + professional), that is a consolidation-pass redesign, not a finding of this pass.

## Final Synthesis

**Relationship Discovery Application is an umbrella alias of the Dating Application.** The market's relationship-first products — the strongest candidates to instantiate a distinct Type — self-describe as dating apps and run the identical user-led candidate loop: evaluation-oriented profile, candidate discovery over the product's own pool, unilateral interest expression, mutual-consent contact gate, private two-person conversation with a controllable pairing lifecycle, designed to exit offline.

What the leaf genuinely contributes is the **relationship-intent layer**: serious-intent pools, intent-forward profile content (upfront intent questions, values and family-plan fields), investment in compatibility/curation machinery inside the loop, and conversation design that pushes toward offline contact. Every element of that layer is a positioning/design specialization of the dating loop — documented as a variant of the Dating Application Type — and fails the defining-direction remove-test for independent Type status.

The alias determination discharges both pre-hung sibling flags (dating-application, matchmaking-platform). The final document is written from the leaf's own angle — the relationship-intent segment of the user-led candidate-discovery loop — with the naming fact stated plainly and consolidation recommended at a taxonomy pass.
