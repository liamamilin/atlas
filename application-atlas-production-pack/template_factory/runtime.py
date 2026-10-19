"""Container-only verifier. No candidate install/start command runs on the host."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
import uuid

from atlas_runtime import atomic_json
from privacy import redact_text
from .artifacts import command
from .store import FactoryError

IMAGES = {
    "static-web": "python:3.12-slim",
    "python-web": "python:3.12-slim",
    "cli": "python:3.12-slim",
    "node-web": "node:22-bookworm-slim",
}


class DockerVerifier:
    def __init__(self, owner="atlas-factory", timeout=300):
        self.executable = shutil.which("docker")
        self.owner, self.timeout = owner, timeout

    def info(self):
        result = {"available": False, "engine": "docker", "images": IMAGES}
        if not self.executable:
            return {**result, "message": "Docker is not installed"}
        try:
            value = subprocess.run(
                [self.executable, "info", "--format", "{{.ServerVersion}}"],
                capture_output=True,
                stdin=subprocess.DEVNULL,
                text=True,
                timeout=10,
            )
            result.update(
                available=value.returncode == 0,
                version=value.stdout.strip()[:80],
                message=None
                if value.returncode == 0
                else "Start Docker Desktop, then retry the job",
            )
        except (OSError, subprocess.TimeoutExpired):
            result["message"] = "Docker did not respond; start Docker Desktop"
        return result

    def _call(self, argv, cancelled, timeout=None):
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            proc = subprocess.Popen(
                [self.executable, *argv], stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr
            )
            start = time.monotonic()
            try:
                while proc.poll() is None:
                    if cancelled():
                        raise FactoryError("verification cancelled", "cancelled", 409)
                    if (
                        os.fstat(stdout.fileno()).st_size
                        + os.fstat(stderr.fileno()).st_size
                        > 8_000_000
                    ):
                        raise FactoryError(
                            "verification output exceeds evidence limit",
                            "verification_output_limit",
                            409,
                        )
                    if time.monotonic() - start > (timeout or self.timeout):
                        raise FactoryError(
                            "container operation timed out", "verification_timeout", 409
                        )
                    time.sleep(0.15)
                # Fast processes can finish between polls; enforce the bound
                # again before reading, including output written on exit.
                if os.fstat(stdout.fileno()).st_size + os.fstat(stderr.fileno()).st_size > 8_000_000:
                    raise FactoryError("verification output exceeds evidence limit", "verification_output_limit", 409)
                stdout.seek(0)
                stderr.seek(0)
                out = redact_text(stdout.read().decode(errors="replace"))
                err = redact_text(stderr.read().decode(errors="replace"))
                return {
                    "argv": argv,
                    "exit_code": proc.returncode,
                    "output": (out + err)[-16000:],
                    # Never parse a suffix as the complete protocol response.
                    # Consumers reject truncated stdout; only display is tail-cut.
                    "stdout": out[:64000],
                    "stdout_truncated": len(out) > 64000,
                    "stderr": err[-16000:],
                    "passed": proc.returncode == 0,
                }
            finally:
                if proc.poll() is None:
                    proc.terminate()
                    try:
                        proc.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                        proc.wait()

    def verify(
        self,
        app,
        plan,
        evidence,
        cancelled=lambda: False,
        progress=lambda _: None,
        baseline=False,
    ):
        if plan.get("profile") not in IMAGES:
            raise FactoryError(
                "This template's runtime is unsupported: "
                + str(plan.get("reason", "unknown profile")),
                "runtime_unavailable",
                409,
            )
        info = self.info()
        if not info["available"]:
            raise FactoryError(
                info.get("message", "Docker unavailable"), "runtime_unavailable", 503
            )
        evidence = Path(evidence)
        evidence.mkdir(parents=True, exist_ok=True)
        name = "atlas-factory-" + uuid.uuid4().hex
        profile, port = plan["profile"], plan["port"]
        image = IMAGES[profile]
        # Images are selected by Atlas, never a repository Dockerfile or mount.
        pulled = self._call(["image", "inspect", image], cancelled, 15)
        if not pulled["passed"]:
            progress("Preparing container image " + image)
            pulled = self._call(["pull", image], cancelled, 600)
            if not pulled["passed"]:
                raise FactoryError(
                    "could not prepare verifier image; inspect Docker/network",
                    "runtime_unavailable",
                    503,
                )
        image_id = self._call(
            ["image", "inspect", "--format", "{{.Id}}", image], cancelled, 15
        )["output"].strip()
        keepalive = (
            ["node", "-e", "setInterval(()=>{},10000)"]
            if profile == "node-web"
            else ["python3", "-c", "import time; time.sleep(86400)"]
        )
        args = [
            "run",
            "-d",
            "--name",
            name,
            "--label",
            "atlas.factory=" + self.owner,
            "--read-only",
            "--cap-drop=ALL",
            "--security-opt=no-new-privileges",
            "--pids-limit=256",
            "--memory=" + os.environ.get("ATLAS_FACTORY_MEMORY", "1g"),
            "--cpus=" + os.environ.get("ATLAS_FACTORY_CPUS", "2"),
            "--user",
            f"{os.getuid()}:{os.getgid()}",
            "--tmpfs",
            "/tmp:rw,nosuid,size=512m,mode=1777",
            "--env",
            "HOME=/tmp",
            "--env",
            "npm_config_cache=/tmp/npm-cache",
            "--env",
            "PYTHONDONTWRITEBYTECODE=1",
            "--env",
            "PYTHONPATH=/tmp/python-packages",
            "--mount",
            f"type=bind,src={Path(app).resolve()},dst=/workspace",
            "--workdir",
            "/workspace",
        ]
        if plan["start"]:
            args += ["--publish", f"127.0.0.1::{port}"]
        # Pin the resolved image ID for this verification, including restart.
        args += [image_id, *keepalive]
        results = []
        report = {
            "passed": False,
            "baseline": baseline,
            "environment": {
                "engine": "docker",
                "image": image,
                "image_id": image_id,
                "platform": "Linux container",
            },
            "steps": results,
        }
        try:
            created = self._call(args, cancelled, 30)
            if not created["passed"]:
                raise FactoryError(
                    "could not create restricted verification container",
                    "runtime_unavailable",
                    503,
                )
            for phase in ("install", "build", "tests"):
                for argv in plan[phase]:
                    progress("Verification: " + phase)
                    result = self._call(["exec", name, *command(argv)], cancelled)
                    results.append({"phase": phase, **result})
                    if not result["passed"]:
                        return report
            if plan["start"]:
                self._start(name, plan, cancelled)
                mapped = self._call(["port", name, str(port) + "/tcp"], cancelled, 10)[
                    "output"
                ].strip()
                hostport = mapped.rsplit(":", 1)[-1]
                if not hostport.isdigit():
                    raise FactoryError(
                        "Docker did not report an application port",
                        "runtime_unavailable",
                        503,
                    )
                base = "http://127.0.0.1:" + hostport
                deadline = time.monotonic() + 30
                while time.monotonic() < deadline:
                    if cancelled():
                        raise FactoryError("verification cancelled", "cancelled", 409)
                    try:
                        self._http(base + "/")
                        break
                    except (OSError, ValueError):
                        time.sleep(0.3)
                else:
                    results.append(
                        {
                            "phase": "start",
                            "passed": False,
                            "output": "Application did not become ready",
                        }
                    )
                    return report
            else:
                base = None
            if baseline:
                report["passed"] = True
                return report
            # Record the actual network boundary instead of claiming egress isolation.
            networks = self._call(
                [
                    "inspect",
                    "--format",
                    "{{range $key, $value := .NetworkSettings.Networks}}{{$key}}{{end}}",
                    name,
                ],
                cancelled,
                10,
            )
            # Keep bridge attachment for loopback access. Browser requests are
            # restricted below; this is not a network-isolated application.
            report["environment"]["network"] = networks["output"].strip()
            browser_checks = any(
                c["action"]
                in {"goto", "fill", "click", "open_link", "expect_text", "reload"}
                for c in plan["checks"]
            )
            if browser_checks:
                result = self._browser(base, plan, evidence, cancelled, name)
                results.extend(result["steps"])
                if not result["passed"]:
                    return report
            else:
                for check in plan["checks"]:
                    if check["action"] == "command":
                        result = self._call(
                            ["exec", name, *command(check["argv"])], cancelled
                        )
                        result["passed"] = (
                            result["passed"] and check["contains"] in result["output"]
                        )
                    elif check["action"] == "http":
                        try:
                            body = self._http(base + check.get("path", "/"))
                            result = {
                                "passed": check["contains"] in body,
                                "output": body[:1000],
                            }
                        except OSError as error:
                            result = {"passed": False, "output": str(error)}
                    elif check["action"] == "restart":
                        self._call(["restart", name], cancelled, 30)
                        self._start(name, plan, cancelled)
                        time.sleep(1)
                        result = {
                            "passed": True,
                            "output": "Application process restarted",
                        }
                    else:
                        raise FactoryError("unsupported check for runtime")
                    results.append({"phase": "acceptance", "check": check, **result})
                    if not result["passed"]:
                        return report
            report["passed"] = True
            return report
        finally:
            if self.executable:
                try:
                    logs = self._call(
                        ["logs", "--tail", "100", name], lambda: False, 10
                    )
                    (evidence / "container.log").write_text(logs["output"])
                    self._call(["rm", "-f", name], lambda: False, 20)
                finally:
                    atomic_json(evidence / "report.json", report)

    def _start(self, name, plan, cancelled):
        result = self._call(
            ["exec", "-d", name, *command(plan["start"])], cancelled, 15
        )
        if not result["passed"]:
            raise FactoryError(
                "could not start application", "verification_failed", 409
            )

    @staticmethod
    def _http(url):
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *args):
                raise ValueError("verification redirects are not followed")

        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({}), NoRedirect()
        )
        with opener.open(url, timeout=3) as response:
            return response.read(1_000_000).decode(errors="replace")

    def _browser(self, base, plan, evidence, cancelled, container):
        # Trusted Node harness; the candidate cannot modify the verifier script.
        node = shutil.which("node")
        module = (
            Path(__file__).resolve().parents[2]
            / "atlas-web/node_modules/@playwright/test/index.mjs"
        )
        if not node or not module.is_file():
            raise FactoryError(
                "install atlas-web dependencies for browser verification",
                "runtime_unavailable",
                503,
            )
        script = evidence / "browser.mjs"
        script.write_text(
            """import { chromium } from """
            + json.dumps(str(module))
            + """;
import fs from 'node:fs';
import { spawnSync } from 'node:child_process';
const input=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const browser=await chromium.launch({headless:true});
const context=await browser.newContext({acceptDownloads:false,serviceWorkers:'block'});
await context.routeWebSocket('**/*', ws=>ws.close());
await context.route('**/*', route=>{try {const u=new URL(route.request().url()); return u.origin===input.base ? route.continue():route.abort();}catch{return route.abort();}});
const page=await context.newPage(); page.setDefaultTimeout(7000);
await context.tracing.start({screenshots:true,snapshots:true});
const steps=[];
try {for (const check of input.checks) {let passed=true, output=''; try {
 const action=check.action;
 if(action==='command') {const r=spawnSync(input.docker,['exec',input.container,...check.argv],{encoding:'utf8',timeout:30000,maxBuffer:1000000});output=(r.stdout||'')+(r.stderr||'');passed=r.status===0&&output.includes(check.contains);}
 if(action==='restart') {let r=spawnSync(input.docker,['restart',input.container],{encoding:'utf8',timeout:30000}); if(r.status!==0)throw new Error('Container restart failed'); r=spawnSync(input.docker,['exec','-d',input.container,...input.start],{encoding:'utf8',timeout:15000});if(r.status!==0)throw new Error('Application restart failed');await new Promise(r=>setTimeout(r,1000));}
 if(action==='goto') await page.goto(input.base+(check.path||'/'));
 if(action==='fill') await page.locator(check.selector).fill(check.value);
 if(action==='click') await page.locator(check.selector).click();
 if(action==='open_link') {const expected=new URL(check.url);expected.hash='';const [request]=await Promise.all([context.waitForEvent('request',{predicate:r=>r.isNavigationRequest()&&r.url()===expected.href}),page.locator(check.selector).click()]);output='Navigation attempted to '+request.url()+'; external response blocked by verifier';}
 if(action==='reload') await page.reload();
 if(action==='expect_text') {if(page.url()==='about:blank') await page.goto(input.base+'/'); await page.getByText(check.contains,{exact:false}).first().waitFor({state:'visible'});}
 if(action==='http') {const r=await context.request.get(input.base+(check.path||'/'),{maxRedirects:0}); const body=await r.text(); passed=r.ok()&&body.includes(check.contains); output=body.slice(0,1000);}
 } catch(error) {passed=false;output=String(error);}
 steps.push({phase:'acceptance',check,passed,output}); if(!passed)break;}
 await page.screenshot({path:input.screenshot,fullPage:true});
} finally {await context.tracing.stop({path:input.trace});await browser.close();}
fs.writeFileSync(input.result,JSON.stringify({passed:steps.length===input.checks.length&&steps.every(s=>s.passed),steps}));
"""
        )
        payload = {
            "base": base,
            "checks": plan["checks"],
            "docker": self.executable,
            "container": container,
            "start": plan["start"],
            "screenshot": str(evidence / "application.png"),
            "trace": str(evidence / "trace.zip"),
            "result": str(evidence / "browser-result.json"),
        }
        atomic_json(evidence / "browser-input.json", payload)
        proc = subprocess.Popen(
            [node, str(script), str(evidence / "browser-input.json")],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        deadline = time.monotonic() + max(60, len(plan["checks"]) * 10)
        try:
            while proc.poll() is None:
                if cancelled() or time.monotonic() > deadline:
                    proc.terminate()
                    raise FactoryError(
                        "browser verification interrupted or timed out",
                        "verification_timeout",
                        409,
                    )
                time.sleep(0.2)
            _, errors = proc.communicate()
            if proc.returncode:
                raise FactoryError(
                    "browser verifier unavailable: "
                    + redact_text(errors.decode(errors="replace"))[-500:],
                    "runtime_unavailable",
                    503,
                )
            return json.loads((evidence / "browser-result.json").read_text())
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.wait()
