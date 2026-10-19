"""Small, reviewable OpenCode CLI adapter for the Agent Harness pilot.

Atlas owns task state, isolation, review, application and acceptance. This module
only validates the project compatibility contract and runs a CLI command with
an argv list (never a shell string). Preflight stores provider names and exit
diagnostics without returning provider command output or credential values; a prompt
run returns execution stdout/stderr for Atlas evidence under its normal retention policy.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import shutil
import subprocess
import re
from typing import Callable, Sequence

from opencode_permissions import (
    detect_opencode_major_version, install_workdir_permission_policy,
    remove_workdir_permission_policy,
)
from privacy import redact_text, redact_value


MAX_EVIDENCE_TEXT_CHARS = 1_000_000


class HarnessCompatibilityError(RuntimeError):
    """The project contract cannot be satisfied by the local CLI."""

    def __init__(self, code: str, message: str, details: dict | None = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}


@dataclass(frozen=True)
class CliResult:
    argv: tuple[str, ...]
    exit_code: int
    stdout: str
    stderr: str
    timed_out: bool = False

    @property
    def passed(self) -> bool:
        return self.exit_code == 0 and not self.timed_out


@dataclass(frozen=True)
class HarnessConfig:
    path: Path
    executable: str
    minimum_version: str
    expected_provider_names: tuple[str, ...]
    command_timeout_seconds: int


def load_harness_config(workdir: str | Path) -> HarnessConfig:
    root = Path(workdir).resolve()
    path = root / ".atlas" / "harness.json"
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise HarnessCompatibilityError(
            "missing_config", "project is missing .atlas/harness.json", {"path": str(path)}) from error
    except (OSError, json.JSONDecodeError) as error:
        raise HarnessCompatibilityError(
            "invalid_config", "cannot read a valid .atlas/harness.json", {"path": str(path)}) from error

    backend = raw.get("backend") if isinstance(raw, dict) else None
    opencode = backend.get("openCode") if isinstance(backend, dict) else None
    if not isinstance(opencode, dict):
        raise HarnessCompatibilityError("invalid_config", "harness.json has no OpenCode backend")
    source = opencode.get("installSource") or {}
    configured_path = source.get("binaryPath")
    executable = configured_path if isinstance(configured_path, str) and configured_path.strip() else "opencode"
    minimum = opencode.get("minimumCompatibleVersion") or opencode.get("preciseVersion")
    if not isinstance(minimum, str) or not minimum.strip():
        raise HarnessCompatibilityError("invalid_config", "OpenCode minimumCompatibleVersion is required")
    provider = raw.get("provider") if isinstance(raw, dict) else None
    records = provider.get("results") if isinstance(provider, dict) else []
    names = tuple(
        item.get("name", "").strip() for item in records
        if isinstance(item, dict) and isinstance(item.get("name"), str) and item["name"].strip()
    )
    policy = raw.get("policy") if isinstance(raw, dict) else {}
    timeout = policy.get("commandTimeoutSeconds", 600) if isinstance(policy, dict) else 600
    try:
        timeout = max(1, int(timeout))
    except (TypeError, ValueError):
        timeout = 600
    return HarnessConfig(path, executable, minimum.strip(), names, timeout)


def version_parts(value: str) -> tuple[int, ...]:
    """Parse numeric semver-ish versions while ignoring a leading `v`."""
    text = value.strip().lstrip("vV")
    match = re.search(r"\d+(?:\.\d+)*", text)
    if not match:
        raise ValueError(f"invalid version: {value!r}")
    return tuple(int(item) for item in match.group(0).split("."))


def version_at_least(actual: str, minimum: str) -> bool:
    left, right = version_parts(actual), version_parts(minimum)
    size = max(len(left), len(right))
    return (left + (0,) * (size - len(left))) >= (right + (0,) * (size - len(right)))


def resolve_executable(config: HarnessConfig) -> str:
    candidate = config.executable
    path = Path(candidate).expanduser()
    if path.is_absolute():
        if not path.is_file() or not path.stat().st_mode & 0o111:
            raise HarnessCompatibilityError(
                "cli_unavailable", "configured OpenCode binary is not executable", {"path": str(path)})
        return str(path)
    resolved = shutil.which(candidate)
    if not resolved:
        raise HarnessCompatibilityError(
            "cli_unavailable", "OpenCode CLI was not found on PATH", {"command": candidate})
    return resolved


def _run(argv: Sequence[str], cwd: Path, timeout: int) -> CliResult:
    environment = dict(os.environ)
    # Permission policy is always Atlas-owned. A project-provided config must
    # not be able to re-enable shell, web, or external-directory access.
    major_version = detect_opencode_major_version(str(argv[0]))
    policy_required = len(argv) > 1 and argv[1] == "run"
    if policy_required:
        install_workdir_permission_policy(cwd, major_version)
    try:
        completed = subprocess.run(
            list(argv), cwd=str(cwd), text=True, capture_output=True,
            timeout=timeout, check=False, env=environment)
        return CliResult(tuple(argv), completed.returncode, completed.stdout, completed.stderr)
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout if isinstance(error.stdout, str) else ""
        stderr = error.stderr if isinstance(error.stderr, str) else ""
        return CliResult(tuple(argv), 124, stdout, stderr, timed_out=True)
    except OSError as error:
        return CliResult(tuple(argv), 127, "", str(error))
    finally:
        if policy_required:
            remove_workdir_permission_policy(cwd)


def preflight(workdir: str | Path, runner: Callable[[Sequence[str], Path, int], CliResult] = _run) -> dict:
    """Validate the compatibility contract and return safe, reviewable evidence."""
    root = Path(workdir).resolve()
    config = load_harness_config(root)
    executable = resolve_executable(config)
    version_result = runner((executable, "--version"), root, config.command_timeout_seconds)
    version_text = (version_result.stdout or version_result.stderr).strip().splitlines()
    raw_version = version_text[0].strip() if version_text else ""
    if not raw_version:
        raise HarnessCompatibilityError(
            "version_unavailable", "OpenCode did not report a version",
            {"exitCode": version_result.exit_code})
    try:
        actual = ".".join(str(item) for item in version_parts(raw_version))
        compatible = version_at_least(actual, config.minimum_version)
    except ValueError:
        actual = raw_version
        compatible = False
    if not compatible:
        raise HarnessCompatibilityError(
            "version_incompatible",
            f"OpenCode {actual} does not satisfy minimum {config.minimum_version}",
            {"actualVersion": actual, "minimumVersion": config.minimum_version})

    # V2's model listing starts the service and may itself require a shell
    # permission in headless configurations. `debug config` is a read-only
    # compatibility probe that exposes provider configuration without
    # contacting a provider or returning credentials.
    provider_command = ((executable, "providers", "list") if actual.split(".", 1)[0] == "1"
                        else (executable, "debug", "config"))
    providers_result = runner(provider_command, root, config.command_timeout_seconds)
    provider_output_present = bool((providers_result.stdout or providers_result.stderr).strip())
    return {
        "status": "passed" if version_result.passed and providers_result.passed and provider_output_present else "failed",
        "configPath": str(config.path),
        "executable": executable,
        "version": actual,
        "minimumVersion": config.minimum_version,
        "providerNames": list(config.expected_provider_names),
        "checks": {
            "version": {"passed": version_result.passed, "exitCode": version_result.exit_code},
            "providers": {"passed": providers_result.passed and provider_output_present, "exitCode": providers_result.exit_code},
        },
        "diagnostics": {
            "providerOutputPresent": provider_output_present,
            "timedOut": version_result.timed_out or providers_result.timed_out,
        },
    }


def build_run_argv(executable: str, prompt: str, workdir: str | Path,
                   model: str | None = None) -> tuple[str, ...]:
    """Build a shell-free CLI invocation for a controlled work directory."""
    if not prompt.strip():
        raise ValueError("prompt is required")
    root = Path(workdir).resolve()
    if not root.is_dir():
        raise ValueError("workdir must be an existing directory")
    # V2 discovers the project from cwd and requires a private server for an
    # unattended run. V1 used --pure; neither version needs the removed --dir
    # form because the subprocess cwd is already the isolated project.
    major_version = detect_opencode_major_version(executable)
    private_flag = "--standalone" if major_version >= 2 else "--pure"
    argv = [executable, "run", "--format", "json", private_flag]
    if model:
        argv.extend(("--model", model))
    argv.append(prompt)
    return tuple(argv)


def run_prompt(workdir: str | Path, prompt: str, model: str | None = None,
               runner: Callable[[Sequence[str], Path, int], CliResult] = _run) -> dict:
    config = load_harness_config(workdir)
    root = Path(workdir).resolve()
    executable = resolve_executable(config)
    argv = build_run_argv(executable, prompt, root, model)
    result = runner(argv, root, config.command_timeout_seconds)
    result_payload = {
        "status": "completed" if result.passed else "failed",
        "argv": list(argv),
        "exitCode": result.exit_code,
        "timedOut": result.timed_out,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    result_payload["summary"] = summarize_run(result_payload)
    return result_payload


def summarize_run(result: dict) -> dict:
    """Normalize a CLI result into task evidence without assuming one event schema.

    OpenCode's JSON mode can evolve, so Atlas records only stable transport facts
    and the set of top-level event types. The original stdout/stderr remain
    available to the evidence writer under its normal retention policy.
    """
    if not isinstance(result, dict):
        raise ValueError("result must be an object")
    exit_code = result.get("exitCode")
    timed_out = bool(result.get("timedOut"))
    if timed_out:
        status = "timed_out"
    elif exit_code == 0:
        status = "completed"
    else:
        status = "failed"
    stdout = result.get("stdout") if isinstance(result.get("stdout"), str) else ""
    stderr = result.get("stderr") if isinstance(result.get("stderr"), str) else ""
    event_types: list[str] = []
    event_count = 0
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        event_count += 1
        event_type = event.get("type")
        if isinstance(event_type, str) and event_type.strip():
            event_types.append(event_type.strip())
    summary = {
        "status": status,
        "exitCode": exit_code,
        "timedOut": timed_out,
        "argv": list(result.get("argv") or []),
        "stdoutBytes": len(stdout.encode("utf-8")),
        "stderrBytes": len(stderr.encode("utf-8")),
        "jsonEventCount": event_count,
        "eventTypes": sorted(set(event_types)),
    }
    code, hint = diagnose_cli_failure(result, stderr)
    summary["diagnosticCode"] = code
    summary["diagnosticHint"] = hint
    return summary


def diagnose_cli_failure(result: dict, stderr: str | None = None) -> tuple[str | None, str | None]:
    """Classify a failed CLI transport without persisting raw provider output.

    The classifier intentionally uses broad, stable signals because OpenCode's
    detailed error schema can change. Raw stderr remains available only in the
    normal evidence directory; the summary exposes a safe code and next action.
    """
    if not isinstance(result, dict):
        return "invalid_result", "inspect the execution evidence"
    if bool(result.get("timedOut")):
        return "timeout", "increase the task timeout or inspect the command output"
    exit_code = result.get("exitCode")
    if exit_code == 0:
        return None, None
    text = stderr if isinstance(stderr, str) else result.get("stderr")
    text = text if isinstance(text, str) else ""
    lowered = text.lower()
    if "filesystem.open" in lowered and ("log" in lowered or "permission" in lowered):
        return "log_access", "allow OpenCode to create or open its local log file, then retry"
    if "unexpected server error" in lowered or "provider" in lowered and "error" in lowered:
        return "provider_error", "check the configured provider, credentials and network, then retry"
    if "unknown option" in lowered or "invalid option" in lowered or "unknown argument" in lowered:
        return "cli_protocol", "check the OpenCode CLI version and Atlas argument contract"
    if "filesystem.open" in lowered or "permission denied" in lowered or "operation not permitted" in lowered:
        return "filesystem_access", "check the isolated workdir and local file permissions"
    return "process_exit", "inspect stderr.txt in the execution evidence directory"


def _bounded_evidence_text(value: str) -> tuple[str, bool]:
    redacted = redact_text(value)
    if len(redacted) <= MAX_EVIDENCE_TEXT_CHARS:
        return redacted, False
    marker = f"\n\n[Atlas truncated {len(redacted) - MAX_EVIDENCE_TEXT_CHARS} characters]\n\n"
    available = MAX_EVIDENCE_TEXT_CHARS - len(marker)
    head = available // 2
    tail = available - head
    return redacted[:head] + marker + redacted[-tail:], True


def write_run_evidence(result: dict, evidence_dir: str | Path) -> dict:
    """Persist CLI transport evidence in a self-contained directory."""
    if not isinstance(result, dict):
        raise ValueError("result must be an object")
    root = Path(evidence_dir).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(root, 0o700)
    summary = result.get("summary") if isinstance(result.get("summary"), dict) \
        else summarize_run(result)
    stdout, stdout_truncated = _bounded_evidence_text(
        result.get("stdout") if isinstance(result.get("stdout"), str) else "")
    stderr, stderr_truncated = _bounded_evidence_text(
        result.get("stderr") if isinstance(result.get("stderr"), str) else "")
    metadata = redact_value({
        "schema": 1,
        "argv": list(result.get("argv") or []),
        "summary": summary,
        "files": {"stdout": "stdout.txt", "stderr": "stderr.txt"},
        "truncated": {"stdout": stdout_truncated, "stderr": stderr_truncated},
    })
    files = {
        "stdout.txt": stdout,
        "stderr.txt": stderr,
        "run.json": json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
    }
    for name, content in files.items():
        path = root / name
        path.write_text(content, encoding="utf-8")
        os.chmod(path, 0o600)
    return {"directory": str(root), "metadata": metadata}
