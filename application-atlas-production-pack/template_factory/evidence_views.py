"""Reconstruct the fixed R7 review inputs without mutating jobs or calling a model."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import textwrap

from .artifacts import tree_manifest
from .store import FactoryError, digest

JOB_ID = "job_3a658ba085e8417ea6faad5cb0cdd493"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
CAMPAIGN_ID = "atlas-v1-first-production-2026-10-19"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"
BATCH_ID = "bat_6b4fc8bf5b4e42d79bc6a9069277e9f0"
SNAPSHOT_DIGEST = "c4778af6053066cc90b22c1c1320928f7bed4ea9c818bed19cf62c3e986e9239"
PROPOSAL_DIGEST = "e7b9e82beb121a4d73852e556eac0eeefd2406af2cd4a3f8fc6489eea4944f54"
OUTER_NAME = "blueprint-spec-review-0-ad1379367f3e742a-runtime-v1"
OUTER_DIGEST = "c67396039eda05f809ab13afb7ee6783d614ab826550db612268cf7ae78746df"
STAGE_PREFIX = "blueprint-spec-review-0-ad1379367f3e742a"
EVIDENCE_DIGEST = "703fa772f6aa0a6c0571d55738994ee991d178b2687fde0b58295e5810dacd4a"
OLD_PROMPT_SHA256 = "c8ae350e5eb1b66a0f4de936a3d39ca862eab6351758069f8f613d72cac84480"
DEADLINE = 1792495312.855422
PHASE_RESERVATION_ID = "bud_fbec046b65054a33a1c132ad8ed2fd32"
PHASE_SCOPE = "blueprint-spec-review:phase_acceptance"

EXPECTED_REVIEWS = {'blueprint-design-check-0-architecture_contract-ad1379367f3e742a': {'checkpoint_digest': '29f22fbaeabf413b594d286e6a1dd3e75d93239814eebad9e6852eeddc275132', 'projection_digest': '294ac39bebaaed1dfdc12d02278a5081753863cea047fc91a50e01f46ad31919', 'input_sha256': 'e9c835290ce052e620935b55d0a3f8df4f9d40b3b2cd10596973f930ce79f77d'}, 'blueprint-design-check-0-decisions_defaults': {'checkpoint_digest': '38f2d5809bdd654411e6140d1444b726d9723645f5e0b5b48a19ef82956c1323', 'projection_digest': '77977c6734b92f6e472d3079090bde729534560e3a751f0ea4e5bc0c93e5ad2a', 'input_sha256': '796976808c92d79992e9a32737b7b05a93bf717ee0bc0b43a8b681ff5f115e00'}, 'blueprint-design-check-0-phase_acceptance': {'checkpoint_digest': 'dd19d90217dc6cadd7e8346ac4d2af2b1b5a73f4fee2f28aa3ea2f8190ad6d8f', 'projection_digest': '39d09af2c64eae5f81b4f83505383eb05902cf1f794e2612786a04892b7b6b4b', 'input_sha256': 'ef0e7f1ab2963050b046060ac088d43513c871a60b33f1329279a4061a7a3b56'}, 'blueprint-design-check-0-product_completeness': {'checkpoint_digest': '0b54d495af79c6c7c22a871a6281e68eba4f74f67376dae63e44d797eae40e58', 'projection_digest': 'b0255218220f34c9e580b55f20cdbd7e102695113711e838f9d2d51791b2c253', 'input_sha256': '0adc04f25137c746bcb89010cea334fd2894165932aee86d78e56db424a2a660'}, 'blueprint-design-check-0-runtime_protocol': {'checkpoint_digest': 'b97302d6a41d00e7ccfc20cf73683c283dddb8869651fc65e3df2683a8be56fb', 'projection_digest': '353b6d2d5c16c26b040997fc53f4526ea3a3a38d2dd2f45cd8a74c42a0aafc06', 'input_sha256': 'eaf2ea9b0a1d526962d1cdab27f62658b3f1966023084e3de0848f7c6c4dc51f'}, 'blueprint-design-check-0-scenario_scope': {'checkpoint_digest': 'd9131dafeef00ecee093b68f7815d09b32d00a97ef80dcef20e207bde2da2473', 'projection_digest': '35b5375d5af54080f290e7ce9d9745042bf1f573631b2b6a25321bfed2114c27', 'input_sha256': 'd4e0b473d22b5ba84037afa688185a5a4f02069451714a79e056a9a4f44eb03a'}}


def _reject(message):
    raise FactoryError(message, "evidence_recovery_binding", 409)


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def readonly_cli_config_identity(config, directory):
    """Validate exact v2 read-only permissions, normalizing only known workspace transport paths."""
    directory = Path(directory).resolve()
    agent_name = "atlas-factory-" + _sha(str(directory).encode())[:12]
    reads = ["input.json", "leaf.md", "source", "source/**"]
    reads += [str(directory / name) for name in reads[:]]
    rules = [{"action": "*", "resource": "*", "effect": "deny"}]
    rules += [{"action": "read", "resource": name, "effect": "allow"} for name in reads]
    expected = {
        "$schema": "https://opencode.ai/config.json", "permissions": rules,
        "agents": {agent_name: {"mode": "primary", "description": "Atlas read-only factory proposal agent", "permissions": rules}},
        "policies": [{"action": action, "resource": resource, "effect": "deny"} for action, resource in
                     [("tool.use", "shell:*"), ("tool.use", "execute:*"), ("plugin.use", "*"), ("mcp.use", "*"), ("skill.use", "*")]],
    }
    if config != expected:
        _reject("read-only review CLI configuration changed")
    # Every excluded value was first checked against the actual known derivation.
    return {"schema": "atlas.readonly-cli-config-identity.v1", "relative_read_resources": reads[:4],
            "absolute_reads": ["{workspace}/" + name for name in reads[:4]],
            "agent": {"name": "atlas-factory-{workspace_sha256_12}", "mode": "primary",
                      "description": "Atlas read-only factory proposal agent"},
            "default_permission": "deny", "policies": expected["policies"], "cli_major": 2}


def _checkpoint(store, name, expected_digest=None):
    cp = store.checkpoint(JOB_ID, name)
    if (not isinstance(cp, dict) or cp.get("digest") != digest(cp.get("result"))
            or (expected_digest and cp["digest"] != expected_digest)):
        _reject("fixed review checkpoint changed: " + name)
    return cp


def build_evidence_review_materials(store, job_id):
    from .cases import CaseLibrary
    from .cognition import (DESIGN_DIMENSIONS, DESIGN_REVIEW_PROMPT, _design_review_payload,
                            _write_design_projection, _r7_design_program_evidence,
                            _r7_phase_acceptance_prompt, _source_projection_material,
                            research_from_accepted_facts, validate_review)
    from .plan_revision import program_revision_contents
    from .scenario_policy import policy_for
    from .source_references import validate_feature_source_references

    if job_id != JOB_ID:
        _reject("evidence recovery is limited to the original R7 job")
    job = store.job(job_id)
    snapshot = json.loads(json.dumps(job["snapshot"]))
    if digest(snapshot) != SNAPSHOT_DIGEST or job["batch_id"] != BATCH_ID:
        _reject("fixed R7 snapshot or batch changed")
    if _sha(DESIGN_REVIEW_PROMPT.encode()) != OLD_PROMPT_SHA256:
        _reject("the other five reviews no longer share the original prompt")
    plan = _checkpoint(store, "blueprint-plan-0", PROPOSAL_DIGEST)["result"]
    outer = _checkpoint(store, OUTER_NAME, OUTER_DIGEST)
    if outer["result"].get("outcome") != "blocked":
        _reject("original six-review blocked overview changed")
    repair = snapshot["cognitive_repair"]
    prepared = repair["prepared_revision"]
    contents = program_revision_contents(store, prepared["prepared_program_revision"])
    evidence = _r7_design_program_evidence(store, prepared, repair["prepared_revision_request"], contents)
    if not evidence or evidence["digest"] != EVIDENCE_DIGEST or len(evidence["files"]) != 23:
        _reject("the fixed 23-file program evidence package changed")
    facts = _checkpoint(store, "blueprint-accepted-facts-view")["result"]
    library = CaseLibrary(store, initialize=False)
    library.require_admissible(snapshot["case_basis"])
    library.validate_facts_view(facts, snapshot["case_basis"])
    snapshot["case_facts_view"] = facts
    choices = _checkpoint(store, "case-adaptation-prepared-0b627399d035068e")["result"]["choices"]
    snapshot["case_design"] = choices
    library.require_design_evidence(snapshot["case_basis"], choices)
    research = research_from_accepted_facts(_checkpoint(store, "blueprint-research")["result"], facts)
    cases = [library.get_case(ref["case_id"], ref["revision"]) for ref in snapshot["case_basis"]["case_refs"]]
    policy = policy_for(snapshot["scenario"], PRODUCT_ID)
    source_manifest, matrix = _source_projection_material(research, cases, snapshot, plan["spec"])
    validate_feature_source_references(plan["spec"], ["S01", *[r["id"] for r in research["sources"]]], binding={
        "scenario_id": snapshot["scenario"]["id"], "scenario_revision": snapshot["scenario"]["revision"],
        "case_basis_digest": snapshot["case_basis"]["basis_digest"], "facts_view_digest": facts["view_digest"],
        "research_source_ids": [r["id"] for r in research["sources"]], "file_plan_digest": digest(plan["file_plan"]),
    })
    original_attempt = store.root / "jobs" / JOB_ID / "attempt-1"
    reused = {}
    new_phase = old_phase = None
    originals = []
    with tempfile.TemporaryDirectory(prefix="atlas-evidence-prepare-") as tmp:
        root = Path(tmp)
        context = root / "shared"
        context.mkdir()
        for name, value in (("GUIDANCE.md", snapshot["config"].get("cognition_guidance", "")), ("REVISION.md", repair["note"])):
            if value:
                (context / name).write_text("\n".join(textwrap.fill(line, width=120) for line in value.splitlines()))
        for dimension in (*DESIGN_DIMENSIONS, "runtime_protocol"):
            cp_name = "blueprint-design-check-0-" + dimension
            if dimension == "architecture_contract":
                cp_name += "-ad1379367f3e742a"
            fixed = EXPECTED_REVIEWS[cp_name]
            cp = _checkpoint(store, cp_name, fixed["checkpoint_digest"])
            report = cp["result"]
            originals.append(report)
            if (report.get("proposal_digest") != PROPOSAL_DIGEST
                    or report.get("projection_digest") != fixed["projection_digest"]
                    or report.get("review_rules_version") != "atlas.current-required-contract.v1"
                    or report.get("outcome") != ("blocked" if dimension == "phase_acceptance" else "passed")):
                _reject("original subreview identity or outcome changed: " + dimension)
            stage_name = STAGE_PREFIX + "-" + dimension + ("-v1" if dimension == "runtime_protocol" else "")
            old_stage = original_attempt / stage_name
            input_bytes = (old_stage / "input.json").read_bytes()
            if _sha(input_bytes) != fixed["input_sha256"]:
                _reject("original subreview input bytes changed: " + dimension)
            payload = json.loads(input_bytes)
            config_identity = readonly_cli_config_identity(json.loads((old_stage / "opencode.json").read_bytes()), old_stage)
            old_source = old_stage / "source"
            original_tree = tree_manifest(old_source)
            if digest(original_tree) != fixed["projection_digest"]:
                _reject("original model-visible tree changed: " + dimension)
            # Rebuild an old-style projection from the *current* fixed plan, facts and rules.
            rebuilt = root / dimension
            rebuilt.mkdir()
            _write_design_projection(rebuilt, dimension, snapshot, plan, research, context, source_manifest, matrix, policy, None)
            rebuilt_payload = _design_review_payload(snapshot, plan, dimension, rebuilt, None)
            if tree_manifest(rebuilt) != original_tree or rebuilt_payload != payload or _json_bytes(rebuilt_payload) != input_bytes:
                _reject("non-phase input changed or original projection cannot be reproduced: " + dimension)
            valid = validate_review(report, old_source, (dimension,))
            if valid["outcome"] != report["outcome"]:
                _reject("original review has inconsistent subchecks")
            identity = {"checkpoint_name": cp_name, "checkpoint_digest": cp["digest"], "record": cp,
                        "identical": True, "input_sha256": _sha(input_bytes), "full_payload_digest": digest(payload),
                        "budget_input_digest": digest({k:v for k,v in payload.items() if k != "language"}),
                        "projection_digest": digest(original_tree), "prompt_sha256": OLD_PROMPT_SHA256,
                        "cli_config_identity": config_identity, "cli_config_sha256": _sha((old_stage/"opencode.json").read_bytes()),
                        "config_digest": digest(snapshot["config"]), "requested_model": snapshot["config"]["model"],
                        "old_and_current_payload_equal": True, "old_and_current_prompt_equal": True,
                        "old_and_current_config_equal": True}
            if dimension != "phase_acceptance":
                reused[dimension] = identity
                continue
            old_phase = {**identity, "stage_name": stage_name, "source_tree_digest": digest(original_tree),
                         "reservation_id": PHASE_RESERVATION_ID,
                         "operation": stage_name + ":" + identity["budget_input_digest"][:16]}
            phase_source = root / "new-phase"
            phase_source.mkdir()
            projection_digest = _write_design_projection(phase_source, dimension, snapshot, plan, research, context, source_manifest, matrix, policy, evidence)
            new_payload = _design_review_payload(snapshot, plan, dimension, phase_source, evidence)
            prompt = _r7_phase_acceptance_prompt(evidence)
            input_digest = digest({k:v for k,v in new_payload.items() if k != "language"})
            new_phase = {"stage_name": stage_name, "payload": new_payload,
                         "input_sha256": _sha(_json_bytes(new_payload)), "full_payload_digest": digest(new_payload),
                         "budget_input_digest": input_digest, "prompt": prompt, "prompt_sha256": _sha(prompt.encode()),
                         "source_tree_digest": projection_digest, "projection_digest": projection_digest,
                         "operation": stage_name + ":" + input_digest[:16], "logical_retry_scope": PHASE_SCOPE,
                         "requested_model": snapshot["config"]["model"], "cli_config_identity": config_identity,
                         "source_files": {name:(phase_source/name).read_text() for name in sorted(tree_manifest(phase_source))}}
    if originals != outer["result"].get("subreviews"):
        _reject("the original six-review overview no longer references its exact six original results")
    if len(reused) != 5 or new_phase is None or old_phase is None:
        _reject("evidence prepare is incomplete")
    with store.connect() as con:
        reservation = con.execute("SELECT * FROM tf_budget_reservation WHERE id=?", (PHASE_RESERVATION_ID,)).fetchone()
    if (not reservation or reservation["status"] != "completed" or reservation["job_id"] != JOB_ID
            or reservation["stage"] != old_phase["operation"] or reservation["retry"] is not None):
        _reject("original phase result is not the completed semantic review")
    return {"binding": {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                        "job_id": JOB_ID, "batch_id": BATCH_ID, "attempt": 1,
                        "snapshot_digest": SNAPSHOT_DIGEST, "deadline": DEADLINE},
            "proposal_digest": PROPOSAL_DIGEST, "plan": plan,
            "old_phase": old_phase,
            "old_aggregate": {"checkpoint_name": OUTER_NAME, "checkpoint_digest": outer["digest"], "record": outer},
            "new_phase": new_phase, "reuse_checks": reused,
            "program_hashes": {name:_sha(content.encode()) for name, content in sorted(contents.items())},
            "evidence_digest": evidence["digest"],
            "evidence_files": {name:_sha(raw) for name,raw in sorted(evidence["files"].items())},
            "case_basis_digest": snapshot["case_basis"]["basis_digest"], "facts_view_digest": facts["view_digest"]}
