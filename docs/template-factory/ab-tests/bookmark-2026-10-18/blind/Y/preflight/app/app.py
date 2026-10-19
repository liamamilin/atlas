"""生活待购与灵感收藏夹 —— 本地单实例书签库。

用法：
    python3 app.py --port PORT --data-dir DIR

只绑定 127.0.0.1，所有持久数据都写在 DIR 内。
"""

import argparse
import os
import sys
import uuid
from datetime import datetime, timezone
from http.server import ThreadingHTTPServer
from urllib.parse import urlsplit

import db
from server import AppHandler
from store import Store

DEFAULT_PORTS = {"http": 80, "https": 443}


class Config(object):
    def __init__(self, origin, base_path, data_dir, stage, quiet):
        parts = urlsplit(origin)
        self.scheme = parts.scheme.lower()
        self.hostname = (parts.hostname or "").lower()
        self.port = parts.port
        default_port = DEFAULT_PORTS.get(self.scheme)
        if self.port is None or self.port == default_port:
            self.authority = self.hostname
            port_text = ""
        else:
            self.authority = "%s:%d" % (self.hostname, self.port)
            port_text = ":%d" % self.port
        self.origin = "%s://%s%s" % (self.scheme, self.hostname, port_text)
        self.base_path = base_path
        self.data_dir = data_dir
        self.stage = stage
        self.quiet = quiet
        self.instance_id = str(uuid.uuid4())
        self.started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        self.store = None


def normalize_base_path(raw):
    text = (raw or "").strip()
    if text == "" or text == "/":
        return ""
    if not text.startswith("/"):
        text = "/" + text
    while len(text) > 1 and text.endswith("/"):
        text = text[:-1]
    return text


def build_origin(raw, port):
    if raw:
        text = raw.strip().rstrip("/")
    else:
        text = "http://127.0.0.1:%d" % port
    parts = urlsplit(text)
    if parts.scheme not in ("http", "https") or not parts.hostname or parts.username or parts.password:
        raise SystemExit("PUBLIC_ORIGIN 配置无效：%s" % raw)
    return text


def parse_args(argv):
    parser = argparse.ArgumentParser(description="生活待购与灵感收藏夹（本地书签库）")
    parser.add_argument("--port", type=int, default=3000)
    parser.add_argument("--data-dir", default=os.path.join(os.getcwd(), "data"))
    parser.add_argument("--public-origin", default=None)
    parser.add_argument("--public-base-path", default=None)
    parser.add_argument("--stage", default="P2")
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.port < 1 or args.port > 65535:
        raise SystemExit("--port 必须是 1–65535")

    origin_raw = args.public_origin or os.environ.get("PUBLIC_ORIGIN")
    origin = build_origin(origin_raw, args.port)

    base_raw = args.public_base_path
    if base_raw is None:
        base_raw = os.environ.get("PUBLIC_BASE_PATH")
    base_path = normalize_base_path(base_raw)

    data_dir = os.path.abspath(args.data_dir)
    conn = db.open_database(data_dir)
    config = Config(origin, base_path, data_dir, args.stage, args.quiet)
    config.store = Store(conn)

    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), AppHandler)
    httpd.daemon_threads = True
    httpd.allow_reuse_address = True
    httpd.config = config
    httpd.quiet = args.quiet

    sys.stderr.write(
        "书签库已启动：http://127.0.0.1:%d%s\n数据目录：%s\nschema 版本：%d\n"
        % (args.port, base_path, data_dir, db.SCHEMA_VERSION)
    )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        conn.close()


if __name__ == "__main__":
    main()
