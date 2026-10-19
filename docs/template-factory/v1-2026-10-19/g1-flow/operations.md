# G1 formal flow operation log

Scope: observations and formal API actions for G1 only. No application/template/DB mutation outside formal services. The campaign remains `atlas-v1-first-production-2026-10-19`; the fixed G1 plan is `plan_87059846caf345d2b2fe690657cf324f`.

## Observation 1

- Campaign calls: 24 / 500; active jobs: 1.
- G1 epoch/deadline preserved: start `1792389754.633465`, deadline `1792418554.633465`; remaining at observation ~24,517 seconds.
- Business repair allowance used: 1.
- `job_d59605a1fbac430e84966ff143871068` (`case-research`): completed, attempt 5, stage `case-committed`.
- `job_d0d9d80dc9f64dd9890fc0b728bd9a5d` (`blueprint-production`): running, attempt 4, stage `blueprint-code-1-2`.
- Frozen artifacts/reviews: none.
- Source: `BatchService.report(plan_87059846caf345d2b2fe690657cf324f)` through local formal store, read only.

## Observation 2 — provider failure

- Formal report: `needs_attention`; queue counts 1 completed / 2; no frozen artifacts.
- Producer `job_d0d9d80dc9f64dd9890fc0b728bd9a5d`: failed, attempt 4, stage `blueprint-code-1-5`.
- Exact service error: `OpenCode CLI failed: {'type': 'provider.invalid-output', 'message': 'OpenAI Chat stream ended without finish_reason', 'status': 200}; {'type': 'provider.invalid-output', 'message': 'OpenAI Chat stream ended without finish_reason', 'status': 200}`.
- Budget at failure: 27 / 500 calls; active 0; business repairs 1; original G1 deadline retained (`1792418554.633465`, ~23,973 seconds remaining).
- Raw formal attempt evidence directory: `application-atlas-production-pack/atlas/template-factory/jobs/job_d0d9d80dc9f64dd9890fc0b728bd9a5d/attempt-4/blueprint-code-1-5/`.
- `input.json`: 1,510 bytes, SHA-256 `85561973a647deaad5ec334550418510bbe60a5eea0808a0ed236bf50dc6b86`.
- `cli-summary.json`: 7,711 bytes, SHA-256 `1cd4160e2eed3e5c13f724ab2ed489443f0eaeb8151864d0a404ebae5e01b99a`, exit code 1; requested model `opencode-go/deepseek-v4.1-flash`, observed model unavailable.
- `events.jsonl`: 511,639 bytes, SHA-256 `b4327a667779a4850d97073f003c6899160bf7a63a34abcaaaadb4a8ad7c8569`.
- `stdout.log`: 510,307 bytes, SHA-256 `5ce69cc725f305419b342bc8a96fa90b4b003803424908c3962960f49f697a4b`; `stderr.log` empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- Formal process record reports finished at epoch `1792394531.8473039`.
- No retry or repair dispatched; awaiting root's bounded-response decision.

## Retry decision — same failed producer

- Root requested a ledger check before retry. Read-only formal ledger records for the producer showed one failed initial reservation for stage `blueprint-code-1-5:902ee7526228d930` (`retry` null; outcome `cli_failed`) and no retry reservation for that exact stage. The campaign limit is two transient retries per stage. Earlier unrelated stage retries do not consume this stage's allowance.
- Dispatched the existing formal API route `POST /api/factory/jobs/job_d0d9d80dc9f64dd9890fc0b728bd9a5d/retry` using `template_factory.api.dispatch`; status 202. The same job is queued as attempt 5 at `blueprint-code-1-5`; no new job, plan, model, or deadline was created.
- The formal dispatch started/recovered the worker. No template/application contents or DB rows were edited directly.

## Observation 3 — frozen candidate and review queued

- Producer job `job_d0d9d80dc9f64dd9890fc0b728bd9a5d` completed at attempt 5 after the same-job retry.
- A frozen draft candidate exists: artifact `tpl_7f4c17e834c342e7b462e6bb8b6379e4`, digest `8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9`.
- Formal `cognitive-review` job `job_8c13691fd4ac4591a83308c02cd4e267` is running, attempt 1. Review status currently `unavailable` while review is in progress; no publication or downstream development has been dispatched.
- Queue has 2/3 completed (research, producer) and one active review. Campaign calls 32/500; business repairs remain 1; original G1 deadline retained (~23,223s remaining).

## Retry decision — cognitive review provider failure

- Formal reservation for review job `job_8c13691fd4ac4591a83308c02cd4e267` showed one failed initial reservation at stage `cognitive-review:85f6308386aca162` (`retry` null, outcome `cli_failed`) and no retry reservation for that stage. The campaign cap permits two retries per stage.
- Dispatched formal `POST /api/factory/jobs/job_8c13691fd4ac4591a83308c02cd4e267/retry` via `template_factory.api.dispatch`; status 202. The same review job is queued at attempt 2/stage `acceptance`; it still refers to the same frozen artifact/digest `tpl_7f4c17e834c342e7b462e6bb8b6379e4` / `8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9` and same configured model.
- No replacement artifact, job, or review decision was created. Official worker dispatch used elevated execution per root's runtime guidance.

## Cognitive review retry 1 — same provider failure

- Formal review returned to `needs_review` at attempt 2 with the same `provider.invalid-output` / missing `finish_reason` error.
- Ledger now shows two failed reservations for `cognitive-review:85f6308386aca162`: initial (`retry` null) and first retry (`retry` 1). The configured cap is 2 retries per stage, so exactly one remained.
- Attempt-2 raw evidence directory: `application-atlas-production-pack/atlas/template-factory/jobs/job_8c13691fd4ac4591a83308c02cd4e267/attempt-2/cognitive-review/`.
- `cli-summary.json`: 7,004 bytes, SHA-256 `9c518ea1cfceed0c76523d4b7d8d83cae150190998efd08b1787673fb470f231`; exit 1; requested model `opencode-go/deepseek-v4.1-flash`.
- `events.jsonl`: 726,353 bytes, SHA-256 `a22d620988ea75d4c4eb8e9fd59dbabd1145a7870aff62b4ada25160ffefc840`.
- `stdout.log`: 724,365 bytes, SHA-256 `3f211ff1b4e631d45bf83a0ee735f6bf22b372baba9a4755d320de203c7504eb`; stderr empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- Formal same-job retry call returned 202. Review job `job_8c13691fd4ac4591a83308c02cd4e267` is queued at attempt 3/stage `acceptance`; artifact and digest unchanged.

## Cognitive review retry 2 — substantive uncertain finding

- Attempt 3 completed the provider call (CLI exit code 0) but formal review is `needs_review`; artifact review status is `uncertain`, not passed. No publication was dispatched.
- Review result summary: the only substantive uncertain item is `architecture_contract`. The reviewer says `invalid_url` does not explicitly state the dot-containing hostname requirement exercised by A02, and the generic error contract omits `bad_request` exercised by A10. Other dimensions in the result are marked passed. The review states it did not execute programs or tests.
- Result `attempt-3/cognitive-review/result.json`: 9,051 bytes, SHA-256 `9059553cf1116c58fe4be7b30f36b058817501c7c5e859bcd079f3e3498b9a58`.
- `cli-summary.json`: 10,159 bytes, SHA-256 `bb5aaab11a24fbf0c78031267b2b7be2b59d7b45e113341131e2d167528d6f50`, exit code 0, requested model `opencode-go/deepseek-v4.1-flash`.
- `events.jsonl`: 720,233 bytes, SHA-256 `9acff284a812fd0a8e8637ed41a08f4adac90c087043a2e09c0f8330208a2eaf`.
- `stdout.log`: 718,047 bytes, SHA-256 `f1e1e5f1a8995df107e03a24551b44c15f80ccd7e7ef42e3b328e51c69f8d3b3`; stderr empty.
- Both configured transient retries for this exact review stage are now consumed. No further provider retry is available within the current cap; no business repair or publication was dispatched.

## G1 paused for bounded business repair decision

- Root directed a pause while the formal retry-scope fix and CI gate work proceed. Called `POST /api/factory/v1/plans/plan_87059846caf345d2b2fe690657cf324f/pause` through `template_factory.api.dispatch`; HTTP 200 and batch state `paused`. Research and producer jobs remain completed; cognitive-review job remains `needs_review` at attempt 3. No checkpoints were deleted.
- Post-pause formal report: campaign budget `active=0`; no queue jobs are running. Worker lock file contained stale PID `86451`; elevated `ps -p 86451` returned no process. All relevant cognitive-review `process.json` markers have `pid: null` and finished timestamps. No terminate signal was sent; the detached worker had already exited.
- Repair API inspection: product-blueprint repair routes to `cognition.queue_repair`; requires `expected_digest` and `note`. `reuse_spec=true` reuses the frozen structured spec, including `architecture_markdown`; `edit_paths` can only include existing `acceptance/` and `references/` paths and explicitly excludes `acceptance/plan.json`. Thus the API cannot reuse spec and edit only documentation paths.
- A documentation contract revision therefore requires `reuse_spec=false` and omitted `edit_paths`; its model prompt should request exactly these prose updates, preserving every acceptance/test assertion: (1) ARCHITECTURE.md `invalid_url` rejects hosts without a dot, per existing A02; (2) malformed JSON uses `bad_request`, per existing A10; (3) remove D04's reference to undefined `purge`, retaining `/restore`. This is not host-enforced file scope and requires fresh independent review. No repair/review dispatched pending root's code/ledger fix.

## Scoped second business repair queued and G1 resumed

- Read `docs/template-factory/v1-2026-10-19/g1-repair-request.json` verbatim. It binds expected digest `8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9`, requests `opencode-go/deepseek-v4.1-flash`, and authorizes exactly `architecture_markdown` plus `decisions.D04.impact`; it explicitly preserves all acceptance rows/IDs and program files.
- Dispatched `POST /api/factory/artifacts/tpl_7f4c17e834c342e7b462e6bb8b6379e4/repair` through `template_factory.api.dispatch` while parent G1 was paused and `ATLAS_FACTORY_DISABLE_WORKER=1`. Returned HTTP 202 with paused repair batch `bat_0f7816b7b2f54fcbb7f8c1b8ab761568`; queued job `job_4f30d0f41ce94a2cbd16ae7996fb27ab`, kind `blueprint-production`, attempt 1. This is the same body/idempotent repair request and same frozen baseline digest.
- Before resume, formal report showed repair ledger `repairs_used=2`, budget active 0, 34 calls/500, and unchanged G1 deadline `1792418554.633465` (about 21,324 seconds remaining).
- Resumed the existing plan through `POST /api/factory/v1/plans/plan_87059846caf345d2b2fe690657cf324f/resume`; HTTP 200. Elevated formal dispatch started the latest worker. Follow-up report shows the queued repair job running at stage `case-adaptation`, attempt 1; calls 35/500, active 1, repairs remain 2, deadline unchanged (~21,303 seconds remaining).
- G1 is not assessed/passed; no publication, P0 development, runtime, T08, or independent proof was dispatched.

## Spec-only business repair stopped at repair cap

- The scoped spec patch completed, but the formal producer's first structural/design review reports `product_completeness: blocked` and `architecture_contract: blocked` (other listed dimensions passed). The production loop attempted its next spec-repair index; persistent ledger rejected it before another CLI call with `budget_repair_limit: product repair limit exhausted`.
- Repair job `job_4f30d0f41ce94a2cbd16ae7996fb27ab` is `paused_budget`, attempt 1, stage `blueprint-spec-review-0-runtime_protocol-v1`; campaign total 42/500, active 0, repairs used 2, deadline `1792418554.633465` unchanged (~20,193 seconds remaining).
- No revised frozen artifact exists. Original artifact `tpl_7f4c17e834c342e7b462e6bb8b6379e4`, digest `8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9`, remains draft/uncertain. No further retry, repair, publication, development, runtime, or T08 call was made.
- `attempt-1/context/SPEC_REVISION_0.json`: 1,959 bytes, SHA-256 `3cd7bb50589e3e27e85c94ee94b6c89f36663ee17887731e25f0d48f857a20f8`.
- `attempt-1/blueprint-spec-review-0/report.json`: 21,337 bytes, SHA-256 `4d4aee241c25b80fe8b0f300007a521e2efdab328c9b8239a37fe2d4358d6141`.
- Product-completeness report: 2,217 bytes, SHA-256 `faeb9f4ecdc14a44d275be9525c21897935857acfc3fd01907fefa26bf6e4127`. Architecture-contract report: 2,502 bytes, SHA-256 `7c54b75b15b5258620b78189c01fba3b80d7488b0e4f68bf5299fd96abc1b074`.

## G1 terminal status

- Official final action: `POST /api/factory/v1/plans/plan_87059846caf345d2b2fe690657cf324f/pause`, dispatched through `template_factory.api.dispatch`, returned HTTP 200 / `paused`. This freezes G1 and its child batches through the formal service; the terminal `paused_budget` job and every checkpoint remain intact.
- Final authoritative `BatchService.report` state: plan `paused`; campaign `atlas-v1-first-production-2026-10-19`; CLI sessions 42/500; active 0; business repairs 2/2; transient retry maximum 2 per stable product review scope and current cognitive review scope used 2/2; original start `1792389754.633465`, original deadline `1792418554.633465` (about 20,115 seconds remained at final report). No limit or clock was reset.
- Case research `job_d59605a1fbac430e84966ff143871068`: completed, attempt 5, `case-committed`.
- Initial producer `job_d0d9d80dc9f64dd9890fc0b728bd9a5d`: completed at attempt 5 after one formal same-job retry. Its attempt-4 `blueprint-code-1-5` failed twice with provider `invalid-output` / stream ended without `finish_reason`; evidence and hashes are in Observation 2 above.
- First frozen candidate `tpl_7f4c17e834c342e7b462e6bb8b6379e4`, digest `8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9`: current cognitive review remains `uncertain`, never passed. Review job `job_8c13691fd4ac4591a83308c02cd4e267` attempt 1 and attempt 2 failed on provider `finish_reason` protocol; two formal retries exhausted its stable cognitive-review scope. Attempt 3 completed and found substantive `architecture_contract` uncertainty: `invalid_url` did not specify A02's dotted-host requirement and generic error contract omitted A10's `bad_request`. Result and raw evidence hashes are in the retry evidence above.
- Second and final business repair job `job_4f30d0f41ce94a2cbd16ae7996fb27ab`: formal spec-only edit paths were `architecture_markdown` and `decisions.D04.impact`; existing acceptance/reference programs were set to reuse byte-for-byte. The exact request is `docs/template-factory/v1-2026-10-19/g1-repair-request.json` (SHA-256 `456a71a85ae3b0e59f1ac763ff2ab520f05ffbc1ef081ee7a3d0456c5174debd`). The generated scoped spec revision is preserved at `application-atlas-production-pack/atlas/template-factory/jobs/job_4f30d0f41ce94a2cbd16ae7996fb27ab/attempt-1/context/SPEC_REVISION_0.json` (SHA-256 `3cd7bb50589e3e27e85c94ee94b6c89f36663ee17887731e25f0d48f857a20f8`). Host design review still marked `product_completeness` and `architecture_contract` blocked; reports and hashes are recorded above. A further internal spec-repair attempt was stopped by the persistent budget with exact error `budget_repair_limit: product repair limit exhausted`; no third business repair or further model call occurred. The job is preserved as `paused_budget`, attempt 1, stage `blueprint-spec-review-0-runtime_protocol-v1`.
- The only artifact remains draft/uncertain; nothing was published or developed. G1 formal assessment: not passed. Independent runtime/P0 proof: `not_run`. T08: `not_started` because its prerequisite G1 has not passed.

### Remaining gates and next decision

- Current repository verification entrypoint documented for a complete local run: `PYTHONPATH=application-atlas-production-pack python3 -m template_factory.v1_checks --output docs/template-factory/v1-2026-10-19/verification/final`. A strict complete run was separately reported by root as passed after the latest source changes, but it does not cure this campaign's blocked review or grant G1.
- If a new business attempt is desired, it requires an explicit new scope/plan decision; do not create another campaign automatically. The persisted product repair cap is exhausted for this campaign.
- Only after a current artifact has a passed cognitive review may it be published via digest-bound `artifact_action`. Then the official P0 path is `POST /api/factory/artifacts/{artifact_id}/develop` with the formal development request, followed by `GET /api/factory/jobs/{job_id}/delivery` and `POST /api/factory/jobs/{job_id}/verify-delivery` with the exact archive SHA-256. Actual runtime is submitted only through the formal acceptance/runtime queue, after the independent executor handoff and only when root releases the runtime slot.
- G1 can be assessed only after all required evidence is present using host `BatchService.assess_g1(plan_id, manifest_path)`; this is an evidence assessment, not a way to set pass manually. T08 preview/run remains prohibited until that formal G1 assessment passes.
