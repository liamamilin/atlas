"""One authorized bookmark flow through the production factory; no publication."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PACK = ROOT / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))

from atlas_runtime import atomic_json
from template_factory.api import dispatch, get_store
from template_factory.cli import CLI
from template_factory.pipeline import Pipeline
from template_factory.worker import execute

MODEL = "commandcode/deepseek/deepseek-v4.1-flash"
SCENARIO = "scn_7756e0007f6a463a97316f3f49c15248"


class PilotCLI(CLI):
    def __init__(self, research_replay=None, review_replay=None):
        super().__init__()
        self.research_replay = research_replay
        self.review_replay = review_replay

    def run(self, directory, prompt, model, timeout, cancelled, progress, **kwargs):
        name = Path(directory).name
        path = self.research_replay if name == "blueprint-research" else self.review_replay if name == "cognitive-review" else None
        if path:
            raw = path.read_bytes()
            receipt = {"cli_status": "replayed_prior_response", "actual_model": None,
                       "requested_model": model, "source": str(path.relative_to(ROOT)),
                       "source_sha256": hashlib.sha256(raw).hexdigest(),
                       "scope": f"Unmodified failed {name} response reused for normal validation and bounded protocol repair; no new initial {name} call."}
            atomic_json(Path(directory) / "replay-receipt.json", receipt)
            atomic_json(Path(directory) / "cli-summary.json", receipt)
            return json.loads(raw)
        return super().run(directory, prompt, model, timeout, cancelled, progress,
                           reasoning_effort="high")


def save(name, value):
    atomic_json(HERE / name, value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["produce", "resume", "review", "export"])
    parser.add_argument("--review-replay", type=Path,
                        help="Replay this pilot's unmodified prior review result, then run normal validation and bounded citation repair")
    args = parser.parse_args()
    if args.review_replay and args.action != "review":
        raise SystemExit("Review replay is only valid for the review action")
    store = get_store()
    if args.action == "produce":
        if (HERE / "run.json").exists():
            raise SystemExit("Already initialized; inspect run.json and resume explicitly.")
        scenario = store.scenario(SCENARIO)
        save("scenario.json", scenario)
        batch = store.create_batch({
            "kind": "blueprint-production", "name": "书签端到端验证：三部分认知模板与独立验收",
            "model": MODEL, "language": "zh", "concurrency": 1, "timeout": 1200,
            "repair_attempts": 1, "scenario_ids": [SCENARIO],
            "scenario_revisions": {SCENARIO: scenario["revision"]},
            "acceptance_protocol": "atlas.acceptance-runner.v1",
            "cognition_guidance": (
                "本次是生活待购与灵感收藏夹的真实首阶段开发及验收。"
                "P0须覆盖保存链接、默认归类、独立创建归类、移动记录、按归类浏览、关键字检索、"
                "从真实页面打开原链接和应用进程重启后数据仍在的完整闭环；不要把必要步骤延后。"
                "推荐可离线运行的Python标准库HTTP服务+SQLite+服务端渲染HTML表单，"
                "真实普通用户可在浏览器完成全部核心操作，尽量无需JS/第三方依赖。"
                "首阶段是单人本地产品，登录/多人权限/云同步/计费不必强加，但成熟能力地图应判断适用性。"
                "架构明确路由、字段、错误与HTML交互约定、持久数据位置以及CLI启动端口和数据目录参数。"
                "应用源码只读独立验收，业务数据允许写/state；运行环境无外网。"
                "验收用例要按冻结runner逐例执行，真实验证用户操作和重要负例，"
                "能用HTTP驱动真实HTML表单完成的流程不要引入缺失的浏览器依赖；"
                "另有独立浏览器验收，不得把未执行的浏览器或重启过程写成已通过。"
                "模板自身不实现应用，不复制以往书签应用或测试源码。"
            ),
        })
        run = {"batch_id": batch["id"], "production_job_id": batch["jobs"][0]["id"],
               "model": MODEL, "reasoning_effort": "high", "scenario_id": SCENARIO,
               "scenario_revision": scenario["revision"], "publication": False,
               "implementation_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                          for p in (PACK / "template_factory").glob("*.py")},
               "authorization": "User requested fresh bookmark template production, OpenCode application development, independent agent acceptance and necessary scoped repairs; no credentials or unrelated project data."}
        save("run.json", run)
    else:
        run = json.loads((HERE / "run.json").read_text())
    prior_research = store.root / "jobs" / run["production_job_id"] / "attempt-1/blueprint-research/result.json"
    replay = prior_research if args.action == "resume" and prior_research.is_file() and store.checkpoint(run["production_job_id"], "blueprint-research-response") is None else None
    if args.review_replay:
        expected = store.root / "jobs/job_2f2cf28525d04a019cc99a897e1492c6/attempt-1/cognitive-review/result.json"
        if args.review_replay.resolve() != expected.resolve():
            raise SystemExit("Replay is restricted to this pilot's preserved failed review response")
    pipeline = Pipeline(store, cli=PilotCLI(research_replay=replay, review_replay=args.review_replay))
    target = run["production_job_id"]
    if args.action == "export":
        artifacts = [a for a in store.artifacts() if a["job_id"] == target]
        if len(artifacts) != 1:
            raise SystemExit("Expected one frozen candidate before export")
        artifact = artifacts[0]
        reviews = [r for r in artifact["acceptances"] if r["method"] == "cognitive-review"]
        if not reviews or reviews[0]["outcome"] not in {"passed", "uncertain"}:
            raise SystemExit("Resolve blocking/incomplete cognition review before development")
        package, status = dispatch("POST", f"/api/factory/artifacts/{artifact['id']}/development-package", body={
            "expected_digest": artifact["digest"], "project_name": "bookmark-life-p0", "phase": "P0",
        }, store=store)
        path, _, _ = dispatch("GET", package["download_url"], store=store)
        target_zip = HERE / "development-package.zip"
        if target_zip.exists() and target_zip.read_bytes() != path.read_bytes():
            raise SystemExit("Do not overwrite an existing export with different bytes")
        shutil.copyfile(path, target_zip)
        shutil.copyfile(store.root / artifact["archive_path"], HERE / "cognitive-template.zip")
        run.update(artifact_id=artifact["id"], artifact_digest=artifact["digest"], bundle_path=artifact["bundle_path"],
                   package_sha256=hashlib.sha256(target_zip.read_bytes()).hexdigest())
        save("run.json", run)
        save("export-result.json", {"status": status, "export": package, "cognition_review": reviews[0],
                                    "scope": "Frozen original and current-phase development package; no application execution or publication."})
        print(json.dumps({"event": "exported", "artifact_id": artifact["id"], "package": str(target_zip)}), flush=True)
        return
    if args.action == "review":
        candidates = [a for a in store.artifacts() if a["job_id"] == target]
        if not candidates:
            raise SystemExit("No frozen artifact yet")
        target = next(j["id"] for j in candidates[0]["acceptance_jobs"] if j["kind"] == "cognitive-review" and j["state"] == "queued")
    selected = store.job(target)
    if selected["state"] != "queued":
        raise SystemExit("Inspect target before retry: " + selected["state"])
    lane = "verification" if args.action == "review" else "production"
    with store.connect() as con:
        rows = con.execute("SELECT id FROM job WHERE state='queued' AND kind " +
                           ("IN ('harness-review','runtime-verification','scenario-review','cognitive-review','blueprint-runtime')" if lane == "verification" else "NOT IN ('harness-review','runtime-verification','scenario-review','cognitive-review','blueprint-runtime')") + " ORDER BY created_at").fetchall()
        if not rows or rows[0]["id"] != target:
            raise SystemExit("Target is not the next scoped job; do not claim another task")
    job = store.claim("bookmark-end-to-end-operator", lane)
    if not job or job["id"] != target:
        raise SystemExit("Unexpected claim; stop rather than execute unrelated work")
    print(json.dumps({"event": "started", "job_id": target, "kind": job["kind"]}), flush=True)
    execute(store, job, pipeline)
    state = store.job(target)
    result = {"job_id": target, "state": state["state"], "stage": state["stage"], "error": state["error"],
              "artifacts": [{"id": a["id"], "digest": a["digest"], "bundle_path": a["bundle_path"], "archive_path": a["archive_path"]}
                            for a in store.artifacts() if a["job_id"] == run["production_job_id"]]}
    save(args.action + "-attempt-" + str(state["attempt"]) + "-result.json", result)
    save(args.action + "-result.json", result)
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
