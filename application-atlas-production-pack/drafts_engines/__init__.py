"""Pluggable draft-writing engines.

Interface:
    engine.generate(idea: dict, prompt_path: str, pack: str, workdir: str, log_path: str) -> bool

idea keys: slug, name, name_zh, desc, link
Registry: ENGINES[name] -> class; selected via drafts/engines.json ("engine" key)
or --engine flag. Adding an engine = one file + one ENGINES entry.
"""
import os
import re
import subprocess

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINES = {}


def register(cls):
    ENGINES[cls.name] = cls
    return cls


def render_prompt(prompt_path, idea, exemplars=("", "")):
    tpl = open(prompt_path, encoding="utf-8").read()
    # strip the meta header (everything before the first "---" separator line)
    m = re.search(r"^---$", tpl, re.M)
    if m:
        tpl = tpl[m.end():]
    subs = {
        "{{NAME}}": idea["name"],
        "{{NAME_ZH}}": idea.get("name_zh", ""),
        "{{DESC}}": idea.get("desc", ""),
        "{{LINK}}": idea.get("link") or "(none provided)",
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
        from drafts_engines import render_prompt, choose_exemplars
        prompt = render_prompt(prompt_path, idea, choose_exemplars(idea))
        cmd = ["opencode", "run", "--dir", workdir]
        if model:
            cmd += ["-m", model]
        cmd.append(prompt)
        env = dict(os.environ)
        # engine-scoped permissions (allow headless write/bash, keep dangerous denies)
        env["OPENCODE_CONFIG"] = os.path.join(os.path.dirname(log_path), "agent.json")
        with open(log_path, "wb") as log:
            p = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT,
                               timeout=timeout or self.default_timeout, env=env)
        return p.returncode == 0


def get_engine(name=None, model=""):
    cls = ENGINES[name or "opencode"]
    if cls.name == "opencode":
        return cls(), model
    return cls(), ""
