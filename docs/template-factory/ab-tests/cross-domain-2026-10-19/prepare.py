"""Freeze a new exploratory three-case, three-handoff experiment before production."""

import hashlib
import json
from pathlib import Path
import random
import shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MODEL = "commandcode/deepseek/deepseek-v4.1-flash"

CASES = {
    "budget": {
        "leaf": "budgeting-application", "name": "个人月度预算与消费前剩余额度",
        "audience": "单个本地用户，不连接银行或支付服务",
        "objective": "按月为用途设置预算，记录和纠正实际支出，在消费前看到准确的计划、已花和剩余，并导出自己的记录。",
        "workflow": ["选择月份并建立分类及预算", "记录有日期、分类、金额和备注的支出", "核对分类及整月计划/实际/剩余，超支可见", "修改或删除误记支出并即时重算", "切换月份、重启后仍可回查", "导出当月支出 CSV"],
        "acceptance": ["仅本人本地数据；货币为人民币，两位小数，支出须为正数，不静默取整或裁剪输入", "每月预算及支出互相隔离；未使用分类仍可见，超支显示负剩余，不自动阻止记账", "修改/删除后汇总与列表一致，失败输入给出反馈且不破坏旧数据", "数据只存指定目录，正常重启保留；导出对应当前月份，中文、引号和换行可往返"],
    },
    "booking": {
        "leaf": "amenity-booking-platform", "name": "社区共享设施的预约与取消",
        "audience": "一个设施管理员和封闭名单内的两个居民",
        "objective": "管理员配置设施，居民登录后选择时段预约、查看自己的预约并取消；同一设施不能被重复占用，权限由服务端执行。",
        "workflow": ["通过本地演示账号登录", "管理员创建可预约设施", "居民查看设施及占用时段，提交开始与结束时间", "居民查看和取消自己的预约，管理员可管理全部", "取消保留状态记录并释放原时段", "刷新及真实重启后仍一致"],
        "acceptance": ["仅回环本地演示，不集成邮件、真实住户、支付或公网身份服务", "管理员与居民角色不可由请求参数伪造；居民不能创建设施、查看别人预约详情或取消别人的记录", "结束必须晚于开始；时段为有时区的 ISO8601，按真实时刻比较；半开区间相邻可预约、重叠不可预约", "并发竞争同一设施重叠时段最多成功一笔；不同设施不互相阻塞", "取消可重复提交但不能破坏历史或别人的数据；失败要说明原因，不伪报成功"],
    },
    "rename": {
        "leaf": "file-manager", "name": "下载目录的预览式批量重命名与撤销",
        "audience": "只整理一个明确指定本地目录的用户",
        "objective": "先预览单目录文件名的文字替换，再明确确认执行，并能撤销这次批量改名；保护原始内容和未选文件。",
        "workflow": ["列出指定目录的真实普通文件", "输入文字查找与替换，输出旧名到新名的计划", "预览不改动原文件，用户确认后执行计划", "查看执行回执和当前文件名", "撤销这次执行并核对文件名与内容恢复"],
        "acceptance": ["Python 标准库 CLI，默认不递归；不处理目录和符号链接，不接触指定根目录外的文件", "查找为非空字面文本，不是正则；新名字必须是单个文件名，不允许目录穿越", "冲突或目标已存在时拒绝整份计划，不覆盖、不静默跳过后说全部成功", "预览与执行间源文件内容被改动须拒绝过期计划；失败后旧数据不能丢失", "执行及撤销均须显式 --confirm，重复执行不得产生第二轮重命名；撤销遇新冲突也不能覆盖", "演示只使用测试创建的普通文件，不对用户真实下载目录运行"],
    },
}

WEB_RUNTIME = """Python3 standard library + SQLite, Chinese browser UI, no install/build/third-party/external assets. Start python3 app.py --port PORT --data-dir DIR, bind 127.0.0.1 only; all durable data in DIR. GET / serves a usable UI connected to the same real state as the JSON API. No fake test-only responses or hardcoded business fixtures. HTTP JSON APIs below are shared integration contracts given identically to every condition, not template-only test conventions. API validation failures must be non-2xx and JSON with an error explanation. UI must provide understandable feedback. Use a few focused modules, at most 12 application files. Developer cannot execute tests; report checks not_run. No external network, telemetry, arbitrary file access, subprocess or installation."""

CONTRACTS = {
    "budget": WEB_RUNTIME + """
JSON API:
GET /api/state?month=YYYY-MM -> {month,categories:[{id,name,budget,spent,remaining}],transactions:[{id,date,category_id,amount,note}],totals:{budget,spent,remaining}}. All monetary response values are decimal strings with two fractional digits (e.g. "0.10").
POST /api/categories {month,name,budget:"decimal"} -> {id}. Creates a category+budget in that month. Duplicate month/name is rejected, no hidden second category.
PUT /api/categories/{id} {budget:"decimal"} -> updated entry; cannot mutate another month accidentally.
POST /api/transactions {date:"YYYY-MM-DD",category_id,amount:"decimal",note} -> {id}; transaction date must match the category month.
PUT /api/transactions/{id} {date,category_id,amount,note} -> updated entry. DELETE /api/transactions/{id} removes that entry; errors preserve original data.
GET /api/export?month=YYYY-MM -> UTF-8 CSV with header date,category,amount,note and matching month rows. Accept standard CSV quoting; do not invent Excel-specific formula behavior as a core requirement.
Browser instrumentation shared to all conditions: data-testid=month,category-name,category-budget,category-save,expense-date,expense-category,expense-amount,expense-note,expense-save. These identify real usable controls; fill month then allow UI state to load; category-save creates category, expense-save records expense. Rest of UI may be designed freely. Category selector option values equal category_id.
""",
    "booking": WEB_RUNTIME + """
Add --init-demo flag ONLY for this local experiment: create initial demo users on a fresh database: admin / AtlasDemo-Admin-9!, alice / AtlasDemo-Alice-9!, bob / AtlasDemo-Bob-9!. Passwords are explicitly synthetic test data, not real credentials. Never reset accounts or records on restart. Use password hashes and server-owned login sessions, no role/owner trust in client payloads.
POST /api/login {username,password} -> {user:{id,username,role}}, sets session cookie. POST /api/logout ends session. GET /api/me -> current user or 401.
GET /api/resources -> {resources:[{id,name}]}. POST /api/resources {name} -> {id}, admin only.
GET /api/availability?resource_id=ID -> {slots:[{start,end}]}, only active reservations, do not expose others' personal details.
POST /api/bookings {resource_id,start,end,note} -> {id}; authenticated resident owner comes from session, not a supplied user_id. Overlap returns 409; invalid dates return 400; unauthorized action 401/403. Adjacent [start,end) intervals do not overlap. Do not restrict demonstration to current-date fixtures.
GET /api/bookings -> {bookings:[{id,resource_id,start,end,note,status,owner_id}]}, residents see own only, admin all. GET /api/bookings/{id} -> one booking; residents forbidden for others.
POST /api/bookings/{id}/cancel -> same booking status=cancelled; owner or admin, idempotent, do not physically delete. Date input with explicit timezone offsets is accepted and compared by instant.
Browser shared controls data-testid=login-username,login-password,login-submit,resource-name,resource-save,booking-resource,booking-start,booking-end,booking-note,booking-save,logout. Show relevant controls only after login/role. booking-start/end can be text ISO8601 fields to avoid browser timezone rewriting. Select option values equal resource_id. Use actual login and persist actual bookings.
""",
    "rename": """Python3 standard-library CLI; entry python3 app.py --root DIR COMMAND ... . No dependency installation, network, shell/subprocess or arbitrary filesystem access. At most 12 application files. Business data is synthetic files solely inside the explicitly assigned root, with optional durable state under DIR/.atlas-renamer/. Never run against app source, HOME, or real Downloads. No fake fixtures or hardcoded names.
Commands and stdout contract (JSON only on stdout; useful Chinese messages/help/errors may be on stderr). Operational failure must exit nonzero and report an error, no false success.
list -> {files:[{name,size}]} lists immediate ordinary files only, excludes internal .atlas-renamer, directories and symlinks.
preview --find TEXT --replace TEXT --plan PATH -> {status:"preview",operations:[{old,new}],plan:PATH}; saves a real immutable plan under DIR/.atlas-renamer/ (PATH must be inside that state directory), does not rename originals. JSON plan should contain enough original identity/content evidence to refuse stale execution; choose format and document it. Keep JSON text readable/multiline.
apply --plan PATH --confirm -> {status:"applied",operations:[{old,new}],receipt:PATH}; do not trust edited plan paths to escape root or overwrite files. Without --confirm reject. On conflict refuse whole batch before mutations. Receipt must support later-process undo. Reapplying same plan must not mutate again (explicit already-applied or nonzero refusal acceptable).
undo --receipt PATH --confirm -> {status:"undone"}; restore this batch only, preserve content. Without --confirm reject. If restore targets now conflict or changed data would be overwritten, refuse without destroying it. Plan/receipt paths must be within root's .atlas-renamer directory, and external symlink state must not permit writes outside the assigned root.
This CLI is one file-manager workflow, not a claim to implement an entire desktop file manager. No recursive operations, delete/trash, cloud or graphical UI is needed. Developer cannot execute; report all checks not_run.
""",
}


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}


def main():
    assert not (HERE / "protocol.json").exists(), "Do not overwrite frozen cases"
    mapping = {}
    rng = random.Random("atlas-cross-domain-2026-10-19")
    for key, info in CASES.items():
        root = HERE / "cases" / key
        root.mkdir(parents=True)
        scenario = {"id": "experiment-" + key, "revision": 1, "status": "experiment-authorized; not a catalog confirmation", **info}
        save(root / "request.json", scenario)
        (root / "REQUEST.md").write_text(
            f"# {info['name']}\n\n用户：{info['audience']}\n\n目标：{info['objective']}\n\n流程：\n"
            + "\n".join("- " + s for s in info["workflow"])
            + "\n\n已确定范围与规则：\n" + "\n".join("- " + s for s in info["acceptance"]) + "\n")
        (root / "CONTRACT.md").write_text(CONTRACTS[key])
        shutil.copyfile(ROOT / "application-atlas-production-pack/applications" / (info["leaf"] + ".md"), root / "leaf.md")
        choices = ["no_template", "full_upfront", "layered_on_demand"]
        rng.shuffle(choices)
        mapping[key] = dict(zip(["M1", "M2", "M3"], choices))
    save(HERE / "condition-map.json", mapping)
    save(HERE / "protocol.json", {
        "created_date": "2026-10-19", "model": MODEL, "reasoning_effort": "high",
        "kind": "exploratory 3 independent domains x 3 arms, one initial generation per cell; not statistical proof",
        "conditions": ["request only", "frozen cognitive package, all files upfront", "byte-identical cognitive package, phase-first then references on demand"],
        "same_controls": ["request, declared integration contract, runtime and tool permissions within each domain", "model and effort", "fresh standalone isolated app-only write session", "1800s infrastructure timeout", "one equal optional product-repair opportunity, initial and repaired outcomes separate", "one retry only for transport/protocol failure, never selecting a better working app by behavior", "no historical application source or hidden evaluation rubric given to authors"],
        "primary": "Independent outcome evaluation of real declared user behaviors; CLI failures remain delivery failures. API, browser, CLI, static and skipped evidence separate.",
        "format_analysis": "Compare full_upfront vs layered_on_demand within each case using identical package hashes. Measure observed reads, correctness, scope/decisions and actual visible usage. Reading instructions may not be followed; report actual access, no automatic token/speed benefit.",
        "evaluation_freeze": "Independent agent must freeze shared core/risk rubrics and test toolchain before templates are generated. Hidden risks tied to declared safety promises; optional unrequested maturity additions are observations, not core failures.",
        "data": "Only Atlas public leaf material, experiment-scoped scenarios, public primary research, synthetic accounts and disposable test files; no production data, secrets or unrelated projects.",
        "publication": False, "factory_database_modified": False,
        "case_input_sha256": {k: hashes(HERE / "cases" / k) for k in CASES},
        "source_of_scope": "User explicitly requested new categories, with/without-template experiments and independent agent evaluation; experiment selection does not confirm catalog drafts.",
    })
    print("Frozen three case requests, common contracts and condition mapping; no provider call yet")


if __name__ == "__main__":
    main()
