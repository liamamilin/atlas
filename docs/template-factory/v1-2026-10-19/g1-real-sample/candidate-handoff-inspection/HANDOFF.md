# Current handoff / 当前开发交接 · P0

Read `KNOWLEDGE.md` for the full planning index and `CURRENT_PHASE.json` for the selected phase packet. The full confirmed scenario, selected and prerequisite capabilities, and all case goals are retained. Prerequisite phases require verification; export makes no completion claim.

Resolve decision triggers from `PROJECT_DECISIONS.json`; defaults are proposed, and every choice starts unconfirmed. Compare this phase with the full scenario and report any scope gap instead of silently changing frozen commitments.

Load architecture contracts from `blueprint/ARCHITECTURE.md`, product rationale from `blueprint/PRODUCT.md`, reuse and licensing notes from `blueprint/CATEGORY.md`, test guidance from `blueprint/acceptance/README.md`, and the strict application delivery protocol from `APP_DELIVERY.md`.

Use `ACCEPTANCE_CONTRACT.json` as an independent inventory. Its status is `not_run`; it declares no commands and export runs no acceptance or application code. Before reporting completion, include actual application start commands and the executed test commands with passed, failed and not-run statuses. Exit code zero alone does not prove user behavior passed. Fix the application when frozen assertions fail; do not weaken or rewrite frozen tests.
