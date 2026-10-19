"""Post-hoc HTTP security/concurrency probes for the frozen bookmark bundle.

This is deliberately separate from the frozen UI acceptance. It runs only against
an isolated Docker container and never follows redirects to external origins.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import threading
import time
import uuid
from urllib.parse import urlencode, quote
from http.client import HTTPConnection

import docker_ui_acceptance as runner


class BookmarkHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.collections = []
        self.bookmarks = []
        self.li_stack = []
        self.current_anchor = None
        self.raw_html = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "li":
            record = None
            classes = set(attrs.get("class", "").split())
            if "collection" in classes or "bookmark" in classes:
                record = {"attrs": attrs, "text": [], "anchors": []}
            self.li_stack.append(record)
        elif tag == "a" and any(item is not None for item in self.li_stack):
            self.current_anchor = {"attrs": attrs, "text": []}
            next(item for item in reversed(self.li_stack) if item is not None)["anchors"].append(self.current_anchor)

    def handle_data(self, data):
        for item in self.li_stack:
            if item is not None:
                item["text"].append(data)
        if self.current_anchor is not None:
            self.current_anchor["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "a":
            self.current_anchor = None
        elif tag == "li" and self.li_stack:
            item = self.li_stack.pop()
            if item is not None:
                item["text"] = "".join(item["text"]).strip()
                item["anchors"] = [
                {"href": a["attrs"].get("href", ""), "text": "".join(a["text"]).strip()}
                    for a in item["anchors"]
                ]
                classes = set(item["attrs"].get("class", "").split())
                if "collection" in classes:
                    self.collections.append(item)
                elif "bookmark" in classes:
                    self.bookmarks.append(item)
            if not self.li_stack:
                self.current_anchor = None


def request(base_url, method="GET", path="/", fields=None):
    from urllib.parse import urlsplit
    parsed = urlsplit(base_url)
    body = urlencode(fields or {}) if method == "POST" else None
    headers = {}
    if body is not None:
        body = body.encode("utf-8")
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Content-Length": str(len(body))}
    conn = HTTPConnection(parsed.hostname, parsed.port, timeout=6)
    try:
        conn.request(method, path, body=body, headers=headers)
        response = conn.getresponse()
        payload = response.read()
        return {
            "status": response.status,
            "reason": response.reason,
            "headers": list(response.getheaders()),
            "body": payload,
        }
    finally:
        conn.close()


def get_library(base_url, query=""):
    path = "/" if not query else "/?q=" + quote(query, safe="")
    response = request(base_url, path=path)
    if response["status"] != 200:
        raise RuntimeError(f"library GET returned {response['status']}")
    parser = BookmarkHTML()
    parser.raw_html = response["body"].decode("utf-8", "replace")
    parser.feed(parser.raw_html)
    return parser


def post(base_url, path, fields):
    result = request(base_url, "POST", path, fields)
    result.pop("body", None)
    result["location"] = next((v for k, v in result["headers"] if k.lower() == "location"), None)
    result["header_names"] = [k for k, _ in result["headers"]]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True, type=Path)
    parser.add_argument("--evidence-dir", required=True, type=Path)
    parser.add_argument("--image", default=runner.IMAGE_DEFAULT)
    parser.add_argument("--concurrency-rounds", type=int, default=20)
    args = parser.parse_args()
    if args.concurrency_rounds < 2 or args.concurrency_rounds > 100:
        raise SystemExit("concurrency rounds must be between 2 and 100")
    evidence = args.evidence_dir.resolve()
    if evidence.exists():
        raise SystemExit(f"evidence directory already exists; refusing overwrite: {evidence}")
    evidence.mkdir(parents=True)
    temp_root = Path(__import__("tempfile").gettempdir()) / f"bookmark-posthoc-{uuid.uuid4().hex}"
    source_root = temp_root / "verified-application"
    data_dir = temp_root / "state"
    token = uuid.uuid4().hex
    network = f"bookmark-posthoc-net-{token[:12]}"
    container = f"bookmark-posthoc-app-{token[:12]}"
    host_port = runner.free_port()
    base_url = f"http://127.0.0.1:{host_port}"
    network_attempted = False
    container_attempted = False
    fixture = None
    fixture_thread = None
    report = {
        "schema": "atlas.bookmark-posthoc-http-probes.v1",
        "kind": "post-hoc-independent-exploration",
        "status": "running",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "evidence_dir": str(evidence),
        "runner_command": ["python3", str(Path(__file__).resolve()), *os.sys.argv[1:]],
        "bundle_dir": str(args.bundle.resolve()),
        "image": args.image,
        "base_url": base_url,
        "network_mode": "dedicated user-defined bridge; egress not enforced",
        "network_none": False,
        "owned_resources": {
            "temporary_root": {"path": str(temp_root), "state": "planned"},
            "network": {"name": network, "state": "planned"},
            "container": {"name": container, "state": "planned"},
            "fixture_server": {"state": "not-used"},
            "fixture_thread": {"state": "not-used"},
        },
        "docker_commands": {
            "network_create": ["docker", "network", "create", network],
            "container_cleanup": ["docker", "rm", "--force", container],
            "network_cleanup": ["docker", "network", "rm", network],
            "container_run_plan": {
                "name": container, "image": args.image,
                "host_publish": f"127.0.0.1:{host_port}:<delivery.runtime.port>",
                "source_mount": f"{source_root}:/app:readonly", "state_mount": f"{data_dir}:/state",
                "runtime_argv": "<verified delivery.json runtime.start>",
            },
        },
        "limitations": ["No browser is used for these post-hoc probes.", "Docker bridge egress is not blocked; probe requests target only 127.0.0.1."],
    }

    def persist():
        report["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        runner.atomic_write_json(evidence / "run.json", report)

    def stage(name):
        report["stage"] = name
        report.setdefault("stage_events", []).append({"stage": name, "state": "started", "at": time.time()})
        persist()

    def done(name, details=None):
        report.setdefault("stage_events", []).append({"stage": name, "state": "completed", "at": time.time(), "details": details or {}})
        persist()

    persist()  # Resource names and commands are durable before any owned resource is created.
    try:
        stage("bundle_verification")
        temp_root.mkdir(mode=0o700)
        data_dir.mkdir(parents=True)
        data_dir.chmod(0o777)
        bundle_info = runner.unpack_verified_bundle(args.bundle, source_root)
        delivery, start_argv, container_port, app_root, data_argument, readiness = runner.read_delivery(source_root / "delivery.json")
        report["bundle"] = bundle_info
        report["delivery_runtime_start_argv"] = start_argv
        report["data_dir_argument"] = data_argument
        report["readiness_path"] = readiness
        report["app_source_sha256_before"] = runner.source_hashes(app_root)
        report["docker_commands"]["container_run_plan"]["runtime_argv"] = start_argv
        report["docker_commands"]["container_run_plan"]["host_publish"] = f"127.0.0.1:{host_port}:{container_port}"
        done("bundle_verification", {"archive_sha256": bundle_info["archive_sha256"]})

        stage("docker_preflight")
        runner.docker("info", timeout=10)
        image_id = runner.docker("image", "inspect", "--format", "{{.Id}}", args.image, timeout=10).stdout.strip()
        report["image_id"] = image_id
        done("docker_preflight", {"image_id": image_id})

        stage("network_setup")
        network_attempted = True
        report["owned_resources"]["network"]["state"] = "creation-attempted"
        persist()
        runner.docker("network", "create", network, timeout=15)
        report["owned_resources"]["network"]["state"] = "created"
        done("network_setup")

        stage("container_start")
        container_attempted = True
        report["owned_resources"]["container"]["state"] = "creation-attempted"
        persist()
        start_result = runner.docker(
            "run", "--detach", "--read-only", "--tmpfs", "/tmp:rw,nosuid,nodev",
            "--cap-drop", "ALL", "--security-opt", "no-new-privileges:true",
            "--memory", "256m", "--cpus", "0.5", "--pids-limit", "64",
            "--user", f"{os.getuid()}:{os.getgid()}", "--workdir", "/app",
            "--mount", f"type=bind,src={app_root},dst=/app,readonly",
            "--mount", f"type=bind,src={data_dir},dst=/state",
            "--network", network, "--publish", f"127.0.0.1:{host_port}:{container_port}",
            "--env", "PYTHONDONTWRITEBYTECODE=1", "--env", "PYTHONUNBUFFERED=1",
            "--name", container, args.image, *start_argv, timeout=30,
        )
        report["container_id"] = start_result.stdout.strip()
        report["owned_resources"]["container"]["state"] = "created"
        report["container_settings"] = runner.container_meta(container)
        ready_url = base_url + readiness
        runner.wait_ready(ready_url, container, timeout=30)
        done("container_start", {"container_id": report["container_id"], "readiness_url": ready_url})

        stage("crlf_url_probe")
        probe_id = "crlf-" + token[:12]
        baseline = get_library(base_url)
        runner.atomic_write_text(evidence / "inventory-before.html", baseline.raw_html)
        # Verify parser semantics against the app's rendered, known-unique collection
        # before treating any post-hoc measurement as product evidence.
        crosscheck_name = f"Parser inventory {token[:8]}"
        crosscheck_post = post(base_url, "/collections", {"name": crosscheck_name})
        crosscheck = get_library(base_url)
        runner.atomic_write_text(evidence / "inventory-parser-crosscheck.html", crosscheck.raw_html)
        crosscheck_rows = [item for item in crosscheck.collections if crosscheck_name in item["text"]]
        if crosscheck_post["status"] != 303 or len(crosscheck_rows) != 1:
            raise RuntimeError("actual app HTML inventory parser cross-check failed")
        report["html_inventory_parser_crosscheck"] = {
            "post_status": crosscheck_post["status"], "expected_name": crosscheck_name,
            "matching_collection_count": len(crosscheck_rows),
            "matching_collection_id": crosscheck_rows[0]["attrs"].get("data-collection-id"),
            "unique_collection_ids": sorted({item["attrs"].get("data-collection-id", "") for item in crosscheck.collections}),
            "html_snapshot": "inventory-parser-crosscheck.html",
        }
        baseline = crosscheck
        baseline_ids = sorted({item["attrs"].get("data-bookmark-id", "") for item in baseline.bookmarks})
        baseline_categories = sorted({item["attrs"].get("data-collection-id", "") for item in baseline.collections})
        injected_header = "X-Codex-Probe"
        payload_url = f"http://example.invalid/path\r\n{injected_header}: injected-{token[:8]}"
        crlf_response = post(base_url, "/bookmarks", {
            "url": payload_url, "title": f"Posthoc CRLF probe {probe_id}",
        })
        after_crlf = get_library(base_url)
        runner.atomic_write_text(evidence / "inventory-after-crlf.html", after_crlf.raw_html)
        after_ids = sorted({item["attrs"].get("data-bookmark-id", "") for item in after_crlf.bookmarks})
        after_categories = sorted({item["attrs"].get("data-collection-id", "") for item in after_crlf.collections})
        matching_crlf_rows = [item for item in after_crlf.bookmarks if probe_id in item["text"]]
        crlf = {
            "payload": {"url_encoded": urlencode({"url": payload_url})[4:]},
            "post_response": crlf_response,
            "rejected_4xx": 400 <= crlf_response["status"] < 500,
            "inventory_unchanged": baseline_ids == after_ids and baseline_categories == after_categories,
            "baseline_bookmark_ids": baseline_ids,
            "after_bookmark_ids": after_ids,
            "baseline_collection_ids": baseline_categories,
            "after_collection_ids": after_categories,
            "redirect_header_probe": {"status": "not_applicable_rejected"},
            "matching_bookmark_rows": [{
                "id": item["attrs"].get("data-bookmark-id"),
                "classes": item["attrs"].get("class", ""),
                "text": item["text"], "anchors": item["anchors"],
            } for item in matching_crlf_rows],
            "html_snapshot": "inventory-after-crlf.html",
        }
        if crlf_response["status"] < 400:
            row = matching_crlf_rows[0] if matching_crlf_rows else None
            if row:
                bookmark_id = row["attrs"].get("data-bookmark-id")
                go_response = request(base_url, path=f"/go/{quote(bookmark_id, safe='')}")
                go_headers = [(key, value) for key, value in go_response["headers"]]
                injected = [(key, value) for key, value in go_headers if key.lower() == injected_header.lower()]
                crlf["redirect_header_probe"] = {
                    "path": f"/go/{bookmark_id}", "status": go_response["status"],
                    "headers": go_headers, "injected_header_present": bool(injected),
                    "location": next((value for key, value in go_headers if key.lower() == "location"), None),
                }
            else:
                crlf["redirect_header_probe"] = {"status": "record_not_found_after_303"}
        crlf["pass"] = crlf["rejected_4xx"] and crlf["inventory_unchanged"] and not crlf["redirect_header_probe"].get("injected_header_present", False)
        report["crlf_probe"] = crlf
        done("crlf_url_probe", {"pass": crlf["pass"], "status": crlf_response["status"]})

        stage("concurrent_category_probe")
        rounds = []
        for index in range(args.concurrency_rounds):
            name = f"Concurrent {token[:8]} {index:02d}"
            barrier = threading.Barrier(2)
            def send_concurrent():
                barrier.wait(timeout=5)
                return post(base_url, "/collections", {"name": name})
            with ThreadPoolExecutor(max_workers=2) as executor:
                futures = [executor.submit(send_concurrent) for _ in range(2)]
                responses, errors = [], []
                for future in futures:
                    try:
                        responses.append(future.result(timeout=10))
                    except Exception as exc:
                        errors.append(repr(exc))
            after = get_library(base_url)
            snapshot_path = evidence / f"inventory-concurrent-{index + 1:02d}.html"
            runner.atomic_write_text(snapshot_path, after.raw_html)
            exact = [item for item in after.collections if name in item["text"]]
            exact_ids = sorted({item["attrs"].get("data-collection-id", "") for item in exact})
            statuses = [response["status"] for response in responses]
            successful = sum(status == 303 for status in statuses)
            rounds.append({
                "round": index + 1, "name": name, "responses": responses, "errors": errors,
                "status_codes": statuses, "successful_303_count": successful,
                "matching_collection_count": len(exact_ids), "matching_collection_ids": exact_ids,
                "matching_collection_texts": [item["text"] for item in exact],
                "html_snapshot": snapshot_path.name,
                "successful_303_name_persisted": successful == 0 or len(exact_ids) >= 1,
                "no_500": 500 not in statuses,
            })
            report["concurrent_category_probe"] = {
                "rounds_requested": args.concurrency_rounds, "rounds_completed": len(rounds), "observations": rounds,
            }
            persist()
        report["concurrent_category_probe"]["pass"] = all(
            item["no_500"] and item["successful_303_name_persisted"] and not item["errors"]
            for item in rounds
        )
        done("concurrent_category_probe", {"pass": report["concurrent_category_probe"]["pass"], "rounds": len(rounds)})
        stage("post_probe_server_logs")
        logs = runner.docker("logs", "--tail", "500", container, check=False, timeout=10)
        report["server_logs"] = {"returncode": logs.returncode, "stdout": logs.stdout, "stderr": logs.stderr}
        done("post_probe_server_logs", {"returncode": logs.returncode, "stdout_chars": len(logs.stdout), "stderr_chars": len(logs.stderr)})

        stage("source_integrity")
        report["app_source_sha256_after"] = runner.source_hashes(app_root)
        report["source_hash_unchanged"] = report["app_source_sha256_before"] == report["app_source_sha256_after"]
        report["result"] = {
            "crlf_url_rejected_without_dirty_data": crlf["pass"],
            "concurrent_same_name_categories_no_500_and_success_persists": report["concurrent_category_probe"]["pass"],
        }
        report["status"] = "completed"
        done("source_integrity", {"unchanged": report["source_hash_unchanged"]})
    except BaseException as exc:
        report["failure_stage"] = report.get("stage")
        if isinstance(exc, KeyboardInterrupt):
            report["status"] = "interrupted"
            report["failure_kind"] = "operator_interruption"
        else:
            report["status"] = "blocked" if isinstance(exc, (FileNotFoundError, TimeoutError, runner.DockerCommandTimeout)) else "failed"
            report["failure_kind"] = "environment_or_readiness" if report["status"] == "blocked" else "probe_harness_failure"
        report["error"] = repr(exc)
        persist()
    finally:
        report["stage"] = "cleanup"
        persist()
        report["cleanup"] = runner.cleanup_resources(
            report, persist, container=container, network=network, temp_root=temp_root,
            container_attempted=container_attempted, network_attempted=network_attempted,
            fixture=fixture, fixture_thread=fixture_thread,
        )
        if not report["cleanup"].get("all_resources_removed"):
            report["cleanup_failure"] = True
        report["completed_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        persist()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "completed" or not report.get("cleanup", {}).get("all_resources_removed"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
