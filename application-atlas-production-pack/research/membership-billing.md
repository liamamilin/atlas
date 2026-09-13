# Research Notes — Membership Billing

Research date: 2026-09-08
Slug: `membership-billing` · Directory leaf: Membership Billing (§25 Nonprofit, Membership & Religious Organizations)

## Research Goal

Understand what a **Membership Billing** application is as an Application Type: what objects exist inside it, what the recurring money loop looks like, who operates it, how billing state connects to membership standing, and where its boundaries sit against Billing Platform, Subscription Billing Platform, Association Management System (AMS), Membership Management System, Member Portal, Fitness Membership Management, Church Giving Platform, and Renewal Management Platform — all adjacent leaves already documented in this Atlas or scheduled as siblings.

## Initial Boundary (pre-research hypothesis)

- Core use: recurring collection of membership dues from a member base by a membership organization or member-based service business.
- Likely nearest neighbors: Billing Platform (generic what-customers-owe systems), Subscription Billing Platform (commercial recurring charges), AMS / Membership Management System (member registries that also settle dues), Member Portal (member-facing self-service), Fitness Membership Management (fitness-family sibling), Church Giving Platform (voluntary vs obligatory money).
- Open questions at start: Is this leaf an alias of Subscription Billing Platform? Is it just the dues module of AMS? Does the market have *dedicated* membership-billing products (vs suites)? What is the load-bearing structure none of the neighbors carry?

## Research Questions

1. What is the billed subject — the member? an account? a family/company unit?
2. What generates a charge — how do plans/levels/dues rules become money claims (invoices/charges), and on what schedule (cycle runs vs anniversary/renewal dates)?
3. How is money collected — stored-card/EFT auto-charge, member self-pay, manual payment recording? What happens on failure (retries, dunning, outsourced recovery)?
4. How does billing state couple back to membership standing (good standing, overdue, suspended, lapsed, dropped, reinstatement)?
5. What lifecycle adjustments exist — plan switch, proration, pauses, price changes, installment/payment plans, early-renewal discounts, optional dues items?
6. What money records exist (invoices, payments, refunds, credits) and how is revenue handed to accounting?
7. What operator surfaces and roles does the billing work require?
8. Is there a product population whose *center of gravity* is billing itself (not the registry, not classes/events) — justifying a distinct Type?

## Representative Products

Selected for market representativeness, documentation depth, different product philosophy, and different customer levels:

| Product | Segment / pole | Philosophy | Evidence depth reached |
|---|---|---|---|
| **Wild Apricot** (Personify) | small associations, nonprofits, chambers, clubs, alumni | self-serve all-in-one membership admin for small orgs | Tier-2 product pages (rendered) + Tier-1 help article inventory (sitemap); article bodies JS-gated |
| **PushPress** | boutique gyms/studios/affiliates | modern software-first, Stripe-backed, member app | Tier-1 help center incl. "Payments — Complete Guide" |
| **ABC Fitness** | large gyms/health clubs, franchises, 24/7 | managed full-service billing processor (registered MSP/ISO) + club platforms | Tier-2 marketing/product pages; help portal login-gated |
| **Daxko** | nonprofit community centers (YMCA/JCC/BGC) + mid-market clubs | software + outsourced payments & revenue-recovery services (registered ISO) | Tier-2 capability/service pages |
| **Novi AMS** | associations run on QuickBooks | dues-rule engine + native accounting integration | Tier-2 product page + Tier-1 knowledge-base inventories (Dues Rules & Invoice Management; Renewals) |

Rejected as samples: Zen Planner (already the designated membership-billing pole of the fitness-studio pass), iMIS (imis.com 403; docs.imis.com unreachable ×1), Mindbody (wellness marketplace family), church giving platforms (different Type, already documented).

## Sources

- Wild Apricot — Payments feature page: https://www.wildapricot.com/features/online-payment-processing (rendered, 2026-09-08)
- Wild Apricot — Member Management feature page: https://www.wildapricot.com/features/membership-management-software (rendered, 2026-09-08)
- Wild Apricot — Help Center article inventory via sitemap: https://gethelp.wildapricot.com/en/sitemap.xml (titles only; bodies JS-gated — see Limitations)
- PushPress — Core product page: https://www.pushpress.com/core ; Help Center: https://help.pushpress.com/ ; Payments Complete Guide: https://help.pushpress.com/en/articles/2781161-core-payments-complete-guide ; Payments/Member Management/Core collections (2026-09-08)
- ABC Fitness — corporate site: https://www.abcfitness.com/ (2026-09-08)
- Daxko — corporate site: https://www.daxko.com/ ; Payments capability: https://www.daxko.com/capabilities/payments ; Revenue Recovery Services: https://www.daxko.com/services/full-service-billing (2026-09-08)
- Novi AMS — site: https://www.noviams.com/membership-management ; KB root: https://help.noviams.com/ ; Member Types, Dues and Renewals collection: https://help.noviams.com/collections/8779507409-member-types-dues-and-renewals ; Dues Rules & Invoice Management collection: https://help.noviams.com/collections/3785284782-dues-rules-invoice-management (2026-09-08)

**Source-access limitations (recorded per evidence rules):**
- help.wildapricot.org transport-failed ×1; article bodies on gethelp.wildapricot.com render title-only (JS-gated) ×2 — article *titles/inventory* retained as direct documentation evidence; body-level precision deliberately NOT asserted.
- imis.com 403 ×1; docs.imis.com transport error ×1 — iMIS abandoned; association-enterprise pole covered by Wild Apricot + Novi instead.
- ABC Fitness support portal and Daxko help center are login-gated; ABC/Daxko evidence is marketing-page level → all claims from those two stay coarse.
- No precise numeric parameters (retry counts, fee percentages, timing windows) from any vendor are carried into the final document.

## Product Observations

### Wild Apricot (A = directly observed on rendered pages / article inventory)

- Automatic renewal payments enabled per membership level; automatic invoice and receipt generation and emailing; payment records created in the member database against the contact (A, payments page).
- Card changes supported; automated emails for upcoming card expiration "to keep members in good standing" — explicit billing→standing vocabulary (A).
- Trigger actions on payment events: activate memberships, send welcome emails, receipts (A).
- Record physical payments; track unpaid invoices; follow up from one dashboard; reports incl. income by source and outstanding debts (aging) (A).
- Renewal machinery: renewal policy configuration, renewal notice timelines, limiting self-renewals per level, automatic membership-status updates during the renewal period (A, member management page).
- Member self-service: view/pay outstanding payments, "invoice themselves", mobile admin invoicing (A).
- Help article inventory documents: manual invoices; settling payments to invoices; credits or payments on account; adjusting/canceling a payment; manual payments; payment types; online payment failures; processing card payments on behalf of members; invoices list; payments & refunds list; payment details; payments report; exporting invoices; customizing/emailing invoices; renewal settings; difference between "renewal overdue" and "lapsed"; manually renewing memberships; bulk update renewal dates; member access to invoices and payments; why a lapsed member got charged twice; a lapsed member paid but is still not active; no renew button cases (A, titles).
- Stated audience: associations, chambers, nonprofits, clubs, alumni — organizations that "rely on members, recurring dues" (A, FAQ).

### PushPress

- **Invoice-first machinery**: "Every transaction in PushPress generates an invoice"; the open invoice controls collection — add items (bundle a product into a plan renewal), partial payment, schedule future auto-collection, split across methods, forgive/delete (A, Payments Complete Guide).
- Per-member next-invoice generation ("Create Next Invoice"), change billing date, plan-level calendar alignment ("billing on the 1st" per plan) (A).
- Failed charges surfaced in three places: Dashboard → Failed Billing; Payments → Invoices tab (filter failed); Member profile → Billing tab. Resolution: verify/re-add card, read failure reason, member contacts bank, unlock ACH-locked invoice and retry; "nightly retry for any member with a valid payment method on file" (A — product-specific behavior detail).
- Collection of overdue balances from those same surfaces; plans do not auto-switch to a newly added card (A).
- ACH direct debit (US; international ACSS/SEPA/BECS documented), Stripe connection, deposits reconciliation reports, full/partial refunds, flex-fee pass-through, payment notifications (A).
- Plan/billing lifecycle: plan switch, prorated plans, price-increase rollout (grandfather vs all members), membership pauses and billing adjustments, installment plans via occurrence-limited recurring plans, specialty plans (e.g., annual maintenance fees), hybrid plans, trial plans (A).
- Billing unit extension: sub-accounts "link parents, children, or couples together to share billing information" (A).
- Status machinery: Lead/Member/Non-Member/Ex-Member; alert status; churned members; click-to-cancel compliance articles for membership cancellations (A).

### ABC Fitness

- Positions full-service billing + payment processing for fitness businesses at scale ("40% of clubs in the US" claim; "40 million members"); registered MSP/ISO of named banks — i.e., the vendor itself is the money mover for member billing (A, marketing-level).
- Club member support offered down to gym members — the processor pole handles member-facing billing contact (A, marketing-level).
- Platforms (Ignite etc.) are club management suites around the billing core; regional platform (ABC Evo) with country-specific banking (A, marketing-level).
- **Evidence limitation**: no operational documentation reachable; no workflow detail asserted from ABC beyond the above.

### Daxko

- Payments capability: credit cards, ACH (batch post/settle), gift cards; automated billing; "expert decline recovery"; payment plans; card account updater; SmartDate resubmission ("determines the ideal time to resubmit charges for each member"); next-day funding; tokenization; fraud/AVS (A, marketing-level).
- **Revenue Recovery Services**: an in-house human team resolves declined charges, insufficient funds, late fees, and outdated billing information on the organization's behalf — outsourced execution of the failure/recovery half of the loop ("delegate resolving late fees and updating billing information") (A, service page).
- Serves YMCAs/JCCs/Boys & Girls Clubs — member-based nonprofits — plus mid-market clubs; Club Automation described as "connected billing, scheduling, payments and member engagement" with "member billing, front desk operations, scheduling, access control, POS" (A, marketing-level).
- Registered ISO of Citizens Bank (A).

### Novi AMS

- Join automation chain observed verbatim: signup → added to database → added to QuickBooks → **dues calculated** → **credit card processed or invoice created** → membership approval → confirmation email (A, product page).
- "Customizable Dues & Renewals: We've never met a dues rule that we haven't been able to accommodate" — dues rules as a first-class configured engine; member types company-based / individual / hybrid (A).
- KB inventory "Dues Rules & Invoice Management" documents: setting up / drafting / updating dues rules for the next membership term; connecting dues rules to QuickBooks items; creating manual dues invoices; recalculating open dues invoices; emailing dues invoices; transaction dates & payment terms on dues invoices; optional dues rules & product add-ons for dues invoices; allowing members to remove optional dues items; tips for collecting on & handling open dues invoices; **automatic drop of members (non-renew & credit)**; manual drop; list of dropped members; **unpaid dues and member benefits**; **reinstatement fees**; deep-dive on member expiration dates & outstanding dues invoices; early renewal discount (A, titles).
- Renewals collection (7 articles) + Smart Renewal Notices emails (A, titles).
- QuickBooks Online integration is the accounting substrate; split-ACH-deposit corrections documented (A, titles).

## Cross-product Comparison

| Structure | Wild Apricot | PushPress | ABC Fitness | Daxko | Novi | Layer |
|---|---|---|---|---|---|---|
| Member-level billed account (with payment methods, billing contact) | ✓ (contact + payment records) | ✓ (profile Billing tab) | ✓ (implied) | ✓ (implied) | ✓ (member record + QB linkage) | A |
| Plan/level/dues-rule configuration as source of amounts | ✓ (membership levels + renewal settings) | ✓ (plans) | ✓ (marketing-level) | ✓ (marketing-level) | ✓ (dues rules) | A |
| Generated money claims per member per period (dues invoices/charges) | ✓ (invoices list; automatic invoices) | ✓ (invoice-first) | ✓ (full-service billing) | ✓ (billing) | ✓ (dues invoices) | A |
| Scheduled recurring generation (cycle or renewal-date driven) | ✓ (renewal dates, renewal settings) | ✓ (billing dates, per-plan calendar billing) | ✓ (marketing-level) | ✓ (marketing-level) | ✓ (terms, expiration dates) | A |
| Stored-method auto-charge (card/EFT draft) | ✓ (automatic renewal payments) | ✓ (card + ACH) | ✓ (processor) | ✓ (card/ACH batches) | ✓ (card processed or invoice) | A |
| Manual payment recording (cash/check/offline) | ✓ (manual payments, record physical payments) | ✓ (cash/account charges in staff flows) | — | — | ✓ (manual dues invoices; collecting tips) | A (3/5 deep) |
| Invoice operations: partial pay, credit, void/adjust, refunds | ✓ (credits on account, adjusting/canceling payments) | ✓ (partial, split, forgive, refunds) | — | — | ✓ (recalculate, credit on drop) | A |
| Failure surfacing + retry/recovery | ✓ (online payment failures; overdue tracking) | ✓ (Failed Billing queue; nightly retry*) | ✓ (processor) | ✓ (SmartDate*, account updater, decline recovery) | ✓ (collecting on open dues) | A/B |
| Outsourced human recovery service | — | — | ✓ (full-service) | ✓ (Revenue Recovery Services) | — | A (2/5) |
| Billing→standing coupling (good standing / overdue / lapsed / dropped; benefits gated; reinstatement) | ✓ (good standing, overdue vs lapsed) | ✓ (alert status; expired-card alerts; churned) | ✓ (implied) | ✓ (retain members via recovery) | ✓ (unpaid dues ↔ benefits; drop; reinstatement fee) | B (4/5 deep, 1 implied) |
| Lifecycle adjustments (switch, prorate, pause, price change, discounts, add-ons) | ✓ (level changes while renewal pending; bulk renewal dates) | ✓ (switch, prorate, pause, price rollout, installments) | — | ✓ (payment plans) | ✓ (optional dues items, early-renewal discount, term updates) | A |
| Accounting handoff (export/native GL/reconciliation) | ✓ (export to QuickBooks; income/payments reports) | ✓ (transactions/deposits reports) | ✓ (reporting claim) | ✓ (accounting capability) | ✓ (native QBO) | A |
| Member self-service payment | ✓ (pay/invoice self, member app) | ✓ (member app) | ✓ (member support claim) | ✓ (implied) | ✓ (Member Compass 24/7) | A/B |
| Billing unit beyond individual (family/company) | ✓ (bundled memberships) | ✓ (sub-accounts) | — | — | ✓ (company-based member types) | A (3/5) |

\* product-specific behavior details retained in notes only.

**Population shape:** the market realizes ONE Type in recognizable poles — self-serve software for small membership organizations (Wild Apricot, Novi), software-first platform for studios (PushPress), and managed billing-processor services for clubs at scale (ABC, Daxko). The poles differ in who *executes* billing (org staff vs vendor staff) and how much the surrounding suite carries (registry, classes, access control), not in the billing core itself.

## Canonical Abstraction

### L0 — Defining Invariant

The membership organization's recurring-dues billing system, whose defining core is four jointly-held structures:

1. **The member billing account of record** — each billed member (or billed unit such as a family or company) held as a persistent record carrying its membership plan/level, dues terms (amount, period/cycle), a billing contact, and stored payment methods. Remove → a member registry/CRM with a price list.
2. **The dues/charge generation engine** — the system generates money claims (dues invoices/charges) from those plan/dues terms on a schedule (recurring cycle runs and/or term-renewal dates), including manual creation. Remove → static price list, or ad-hoc one-off payments with nothing recurring.
3. **The payment collection loop** — recorded settlement against those claims: automatic charging of stored payment methods (card/bank draft) and/or manually recorded payments, with the money records maintained per member (payments, refunds, credits). Remove → an invoice archive with no money movement.
4. **The billing→standing coupling** — the member's payment/billing state feeds membership standing and its consequences (good standing vs overdue/suspended/lapsed/dropped; benefit or access gating; re-entry through renewal payment or reinstatement). Remove → generic billing software with member-shaped customers (Billing Platform territory).

Jointly-held is load-bearing: 1 alone = roster with prices; 2 alone = dues calculator; 3 alone = payment processor; 1+2 without 3 = invoicing with no settlement; 1+2+3 without 4 = generic billing; 4 without 1–3 = a status board driven by hand.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Failed-payment machinery: failure surfacing/queues, retries, card-expiration notices, card account updater, decline/dunning communications.
- Invoice operations: partial payments, splits, credits/credit on drop, voids, refunds, invoice emailing/customization/export.
- Member self-service: view invoices, pay dues, update payment method; member-facing payment surfaces.
- Renewal machinery: renewal notices/reminders, renewal policies, self-renewal permissions, early-renewal discounts.
- Lifecycle adjustments: plan switch/upgrade, proration, pauses, price-change rollout, installment/payment plans, optional dues items/add-ons.
- Accounting handoff: GL/accounting export or native integration, reconciliation/deposit reports, aging and revenue reports (income by source, outstanding/aging, renewals).
- Lifecycle communications: dues/receipt/failed-payment notifications.
- Bulk operations: batch invoicing, bulk renewal-date updates, bulk drop.

### L2 — Variant / Optional Structure

- Execution posture: org staff operate billing vs vendor-run managed billing/recovery services (processor pole).
- Payment rails and regionalization: ACH/direct-debit schemes per country, wallets, regional banking, tax/fee pass-through models.
- Billing-unit models: individual, family/household sub-accounts, company-with-seats membership.
- Calendar-aligned cycle billing vs anniversary/renewal-date billing; installment plans; annual/multi-term dues.
- Vertical seasoning: fitness (annual maintenance fees, access gating), associations (term-based dues rules, optional dues items, chapter-level billing — unverified), community centers (program/monthly billing mixes).
- Suite context: billing as a module inside AMS/club suites vs as the product's center of gravity.
- Reinstatement fees, non-renew-with-credit policies, debt-collection handoff.

### L3 — Vendor-specific Detail (research notes only)

- PushPress: nightly retry for valid cards on file; invoice Unlock for ACH-locked invoices; occurrence-limited plans for installments; plans do not auto-switch cards; "billing on the 1st" is per-plan only.
- Daxko: SmartDate resubmission timing; Flex Fees up to 3%; next-day funding claim.
- ABC: MSP/ISO registrations (Wells Fargo / Central Bank of St. Louis); "40% of clubs" claim; ABC Evo country-specific banking.
- Wild Apricot: Personify Payments add-on; article-level specifics unreachable.
- Novi: dues rules bound to QuickBooks items; split-ACH-deposit corrections; Member Health® scoring (engagement, not billing).

## Rejected Findings

- "Membership billing = subscription billing for members": rejected as the L0 — the member-relationship subject and the standing/benefit coupling are carried by all deep samples and absent from generic billing products; recurring-charge machinery alone (the shared part) is the *common substrate*, not the definition.
- "Card-on-file auto-charge is definitional": rejected — the paper dues ledger (notices + recorded payments + delinquency marks) satisfies the core; auto-charge is the dominant modern implementation of the collection loop.
- "Invoices are definitional as 'invoices'": the invariant is the per-member money claim held as a record; fitness processors speak of billing/drafts, associations of dues invoices. Naming varies.
- "Managed recovery services are part of the Type": they are a pole of *who executes* the loop, optional (2/5), not structural.
- Single-source behaviors (nightly retry, SmartDate, Flex-Fee ceiling) not promoted.

## Boundary Findings

| Neighbor | Judgment | "Remove what → becomes the other Type" |
|---|---|---|
| **Billing Platform** (§08, processed) | adjacent; model-neutral "what customers owe" machinery is the shared substrate | Remove the membership subject + dues terms + billing→standing coupling → generic Billing Platform. |
| **Subscription Billing Platform** (§08, unprocessed) | adjacent; machinery overlaps (recurring charges, card on file, dunning, plan changes); seam = billed relationship and fulfillment | The charge is *dues for belonging* to an organization (standing is the fulfillment, gated by payment) vs a commercial subscription to products/services/access. Unprocessed leaf — flag for joint review. |
| **AMS** (§25, processed) | overlapping-leg seam; AMS L0 contains the dues-obligation-and-renewal cycle as one of three legs over a constituent registry | Remove the dues/revenue-loop depth (billing runs, invoices, recovery, accounting handoff) and center the registry/relationship → AMS. Center the revenue loop and thin the registry → Membership Billing. Keep both, center-of-gravity seam (precedent: record-first vs flow-first siblings). |
| **Membership Management System** (§25 sibling, unprocessed) | expected registry-centric sibling | Remove the member-registry breadth → the billing loop alone is this Type. Flag noted for that pass. |
| **Member Portal** (§25, processed) | complementary surface | Remove the operator-side revenue machinery; keep only the member-facing self-service surface → Member Portal. |
| **Fitness Membership Management** (processed) | family sibling with wider objects | Remove check-in/access/class/facility machinery, keep the member+dues+standing loop → Membership Billing; the fitness pass itself names this seam. |
| **Church Giving Platform** (processed) | different money semantics | Dues are an obligation with terms and standing consequences; voluntary gifts have neither → Church Giving Platform. |
| **Renewal Management Platform** (§07, processed) | different object | That pass's own seam: billing is "money execution incl. auto-renewal, no decision object" → the renewal *decision* layer is not this Type. |
| **Collections Automation Platform** (§08, processed) | adjacent recovery machinery | Collections pursues general AR balances; here recovery is over member dues and feeds standing. Dues recovery as a standard capability, not the Type. |
| **Subscription Commerce Platform / Creator Subscription Platform** (processed) | different fulfillment | Goods delivery per cycle / fan-support tiers vs organizational belonging. |

## §24 Historical / Market-Sample Check

Conceptual (no historical source fetched): the paper-era membership secretary's or club billing office's ledger — member ledger cards with dues rates, periodic dues notices/invoices, recorded payments (cash/check), delinquency marks suspending privileges ("not in good standing"), and reinstatement on payment — satisfies all four legs. Early bank-draft/EFT club billing (a decades-old industry practice for health clubs) satisfies it with auto-charge but without portals, card updaters, or suites. The definition therefore names no payment rail, no portal, no cycle convention — only the four jointly-held structures. ✔

## Uncertainties

- Union-dues billing software and chapter/district dues flows (associations) were not directly sourced — held as plausible variants, weakly evidenced.
- Precise boundary behavior of enterprise AMS billing modules (iMIS unreachable) — asserted only from the AMS pass's own L0, not from iMIS.
- Whether Subscription Billing Platform's eventual L0 will absorb part of this Type's machinery — flagged for that pass.
- Wild Apricot body-level mechanics (e.g., how overdue→lapsed transitions are configured) not verified; only their documented existence asserted.

## Final Synthesis

A Membership Billing application is the operator-side system of record for collecting recurring dues from a member base. Its world is: member billing accounts (each carrying plan/dues terms, billing contact, payment methods) → dues/charge generation from those terms (scheduled cycle or renewal-date driven, manual override possible) → payment collection and money records (auto-charge, manual recording, refunds/credits) → billing-state feedback into membership standing (good standing/overdue/lapsed/dropped, benefit gating, reinstatement). Everything else — failure queues, dunning, self-service payment, proration, plan switches, accounting handoff, managed recovery services, vertical seasoning — is standard capability, variant, or vendor detail. The Type holds across small self-serve associations, boutique studios, large club billing processors, and nonprofit community centers, and it holds at ledger-and-notice depth historically.
