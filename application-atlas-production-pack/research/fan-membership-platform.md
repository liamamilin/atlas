# Research Notes — Fan Membership Platform

Research date: 2026-09-07
Status: leaf processed under v1.1 methodology
Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Paid Community Platform [unprocessed], Creator Subscription Platform [processed 2026-09-07 — this pass is the designated joint-review counterparty], Creator Tip Platform [processed], Creator Storefront [processed], Digital Product Commerce Platform [processed], Creator Course Commerce Platform [processed], Coaching Commerce Platform [processed], Creator CRM [processed], Creator Revenue Management [processed], Creator Affiliate Dashboard [processed]; related neighbors: Fan Engagement Platform [processed — label-collision counterparty], Membership Management System / Member Portal §25, Online Donation Platform §25, Media Subscription Management §27)

---

## Research Goal

Understand what a "Fan Membership Platform" is as an Application Type, and discharge the joint-review obligation recorded by the Creator Subscription Platform pass: determine whether fan-membership-platform is a near-alias of creator-subscription-platform (as flagged) or a defensible sibling with its own center of gravity; establish the defining core, the membership/belonging emphasis evidence, the billing-and-benefit lifecycle, and the boundary against the §27 creator cluster and the §25 membership family.

## Initial Boundary

- Working hypothesis: a platform where a fan becomes a recurring-paying *member* of a specific creator's membership program (fan club / membership program), receiving member status and declared benefits while membership is active; the creator authors plans/levels, manages the member roster, and receives the dues.
- Primary users: the creator (plan author, member-roster operator, benefit provider) and the fan (member).
- Nearest confusions going in:
  1. **Creator Subscription Platform (§27 sibling)** — flagged NEAR-ALIAS; market uses "membership" and "subscription" interchangeably for the same recurring fan→creator structure. This pass is the joint-review counterparty.
  2. **Paid Community Platform (§27 sibling, unprocessed)** — venue access vs creator membership benefits.
  3. **Fan Engagement Platform (§27, processed)** — label collision: creator-economy products sometimes self-label "fan engagement"; that pass routed them here / to Creator Subscription.
  4. **Membership Management System / Member Portal (§25)** — business/association memberships; the counterparty is an organization, not a creator.
  5. **Online Donation Platform (§25)** — one-time vs standing.
  6. **Creator Tip Platform (§27, processed)** — one-time act vs standing membership.
- Cluster seam test carried from prior passes: **what a purchase converts into** (coaching → tracked human-service engagement; course → curriculum access; storefront → goods/downloads; community → venue; subscription → standing entitlement). Feature presence is explicitly NOT the seam.
- This pass deliberately samples the *membership-emphasis* products (fan-club realizations) that the sibling pass did not sample directly, to give the joint review independent evidence.

## Research Questions

1. What is the central object — the membership, the member, the plan/level? How do they relate?
2. What does a fan's recurring payment convert into in the membership reading (member standing, declared benefits, member-limited access)?
3. What benefit types do platforms support (limited content, member roles, goods, experiences, back-catalog)?
4. How does the membership lifecycle work (join, renew, lapse/expiry, upgrade/downgrade, cancel, rejoin, comp)?
5. What does the fan-side surface contain (join page, benefits, member self-service) vs the creator-side surface (plan editor, roster, benefit ops, messaging, earnings)?
6. How do regional realizations differ (Japanese fan-club platforms: dues vocabulary, capacity, closure, payment rails, legal disclosures)?
7. Joint review: is fan-membership-platform an alias of creator-subscription-platform, or keep-both on an emphasis axis?
8. Where are the boundaries vs Paid Community, Tip, Fan Engagement, §25 membership family, donation, media subscription?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers + regional coverage, deliberately disjoint from the sibling pass's direct samples (Ghost, Memberful) except where overlap is market-central:

1. **Buy Me a Coffee (BMAC)** — support-first creator platform whose recurring product is literally named "memberships" (levels, rewards, supporter billing). Tier-1 official help center, fully reachable and fetched this pass. Solo-creator tier.
2. **Fantia** — Japanese fan-club platform ("ファンクラブプラットフォーム"), self-described as a fan-club platform where fans join creators' fan clubs with membership dues (会費). Tier-1 official help center, fully reachable and fetched this pass. Regional pole; different payment rails and legal context.
3. **Patreon** — the canonical fan-membership/patronage platform; structural treatment only. support.patreon.com, patreon.com, and docs.patreon.com all unreachable this pass (timeouts; 3+ attempts across domains, consistent with two prior passes). Its platform-managed billing posture is taken from official Ghost migration documentation (verified in the paired sibling pass, 2026-09-07).
4. **Platform-native channel memberships (YouTube/Twitch-class)** — structural pole only; support.google.com/youtube article unreachable (timeout ×2). Not sampled directly; no product-specific claims.

Unreachable this pass (recorded as limitations, not silently substituted from memory): support.patreon.com (timeout ×2), patreon.com (timeout), docs.patreon.com (timeout), help.ko-fi.com (transport error), ko-fi.com (403), support.google.com/youtube channel memberships (timeout ×2), fanbox.cc (timeout ×2), weverse/bubble idol-fan-club surfaces (not attempted after the above pattern — treated as unverified territory).

## Sources

### Buy Me a Coffee (Tier 1 — official help center, fetched 2026-09-07)
- A simple guide to get started with memberships — https://help.buymeacoffee.com/en/articles/9969554 (level creation, rewards, member limits, Discord roles, welcome message, page settings, giveaways, level lifecycle pause/unpublish/delete, billing, dunning, cancellation, price-for-life, lifetime, messaging, renewal notifications)

### Fantia (Tier 1 — official help center, fetched 2026-09-07)
- Help center index — https://help.fantia.jp/ (full navigation map: fan-side and creator-side collections)
- ファンティアとは何ですか？ — https://help.fantia.jp/237 (platform definition)
- どんなプランを作成すればいいですか？ — https://help.fantia.jp/567 (plan model, genre price ladders, plan creation)
- 会員プランはいくらまで設定できますか？ — https://help.fantia.jp/252 (price range, plan-count; via related-article snippet)
- 一度作成した会員プランは編集できますか？ — https://help.fantia.jp/253 (amount uneditable; delete-recreate; via related-article snippet)
- 一度作成した会員プランは削除できますか？ — https://help.fantia.jp/254 (deletion semantics; via related-article snippet)
- 有料プランの有効期限とはなんですか？ — https://help.fantia.jp/319 (expiry = entitlement window; monthly auto-renewal)
- Related-article snippets observed on the above pages: /291 (join benefits), /723 (recruitment-ended state), /296 (fan club closure), /294 (leaving a plan), /2506 (fulfillment timing disclosure), /651 (free plan undeletable)
- Fantia root — https://fantia.jp/ (positioning: ファンクラブプラットフォーム; shop→fan club upgrade; plan/limited-content/commission features)

### Patreon (Tier 2 — structural only)
- Via official Ghost migration documentation https://docs.ghost.org/migration/patreon/ (fetched and verified in the paired creator-subscription-platform pass, 2026-09-07): "Patreon manages your subscriptions on your behalf"; patron CSV export from patreon.com/members; complimentary-status cross-platform pattern.

### Cluster evidence (in-repo, prior passes)
- research/creator-subscription-platform.md (Ghost / Memberful / BMAC direct; Patreon / Substack structural; L0–L3; boundary findings; near-alias flag)
- STATUS.md Boundary Issues lines for creator-subscription-platform (near-alias risk, joint-review recommendation) and fan-engagement-platform (label-collision note naming this leaf as counterparty)

Evidence layers used below: **A** = directly observed on an official source for a specific product this pass; **A′** = directly observed official evidence recorded in a paired prior pass and re-verified in-repo; **B** = cross-product commonality across the researched sample; **C** = canonical inference from comparison + boundary reasoning.

---

## Product A — Buy Me a Coffee (direct, Layer A)

### Key observations

- **Positioning**: "Buy Me a Coffee is best known for allowing creators to receive one-time support, but what if you could get support every month? That's where memberships come in! Setting up different membership levels allows you to turn your income into something steady and reliable." One account spans one-time supports, memberships, shop, posts, messaging.
- **Membership level = creator-authored offer**: name, image, description, **monthly and yearly subscription fees**; **rewards** selected from a reward library or custom-written ("You can add as many rewards as you want", reorderable); **welcome message** shown to the member after payment completes.
- **Level controls**: limit the number of members per level (workload management or exclusivity/urgency); connect Discord roles per level ("exclusive channels, special badges"); highlight a level on the page.
- **Page settings**: accept annual memberships (pay a year upfront); display member count (social proof); display monthly earnings (progress/growth motivation).
- **Membership giveaways**: comped memberships with expiry "as short as 7 days" so people can "experience the perks firsthand".
- **Level lifecycle**: edit anytime; **pause** (stops billing for current members and blocks new sign-ups; 1/3/6-month periods with auto-resume; can unpause early); **unpublish** (stops new members; current members keep content and keep being billed); **delete** (permanent; only when no active members or posts).
- **Billing**: "Memberships renew either monthly or yearly… This continues automatically unless the member or creator cancels or if the card doesn't have enough funds." Members charged immediately on subscribe, then billed on the same calendar day monthly (or yearly) from first payment. Renewal triggers an email notification to the member.
- **Dunning**: "If the card lacks balance, the system will try up to three more times. If the payment still fails, the membership is canceled." (Same for yearly.)
- **Cancellation**: member can cancel anytime; access to all benefits continues "until the current subscription period (monthly or yearly) ends, but no further renewals will occur". Canceling right after subscribing does not stop the initial payment. **Creators can also cancel a member's subscription** from the member's profile.
- **Price grandfathering**: "Whatever price people are charged when they sign up for the Membership is their price for life. Only your new members will be charged the new price."
- **Lifetime membership**: a lifetime option lets supporters "become members forever with a single payment".
- **Member messaging**: creator selects a member group, types a message, sends.
- **Tips for creators** (product's own framing of benefits): bonus content, private forum access, behind-the-scenes updates, physical rewards like stickers or T-shirts; start with one level and add tiers as the community grows.

### Reading
BMAC is the support-first membership realization: the recurring product is framed as *monthly support* expressed as membership levels with rewards. It carries the full membership lifecycle (levels → join → auto-renew → dunning → cancel-at-period-end → comp → lifetime) and the belonging vocabulary (member count, welcome message, Discord roles/badges).

---

## Product B — Fantia (direct, Layer A)

### Key observations

- **Positioning**: "ファンティア[Fantia]はクリエイター支援プラットフォームです" — a creator-support platform; the root page self-describes Fantia as "国内最大級の**ファンクラブ**プラットフォーム" (one of Japan's largest **fan-club** platforms). Creators open a **ファンクラブ (fan club)**; fans join (入会/参加).
- **Fan club → plans**: "ファンクラブでは、無料プランのほか、ご希望の会費でファンの方に限定特典を提供する「有料プラン」を作成できます" — free plans plus paid plans at a creator-chosen dues (会費) providing limited perks (限定特典); plans can also gate product sales (plan-limited shop items).
- **Content model**: posts split into 公開コンテンツ (public content) and 限定コンテンツ (limited content viewable only by joined fans); back numbers (バックナンバー) give access to past limited content (fan-side help collections for both, plus 投稿セレクト).
- **Plan model (creator-side)**: paid-plan price range 100–100,000 yen; no plan-count limit ("設定できるプランの数に上限はありません"); genre model cases show price-perk ladders (e.g. illustration: 0 yen public art / 500 yen hi-res + unpublished / 1000 yen PSD + doujinshi). **A plan's amount cannot be edited after creation** — to change price, apply to delete the plan and create a new one; deletion with existing members stops new joins immediately and takes effect at the end of the following month. Free plans cannot be deleted but can be effectively closed with a 1-person member cap.
- **Join benefits (fan-side)**: joining a fan club grants viewing of fan-club limited content, notifications of new posts, and the ability to purchase member-limited goods.
- **Entitlement window**: a paid plan's 有効期限 (valid period) is "the period during which the member can view that plan's member-limited content"; joined plans "auto-renew monthly (月単位で加入期間が自動更新)"; when the period lapses, viewing/purchasing that plan's limited content becomes unavailable. The member's joined-club list shows each plan's expiry.
- **Capacity/recruitment**: a plan shows 募集終了 (recruitment ended) when it reaches the creator-set recruitment limit (募集人数) or when deletion was applied; the creator can raise the limit to reopen.
- **Leave/switch**: members leave a plan (退会) from the plan list or via "プランを変更" (change plan); upgrade (more expensive plan) and downgrade are documented fan flows; switching plans does not change the join date (per article title); monthly-cycle notes exist (bodies not individually fetched beyond titles/snippets).
- **Club closure**: a fan club auto-closes the month after the creator applies for closure; plan members keep limited-content access until the end of the following month.
- **Fan-side participation layer (belonging emphasis)**: 支援ポイント (support points — earned through activity), スタンプ (stamps/stamp books), 応援メッセージ (support messages with display order), チップ (tips), 上乗せ支援 (add-on support above the dues, one-time or recurring, changeable/stoppable), メッセージ (private messages between fan and creator), 友達招待 (friend-invite campaigns with platform coins).
- **Payments (regional rails)**: credit card (3D Secure), bank transfer (Pay-easy), convenience-store payment, platform coins (とらコイン), atone deferred payment, Minna Bank; multi-month lump payment of dues; refunds routed per method.
- **Earnings (creator-side)**: monthly settlement of fan-club membership fees and product sales; transfer application to a bank account (or conversion to platform coins); **category-based platform fees**; tax/withholding documentation; overseas-account transfer.
- **Legal/compliance surfaces**: 特定商取引法 (Act on Specified Commercial Transactions) display settings required for opening a fan club; adult-content filings (AV新法 documents attachable to posts/products); age verification/ID submission for creators; fulfillment-timing disclosure (dues/DL/post-sales fulfilled immediately on payment; physical goods shipped within 7 days).
- **Privacy rule**: joining does not pass the fan's email/card details to the creator; personal details pass only for physical-goods shipping ("自宅から発送" goods).

### Reading
Fantia is the fan-club realization: the container is the creator's *fan club*, the recurring payment is *membership dues* (会費/会員費), the entitlement is member-limited content and member-limited goods, and the fan-side surface is thick with belonging/participation machinery (points, stamps, support messages, add-on support, invites). The lifecycle runs on monthly auto-renewal with explicit expiry windows, capacity limits, closure grace periods, and no plan-price edits (delete-recreate instead). Regional payment rails and statutory disclosures are native.

---

## Product C — Patreon (structural, Layer A′ via official Ghost migration doc)

- "Since Patreon manages your subscriptions on your behalf, there is no direct migration path to move your paid subscriptions from Patreon to other platforms." — Patreon operates the billing relationship for the creator (platform-managed payments pole).
- Creators export their patron/member list as CSV from patreon.com/members (email required for import elsewhere); cross-platform pattern: import patrons with complimentary/paid status while billing stays in Patreon.
- All three Patreon domains unreachable this pass (recorded limitation). No Patreon-specific workflow claims beyond the above. Patreon's "memberships" vocabulary (patrons as members, tiered memberships) is market-common but is not asserted here from primary evidence.

## Product D — Platform-native channel memberships (structural pole, no direct evidence)

- Market-common shape (recurring fan payments to a channel/creator inside a large content platform, with tiers/perks/badges) is widely known, but the official documentation was unreachable this pass (timeout ×2). Treated as a structural packaging pole only; no operational claims.

---

## Cross-product Comparison

| Dimension | Buy Me a Coffee | Fantia | Patreon (structural) | Platform-native (structural) |
|---|---|---|---|---|
| Container | creator page with membership levels | creator's ファン club (fan club) | creator page (patrons) | channel/creator inside a big platform |
| Offer unit | membership level (name/img/desc + monthly/yearly fees + rewards) | plan (無料プラン / 有料プラン at chosen 会費 with 限定特典) | tiers (structural) | membership tiers (structural) |
| Recurring core | auto-renews monthly/yearly until cancel/failure | monthly auto-renewal of 有効期限 | platform-managed recurring billing | recurring (structural) |
| Benefit/entitlement | rewards/perks, members-only posts, Discord roles/badges, welcome message | member-limited content, member-limited goods, back numbers | perks per tier (structural) | perks/badges (structural) |
| Entitlement ↔ state | access until period end after cancel; canceled on dunning failure | expiry window explicit; lapsed = cannot view/purchase; closure grace till end of next month | platform-managed | platform-managed |
| Capacity limits | member-limit per level (optional) | 募集人数 limit; 募集終了 state (native) | — | — |
| Comps | giveaways (7-day min expiry) | free tickets (無料チケット); gift codes | complimentary status (structural) | — |
| Pause | level pause 1/3/6 months | (not observed) | — | — |
| Price change | price-for-life grandfathering (new members pay new price) | amount uneditable → delete-recreate; deletion end of following month | — | — |
| Lifetime | lifetime membership (single payment) | (not observed) | — | — |
| Community attach | Discord roles per level | platform-native comments/messages; member messaging | community feed (structural) | platform-native |
| Fan-side belonging | welcome message, member count, supporter framing | support points, stamps, 応援メッセージ, add-on support, invites | — | — |
| Extras beside dues | one-time tips, shop | tips, add-on support (上乗せ支援), commissions, goods shop | — | — |
| Earnings rail | platform payouts (moderation-gated; per sibling pass) | monthly settlement → bank transfer or coins; category-based platform fees | platform-managed | platform revenue share (structural) |
| Regional/legal | — | convenience-store/bank/coins/atone; 特定商取引法 display; AV新法; age verification; fulfillment-timing disclosure | — | — |

**Stop condition check.** With two direct Tier-1 samples at opposite cultural poles (BMAC English-language support-first; Fantia Japanese fan-club), one structural platform-managed pole (Patreon), and the sibling pass's direct samples (Ghost/Memberful — publishing-native pole), the core model, lifecycle, and boundary behavior are stable; further samples would repeat evidence. Stopping.

---

## Canonical Abstraction

### L0 — Defining Invariant

A Fan Membership Platform is recognizable when all four hold; remove any one and it becomes a different Type:

1. **Fan→creator recurring membership dues** — the fan pays recurring dues (membership fees) to a *specific creator* for belonging to that creator's membership program/fan club. Remove recurrence → Creator Tip Platform (one-time support). Remove the individual creator as counterparty (business membership / platform catalog) → §25 Membership Management or Media Subscription.
2. **Creator-authored membership plan/level** — the creator defines the membership offer: named plan/level carrying dues and declared member benefits. Single-plan offers are the degenerate case; tier ladders are the common shape but not the invariant. Remove creator-authored offers → platform-defined media subscription.
3. **State-linked member standing and benefits** — while the membership is active, the fan holds member standing and the plan's declared benefits (most concretely member-limited content/goods access); granted on joining, maintained across renewals, ended by lapse or cancellation (with period-end or grace semantics varying by product). Remove state-linked standing fulfillment (buy discrete goods instead) → storefront / digital product commerce.
4. **Creator-side membership management** — the creator operates the program: author plans, see and manage the member roster (comp, cancel, respond), communicate with members, and receive the dues (platform payout or creator-owned processor). Remove it → a bare payment processor, not an application.

Deliberately NOT in L0 (modern common, not definitional): tier ladders, free plans, member-count displays, welcome messages, Discord/community roles, gamification (points/stamps), capacity limits, back numbers, giveaways, pause, lifetime membership, digital delivery itself, any specific payment rail.

### L1 — Common Mature Structure

Present across the researched sample (Layer B unless noted):

- **Multiple plans/levels with a price–perk gradient** (BMAC levels; Fantia genre ladders; Patreon tiers structurally)
- **Free plan/free side as funnel** (Fantia free plan native and undeletable; BMAC's free-side funnel is one-time supporters instead — common, not universal)
- **Members-only content posting** (public vs member-limited split — Fantia explicit; BMAC members-only posts; sibling samples identical)
- **Auto-renewal until cancel or payment failure, with renewal notifications** (BMAC explicit; Fantia monthly auto-renewal of the valid period)
- **Cancel semantics: stop renewals, keep access until period end** (BMAC explicit; Fantia expiry model; sibling samples identical)
- **Dunning/failed-payment handling** (BMAC 3 retries then cancel; sibling: Memberful retry-then-deactivate, Ghost via Stripe)
- **Comped memberships** (BMAC giveaways with expiry; Fantia free tickets and gift codes; sibling: comps/free access)
- **Creator→member communication** (BMAC member-group messaging; Fantia creator↔fan messages and support messages)
- **Member-limited goods purchasing** (Fantia member-limited shop items; BMAC rewards include physical items)
- **Member self-service** (join/leave/switch plans — Fantia plan-change flows; BMAC cancel; sibling: member account management)
- **Earnings path** (Fantia monthly settlement/transfer application; BMAC platform payouts; sibling: creator-owned Stripe pole)
- **Price stability for existing members** (BMAC price-for-life; Fantia uneditable plan amounts — different mechanisms, same posture; sibling: grandfathering pattern)
- **Upgrade/downgrade between plans** (Fantia explicit; sibling: plan switching)
- **Recurring-revenue/member metrics** (BMAC display toggles; Fantia dashboard/confirmed-member counts; sibling: MRR/churn)
- **Platform fee / payout machinery** (Fantia category-based fees; sibling poles documented)

### L2 — Variant / Optional Structure

- **Packaging**: standalone fan-membership platform (BMAC, Fantia) / publishing-native memberships (Ghost/Substack — sibling) / embedded infrastructure on the creator's own site (Memberful — sibling) / platform-native channel memberships inside large content platforms (structural pole)
- **Payment posture**: platform-managed payouts with platform fee (BMAC, Fantia, Patreon) ↔ creator-owned processor with 0% platform fee (Ghost/Memberful — sibling)
- **Regional payment rails and compliance** (Fantia: convenience store, bank transfer/Pay-easy, coins, deferred payment, multi-month lump sums; statutory transaction disclosures; adult-content filings; age verification) — region-shaped variant
- **Belonging/participation machinery** (Fantia support points, stamps, 応援メッセージ, add-on support, friend-invite campaigns; BMAC welcome message + member-count social proof) — the membership-emphasis signature; present in degrees elsewhere
- **Capacity/exclusivity controls** (BMAC member limits; Fantia recruitment limits with 募集終了 states)
- **Level lifecycle operations** (BMAC pause/unpublish/delete semantics; Fantia plan deletion with grace period; sibling: pause)
- **Lifetime membership** — one-time payment for permanent standing (BMAC explicit; sibling flags it bending recurrence); documented as a variant, not the definition
- **Back-catalog access** (Fantia back numbers / post-select; sibling: private podcast feeds and archives)
- **Adjacent earning mechanisms in the same account** (tips, commissions/requests, goods shop — BMAC and Fantia both bundle these; feature presence is not the seam)
- **Adult-content specialization** (Fantia R18 segmentation with filings; market-known elsewhere; not asserted beyond Fantia's own documents)
- **Audience scale**: solo creators ↔ professional publishers (sibling samples) ↔ idol/agency fan-club operations (unverified this pass)

### L3 — Vendor-specific (research notes only)

- **BMAC**: reward library; 7-day minimum giveaway expiry; pause periods 1/3/6 months with auto-resume; unpublish vs delete semantics (delete requires zero active members/posts); billing on the same calendar day monthly/yearly from first payment; renewal notification emails; dunning = 3 further attempts then cancel; creator-side member cancel via "view info"; member-count and monthly-earnings display toggles; lifetime membership; moderation gates before payouts (per sibling pass).
- **Fantia**: fan-club container and 会費 vocabulary; plan price range 100–100,000 yen; plan-count uncapped; plan amount uneditable (delete-recreate; deletion at end of following month with new-join stop); free plan undeletable (cap-1 workaround); free tickets and gift codes; back numbers and 投稿セレクト; support points/stamps/応援メッセージ; add-on support (one-time at join/change, or recurring on the next month's dues; changeable/stoppable); tips; commissions; friend-invite campaigns with とらコイン; payment rails (credit card + 3D Secure, Pay-easy, convenience store, とらコイン, atone, Minna Bank); monthly settlement with transfer application, category-based platform fees, overseas transfer; 特定商取引法 display requirement; AV新法 document attachment; age verification/ID; fulfillment-timing disclosure (immediate for dues/DL/tips; ≤7 days ship for physical goods); fan privacy rule (no personal data to creator except physical shipping); fan club closure auto after application month with access till end of next month; fan-club freeze (凍結) state.
- **Patreon** (structural): platform-managed billing ("on your behalf"); patron CSV export; complimentary-status cross-platform pattern. Help center unreachable across three passes.

---

## Rejected Findings (considered and not promoted)

- **"Membership ≠ subscription" as a structural claim** — rejected: the recurring-payment core, the offer structure, and the entitlement lifecycle are the same in both readings; the difference is emphasis/vocabulary (see joint review below). BMAC calls its recurring product "memberships" bought with "subscription fees".
- **"Tiers/levels are definitional"** — rejected: single-plan membership programs exist (Substack's publication-level paid subscription is the sibling's structural evidence; BMAC's own advice is to start with one level).
- **"Belonging machinery (points/stamps/badges) is definitional"** — rejected: it is Fantia-strong and BMAC-weak; common-not-core. The invariant is member standing + declared benefits, not gamification.
- **"Member-limited content is definitional"** — rejected as invariant (though it is the most common benefit): pure-support memberships with nominally empty benefit sets are a known pattern (sibling pass), and physical/experience perks appear without content gating.
- **"Capacity limits are definitional"** — rejected: optional in both direct samples.
- **"Digital delivery is definitional"** — rejected by the historical check: postal fan clubs with annual dues and mailed newsletters satisfy the core.
- **"Platform must process payments"** — rejected: the sibling's creator-owned-processor pole (Ghost/Memberful) satisfies the core.

## Boundary Findings

1. **vs Creator Subscription Platform (§27 sibling) — JOINT REVIEW DISCHARGED, keep-both on an emphasis axis.** The sibling pass flagged this leaf as the highest near-alias risk in the cluster and recommended joint review with candidate outcomes "merge" or "keep-both on the payment-vs-belonging emphasis axis". This pass's independent membership-side evidence (BMAC + Fantia) confirms the sibling's facts: the market uses both words for one recurring fan→creator structure (BMAC "memberships"/"subscription fees"; Ghost "paid members"/"paid subscriptions"; Patreon "patrons/members"; Fantia 会費/会員費 under a subscription-style monthly renewal). Direct evidence also confirms the caveat: every sampled product exhibits both emphases in one structure. **Outcome: keep-both leaves, one shared defining core, differentiated centers of gravity** — Creator Subscription Platform foregrounds the recurring payment relationship and the gated output stream (publishing-native products); Fan Membership Platform foregrounds the fan's standing membership in a creator's program with declared benefits and belonging machinery (fan-club/support products). The seam is emphasis and product vocabulary, not structure. Both documents cross-reference the other; the directory owner may still prefer a merge (one Type, two market names) — recorded for review. Lifetime membership remains flagged as the recurrence-bending edge case in both.
2. **vs Paid Community Platform (§27 sibling, unprocessed)** — fulfillment-structure test: a paid community sells access to a *venue* (the space is the product); a fan membership sells standing in a creator's *membership program* with the creator's output/benefits as the declared return. Community attachment is a declared benefit here (Discord roles; member messaging), not the container. Diagnostic: remove the creator's program/benefits and keep the venue → Paid Community Platform.
3. **vs Creator Tip Platform (§27 sibling, processed)** — recurrence is the seam: tips are one-time acts with no standing; memberships are standing commitments. Both direct samples ship tips in the same account as memberships (BMAC one-time supports; Fantia チップ + 上乗せ支援) — feature presence is not the seam (cluster-established test). Diagnostic: remove auto-renewal and standing → tip.
4. **vs Fan Engagement Platform (§27, processed) — label-collision counterparty confirmation.** That pass recorded that creator-economy products loosely self-label "fan engagement" and routed them to this leaf / Creator Subscription. Confirmed from this side: the operator here is an individual creator and the fan *pays*; the Fan Engagement Platform's operator is a rights-holding organization and participation is free with indirect monetization. Remove the payment and the creator; add the organization's fan database → that Type.
5. **vs Membership Management System / Member Portal (§25)** — family resemblance in vocabulary (members, dues, roster, renewal) but different counterparty and fulfillment: §25 membership systems serve organizations (associations, gyms, churches) whose members pay for organizational standing/services; here the counterparty is a specific creator and the fulfillment is the creator's output/benefits. Diagnostic: replace the creator with an organization and the benefits with organizational services → §25.
6. **vs Online Donation Platform (§25)** — donations are voluntary, typically one-off or loosely recurring gifts with no declared benefit set and no member standing; memberships carry declared benefits and standing. Support framing overlaps (Fantia's 支援 = support vocabulary) but the standing/benefit structure is the seam.
7. **vs Creator Storefront / Digital Product Commerce (§27, processed)** — goods purchase converts into discrete goods/downloads; membership dues convert into standing member benefits. Member-limited shop items (Fantia) and bundled rewards (BMAC) sit *inside* the membership benefit set — feature presence is not the seam.
8. **vs Media Subscription Management (§27) / Video Streaming Platform** — counterparty test: media subscriptions are paid to a platform/publisher for a catalog; fan memberships are paid to an individual creator. Remove the individual creator → media subscription.
9. **vs Creator CRM (§27, processed)** — the member roster here is a CRM-shaped component; the Type centers the fan-facing membership experience and dues billing, not creator-side person records/progression. Consistent with that pass's recorded seam.
10. **vs Creator Revenue Management (§27, processed)** — this Type is a fan-facing earning mechanism; revenue management is the creator-side money layer above mechanisms. Objects differ (membership/benefit vs income record/payout).

### "去掉什么就变成另一个 Type" tests

- Remove recurring dues (one-time) → Creator Tip Platform.
- Remove the individual creator as counterparty → §25 Membership Management (organization) or Media Subscription (catalog).
- Remove creator-authored offers → platform-defined media subscription.
- Remove standing benefits (buy discrete goods) → Creator Storefront / Digital Product Commerce.
- Remove the creator's program, keep a venue → Paid Community Platform.
- Remove payment entirely (free participation, org-run engagement loop) → Fan Engagement Platform.
- Remove the fan-facing membership surface (keep creator-side records) → Creator CRM.

### Taxonomy observation (for STATUS.md Boundary Issues)

Joint review with creator-subscription-platform discharged: keep-both on the emphasis axis (payment-and-stream vs belonging-and-benefits), with the explicit caveat that all sampled products exhibit both emphases in one structure and that a merge remains a defensible directory-owner choice. Fan Membership Platform's independent evidentiary value: the fan-club/belonging realizations (Fantia) and support-first memberships (BMAC) — the membership-emphasis pole the sibling pass could not sample directly. Platform-native channel memberships remain a structural pole with no direct evidence in either pass (docs unreachable in both).

### Historical / market-sample check (§24)

Would older/regional/platform-native products still fit?

- **20th-century fan club with annual dues (postal era)**: fans pay recurring dues to a specific performer's club, receive club newsletters/perks, and are kept on the club's roster; the club maintains dues records. Satisfies L0 fully — the "membership" word itself is the belonging emphasis. No digital delivery, no tiers, no platform — fits.
- **Japanese fan-club tradition / 応援 culture (regional)**: Fantia's realization is the direct digitization of fan-club dues and member-limited benefits; fits.
- **Platform-native channel memberships (YouTube/Twitch-class)**: recurring fan payments to a channel with tiers/perks — fits structurally; not directly evidenced this pass.
- **Counter-checks**: a gym or association membership fails L0 (counterparty is a business/organization, not a creator's program — §25); a one-time tip fails (no standing/recurrence); a Netflix subscription fails (platform catalog, not creator-authored offer); a paid community venue fails (venue, not creator program).

Therefore L0 must not include: digital delivery, tier ladders, free plans, belonging gamification, capacity limits, community attachment, specific payment rails, pause/lifetime mechanics. The identity abstraction is "recurring fan→creator membership standing with offer-defined benefits", not "Patreon-style tier page" and not "newsletter paywall".

## Uncertainties

1. **Patreon help center / API docs unreachable** (timeouts across three passes and multiple domains) — Patreon treated structurally only. Its tier/perk-fulfillment machinery (e.g., perk delivery tooling) is not asserted.
2. **Platform-native channel memberships (YouTube/Twitch-class) unreachable in both passes** — packaging pole described structurally; whether their machinery differs materially (revenue-share terms, tier rigidity, member badge mechanics) is unknown.
3. **Ko-fi / pixiv FANBOX / Weverse / bubble unreachable this pass** — the membership-side sample is two products deep (BMAC, Fantia) plus structural poles; assertions of cross-product commonality lean on the sibling pass's direct samples (Ghost/Memberful/BMAC) for the third leg. Where a claim rests on only BMAC + Fantia, it is marked as such in L1.
4. **Fantia article bodies only partially fetched** (nav-heavy pages; related-article snippets carry precise facts) — plan-change join-date semantics and monthly-cycle leave timing observed only in titles; not asserted in detail.
5. **Idol/agency fan-club operations (Weverse/bubble-class)** — widely associated with the membership emphasis; zero official evidence this pass; left unverified, no claims made.
6. **Free-plan universality** — Fantia has a native free plan; BMAC does not (one-time supporters as funnel); sibling samples mixed. L1 phrased "common, not universal".
7. **Entitlement edge timing** — exactly when access ends at lapse/cancel varies (BMAC: period end; Fantia: expiry window with closure grace; Memberful: dunning deactivation). Asserted only as "benefits follow membership state; exact edge semantics are product-dependent".

## Final Synthesis

A Fan Membership Platform is the fan-side membership application of the creator economy: the fan becomes a recurring-dues member of a specific creator's membership program (fan club), holding member standing and the plan's declared benefits for as long as the membership is active. Its world model:

```text
Creator's membership program / fan club (container owned by one creator)
└── Membership plan / level (creator-authored: dues + declared member benefits)
    └── Membership (fan joins → recurring dues, auto-renewing until cancelled/lapsed)
        ├── state: active ⇄ paused/past-due → cancelled/expired (rejoin possible)
        └── member standing + benefits (member-limited content/goods, roles, perks)
            ↑ granted on joining, maintained across renewals
            ↓ ended by lapse/cancellation (period-end or grace semantics vary)
Creator-side management surface
└── plan authoring · member roster (comp/cancel/view) · member messaging · earnings/settlement
Fan-side surface
└── join page (levels, benefits, member count) · member hub (benefits, expiry, plan changes)
    · participation/belonging layer (messages, points, add-on support) where present
```

The defining core is deliberately small and is shared with Creator Subscription Platform: recurring fan→creator dues, a creator-authored offer, state-linked standing benefits, and creator-side management. What this leaf adds is the membership center of gravity — the fan's belonging to a program (join/roster/benefits/standing) as the primary frame, realized most distinctly in fan-club platforms and support-first membership products. Tier ladders, free plans, belonging gamification, capacity limits, community roles, back catalogs, and regional payment rails are mature-market structure, variant, or vendor detail — not definition.
