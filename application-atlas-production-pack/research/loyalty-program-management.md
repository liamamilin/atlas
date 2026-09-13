# Research Notes — Loyalty Program Management

Research date: 2026-09-08

## Research Goal

Understand what a Loyalty Program Management application actually is by studying how real products structure loyalty programs: what objects exist, how value accrues, how it redeems, who operates it, and where its boundaries sit against the two processed §05.15 siblings (Gift Card Management, Store Credit / Stored Value Platform) and the processed §06 siblings (Referral Marketing Platform, Customer Advocacy Platform, Promotion Management).

## Initial Boundary

Initial hypothesis: the Type is the brand/merchant-side system of record for running a customer loyalty program — an enrolled customer population whose recorded behavior earns program-defined value (points/stamps/status) tracked in member balances, redeemable per program rules. Nearest neighbors: gift cards (prepaid instruments), store credit (owed value), referral marketing (rewards for bringing other people), promotion management (transaction price changes), CRM (customer relationship records), membership management (dues-based access).

## Research Questions

1. What is the program as a configured object? What does it contain?
2. What is a member? How is a customer enrolled and identified?
3. How does earning work — what behaviors qualify, under what rule shapes?
4. What is the earned value? Points only? Stamps? Status?
5. How does redemption work — what forms can rewards take, how are they issued?
6. What lifecycle states exist (pending, expiry, adjustment, refund handling)?
7. What operator surfaces exist (config, member ops, campaigns, reporting)?
8. What member-facing surfaces exist (portal, panel, app, wallet, checkout)?
9. Where exactly do the seams sit vs gift cards / store credit / referral / promotion / membership?
10. Would pre-digital loyalty (stamp books, punch cards) satisfy the same core?

## Representative Products

Selected for market representation, documentation completeness, product philosophy diversity, and customer-tier diversity:

| Product | Pole | Customer tier | Evidence tier |
|---|---|---|---|
| Square Loyalty | POS-embedded loyalty module | SMB brick-and-mortar | Tier 1 (developer docs) |
| Smile.io | Self-serve e-commerce loyalty SaaS (Shopify/BigCommerce app) | SMB/mid-market D2C | Tier 1 (developer docs + fundamentals) |
| Open Loyalty | Headless / white-label loyalty engine | Enterprise / integrators | Tier 1 (user guide + API index) |
| Antavo | Enterprise standalone loyalty platform | Enterprise (retail, travel, fashion) | Tier 1 (docs portal + points-economy page) |
| Stamp Me | Mobile digital punch-card platform (minimal pole) | Small physical businesses | Tier 2 (how-it-works product page) |

Rejected/absent sample: Yotpo (Loyalty & Referrals) — docs.yotpo.com and dev.yotpo.com both unreachable (transport errors ×2 each host); support site 404. Abandoned per network-constrained rule. Paytronix/Givex-class enterprise suites (loyalty + gift card bundling) were also unreachable in this pass and in the two sibling passes — bundling posture remains structurally inferred, not observed.

## Sources

- Square — Loyalty Program overview: https://developer.squareup.com/docs/loyalty/overview (fetched 2026-09-08)
- Square — Create and Retrieve Loyalty Accounts: https://developer.squareup.com/docs/loyalty-api/loyalty-accounts (fetched 2026-09-08)
- Smile.io — Developer documentation home + index: https://docs.smile.io/ / https://dev.smile.io/llms.txt (fetched 2026-09-08)
- Smile.io — Concepts & fundamentals: https://dev.smile.io/guides/fundamentals.md (fetched 2026-09-08)
- Open Loyalty — Documentation home: https://docs.openloyalty.io/ (fetched 2026-09-08)
- Open Loyalty — User Guide index: https://docs.openloyalty.io/en/latest/userguide/index.html (fetched 2026-09-08)
- Antavo — Documentation home + index: https://docs.antavo.com/ / https://docs.antavo.com/llms.txt (fetched 2026-09-08)
- Antavo — Points economy: https://docs.antavo.com/docs/points-economy.md (fetched 2026-09-08)
- Stamp Me — How It Works: https://www.stampme.com/how-it-works (fetched 2026-09-08)
- Sibling research notes: research/gift-card-management.md, research/store-credit-stored-value-platform.md, research/referral-marketing-platform.md (Boundary Findings read as counterparty input)

## Product Observations

### Square Loyalty (evidence layer A unless noted)

- One loyalty program per seller account, with one or more participating locations; configured in the Square Dashboard (accrual rules, reward tiers). The API can read the program but cannot create/update it — configuration is an operator-console job.
- **Accrual rules** define how buyers earn points; the rule type determines the "program type":
  - Visit-based (points per visit, optional minimum spend)
  - Amount-spent (points per currency unit spent)
  - Item-based (points for specific catalog items)
  - Category-based (points for catalog categories)
- **Loyalty promotions** let sellers run temporary extra-points events on purchases.
- **Reward tiers** define redemption: points required + value + scope. Reward types: amount or percentage discount on entire sale; on specific categories; on specific items; free item from catalog. Multiple tiers = escalating redemption options ("10 points = free coffee / 15 = free sandwich"). The pricing engine applies discounts to maximize buyer value.
- **LoyaltyAccount** = program_id + customer_id (Customer Directory profile) + mapping (phone number; one phone → one account per program) + balance + lifetime_points + enrolled_at + expiring_point_deadlines (expiry schedule).
- Enrollment is opt-in: buyer agrees to terms of service at POS or on a loyalty status page; text notifications require prior ToS acceptance.
- Balance is changed only by AccumulateLoyaltyPoints / AdjustLoyaltyPoints / Create-Redeem-DeleteLoyaltyReward. **Negative balances are possible** (adjustments, refunds, exchanges) — applications must handle them.
- **Loyalty events** are searchable records of balance-changing activity — an event ledger over the account.
- Loyalty and Gift Cards are **separate product/API surfaces** under the same Customers domain (direct confirmation of the seam recorded by the store-credit pass).

### Smile.io

- Philosophy stated in docs: **"actions in, rewards out"** — the merchant's systems notify Smile of customer actions (Activities); Smile evaluates them against configured **Earning Rules** and issues rewards internally.
- Native activity types (orders, social sharing, birthdays, more) sync automatically; custom activity types enable "rewarding for any action" via the create-activity endpoint — i.e., earning events beyond purchases.
- Earn evaluation is asynchronous; when a rule matches and criteria are met, a **Reward Fulfillment** is generated. On earning, a **Points Transaction** record is created and the points balance field on the **Customer** object updates. (At activity time, the only earn payout type is points.)
- **Points Products** = the redeemable rewards, configured by the merchant (fixed or variable value); redemption happens via native UI components (Smile UI panel, Shopify checkout extensions), SDK, or API purchase endpoint. A **Points Purchase** records the spend; **Reward Fulfillments** commonly carry unique discount codes.
- **VIP Tiers** with milestones; **VIP Tier Change** objects record movement between tiers.
- **Customer Identity** objects link external systems' records to Smile customers.
- Surfaces: Smile UI (prebuilt loyalty panel + launcher), loyalty landing page, points-at-checkout (dropdown/slider), Smile Admin for merchants. Rest API + JS SDK + webhooks + app ecosystem (OAuth apps can define activity types). Referral exists as a sibling resource (Referral object + Referral Settings) on the same platform — bundling evidence.

### Open Loyalty

- Enterprise/headless engine ("technology for loyalty solutions" built for starting loyalty projects; white-label-friendly).
- User-guide model: **Customers** (accounts referenced by levels and segments), **Levels** (customer tiers reached by accumulated points; per-level fixed rewards and time-limited special rewards), **Points transfers** (add/manage point movement records), **Transactions** (transaction records matched to customers — purchase data imported, e.g. scheduled transaction import from POS), **Earning rules** ("the engine of your Loyalty Program" — from rewarding high-value customers to stopping earning entirely), **Reward Campaigns** (rewards available in the program: types, assignment to specific customers, activity time windows, redemption tracking by customer), **Segments**, **POS / Stores / Merchants** (channel registry: online and offline selling points), Admin + ACL + Analytics + Audit APIs, Webhooks, Events.
- This is the classic enterprise shape: transaction ingestion from commerce systems drives the earn engine; reward campaigns are a managed catalog with assignment and redemption accounting.

### Antavo

- Enterprise standalone "Loyalty Engine" with a Management UI. Module map (from docs index + points-economy page):
  - **Points economy** module consolidating: *Incentivized purchase* (earn rules tab), *Checkout accept* (pending points tab — points held pending until the transaction's return window clears), *Burn rules* (redemption rules tab), *Expiring points* (expiration tab).
  - **Rewards**: reward settings/categories/statistics, coupons, coupon import, offers, thank-you page, reward claim notification.
  - **Tiers**: full tiers configuration module.
  - **Gamification**: challenges, quizzes, prize wheels, contests, gamified profiling/reviews, treasure hunts, social share/follow campaigns, birthday rewards, friend referral.
  - **Workflows**: automation engine (triggers, actions, filters, flow control, modifiers) with logs — the platform automates program operations beyond simple accrual.
  - **Customers**: uniform customer profile, customer actions, customer mapping, multi-accounts, customer grouping, segments, audiences, lists.
  - **Fraud prevention**: dedicated module for detecting and preventing fraudulent actions.
  - **In-store**: wallet, stores, checkout accept, incentivized purchase; historical transaction imports, customer imports.
  - **Integrations**: marketing-automation connectors (Klaviyo, Braze, Salesforce Marketing Cloud, Emarsys, mParticle, Twilio Segment, …), webhooks, Auth0 SSO; enterprise governance (roles, user groups, MFA, SSO, content approvals, multi-language).
  - Adjacent products on the platform: **Promotion Engine** (separate promotions surface), **Optimizer** (AI insights over loyalty data), **Planner** (loyalty concept design), **Clubs** module, **Product Hub** (catalog).
- The Promotion Engine existing as a *separate* product surface is direct evidence of the loyalty-vs-promotion seam from the vendor's own architecture.

### Stamp Me (minimal pole)

- Mobile-first digital punch card: "takes the traditional 'Buy X, Get Y'-style loyalty cards and puts them on your customer's phones."
- Customer flow: download app → register details → join the business's program → **collect stamps** per transaction/purchase/check-in (count set by the business) → **reward voucher issued after the required number of stamps** → claim in-store (show voucher to staff) or online.
- Stamp validation methods (how a real-world transaction becomes an earn event): merchant app scanning the customer's **Member Code** (in-app or Apple/Google Wallet pass), NFC countertop pod, NFC tag, printed QR/alphanumeric OneStamps on products/bags, manual application via the **Loyalty Portal**.
- Business side: loyalty portal (real-time activity, member management, communications, campaigns, stamp-card editing); birthday club, gamification, random rewards; single or multi-location; **multi-brand networks** (one stamp card across banners); private-label/white-label option.
- No POS integration required ("no software, hardware or point-of-sale integration required") — the earn loop runs on explicit validation at the counter.

## Cross-product Comparison

| Structure | Square | Smile | Open Loyalty | Antavo | Stamp Me | Layer |
|---|---|---|---|---|---|---|
| Program as configured container (earn + reward rules) | ✓ (dashboard-configured; API read-only) | ✓ (Smile Admin) | ✓ (admin) | ✓ (Management UI) | ✓ (stamp-card setup) | L0 |
| Enrolled member with earned-value balance | ✓ LoyaltyAccount (balance, lifetime) | ✓ Customer points balance | ✓ Customer + points | ✓ customer profile + points | ✓ member stamp count | L0 |
| Behavior-triggered accrual under earn rules | ✓ 4 purchase-based rule shapes | ✓ earning rules over activities (purchase + non-purchase) | ✓ earning rules over imported transactions | ✓ incentivized purchase earn rules | ✓ stamps per transaction/check-in | L0 |
| Redemption per program rules (configured options) | ✓ reward tiers → discounts/free item | ✓ points products → reward fulfillment (discount codes) | ✓ reward campaigns | ✓ burn rules + rewards/coupons | ✓ voucher at stamp threshold | L0 |
| Earn-event ledger (typed point movements) | ✓ loyalty events | ✓ points transactions | ✓ points transfers | ✓ (points machinery + jobs/audit) | implicit (portal activity) | L1 |
| Manual operator adjustment of balances | ✓ AdjustLoyaltyPoints (negative possible) | ✓ points transaction add/deduct | ✓ points transfers | ✓ (jobs/imports/workflow actions) | ✓ manual stamp application | L1 |
| Identification surface binding behavior to member | ✓ phone-number mapping | ✓ customer identity linkage | ✓ transaction↔customer matching | ✓ customer mapping | ✓ member code scan / NFC tap / QR | L1 |
| Bonus/multiplier earn campaigns | ✓ loyalty promotions | (campaign surfaces; not observed in detail) | ✓ time-limited special rewards | ✓ tiered/purchase-related campaigns | ✓ campaigns | L1 |
| Expiry of earned value | ✓ expiring_point_deadlines | (points settings; not observed in detail) | (not observed) | ✓ expiring points module | (not observed) | L1 (thin in sample breadth) |
| Return/refund handling | ✓ negative balance via refund/adjustment | (not observed) | (not observed) | ✓ pending points until return window (checkout accept) | (not observed) | L1 — two observed postures |
| Member tiers / status ladder | ✗ (reward tiers are redemption options, not member status) | ✓ VIP tiers + tier changes | ✓ levels | ✓ tiers module | ✗ | L1 — common but NOT definitional |
| Member-facing balance surface | ✓ POS ToS/status page | ✓ Smile UI panel + landing page | headless (customer-facing via API) | ✓ wallet | ✓ app + wallet passes | L1 |
| Checkout/POS redemption UI | ✓ (POS reward redemption) | ✓ points-at-checkout dropdown/slider | ✓ via POS/API | ✓ in-store offers | ✓ voucher shown to staff | L1 |
| Referral as earn/bundle | ✗ | ✓ sibling resource on same platform | ✗ | ✓ friend-referral module | ✗ | L2 |
| Non-purchase earn actions (birthday, social, custom) | ✗ | ✓ native + custom activity types | (segments/limits observed; actions not detailed) | ✓ birthday, social, gamified | ✓ check-ins | L1/L2 |
| Gamification layer | ✗ | ✗ | ✗ | ✓ extensive | ✓ light | L2 |
| Fraud prevention module | ✗ | (rule criteria) | (audit) | ✓ dedicated module | ✗ | L2 |
| Marketing-automation integrations | (Square ecosystem) | (webhooks/apps) | ✓ webhooks/ACL/analytics | ✓ extensive connectors | ✓ communications | L2 |
| Headless/white-label posture | ✗ | (SDK/UI = embeddable) | ✓ core posture | ✓ API-first | ✓ private-label option | L2 |
| Multi-brand/coalition operation | ✗ | ✗ | (multi-store/merchant) | (multi-account) | ✓ multi-banner | L2 |

## Canonical Model

### L0 — Defining Invariant (jointly held; remove any one and the Type collapses)

1. **The loyalty program of record** — a brand-configured container defining how value is earned and redeemed: earn rules, redemption options, plus policy (expiry, limits, tiers where present). Without it → a CRM with customer records, or ad-hoc coupons.
2. **The enrolled member** — an identified customer holding a member account that carries a balance of earned value (and lifetime earned) within that program. Without it → anonymous promotion; without the program linkage → a CRM segment.
3. **Behavior-triggered accrual** — recorded qualifying behavior (purchases above all; non-purchase actions in mature products), evaluated against configured earn rules, moves value into the member's balance. Without it → gift cards / store credit (value issued, owed, or deposited rather than earned).
4. **Redemption under program rules** — accumulated value exchanged for configured benefits (discounts, free items, vouchers, perks) via the program's redemption options. Without it → a behavior tracker/analytics feed.

Jointly-held is load-bearing: program + members without accrual = membership roster; accrual + redemption without program = spreadsheet ledger; program + accrual without redemption = points accountancy nobody can spend.

### L1 — Common Mature Structure

- Typed earn-event ledger over each member account (points transactions / loyalty events / transfers)
- Operator identification surface binding real-world behavior to the member (phone lookup, member code scan, NFC tap, QR, email match on transaction import)
- Manual adjustments (goodwill, corrections) with full audit; negative balances possible after refunds
- Temporary bonus/multiplier earn campaigns (promotions)
- Expiry policy on earned value
- Return/refund handling — two observed postures: retroactive adjustment (Square's negative balance) vs pending hold until the return window clears (Antavo checkout accept)
- Member-facing balance surfaces (panel/portal/app/wallet pass showing balance, history, rewards)
- Redemption execution at the merchant's selling surfaces (POS redemption, checkout dropdown/slider, voucher display) with reward issuance as coupons/vouchers/instant discounts
- Member tiers / status ladders with tier benefits (3 of 5 sample products; absent in the punch-card pole and the SMB POS pole)
- Program reporting/analytics; admin roles/permissions
- Integration spine: commerce/POS event ingestion (native or via API/webhooks), marketing-automation connectors

### L2 — Variant / Optional

- Value form: points vs stamps vs visit counts; status-only programs (points-free) appear in the wider market but were not directly sampled — kept as possible variant, not asserted
- Reward payout form: coupons, instant discounts, free items, vouchers, physical/perk rewards
- Tier qualification bases (spend, points, paid)
- Non-purchase earning (birthday, social, review, custom activities)
- Gamification layers; referral modules riding the same platform
- Fraud-prevention machinery
- Paid-membership programs (dues-paid benefits) sit on the seam toward Membership Management — the behavior-earned core does not cover them
- Coalition/multi-brand programs; private-label/white-label delivery; headless engines; POS-embedded vs standalone packaging

### L3 — Vendor-specific (stays here)

- Square: one program per seller account; phone-number mapping uniqueness; API read-only program config; pricing engine maximizing discount application; ToS-gated SMS
- Smile: "actions in, rewards out" async evaluation; earn payouts are points-only at activity time; Smile UI panel/launcher; app ecosystem with OAuth
- Open Loyalty: Symfony-stack technology, scheduled transaction import cookbook, ACL/analytics/audit API taxonomy
- Antavo: Promotion Engine / Optimizer (AI insights) / Planner / Clubs / Product Hub as separate platform surfaces; workflow trigger-action-modifier machinery; content approvals; extensive connector catalog
- Stamp Me: StampPod/StampTag/OneStamps validation hardware, Apple/Google Wallet pass integration, multi-banner networks, private label

## Evidence → Assertion Calibration

- All five sampled products directly evidence: program container, enrolled members with balances, behavior-driven accrual, configured redemption (layer B cross-product).
- Tiers: 3/5 sampled products — written as common, never definitional.
- Pending-points posture: 1 product (Antavo) — written as one observed posture; the retroactive-adjustment posture (Square) is the second; presented as two documented approaches.
- Expiry: 2/5 directly documented (Square deadlines, Antavo module) — presented as common program policy with confidence, since it is structurally implied by any points economy; numeric windows never asserted.
- "Points are not money": the sample consistently redeems via configured options rather than tender drawdown — presented as the typical spend grammar, with the store-credit cashback seam explicitly noted as the meeting point (Rise "skip the points — real currency" positioning recorded by the sibling pass).

## Rejected Findings

- "Loyalty = marketing campaigns" — rejected; the Type is an always-on program of record; campaigns are temporary layers on earn/redemption.
- "Points are the defining currency" — rejected; stamps (Stamp Me) and visit counts (Square) are equally valid earn units; the abstraction is *earned program value*.
- "Member tiers are definitional" — rejected; two of five sampled products run programs without member tiers; Square's "reward tiers" are redemption options, not member status — a naming trap this pass had to disentangle.
- "Loyalty points function as tender" — rejected for the canonical model; redemption is via configured options in all sampled products; store-credit-like cashback is the documented meeting seam, not the norm.
- "Referral machinery is part of loyalty" — rejected to L2/boundary; shared platforms and currencies, but different reward attachment.
- "Coalition/multi-brand is the Type" — rejected to L2 (Stamp Me evidence only in sample).
- "Paid membership (Amazon-Prime-style) is loyalty" — rejected; different provenance (dues vs behavior); boundary noted.

## Boundary Findings

| Nearby Type | Seam | Removal test |
|---|---|---|
| Gift Card Management (§05.15, processed) | Provenance of value: loyalty value is *earned through recorded behavior under accrual rules*; gift card value is *purchased by a giver under a merchant program*. They meet where loyalty rewards are paid out as gift cards. | Remove earning/accrual and the member-earned balance from a loyalty product and what remains may be a gift card program; remove purchased-instrument issuance/redemption drawdown from gift card management and no loyalty program remains. |
| Store Credit / Stored Value Platform (§05.15, processed) | Provenance + spend grammar: loyalty value is behavior-earned and redeemed via *configured benefit options* (catalog/tiers/vouchers); store credit is issued/owed/deposited currency value spent *as tender*. Meeting point: cashback-style rewards paid as credit (sibling pass documented Rise's "skip the points — real currency" positioning; Square ships Loyalty and Gift Cards as separate APIs — directly re-confirmed in this pass's Square docs nav). | Make credit earned-by-behavior and bound to configured redemption options → points; let points spend as raw tender → credit. |
| Referral Marketing Platform (§06, processed) | What the reward attaches to: loyalty rewards the customer's *own repeat behavior*; referral rewards the *arrival/conversion of other people*. Shared currencies (points/credit) and shared vendors (Friendbuy, ReferralCandy loyalty campaigns per sibling; Smile referral resource; Antavo friend-referral module observed here) make product-based separation impossible — the attachment test must be used. | Remove the referred-other-person attribution and reward from a referral platform → its reward machinery collapses into loyalty/advocacy territory; add referred-person attribution to loyalty → referral. |
| Customer Advocacy Platform (§06, processed) | Advocacy rewards/badges are common-mature recognition inside a reviews/UGC/references motion; loyalty's managed object is the earned-value economy. | Remove points economy from an advocacy platform and it still runs asks/participation. |
| Promotion Management (§06, processed) | Promotions change transaction price for eligible anonymous/segmented populations; loyalty runs an always-on member program whose redemption *produces* discounts. Member-targeted offers are a promotion capability without owning the program. (Antavo ships Promotion Engine as a separate surface; promotion-management pass recorded the mirrored seam.) | Remove earn rules and balances → promotion tooling; remove price-change machinery from loyalty and it still runs the program. |
| CRM (§07) | CRM holds customer relationships and interaction history; loyalty adds the program rules engine and the earned-value ledger. Loyalty reads/writes CRM records (Square loyalty account ↔ customer profile; Antavo uniform customer profile). | Remove balances/accrual → CRM. |
| Membership Management / Member Benefits (§25) | Membership value derives from dues/paid access and standing; loyalty value derives from behavior. Paid-membership loyalty variants sit on the seam. | Value enters by payment of dues → membership; by qualifying behavior → loyalty. |
| Retail POS / E-commerce Platform / Checkout | Redemption and identification happen inside those surfaces; loyalty owns program, rules, balances, ledger. Packaging is embedded (Square inside Square POS; Smile as a commerce-platform app) or standalone (Antavo, Open Loyalty). | Remove the program/ledger and the store still sells; remove checkout/POS and loyalty still manages the program. |
| Fan Engagement Platform (§26, processed) / vertical suites | Loyalty points there are one component beside tickets/content/campaigns; remove everything but the points ledger → this Type (fan-engagement pass recorded the mirrored seam). | Points economy as the whole model → loyalty. |
| Affiliate Management / Networks (§06) | Participants are external partners earning commissions; loyalty participants are the brand's own customers earning program value. | Different participant population and incentive semantics. |
| Rewards & Incentive Distribution (Tango-class) | Distributes third-party rewards catalogs; owns no member balances or accrual rules. | Owns no member economy → distribution platform. |

**Joint-review discharges (from this side):**
- vs gift-card-management: keep-both RATIFIED. Provenance seam confirmed; Square's separate Loyalty vs Gift Cards APIs directly observed; loyalty-suite gift-card bundling (Paytronix/Givex-class) remains unobserved (sites unreachable across all three passes) — held as packaging variant.
- vs store-credit-stored-value-platform: keep-both RATIFIED with the two-part seam (provenance + spend grammar) confirmed from the loyalty side.
- vs referral-marketing-platform: joint review RESOLVED — keep-both; the seam is the reward attachment (own behavior vs another person's qualifying action), not the currency; straddle products (Friendbuy-class) run both motions on shared infrastructure.

## Historical / Market-Sample Check

Pre-digital loyalty satisfies the core: the paper stamp book (stamps earned per purchase under the issuing program's rules, held by the customer as their "balance", redeemed against a catalog/counter reward) and the café punch card ("buy 10 get 1" — the card is the member account, punches are accrual, the free item is redemption) contain all four L0 structures with no software, no cloud, no apps, no tiers, no marketing automation. Conversely, a dues-paid club with fixed benefits fails leg 3 (no behavior-earned accrual) — correctly excluded as membership, not loyalty. The L0 passes the historical check; nothing cloud/app/AI-specific is definitional.

## Uncertainties

1. Smile's points-settings and expiry mechanics were observed only at index level (object names, not semantics); no expiry claim is attributed specifically to Smile.
2. Open Loyalty's reward-campaign redemption mechanics (assignment, activity windows) are documented at user-guide level; deeper state machinery not fetched. Claims kept at index level.
3. Enterprise loyalty-suite bundling of gift cards (Paytronix/Givex-class) remains structurally inferred — unreachable across this pass and both sibling passes. Recorded once more for the record; do not assert bundling as market fact.
4. Status-only (points-free) tier programs and coalition programs in the wider market (travel/hospitality) are known instances but were not directly sampled; the airline frequent-flyer pattern is cited in the final document only as a generic large-scale instance, without product specifics.
5. Antavo's wallet module (in-store) was observed at index level only; no wallet-mechanics claims made.
6. Tax/legal treatment of points (liability accounting, escheatment, financial recognition of breakage) was not observed in any sampled product's docs; deliberately absent from the final document.

## Final Synthesis

Loyalty Program Management is the brand-side system of record for operating a customer loyalty program. Its defining core is small and jointly held: a configured program (earn rules + redemption options + policy) over an enrolled member population, where recorded qualifying behavior accrues earned value into member balances under the program's rules, and that value redeems through configured benefit options. Everything else commonly associated — member tiers, birthday bonuses, gamification, referral modules, fraud engines, marketing-automation integrations, mobile apps and wallet passes — is standard or optional structure layered on that core. The paper stamp book satisfies the same core, which is the historical check that the core is not an artifact of modern SaaS. The Type's boundaries are held by provenance of value (earned vs purchased vs owed), spend grammar (configured benefit redemption vs tender), reward attachment (own behavior vs referred others), and program ownership (brand-side ledger vs transaction-scoped promotion or distribution platform).
