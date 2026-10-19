"""One observed-failure product repair; initial artifacts remain immutable."""

import argparse
import json
from prepare import HERE, hashes, save
from develop import run_cell


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case", required=True, choices=["budget", "booking", "rename"]
    )
    parser.add_argument("--label", required=True, choices=["M1", "M2", "M3"])
    parser.add_argument("--feedback", required=True)
    args = parser.parse_args()
    cell = HERE / "runs" / args.case / args.label / "initial"
    receipt = json.loads((cell / "delivery.json").read_text())
    assert receipt["status"] in ["delivered", "delivered_with_source_findings"]
    app = cell / "application"
    assert hashes(app) == receipt["source_sha256"]
    path = (HERE / args.feedback).resolve()
    assert path.is_relative_to(HERE / "feedback")
    feedback = json.loads(path.read_text())
    assert feedback["kind"] == "observed_runtime_failure"
    repair = HERE / "runs" / args.case / args.label / "repair"
    repair.mkdir(exist_ok=True)
    decision = repair / "repair-decision.json"
    if not decision.exists():
        save(
            decision,
            {
                "initial_source_sha256": hashes(app),
                "feedback": feedback,
                "policy": "One optional product repair after actual material failure, no app hand edits; original core criteria and initial evidence unchanged, exploratory probes identified separately",
                "stdin_boundary": "Author driver DEVNULL; original budget common launcher script removed (repair-round control change)"
                if args.case == "budget"
                else "DEVNULL in both initial and repair rounds",
            },
        )
    run_cell(args.case, args.label, repair_source=app, feedback=feedback)
    assert hashes(app) == receipt["source_sha256"]


if __name__ == "__main__":
    main()
