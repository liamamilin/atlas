"""Generate and freeze an application proposal from an exported Atlas package.

The driver authors no application source. OpenCode proposes a plan and one file
at a time; this host validates, preserves the raw evidence, and packages the
proposal for the later independent runtime stage.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import zipfile
import uuid

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PACK = ROOT / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))

from atlas_runtime import atomic_json
from template_factory.artifacts import tree_manifest
from template_factory.cognition import apply_file_response
from template_factory.cli import CLI
from template_factory.delivery import prepare_application
from template_factory.store import FactoryError

MODEL = "commandcode/deepseek/deepseek-v4.1-flash"
EFFORT = "high"
TIMEOUT = 1200
PLAN_NAME = "application-plan.json"
PLAN_PROMPT = """Read source/product-context/HANDOFF.md, CURRENT_PHASE.json,
PROJECT_DECISIONS.json and APP_DELIVERY.md first. Read the complete P0 contract
and the relevant blueprint/ARCHITECTURE.md, PRODUCT.md, DECISIONS.md,
acceptance/README.md and acceptance programs from source/product-context/.
Implement only the selected phase and preserve every frozen contract. Do not
copy or search for historical application source. If source/application-base/
is listed, consult it only as the frozen app being repaired. Plan a small offline Python
standard-library + SQLite + server-rendered HTML application unless the frozen
architecture explicitly commits another stack. Runtime integration: use literal
--port and --data-dir values, store mutable data under /state, and support an
explicit --host option. A normal local launch should default to loopback; the
Docker delivery command should explicitly bind 0.0.0.0 INSIDE the container,
whose port the evaluator publishes only on host 127.0.0.1. This does not add
public sharing, remote fetching, or authentication. Keep source modules independent
where useful. Include every required source, README.md and delivery.json. Each
plan row must be {"path":"relative application-root path","purpose":"...",
"imports":[],"exports":[]} and explain cross-file interfaces. Use no generated
test code and do not claim behavior has been tested. Return only
{"file_plan":[...]} as valid JSON. Paths must be unique and safe. The exact
delivery.json will be authored by you in a later file call and must declare
schema atlas.application-delivery.v1, root '.', exact other source files, and
the offline runtime contract in APP_DELIVERY.md. Runtime commands are literal
argv executed as supplied: use an actual port from 1024 to 65535 and a data
directory beneath the persistent writable /state mount; never use placeholders."""
FILE_PROMPT = """Read source/product-context/HANDOFF.md, CURRENT_PHASE.json,
PROJECT_DECISIONS.json and APP_DELIVERY.md; then read the frozen architecture,
P0 acceptance contract/programs relevant to this file. Preserve the runtime
integration in the file plan: --host defaults to loopback for normal local use,
while delivery.json explicitly uses --host 0.0.0.0 inside the managed container;
its host port is published only on 127.0.0.1. Runtime args are literal and the
data directory is /state, not a relative directory in read-only source. Read
source/application-plan.json and all previously written files listed in
source/application/ or source/application-base/. Author exactly the requested application source file,
README.md, or delivery.json. Preserve the frozen template and do not modify its
acceptance programs. Do not execute code or claim tests passed. Return either
exactly {"path":"the requested relative path","content":"complete UTF-8
content"}, or exactly {"path":"the requested relative path",
"replacements":[{"old":"exact unique existing text","new":"replacement"}]}.
No commentary, extra fields, patches by approximation, or placeholders."""

RESERVED = {
    "delivery-receipt.json", "cli-summary.json", "result.json", "input.json",
    "AGENTS.md", "CLAUDE.md", "opencode.json", "opencode.jsonc",
}
MAX_FILES = 300
MAX_FILE_SIZE = 8 * 1024 * 1024


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest_digest(manifest: dict[str, str]) -> str:
    payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha(payload)


def paths_overlap(left: Path, right: Path) -> bool:
    left, right = left.resolve(), right.resolve()
    return left == right or left in right.parents or right in left.parents


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(path, value)


def safe_rel(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise FactoryError("invalid application path")
    path = PurePosixPath(value)
    if path.is_absolute() or str(path) != value or any(p in {"", ".", ".."} for p in path.parts):
        raise FactoryError("application paths must be normalized relative paths")
    if path.name in RESERVED or any(p in {".git", ".opencode", "node_modules", ".venv", "__pycache__"} for p in path.parts):
        raise FactoryError("application path uses a reserved name")
    if path.name.startswith(".env") or path.suffix.lower() in {".pem", ".key", ".p12"}:
        raise FactoryError("application path may contain credentials")
    return value


def unpack_package(package: Path, destination: Path) -> Path:
    """Copy a package directory or safely unpack its ZIP, returning package root."""
    if package.is_dir():
        tree_manifest(package)
        source = package.resolve()
        shutil.copytree(source, destination, symlinks=False)
        return destination
    if not package.is_file() or package.suffix.lower() != ".zip":
        raise FactoryError("--package must be an exported package directory or ZIP")
    destination.mkdir(parents=True)
    with zipfile.ZipFile(package) as archive:
        names = set()
        for info in archive.infolist():
            if info.is_dir():
                continue
            name = safe_rel(info.filename)
            mode = info.external_attr >> 16
            if mode and (mode & 0o170000) not in (0, 0o100000):
                raise FactoryError("package ZIP contains a link or special file")
            if name in names:
                raise FactoryError("package ZIP contains duplicate paths")
            names.add(name)
            if info.file_size > MAX_FILE_SIZE:
                raise FactoryError("package file exceeds the size limit")
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(info))
    return destination


def package_content_manifest(package: Path) -> dict[str, str]:
    """Return package file hashes independent of ZIP timestamps/metadata."""
    package = Path(package)
    if package.is_dir():
        manifest = {}
        for path in sorted(package.rglob("*")):
            if path.is_dir() and not path.is_symlink():
                continue
            rel = path.relative_to(package).as_posix()
            safe_rel(rel)
            if path.is_symlink() or not path.is_file():
                raise FactoryError("package directory contains a link or special file")
            manifest[rel] = sha(path.read_bytes())
        if not manifest:
            raise FactoryError("package directory is empty")
        return manifest
    if not package.is_file() or package.suffix.lower() != ".zip":
        raise FactoryError("--package must be an exported development package directory or ZIP")
    manifest = {}
    with zipfile.ZipFile(package) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            name = safe_rel(info.filename)
            mode = info.external_attr >> 16
            if mode and (mode & 0o170000) not in (0, 0o100000):
                raise FactoryError("package ZIP contains a link or special file")
            if name in manifest:
                raise FactoryError("package ZIP contains duplicate paths")
            if info.file_size > MAX_FILE_SIZE:
                raise FactoryError("package file exceeds the size limit")
            manifest[name] = sha(archive.read(info))
    if not manifest:
        raise FactoryError("package ZIP is empty")
    return manifest


def package_content_digest(package: Path) -> str:
    return manifest_digest(package_content_manifest(package))


def package_context_digest(package: Path) -> str:
    manifest = package_content_manifest(package)
    prefix = "source/product-context/"
    nested = {name[len(prefix):]: digest for name, digest in manifest.items() if name.startswith(prefix)}
    return manifest_digest(nested or manifest)


def locate_context(package_root: Path) -> Path:
    candidates = [package_root / "source" / "product-context", package_root]
    for candidate in candidates:
        if all((candidate / name).is_file() for name in
               ("HANDOFF.md", "CURRENT_PHASE.json", "PROJECT_DECISIONS.json", "APP_DELIVERY.md")):
            return candidate
    raise FactoryError("package must contain HANDOFF.md, CURRENT_PHASE.json, PROJECT_DECISIONS.json and APP_DELIVERY.md")


def context_inventory(context: Path) -> list[str]:
    files = sorted(p.relative_to(context).as_posix() for p in context.rglob("*") if p.is_file())
    required = {"HANDOFF.md", "CURRENT_PHASE.json", "PROJECT_DECISIONS.json", "APP_DELIVERY.md",
                "HANDOFF_MANIFEST.json",
                "blueprint/ARCHITECTURE.md", "blueprint/PRODUCT.md", "blueprint/DECISIONS.md",
                "blueprint/acceptance/README.md", "blueprint/acceptance/plan.json"}
    missing = required - set(files)
    if missing:
        raise FactoryError("development package is incomplete: " + ", ".join(sorted(missing)))
    contract = json.loads((context / "ACCEPTANCE_CONTRACT.json").read_text(encoding="utf-8"))
    if contract.get("status") != "not_run" or not contract.get("required_case_ids"):
        raise FactoryError("frozen acceptance contract is missing or not in not_run state")
    manifest = json.loads((context / "HANDOFF_MANIFEST.json").read_text(encoding="utf-8"))
    expected_entries = {
        "README.md", "AGENT.md", "HANDOFF.md", "KNOWLEDGE.md", "CURRENT_PHASE.json",
        "PROJECT_DECISIONS.json", "ACCEPTANCE_CONTRACT.json", "APP_DELIVERY.md",
    }
    entry_hashes = manifest.get("entry_sha256")
    if not isinstance(entry_hashes, dict) or set(entry_hashes) != expected_entries:
        raise FactoryError("development handoff manifest has an incomplete entry inventory")
    for name, expected in entry_hashes.items():
        target = context / safe_rel(name)
        if not target.is_file() or sha(target.read_bytes()) != expected:
            raise FactoryError("development handoff entry hash mismatch: " + name)
    blueprint_hashes = manifest.get("blueprint_sha256")
    if not isinstance(blueprint_hashes, dict) or tree_manifest(context / "blueprint") != blueprint_hashes:
        raise FactoryError("frozen blueprint hash inventory mismatch")
    return files


def seed_stage(stage: Path, context: Path, plan=None, written=None, failed_proposal=None) -> list[str]:
    stage.mkdir(parents=True, exist_ok=True)
    source = stage / "source" / "product-context"
    if not source.exists():
        shutil.copytree(context, source)
    inventory = ["source/product-context/" + p for p in context_inventory(source)]
    if plan is not None:
        (stage / "source" / PLAN_NAME).write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        inventory.append("source/" + PLAN_NAME)
    if written:
        app_source = stage / "source" / "application"
        app_source.mkdir(parents=True, exist_ok=True)
        for rel, content in written.items():
            target = app_source / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            inventory.append("source/application/" + rel)
    if failed_proposal:
        failed_root = stage / "source" / "failed-proposal"
        for rel, content in failed_proposal.items():
            target = failed_root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            inventory.append("source/failed-proposal/" + rel)
    return sorted(inventory)


def call_cli(stage: Path, prompt: str, inventory: list[str], extra: dict):
    stage.mkdir(parents=True, exist_ok=True)
    write_json(stage / "input.json", {"phase": "P0", "source_inventory": inventory, **extra})
    return CLI().run(stage, prompt, MODEL, TIMEOUT, lambda: False, lambda *args: None,
                     reasoning_effort=EFFORT)


def fresh_stage(base: Path) -> Path:
    if not base.exists():
        return base
    index = 1
    while True:
        candidate = base.with_name(base.name + "-attempt-" + str(index))
        if not candidate.exists():
            return candidate
        index += 1


def normalize_plan(raw) -> list[dict]:
    rows = raw.get("file_plan") if isinstance(raw, dict) else None
    if not isinstance(rows, list) or not rows or len(rows) > MAX_FILES:
        raise FactoryError("file plan must contain 1 to 300 files")
    seen = set()
    normalized = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"path", "purpose", "imports", "exports"}:
            raise FactoryError("each file plan row needs path, purpose, imports and exports")
        path = safe_rel(row["path"])
        if path in seen:
            raise FactoryError("duplicate planned application path")
        if not all(isinstance(row[k], str) and row[k].strip() for k in ("purpose",)):
            raise FactoryError("file purpose must be nonempty")
        if not all(isinstance(row[k], list) and all(isinstance(x, str) for x in row[k]) for k in ("imports", "exports")):
            raise FactoryError("imports and exports must be string arrays")
        seen.add(path)
        normalized.append(row)
    if "README.md" not in seen or "delivery.json" not in seen:
        raise FactoryError("file plan must include README.md and delivery.json")
    return normalized


def validate_content(path: str, content: str) -> None:
    if not isinstance(content, str) or not content.strip():
        raise FactoryError("application file content must be nonempty")
    size = len(content.encode("utf-8"))
    if size > MAX_FILE_SIZE:
        raise FactoryError("application file exceeds 8 MiB")
    if path.endswith(".py"):
        ast.parse(content, filename=path)
    elif path.endswith(".json"):
        json.loads(content)


def validate_runtime_metadata(files: dict[str, str], architecture_text: str = "") -> None:
    value = json.loads(files["delivery.json"])
    if value.get("schema") != "atlas.application-delivery.v1" or value.get("root") != ".":
        raise FactoryError("delivery.json must use atlas.application-delivery.v1 and root '.'")
    runtime = value.get("runtime")
    if not isinstance(runtime, dict) or runtime.get("profile") != "python-web":
        raise FactoryError("bookmark pilot requires the offline python-web profile")
    if runtime.get("install") != [] or runtime.get("build") != []:
        raise FactoryError("offline Python standard-library delivery requires empty install/build")
    start = runtime.get("start")
    if not isinstance(start, list) or len(start) < 2 or start[0] not in {"python", "python3"}:
        raise FactoryError("runtime.start must launch the Python application")
    if "--port" not in start or "--data-dir" not in start:
        raise FactoryError("runtime.start must accept --port and --data-dir")
    if any("{" in value or "}" in value for value in start):
        raise FactoryError("runtime.start arguments must be literal values, without placeholders")
    if type(runtime.get("port")) is not int or not 1024 <= runtime["port"] <= 65535:
        raise FactoryError("runtime.port must be between 1024 and 65535")
    data_arg = start.index("--data-dir")
    port_arg = start.index("--port")
    if port_arg + 1 >= len(start) or start[port_arg + 1] != str(runtime["port"]):
        raise FactoryError("runtime.start --port must equal the literal runtime.port")
    if data_arg + 1 >= len(start) or not (start[data_arg + 1] == "/state" or start[data_arg + 1].startswith("/state/")):
        raise FactoryError("runtime.start --data-dir must point to the persistent writable /state volume")
    if "--data-dir" not in architecture_text or "SQLite" not in architecture_text:
        raise FactoryError("runtime entry and persistent store must follow frozen SQLite/data-dir architecture")


def source_archive(files: dict[str, str]) -> bytes:
    import io
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, content in sorted(files.items()):
            archive.writestr(path, content.encode("utf-8"))
    return output.getvalue()


def verify_frozen(output: Path, expected_package_digest: str | None = None,
                  expected_phase: str | None = None,
                  expected_context_digest: str | None = None,
                  expected_repair_scope: dict | None = None) -> dict:
    receipt_path = output / "delivery-receipt.json"
    archive = output / "application.zip"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    data = archive.read_bytes()
    if sha(data) != receipt.get("archive_sha256"):
        raise FactoryError("frozen application ZIP hash mismatch")
    expected = receipt.get("files_sha256")
    with zipfile.ZipFile(archive) as zipped:
        actual = {name: sha(zipped.read(name)) for name in sorted(zipped.namelist())}
    if actual != expected:
        raise FactoryError("frozen application file hashes mismatch")
    source_manifest = tree_manifest(output / "application")
    if source_manifest != receipt.get("application_source_sha256"):
        raise FactoryError("frozen application directory differs from its receipt")
    if expected_package_digest is not None and receipt.get("source_package_sha256") != expected_package_digest:
        raise FactoryError("frozen application was produced from a different source package")
    if expected_phase is not None and receipt.get("phase") != expected_phase:
        raise FactoryError("frozen application phase differs from the requested phase")
    if expected_context_digest is not None and receipt.get("source_context_sha256") != expected_context_digest:
        raise FactoryError("frozen application was produced from a different product context")
    if expected_repair_scope is not None and receipt.get("repair_scope") != expected_repair_scope:
        raise FactoryError("frozen application has a different repair scope")
    return receipt


def freeze(files: dict[str, str], output: Path, cli_summaries: list[dict], host_checks: dict,
           architecture_text: str, package_digest: str, context_digest: str, phase: str,
           repair_scope: dict | None = None) -> dict:
    if output.exists():
        if (output / "delivery-receipt.json").is_file():
            return verify_frozen(output, package_digest, phase, context_digest, repair_scope)
        raise FactoryError("output exists without a valid frozen receipt; refusing overwrite")
    validate_runtime_metadata(files, architecture_text)
    application_files = {path: content for path, content in files.items() if path != "delivery.json"}
    archive_data = source_archive(files)
    with tempfile.TemporaryDirectory(prefix="atlas-app-prepare-") as temp:
        prepared = Path(temp) / "application"
        prepared.mkdir()
        metadata = prepare_application(archive_data, prepared)
        if set(metadata["files"]) != set(application_files):
            raise FactoryError("prepare_application returned a different source inventory")
    output.mkdir(parents=True)
    (output / "application").mkdir()
    for path, content in application_files.items():
        target = output / "application" / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    (output / "application.zip").write_bytes(archive_data)
    file_hashes = {path: sha(content.encode("utf-8")) for path, content in sorted(files.items())}
    receipt = {
        "schema": "atlas.application-delivery-receipt.v1",
        "delivery_schema": "atlas.application-delivery.v1",
        "phase": phase,
        "source_package_sha256": package_digest,
        "source_context_sha256": context_digest,
        "archive_sha256": sha(archive_data),
        "files_sha256": file_hashes,
        "application_source_sha256": {p: h for p, h in file_hashes.items() if p != "delivery.json"},
        "validated_metadata": metadata,
        "frozen": True,
    }
    if repair_scope is not None:
        receipt["repair_scope"] = repair_scope
    write_json(output / "delivery-receipt.json", receipt)
    write_json(output / "cli-summaries.json", cli_summaries)
    write_json(output / "host-checks.json", host_checks)
    if repair_scope is not None:
        write_json(output / "repair-scope.json", repair_scope)
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True, type=Path, help="exported complete development package directory or ZIP")
    parser.add_argument("--phase", required=True, choices=["P0"])
    parser.add_argument("--output", type=Path, help="output directory (default: development/initial)")
    parser.add_argument("--repair-from", type=Path, help="frozen application directory to use as repair context")
    parser.add_argument("--feedback", type=Path, help="JSON repair feedback file; required with --repair-from")
    parser.add_argument("--edit-paths", nargs="+", help="restrict a repair to these existing frozen application source files")
    args = parser.parse_args(argv)
    output = (args.output or HERE / "development" / "initial").resolve()
    repair = args.repair_from.resolve() if args.repair_from else None
    package_digest = package_content_digest(args.package.resolve())
    context_digest = package_context_digest(args.package.resolve())
    if bool(repair) != bool(args.feedback):
        parser.error("--repair-from and --feedback must be supplied together")
    if args.edit_paths and not repair:
        parser.error("--edit-paths requires --repair-from and --feedback")
    feedback_value = None
    feedback_digest = None
    if repair:
        try:
            feedback_bytes = args.feedback.read_bytes()
            feedback_value = json.loads(feedback_bytes.decode("utf-8"))
        except FileNotFoundError as error:
            raise FactoryError("repair feedback file does not exist") from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise FactoryError("repair feedback must be valid UTF-8 JSON") from error
        feedback_digest = sha(feedback_bytes)
    work = output.parent / (output.name + ".work")
    if repair and (paths_overlap(output, repair) or paths_overlap(work, repair)):
        parser.error("repair output and work directories must be outside and separate from the frozen base")
    repair_scope = None
    base_receipt = None
    base_files = None
    if args.edit_paths:
        base_receipt = verify_frozen(repair, package_digest, args.phase, context_digest)
        base_files = load_frozen_files(repair)
        repair_scope = make_repair_scope(base_receipt, base_files, args.edit_paths, feedback_digest)
    if output.exists() and (output / "delivery-receipt.json").is_file():
        print(json.dumps(verify_frozen(output, package_digest, args.phase, context_digest, repair_scope), ensure_ascii=False, indent=2))
        return 0
    if not work.exists():
        work.mkdir(parents=True)
        write_json(work / "work-receipt.json", {
            "schema": "atlas.application-development-work.v1",
            "source_package_sha256": package_digest,
            "source_context_sha256": context_digest,
            "repair_scope_sha256": manifest_digest(repair_scope) if repair_scope is not None else None,
            "repair_feedback_sha256": feedback_digest,
            "phase": args.phase,
        })
    else:
        work_receipt_path = work / "work-receipt.json"
        if not work_receipt_path.is_file():
            raise FactoryError("existing work directory has no package/phase binding; use a new --output")
        work_receipt = json.loads(work_receipt_path.read_text(encoding="utf-8"))
        if (work_receipt.get("source_package_sha256") != package_digest
                or work_receipt.get("source_context_sha256") != context_digest
                or work_receipt.get("repair_scope_sha256") != (manifest_digest(repair_scope) if repair_scope is not None else None)
                or work_receipt.get("repair_feedback_sha256") != feedback_digest
                or work_receipt.get("phase") != args.phase):
            raise FactoryError("existing work directory is bound to a different package or phase")
    input_root = work / "package"
    if not input_root.exists():
        package_root = unpack_package(args.package.resolve(), input_root)
        context = locate_context(package_root)
        shutil.copytree(context, work / "product-context")
        context_hashes = tree_manifest(work / "product-context")
        context_inventory(work / "product-context")
        write_json(work / "product-context.sha256.json", {"digest": manifest_digest(context_hashes), "files": context_hashes})
    context = work / "product-context"
    if not context.is_dir():
        raise FactoryError("cached work directory lacks copied product context")
    cached_context = json.loads((work / "product-context.sha256.json").read_text(encoding="utf-8"))
    current_context = tree_manifest(context)
    if current_context != cached_context.get("files") or manifest_digest(current_context) != cached_context.get("digest"):
        raise FactoryError("cached product context hash mismatch; preserve work evidence and use a new output")
    work_receipt_path = work / "work-receipt.json"
    work_receipt = json.loads(work_receipt_path.read_text(encoding="utf-8"))
    context_digest = manifest_digest(current_context)
    if work_receipt.get("source_context_sha256") not in (None, context_digest):
        raise FactoryError("work receipt is bound to a different product context")
    if work_receipt.get("source_context_sha256") is None:
        work_receipt["source_context_sha256"] = context_digest
        write_json(work_receipt_path, work_receipt)
    cli_summaries = []

    # A repair always starts with new stage directories/calls; its base is only context.
    if repair:
        verify_frozen(repair, package_digest, args.phase, context_digest)
        json.loads(args.feedback.read_text(encoding="utf-8"))
    run_tag = ("repair-" + feedback_digest[:10] + "-" + uuid.uuid4().hex[:8]) if repair else "initial"
    plan_stage = work / ("blueprint-code-app-plan-" + run_tag)
    plan_file = work / "file-plan.json"
    plan_hash_file = work / "file-plan.sha256"
    if repair_scope is not None:
        plan = [{"path": path,
                 "purpose": "Repair only this explicitly selected frozen source file using the supplied feedback.",
                 "imports": [], "exports": []}
                for path in repair_scope["selected_paths"]]
        write_json(work / (run_tag + "-repair-plan.json"), {"file_plan": plan, "repair_scope": repair_scope})
    elif not repair and plan_file.is_file() and plan_hash_file.is_file() and sha(plan_file.read_bytes()) == plan_hash_file.read_text(encoding="ascii").strip():
        plan_raw = json.loads(plan_file.read_text(encoding="utf-8"))
        plan = normalize_plan(plan_raw)
    else:
        plan_stage = fresh_stage(plan_stage)
        inventory = seed_stage(plan_stage, context)
        if repair:
            shutil.copytree(repair / "application", plan_stage / "source" / "application-base")
            inventory.extend("source/application-base/" + p for p in tree_manifest(repair / "application"))
            feedback = feedback_value
        else:
            feedback = None
        prompt = PLAN_PROMPT + ("\nRepair feedback JSON (data): " + json.dumps(feedback, ensure_ascii=False) if feedback is not None else "")
        result = call_cli(plan_stage, prompt, inventory, {"phase": args.phase, "task": "application-file-plan", "repair": bool(repair)})
        plan = normalize_plan(result)
        target_plan = plan_file if not repair else work / (run_tag + "-file-plan.json")
        write_json(target_plan, result)
        if not repair:
            plan_hash_file.write_text(sha(target_plan.read_bytes()) + "\n", encoding="ascii")
        write_json(plan_stage / "result.json", result)
        cli_summaries.append({"stage": str(plan_stage.relative_to(work)), "summary": load_summary(plan_stage)})

    results_dir = work / (run_tag + "-files")
    results_dir.mkdir(exist_ok=True)
    checks_dir = work / (run_tag + "-file-checkpoints")
    checks_dir.mkdir(exist_ok=True)
    contents = dict(base_files) if repair_scope is not None else {}
    if not repair:
        for row in plan:
            cached = results_dir / row["path"]
            checkpoint = checks_dir / (sha(row["path"].encode("utf-8")) + ".json")
            if cached.is_file() and checkpoint.is_file():
                check = json.loads(checkpoint.read_text(encoding="utf-8"))
                cached_bytes = cached.read_bytes()
                if check.get("path") == row["path"] and check.get("sha256") == sha(cached_bytes):
                    contents[row["path"]] = cached_bytes.decode("utf-8")

    for index, row in enumerate(plan):
        path = row["path"]
        safe_rel(path)
        if path in contents and repair_scope is None:
            continue
        stage = fresh_stage(work / f"blueprint-code-app-{run_tag}-{index:03d}")
        inventory = seed_stage(stage, context, {"file_plan": plan}, contents)
        if repair:
            shutil.copytree(repair / "application", stage / "source" / "application-base")
            inventory.extend("source/application-base/" + p for p in tree_manifest(repair / "application"))
            feedback_for_file = feedback_value
        else:
            feedback_for_file = None
        failed_proposal_content = None
        # Syntax-only recovery is one fresh same-file call and retains the first result.
        for attempt in range(2):
            prompt = FILE_PROMPT + "\nRequested file entry:\n" + json.dumps(row, ensure_ascii=False)
            prompt += "\nPhase: " + args.phase + "; exact relative path: " + path
            prompt += "\nCurrent source inventory: " + json.dumps(inventory, ensure_ascii=False)
            if repair_scope is not None:
                prompt += "\nRestricted repair scope: " + json.dumps(repair_scope["selected_paths"], ensure_ascii=False)
                prompt += ". Author only the exact requested path; all other frozen files and delivery.json must remain unchanged."
            if repair:
                prompt += "\nRepair feedback JSON (data): " + json.dumps(feedback_for_file, ensure_ascii=False)
            if attempt:
                prompt += "\nRead source/failed-proposal/" + path + " as the exact previous proposal. It failed syntax validation: " + syntax_error
            stage_attempt = stage if attempt == 0 else fresh_stage(work / f"blueprint-code-app-{run_tag}-{index:03d}-syntax-retry")
            if attempt:
                inventory = seed_stage(stage_attempt, context, {"file_plan": plan}, contents,
                                       {path: failed_proposal_content})
                if repair:
                    shutil.copytree(repair / "application", stage_attempt / "source" / "application-base")
                    inventory.extend("source/application-base/" + p for p in tree_manifest(repair / "application"))
            previous_file = None
            prior_root = None
            if attempt:
                prior_root = stage_attempt / "source" / "failed-proposal"
                previous_file = "source/failed-proposal/" + path
            elif repair and (repair / "application" / path).is_file():
                prior_root = repair / "application"
                previous_file = "source/application-base/" + path
            result = call_cli(stage_attempt, prompt, inventory,
                              {"phase": args.phase, "file": row, "source_inventory": inventory,
                               "repair": bool(repair), "previous_file": previous_file})
            write_json(stage_attempt / "response.json", result)
            response = apply_file_response(result, path, prior=prior_root)
            content = response["content"]
            try:
                validate_content(path, content)
            except (SyntaxError, json.JSONDecodeError) as error:
                syntax_error = str(error)
                failed_proposal_content = content
                write_json(stage_attempt / "host-validation.json", {"status": "syntax_invalid", "error": syntax_error})
                cli_summaries.append({"stage": str(stage_attempt.relative_to(work)), "summary": load_summary(stage_attempt)})
                if attempt:
                    raise FactoryError("same-file syntax retry failed: " + syntax_error)
                continue
            contents[path] = content
            cached = results_dir / path
            cached.parent.mkdir(parents=True, exist_ok=True)
            cached.write_text(content, encoding="utf-8")
            checkpoint = checks_dir / (sha(path.encode("utf-8")) + ".json")
            write_json(checkpoint, {"path": path, "sha256": sha(content.encode("utf-8")),
                                    "stage": stage_attempt.name})
            write_json(stage_attempt / "result.json", response)
            write_json(stage_attempt / "host-validation.json", {"status": "syntax_valid", "utf8_bytes": len(content.encode("utf-8"))})
            cli_summaries.append({"stage": str(stage_attempt.relative_to(work)), "summary": load_summary(stage_attempt)})
            break

    if repair_scope is not None:
        if set(contents) != set(base_files):
            raise FactoryError("scoped repair changed the frozen application file inventory")
        actual_unchanged = {path: sha(contents[path].encode("utf-8"))
                            for path in repair_scope["unchanged_sha256"]}
        if actual_unchanged != repair_scope["unchanged_sha256"]:
            raise FactoryError("scoped repair changed an unselected source file or delivery.json")
    architecture_text = (context / "blueprint" / "ARCHITECTURE.md").read_text(encoding="utf-8")
    validate_runtime_metadata(contents, architecture_text)
    final_output = freeze(contents, output, all_cli_summaries(work),
                          {"python_ast": "passed" if any(p.endswith(".py") for p in contents) else "not_applicable",
                           "json_parse": "passed" if any(p.endswith(".json") for p in contents) else "not_applicable",
                           "path_safety": "passed", "inventory": "passed", "utf8_size": "passed",
                           "delivery_prepare_application": "passed", "behavior": "not_run"}, architecture_text,
                          package_digest, context_digest, args.phase, repair_scope)
    print(json.dumps(final_output, ensure_ascii=False, indent=2))
    return 0


def load_summary(stage: Path):
    path = stage / "cli-summary.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {"status": "missing"}


def load_frozen_files(output: Path) -> dict[str, str]:
    """Read exact UTF-8 source and delivery bytes from a verified archive."""
    with zipfile.ZipFile(output / "application.zip") as archive:
        files = {}
        for name in archive.namelist():
            safe_rel(name)
            files[name] = archive.read(name).decode("utf-8")
    return files


def make_repair_scope(receipt: dict, files: dict[str, str], selected_paths: list[str],
                      feedback_sha256: str) -> dict:
    if not isinstance(selected_paths, list) or not selected_paths:
        raise FactoryError("--edit-paths must name at least one frozen source file")
    selected = [safe_rel(path) for path in selected_paths]
    if len(selected) > MAX_FILES:
        raise FactoryError("--edit-paths may select at most 300 files")
    if len(set(selected)) != len(selected):
        raise FactoryError("--edit-paths contains duplicate paths")
    if "delivery.json" in selected:
        raise FactoryError("delivery.json is immutable during scoped source repair")
    app_paths = set(files) - {"delivery.json"}
    unknown = set(selected) - app_paths
    if unknown:
        raise FactoryError("--edit-paths must select existing application source files: " + ", ".join(sorted(unknown)))
    hashes = {path: sha(content.encode("utf-8")) for path, content in files.items()}
    unchanged = {path: hashes[path] for path in sorted(set(files) - set(selected))}
    return {
        "base_archive_sha256": receipt["archive_sha256"],
        "feedback_sha256": feedback_sha256,
        "selected_paths": sorted(selected),
        "unchanged_sha256": unchanged,
    }


def all_cli_summaries(work: Path) -> list[dict]:
    rows = []
    for stage in sorted(work.glob("blueprint-code-app-*")):
        summary_path = stage / "cli-summary.json"
        if summary_path.is_file():
            rows.append({"stage": stage.name, "summary": json.loads(summary_path.read_text(encoding="utf-8"))})
    return rows


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FactoryError as error:
        print(json.dumps({"error": str(error), "code": error.code}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
