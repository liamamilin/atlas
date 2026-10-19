"""Pluggable draft-writing engines.

Interface:
    engine.generate(idea: dict, prompt_path: str, pack: str, workdir: str, log_path: str) -> bool

idea keys: slug, name, name_zh, desc, link
Registry: ENGINES[name] -> class; selected via drafts/engines.json ("engine" key)
or --engine flag. Adding an engine = one file + one ENGINES entry.
"""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading

from opencode_permissions import (
    detect_opencode_major_version, install_workdir_permission_policy,
    remove_workdir_permission_policy,
)
from privacy import redact_text

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MCP_ATLAS_SCRIPT = str(Path(__file__).resolve().parent.parent / "mcp_atlas.py")

ENGINES = {}
_DRAFT_POLICY_LOCK = threading.Lock()


def register(cls):
    ENGINES[cls.name] = cls
    return cls


def render_prompt(prompt_path, idea, exemplars=("", "")):
    tpl = Path(prompt_path).read_text(encoding="utf-8")
    # strip the meta header (everything before the first "---" separator line)
    m = re.search(r"^---$", tpl, re.M)
    if m:
        tpl = tpl[m.end():]
    subs = {
        "{{NAME}}": idea["name"],
        "{{NAME_ZH}}": idea.get("name_zh", ""),
        "{{DESC}}": idea.get("desc", ""),
        "{{LINK}}": idea.get("link") or "(none provided)",
        "{{LINK_EXCERPT}}": idea.get("link_excerpt") or "(no safe link excerpt was available)",
        "{{SLUG}}": idea["slug"],
        "{{EXEMPLAR1}}": exemplars[0],
        "{{EXEMPLAR2}}": exemplars[1],
    }
    for k, v in subs.items():
        tpl = tpl.replace(k, v)
    return tpl


def choose_exemplars(idea):
    """Exemplar leaves for calibration: nearest by slug prefix, else fixed defaults."""
    apps = os.path.join(PACK, "applications")
    fixed = ["directory-application", "3d-animation-application"]
    out = []
    for key in (idea["slug"], idea.get("name", "")):
        words = re.split(r"[-\s]+", key.lower()) if key else []
        scored = []
        for f in os.listdir(apps):
            s = f[:-3]
            hit = sum(1 for w in words if w and w in s)
            if hit:
                scored.append((-hit, s))
        scored.sort()
        out = [s for _, s in scored[:2]]
        if out:
            break
    return (out + [e for e in fixed if e not in out])[:2]


def draft_permission_config(
        slug: str, exemplars: tuple[str, str], major_version: int,
        allow_web: bool = False) -> dict:
    read_paths = [
        "WRITING_GUIDE.md",
        f"applications/{exemplars[0]}.md",
        f"applications/{exemplars[1]}.md",
        f"drafts/{slug}.md",
    ]
    output_paths = [
        f"drafts/{slug}.identity.json",
        f"drafts/{slug}.body.md",
        f"drafts/{slug}.research.md",
    ]
    web_effect = "ask" if allow_web else "deny"
    if major_version >= 2:
        mcp_read_tools = (
            "search_atlas", "get_leaf", "read_atlas_source",
            "get_atlas_source_manifest", "get_section_tree", "get_neighbors",
        )
        permissions = [
            {"action": "*", "resource": "*", "effect": "deny"},
            {"action": "read", "resource": "*", "effect": "deny"},
            *[
                {"action": "read", "resource": path, "effect": "allow"}
                for path in read_paths
            ],
            {"action": "edit", "resource": "*", "effect": "deny"},
            *[
                {"action": "edit", "resource": path, "effect": "allow"}
                for path in output_paths
            ],
            {"action": "edit", "resource": ".opencode/**", "effect": "deny"},
            {"action": "edit", "resource": ".opencode/opencode.json", "effect": "deny"},
            {"action": "glob", "resource": "*", "effect": "deny"},
            {"action": "grep", "resource": "*", "effect": "deny"},
            {"action": "shell", "resource": "*", "effect": "deny"},
            {"action": "webfetch", "resource": "*", "effect": web_effect},
            {"action": "websearch", "resource": "*", "effect": web_effect},
            {"action": "external_directory", "resource": "*", "effect": "deny"},
            {"action": "subagent", "resource": "*", "effect": "deny"},
            {"action": "question", "resource": "*", "effect": "deny"},
            {"action": "execute", "resource": "*", "effect": "deny"},
            {"action": "application_atlas_classify_product", "resource": "*", "effect": "deny"},
            *[
                {"action": f"application_atlas_{tool}", "resource": "*", "effect": "allow"}
                for tool in mcp_read_tools
            ],
        ]
        return {
            "$schema": "https://opencode.ai/config.json",
            "permissions": permissions,
            "agents": {"build": {"permissions": permissions}},
            "mcp": {
                "application-atlas": {
                    "type": "local",
                    "command": [sys.executable, MCP_ATLAS_SCRIPT, "--atlas-read-only"],
                    "enabled": True,
                },
            },
        }
    permission = {
        "read": {"*": "deny", **{path: "allow" for path in read_paths}},
        "edit": {
            "*": "deny",
            **{path: "allow" for path in output_paths},
            "opencode.json": "deny",
            ".opencode/opencode.json": "deny",
        },
        "glob": "deny",
        "grep": "deny",
        "list": "deny",
        "code_mode": "deny",
        "skill": "deny",
        "execute": "deny",
        "bash": "deny",
        "webfetch": web_effect,
        "websearch": web_effect,
        "application_atlas_classify_product": "deny",
        "application_atlas_search_atlas": "allow",
        "application_atlas_get_leaf": "allow",
        "application_atlas_read_atlas_source": "allow",
        "application_atlas_get_atlas_source_manifest": "allow",
        "application_atlas_get_section_tree": "allow",
        "application_atlas_get_neighbors": "allow",
        "external_directory": "deny",
        "task": "deny",
        "question": "deny",
    }
    return {
        "$schema": "https://opencode.ai/config.json",
        "permission": permission,
        "agent": {"build": {"permission": permission}},
        # V1 has one project config file, so the temporary policy replaces the
        # pack's MCP declaration. Keep only Atlas's read-only server available;
        # the V2 policy above declares the same server explicitly.
        "mcp": {
            "application-atlas": {
                "type": "local",
                "command": [sys.executable, MCP_ATLAS_SCRIPT, "--atlas-read-only"],
                "enabled": True,
            },
        },
    }


def _bounded_draft_log(value: str) -> str:
    value = redact_text(value)
    limit = 1_000_000
    if len(value) <= limit:
        return value
    marker = f"\n\n[Atlas truncated {len(value) - limit} characters]\n\n"
    available = limit - len(marker)
    head = available // 2
    return value[:head] + marker + value[-available + head:]


class BaseEngine:
    name = "base"
    default_timeout = 3600

    def run(self, cmd, log_path, timeout=None):
        with open(log_path, "wb") as log:
            p = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT,
                               timeout=timeout or self.default_timeout)
        return p.returncode == 0


@register
class OpencodeEngine(BaseEngine):
    name = "opencode"

    def generate(self, idea, prompt_path, workdir, log_path, model="", timeout=None):
        from drafts_engines import choose_exemplars, draft_permission_config, render_prompt
        exemplars = choose_exemplars(idea)
        prompt = render_prompt(prompt_path, idea, exemplars)
        # V2 discovers the project from cwd; --dir was removed from the current
        # CLI and the old OPENCODE_CONFIG variable is ignored by V2.
        executable = os.environ.get("ATLAS_OPENCODE_BINARY", "").strip()
        if not executable:
            executable = shutil.which("opencode") or "opencode"
        major_version = detect_opencode_major_version(executable)
        private_flag = "--standalone" if major_version >= 2 else "--pure"
        cmd = [executable, "run", private_flag]
        if model:
            cmd += ["--model", model]
        cmd.append(prompt)
        allow_web = os.environ.get("ATLAS_DRAFT_ALLOW_WEB") == "1"
        # Atlas temporarily owns the project config. Serializing this short
        # section avoids two draft workers racing on the same pack-level path.
        with _DRAFT_POLICY_LOCK:
            install_workdir_permission_policy(workdir, major_version)
            try:
                # Replace the generic execution policy with the draft-specific
                # exact read/write/MCP policy for the duration of the run.
                target = (Path(workdir) / ".opencode" / "opencode.json"
                          if major_version >= 2 else Path(workdir) / "opencode.json")
                target.parent.mkdir(parents=True, exist_ok=True)
                os.chmod(target, 0o600)
                target.write_text(json.dumps(
                    draft_permission_config(
                        idea["slug"], exemplars, major_version,
                        allow_web=allow_web),
                    ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                os.chmod(target, 0o400)
                env = dict(os.environ)
                completed = subprocess.run(
                    cmd, cwd=str(workdir), text=True, capture_output=True,
                    timeout=timeout or self.default_timeout, env=env, check=False)
            finally:
                remove_workdir_permission_policy(workdir)
        output = _bounded_draft_log(
            (completed.stdout or "") + (completed.stderr or ""))
        Path(log_path).write_text(output, encoding="utf-8")
        os.chmod(log_path, 0o600)
        return completed.returncode == 0


def get_engine(name=None, model=""):
    cls = ENGINES[name or "opencode"]
    if cls.name == "opencode":
        return cls(), model
    return cls(), ""
