"""Opt-in integration tests that run only synthetic apps in local Docker."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.blueprint_runtime import BlueprintRuntimeVerifier
from template_factory.runtime import IMAGES
from template_factory.store import FactoryError


ENABLED = os.environ.get("ATLAS_RUN_DOCKER_INTEGRATION") == "1"


def _write_suite(root, rows, programs):
    root = Path(root)
    acceptance = root / "acceptance"
    acceptance.mkdir(parents=True)
    for path, source in programs.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source, encoding="utf-8")
    (acceptance / "runner.json").write_text(json.dumps({
        "schema": "atlas.acceptance-runner.v1",
        "result_schema": "atlas.acceptance-result.v1",
        "cases": {row["id"]: {"args": row["args"]} for row in rows},
    }), encoding="utf-8")
    return {"acceptance": [{key: value for key, value in row.items() if key != "args"} for row in rows],
            "phases": [{"id": "P0"}]}


def _python_http_app(body, startup_diagnostic=""):
    return """import sys,traceback
from http.server import BaseHTTPRequestHandler,HTTPServer
diagnostic = %r
if diagnostic:
    try:
        raise RuntimeError(diagnostic)
    except RuntimeError:
        traceback.print_exc()
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = %r.encode()
        self.send_response(200)
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)
    def log_message(self, *args):
        pass
HTTPServer(('0.0.0.0', int(sys.argv[1])), Handler).serve_forever()
""" % (startup_diagnostic, body)


def _node_http_app():
    return """const http=require('http');
const port=Number(process.argv[2]);
console.error('node synthetic startup capture');
http.createServer((req,res)=>{res.writeHead(200,{'Content-Type':'text/plain'});res.end('synthetic-ok')}).listen(port,'0.0.0.0');
"""


def _py_http_case():
    return """import json,sys,urllib.request
case_id,base=sys.argv[1],sys.argv[2]
try:
    body=urllib.request.urlopen(base,timeout=3).read().decode()
    ok='synthetic-ok' in body
except Exception as error:
    body=str(error); ok=False
print(json.dumps({'schema':'atlas.acceptance-result.v1','case_id':case_id,'status':'passed' if ok else 'failed','assertions':[{'id':'body','passed':ok,'detail':body[:200]}]}))
sys.exit(0 if ok else 1)
"""


def _node_http_case():
    return """const [caseId,base]=process.argv.slice(2);
let detail='',ok=false;
try { const response=await fetch(base); detail=await response.text(); ok=response.ok&&detail.includes('synthetic-ok'); }
catch(error) { detail=String(error); }
console.log(JSON.stringify({schema:'atlas.acceptance-result.v1',case_id:caseId,status:ok?'passed':'failed',assertions:[{id:'body',passed:ok,detail:detail.slice(0,200)}]}));
process.exit(ok?0:1);
"""


@unittest.skipUnless(ENABLED, "set ATLAS_RUN_DOCKER_INTEGRATION=1 to run isolated local Docker tests")
class BlueprintRuntimeDockerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("docker"):
            raise unittest.SkipTest("Docker CLI unavailable")
        info = subprocess.run(["docker", "info", "--format", "{{.ServerVersion}}"], capture_output=True, text=True, timeout=10)
        if info.returncode:
            raise unittest.SkipTest("Docker daemon unavailable: " + info.stderr[-300:])
        for image in set(IMAGES.values()):
            exists = subprocess.run(["docker", "image", "inspect", image], capture_output=True, text=True, timeout=10)
            if exists.returncode:
                raise unittest.SkipTest("required local image missing: " + image)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="atlas-blueprint-docker-test-")
        self.root = Path(self.tmp.name)
        self.owner = "atlas-blueprint-integration-" + uuid.uuid4().hex
        self.verifier = BlueprintRuntimeVerifier(owner=self.owner, timeout=75)
        self.evidence = self.root / "evidence"
        self.app = self.root / "app"
        self.app.mkdir()

    def tearDown(self):
        self.assert_no_owned_containers()
        self.tmp.cleanup()

    def assert_no_owned_containers(self):
        result = subprocess.run(["docker", "ps", "-aq", "--filter", "label=atlas.factory=" + self.owner],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "", "owned Docker container remained after verifier cleanup")

    def make_web(self, body="synthetic-ok", startup_diagnostic=""):
        (self.app / "main.py").write_text(_python_http_app(body, startup_diagnostic), encoding="utf-8")
        runtime = {"profile":"python-web", "install":[], "build":[],
                   "start":["python3", "-c", _python_http_app(body, startup_diagnostic), "8080"],
                   "port":8080, "readiness_path":"/"}
        return runtime

    def make_web_suite(self, negative=False):
        rows = [
            {"id":"A01", "phase":"P0", "implementation":"acceptance/python_http.py",
             "args":["{case_id}", "{base_url}"]},
            {"id":"A02", "phase":"P0", "implementation":"acceptance/node_http.mjs",
             "args":["{case_id}", "{base_url}"]},
        ]
        source = self.root / "frozen-source"
        spec = _write_suite(source, rows, {
            "acceptance/python_http.py": _py_http_case(),
            "acceptance/node_http.mjs": _node_http_case(),
        })
        return source, spec

    def test_mixed_python_node_cases_pass_against_stdlib_web_app_and_preserve_source(self):
        runtime = self.make_web()
        source, spec = self.make_web_suite()
        before = {p.relative_to(self.app).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in self.app.rglob("*") if p.is_file()}
        report = self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        after = {p.relative_to(self.app).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in self.app.rglob("*") if p.is_file()}
        self.assertTrue(report["passed"], report)
        self.assertEqual([row["id"] for row in report["case_results"]], ["A01", "A02"])
        self.assertEqual(before, after)
        self.assertTrue(report["app_source_unchanged"])
        self.assertTrue(report["cleanup"]["success"])

    def test_negative_acceptance_valid_failed_json_and_nonzero_exit_is_blocked(self):
        runtime = self.make_web(body="synthetic-wrong")
        source, spec = self.make_web_suite(negative=True)
        report = self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        self.assertFalse(report["passed"])
        self.assertEqual(report["case_results"][0]["status"], "failed")
        self.assertEqual(report["case_results"][0]["exit_code"], 1)
        self.assertEqual(report["outcome"], "blocked")

    def test_startup_exception_traceback_is_captured_from_stderr(self):
        runtime = self.make_web(startup_diagnostic="synthetic startup exception")
        source, spec = self.make_web_suite()
        report = self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        captured = report["startup"]["captured_output"]["stderr"]
        self.assertIn("RuntimeError: synthetic startup exception", captured)
        self.assertTrue(report["startup"]["readiness"]["passed"])

    def test_startup_exception_exit_is_blocked_and_traceback_is_preserved(self):
        (self.app / "main.py").write_text("raise RuntimeError('synthetic startup exit')\n", encoding="utf-8")
        runtime = {"profile":"python-web", "install":[], "build":[],
                   "start":["python3", "main.py"], "port":8080, "readiness_path":"/"}
        row = {"id":"A01", "phase":"P0", "implementation":"acceptance/python_http.py",
               "args":["{case_id}", "{base_url}"]}
        source = self.root / "frozen-source"
        spec = _write_suite(source, [row], {"acceptance/python_http.py":_py_http_case()})
        self.verifier.timeout = 45
        report = self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        self.assertEqual(report["outcome"], "blocked")
        self.assertEqual(report["startup"]["status"], "blocked")
        self.assertEqual(report["case_results"], [])
        self.assertIn("RuntimeError: synthetic startup exit", report["startup"]["captured_output"]["stderr"])

    def test_node_web_launcher_serves_real_request_to_python_tester(self):
        (self.app / "main.js").write_text(_node_http_app(), encoding="utf-8")
        runtime = {"profile":"node-web", "install":[], "build":[],
                   "start":["node", "main.js", "8080"], "port":8080, "readiness_path":"/"}
        row = {"id":"A01", "phase":"P0", "implementation":"acceptance/python_http.py",
               "args":["{case_id}", "{base_url}"]}
        source = self.root / "frozen-source"
        spec = _write_suite(source, [row], {"acceptance/python_http.py":_py_http_case()})
        report = self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        self.assertTrue(report["passed"], report)
        refs = {item["reference"] for item in report["environment"]["images"].values()}
        self.assertIn("node:22-bookworm-slim", refs)
        self.assertIn("python:3.12-slim", refs)
        self.assertIn("node synthetic startup capture", report["startup"]["captured_output"]["stderr"])

    def test_cli_smoke_and_mixed_python_node_acceptance(self):
        cli_source = """import argparse,json,sys
parser=argparse.ArgumentParser()
parser.add_argument('--smoke',action='store_true')
parser.add_argument('--input')
args=parser.parse_args()
if args.smoke:
    print('synthetic-cli-smoke')
    raise SystemExit(0)
if not args.input:
    parser.error('--input is required')
try:
    value=json.load(open(args.input,encoding='utf-8'))
    left,right=value['left'],value['right']
    if type(left) is not int or type(right) is not int:
        parser.error('values must be integers')
    if left < 0 or right < 0:
        parser.error('values must be non-negative')
except (OSError,ValueError,KeyError) as error:
    parser.error(str(error))
print(left+right)
"""
        (self.app / "main.py").write_text(cli_source, encoding="utf-8")
        runtime = {"profile":"cli", "install":[], "build":[], "smoke":["python3", "main.py", "--smoke"]}
        rows = [
            {"id":"A01", "phase":"P0", "implementation":"acceptance/python_cli.py", "args":["{case_id}", "{app_root}", "{data_dir}"]},
            {"id":"A02", "phase":"P0", "implementation":"acceptance/python_cli.py", "args":["{case_id}", "{app_root}", "{data_dir}", "invalid"]},
        ]
        py = """import json,pathlib,subprocess,sys
case_id,root,data_dir=sys.argv[1:4]
invalid=len(sys.argv)>4
fixture=pathlib.Path(data_dir)/('invalid.json' if invalid else 'valid.json')
fixture.write_text(json.dumps({'left':-2 if invalid else 4,'right':3}),encoding='utf-8')
result=subprocess.run([sys.executable,str(pathlib.Path(root)/'main.py'),'--input',str(fixture)],capture_output=True,text=True,timeout=5)
ok=(result.returncode==2 and 'values must be non-negative' in result.stderr) if invalid else (result.returncode==0 and result.stdout.strip()=='7')
detail=(result.stdout+' '+result.stderr).strip()[:200]
print(json.dumps({'schema':'atlas.acceptance-result.v1','case_id':case_id,'status':'passed' if ok else 'failed','assertions':[{'id':'cli-behavior','passed':ok,'detail':detail}]}))
sys.exit(0 if ok else 1)
"""
        source = self.root / "frozen-source"
        spec = _write_suite(source, rows, {"acceptance/python_cli.py":py})
        report = self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        self.assertTrue(report["passed"], report)
        self.assertEqual({row["status"] for row in report["case_results"]}, {"passed"})
        self.assertTrue((self.app / "main.py").read_text(encoding="utf-8").startswith("import argparse"))
        self.assertEqual(report["startup"]["status"], "passed")

    def test_total_timeout_removes_every_owned_container(self):
        runtime = self.make_web()
        source, spec = self.make_web_suite()
        self.verifier.timeout = 2
        with self.assertRaises(FactoryError) as caught:
            self.verifier.verify(self.app, source, spec, "P0", self.evidence, runtime)
        self.assertEqual(caught.exception.code, "verification_timeout")
        report = json.loads((self.evidence / "report.json").read_text(encoding="utf-8"))
        self.assertEqual(report["outcome"], "unavailable")
        self.assertTrue(report["cleanup"]["success"], report["cleanup"])
        self.assert_no_owned_containers()


if __name__ == "__main__":
    unittest.main()
