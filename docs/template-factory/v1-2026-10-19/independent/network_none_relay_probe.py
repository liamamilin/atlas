"""Synthetic stdlib relay probe against a preinstalled Python image; never product evidence."""
import http.client
import json
import threading
import time
import uuid

import docker_acceptance as runner

IMAGE = "docker.io/library/python:3.12-slim"
APP_PORT = 8765
APP_CODE = r'''from http.server import BaseHTTPRequestHandler,HTTPServer
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  b=b"ok"; self.send_response(200); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
 def do_POST(self):
  n=int(self.headers.get("Content-Length","0")); body=self.rfile.read(n)
  self.send_response(302); self.send_header("Location","http://127.0.0.1:5199/original"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
 def log_message(self,*a): pass
HTTPServer(("0.0.0.0",8765),H).serve_forever()
'''


def request(port, method, path, body=b""):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    try:
        conn.request(method, path, body=body, headers={"Content-Length": str(len(body))})
        response = conn.getresponse()
        return response.status, dict(response.getheaders()), response.read()
    finally:
        conn.close()


def main():
    image_id = runner.docker("image", "inspect", "--format", "{{.Id}}", IMAGE, timeout=10).stdout.strip()
    token = uuid.uuid4().hex[:12]
    name = "bookmark-relay-probe-" + token
    host_port = runner.free_port()
    server = None
    thread = None
    created = False
    result = {"classification": "synthetic relay capability probe; not application acceptance or evidence",
              "image": IMAGE, "image_id": image_id, "network_mode": "none", "published_ports": False}
    try:
        run = runner.docker("run", "--detach", "--network", "none", "--name", name,
                            IMAGE, "python3", "-u", "-c", APP_CODE, timeout=20)
        created = True
        result["container_id"] = run.stdout.strip()
        meta_before = runner.container_meta(name)
        runner.verify_network_none(meta_before)
        result["before"] = {"id": meta_before["id"], "started_at": meta_before["state"]["StartedAt"],
                             "network_mode": meta_before["network_mode"], "port_bindings": meta_before["port_bindings"],
                             "effective_ports": meta_before["effective_ports"], "networks": meta_before["networks"]}
        runner.AppRelay.container, runner.AppRelay.port = name, APP_PORT
        runner.AppRelay.log_message = lambda self, fmt, *args: None
        server = runner.ThreadingHTTPServer(("127.0.0.1", host_port), runner.AppRelay)
        server.daemon_threads = True
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        time.sleep(.5)
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            try:
                status, _, body = request(host_port, "GET", "/health")
                if status == 200 and body == b"ok":
                    break
            except OSError:
                pass
            time.sleep(.2)
        else:
            raise RuntimeError("relay did not reach synthetic server")
        status, _, body = request(host_port, "POST", "/redirect", b"synthetic-post-body")
        # This probe endpoint redirects; relay must return the response without following it.
        if status != 302 or body != b"synthetic-post-body":
            raise AssertionError(f"POST/302 passthrough mismatch: status={status}, body={body!r}")
        _, headers, _ = request(host_port, "POST", "/redirect", b"location-check")
        location = headers.get("Location") or headers.get("location")
        if location != "http://127.0.0.1:5199/original":
            raise AssertionError(f"relay changed redirect Location: {location!r}")
        result["relay_checks"] = {"get_200": True, "post_302_not_followed": True, "location_exact": location}
        runner.docker("restart", "--time", "1", name, timeout=15)
        meta_after = runner.container_meta(name)
        runner.verify_network_none(meta_after)
        if meta_before["id"] != meta_after["id"] or meta_before["state"]["StartedAt"] == meta_after["state"]["StartedAt"]:
            raise AssertionError("restart did not preserve container ID and change StartedAt")
        result["after"] = {"id": meta_after["id"], "started_at": meta_after["state"]["StartedAt"],
                            "network_mode": meta_after["network_mode"], "port_bindings": meta_after["port_bindings"],
                            "effective_ports": meta_after["effective_ports"], "networks": meta_after["networks"]}
        status, _, body = request(host_port, "GET", "/after-restart")
        if status != 200 or body != b"ok":
            raise AssertionError("relay failed after same-container restart")
        result["same_container_restart_and_relay_after_restart"] = True
    finally:
        if created:
            runner.docker("rm", "--force", name, check=False, timeout=15)
        if server is not None:
            server.shutdown()
            if not runner.AppRelay.wait_drained():
                result["relay_drained"] = False
            else:
                result["relay_drained"] = True
            server.server_close()
        if thread is not None:
            thread.join(timeout=3)
            result["relay_thread_stopped"] = not thread.is_alive()
        absent = runner.docker("inspect", name, check=False, timeout=10)
        result["container_absent"] = runner._docker_says_missing(absent)
    if not result.get("container_absent") or not result.get("relay_thread_stopped") or not result.get("relay_drained"):
        raise RuntimeError(f"probe cleanup failed: {result}")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
