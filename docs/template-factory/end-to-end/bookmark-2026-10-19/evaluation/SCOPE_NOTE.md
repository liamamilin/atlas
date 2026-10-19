# Acceptance scope calibration

This note supplements the frozen acceptance plan without changing `PLAN.md` or `freeze.json`. The original scenario remains the authority for product scope.

The P0 core workflow is derived from scenario revision 2: save and retain URLs, organize them in categories, move records, browse or search for them, and open the original page. The validation, HTML output safety, and unsafe URL checks in the plan are applicable safety and data-integrity negative cases; they do not add unrelated product features.

Repeated submission is a risk-exploration check, not an unconditional product requirement. During acceptance, observe and report whether repeating a save or category-create action produces a duplicate. Treat duplication as a contract failure only if the newly generated template explicitly promises idempotency or uniqueness for that operation (including a unique-URL rule). Otherwise record the observed behavior as a finding, without failing acceptance solely for duplication. Do not infer such a promise from this note or from the scenario itself.

This calibration does not remove the duplicate-effect observation from the frozen plan and does not alter any frozen file or its hash. Before execution, inspect the newly produced template contract to determine whether it explicitly defines uniqueness or idempotency.
