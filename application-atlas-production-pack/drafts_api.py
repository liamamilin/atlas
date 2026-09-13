#!/usr/bin/env python3
"""Draft-leaf API server (local, stdlib only).

  python3 drafts_api.py [--port 5199]

Endpoints:
  GET    /api/health
  GET    /api/drafts                     list drafts (frontmatter + lint_ok)
  POST   /api/drafts                     create + start engine in background
                                         body: {name?, name_zh?, desc?, link?, force?}
                                         name 留空 -> 临时 wip-slug，引擎调研后在 identity.json 定名
  GET    /api/drafts/<slug>              {front, body, research, lint, collision}
  PUT    /api/drafts/<slug>              save body   {body}
  DELETE /api/drafts/<slug>              delete draft + research files
  POST   /api/dedupe                     {slug} -> vector top-5 stored in review.json
  GET    /api/review                     full review.json

Run alongside `npm run dev` (vite proxies /api -> :5199).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, unquote

from atlas_runtime import PACK as DATA_PACK, api_key, atomic_write, corpus_lock, recover_publication
from review_store import load_review, update_review, fingerprint, corpus_revision, review_current, valid_slug
PACK = str(DATA_PACK)
sys.path.insert(0, PACK)
from leaf_lint import lint, parse_front
import draft_new as dn

DRAFTS = os.path.join(PACK, "drafts")
PROMPT = os.path.join(PACK, "drafts_prompt.md")
WORKDIR = os.path.dirname(PACK)
REVIEW = os.path.join(DRAFTS, "review.json")

GEN_LOCK = threading.Semaphore(2)          # max concurrent engine runs
GEN_THREADS = {}
PROMOTE_LOCK = threading.Lock()
PROMOTE_THREADS = set()

# ---- 模型生成身份（英文名/中文名/一句话想法，创建时 name/desc 可不填） ----
ID_MODEL = os.environ.get("ATLAS_DEDUP_MODEL", "mimo-v2.5")
ID_PROMPT = """你是软件类型语料库的编辑。根据用户提供的信息，为新软件类型起名并概括主张。

用户输入:
- 一句话想法: {desc}
- 调研起点链接: {link}
{extra}

要求:
- name: 英文类型名，2-5 个单词 Title Case（如 CLI Accounting Tool），指类别而非具体产品
- name_zh: 中文名，不超过 12 个汉字
- desc: 一句话中文主张，含「形态+核心机制+边界说明」，风格如「单机命令行复式记账工具（ledger/hledger 一类：纯文本账本、无 GUI）」，不超过 60 字

只输出 JSON: {{"name":"...","name_zh":"...","desc":"..."}}"""


def _fetch_text(url, n=3000):
    raw = urllib.request.urlopen(urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 atlas-identity/1.0"}), timeout=20).read(200000)
    txt = re.sub(r"<script.*?</script>|<style.*?</style>", " ",
                 raw.decode("utf-8", "ignore"), flags=re.S | re.I)
    txt = re.sub(r"<[^>]+>", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()[:n]


def gen_identity(desc, link):
    """desc/link 至少一个非空 -> {name,name_zh,desc} 或 {error}"""
    extra = ""
    if link and not desc:
        try:
            extra = "\n链接页面内容摘录:\n" + _fetch_text(link)
        except Exception as e:
            extra = f"\n（链接抓取失败: {e}）"
    body_msg = {"model": ID_MODEL,
                "messages": [{"role": "user", "content": ID_PROMPT.format(
                    desc=desc or "（无）", link=link or "（无）", extra=extra)}],
                "temperature": 0.3, "max_tokens": 3000}
    try:
        key = api_key()
        r = json.load(urllib.request.urlopen(urllib.request.Request(
            "https://opencode.ai/zen/go/v1/chat/completions", json.dumps(body_msg).encode(),
            {"Authorization": f"Bearer {key}", "Content-Type": "application/json",
             "x-opencode-session": "atlas-identity", "User-Agent": "atlas-identity/1.0"}),
            timeout=300))
        msg = r["choices"][0]["message"]
        txt = (msg.get("content") or "").strip()
        if not txt and msg.get("reasoning"):
            txt = str(msg["reasoning"]).strip()
        m = re.search(r"\{.*\}", txt, re.S)
        out = json.loads(m.group(0)) if m else {}
        name = str(out.get("name", "")).strip()
        name_zh = str(out.get("name_zh", "")).strip()
        d = str(out.get("desc", "")).strip()
        if not name or not d:
            return {"error": f"模型未能生成有效身份: {txt[:200]}"}
        return {"name": name, "name_zh": name_zh, "desc": d}
    except Exception as e:
        return {"error": f"身份生成失败: {e}"}


def draft_path(slug):
    return os.path.join(DRAFTS, valid_slug(slug) + ".md")


def list_drafts():
    out = []
    rv_all = load_review(PACK)
    for f in sorted(os.listdir(DRAFTS)):
        if not f.endswith(".md") or f.endswith(".research.md") or \
                f.endswith(".body.md") or f.endswith(".zh.md"):
            continue
        p = os.path.join(DRAFTS, f)
        front, body = parse_front(open(p, encoding="utf-8").read())
        r = lint(p)
        out.append({"slug": front.get("slug", f[:-3]), "name": front.get("name", ""),
                    "name_zh": front.get("name_zh", ""), "status": front.get("status", "?"),
                    "created": front.get("created", ""), "engine": front.get("engine", ""),
                    "size": r["size"], "lint_ok": r["ok"], "lint_errors": len(r["errors"]),
                    "dup": _dup_info(rv_all.get(front.get("slug", f[:-3]), {}))})
    return out


def _dup_info(rv):
    ident = rv.get("identity") or {}
    if ident.get("verdict") in ("same", "variant"):
        return {"verdict": ident["verdict"], "best": ident.get("best")}
    return None


def draft_progress(slug):
    """Live generation signals from files the engine writes as it works."""
    out = {"body_chars": 0, "research_chars": 0, "last_h2": "", "sections_done": 0,
           "log_tail": [], "updated_at": 0}
    bp = os.path.join(DRAFTS, slug + ".body.md")
    rp = os.path.join(DRAFTS, slug + ".research.md")
    lp = os.path.join(DRAFTS, slug + ".opencode.log")
    if os.path.exists(rp):
        out["research_chars"] = os.path.getsize(rp)
    if os.path.exists(bp):
        out["body_chars"] = os.path.getsize(bp)
        out["updated_at"] = int(os.path.getmtime(bp))
        hs = re.findall(r"^## (.+)$", open(bp, encoding="utf-8", errors="ignore").read(), re.M)
        out["sections_done"] = len(hs)
        if hs:
            out["last_h2"] = hs[-1].strip()
    if os.path.exists(lp):
        raw = re.sub(r"\x1b\[[0-9;]*m", "", open(lp, "rb").read()[-3000:].decode("utf-8", "ignore"))
        out["log_tail"] = [l.strip() for l in raw.splitlines() if l.strip()][-6:]
    return out


def read_draft(slug):
    p = draft_path(slug)
    if not os.path.exists(p):
        return None
    text = open(p, encoding="utf-8").read()
    front, body = parse_front(text)
    rp = os.path.join(DRAFTS, slug + ".research.md")
    research = open(rp, encoding="utf-8").read() if os.path.exists(rp) else None
    rzp = os.path.join(DRAFTS, slug + ".research.zh.md")
    research_zh = open(rzp, encoding="utf-8").read() if os.path.exists(rzp) else None
    zh = None
    zp = os.path.join(DRAFTS, slug + ".zh.json")
    if os.path.exists(zp):
        try:
            zh = json.load(open(zp, encoding="utf-8"))
        except Exception:
            zh = None
    rv = load_review(PACK).get(slug, {})
    ident = rv.get("identity") or {}
    if ident.get("verdict") in ("same", "variant") and not rv.get("verdict"):
        rv = {**rv, "verdict": ident["verdict"], "best": ident.get("best"),
              "reason": ident.get("reason")}
    top = rv.get("top") or rv.get("collision") or []
    return {"slug": slug, "front": front, "body": body, "research": research,
            "research_zh": research_zh, "zh": zh,
            "lint": lint(p), "collision": top or [],
            "review": {**rv, "current": review_current(slug, rv, PACK)}, "progress": draft_progress(slug)}


def list_sections():
    import sqlite3
    con = sqlite3.connect(os.path.join(PACK, "atlas", "atlas.sqlite"))
    rows = con.execute(
        "SELECT id, name, name_zh FROM section WHERE parent != '' ORDER BY id").fetchall()
    con.close()
    return [{"id": r[0], "name": r[1], "name_zh": r[2]} for r in rows]


ZH_SRC = [("overview", ("overview",)), ("how", ("how it works",)),
          ("rules", ("important rules", "rules")), ("variants", ("variants",)),
          ("products", ("representative products", "products"))]
ZH_TRUNC = {"overview": 4000, "how": 2500, "rules": 1800, "variants": 2500, "products": 1800}


RESEARCH_PROMPT = """把下面的软件类型「边界发现/不确定性」调研文档翻译成中文。
要求:
- 保留 Markdown 结构（## / ### 标题、列表、粗体、表格）
- 类型名、产品名、leaf slug 保留英文；证据等级标记（A/B/C）原样保留
- 只输出译文正文，不要任何解释

{research}"""


def translate_research(slug):
    rp = os.path.join(DRAFTS, slug + ".research.md")
    if not os.path.exists(rp):
        return False
    research = open(rp, encoding="utf-8").read()
    key = api_key()
    body_msg = {"model": ID_MODEL,
                "messages": [{"role": "user",
                              "content": RESEARCH_PROMPT.format(research=research)}],
                "temperature": 0.1, "max_tokens": 8000}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "https://opencode.ai/zen/go/v1/chat/completions", json.dumps(body_msg).encode(),
        {"Authorization": f"Bearer {key}", "Content-Type": "application/json",
         "x-opencode-session": "atlas-translate-research",
         "User-Agent": "atlas-translate/1.0"}), timeout=600))
    msg = r["choices"][0]["message"]
    txt = (msg.get("content") or "").strip()
    if not txt and msg.get("reasoning"):
        txt = str(msg["reasoning"]).strip()
    if not txt:
        raise RuntimeError("empty translation")
    txt = re.sub(r"^```[a-zA-Z]*\s*", "", txt)
    txt = re.sub(r"\s*```\s*$", "", txt)
    open(os.path.join(DRAFTS, slug + ".research.zh.md"), "w", encoding="utf-8").write(txt)
    return True


def translate_draft(slug):
    """Generate zh preview (5 key fields) via the corpus translation pipeline."""
    front, body = parse_front(open(draft_path(slug), encoding="utf-8").read())
    import re as _re
    parts = _re.split(r"^##\s+(.+)$", body, flags=_re.M)
    sections = {parts[i].strip().lower(): parts[i + 1]
                for i in range(1, len(parts) - 1, 2)}

    def grab(*names):
        for n in names:
            for k, v in sections.items():
                if k.startswith(n):
                    return v
        return ""

    from translate_bodies import call_api, PROMPT, parse_out
    fields = {k: grab(*names).strip() for k, names in ZH_SRC}
    payload = json.dumps({k: fields[k][:ZH_TRUNC[k]] for k in fields}, ensure_ascii=False)
    zh = parse_out(call_api(PROMPT.format(json=payload)))
    zh["slug"] = slug
    zh["engine"] = "api"
    try:
        zh["research_zh"] = bool(translate_research(slug))
    except Exception as e:
        zh["research_zh"] = False
        zh["research_zh_error"] = str(e)
    json.dump(zh, open(os.path.join(DRAFTS, slug + ".zh.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return zh


def run_promote(slug, action, kw):
    try:
        import promote_draft as pd
        pd.promote(slug, action, kw["section"] if action == "new" else kw["into"])
    except Exception as error:
        update_review(slug, {"promote_error": str(error)}, PACK)
        if os.path.exists(draft_path(slug)):
            dn.refresh_front(slug, "draft")
    finally:
        PROMOTE_THREADS.discard(slug)
        PROMOTE_LOCK.release()


def save_body(slug, body):
    p = draft_path(slug)
    if not os.path.exists(p):
        return False
    text = open(p, encoding="utf-8").read()
    m = re.match(r"\A---\n.*?\n---\n", text, re.S)
    atomic_write(p, (m.group(0) if m else "") + body)
    return True


def apply_identity(slug):
    """引擎完成后：读 identity.json 定名/裁决。返回非 None 表示查重失败，勿再翻译。"""
    ip = os.path.join(DRAFTS, slug + ".identity.json")
    ident = {}
    if os.path.exists(ip):
        try:
            ident = json.load(open(ip, encoding="utf-8"))
        except Exception:
            ident = {}
    if ident.get("verdict") in ("same", "variant"):
        update_review(slug, {"identity": ident}, PACK)
        dn.refresh_front(slug, "failed",
                         extra=f"dedupe: 引擎调研判定 {ident.get('verdict')} / {ident.get('best')}: "
                               f"{ident.get('reason', '')[:120]}")
        if os.path.exists(ip):
            os.remove(ip)
        return ident
    front, _ = parse_front(open(draft_path(slug), encoding="utf-8").read())
    text = open(draft_path(slug), encoding="utf-8").read()
    desc = str(ident.get("desc") or "").strip() or (front.get("desc") or "").strip()
    if front.get("name_source") == "pending":
        name = str(ident.get("name", "")).strip()
        name_zh = str(ident.get("name_zh", "")).strip()
        if not name:
            gen = gen_identity(desc, front.get("link", ""))
            if "error" not in gen:
                name, name_zh = gen["name"], gen["name_zh"]
                desc = desc or gen["desc"]
        if name and not name_zh:
            gen = gen_identity(desc, front.get("link", ""))
            if "error" not in gen and gen.get("name_zh"):
                name_zh = gen["name_zh"]
        if name:
            text = re.sub(r"^name: .*$", f"name: {name}", text, count=1, flags=re.M)
            text = re.sub(r"^name_zh: .*$", f"name_zh: {name_zh}", text, count=1, flags=re.M)
            text = re.sub(r"^name_source: .*$", "name_source: model", text, count=1, flags=re.M)
    if desc and desc != front.get("desc"):
        text = re.sub(r"^desc: .*$", f"desc: {desc}", text, count=1, flags=re.M)
    m = re.search(r"^name: (.*)$", text, re.M)
    if m and m.group(1).strip():
        text = re.sub(r"^# .*$", f"# {m.group(1).strip()}", text, count=1, flags=re.M)
    open(draft_path(slug), "w", encoding="utf-8").write(text)
    top = dn.collision(desc) if desc else []
    update_review(slug, {"identity": ident or None, "collision": top}, PACK)
    if os.path.exists(ip):
        os.remove(ip)
    return None


def run_engine(slug):
    """Background: engine writes body, lint gates it, status flips."""
    try:
        _run_engine(slug)
    finally:
        GEN_THREADS.pop(slug, None)


def _run_engine(slug):
    front, _ = parse_front(open(draft_path(slug), encoding="utf-8").read())
    idea = {"slug": slug, "name": front.get("name", slug), "name_zh": front.get("name_zh", ""),
            "desc": front.get("desc", ""), "link": front.get("link", "")}
    from drafts_engines import get_engine
    cfg = json.load(open(dn.ENGINES_CFG)) if os.path.exists(dn.ENGINES_CFG) else {}
    eng, _ = get_engine(front.get("engine") or cfg.get("engine"))
    model = front.get("model") or cfg.get("model")
    log_path = os.path.join(DRAFTS, slug + ".opencode.log")
    try:
        with GEN_LOCK:
            ok = eng.generate(idea, PROMPT, WORKDIR, log_path, model=model)
    except Exception as e:
        ok = False
        with open(log_path, "ab") as log:
            log.write(f"\n[api] engine exception: {e}\n".encode())
    if ok and dn.assemble(slug):
        if apply_identity(slug):
            return
        r = lint(draft_path(slug))
        extra = f"lint_errors: {len(r['errors'])}\nlint_warnings: {len(r['warnings'])}"
        dn.refresh_front(slug, "draft" if r["ok"] else "failed", extra=extra)
        if r["ok"]:
            try:
                translate_draft(slug)
            except Exception as e:
                with open(os.path.join(DRAFTS, slug + ".opencode.log"), "ab") as log:
                    log.write(f"\n[api] zh translate failed: {e}\n".encode())
    else:
        if os.path.exists(os.path.join(DRAFTS, slug + ".identity.json")) and apply_identity(slug):
            return
        dn.refresh_front(slug, "failed", extra="lint: engine failed, see .opencode.log")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print("[api]", fmt % args)

    def _json(self, obj, code=200):
        data = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/api/health":
            return self._json({"ok": True, "generating": sorted(GEN_THREADS), "promoting": sorted(PROMOTE_THREADS)})
        if path == "/api/drafts":
            return self._json(list_drafts())
        if path == "/api/sections":
            return self._json(list_sections())
        if path == "/api/review":
            return self._json(load_review(PACK))
        m = re.match(r"^/api/drafts/([\w-]+)$", path)
        if m:
            d = read_draft(m.group(1))
            return self._json(d) if d else self._json({"error": "not found"}, 404)
        self._json({"error": "no route"}, 404)

    def do_POST(self):
        path = unquote(urlparse(self.path).path)
        if path == "/api/drafts":
            b = self._body()
            res, code = self._create(b)
            return self._json(res, code)
        if path == "/api/dedupe":
            slug = self._body().get("slug", "")
            try:
                valid_slug(slug)
            except ValueError as error:
                return self._json({"error": str(error)}, 400)
            p = draft_path(slug)
            if not os.path.exists(p):
                return self._json({"error": "not found"}, 404)
            front, _ = parse_front(open(p, encoding="utf-8").read())
            if not (front.get("desc") or "").strip():
                return self._json(
                    {"error": "主张（desc）为空：等引擎调研定名后再查重"}, 409)
            if front.get("status") in ("promoting", "generating"):
                return self._json({"error": "等待当前任务结束后再查重"}, 409)
            before = fingerprint(slug, PACK)
            revision = corpus_revision(PACK)
            top = dn.collision(front["desc"])
            verdict = {}
            try:
                from dedupe_judge import judge
                verdict = judge(slug)
            except Exception as e:
                verdict = {"verdict": "error", "reason": str(e)}
            import datetime
            if before != fingerprint(slug, PACK) or revision != corpus_revision(PACK):
                return self._json({"error": "查重期间草稿或语料已更新，请重试"}, 409)
            update_review(slug, {"deduped_at": datetime.datetime.now().isoformat(),
                "top": top, **verdict, "draft_fingerprint": before, "corpus_revision": revision}, PACK)
            return self._json({"slug": slug, "top": top, "verdict": verdict})
        m = re.match(r"^/api/drafts/([\w-]+)/translate$", path)
        if m:
            slug = m.group(1)
            if not os.path.exists(draft_path(slug)):
                return self._json({"error": "not found"}, 404)
            th = threading.Thread(target=translate_draft, args=(slug,), daemon=True)
            th.start()
            return self._json({"slug": slug, "translating": True}, 202)
        if path == "/api/promote":
            b = self._body()
            slug, action = b.get("slug", ""), b.get("action", "")
            import promote_draft as pd
            try:
                front, _, _ = pd.validate_promotion(slug, action, b.get("section") if action == "new" else b.get("into"))
                if front.get("status") != "draft":
                    return self._json({"error": "该草稿已有入库任务正在运行"}, 409)
            except (ValueError, FileNotFoundError) as error:
                return self._json({"error": str(error)}, 409)
            if not PROMOTE_LOCK.acquire(blocking=False):
                return self._json({"error": "已有入库任务正在运行"}, 409)
            try:
                dn.refresh_front(slug, "promoting")
                PROMOTE_THREADS.add(slug)
                threading.Thread(target=run_promote, args=(slug, action, b), daemon=True).start()
            except Exception:
                PROMOTE_THREADS.discard(slug)
                PROMOTE_LOCK.release()
                raise
            return self._json({"slug": slug, "status": "promoting"}, 202)
        self._json({"error": "no route"}, 404)

    def _create(self, b):
        name = (b.get("name") or "").strip()
        name_zh = (b.get("name_zh") or "").strip()
        desc = (b.get("desc") or "").strip()
        link = (b.get("link") or "").strip()
        if not desc and not link:
            return {"error": "一句话想法和调研链接至少填一个"}, 400
        if name:
            slug = dn.slugify(b.get("slug") or name)
            name_source = "user"
        else:
            # 方案A：名字留空 -> 临时占位 slug，引擎调研后定名
            base = dn.slugify(desc or urlparse(link).netloc + urlparse(link).path) or "draft"
            slug = dn.unique_slug(("wip-" + base)[:48])
            name = "(调研后定名)"
            name_zh = ""
            name_source = "pending"
        taken = dn.slug_taken(slug)
        if taken:
            return {"error": f"slug「{slug}」已存在于{'草稿区' if taken == 'draft' else '正式语料'}"}, 409
        top = dn.collision(desc) if desc else []
        if top and top[0][1] >= dn.HIGH_SIM and not b.get("force"):
            return {"error": f"与语料相似度过高 ({top[0][1]:.3f})，如确认请勾选 force",
                    "collision": top}, 409
        idea = {"slug": slug, "name": name, "name_zh": name_zh,
                "desc": desc, "link": link, "name_source": name_source}
        dn.write_draft(slug, idea, "opencode", "human")
        th = threading.Thread(target=run_engine, args=(slug,), daemon=True)
        GEN_THREADS[slug] = th
        th.start()
        return {"slug": slug, "status": "generating", "collision": top}, 201

    def do_PUT(self):
        path = unquote(urlparse(self.path).path)
        m = re.match(r"^/api/drafts/([\w-]+)$", path)
        if m:
            slug = m.group(1)
            path = draft_path(slug)
            if not os.path.exists(path):
                return self._json({"error": "not found"}, 404)
            front, _ = parse_front(open(path, encoding="utf-8").read())
            if front.get("status") in ("promoting", "generating", "promoted"):
                return self._json({"error": "当前状态不允许编辑"}, 409)
            save_body(slug, self._body().get("body", ""))
            r = lint(path)
            status = "failed" if r["errors"] else "draft"
            dn.refresh_front(slug, status,
                             extra=f"lint_errors: {len(r['errors'])}\nlint_warnings: {len(r['warnings'])}")
            return self._json({"slug": slug, "lint": r, "status": status})
        self._json({"error": "no route"}, 404)

    def do_DELETE(self):
        path = unquote(urlparse(self.path).path)
        m = re.match(r"^/api/drafts/([\w-]+)$", path)
        if m:
            slug = m.group(1)
            path = draft_path(slug)
            if os.path.exists(path):
                front, _ = parse_front(open(path, encoding="utf-8").read())
                if front.get("status") in ("promoting", "generating"):
                    return self._json({"error": "任务执行期间不能删除草稿"}, 409)
            removed = []
            for suffix in (".md", ".research.md", ".zh.json", ".opencode.log",
                           ".identity.json", ".research.zh.md", ".body.md"):
                p = os.path.join(DRAFTS, slug + suffix)
                if os.path.exists(p):
                    os.remove(p)
                    removed.append(slug + suffix)
            return self._json({"removed": removed})
        self._json({"error": "no route"}, 404)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=5199)
    args = ap.parse_args()
    with corpus_lock(PACK):
        recover_publication(PACK)
        for item in list_drafts():
            if item["status"] == "promoting":
                dn.refresh_front(item["slug"], "draft")
                update_review(item["slug"], {"promote_error": "上次入库中断，请重新查重后重试"}, PACK)
    print(f"drafts API on :{args.port}  (drafts dir: {DRAFTS})")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
